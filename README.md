<div align="center">

# SDA-DSC-211 · Advanced Machine Learning Methods
# أساليب تعلم الآلة المتقدمة

**Tamweel Lite — مشروع يومي متدرج ينتهي بمشروع متكامل**

[بوابة الدورة](https://almiyead-rgb.github.io/advanced-machine-learning-methods-sda-dsc-211/) · [مسار التعلم اليومي](DAILY_LEARNING_PATH.md) · [النتائج المتوقعة](EXPECTED_RESULTS.md) · [دليل التسليم](SUBMISSION_GUIDE.md)

</div>

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## الفكرة الأساسية

لا توجد قوالب تقارير أو عرض تقديمي إلزامي. يعمل المتدرب كل يوم على جزء واحد من مشروع **Tamweel Lite** داخل Google Colab، ثم يرفع في اليوم نفسه:

1. دفتر اليوم بعد تنفيذ `Run all`.
2. ملفات النتائج التي أنشأها الكود.
3. إجابة قصيرة عن سؤال اليوم داخل `README.md` في مستودعه.

في اليوم الخامس يجمع الكود المراحل السابقة ويصدر النموذج النهائي وملف التنبؤات والحزمة المتكاملة. بعد ذلك يشغّل المتدرب دفتر الفحص 99 مرة واحدة قبل التسليم النهائي.

## Simple learning model | نموذج التعلم المبسط

| Day | Lab | What you build | سؤال التسليم اليومي |
|---:|---|---|---|
| 0 | [Readiness Notebook](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/00_readiness_check.ipynb) | فحص البيئة والحسابات والملفات | هل بيئتك جاهزة دون أخطاء حمراء؟ |
| 1 | [Colab 01](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/01_baseline_boosting.ipynb) | مقارنة Logistic Regression وXGBoost وLightGBM | أي نموذج اخترت مبدئيًا، وما الدليل الأقوى من نتائجك؟ |
| 2 | [Colab 02](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/02_validation_tuning.ipynb) | تحقق زمني ومنع التسرب وضبط محدود | ما مثال التسرب الذي اكتشفته، وكيف منعته؟ |
| 3 | [Colab 03](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/03_cost_sensitive_decision.ipynb) | عتبة قرار تراعي التكلفة والسعة | لماذا لا تكفي العتبة 0.5 دائمًا؟ |
| 4 | [Colab 04](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/04_explain_calibrate.ipynb) | تفسير النموذج ومعايرة الاحتمالات | ما أهم خاصية في تفسيرك، وما الحد الذي يمنعك من اعتبارها سببًا؟ |
| 5 | [Colab 05](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/05_final_model.ipynb) | اختيار النموذج النهائي وتصدير المشروع | لماذا اخترت النموذج الفردي أو التجميع في النسخة النهائية؟ |

## خطوات كل يوم

1. افتح لاب اليوم في Colab.
2. اختر CPU المجاني ثم `Runtime → Run all`.
3. لا تعدّل الكود قبل نجاح التشغيل الأول.
4. قارن نتائجك بصفحة [النتائج المتوقعة](EXPECTED_RESULTS.md).
5. نزّل الدفتر المنفذ وملفات النتائج.
6. ارفعها إلى مستودعك في اليوم نفسه.
7. أضف إجابة سؤال اليوم في `README.md` تحت عنوان `Daily answers | الإجابات اليومية`.
8. تأكد من أن الملفات تفتح من نافذة خاصة.

## Daily submission | التسليم اليومي

يرسل المتدرب عبر القناة المعتمدة:

```text
الاسم:
رمز المتدرب:
اليوم:
رابط مستودع GitHub:
رابط Notebook اليوم:
```

لا تمنح التسليمات اليومية درجة مستقلة، لكنها تدخل ضمن اكتمال المتطلبات الإدارية للمشروع.

## Final project | المشروع النهائي

بنهاية اليوم الخامس يجب أن يحتوي المستودع على:

```text
README.md
notebooks/01_baseline_boosting.ipynb
notebooks/02_validation_tuning.ipynb
notebooks/03_cost_sensitive_decision.ipynb
notebooks/04_explain_calibrate.ipynb
notebooks/05_final_model.ipynb
notebooks/99_final_submission_check.ipynb
artifacts/
reports/MODEL_CARD.md
reports/ENSEMBLE_DECISION.md
submission/submission.csv
tamweel/inference.py
```

ملفات `MODEL_CARD.md` و`ENSEMBLE_DECISION.md` تنتجها اللابات؛ لا توجد قوالب منفصلة يعبئها المتدرب.

## Final check | الفحص النهائي

1. أكمل الأيام الخمسة وتسليماتها.
2. افتح [Notebook 99](https://colab.research.google.com/github/almiyead-rgb/sda-dsc-211-student-template/blob/main/notebooks/99_final_submission_check.ipynb).
3. صحح أي مشكلة قبل التسليم؛ التصحيح الرسمي للمشروع يتم مرة واحدة.
4. شغّل **Actions → Final Project Check**.
5. سلّم رابط المستودع عبر القناة الخاصة المعتمدة.

## Assessment and certificate | التقييم والشهادة

- المشروع يقيم من **100 درجة** وفق المتطلبات التقنية والإدارية.
- الحضور شرط مستقل لاستحقاق الشهادة.
- من يستوفي الحضور، ويسلم المشروع، ويحصل على **70 فأعلى** يحصل على **شهادة اجتياز من سدايا**.
- من يستوفي الحضور دون مشروع، أو يحصل على أقل من 70، يحصل على **شهادة حضور فقط من سدايا**.

راجع [سلم التقييم](RUBRIC.md) و[المتطلبات الإدارية](ADMINISTRATIVE_REQUIREMENTS.md).

> البيانات اصطناعية. يمنع رفع كلمات المرور أو Tokens أو مفاتيح API أو بيانات شخصية أو بيانات جهة عمل حقيقية.

Prepared and delivered by **Meaad Al-Marri | ميعاد المري**.
