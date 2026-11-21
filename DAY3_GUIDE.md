# Day 3 Guide | دليل اليوم الثالث

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## الهدف

تحويل احتمالات OOF إلى سياسة مراجعة تراعي عدم توازن الفئات وتكلفة القرار التعليمية وسعة المراجعة.

## خطوات التنفيذ

1. افتح [Notebook 03](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/03_cost_sensitive_decision.ipynb).
2. نفّذ `Runtime → Run all` على CPU المجاني.
3. راجع مقارنة طرق المعالجة ومسح العتبات.
4. تحقق من تطبيق `10 × FN + FP` ومن عدم تجاوز السعة 12% لكل فترة تحقق.
5. قارن النتائج مع [النتائج المرجعية](EXPECTED_RESULTS.md#اليوم-الثالث).

## ارفع اليوم نفسه

```text
notebooks/03_cost_sensitive_decision.ipynb
artifacts/threshold_metrics.json
artifacts/threshold_sweep.csv
artifacts/day3_region_audit.csv
artifacts/cost_curve.png
```

## سؤال اليوم

**لماذا لا تكفي العتبة 0.5 دائمًا؟**

ضع الإجابة في README تحت `Day 3 | اليوم الثالث`، ثم أرسل رابط Notebook اليوم.

## لا تنسَ

إشارة المراجعة ليست قبولًا أو رفضًا، وتكلفة القرار وحدات تعليمية وليست مبلغًا ماليًا.

## English summary

Run Notebook 03, inspect threshold cost and capacity, upload the outputs, then explain why a fixed 0.5 threshold may be inappropriate.
