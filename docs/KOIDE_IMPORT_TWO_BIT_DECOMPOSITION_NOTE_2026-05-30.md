# Koide Kähler Triple and Two Independent Selection Bits

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Claim boundary:** finite `C_3` generation geometry and measure-selection localization.
This note does not approve a new convention and does not derive `Q=2/3`.
**Primary runner:**
`scripts/frontier_koide_import_two_bit_decomposition_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_import_two_bit_decomposition_2026_05_30.txt`.

## Result

The `C_3` generation geometry already contains the finite Kähler data:
`Jcs=(C-C^2)/sqrt(3)` generates the `C_3` rotation about the `(1,1,1)` axis, satisfies
`Jcs^2=-P_doublet`, gives the geometric two-form `omega=g.Jcs`, and defines the
holomorphic doublet projector. The runner also checks that the doublet is complex-type
by Frobenius-Schur indicator.

What remains is not a missing two-form. The source residual separates into two
independent data:

- orientation of `Jcs` (`+Jcs` versus `-Jcs`), a sign/readout choice;
- modulus/measure selection, `r=|b|^2/a^2`, where per-block weighting gives
  `r=1/2 -> Q=2/3` and per-dimension weighting gives `r=1 -> Q=1`.

These are independent because every circulant mass operator
`H=aI+bC+conj(b)C^2` commutes with `Jcs` for all `r`. Orienting `Jcs` does not choose
the modulus.

The runner also checks that a symmetric anticommuting mass-operator class has spectrum
`{-s,0,+s}`. That excludes that class as an eigenvalue-mass operator for three nonzero
charged-lepton masses, but it does not refute the separate eigenvector-readout theorem.

## Boundary

This note localizes the residual; it does not close it. Future work must derive or admit
the measure/modulus selector, or derive the rank/dimension route instead.

## Load-Bearing Authorities

[KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
[KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
[STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17.md)
[SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md](SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md)

## No-Go Discipline Gate

**N1 - Alternative routes.** Five routes were checked. Route 1: the Kähler two-form is
missing; fails because `omega=g.Jcs` is constructed from `C`. Route 2: orienting `Jcs`
fixes `r`; fails because `[H,Jcs]=0` for all circulant `H`. Route 3: a symmetric
anticommuting eigenvalue mass operator supplies the route; fails for that readout because
it has a zero eigenvalue. Route 4: representation theory ranks `(1,1)` versus `(1,2)`;
left open by the cited isotype-split note. Route 5: determinant/Pfaffian counting supplies
per-block weighting; handled by the companion Kähler-Dirac note and does not select
per-block weighting.

**N2 - Wall independence.** Orientation and modulus are independent; closing orientation
does not close the measure selector.

**N3 - Hidden-wall scan.** "Kähler," "orientation," and "modulus" are explicit finite
objects. No selector is assumed.

**N4 - Residual matching.** The residual matches the shared Koide measure selector:
per-block `(1,1)` versus per-dimension `(1,2)`.

**N5 - Rhetoric audit.** "Not a missing two-form" is scoped to finite generation
geometry. It does not say the matter action supplies the needed kinetic/measure term.

**N6 - Partial-closure path.** A later source theorem deriving the measure selector, or
an explicit convention, could close the residual without an axiom change.

**N7 - Steelman.** The strongest route is that the geometric `Jcs` orientation combines
with emergent-time quantization to select per-complex-mode counting. This note grants the
geometry and leaves the quantization selector open.

**N8 - Cross-cycle echo.** The same residual appears in the K0-real/K0-complex,
record-degeneracy, and reality-type notes. This note narrows the shape of the residual
without closing it.
