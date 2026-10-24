---
claim_id: far_termination_winding_keeps_a_pi_free_screening_near_wall_but_the_end_is_a_chosen_boundary_bit_and_the_far_wall_must_gap_all_three_families_together_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Candidate clause (pi-repair A4 reading): CL-1's bulk tick has W = 0; the slab's far termination layer carries a family-class turn-graded winding. Supplied models: pi-repair's sector-resolved class-A toy (QWZ Floquet strip per turn sector + a chiral-shift layer standing in for the FREEZE layer) and a T-symmetric 3D Wilson domain-wall slab (m0 = 0.6, T = i sigma_y K). (G) Both end placements are valid slabs with the same bulk and total winding; U -> U^+ keeps the layer's end; given light q 2 and one far mirror Weyl the family-class W is one of two values: the clause carries ~3 bits of boundary information, none forced by an adopted rule. (N) Near wall: (F_0, F_pi) = (f(2,+), 0) over g and Lx; no layer-preserving doubler map can exist (exact lemma), and the near wall screens (induced charge 0.42) while an exactly S-doubled control gives 1e-12; a far-layer T-odd tetrahedral-covariant term leaks a reciprocity-odd dim-5 near-wall term falling as (1 - m0)^2 per layer (0.168 measured). (C) T kept by the bulk acts with X = 1 on copies: J = 0. (F) Far wall per family (q1,-), (q2,+), (q1,-) x 16: gauge and mod-16 anomalies vanish, the turn Z3 cubic is 6 mod 9 for k = 0 (nonzero for every twist), and vanishes for N_f = 0 mod 3 (supplied index form). Not covered: the slab on CL-1's 8-mode cell with a real FREEZE layer, the far-wall symmetric gapping itself, interactions, gauge fields."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_family_class_winding_forces_bulk_pi_states_but_a_slab_can_put_all_its_pi_flow_on_the_far_wall_while_no_tick_alternating_term_separates_pi_pi_from_zero_zero_bounded_theorem_note_2026-10-24
  - the_family_class_ticks_forced_pi_sector_is_a_light_charged_inverted_copy_whose_doubler_map_cancels_all_vacuum_polarization_so_it_needs_repair_while_its_anomalies_stay_safe_bounded_theorem_note_2026-10-24
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
  - the_family_class_tick_keeps_a_time_reversing_antiunitary_that_fixes_every_family_so_it_supplies_no_quark_cp_phase_and_keeps_theta_bar_at_zero_or_pi_bounded_theorem_note_2026-10-24
  - a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
runner: scripts/far_termination_winding_keeps_a_pi_free_screening_near_wall_but_the_end_is_a_chosen_boundary_bit_and_the_far_wall_must_gap_all_three_families_together_2026_10_24.py
---

# Far-termination winding keeps a pi-free, screening near wall, but the end is a chosen boundary bit and the far wall must gap all three families together

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] reading or estimate.
Runner: runner.py, TOTAL: PASS=9 FAIL=0, 3.4 s, 107 MB peak, 4.1 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (scratch/far_termination_winding_test_run.py). Axioms unchanged. No CL edit. No rule adopted.
Criteria: criteria_pre_run.txt, written before code. Every outcome matched its prediction. Code-level fixes on the way:
a T-operator dimension bug (crash), and N4's first run FAILED because the check compared the two-layer ratio (0.028) with
the per-layer criterion; the per-layer factor is sqrt(0.028) = 0.168 against the predicted 0.16. The claim did not change.

Repo first: git grep of origin/main (docs, scripts) for "far termination" and "termination layer" finds nothing; open PRs
#10064 (floquet-pi-slab) and #10073 (pi-repair) are the base. This note tests pi-repair's candidate.

## G. Gate and forcing

- G1 [T]/[F]. Same W = 0 bulk, same total det winding W_F = (-2, 1, 1), two placements of the winding layer:
  - far layer: near wall (F_0, F_pi) = (f(2,+), 0), far wall (f(1,-), W_F);
  - near layer: near wall (C + W_F, W_F) = ((-3, 2, 1), (-2, 1, 1)), i.e. the pi copy is back on our wall.
  Both are valid gapped-bulk unitary slabs, and nothing in the bulk tick tells them apart.
- G2 [T]/[F]. The record arrow does not pick the end. Reversing the tick (U -> U^+) negates every flow and leaves the layer
  where it was (the near wall stays pi-free). The arrow orients the tick; the layer index is a role-block coordinate.
  Cube fold: FREEZE and its inverse select the same fold (slab-parity), so the fold does not fix the sign or the end.
  Zoom ladder [S]: if the layer index were read as the zoom rung, the finest rung is a forced end (CL-1 puts matter on the
  finest block), so "near wall = finest rung" would be forced. But putting the winding at the coarse end rather than the
  fine end is still decided by the pi-sector measurement (vacuum polarization), not by a rule.
- G3 [T]. With light q 2 (C = f(2,+)) and one far mirror Weyl at 0, the far wall has F_0 = -C + W = f(q,-), so
  W = C + f(q,-). For q in {0, 1} this gives W = (-1, 2, -1) or (-2, 1, 1); both are family class and both give
  N_f = 0 mod 3. q = 2 gives W = 0. So the clause fixes three things: W != 0 (1 bit), the end (1 bit) and the mirror charge
  (1 bit). That is about 3 bits of boundary information, and none of them is forced.
- Is a chosen boundary still a rule? Yes in kind. It is a boundary condition on the update (one layer, at one end), like
  the past hypothesis is a boundary condition on the state. It constrains only updates and layers. It costs about 3 bits
  and it is selected by measurement (no pi copy on our wall), so it is a working rule with an explicit choice, not a
  derived one.

Gate result for "the slab's far termination layer carries a family-class turn-graded winding; the bulk tick has W = 0":
1. No measured number: PASS. The components are the minimal integers, not fitted.
2. No observed structure named: PASS. It names a layer, an end and a winding of the cube turn. It does not name families,
   a group or a scale. N_f = 0 mod 3 is a consequence.
3. Prediction not built for: UNTESTED. It was built for the pi-free near wall, which therefore does not count. Untested
   consequences it was not built for:
   - (a) the far wall must gap all three families TOGETHER (F1), so the heavy sector has no family-diagonal gap;
   - (b) the near-wall T-odd content is only a leaked dim-5 reciprocity-odd term, falling as 0.16^Ls (N4);
   - (c) J = 0 from the tick at the near wall (C1).
   None of these is measured yet.
4. Axiom bent: none. It bends CL-1's reading "one tick for every layer" (one layer differs), and the slab termination is
   a choice.
Overall: PASSES the gate as UNTESTED (clauses 1, 2, 4 pass; clause 3 is untested).

## N. Near wall on the W = 0 bulk

- N1 [F]. In every tested case (Lx 6, 8, 10; g 0.2, 0.3, 0.5) the near wall is (f(2,+), 0): one light q 2 Weyl per field,
  with no pi copy.
- N2 [T]/[F]. Lemma. A layer-preserving S with S U(k) S^-1 = -U(k + pi) maps each wall crossing at 0 to one at pi with the
  same hand, so F_0 = F_pi on each wall. The repaired near wall has F_0 != F_pi, so no such S exists. The spectrum of U(k)
  sits 1.46 away from that of -U(k + pi). This removes the mechanism that made vacuum polarization vanish.
- N3 [F]. Vacuum polarization, measured on a 12-site ring x 8 layers + the far layer, in the C = +1 sector, with near-wall
  kicks (lam 0.5) over 24 ticks:
  - the repaired near wall screens: max |dN_near| = 0.424;
  - the exactly S-doubled control (U plus its inverted pi image, the pi-sector-stability mechanism) gives 1e-12.
  - The near-layer placement also responds (0.925), because the toy's chiral shift has no exact FREEZE doubler. The toy
    therefore does not reproduce FREEZE's exact cancellation; that cancellation is pi-sector-stability's result.
  So the restored polarization follows from N2 together with the control, not from any toy number. The 27 MHz Uehling
  test returns qualitatively; it is not computed here.
- N4 [T]/[F]. Which T-odd terms remain near the near wall? This was checked in a T-symmetric 3D Wilson domain-wall slab
  (T = i sigma_y K, T^2 = -1, exact to 0):
  - a T-even far-layer term leaves E(k) = E(-k) on the near wall exactly (4e-16);
  - a tetrahedral-covariant, T-odd far-layer term (sigma_x sin ky sin kz + cyc, coefficient 0.3) leaks a reciprocity-odd
    near-wall term E(k) - E(-k) of -5.7e-5, -1.6e-6, -4.6e-8, -1.3e-9 at Ls = 4, 6, 8, 10. The per-layer factor is 0.168,
    against (1 - m0)^2 = 0.16. It is first order in the near mode's weight on the far layer.
  - [T] Constant b terms are forbidden by the 12 tetrahedral rotations, which FREEZE-class layers keep (any rotation group
    with an irreducible vector forbids an invariant b). All K^1 terms on one Weyl are T-even.
  - So the near wall's T-odd content is ONE class, a dim-5 n_x n_y n_z reciprocity-odd term of size ~0.16^Ls. FREEZE's
    m(K) L-R term needs the R mirror, which now lies on the far wall, so it reaches the near wall only through the same leak.
- N5 [S]. Estimate: with a = l_P and a Crab-type |eta| < 1e-7, the leak needs Ls >~ 11 layers (coupling 0.3 supplied).
  The T-symmetric bulk otherwise restores CL-1's full 192 group at the near wall. The lapse-in-step clause applies
  unchanged, since CL-1's tick keeps its step angle; new-tick-recheck's lapse repair is then not needed.

## C. CP at the near wall

- C1 [T]. The W = 0 bulk keeps Floquet T itself, and T acts on copies with X = 1 (it fixes the families).
  - Masses that respect it are real, det[Hu, Hd] = 0, and J = 0 (max |J| = 0 over 300 draws).
  - A family-universal leak (a multiple of 1) leaves the commutator unchanged, so J = 0.
  - Generic supplied phases do give J != 0.
- So CP still needs a non-family-blind ingredient that breaks every family-fixing antiunitary. This was already true on
  the FREEZE bulk (cp-source-new-tick: T x C2'), so the status is unchanged, not worse. theta-bar is 0 or pi from the tick.

## F. Far wall

- F1 [T]. Per family the far wall holds (q1,-), (q2,+), (q1,-), each a 16.
  - Gauge anomalies vanish (each 16 is anomaly-free).
  - The Weyl count (48) and the net hand (-16) are both 0 mod 16.
  - The turn Z3 anomaly (Z3-Spin10^2, Z3-grav, Z3^3) is NOT zero per family for any twist: (0, 0, 6), (1, 2, 5) and
    (2, 1, 7) for k = 0, 1, 2. For the untwisted turn it vanishes exactly for N_f in {3, 6, 9}. This uses the supplied
    anomaly-family-count index form; the mod-9 cubic matches the literature's Z3 condition (Hsieh-type), and that is
    supplied too.
- So symmetric gapping is allowed in principle only for the three families TOGETHER. That is the same mod-3 count, now
  stated as the far-wall SMG condition. It agrees with gap-vertex-family-tensor, where the minimal turn-neutral far-wall
  term at N_f = 3 couples all families (8 changes).
- The SMG itself is not shown: a family-collective 3 x 48-Weyl interacting gap is still open.

## Verdict: CANDIDATE

- No measurable cost was found at the near wall. It is pi-free and it screens. Its T-odd content is a leak, below the
  Crab bound for Ls >~ 11. CP and theta are unchanged in status.
- It passes the gate as UNTESTED.
- It needs:
  - (i) a rule that fixes the termination; it is currently a chosen ~3-bit boundary condition, selected by measurement;
  - (ii) a demonstrated family-collective symmetric gap of the far wall (anomaly-allowed only for N_f = 0 mod 3);
  - (iii) a build on CL-1's 8-mode cell with a real FREEZE layer.
- The adoption criterion "termination forced" FAILS (G1 to G3). That failure is a result.

## Smuggling review

- Supplied:
  - the class-A sector toy and its chiral-shift stand-in for FREEZE;
  - the Wilson slab (m0 = 0.6) and the far coupling 0.3;
  - the anomaly index form and the mod-9 cubic;
  - the eta bound mapping;
  - the termination end, its existence and the mirror charge.
- Forced:
  - per-wall F_0 - F_pi = C;
  - the doubler lemma (N2);
  - the arrow-independence of the end (G2);
  - the two-option count (G3);
  - the per-family turn anomaly (F1);
  - T with X = 1 giving J = 0;
  - the ban on b by tetrahedral rotations;
  - leak scaling with the near-mode far-layer weight.
