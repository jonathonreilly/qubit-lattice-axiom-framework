# Six-Mode Paired-Direction Coin `b`-Eigenvalue Determinant Factorization

**Date:** 2026-07-23
**Type:** positive_theorem
**Status:** proposed_retained
**Runner:** [`scripts/six_mode_paired_direction_coin_b_eigenvalue_determinant_factorization_2026_07_23.py`](../scripts/six_mode_paired_direction_coin_b_eigenvalue_determinant_factorization_2026_07_23.py)

## Question

Consider a six-component paired-direction walk whose opposite directions are
swapped by

```text
R = (12)(34)(56).
```

Let `P = 11^T/6` be the scalar projector and define

```text
Q(b) = 2 P + (b-1) I/2 - (b+1) R/2,
D(x,y,z) = diag(x, x^-1, y, y^-1, z, z^-1).
```

What is the exact `b`-eigenvalue determinant of the streamed matrix
`D Q(b)`?

## Theorem

In the Laurent polynomial ring
`C[b, x, x^-1, y, y^-1, z, z^-1]`,

```text
det(D Q(b) - b I)
  = - b^3 (b-1)^2 (b+1)
      (x-1)^2 (y-1)^2 (z-1)^2 / (8 x y z).
```

At `D=I`, the characteristic polynomial of `Q(b)` is

```text
det(lambda I - Q(b))
  = (lambda-1) (lambda+1)^2 (lambda-b)^3.
```

Thus the zero-momentum eigenvalues are `1`, `-1`, and `b`, with
multiplicities `1`, `2`, and `3`, respectively.

## Proof

Write

```text
A = (b-1) I/2 - (b+1) R/2,
Q = A + 11^T/3.
```

Then

```text
D Q - b I = B + (D1) 1^T/3,
B = D A - b I.
```

The matrix `B` is the direct sum of one `2 x 2` block for each of
`t in {x,y,z}`.  If

```text
a = (b-1)/2,  c = (b+1)/2,
```

the `t` block is

```text
B_t = [[t a - b,  -t c],
       [-c/t,      a/t - b]].
```

Direct expansion gives

```text
det(B_t) = -b (b-1) (t-1)^2/(2t).
```

For generic parameters, the rank-one determinant lemma gives

```text
det(B + (D1)1^T/3)
  = det(B) [1 + 1^T B^-1 D1/3].
```

Solving the three independent `2 x 2` blocks yields

```text
1^T B_t^-1 (t, t^-1)^T = 2/(b-1).
```

The three blocks therefore contribute

```text
1 + 1^T B^-1 D1/3 = (b+1)/(b-1).
```

Multiplying this by the three block determinants gives the stated
factorization.  The calculation was made for generic parameters only to use
the inverse; equality in the Laurent polynomial ring extends it to the
exceptional parameter values.  The characteristic polynomial follows directly
from the scalar line, the two-dimensional even subspace orthogonal to it, and
the three-dimensional odd subspace of `R`.

## Verification

The paired runner checks the result by two independent algebraic routes:

1. direct symbolic expansion of the full `6 x 6` determinant;
2. the `2 x 2` block plus rank-one-determinant-lemma derivation above.

It also tests exact specializations and wrong-sign/missing-factor controls so
that a copied expected value cannot award itself a pass.

## Boundary

This is an exact algebraic theorem for the matrix defined here.  It imports no
measured, fitted, literature, normalization, boundary-condition, or
state-contingent value.

It does not identify `b` with a physical energy, mass, rate, probability, or
observable.  It does not claim flat-band absence, absence of finitely supported
states, localization, an interacting/contact theorem, an infinite-volume
result, a clock, or a continuum limit.  Any such statement needs its own
bridge and proof.
