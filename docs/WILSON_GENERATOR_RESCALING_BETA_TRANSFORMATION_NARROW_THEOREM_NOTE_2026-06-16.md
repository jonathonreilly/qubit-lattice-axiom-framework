# Formal Scalar-Argument Rescaling and Gram Transformation

**Date:** 2026-06-16. Clean-retention rescope: 2026-07-18.
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

## Theorem

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

If the supplied Hermitian family also satisfies
`Tr(T_a T_b)=delta_ab/2`, define `T'_a=c T_a`. Then

```text
s'T'_a = sT_a,
Tr(T'_a T'_b) = c^2 delta_ab/2.
```

Thus the paired transformation preserves the product in the exponent and the
native quadratic coefficient, while a nontrivial generator rescaling changes
the supplied Gram relation.

## Proof

All statements are direct substitution and trace bilinearity:

```text
(c^2 w)(s/c)^2 = w s^2,
(s/c)(c T_a) = sT_a,
Tr((cT_a)(cT_b)) = c^2 Tr(T_aT_b).
```

Positivity makes every displayed division defined. No other input is used.

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
TOTAL: PASS=81 FAIL=0
```
