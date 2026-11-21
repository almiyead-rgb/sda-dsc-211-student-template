# Day 4 Guide | دليل اليوم الرابع

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## الهدف

تفسير النموذج وقياس معايرة الاحتمالات واستقرار النتائج، مع الالتزام بحدود التفسير.

## خطوات التنفيذ

1. افتح [Notebook 04](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/04_explain_calibrate.ipynb).
2. نفّذ `Runtime → Run all` على CPU المجاني.
3. راجع Permutation Importance وSHAP العالمي والمحلي.
4. راجع Brier وECE ومنحنى الموثوقية والاستقرار.
5. قارن النتائج مع [النتائج المرجعية](EXPECTED_RESULTS.md#اليوم-الرابع).

## ارفع اليوم نفسه

```text
notebooks/04_explain_calibrate.ipynb
artifacts/permutation_importance.csv
artifacts/shap_beeswarm.png
artifacts/shap_waterfall.png
artifacts/reliability_curve.png
artifacts/calibration_metrics.json
```

## سؤال اليوم

**ما أهم خاصية في تفسيرك، ولماذا لا تعد دليلًا على السببية؟**

ضع الإجابة في README تحت `Day 4 | اليوم الرابع`، ثم أرسل رابط Notebook اليوم.

## لا تنسَ

SHAP يشرح سلوك النموذج ولا يثبت سببًا حقيقيًا أو عدالة أو امتثالًا. وقد تكون `CAPACITY_REVIEW_REQUIRED` نتيجة صحيحة.

## English summary

Run Notebook 04, inspect SHAP, calibration and stability, upload the key outputs, then identify an important feature and explain why it is not causal proof.
