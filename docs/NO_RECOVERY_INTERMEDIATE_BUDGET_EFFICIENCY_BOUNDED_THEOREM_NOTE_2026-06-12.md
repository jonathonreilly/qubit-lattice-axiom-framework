# No Recovery: Blanks Are Monotonically Consumed While the Branch-Relational Record Functional Decays, the Budget Bound Holds at Every Intermediate Time, and the Record-Functional Efficiency η(ε) Falls on the Probed Grid (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (composes the branching-ledger and erosion threads, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_no_recovery_efficiency_table_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_no_recovery_efficiency_table_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=17 FAIL=0` — exact trees, broadcast + erosion phases.

## Dependency Boundary

This packet composes the finite branch-budget model from
[`BRANCHING_RECORD_BUDGET_INEQUALITY_BOUNDED_THEOREM_NOTE_2026-06-12.md`](BRANCHING_RECORD_BUDGET_INEQUALITY_BOUNDED_THEOREM_NOTE_2026-06-12.md)
with the branch-functional erosion model from
[`RECORD_EROSION_BRANCH_VS_ENSEMBLE_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md`](RECORD_EROSION_BRANCH_VS_ENSEMBLE_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-06-12.md).
The runner independently reproduces the finite transition rules, probability
normalization, blank-consumption ledger, and erosion table used here.

The eroding object is the branch-state connected-correlator record functional,
not the Record axiom's durable registration of a realized outcome. No durable
record is claimed to unform, change, or re-register.

## Findings

- **No recovery — a theorem by construction, stated as such**: in this model no
  transition maps any register back to blank (broadcasts consume blanks; the
  erosion step moves record labels into the model's erased label), so the
  Born-weighted blank count is monotone non-increasing by structure — the gate
  (`10⁻¹²`, every probed `ε`) verifies the implementation, not a discovered
  dynamical effect.
- **The budget bound holds at every intermediate time**: `R(t) ≤ C(t)` (records ≤
  cumulative blanks consumed) along the whole tracked trajectory, every probed `ε`.
- **The efficiency table**: `η(ε) = R_final/C_final` **decreases with `ε` on the
  probed grid** (gated; threshold-probed at `0.3/0.5/0.7` with the fixed monotone
  direction) — stronger measurement wastes consumed blanks in this finite model.
  Endpoints exact: `ε = 0` gives `η = 1` (every consumed blank holds a
  branch-functional record); the `|0⟩`-pointer gives `η = 0`.

## Scope

This model, exact; the no-recovery monotonicity, intermediate-time budget, and
efficiency table are the data. Probability normalization is checked in-runner;
any broader Born-chain authority is inherited through the linked finite
branch-budget packets and is not re-graded here. No new axiom/primitive/measure/
weight; `r` untouched. The audit lane grades.
