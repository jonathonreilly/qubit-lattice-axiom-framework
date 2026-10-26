---
claim_id: the_rule_fixed_dimension_six_proton_coefficient_is_subluminal_and_outside_the_auger_hadronic_liv_sign_range_bounded_theorem_note_2026-10-26
claim_type: bounded_theorem
claim_scope: "Conversion of CL-1's dimension-six dispersion (link band c_g = -S/24, copy-mass shift c6 = -(1/8)(S - 1/3), S = sum n_i^4; E = p + c p^3/E*^2, E* = hbar c/2L, L = sqrt(8 pi) l_P at kappa = 1) to the Auger convention E^2 - p^2 = m^2 + delta_{had,2} E^4: delta = 2c/E*^2. Sky averages exact (<S> = 3/5: c_g = -1/40, c6 = -1/30, c_q = -7/120). With supplied toy PDFs (2 GeV) and LO N = 4 evolution to E*, the parton weight sum <x^3> is 0.063 (2 GeV) or 0.0045 (E*), giving delta_had,2 = -(0.34 to 4.3)e-57 eV^-2 sky-averaged, -(0.08 to 1.2)e-57 on body diagonals, -(0.7 to 9.1)e-57 on axes: negative (subluminal) on every ray, outside the delta_had > 0 range of Auger 2022. In the pure-proton convention of Maccione et al. 2009, eta_p = -(0.013 to 1.35), beyond their -1e-3 grid edge. Parton-additive composites radiate hard photons (p -> p gamma from 3.2-4.4 EeV) and pions (7-21 EeV); kinematics only, no rates. Not covered: emission rates, nuclear structure beyond nucleon additivity, a fit of the UHECR data with this model."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_rule_fixed_dimension_six_proton_coefficient_is_subluminal_and_outside_the_auger_hadronic_liv_sign_range_2026_10_26.py
---

# The rule-fixed dimension-six proton coefficient is subluminal and outside the Auger hadronic LIV sign range

Runner: runner.py, TOTAL: PASS=13 FAIL=0, 0.2 s, ~120 MB peak, 4.3 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Criteria were fixed before the run (criteria_pre_run.txt). Axioms unchanged; no CL edit; nothing adopted.
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading.

## Sources (fetched 2026-10-26)
- Pierre Auger Collaboration, JCAP 2022, arXiv:2112.06773.
  - Eq. 2.2: E_i^2 - p_i^2 = m_i^2 + sum_n delta_{i,n} E_i^{2+n}.
  - delta_had := delta_p = delta_pi/2 = A^n delta_A.
  - Only positive coefficients (delta_had > 0) are considered.
  - Abstract: delta_had,2 < 10^-57 eV^-2 at 5 sigma CL.
  - The n = 2 number is not a separate fit. It comes from Eq. 6.4, delta_had,n = delta_had,0 R_cut^-n Z^-n with Z = 1, applied to a combined spectrum + Xmax fit with free mixed composition.
  - Photon sector, in the alternative scenario with subdominant protons only: delta_gamma,2 > -10^-58 eV^-2.
- Pierre Auger Collaboration, arXiv:2602.14720 (muon-number fluctuations, composition-independent).
  - Form: E^2 - p^2 = m^2 + eta p^{n+2}/M_Pl^n, negative eta only, applied to pi0.
  - n = 1 only: eta_pi > -1.26e-6, quoted as 5 sigma (it equals the 99.9% CL table row).
  - n = 2 is left for future work. The paper cites the propagation limit eta_pi^(2) < 0.3 (5 sigma), which is the 2022 number converted with eta_pi = 2 eta_p.
- Maccione, Taylor, Mattingly, Liberati, JCAP 2009, arXiv:0902.1756. Form E^2 = p^2 + m^2 + eta p^4/M_Pl^2, pure-proton flux, Auger spectrum.
  - 99% CL: -1e-3 <~ eta_p <~ 1e-6. The lower edge is the edge of their grid.
  - Exception: the narrow region where eta_p and eta_pi are both negative and nearly equal, where |eta_p| < 1e-3 is required.
- Highest-energy events (used in G only): TA "Amaterasu" 244 EeV (Science 382, 903, 2023); Fly's Eye ~3.2e20 eV (recalled from the literature, not fetched).

## Results
- [T] A1. Convention map:
  - delta_had,2 = 2c/E*^2 = 1.35e-54 c eV^-2;
  - eta (MTML) = 2c (M_P/E*)^2 = 201 c.
  - With c < 0 the group velocity is 1 - 3|c|p^2/E*^2, so the term is SUBLUMINAL on every ray. Auger's delta_had > 0 is the superluminal sign (by their Eq. 2.2).
- [T] B1/B2. Directions:
  - <S> over the sky is 3/5 exactly. S runs from 1/3 (body diagonals) to 1 (axes).
  - Sky averages: c_g = -1/40, c6 = -1/30, quark/lepton c_q = -7/120.
  - Axes: c_q = -1/8. Body diagonals: c_q = c_g = -1/72.
  - Fermions are never less subluminal than links.
- [E] C. The hadron step (supplied):
  - c_p = sum_i <x^3>_i c_i, assuming parton additivity at fixed momentum fractions (E_p = sum E_i(x_i P)).
  - The toy PDFs at 2 GeV have valence momentum 0.42 and gluon 0.44, giving W_q = 0.049 and W_g = 0.014 (sum 0.063; shape scan 0.044-0.091).
  - c_i is fixed at the cell, so the RG-consistent matrix element is the N = 4 moment at mu ~ E*. LO singlet evolution (alpha_s(2 GeV) = 0.30 supplied, nf 5 -> 6) lowers it to 0.0045 (scan 0.003-0.007), a factor 0.072.
  - The 2 GeV value is an upper estimate.
- [E] D. delta_had,2 in eV^-2:

| Ray | W at 2 GeV | W at E* | Ratio to 1e-57 (2 GeV / E*) |
|---|---|---|---|
| Axis | -9.1e-57 | -7.1e-58 | 9.1 / 0.71 |
| Sky average | -4.3e-57 | -3.4e-58 | 4.3 / 0.34 |
| Body diagonal (least constrained) | -1.2e-57 | -8.5e-58 | 1.2 / 0.084 |

  - Negative on every ray, so outside the sign range Auger scanned.
  - Auger also states that negative coefficients change attenuation little in their (n = 0) treatment.
  - In exact n = 2 two-body kinematics, the subluminal sign is the one that CLOSES photopion (F1).
  - The two treatments disagree on which sign suppresses interactions at n = 2: with delta_pi = 2 delta_p, the threshold shift goes as (1-x)^3 + 2x^3 - 1 < 0. So even a sign-flipped "by effect" mapping of Auger's number is not clean.
- [E] E1. Under the pure-proton assumption, every predicted eta_p (-0.013 to -1.35) lies outside MTML's allowed region, by 13-1350 x the -1e-3 grid edge. The allowed exception needs |eta_p| < 1e-3 and fails too.
- [F] F1. The GZK branch (pion fraction <= 1/2) of p + gamma_CMB -> p + pi is closed at every energy, even on the body ray at the cell-scale weight (|c_p| = 6.3e-5; eta ~ 0.013 >> 1e-4).
- [E/F] G1, a new consequence. Composites built additively from partons are less subluminal than photons, since W < 1 and |c_p| << |c_g|.
  - So hard vacuum emission p -> p gamma opens at 3.2-4.4 EeV (best photon share y ~ 0.7). Soft emission stays closed.
  - p -> p pi0 opens at 7-21 EeV, because the pion has a larger weight than the proton.
  - Only kinematics are computed. The elastic form factor at |q^2| ~ 10 GeV^2 suppresses the rate (~1e-5), but a crude rate estimate is still far shorter than a Mpc [S].
- [E] G2. For nuclei, the incoherent nucleon-level emission threshold is about A x E_th, which is rigidity-like:

| Nucleus | Threshold (EeV) |
|---|---|
| He | 13-17 |
| N | 45-59 |
| Si | 91-119 |
| Fe | 182-238 |

  The 244 EeV event sits at the Fe threshold.
- [E] P1. The photon delta_gamma,2 is 190-560 x beyond -1e-58. That bound assumes LI electrons, and here gamma -> e+e- is open above 80-122 PeV, so the bound is not applied.
- [E] H1. If the Auger magnitude were imposed regardless of sign, the worst case is the sky average at the 2 GeV weight (4.3 x). Because delta scales as L^2, this needs L x 0.48, i.e. kappa = 0.23 in L = sqrt(8 pi kappa) l_P with G fixed.
  - This bends the one-G clause's kappa = 1 reference (edge stiffness 1), which is a supplied choice, not forced.
  - The split window's cell factor (<= 2) alone could do it.

## Verdict (per pre-registered criteria)
- Auger 2022 hadronic bound: NOT COVERED, because the sign is outside the scanned range and the n = 2 number is a rescaling. So the result is CONSISTENT.
  - A magnitude-only comparison gives R_sky = 0.34-4.3 and R_axis = 0.7-9.1. That is below the factor-10 exclusion line, so at most IN TENSION, and only with the low-scale weighting.
- Auger 2026 muon bound: NOT APPLICABLE (n = 1). The cubic rules have no n = 1 term.
- Pure-proton GZK (MTML 2009): EXCLUDED by >= 13 x, but only under the pure-proton, no-source-cutoff assumption that Auger's composition data disfavour. Per the criteria, IN TENSION.
- Overall: NOT EXCLUDED by any published hadronic LIV bound. The real confrontation is now G:
  - no protons above ~4 EeV;
  - a maximum energy of about A x 4 EeV per species;
  - Fe at ~2e20 eV against the 244 EeV and ~320 EeV events.
  - This is IN TENSION at the Fe edge, with no rate computed.
  - Note that Auger's own mixed-composition fit already wants a Peters-cycle cutoff of about Z x R_cut.

## Rescues if a future fit excludes it
- (i) A smaller cell (kappa < 1, about 0.2). This bends kappa = 1.
- (ii) A cancellation: a rule giving composites the dispersion of their constituents. That would undo additivity (the "soccer-ball" issue) and remove G.
- (iii) The sign is already the GZK-irrelevant one for the Auger bound.

## Assumptions / smuggling review
- Supplied:
  - PDFs and alpha_s;
  - the parton-additivity model of hadron and nuclear dispersion;
  - the choice of scale (2 GeV vs E*);
  - kappa = 1 (unit map), M_P, masses, T_CMB;
  - all literature numbers, and the event energies.
- Forced, by the upstream [F]: c_g, c6, and their angular forms.
- Exact here: the conventions, the sky averages, and the kinematics.
- Not done: emission rates, Fermi motion and binding beyond the separation energy, and a full propagation fit. The direction dependence is compared per ray, because Auger assumes isotropy; the bound applies to the effective coefficient along the arrival directions.
- No rule proposed, so there is no gate to pass.
