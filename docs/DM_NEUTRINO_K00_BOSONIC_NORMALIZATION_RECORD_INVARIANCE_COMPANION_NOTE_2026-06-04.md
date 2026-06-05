---
claim_id: dm_neutrino_k00_bosonic_normalization_record_invariance_companion_note_2026-06-04
claim_type_author_hint: meta
---

# DM Neutrino K00 Bosonic Normalization Record Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / record-invariance evidence)
**Status:** companion-only. This records that the parent finite matrix
calculation and source-response comparison do not use Record axiom content. It
is not a new theorem claim, not a verdict change, and not independent review
work.
**Companion target:** `dm_neutrino_k00_bosonic_normalization_theorem_note_2026-04-15`
([`DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md`](DM_NEUTRINO_K00_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md))
**Primary runner:**
[`scripts/audit_companion_dm_neutrino_k00_bosonic_normalization_record_invariance_2026_06_04.py`](../scripts/audit_companion_dm_neutrino_k00_bosonic_normalization_record_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_neutrino_k00_bosonic_normalization_record_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_neutrino_k00_bosonic_normalization_record_invariance_2026_06_04.txt)

## Claim Boundary

The parent surface is a conditional heavy-neutrino diagonal-normalization
packet. Its runner-checked algebra fixes the Frobenius-dual generator
`F00 = J3/3`, checks that it is isospectral to `(1/2) J2`, verifies identical
finite bosonic response on scalar baselines, and then carries the imported
source-amplitude branch through `tau_+ = 1` to `K00 = 2`.

This companion does not derive the observable-principle premise, the
source-amplitude premise, or the endpoint value as a baseline-framework result.
It does not change the parent row. Axioms and primitives are premise context
here; they are not verdict-grade support for a bounded row.

The narrow evidence recorded here is:

1. the parent note hash, claim type, dependency list, and runner path match the
   live ledger row;
2. the parent runner exits with `SUMMARY: PASS=11 FAIL=0`;
3. the parent load-bearing sections contain the `K00` target formula, the
   `F00 = J3/3` projector identity, the `(1/2) J2` source comparison, the
   identical bosonic response statement, and the `tau_E = tau_T = 1/2`
   arithmetic;
4. the parent load-bearing sections do not use Record axiom content;
5. the parent runner output is unchanged under counterfactual markers where
   Record is asserted or not asserted.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not derive the observable-principle premise.
- It does not derive the source-amplitude premise.
- It does not change the parent dependency boundary.
- It does not treat axioms or primitives as bounded-row support.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent finite
projector, isospectrality, response, and arithmetic checks are
record-invariant, while any stronger chain remains outside this companion.
