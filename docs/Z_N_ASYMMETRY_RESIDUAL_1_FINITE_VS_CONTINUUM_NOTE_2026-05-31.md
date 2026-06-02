# Z_N Spectral Asymmetry: Finite/Continuum Separation for L3(1,2)=2/9

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** finite algebraic separation between the framework's
`L_3(1,2)=2/9` Molien/Lefschetz weight and continuum spin-Dirac lens eta. External
Atiyah-Bott/Donnelly/APS language is context only, not a source derivation.
**Primary runner:**
`scripts/frontier_z_n_asymmetry_finite_vs_continuum_separation.py`
with cache
`logs/runner-cache/frontier_z_n_asymmetry_finite_vs_continuum_separation.txt`.

## Result

The finite framework object is the holomorphic-Lefschetz/Molien weight of the `C_3`
action on the generation doublet:

```
L_3(1,2) = (1/3) sum_k det[(C^k-I)^(-1) | doublet] = 2/9.
```

The runner separates this value from two continuum-style comparators built from the same
rotation data `(3;(1,2))`:

- Molien/Lefschetz weight: `+2/9`.
- G-signature cot-product: `-2/9`.
- spin-Dirac lens csc-product: `0`.

So the literal continuum spin-Dirac eta is not the same number as the finite `2/9`
weight. The note also checks that `2/9` is not an algebraic integer, while index and
equivariant spectral-flow values are algebraic integers; the suspension spectral flow
across the doublet zero crossing is the integer `2`, not `2/9`.

Finally, the flat staggered operator still has the expected bulk `+/-` pairing and bulk
signed count zero, while the finite `hw=1` generation sector is not paired by the
`(pi,pi,pi)` shift. This explains how the finite equivariant sector can carry a nonzero
character jump without being a continuum eta of the flat bulk operator.

## Boundary

This note tightens the continuum residual; it does not close it. The finite denominator
and Molien/Lefschetz weight are source-internal. A self-adjoint continuum eta on a curved
or boundary substrate still requires a source bridge not supplied here.

## Load-Bearing Authorities

[AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
[NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md](NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md)
[STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md)
[HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md](HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md)
[KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md)
[THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)

## No-Go Discipline Gate

**N1 - Alternative routes.** Five continuum-closure routes were checked. Route 1:
representation data alone gives a continuum eta; fails because the data-to-eta map is an
external bridge. Route 2: the flat staggered operator supplies a nonzero bulk eta; fails
because bulk signed count is zero. Route 3: spectral flow gives `2/9`; fails because the
flow is integer `2`. Route 4: Molien regular-point evaluation is the spin-Dirac eta;
fails because the csc-product value is `0`. Route 5: finite equivariant sector jump is
already continuum eta; fails because it is finite-sector character data, not a curved or
boundary continuum operator.

**N2 - Wall independence.** The number-class wall (`2/9` is not an algebraic integer) and
the comparator wall (spin-Dirac eta is `0`) are independent.

**N3 - Hidden-wall scan.** The proof keeps Molien/Lefschetz, signature defect, spin-Dirac
eta, bulk pairing, and finite sector as distinct objects.

**N4 - Residual matching.** This note addresses only the finite/continuum residual. The
finite operator-identification residual is handled by the companion source note.

**N5 - Rhetoric audit.** "Not continuum eta" means the finite `2/9` weight is not the
literal spin-Dirac lens eta or an index/spectral-flow value. It does not rule out a later
curved/boundary source bridge producing an appropriate continuum object.

**N6 - Partial-closure path.** A later bounded theorem could build a curved substrate,
boundary geometry, Wilson/domain-wall mass, or spectral-flow bridge. This note does not
call for an axiom change.

**N7 - Steelman.** The strongest continuum argument is that the finite denominator is the
local fixed-point factor expected in Atiyah-Bott/Donnelly formulas. The runner grants the
local denominator and separates it from the self-adjoint continuum eta value.

**N8 - Cross-cycle echo.** The same finite-versus-continuum boundary appears in the APS
block-by-block route and the staggered bulk-vanishing scoping note. This note builds the
finite/operator side and leaves the continuum side open.
