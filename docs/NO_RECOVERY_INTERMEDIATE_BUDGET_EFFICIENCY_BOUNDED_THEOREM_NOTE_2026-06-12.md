# No Recovery: Blanks Are Monotonically Consumed Even as Records Die, the Budget Bound Holds at Every Intermediate Time, and the Record Efficiency η(ε) Falls With Measurement Strength (Bounded)

**Date:** 2026-06-12
**Type:** bounded theorem (composes the branching-ledger and erosion threads, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_no_recovery_efficiency_table_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_no_recovery_efficiency_table_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=17 FAIL=0` — exact trees, broadcast + erosion phases.

## Findings

- **No recovery — a theorem by construction, stated as such**: in this model no
  transition maps any register back to blank (broadcasts consume; erosion erases),
  so the Born-weighted blank count is monotone non-increasing by structure — the
  gate (`10⁻¹²`, every `ε`) verifies the implementation, not a discovered dynamical
  effect.
- **The budget bound holds at every intermediate time**: `R(t) ≤ C(t)` (records ≤
  cumulative blanks consumed) along the whole trajectory, all `ε`.
- **The efficiency table**: `η(ε) = R_final/C_final` **decreases with ε** (gated;
  threshold-probed at `0.3/0.5/0.7` with the fixed monotone direction) — stronger
  measurement wastes consumed blanks. Endpoints exact: `ε = 0` gives `η = 1`
  (every consumed blank holds a record); the `|0⟩`-pointer gives `η = 0`.

## Scope

This model, exact; the no-recovery monotonicity, intermediate-time budget, and
efficiency table are the data; Born cap inherited. No new axiom/primitive/measure/
weight; `r` untouched. The audit lane grades.
