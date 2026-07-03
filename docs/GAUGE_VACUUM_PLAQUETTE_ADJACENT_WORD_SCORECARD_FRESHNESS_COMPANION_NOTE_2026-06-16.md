# Gauge Vacuum Plaquette Adjacent-Word Scorecard Freshness Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-16
**Type:** meta (post-audit scorecard freshness companion)
**Status:** companion-only. This note does not re-audit, does not edit an
audit verdict, does not promote a row, does not add an axiom, and does
not change the parent theorem statement.

**Companion target:**
[`GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md`](GAUGE_VACUUM_PLAQUETTE_ADJACENT_WORD_CONTRACTION_DERIVED_NARROW_THEOREM_NOTE_2026-06-12.md)

**Primary verifier:**
[`scripts/audit_companion_gauge_vacuum_plaquette_adjacent_word_scorecard_freshness_2026_06_16.py`](../scripts/audit_companion_gauge_vacuum_plaquette_adjacent_word_scorecard_freshness_2026_06_16.py)

**Cached log:**
[`logs/runner-cache/audit_companion_gauge_vacuum_plaquette_adjacent_word_scorecard_freshness_2026_06_16.txt`](../logs/runner-cache/audit_companion_gauge_vacuum_plaquette_adjacent_word_scorecard_freshness_2026_06_16.txt)

---

## Why This Companion Exists

The parent note's verification block displays the historical expected tail

```text
TOTAL: PASS=25, FAIL=0
```

The current parent runner and its SHA-pinned cache instead end with

```text
TOTAL: PASS=28, FAIL=0
```

The three additional passing checks are the reviewer checks in the
parent runner's `Part R` section:

1. derived two-word and three-word trivial-slice readouts agree;
2. the three-word Perron vector is not rank-one across the outer word;
3. the all-trivial-except-word0 slice of the three-word Perron vector is
   proportional to the two-word slice.

Those checks refine the executable support surface without changing the
parent's bounded scope, residual list, numerical readout, or comparator
firewall. A direct one-line edit to the parent note would change the
already-audited parent bytes. This companion leaves the parent note
untouched and records the freshness discrepancy for independent review
handling.

## Non-Claims

This companion makes only a source-hygiene claim:

- it verifies that the parent note still displays `PASS=25, FAIL=0`;
- it verifies that the current parent runner and cache display
  `PASS=28, FAIL=0`;
- it identifies the three extra passing checks as reviewer-check additions;
- it makes no claim that the parent row's status changes;
- it makes no claim about the full spatial Wilson environment,
  rim-boundary `eta`, `L_perp` limit, untruncated convergence, analytic
  plaquette value, or canonical repinning.

Any decision to refresh the parent display, reseed hashes, or revisit the
parent row remains outside this companion.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/audit_companion_gauge_vacuum_plaquette_adjacent_word_scorecard_freshness_2026_06_16.py
```

Expected tail:

```text
TOTAL: PASS=9 FAIL=0
```
