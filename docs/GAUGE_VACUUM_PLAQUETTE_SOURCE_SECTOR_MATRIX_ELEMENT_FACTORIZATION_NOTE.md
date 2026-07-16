# Gauge-Vacuum Plaquette Conditional Source-Sector Matrix-Element Factorization Theorem

**Date:** 2026-04-17; conditional-scope repair 2026-07-16
**Claim type:** positive_theorem
**Claim scope:** exact finite-dimensional linear algebra on a stated truncated
`SU(3)` character basis, conditional on a supplied positive
character-diagonal operator `D_beta`; no identification of `D_beta` with the
stripped Wilson residual is claimed.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit verdict or effective status.
**Script:** `scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py`
**Runner cache:** `logs/runner-cache/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.txt`

## Question

What factorization and matrix-element statements follow exactly on a finite
`SU(3)` character-basis truncation once the middle operator is explicitly
supplied as positive, character-diagonal, and conjugation-symmetric?

## Answer

Fix a finite character box, the self-adjoint source recurrence `J`, and

`M_beta := exp[(beta / 2) J]`.

Supply an operator `D_beta` by its character-basis action

`D_beta chi_(p,q) = kappa_(p,q)(beta) chi_(p,q)`,

where every `kappa_(p,q)(beta)` is real and nonnegative and

`kappa_(p,q)(beta) = kappa_(q,p)(beta)`.

Define

`T_beta := M_beta D_beta M_beta`.

Then `T_beta` is positive semidefinite, self-adjoint, and invariant under the
character-conjugation swap. Its matrix elements are exactly

`(T_beta)_(lambda,mu)
 = sum_nu (M_beta)_(lambda,nu) kappa_nu(beta) (M_beta)_(nu,mu)`.

This is a conditional theorem for a supplied `D_beta`. It does not derive a
Wilson residual operator, prove that a stripped Wilson compression is
character-diagonal, or compute any physical `kappa_(p,q)(beta)`.

## Finite character truncation

Fix `N >= 0` and let

`B_N := {(p,q) : 0 <= p,q <= N}`,

`H_N := span{chi_(p,q) : (p,q) in B_N}`,

with the irreducible characters taken as an orthonormal basis. Let `P_N` be
orthogonal projection onto `H_N`. Define the compressed source recurrence by

`J_N := P_N [(chi_(1,0) + chi_(0,1))/6] P_N`.

Equivalently, its action is the six-neighbour recurrence

`J_N chi_(p,q) = (1/6) P_N [
    chi_(p+1,q) + chi_(p-1,q+1) + chi_(p,q-1)
  + chi_(p,q+1) + chi_(p+1,q-1) + chi_(p-1,q)]`,

where terms with a negative label or outside `B_N` are omitted. The finite
recurrence graph is undirected, so `J_N` is real self-adjoint.

Let `S_N` be the conjugation swap

`S_N chi_(p,q) := chi_(q,p)`.

The recurrence is invariant under `(p,q) <-> (q,p)`, hence
`S_N J_N = J_N S_N`. For real `beta`, define

`M_beta := exp[(beta/2) J_N]`.

Functional calculus then gives, exactly:

- `M_beta` is self-adjoint;
- `M_beta` is strictly positive and invertible;
- `S_N M_beta = M_beta S_N`.

No floating-point exponentiation is needed for these conclusions.

## Supplied diagonal hypothesis

The theorem assumes, rather than derives, a real coefficient family

`kappa_(p,q)(beta) >= 0`,

`kappa_(p,q)(beta) = kappa_(q,p)(beta)`.

Define

`D_beta := sum_((p,q) in B_N)
              kappa_(p,q)(beta) |chi_(p,q)><chi_(p,q)|`.

Thus character diagonality, positivity, and swap symmetry are explicit input
hypotheses. Zeros are allowed, so `D_beta` and `T_beta` may be semidefinite.
No normalization such as `kappa_(0,0)=1` is required by this theorem.

## Theorem

Under the finite-truncation and supplied-`D_beta` hypotheses above, define

`T_beta := M_beta D_beta M_beta`.

Then the following statements hold.

### 1. Exact matrix-element sum

For `lambda,mu in B_N`, insert the character-basis resolution of the identity:

`(T_beta)_(lambda,mu)
 = <chi_lambda, M_beta D_beta M_beta chi_mu>`

`= sum_(nu in B_N)
   (M_beta)_(lambda,nu) kappa_nu(beta) (M_beta)_(nu,mu)`.

This is an exact finite sum and is simply the matrix law for the explicitly
supplied diagonal operator.

### 2. Positivity and self-adjointness

For every `v in H_N`,

`<v,T_beta v>
 = <M_beta v,D_beta M_beta v>
 = sum_nu kappa_nu(beta) |(M_beta v)_nu|^2 >= 0`.

Also

`T_beta^* = M_beta^* D_beta^* M_beta^* = T_beta`.

Equivalently, with

`B_beta := D_beta^(1/2) M_beta`,

one has the exact Gram factorization

`T_beta = B_beta^* B_beta`.

### 3. Conjugation symmetry

Because both `M_beta` and `D_beta` commute with `S_N`,

`S_N T_beta = T_beta S_N`.

### 4. Rank, kernel, and spectral bounds

Since `M_beta` is invertible,

`rank(T_beta) = rank(D_beta)`,

`ker(T_beta) = M_beta^(-1) ker(D_beta)`.

Write `m_-` and `m_+` for the smallest and largest eigenvalues of `M_beta`,
and `d_-` and `d_+` for the smallest and largest supplied coefficients.
Then

`d_- m_-^2 <= lambda_min(T_beta)`

and

`lambda_max(T_beta) <= d_+ m_+^2`.

In particular, `T_beta` is positive definite exactly when every supplied
coefficient is strictly positive; supplied zeros give the corresponding
semidefinite nullity through the invertible congruence.

## The `beta = 6` specialization

For `beta=6`, and only after a diagonal operator `D_6` has been supplied,

`M_6 = exp(3J_N)`,

`T_6 = exp(3J_N) D_6 exp(3J_N)`,

with

`(T_6)_(lambda,mu)
 = sum_nu (exp(3J_N))_(lambda,nu)
          kappa_nu(6)
          (exp(3J_N))_(nu,mu)`.

This specialization does not identify `D_6` with a Wilson residual and does
not turn a generic coefficient sequence into Wilson data.

## Retracted Wilson inference and the missing stronger condition

An earlier version inferred that a stripped Wilson residual compression was a
central convolution operator, hence character-diagonal, from reality,
positivity, self-adjointness, and simultaneous-conjugation invariance. That
inference is retracted.

Those properties do not force character diagonality. On `H_N` with `N>=1`,
let

`v := chi_(0,0) + chi_(1,1)`,

`C := I + |v><v|`.

Then `C` is strictly positive and self-adjoint, and it commutes with `S_N`
because `S_N v=v`. But

`<chi_(0,0), C chi_(1,1)> = 1`,

so `C` mixes characters and is not diagonal. Replacing `C` by `diag(C)` loses
the cross terms in `M_beta C M_beta`; a `kappa`-only formula is therefore not
valid for a general positive swap-symmetric operator.

The corresponding finite kernel

`K_C(U,V) := sum_(lambda,mu) C_(lambda,mu)
chi_lambda(U) overline(chi_mu(V))`

is separately conjugation invariant in `U` and `V`, hence in particular
simultaneous-conjugation invariant. Thus the hostile example satisfies the old
invariance premise as well as positivity and self-adjointness.

The representation-theoretic condition that would justify character
diagonality is stronger: for example, derive an actual kernel

`K(U,V) = k(U V^(-1))`

with `k` a central class function. Alternatively, after extending the operator
to the relevant `L^2(SU(3))` representation space, prove the full left/right
regular-action intertwining conditions whose commutant gives central
convolution. Then Schur/Peter-Weyl theory gives character eigenvectors.
Simultaneous conjugation alone only commutes with the conjugation action; it
does not provide this translation/convolution structure.

For the Wilson application, the remaining wall is therefore an explicit
calculation or theorem showing that the algebraically stripped, compressed
two-slice Wilson residual has this stronger structure, or a direct calculation
of its character-basis matrix showing that every off-diagonal entry vanishes.
Current-main static spatial-environment coefficient calculations do not by
themselves identify that static convolution with the stripped two-slice
operator.

## Exact theorem versus runner witnesses

The proof above is exact finite-dimensional linear algebra. The runner keeps
that proof boundary visible:

- a small `N=1` case uses `Fraction`-only rational matrices with an explicitly
  supplied invertible rational `M`, including an exact Gram identity and the
  hostile mixing operator `C`;
- multiple larger boxes use deterministic floating-point matrix exponentials
  only as finite witnesses;
- the floating residuals and eigenspectra are not described as exact proofs;
- the tested supplied sequences include irregular positive rational data,
  algebraic data, same-total-weight asymmetry compatible with conjugation,
  and zero/semidefinite cases;
- a guarded diagonal helper accepts supplied diagonal `D` and rejects the
  hostile off-diagonal `C`.

## What this closes

- the exact finite-dimensional matrix-element formula for a supplied positive
  character-diagonal `D_beta`;
- exact positivity, self-adjointness, conjugation symmetry, rank/kernel, and
  spectral consequences of that supplied-operator theorem;
- the conditional `beta=6` specialization for a supplied `D_6`.

## What remains open

- derivation of the actual stripped Wilson residual as a central convolution
  or direct proof of its character diagonality;
- proof that stripping/compression preserves any additional positivity or
  operator structure needed in the physical Wilson construction;
- physical `kappa_(p,q)(6)` data;
- a `beta=6` Wilson Perron state, plaquette value, or repo-wide numerical
  repinning.

## Command

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_source_sector_matrix_element_factorization.py
```
