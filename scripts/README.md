# أدوات مساعدة لتشغيل مشروعك

ينفذ دفتر الاستعداد الإعداد والفحوص تلقائيًا. لا تحتاج إلى استخدام الطرفية.

- `setup_colab.py`: يجهز المساحة ويثبت الإصدارات المطلوبة ويتحقق من بصمات الملفات.
- `data_checks.py`: يفحص الأعمدة والقيم والفصل بين ملفات التدريب والتحدي.
- `readiness_checks.py`: يجرب توافق المكتبات على عينة تعليمية صغيرة مستقلة عن المشروع.
- `generate_synthetic_data.py`: يعيد إنشاء التدريب ونسخة التسرب بالبذرة المعلنة؛ لا ينشئ بيانات التحدي أو إجاباتها.

للتوسع الاختياري محليًا، من جذر مشروعك:

```bash
python scripts/generate_synthetic_data.py --output regenerated_data
python -m unittest discover -s tests -v
```

The notebook handles setup for you. These helpers validate inputs and software compatibility; they do not replace your model comparisons or written reasoning.
