# Final Check Guide | دليل الفحص النهائي

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## قبل التصحيح النهائي

التصحيح الرسمي يتم مرة واحدة؛ لذلك نفّذ هذه القائمة قبل إرسال المشروع:

### 1. الأيام الخمسة

- Notebook 01 منفذ ومرفوع.
- Notebook 02 منفذ ومرفوع.
- Notebook 03 منفذ ومرفوع.
- Notebook 04 منفذ ومرفوع.
- Notebook 05 منفذ ومرفوع.
- إجابات الأسئلة الخمسة موجودة في README.

### 2. النتائج

قارن الملفات والحالات وعدد الصفوف مع [EXPECTED_RESULTS.md](EXPECTED_RESULTS.md). لا يشترط تطابق زمن التشغيل أو بايتات الصور.

### 3. المشروع النهائي

تأكد من وجود:

```text
submission/submission.csv
artifacts/final_model/
artifacts/final_metrics.json
artifacts/final_policy.json
reports/MODEL_CARD.md
reports/ENSEMBLE_DECISION.md
tamweel/inference.py
```

لا يوجد عرض تقديمي مطلوب، ولا توجد قوالب يدوية مطلوبة.

### 4. الأمن

ابحث في المستودع عن:

```text
sk-
ghp_
AIza
.env
password
token
```

وأزل أي سر أو بيانات شخصية قبل التسليم. إذا نُشر مفتاح فعلي، ألغِه وغيرْه؛ لا يكفي حذف الملف.

### 5. الفحص الآلي

1. شغّل [Notebook 99](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/99_final_submission_check.ipynb).
2. صحح الأخطاء.
3. شغّل `Actions → Final Project Check`.
4. افتح المستودع من نافذة خاصة.
5. أرسل الرابط النهائي عبر القناة الخاصة.

## English summary

Verify all five executed notebooks, daily answers, expected output structures, final model files, submission CSV and security. No presentation or manual templates are required. Run Notebook 99 and Final Project Check before the single formal grading.
