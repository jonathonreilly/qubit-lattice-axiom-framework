# Abstract Hermitian-Product Conjugation-Parity Theorem for an Explicit Matrix Family

**Date:** 2026-04-16; abstract-matrix source rescope 2026-07-18
**Status:** bounded theorem in finite matrix algebra
**Claim type:** `bounded_theorem`
**Primary runner:** `scripts/frontier_dm_pmns_he_parity_repair.py`
**Cached output:** `logs/runner-cache/frontier_dm_pmns_he_parity_repair.txt`
**Dependencies:** none; the matrix family is defined explicitly below
**Status authority:** independent audit lane only

The historical filename and claim identifier are retained only for stable
repository references. They do not supply an interpretation of the matrix.

## Exact theorem

Let

```text
x1, x2, x3, y1, y2, y3, delta in R
```

and define the following abstract one-parameter matrix family:

```text
Y(delta) =
[[x1,                    y1,  0],
 [ 0,                    x2, y2],
 [y3 exp(i delta),        0, x3]].
```

Set

```text
H(delta) = Y(delta) Y(delta)^dagger.
```

Then direct multiplication gives

```text
H(delta) =
[[x1^2 + y1^2,           x2 y1, x1 y3 exp(-i delta)],
 [x2 y1,          x2^2 + y2^2,                 x3 y2],
 [x1 y3 exp(i delta),     x3 y2,         x3^2 + y3^2]].
```

For every real choice of the seven parameters:

1. `H(delta)` is Hermitian and positive semidefinite;
2. `H(-delta) = conjugate(H(delta))`, where the conjugation on the
   right is entrywise; and
3. if a scalar function `F` on this matrix family satisfies
   `F(conjugate(H)) = F(H)` for every member `H` of the family, then
   `delta -> F(H(delta))` is even.

This statement is the entire theorem.

## Direct multiplication and product order

Write the rows of `Y(delta)` as

```text
r1 = (x1, y1, 0),
r2 = (0, x2, y2),
r3 = (y3 exp(i delta), 0, x3).
```

Because `H_ab = r_a r_b^dagger`, the nine entries are

```text
H11 = x1^2 + y1^2,
H12 = x2 y1,
H13 = x1 y3 exp(-i delta),
H21 = x2 y1,
H22 = x2^2 + y2^2,
H23 = x3 y2,
H31 = x1 y3 exp(i delta),
H32 = x3 y2,
H33 = x3^2 + y3^2.
```

This is specifically `Y Y^dagger`. In general, `Y^dagger Y` is a different
matrix and is not substituted anywhere in the theorem.

The displayed entries obey `H_ba = conjugate(H_ab)`, so `H` is Hermitian.
For any `v in C^3`,

```text
v^dagger H v
  = v^dagger Y Y^dagger v
  = (Y^dagger v)^dagger (Y^dagger v)
  = ||Y^dagger v||_2^2
  >= 0.
```

Thus `H` is positive semidefinite. This conclusion uses the displayed
`Y Y^dagger` order. It does not require `Y` to be invertible: the Gram-matrix
argument includes zero coordinates, singular matrices, and every
rank-deficient case.

## Conjugation parity and the universal corollary

Only `H13` and `H31` depend on `delta`. Replacing `delta` by `-delta`
interchanges `exp(i delta)` and `exp(-i delta)`. All six coordinates are real,
so every remaining entry is fixed by conjugation. Hence

```text
H(-delta) = conjugate(H(delta)).
```

The seven phase-independent entries are individually even. The two
phase-sensitive entries are only conjugation-paired:

```text
H13(-delta) = conjugate(H13(delta)) = H31(delta),
H31(-delta) = conjugate(H31(delta)) = H13(delta).
```

They are not individually even for generic real coordinates and phase. The
real-coordinate premise is essential to the displayed parity implication;
allowing arbitrary complex coordinates need not preserve it.

Now let `F` be any scalar function on this family with
`F(conjugate(H)) = F(H)`. Then

```text
F(H(-delta))
  = F(conjugate(H(delta)))
  = F(H(delta)),
```

which is exactly evenness of the composite. No stronger condition on `F` is
being inferred.

## Derived concrete invariant examples

Define

```text
A = x1^2 + y1^2,  B = x2^2 + y2^2,  C = x3^2 + y3^2,
p = x2 y1,         q = x1 y3,         r = x3 y2,
a = x1 x2 x3,      b = y1 y2 y3.
```

The characteristic polynomial has the form

```text
chi_H(t) = t^3 - c1 t^2 + c2 t - c3,
c1 = A + B + C,
c2 = AB + AC + BC - p^2 - q^2 - r^2,
c3 = det(H) = a^2 + b^2 + 2ab cos(delta).
```

These formulas follow by expanding the displayed matrix. They show directly
that the trace, determinant, and all characteristic coefficients are real and
even. Equality of the characteristic polynomials at `delta` and `-delta`
implies equality of the eigenvalue multisets, with algebraic multiplicity.

For every integer `k >= 1`, `H^k` is Hermitian, so `tr(H^k)` is real. Also,

```text
tr(H(-delta)^k)
  = tr(conjugate(H(delta)^k))
  = conjugate(tr(H(delta)^k))
  = tr(H(delta)^k).
```

Thus every trace power is even. Finally,

```text
||H||_F^2 = sum_ab |H_ab|^2 = tr(H^2),
```

so the Frobenius norm is conjugation-invariant and even as well. These examples
are consequences of the theorem, not extra interpretation of the symbols.

## Exact positive-semidefinite checks

The principal minors also make positive semidefiniteness explicit. The three
nontrivial `2 x 2` principal minors are

```text
x1^2 x2^2 + x1^2 y2^2 + y1^2 y2^2,
x1^2 x3^2 + y1^2 x3^2 + y1^2 y3^2,
x2^2 x3^2 + x2^2 y3^2 + y2^2 y3^2,
```

and

```text
det(H)
  = (a + b cos(delta))^2 + (b sin(delta))^2
  = |det(Y)|^2.
```

Together with the nonnegative diagonal entries, every principal minor is
nonnegative, consistently with the Gram-matrix proof above.

## Scope boundary

This note does not derive the explicitly defined matrix family from the
framework baseline or identify it as a PMNS chart, a Yukawa law, a
charged-lepton carrier, or a leptogenesis input. It supplies no selector,
stationary system, KKT solution, branch classification, branch-minimality
result, CP-asymmetry law, or physical phase-selection mechanism.

A physical use would require a separate retained bridge deriving both the
matrix family and the proposed interpretation. No such bridge is cited or
load-bearing here; the physical bridge remains open in this note.

## Verification

Run the three independent modes:

```bash
python3 scripts/frontier_dm_pmns_he_parity_repair.py --mode normal
python3 scripts/frontier_dm_pmns_he_parity_repair.py --mode independent
python3 scripts/frontier_dm_pmns_he_parity_repair.py --mode hostile
```

The normal route performs direct symbolic multiplication and exact invariant
checks. The independent route reconstructs `Y Y^dagger` as a sum of column
outer products and uses separately coded numerical characteristic-polynomial
and principal-minor checks. The hostile route recomputes and rejects a wrong
phase sign, a moved phase, a non-conjugating transpose, substitution of
`Y^dagger Y`, complex-coordinate drift, false entrywise evenness, and a wrong
characteristic coefficient.

## Bottom line

For the explicitly defined real-coordinate matrix family above, and only that
family, `H = Y Y^dagger` is the displayed Hermitian positive-semidefinite
matrix, sign reversal of `delta` is entrywise conjugation, and every
conjugation-invariant scalar composite is even.
