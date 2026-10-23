---
claim_id: the_two_tiling_tick_has_no_cell_local_family_symmetry_and_a_turn_triplet_forces_turn_invariant_mixing_to_be_cp_blind_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Supplied model: CL-1's cube tick (one global face-phase field, -1 on every face; even exp(-i(eps-mu/2)R), odd exp(+i(eps+mu/2)R), copy factor on even cubes), Bloch over 2Z^3; a one-parent-cube nesting (8 fine cubes, parent hops identity on child labels); and a nested two-tiling lattice over 4Z^3. (A) Exact: the cell-local commutant of the full two-tiling update over all k is the scalars, with or without the copy mass and at fixed or varying step (the dim 8 of families-from-tastes A11 is a 3-momentum undersampling). Fibre degeneracy is 4 (spin x 2 tastes) without the copy mass and 2 (spin x 1 family) with it, at every momentum tested. With the copy mass no fibre space of dim >= 3 exists. (B) Exact: one parent cube has commutant (M2+M2)x(M2+M2) (dim 64). Each of its four sectors carries a 4-dim family space (fine 2 x parent 2) on which the spin-stripped turn acts as 1+1+w+w^2, so it holds a turn triplet. Adding CL-1's second tiling (the fine odd cube) cuts it to an abelian commutant (dim 2 or 10) with every multiplicity 1 and breaks the turn. The nested two-tiling lattice has fibre multiplicity 1 with the copy mass, and the turn is not a symmetry of it. (C) Exact lemma: if both up and down masses are invariant under the turn (no axis chosen), [Hu,Hd] lies in the turn's commutant, sum of M_n_lambda. So J = 0 unless one turn eigenvalue holds >= 3 families, and a family triplet that the turn distinguishes gives J = 0 identically. Checked on every family space found. No three-family CKM with J != 0 arises without choosing an axis. Every mass coefficient is FITTED."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - zoom_blocks_carry_no_protected_sixteen_and_the_three_cube_link_types_give_a_commutative_family_blind_mass_algebra_bounded_theorem_note_2026-10-22
  - the_cube_tastes_are_two_doublets_and_no_symmetry_protects_a_family_triplet_bounded_theorem_note_2026-10-22
  - the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
runner: scripts/the_two_tiling_tick_has_no_cell_local_family_symmetry_and_a_turn_triplet_forces_turn_invariant_mixing_to_be_cp_blind_2026_10_22.py
---

# The two-tiling tick has no cell-local family symmetry, and a turn triplet forces turn-invariant mixing to be CP-blind

Claim type: bounded_theorem. Runner: runner.py (TOTAL: PASS=10 FAIL=0, seed 20261022).
- Through scripts/runner_cache.execute_runner under the unique filename
  scripts/two_tiling_family_space_agent_test_20261022.py: status ok, exit 0, 1.8 s, 2994 characters of stdout.
- Peak memory is about 120 MB.
- The copy and its live log were removed afterwards.

The minimal axioms are unchanged, and the register carries no premise weight.

## Questions

zoom-three-links found that one cube's tick commutant is M2+M2 (2 families per sector, J = 0). This note asks:
- (a) What is the internal (family) commutant of the FULL two-tiling CL-1 update, with and without the copy mass?
- (b) What is it for a two-rung nesting, a fine cube inside its parent cube?
- Does either carry a family space of dim >= 3 on which the cube's three-fold turn acts nontrivially?
- Can up and down masses built from different allowed, turn-invariant operators fail to commute and give a nonzero
  CKM and J without fitted numbers?

## Setting (supplied)

- The update is the register's CL-1 text, with one global face-phase field eta = (1, (-1)^x, (-1)^(x+y)).
- R = sum W_i / sqrt3 on each cube.
- The copy factor is exp(i(M/4)(R - i w)), with w = W1W2W3, applied before and after the even half-tick.
- Generic fixed eps = 0.37, mu = 0.11 and M = 0.53 are used, plus a structural version over all steps.
- "Internal" has two meanings here:
  - cell-local: k-independent operators on the cell, commuting at every k;
  - fibre: degenerate eigenspaces of U(k) at fixed k.
- The turn is g: e1 -> e2 -> e3 -> e1, about the cube diagonal. It is lifted by site phases (BFS), and the lift is
  checked exactly.
- In the nesting, parent hops pass each mode to the same mode of the neighbouring child cube (CL-1 shift reading,
  "same site labels"). Parent face phases are -1.

## A. Full two-tiling update (theorems and exact finite checks)

- A1 (exact). The cell-local commutant of the update over all k is 1-dimensional (scalars only) in every case:
  structural, fixed step at mu = 0, mu != 0, and with the copy mass. It is saturated at 12 and at 20 momenta.
  - With 3 momenta the computation gives 4 or 8. That is an upper bound only.
  - This NARROWS families-from-tastes A11 ("dim 8 over all k"). That runner used 3 momenta, and its 8 is an
    undersampled bound.
  - Taste symmetries of this tick are not cell-local, so CL-1's two tilings leave no internal family symmetry at all.
- A2 (exact at the tested momenta; generic, axis, 0, pi). U(k) is 4-fold degenerate without the copy mass and 2-fold
  degenerate with it:
  - 4 = spin x 2 tastes;
  - 2 = spin x 1 family (the register's one light family).
- A3. The turn lift exists on both tilings and keeps the copy sign.
  - Without the copy mass, the 4-dim fibre spaces at turn-fixed k carry turn multiplicities [2,1,1], which include a
    turn triplet. That triplet is spin x taste (E of O times spin-1/2), not a family triplet.
  - With the copy mass, no fibre space of dim >= 3 exists.

## B. Two-rung nesting

- B1 (theorem, checked). For one parent cube over 8 fine cubes, the fine and parent Cliffords commute, so the algebra
  is Cl x Cl and the commutant is (M2+M2) x (M2+M2), of dim 64.
  - There are four sectors (w_fine, w_parent), each (spin 2x2) x FAMILY 4, with family 4 = fine 2 x parent 2.
  - With its spin part stripped (Skolem-Noether: the turn times the inverse spinor rotation lies in the commutant),
    the turn acts on each 4-dim family space as E x E = 1+1+w+w^2. So the family space holds a genuine turn triplet.
  - This is the only place in the probe where a >= 3-dim family space with a nontrivial turn appears.
- B2 (exact). Adding CL-1's second tiling, the fine odd cube at the block centre, destroys it:
  - the commutant has dim 2 (hop directions separately) or 10 (flat ticks + copy signs);
  - it is abelian, with every multiplicity 1;
  - the turn is no longer a symmetry (word traces differ).
  So the B1 family 4 exists only for a one-tiling nesting, which is not CL-1.
- B3 (exact at the tested momenta). The nested two-tiling lattice (Bloch 4Z^3, fine and parent even and odd ticks,
  copy at both rungs):
  - fibre multiplicity is 4 without the copy mass and 1 with it at generic and axis k (2 at k = 0);
  - the turn is NOT a symmetry: word traces differ by up to 128, while the fine tilings alone give 0.
  So this nesting, with parent hops identity on child labels, breaks the turn through mixed fine-odd and parent
  loops. A turn-covariant parent dressing is open.

## C. Mixing without an axis

- C2 (theorem). Let the turn act on the left-handed family space as rho, and let Hu = Mu Mu^dag and Hd = Md Md^dag be
  turn-invariant. Then:
  - C = [Hu, Hd] lies in the commutant of rho, the sum over eigenvalues lambda of M_(n_lambda);
  - every block of C is traceless.
  For three families J is proportional to det C, so J = 0 unless one eigenvalue holds all three families, that is,
  unless the turn acts as a scalar on them.
  - For a triplet (1, w, w^2): det C = 0 identically (numerically 1e-44).
  - For 1+1+w: det C = 0 (1e-29).
  - For a scalar turn: generic, about 1e4.
  - Generalisation: a CP-odd quartet needs a turn eigenspace of >= 3 families.
- C1 (finite, every family space found). Turn-invariant up and down masses do fail to commute (|[Mu,Md]| = 3 to 155),
  so mixing angles are nonzero. Every CP quartet vanishes, at 1e-16. The axis-choosing control (non-invariant masses)
  gives |J| of about 0.06, so the test is live.
- C3. Every coefficient of an invariant mass operator is FITTED. In B1 that is 6 real numbers per mass per sector
  (invariant algebra M2+C+C), and no rule fixes them.

## Verdict

- (a) The full two-tiling CL-1 update has no internal family algebra: the cell-local commutant is the scalars. With
  the copy mass the fibre family multiplicity is 1, so there is no triplet.
- (b) A two-rung nesting gives a 4-dim family space containing a turn triplet only if the second tiling is dropped. With
  CL-1's two tilings it collapses to multiplicity 1 and the turn is lost.
- The decisive exact obstruction holds even where a triplet exists: turn-invariant (axis-free) up and down masses give
  nonzero mixing angles but J = 0 identically. Nonzero J needs either >= 3 families that the turn cannot tell apart
  (which removes the turn's reason for three), or a chosen axis or a turn-breaking vacuum.
- Three-family CKM with J != 0 is not obtained.

## Gate (anti-smuggling)

No new rule is proposed. All results are about CL-1 as written plus a supplied nesting (parent hops identity on child
labels). The gate is not applicable to a rule. For the mixing question:
- (1) Every mass coefficient is FITTED.
- (2) No structure is inserted by name.
- (3) The prediction "J = 0 for every turn-invariant mass" is falsified by measurement (J of about 3e-5 is measured).
  So turn-invariant family masses on any turn-distinguished family space are EXCLUDED, and the CP source must break the
  turn.
- (4) No axiom is bent.

## Smuggling review (supplied vs forced)

- Supplied:
  - the parent-hop map (identity on child labels);
  - the one-parent-cube block of B1;
  - the parameter values (generic);
  - the choice of the turn as the symmetry that "no axis" means. Larger groups only shrink the invariant algebra, so
    J = 0 persists.
- Forced: A1, A2, B1 structure, B2, the C2 lemma.
- Not shown:
  - a turn-covariant two-rung dressing that keeps the turn with both tilings;
  - whether a spontaneous turn-breaking vacuum (an order parameter, not a chosen axis) could source J with a
    non-fitted magnitude. That is the live route this note points to.

## Speculation (labelled)

The C2 lemma suggests that CP violation must come from a turn-breaking order parameter (a vacuum choice of axis) rather
than from family-space geometry. If that order parameter's orientation is random per domain, J would be domain-uniform
in magnitude only if it is fixed by the vacuum energy. Untested.

## Repo context

- Builds on zoom-three-links (single-cube commutant M2+M2) and family-count-5mode (N = 0 mod 3 via the turn charge).
- Narrows families-from-tastes A11 (dim 8 is undersampled; the true value is 1).
- Consistent with the families-from-tastes E+E taste content and one light family.
- Consistent with family-register (F3 = 3 from a supplied register: the C2 lemma applies to it too. A turn-invariant
  mass on its 3 protected families can give J != 0 only if the turn fixes all three, which it does there by
  construction, but it has no rule for the mixing).
