# Daily Learning Path | مسار التعلم والتسليم اليومي

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## القاعدة التشغيلية

كل يوم = **تعلم قصير + لاب Colab + ناتج قابل للمقارنة + سؤال واحد + رفع يومي**.

لا توجد قوالب يدوية، ولا عرض تقديمي إلزامي. ينتج الكود الملفات الفنية تلقائيًا، ويجمع اليوم الخامس المشروع النهائي.

## قبل اليوم الأول

1. أنشئ مستودع GitHub عامًا باسم واضح.
2. افتح [دفتر الاستعداد 00](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/00_readiness_check.ipynb).
3. تأكد من ظهور حالة جاهزية دون أخطاء حمراء.
4. أنشئ في `README.md` عنوانًا باسم:

```text
## Daily answers | الإجابات اليومية
```

## اليوم الأول — النماذج الأساسية والتعزيز

**التعلم:** الفرق بين خط الأساس وXGBoost وLightGBM، وقراءة ROC-AUC وAverage Precision.

**نفّذ:** [Notebook 01](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/01_baseline_boosting.ipynb)

**ارفع اليوم نفسه:**

```text
notebooks/01_baseline_boosting.ipynb
artifacts/day1_model_comparison.csv
artifacts/day1_learning_curves.png
artifacts/day1_roc_pr.png
```

**السؤال:** أي نموذج اخترت مبدئيًا، وما الدليل الأقوى من نتائجك؟

## اليوم الثاني — التحقق ومنع التسرب

**التعلم:** الفصل الزمني، فصل العملاء، نضج الهدف، ومنع تسرب البيانات، وضبط Optuna المحدود.

**نفّذ:** [Notebook 02](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/02_validation_tuning.ipynb)

**ارفع اليوم نفسه:**

```text
notebooks/02_validation_tuning.ipynb
artifacts/validation_summary.csv
artifacts/leakage_audit.csv
artifacts/fold_audit.csv
artifacts/optuna_results.csv
```

**السؤال:** ما مثال التسرب الذي اكتشفته، وكيف منعته؟

## اليوم الثالث — القرار الحساس للتكلفة

**التعلم:** عدم توازن الفئات، تنبؤات OOF، تكلفة القرار التعليمية، العتبة، وسعة المراجعة.

**نفّذ:** [Notebook 03](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/03_cost_sensitive_decision.ipynb)

**ارفع اليوم نفسه:**

```text
notebooks/03_cost_sensitive_decision.ipynb
artifacts/threshold_metrics.json
artifacts/threshold_sweep.csv
artifacts/day3_region_audit.csv
artifacts/cost_curve.png
```

**السؤال:** لماذا لا تكفي العتبة 0.5 دائمًا؟

## اليوم الرابع — التفسير والمعايرة

**التعلم:** Permutation Importance وSHAP والتفسير المحلي والعام ومعايرة الاحتمالات والاستقرار.

**نفّذ:** [Notebook 04](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/04_explain_calibrate.ipynb)

**ارفع اليوم نفسه:**

```text
notebooks/04_explain_calibrate.ipynb
artifacts/permutation_importance.csv
artifacts/shap_beeswarm.png
artifacts/shap_waterfall.png
artifacts/reliability_curve.png
artifacts/calibration_metrics.json
```

**السؤال:** ما أهم خاصية في تفسيرك، وما الحد الذي يمنعك من اعتبارها سببًا؟

## اليوم الخامس — النموذج النهائي والتصدير

**التعلم:** مقارنة النموذج الفردي بالتجميع، Worth-It Gate، المعايرة النهائية، الاستدلال، وتصدير المشروع.

**نفّذ:** [Notebook 05](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/05_final_model.ipynb)

**ارفع اليوم نفسه:**

```text
notebooks/05_final_model.ipynb
artifacts/ensemble_comparison.csv
artifacts/final_metrics.json
artifacts/final_policy.json
reports/MODEL_CARD.md
reports/ENSEMBLE_DECISION.md
submission/submission.csv
artifacts/final_model/
```

**السؤال:** لماذا اخترت النموذج الفردي أو التجميع في النسخة النهائية؟

## نهاية اليوم الخامس

1. راجع [النتائج المتوقعة](EXPECTED_RESULTS.md).
2. تأكد من وجود إجابات الأيام الخمسة في `README.md`.
3. شغّل [Notebook 99](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/99_final_submission_check.ipynb).
4. افتح المستودع من نافذة خاصة وتأكد أن جميع الملفات تعمل.
5. أرسل رابط المشروع النهائي مرة واحدة عبر القناة الخاصة.

## English summary

Complete one Colab lab each day, compare the generated files with `EXPECTED_RESULTS.md`, answer one short question in your README, and upload the executed notebook plus key outputs on the same day. Day 5 exports the integrated project; Notebook 99 is the final self-check before the single formal grading.
