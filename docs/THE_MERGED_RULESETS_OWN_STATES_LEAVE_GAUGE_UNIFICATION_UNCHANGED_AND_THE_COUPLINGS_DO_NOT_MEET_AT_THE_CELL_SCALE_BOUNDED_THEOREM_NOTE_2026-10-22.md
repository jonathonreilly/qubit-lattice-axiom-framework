---
claim_id: the_merged_rulesets_own_states_leave_gauge_unification_unchanged_and_the_couplings_do_not_meet_at_the_cell_scale_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the merged information-minimisation ruleset (M0-M5: Spin(10) frame group, content = complete 16s, a mirror 16bar per family, a heavy singlet-taste 16, U(1)_chi = N - 5/2 broken by nu^c nu^c, unprotected states gapped at the cell scale). Exact: one-loop b_i and two-loop B_ij rebuilt from the field list reproduce the SM values; a complete 16 or 16bar shifts every b_i by 4/3, and nu^c, the U(1)_chi boson and the nu^c nu^c condensate shift none; Tr X = Tr(Y X) = 0 on the 16. So none of the ruleset's own intermediate states changes the one-loop unification scale or the predicted sin^2 theta_W and alpha_s, whatever its scale; the required B-ratio (b3-b2)/(b2-b1) = 0.718 against the SM's 0.528 is untouched. With the scales the ruleset fixes (mirror and singlet taste at the cell scale, 1.22e18 or 2.44e18 GeV under the two unit-map readings), the running below the cell scale is exactly the SM's. Finite diagnostics (two-loop gauge + top Yukawa, measured M_Z couplings as boundary values): alpha1 = alpha2 at 1.1e13 GeV with 1/alpha3 off by 4.9; alpha2 = alpha3 at 2.9e16 GeV, 1.9 decades below M_cell(B); at M_cell(B) 1/alpha_(1,2,3) = 34.1, 48.4, 51.1. With M_U = M_cell and alpha_em as the only input (0 fitted scales) sin^2 theta_W(M_Z) = 0.161 and alpha_s is non-perturbative (one loop; two-loop pairwise sin^2 = 0.162, alpha_s = 0.179). With M_U fitted (1 FITTED) alpha_s(M_Z) = 0.074 and tau(p -> e+ pi0) ~ 1e24 yr, excluded. A supplied minimal Pati-Salam intermediate fits with 2 FITTED scales (M_I = 1.4e11, M_U = 8.0e15 GeV, 1/alpha_U = 45.2, tau ~ 4e35 yr, passing Super-K by a factor ~18 that is inside its own error), and it cannot place M_U at the cell scale for any M_I. Pure-gauge Wilson lattice-scheme constants at the cutoff have the wrong sign for the 2-3 pair and are a quarter of the size the 1-2 pair needs. The vacuum orientation of the 45, the Higgs-sector content and the ruleset's actual lattice action are not computed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_merged_rulesets_own_states_leave_gauge_unification_unchanged_and_the_couplings_do_not_meet_at_the_cell_scale_2026_10_22.py
---

# The merged ruleset's own states leave gauge unification unchanged, and the couplings do not meet at the cell scale

Claim type: bounded_theorem.
Primary runner: `scripts/the_merged_rulesets_own_states_leave_gauge_unification_unchanged_and_the_couplings_do_not_meet_at_the_cell_scale_2026_10_22.py`.

The merged information-minimisation ruleset (campaign probe minimal-toe-merged) protects one 16 of Spin(10) per family. Its embedding check gives sin^2 theta_W = 3/8 at the breaking scale. Its one-loop comparison found that SM-only running meets alpha1 = alpha2 at 1e13 GeV, with 1/alpha3 off by 5.6, below the proton-decay bound. It left this as a tension that the ruleset's own intermediate states would have to resolve. This note runs the couplings with exactly those states, at the scales the ruleset fixes, and counts every scale that has to be chosen. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) and the [candidate-law register](CANDIDATE_LAWS.md) are unchanged.

## Statement

1. (Coefficients from content, exact.) The one-loop coefficient b_i = -11/3 C2(G_i) + 2/3 sum_Weyl S_i + 1/3 sum_complex-scalar S_i and the two-loop Machacek-Vaughn B_ij are rebuilt from the field list. For 3 x 16 plus one Higgs doublet they give b = (41/10, -19/6, -7) and the standard SM B matrix (G1, G2).
2. (Universality, exact.)
   - A complete 16 has S_1 = S_2 = S_3 = 2 in the GUT normalisation that the Spin(10) embedding fixes, so it shifts every b_i by 4/3 (G3).
   - The mirror 16bar has the same S_i and therefore the same shift.
   - The singlet-taste state is a family singlet that carries a full 16, so it shifts every b_i by 4/3 too.
   - nu^c, the U(1)_chi gauge boson and a nu^c nu^c condensate are SM singlets, with db_i = 0 (G4).
   - On the 16, Tr X = 0 and Tr(Y X) = 0, where X has charges (-5, -1, 3) on (1, 10, 5b). So the fermions induce no hypercharge-chi kinetic mixing (G5).
   - Hence, at one loop, every intermediate state the ruleset names moves all 1/alpha_i by the same amount at every scale. The unification scale, sin^2 theta_W(M_Z) and alpha_s(M_Z) as predicted from alpha_em, and the B-ratio (b3 - b2)/(b2 - b1) do not depend on these states or their scales. Only 1/alpha_U moves. The data need B = 0.718; the SM gives 23/6 / (109/15) = 0.528 (R2).
3. (Law-fixed scales.) The ruleset fixes one dimensionful scale, the cell scale. The two unit-map readings give M_cell = 1.218e18 GeV (u = site) or 2.435e18 GeV (u = rung).
   - The mirror is gapped at the cell scale. M4 requires this, and the QMC probes find a symmetric gap of order the hop.
   - The singlet taste is unprotected (M4), so it sits at the cell scale.
   - Any Spin(10)-breaking orientation of a 45 is a cell-scale vacuum, because no smaller law scale exists.
   - The nu^c nu^c scale is not fixed; m3 alone would need about 5e14 GeV, which would make it FITTED. It is SM-blind anyway.
   - So below M_cell the running is exactly the SM's (T1, T2).
4. (Finite diagnostics, two loop, gauge + top Yukawa.)
   - alpha1 = alpha2 at M12 = 1.08e13 GeV, with 1/alpha_12 = 42.2 and 1/alpha3 - 1/alpha_12 = -4.92.
   - alpha1 = alpha3 at 1.7e14 GeV; alpha2 = alpha3 at M23 = 2.93e16 GeV.
   - At M_cell(A) and M_cell(B), 1/alpha_(1,2,3) = (34.6, 48.0, 50.3) and (34.1, 48.4, 51.1).
   - The couplings do not meet at the cell scale: M12 lies 5.4 decades below M_cell(B), and even M23 lies 1.9 decades below it (R3, R4).
5. (Predictions, with the fitted count stated.)
   - 0 FITTED, M_U = M_cell(B), alpha_em as the only input, one loop: 1/alpha_U = 39.7, sin^2 theta_W(M_Z) = 0.161 against the measured 0.2313, and 1/alpha_s = -2.4, i.e. colour is non-perturbative above M_Z (P1).
   - Two-loop pairwise versions: alpha1 = alpha2 at M_cell needs sin^2 = 0.162, and alpha2 = alpha3 at M_cell needs alpha_s = 0.179 against the measured 0.1180 (P2).
   - 1 FITTED (M_U set by alpha1 = alpha2): alpha_s(M_Z) = 0.074 (P3).
   - The supplied minimal Pati-Salam chain, SU(4) x SU(2)L x SU(2)R with 3 x [(4,2,1) + (4b,1,2)] + (1,2,2)_C + (10,1,3)_C, has b = (-23/3, -3, 11/3) (P4).
     - With 2 FITTED scales, M_I = 1.41e11 GeV and M_U = 7.97e15 GeV, and 1/alpha_U = 45.2. All three measured couplings are used, so no coupling is predicted (P5).
     - For no M_I in [1e4 GeV, M23] does alpha4 = alpha2L happen above M23, so the chain cannot put M_U at the cell scale (P6).
6. (Cutoff scheme constant, estimate.)
   - For pure-gauge Wilson SU(N), 1/alpha_MSbar(1/a) = 1/alpha_lat - D_N, with D_N = (11N/6pi) ln 38.853 - pi/(2N): D_3 = 5.88 and D_2 = 3.49.
   - If the lattice couplings were equal at the cutoff, MSbar would give 1/alpha3 - 1/alpha2 = -2.40, while the data need +2.74 at M_cell(B). The sign is wrong (L1).
   - The 1-2 pair needs 1/alpha1 - 1/alpha2 = -14.2, more than twice the largest constant D_3 (about 2.4 times; L2).
7. (Proton, p -> e+ pi0 by Spin(10) gauge exchange, with M_X = M_U.) The inputs are lattice matrix elements 0.131 and 0.134 GeV^2 (cited), one-loop long-distance A_L = 1.23 and one-loop short-distance enhancement.
   - The 1-FITTED SM point gives 1.4e24 yr, excluded by Super-K (2.4e34 yr) by 1e10 (K1).
   - The PS point gives 4.4e35 yr, passing by 18. That factor is inside the factor-30 error from M_X/M_U = 1/2 to 2 and the hadronic error (K2).
   - X bosons at M_cell(B) give 4.0e45 yr, the same order as the cell-scale contact estimate of the proton-theta probe (K3).

## Derivation

- Coefficients. The index S_i(R) = T_i(R_i) x prod_(k != i) dim_k, with T = C2 = (3/5) Y^2 for the GUT-normalised hypercharge. The coefficients are:
  - b_i = -11/3 C2(G_i) + 2/3 sum_W S_i + 1/3 sum_C S_i.
  - B_ij = -34/3 C2(G_i)^2 delta_ij + sum_W S_i [10/3 C2(G_i) delta_ij + 2 C2_j] + sum_C S_i [2/3 C2(G_i) delta_ij + 4 C2_j].
  All arithmetic is in exact fractions.
- Universality. On the 16, sum over Weyl fields of T_SU3 = 2 (Q: 1, u^c and d^c: 1/2 each), T_SU2 = 2 (Q: 3/2, L: 1/2), and (3/5) sum Y^2 = (3/5)(10/3) = 2. A conjugate representation has the same T and C2. At one loop the matching is a step at each mass, so equal Delta b_i shifts every 1/alpha_i(mu) by the same function of mu. Both the condition alpha_i = alpha_j and the alpha_em-only prediction depend only on the differences b_i - b_j.
- Running. Two-loop gauge with -C_i y_t^2, C = (17/10, 3/2, 2), plus one-loop top Yukawa, RK4 in ln mu. Boundary values: alpha_em^-1 = 127.951, sin^2 = 0.23129, alpha_s = 0.1180, y_t(M_Z) = 0.975.
- Pati-Salam matching at M_I: alpha4 = alpha3, alpha2L = alpha2, and 1/alpha2R = (5/3)(1/alpha1) - (2/3)(1/alpha4). Above M_I the running is two-loop gauge only.
- Proton. Gamma = m_p (1 - m_pi^2/m_p^2)^2 / (32 pi) A_L^2 [(A_SD,1 k^2 (1 + |V_ud|^2) W_RL)^2 + (A_SD,2 2k^2 W_LL)^2], with k^2 = g_U^2 / (2 M_X^2) = 2 pi alpha_U / M_X^2. Here A_SD = prod_i (alpha_i(M_Z)/alpha_U)^(gamma_i/(-b_i)), with gamma = (23/20 or 11/20, 9/4, 2).

## Checks

The runner prints 23 PASS / 0 FAIL in about 1.3 s.
- G1-G5 are exact: the coefficients and the universality and trace identities.
- R1-R4 are the running diagnostics. R1 reproduces the merged probe's one-loop 1.0e13 and 5.60.
- T1-T3 cover the thresholds: T1 and T2 are the ruleset-fixed thresholds, and T3 is a counterfactual mirror light from 1 TeV. T3 gives M12 = 1.7e13 and 1/alpha_12 = 26.6, with the 1/alpha3 mismatch still -5.2: a two-loop shift only.
- P1-P6 are the predictions and fit counts.
- L1-L2 are the cutoff scheme constants.
- K1-K3 are the proton estimates.

## Estimates against measurement

- sin^2 theta_W(M_Z): the 0-fit prediction is 0.161 against the measured 0.23129 +- 0.00004. That is missed.
- alpha_s(M_Z): the 0-fit prediction is non-perturbative (0.179 from the 2-3 pair alone), and the 1-fit prediction is 0.074, against 0.1180 +- 0.0009. That is missed.
- The unification scale does not coincide with M_cell: the nearest pairwise crossing, M23 = 2.9e16, is a factor of 42 to 83 below it. The ruleset fixes no scale between M_Z and M_cell, so any intermediate scale is FITTED. The supplied PS chain needs 2 FITTED scales, plus supplied scalar content, and predicts no coupling.
- Proton: if unification were set by the data with SM content, Super-K would exclude it. The PS fit survives only marginally. Gauge bosons at M_cell are safe by 1e11.

## Boundary

- The vacuum orientation of the 45 (merged decisive calculation 1) is not computed. An aX + bY orientation gives SM x U(1)_chi directly, which is the SM-only case. A 54 or 210 orientation giving Pati-Salam would put M_I at the cell scale (the only law scale), which is again the SM-only case below M_cell.
- Not computed:
  - the Higgs-sector content (row 17 is open; the doublet itself is an incomplete multiplet and is supplied)
  - Y-chi kinetic mixing from scalars
  - one-loop matching constants of the heavy vectors (order T/(12 pi))
  - the ruleset's own lattice action; the Wilson constant is an estimate for a supplied action
  - the induced 1/g^2 at the cell (sibling probe induced-couplings)
- The boundary values at M_Z are comparison data, not inputs to any rule.
- No rule is proposed here.
- Gate for the merged ruleset's unification prediction:
  - item 1 (no fitted number) passes only in the 0-fit reading, and that reading fails measurement.
  - every repair tested needs FITTED scales (1 for SM M_U; 2 for PS) and supplied incomplete multiplets.
