---
claim_id: scale_ladder_gravity_orthoscheme_zero_action_curvature_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied Regge second variations of three translation-periodic triangulations of Z^3 x Z_tau, built by a generic Bloch Regge code that reproduces the landed Kuhn-complex module's edge form to 1.3e-8. Floating-point checks at sampled momenta: (1) Kuhn (path) complex with hypercubic edge lengths: the edge form has nullity five while the linearised deficit map has rank fifteen minus four, so the null direction beyond the vertex displacements has nonzero linearised curvature (|D x|/|D| >= 0.59) and zero quadratic Regge action. (2) The barycentric subdivision of the cubical complex (384 simplices, all orthoschemes; 240 edge classes; 16 vertex types per cell; symmetric under signed permutations of all four axes, including the tick reflection): nullity 80 = 64 vertex displacements + 16, with a singular-value gap of 6e6 or more; the 16 extra directions have nonzero linearised curvature, and four or five of them have metric share above 0.2. (3) Kuhn complex, hypercubic lengths: the P1 scalar stiffness equals sum_mu 4 sin^2(p_mu/2) (deviation 1.4e-15 at complex momenta), and the on-shell tick momentum is pure imaginary for real spatial momenta. (4) Lengths from g0 = 1 + 0.3 u u^T (u = (1,1,1,1)): Re k_t / |k| tends to a nonzero constant (0.27). (5) Lengths from g0 = 1 + c u_s u_s^T (u_s = (1,1,1,0), c = 0.2, 0.05): the fifth null direction is lifted, the eliminated non-metric edge block is stiff, and Re k_t / |k| falls as |k|^2. (6) At c = 0.2 the full edge form with non-metric edges eliminated has O(k^2) symbol -(1/4) sqrt(det g0) EH_g0 (misfit 3.2e-8). (7) The D4 cone: vertices D4 = Z^4 u (Z^4 + u/2) plus the deep holes (e_mu + e_nu)/2, each Delaunay 16-cell coned from its centre; 96 simplices tile the cell (volume 1 to 1e-12), the simplex set is invariant under all 384 signed axis permutations, and no simplex is an orthoscheme; 72 edge classes, 8 vertex types. (8) Its edge form has nullity 32, equal to the rank of the vertex displacements, at three momenta (gap 7e7 or more). (9) With non-metric, non-gauge edge directions eliminated, its O(k^2) symbol is -(1/4) EH (misfit 2.7e-5). (10) Its P1 scalar has pure imaginary on-shell tick momentum for real spatial momenta (|Re| <= 4e-16), and no on-shell O(k^4) correction (|alpha| <= 2.5e-5, 4 directions). (11) Near the light cone its edge form has two real shells omega^2 = k^2 (1 -+ c k^2), with c = 1/12 (axis) and 1/16 (face diagonal), each adding one metric and one non-metric null direction; on the body diagonal they coincide (nullity 35, c = 0 within 4e-4). (12) It has 8 massless non-gauge directions (linearised EH has 6); the on-shell P1 stress overlaps the 2 non-metric ones with a fraction that halves when momenta halve. Not claimed: that every orthoscheme triangulation has such directions, any mechanism, nonlinear statements, that these directions are or are not symmetries of the nonlinear action, reflection positivity, that the D4 cone is unique or preferred, the physical status of its two non-metric massless modes, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_orthoscheme_zero_action_curvature_2026_10_18.py
---

# Orthoscheme Regge carriers hide curvature from the quadratic action; a D4-cone carrier does not

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on supplied models. Nothing
is adopted.

## Question

The scale-ladder gravity note (open PR #9708) found three things on the 4D path (Kuhn) complex
with hypercubic edge lengths:
- the Regge edge form has a fifth null direction beyond the four vertex displacements;
- its metric part is uuᵀ − 2·1 modulo gauge;
- a geometrically coupled (P1) scalar sources it, so the linearised field equations have no
  solution in that channel.

Moving the background off the hypercubic point lifts the direction. But the body-diagonal
deformation that does so makes energies complex.

This note asks three questions:
1. Is the fifth direction a hidden flat deformation, or curvature?
2. Does a triangulation with the tick reflection, which the Kuhn complex lacks, avoid it?
3. Which deformations lift it while keeping the energies real?
4. Is there a triangulation with all three properties: cubic covariance with the tick on the
   same footing, a real spectrum, and no hidden curvature?

## Result (supplied models)

1. **It is curvature, not a flat deformation.**
   - On the Kuhn complex with hypercubic lengths, the linearised deficit map D (hinges × edges)
     has rank 15 − 4, so only the vertex displacements are flat. This agrees with the fact that
     a flat simplicial metric on a simply connected complex develops into ℝ⁴.
   - The edge form Q = A′ᵀD (A′ the area gradients) nevertheless has nullity 5. The fifth null
     vector has |Dx|/|D| ≥ 0.59.
   - So it is a curvature pattern whose deficits are orthogonal to every area variation: the
     quadratic Regge action does not see it.
2. **A B4-symmetric triangulation with the tick reflection does not avoid it.**
   - The barycentric subdivision of the cubical complex has 384 simplices, 240 edge classes
     and 16 vertex types per cell. It is symmetric under all signed axis permutations,
     including the tick reflection.
   - Its edge form has nullity 80 at every sampled momentum: 64 vertex displacements plus 16
     extra directions, with a singular-value gap of 6e6 or more.
   - The extras are curved (|Dx|/|D| ≥ 0.33). Four or five of them have metric share above
     0.2.
   - Every one of its simplices is an orthoscheme (each step changes one coordinate by 1/2),
     as are the Kuhn simplices with hypercubic lengths.
3. **The hypercubic point's real spectrum is itself an orthoscheme effect.**
   - With hypercubic lengths, the P1 scalar on the Kuhn complex is exactly the
     nearest-neighbour Laplacian Σ_μ 4 sin²(p_μ/2), at complex momenta to 1.4e−15.
   - That operator is symmetric under the tick reflection, although the complex is not. So the
     on-shell tick momentum is pure imaginary for real spatial momenta, and the energies are
     real.
4. **Tilt: non-real at leading order.** For g0 = 1 + 0.3 uuᵀ, Re k_t/|k| tends to 0.27 as
   |k| → 0.
5. **Spatial trigonal skew: non-real only at relative order k².**
   - For g0 = 1 + c u_s u_sᵀ with u_s = (1,1,1,0) and c = 0.2 or 0.05, the fifth direction is
     lifted, and the eliminated non-metric edge block is stiff (eigenvalue ≥ 2.6).
   - Re k_t/|k| falls by 3.99 per halving of |k|. The departure from a real spectrum is
     therefore an (a/w)²-suppressed effect.
6. **Metric universality of the full form at the skew.** At c = 0.2, the full edge form with
   the non-metric edges eliminated has symbol −(1/4)·√(det g0)·EH_g0 (misfit 3.2e−8).

7. **A carrier with all three properties: the D4 cone.**
   - Add the hypercube centres to Z⁴. This gives the D4 lattice, whose Delaunay cells are
     regular 16-cells centred at the deep holes (e_μ + e_ν)/2.
   - Cone each 16-cell from its centre over its 16 tetrahedral facets. The resulting 96
     simplices tile the cell, the complex is invariant under all 384 signed axis permutations
     (spatial cubic group and tick reflection), and no simplex is an orthoscheme.
8. **No hidden curvature.** Its edge-form null directions are exactly its 32 vertex
   displacements.
9. **Einstein–Hilbert.** With non-metric, non-gauge edge directions eliminated, its leading
   symbol is −(1/4) EH.
10. **Real energies and a clean scalar.**
    - The P1 scalar on the D4 cone has real energies.
    - It has no on-shell O(k⁴) correction, consistent with the larger symmetry of the D4
      tiling, which forbids quartic anisotropy.
11. **The graviton's first correction is a split pair.**
    - Two real shells, ω² = k²(1 ∓ c k²), with c = 1/12 on the axis, 1/16 on the face diagonal
      and 0 on the body diagonal.
    - Each shell adds one metric (TT) null direction and one non-metric one, so the TT pair is
      birefringent at O(k⁴).
12. **The price: two non-metric massless partner modes.**
    - There are 8 massless non-gauge directions; linearised EH has 6. The extra two are
      non-metric, sit on the same leading cone, and mix with the TT pair at O(k⁴).
    - On-shell matter couples to them only at relative order k (the overlap halves per
      halving). An exchange between matter sources through them is therefore suppressed by
      (a/w)² relative to the graviton.

## Reading on the ladder (interpretation, not claims)

- **The gravity rung's wall, narrowed and then passed by one carrier.** The Kuhn complex can
  have any two of three properties, but not all three:
  - a cubically covariant geometry with the tick on the same footing (the hypercubic lengths
    the kinetic-isotropy primitive points to);
  - a real spectrum at leading order;
  - no curvature that the quadratic action cannot see, so that geometrically coupled matter
    has a well-posed linear response.

  | Background | Covariant + same footing | Real at leading order | No unseen curvature |
  |---|---|---|---|
  | hypercubic | yes | yes | no |
  | spatial skew | no | yes | yes |
  | tilt | no | no | yes |

  The symmetric barycentric subdivision does not help: it has more unseen-curvature directions.
- **The D4 cone has all three.**
  - It has the hypercubic geometry, cubic and tick-reflection symmetry, real energies, and no
    hidden curvature, and its leading graviton is Einstein–Hilbert.
  - Its costs are visible and suppressed:
    - two non-metric massless partner modes, coupled to matter at relative order a/w;
    - O(k⁴) birefringence of the TT pair.
  - Its vertices go beyond the sites: the hypercube centres and the deep holes. On the ladder,
    the gravity carrier lives on a refined geometric rung, as the corner fermion lives on a
    blocked one.
- **The orthoscheme pattern.** Both complexes with hidden curvature are built from
  orthoschemes; the one without is not. This is a correlation across three complexes, not a
  theorem.
- **Next targets.**
  - Whether the D4 cone's partner modes can be removed by a different coning, or are forced.
  - The D4 cone's Ward identity for P1 matter.
  - Its Newtonian rung.
  - A proof of the closed form for c(n̂). The candidate c² = [(1 − S₂)² − 12 T]/144, with
    S₂ = Σ_{i<j} n̂ᵢ²n̂ⱼ² and T = n̂ₓ²n̂ᵧ²n̂_z², was read off four directions. It predicts three
    further directions to within 0.4% at |k| = 0.05 (probe workspace, not in the runner).

## Premises

- **Axioms used.** Lattice (Z³ adjacency and its cubic group, for the comparison).
- **Primitive used.** The kinetic-isotropy primitive, for the hypercubic tick footing.
- **Supplied.**
  - The two triangulations.
  - The Regge action.
  - The edge lengths from g0.
  - The P1 scalar.
  - The line map to metric variables.
- **Standard facts used.**
  - The Schläfli identity (second variation = area gradients times deficit gradients).
  - Developability of flat simply connected simplicial metrics.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Weak-field Regge calculus on the hypercubic (Kuhn) lattice.** Roček and Williams, Phys.
  Lett. B 104, 31 (1981); Z. Phys. C 21, 371 (1984). Extra zero modes may be discussed there.
- **Linearised Regge calculus as a finite-element complex.** Christiansen, "On the
  linearization of Regge calculus" (Numer. Math., 2011).
- **Linearised Regge dynamics and lattice gravitons.** Dittrich, Freidel and Speziale,
  arXiv:0707.4513; Höhn, arXiv:1411.5672.
- **Orthoschemes and the path triangulation.** Freudenthal (1942); Kuhn (1960).
- **New here.**
  - The curvature (not flatness) of the Kuhn fifth direction.
  - The barycentric count and its metric content.
  - The tilt/skew comparison of real spectrum against unseen curvature.
  - The D4-cone carrier and its graviton, scalar and partner-mode properties.

## No-Go Discipline Gate

- **N1 — routes.**
  - Non-orthoscheme triangulations with cubic and tick-reflection symmetry.
  - Extra vertex sets.
  - Matter with a Ward identity for these directions.
  - Nonlinear lifting.
  - Lorentzian Regge.
- **N2/N3 — scope.**
  - Two triangulations.
  - Three backgrounds per family.
  - Sampled momenta.
  - Finite-difference dihedral derivatives (step 1e−6), with a floor of about 1e−10.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Cannot have all three" is a statement about the carriers tested, not about
  all triangulations.
- **N6/N7 — strongest objections.**
  - Orthoscheme-ness is a correlation across three complexes, not a proof.
  - The D4 cone's partner modes are massless and could matter at nonlinear order.
  - The skew's non-real (a/w)² term is small but nonzero.
  - The direction might be harmless nonlinearly.
- **N8 — earlier claims.** Sharpens the companion note's fifth-direction items. It does not
  change the 2026-09-03 note's counts.

## Verification

```bash
python3 scripts/scale_ladder_gravity_orthoscheme_zero_action_curvature_2026_10_18.py
```

Expected: `TOTAL: PASS=13 FAIL=0` (about 50 seconds).

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
