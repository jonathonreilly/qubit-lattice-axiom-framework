# d=3 Even-d2 Truncation Protection Coincides With the Chart-Period Commensuration Criterion on the Tested Step-2 Grid L = {8,10,12,14,16,18} (Out-of-Sample L=16/18 Confirmed; Bounded)

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Primary runner:** `scripts/frontier_d3_commensuration_criterion_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_d3_commensuration_criterion_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=18 FAIL=0`.
**Status authority:** independent audit lane. This source note does not set or predict an audit outcome and does not edit audit-owned registry, ledger, queue, or publication-status surfaces.

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency. The independent audit lane owns status.

## Claim

For the synthetic step-2 chart family used in the d=3 range runner, **on the
tested grid `L = {8, 10, 12, 14, 16, 18}`** the next-checkerboard protection
after even-`d2` truncation holds exactly when every second-chart period is even
(no claim beyond this grid or this chart family).  The second chart has periods

```text
K_periods = (L/2, L, L/2),
```

so on the tested grid this is the same as `L = 0 mod 4`.

The runner checks the criterion two ways:

1. A structural finite check over every kept/decimated pair in the `K` chart
   verifies that minimal-vector `d2` parity matches chart parity exactly for
   `L = 8, 12, 16`, and fails for `L = 10, 14, 18`.
2. The full step-2 Schur machinery then verifies that this structural
   correspondence is equivalent, on the grid, to
   `H_kd_after < 1e-14` after even-`d2` truncation.

The iff is established on the tested grid `L = {8, 10, 12, 14, 16, 18}` for this
chart family `(L/2, L, L/2)`; no claim is made beyond the grid or the family.

## Gates

The opening gates reproduce the landed wave-8 dichotomy before adding new
out-of-sample cases:

- `L = 8, 12`: protected at `1e-14`.
- `L = 10`: failure magnitude anchored at `0.748 +/- 0.01`.
- `L = 14`: failure magnitude anchored at `0.747 +/- 0.01`.
- Before truncation, the next-checkerboard `H_kd` is nonzero at every
  `L = 8, 10, 12, 14, 16, 18` as an anti-fabrication gate.

The new prediction gates are:

- `L = 16`, periods `(8, 16, 8)`: all periods even, so protection must hold at
  `1e-14`; measured `H_kd_after = 0`.
- `L = 18`, periods `(9, 18, 9)`: odd components remain, so protection must
  fail above `0.1`; measured `H_kd_after = 0.7472858924365249`.

The runner prints the full dichotomy table for
`L = 8, 10, 12, 14, 16, 18` and exits nonzero on any failed gate.

## Scope

This is a finite-dimensional bounded check for this chart family and this grid.
It does not claim a theorem for all possible chart choices, an RG flow, a
continuum statement, or an audit result.  The audit lane grades.

## Dependencies

- [`D3_STEP2_RANGE_GROWTH_PERIOD_CLASS_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-12.md`](D3_STEP2_RANGE_GROWTH_PERIOD_CLASS_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  -- the step-2 Schur machinery, synthetic chart family, and landed `L = 8,10,12,14`
  period-class dichotomy that this note extends on the tested grid.
- [`D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md`](D3_CHECKERBOARD_STEP1_CLOSED_FORM_PARITY_LEMMA_BOUNDED_THEOREM_NOTE_2026-06-12.md)
  -- the step-1 closed form and parity lemma used as the structural anchor.
