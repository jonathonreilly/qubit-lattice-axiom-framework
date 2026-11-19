---
claim_id: the_sign_of_the_mass_angle_picks_one_cube_fold_of_the_two_tiling_tick_and_its_misfolds_are_the_matter_fermions_while_dimer_resonance_and_symmetric_window_rules_leave_the_3d_fold_unselected_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Finite exact diagnostics. Pair (dimer) coverings enumerated on 4x4, 6x6, 8x8 and 4x4x4 tori. Quantum dimer resonance H = -t sum flip + v sum flippable: exact extreme ends (v -> -inf, v > t), the RK point's tiling balance, the one-cube problem, product-crystal energies, and an exact 6x6 control. The CL-1 cube hop R (edge hops with spin-3/2 overlap phases) on one cube (256-state Fock space) and the two-tiling tick, even step eps - mu/2 and odd step eps + mu/2, on the 8^3 torus and 16xLxL slabs (L = 4, 6), single-particle, eps = 0.3, copy mass M = 0.2 in one check. Tile-level window rules on 8x8, 12x12 and 4^3 tilings by 2^d tiles. Results: the 3D landscape of any partner-in-star rule has >= 9^(N/8) folds; dimer resonance picks the columnar states at v -> -inf (3 axes x 2 offsets, each inside one CL-1 tiling), a highly degenerate no-resonance set for v > t, and no fold at the RK point; the cube crystal is the best product crystal for -0.802 < v/t < 0.671, but the exact 2D control shows product energies do not decide the phase; the cube's four-unit vacuum is 91% in the span of its nine pair coverings, and the cube tick is not a plaquette flip; the two-tiling tick's quasi-energy gap is exactly |mu|, so every mu < 0 vacuum is continuously the even-cube fold and every mu > 0 vacuum the odd-cube fold, with every site bound by the face-mirror condition at the limits; point misfolds are odd cubes, which are fermions in a 4-state level split 2 + 2 by the copy sign, costing |mu|; wall misfolds carry gapless 2+1 fermions; a symmetric 3^d window rule leaves 2^O(L^(d-1)) sliding folds, and a 2x5 anti-slide window leaves only the aligned 2D crystals; the fewest-change transport cannot select. Toy and finite: the fold has no free sites, its strength at physical masses is ~1e-22, and the nested role-block layout is not produced."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_sign_of_the_mass_angle_picks_one_cube_fold_of_the_two_tiling_tick_and_its_misfolds_are_the_matter_fermions_while_dimer_resonance_and_symmetric_window_rules_leave_the_3d_fold_unselected_2026_10_22.py
---

# The sign of the mass angle picks one cube fold of the two-tiling tick, and its misfolds are the matter fermions; dimer resonance and symmetric window rules leave the 3D fold unselected

Claim type: bounded_theorem. The candidate-law register has zero premise weight. Axiom text is unchanged. Lattice: "No site is privileged." Record: "When present, a record locks exactly one admissible local possibility."

## Question

neighbourhood-roles found that the uniform star rule folds uniquely in 1D, as two pair coverings, but has a massively degenerate zero-phase manifold in 2D and 3D. So a rule that selects the fold is missing. This note tests four candidates on small exact models:
- (a) quantum resonance of pairs (order by disorder);
- (b) the CL-1 cube tick itself;
- (c) a frustration-free cube rule;
- (d) the fewest-change transport.

The target is a unique fold, up to symmetry, that is commensurate with the 2^3 cubes.

## Results

### A. Landscape

**A1 [T]. Corrected 2D counts.** The 4x4 and 6x6 tori have 272 and 90176 pair coverings. The neighbourhood-roles figures (121, 28561) leave out the coverings that wrap around the torus. Those figures are lower bounds, so that note's conclusion stands.

**A2 [T]. A 3D lower bound.** Pairings inside the even cubes alone give 9^(N/8) zero-phase folds of any rule that is zero when a site's partner sits in its star. That is an entropy of at least ln9/8 = 0.275 nats per site.

### B. (a) Dimer resonance

**B1 [T]. The v -> -inf end is columnar.** The number of flippable plaquettes obeys N_f <= N, and equality forces the columnar states: 6 on 4x4x4 (3 axes x 2 offsets).
- Each columnar state lies wholly inside the cubes of ONE CL-1 tiling.
- Each breaks the 24 rotations down to those about one axis.

**B2 [T+D]. The v > t side is degenerate.** The ground states are the coverings with no flippable plaquette.
- 2D: 4(2^(L/2) - 1) of them.
- 3D: 20000 or more on 4x4x4 (the search stopped at its cap).

There is no unique fold on this side.

**B3 [T]. The RK point selects no fold.** In each sector the ground state is the equal-weight sum. The (1,1,1) translation swaps the tilings and maps sector W to -W, so the zero-flux sector puts exactly half the pairs in each tiling. In 3D the RK point sits in the Coulomb liquid (literature, not computed here): no crystal.

**B4 [T]. One cube.** A cube has 9 coverings. It has a unique, gapped resonating ground state with e_c = 3v - sqrt(v^2 + 8).

**B5 [T]. Product crystals.** Per site, the cube crystal's energy e_c/8 + v/6 is below the columnar state's (v) and the no-resonance states' (0) for -0.802 < v/t < 0.671.

**B6 [D]. 2D control.** The exact 6x6 ground energy lies about 0.06 per site below every product crystal. So B5 is a candidate ordering, not a selection theorem.

### C. (b) The CL-1 cube tick

**C1 [T]. The cube hop.** R^2 = 1, and every face carries phase -1. The copy sign s commutes with R and splits each 4-dimensional eigenspace into 2 + 2.

**C2 [T+D]. The tick is not a plaquette flip.**
- The cube's four-unit vacuum is 91% inside the span of its 9 pair coverings (bond orbitals), against 39% for the best single covering. It is a resonating cube.
- The one-body hop leaks out of that span (norm 1.14), so it is not a dimer-plaquette flip.

**C3 [T+D]. The gap is exactly |mu|.** The two-tiling tick satisfies cos w = cos a cos b + sin a sin b S with S in [-1, 1]. So the quasi-energy gap is exactly |mu| (checked to 1e-9 on 8^3), and it closes only at mu = 0. Every vacuum with mu < 0 is continuously connected to the mu = -2 eps vacuum, and every vacuum with mu > 0 to the +2 eps one.

**C4 [T+D]. The fold limits are cube folds.**
- At mu = -2 eps every even cube holds exactly 4 units. For a face A and its mirror face A', n_A + n_A' is definite (variance 9e-16) while n_A is not (variance 0.33).
- At mu = +2 eps the same holds for every odd cube.
- So every site is bound and none is free.

**The fold is picked by the sign of the mass angle**, a term that CL-1 already carries: mu = mN > 0 gives the odd-cube fold. At mu = 0 the vacuum is unfolded.

**C5 [D+E]. The fold is weak at physical masses.** The imbalance between the tilings' cube-number variances is about 9|mu| on 8^3. For the electron that is about 4e-22, so the vacuum is unfolded at the cell scale.

**C6 [D]. The copy mass also selects.** With M = 0.2 on even cubes and mu = 0, the light copy stays gapless but the vacuum is unbalanced (Var N_even 1.50, Var N_odd 0.66). The copy mass is a second fold selector already in CL-1.

**C7 [T]. Point misfolds are the matter fermions.** A misfold is a cube with 5 or 3 units. It has odd parity, so it is a fermion (the modes anticommute). It sits in a 4-state level split 2 + 2 by the copy sign (CL-1's doublet x copy) and costs |mu|. So the misfold is CL-1's matter particle.

**C8 [D]. Wall misfolds.** A wall where the sign of mu flips carries gapless 2+1 fermions: 8 zero modes, and in-gap states that grow with the wall's area (20 -> 40 for area 16 -> 36).

### D. (c) Symmetric window rules (tile level)

**D1 [T]. A Majumdar-Ghosh-type rule is not enough.** Take the rule "every 3^d window holds a whole tile". Every tiling satisfies it, including the sliding ones (744 of 744 on 4^3, of which 8 are aligned). That gives zero entropy per site, but the fold is not unique.

**D2 [T+D]. An anti-slide window works in 2D.** A covariant window spanning 2x5 sites leaves only the 4 aligned 2D crystals. It is not cube-local, it is untested in 3D, and the claim that the qubit kernel equals the tilings is assumed.

### E. (d) The fewest-change transport

**E1 [T+D]. The transport cannot select.** CL-2 moves only the actual configuration and never conditions the odds, so it cannot pick a fold. The half-tick odds are stationary only at the two fold limits, and the two limits tie.

## Reading

The 3D fold is selected, uniquely up to 2Z^3 translations, by the sign of the mass angle. Equivalently, it is selected by the even/odd asymmetry that CL-1 already writes into each species' tick, and by its copy mass.

The selected fold is the cube crystal of one tiling. It is commensurate with the 2^3 cubes, keeps all 24 rotations, and is 91% a resonating-pair cube. Its point misfolds are exactly the massive matter fermions, in CL-1's doublet x copy level.

What the fold does not give:
- No site in the fold is free, so the fold has no matter sites.
- The fold's strength is the mass, so light matter cannot carry a cell-scale layout.
- The nested B_f / b_e block layout (rishons on block faces, edge registers coarser) is not produced.

Pure dimer resonance gives columnar states, a degenerate set, or a liquid, never the cube crystal as a theorem. Symmetric rules need windows larger than a cube.

## Candidate law text (proposal, not recommended for adoption yet)

> CL-1 (fold clause). A mode set's roles are read from its vacuum: in the vacuum of a set whose even and odd steps differ by mass angle mu, the cubes of the tiling named by the sign of mu hold definite totals, so their sites are bound (register) and carry no record; a cube whose total departs from its vacuum value is a particle of that set.

It would replace nothing in CL-1's layout yet. It cannot replace "Matter modes sit on the finest role block and edge registers on the coarsest", nor the B_f rishon orbits: the fold has no free sites, and it is cell-strong only for |mu| of order 1. It restates the even/odd mass asymmetry as the role selector. It also adds a derived fact: matter particles are misfolds.

## Smuggling review

**Supplied:**
- eps = 0.3, the mu scan and M = 0.2;
- the bond-orbital reading of a pair;
- the product ansatze;
- the window shapes;
- the search cap.

**From CL-1, not new:** the two tilings, R and its phases, the even/odd split of the steps, and the copy mass.

**Not derived:**
- a cell-strong fold for light modes;
- free sites inside a fold;
- the nested layout and gauge-factor sizes;
- the 3D version of the anti-slide rule.

**Lopsidedness:** the selector is the sign of mu, which is the sign of the mass. It is not a new choice.

Related work on main, cited: the cubic ring-model and RK notes (`docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md`, `docs/DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_ANNIHILATES_UNIFORM_ICE_EXACTLY_AT_THE_ROKHSAR_KIVELSON_POINT_AND_UNRECORDED_PLAQUETTES_CAN_POLARIZE_THE_ICE_BOUNDED_THEOREM_NOTE_2026-09-24.md`), which treat link ice, not site pairs. This note narrows neighbourhood-roles B5 by correcting its counts and adding the selector.
