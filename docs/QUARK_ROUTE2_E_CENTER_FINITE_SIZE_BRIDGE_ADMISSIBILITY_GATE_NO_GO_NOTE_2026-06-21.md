# Route-2 E-Center Finite-Size Bridge Admissibility Gate No-Go Note

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no-go for retiring the Route-2 E-center endpoint triple from the
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go for retiring the Route-2 E-center endpoint triple from the
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_e_center_finite_size_bridge_gate_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_e_center_finite_size_bridge_gate_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_e_center_finite_size_bridge_gate_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_e_center_finite_size_bridge_gate_no_go_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md), [QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md), [S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md), [S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md](S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md)

current finite-size bridge evidence.

## Scope

The parent S3/Route-2 row remains blocked by the missing readout endpoint
triple:

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
  = (-1, -2, 21/4).
```

After the T-side entries are supplied, the live missing entry is equivalently:

```text
rho_E = 21/4
q_E = 15/8
c_TE = -8/9.
```

This note tests the finite-size rescue route:

```text
N=15 measured E-center calibration + finite-size bridge
  -> exact q_E = 15/8.
```

The parent row remains open, and this note does not reject future nonblind
source/readout routes.  It only states what the current finite-size evidence
can and cannot do.

## Inputs

The current surface already has three relevant facts.

1. The measured-calibration note says the `N=15` stack value is close to the
   target but explicitly names a box-size scan as the needed discriminator.
2. The box-size scan reconstructs the landed observable at `N=15` and shows
   that the two named schedules miss the target:
   - fixed physical probe radius: post-`N=15` `q_E(N)` runs negative;
   - box-proportional radius: the tail goes toward `(q_E, q_T) = (1, 1)`,
     not `(15/8, 5/6)`.
3. A first-principles radius-window probe, using the same box-size scan
   evaluator, sampled broad interior radius windows:
   - `N=17`, radii `2.00` through `7.20`;
   - `N=19`, radii `2.00` through `8.00`.

In those sampled windows, `q_E` never reaches `15/8`.  The largest sampled
values are about `1.0265` for `N=17` and `1.1437` for `N=19`, still below the
target.

## Gate

The finite-size route now has a precise admissibility gate.

| Candidate bridge | Current status | Reason |
|---|---|---|
| single `N=15` exactification | no-go | one box does not identify an infinite-volume endpoint |
| fixed-radius same-functional limit | no-go | the existing scan misses `15/8` after `N=15` |
| box-proportional same-functional limit | no-go | the existing scan tends toward `(1, 1)`, not target |
| sampled untuned radius-window rescue | no-go in sampled windows | `N=17` and `N=19` broad windows do not cross `15/8` |
| post-hoc radius schedule | open only with new import | a schedule chosen to hit the target is a selector, not a derivation |
| changed normalization or probe | open only as new functional | changing the observable is not a finite-size limit of the landed one |
| independent source/readout primitive | open positive route | this is still the direct way to retire the endpoint triple |

## Claim Status

Actual current surface status: `no-go` for current finite-size bridge
retirement of the endpoint triple.

Trace class: `negative_route_pruning`.

Reachability: prunes finite-size exactification from the current
same-functional evidence.  The parent row remains open:
`s3_time_theta_to_slice_coupling_note`.

## Future Positive Route

A future finite-size PR could still move the endpoint if it supplies one of:

- a predeclared schedule theorem that selects a radius/normalization family
  before comparing to `15/8`;
- a selector theorem explaining why the `N=15` numerator excursion is
  structurally distinguished;
- an independent nonblind source/readout primitive that derives
  `rho_E = 21/4` without using finite-size target matching.

Without one of those inputs, finite-size evidence remains support or route
pruning, not endpoint derivation.

## Runner Certificate

Expected local certificate:

```text
TOTAL: PASS=32 FAIL=0
```
