# Quark Route-2 Positive Source-Functional Cone No-Go

**Date:** 2026-06-21
**Status:** scoped no-go; branch-local physics-loop packet only
**Primary runner:** `scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py`

## Scope

This note tests a defined nonlinear family left open by the Route-2 readout
work:

```text
finite positive channel-local source/readout functionals
with net channel-weight exponent p >= -1.
```

This covers ordinary positive polynomial or trace/projector weight dependence
(`p >= 0`) and source/readout responses with at most one explicit inverse
channel-volume power (`p = -1`). It does not cover signed cancellations, an
explicit two-denominator density-square primitive, or future nonlinear tensor
observables outside this exponent-cone model.

## Exact Cone Bound

The current finite-star channel weights are:

```text
w_E = 1/3,  w_T = 1/2,  r = w_E/w_T = 2/3.
```

For a positive finite sum

```text
F_X = sum_i c_i w_X^{p_i},  c_i >= 0,
```

the E/T ratio is a positive weighted average of `r^{p_i}`:

```text
F_E/F_T =
  (sum_i c_i w_T^{p_i} r^{p_i}) / (sum_i c_i w_T^{p_i}).
```

Therefore:

```text
p_i >= 0   => F_E/F_T <= 1,
p_i >= -1  => F_E/F_T <= r^{-1} = 3/2.
```

The Route-2 endpoint needs:

```text
q_E/q_T = 9/4.
```

Thus no positive finite channel-local functional with net exponent `p >= -1`
can derive the endpoint covariance. It can at most give:

```text
q_E <= (3/2)(5/6) = 5/4,
rho_E <= 6(5/4 - 1) = 3/2,
c_TE = (-2)(5/6)/(5/4) = -4/3
```

at the upper one-inverse boundary.

## What Still Works Conditionally

The target appears immediately when the net exponent reaches `p=-2`:

```text
(w_E/w_T)^-2 = (2/3)^-2 = 9/4
q_E = (9/4)(5/6) = 15/8
rho_E = 21/4
c_TE = -8/9.
```

The runner also leaves the signed escape open. For example:

```text
R_X = 1/w_X - 6/5
```

gives:

```text
R_E/R_T = (3 - 6/5)/(2 - 6/5) = 9/4.
```

That fit uses a negative coefficient, so it is outside the positive cone.

## Claim Boundary

This block prunes only the route:

```text
positive finite source/readout cone with no more than one inverse
channel-volume power => Route-2 endpoint covariance 9/4.
```

It does not prove impossibility over arbitrary future nonlinear observables.
The remaining live possibilities are now sharply named:

1. an explicit density-square primitive with net exponent `p=-2`;
2. a signed source/readout cancellation rule;
3. a future nonlinear tensor observable outside this exponent-cone model.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py
```

Expected result:

```text
PASS=30 FAIL=0 TOTAL=30
```
