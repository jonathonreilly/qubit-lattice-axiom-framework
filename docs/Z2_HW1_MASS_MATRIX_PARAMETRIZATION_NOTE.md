# Z_2 `hw=1` Mass-Matrix Parametrization Note

**Date:** 2026-04-17 (corrected 2026-07-15)
**Claim type:** positive_theorem
**Status:** proposed exact finite-dimensional structural theorem; audit-status
authority belongs to the independent audit lane
**Script:** `scripts/frontier_z2_hw1_mass_matrix_parametrization.py`
**Authority role:** self-contained normal-form theorem for a supplied
three-point axis-permutation representation; not a physical-carrier,
mass-hierarchy, or parameter-selection theorem

## Safe statement

Let `V_1 = span(X_1, X_2, X_3)` be a supplied complex inner-product space on
which `S_3` permutes the displayed basis vectors. Let
`Z_2 = <s>`, with `s=(12)`, fix axis `3` while swapping axes `1` and `2`.
In the ordered basis `(X_3, X_1, X_2)`, every `Z_2`-invariant Hermitian
operator on `V_1` has the form

```text
M(a, b, c, d) = [[a,  d,  d ],
                 [d*, b,  c ],
                 [d*, c,  b ]]
```

with `a, b, c in R` and `d in C`. This is a `5`-real-parameter family.

The vector `(X_1 - X_2) / sqrt(2)` is an exact sign eigenvector with eigenvalue
`b - c`. On the two-dimensional trivial block spanned by
`X_3` and `(X_1 + X_2)/sqrt(2)`, the operator reduces to the Hermitian block

```text
[[a,        sqrt(2) d],
 [sqrt(2)d*, b + c   ]]
```

with eigenvalues

```text
lambda_pm = ((a + b + c) +- sqrt((a - b - c)^2 + 8 |d|^2)) / 2.
```

Generic points in this `5`-real-parameter family give three distinct
eigenvalues. The exact full-`S_3`-invariant locus is the two-real-parameter
subspace

```text
a = b,  d = c with c in R.
```

On that locus,

```text
M = (a - c) I_3 + c J_3,
spec(M) = {a + 2c, a - c, a - c},
```

where `J_3` is the all-ones matrix. Thus exact `S_3` invariance forces at
most two spectral values; it does not select either real parameter.

## Derivation from explicit generators

In the ordered basis `(X_3, X_1, X_2)`, take the generating transposition and
3-cycle to be

```text
S = U((12))  = [[1, 0, 0],       R = U((123)) = [[0, 0, 1],
                [0, 0, 1],                       [1, 0, 0],
                [0, 1, 0]],                      [0, 1, 0]].
```

They obey `S^2=R^3=I` and `S R S=R^(-1)`, so they generate all six
permutation matrices. Start with a general Hermitian `3 x 3` matrix.
The equation `S M S^dagger=M` equates the last two diagonal entries, equates
the two first-row off-diagonal entries, and makes the `(2,3)` entry real.
This gives exactly the displayed residual form with
`a,b,c in R` and `d in C`.

For that form, the remaining generator equation is explicit:

```text
R M R^dagger - M =
[[b-a, d*-d, c-d ],
 [d-d*, a-b, d-c ],
 [c-d*, d*-c, 0  ]].
```

It vanishes if and only if `a=b`, `d=d*`, and `d=c`. Since Hermiticity
already made `c` real, this is precisely `a=b` and `d=c in R`. Conversely,
those conditions make `M` invariant under both generators and therefore under
all of `S_3`. This proves necessity and sufficiency without sampling.

## Classical results applied

- Schur's lemma on the `Z_2` decomposition `V_1 ~= 2 * trivial + sign`
- the Hermitian spectral theorem
- the quadratic formula for the `2 x 2` Hermitian secular equation

## Framework-specific step

- the symbols `X_i` and `hw=1` label the supplied three-dimensional source
  surface only; this note does not derive a physical carrier or symmetry-
  breaking mechanism
- any application to a physical mass operator must separately establish the
  carrier identification, its group action, and pointwise operator invariance

## Why it matters on `main`

This is a finite linear-algebra support tool complementary to the separate
conditional `S_3` commutant classification. It exposes the full residual
`Z_2` Hermitian normal form and its exact full-`S_3` sublocus on the supplied
representation. It does not claim a derived flavor hierarchy, identify the
space with physical generations, establish physical symmetry breaking, or
select a point in the five-real-parameter family.

## Verification

Run:

```bash
python3 scripts/frontier_z2_hw1_mass_matrix_parametrization.py
```

The runner checks invariance, the `5`-dimensional real parameter count, the
sign eigenvector, the explicit `2 x 2` block, and the closed-form spectrum. It
then performs an exact symbolic solve of the transposition and 3-cycle
invariance equations, checks all six permutation matrices on the resulting
`S_3` locus, verifies its spectrum, and exercises hostile controls omitting
each necessary locus condition.
