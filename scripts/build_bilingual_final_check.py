"""Convert Notebook 99 learner markdown to paired bilingual cells without changing code."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

CONTENT_VERSION = "1.1.0"
REQUIRED_ORDER = "en-left-ar-right"
DEFAULT_NOTEBOOK = Path("notebooks/99_final_submission_check.ipynb")
DEFAULT_CONTRACT = Path("content/notebook99_code_contract.json")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected an object in {path}")
    return value


def source_text(cell: dict[str, Any]) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    if isinstance(source, str):
        return source
    raise ValueError("Notebook cell source must be a string or list of strings.")


def code_hashes(notebook: dict[str, Any]) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        cell_id = cell.get("id")
        if not isinstance(cell_id, str) or not cell_id:
            raise ValueError("Every executable cell must have a stable id.")
        hashes[cell_id] = hashlib.sha256(source_text(cell).encode("utf-8")).hexdigest()
    return hashes


def contract_hashes(contract: dict[str, Any]) -> dict[str, str]:
    return {item["id"]: item["sha256"] for item in contract.get("code_cells", [])}


def verify_code(actual: dict[str, str], expected: dict[str, str], stage: str) -> None:
    missing = sorted(set(expected) - set(actual))
    unexpected = sorted(set(actual) - set(expected))
    changed = sorted(
        cell_id
        for cell_id in set(expected) & set(actual)
        if expected[cell_id] != actual[cell_id]
    )
    if missing or unexpected or changed:
        raise RuntimeError(
            f"Executable-cell contract failed during {stage}: "
            f"missing={missing}, unexpected={unexpected}, changed={changed}"
        )


def as_lines(text: str) -> list[str]:
    stripped = text.strip()
    if not stripped:
        return []
    values = stripped.splitlines()
    return [value + "\n" for value in values[:-1]] + [values[-1]]


def paired_cell(
    pair_id: str,
    en_title: str,
    en_body: str,
    ar_title: str,
    ar_body: str,
) -> dict[str, Any]:
    html = f"""
<table style="width:100%; border-collapse:collapse;">
<tr>
<td width="50%" valign="top" dir="ltr" style="padding:14px; border:1px solid #d0d7de;">
<h2>{en_title}</h2>
{en_body.strip()}
</td>
<td width="50%" valign="top" dir="rtl" style="padding:14px; border:1px solid #d0d7de;">
<h2>{ar_title}</h2>
{ar_body.strip()}
</td>
</tr>
</table>
"""
    return {
        "cell_type": "markdown",
        "id": pair_id.replace("_", "-"),
        "metadata": {
            "bilingual_pair_id": pair_id,
            "bilingual_order": REQUIRED_ORDER,
            "learner_facing": True,
            "content_version": CONTENT_VERSION,
        },
        "source": as_lines(html),
    }


SECTIONS: dict[str, dict[str, str]] = {'final_check_header': {'pair_id': 'final_check_header',
                        'en_title': 'Notebook 99 · Final project self-check',
                        'ar_title': 'دفتر 99 · الفحص الذاتي النهائي',
                        'en_body': '<p><strong>SDA-DSC-211 · Tamweel Lite · Meaad '
                                   'Al-Marri</strong></p><p>Check your own project against '
                                   'the published requirements. This is a read-only '
                                   'self-check, not a grade or submission receipt.</p>',
                        'ar_body': '<p><strong>SDA-DSC-211 · تمويل لايت · ميعاد '
                                   'المري</strong></p><p>راجع مشروعك وفق المتطلبات المنشورة. '
                                   'الفحص ذاتي وللقراءة فقط؛ لا يمنح درجة ولا يرسل '
                                   'التسليم.</p>'},
 'final_check_source': {'pair_id': 'final_check_source',
                        'en_title': '1. Choose the complete project',
                        'ar_title': '١. اختر المشروع الكامل',
                        'en_body': '<p>Use the public GitHub repository link, or one ZIP of '
                                   'the entire project. Do not upload the Day 5 ZIP alone. '
                                   'The GitHub option reads the latest default branch '
                                   'snapshot when you run it.</p>',
                        'ar_body': '<p>استخدم رابط مستودع GitHub العام، أو ZIP واحدًا يشمل '
                                   'المشروع بالكامل، لا حزمة اليوم الخامس وحدها. يقرأ خيار '
                                   'GitHub أحدث نسخة من الفرع الافتراضي وقت الفحص.</p>'},
 'final_check_tools': {'pair_id': 'final_check_tools',
                       'en_title': '2. Prepare the checker',
                       'ar_title': '٢. جهّز الفاحص',
                       'en_body': '<p>Run the next cell once. No packages, passwords, tokens '
                                  'or Drive connection are needed. The checker does not '
                                  'execute student code.</p>',
                       'ar_body': '<p>شغّل الخلية التالية مرة واحدة. لا تحتاج إلى تثبيت '
                                  'مكتبات أو إدخال مفتاح أو ربط Drive. الفاحص لا يشغّل شيفرة '
                                  'الطالب.</p>'},
 'final_check_snapshot': {'pair_id': 'final_check_snapshot',
                          'en_title': '3. Inspect the snapshot',
                          'ar_title': '٣. افحص نسخة المشروع',
                          'en_body': '<p>Paste the repository link in '
                                     '<code>PROJECT_URL</code>, or leave both fields blank '
                                     'and upload a complete ZIP. The checker reads notebooks '
                                     '01–05, the five README answers, key daily and Day 5 '
                                     'outputs, predictions and obvious credential '
                                     'warnings.</p>',
                          'ar_body': '<p>ضع الرابط في <code>PROJECT_URL</code>، أو اترك '
                                     'الحقلين فارغين وارفع ZIP كاملًا. يراجع الفاحص الدفاتر '
                                     '01–05، وإجابات README الخمس، والمخرجات اليومية '
                                     'والنهائية، والتنبؤات، والمؤشرات الظاهرة على وجود مفاتيح '
                                     'وصول.</p>'},
 'final_check_run': {'pair_id': 'final_check_run',
                     'en_title': '4. Read the findings',
                     'ar_title': '٤. اقرأ الملاحظات',
                     'en_body': '<p><strong>FIX:</strong> correct the specified item. '
                                '<strong>REVIEW:</strong> inspect it manually. The checker '
                                'cannot judge the quality of an answer, verify attendance or '
                                'certify model performance.</p>',
                     'ar_body': '<p><strong>FIX:</strong> صحح البند المحدد. '
                                '<strong>REVIEW:</strong> راجعه يدويًا. الفاحص لا يحكم على '
                                'جودة الإجابة، ولا يتحقق من الحضور، ولا يثبت أداء '
                                'النموذج.</p>'},
 'final_check_save': {'pair_id': 'final_check_save',
                      'en_title': '5. Save and submit separately',
                      'ar_title': '٥. احفظ التقرير وسلّم بشكل مستقل',
                      'en_body': '<p>Download the JSON report from Colab Files if needed. '
                                 'After any project change, rerun this self-check. The <a '
                                 'href="https://github.com/almiyead-rgb/sda-dsc-211-student-template/blob/main/SUBMISSION_GUIDE.md">submission '
                                 'guide</a> explains the remaining steps. No presentation or '
                                 'submission tag is required.</p>',
                      'ar_body': '<p>نزّل تقرير JSON من لوحة Files عند الحاجة، وأعد الفحص بعد '
                                 'أي تعديل. اتبع <a '
                                 'href="https://github.com/almiyead-rgb/sda-dsc-211-student-template/blob/main/SUBMISSION_GUIDE.md">دليل '
                                 'التسليم</a> لإكمال الخطوات وإرسال رابطك عبر القناة الخاصة. '
                                 'لا يلزم عرض تقديمي أو وسم تسليم.</p>'}}

PAIR_TO_SECTION = {value["pair_id"]: value for value in SECTIONS.values()}


def build_notebook(notebook: dict[str, Any], contract: dict[str, Any]) -> dict[str, Any]:
    expected_code = contract_hashes(contract)
    verify_code(code_hashes(notebook), expected_code, "before bilingual conversion")
    seen_pairs: set[str] = set()
    cells: list[dict[str, Any]] = []

    for cell in notebook.get("cells", []):
        if cell.get("cell_type") != "markdown":
            cells.append(cell)
            continue
        cell_id = cell.get("id")
        metadata = cell.get("metadata", {})
        pair_id = metadata.get("bilingual_pair_id") if isinstance(metadata, dict) else None
        if cell_id in SECTIONS:
            section = SECTIONS[cell_id]
        elif pair_id in PAIR_TO_SECTION:
            section = PAIR_TO_SECTION[str(pair_id)]
        else:
            raise RuntimeError(f"Unexpected Notebook 99 markdown cell: id={cell_id!r}, pair={pair_id!r}")
        if section["pair_id"] in seen_pairs:
            raise RuntimeError(f"Duplicate bilingual pair {section['pair_id']}")
        seen_pairs.add(section["pair_id"])
        cells.append(
            paired_cell(
                section["pair_id"],
                section["en_title"],
                section["en_body"],
                section["ar_title"],
                section["ar_body"],
            )
        )

    expected_pairs = set(PAIR_TO_SECTION)
    if seen_pairs != expected_pairs:
        raise RuntimeError(
            f"Notebook 99 markdown coverage mismatch: "
            f"missing={sorted(expected_pairs - seen_pairs)}, "
            f"unexpected={sorted(seen_pairs - expected_pairs)}"
        )
    notebook["cells"] = cells
    notebook.setdefault("metadata", {})["bilingual_content_version"] = CONTENT_VERSION
    notebook["metadata"]["bilingual_order"] = REQUIRED_ORDER
    verify_code(code_hashes(notebook), expected_code, "after bilingual conversion")
    return notebook


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notebook", type=Path, default=DEFAULT_NOTEBOOK)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument(
        "--output-report",
        type=Path,
        default=Path("check-output/notebook99-bilingual-build.json"),
    )
    args = parser.parse_args()
    notebook = load_json(args.notebook)
    contract = load_json(args.contract)
    before = code_hashes(notebook)
    converted = build_notebook(notebook, contract)
    after = code_hashes(converted)
    args.notebook.write_text(
        json.dumps(converted, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    report = {
        "status": "PASS",
        "notebook": str(args.notebook),
        "content_version": CONTENT_VERSION,
        "bilingual_order": REQUIRED_ORDER,
        "paired_sections": len(SECTIONS),
        "executable_cells": len(before),
        "code_preserved": before == after == contract_hashes(contract),
        "pair_ids": [value["pair_id"] for value in SECTIONS.values()],
        "execution_scope": "Structural conversion only; live final check requires a learner project snapshot and Colab download/upload interactions.",
    }
    args.output_report.parent.mkdir(parents=True, exist_ok=True)
    args.output_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
