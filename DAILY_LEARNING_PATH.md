# Daily Learning Path | مسار التعلم والتسليم اليومي

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## القاعدة اليومية

كل يوم يتبع المسار نفسه:

```text
1. اقرأ هدف اليوم
2. افتح Notebook الرسمي
3. شغّل Run all على CPU المجاني
4. نزّل Notebook وملفات النتائج
5. قارنها بالنتائج المرجعية
6. أجب عن سؤال اليوم في README
7. ارفع العمل وأرسل الرابط في اليوم نفسه
```

## قبل اليوم الأول — الاستعداد

- شغّل [Notebook 00](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/00_readiness_check.ipynb).
- أنشئ مستودعًا عامًا.
- أضف في README عنوان `Daily answers | الإجابات اليومية`.

## اليوم الأول — مقارنة النماذج

**تتعلم:** الفرق بين Logistic Regression وXGBoost وLightGBM، وقراءة ROC-AUC وAverage Precision.

**اللاب:** [Notebook 01](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/01_baseline_boosting.ipynb)

**ارفع:**

```text
notebooks/01_baseline_boosting.ipynb
artifacts/day1_model_comparison.csv
artifacts/day1_learning_curves.png
artifacts/day1_roc_pr.png
```

**سؤال اليوم:** أي نموذج اخترت مبدئيًا، وما الدليل الأقوى من نتائجك؟

## اليوم الثاني — التحقق ومنع التسرب

**تتعلم:** الفصل الزمني، فصل العملاء، نضج الهدف، منع التسرب، والبحث المحدود باستخدام Optuna.

**اللاب:** [Notebook 02](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/02_validation_tuning.ipynb)

**ارفع:**

```text
notebooks/02_validation_tuning.ipynb
artifacts/validation_summary.csv
artifacts/leakage_audit.csv
artifacts/fold_audit.csv
artifacts/optuna_results.csv
```

**سؤال اليوم:** ما مثال التسرب الذي اكتشفته، وكيف منعته؟

## اليوم الثالث — العتبة والتكلفة والسعة

**تتعلم:** عدم توازن الفئات، OOF، تكلفة القرار التعليمية، اختيار العتبة، وسعة المراجعة.

**اللاب:** [Notebook 03](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/03_cost_sensitive_decision.ipynb)

**ارفع:**

```text
notebooks/03_cost_sensitive_decision.ipynb
artifacts/threshold_metrics.json
artifacts/threshold_sweep.csv
artifacts/day3_region_audit.csv
artifacts/cost_curve.png
```

**سؤال اليوم:** لماذا لا تكفي العتبة 0.5 دائمًا؟

## اليوم الرابع — التفسير والمعايرة

**تتعلم:** Permutation Importance وSHAP والتفسير المحلي والعام ومعايرة الاحتمالات والاستقرار.

**اللاب:** [Notebook 04](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/04_explain_calibrate.ipynb)

**ارفع:**

```text
notebooks/04_explain_calibrate.ipynb
artifacts/permutation_importance.csv
artifacts/shap_beeswarm.png
artifacts/shap_waterfall.png
artifacts/reliability_curve.png
artifacts/calibration_metrics.json
```

**سؤال اليوم:** ما أهم خاصية في تفسيرك، ولماذا لا تعد دليلًا على السببية؟

## اليوم الخامس — النموذج النهائي

**تتعلم:** مقارنة النموذج الفردي بالتجميع، Worth-It Gate، التثبيت النهائي، الاستدلال، وتصدير المشروع.

**اللاب:** [Notebook 05](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/05_final_model.ipynb)

**ارفع:**

```text
notebooks/05_final_model.ipynb
artifacts/ensemble_comparison.csv
artifacts/final_metrics.json
artifacts/final_policy.json
artifacts/final_model/
reports/MODEL_CARD.md
reports/ENSEMBLE_DECISION.md
submission/submission.csv
submission/project_bundle.zip
```

فك ضغط `submission/project_bundle.zip` وارفع محتوياته إلى مستودعك مع المحافظة على أسماء المجلدات.

**سؤال اليوم:** لماذا اخترت النموذج الفردي أو التجميع في النسخة النهائية؟

## رسالة التسليم اليومي

```text
الاسم:
رمز المتدرب:
اليوم:
رابط مستودع GitHub:
رابط Notebook اليوم:
```

## بعد اليوم الخامس

1. قارن المشروع مع [النتائج المرجعية](EXPECTED_RESULTS.md).
2. أكمل [الفحص النهائي](FINAL_CHECK_GUIDE.md).
3. شغّل Notebook 99.
4. شغّل Final Project Check.
5. أرسل رابط المستودع النهائي عبر القناة الخاصة.

التسليمات اليومية تثبت التقدم، أما التقييم الرسمي فيتم مرة واحدة على المشروع المتكامل.

## English summary

Every day: learn, run the official Colab notebook, download outputs, compare them with the reference page, answer one question in README, and upload on the same day. Day 5 exports the complete project bundle for the single final assessment.
