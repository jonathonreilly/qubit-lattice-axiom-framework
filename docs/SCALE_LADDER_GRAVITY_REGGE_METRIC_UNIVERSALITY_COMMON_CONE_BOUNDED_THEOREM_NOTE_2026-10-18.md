---
claim_id: scale_ladder_gravity_regge_metric_universality_common_cone_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied models on the 4D path (Kuhn) complex on Z^3 x Z_tau (24 path 4-simplices per cell, 15 edge classes), with flat edge lengths l_v^2 = v^T g0 v and g0 = 1 + b u u^T, u = (1,1,1,1): the Regge second variation of the companion notes, a P1 (Whitney 0-form) scalar and a Whitney 1-form Maxwell field. Floating-point checks, with exact group-closure and polynomial-rank computations where stated: (1) Census by numerical rank of polynomial forms. Two-derivative quadratic forms that are invariant and gauge-invariant under linearised diffeomorphisms (spin 2) or U(1) (spin 1) number 1/1/1 for scalar/spin-1/spin-2 under the hyperoctahedral group B4, 2/2/2 under K48 = S4 x {+-1} (the complex's isometries), and 2/2/2 under spatial O_h x tick reversal; no spin-2 mass form is gauge-invariant; K48 together with the tick reflection generates B4 (exact group closure, order 384). (2) The two K48 gauge-invariant spin-2 forms are spanned by linearised Einstein-Hilbert forms of K48-invariant flat metrics (residual 1.6e-14). (3) The Regge O(k^2) symbol equals -(1/4) sqrt(det g0) EH_g0 at b = 0, 0.3, -0.15 to within 1e-5 (Richardson-extrapolated finite differences). (4) The P1 scalar's and Whitney Maxwell's leading symbols equal sqrt(g) times their continuum forms in g0 (b = 0, 0.3; 5e-8). (5) At b = 0.3 the scalar's on-shell tick momentum for a real spatial momentum is complex; at b = 0 it is pure imaginary. (6) At b = 0 the on-shell O(k^4) law omega^2 = k^2 [1 - k^2 (1 + sum n^4)/12] holds for both Regge TT modes and for the P1 scalar in five directions (3.5e-7); Whitney Maxwell is birefringent at this order and distinguishes face+ from face-. (7) At b = 0, on the P1 scalar's exact lattice shell sum_mu 4 sin^2(p_mu/2) = 0, the Regge 15 x 15 edge form has seven null directions at every sampled point (6 directions, |k| up to 2.5; 7th singular value <= 4e-16 relative), against five off shell; Whitney Maxwell is off that shell. (8) At real momenta the Regge form has five null directions at b = 0 and four at b = 0.3, -0.15. (9) The P1 scalar's vertex-displacement Ward response on the lattice shell falls as s^5 under momentum scaling, against s^3 off shell, so conservation holds at leading order and fails at relative order s^2. Not claimed: any all-momentum proof of (7), a mechanism for (7) or (8), interacting or radiative statements, reflection positivity or OS reconstruction of any of these models, a Record-to-geometry map, a common cone for fermions or for the framework's own matter models, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - cubic_coxeter_regge_ok4_lattice_fingerprint_bounded_theorem_note_2026-06-10
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18.py
---

# The gravity rung of the scale ladder: the Regge graviton's cone is the edge-length metric's, and a scalar shares it exactly

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on supplied models, plus
an exact group closure. Nothing is adopted.

## Question

The scale-ladder note (open PR #9702) found that lattice symmetry plus an exact redundancy
leaves one leading form in three lanes. Under the hyperoctahedral group B4 that form is
linearised Einstein–Hilbert, with two polarisations at one speed. That note named a common
light cone as the wall shared by the electron, Maxwell and gravity lanes. It proposed, but did
not run, two gravity probes:
- extract the full symbol of the repository's Regge Hessian;
- test whether a matter stress is a conserved (Noether) source.

This note runs both on the one supplied gravity model where every rung is built: the Regge
second variation on the 4D path complex (companion notes of 2026-06-10 and 2026-09-03).

The complex's isometry group is not B4. It is K48 = S4 × {±1}: permutations of all four axes,
tick included, and the global inversion. There are no single-axis reflections. So the first
question is whether the complex's own symmetry forces the graviton's leading form at all.

## Result (supplied models, b = 0 unless stated)

1. **The complex's symmetry does not force Einstein–Hilbert.**
   - Two-derivative quadratic forms that are invariant and gauge-invariant number 2/2/2 for
     scalar/spin-1/spin-2 under K48.
   - Under B4 they number 1/1/1. Under spatial O_h with tick reversal they number 2/2/2.
   - No spin-2 mass form is gauge-invariant under any of the three groups.
   - K48 together with the tick reflection generates all of B4 (exact closure, order 384).
2. **The extra form is a choice of flat background.**
   - The two K48 gauge-invariant spin-2 forms are exactly the linearised EH forms of the
     K48-invariant flat metrics g0 = a·1 + b·uuᵀ, with u = (1,1,1,1).
   - The second direction is a body-diagonal deformation of the background. It mixes tick
     and space.
3. **Metric universality.**
   - Give the complex edge lengths l_v² = vᵀg0v. Its Regge O(k²) symbol is then
     −(1/4)·√(det g0)·EH_g0: coefficients −0.250000, −0.370810 and −0.158114 at b = 0, 0.3
     and −0.15.
   - So the graviton's leading form and cone are those of the metric its edge lengths encode,
     whatever K48-invariant metric that is. Lattice symmetry selects the family; the
     geometry selects the member.
4. **A common cone at leading order.**
   - Put a P1 scalar and a Whitney 1-form Maxwell field on the same complex with the same
     lengths. Their leading symbols are √g times the continuum scalar and Maxwell forms in
     g0, at b = 0 and 0.3.
   - Every field discretised geometrically on the one complex therefore inherits the same
     leading cone as the graviton, even when that cone is not isotropic.
5. **The body-diagonal deformation is not a real-time theory.**
   - At b = 0.3 the scalar's on-shell tick momentum for a real spatial momentum is complex.
     Under k_t = iE the energy is then not real.
   - At b = 0 it is pure imaginary, so the energy is real.
   - This is the scale-ladder note's g3 obstruction in a new form. Here the deformation that
     would let a field's speed drift is a tilt of the cone along the 4D body diagonal, and it
     is incompatible with a real spectrum. Whether the full interacting dynamics keeps a real
     spectrum (reflection positivity) is not decided here.
6. **The first lattice correction, by exact elimination of the lattice-only edge modes.**
   - The Regge TT pair and the P1 scalar both obey ω² = k²[1 − k²(1 + Σn̂⁴)/12]. The axis,
     face and body values are −1/6, −1/8 and −1/9.
   - The two TT polarisations stay degenerate.
   - This reproduces the OK4 note's Regge numbers by a method independent of its projection
     convention.
   - Whitney Maxwell has a different law at this order. It is birefringent (axis −0.1027 and
     −0.0859) and S4-only: face+ gives −0.0707, face− gives −0.0820.
7. **The exact lattice shell at b = 0.**
   - The 2026-09-03 note (its T3 and T4a) already found nullity seven at refined frequencies
     and supported 4 sinh²(ω/2) = Σ_i 4 sin²(k_i/2) at 32 points. That is the Euclidean form of
     Σ_μ 4 sin²(p_μ/2) = 0.
   - This note re-checks it by direct evaluation on the formula, and adds one identification:
     the formula is exactly the P1 scalar's shell on the same complex.
   - On that shell the Regge edge form has seven null directions at every sampled point. Five are always present: the four vertex
     displacements and the fifth branch. The two TT modes are the other two.
   - The sample covered six directions and |k| up to 2.5; the 7th relative singular value was
     ≤ 4e−16, against ≥ 1.6e−5 for the 6th off shell.
   - So, at the sampled momenta, the graviton propagates with exactly the scalar's lattice
     dispersion, not just at O(k⁴).
   - Whitney Maxwell is not on that shell.
8. **The fifth null direction is special to the hypercubic edge metric.** At real momenta
   there are five null directions at b = 0 and four (the vertex displacements) at b = 0.3 and
   −0.15. Away from b = 0 the coincidence in item 7 also fails beyond leading order (finite
   samples in the probe workspace).
9. **The source is conserved only at leading order.**
   - Hold vertex field values fixed and move the vertices; this gives the P1 scalar's stress
     response.
   - With both legs on shell, its Ward violation falls as s⁵ when all momenta scale by s:
     halving ratios 31.95–31.99. Off shell it falls as s³ (ratios 7.91–8.01).
   - So stress conservation, the condition for coupling the source consistently to the
     exactly gauge-invariant Regge form, is a leading-order cross-rung invariant, broken at
     relative order (a/w)².

## Reading on the ladder (interpretation, not claims)

- **Gravity's cone is carried by geometry, not by lattice symmetry.**
  - The ladder note's mechanism is symmetry plus redundancy leaving one form. On this
    complex it leaves two.
  - What removes the second form is that every field couples to one edge-length metric.
    That is a lattice form of universal coupling.
  - It makes the leading cone common across the graviton, a scalar and a Maxwell field even
    before any symmetry argument.
- **What is still needed for a protected common cone.**
  - Per field, K48 allows one marginal body-diagonal tilt b_f.
  - Radiative corrections in an interacting theory with only K48 could move each b_f
    separately. That is the Collins fine-tuning problem in this geometry.
  - A real spectrum forbids b_f ≠ 0. Adding the tick reflection to K48 gives B4, where one
    form remains per field.
  - So the remaining condition is the reflection-positivity half of the ladder note's
    proposed primitive. The approved kinetic-isotropy primitive already supplies the other
    half: tick and space graded on the same footing (here, S4 permutes the tick with space,
    so no separate tick speed exists).
- **The first correction is shared by the graviton and the scalar, exactly at b = 0.**
  - The ladder's (a/w)² suppression is realised: the leading violation is O(k⁴).
  - The graviton and the P1 scalar share even that correction, exactly on the lattice shell.
  - Whitney Maxwell does not. The standard hypercubic link discretisation of Maxwell has the
    Σ 4 sin²(p/2) shell by construction, and it lives on the axis edges of the same complex.
  - So a common shell beyond leading order depends on the discretisation, while a common
    leading cone does not.
- **The source obligation (scorecard G2) moves.**
  - Conservation of a geometrically coupled matter stress holds at the leading rung and
    fails at relative order (a/w)².
  - The open item is now whether a matter discretisation with exact lattice conservation
    exists on this complex, or whether the residual must be carried as a dimension-six
    effect.

## Premises

- **Axioms used.** Lattice (Z³ and its cubic symmetry, for the spatial face).
- **Primitive used.** The kinetic-isotropy primitive, which puts the tick edge on the same
  footing as the spatial edge.
- **Supplied.**
  - The 4D path complex.
  - The Regge action and its Euclidean signature.
  - Edge lengths from g0.
  - The P1 and Whitney discretisations.
  - The line map from continuum fields to edges.
- **Standard facts used.**
  - Polynomial invariant theory by numerical rank.
  - The linearised EH form.
  - Schur complements.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Weak-field Regge calculus on the hypercubic (Kuhn) lattice.** Roček and Williams, Phys.
  Lett. B 104, 31 (1981); Z. Phys. C 21, 371 (1984). Item 7 may be known there.
- **Linearised Regge dynamics and lattice gravitons.** Dittrich, Freidel and Speziale,
  arXiv:0707.4513; Höhn, arXiv:1411.5672.
- **Convergence of Regge curvature to the continuum.** Cheeger, Müller and Schrader, Commun.
  Math. Phys. 92, 405 (1984). This is the general form of item 3.
- **Whitney forms.** Whitney, Geometric Integration Theory (1957).
- **The path triangulation.** Freudenthal, Ann. Math. 43, 580 (1942); Kuhn (1960).
- **Emergent Lorentz invariance and fine-tuning.** Collins, Perez, Sudarsky, Urrutia and
  Vucetich, PRL 93, 191301 (2004).
- **Reflection positivity.** Osterwalder and Schrader, Commun. Math. Phys. 31, 83 (1973).
- **New here.**
  - The K48 census and its identification with flat backgrounds.
  - The cross-field leading-cone check on one complex.
  - The O(k⁴) comparison across spins.
  - The identification of the 2026-09-03 shell with the P1 scalar's exact shell, and its
    failure at b ≠ 0. The shell itself is the 2026-09-03 note's finding.
  - The fifth-mode dependence on b.
  - The Ward scaling.

## No-Go Discipline Gate

- **N1 — routes.**
  - Other triangulations of Z³ × Z_τ.
  - Other matter discretisations: hypercubic links, Kähler–Dirac.
  - Interacting versions.
  - Lorentzian Regge.
- **N2/N3 — scope.**
  - One complex.
  - Three K48-invariant backgrounds.
  - Sampled momenta.
  - Floating-point ranks.
- **N4 — inputs.** Richardson-extrapolated finite differences; thresholds 1e−12 to 1e−5 as
  printed by the runner.
- **N5 — wording.** "Common cone" means a common leading symbol in these supplied models. No
  speed of any physical field is identified.
- **N6/N7 — strongest objections.**
  - Item 7 is sampled, not proved.
  - Item 5 is stated for the free scalar only.
  - The protection argument relies on reflection positivity, which is not established for
    any of these models.
- **N8 — earlier claims.**
  - Extends the 2026-06-10 and 2026-09-03 Regge notes and the scale-ladder note.
  - Items 6 and 7 at b = 0 re-check those notes' O(k⁴) law and lattice shell by different
    methods; they are not new findings.
  - Narrows that note's gravity probe: "lattice symmetry plus exact linearised-diffeo
    redundancy forces linearised Einstein–Hilbert" holds for B4, not for this complex's own
    group.

## Verification

```bash
python3 scripts/scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18.py
```

Expected: `TOTAL: PASS=12 FAIL=0` (about 30 seconds).

Probe scripts, the findings log and the goal are in
`.claude/science/physics-loops/scale-ladder-gravity-20261018/`.

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [OK4 fingerprint note](CUBIC_COXETER_REGGE_OK4_LATTICE_FINGERPRINT_BOUNDED_THEOREM_NOTE_2026-06-10.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
