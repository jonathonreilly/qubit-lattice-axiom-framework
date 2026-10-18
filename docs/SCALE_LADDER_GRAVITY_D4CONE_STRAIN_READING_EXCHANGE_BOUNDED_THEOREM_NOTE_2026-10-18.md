---
claim_id: scale_ladder_gravity_d4cone_strain_reading_exchange_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied model: the Regge second variation of the D4 cone (vertices Z^4 u (Z^4 + u/2) plus the deep holes (e_mu + e_nu)/2, each D4 Delaunay 16-cell coned from its centre; 96 simplices, 72 edge classes, 8 vertex types; hypercubic edge lengths; index 3 = tick), built by a generic Bloch Regge code with finite-difference dihedral derivatives, and a matter reading L: a least-squares metric fitted to the relative strains delta(l^2)/l^2 of the 24 site-site segments of a cell (4 axes, 12 face diagonals through the holes, 8 body diagonals through the centre), with class weights (w_a, w_f, w_b); w = (1, 1, 1) is the strain reading. Exchanges use the edge form inverted on the orthogonal complement of the exact vertex-displacement range. Floating-point checks at sampled momenta: (1) Static T_tt source; Euclidean test sources n n^T with n = (e_perp, i) (null) and (0,0,0,i) (dust): amplitude ratio 1.99989, 1.99997, 1.99998 at |k| = 0.04, 0.02, 0.015, and k^2 times the dust amplitude 2.00026 -> 2.00005. (2) Lattice-conserved sources (c . L G_site = 0 exactly) at |k| = 0.01 in six directions, including the tick axis and two generic directions with tick component: k^2 times the exchange fits alpha T1*.T2 + beta trT1* trT2 with alpha = -4.0000 and beta = +2.0000 (within 1e-4); the fit residual falls with |k| (about 3e-3 at most at 0.01); the non-metric partners' share is <= 5e-7 and falls 4x on halving |k|. (3) Near the light cone (k_t = i omega, spatial |k| = 0.08, 0.04, three directions), on each shell the largest strain reading of a non-metric null direction is 0.26-0.32 |k| times the largest reading of a metric one. (4) A site-only scalar with nearest-neighbour differences (corner or cell-averaged gradients) and stress coupled through L: for on-shell mode pairs the vertex-displacement Ward ratio |c . L G_site| / (|c| |L G_site|) halves when momenta halve (corner 1.3e-2 at s = 0.1; cell-averaged 3.4e-3), while the cell-averaged stress is continuum-conserved to relative O(k^2). (5) L G_site equals e^{i q . p_row} times the continuum symmetrised gradient on its support, with p = 1/2 along mu and 1/8 across for h_mumu and 1/2 along mu, nu and 1/4 across for h_munu (to 1e-5), plus entries off that support at relative O(k). (6) For two on-shell scalar pairs at momenta q and -q, the exchange changes under the gauge-fixing weight 1 -> 10 by a relative amount that falls 4.8-8.6x on halving the momenta, and differs from -4 (T1.T2 - trT1 trT2/2)/q^2 by a relative amount that falls about 2x. (7) For eight class weightings and two directions, alpha = -4 and beta = 2 - (2/3) rho^2 with rho = 4 (w_a - w_b)/(4 w_a + 12 w_f + 8 w_b), within 3e-4; so the exchange has the linearised-EH trace ratio iff w_a = w_b, for every tested face weight including 0. (8) The weighted fourth moment of the 24 segment directions is isotropic (to 1e-16) iff w_a = w_b; the strain reading differs from the Euclidean pseudo-inverse of the line map (relative misfit 0.65 over all 72 edges, 0.22 over the 44 edges it uses). Not claimed: nonlinear statements, any principle singling out the reading beyond the fourth-moment condition, a site-matter discretisation with an exact Ward identity, the physical status of the partner modes, a PPN value, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_d4cone_strain_reading_exchange_2026_10_18.py
---

# The D4-cone Regge carrier with a strain-fitted matter reading: exchange off the static slice, a site-scalar Ward identity, and why the weights matter

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on a supplied model.
Nothing is adopted.

## Question

The orthoscheme note (open PR #9714) built the D4-cone Regge carrier. Its edge form has no null
directions beyond the vertex displacements, and its leading symbol is −(1/4) EH. It also has two
massless non-metric partner modes. Read through the relative-strain least-squares metric of the 24
site–site segments, the partners appear only at O(k), and a static T_tt source gives h_tt·k² = −2
with h_xx = −h_tt.

This note asks four questions about that supplied carrier:
1. Does the exchange keep the linearised-EH form beyond the static slice: for a null-fluid test
   source, at Euclidean momenta with a tick component, and near the light cone?
2. Does a site-only scalar coupled through this reading satisfy the lattice vertex-displacement
   Ward identity, and if not, at what order does it fail?
3. Is the 1/l⁴ weighting forced, or one choice among several?
4. If it is one choice among several, which condition picks out the readings that work?

## Result (supplied model)

1. **Null-fluid test source: ratio 2.**
   - Take a static T_tt source. Compare two Euclidean test sources: null fluid nnᵀ with
     n = (e_⊥, i), and static dust with n = (0,0,0,i).
   - The ratio of the null-fluid amplitude to the dust amplitude is 1.99989, 1.99997 and 1.99998
     at |k| = 0.04, 0.02 and 0.015.
   - The dust amplitude times k² is 2.000 (the static h_tt·k² = −2 of PR #9714, with the
     Euclidean sign).
2. **Exchange off the static slice: the linearised-EH form.**
   - Use sources that are exactly conserved for this reading (c·L G_site = 0).
   - In six directions at |k| = 0.01 (axis, tick axis, a tick–space face direction, the body
     diagonal and two generic directions), k² times the exchange is
     α T₁·T₂ + β trT₁ trT₂ with α = −4.0000 and β = +2.0000. That is
     −4 (T₁·T₂ − ½ trT₁ trT₂), with the linearised-EH trace ratio −1/2.
   - The partners' share is at most 5e−7 and falls 4× on halving |k|, so it is O(k²).
   - A technical point: two vertex-displacement eigenvalues of the finite-difference edge form sit
     near 1e−9, above a plain pseudo-inverse cutoff. Off the axes the sources overlap them at
     O(k²), and a plain pseudo-inverse then gives wrong exchanges. All exchanges here invert the
     form on the exact orthogonal complement of the displacement range. The earlier static-axis
     numbers are unaffected, because there the overlap is exactly zero.
3. **Near the light cone the partners stay weak.**
   - On the graviton shells k_t = iω (spatial |k| = 0.08 and 0.04; axis, face diagonal and a
     generic direction), the strain reading of the non-metric null directions is 0.26–0.32 |k|
     times that of the metric ones.
   - So on shell the partner coupling is O(k) in amplitude.
4. **Site scalar: the Ward identity fails at relative O(k).**
   - Put a scalar on the Z⁴ sites only, with the nearest-neighbour action
     ½ Σ √g g^{μν} D_μφ D_νφ. Here g = 1 + h, h is read by the strain fit, and D_μ is either
     the corner forward difference or the cell average over the 8 parallel edges.
   - For on-shell mode pairs, the ratio |c·L G_site| / (|c| |L G_site|) halves when the momenta
     halve, for both gradients. The coefficients are 0.13 s (corner) and 0.034 s (cell-averaged).
   - The cell-averaged stress itself is continuum-conserved to relative O(k²). The O(k) failure
     therefore comes from the reading, not from the scalar.
5. **Where the O(k) comes from.**
   - The reading's gradient symbol L G_site equals e^{iq·p_row} times the continuum
     symmetrised gradient on its support.
   - The registration points differ by component:
     - h_μμ: 1/2 along μ and 1/8 across;
     - h_μν: 1/2 along μ and ν, and 1/4 across.
   - It also has entries off the continuum support, at relative O(k).
   - Each segment registers strain at its own midpoint, and the least-squares fit mixes those
     midpoints. So no single-point stress placement can match it.
6. **The physical size of the violation is O(k²).**
   - Exchange two on-shell scalar pairs at momenta q and −q. Changing the gauge-fixing weight
     from 1 to 10 changes the exchange by a relative amount that falls 4.8–8.6× on halving the
     momenta: 2.6e−3 → 5.4e−4 (corner) and 3.1e−4 → 3.6e−5 (cell-averaged).
   - The distance from −4 (T₁·T₂ − ½ trT₁ trT₂)/q² is O(k), from the registration-point
     offsets in item 5.
7. **The weighting is not forced, but one condition is.**
   - Take class weights (w_a, w_f, w_b) on relative strain (axis, face, body). The strain
     reading is (1, 1, 1); uniform weights on δ(l²) are (1, 4, 16).
   - For eight weightings and two directions, α = −4 and β = 2 − (2/3) ρ², with
     ρ = 4 (w_a − w_b) / (4 w_a + 12 w_f + 8 w_b), within 3e−4.
   - So the partner enters as a conformal scalar with coupling ρ. The exchange has the
     linearised-EH form iff w_a = w_b, whatever the face weight. The face weights 0, 1/4, 1 and 4
     all give α = −4 and β = +2.
   - The ratio α/(α+β) = 2/(1 + ρ²/3) reproduces both earlier numbers: 1.9286 for uniform δ(l²)
     (ρ = −1/3, the −0.074 partner weight in the probe workspace) and 1.5 for ρ = ±1 (the
     full-strength conformal partner of the face-diagonal reading in PR #9714).
8. **The condition is isotropy of the fourth moment.**
   - The weighted 24 segment directions have an isotropic fourth moment Σ w v̂⊗v̂⊗v̂⊗v̂ iff
     w_a = w_b (anisotropy 1e−16 when they are equal, and 0.10 and 0.32 for two unequal cases).
   - Equivalently, the least-squares normal matrix of the reading is invariant under all
     rotations, not just under the signed axis permutations.
   - By hand: Σ_μ v̂_μ⁴ is 1 (axis), 1/2 (face) and 1/4 (body), against the isotropic 1/2. The
     anisotropy is therefore 4 w_a(1/2) − 8 w_b(1/4) = 2 (w_a − w_b), proportional to ρ's
     numerator. The face diagonals are already isotropic by themselves, which is why w_f is free.
   - The reading is not the Euclidean pseudo-inverse of the line map (misfit 0.65 over all 72
     edges, 0.22 over the 44 edges the reading uses).

## Reading on the ladder (interpretation, not claims)

- **The carrier passes the next three tests at leading order.** The comparison values are those
  of linearised GR:
  - the null/dust ratio is 2, the value 1 + γ takes in linearised GR;
  - the exchange off the static slice has the EH trace ratio −1/2;
  - the partners couple at O(k) both off shell and on the shells.

  In the supplied model, then, the D4 cone with a fourth-moment-isotropic reading has the
  linearised-GR exchange structure at leading order, not only its static limit.
- **What fixes the reading.** The 1/l⁴ weights are not singled out. What the exchange needs is
  that matter's metric fit have rotation-isotropic normal equations, which here means axis and
  body segments weighted equally in relative strain. That is a one-parameter family (the face
  weight). The condition ties partner decoupling to the reading not preferring the lattice axes,
  which is a cleaner statement than "use 1/l⁴". Interpretation, not a claim: whether a site
  matter field can be made to read the geometry this way from its own dynamics is open.
- **The Ward identity is the next wall.** A naive site scalar coupled through the strain fit
  breaks the lattice vertex-displacement Ward identity at relative O(k). The exchange it
  produces is gauge-dependent only at O(k²). That is harmless for the leading-order statements,
  but it rules out an exact lattice diffeomorphism Ward identity for this coupling. A matter
  action whose stress is evaluated on the same segments and midpoints as the reading would be the
  natural thing to try next.
- **Next targets.**
  - A segment-wise matter coupling: the stress assembled per segment at the segment's midpoint,
    so that it matches the reading's registration points, together with its Ward order.
  - Whether a principle selects the face weight.
  - The O(k⁴) birefringence through the reading.

## Premises

- **Axioms used.** Lattice (Z³ adjacency and its cubic group, for the comparison).
- **Primitive used.** The kinetic-isotropy primitive, for the hypercubic tick footing.
- **Supplied.**
  - The D4-cone triangulation.
  - The Regge action.
  - The hypercubic edge lengths.
  - The segment-strain least-squares reading and its class weights.
  - The site scalar's nearest-neighbour action.
  - The Euclidean test sources and their analytic continuation to a null vector.
- **Standard facts used.**
  - The Schläfli identity.
  - The Euclidean linearised-EH exchange form for conserved sources.
  - Spherical-design moments.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Weak-field Regge calculus.** Roček and Williams, Phys. Lett. B 104, 31 (1981).
- **Linearised Regge calculus as a finite-element complex.** Christiansen (Numer. Math., 2011).
- **Lattice gravitons in linearised Regge calculus.** Dittrich, Freidel and Speziale,
  arXiv:0707.4513.
- **Spherical designs.** Delsarte, Goethals and Seidel (1977).
- **New here.**
  - The exchange of the D4-cone carrier off the static slice through the strain reading.
  - The light-cone partner reading.
  - The site-scalar Ward order and its registration-point origin.
  - The closed form β = 2 − (2/3)ρ² over the class-weight family, and the
    fourth-moment-isotropy condition.

## No-Go Discipline Gate

- **N1 — routes.**
  - Segment-wise matter couplings.
  - Non-site matter with its own displacement Ward identity.
  - Other site–site segment sets (longer segments).
  - Nonlinear readings.
- **N2/N3 — scope.**
  - One carrier and one segment set.
  - Six Euclidean directions, three light-cone directions and two scalar mode sets.
  - Eight weightings.
  - Finite-difference dihedral derivatives (step 1e−6).
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Fails at O(k)" is stated for the two gradients tested and for this reading.
  "Iff w_a = w_b" is the closed form verified over eight weightings, with the fourth-moment
  identity derived by hand.
- **N6/N7 — strongest objections.**
  - Leading order only.
  - Partners could matter nonlinearly.
  - The null source is an analytic continuation of a Euclidean bilinear.
  - The light-cone shells nearly merge at |k| = 0.04 (nullity 36), so the partner ratio there
    uses the classification by metric overlap.
- **N8 — earlier claims.** Extends PR #9714's items 16–17 off the static slice. It does not
  change its numbers.

## Verification

```bash
python3 scripts/scale_ladder_gravity_d4cone_strain_reading_exchange_2026_10_18.py
```

Expected: `TOTAL: PASS=8 FAIL=0` (about 15 seconds).

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
