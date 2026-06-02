# Koide Kähler-Dirac Is Silent on the Measure

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** finite Kähler-Dirac/Fock-space check and generation-measure
localization. This note does not derive the Koide mass measure.
**Primary runner:**
`scripts/frontier_koide_kahler_dirac_silent_on_measure_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_kahler_dirac_silent_on_measure_2026_05_30.txt`.

## Result

On `Lambda*(R^3)`, the Kähler-Dirac operator `D_KD=d-delta` is real-antisymmetric and
`iD_KD` is Hermitian, but it is grade-off-diagonal. Every grade-diagonal block
`Lambda^k -> Lambda^k` vanishes, including the `Lambda^1 -> Lambda^1` generation
triplet block. Therefore this operator does not itself provide a within-generation
kinetic/complex-structure selector for the Koide measure.

The runner also checks that determinant/Pfaffian measures do not give the per-block
counting: for `M=aI+b(C+C^2)`, `det(M)=(a+2b)(a-b)^2`, and
`det(M tensor eps)=det(M)^2`, so the doublet is counted with dimension power 2. This is
the per-dimension/rank route, not the per-block route.

Finally, the two candidate complex-structure objects are limited in different ways:
central `iI_3` is generation-blind, while `Jcs^2=-P_doublet` and `det(Jcs)=0`, so `Jcs`
is not a full-space complex structure. The remaining binary is whether the generation
matter action carries a within-generation real-antisymmetric bilinear; if yes, it must be
the `Jcs` direction, and if no, rank/dimension counting remains.

## Boundary

This note sharpens the source question. It does not select the answer. The result is that
the Kähler-Dirac operator and determinant/Pfaffian counting do not by themselves derive
the per-block `r=1/2` measure.

## Load-Bearing Authorities

[STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md)
[CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
[KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md](KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md)

Non-load-bearing caution: `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28`
is not used as a premise here.

## No-Go Discipline Gate

**N1 - Alternative routes.** Five routes were checked. Route 1: `D_KD` supplies the
within-generation selector; fails because the `Lambda^1` block is zero. Route 2:
determinant/Pfaffian counting gives per-block weighting; fails because both count the
doublet with power 2. Route 3: central `iI_3` selects the doublet measure; fails because
it is generation-blind. Route 4: `Jcs` is a full-space complex structure; fails because
`Jcs^2=-P_doublet` and `det(Jcs)=0`. Route 5: symmetric `C_3`-equivariant mass operators
select a measure; fails because they commute with both candidate structures.

**N2 - Wall independence.** The surviving wall is one binary: whether a
within-generation real-antisymmetric bilinear is present in the matter action.

**N3 - Hidden-wall scan.** The proof distinguishes form-complex `i`, `Jcs`, determinant,
Pfaffian, and matter-action bilinear. No one of these is silently promoted to a selector.

**N4 - Residual matching.** The residual matches the measure selector isolated in the
isotype-split and Kähler-triple notes.

**N5 - Rhetoric audit.** "Silent" means `D_KD` has no grade-diagonal generation block; it
does not mean no later matter-action theorem can supply such a bilinear.

**N6 - Partial-closure path.** A source theorem proving or excluding the real-antisymmetric
generation bilinear could close the binary. This note does not call for an axiom change.

**N7 - Steelman.** The strongest per-block route is that a first-order matter action could
carry a `Jcs` symplectic term even though `D_KD` itself is grade-off-diagonal. This note
leaves that route open.

**N8 - Cross-cycle echo.** The same measure binary appears in the Kähler-triple,
reality-type, record-degeneracy, and K0-real/K0-complex notes. This note removes two
candidate closures and leaves the shared residual explicit.
