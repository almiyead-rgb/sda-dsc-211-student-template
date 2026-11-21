# Final Check Guide | دليل الفحص النهائي

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

## نفّذ هذا الفحص قبل إرسال الرابط النهائي

### 1. الدفاتر

- [ ] Notebook 01 منفذ بالمخرجات.
- [ ] Notebook 02 منفذ بالمخرجات.
- [ ] Notebook 03 منفذ بالمخرجات.
- [ ] Notebook 04 منفذ بالمخرجات.
- [ ] Notebook 05 منفذ بالمخرجات.
- [ ] Notebook 99 موجود.
- [ ] لا توجد أخطاء حمراء محفوظة.

### 2. الإجابات اليومية

- [ ] يوجد عنوان `Daily answers | الإجابات اليومية` في README.
- [ ] توجد إجابة واضحة لكل يوم من 1 إلى 5.
- [ ] تستند الإجابات إلى نتائج تشغيلك.

### 3. النتائج

- [ ] قارنت أسماء الملفات وأعداد الصفوف مع [EXPECTED_RESULTS.md](EXPECTED_RESULTS.md).
- [ ] ملفات CSV وJSON ليست فارغة.
- [ ] الاحتمالات بين 0 و1.
- [ ] لا توجد معرفات مكررة في `submission.csv`.
- [ ] يحتوي `submission.csv` على 2,500 صف.

### 4. المشروع النهائي

- [ ] `artifacts/final_model/` موجود.
- [ ] `artifacts/final_metrics.json` موجود.
- [ ] `artifacts/final_policy.json` موجود.
- [ ] `reports/MODEL_CARD.md` موجود.
- [ ] `reports/ENSEMBLE_DECISION.md` موجود.
- [ ] `tamweel/inference.py` موجود.

### 5. الأمن

تأكد من عدم وجود:

```text
sk-
ghp_
github_pat_
AIza
.env
password
token
```

إذا نشرت مفتاحًا حقيقيًا، ألغِه وغيرْه فورًا؛ حذف الملف وحده لا يكفي.

### 6. الفحص الآلي

1. شغّل Notebook 99.
2. صحح كل خطأ مانع.
3. شغّل `Actions → Final Project Check`.
4. تأكد أن الفحص ناجح.
5. افتح المستودع من نافذة خاصة.
6. أرسل الرابط النهائي عبر القناة الخاصة.

التقييم الرسمي يتم مرة واحدة؛ لا ترسل المشروع قبل إكمال هذه القائمة.

## English summary

Verify the five executed notebooks, five README answers, expected output structure, final model files, submission CSV and security. Run Notebook 99 and the Final Project Check before sending the final repository link.
