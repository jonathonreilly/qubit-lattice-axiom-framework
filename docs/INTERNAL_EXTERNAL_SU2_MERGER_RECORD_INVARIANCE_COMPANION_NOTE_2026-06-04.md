---
claim_id: internal_external_su2_merger_record_invariance_companion_note_2026-06-04
claim_type_author_hint: meta
---

# Internal-External SU(2) Merger Record Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / record-invariance evidence)
**Status:** companion-only. This records that the parent operator-identification
chain does not use Record axiom content. It is not a new theorem claim, not a
verdict change, and not independent review work.
**Companion target:** `internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27`
([`INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md))
**Primary runner:**
[`scripts/audit_companion_internal_external_su2_merger_record_invariance_2026_06_04.py`](../scripts/audit_companion_internal_external_su2_merger_record_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_internal_external_su2_merger_record_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_internal_external_su2_merger_record_invariance_2026_06_04.txt)

## Claim Boundary

The parent surface identifies the per-site internal `su(2)` spin generators
with the infinitesimal `Spin(3)` generators arising from the Clifford universal
property, on the repo-baseline one-qubit operator algebra. Its load-bearing
content is exact Pauli/Clifford/Lie algebra on `H_x = C^2`, together with
proper cubic spin lifts and improper signed Clifford-generator actions.

This companion does not add an axiom, primitive, regulator reading, lattice
translation result, physical scale, or numerical lane. It does not change the
parent row. Axioms and primitives are premise context here; they are not
verdict-grade support for a bounded row.

The narrow evidence recorded here is:

1. the parent note hash, claim type, dependency list, and runner path match the
   live ledger row;
2. the parent runner exits with `TOTAL: PASS=273 FAIL=0`;
3. the parent load-bearing sections contain the Pauli, bivector, `su(2)`,
   `Spin(3)`, cubic-lift, and signed-action operator identities;
4. the parent load-bearing sections do not use Record axiom content;
5. the parent runner output is unchanged under counterfactual markers where
   Record is asserted or not asserted.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not derive lattice discreteness, translation primitives, cubic
  Bravais structure, or a physical scale.
- It does not introduce a Coleman-Mandula or Haag-Lopuszanski-Sohnius claim.
- It does not treat axioms or primitives as bounded-row support.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent
operator-identification chain is record-invariant, while all nonlocal,
translation, scale, and numerical-lane uses remain outside this companion.
