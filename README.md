<div align="center">

# SDA-DSC-211 · Advanced Machine Learning Methods  
# أساليب تعلم الآلة المتقدمة

**Tamweel Lite student project | مشروع المتدرب Tamweel Lite**

[Learning portal](https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/) · [Arabic portal](https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/ar.html) · [English portal](https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/en.html)

[![Environment Check](https://github.com/almiyead-rgb/sda-dsc-211-student-template/actions/workflows/validate.yml/badge.svg)](https://github.com/almiyead-rgb/sda-dsc-211-student-template/actions/workflows/validate.yml)
[![Notebook Smoke Test](https://github.com/almiyead-rgb/sda-dsc-211-student-template/actions/workflows/notebook_smoke.yml/badge.svg)](https://github.com/almiyead-rgb/sda-dsc-211-student-template/actions/workflows/notebook_smoke.yml)
[![Bilingual Content Check](https://github.com/almiyead-rgb/sda-dsc-211-student-template/actions/workflows/bilingual_content_check.yml/badge.svg)](https://github.com/almiyead-rgb/sda-dsc-211-student-template/actions/workflows/bilingual_content_check.yml)

</div>

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

<table>
<tr>
<td width="50%" valign="top" dir="ltr">

## Your project workspace

Use this template to build one connected project across five days. Keep your notebooks, reports, evidence and final presentation in your own repository.

The status badges validate the template and workflows. A green badge does not award marks, prove attendance or issue a certificate.

</td>
<td width="50%" valign="top" dir="rtl">

## مساحة مشروعك

استخدم هذا القالب لبناء مشروع واحد مترابط خلال خمسة أيام. احفظ دفاترك وتقاريرك وأدلتك وعرضك النهائي داخل مستودعك الخاص بالمشروع.

تفحص مؤشرات الحالة القالب ومسارات الأتمتة. لا يمنح اللون الأخضر درجات، ولا يثبت الحضور، ولا يصدر شهادة.

</td>
</tr>
</table>

## Start here | ابدأ هنا

<table>
<tr>
<td width="50%" valign="top" dir="ltr">

1. Read [START_HERE.md](START_HERE.md).
2. Complete the [readiness guide](READINESS_GUIDE.md).
3. Open [Notebook 00 in Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/00_readiness_check.ipynb).
4. Save a copy of each notebook before editing it.
5. Keep code, reports and actual output files; screenshots alone are not sufficient evidence.

</td>
<td width="50%" valign="top" dir="rtl">

1. اقرأ [START_HERE.md](START_HERE.md).
2. أكمل [دليل الاستعداد](READINESS_GUIDE.md).
3. افتح [دفتر 00 في Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/00_readiness_check.ipynb).
4. احفظ نسخة من كل دفتر قبل تعديله.
5. احتفظ بالكود والتقارير وملفات المخرجات الفعلية؛ لا تكفي لقطات الشاشة وحدها كدليل.

</td>
</tr>
</table>

## Five-day build | البناء خلال خمسة أيام

| Day | English focus and evidence | المحور والدليل بالعربية | Lab |
|---:|---|---|---|
| 1 | Baseline, XGBoost and LightGBM; model comparison | خط الأساس وXGBoost وLightGBM؛ مقارنة النماذج | [Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/01_baseline_boosting.ipynb) · [Guide](DAY1_GUIDE.md) |
| 2 | Honest validation, leakage control and bounded Optuna search | التحقق الصادق ومنع التسرب والبحث المحدود بـOptuna | [Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/02_validation_tuning.ipynb) · [Guide](DAY2_GUIDE.md) |
| 3 | Imbalance, OOF probabilities, simulated decision cost and capacity | عدم التوازن واحتمالات OOF وتكلفة القرار التعليمية والسعة | [Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/03_cost_sensitive_decision.ipynb) · [Guide](DAY3_GUIDE.md) |
| 4 | Permutation importance, SHAP, calibration and stability | أهمية التبديل وSHAP والمعايرة والاستقرار | [Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/04_explain_calibrate.ipynb) · [Guide](DAY4_GUIDE.md) |
| 5 | Averaging, stacking, final model, Model Card and delivery | المتوسطات والتكديس والنموذج النهائي وبطاقة النموذج والتسليم | [Colab](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/05_final_model.ipynb) · [Guide](DAY5_GUIDE.md) |

## Repository map | خريطة المستودع

- `notebooks/` — executed daily notebooks | دفاتر الأيام المنفذة
- `artifacts/` — CSV, JSON, figures and evidence | ملفات الأدلة والرسوم
- `reports/` — Decision Card, interpretation report and Model Card | تقارير المشروع
- `submission/` — final predictions and manifest | التنبؤات النهائية والـManifest
- `presentation/` — five-slide presentation and PDF | العرض النهائي
- `tamweel/` — reproducible inference interface | واجهة الاستدلال
- `scripts/` — setup and checks | أدوات الإعداد والفحص
- `data/` — synthetic data and contract | البيانات الاصطناعية وعقد البيانات

## Assessment and certificates | التقييم والشهادات

<table>
<tr>
<td width="50%" valign="top" dir="ltr">

- **Project score:** 100 points.
- **Technical requirements:** 80 points.
- **Administrative requirements:** 20 points.
- **Completion threshold:** 70 / 100.
- **Attendance:** verified separately and required for completion-certificate eligibility.

A learner who satisfies the approved attendance requirement, submits the project and earns 70 or more receives a **SDAIA completion certificate**. A learner who satisfies the attendance requirement but submits no project, or earns less than 70, receives a **SDAIA attendance certificate only**.

Read [RUBRIC.md](RUBRIC.md), [TECHNICAL_REQUIREMENTS.md](TECHNICAL_REQUIREMENTS.md) and [ADMINISTRATIVE_REQUIREMENTS.md](ADMINISTRATIVE_REQUIREMENTS.md).

</td>
<td width="50%" valign="top" dir="rtl">

- **درجة المشروع:** 100 درجة.
- **المتطلبات التقنية:** 80 درجة.
- **المتطلبات الإدارية:** 20 درجة.
- **حد الاجتياز:** 70 من 100.
- **الحضور:** يُتحقق منه بصورة مستقلة، وهو شرط لاستحقاق شهادة الاجتياز.

يحصل المتدرب على **شهادة اجتياز من سدايا** عند استيفاء متطلبات الحضور المعتمدة، وتسليم المشروع، والحصول على 70 درجة فأعلى. أما من يستوفي الحضور دون تسليم مشروع، أو يحصل على أقل من 70، فيحصل على **شهادة حضور فقط من سدايا**.

راجع [سلم التقييم](RUBRIC.md) و[المتطلبات التقنية](TECHNICAL_REQUIREMENTS.md) و[المتطلبات الإدارية](ADMINISTRATIVE_REQUIREMENTS.md).

</td>
</tr>
</table>

## Final verification and submission | الفحص والتسليم النهائي

1. Complete all notebooks, learner responses and reports. | أكمل جميع الدفاتر والإجابات والتقارير.
2. Run [Notebook 99](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/99_final_submission_check.ipynb). | شغّل دفتر 99.
3. Correct issues and rerun the check. | صحح الملاحظات وأعد الفحص.
4. Run **Actions → Final Project Check**. | شغّل الفحص النهائي في GitHub Actions.
5. Create the final tag on the exact checked commit. | أنشئ Tag نهائيًا على Commit نفسه.
6. Submit through the approved private cohort channel. | سلّم عبر القناة الخاصة المعتمدة للدفعة.

Technical readiness is not a grade, attendance record or certificate decision.

الجاهزية التقنية ليست درجة ولا سجل حضور ولا قرار شهادة.

## Guides and support | الأدلة والدعم

| Need | Resource | الاحتياج | المرجع |
|---|---|---|---|
| Colab | [COLAB_GUIDE.md](COLAB_GUIDE.md) | استخدام Colab | [دليل Colab](COLAB_GUIDE.md) |
| GitHub | [GITHUB_GUIDE.md](GITHUB_GUIDE.md) | حفظ المشروع | [دليل GitHub](GITHUB_GUIDE.md) |
| Requirements | [TECHNICAL_REQUIREMENTS.md](TECHNICAL_REQUIREMENTS.md) · [ADMINISTRATIVE_REQUIREMENTS.md](ADMINISTRATIVE_REQUIREMENTS.md) | المتطلبات | [التقنية](TECHNICAL_REQUIREMENTS.md) · [الإدارية](ADMINISTRATIVE_REQUIREMENTS.md) |
| Submission | [SUBMISSION_GUIDE.md](SUBMISSION_GUIDE.md) · [FINAL_CHECK_GUIDE.md](FINAL_CHECK_GUIDE.md) | التسليم والفحص | [دليل التسليم](SUBMISSION_GUIDE.md) · [دليل الفحص](FINAL_CHECK_GUIDE.md) |
| Terms | [GLOSSARY.md](GLOSSARY.md) | المصطلحات | [القاموس](GLOSSARY.md) |
| Troubleshooting | [TROUBLESHOOTING.md](TROUBLESHOOTING.md) · [FAQ.md](FAQ.md) | حل المشكلات | [حل المشكلات](TROUBLESHOOTING.md) · [الأسئلة الشائعة](FAQ.md) |
| Learning resources | [LEARNING_RESOURCES.md](LEARNING_RESOURCES.md) | الفيديوهات والمراجع | [الموارد التعليمية](LEARNING_RESOURCES.md) |

> Do not place personal data, passwords, access tokens, private grades or submission receipts in a public repository.  
> لا تضع بيانات شخصية أو كلمات مرور أو رموز وصول أو درجات خاصة أو إيصالات تسليم داخل مستودع عام.

Prepared and delivered by **Meaad Al-Marri | ميعاد المري** · [Attribution and educational use](NOTICE.md).
