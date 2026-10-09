# E2 and E3: worker report (Claude Opus 5.5, xhigh; 2026-10-09)

Verbatim final report. Referee pending (codex gpt-5.6-sol xhigh); verdicts are not recorded in TESTS.md until it returns. Scripts in `scripts/E23/`.

**What I read first:** the full axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`, all 233 lines) and `PRIMITIVE_REGISTRY_CHECK.md` (three primitives; none supplies a substrate). In the exercise folder I read SUMMARY, TESTS (E2/E3 readings at `TESTS.md:184-209`, unchanged), R3_price, kill_F1a and its referee, R1 and OUTSIDE_VIEW, and reused their formulas.

## Plain summary

None of the substrates passes. Each one either resists shear on average, or carries a random patchwork of stiffness that doesn't fade at long wavelengths.

- **Grid with sites missing (E2):** at every occupancy p tested, the vacuum still resists shear on average in both channels. Every p < 1 adds white noise (the per-site random part does not thin out at long wavelengths). Letting sites appear over time just moves along the same curve: the noise only vanishes at p = 1, which is the full crystal.
- **Quasicrystal (E3a):** its noise is strongly suppressed, but its average stiffness is not zero. The value is direction-independent and depends on the coupling range. At R3's range R = 1.8 it happens to be close to zero; at R = 2.2 it is about as large as the crystal's.
- **Hyperuniform disordered sets (E3b):** a smooth point density does not give a smooth stiffness. The noise is white and the mean is nonzero.
- **Growing random set (E3c):** zero mean, but white noise at every stage. Nothing moves, so growth never smooths the noise away.

The pattern across all of them: the ordered sets have suppressed noise but a nonzero mean, and the zero-mean (Poisson-like) sets have white noise. No frozen substrate tested has both a zero mean and suppressed noise.

## Method

- **Field:** a free scalar, H = ½π² + ½φ(L_g+m²)φ, on the present points only. The metric is g = e^{th} with h traceless. E′ and E″ are computed exactly by eigen-perturbation (R3's formula).
- **Validation (CHECKED):**
  - The crystal reproduces 0.0473827 / 0.0140046.
  - Finite differences agree to 9 digits.
  - The small-p slopes match the exact isolated-pair term.
- **Couplings:**
  - (i) nn: unit Z³ bonds among present sites, weight 1/d_g².
  - (ii) pd: R3's kernel, R = 1.8, with pairs chosen by the current proper distance.
- **Fields:** bosons at m² = 1 and 0.04, plus a smeared spinless fermion sea as a secondary check.
- **Noise:** K1's estimator, sd·√N per direction against box size. White means flat, i.e. exponent q = −0.5.
- **Quasicrystal:** open patches, with the local density ½[√(L+m²)]_ii. A 2.5-unit edge buffer biases the mean by about 1e-6 (checked).

## E2: mean stiffness per present site (boson m² = 1, SE ≤ 4e-4) and noise sd·√N

| p | pd E_g | pd T_2g | nn E_g | nn T_2g | sd·√N (pd T_2g / nn T_2g) |
|---|---|---|---|---|---|
| 1 | +.0474 | +.0140 | +.168 | −.183 | 0 / 0 |
| 0.9 | +.0424 | +.0136 | +.154 | −.171 | .017 / .041 |
| 0.7 | +.0321 | +.0125 | +.125 | −.145 | .044 / .059 |
| 0.5 | +.0220 | +.0109 | +.092 | −.113 | .067 / .080 |
| 0.3116 (p_c) | +.0127 | +.0083 | +.059 | −.077 | .075 / .077 |
| 0.1 | +.0035 | +.0033 | +.019 | −.027 | .054 / .061 |

- **Small-p slopes (EXACT):** pd +0.0329p / +0.0385p; nn +0.1925p / −0.2887p.
- **Light boson, pd:** E_g changes sign between p = 0.5 and p_c, while T_2g stays at +0.026. That is a zero in one channel only, and its position depends on the mass.
- **Fermion sea:** the two channels are never zero at the same p.
- **Noise:** all 24 pooled fits (L = 8–24, N ≈ 50–2000) give q between −0.60 and −0.38, each within 2 SE of white.
- **Percolation threshold:** the curves are smooth through p_c.
- **Growing dilution (b):** sites appear and never disappear. By Theorem A (`docs/RECORD_ACTIVATION_CRITICALITY_AND_CONDITIONED_PLANAR_MODELS_BOUNDED_THEOREM_NOTE_2026-10-08.md:66`, landed), the set at any fixed time is Bernoulli(p(t)).
  - Stage means equal the frozen ones (CHECKED).
  - The random part carries over between neighbouring stages (correlation 0.2–0.7) and is partly refreshed by new sites.
  - What the vacuum responds to is the instantaneous present set. This "adiabatic" reading is a supplied assumption.

## E3: per substrate (pd coupling, m² = 1, density 1)

| Substrate | Mean E_g / T_2g | Noise | S(0) |
|---|---|---|---|
| Icosahedral cut-and-project set, spherical window (not the Ammann–Kramer tiling), R = 1.8 | −0.00020 ± 0.00007, same in both channels | n = 1138 averages scatter 0.33–0.47× independent sites; S_F(k = 0.5) 6× below Poisson and falling | ≈ 0 |
| same set, R = 2.2 | **+0.04542 ± 0.00009**, same in both channels | same | ≈ 0 |
| same set, pair-potential level, by range | −0.067 (R 1.2), +0.003 (1.8), +0.198 (2.2), −0.092 (3.0) | pair-level S_F(0.15) 35× below Poisson (195k points) | ≈ 0 |
| Perturbed Z³, s = 0.1 / 0.3 / 0.5 / 0.8 | .033/.017; .0099/.0089; .0039/.0038; .0008/.0009 (5 SE) | sd·√N .015–.07, flat in L | > 0 |
| Perturbed Z³, s ≥ 1.2 | not resolved (< 4e-4) | ≈ Poisson's .067 | > 0 |
| Stealthy hyperuniform, χ = 0.30 (S(k ≤ 4.7) < 1e-26) | +.024 / +.024 | q = −0.41 ± .08, −0.50 ± .08 | > 0 |
| Growing Poisson, ρ = 0.25 → 2 | 0 within 3 SE | sd·√N .045–.08 at every stage | > 0 |

## Verdicts against the fixed readings

- **E2: FAIL** (bounded). The mean is nonzero in both channels at every p searched, and S(0) > 0 for every p < 1. Only p = 1 has S(0) = 0, and its mean is the crystal's. Searched: p ∈ {1, .9, .7, .5, .3116, .3, .2, .1}, two couplings, three fields, frozen dilution plus one growth schedule.
- **E3(a) quasicrystal: FAIL on the mean.** It is isotropic and nonzero. Its size swings with the coupling range and crosses zero only at isolated ranges, so a zero there would be tuning. Its noise is suppressed (CHECKED at pair level; indicative for the full functional).
- **E3(b) hyperuniform: FAIL on both.** The mean is nonzero and the stiffness noise is white, even though the point density is hyperuniform.
- **E3(c) growing Poisson: FAIL on noise.** The mean is zero, as Lemma A predicts. In the version where the range scales with spacing, every stage has exactly K1's law (EXACT).

**Predictions tested, not assumed:**
- "Solid-like ⇒ shear stiffness" is confirmed for every ordered or correlated set.
- Icosahedral symmetry forcing E_g = T_2g is confirmed.
- R3's lemma (`R3_price.md:34`) is confirmed: the quasicrystal's pair-level response oscillates with range.
- Prior art: with b = 0, pair-level shear-blindness forces g₂ ≡ 1 and hence S(k) ≡ 1, so a pair-level zero mean and a hyperuniform density exclude each other (`kill_F1a.md:24`).
- The referee's open escape, a "hyperuniform stress" (`kill_F1a_referee.md:58`), is not provided by a hyperuniform density.

**One light cone (separate observation, ARGUED).** Every substrate here is a static spatial medium. Because records are permanent, present sites are fixed world-lines even while the set grows, so each substrate has a rest frame. None has T1's hypercubic time–space symmetry (`TESTS.md:62-70`), so a Collins speed split between species is expected. Not computed.

## What a referee should re-check

1. Only the spherical window was run. The polyhedral-window Ammann–Kramer tiling was not.
2. Quasicrystal S(0) for the full functional rests on one radius-11 patch plus the 12-patch scatter.
3. The perturbed-lattice mean at s ≥ 1.2 is unresolved.
4. The fermion sea at p = 1 is sensitive to box size.
5. The periodic-box fixed-N noise estimator is argued, not proved, to be a lower bound on S(q→0).
6. The nn weight 1/d_g² is a supplied choice; with it, T_2g appears only at second order.

**Labels:**
- EXACT: the small-p slopes; the Theorem-A reduction; icosahedral isotropy; the scale-free growth stage equal to K1's law.
- CHECKED: all the tables.
- ARGUED: the light cone; the lower-bound property of the noise estimator.
- COMPARATOR: Collins et al.

Files are in /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/ex_grav/E23/ (each .py has a matching .out):
- e23_core.py
- E2_0_validate.py
- E2_1_frozen_dilution.py
- E2_1b_noise_extension.py
- E2_2_growing.py
- E2_3_pooled_fits.py
- E2_4_table.py
- E3_a_core.py
- E3_a0_validate_local.py
- E3_a1_quasicrystal.py
- E3_a2_patch_noise.py
- E3_a4_qc_precision.py
- E3_a5_pair_level_scan.py
- E3_a6_pair_level_window_noise.py
- E3_a7_pair_level_Sk.py
- E3_a8_pool_precision.py
- E3_b_hyperuniform.py
- E3_b2_large_s_and_control.py
- E3_b3_stealth_more.py
- E3_b4_stealth_pooled.py