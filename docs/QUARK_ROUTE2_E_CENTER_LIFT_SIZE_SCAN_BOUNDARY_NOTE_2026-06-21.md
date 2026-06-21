# Route-2 E-Center Lift Size-Scan Boundary: the 15^3 Calibration Replay Is Real, but the Current Finite-Box Family Does Not Certify Convergence

**Date:** 2026-06-21
**Claim type:** bounded-support / narrow negative route pruning
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the naive finite-box extrapolation route for the open `rho_E = 21/4` endpoint, without closing the endpoint theorem.
**Status authority:** branch-local physics-loop artifact only. This note writes no audit verdict, retags no ledger row, and does not update repo-wide authority surfaces.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_lift_size_scan_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_e_center_lift_size_scan_boundary_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_e_center_lift_size_scan_boundary_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_e_center_lift_size_scan_boundary_2026_06_21.txt)

## Target Boundary

The June 10 measured-calibration note relocated the open Route-2 E-channel pin from a structureless free parameter to a concrete stack functional:

```text
q_E = gamma_E(center) / gamma_E(shell), measured on the Lambda_R shell-response endpoint family.
```

At `SIZE=15`, the landed center-excess cache gives `q_E = 1.876246130347`, within finite-box tolerance of the target `15/8`, and the exact endpoint algebra says

```text
rho_E = 21/4 <=> q_E = 15/8 <=> q_E = (9/4) q_T <=> center T/E = -8/9.
```

The load-bearing caveat in that note was the missing discriminator: a box-size scan of `q_E(N)` after parameterizing the `SIZE=15`-pinned module chain.

## What This Block Adds

The runner performs the first executable size-parameterized replay of that chain.

It leaves the upstream modules untouched, but locally patches the tensor Schur action to infer its size from `phi_grid.shape[0]` instead of always constructing the `15^3` Schur map. The same source family, tensor metric, and reduced-shell normalization are then replayed at odd sizes:

| size | status | `q_T` | `q_E` | `rho_E` | shell `T/E` | center `T/E` |
|---:|---|---:|---:|---:|---:|---:|
| 9 | boundary | reduced-shell anchor unavailable |  |  |  |  |
| 11 | computed | `+0.902060859652` | `+0.846134199720` | `-0.923194801679` | `+2.203976484535` | `+2.349652009045` |
| 13 | computed | `+0.870086497080` | `-0.038869990679` | `-6.233219944075` | `+5.382863503774` | `-120.492872996108` |
| 15 | computed | `+0.833328197623` | `+1.876246130347` | `+5.257476782081` | `-2.005382749600` | `-0.890683778231` |
| 17 | computed | `-0.196795039281` | `-5.836999720859` | `-41.021998325154` | `+3.921154955292` | `+0.132202138146` |

The `15^3` row reproduces the landed calibration cache to floating precision. That is a positive reproducibility check, not the problem.

The problem is that the neighboring executable boxes do not lie near the target chain and do not form a monotone convergence certificate. In particular, sizes 11, 13, and 17 are outside a broad target envelope; sizes 13 and 17 flip the sign of `q_E`; and sizes 11, 13, and 17 have shell `T/E` with the wrong sign relative to the `-2` endpoint.

Therefore the `15^3` match cannot be cited as finite-size convergence evidence under the current parameterization.

## Narrow Interpretation

This block is a no-go only for the naive route:

```text
15^3 measured match -> therefore q_E(N) is converging to 15/8.
```

It does not refute a future size-stable/infinite-volume theorem. The checked boxes are small, the reduced-shell anchor itself has a threshold, and the current replay changes several finite-box semantics at once: Schur trace map, shell orbit geometry, tensor interpolation, and support Green columns. A future theorem could still define a different size-stable family and prove `q_E(N) -> 15/8`.

The honest blocker is sharper now: before the June 10 calibration can support the `rho_E = 21/4` endpoint theorem, the route needs a size-stable parameterization/continuum family whose finite-box values do not make the `15^3` row look isolated.

## Exact Algebra That Remains Available

The endpoint arithmetic is still exact support:

```text
rho_T = -1
q_T = 1 + rho_T/6 = 5/6
q_E = 15/8
q_E/q_T = 9/4
shell T/E = -2
center T/E = (shell T/E) q_T/q_E = -8/9
rho_E = 6(q_E - 1) = 21/4
```

This block only says the current finite-box replay does not derive the needed `q_E = 15/8` limit.

## Forbidden-Imports Check

No observed masses, fitted targets, or PDG values are consumed. The target rationals appear only as the open endpoint comparator already named by the Route-2 readout notes. The numerical rows are stack-internal replay outputs from the same source/tensor/shell modules used by the landed calibration.

## Net

The next science target should not be another claim that the `15^3` row is close. It should be one of:

1. define a size-stable Schur/shell/tensor family and rerun the extrapolation there;
2. derive `q_E = 15/8` by a non-finite-box covariance bridge independent of this replay; or
3. prove that the current finite-box source family has an intrinsic boundary/anchor transition that explains why `N=15` is special.
