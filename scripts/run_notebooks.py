"""Execute every lab in a fresh kernel and workspace.

The runner verifies technical execution only. Daily learner answers are checked in
README by the final submission validator; they no longer block notebook execution.
"""
import argparse
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile
import time
import nbformat
from nbclient import NotebookClient
from submission_contract import NOTEBOOKS, inventory, inventory_digest, json_read, digest


def worker(source, output, strict):
    source, output = Path(source), Path(output)
    with tempfile.TemporaryDirectory(prefix='tamweel-lab-') as folder:
        work = Path(folder)
        notebook = nbformat.read(source, as_version=4)
        adapted = 0
        for cell in notebook.cells:
            if cell.cell_type != 'code':
                continue
            lines = cell.source.splitlines()
            for index, line in enumerate(lines):
                if line.startswith('ROOT = ') and 'TAMWEEL_PROJECT_DIR' in line:
                    lines[index] = 'ROOT = Path(os.environ["TAMWEEL_PROJECT_DIR"]).resolve()'
                    adapted += 1
            cell.source = '\n'.join(lines)
        if adapted != 1:
            raise ValueError('Expected exactly one documented workspace setting in the notebook.')

        os.environ.update(
            ASSESSMENT_MODE='1',
            TAMWEEL_PROJECT_DIR=str(work),
            OMP_NUM_THREADS='2',
            OPENBLAS_NUM_THREADS='2',
            PYTHONDONTWRITEBYTECODE='1',
        )
        started = time.perf_counter()
        NotebookClient(
            notebook,
            timeout=180,
            kernel_name='python3',
            resources={'metadata': {'path': str(work)}},
        ).execute()

        technical_complete = True
        technical_status = 'READINESS_COMPLETE'
        if source.name[:2] != '00':
            day = int(source.name[:2])
            run_record = json_read(work / f'artifacts/day{day}_run.json')
            technical_status = run_record.get('technical_status')
            technical_complete = technical_status == 'TECHNICAL_READY'
            if not technical_complete:
                raise ValueError('Live technical computation is incomplete; recovery output is not final evidence.')

        result = {
            'status': 'PASS' if technical_complete else 'FAIL',
            'technical_complete': technical_complete,
            'learner_complete': technical_complete,
            'technical_status': technical_status,
            'seconds': round(time.perf_counter() - started, 2),
            'source_sha256': digest(source),
            'workspace_adapter': 'Only ROOT redirected to a fresh temporary workspace.',
            'code_cells': sum(cell.cell_type == 'code' for cell in notebook.cells),
            'answer_scope': 'Daily answers are reviewed from README, not required for code execution.',
        }
        output.write_text(json.dumps(result, indent=2), encoding='utf-8')


def run(root, output, strict=False):
    root, output = Path(root).resolve(), Path(output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    before = inventory_digest(inventory(root))
    results = []

    for name in NOTEBOOKS:
        notebook_path = f'notebooks/{name}.ipynb'
        result_path = output / f'{name}.json'
        command = [
            sys.executable,
            str(Path(__file__).resolve()),
            '--worker', str(root / notebook_path),
            '--output', str(result_path),
        ]
        if strict:
            command.append('--strict')
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding='utf-8',
                errors='replace',
                timeout=360,
                env={**os.environ, 'PYTHONIOENCODING': 'utf-8'},
            )
        except subprocess.TimeoutExpired:
            result = {
                'status': 'FAIL',
                'technical_complete': False,
                'learner_complete': False,
                'detail': 'Notebook exceeded the six-minute limit.',
            }
        else:
            (output / f'{name}.log').write_text(
                completed.stdout + '\n' + completed.stderr,
                encoding='utf-8',
            )
            if completed.returncode == 0 and result_path.exists():
                result = json_read(result_path)
            else:
                result = {
                    'status': 'FAIL',
                    'technical_complete': False,
                    'learner_complete': False,
                    'detail': 'See notebook log.',
                }
        results.append({'notebook': notebook_path, **result})
        print(f"{notebook_path}: {result['status']} ({time.perf_counter() - started:.1f}s)", flush=True)

    unchanged = before == inventory_digest(inventory(root))
    report = {
        'status': 'PASS' if unchanged and all(item['status'] == 'PASS' for item in results) else 'FAIL',
        'assessment_mode': True,
        'strict_learner_mode': strict,
        'content_sha256': before,
        'source_files_unchanged': unchanged,
        'notebooks': results,
        'scope': (
            'Fresh kernels and workspaces, one notebook at a time. '
            'Daily README answers and grading remain separate.'
        ),
    }
    (output / 'notebook_run.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--strict', action='store_true')
    parser.add_argument('--worker', type=Path)
    args = parser.parse_args()
    if args.worker:
        worker(args.worker, args.output, args.strict)
    else:
        raise SystemExit(0 if run(args.root, args.output, args.strict)['status'] == 'PASS' else 1)
