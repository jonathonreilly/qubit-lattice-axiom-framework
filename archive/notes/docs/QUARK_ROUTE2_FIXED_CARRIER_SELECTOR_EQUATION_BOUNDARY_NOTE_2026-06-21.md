# Quark Route-2 Fixed-Carrier Selector Equation Boundary

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / negative route pruning; no endpoint closure
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_fixed_carrier_selector_equation_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_fixed_carrier_selector_equation_boundary_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_fixed_carrier_selector_equation_boundary_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_fixed_carrier_selector_equation_boundary_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md), [QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md), [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

## Scope

This block attacks the fixed-carrier E-center selector residual exposed by the
Route-2 readout stack. It works after the standard conditional T-side values

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2
```

are granted as stretch premises. The remaining target is

```text
rho_E := beta_E / alpha_E = 21/4,
q_E := gamma_E(center) / gamma_E(shell) = 15/8,
c_TE := gamma_T(center) / gamma_E(center) = -8/9.
```

The goal is not to audit those premises and not to land the endpoint triple.
The goal is to test whether first-principles fixed-carrier selector equations
on the already available shell/center source vectors can select the E-center
value without importing an equivalent center/source primitive.

## Authority Inputs

- [[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the exact restricted carrier columns and missing-map obstruction.
- [[QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)
  supplies the conditional time-coupling context.
- [[S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  names the inherited unique-coupling blocker.
- [[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
  supplies the minimal-naturality boundary and target equivalences.
- [[QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)
  supplies the E-center-blindness boundary.
- [[QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md)](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md)
  supplies the named source-domain bridge target.
- [[MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)](MINIMAL_AXIOMS_2026-06-05.md)
  supplies the Record/Quantum non-supply boundary for readout context,
  weighting, metrics, and source primitives.

## Minimal Fixed-Carrier Data

Normalize `alpha_E = 1`. With the granted T-side values, the fixed carrier
gives the two source vectors

```text
S = (gamma_E(shell), gamma_T(shell)) = (1, -2),
C(q_E) = (gamma_E(center), gamma_T(center)) = (q_E, -5/3).
```

The E-center entry is the only remaining variable:

```text
q_E = 1 + rho_E/6.
```

The target is therefore the single point

```text
q_E = 15/8
```

on this affine line.

## Selector Equation Fan-Out

The runner checks exact fixed-carrier equations that a first-principles source
selector might plausibly try before adding a new center/source primitive:

| Selector frame | Equation | Selected `q_E` | Selected `rho_E` |
|---|---:|---:|---:|
| no E-center lift | `q_E = 1` | `1` | `0` |
| same T/E slope / collinearity | `C_T/C_E = S_T/S_E` | `5/6` | `-1` |
| product conservation | `C_E C_T = S_E S_T` | `6/5` | `6/5` |
| positive linear source conservation | `a C_E + b C_T = a S_E + b S_T`, `a,b >= 0` | no target solution | n/a |
| absolute L1 source conservation | `|C_E| + |C_T| = |S_E| + |S_T|` | `4/3` | `2` |
| E/T absolute equality at center | `C_E = |C_T|` | `5/3` | `4` |

None selects `q_E = 15/8`.

## Boundary: What Would Select the Target

Two exact ways to force the target are still visible:

1. Add the center/source bridge

```text
c_TE = gamma_T(center)/gamma_E(center) = -8/9.
```

Since `gamma_T(center) = -5/3`, this gives

```text
q_E = (-5/3) / (-8/9) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

This is exactly the previously named source-domain bridge target, not a
derivation from the fixed-carrier equations alone.

2. Fit a positive diagonal quadratic metric

```text
a C_E^2 + b C_T^2 = a S_E^2 + b S_T^2.
```

For `q_E = 15/8`, this requires the metric ratio

```text
b/a = 1449/704.
```

That ratio is not supplied by the current fixed carrier, Record axiom, or
Route-2 exact readout/time stack. It is a new selector metric. A quadratic
norm route can therefore reproduce the target only by supplying a metric that
already encodes the missing selection.

## Result

**Theorem (fixed-carrier selector equation boundary).** On the fixed Route-2
carrier with the granted T-side values, the usual source-vector conservation,
collinearity, product, positive-linear, and elementary norm/equipartition
selector equations do not select `q_E = 15/8` or
`rho_E = 21/4`. The target is selected exactly by adding either the center
bridge `c_TE = -8/9` or an equivalent fitted metric/source primitive. Thus the
fixed-carrier selector-equation route does not close the endpoint triple on
the current surface; it sharpens the remaining positive target to a genuine
E-center source/readout primitive.

## What This Prunes

This block prunes the route

```text
fixed Route-2 carrier
+ granted T-side endpoint values
+ basic source-vector conservation/equipartition selector equation
=> rho_E = 21/4.
```

It does not prune a future theorem that derives `c_TE = -8/9`, derives the
metric ratio `1449/704`, or supplies another typed E-center source/readout
primitive from current-surface authorities.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_fixed_carrier_selector_equation_boundary_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=51, FAIL=0
VERDICT: fixed-carrier selector equations do not derive rho_E = 21/4.
```
