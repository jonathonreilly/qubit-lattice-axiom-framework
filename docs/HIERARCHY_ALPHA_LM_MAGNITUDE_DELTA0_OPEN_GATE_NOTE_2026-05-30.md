# Hierarchy Alpha_LM Magnitude Delta-Zero Open Gate

**Date:** 2026-05-30
**Claim type:** open_gate
**Status:** source note; downstream status is decided by independent review.
**Primary runner:** [`scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py`](../scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py)

## Result

This note isolates the magnitude content in the hierarchy substitution

```text
alpha_LM = alpha_bare / u_0,
alpha_LM^16 = alpha_bare^16 * u_0^-16.
```

The runner verifies three local facts.

1. With `g_bare = 1`, `alpha_bare = 1/(4 pi)`, so
   `alpha_bare^16 = (4 pi)^-16 = 2.586e-18`.
2. The exact Matsubara determinant and condensate-density forms checked here
   contain `u_0` but no explicit `alpha_bare`.
3. The triplet
   `alpha_bare`, `alpha_LM = alpha_bare/u_0`,
   `alpha_s = alpha_bare/u_0^2` is a constant-ratio geometric progression.
   In the corresponding `1/alpha` variables the equal-step test gives
   `Delta_2 / Delta_1 = u_0`, not `1`.

Thus the checked block observables do not by themselves supply the
`(4 pi)^-16` coupling-power magnitude.  A transport interpretation of that
constant-ratio progression remains an open gate on the current `delta = 0`
lattice baseline; the finite algebra here records the obstruction surface but
does not close the hierarchy formula.

## Boundary

This note does not derive `v`, does not close the hierarchy lane, and does not
approve a new axiom, primitive, or Tier-A admission.  It also does not claim
that every possible future mechanism is closed.

The exact boundary is narrower:

```text
block determinant / condensate forms checked here: u_0-only;
alpha_LM magnitude factor: carries alpha_bare^16 by algebraic relabeling;
transport source for that coupling-power magnitude on the current baseline:
open.
```

A future source could close this gate by deriving an explicit `alpha_bare`
dependence inside the relevant block observable, or by deriving a baseline-native
transport rule that supplies the same constant-ratio coupling-power magnitude.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: hierarchy alpha_LM magnitude delta-zero open-gate checks pass.
```
