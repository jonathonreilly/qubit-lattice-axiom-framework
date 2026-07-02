# Exact Q-gen Metzler Violation for All Odd N -- Closed Form Bounded Note

**Date:** 2026-07-02  
**Type:** bounded theorem (closed-form finite-generator obstruction)  
**Claim type:** bounded_theorem  
**Status:** source proposal / bounded-theorem artifact. This note does not set
an audit outcome, derive a Record bridge, or select an action.  
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.  
**Paired runner:**
[`scripts/frontier_exact_qgen_metzler_all_odd_n_2026_07_02.py`](../scripts/frontier_exact_qgen_metzler_all_odd_n_2026_07_02.py)  
**Cached output:**
[`outputs/frontier_exact_qgen_metzler_all_odd_n_2026_07_02.txt`](../outputs/frontier_exact_qgen_metzler_all_odd_n_2026_07_02.txt)

## Purpose

Block13 proved the finite Metzler lemma and certified exact `Q-gen`
positivity failure on tested `Z_5` and `Z_7`. This note removes the tested-only
restriction for odd cyclic groups.

For every odd `N>=5`, the exact finite `Q-gen` character family

```text
chi_n(P_t) = exp(-t n^2)
```

on symmetric residues has a generator with a negative off-diagonal entry at
displacement `j=2`. By Block13's finite Metzler lemma, it is not a positive
convolution semigroup.

## T1 -- convention and odd-N closed form

Use the Fourier convention

```text
hat a(k) = sum_{j in Z_N} a_j exp(-2 pi i k j/N),
a_j      = (1/N) sum_{k in Z_N} hat a(k) exp(2 pi i k j/N).
```

A convolution generator whose characters are

```text
hat P_t(k) = exp(-t psi(k))
```

has generator Fourier coefficients

```text
hat L(k) = -psi(k),
L_j = -(1/N) sum_k psi(k) exp(2 pi i k j/N).
```

For odd `N=2M+1`, take the symmetric representatives

```text
k in {-M, ..., M},   psi(k)=k^2.
```

Since `psi` is even, for `j != 0`,

```text
L_j = -(1/N) S_j,
S_j = sum_{n=-M}^{M} n^2 cos(2 pi n j/N).
```

Let

```text
D(theta) = sum_{n=-M}^{M} exp(i n theta)
         = sin(N theta/2) / sin(theta/2).
```

Then

```text
D''(theta) = - sum_{n=-M}^{M} n^2 exp(i n theta),
S_j = -D''(2 pi j/N).
```

Write `u(theta)=sin(N theta/2)` and `v(theta)=sin(theta/2)`. At

```text
theta_j = 2 pi j/N,  1 <= j <= N-1,
```

the numerator vanishes:

```text
u(theta_j)=sin(pi j)=0.
```

Also `u''(theta_j)=0`. Therefore the quotient rule at a numerator zero gives

```text
D''(theta_j) = -2 u'(theta_j) v'(theta_j) / v(theta_j)^2.
```

The needed derivatives are

```text
u'(theta_j) = (N/2)(-1)^j,
v(theta_j)  = sin(pi j/N),
v'(theta_j) = (1/2) cos(pi j/N).
```

Hence

```text
D''(theta_j)
= -(N/2)(-1)^j cos(pi j/N) / sin^2(pi j/N),
```

and therefore

```text
S_j
= (N/2)(-1)^j cos(pi j/N) / sin^2(pi j/N).
```

The paired runner verifies this exact closed form against direct symbolic
summation for `N=5,7,9,11,13` and every `1<=j<=N-1`.

## T2 -- all odd N>=5 violate Metzler at j=2

Substituting the closed form into `L_j=-(1/N)S_j` gives, for odd `N`,

```text
L_j = -(1/2)(-1)^j cos(pi j/N) / sin^2(pi j/N).
```

At displacement `j=2`,

```text
L_2 = -(1/2) cos(2 pi/N) / sin^2(2 pi/N).
```

For every odd `N>=5`,

```text
0 < 2 pi/N <= 2 pi/5 < pi/2,
```

so `cos(2 pi/N)>0` and `sin^2(2 pi/N)>0`. Thus

```text
L_2 < 0.
```

This is an off-diagonal entry of the exact `Q-gen` circulant generator. By
Block13's finite Metzler lemma, the semigroup `exp(tL)` cannot be entrywise
nonnegative for all `t>=0`. Therefore the exact `Q-gen` character family is
not a positive convolution semigroup on any odd `Z_N` with `N>=5`.

## T3 -- even-N convention and analogous result

For even `N=2M`, the boundary mode `N/2` is self-inverse. The convention used
here is to count that boundary mode once, with representatives

```text
{-M+1, ..., M}.
```

This gives

```text
psi(n)=n^2,
S_j^even = sum_{n=-M+1}^{M} n^2 cos(2 pi n j/N).
```

Set

```text
F(theta) = sum_{n=-M+1}^{M} exp(i n theta)
         = exp(i theta/2) sin(N theta/2) / sin(theta/2).
```

At `theta_j=2 pi j/N`, `1<=j<=N-1`, the sine numerator vanishes. Let

```text
D_N(theta) = sin(N theta/2) / sin(theta/2),
alpha = pi j/N.
```

At `theta_j`,

```text
D_N'(theta_j)  = (N/2)(-1)^j / sin(alpha),
D_N''(theta_j) = -(N/2)(-1)^j cos(alpha) / sin^2(alpha).
```

Because `F(theta)=exp(i theta/2)D_N(theta)` and `D_N(theta_j)=0`,

```text
F''(theta_j)
= exp(i alpha) (i D_N'(theta_j) + D_N''(theta_j)).
```

Taking the real part and using `S_j^even=-Re F''(theta_j)` gives

```text
S_j^even = (N/2)(-1)^j / sin^2(pi j/N),
L_j^even = -(1/2)(-1)^j / sin^2(pi j/N).
```

Thus, under this boundary-mode convention,

```text
L_2^even = -1 / (2 sin^2(2 pi/N)) < 0
```

for every even `N>=4`. The runner verifies the even closed form by direct exact
symbolic summation for `N=6,8,10,12,14` and all off-zero displacements, and
checks the `j=2` sign for those same even values.

## T4 -- consequence for the Block10 trichotomy

Block13's bifurcation now upgrades on odd cyclic groups: exact finite `Q-gen`
versus positivity is unconditional for every odd `Z_N` with `N>=5`. The
wrapped Gaussian remains the positive Gaussian-like finite object, but it has
theta-image corrections rather than exact finite quadratic characters. Thus
Block10's trichotomy horn (a), if pursued as an extended-step exact `Q-gen`
construction, is not merely signed in tested examples; on all odd `N>=5` it is
incompatible with finite Markov positivity. This note still does not select a
horn or prove a Record bridge.

## What this note does NOT claim

- No action is selected.
- No Record bridge is proved.
- No horn of the Block10 trichotomy is selected.
- No literature theorem is imported.
- No new axiom or primitive is introduced.
- No wrapped-Gaussian correction theorem beyond the Block13 sampled
  correction data is added here.
- The even statement is conditional on the stated one-copy convention for the
  self-inverse `N/2` boundary mode.
- Sibling inputs are stacked and unaudited; status authority remains with the
  independent audit lane.

## Load-bearing inputs

- Block13 sibling:
  [`EXACT_QGEN_NOT_POSITIVE_ON_ZN_WRAPPED_GAUSSIAN_CORRECTION_BOUNDED_NOTE_2026-07-02.md`](EXACT_QGEN_NOT_POSITIVE_ON_ZN_WRAPPED_GAUSSIAN_CORRECTION_BOUNDED_NOTE_2026-07-02.md).
  Role: supplies the finite Metzler lemma and the tested `N=5,7` positivity
  obstruction that this note upgrades to a closed-form all-odd theorem. This
  sibling is stacked and unaudited.

## Paired runner

The paired runner reports:

```text
SUMMARY PASS=109 FAIL=0 TOTAL=109
SUMMARY ODD_CLOSED_FORM verified_N=5,7,9,11,13 all_j; odd_j2_negative_N=5..41
SUMMARY EVEN_SCOPE convention=residues_-N/2+1..N/2; closed_form_verified_N=6,8,10,12,14 all_j; sampled_j2_negative_N=6,8,10,12,14; theorem=even_N>=4_j2_negative_under_this_convention
```
