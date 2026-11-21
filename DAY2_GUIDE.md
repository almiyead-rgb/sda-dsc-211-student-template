# Day 2 Guide | دليل اليوم الثاني

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## الهدف

بناء تحقق صادق يفصل الزمن والعملاء، ويمنع تسرب المعلومات، ويستخدم بحث Optuna محدودًا.

## خطوات التنفيذ

1. افتح [Notebook 02](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/02_validation_tuning.ipynb).
2. اختر CPU المجاني واترك الإعدادات الافتراضية.
3. نفّذ `Runtime → Run all`.
4. راجع `leakage_audit.csv` و`fold_audit.csv` ونتائج Optuna وOOF.
5. قارن ملفاتك مع [النتائج المرجعية](EXPECTED_RESULTS.md#اليوم-الثاني).

## ارفع اليوم نفسه

```text
notebooks/02_validation_tuning.ipynb
artifacts/validation_summary.csv
artifacts/leakage_audit.csv
artifacts/fold_audit.csv
artifacts/optuna_results.csv
```

## سؤال اليوم

**ما مثال التسرب الذي اكتشفته، وكيف منعته؟**

ضع الإجابة في README تحت `Day 2 | اليوم الثاني`، ثم أرسل رابط Notebook اليوم.

## لا تنسَ

لا تستخدم صفوف المستقبل أو العملاء الموجودين في التحقق داخل التدريب، ولا تختَر المعاملات من بيانات التحدي.

## English summary

Run Notebook 02, inspect the leakage and fold audits, upload the executed notebook and validation outputs, then explain one leakage risk and the control that prevented it.
