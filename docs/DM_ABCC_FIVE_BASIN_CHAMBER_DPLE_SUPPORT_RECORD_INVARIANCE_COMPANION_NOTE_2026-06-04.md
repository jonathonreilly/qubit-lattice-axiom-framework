---
claim_id: dm_abcc_five_basin_chamber_dple_support_record_invariance_companion_note_2026-06-04
claim_type_author_hint: meta
---

# DM A-BCC Five-Basin Chamber-DPLE Support Record Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / record-invariance evidence)
**Status:** companion-only. This records that the parent finite
chamber-DPLE arithmetic does not use Record axiom content. It is not a new
theorem claim, not a verdict change, and not independent review work.
**Companion target:** `dm_abcc_five_basin_chamber_dple_support_theorem_note_2026-04-21`
([`DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md`](DM_ABCC_FIVE_BASIN_CHAMBER_DPLE_SUPPORT_THEOREM_NOTE_2026-04-21.md))
**Primary runner:**
[`scripts/audit_companion_dm_abcc_five_basin_record_invariance_2026_06_04.py`](../scripts/audit_companion_dm_abcc_five_basin_record_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_dm_abcc_five_basin_record_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_dm_abcc_five_basin_record_invariance_2026_06_04.txt)

## Claim Boundary

The parent surface is a finite calculation on the explicitly tabulated
five-basin chart. Its load-bearing statement is that the chamber filter keeps
`{Basin 1, Basin 2, Basin X}`, the `F_4` selector keeps `{Basin 1}`, and the
composition `chamber intersection F_4` selects `Basin 1` uniquely.

This companion does not derive the five-basin chart or selector structure, and
it does not change the parent row. Axioms and primitives are premise context
here; they are not verdict-grade support for a bounded row.

The narrow evidence recorded here is:

1. the parent note hash, claim type, dependency list, and runner path match the
   live ledger row;
2. the parent runner exits with `TOTAL: PASS=24 FAIL=0`;
3. the parent load-bearing sections contain the five-basin chamber filter,
   `F_4(Basin 2)` negative-discriminant step, and unique-composition result;
4. the parent load-bearing sections do not use Record axiom content;
5. the parent runner output is unchanged under counterfactual markers where
   Record is asserted or not asserted.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not derive the source chart or selector structure.
- It does not change the parent dependency boundary.
- It does not treat axioms or primitives as bounded-row support.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent finite
chamber-DPLE calculation is record-invariant, while any stronger chain remains
outside this companion.
