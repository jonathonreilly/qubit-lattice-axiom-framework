# Supplied-Diagonal Finite-Box Convolution-Realization Uniqueness

**Date:** 2026-05-17; conditional-scope repair 2026-07-16
**Claim type:** bounded_theorem
**Claim scope:** exact inverse Peter-Weyl algebra on a finite `SU(3)`
character box for a separately supplied positive character-diagonal,
conjugation-symmetric operator. This note does not prove that the stripped
physical Wilson residual has that operator class.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Runner:** [`scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_finite_box_convolution_realization_uniqueness_narrow.py`](../scripts/frontier_gauge_vacuum_plaquette_spatial_environment_character_measure_finite_box_convolution_realization_uniqueness_narrow.py)

## Finite setup

Fix

```text
B = {(p,q) : 0 <= p,q <= NMAX},
H_B = span{chi_(p,q) : (p,q) in B}.
```

The characters are orthonormal in the class-function Haar inner product.
Supply coefficients

```text
rho_(p,q) >= 0,
rho_(p,q) = rho_(q,p),
```

and the diagonal operator

```text
R[rho] chi_(p,q) = rho_(p,q) chi_(p,q).
```

No claim is made here that `R[rho]` is obtained from the physical Wilson
kernel.

For any normalization `z_0 > 0`, define the finite character polynomial

```text
Z[rho](W) = z_0 sum_((p,q) in B) d_(p,q) rho_(p,q) chi_(p,q)(W),
d_(p,q) = (p+1)(q+1)(p+q+2)/2.
```

## Conditional theorem

Define scale-divided convolution by

```text
(C_(Z[rho]/z_0) f)(V)
  := integral_(SU(3)) (Z[rho](V W^(-1))/z_0) f(W) dW.
```

This is division by the supplied scale `z_0`; it is not normalization by the
actual trivial character coefficient unless `rho_(0,0)=1`. It acts on the
supplied finite character packet by

```text
C_(Z[rho]/z_0) chi_(p,q) = rho_(p,q) chi_(p,q).
```

Therefore

```text
C_(Z[rho]/z_0)|_(H_B) = R[rho].
```

This is the finite Peter-Weyl identity

```text
chi_lambda * chi_mu
  = (delta_(lambda,mu) / d_lambda) chi_lambda
```

applied coefficient by coefficient.

The scale-divided finite character polynomial is unique. If another finite
central polynomial

```text
Z'(W) = z'_0 sum_((p,q) in B) d_(p,q) rho'_(p,q) chi_(p,q)(W)
```

has the same scale-divided convolution action on `H_B`, character
orthonormality gives

```text
rho'_(p,q) = rho_(p,q)
```

for every weight in `B`, hence `Z'/z'_0 = Z[rho]/z_0`.

## Relation to algebraic stripping

The context note
`docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_FINITE_BOX_STRIPPING_UNIQUENESS_NARROW_NOTE_2026-05-17.md`
proves that, after a factorized form

```text
K = M D^loc R M
```

is supplied with invertible `M` and `D^loc`, the residual operator is
algebraically unique:

```text
R = (D^loc)^(-1) M^(-1) K M^(-1).
```

That statement does not imply that `R` is diagonal. The present theorem
begins only after a diagonal `R[rho]` is separately supplied.

## Hostile boundary

Let `v = chi_(0,0) + chi_(1,1)` on a box containing those weights and set

```text
C = I + |v><v|.
```

Then `C` is positive definite, self-adjoint, and commutes with conjugation
swap, but it has nonzero off-diagonal character matrix elements. Thus
positivity plus conjugation symmetry does not provide coefficients
`rho_(p,q)` or a convolution realization of the form above. Replacing `C`
by `diag(C)` loses operator information.

## Numerical witness boundary

The runner instantiates several supplied coefficient packets, including the
normalized values of the explicitly stipulated finite integral

```text
rho_(p,q)(6) = c_(p,q)(6) / (d_(p,q)c_(0,0)(6)).
```

That is a chosen bounded witness of the conditional algebra. The cited row
supplies only the integral evaluation; it is not a derivation or selection of
the compressed multi-link spatial Wilson environment.

## What remains open

To apply this theorem to the physical source-sector residual, one must first
derive that the stripped Wilson compression commutes with the relevant
regular translations, equivalently that it is convolution by a central
kernel, or calculate its character-basis off-diagonal matrix elements
directly and prove that they vanish. Algebraic stripping uniqueness and
conjugation-swap symmetry alone do not supply that result.

## Dependencies

- [SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the character/convolution normalization.
- [GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md](GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md)
  supplies the finite stipulated-integral values used as a chosen witness only.

Context only:
`docs/GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md`
and
`docs/GAUGE_VACUUM_PLAQUETTE_RESIDUAL_ENVIRONMENT_FINITE_BOX_STRIPPING_UNIQUENESS_NARROW_NOTE_2026-05-17.md`.
