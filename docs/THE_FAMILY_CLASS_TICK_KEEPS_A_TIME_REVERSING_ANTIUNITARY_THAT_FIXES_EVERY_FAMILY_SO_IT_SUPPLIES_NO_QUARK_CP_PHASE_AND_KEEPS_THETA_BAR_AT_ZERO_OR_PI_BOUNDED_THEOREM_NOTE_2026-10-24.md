---
claim_id: the_family_class_tick_keeps_a_time_reversing_antiunitary_that_fixes_every_family_so_it_supplies_no_quark_cp_phase_and_keeps_theta_bar_at_zero_or_pi_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Supplied model: the adopted family-class tick's light node as the exact five-direction Clifford walk U = f + i n.Gamma (f = mean cos K, hops sin K_a/sqrt3 on tau3 sigma_a, L-R pieces Re H, Im H on tau1, tau2, H = (sqrt2/3)(cos Kx + w* cos Ky + w cos Kz)); three families as copies or as zoom-3 characters (2pi/3) j (1,1,1); 3x3 mass matrices supplied. (1) Exact: with every family at q = 2 the turn is a scalar on family space, so the turn-CP lemma no longer forces J = 0 (seeded generic masses: median |J| 2.5e-2). (2) Exact/finite: Floquet T alone has no antiunitary intertwiner, but T x C2' for all three axis-reversing C2' (and T x C2'(1,1,0), T x C4z) does, unitary, keeping L as L; T x C2'(1,-1,0) fixes every zoom-3 family label (T alone swaps j = 1, 2). (3) Exact lemma: any antiunitary acting on the doublets by a unitary X forces det[Hu,Hd] = 0, so J = 0, and with X = 1 or diagonal real-basis masses give arg det(Mu Md) in {0, pi}. (4) Exact: the tick's L-R pieces H and m(K) vanish at the node and on the whole turn axis (1 + w + w^2 = 0), and a family-blind tick contributes only multiples of 1 in family space. (5) Estimate: read as a worst-case family-universal mass entry, the T-odd piece gives J ~ 2e-34 and theta ~ 7e-33 at a = 10 l_P. (6) Seeded: generic supplied phases give J != 0 and theta_tree of order one (median 0.74 rad, 0 of 2000 below 1e-10). Not covered: interactions, gauge fields, the copy mass on top of the tick (its kept group not recomputed here), which Weyls are quarks, loops, spontaneous breaking."
upstream_dependencies:
  - a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
  - the_family_class_tick_has_no_step_angle_so_the_lapse_rides_a_winding_free_layer_while_the_speed_tie_and_slab_survive_and_the_overlap_takes_its_time_even_kernel_bounded_theorem_note_2026-10-24
  - no_principle_tested_forces_a_nonzero_turn_graded_tick_winding_because_chiral_walls_exist_at_zero_winding_time_reversal_forbids_the_family_class_and_fewest_changes_selects_zero_bounded_theorem_note_2026-10-24
  - the_two_tiling_tick_has_no_cell_local_family_symmetry_and_a_turn_triplet_forces_turn_invariant_mixing_to_be_cp_blind_bounded_theorem_note_2026-10-22
  - a_turn_kept_by_the_update_and_broken_by_the_vacuum_gives_cp_and_theta_bar_together_unless_a_nelson_barr_block_is_supplied_bounded_theorem_note_2026-10-22
runner: see stems.txt
---

# The family-class tick keeps a time-reversing antiunitary that fixes every family, so it supplies no quark CP phase and keeps theta-bar at 0 or pi

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] estimate or reading.
Runner: runner.py, TOTAL: PASS=10 FAIL=0, 0.3 s, 37 MB, 2.6 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (scratchpad cp_source_new_tick_test.py). Axioms and CL text unchanged. No rule adopted.
Criteria: criteria_pre_run.txt, written before code. One deviation: the first run failed D2 on an absolute
|det[Hu,Hd]| < 1e-13 (value 4e-11 on O(10) matrices); the check was changed to the scale-free |det C|/||C||^3 and
an absolute |J| < 1e-13. Both now pass (2e-15, 6e-16). The first-run failure was a units issue, not physics.

## Question
The register's CL-1 recheck says "every light Weyl carries one turn charge q = 2, so CP in mixing is allowed" and
lists the CP phase as open. Where can J != 0 (measured 3.08e-5) come from on the adopted rules? Does the tick's
T breaking supply it? Does the same breaking feed theta-bar (bound ~1e-10)?

Repo first: git grep of origin/main for "generalized CP" finds nothing; no open PR matches "Jarlskog family-class".
Built on: two-tiling-family-space (turn-CP lemma C), spontaneous-turn-cp (J and theta tied), strong-cp-revisit
(kept antiunitary forbids theta_gauge; zoom-3 Nelson-Barr), t-breaking-tick-lowenergy (96-element group, m(K)),
new-tick-recheck (five-direction walk; T-odd phase out of the history weight), record-arrow-family-phase
(shared antiunitary gives J = 0; here generalised to any family action X).

## 1. The turn-CP obstruction is lifted, but nothing labels the families [T]
- With all three families at q = 2, the turn acts as w^2 times 1 on family space. Its commutant is all of M3, so
  lemma C gives no constraint. Seeded check: a triplet (0,1,2) gives max|J| = 0 over 200; all q = 2 gives median
  |J| 2.5e-2 over 2000. The register's "allowed" is correct as far as the turn goes.
- What labels the families? The rules give N_f = 0 mod 3 copies of one q = 2 Weyl; the tick is the same on each.
  On its own the tick therefore has a U(3) family symmetry: masses come out proportional to 1, degenerate, and
  mixing is unphysical (det[Hu,Hd] = 0). A label has to be supplied: copy index or the zoom-3 characters
  (2pi/3) j (1,1,1) used by strong-cp-revisit. Neither is fixed by a law.

## 2. The family-class tick keeps a time-reversing antiunitary [T]/[F]
- On the rebuilt node, Floquet T alone (V conj U(K) V^+ = U(-K)^+) has no solution: the smallest singular value of
  the stacked system over 12 momenta is 1.98, and the null space is 0. This is the known T breaking.
- T x C2' does have one, for all three axis-reversing C2' (1,-1,0), (1,0,-1), (0,1,-1), and also T x C2'(1,1,0)
  and T x C4z. T x C2z (a tetrahedral C2) does not. This matches t-breaking-tick-lowenergy's rule (kept iff
  [non-tetrahedral] = antiunitary mod 2).
- For T x C2'(1,-1,0): V is unitary (to 4e-16), intertwines 20 fresh momenta (7e-16), maps tau3 to tau3 (L stays L),
  and (V K)^2 = +1.
- On families: T x C2'(1,-1,0) sends every zoom-3 label j to itself (X diagonal); on copies it acts as X = 1.
  T alone would swap j = 1 and 2; T x C4z sends j = 1, 2 off the family set.
- So the T breaking is real, but a T-type antiunitary survives in the 96-element group. It is time-reversing,
  keeps chirality, keeps the turn charge and keeps each family.

## 3. Generalized-CP lemma: any such antiunitary forces J = 0 [T]
- Suppose Hu = X conj(Hu) X^+ and Hd = X conj(Hd) X^+ for one unitary X on the doublets. Then
  det[Hu,Hd] = conj(det[Hu,Hd]). The determinant of a commutator of Hermitian 3x3 matrices is imaginary, so it is 0,
  and J = 0. This holds for every X.
- Runner: X = S S^T over 300 random S gives condition error 1e-14, |det C|/||C||^3 2e-15 and |J| 6e-16.
- theta: with X = 1 (copies) or diagonal, the masses are real in a basis, and arg det(Mu Md) is in {0, pi} exactly.
  The same antiunitary is odd on the theta density: E.B is T-odd and invariant under a proper rotation. So
  theta_gauge is in {0, pi} (as strong-cp-revisit found with T x C4 / PH x C4), and theta_bar is in {0, pi}.
- Consequence: while the mass sector respects the kept group, CP in quark mixing is FORBIDDEN, even with every family
  at q = 2. Breaking T is not enough. J != 0 needs the mass sector to break T x C2' (and every other time-reversing
  antiunitary that maps the light families to themselves).

## 4. The tick's T-odd pieces do not reach the mass matrices [T]/[S]
- [T] The tick's L-R pieces are H(K) (with the T-odd phase Im H, the overlap defect 2|Im H||G5|) and its node
  expansion m(K). Both vanish at K = 0 and on the entire turn axis, because 1 + w + w^2 = 0 (runner: 2e-16, 9e-17).
  So they give no mass entry at the node and none at any zoom-3 family point.
- [T] The tick is family-blind, so whatever it contributes is a multiple of 1 in family space.
- [T] The T-odd piece is itself T x C2'-even, because it is part of the tick that T x C2' keeps. Adding it cannot
  break the lemma of section 3.
- [T] m(K) couples the light L (q = 2) to the R mirror (q = 1) on the far wall, not to a quark singlet. It enters
  light dispersion only through |m|^2 (cos theta = mean cos K exactly), and the time-even overlap kernel drops it
  from the history weight (new-tick-recheck).
- [S] Worst case (against all of the above): read m at K a = m_t a / hbar c as a family-universal complex mass
  entry of relative size eps = (sqrt2/6)(Ka)^2. J and theta are linear in eps (slopes 0.04 and 1.35, median over
  100 real-basis samples). That gives J ~ 2e-36 and theta ~ 7e-35 at a = l_P, and 2e-34 and 7e-33 at a = 10 l_P.
  This is 29 orders of magnitude below J = 3.08e-5 and 23 below theta's 1e-10.

## 5. Supplied phases: J and theta come together [F]
- With generic complex Yukawas that break every kept antiunitary (supplied, FITTED class): median |J| 2.5e-2, J > 1e-6
  in all 2000, and median theta_tree 0.74 rad (distance to {0, pi}). None of the 2000 is below 1e-10.
- This is the same tie spontaneous-turn-cp found. The only separation on record is strong-cp-revisit's zoom-3
  Nelson-Barr reading (supplied copy and vacuum scales).

## Answer
- (1) The turn-CP obstruction is lifted, since the family label is no longer a turn charge. But the rules give no
  family label at all: the tick is family-blind, with U(3) and degenerate masses. And a kept time-reversing
  antiunitary, T x C2', fixes every family. By the generalized-CP lemma it forces J = 0 for any mass sector that
  respects the tick's group.
- (2) The tick's T-odd structure (m(K), the 2|Im H||G5| phase) is T x C2'-even, family-universal, zero at the node and
  on the turn axis, and couples L to the mirror. It cannot give a rephasing-invariant J. Even read as a worst-case
  universal mass it gives J < 1e-33.
- (3) Strong CP: while the kept group holds, theta_bar is in {0, pi} exactly. The tick-sized leak is ~1e-32 at most
  (a = 10 l_P), far below 1e-10. Once supplied phases give J, theta_bar is generically O(1) (median 0.74) unless a
  Nelson-Barr-type structure is also supplied.
- VERDICT: CP is NOT supplied by the tick. It is ALLOWED, but it needs input: mass-sector phases that break T x C2',
  not just T. The register's "CP in mixing is allowed" should be narrowed to "allowed by the turn; still forbidden by
  the kept T x C2' unless the mass sector breaks it". Strong CP: 0 or pi from the tick, and the problem returns with
  the supplied phases (J and theta tied).

## What a CP law must now do (route, not a wall)
- Give a family label from cluster structure, and break T x C2' in the mass sector only, with arg det kept at 0.
- A candidate: a zoom-3 mass rule where T x C2' maps light-heavy entries to each other with X acting off the light
  block, which is the Nelson-Barr pattern. Untested here.

## Smuggling review
- Supplied:
  - the Clifford rebuild of the node, taken from new-tick-recheck's stated form (basis convention, P = -1 irrep);
  - the family labels (copies or zoom-3);
  - the mass matrices, all seeded and FITTED class;
  - m_t and E_P for the estimate;
  - a = 1 to 10 l_P.
- Forced:
  - the T null space (0) and the T x C2' and T x C4 intertwiners;
  - the family action of T x C2';
  - the generalized-CP lemma;
  - the vanishing of H and m on the turn axis;
  - the linearity of the leak.
- Not computed:
  - the copy mass on top of the tick (the register says it keeps T composed with a fourfold turn; whether that
    element fixes the families is not checked here);
  - interactions and loops;
  - spontaneous breaking of T x C2' (it would give domain walls, as in spontaneous-turn-cp);
  - which Weyls are quark doublets and singlets.
- Gate: no rule is proposed, so the gate does not apply.
