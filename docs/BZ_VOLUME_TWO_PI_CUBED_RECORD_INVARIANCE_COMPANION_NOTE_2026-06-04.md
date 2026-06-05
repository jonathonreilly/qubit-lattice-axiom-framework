---
claim_id: bz_volume_two_pi_cubed_record_invariance_companion_note_2026-06-04
claim_type_author_hint: meta
---

# BZ Volume Two-Pi-Cubed Record Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / record-invariance evidence)
**Status:** companion-only. This records that the parent BZ-volume theorem's
load-bearing arithmetic uses only lattice/Pontryagin/Haar content and is
unchanged by the repo's Record axiom adoption. It is not a new theorem claim,
not a verdict change, and not independent audit work.
**Companion target:** `bz_volume_two_pi_cubed_substrate_internal_narrow_theorem_note_2026-05-26`
([`BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md`](BZ_VOLUME_TWO_PI_CUBED_SUBSTRATE_INTERNAL_NARROW_THEOREM_NOTE_2026-05-26.md))
**Primary runner:**
[`scripts/audit_companion_bz_volume_two_pi_cubed_record_invariance_2026_06_04.py`](../scripts/audit_companion_bz_volume_two_pi_cubed_record_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_bz_volume_two_pi_cubed_record_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_bz_volume_two_pi_cubed_record_invariance_2026_06_04.txt)

## Claim Boundary

The parent remains dependency-pending after the minimal-axiom premise update.
This companion does not remove or close that dependency. Axioms and primitives
are premise context here; they are not verdict-grade support for a bounded row.

The narrow evidence recorded here is:

1. the parent note hash and runner path match the live ledger row;
2. the parent runner exits with `TOTAL : PASS = 55, FAIL = 0`;
3. the parent load-bearing sections contain the lattice, Pontryagin-dual, and
   Haar-measure ingredients;
4. the parent load-bearing sections do not use Record axiom content;
5. direct arithmetic reproduces `vol([-pi, pi]^3) = (2*pi)^3` and Haar density
   `1/(2*pi)^3`;
6. the same arithmetic is unchanged under a counterfactual marker where Record
   is asserted or not asserted.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not treat `minimal_axioms` as bounded-row support.
- It does not close the parent after the premise update.
- It does not close any four-dimensional loop-measure or hierarchy factor.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent BZ-volume
arithmetic is record-invariant, while the parent still waits on independent
review under the current premise set.
