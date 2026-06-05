---
claim_id: tensor_product_translation_fermion_operator_bridge_record_invariance_companion_note_2026-06-04
claim_type_author_hint: meta
---

# Tensor-Product Translation Fermion Operator Bridge Record Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / record-invariance evidence)
**Status:** companion-only. This records that the parent finite tensor-product
translation and fermion-operator checks do not use Record axiom content. It is
not a new theorem claim, not a verdict change, and not independent review work.
**Companion target:** `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
([`TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md`](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md))
**Primary runner:**
[`scripts/audit_companion_tensor_product_translation_fermion_operator_bridge_record_invariance_2026_06_04.py`](../scripts/audit_companion_tensor_product_translation_fermion_operator_bridge_record_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_tensor_product_translation_fermion_operator_bridge_record_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_tensor_product_translation_fermion_operator_bridge_record_invariance_2026_06_04.txt)

## Claim Boundary

The parent surface is a finite tensor-product operator bridge. Its
load-bearing content is the construction of the finite tensor-product space
`H_Lambda`, the per-site ladder operators, the tensor-permutation translation
unitary `T_a`, and the four identities: unitarity, group law,
fermion-operator covariance, and charge conservation for `Q_total`.

This companion does not derive a Jordan-Wigner construction, a Noether current,
translation invariance of a Hamiltonian, or a physical observable claim. It
does not change the parent row. Axioms and primitives are premise context here;
they are not verdict-grade support for the row's status.

The narrow evidence recorded here is:

1. the parent note hash, claim type, dependency list, and runner path match the
   live ledger row;
2. the parent runner exits with `PASS=131 FAIL=0`;
3. the parent load-bearing sections contain the tensor-product space,
   single-mode operators, translation unitary, `Q_total`, and identities
   (T1)-(T4);
4. the parent load-bearing sections do not use Record axiom content;
5. the parent runner output is unchanged under counterfactual markers where
   Record is asserted or not asserted.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not derive cross-site anticommutation.
- It does not derive a Noether current.
- It does not derive translation invariance of a Hamiltonian.
- It does not change the parent dependency boundary.
- It does not treat axioms or primitives as verdict-grade support.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent exact symbolic
operator bridge is record-invariant, while any stronger chain remains outside
this companion.
