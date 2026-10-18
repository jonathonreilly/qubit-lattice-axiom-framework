---
claim_id: scale_ladder_gravity_d4_cone_fermion_cone_reflection_positivity_curvature_squared_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied models on the D4 cone (D4 = Z^4 u (Z^4 + u/2) with deep holes; each Delaunay 16-cell coned from its centre) and on the Kuhn (path) complex, hypercubic geometry, index 3 = tick; floating-point checks at sampled momenta. (1) The Whitney complex of the D4 cone has 8, 72, 208, 240, 96 classes of degree 0-4 per cell, d^2 = 0 to 2e-16, Euler characteristic 0, and positive mass matrices. (2) The Whitney Hodge Laplacians (the square of the Dirac-Kahler operator d - delta) have exactly C(4,k) = 1, 4, 6, 4, 1 eigenvalues falling as k^2 per degree, all equal to k^2 to 3e-6 at |k| = 0.01, and the next eigenvalue is at least 25. (3) At p = (k n, i k) with |k| = 0.05 on the axis and one generic direction, those 16 eigenvalues are at most 3.1e-9 k^2 (an O(k^4) on-shell term would give about 1e-4 k^2). (4) The OS reflection-positivity test (positive semidefiniteness of the reflected covariance on one half of an N_t = 6 time torus) passes for the nearest-neighbour Laplacian and fails for a higher-derivative scalar (-2.7e-2) and for the D4-cone P1 scalar with its consistent mass matrix (-9.3e-5). (5) The D4-cone P1 scalar with lumped mass passes at the site plane and at the centre plane for two spatial momenta (-2e-16). (6) The D4-cone Whitney 1-form with curl-curl action and diagonal mass passes at both planes (-1.6e-14); with the consistent mass it fails (-9.2e-4). (7) Adding lambda sum_h delta_h^2 with lambda = -0.1 to the Regge second variation reduces the Kuhn edge form's nullity from 5 to 4 and the D4 cone's massless non-gauge directions from 8 to 6. (8) With that term, neither complex has rank drops at real tick momentum in (0, 3) at |k_s| = 0.05, and both have the root omega = 0.05. (9) With that term, a static T_tt source read through the D4 face-diagonal site metric, or through either of two least-squares Kuhn readings, gives h_tt k^2 = -2.000 and h_xx/h_tt = -1.000 to 2e-4 at two momenta. (10) At |k| = 1 the D4 response gives h_tt k^2 = -1.84, not an exact lattice Poisson equation. Not claimed: reflection positivity of the Dirac-Kahler fermion or of the graviton (the Euclidean conformal mode is unbounded), massless-limit or interacting statements, positivity of the curvature-squared action, its high-energy (Stelle-type) ghosts, a derivation of lengths or of the source from records, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_d4_cone_fermion_cone_reflection_positivity_curvature_squared_2026_10_18.py
---

# The D4-cone carrier: a fermion on the common cone, a positive transfer matrix for its scalar and photon, and a curvature-squared term that gaps the extra modes

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on supplied models. Nothing
is adopted.

## Question

Open PRs #9714, #9772 and #9774 built the D4 cone, a B4-symmetric Regge carrier on the
hypercubic geometry. On it:
- the scalar, the photon and the graviton share the leading cone;
- the scalar and the photon also share it through O(k⁴);
- the graviton carries two massless partner modes;
- with a strain-fitted matter reading, its static limit and its light bending match
  linearised GR.

That work left three questions:
1. Does a fermion share the cone?
2. Are the free fields reflection positive, so that a real-time Hamiltonian exists?
3. Can the extra modes be removed without relying on a particular matter reading?

## Result (supplied models)

1. **A fermion on the common cone.**
   - The Dirac–Kähler operator d − δ squares to minus the Hodge Laplacian on forms of every
     degree. Here it is built from Whitney forms on the D4 cone.
   - The Hodge Laplacians have exactly C(4,k) massless modes per degree, 16 in all: the
     Dirac–Kähler count of 4 Dirac fields × 4 tastes, with no doublers.
   - All of them sit at λ = k² (the common cone), and the next level is at least 25.
2. **No O(k⁴) term for any fermion component.** On the continuum shell ω = k, all 16 are null
   to O(k⁶). So the fermion shares the cone with the scalar and the photon through O(k⁴), and
   only the graviton departs at that order.
3. **The reflection-positivity test discriminates.**
   - The test asks whether the reflected covariance on one half of a time torus is positive
     semidefinite.
   - It passes for the nearest-neighbour Laplacian, and fails for a higher-derivative scalar
     and for the D4-cone P1 scalar with its consistent mass matrix. That mass matrix couples
     across the plane with the wrong sign.
4. **The D4-cone scalar and photon are reflection positive.**
   - The P1 scalar with lumped mass passes at both inequivalent tick planes, the one through
     the sites and the one through the cell centres. All 72 of its stiffness couplings are
     ferromagnetic or zero.
   - The Whitney 1-form field with diagonal mass also passes at both planes.
   - So, with lumped masses, both define positive transfer matrices: a real-time Hamiltonian.
5. **A curvature-squared term gaps the extra modes.**
   - Add λ Σ_h δ_h² with λ = −0.1, a lattice curvature-squared term of the Hamber–Williams
     type.
   - It lifts the Kuhn complex's fifth null direction, leaving only the vertex displacements.
   - It gaps the D4 cone's two partner modes; the next eigenvalue is 1.37 at |k| = 0.01.
   - On metric modes the deficits are O(k²), so the term changes the graviton only at O(k⁴).
   - There are no tachyonic roots, and the light-cone root survives. The new massive modes lie
     near the cutoff: 1.9 on Kuhn; 2.75 and 2.95 on the D4 cone.
6. **Linearised GR for any reading tested, on either complex.**
   - With the term, a static T_tt source gives h_tt·k² = −2 and h_xx/h_tt = −1.
   - This holds on the D4 cone through the face-diagonal reading. That reading gave a −2/3
     conformal partner without the term.
   - It also holds on the Kuhn complex, whose linear response was ill-posed without the term.
7. **Not an exact lattice Poisson equation.** At |k| = 1 the D4 response departs from −2/k²
   and from −2/Σ 4 sin²(k/2), by about 8% and 16%. The corrections are O(k²), as expected from
   the massive modes (a short-range Yukawa-type correction).

## Reading on the ladder (interpretation, not claims)

| Field on the D4 cone | Leading cone | O(k⁴) | Reflection positive (tested) |
|---|---|---|---|
| scalar (P1, lumped mass) | yes | none | yes |
| photon (Whitney 1-form) | yes | none | yes, with a mass regulator |
| fermion (Dirac–Kähler, 16 = 4 × 4) | yes | none, all degrees | open |
| graviton (Regge) | yes | split ∓c k² | ill-posed (conformal mode) |

- **The common light cone, for this supplied family.** One geometric carrier gives one cone
  for spins 0, ½, 1 and 2. Spins 0, ½ and 1 share it through O(k⁴). The scalar and the photon
  have a positive transfer matrix.
- **The extra-mode problem has a local fix.** The hidden-curvature and partner modes of
  #9708, #9714 and #9774 carry curvature, so a curvature-squared term gives them a mass near
  the cutoff. Linearised GR then follows without choosing a matter reading.
- **Costs of the fix.**
  - The sign of λ is fixed by requiring no tachyons.
  - The new massive modes are Stelle-type: in continuum language, curvature-squared gravity
    has a massive spin-2 ghost. Their sign and norm need the same scrutiny as the conformal
    mode.
- **What stays open.**
  - Reflection positivity for the fermion and for gravity.
  - Interacting statements.
  - A derivation of the lengths, and of the identification of T_tt, from records. The bridge
    note of 2026-09-03 supplies lengths from a potential; this carrier reproduces its ν = 1
    selection at leading order but does not derive the potential.

## Premises

- **Supplied.**
  - The D4 cone and the Kuhn complex.
  - The Regge action and the curvature-squared term with its coefficient.
  - The Whitney, P1 and Dirac–Kähler discretisations.
  - Lumped and diagonal masses.
  - The readings.
- **Primitive used.** The kinetic-isotropy primitive, for the tick footing.
- **Standard facts used.**
  - Whitney forms and their mass matrices.
  - The Osterwalder–Schrader criterion for Gaussian measures.
  - The Schläfli identity.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Dirac–Kähler fermions on the lattice.** Becher and Joos, Z. Phys. C 15, 343 (1982); Rabin,
  Nucl. Phys. B 201, 315 (1982).
- **Reflection positivity.** Osterwalder and Schrader (1973); Osterwalder and Seiler (1978).
- **Curvature-squared Regge gravity.** Hamber and Williams (1984 onward).
- **Ghosts in curvature-squared gravity.** Stelle, Phys. Rev. D 16, 953 (1977).
- **Whitney forms and finite-element exterior calculus.** Whitney (1957); Arnold, Falk and
  Winther (2006).
- **The repository's Dirac–Kähler lane** uses a different carrier: a cochain DK with the
  sin² k shell.
- **New here.**
  - The D4-cone Dirac–Kähler cone count and its O(k⁴) statement.
  - The reflection-positivity results and their mass-matrix dependence.
  - The curvature-squared gap on both carriers, with reading-independent linearised GR.

## No-Go Discipline Gate

- **N1 — routes.**
  - Fermion reflection positivity (Grassmann OS).
  - Gravity reflection positivity with a conformal-mode prescription.
  - Other mass lumpings.
  - Other signs and sizes of λ.
- **N2/N3 — scope.**
  - One torus length (N_t = 6).
  - Two spatial momenta for reflection positivity.
  - Sampled momenta elsewhere.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Reflection positive" refers to the tested Gaussian measures only.
- **N6/N7 — strongest objections.**
  - The curvature-squared term is a supplied action term.
  - Its high-energy modes need a positivity analysis.
  - Item 3 tests two directions.
- **N8 — earlier claims.** Extends #9714, #9772 and #9774. It removes the need for #9714's
  strain-fitted reading once the term is present.

## Verification

```bash
python3 scripts/scale_ladder_gravity_d4_cone_fermion_cone_reflection_positivity_curvature_squared_2026_10_18.py
```

Expected: `TOTAL: PASS=10 FAIL=0` (about 30 seconds).

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
