# Koide Reality Type Is Permitted, Not Forced: Real D Does Not Select the Wick Face

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** finite `C_3`/`Jcs` reality-type localization and the associated
per-block versus per-dimension Koide measure comparison. This note does not select the
physical readout or measure.
**Primary runner:**
`scripts/frontier_koide_reality_type_permitted_not_forced_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_reality_type_permitted_not_forced_2026_05_30.txt`.

## Result

Reality of the operator matrix `D` is necessary background for the real/Jcs face, but it
is not sufficient to select that face. A single real anti-Hermitian `D` on an explicitly
complex space supports both:

- the real symplectic bilinear `omega(u,v)=u^T D v`, whose two-dimensional doublet
  Pfaffian counts the doublet once; and
- the Hermitian sesquilinear `h(u,v)=conj(u)^T(iD)v`, whose determinant counts the
  doublet twice.

Thus "real matrix" does not imply "real field" and does not choose between the
Majorana/Pfaffian and Dirac/determinant Wick faces.

## Computed Content

The runner checks:

- `D=Jcs` is real and anti-Hermitian.
- The same `D` defines a nonzero antisymmetric symplectic form and an Hermitian `iD`.
- `Jcs=(C-C^2)/sqrt(3)` spans the `C_3`-equivariant real-antisymmetric operators on
  `R^3`; on the doublet, `Jcs^2=-I_2`, so the doublet is a genuine complex line.
- `Pf(lambda J_2)` has degree 1 while `det(lambda I_2)` has degree 2.
- A Hermitian circulant `H=aI+bC+conj(b)C^2` commutes with `Jcs` and has three distinct
  real eigenvalues for generic complex `b`, so the real/Jcs face is compatible with a
  three-mass signed spectrum.
- `Q=(1+2r)/3`; the per-block reading gives `r=1/2 -> Q=2/3`, while the per-dimension
  reading gives `r=1 -> Q=1`.

## Boundary

The note dissolves one overclaim: `D`-reality alone does not force the per-block Koide
reading. The remaining source problem is a Wick-face/measure selector: derive the
Pfaffian/per-block face, derive the determinant/per-dimension face, or explicitly admit a
convention elsewhere. This note does not add or approve that selector.

The Berry/Wess-Zumino form `B^T Jcs Bdot` is a possible future route because it is
`C_3`-invariant without requiring a continuous `U(1)_b` symmetry. This note only records
that route as open context; it does not prove that the matter action supplies such a term.

## Load-Bearing Authorities

[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
[STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md)
[STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md)
[CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)

Non-load-bearing caution: `KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29`
is not used as a premise for this note.

## No-Go Discipline Gate

**N1 - Alternative routes.** Five routes were checked. Route 1: real `D` forces the
real-field/Pfaffian face; attempted, fails because the same `D` supports the Hermitian
determinant face. Route 2: uniqueness of `Jcs` forces the per-block measure; attempted,
fails because uniqueness supplies a complex structure, not a measure selector. Route 3:
Pfaffian degree 1 beats determinant degree 2; attempted, fails because degree comparison
only distinguishes the two candidate readings. Route 4: a three-real-mass spectrum
excludes the real/Jcs face; attempted, fails because `[H,Jcs]=0` with three distinct real
eigenvalues. Route 5: a `C_3`-invariant Berry/Wess-Zumino term closes the selector;
identified as an open route, not supplied by this note.

**N2 - Wall independence.** The collapsed residual is one selector: Wick face/measure
choice. Field-reality, Pfaffian degree, and Berry-term source are not independent
closures unless one of them actually selects that face.

**N3 - Hidden-wall scan.** "Real," "field," "Pfaffian," "Dirac," and "Berry" are all
kept as explicit algebraic or open-context terms. No phrase is used to smuggle a physical
selector.

**N4 - Residual matching.** The residual matches the isotype/block-weight residual:
per-block `(1,1)` versus per-dimension `(1,2)`. The cited staggered-Dirac and CL3 split
notes supply context for the determinant/complex side, not a selector against the
Pfaffian side.

**N5 - Rhetoric audit.** "Reality of `D` does not force `Q=2/3`" means only that the
real-matrix property does not select the Wick face. It is not a claim that no later
geometric-phase or matter-action theorem could select the per-block face.

**N6 - Partial-closure path.** A source theorem deriving the Berry/WZ term, a source
theorem deriving determinant weighting, or an explicit convention/admission could close
the selector. This note does not call for an axiom change.

**N7 - Steelman.** The strongest pro-per-block route is that the unique `C_3`-equivariant
`Jcs` is the natural doublet complex structure and a geometric phase should count the
doublet once. The runner grants uniqueness and Pfaffian degree; what remains missing is
the source that makes that face physical.

**N8 - Cross-cycle echo.** The same selector appears in the block-weight frontier,
isotype-split, K0-real/K0-complex, D3 record-degeneracy, and records-objectivity notes.
This note narrows one failed route without closing the shared residual.
