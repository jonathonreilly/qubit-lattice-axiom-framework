---
claim_id: scale_ladder_gravity_d4cone_exact_ward_site_scalar_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Supplied model: the Regge second variation of the D4 cone (vertices Z^4 u (Z^4 + u/2) plus the deep holes (e_mu + e_nu)/2, each D4 Delaunay 16-cell coned from its centre; 96 simplices, 72 edge classes; hypercubic edge lengths; index 3 = tick), built by a generic Bloch Regge code with finite-difference dihedral derivatives, and a nearest-neighbour scalar on the Z^4 sites (symbol K0(k) = sum_mu (2 - 2 cos k_mu)) coupled linearly to the relative strains of the 4 axis and 12 face-diagonal site-site segments of each cell. Write x = e^{-i k1}, y = e^{i k2} for the two modes, w = 1/(xy) and d = y - x. (1) The corner stress S_mn = -(1/4) d_m d_n + (1/4)[(w_m - 1)(w_n - 1) - delta_mn sum_l (w_l - 1)^2] satisfies sum_m (w_m - 1) S_mn = -(1/4) d_n (K0(k2) - K0(k1)) at six random complex momentum pairs to 4e-14, so it is exactly conserved on shell; on shell |S - S_min|/|S| falls linearly (1.6e-2, 7.9e-3, 3.9e-3), S_min being the minimal stress with forward differences. (2) The vertex-displacement relative strains of the axis and face segments in the carrier's code equal the symbolic rows 2(w_mu - 1) e_mu, (w_m w_n - 1)(e_m + e_n), (w_m - w_n)(e_m - e_n) to 3e-16; an explicit local map from a symmetric corner tensor to segment couplings (axis S_nn/2 - sum_n' (w_n' - 1) S_nn'/4, face S_mn/2 and -S_mn/2) reproduces sum_m (w_m - 1) S_mn to 2e-16, and on constant metrics the coupling equals (1/2) c(S).h (0.5000). (3) The symmetrised scalar coupling therefore has an on-shell Ward ratio |b . W|/(|b| |W|) <= 3e-14 at finite complex momenta (scales 0.5, 0.1, 0.02), with or without the face combination in (4); moving one tick momentum 10% off shell gives 6e-5 to 4e-3. (4) The face combination N_f = eps_+ + eps_- - (1/2)(four axis strains of the plaquette) is blind to vertex displacements to 1e-16 and its constant-metric reading falls with |k| (1.0e-5, 2.5e-6 at |k| = 0.02, 0.01). (5) Exchange through the edge form (inverted on the complement of the vertex-displacement range) between exactly conserved corner sources, |k| = 0.01, axis, tick, generic and body directions: k^2 times it fits alpha T1*.T2 + beta trT1* trT2 (T = S/2) with alpha = -4.000 and beta = 4/3 without N_f, and alpha = -4.000, beta = 2.000 with N_f weighted by trS/24 (within 3e-4). (6) With that weight the scalar's coupling to the carrier's two non-metric partner modes relative to its metric-mode coupling is 2.8e-3 and 1.4e-3 at |k| = 0.02 and 0.01 (0.85 without it), and the exchange of two on-shell scalar pairs changes under the gauge-fixing weight 1 -> 10 by <= 2e-12. Not claimed: nonlinear statements, uniqueness of the stress or of the face weight, an interacting matter field, the physical status of the partner modes, or any physical identification."
upstream_dependencies:
  - the_regge_second_variation_on_the_4d_cubic_coxeter_complex_carries_a_native_linearised_graviton_bounded_theorem_note_2026-09-03
  - kinetic_isotropy_primitive
  - minimal_axioms
runner: scripts/scale_ladder_gravity_d4cone_exact_ward_site_scalar_2026_10_18.py
---

# A site scalar with an exact lattice Ward identity on the D4-cone Regge carrier

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite floating-point checks on a supplied model.
Nothing is adopted.

## Question

Two open PRs set this up.
- The D4-cone carrier (open PR #9714) has no hidden curvature and an Einstein–Hilbert leading
  symbol. It also has two massless non-metric partner modes.
- Open PR #9774 coupled a site scalar to that carrier through segment strains. With the stress
  evaluated at the segment midpoints, the lattice vertex-displacement Ward identity held to
  relative O(k²), but not exactly.

This note asks whether a local site-scalar coupling can satisfy that Ward identity exactly while
keeping the linearised-EH exchange and decoupling the partners.

## Result (supplied model)

1. **An exactly conserved local corner stress.**
   - Write x = e^{−ik₁} and y = e^{ik₂} for the two modes, w = 1/(xy) for the momentum transfer,
     and d = y − x.
   - The nearest-neighbour symbol obeys an algebraic identity:
     K₀(y) − K₀(x) = Σ_μ (w_μ − 1)(y_μ − x_μ).
   - It follows that
     S_μν = −¼ d_μ d_ν + ¼[(w_μ−1)(w_ν−1) − δ_μν Σ_λ (w_λ−1)²]
     satisfies Σ_μ (w_μ − 1) S_μν = −¼ d_ν (K₀(k₂) − K₀(k₁)) identically. The second bracket
     is identically conserved.
   - So S is exactly conserved on shell. It is local (nearest-neighbour shifts) and symmetric.
   - At leading order it is the minimal stress: the distance falls linearly with |k|.
2. **Segment strains carry any symmetric corner stress exactly.**
   - The vertex-displacement strains of the axis and face segments in the carrier's code are
     2(w_μ − 1)e_μ, (w_m w_n − 1)(e_m + e_n) and (w_m − w_n)(e_m − e_n).
   - A local combination of them gives (w_n − 1)e_m + (w_m − 1)e_n for each pair: face
     couplings ±S_mn/2, and axis couplings −(w_n − 1)S_mn/4 and −(w_m − 1)S_mn/4.
   - Together with axis couplings S_νν/2, this reproduces Σ_μ (w_μ − 1) S_μν exactly.
3. **An exact on-shell Ward identity.** The site scalar coupled this way has
   |b·W| / (|b| |W|) ≤ 3e−14 at finite complex momenta. Moving one tick momentum 10% off shell
   gives 6e−5 to 4e−3.
4. **The partners, and the face weight that removes them.**
   - On its own, this coupling reads the diagonal of the metric through the axes only. Through
     it the exchange between exactly conserved sources is
     −4 (T₁·T₂ − ⅓ trT₁ trT₂)/k², i.e. α = −4 and β = 4/3. That is a conformal partner at
     full strength, as for the face-diagonal reading in PR #9714.
   - Each face carries a strain combination,
     N_f = ε₊ + ε₋ − ½(the four axis strains of the plaquette),
     that is blind to vertex displacements to rounding. Its constant-metric reading falls with
     |k|.
   - Adding N_f with weight trS/24 leaves the Ward identity exact and the metric coupling
     unchanged at leading order. The exchange becomes α = −4.000, β = +2.000 in the axis, tick,
     generic and body directions: the linearised-EH form.
   - The value 1/24 is what cancels the partner coupling. The partner's strains are axis 1,
     face 0, body −½, so the trace coupling ½·trS from the axes is cancelled by 12 × (1/24)·trS
     from the faces.
5. **Exact gauge independence.**
   - With the weight, the scalar's coupling to the partners relative to its metric-mode coupling
     is 2.8e−3 and 1.4e−3 at |k| = 0.02 and 0.01, against 0.85 without it.
   - The exchange of two on-shell scalar pairs changes under the gauge-fixing weight 1 → 10 by at
     most 2e−12. With the midpoint coupling of PR #9774 this was O(k⁴).

## Reading on the ladder (interpretation, not claims)

- **The Ward wall is passed for this matter field.** On the supplied D4-cone carrier, a
  nearest-neighbour site scalar now has three properties at once:
  - its lattice vertex-displacement Ward identity holds exactly on shell;
  - its exchange is the linearised-EH form;
  - its coupling to the non-metric partners vanishes at leading order.

  The identity in item 1 also supplies the compensating field variation. By the standard Noether
  argument, the free action plus this coupling is invariant to first order under a vertex
  displacement combined with a local field variation proportional to d. This is read off the
  identity, not checked separately by the runner.
- **What did the work.** Exact conservation came from an algebraic identity of the
  nearest-neighbour symbol, not from a geometric (finite-element) action. Finite-element matter
  generally has nonzero discrete configurational forces on shell. Partner decoupling came from a
  displacement-blind face strain, the same freedom that the weighting family of PR #9774 exposed.
- **Next targets.**
  - The same construction for the gauge field and for the staggered fermion carriers.
  - An interacting field, where free-field identities no longer suffice.
  - Whether the weight 1/24 or the improvement coefficient ¼ follows from a principle such as
    tick-reflection positivity or a minimal coupling rule.

## Premises

- **Axioms used.** Lattice (Z³ nearest-neighbour adjacency and the tick, for the scalar's
  action).
- **Primitive used.** The kinetic-isotropy primitive, for the hypercubic tick footing.
- **Supplied.**
  - The D4-cone triangulation and the Regge action.
  - The nearest-neighbour scalar.
  - The corner stress S and its improvement coefficient.
  - The segment map.
  - The face combination and its weight.
- **Standard facts used.**
  - The Schläfli identity.
  - The Euclidean linearised-EH exchange form for conserved sources.
  - The Noether argument linking a Ward identity to a compensating field variation.

## Relation to prior work

Citations are from memory and were not checked against the primaries.

- **Weak-field Regge calculus.** Roček and Williams (1981, 1984).
- **Diffeomorphism symmetry in Regge calculus and perfect actions.** Bahr and Dittrich,
  arXiv:0905.1670.
- **Discrete configurational forces in finite elements.** Mesh-optimisation literature (for
  example Thoutireddy and Ortiz, 2004).
- **Lattice energy–momentum tensors.** These are generally not exactly conserved for interacting
  theories (Caracciolo, Curci, Menotti and Pelissetto, 1990).
- **New here.**
  - The exactly conserved local corner stress for the nearest-neighbour scalar, written via
    K₀(y) − K₀(x) = Σ(w − 1)(y − x).
  - Its exact transfer to the D4-cone segment strains.
  - The displacement-blind face combination and the weight 1/24 that decouples the partners.

## No-Go Discipline Gate

- **N1 — routes.**
  - Other improvement coefficients.
  - Body-segment couplings.
  - Other matter fields.
  - Interacting fields.
- **N2/N3 — scope.**
  - One carrier and one scalar.
  - Four Euclidean directions, three complex scales and two on-shell exchange sets.
  - Free field only.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Exact" means at rounding level in floating point. The conservation itself is
  an algebraic identity, checked numerically at random complex momenta.
- **N6/N7 — strongest objections.**
  - Free-field identities do not survive interactions.
  - The weight 1/24 is fixed by the partner condition, not by an independent principle.
  - Leading order only for the exchange form.
- **N8 — earlier claims.** Supersedes the O(k²) Ward order of PR #9774's midpoint coupling for
  this scalar. It does not change any other number there.

## Verification

```bash
python3 scripts/scale_ladder_gravity_d4cone_exact_ward_site_scalar_2026_10_18.py
```

Expected: `TOTAL: PASS=6 FAIL=0` (a few seconds).

## Load-bearing sources

- [Regge 4D complex note](THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md)
- [Kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
