---
claim_id: zoom_blocks_carry_no_protected_sixteen_and_the_three_cube_link_types_give_a_commutative_family_blind_mass_algebra_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Supplied model: L^3 blocks of one-mode sites with the cube point group O_h acting by site permutation, and the CL-1 cube hops W_i (face phases -1) on a 2x2x2 cube. (A) Exact: an internal Spin(10) commuting with O_h needs five complex modes in one 1-dim O_h isotypic block; the largest such multiplicity is 1, 4, 4, 10, 10 for L = 2..6, so the smallest block with room is 5^3. Finite diagnostics (seeded): on the 2^3 block (256 states) a generic O_h-symmetrised interacting number-conserving H has multiplets of size at most 3; on 5^3 a generic O_h hop with axis, face and body links splits the 10 orbit-uniform modes into 10 distinct levels, so a block Spin(10) is a tuning, not protected by structure. Where it is imposed, its 2pi rotation is -1 on the block's 32 states, so the composite-sixteen centre theorem applies blockwise and a fixed block lattice carries no 16 quasiparticle. (B) Exact: the axis, face and body adjacencies of a cube commute (levels 1,1,3,3); on Z^3 the three ranges (counts 6/12/8) commute for any up and down distance functions; so geometry-only mass rules give at most two nondegenerate families, V a permutation, J = 0. The face and body links are the products W_iW_j and w = W1W2W3 of the CL-1 hops; the tick's commutant on a cube is M2+M2 (two families per w-sector), every mass term in it (staggered or not) gives block-diagonal 2+2 mixing with J = 0 identically, and its rotation-covariant part is the identity alone. No physical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - spin10_mott_sites_carry_no_composite_sixteen_the_centre_fixes_every_fermion_to_the_vector_class_bounded_theorem_note_2026-10-22
  - five_modes_per_site_are_the_smallest_anomaly_free_protected_spin2n_content_bounded_theorem_note_2026-10-22
  - a_fold_ladder_family_mass_rule_gives_rank_three_and_handed_cp_but_its_content_is_the_fitted_rungs_and_it_leaves_theta_bar_order_one_bounded_theorem_note_2026-10-22
  - a_path_sum_flavour_rule_with_forced_rungs_is_family_blind_or_flat_and_its_structural_theta_bar_zeros_kill_cp_or_tie_down_to_up_bounded_theorem_note_2026-10-22
runner: scripts/zoom_blocks_carry_no_protected_sixteen_and_the_three_cube_link_types_give_a_commutative_family_blind_mass_algebra_2026_10_22.py
---

# Zoom blocks carry no protected sixteen, and the three cube link types give a commutative, family-blind mass algebra

Claim type: bounded_theorem. Runner: runner.py (TOTAL: PASS=11 FAIL=0, 0.3 s, small memory, stdout 2897
characters, seed 20261022). It was run through scripts/runner_cache.execute_runner under the unique filename
scripts/zoom_three_links_agent_test_20261022.py (status ok); the copy and its live log were removed. The minimal axioms
are unchanged. The register carries no premise weight.

## Questions (owner suggestions)

(A) Can a coarse block of one-qubit sites carry a protected 16 through its structure, avoiding the fixed-lattice
Spin(10) obstruction of composite-sixteen? (B) Do the cube's three link types (axis 1, face sqrt2, body sqrt3), with
strengths fixed by geometry, give a non-fitted mass and mixing structure: families, distinct up and down patterns,
nonzero CKM, and arg det = 0?

## A. Zoom and the 16

- A1 (theorem). A Spin(10) acting on 10 Majorana directions of a block and commuting with the block symmetry O_h must
  have O_h acting on those 10 directions as one scalar character (Schur: the commutant of so(10) on R^10 is R). The
  Majoranas of an L^3 block carry (permutation rep) x R^2, so the room is 2 x (multiplicity of a 1-dim character).
  This multiplicity is the number of site orbits for A1g: 1, 4, 4, 10, 10 for L = 2..6. Neither 2^3 nor 3^3 has room.
  The smallest is 5^3, whose 10 orbit-uniform modes leave room for five.
- A2 (finite). On the 2^3 block (8 modes, 256 states), a generic O_h-symmetrised interacting H has multiplets of 1, 2
  and 3 only. A protected 16-fold level would need a 16-dim irrep. Point groups have irreps of dimension at most 3, or
  4 for the double cover that the CL-1 face phases produce, so it would have to be a supplied degeneracy.
- A3 (finite). On 5^3 a generic O_h hop built from the three link types gives the 10 A1g modes 10 distinct levels
  (min gap 0.185). Five degenerate modes are a tuning. Least information does not select them.
- A4 (theorem). Even where a block Spin(10) is imposed, its 2pi rotation is -1 on all 32 states of the five modes, a
  c-number per block. So composite-sixteen (B) applies with "site" read as "block": on a fixed block lattice every
  fermion-parity-odd excitation is in the vector class. Zooming changes the unit but not the obstruction. The only
  way past it is a 16 as a SINGLE-PARTICLE multiplet (16 modes in the 16, as in the octree-16 reading), which needs a
  supplied U(16) or Spin(10) and is not given by any block's structure.
- Verdict A: no. A zoom does not give the 16-label equivalent through block symmetry plus least information. What
  remains is a 16 carried by one-particle modes or by a moving unit, and both are outside this test.

## B. Three link types

- B1 (theorem). The cube adjacencies A_axis (12 links), A_face (12) and A_body (4) commute: they form the Bose-Mesner
  algebra of the 3-cube. The eigenvectors are (-1)^(s.x), with eigenvalues (3-2w, ((3-2w)^2-3)/2, (-1)^w) and
  multiplicities 1, 3, 3, 1.
- B2 (theorem; 20 seeded checks). Any geometry-only rule M = f(1, A_axis, A_face, A_body) gives levels 1+1+3+3. So
  there are at most two nondegenerate "families", and the triplets are exactly degenerate (the measured 3-family
  hierarchy is excluded). [M_u, M_d] = 0, so V is a permutation and J = 0. arg det is real, so theta-bar is
  structurally zero, but there is no CP. The strengths f(sqrt2)/f(1) and f(sqrt3)/f(1) are 2 FITTED numbers per
  sector, and no choice of them escapes these statements.
- B3 (theorem). On Z^3 (a 4^3 torus check, counts 6/12/8), translation-invariant hops of the three ranges commute for
  any up and down distance functions. That gives one band per species, and the ranges alone give no family index.
- B4 (theorem). In CL-1 the three link types are not independent. W_iW_j is exactly the face-diagonal hop, and
  w = W1W2W3 is the body-diagonal hop, central in the tick algebra, with w^2 = -1. The three ranges are the tick's
  Clifford algebra 1+3+3+1.
- B5 (theorem). The tick's commutant on one cube has dimension 8 and is non-abelian (M2+M2 over the w = +-i sectors).
  So C^8 = (spin 2) x (family 2) per sector, and one cube carries two families per sector, not three.
- B6 (theorem; 10 seeded checks, plus a 3-family control with invariant 0.031). Every mass term in the commutant,
  bare or staggered by (-1)^(x+y+z), gives H = MM^dag commuting with w. The mixing is block-diagonal 2+2, and
  Im tr(Pu Pd Pu Pd) <= 1e-16. So J = 0 for every choice, fitted or not.
- B7 (theorem). Every O_h element lifts by a site gauge to U with U W_i U^T = W_sigma(i). The rotation-covariant part
  of the commutant is span{1} for both O and O_h. So a geometry-fixed family mass matrix is a multiple of 1, and any
  family splitting is a lopsided input that chooses an axis.
- Verdict B: no. Geometry-fixed link strengths give a commutative, family-blind mass algebra, with V = 1 or a
  permutation and J = 0. Strong CP is satisfied only trivially (real determinants), which is the same structural-zero
  kills-CP pattern as forced-rungs. Nonzero CKM needs non-commuting up and down structures. Those exist in the
  commutant only after an axis or sector choice, which is FITTED or lopsided, and even then one cube gives two
  families per sector, so J stays 0. Three families with CP need structure beyond one cube: several cubes or rungs,
  as in fold-ladder, whose rungs were fitted.

## Anti-smuggling gate

No rule is proposed for adoption. Both candidate readings fail. (A) needs a supplied degeneracy (U(16) or Spin(10)).
(B) gives no 3 nondegenerate families, J = 0 and V trivial at every value of its 2 fitted strength ratios. Axiom bent:
none. The prediction not built in, two families per w-sector and family-blind geometric masses on one cube, disagrees
with measurement (three families, J = 3.08e-5).

## What this narrows (for next probes)

1. A 16 needs a symmetry with a >= 16-dim irrep acting on one-particle modes, or a unit whose count can change (a
   moving block or defect). Pure block structure is ruled out.
2. A 3-family CP structure needs a family space of dimension >= 3 on which up and down act through NON-commuting
   operators chosen without an axis. One cube's commutant (M2+M2) is too small. The next candidate is the commutant of
   the two-tiling update (even plus odd cubes) or of a 2-rung block, where the multiplicity space can reach 3 or more.

Supplied: the block point-group action, the one-mode-per-site Fock structure, the CL-1 W_i with -1 face phases, the
mass terms tested (commutant and staggered commutant), the seeds, and the reading of eigen-levels as families.
