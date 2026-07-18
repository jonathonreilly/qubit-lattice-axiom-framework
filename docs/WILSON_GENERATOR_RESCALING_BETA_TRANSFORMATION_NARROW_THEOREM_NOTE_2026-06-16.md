# Formal Scalar-Argument Rescaling and Gram Transformation

**Date:** 2026-06-16. Abstract-algebra rescope: 2026-07-18.
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py`](../scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py)

## Purpose

This note proves an exact transformation law for the native quadratic
coefficient supplied by
[`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
Its stable filename is historical. No comparison target or preferred scalar
value is part of the theorem.

The cited matrix theorem gives, for a Gram-normalized Hermitian family,

```text
q(w,s,n) := [x^2 F2] w D(sx) = w s^2/(4n).
```

## Theorem: two distinct transformations

### 1. Fixed normalized family: scalar coefficient identity

Let `n>=1` and let `w,s,c>0`. Define

```text
w' = c^2 w,
s' = s/c.
```

Then the quadratic coefficient is invariant:

```text
q(w',s',n)
  = (c^2 w)(s^2/c^2)/(4n)
  = q(w,s,n).
```

This is an identity between scalar-coordinate values of `q` for the same
half-Gram family. For `c != 1`, changing `s` changes the exponent argument; no
generator transformation is part of this first statement.

### 2. Generator covariance: exponent identity and Gram change

If the supplied Hermitian family also satisfies
`Tr(T_a T_b)=delta_ab/2`, define `T'_a=c T_a`. Then

```text
s'T'_a = sT_a,
Tr(T'_a T'_b) = c^2 delta_ab/2.
```

Writing `A'=sum_a f_a T'_a=cA`, the simultaneous map `s'=s/c` preserves the
exponent and deficit exactly: `s'A'=sA` and `D_{T'}(s'x)=D_T(sx)`. It preserves
the weighted expression only when `w'=w`. If one also imposes the first
statement's `w'=c^2w`, the weighted deficit and its quadratic coefficient
scale by `c^2`; they are not invariant.

Equivalently, for a family with
`Tr(T_aT_b)=kappa delta_ab/2`, direct Gram contraction gives

```text
q_kappa(w,s,n) = w s^2 kappa/(4n).
```

Under `T'=cT`, `s'=s/c`, and hence `kappa'=c^2 kappa`, this quantity is
invariant for fixed `w`, while it scales by `c^2` if `w'=c^2w` is imposed as
well.

## Proof

All statements are direct substitution and trace bilinearity:

```text
(c^2 w)(s/c)^2 = w s^2,
(s/c)(c T_a) = sT_a,
Tr((cT_a)(cT_b)) = c^2 Tr(T_aT_b).
```

The generalized coefficient follows by replacing the half-Gram contraction
with `Tr(A^2)=kappa F2/2`. Positivity of `c` makes the displayed division
defined; the scalar coefficient identity itself is algebraic. No other input
is used.

## Boundary

This note does not supply an external interpretation of `w`, `s`, or `T_a`;
does not choose a comparison coefficient or solve a parameter equation; and
does not turn a changed Gram convention into a preferred normalization. It
also does not set an audit verdict or status promotion. Any use beyond the
displayed matrix and scalar algebra requires separate authority.

## Verification

```text
python3 scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py
```

Expected:

```text
TOTAL: PASS=91 FAIL=0
```
