# Assessment Rubric | سلم التقييم

<!-- BILINGUAL:EN -->
<!-- BILINGUAL:AR -->

<table>
<tr>
<td width="50%" valign="top" dir="ltr">

## Assessment model

The final assessment is based on two elements:

1. **Project:** scored out of **100 points** and assessed against technical and administrative requirements.
2. **Attendance:** a separate eligibility requirement that determines the certificate type; it is not added as project points.

A learner who meets the approved attendance requirement, submits the project and earns **70 or more out of 100** receives a **SDAIA completion certificate**. A learner who meets the attendance requirement but does not submit a project, or earns less than 70, receives a **SDAIA attendance certificate only**.

</td>
<td width="50%" valign="top" dir="rtl">

## نموذج التقييم

يعتمد التقييم النهائي على عنصرين:

1. **المشروع:** يُقيَّم من **100 درجة** وفق المتطلبات التقنية والإدارية.
2. **الحضور:** شرط مستقل يحدد نوع الشهادة، ولا يضاف بوصفه درجات إلى المشروع.

يحصل المتدرب على **شهادة اجتياز من سدايا** عند استيفاء متطلبات الحضور المعتمدة، وتسليم المشروع، والحصول على **70 درجة فأعلى من 100**. أما من يستوفي الحضور دون تسليم مشروع، أو يحصل على أقل من 70، فيحصل على **شهادة حضور فقط من سدايا**.

</td>
</tr>
</table>

## Technical project requirements — 80 points | المتطلبات التقنية للمشروع — 80 درجة

| Code | Points | English criterion | المعيار بالعربية | Primary evidence |
|---|---:|---|---|---|
| T1 | 10 | Reproducibility, Colab readiness, dependency control and clean execution | قابلية إعادة الإنتاج وجاهزية Colab وضبط الإصدارات والتشغيل السليم | versions, seeds, hashes, logs, manifest |
| T2 | 10 | Day 1 baseline, XGBoost and LightGBM comparison | اليوم الأول: خط الأساس ومقارنة XGBoost وLightGBM | model comparison, learning curves, candidate decision |
| T3 | 15 | Day 2 honest validation, leakage control and bounded Optuna search | اليوم الثاني: التحقق الصادق ومنع التسرب وبحث Optuna المحدود | role/fold audits, OOF evidence, search results |
| T4 | 15 | Day 3 imbalance treatment, simulated decision cost, threshold and capacity | اليوم الثالث: معالجة عدم التوازن وتكلفة القرار التعليمية والعتبة والسعة | OOF predictions, threshold sweep, Decision Card |
| T5 | 15 | Day 4 permutation importance, SHAP, calibration and stability | اليوم الرابع: أهمية التبديل وSHAP والمعايرة والاستقرار | figures, metrics, Interpretability Report |
| T6 | 10 | Day 5 final model, ensemble decision, integrated pipeline and portable inference | اليوم الخامس: النموذج النهائي وقرار التجميع والخط المتكامل والاستدلال القابل للنقل | Worth-It Gate, final model, inference test |
| T7 | 5 | Model Card, responsible-use limits, regional audit and unresolved gaps | بطاقة النموذج وحدود الاستخدام المسؤول وتدقيق المناطق والفجوات | Model Card, limitations, monitoring notes |
|  | **80** | **Technical subtotal** | **مجموع المتطلبات التقنية** |  |

## Administrative project requirements — 20 points | المتطلبات الإدارية للمشروع — 20 درجة

| Code | Points | English criterion | المعيار بالعربية | Primary evidence |
|---|---:|---|---|---|
| A1 | 6 | Professional repository structure, README, clear navigation and complete required files | تنظيم مهني للمستودع وREADME واضح وتنقل سهل واكتمال الملفات المطلوبة | README, links, folders, rendered pages |
| A2 | 4 | Documentation, provenance, source disclosure, package versions and limitations | التوثيق ومصدر التنفيذ والإفصاح عن المصادر وإصدارات الحزم والقيود | README, provenance, references, disclosures |
| A3 | 5 | Final verification, exact version identity and complete submission package | الفحص النهائي وتحديد النسخة الدقيقة واكتمال حزمة التسليم | Notebook 99, tag, exact SHA, manifest, submission files |
| A4 | 5 | Final presentation and project defence using evidence from the submitted repository | العرض النهائي ومناقشة المشروع بالاستناد إلى أدلة المستودع المسلّم | five-slide PDF, oral answers, repository evidence |
|  | **20** | **Administrative subtotal** | **مجموع المتطلبات الإدارية** |  |

## Final score | الدرجة النهائية

```text
Final project score = Technical requirements (80) + Administrative requirements (20) = 100
درجة المشروع النهائية = المتطلبات التقنية (80) + المتطلبات الإدارية (20) = 100
```

- **70–100:** project passes, subject to satisfying the approved attendance requirement.
- **0–69.99:** project does not meet the completion threshold.
- Attendance is verified separately and is not converted into project marks.

- **من 70 إلى 100:** يجتاز المشروع، بشرط استيفاء متطلبات الحضور المعتمدة.
- **أقل من 70:** لا يحقق المشروع حد الاجتياز.
- يُتحقق من الحضور بصورة مستقلة ولا يحول إلى درجات داخل المشروع.

## Certificate outcomes | نتائج الشهادة

| Attendance status | Project status | Certificate outcome |
|---|---|---|
| Approved attendance requirement met | Project submitted and score is 70 or more | **SDAIA completion certificate — شهادة اجتياز من سدايا** |
| Approved attendance requirement met | No project submitted, or score is below 70 | **SDAIA attendance certificate only — شهادة حضور فقط من سدايا** |
| Approved attendance requirement not met | Any project status | Certificate status is handled according to the approved SDAIA attendance rules. |

## Performance levels | مستويات الأداء

| Level | English descriptor | الوصف بالعربية | Typical score range within a criterion |
|---|---|---|---|
| 4 — Mastered | Correct, complete, reproducible, well justified and supported by consistent evidence. | صحيح ومكتمل وقابل لإعادة الإنتاج ومبرر ومدعوم بأدلة متسقة. | 90–100% of criterion points |
| 3 — Achieved | Core requirement is correct and reproducible with minor gaps. | المتطلب الأساسي صحيح وقابل لإعادة الإنتاج مع نواقص محدودة. | 70–89% |
| 2 — Partially achieved | Output exists, but method, evidence or interpretation is incomplete. | يوجد مخرج، لكن المنهج أو الدليل أو التفسير غير مكتمل. | 40–69% |
| 1 — Not achieved | Required output is missing, materially incorrect, unsupported or not reproducible. | المخرج المطلوب مفقود أو خاطئ جوهريًا أو غير مدعوم أو غير قابل لإعادة الإنتاج. | 0–39% |

## Integrity gates | بوابات النزاهة

A numerical score is not final until the following gates are cleared:

لا تصبح الدرجة نهائية قبل اجتياز البوابات الآتية:

| Gate | Blocking condition | الحالة المانعة |
|---|---|---|
| G1 — Leakage | A prohibited, post-outcome or target-derived feature is used. | استخدام خاصية محظورة أو لاحقة للنتيجة أو مشتقة من الهدف. |
| G2 — Challenge isolation | Challenge labels or hidden evaluator data are used for training or selection. | استخدام تسميات التحدي أو بيانات المقيم المخفية في التدريب أو الاختيار. |
| G3 — Honest policy selection | The final threshold is selected from final evaluation or challenge data. | اختيار العتبة النهائية من بيانات التقييم النهائي أو التحدي. |
| G4 — Reproducibility | The submitted version cannot reproduce the required outputs. | عدم قدرة النسخة المسلّمة على إعادة إنتاج المخرجات المطلوبة. |
| G5 — Hard-coding | Predictions, metrics or evidence are fabricated, copied or hard-coded. | اصطناع التنبؤات أو المقاييس أو الأدلة أو نسخها أو تثبيتها يدويًا. |
| G6 — Version identity | Tag, exact SHA, manifest and submitted files do not identify one version. | عدم تطابق Tag وSHA والـmanifest والملفات على نسخة واحدة. |
| G7 — Recovery disclosure | Example or recovery output is presented as personal execution without disclosure. | تقديم مخرجات المثال أو الاستعادة بوصفها تنفيذًا شخصيًا دون إفصاح. |
| G8 — Privacy/security | Secrets, personal data, private grades, receipts or hidden labels are published. | نشر أسرار أو بيانات شخصية أو درجات أو إيصالات خاصة أو تسميات مخفية. |
| G9 — Ownership | The learner cannot explain a central project decision using repository evidence. | عدم قدرة المتدرب على شرح قرار محوري باستخدام أدلة المستودع. |

## Score calculation rules | قواعد احتساب الدرجة

1. The technical subtotal is capped at 80 points. | مجموع المتطلبات التقنية بحد أقصى 80 درجة.
2. The administrative subtotal is capped at 20 points. | مجموع المتطلبات الإدارية بحد أقصى 20 درجة.
3. The final project score is capped at 100 points. | درجة المشروع النهائية بحد أقصى 100 درجة.
4. The presentation and defence are assessed within the administrative project requirements and do not have a separate score outside the 100 points. | يُقيَّم العرض والمناقشة ضمن المتطلبات الإدارية للمشروع ولا توجد لهما درجة منفصلة خارج الـ100.
5. Attendance is a certificate-eligibility requirement, not a project score. | الحضور شرط لاستحقاق نوع الشهادة وليس درجة من درجات المشروع.
6. A score below 70 remains below the completion threshold after display rounding. | تظل الدرجة الأقل من 70 دون حد الاجتياز بعد التقريب الشكلي.
7. Automated checks provide evidence; they do not award automatic marks or issue a certificate. | تقدم الفحوص الآلية أدلة ولا تمنح درجات آلية أو تصدر شهادة.
