---
claim_id: the_family_class_tick_has_no_step_angle_so_the_lapse_rides_a_winding_free_layer_while_the_speed_tie_and_slab_survive_and_the_overlap_takes_its_time_even_kernel_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Recheck, on the adopted family-class tick (FREEZE, W_F = (-2,1,1), free fields on CL-1's 2x2x2 cell), of four results derived with CL-1's W = 0 tick. (1) Exact: FREEZE's light dispersion cos theta = mean cos K is CL-1's tick at its maximal step eps = pi/2 (all 8 bands of U1(pi/2)), so FREEZE has no free step angle; W is a homotopy invariant, so no continuous family of ticks joins eps = 0 to FREEZE, and the fractional power U_F^s is discontinuous at the pi node. Repair (finite diagnostic): a lapse layer exp(i G_N) U_F, G_N the tick's own linear term times (N sqrt(gamma^ii) - 1), is turn-covariant and homotopic to 1, keeps W = W_F for every N, and scales low quasi-energies by N sqrt(gamma^ii) per axis (8e-6 at |K| = 0.01). (2) The speed tie survives with tau fixed at 1/sqrt3; at tau^2 = 1/3 the graviton relation of tick-fraction-waves is identically cos w = mean cos k, FREEZE's light relation (9e-16). (3) Exact: FREEZE is a Clifford walk over five anticommuting directions; on one 4-spinor these exhaust Cl(5), so a direct Euclidean transcription is not g5-hermitian, with defect exactly 2|Im H| |G5|. Repair: the T-even kernel (hop sin K/sqrt3, Wilson term = the tick's scalar 1 - f, r_s = 1/3) gives GW to 4e-15, one zero only for 0 < m0 < 2/3 (narrower than 0 < m0 < 2), and on a U(1) 4^4 background index 0, 1, 4 for Q = 0, 1 and charge 2, equal to the old kernel's. (4) The odd Ls = 7 floquet-pi-slab of the adopted tick, at N = 1 and with the lapse layer at N = 0.9, keeps bulk gaps 0.50 at 0 and pi, W = W_F, the light q 2 on the near wall and the mirror q 1 on the far wall. Not covered: interactions, gauge fields on the slab, non-abelian index on the new kernel, the copy mass, a finite-range (rather than exponentially local) lapse layer, moving sources."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - a_family_class_tick_keeps_a_96_element_magnetic_group_that_forbids_every_low_energy_rotation_or_lorentz_violating_dispersion_term_below_dimension_six_and_leaves_its_time_reversal_breaking_in_one_chirality_flip_term_bounded_theorem_note_2026-10-24
  - skip_patterns_carry_the_tick_fraction_on_clocks_but_every_skip_front_makes_pairs_so_the_lapse_is_read_into_the_cube_step_bounded_theorem_note_2026-10-23
  - the_tick_fraction_and_pair_offsets_answering_the_hinge_sum_are_constraints_and_leave_exactly_two_tensor_waves_on_the_edge_cone_with_the_quadrupole_coefficient_bounded_theorem_note_2026-10-23
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
runner: scripts/the_family_class_tick_has_no_step_angle_so_the_lapse_rides_a_winding_free_layer_while_the_speed_tie_and_slab_survive_and_the_overlap_takes_its_time_even_kernel_2026_10_24.py
---

# The family-class tick has no step angle, so the lapse rides a winding-free layer; the speed tie and the slab survive, and the overlap takes the tick's time-even kernel

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] estimate or reading.
Runner: runner.py, TOTAL: PASS=9 FAIL=0, 6 s, 198 MB peak, 4.0 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (scratch/new_tick_recheck_test_run.py). Axioms unchanged. No rule adopted, no CL edit.
Criteria were written before any code (criteria_pre_run.txt) and used unchanged.

## Question

CL-1 now adopts a family-class tick (FREEZE, W_F = (-2,1,1)). Several adopted results were derived with CL-1's W = 0
tick. Which survive? (1) lapse in the step (skip-rule); (2) the light/graviton speed tie (tick-fraction-waves);
(3) the history-level overlap: GW, no doublers, index (overlap-from-walk, overlap-colour); (4) the Floquet-pi slab
(floquet-pi-slab). FREEZE is rebuilt with the t-breaking-tick-lowenergy code (same seed and draw order).

## 1. Lapse in the step: NEEDS REPAIR (repair found)

- [T] FREEZE's light dispersion, cos theta = mean cos K, is exactly the dispersion of CL-1's own tick at its maximal step
  eps = pi/2. All 8 bands of U1(pi/2) obey it to 5e-16, and U1(eps) has speed sin(eps)/sqrt3 per cell. So FREEZE is the
  "sin eps0 = 1" tick. It has no step angle: its light speed is pinned at 1/sqrt3.
- [T] W is a homotopy invariant of K -> U(K), and the identity (eps = 0) has W = 0. So no continuous family of tick
  unitaries joins eps = 0 to FREEZE inside the class. The fractional power U_F^s is not a way out: at s = 0.9 it jumps by
  1.24 across the pi node R, so it is not local. The adopted "sin(eps_cube) = sqrt3 N rms sqrt(gamma^ii)" has nothing to
  act on.
- [F] Repair (lapse layer). Take the tick to be exp(i G_N) U_F, with
    G_N = Pi+ Y [ sum_i (N sqrt(gamma^ii) - 1) sin K_i gamma_i / sqrt3 ] Y^+ Pi+,
  that is, the tick's OWN linear term times (N sqrt(gamma^ii) - 1). Properties:
  - it is turn-covariant (4e-15) and homotopic to 1, so W = W_F exactly for every N (checked at N = 0.7, 0.9 and 1.3);
  - low quasi-energies scale by N sqrt(gamma^ii) per axis, to 8e-6 at |K| = 0.01, including an anisotropic (0.7, 0.9, 1.1);
  - every site still ticks every half-tick, and a static source gives a static tick. So skip-rule's no-pair argument
    carries over unchanged.
- Cost. The layer is exponentially local (exp of a range-1 generator), not a finite-range cube layer. A finite-range form
  is not built. The lapse ceiling that skip-rule predicted (N <= 1/(sqrt3 sin eps0 ...)) no longer follows from a step
  angle. With the layer, any N works.
- Wording for the register: "the lapse is carried by a winding-free layer of the tick's own linear term", not by the step
  angle.

## 2. Speed tie: SURVIVES (sharpened)

- [T] The tie is still one tick/edge ratio. tau, the graviton's label speed, must equal the light speed per tick. That is
  now 1/sqrt3, fixed by the tick (sin eps0 = 1), where before it was a free sin(eps0)/sqrt3.
- [T] At tau^2 = 1/3, tick-fraction-waves' relation sin^2(w/2) = tau^2 sum sin^2(k_i/2) is identically cos w = mean cos k,
  FREEZE's light relation. The runner finds 9e-16 over 20 directions and |k| up to 1.5.
  - [S] If the graviton's k and the light's K are in the same lattice units (the waves note's "blocks"), light and
    graviton agree at every lattice k, not only as k -> 0.
- With the lapse layer, both cones scale by N: the slope gap is 6e-6 at N = 0.9.
- The graviton is never superluminal: tau^2 = 1/3 <= sum khat^4, with equality along (111).

## 3. Overlap: NEEDS REPAIR (repair found); GW and index survive on the repaired kernel

- [T] The new tick is a Clifford walk U = f + i n.Gamma over FIVE anticommuting directions: the three hops sin K_i/sqrt3
  and the two L-R components Re H and Im H, with H = (sqrt2/3)(cos Kx + w* cos Ky + w cos Kz). The runner checks this to
  6e-16.
- [T] On one 4-spinor these five directions exhaust Cl(5), since their product is a scalar. So no time gamma
  anticommutes with all five, and gamma5 must be one of the L-R directions.
  - The direct Euclidean transcription is therefore NOT g5-hermitian. Its defect is exactly 2|Im H| |G5|, which is the
    tick's T-odd phase, the same structure as t-breaking-tick-lowenergy's m(K).
  - V = g5 sign(g5 X) cannot be formed from it as it stands.
- [T]/[F] Repair: the T-even kernel, built from the tick's own T-even pieces. The hop is sin K/sqrt3, and the Wilson term
  is the tick's scalar 1 - f = (1/3) sum(1 - cos K_i). This is the Wilson form with r_s = 1/3.
  - GW holds to 4e-15 on 8^4.
  - D vanishes only at k = 0 for 0 < m0 < 2/3. The corner masses are 2 n_s/3 + 2 n_t, so there are 1, 4 and 7 zeros at
    m0 = 0.4, 1.0 and 1.7.
  - The one-species window is NARROWER than the old 0 < m0 < 2 (this is overlap-from-walk A2's tick-weight statement
    with r_s = 1/3).
- [F] One small background: U(1) on 4^4, fluxes (n, n) in the (12) and (34) planes.
  - The new kernel's index is 0, 1, 4 for Q = 0, Q = 1, and charge 2 (Q = 4).
  - These equal the flux prediction e^2 Q and the old kernel's (r = 1, m0 = 1) values.
  - GW holds in the background to 2e-13. The minimum |g5 X| is 0.078.
- The index-based anomaly checks (the overlap-nonabelian and overlap-colour sums) are statements about indices, so for
  this abelian background they carry over. The non-abelian and SU(3) backgrounds were not rerun on the new kernel.
- Cost. The history weight now sees only the tick's T-even part. The T-odd L-R term (dimension 5 at the node, the CP
  structure) is not in the matter history weight. Whether CP must re-enter through the weight is open.
- [S] The alternative, an 8-spinor Cl(7) embedding that keeps all five directions, is g5-hermitian. But it has two
  Dirac fields per cell: it re-lights FREEZE's frozen copy. It was not chosen and not computed.

## 4. Slab: SURVIVES

- [F] The odd (Ls = 7) slab of floquet-pi-slab, built from the adopted tick at N = 1 and with the lapse layer at N = 0.9,
  keeps:
  - bulk gaps of 0.500 at 0 and at pi (8^4 grid);
  - W = W_F;
  - the light q 2 (hand +1) on the near wall and the mirror q 1 (hand -1) on the far wall, both at (K = 0, 0) and at the
    (R, pi) partner.
- So there is one protected light Weyl per field at quasi-energy 0, with its pi partner at cell scale, as the register
  already says. The lapse layer, being winding-free, does not move the walls.

## Answer

| item | verdict | what changes |
|------|---------|--------------|
| (1) lapse in the step | NEEDS REPAIR | FREEZE is the maximal-step tick and has no step angle; carry N by a winding-free layer of the tick's own linear term (W unchanged, low quasi-energies scale by N sqrt(gamma^ii)). |
| (2) speed tie | SURVIVES | tau is now fixed at 1/sqrt3, and the graviton relation coincides with the light relation. |
| (3) overlap | NEEDS REPAIR | build it from the tick's T-even kernel (Wilson form, r_s = 1/3, window 0 < m0 < 2/3). GW, no doublers and the abelian index (equal to the old kernel's) then survive. The T-odd part cannot enter a 4-spinor g5-hermitian kernel. |
| (4) slab | SURVIVES | unchanged, also under the lapse layer. |

No FAILS.

## Smuggling review

- Supplied:
  - FREEZE (as in the adopted clause) and its rebuild;
  - the lapse layer's form: the tick's own linear term, chosen because it is the unique allowed linear coupling of
    t-breaking-tick-lowenergy, not fitted;
  - the Euclidean kernel identification. As in overlap-from-walk it is supplied; here it is restricted to the tick's T-even
    pieces, with the Wilson weight taken as the tick's own scalar 1 - f;
  - m0 values in the window;
  - the 4^4 U(1) background;
  - g = 0.5 and Ls = 7 for the slab;
  - the units identification for the all-k speed coincidence [S].
- Forced:
  - FREEZE's light relation equals CL-1's tick at eps = pi/2;
  - W's homotopy invariance, so there is no step path;
  - W is kept under any turn-covariant layer homotopic to 1;
  - the Cl(5) exhaustion and the exact g5-hermiticity defect 2|Im H||G5|;
  - the corner-mass window 2/3;
  - the index values;
  - the slab wall content.
- Gate for the two repairs:
  - (1) no measured number is chosen;
  - (2) no observed structure is named;
  - (3) predictions not built in: the light and graviton relations coincide at all k [S units]; zero vacuum pairs in a
    static field (inherited); the one-species window m0 < 2/3. All are UNTESTED against measurement beyond inheritance;
  - (4) they bend nothing new. Both are readings of CL-1's tick clause, and the lapse layer replaces "sin eps_cube = ...".

## Boundary

- Not rerun on the new kernel: interactions, gauge fields on the slab, and the non-abelian/colour index.
- Not covered: the copy mass on top of FREEZE (the rest phase m N is not checked); moving-source adiabaticity of the lapse
  layer; a finite-range lapse layer.
- Whether the history weight must carry the T-odd term is open.

Uses: register CL-1 (family-class tick, lapse in the step, history-level weighting), t-breaking-tick-lowenergy (FREEZE
rebuild, unique linear term), skip-rule, tick-fraction-waves (B6 relation, speed tie), overlap-from-walk (A1, A2, D1),
overlap-colour (index-based sums), floquet-pi-slab (slab construction, wall diagnostics). Narrows: skip-rule's step-angle
wording and its lapse ceiling; overlap-from-walk's m0 window (to 0 < m0 < 2/3 on the new tick's kernel).
