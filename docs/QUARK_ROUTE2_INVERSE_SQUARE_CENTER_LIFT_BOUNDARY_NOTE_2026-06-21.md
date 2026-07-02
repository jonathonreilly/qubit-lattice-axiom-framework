# Quark Route-2 Inverse-Square Center-Lift Boundary

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / exact support boundary; no endpoint closure
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_inverse_square_center_lift_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_inverse_square_center_lift_boundary_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_inverse_square_center_lift_boundary_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_inverse_square_center_lift_boundary_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md), [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

## Scope

The covariance/Schur route identifies the sharp remaining same-domain gap as

```text
lambda = q_E/q_T = kappa^2 = 9/4,
```

equivalently an inverse-square center-lift rule

```text
q_X proportional to w_X^-2
```

where the O_h per-arm channel weights are

```text
w_E = 1/3,
w_T = 1/2.
```

This block sharpens that gap into the exact normalized law that would close the
Route-2 endpoint:

```text
q_X w_X^2 = 5/24.
```

It then checks whether current named O_h/quadratic/naturality/Record surfaces
derive that reciprocal-weight normalization.

## Authority Inputs

- [[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the endpoint algebra.
- [[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
  keeps `rho_E` free unless an E-center primitive is supplied.
- [[QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)
  derives the same-domain `kappa=3/2` value but not the covariance bridge.
- [[QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  identifies the inverse-square law as the exact gap and states no named
  functional produces it.
- [[TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md)](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md)
  supplies the shared center-excess denominator `1/6`.
- [[MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)](MINIMAL_AXIOMS_2026-06-05.md)
  withholds readout weighting and source primitives from the base Record/Quantum
  surface.

## Exact Boundary

Given the T-side value

```text
q_T = 5/6
```

and the O_h T-channel per-arm weight

```text
w_T = 1/2,
```

an inverse-square law fixes the common normalized constant as

```text
C = q_T w_T^2 = (5/6)(1/4) = 5/24.
```

Applying the same law to the E-channel weight `w_E=1/3` gives

```text
q_E = C / w_E^2 = (5/24) / (1/9) = 15/8,
rho_E = 6(q_E - 1) = 21/4,
c_TE = (-2)(5/6)/(15/8) = -8/9.
```

So the inverse-square law is an exact closure candidate.

## Why This Still Does Not Close The Endpoint

The current O_h covariance route derives the value `kappa=3/2`, and the Schur
route proves that a quadratic O_h-invariant functional has a free E:T reduced
ratio. Those surfaces do not derive a reciprocal-weight law, and especially do
not derive the normalized constant `5/24`.

The exact power-law table is:

| Lift rule | `q_E/q_T` from weights | Result |
|---|---:|---|
| `w_X^2` | `4/9` | wrong slot/value |
| `w_X` | `2/3` | wrong slot/value |
| `w_X^0` | `1` | no covariance |
| `w_X^-1` | `3/2` | one leverage power |
| `w_X^-2` | `9/4` | target covariance |

The target is uniquely the inverse-square power among these natural integer
weight powers. Selecting that reciprocal power is itself the missing
source/readout primitive.

## Result

**Theorem (Route-2 inverse-square center-lift boundary).** The normalized
inverse-square center-lift law

```text
q_X w_X^2 = 5/24
```

would derive the Route-2 E-center target exactly. Current named O_h
equivariance, quadratic Schur, naturality, center-excess, and minimal-axiom
surfaces do not derive that law or its normalization. Therefore the route is
an exact support boundary and a sharpened open primitive target, not endpoint
closure.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_center_lift_boundary_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=40, FAIL=0
VERDICT: inverse-square center-lift normalization would close Route-2, but remains an open primitive.
```
