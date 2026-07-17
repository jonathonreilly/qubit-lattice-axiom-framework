# Cubic-Reciprocal Series Bounds and Rational Normalization — Positive Theorem

**Date:** 2026-05-28 (self-contained formal repair: 2026-07-17)
**Type:** positive_theorem
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source states and
proves a theorem; it neither assigns nor predicts an audit verdict.
**Tier:** exact analysis bounds and finite algebra over `Q`
**Dependencies:** none
**Primary runner:**
[`scripts/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.py`](../scripts/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.py)
**Cached log:**
[`logs/runner-cache/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.txt`](../logs/runner-cache/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.txt)

## Claim

This note proves two independent statements from explicit definitions. The
first gives rational lower and upper brackets for a convergent series. The
second gives the exact scaling and unique target normalization of a positive
rational monomial. No physical constant, measured value, comparator, unit
conversion, or framework premise occurs in either theorem.

## T1 — rational brackets for the cubic-reciprocal series

Define

```text
Z   = sum_{k=1}^infinity 1/k^3,
S_N = sum_{k=1}^N        1/k^3              (N in Z, N >= 1).
```

Every `S_N` is rational. Define two further rational numbers

```text
L_N = S_N + 1/[2(N+1)^2],
U_N = S_N + 1/(2N^2).
```

Then, for every integer `N >= 1`,

```text
L_N <= Z <= U_N.                                      (1)
```

The bracket width is exactly

```text
U_N-L_N = (2N+1)/[2N^2(N+1)^2].                       (2)
```

Consequently the doubled series has the entirely rational certificate

```text
2S_N + 1/(N+1)^2 <= 2Z <= 2S_N + 1/N^2.              (3)
```

The intervals are nested:

```text
L_N <= L_(N+1) <= Z <= U_(N+1) <= U_N.               (4)
```

Their widths tend to zero, so the rational brackets determine `Z` uniquely.

### Proof of T1

The function `f(x)=x^(-3)` is positive and strictly decreasing on
`[1,infinity)`. For each integer `k >= N+1`, monotonicity gives

```text
integral_k^(k+1) f(x) dx <= 1/k^3
                          <= integral_(k-1)^k f(x) dx.
```

Summing these inequalities and taking the increasing finite-sum limit gives

```text
integral_(N+1)^infinity x^(-3) dx
  <= sum_(k=N+1)^infinity 1/k^3
  <= integral_N^infinity x^(-3) dx.
```

Since

```text
integral_A^infinity x^(-3) dx = 1/(2A^2),
```

adding `S_N` proves (1). Direct subtraction proves (2), and multiplying
(1) by two proves (3).

For nesting, write the two exact increments as

```text
L_(N+1)-L_N
  = 1/(N+1)^3 + 1/[2(N+2)^2] - 1/[2(N+1)^2] > 0,

U_N-U_(N+1)
  = 1/(2N^2) - 1/(N+1)^3 - 1/[2(N+1)^2] > 0.
```

After multiplication by the positive common denominators, the respective
numerators are `3N+5` and `3N+1`. This proves (4). Formula (2) tends to zero
because its numerator has degree one and its denominator degree four.

## T2 — positive rational monomial and unique normalization

For positive rationals `a,t,m,r,s`, define

```text
C(a,t,m,r,s) = a t^3 m s / r.                         (5)
```

For every positive rational `lambda`, exact scaling in each coordinate is

```text
C(lambda a,t,m,r,s) = lambda C(a,t,m,r,s),
C(a,lambda t,m,r,s) = lambda^3 C(a,t,m,r,s),
C(a,t,lambda m,r,s) = lambda C(a,t,m,r,s),
C(a,t,m,lambda r,s) = C(a,t,m,r,s)/lambda,
C(a,t,m,r,lambda s) = lambda C(a,t,m,r,s).            (6)
```

For two positive parameter tuples, the complete ratio identity is

```text
C(a',t',m',r',s') / C(a,t,m,r,s)
 = (a'/a)(t'/t)^3(m'/m)(r/r')(s'/s).                 (7)
```

Fix positive rationals `a,t,m,r` and set

```text
C_0 = C(a,t,m,r,1) = a t^3 m/r.
```

For every positive rational target `q`, there is exactly one positive
rational normalization `s_*` satisfying `C(a,t,m,r,s_*)=q`, namely

```text
s_* = q/C_0 = q r/(a t^3 m).                          (8)
```

Its exact displacement from the unit normalization is

```text
s_*-1 = (q-C_0)/C_0.                                  (9)
```

### Proof of T2

Equations (6) and (7) follow by cancellation in the field `Q`. For fixed
`a,t,m,r`, equation (5) is `C=C_0 s` with `C_0>0`. Thus `C=q` is equivalent
to `s=q/C_0`, proving existence, positivity, and uniqueness in (8). Subtracting
one gives (9).

As a fully exact example, choose

```text
(a,t,m,r) = (2,3,5,7),     C_0=270/7,     q=54.
```

Then `s_*=7/5`, `s_*-1=2/5`, and

```text
C(2,3,5,7,7/5)=54
```

exactly.

## Boundary of the theorem

The two results above are self-contained mathematics. The historical filename
preserves repository identity only. The symbols in T1 and T2 carry no physical
interpretation, and the example values are chosen solely for exact rational
arithmetic. In particular, this theorem supplies no baryon density, photon
density, cosmological temperature, particle mass, gravitational constant,
metrology convention, observational coefficient, published comparison, or
framework-derived normalization.

The definitions are not admissions: T1 is universally quantified over every
integer `N>=1`, and T2 is universally quantified over its written positive
rational domain.

## Cited dependencies and imports

None. T1 uses only monotonicity, elementary integration of `x^(-3)`, and
rational finite sums. T2 uses only field arithmetic in `Q`. No framework
axiom, approved primitive, external paper, observed value, or fitted quantity
is load-bearing.

## Validation

The companion runner uses exact `Fraction` arithmetic in three modes:

1. normal mode verifies T1 and T2 across exhaustive finite integer and
   positive-rational grids, including bracket nesting, exact widths, every
   scaling law, the ratio identity, and normalization uniqueness;
2. `--independent` reconstructs `S_N` with a single integer common
   denominator, checks the cell-integral inequalities and their telescoping
   finite forms, and verifies the monomial theorem by cleared denominators;
3. `--hostile` rejects booleans, floats, integer subclasses, `Fraction`
   subclasses, nonpositive domains, zero denominators, and malformed calls,
   while enforcing the source interpretation boundary.

Selectable mutation fixtures alter actual summands, tail endpoints,
coefficient exponents, denominator placement, normalization direction, input
coercion, or source prose. Every individual mutation and their aggregate must
exit nonzero in all three modes.
