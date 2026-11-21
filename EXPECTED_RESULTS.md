# Expected Results | النتائج المرجعية المتوقعة

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## كيف تستخدم هذه الصفحة؟

استخدمها للتحقق من **أسماء الملفات، وعدد الصفوف، وحالة التشغيل، وبنية المخرجات**. لا تنسخ النتائج، ولا يلزم تطابق زمن التشغيل أو بايتات الصور أو كل منزلة عشرية.

الاختلاف البسيط في المقاييس مقبول. أما الملف المفقود، أو الناتج الفارغ، أو الاحتمال خارج المدى 0–1، أو المعرف المكرر، أو حالة تشغيل فاشلة فيجب إصلاحه.

## اليوم الأول

| التحقق | النتيجة المرجعية |
|---|---|
| النماذج | Logistic Regression وXGBoost وLightGBM |
| `day1_model_comparison.csv` | 3 صفوف |
| `day1_comparison_predictions.csv` | 2,000 صف |
| `day1_split_membership.csv` | 10,000 صف |
| الرسوم | `day1_learning_curves.png` و`day1_roc_pr.png` |
| الحالة | `TECHNICAL_READY` |

## اليوم الثاني

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

## اليوم الثالث

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
Review capacity ≤ 12% لكل فترة تحقق
probability ≥ threshold = إشارة مراجعة وليست رفضًا
```

## اليوم الرابع

| الملف | العدد المرجعي |
|---|---:|
| `day4_roles.csv` | 10,000 |
| `day4_predictions.csv` | 2,906 |
| `permutation_importance.csv` | 20 |
| `day4_shap_global.csv` | 22 |
| `day4_reason_codes.csv` | 3 |
| `day4_reliability_bins.csv` | 20 |
| `day4_bootstrap.csv` | 200 |
| `day4_policy_sweep.csv` | 592 |
| `day4_review_flags.csv` | 1,733 |

```text
Technical status = TECHNICAL_READY
Explanation source = LIVE
Capacity status = CAPACITY_REVIEW_REQUIRED
SHAP sample = 300 × 22
```

`CAPACITY_REVIEW_REQUIRED` نتيجة مقبولة وليست خطأ تشغيل.

## اليوم الخامس

| الملف | العدد المرجعي |
|---|---:|
| `day5_roles.csv` | 10,000 |
| `day5_oof_predictions.csv` | 2,155 |
| `day5_fold_scores.csv` | 18 |
| `ensemble_comparison.csv` | 6 |
| `day5_threshold_sweep.csv` | 2,158 |
| `day5_calibration_predictions.csv` | 836 |
| `submission/submission.csv` | 2,500 |

```text
Technical status = TECHNICAL_READY
Source = LIVE
```

قد تعرض التجربة المرجعية `Logistic` و`KEEP SINGLE`، لكن لا يلزم نسخ هذا القرار. اعتمد قرار تشغيلك إذا كان مدعومًا بملف `ensemble_comparison.csv` وقابلًا لإعادة الإنتاج.

## الفحص النهائي

- الدفاتر 01–05 منفذة بالمخرجات.
- إجابات الأيام الخمسة موجودة في README.
- `submission.csv` يحتوي 2,500 صف ومعرفات غير مكررة.
- الاحتمالات بين 0 و1.
- ملفات النموذج النهائي و`tamweel/inference.py` موجودة.
- لا توجد أسرار أو بيانات شخصية.
- ينجح Notebook 99 وFinal Project Check.

## English summary

Compare structure, file names, row counts and status fields. Small metric differences are acceptable. Fix missing files, empty outputs, invalid probabilities, duplicate identifiers and failed technical states before submission.
