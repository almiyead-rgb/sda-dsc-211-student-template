"""Explain final-project omissions without assigning a grade.

The simplified learner workflow requires five executed notebooks, key generated
outputs, one short README answer per day and the integrated Day 5 project. It does
not require a presentation or manually completed report templates.
"""
import argparse
from pathlib import Path
import json
import re
import numpy as np
import pandas as pd
from submission_contract import (
    REQUIRED, DAILY_REQUIRED, NOTEBOOKS, MANIFEST,
    json_read, inventory, inventory_digest, check_manifest, digest,
)
from day5_delivery import validate_submission as validate_prediction_file, replay_submission
from day3_decision import CostPolicy
from data_checks import validate_frame

EXPECTED_CONTRACT_SHA = '3b2d60c52452cb1cc43ea105992211746e5da44cdb2e5ed73b04bbce52dd5d21'
READY = 'READY FOR FINAL SUBMISSION | جاهز للتسليم النهائي'

DAILY_ANSWER_LABELS = {
    1: ('Day 1', 'اليوم الأول'),
    2: ('Day 2', 'اليوم الثاني'),
    3: ('Day 3', 'اليوم الثالث'),
    4: ('Day 4', 'اليوم الرابع'),
    5: ('Day 5', 'اليوم الخامس'),
}


def validate(root, smoke_report=None, template=False):
    root = Path(root).resolve()
    rows = []

    def check(name, location, fix, operation):
        try:
            operation()
        except (OSError, ValueError, KeyError, TypeError, AssertionError, json.JSONDecodeError) as error:
            rows.append({
                'check': name,
                'status': 'FAIL',
                'file': location,
                'how_to_fix': fix,
                'detail': str(error)[:350],
            })
        else:
            rows.append({
                'check': name,
                'status': 'PASS',
                'file': location,
                'how_to_fix': '',
                'detail': '',
            })

    def require(condition, message):
        if not condition:
            raise ValueError(message)

    check(
        'safe_files', '.',
        'أزل الملفات الخاصة والروابط الرمزية والملفات غير المدعومة.',
        lambda: inventory(root),
    )

    def data_check():
        require(
            digest(root / 'data/data_contract.json') == EXPECTED_CONTRACT_SHA,
            'Use the released data contract unchanged.',
        )
        contract = json_read(root / 'data/data_contract.json')
        for kind in ['train', 'challenge']:
            validate_frame(pd.read_csv(root / f'data/tamweel_{kind}.csv'), contract, kind)
        manifest = json_read(root / 'data/data_manifest.json')
        for name in ['data/tamweel_train.csv', 'data/tamweel_challenge.csv']:
            require(
                digest(root / name) == manifest['files'][name]['sha256'],
                f'Data checksum mismatch: {name}',
            )

    check('data_contract', 'data/', 'استعد بيانات الدورة وعقدها من المستودع الرسمي.', data_check)

    if template:
        for name in NOTEBOOKS:
            def notebook_structure(name=name):
                item = json_read(root / f'notebooks/{name}.ipynb')
                require(
                    item.get('nbformat') == 4
                    and any(cell['cell_type'] == 'code' for cell in item['cells']),
                    'Invalid notebook.',
                )
            check(
                'notebook_structure', f'notebooks/{name}.ipynb',
                'استعد دفتر التطبيق من المستودع الرسمي.',
                notebook_structure,
            )
        healthy = all(row['status'] == 'PASS' for row in rows)
        return {
            'status': 'STARTER_TEMPLATE_HEALTHY' if healthy else 'CHECKS_FAILED',
            'ready_for_submission': False,
            'automatic_grade': None,
            'checks': rows,
            'meaning': 'فحص القالب فقط؛ لا يدل على اكتمال مشروع متدرب.',
        }

    for name in REQUIRED:
        check(
            'required_file', name,
            'أضف الملف الفعلي إلى المسار المحدد؛ لا يكفي ZIP أو صورة شاشة.',
            lambda name=name: require(
                (root / name).is_file() and (root / name).stat().st_size > 0,
                'Missing or empty file.',
            ),
        )

    def find_daily_file(day, name):
        candidates = [
            root / 'artifacts' / name,
            root / 'evidence' / f'day{day}' / name,
        ]
        existing = [path for path in candidates if path.is_file() and path.stat().st_size > 0]
        require(existing, f'Missing daily output: {name}')
        return existing[0]

    for day in range(1, 5):
        for name in DAILY_REQUIRED[day]:
            check(
                'daily_output', f'Day {day}: {name}',
                'نزّل ملف النتيجة من Colab وارفعه إلى artifacts/ أو evidence/dayN/.',
                lambda day=day, name=name: find_daily_file(day, name),
            )

    def daily_answers():
        readme = (root / 'README.md').read_text(encoding='utf-8-sig')
        require(
            'Daily answers' in readme or 'الإجابات اليومية' in readme,
            'Add the Daily answers | الإجابات اليومية section to README.',
        )
        for day, labels in DAILY_ANSWER_LABELS.items():
            matching_label = next((label for label in labels if label in readme), None)
            require(matching_label is not None, f'Missing Day {day} answer heading.')
            pattern = re.compile(
                rf'(?:{re.escape(labels[0])}|{re.escape(labels[1])}).{{0,120}}\n(?P<answer>.+?)(?=\n#{1,4}\s|\Z)',
                re.IGNORECASE | re.DOTALL,
            )
            match = pattern.search(readme)
            require(match is not None, f'Missing Day {day} answer text.')
            answer = re.sub(r'[`#>*_\-]', ' ', match.group('answer')).strip()
            require(len(answer) >= 15, f'Day {day} answer is too short.')
    check(
        'daily_answers', 'README.md',
        'أضف إجابة قصيرة واضحة لكل يوم تحت Daily answers | الإجابات اليومية.',
        daily_answers,
    )

    def live_run(path):
        record = json_read(path)
        require(record.get('technical_status') == 'TECHNICAL_READY', 'Technical run is incomplete.')
        config = record.get('effective_config', record.get('config', {}))
        require(
            isinstance(config.get('seed'), int) and not isinstance(config.get('seed'), bool),
            'Record an integer seed in the effective run configuration.',
        )
        rendered = json.dumps(record)
        require(
            not any(word in rendered for word in ['EDUCATIONAL_EXAMPLE', 'EXAMPLE_ONLY', 'PRECOMPUTED']),
            'Recovery/example evidence is not accepted as final execution.',
        )

    for day in range(1, 6):
        def check_day_run(day=day):
            candidates = [
                root / 'artifacts' / f'day{day}_run.json',
                root / 'evidence' / f'day{day}' / f'day{day}_run.json',
            ]
            path = next((item for item in candidates if item.is_file()), None)
            require(path is not None, f'Missing day{day}_run.json')
            live_run(path)
        check(
            'live_execution', f'Day {day} run record',
            'شغّل Notebook اليوم على FAST_MODE الفعلي ثم ارفع ملف dayN_run.json.',
            check_day_run,
        )

    for name in NOTEBOOKS[1:]:
        def executed(name=name):
            notebook = json_read(root / f'notebooks/{name}.ipynb')
            cells = [
                cell for cell in notebook['cells']
                if cell['cell_type'] == 'code' and ''.join(cell['source']).strip()
            ]
            require(cells, 'Notebook contains no code.')
            require(
                all(isinstance(cell.get('execution_count'), int) and cell['execution_count'] > 0 for cell in cells),
                'Save the executed notebook with outputs.',
            )
            require(
                not any(output['output_type'] == 'error' for cell in cells for output in cell.get('outputs', [])),
                'An error output remains.',
            )
        check(
            'executed_notebook', f'notebooks/{name}.ipynb',
            'نفّذ Run all ثم نزّل وارفع Notebook بالمخرجات دون أخطاء حمراء.',
            executed,
        )

    for name in ['reports/MODEL_CARD.md', 'reports/ENSEMBLE_DECISION.md']:
        def generated_report(name=name):
            text = (root / name).read_text(encoding='utf-8-sig')
            require(len(text.strip()) >= 100, 'Generated report is empty or incomplete.')
        check(
            'generated_report', name,
            'أعد تشغيل اليوم الخامس ليولد التقرير تلقائيًا.',
            generated_report,
        )

    def final_predictions():
        policy = json_read(root / 'artifacts/final_policy.json')
        require(
            policy['cost_policy'] == {
                'false_negative_cost': 10.0,
                'false_positive_cost': 1.0,
                'max_flag_fraction': .12,
            },
            'Use the announced educational policy.',
        )
        contract = json_read(root / 'data/data_contract.json')
        model = json_read(root / 'artifacts/final_model/model.json')
        require(
            model['contract'] == contract
            and model['features'] == [feature['name'] for feature in contract['features']],
            'Model predictors differ from the approved features.',
        )
        submitted = pd.read_csv(root / 'submission/submission.csv', float_precision='round_trip')
        challenge = pd.read_csv(root / 'data/tamweel_challenge.csv')
        validate_prediction_file(
            submitted,
            challenge,
            policy['calibrated_threshold'],
            CostPolicy(**policy['cost_policy']),
        )
        replayed = replay_submission(root).set_index('application_id').loc[submitted.application_id]
        require(
            np.allclose(replayed.probability, submitted.probability, rtol=0, atol=1e-9)
            and np.array_equal(replayed.decision, submitted.decision),
            'Submission differs from the saved model and full-batch policy.',
        )
        require(len(submitted) == 2500, 'Final submission must contain 2,500 rows.')
    check(
        'predictions_and_policy', 'submission/submission.csv',
        'أعد التصدير من النموذج والسياسة المجمدين؛ لا تعدّل CSV يدويًا.',
        final_predictions,
    )

    check(
        'final_manifest', MANIFEST,
        'أعد بناء manifest بعد آخر تعديل ثم أعد الفحص.',
        lambda: check_manifest(root),
    )

    def clean_execution():
        require(smoke_report is not None, 'Fresh execution report required.')
        proof = json_read(smoke_report)
        require(
            proof.get('status') == 'PASS'
            and proof.get('assessment_mode') is True
            and proof.get('strict_learner_mode') is True,
            'Fresh execution did not pass in assessment mode.',
        )
        require(
            proof.get('content_sha256') == inventory_digest(inventory(root)),
            'Fresh execution report belongs to different project bytes.',
        )
        expected = [f'notebooks/{name}.ipynb' for name in NOTEBOOKS]
        require(
            [item['notebook'] for item in proof['notebooks']] == expected,
            'Clean run must cover readiness and all five labs.',
        )
        require(
            all(item['status'] == 'PASS' and item.get('technical_complete', True) for item in proof['notebooks']),
            'One or more notebooks failed technical execution.',
        )
    check(
        'fresh_execution', 'notebooks/',
        'شغّل Notebook 99 أو Final Project Check على الملفات النهائية نفسها.',
        clean_execution,
    )

    passed = all(row['status'] == 'PASS' for row in rows)
    return {
        'status': READY if passed else 'NEEDS_WORK | يحتاج استكمالًا',
        'ready_for_submission': passed,
        'automatic_grade': None,
        'checks': rows,
        'meaning': (
            'Mechanical readiness only. The instructor grades the project once '
            'using technical evidence, daily answers and authorship review.'
        ),
    }


def write_report(result, output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    (output / 'self_check_report.json').write_text(
        json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False),
        encoding='utf-8',
    )
    lines = [
        f"# {result['status']}", '', result['meaning'], '',
        '| Check | Status | File | How to fix |', '|---|---|---|---|',
    ]
    lines += [
        f"| {row['check']} | {row['status']} | {row['file']} | {row['how_to_fix']} |"
        for row in result['checks']
    ]
    (output / 'self_check_report.md').write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--smoke-report', type=Path)
    parser.add_argument('--output', type=Path, default=Path('.check-output'))
    parser.add_argument('--template', action='store_true')
    args = parser.parse_args()
    result = validate(args.root, args.smoke_report, args.template)
    write_report(result, args.output)
    print(result['status'])
    for row in result['checks']:
        if row['status'] == 'FAIL':
            print(f"FAIL | {row['file']} | {row['how_to_fix']} | {row['detail']}")
    raise SystemExit(
        0 if result['ready_for_submission'] or result['status'] == 'STARTER_TEMPLATE_HEALTHY' else 1
    )
