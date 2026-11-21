# Daily and Final Submission Guide | دليل التسليم اليومي والنهائي

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## السياسة المبسطة

يبني المتدرب مشروعًا واحدًا خلال خمسة أيام. يوجد **تسليم متابعة يومي**، ثم **تسليم نهائي واحد للتقييم**. لا توجد قوالب تقارير أو عرض تقديمي إلزامي.

## التسليم اليومي

في نهاية كل يوم أرسل عبر القناة المعتمدة:

```text
الاسم:
رمز المتدرب:
اليوم:
رابط المستودع:
رابط Notebook اليوم:
```

ويجب أن يكون قد رُفع إلى GitHub:

1. Notebook اليوم بعد `Run all`.
2. ملفات النتائج الأساسية المحددة في [مسار التعلم اليومي](DAILY_LEARNING_PATH.md).
3. إجابة سؤال اليوم داخل README.

التسليم اليومي يستخدم للتحقق من التقدم واكتشاف المشكلة مبكرًا. لا يمثل تصحيحًا نهائيًا ولا يمنح درجة مستقلة.

## التسليم النهائي

بعد اليوم الخامس:

1. تأكد من اكتمال تسليمات الأيام الخمسة.
2. قارن النتائج مع [EXPECTED_RESULTS.md](EXPECTED_RESULTS.md).
3. شغّل Notebook 99 مرة واحدة.
4. صحح جميع المشكلات قبل الإرسال؛ التصحيح الرسمي يتم مرة واحدة.
5. شغّل Final Project Check في GitHub Actions.
6. أرسل رابط المستودع النهائي عبر القناة الخاصة.

## الحد الأدنى للمشروع النهائي

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
artifacts/final_model/
tamweel/inference.py
```

## لا يطلب من المتدرب

- إعداد عرض تقديمي.
- تعبئة قوالب تقارير منفصلة.
- ربط Colab بحساب GitHub.
- منح Colab Token أو صلاحية وصول.
- شراء اشتراك أو استخدام GPU.

## Security | الأمن

يمنع رفع كلمات المرور أو API Keys أو GitHub Tokens أو ملفات `.env` أو بيانات شخصية أو بيانات جهة عمل حقيقية.

## English summary

Upload the executed notebook, key generated outputs and one short README answer at the end of each day. On Day 5, export the integrated project, run Notebook 99 and GitHub Final Project Check, then submit the repository once for formal grading.
