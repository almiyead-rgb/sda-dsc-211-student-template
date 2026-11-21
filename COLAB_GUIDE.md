# Google Colab Guide | دليل Google Colab

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## استخدم Colab للتنفيذ وGitHub للحفظ

جلسة Colab مؤقتة. قد تختفي المتغيرات والملفات عند انتهاء الجلسة؛ لذلك نزّل عملك في نهاية كل يوم وارفعه إلى GitHub.

## تشغيل اللاب

1. افتح رابط Notebook الرسمي من بوابة الدورة أو [مسار الأيام الخمسة](DAILY_LEARNING_PATH.md).
2. تأكد أن الرابط يحتوي على:

```text
almiyead-rgb/sda-dsc-211-student-template
```

3. اختر CPU المجاني.
4. اترك `FAST_MODE=True`.
5. نفّذ `Runtime → Run all`.
6. لا تعدّل الكود قبل نجاح التشغيل الأول.
7. انتظر حتى تنتهي جميع الخلايا.
8. اقرأ النتائج والتحذيرات؛ بعض الحالات مثل `CAPACITY_REVIEW_REQUIRED` نتيجة تعليمية وليست خطأ.

## حفظ Notebook

بعد نجاح التشغيل:

1. اختر `File → Download → Download .ipynb`.
2. لا تمسح المخرجات من الدفتر.
3. ارفع الملف إلى مجلد `notebooks/` في مستودعك.

## تنزيل ملفات النتائج

1. افتح لوحة `Files` في الجانب الأيسر.
2. اضغط Refresh إذا لم تظهر الملفات.
3. افتح مجلد `/content/tamweel/`.
4. نزّل الملفات المطلوبة من `artifacts/` أو `reports/` أو `submission/`.
5. عند توفر ملف ZIP، نزّله وفك ضغطه على جهازك قبل الرفع إلى GitHub.

## إعادة التشغيل

أعد تشغيل الجلسة عندما:

- يطلب Notebook ذلك بعد تثبيت الحزم.
- يظهر تعارض في إصدارات الحزم.
- شغّلت الخلايا بترتيب غير صحيح.

بعد إعادة التشغيل، نفّذ `Run all` من البداية.

## قواعد الأمان

- لا تربط Google Drive.
- لا تدخل كلمة مرور أو Token أو API Key.
- لا تعطّل فحوص البصمة أو عقد البيانات.
- لا تستخدم ملفات أو نتائج متدرب آخر.
- لا ترفع صورًا بدل الملفات الفعلية.

## قبل إغلاق Colab

- [ ] Notebook منفذ ولا يحتوي أخطاء حمراء.
- [ ] Notebook محفوظ على جهازك.
- [ ] ملفات النتائج المطلوبة محفوظة على جهازك.
- [ ] الملفات مرفوعة إلى GitHub.
- [ ] فتحت الملفات من GitHub وتأكدت منها.

## English summary

Use free CPU, keep `FAST_MODE=True`, run all cells from the beginning, download the executed notebook and generated files, then upload them manually to GitHub. Do not connect Drive or GitHub accounts and never paste a token into Colab.
