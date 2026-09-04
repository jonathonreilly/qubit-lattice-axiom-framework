# Quark Route-2 Coefficient-Selection Boundary

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** negative route boundary
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go
**Trace class:** negative_route_pruning
**Reachability to target:** prunes target-free coefficient-selection routes for
the S3/Route-2 readout endpoint residual
**Primary runner:** [`scripts/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.py)
(`PASS=9 FAIL=0`)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.txt)

## Target Residual

The Route-2 readout-map authority reduces the endpoint problem to

```text
P_R = [[alpha_E, 0, beta_E, 0],
       [0, alpha_T, 0, beta_T]].
```

After the two T-side entries are granted,

```text
beta_T / alpha_T = -1,
alpha_T / alpha_E = -2,
q_T = 5/6,
s_TE = -2,
```

the remaining E-row direction is

```text
rho_E := beta_E / alpha_E,
q_E = 1 + rho_E / 6.
```

The target is exactly equivalent to

```text
rho_E = 21/4
q_E = 15/8
c_TE = -8/9
lambda := q_E / q_T = 9/4.
```

This note asks whether a target-free coefficient-selection principle on the
reduced family selects that E-row direction.

## Reduced Selection Surface

The endpoint-relevant E-row is projective:

```text
ell_E ~ (1, rho_E).
```

The positive shell/center orientation gives only

```text
rho_E > -6.
```

Thus the exact selection surface is the positive projective interval

```text
E_pos = { scale*(1,rho_E) : scale > 0, rho_E > -6 }.
```

The runner verifies that sample values

```text
rho_E in {-5, -1, 0, 1, 21/4, 6}
```

all stay admissible and have distinct `q_E` and `lambda` values. The
E-center-blind data

```text
q_T = 5/6,
s_TE = -2
```

are identical across those choices.

## Selector Scan

The exact target-free selectors tested here do not pick `rho_E=21/4`:

| Selector | Exact result | Status |
|---|---:|---|
| minimal slope / no E-center lift | `rho_E=0` | target-free |
| same E and T center/shell lift | `rho_E=-1` | target-free |
| one reciprocal projector-weight lift | `rho_E=3/2` | target-free one-power |
| inverse-square projector-weight lift | `rho_E=21/4` | missing selector |

The last row is real conditional structure: it lands exactly. But selecting
that inverse-square rule is precisely the open theorem content. It is not
forced by the current reduced readout map, positivity, E-center-blind data, or
ordinary one-power leverage.

## Variational Boundary

A general one-variable quadratic variational selector can be made to land
anywhere:

```text
F(q) = A q^2 + B q + C,
q_* = -B/(2A).
```

To select the Route-2 target,

```text
q_* = 15/8
```

the functional must contain

```text
B/A = -15/4.
```

That coefficient ratio is target-equivalent data. Without an independent
theorem deriving it, the variational form does not select the endpoint; it
only hides the endpoint inside the functional.

Target-free quadratic anchors from the existing reduced surface land at

```text
q_E in {1, 5/6, 5/4},
```

not `15/8`.

## Free-Ratio Boundary

The broader quadratic/readout coefficient class is also not selective. A free
coefficient ratio can realize target and non-target values in the same
algebraic class:

```text
lambda in {1, 3/2, 9/4, 4/3}
```

maps to

```text
rho_E in {-1, 3/2, 21/4, 2/3}.
```

So observing that one allowed coefficient ratio gives `21/4` is not a
selection theorem. The missing step is a rule choosing that ratio.

Equivalently, a projector-weight power law

```text
lambda = kappa^n,  kappa = 3/2
```

gives

```text
n=0 -> rho_E=-1
n=1 -> rho_E=3/2
n=2 -> rho_E=21/4.
```

The endpoint lands only after the exponent is set to `n=2`; selecting that
exponent is the still-open coefficient-selection theorem.

## What Is Claimed

- The reduced endpoint selection surface is the positive projective E-row
  direction `rho_E > -6`.
- E-center-blind data and positivity do not select a point on that interval.
- Ordinary target-free selectors tested here pick `rho_E=-1`, `0`, or `3/2`,
  or leave `rho_E` free.
- A general quadratic variational selector reaches the target only by
  importing the target-equivalent coefficient ratio `B/A=-15/4`.
- The inverse-square projector-weight rule reaches the target exactly, but
  selecting that rule or the exponent `n=2` is the missing theorem content.

## What Is Not Claimed

- This note does not prove that all future coefficient-selection principles
  are impossible.
- This note does not supply `rho_E=21/4`.
- This note does not close the Route-2 endpoint triple.
- This note does not close the parent [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  open gate.
- This note does not adopt the inverse-square rule as a new primitive.

## Load-Bearing Inputs

- [[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  - restricted readout family and endpoint algebra.
- [[`QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md)](QUARK_ROUTE2_ELL_E_STRUCTURAL_NARROWING_BOUNDED_NOTE_2026-06-12.md)
  - projective E-row direction and positive interval.
- [[`QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md`](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)](QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md)
  - E-center-blind data cannot select `rho_E`.
- [[`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)
  - same-domain `kappa=3/2` and covariance residual.
- [[`QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  - inverse-square gap and free-ratio quadratic boundary.
- [[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  - downstream open gate that inherits the readout endpoint obstruction.

## Forbidden-Imports Check

No observed quark mass, CKM/J target, live endpoint fit, PDG value,
nearest-rational selector, or new physical weighting rule is used. The exact
rationals `5/6`, `15/8`, `9/4`, and `21/4` appear only as the already named
Route-2 comparison target. The runner derives every tested selector outcome by
exact rational arithmetic.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.py
```

Expected:

```text
PASS=9 FAIL=0
```
