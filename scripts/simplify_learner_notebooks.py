"""Align learner-facing notebook Markdown with the one-question daily workflow.

Executable cells are preserved byte-for-byte. The script removes old multi-response
instructions from Markdown, adds one official instruction near the top, and adds
one required question at the end of each Day 1–5 notebook.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DAYS = {
    1: {
        "path": "notebooks/01_baseline_boosting.ipynb",
        "title_en": "Model comparison",
        "title_ar": "مقارنة النماذج",
        "question_en": "Which model did you select initially, and what is the strongest result supporting your choice?",
        "question_ar": "أي نموذج اخترت مبدئيًا، وما الدليل الأقوى من نتائجك؟",
    },
    2: {
        "path": "notebooks/02_validation_tuning.ipynb",
        "title_en": "Honest validation",
        "title_ar": "التحقق الصادق",
        "question_en": "What leakage risk did you identify, and how did the validation design prevent it?",
        "question_ar": "ما خطر التسرب الذي اكتشفته، وكيف منعه تصميم التحقق؟",
    },
    3: {
        "path": "notebooks/03_cost_sensitive_decision.ipynb",
        "title_en": "Decision threshold",
        "title_ar": "عتبة القرار",
        "question_en": "Why is a fixed threshold of 0.5 not always suitable for this review policy?",
        "question_ar": "لماذا لا تكون العتبة الثابتة 0.5 مناسبة دائمًا لسياسة المراجعة؟",
    },
    4: {
        "path": "notebooks/04_explain_calibrate.ipynb",
        "title_en": "Interpretation and calibration",
        "title_ar": "التفسير والمعايرة",
        "question_en": "Which feature was most important in your explanation, and why does that not prove causality?",
        "question_ar": "ما أهم خاصية في تفسيرك، ولماذا لا يثبت ذلك السببية؟",
    },
    5: {
        "path": "notebooks/05_final_model.ipynb",
        "title_en": "Final model",
        "title_ar": "النموذج النهائي",
        "question_en": "Why did you choose the single model or the ensemble for the final project?",
        "question_ar": "لماذا اخترت النموذج الفردي أو التجميع في المشروع النهائي؟",
    },
}

PROMPT_SIGNALS = (
    "learner checkpoint",
    "learner-owned",
    "own the decision",
    "your decision",
    "your responses",
    "exit answers",
    "write your argument",
    "complete the responses",
    "نقطة تعلم",
    "إجابات المتدرب",
    "امتلك قرارك",
    "اكتب قرارك",
    "أكمل الإجابات",
    "أسئلة الخروج",
)

REPLACEMENTS = {
    "your written decision": "one short daily answer in README",
    "قرارك المكتوب": "إجابة يومية قصيرة في README",
    "five-slide PDF presentation": "final GitHub repository",
    "عرضًا من خمس شرائح بصيغة PDF": "مستودع GitHub النهائي",
    "final presentation": "final project",
    "العرض النهائي": "المشروع النهائي",
}


def paired_box(en_heading: str, en_body: str, ar_heading: str, ar_body: str) -> list[str]:
    html = f'''<table style="width:100%; border-collapse:collapse;">
<tr>
<td width="50%" valign="top" dir="ltr" style="padding:14px; border:1px solid #d0d7de;">
<h2>{en_heading}</h2>
<p>{en_body}</p>
</td>
<td width="50%" valign="top" dir="rtl" style="padding:14px; border:1px solid #d0d7de;">
<h2>{ar_heading}</h2>
<p>{ar_body}</p>
</td>
</tr>
</table>'''
    return [line + "\n" for line in html.splitlines()[:-1]] + [html.splitlines()[-1]]


def official_instruction(day: int) -> dict:
    return {
        "cell_type": "markdown",
        "id": f"day{day}-official-daily-task",
        "metadata": {
            "bilingual_pair_id": f"day{day}_official_daily_task",
            "bilingual_order": "en-left-ar-right",
            "learner_facing": True,
            "content_version": "1.2.0",
            "daily_requirement": True,
        },
        "source": paired_box(
            "Official daily requirement",
            "Run all cells, compare the generated files with EXPECTED_RESULTS.md, then answer only the single question at the end of this notebook in your repository README. Additional legacy reflection variables inside code cells are compatibility fields; leave them unchanged.",
            "المطلوب اليومي المعتمد",
            "شغّل جميع الخلايا، وقارن الملفات الناتجة بصفحة EXPECTED_RESULTS.md، ثم أجب فقط عن السؤال الواحد في نهاية هذا الدفتر داخل README في مستودعك. حقول الانعكاس القديمة داخل خلايا الكود مخصصة للتوافق؛ اتركها دون تعديل.",
        ),
    }


def neutral_checkpoint(day: int, index: int, metadata: dict, cell_id: str) -> dict:
    clean_metadata = dict(metadata)
    clean_metadata.update(
        bilingual_pair_id=clean_metadata.get("bilingual_pair_id", f"day{day}_evidence_review_{index}"),
        bilingual_order="en-left-ar-right",
        learner_facing=True,
        content_version="1.2.0",
    )
    return {
        "cell_type": "markdown",
        "id": cell_id,
        "metadata": clean_metadata,
        "source": paired_box(
            "Review the evidence",
            "Read the output produced by the previous code cell and keep the generated files. No answer is required in this cell; the only required answer appears at the end of the notebook.",
            "راجع الأدلة",
            "اقرأ المخرجات التي أنشأتها خلية الكود السابقة واحتفظ بالملفات الناتجة. لا تكتب إجابة في هذه الخلية؛ الإجابة الوحيدة المطلوبة موجودة في نهاية الدفتر.",
        ),
    }


def final_question(day: int, item: dict) -> dict:
    return {
        "cell_type": "markdown",
        "id": f"day{day}-single-daily-question",
        "metadata": {
            "bilingual_pair_id": f"day{day}_single_daily_question",
            "bilingual_order": "en-left-ar-right",
            "learner_facing": True,
            "content_version": "1.2.0",
            "daily_question": True,
        },
        "source": paired_box(
            f"Daily question · {item['title_en']}",
            f"<strong>{item['question_en']}</strong><br><br>Write a short answer under <code>Day {day}</code> in the <code>Daily answers | الإجابات اليومية</code> section of your repository README. Then download this executed notebook and the required generated files and upload them on the same day.",
            f"سؤال اليوم · {item['title_ar']}",
            f"<strong>{item['question_ar']}</strong><br><br>اكتب إجابة مختصرة تحت <code>Day {day} | اليوم {day}</code> في قسم <code>Daily answers | الإجابات اليومية</code> داخل README في مستودعك، ثم نزّل هذا الدفتر بعد التنفيذ وملفات النتائج المطلوبة وارفعها في اليوم نفسه.",
        ),
    }


def simplify(day: int, item: dict) -> bool:
    path = ROOT / item["path"]
    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = notebook["cells"]

    # Remove a previous generated instruction/question before rebuilding.
    cells = [
        cell for cell in cells
        if cell.get("id") not in {
            f"day{day}-official-daily-task",
            f"day{day}-single-daily-question",
        }
    ]

    rebuilt = []
    instruction_added = False
    prompt_index = 0
    for cell in cells:
        if cell.get("cell_type") == "markdown":
            text = "".join(cell.get("source", []))
            lowered = text.casefold()
            if any(signal.casefold() in lowered for signal in PROMPT_SIGNALS):
                prompt_index += 1
                cell = neutral_checkpoint(
                    day,
                    prompt_index,
                    cell.get("metadata", {}),
                    cell.get("id", f"day{day}-review-{prompt_index}"),
                )
            else:
                for old, new in REPLACEMENTS.items():
                    text = text.replace(old, new)
                cell["source"] = [line + "\n" for line in text.splitlines()[:-1]] + ([text.splitlines()[-1]] if text.splitlines() else [])
        rebuilt.append(cell)
        if not instruction_added and cell.get("cell_type") == "markdown":
            rebuilt.append(official_instruction(day))
            instruction_added = True

    rebuilt.append(final_question(day, item))
    notebook["cells"] = rebuilt
    rendered = json.dumps(notebook, ensure_ascii=False, indent=1) + "\n"
    old = path.read_text(encoding="utf-8")
    if rendered == old:
        return False
    path.write_text(rendered, encoding="utf-8")
    return True


def main() -> int:
    changed = []
    for day, item in DAYS.items():
        if simplify(day, item):
            changed.append(item["path"])
    print("Updated notebooks:" if changed else "No notebook changes required.")
    for path in changed:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
