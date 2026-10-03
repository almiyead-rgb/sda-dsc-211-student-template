# Release Freeze Status | حالة تجميد الإصدار

**Target | الهدف:** `v1.1.0`  
**Repository | المستودع:** `almiyead-rgb/sda-dsc-211-student-template`  
**Current state | الحالة الحالية:** `CANDIDATE — NOT RELEASED | مرشح — غير منشور`

## Automated controls | الضوابط الآلية

- [x] Bilingual content validation
- [x] Environment validation
- [x] Reference parity for Days 1–5
- [x] Fresh-kernel notebook smoke test
- [x] Notebook 99 contract and structural validation
- [x] Release-candidate integrity validation
- [x] Deterministic candidate manifest generation

## Manual and private controls | الضوابط اليدوية والخاصة

- [ ] Hosted Colab acceptance completed and signed
- [ ] Visual bilingual rendering reviewed in hosted Colab
- [ ] Private evaluator repository created and tested
- [ ] Hidden evaluation assets generated and access-restricted
- [ ] Private submission registry created and receipt workflow tested
- [ ] Final release notes reviewed
- [ ] Learner and portal candidate manifests cross-checked
- [ ] Final learner-facing content freeze approved
- [ ] Final `release_manifest.json` generated after freeze
- [ ] Coordinated merge and `v1.1.0` publication approved

## Freeze rule | قاعدة التجميد

No merge, tag or public release is authorised while any mandatory item above remains unchecked. The candidate manifest may be refreshed during development; the final manifest is generated only after manual acceptance and private-control testing.

لا يُسمح بالدمج أو إنشاء Tag أو نشر الإصدار ما دام أي بند إلزامي أعلاه غير مكتمل. يجوز تحديث Manifest المرشح أثناء التطوير، أما Manifest النهائي فلا يُنشأ إلا بعد اعتماد Colab واختبار الضوابط الخاصة.
