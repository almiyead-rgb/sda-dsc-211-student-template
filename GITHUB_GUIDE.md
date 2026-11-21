# Simple GitHub Guide | دليل GitHub المبسط

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## إنشاء المستودع

1. اختر `New repository`.
2. استخدم الاسم `SDA-DSC-211-StudentCode`.
3. اختر `Public`.
4. فعّل `Add a README file`.
5. اضغط `Create repository`.

## تنظيم المشروع

استخدم هذا التنظيم قبل التسليم النهائي:

```text
README.md
notebooks/
artifacts/
reports/
submission/
tamweel/
```

يمكنك رفع المجلد كاملًا بسحبه إلى صفحة `Upload files`. في الأيام الأولى يكفي رفع Notebook والملفات المطلوبة، ثم تنظيم المشروع كاملًا عند تصدير حزمة اليوم الخامس.

## رفع ملفات كل يوم

1. نزّل Notebook وملفات النتائج من Colab.
2. افتح مستودعك.
3. اختر `Add file → Upload files`.
4. ارفع الملفات إلى المسار المطلوب.
5. اكتب رسالة واضحة، مثل:

```text
Complete Day 3 decision lab
```

6. اضغط `Commit changes`.

## كتابة إجابات الأيام

أضف إلى README:

```markdown
## Daily answers | الإجابات اليومية

### Day 1 | اليوم الأول
إجابتك...

### Day 2 | اليوم الثاني
إجابتك...

### Day 3 | اليوم الثالث
إجابتك...

### Day 4 | اليوم الرابع
إجابتك...

### Day 5 | اليوم الخامس
إجابتك...
```

## فحص المستودع

- افتح الرابط من نافذة خاصة.
- تأكد أن المستودع Public.
- افتح Notebook وتأكد من ظهور المخرجات.
- افتح ملفات CSV وJSON وتأكد أنها ليست فارغة.
- لا ترفع ZIP وحده؛ فك الضغط وارفع الملفات المطلوبة.

## الأمن

لا ترفع كلمات مرور أو GitHub Tokens أو API Keys أو ملفات `.env` أو بيانات شخصية. لا تربط Colab بحساب GitHub؛ استخدم التنزيل والرفع اليدوي.

## English summary

Create one normal public repository, upload files through the browser, keep the final folder structure, and add one daily answer to README. No template, terminal, token or Colab–GitHub connection is required.
