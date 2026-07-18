# Gauge-Vacuum Plaquette Supplied-Diagonal Source-Sector Factorization Theorem

**Date:** 2026-04-17; positive supplied-diagonal theorem 2026-07-18
**Claim type:** positive_theorem
**Claim scope:** exact finite-dimensional factorization, positivity, symmetry,
rank, kernel, and spectral consequences on a finite `SU(3)` character box for
an explicitly supplied real nonnegative swap-symmetric diagonal sequence.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit verdict or effective status.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py`
**Runner cache:** `logs/runner-cache/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.txt`

## Question

What follows exactly from the finite character recurrence when the middle
operator is supplied by a nonnegative swap-symmetric diagonal sequence?

## Typed inputs

Fix `N >= 0` and the finite square character box

`B_N := {(p,q) : 0 <= p,q <= N}`.

Let

`H_N := span{chi_(p,q) : (p,q) in B_N}`

with the irreducible characters as an orthonormal basis, and let `P_N` be the
orthogonal projection onto `H_N`.

The first operator input is the explicit real six-neighbor recurrence

`J_N chi_(p,q) = (1/6) P_N [
    chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
  + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q)]`,

where labels outside `B_N` are omitted. Equivalently,

`J_N := P_N [(chi_(1,0) + chi_(0,1))/6] P_N`.

Let the swap be

`S_N chi_(p,q) := chi_(q,p)`.

For a supplied real number `beta`, set

`M_beta := exp[(beta/2) J_N]`.

The second operator input is a supplied sequence

`kappa_(p,q)(beta) in R`,

typed by

`kappa_(p,q)(beta) >= 0`,

`kappa_(p,q)(beta) = kappa_(q,p)(beta)`.

It defines the character-diagonal operator

`D_beta := sum_((p,q) in B_N)
              kappa_(p,q)(beta) |chi_(p,q)><chi_(p,q)|`.

Zeros are allowed, and no normalization of the supplied sequence is required.

## Theorem and outputs

Define

`T_beta := M_beta D_beta M_beta`.

Then all of the following hold.

### 1. Properties of `M_beta`

The recurrence graph is undirected, so `J_N=J_N^*`. Its neighbor list is
preserved by `(p,q) <-> (q,p)`, hence

`S_N J_N = J_N S_N`.

The spectral theorem therefore gives

`M_beta = M_beta^* > 0`,

`M_beta^(-1) = exp[-(beta/2)J_N]`,

`S_N M_beta = M_beta S_N`.

Thus `M_beta` is self-adjoint, strictly positive, invertible, and
swap-commuting for every real `beta`.

### 2. Exact finite matrix-element sum

For `lambda,mu in B_N`, insertion of the character-basis resolution of the
identity gives

`(T_beta)_(lambda,mu)
 = <chi_lambda, M_beta D_beta M_beta chi_mu>`

`= sum_(nu in B_N)
   (M_beta)_(lambda,nu) kappa_nu(beta) (M_beta)_(nu,mu)`.

The order of both `M_beta` indices is fixed by the row-column convention in
this displayed formula.

### 3. Positivity, self-adjointness, and exact Gram factorization

For every `v in H_N`,

`<v,T_beta v>
 = <M_beta v,D_beta M_beta v>
 = sum_(nu in B_N) kappa_nu(beta) |(M_beta v)_nu|^2 >= 0`.

With

`B_beta := D_beta^(1/2) M_beta`,

one has the exact Gram factorization

`T_beta = B_beta^* B_beta`.

Consequently `T_beta` is positive semidefinite and self-adjoint.

### 4. Swap symmetry

The supplied coefficient symmetry is exactly the statement

`S_N D_beta = D_beta S_N`.

Together with the corresponding identity for `M_beta`, this gives

`S_N T_beta = T_beta S_N`.

### 5. Rank and kernel

Invertibility of `M_beta` gives the exact congruence identities

`rank(T_beta) = rank(D_beta)`,

`ker(T_beta) = M_beta^(-1) ker(D_beta)`.

Thus each supplied zero contributes exactly one null direction, transported
by `M_beta^(-1)`.

### 6. Spectral bounds and definiteness

Let

`m_- := lambda_min(M_beta)`, `m_+ := lambda_max(M_beta)`,

`d_- := min_(nu in B_N) kappa_nu(beta)`,
`d_+ := max_(nu in B_N) kappa_nu(beta)`.

For every unit vector `v`,

`d_- m_-^2
 <= <v,T_beta v>
 <= d_+ m_+^2`.

Hence

`d_- m_-^2 <= lambda_min(T_beta)`

and

`lambda_max(T_beta) <= d_+ m_+^2`.

In particular, `T_beta` is positive definite if and only if every supplied
coefficient is strictly positive. If any supplied coefficient is zero,
`T_beta` is positive semidefinite with the rank and kernel stated above.

## The `beta = 6` specialization

At `beta=6`,

`M_6 = exp(3J_N)`,

`T_6 = exp(3J_N) D_6 exp(3J_N)`,

and

`(T_6)_(lambda,mu)
 = sum_(nu in B_N) (exp(3J_N))_(lambda,nu)
          kappa_nu(6)
          (exp(3J_N))_(nu,mu)`.

The same positivity, self-adjointness, swap, rank, kernel, spectral-bound, and
definiteness conclusions apply.

This theorem accepts `D_beta` through its typed supplied sequence and returns
`T_beta` with the outputs above.

## Verification

The runner separates exact algebra from deterministic numerical support:

- `Fraction`-only boxes verify recurrence self-adjointness and swap
  commutation, including `N=0`;
- exact rational matrices verify the matrix-element convention, Gram
  orientation, rank/kernel identities, and strictly-positive, partly-zero,
  all-zero, and `beta=0` cases;
- deterministic symmetric eigendecompositions support the exponential and
  spectral statements on several larger boxes and irregular supplied
  sequences, including `beta=6`;
- mutation validators reject malformed diagonal input, a wrong matrix-element
  contraction, a negative coefficient for the positivity conclusion, broken
  coefficient swap symmetry for the swap conclusion, and singular or
  non-positive multiplier surrogates for invertibility-dependent conclusions.

Floating residuals are reported only as numerical support; the theorem is the
finite-dimensional argument above.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py
```
