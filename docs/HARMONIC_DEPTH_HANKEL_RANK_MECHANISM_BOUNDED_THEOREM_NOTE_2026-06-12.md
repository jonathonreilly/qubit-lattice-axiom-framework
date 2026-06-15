# The Harmonic-Depth Mechanism Located in Numerical Trajectory Rank (Window/Threshold-Relative): Censored Lower Bounds at Window 64, K=6 Smallest at Windows 64/128, Coupled-Gap Counts Identical (Bounded)

**Date:** 2026-06-12
**Type:** bounded_theorem (the mechanism follow-on of the state-dependent-depth note, in review — cross-referenced, not graded)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_harmonic_depth_hankel_rank_2026_06_12.py`
**Cache:** `logs/runner-cache/frontier_harmonic_depth_hankel_rank_2026_06_12.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=19 FAIL=0` - anchors reproduced first (the landed ceilings and the K=6 saturation).

## Findings

- **The numerical trajectory rank (window/threshold-relative) tracks the depth**:
  default-threshold ranks are window-64 `{K=3: >=64, K=4: >=64, K=5: 34, K=6: 28}`
  and window-128 `{K=3: 71, K=4: 84, K=5: 36, K=6: 35}`; rank `>= window` is
  censored and reported as a lower bound. The shallow `K = 6` state has the
  **smallest uncensored** rank at both windows; `K = 3/4` are censored-or-larger
  relative to `K = 6` (fixed gates; capture-at-order-4 cross-check `0.995` vs
  `0.898/0.778`; threshold sensitivity `1e-5/1e-6/1e-7` keeps K=6 smallest).
- **Identical coupled-gap counts cannot explain the ordering (3 each, gated)**:
  the number of distinct site-`0/1`-coupled spectral gaps is **identical across
  states** (3 each, weight-floor gated). It does **not** explain the rank ordering.
  The remaining mechanism target is the *distribution* of coupling weight over
  tones (the named follow-on), not the tone inventory.

## Scope

Exact, `L = 3`, the rank-admissible domain; per-state tables are realized-state data;
the gated relations are the claims. No new axiom/primitive/measure/weight; `r`
untouched. The audit lane grades.
