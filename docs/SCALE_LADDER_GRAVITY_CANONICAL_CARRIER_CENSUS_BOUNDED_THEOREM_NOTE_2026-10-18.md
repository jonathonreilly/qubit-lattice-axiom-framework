---
claim_id: scale_ladder_gravity_canonical_carrier_census_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied models; floating-point checks (index 3 = tick). Carriers: Z^4 plus a union of half-integer orbits (link midpoints {1}, face centres {2}, cube centres {3}, hypercube centres {4}); Delaunay cells of the periodic set, every non-simplicial face coned from its circumcentre; the Regge second variation with Euclidean lengths. (1) On {4} the builder reproduces the D4 cone (96 simplices, 8 vertex types, 72 edges, volume 1). (2) Edge-form nullity minus vertex-displacement rank (hidden curvature) and massless non-gauge directions minus 6 (partners), at sampled momenta, are 1/0 on Z^4 alone, 0/0 on {1} and {3}, 0/2 on {2} and {4}; the five carriers are invariant under all 384 signed axis permutations. (3) For the 16 Whitney Hodge modes (the square of Dirac-Kahler) at omega = |k| = 0.025, max |lambda|/k^4 over two directions is 8e-7 on {4} and 3e-6 on {2}, and 3e-2 on {1} and 6e-3 on {3}. (4) On {1}, a static T_tt source read through two different site readings that are exact on constant metrics and blind to every non-site vertex displacement gives h_tt k^2 = -2.0000 and h_xx/h_tt = -1.0000 at two momenta, with no curvature-squared term. (5) On {1}, the P1 scalar with lumped mass passes the Gaussian Osterwalder-Schrader test at the site and centre planes (-3e-16). (6) Scaled by 2, the vertices of {1} are exactly the 16 residues of Z^4 mod 2 (every site of each 2^4 block) and those of {4} are the 8 even-parity residues. (7) On {1}, a P1 field on every vertex has on-shell stress with a component along the vertex displacements of 1.6 times its norm, and a uniform-displacement part falling linearly in k. Probe-workspace results, not in the runner: the profile of all 16 sets (15 with the O(k^4) test) and the graviton shells on {1}. Not claimed: completeness beyond this class, a mechanism, nonlinear or interacting statements, positivity for the fermion or graviton, a block-reading rule derived from records, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_canonical_carrier_census_2026_10_18.py
---

# Which Regge carrier? A census of canonical symmetric triangulations, and the zoom-out reading

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on supplied models. Nothing
is adopted.

## Question

Open PRs #9708–#9821 found the D4 cone as a gravity carrier. Is it forced, or one choice among
many?

To make that computable, this note uses a choice-free class of carriers:
- **Vertex sets.** Z⁴ plus any union of the four half-integer orbits, 16 sets in all. The
  orbits are link midpoints {1}, face centres {2}, cube centres {3} and hypercube centres {4}.
- **Cells.** The Delaunay cells of each set.
- **Coning.** Every non-simplicial face, at every level, is coned from its circumcentre. This
  keeps every symmetry of the set.

## Result (supplied models)

1. **The builder reproduces the D4 cone** on {4}.
2. **Profiles.** Hidden curvature is a null direction beyond the vertex displacements. Partners
   are massless directions beyond the 6 of linearised EH.

   | Vertex set | Hidden curvature | Partners |
   |---|---|---|
   | Z⁴ alone | 1 | 0 |
   | {1} | 0 | 0 |
   | {3} | 0 | 0 |
   | {2} | 0 | 2 |
   | {4} (the D4 cone) | 0 | 2 |

   All five carriers are B4-symmetric.
3. **The O(k⁴) matter cone.** For the 16 Dirac–Kähler (Whitney Hodge) modes on ω = k, there is
   no O(k⁴) term on {4} or {2}, and there is splitting on {1} and {3}.
4. **The link-midpoint carrier {1} gives linearised GR with no extra term.** Two different
   consistent site readings give h_tt·k² = −2 and h_xx/h_tt = −1. A consistent reading is exact
   on constant metrics and blind to every non-site vertex displacement.
5. **Reflection positivity.** On {1} the P1 scalar with lumped mass passes the Gaussian
   reflection-positivity test at both planes.
6. **The zoom-out.**
   - Scaled by 2, so one rung out, the vertices of {1} are exactly the sites of each 2⁴ block:
     all 16 residues of Z⁴ mod 2, and nothing else.
   - The D4 cone's vertices are the 8 even-parity sites.
   - So no points between sites are used: {1} is a symmetric triangulation of the site lattice
     itself, read at block spacing 2.
7. **Gravity at that rung reads matter per block.**
   - A P1 field on every site sources the relative displacements of the 16 sublattices at
     O(1). Those displacements are exact null directions of the edge form, so that coupling is
     inconsistent.
   - The uniform (lattice-diffeo) part is only O(k).
   - The consistent readings of item 4 are block readings.

The probe workspace extends items 2–3 to all 16 sets (the O(k⁴) test on 15):
- Hidden curvature appears only for Z⁴ alone and for all four orbits together, which is Z⁴ at
  half spacing.
- An exact O(k⁴) matter cone appears exactly on the even sets {2}, {4} and {2,4}, and all three
  carry partners.
- Every partner-free carrier splits at O(k⁴).
- Every carrier needs zoom 2, 4 or 8. {1}, the D4 cone and Z⁴ alone need zoom 2.

## Reading on the ladder (interpretation, not claims)

- **Where gravity lives.** The owner's answer to "may geometry use points between sites?" was:
  test them, do not use them, and zoom out. The census makes that concrete.
  - At the 1-site rung the canonical triangulation of the sites (Z⁴ alone, coned) hides
    curvature, as the Kuhn complex does.
  - At the 2-site rung the canonical triangulation of all sites, {1}, is clean: no hidden
    curvature, no partners, an EH graviton, GR statics for any consistent block reading, and
    a reflection-positive scalar.
  - So gravity is a 2-rung object built on the sites, with no new points.
- **Selection.** Within this class no carrier has all four of: no hidden curvature, no
  partners, an exact O(k⁴) matter cone, and use of every site. The trade-off is:
  - {1}: every site, clean at linear order, O(k⁴) matter splitting suppressed by (a/w)².
  - The D4 cone: even sites only, an exact O(k⁴) matter cone, two partners that a
    curvature-squared term gaps (PR #9821).

  The smallest clean carrier that uses every site at zoom 2 is {1}.
- **Matter is read per block.** On {1}, matter on every site cannot couple site by site to the
  2-rung geometry. Gravity's source is a block quantity. That is a ladder statement of how
  coarse geometry reads fine matter, and it is the open part of the record-to-geometry bridge.

## Premises

- **Supplied.**
  - The class of carriers.
  - The Regge action.
  - The Whitney and P1 discretisations.
  - Lumped masses.
  - The readings.
- **Axioms used.** Lattice (sites Z³, cubic symmetry).
- **Primitive used.** The kinetic-isotropy primitive, which puts the tick on the same footing
  as space.
- **Standard facts used.**
  - Delaunay cells.
  - Circumcentric coning.
  - The Schläfli identity.
  - The Osterwalder–Schrader criterion for Gaussians.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Delaunay and Voronoi geometry of lattices.** Conway and Sloane.
- **Regge calculus.** Roček and Williams; Hamber and Williams.
- **Whitney forms.** Whitney (1957); Arnold, Falk and Winther (2006).
- **New here.**
  - The census.
  - The parity pattern of the O(k⁴) matter cone and of the partners.
  - The zoom-out identification of {1} with a triangulation of the sites.
  - The per-block reading requirement.

## No-Go Discipline Gate

- **N1 — routes.**
  - Other choice-free constructions.
  - Weighted Delaunay.
  - Larger zooms.
  - Readings that are not blocks.
- **N2/N3 — scope.**
  - The 16-set class.
  - Sampled momenta.
  - One set ({1,2,3}) without the O(k⁴) test.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Selection" and "smallest" are within this class only.
- **N6/N7 — strongest objections.**
  - The class is one construction.
  - The O(k⁴) splitting on {1} is a Lorentz violation suppressed by (a/w)², not zero.
- **N8 — earlier claims.** Places #9714's D4 cone as one member of the class. It does not
  change that PR.

## Verification

```bash
python3 scripts/scale_ladder_gravity_canonical_carrier_census_2026_10_18.py
```

Expected: `TOTAL: PASS=7 FAIL=0` (about 4 minutes).

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
