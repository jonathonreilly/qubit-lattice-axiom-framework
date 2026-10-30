---
claim_id: a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-field Floquet (circuit) slabs on CL-1's 2x2x2 cell with the site-gauged (111) turn T3 as a symmetry on the turn axis K = kappa (1,1,1). (T1) Sum rule: in each turn sector the eigenphase flow through every quasi-energy equals the winding W_a of det U_a(kappa), so F_0 = F_pi = W in Z[Z3] (augmentation 0). Every circuit of cube-local gates that each commute with T3 (and every exp(-i t H) with H turn-symmetric) has W = 0, so q_mirror = q_light holds in each gap separately. (T2) FREEZE (twist-local-single) has W = (-2, 1, 1); hence FREEZE is not a product of T3-commuting cube-local gates at any depth. (T3) A light q 2 Weyl at 0 with the q 1 mirror only at pi is impossible; light q 2 and mirror q 1 at 0 force flow (-2, 1, 1) at pi, i.e. at least two more Weyls at pi per family. (F) A coupled-layer circuit slab (layers alternating FREEZE and its inverse, turn-commuting tau3-label gates q 1 on even bonds and q 2 on odd bonds, g = 0.5) has its bulk gapped at 0 and pi (0.50 on a 12^4 grid). For odd Ls the near wall holds the light q 2 (hand +1) at (K = 0, 0) and (R, pi), and the far wall holds the mirror q 1 (hand -1) at both. For even Ls the far wall holds q 2. With the anomaly-family-count index and Omega twist, the odd slab allows N_f = 3, 6, 9. Not covered: interactions, gauge fields, the Omega gapping itself, a rule fixing the termination."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_cell_slab_cannot_put_its_mirror_in_the_other_copy_because_turn_axis_eigenvalue_flow_forces_q_mirror_equal_q_light_on_any_static_slab_bounded_theorem_note_2026-10-23
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
  - the_slab_mirror_sits_on_the_light_copy_so_the_turn_anomaly_allows_every_family_count_and_the_number_conserving_spin12_term_cannot_gap_the_mirror_bounded_theorem_note_2026-10-23
  - the_label_selective_charge_four_mirror_term_on_the_freeze_walk_first_exists_at_four_families_and_frees_the_light_partners_bounded_theorem_note_2026-10-23
  - a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
runner: scripts/a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_2026_10_23.py
---

# A circuit slab puts its mirror in the other copy only through a nonzero turn-graded winding, which forces equal flow at quasi-energy pi and is set by termination

Claim type: bounded_theorem. Exact statements are labelled [T], finite diagnostics [F] and readings [S].
Runner: runner.py, TOTAL: PASS=12 FAIL=0, 7.7 s, 62 MB peak, 4.8 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/floquet_pi_slab_test_run.py). Axioms unchanged. No rule adopted.

## Question

copy-flip-slab proved that on any STATIC turn-symmetric slab whose only turn-axis crossings are the wall Weyls,
q_mirror = q_light, so the cube-turn anomaly gives no family-count constraint. It named the escape as a Floquet circuit with
a second gap at quasi-energy pi, as FREEZE has. This note builds the slab as a circuit: layers form the role-block
coordinate, and each tick is FREEZE's cube-local gate sequence per layer plus layer gates. Wall modes are allowed at 0 and
at pi. Questions:
- Can the near wall hold the light (q 2) at 0 and the far wall the mirror in the other copy (q 1), at 0 or at pi, with the
  bulk gapped at both?
- (1) What is the modified sum rule?
- (2) Does FREEZE's structure realise it without fitting?
- (3) Does the anomaly-family-count bookkeeping with Omega then give N_f = 0 mod 3?
- (4) Does the light keep one shared turn charge?

Repo first. A git grep of origin/main (docs, scripts) for "anomalous floquet", "turn-graded winding", "sector winding"
and "coupled-layer" found nothing. This note builds on and narrows:
- copy-flip-slab (D3 and its Floquet reading D4);
- twist-local-single (FREEZE; its A3 finite search);
- anomaly-family-count (the index and the Omega twist selection);
- freeze-mirror-smg (charge-4 terms on FREEZE's label);
- chiral-tick-form (W3 = 0 for exp(-i theta h) circuits).

## Pass criteria

The criteria were written before any code ran (criteria_pre_run.txt). Afterwards, four short scratch scripts outside D
checked the FREEZE winding, the bulk gap against g, and the open slab.

PASS needed all five:
- P1: a bulk-gapped circuit slab with near light q 2 and far mirror q 1;
- P2: the sum rule;
- P3: the far copy forced by a rule;
- P4: allowed N_f = {3, 6, 9};
- P5: one shared light charge, with no light content beyond FREEZE's own pinned pi node.

Predicted: FAIL at P3 only. Every line matched its prediction.

## A. FREEZE on its turn axis

- A1 [T]/[F]. The turn T3 (CL-1's site-gauged C3, T3^3 = 1) is a symmetry of U_F on the axis and keeps Pi+, tau3 and chi.
  - At K = 0, the tau3 = +1 pair (q 1, turn sectors {1, w^2}) and the tau3 = -1 pair (q 2, sectors {1, w}) sit at
    quasi-energy 0.
  - At R they sit at pi.
- A2 [T]/[F]. FREEZE's turn-graded winding is W_F = (-2, 1, 1) over sectors (1, w, w^2). Here W_a is the winding of
  det U_a(kappa) around the axis loop.
  - The axis flow through 0 (at K = 0) and through pi (at R) both equal W_F.
  - There is no other axis crossing.

## B. Sum rule (answer to 1)

- B0 [T]. For a unitary family in one sector, the net number of eigenphases crossing any fixed eps upward equals the
  winding of the determinant. Hence F_0 = F_pi = W, with sum_a W_a = 0, because each gate's total det has zero winding.
  - Static Hamiltonian: W = 0 and there is no pi gap, so F_0 = 0. This is copy-flip-slab D3.
- B1 [T]. Lemma. A cube-local gate that commutes with T3 keeps every turn sector, and its sector det is constant in kappa.
  - On the even tiling the gate is C.
  - On the odd tiling it is D(K) C D(K)^+, and D(kappa) = diag(e^(-i kappa (a1+a2+a3))) commutes with T3 on the axis.
  - So any circuit of such gates has W = 0. So does exp(-i t H) with H turn-symmetric.
  - Checked: a depth-7 random covariant circuit has W = (0, 0, 0).
  - In such circuits each gap balances on its own, and q_mirror = q_light holds at 0 and at pi separately.
- B2 [T]. Corollary. W_F != 0, so FREEZE is not a product of cube-local gates that each commute with the (111) turn, at any
  depth. This upgrades twist-local-single A3 (a finite search at depths 5, 7 and 9 over all 12 rotations) to an exact
  statement, under a weaker covariance (one turn).
- B3 [T]. The single-pair flow is f(q, h) = h (e_(q+2) - e_(q+1)), as in copy-flip-slab D2.
  - (i) A light q 2 at 0 with the q 1 mirror only at pi is impossible: F_0 = (-1, 1, 0) differs from F_pi = (-1, 0, 1),
    whatever W is.
  - (ii) A light q 2 and a mirror q 1 both at 0 give F_0 = W = (-2, 1, 1). The pi gap must carry the same flow, and that is
    no single-pair flow, so there are at least two more Weyls at pi per family. This is a forced pi doubling.
  - Modified sum rule: sum over 0-crossings of f(q, h) = sum over pi-crossings of f(q, h) = W.
  - q_mirror != q_light is allowed exactly when W != 0. That needs gates that are not individually turn-commuting, and the
    pi content then copies the 0 content's flow.

## C. The circuit slab (answer to 2)

Construction:
- Layers alternate F = U_F and F^+.
- Layer gates exp(-i g P (x) X_bond) use the turn-commuting label projectors P_q1 = Pi+ (1 + tau3)/2 and
  P_q2 = Pi+ (1 - tau3)/2.
- The tick is G_odd(q 2) G_even(q 1) (sum_l F_l), with g = 0.5.

Results:
- C1 [F]. The period-2 bulk is gapped at both 0 and pi. The gap is 0.50 at each on a 12^4 grid that contains K = 0 and R.
  - The min gap on 6^4 is 0.20, 0.43, 0.03 and 0.17 at g = 0.2, 0.8, 1.2 and 1.4: a window g < ~1.2, not a tuned value.
- C2 [T]/[F]. The alternation is forced by the bulk gap.
  - An all-F stack has W = Ls W_F, which is (-12, 6, 6) at Ls = 6.
  - Its bulk carries 2 W_F per two layers at every k_l, so an eigenphase passes through 0 and pi for every k_l: gapless.
  - The bulk period must have zero net W.
- C3 [T]/[F]. Odd Ls (7 and 13):
  - The near wall holds the light q 2 (hand +1) at (K = 0, 0) and at (R, pi).
  - The far wall holds the mirror q 1 (hand -1, the other copy) at both.
  - F_0 = F_pi = W = W_F, and the near-wall flow is f(2, +) = (-1, 1, 0).
  - The node states are exact single-layer eigenvectors, because the labels are exact at the nodes.
- C4 [T]/[F]. Even Ls (6 and 12), same bulk: the far wall holds q 2 (hand -1), so q_mirror = q_light, with
  W = F_0 = F_pi = 0.
- C5 [F]. With both labels on the even bonds and the same odd Ls, the whole FREEZE pair sits on the far wall, again with
  W = W_F.
- C6 [F]. The open Ls = 7 slab has no other state at 0 or pi off the nodes (gap 0.52 on a 6^3 wall grid).

Answer (2): yes, it is realised, with no measured number and g in a window. But two things are choices:
- the far copy is fixed by termination (the net number of F minus F^+ layers, i.e. Ls parity);
- the near/far split is fixed by the label bond pattern.

The bulk does not force either. P3 FAILS.

## D. Bookkeeping (answers to 3 and 4)

- D1 [T]. The anomaly-family-count index is applied with the Omega twist k = -q_mirror, using the far-wall
  Z3-Spin(10)^2, Z3-gravity and Z3^3 coefficients.
  - Odd slab (lights {2 at 0, 2 at pi}, mirrors {1, 1}): allowed N_f = {3, 6, 9}.
  - The pi doubling keeps the mod 3, because the node count 2 is prime to 3.
  - The reflected slab (light 1, mirror 2) gives the same set.
  - Even slab: every N_f.
  - The smallest nonzero count is 3, but nothing in the rules prefers 3 over 6. Minimality is still supplied.
- D2 [T]. All light Weyls (both nodes, every stacked family) carry one turn charge, q 2.
  - The turn-CP lemma (J = 0 for turn-invariant masses on a turn-charged triplet) therefore does not force J = 0.
  - J != 0 is allowed, not supplied.
- D3 [S]. A tension with freeze-mirror-smg. On FREEZE's bare label doublet, a T-invariant charge-4 mirror term first exists
  at N_f = 4 (C(N_f, 4) such terms). The Omega in D1 is anomaly-family-count's per-family pairing inside a 16. At N_f = 3 the
  mirror gap therefore needs the 16's internal structure. It is not computed here.

## Answer

1. Sum rule: F_0 = F_pi = W, where W is the turn-graded det winding.
   - q_mirror != q_light is allowed exactly when W != 0.
   - W != 0 is impossible for circuits of turn-commuting gates (B1). FREEZE has W = (-2, 1, 1), which proves that its
     layering cannot be turn-covariant.
   - The mirror cannot sit at pi alone. If it sits at 0 in the other copy, the pi gap must repeat the flow (at least two
     more Weyls per family).
2. FREEZE's structure realises the copy-flipped slab: alternate FREEZE and inverse layers, with label dimer gates. The bulk
   is gapped at 0 and pi. The near wall holds q 2 at 0 and pi, and the far wall holds q 1 at 0 and pi.
   - It is NOT forced: Ls parity and the bond pattern choose the far copy, and even Ls gives q_mirror = q_light.
3. On the odd slab the bookkeeping gives N_f = 0 mod 3 (3, 6, 9). Minimality is still supplied, and the gapping at N_f = 3
   needs the 16 pairing (D3).
4. Yes. One shared light charge, q 2, so J != 0 is allowed.

Synthesis: FAIL at P3 only, as predicted. P1, P2, P4 and P5 pass.

## Gate (anti-smuggling)

No rule is proposed. A rule "the slab holds an odd net number of FREEZE ticks" would fix the termination to obtain 3. That
fails item 1 in spirit, because its only motive is the count, unless it predicts something else.

UNTESTED predictions of the construction:
- the pi-quasi-energy light partner at R on the light wall (tick-staggered, as in FREEZE);
- the mirror at both nodes on the far wall.

## Smuggling review

Supplied:
- FREEZE (twist-local-single);
- the F/F^+ alternation (forced by the bulk gap only once FREEZE layers are given);
- the label bond pattern;
- g;
- Ls and its parity;
- free fields;
- the Omega term and the 16 (anomaly-family-count).

Forced:
- the Floquet sum rule;
- the covariant-gate lemma W = 0;
- FREEZE's W_F = (-2, 1, 1) and the exact no-covariant-layering corollary;
- the impossibility of a pi-only mirror;
- the forced pi doubling;
- the termination dependence of the far copy;
- the mod 3 on the odd slab;
- the shared light charge.

Not shown:
- interacting gapping of the far wall at N_f = 3;
- gauge fields;
- a rule that fixes the termination.
