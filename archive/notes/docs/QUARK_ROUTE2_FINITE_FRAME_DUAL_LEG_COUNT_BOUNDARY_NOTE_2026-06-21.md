# Quark Route-2 Finite-Frame Dual-Leg Count Boundary

**Date:** 2026-06-21
**Claim type:** bounded_theorem
**Claim scope:** conditional_support
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** conditional-support / no-go boundary
**Trace class:** upstream_support
**Reachability to target:** supports and prunes finite-frame/Riesz routes for the
S3/Route-2 readout endpoint residual
**Primary runner:** [`scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py`](../scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py)
(`PASS=9 FAIL=0`)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.txt)

## Target Residual

The parent Route-2 readout endpoint remains the exact triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E)
= (-1, -2, 21/4).
```

After the two T-side entries are granted, the irreducible remaining entry is

```text
rho_E := beta_E / alpha_E = 21/4,
q_E = 1 + rho_E / 6 = 15/8.
```

Equivalently, with `q_T = 5/6`, the covariance ratio is

```text
lambda := q_E / q_T = 9/4.
```

Earlier Route-2 notes already derived the same-domain six-arm `O_h` shell
leverage

```text
kappa = w_T / w_E = (1/2) / (1/3) = 3/2,
kappa^2 = 9/4.
```

This block tests whether finite-frame or Riesz duality supplies the missing
second power of `kappa`.

## Exact Finite-Frame Facts

On the six arms of the octahedral star, the permutation representation
decomposes as

```text
A1 (+) E (+) T1
```

with ranks `(1,2,3)`. The per-arm projector weights are

```text
w_E = 1/3,
w_T = 1/2.
```

For each channel `X in {E,T1}`, the unnormalized projected arm vectors
`P_X e_a` have frame operator

```text
sum_a |P_X e_a><P_X e_a| = P_X.
```

So the unnormalized projected-arm frame is Parseval on the channel and
contributes no reciprocal projector-weight factor:

```text
lambda_0 = 1.
```

If instead each nonzero projected arm vector is unit-normalized, the channel
frame operator is

```text
S_X = (1 / w_X) P_X.
```

Thus a single unit-frame analysis leg contributes

```text
lambda_1 = (1 / w_E) / (1 / w_T) = 3 / 2.
```

Two independent reciprocal unit-frame analysis legs would contribute

```text
lambda_2 = lambda_1^2 = 9 / 4.
```

Under the granted T-side algebra, this exactly reproduces the target:

```text
q_E = lambda_2 q_T = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

## Boundary Result

The finite-frame calculation explains precisely where the target number can
come from:

```text
two reciprocal unit-frame analysis legs.
```

But the current Route-2 readout surface does not derive either of the two
load-bearing ingredients needed to turn that explanation into endpoint
closure:

1. a theorem that the readout uses unit-normalized projected-arm analysis
   rather than the unnormalized Parseval frame or canonical reconstruction;
2. a theorem that there are exactly two independent reciprocal analysis legs
   in the source/readout endpoint map.

Canonical Riesz dual reconstruction is a falsifier for the naive Riesz route:
because `S_X = (1/w_X)P_X`, its inverse cancels the frame bound and reconstructs
`P_X`. It therefore contributes

```text
lambda = 1,
```

not `9/4`.

A single unit-frame analysis leg is also insufficient:

```text
lambda = 3/2,
q_E = 5/4,
rho_E = 3/2.
```

Only two reciprocal unit-frame analysis legs reproduce

```text
lambda = 9/4,
rho_E = 21/4.
```

## Product-Gauge Obstruction

The exact reduced readout endpoint sees the product of source/readout
normalization factors, not a canonical split between them. For example,

```text
(source, readout) in {(1,9/4), (3/2,3/2), (9/4,1), (27/16,4/3)}
```

all give product `9/4`, hence the same reduced endpoint value
`rho_E = 21/4`. The current reduced map has no invariant that selects one of
these decompositions, and therefore no invariant that selects "two reciprocal
analysis legs" rather than another product representation.

This is the precise remaining wall for the finite-frame/Riesz route.

## What Is Claimed

- The six-arm `O_h` projector weights are exactly `w_E=1/3` and `w_T=1/2`.
- Unnormalized projected-arm frames are Parseval and give no endpoint lift.
- Unit-normalized analysis gives one reciprocal factor `3/2`.
- Two independent unit-frame analysis legs conditionally give `9/4` and hence
  `rho_E=21/4` under the granted T-side algebra.
- Canonical Riesz reconstruction cancels the frame bound and does not produce
  the endpoint lift.
- The reduced readout map observes only the product factor and does not derive
  the source/readout split or leg count.

## What Is Not Claimed

- This note does not supply `rho_E=21/4` on the current surface.
- This note does not close the Route-2 readout endpoint triple.
- This note does not close the parent [`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  open gate.
- This note does not adopt a new primitive asserting two reciprocal analysis
  legs.
- This note does not use observed masses, endpoint fitting, nearest-rational
  selection, or live readout calibration as proof inputs.

## Load-Bearing Inputs

- [[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  - restricted readout map, granted T-side algebra, and the residual
  `rho_E=21/4`.
- [[`QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)
  - same-domain `kappa=3/2` relocation and covariance residual.
- [[`QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  - inverse-square projector-weight gap statement and quadratic no-go.
- [[`QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md`](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md)](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md)
  - typed E-center lift target.
- [[`S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)
  - downstream open gate that inherits the readout endpoint obstruction.

## Forbidden-Imports Check

No PDG values, observed quark masses, CKM/J target minimization,
nearest-rational endpoint selection, live-endpoint calibration, or fitted
readout value is used. The exact rationals `5/6`, `15/8`, `9/4`, and `21/4`
appear only as the already-named Route-2 endpoint comparison target. The
finite-frame weights, Parseval identity, unit-frame frame bounds, Riesz
cancellation, leg-count ladder, and product-gauge obstruction are recomputed
directly by the runner.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py
```

Expected:

```text
PASS=9 FAIL=0
```
