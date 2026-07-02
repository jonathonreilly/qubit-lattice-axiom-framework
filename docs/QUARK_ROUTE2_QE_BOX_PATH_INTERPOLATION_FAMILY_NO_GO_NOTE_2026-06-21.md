# Route-2 q_E Box-Path Interpolation Family: the N=15 Lift Does Not Persist on the Sampled Radius-Scaling Paths

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** bounded support / negative route-pruning note
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**actual_current_surface_status:** bounded-support
**trace_class:** negative_route_pruning
**reachability_to_target:** prunes
**Primary runner:** [`scripts/frontier_quark_route2_qe_box_path_interpolation_family_no_go_2026_06_21.py`](../scripts/frontier_quark_route2_qe_box_path_interpolation_family_no_go_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_qe_box_path_interpolation_family_no_go_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_qe_box_path_interpolation_family_no_go_2026_06_21.txt)

## Target

The active S3/Route-2 gate reduces the remaining readout obstruction to

```text
(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4).
```

After granting the two T-side candidates, the missing E-side entry is

```text
rho_E := beta_E/alpha_E = 21/4,
q_E = 1 + rho_E/6 = 15/8.
```

The current restricted carrier/readout class leaves `rho_E` free unless an additional E-center endpoint ratio, source-domain rule, or stronger readout-map primitive is supplied. The measured-calibration note found that the landed `N=15` stack nearly realizes `q_E=15/8`; the June 10 box-size scan then showed the two endpoint boundary paths fail: fixed radius runs negative, while box-proportional radius tends toward `(q_T,q_E) ~= (1,1)`.

This note tests the natural interpolation rescue between those endpoints.

## Tested Family

The runner reuses the landed June 10 `q_E` box-size machinery verbatim and scans the finite rational exponent grid

```text
r_N(p) = 4.25 * ((N - 2)/13)^p,
p in {0, 1/4, 1/2, 3/4, 1},
N in {17, 21, 25}.
```

All paths pass through the same `N=15` radius because `((15 - 2)/13)^p = 1`, so the family preserves the measured-calibration coincidence at the common origin. The question is whether any sampled path carries that coincidence toward a stable larger-box value.

The target values `15/8` and `5/6` are comparators only, not proof inputs or fitting objectives.

## Result

The runner first reproduces the common `N=15` origin:

| quantity | value | comparator | gap |
|---|---:|---:|---:|
| `q_E(N=15)` | `+1.876246130` | `15/8 = +1.875000000` | `0.001246` |
| `q_T(N=15)` | `+0.833328198` | `5/6 = +0.833333333` | `0.000005` |

Then the interpolation grid gives:

| `p` | `q_E(N=17)` | `q_E(N=21)` | `q_E(N=25)` | `N=25` gap to `15/8` |
|---:|---:|---:|---:|---:|
| `0` | `-5.837000` | `-8.674606` | `-10.377200` | `12.252200` |
| `1/4` | `+9.596912` | `-21.994552` | `+6.570619` | `4.695619` |
| `1/2` | `+0.987795` | `+0.873746` | `+0.080591` | `1.794409` |
| `3/4` | `+1.106491` | `+0.878940` | `+0.929144` | `0.945856` |
| `1` | `+2.708438` | `+1.054009` | `+0.981191` | `0.893809` |

No sampled path tracks `15/8` across the larger boxes, and no sampled path lands near `15/8` at the largest sampled box. The best largest-box sample is the proportional endpoint `p=1`, with `q_E(N=25)=0.981191`, still `0.893809` away from `15/8`.

The mechanism is also not a new stable source primitive. The non-fixed interpolants inherit `beta_E(shell)` sign or near-zero sensitivity:

| `p` | `beta_E(shell)` signs over `N=17,21,25` | minimum absolute shell denominator |
|---:|---|---:|
| `1/4` | `-, +, -` | `9.56e-07` |
| `1/2` | `-, +, +` | `1.12e-05` |
| `3/4` | `-, +, -` | `1.48e-06` |
| `1` | `-, -, +` | `3.58e-07` |

So the interpolation family carries the same denominator sensitivity exposed by the box-size scan rather than an E-center source-domain rule.

## What This Prunes

This prunes the finite box-path interpolation rescue:

```text
N=15 measured q_E ~= 15/8
  + smooth radius scaling between fixed and proportional boxes
  => stable large-box q_E = 15/8.
```

Within the tested rational exponent grid, that implication fails. The `N=15` agreement is a common-origin finite-box fact, not a stable readout primitive along these paths.

## Boundaries

This is not a derivation of `beta_E/alpha_E = 21/4`.

This is not a no-go theorem for every possible radius path, every new observable, or every source-domain/readout-map primitive. A genuinely new primitive that changes the observable or supplies an independent E-center selector remains outside this packet.

This does not weaken the exact Route-2 carrier/readout reductions already in hand. It only removes one way the measured `N=15` calibration might have been promoted into the missing E-side entry.

## Load-Bearing Inputs

- [[`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md)](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) - the active open gate and the reduced endpoint triple.
- [[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) - the exact restricted carrier/readout reduction and missing-map obstruction.
- [[`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) - the boundary that the restricted class leaves `rho_E` free.
- [[`QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md)](QUARK_ROUTE2_E_CENTER_LIFT_MEASURED_CALIBRATION_NARROW_THEOREM_NOTE_2026-06-10.md) - the `N=15` measured-calibration coincidence this packet tries to stress.
- [[`QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md) - the endpoint path failures this packet extends to a bounded interpolation grid.

## Forbidden-Imports Check

No observed quark masses, fitted Yukawa values, CKM targets, PDG values, or nearest-rational selectors are used. The only numerical objects are the stack's own box Green's functions, metric/Ricci readout functions already used by the June 10 scan, exact rational exponent choices, and comparator values named by the open Route-2 gate.

## Next Exact Target

The remaining positive route is not another smooth rescue of the `N=15` box path. It is a direct E-center selector: a source-domain rule, a non-invariant typed readout primitive, or a stronger readout-map theorem that evaluates the E-center column rather than leaving `rho_E` free.
