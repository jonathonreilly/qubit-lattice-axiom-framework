---
claim_id: scale_ladder_gravity_d4_cone_common_cone_spins_zero_one_two_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied models; floating-point checks at sampled momenta (index 3 = tick). (1) On the Kuhn (path) complex with hypercubic edge lengths, a least-squares metric fitted to the relative strains delta(l^2)/l^2 of its 15 edge classes is exact on constant metrics (1e-15) and reads the fifth zero-action null direction of the Regge edge form with norm 0.69-0.75 at three momenta. (2) On the D4 cone (D4 = Z^4 u (Z^4 + u/2) with deep holes; each Delaunay 16-cell coned from its centre), the Whitney 1-form Maxwell form has nullity 8, equal to the rank of the vertex gauge directions, and its leading symbol equals the continuum F^2/2 to 3.1e-8. (3) It has three massless non-gauge directions (eigenvalues falling as k^2), and its next eigenvalue is 1.69 at |k| = 0.01. (4) Near omega = k, both photon polarisations appear on one shell (nullity 8 -> 10 in four directions), with no on-shell O(k^4) term (|alpha| <= 4e-7 at |k| = 0.05). (5) With omega^2 = k^2 (1 + alpha k^2 + beta k^4), the P1 scalar and the photon both have beta = 0 on the axis (|beta| <= 2e-5), and in the face, body and one generic direction the photon's beta is -1/4 of the scalar's (scalar +0.00052, +0.00062, +0.00049) at |k| = 0.3. Not claimed: asymptotic coefficients beyond the sampled momenta, interacting or nonlinear statements, fermions, reflection positivity, the companion graviton statements, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_d4_cone_common_cone_spins_zero_one_two_2026_10_18.py
---

# One cone for spins 0, 1 and 2 on the D4-cone carrier

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on supplied models. Nothing
is adopted.

## Question

The companion PR #9714 introduced the D4 cone: the D4 Delaunay 16-cells, coned from their
centres. On the hypercubic geometry it has three properties:
- symmetry under all signed axis permutations, including the tick reflection;
- no curvature hidden from the quadratic Regge action;
- a leading −(1/4) EH graviton.

That PR also found two things about the graviton and its coupling:
- the graviton's first lattice correction is a split pair of shells, ω² = k²(1 ∓ c k²);
- with a strain-fitted matter reading, the static limit is linearised GR.

This note asks two questions:
1. Does a photon on the same carrier share the cone, and to what order?
2. Does that strain-fitted reading also rescue the Kuhn complex?

## Result (supplied models)

1. **The Kuhn control.**
   - On the Kuhn complex every vertex is a site, so a strain-fitted metric reads all 15 edge
     classes.
   - It is exact on constant metrics, yet it reads the fifth zero-action direction at O(1)
     (norm 0.69–0.75).
   - So the strain-fitted reading does not decouple that direction there. The D4 cone's success
     is not a property of the reading alone.
2. **The photon has no extra null directions.** Whitney 1-form Maxwell on the D4 cone has
   nullity 8, equal to its vertex gauge directions, and its leading symbol is the continuum one.
3. **The photon has no partner modes.** There are three massless non-gauge directions, the
   continuum count, and the next eigenvalue is O(1). This contrasts with the graviton's two
   extra partners on the same complex.
4. **The photon cone through O(k⁴).** Both polarisations sit on one shell, and that shell has no
   O(k⁴) correction in any of the four sampled directions. The P1 scalar on the D4 cone also
   has none (companion PR).
5. **The first difference is at O(k⁶).**
   - With ω² = k²(1 + αk² + βk⁴), both the scalar and the photon have β = 0 on the axis.
   - Elsewhere the photon's β is −1/4 of the scalar's.
   - The scalar's β is small: 5e−4 to 6e−4.

## Reading on the ladder (interpretation, not claims)

| Order | Shared by | Notes |
|---|---|---|
| leading (k²) | scalar, photon, graviton | one cone, set by the shared geometry |
| k⁴ | scalar, photon | no correction for either |
| k⁴ | graviton | split ∓c k² through mixing with its two partner modes |
| k⁶ | — | scalar and photon differ; coefficients ~10⁻⁴ |

- **Ladder suppression.** Each departure is suppressed by powers of a/w. A k⁴ difference
  between the graviton and light enters at relative order (a/w)².
- **The graviton is the outlier because of its partners.** The k⁴ splitting comes from mixing
  with non-metric partner modes; the photon has no partners and no splitting. Removing or
  massing the partners is the remaining improvement, the same target the companion PR names.
- **The Kuhn control locates where the D4 cone helps.** On Kuhn, the strain reading cannot
  separate the hidden direction from metric content, because every vertex is a site.

## Premises

- **Supplied.**
  - The D4 cone.
  - The Kuhn complex.
  - The Regge action.
  - The Whitney and P1 discretisations.
  - The strain-fitted reading.
  - The line maps.
- **Primitive used.** The kinetic-isotropy primitive, for the tick footing.
- **Standard facts used.**
  - Whitney forms.
  - Least squares.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Whitney forms.** Whitney, Geometric Integration Theory (1957).
- **Finite-element exterior calculus.** Arnold, Falk and Winther, Acta Numer. 15 (2006).
- **The D4 lattice and its 16-cell honeycomb.** Conway and Sloane, Sphere Packings, Lattices
  and Groups.
- **Linearised Regge calculus on hypercubic lattices.** Roček and Williams (1981, 1984).
- **New here.**
  - The Whitney photon on the D4 cone and its order-by-order cone comparison with the scalar.
  - The Kuhn strain-reading control.

## No-Go Discipline Gate

- **N1 — routes.**
  - Other discretisations of Maxwell on the D4 cone.
  - Fermions.
  - Partner-free gravity carriers.
- **N2/N3 — scope.**
  - Sampled momenta and four directions.
  - Floating-point roots.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "One cone" means a common leading symbol and the stated on-shell orders, in
  these supplied models.
- **N6/N7 — strongest objections.**
  - The β ratio is sampled at one |k|.
  - Item 1 shows one reading fails on Kuhn. It does not rule out other readings.
- **N8 — earlier claims.** Extends PR #9714. It does not change it.

## Verification

```bash
python3 scripts/scale_ladder_gravity_d4_cone_common_cone_spins_zero_one_two_2026_10_18.py
```

Expected: `TOTAL: PASS=5 FAIL=0` (about 90 seconds).

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
