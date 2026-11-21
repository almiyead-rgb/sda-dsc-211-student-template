<div align="center">

# SDA-DSC-211 · Advanced Machine Learning Methods
# أساليب تعلم الآلة المتقدمة

**Tamweel Lite — خمسة أيام، خمسة لابات، مشروع واحد متكامل**

[بوابة الدورة](https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/) · [ابدأ هنا](START_HERE.md) · [مسار الأيام الخمسة](DAILY_LEARNING_PATH.md) · [النتائج المرجعية](EXPECTED_RESULTS.md) · [التسليم](SUBMISSION_GUIDE.md)

</div>

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## كيف تعمل الدورة؟

تبني مشروع **Tamweel Lite** تدريجيًا. في كل يوم تتعلم مفهومًا، وتشغّل لابًا على Google Colab، وتقارن مخرجاتك بالنتائج المرجعية، وتجيب عن سؤال واحد، ثم ترفع عمل اليوم إلى مستودعك في GitHub.

```text
تعلم → شغّل Colab → قارن النتائج → أجب → ارفع يوميًا
                                      ↓
                       مشروع متكامل في اليوم الخامس
                                      ↓
                         Notebook 99 → التسليم النهائي
```

## قبل اليوم الأول

1. أنشئ مستودعًا عامًا باسم `SDA-DSC-211-StudentCode`.
2. أضف ملف `README.md`.
3. شغّل [Notebook 00](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/00_readiness_check.ipynb).
4. استخدم CPU المجاني، ولا تربط Colab بحساب GitHub ولا تستخدم Token.
5. اقرأ [دليل الاستعداد](READINESS_GUIDE.md).

## رحلة الأيام الخمسة

| اليوم | اللاب | ما تبنيه | سؤال اليوم |
|---:|---|---|---|
| 1 | [Notebook 01](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/01_baseline_boosting.ipynb) | مقارنة Logistic Regression وXGBoost وLightGBM | أي نموذج اخترت، وما الدليل الأقوى من نتائجك؟ |
| 2 | [Notebook 02](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/02_validation_tuning.ipynb) | تحقق زمني ومنع التسرب وضبط محدود | ما التسرب الذي اكتشفته، وكيف منعته؟ |
| 3 | [Notebook 03](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/03_cost_sensitive_decision.ipynb) | عتبة قرار تراعي التكلفة والسعة | لماذا لا تكفي العتبة 0.5 دائمًا؟ |
| 4 | [Notebook 04](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/04_explain_calibrate.ipynb) | تفسير النموذج ومعايرة الاحتمالات | ما أهم خاصية، ولماذا لا تثبت السببية؟ |
| 5 | [Notebook 05](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/05_final_model.ipynb) | اختيار النموذج النهائي وتصدير المشروع | لماذا اخترت النموذج الفردي أو التجميع؟ |

## المطلوب في نهاية كل يوم

- Notebook اليوم بعد `Runtime → Run all`، محفوظًا بالمخرجات ومن دون أخطاء حمراء.
- ملفات النتائج الرئيسة المحددة في [مسار التعلم اليومي](DAILY_LEARNING_PATH.md).
- إجابة سؤال اليوم داخل `README.md` تحت عنوان:

```text
## Daily answers | الإجابات اليومية
```

- إرسال رابط المستودع ورابط Notebook اليوم عبر القناة المعتمدة.

## المشروع النهائي

ينتج اليوم الخامس النموذج النهائي وملف `submission/submission.csv` وتقارير الكود وحزمة المشروع. بعد رفع الحزمة إلى GitHub:

1. راجع [النتائج المرجعية](EXPECTED_RESULTS.md).
2. أكمل [قائمة الفحص النهائي](FINAL_CHECK_GUIDE.md).
3. شغّل [Notebook 99](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/99_final_submission_check.ipynb).
4. شغّل `Actions → Final Project Check`.
5. أرسل رابط المستودع النهائي مرة واحدة عبر القناة الخاصة.

## التقييم والشهادة

- المشروع من **100 درجة**: 80 تقنية و20 إدارية.
- حد الاجتياز **70 من 100**.
- الحضور شرط مستقل لاستحقاق الشهادة.
- استيفاء الحضور + مشروع بدرجة 70 فأعلى = **شهادة اجتياز من سدايا**.
- استيفاء الحضور دون مشروع، أو بدرجة أقل من 70 = **شهادة حضور فقط من سدايا**.

راجع [سلم التقييم](RUBRIC.md).

## الأمن والخصوصية

يمنع رفع كلمات المرور، وGitHub Tokens، ومفاتيح API، وملفات `.env`، وأرقام الهوية، والبيانات الشخصية، أو أي بيانات حقيقية لعملاء أو جهات عمل.

## English summary

Complete one Colab lab each day, compare your generated outputs with the reference page, answer one short question in README, and upload the executed notebook and key files on the same day. Day 5 exports the integrated project. Run Notebook 99 and the Final Project Check before the single final submission.
