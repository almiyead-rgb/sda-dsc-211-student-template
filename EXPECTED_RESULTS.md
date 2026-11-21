# Expected Results | النتائج المرجعية المتوقعة

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## طريقة الاستخدام

هذه الصفحة ليست إجابة جاهزة ولا درجة. استخدمها للتأكد من أن تشغيلك أنتج **البنية والحجم والحالة المتوقعة** قبل التسليم. قد تختلف قيم المقاييس والزمن قليلًا حسب بيئة Colab، لكن أسماء الملفات وعدد الصفوف الرئيس وحالات الجاهزية يجب أن تكون متقاربة مع المرجع.

## Day 1 | اليوم الأول

- ثلاثة نماذج: Logistic Regression وXGBoost وLightGBM.
- `day1_model_comparison.csv`: ثلاثة صفوف.
- `day1_comparison_predictions.csv`: عدد 2,000 صف.
- `day1_split_membership.csv`: عدد 10,000 صف.
- وجود `day1_learning_curves.png` و`day1_roc_pr.png`.
- الحالة التقنية المتوقعة: `TECHNICAL_READY`.

تحقق من أن ROC-AUC وAverage Precision بين 0 و1، وأن اختيارك مدعوم بنتيجة من تشغيلك.

## Day 2 | اليوم الثاني

| الملف | العدد المرجعي |
|---|---:|
| `validation_report.csv` | 12 |
| `validation_summary.csv` | 4 |
| `optuna_results.csv` | 8 |
| `leakage_audit.csv` | 28 |
| `fold_audit.csv` | 3 |
| `day2_oof_predictions.csv` | 10,078 |
| `day2_oof_coverage.csv` | 10,000 |

```text
technical_status = TECHNICAL_READY
whole-data OOF coverage ≈ 0.5039
shared customers inside a fold = 0
```

## Day 3 | اليوم الثالث

| الملف | العدد المرجعي |
|---|---:|
| `day3_model_report.csv` | 9 |
| `day3_model_comparison.csv` | 3 |
| `day3_oof_predictions.csv` | 15,117 |
| `day3_oof_coverage.csv` | 10,000 |
| `threshold_sweep.csv` | 5,042 |
| `day3_review_flags.csv` | 5,039 |
| `day3_period_capacity.csv` | 3 |
| `day3_region_audit.csv` | 4 |
| `day3_cost_sensitivity.csv` | 3 |

```text
Simulated Decision Loss = 10 × FN + FP
Review capacity ≤ 12% في كل فترة تحقق
probability ≥ threshold تعني إشارة مراجعة، وليست رفضًا
```

## Day 4 | اليوم الرابع

| الملف | العدد المرجعي |
|---|---:|
| `day4_roles.csv` | 10,000 |
| `day4_predictions.csv` | 2,906 |
| `permutation_importance.csv` | 20 |
| `day4_shap_global.csv` | 22 |
| `day4_reason_codes.csv` | 3 |
| `day4_local_stability.csv` | 3 |
| `day4_reliability_bins.csv` | 20 |
| `day4_period_metrics.csv` | 4 |
| `day4_bootstrap.csv` | 200 |
| `day4_policy_sweep.csv` | 592 |
| `day4_review_flags.csv` | 1,733 |
| `day4_capacity.csv` | 2 |

```text
Technical status = TECHNICAL_READY
Explanation source = LIVE
Capacity status = CAPACITY_REVIEW_REQUIRED
SHAP sample = 300 rows × 22 features
```

`CAPACITY_REVIEW_REQUIRED` نتيجة تعليمية مقبولة وليست خطأ تشغيل.

## Day 5 | اليوم الخامس

| الملف | العدد المرجعي |
|---|---:|
| `day5_roles.csv` | 10,000 |
| `day5_oof_predictions.csv` | 2,155 |
| `day5_fold_scores.csv` | 18 |
| `ensemble_comparison.csv` | 6 |
| `day5_threshold_sweep.csv` | 2,158 |
| `day5_region_audit.csv` | 4 |
| `day5_period_capacity.csv` | 3 |
| `day5_cost_sensitivity.csv` | 3 |
| `day5_probability_correlation.csv` | 3 |
| `day5_residual_correlation.csv` | 3 |
| `day5_calibration_predictions.csv` | 836 |
| `day5_calibration_fit_bins.csv` | 20 |
| `submission/submission.csv` | 2,500 |

الحالة المرجعية في التشغيل المنشور:

```text
Technical status = TECHNICAL_READY
Source = LIVE
Chosen candidate = Logistic
Complexity decision = KEEP SINGLE
```

ليس مطلوبًا أن يختار كل متدرب Logistic أو `KEEP SINGLE` إذا تغير تشغيله بصورة مبررة، لكن يجب أن تكون النتيجة قابلة لإعادة الإنتاج ومدعومة بملف `ensemble_comparison.csv`.

## Final self-check | الفحص النهائي

- الدفاتر الخمسة منفذة وتحتوي على مخرجات.
- `submission/submission.csv` يحتوي على 2,500 صف ومعرفات غير مكررة.
- تعمل `tamweel/inference.py`.
- توجد ملفات النموذج النهائي.
- توجد إجابات الأيام الخمسة في README.
- لا توجد مفاتيح أو كلمات مرور أو بيانات شخصية.
- ينجح Notebook 99 وFinal Project Check.

## English summary

Compare file names, row counts, status fields and output structure—not runtime seconds or exact image bytes. Small metric variation may occur, but missing files, empty outputs, invalid probabilities, duplicated identifiers or failed readiness states must be fixed before submission.
