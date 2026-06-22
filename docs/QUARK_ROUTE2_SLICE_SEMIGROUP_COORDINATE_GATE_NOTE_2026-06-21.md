# Quark Route-2 Slice-Semigroup Coordinate Gate Note

**Date:** 2026-06-21
**Status:** no-go / semigroup-coordinate boundary.
**Primary runner:** `scripts/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.py`
**Output:** `outputs/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.txt`

## Claim Boundary

The exact Route-2 endpoint target follows from the inverse-square value
`lambda = 9/4` only if that value scales the raw lift coordinate:

```text
q_E = lambda q_T = (9/4)(5/6) = 15/8,
rho_E = 6(q_E - 1) = 21/4.
```

Block87 isolated that as a coordinate-selector gap. This block asks whether
the S3 time slice semigroup can justify the raw `q` coordinate.

## Result

The slice semigroup does not select raw `q` scaling.

The parent S3 time surface supplies an exact conditional semigroup once a
readout map is supplied:

```text
V_R(t) = exp(-t Lambda_R) u_*,
Xi_P(t ; c) = (P_R c) x V_R(t).
```

But a constant raw-lift scaling law

```text
F(q) = lambda q
```

is not a semigroup endomorphism unless `lambda = 1`:

```text
F(1) = lambda != 1,
F(q1 q2) = lambda q1 q2,
F(q1)F(q2) = lambda^2 q1 q2.
```

For the needed `lambda = 9/4`, the identity and composition laws fail.

## Generator Coordinates Miss The Endpoint

The semigroup-natural coordinate is the logarithmic generator. Scaling that
coordinate gives

```text
q_E = q_T^lambda.
```

Because `0 < q_T = 5/6 < 1` and `lambda = 9/4 > 1`, this gives
`q_E < 1`, while the endpoint target has `q_E = 15/8 > 1`.

Even the sign-flipped generator scaling misses:

```text
q_E = q_T^(-lambda) = (6/5)^(9/4) < (6/5)^3 = 216/125 < 15/8.
```

The additive generator/increment coordinate also misses:

```text
1 + lambda(q_T - 1) = 5/8.
```

## Current-Surface Firewall

This block does not close the parent endpoint triple. It sharpens the
remaining positive target:

```text
derive a non-semigroup readout primitive that selects raw q_X scaling, or
derive a different typed source/readout bridge to q_E = 15/8.
```

The S3 slice semigroup verifies the conditional readout-to-slice family; it
does not supply the raw `q` coordinate selector needed for `21/4`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_slice_semigroup_coordinate_gate_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=29, FAIL=0
```
