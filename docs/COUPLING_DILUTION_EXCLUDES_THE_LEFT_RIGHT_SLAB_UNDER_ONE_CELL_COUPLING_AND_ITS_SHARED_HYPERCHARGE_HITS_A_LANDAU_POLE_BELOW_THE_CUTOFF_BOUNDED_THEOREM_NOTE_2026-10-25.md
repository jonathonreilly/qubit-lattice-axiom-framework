---
claim_id: coupling_dilution_excludes_the_left_right_slab_under_one_cell_coupling_and_its_shared_hypercharge_hits_a_landau_pole_below_the_cutoff_bounded_theorem_note_2026-10-25
claim_type: bounded_theorem
claim_scope: "Exact layer-chain and matching identities plus one-loop estimates against measured couplings for the left-right slab (SU(3) and U(1)_Y shared across the bulk, SU(2) per wall, mirror at v'). Exact: a flat zero mode over Ls layers has 1/g4^2 = sum_k 1/g_k^2 (rational arithmetic, error 1e-26), a disordered-link wall mode has g4 = g_wall, so one common cell coupling gives alpha_3 : alpha_sh : alpha_2 = 1/Ls : 1/Ls : 1 at the cutoff; H' breaks SU(2)' x U(1)_sh to Y_low = T3' + Y_sh with 1/alpha_Y = 1/alpha_sh + 1/alpha_2' (7e-11); b = (41/3, -19/6, -3) above v' from the field list. Estimates (supplied: MZ couplings, Lambda = 2.4e18 or 1.22e18 GeV, v' in [1e8, 1e11] GeV, one-loop): the shared U(1) has a Landau pole at 8e14-1.3e18 GeV, below 2.4e18 for every v' in the window (it clears only for v' > 9.5e11); Ls_fit = alpha_2/alpha_3 at the cutoff is 0.64-0.73 (1.04 without mirror), asymptote 0.95 (2.21 without mirror) for any cutoff; with alpha0 fixed by alpha_2, alpha_s(MZ) = 0.043 (Ls = 1), 0.014 (Ls = 2), 4e-4 (Ls 46-58); no continuous Ls in [1, 100] fits alpha_s and alpha_Y within 10% (best 61%); a weak SU(2) wall with a confining SU(2) bulk needs couplings differing by 6.3x; per-layer beta3 = 14.9-19.0/Ls, so flat colour needs Ls <~ 5-6, disjoint from the portal's 46-58. Not covered: two-loop running, anisotropic or Monte Carlo bulk phases, the CL-1 cell slab, a derivation of v' or of any per-factor coupling."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - mirror_quark_portal_is_a_shared_hypercharge_bare_mass_that_keeps_theta_tree_zero_and_lets_mirror_quarks_decay_bounded_theorem_note_2026-10-24
  - wall_local_electroweak_registers_are_realisable_on_a_confining_layer_bulk_but_chosen_and_leave_stable_fractional_charges_bounded_theorem_note_2026-10-24
  - face_swap_parity_gives_a_tree_level_zero_theta_only_with_wall_local_electroweak_registers_and_shared_colour_bounded_theorem_note_2026-10-24
  - one_running_cell_coupling_sets_the_colour_to_weak_rung_ratio_but_fits_the_weak_and_seesaw_ranks_and_fails_for_the_electroweak_factors_bounded_theorem_note_2026-10-22
runner: scripts/coupling_dilution_excludes_the_left_right_slab_under_one_cell_coupling_and_its_shared_hypercharge_hits_a_landau_pole_below_the_cutoff_2026_10_25.py
---

# Coupling dilution excludes the left-right slab under one cell coupling, and its shared hypercharge hits a Landau pole below the cutoff

Claim type: bounded_theorem. Labels: [T] exact, [E] estimate with supplied numbers, [S] reading.
Runner: runner.py, TOTAL: PASS=12 FAIL=0, 0.9 s, 35 MB peak, 4.0 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (coupling_dilution_test_run.py in the scratchpad, removed after the run).
Axioms and register unchanged; no rule adopted. Criteria were written before any code (criteria_pre_run.txt).

Register check. CL-1 'Couplings' does NOT fix one common coupling: it reads couplings per factor from flavour
counts F per end and states that no factor-blind rule fits. 'One running coupling' (one-gap-scale) was REJECTED at
the gate (U(1)_Y 32% off colour in GUT normalisation). So "one common cell coupling" is tested here as a hypothesis.
Repo first: git grep of origin/main for slab coupling dilution found nothing relevant.

Pre-set mismatches (recorded, not tuned away):
- P1 first run: float inversion of the near-singular chain gave 3e-4 error (a conditioning artefact, not physics).
  Replaced by an exact rational Schur complement: 1e-26.
- P3: the pre-set criterion (pole below 2.4e18 for the whole window) holds. The code first also demanded it for the
  1.22e18 cutoff reading; at v' = 1e11 with a single threshold the pole (1.31e18) clears that reading. Recorded as an
  exception; the spread-threshold variant puts the pole at <= 5e15 everywhere.
- P4: hand-estimate slip. 1/alpha_Y(cutoff, SM normalisation) is 57.2, not 20.6. So the SM-only control gives
  ratios 1.13 (SM), 0.68 (GUT) and 40.7 (cell 1/6), not "> 25% off for all three". The SM-normalised control is within
  13%. This is not the structure under test: in the LR slab the shared U(1) has a pole in the whole window.
- P6: the pre-set alpha_s(MZ) = 0.15 at Ls = 1 is the SM-only control (measured 0.153). With the mirror content
  (b3 = -3 above v') it is 0.043. The Ls window giving alpha_s in [0.110, 0.126] is empty for Ls >= 1.
- P7: the wall-local D2 value 14.9/Ls is reproduced with mirror thresholds spread at m_f v'/v. A single threshold at
  v' gives 16.9-19.0/Ls. Both are printed; the conclusion is the same.

## A. Dilution law [T]

- A1. Gaussian layer chain with in-layer inverse couplings 1/g_k^2 and inter-layer stiffness kappa > 0: as p -> 0,
  p^2 G_00(p) -> 1/sum_k(1/g_k^2), for Ls in {2, 5, 16, 50} and kappa in {0.1, 1, 10} (exact rationals, 1e-26).
  With kappa = 0 (disordered links) the wall mode has g4 = g_wall.
- So with ONE cell coupling g0 on every link: 1/alpha_3 = 1/alpha_sh(c) = Ls/alpha0 (shared) and 1/alpha_2 = 1/alpha0
  (wall-local). Two consequences:
  - the shared factors must be EQUAL at the cutoff, whatever Ls is (an Ls-free test);
  - Ls = alpha_2/alpha_3 at the cutoff.
- The U(1) normalisation c (1/alpha_common = c/alpha_Y) is supplied: SM 1, GUT 3/5, register cell unit 1/6 -> 36.
- A2 [T]. In this structure the low-energy hypercharge is NOT the shared U(1). H' (an SU(2)' doublet with Y_sh != 0,
  needed for the mirror masses D = Y^dag h') breaks SU(2)' x U(1)_sh to Y_low = T3' + Y_sh. Light fields have T3' = 0,
  so they keep their charges, and 1/alpha_Y(v') = 1/alpha_sh(v') + 1/alpha_2'(v'), with alpha_2' = alpha_2 by P_slab.
  Checked by diagonalising the neutral mass matrix (7e-11). This is the Babu-Mohapatra matching (Y_sh = (B-L)/2).
- A3 [T]. From the field list: b(SM) = (41/6, -19/6, -7) and, above v', b = (41/3, -19/6, -3) (SM normalisation for
  U(1)). The mirror doubles the shared U(1) slope and leaves SU(2)_L untouched.

## B. Against measurement [E] (one loop, supplied MZ inputs)

- B1. Shared hypercharge Landau pole (P3):
  - 1/alpha_sh(v') = 1/alpha_Y - 1/alpha_2 = 47 (v' = 1e8) to 36 (v' = 1e11), single threshold;
  - with slope 41/3 it reaches zero at 2.1e17 to 1.3e18 GeV (single threshold), or 8e14 to 5e15 GeV (mirror
    thresholds at m_f v'/v);
  - so it is below the cutoff 2.4e18 for every v' in the face-swap window, and the pole clears 2.4e18 only for
    v' > 9.5e11 GeV.
  - Dilution only RAISES 1/alpha_sh at the cutoff (Ls/alpha0 > 0), while the measured running needs it negative.
    So the shared-U(1)_Y LR slab is excluded in the window for EVERY Ls and every normalisation, with or without one
    common coupling. This is new: the portal and wall-local notes did not run U(1)_sh.
- B2. Ls-free equality (P4): above the window, c/alpha_sh = 1/alpha_3 at the cutoff only for the cell unit (c = 36),
  at v' = 7.2e12 GeV. That is outside the window (and set by fitting v'), and there Ls_fit = 0.87 < 1. SM and GUT
  normalisations never equalise for v' in (9.5e11, 1e17).
- B3. Colour vs SU(2) (P5): Ls_fit = 0.64-0.73 with the mirror, 1.03-1.04 SM-only, at both cutoff readings.
  - Asymptotic freedom does NOT rescue dilution. The ratio (1/alpha_3)/(1/alpha_2) tends to b3/b2 for any cutoff:
    2.21 SM-only (so Ls >= 3 is excluded for any cutoff, and Ls = 2 needs ln(Lambda/MZ) = 478, Lambda ~ 1e209 GeV)
    and 0.95 with the mirror (every Ls >= 1 is excluded).
  - QCD's faster running is exactly what makes alpha_s > alpha_2 at MZ from alpha_3 ~ alpha_2 at the cutoff. It has
    no room to absorb a factor Ls >= 2.
- B4. Downward prediction (P6), alpha0 fixed by alpha_2(MZ), v' = 1e10, Lambda = 2.4e18:
  - Ls = 1: alpha_s(MZ) = 0.043;
  - Ls = 2: 0.014;
  - Ls = 5: 4.6e-3;
  - Ls = 46-58: 4.5e-4 to 3.6e-4.
  - The measured value is 0.118. SM-only control: 0.153 (Ls = 1) and 0.018 (Ls = 2).
  - The best joint fit to (alpha_s, alpha_Y) over continuous Ls in [1, 100], every c, v' and cutoff misses by 61%.
- B5. SU(2) wall-locality with one coupling (P8): wall-local A2 needs a confining SU(2) bulk, beta_b <= 2.45, i.e.
  1/alpha_bulk <= 7.7. The wall needs 1/alpha_2(cutoff) = 48.6, which is 6.3x apart. One coupling cannot make SU(2)
  wall-local at all.
- B6. Per-factor couplings instead (P7, a FIT): the per-layer beta3 is 14.9-19.0/Ls, so a flat (weak) colour bulk with
  beta3 >= 3 (supplied 5D value) needs Ls <~ 5-6. At the portal's Ls = 46-58 it is 0.26-0.41: a deeply
  strong-coupled colour bulk, not a flat shared register. The two windows are disjoint (sharpens wall-local D2).

## Answers

1. Ratios at the cutoff: g_s^2 : g_Y,sh^2 (normalised by c) : g_2^2 = 1/Ls : 1/Ls : 1. The danger is real.
   Running does not rescue it: alpha_2/alpha_3 at the cutoff is 0.64-1.04 against Ls >= 2. And the shared U(1)
   becomes non-perturbative below the cutoff.
2. No Ls fits all three. The colour fit wants Ls < 1, the hypercharge has a pole, and neither the portal window
   (46-58) nor the flat-colour bound (<= 5) is reachable. The two Ls windows are also mutually disjoint.
3. Verdict: EXCLUDES the LR slab under one common cell coupling (B1, B3, B4, B5, each independently). The
   shared-U(1)_Y LR slab is ALSO excluded with per-factor couplings in the v' window (B1). With per-factor couplings
   and v' > 1e12, it would be a FIT that also contradicts the face-swap theta bound v' < ~1e11.

## Gate (for "one cell coupling, flat bulk zero mode for shared factors")

1. Measured numbers: none chosen to pass. Ls is scanned, never fitted to a pass.
2. Named structure: the share set {SU(3), U(1)_Y} and SU(2) per wall are inherited from the portal note (risk noted
   there).
3. Prediction not built for: coupling ratios at the cutoff. Tested and FAILED (excluded).
4. Bends: the Links clause (layer registers) and the Lattice axiom (physical layers, owner decision 5), as upstream.

## Walls move (next)

- A share set without the U(1)_sh pole: share SU(3) only and make hypercharge a wall-local U(1) on each wall plus a
  (q, -q) condensate (portal option (i)). Its running is per wall and has no doubled slope; test against B1/B3.
- Colour wall-local with an undiluted wall coupling and SU(2) shared? That is face-swap B4 (excluded).
- A non-flat (warped/anisotropic) zero-mode profile changes sum_k 1/g_k^2 into a weighted sum. That could give
  dilution < Ls but cannot give enhancement (A1 is a sum of positives), so B3's alpha_2/alpha_3 < 1 still needs
  colour layers STRONGER than SU(2) layers.

## Smuggling review

- Supplied:
  - the MZ couplings and PDG masses;
  - the cutoff readings and the v' window;
  - one-loop running with step thresholds;
  - the normalisations c;
  - the 5D beta3 ~ 3 and SU(2) beta_b <= 2.45 values from wall-local;
  - P_slab g2' = g2.
- Forced:
  - the layer-sum law (A1);
  - the T3' + Y_sh matching (A2);
  - the b coefficients from the field list (A3);
  - the asymptotic ratio b3/b2.
- No measured number was chosen to pass anything.
