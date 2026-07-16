# Gauge-Vacuum Plaquette Supplied-D Residual Quotient and Formal Convolution Packaging

**Date:** 2026-05-17; supplied-input repin 2026-07-16
**Claim type:** bounded_theorem
**Claim scope:** exact per-weight algebra for the quotient of two explicitly
supplied character-diagonal operators and its formal central-convolution
packaging. This note does not derive the stripped Wilson residual, its
character diagonality, or its identification with an unmarked Wilson
environment.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit verdict or effective status.
**Primary runner:** `scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py`
**Runner cache:** `logs/runner-cache/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.txt`

## Scope correction

An earlier version treated the diagonal middle operator in

`T_beta = exp[(beta/2)J] D_beta exp[(beta/2)J]`

as a Wilson-derived fact and then named the diagonal quotient
`(D_beta^loc)^(-1)D_beta` the physical residual environment. That use is
retracted. The source-sector factorization authority now proves only a
conditional theorem for a supplied positive character-diagonal `D_beta`.

Accordingly, this consumer retains only the conditional quotient algebra:

- `D_beta` is an explicit supplied diagonal input;
- `D_beta^loc` is an explicit supplied strictly positive diagonal input;
- their quotient is diagonal because both inputs are diagonal;
- a diagonal coefficient sequence has the standard formal
  central-convolution representation.

None of those statements proves that an actual stripped Wilson compression is
diagonal or that a separately computed static Wilson boundary density is the
same operator.

## Supplied inputs

Let the dominant weights be `(p,q) in P_+(SU(3))`. Supply real coefficient
families satisfying

`kappa_(p,q)(beta) >= 0`,

`kappa_(p,q)(beta) = kappa_(q,p)(beta)`,

and strictly positive local coefficients

`a_(p,q)(beta) > 0`,

`a_(p,q)(beta) = a_(q,p)(beta)`.

Define the two character-diagonal operators

`D_beta chi_(p,q) = kappa_(p,q)(beta) chi_(p,q)`,

`D_beta^loc chi_(p,q) = a_(p,q)(beta)^4 chi_(p,q)`.

The quotient theorem below is conditional on both diagonal inputs. Context
examples are recorded in
`docs/GAUGE_VACUUM_PLAQUETTE_SOURCE_SECTOR_MATRIX_ELEMENT_FACTORIZATION_NOTE.md`,
`docs/GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md`,
and
`docs/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md`;
none supplies Wilson provenance for `D_beta`.

## Theorem 1: exact diagonal quotient

Define

`R_beta[r] := (D_beta^loc)^(-1) D_beta`.

Then, per weight,

`R_beta[r] chi_(p,q)
 = r_(p,q)(beta) chi_(p,q)`,

where

`r_(p,q)(beta)
 = kappa_(p,q)(beta) / a_(p,q)(beta)^4`.

Therefore `R_beta[r]` is positive semidefinite, self-adjoint, and invariant
under `(p,q)<->(q,p)`. This conclusion is exact because it is the quotient of
the supplied diagonal coefficient sequences. It makes no statement about a
general positive swap-symmetric operator with character mixing.

## Theorem 2: formal convolution packaging

Choose an arbitrary positive scale `lambda(beta)>0` and define formal
Peter-Weyl coefficients

`z_(p,q)(beta) := lambda(beta) r_(p,q)(beta)`.

On every finite weight window, define the central class polynomial

`Z_beta^(N)(W)
 = sum_(0<=p,q<=N) d_(p,q) z_(p,q)(beta) chi_(p,q)(W)`.

The abstract character/convolution theorem
[SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md](SU3_CHARACTER_DIAGONAL_CONVOLUTION_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
and Schur orthogonality give, on that finite window,

`C_(Z_beta^(N)) chi_(p,q)
 = z_(p,q)(beta) chi_(p,q)`.

Hence

`R_beta[r] chi_(p,q)
 = (1/lambda(beta)) C_(Z_beta^(N)) chi_(p,q)`

for each weight in the window. The compatible collection of these finite
identities is the all-weight formal sequence used here. No convergence of an
infinite Peter-Weyl series and no full-Hilbert-space operator equality is
claimed.

## Theorem 3: normalization

Assume additionally for this normalization statement that
`kappa_(0,0)(beta)>0`. Because `a_(0,0)=1` for the normalized local packet,

`r_(0,0)(beta)=kappa_(0,0)(beta)`

and

`z_(0,0)(beta)=lambda(beta) kappa_(0,0)(beta)`.

Thus normalized convolution by `Z/z_(0,0)` gives

`R_beta[r] / kappa_(0,0)(beta)`,

not `R_beta[r]`, unless the additional hypothesis
`kappa_(0,0)(beta)=1` is supplied. This note does not assume that
normalization.

If `kappa_(0,0)(beta)=0`, then `z_(0,0)(beta)=0` and normalization by the
actual trivial coefficient is undefined. The unnormalized finite-window
identity in Theorem 2 remains valid.

## Why this is not a Wilson identification

For a general operator `C` on the character basis, the diagonal sequence
`diag(C)` does not determine `C`. A positive self-adjoint operator can commute
with the conjugation swap and still have nonzero off-diagonal character
matrix elements. The primary source-sector runner gives an explicit strictly
positive example and rejects a helper that silently uses only `diag(C)`.

Consequently, the notation `R_beta[r]` in this note means the quotient of the
two supplied diagonal inputs above. It is not licensed as notation for the
actual Wilson residual until a separate theorem proves one of the following:

- the stripped Wilson compression has a kernel `K(U,V)=k(UV^(-1))` with `k`
  central;
- it commutes with the full regular-translation actions required for central
  convolution;
- or a direct Wilson-kernel calculation proves every off-diagonal character
  matrix element vanishes.

The current static spatial-environment note explicitly leaves its
identification with the stripped two-slice source residual open.

## What this preserves

- exact quotient algebra for supplied diagonal `D_beta` and `D_beta^loc`;
- positivity, self-adjointness, and conjugation symmetry of that supplied
  quotient;
- the finite-window Schur/Peter-Weyl dictionary between a supplied diagonal
  sequence and a formal central convolution;
- the normalization distinction between `lambda(beta)` and the actual trivial
  coefficient.

## What this does not claim

- Wilson-derived diagonality of `D_beta` or the quotient;
- identification of the quotient with the physical unmarked spatial Wilson
  environment;
- an actual all-weight class function or `L^2` operator equality;
- physical `rho_(p,q)(6)`, a Wilson Perron state, analytic `P(6)`, or any
  numerical repinning.

## Command

```bash
python3 scripts/audit_companion_gauge_vacuum_plaquette_residual_environment_all_weight_convolution_identification.py
```

The runner uses exact symbolic diagonal inputs. Its output is evidence for the
conditional algebra above, not for the missing Wilson operator-compression
bridge.
