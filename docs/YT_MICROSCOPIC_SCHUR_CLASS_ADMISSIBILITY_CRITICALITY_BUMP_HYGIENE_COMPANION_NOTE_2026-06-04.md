---
claim_id: yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_companion_note_2026-06-04
claim_type_author_hint: meta
---

# YT Microscopic Schur-Class Admissibility Criticality-Bump Hygiene Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / criticality-readiness evidence)
**Status:** companion-only. This records that the parent note hash,
dependency wiring, and runner numerics are reproducible on the current tree.
It is not a new theorem claim, not a verdict change, and not independent
audit work.
**Companion target:** `yt_microscopic_schur_class_admissibility_note`
([`YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md`](YT_MICROSCOPIC_SCHUR_CLASS_ADMISSIBILITY_NOTE.md))
**Primary runner:**
[`scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py`](../scripts/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.txt`](../logs/runner-cache/audit_companion_yt_microscopic_schur_class_admissibility_criticality_bump_hygiene_2026_06_04.txt)

## Claim Boundary

The parent remains dependency-pending because its two registered upstream
dependency rows remain unresolved in the ledger. This companion does not remove
or close those dependencies.

The narrow evidence recorded here is:

1. the parent note hash matches the live ledger row;
2. the parent row still declares exactly the two Schur dependency edges named
   by its helper runners;
3. the parent runner exits with `FINAL TALLY: 5 PASS / 0 FAIL`;
4. the runner reproduces the previously cited finite-scale figures:
   576 microscopic operators tested, 576 coarse reductions in class,
   max response gap `5.144895e-03`, and conservative budget
   `1.214751e-02`;
5. the current criticality value is the same value present in the earlier
   positive-verdict snapshot that was later invalidated by a priority bump.

## What This Does Not Claim

- It does not claim a new theorem.
- It does not change the parent or this companion's verdict fields.
- It does not close the two upstream Schur dependency rows.
- It does not certify zero endpoint budget.
- It does not certify unbounded `y_t`.
- It does not cover microscopic realizations outside the tested locality tube.
- It does not edit generated ledger, queue, or publication-status files.

The safe downstream use is only this meta evidence: the parent runner's
finite Schur-class admissibility checks remain reproducible, while the parent
still waits on its two upstream Schur dependencies.
