---
claim_id: a_turn_kept_by_the_update_and_broken_by_the_vacuum_gives_cp_and_theta_bar_together_unless_a_nelson_barr_block_is_supplied_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Supplied model, finite diagnostic. Three families with turn charges (1, w, w^2) on Q, u, d; mass entries need a vacuum field of charge q_L - q_R mod 3; all couplings real (T/CP of the update); CP broken only by vacuum phases. (A) Exact: one turn-charged order parameter phi with linear couplings gives det M = p + r1 phi^3 + r2 phi*^3, so Im det = (r1 - r2) v^3 sin 3a; J is 2pi/3-periodic and odd in a. Turn-aligned vacua (phi^3 real) give J = 0 and arg det in {0, pi}. A generic phase gives J != 0 and theta_bar_tree = O(1) (median 1.5 rad over 200 seeded samples, smallest 1e-3, against < 1e-10 required). The renormalizable one-field Z3+T potential has aligned minima only. A reflection (1<->2, phi<->phi*) forces det real and J = 0 together. One tuned real relation gives theta_tree = 0 with J != 0 (FITTED). (B) A Nelson-Barr-type block keeps the turn exact and theta_tree real: the light block comes from a real-aligned turn-charged chi, plus one heavy vector-like down-type copy D and two Z2-odd turn-charged phi1, phi2 entering only the D_L d_R row; the Z2 forbids Q D_R. Then det M_d = det(m_d) M_D is real for every vacuum, and the Z3 x Z2 x T potential's minimum gives J != 0 in 21/40 seeded cases (J = 0 for real phases). J is unsuppressed only for |F| ~ M_D; theta_tree = pi in 17/40 cases (a discrete sign choice). (C) Estimate: a spontaneously broken turn makes Z3 domain walls, so the breaking must happen before or during inflation (T_RH < v). All coupling values are FITTED or seeded."
upstream_dependencies:
  - the_two_tiling_tick_has_no_cell_local_family_symmetry_and_a_turn_triplet_forces_turn_invariant_mixing_to_be_cp_blind_bounded_theorem_note_2026-10-22
  - the_light_copy_carries_a_nonzero_turn_charge_so_a_symmetrically_gapped_mirror_needs_family_count_zero_mod_three_bounded_theorem_note_2026-10-22
  - a_path_sum_flavour_rule_with_forced_rungs_is_family_blind_or_flat_and_its_structural_theta_bar_zeros_kill_cp_or_tie_down_to_up_bounded_theorem_note_2026-10-22
runner: see stems.txt
---

# A turn kept by the update and broken by the vacuum gives CP and theta-bar together unless a Nelson-Barr block is supplied

Runner: runner.py (PASS=15, FAIL=0, 1.4 s, 80 MB). The harness copy gave status ok, exit 0, 1.0 s.

## Question
two-tiling-family-space (TURN-CP lemma): if the masses are turn-invariant on a turn-charged triplet, then J = 0.
family-count-5mode: N_f = 0 mod 3 needs the turn. Escape tested here: the update keeps the turn and T exactly,
and the vacuum breaks both spontaneously.

## Results
1. Family count (logic, not computed). Anomaly matching constrains the exact UV turn in any vacuum. The N = 0 mod 3
   step needs the mirror to be gapped while the turn is still unbroken. It survives only if the turn breaks below
   the mirror-gap scale, in the light sector (v_phi << Lambda_mirror). If the turn-breaking condensate is itself
   what gaps the mirror, the turn is broken there and the count constraint is lost.
2. The vacuum can give J != 0: there is no masking lemma once the vacuum carries turn charge (A3, A5, B3).
3. Strong CP with one turn-charged order parameter fails structurally (A4, A5). The determinant carries charge 0,
   so it depends on phi only through |phi|^2 and phi^3. The same CP-odd invariant Im phi^3 feeds both J and arg det.
   No structural choice in this class separates them. The reflection that forces arg det = 0 also forces J = 0 (A7).
   Tuning one relation is a fit (A8).
4. Nelson-Barr form (B). It works, with theta_tree in {0, pi} exactly and J != 0, but it needs supplied structure:
   - a heavy vector-like down-type copy D;
   - an extra Z2 (D, phi1 and phi2 odd), because the turn alone cannot forbid Q D_R (every charge is reachable);
   - a real-aligned chi, because with only turn-charged light families and no chi the light block is diagonal;
     then the phases rephase away and J = 0;
   - two Z2-odd fields: one is not enough, because phi^3 is Z2-odd and the minimum is then CP-conserving modulo Z2;
   - the scale condition |F| ~ M_D (B5);
   - a positive-sign choice to get theta = 0 rather than pi.
   Loop corrections to theta_bar (the Nelson-Barr quality problem in the literature: Dine-Draper and Vecchi)
   are not computed.
5. Domain walls (estimate). Stable Z3 walls with sigma = v^3 dominate at T ~ 2e-5 GeV for v = 1 TeV, and
   Zel'dovich-Kobzarev-Okun needs sigma^(1/3) below about 1 MeV. A turn that the update keeps exactly gives no
   bias term, so the breaking must precede or occur during inflation, with T_RH below v.

## Theorems / finite diagnostics / estimates / speculation
- Exact (supplied model): A1, A2, A4, A7, B1, B2 and B4.
- Finite seeded diagnostics: A5, A8, B3, B5 and B6. J values from random O(1) couplings are not compared with 3.08e-5.
- Estimate: C.
- Speculation: the extra Z2 might be a cube parity, and chi/phi might be cube-turn-charged composites. Neither is
  shown. YT_CLASS_7_SPONTANEOUS_C3_BREAKING_NOTE_2026-04-18 (on main) found no retained bilinear that carries a
  generation label and could break C3; that would have to be overturned first.

## Gate (anti-smuggling)
Candidate rule: "the update keeps the turn and T; the vacuum breaks them".
(1) No measured number chosen: pass, but every coupling is FITTED, there are roughly 23 real parameters against 10
    flavour observables, and theta_tree = 0 needs a sign choice.
(2) No observed structure by name: FAIL for the version that passes strong CP. It writes in a down-type
    vector-like copy, an extra Z2 and three turn-charged scalars.
(3) Prediction not built for: a heavy vector-like down-type quark with M_D ~ |F|, CKM non-unitarity of order
    (m_d/M_D)^2, and the turn breaking before inflation. All are UNTESTED.
(4) Axiom bent: none (vacuum structure only).
Verdict: FAIL as a rule. The minimal escape (one order parameter) reproduces J only together with an O(1)
theta_bar. The Nelson-Barr version separates them, but only by supplying field content and a Z2 by hand.
Open route: derive the Z2-odd heavy copy and the aligned chi from cube structure (composite before atomic).
