# T57 pre-registration (written BEFORE running t57_test.py)

Wall: R_base x S = 31/9 x S is a group-theory identity presented as Omega_DM/Omega_b.
Inputs are the lane's own (bypass note 2026-04-25 and R_BASE note): m_DM = 16 v = 3940.5 GeV,
alpha_X = alpha_LM = 0.090668, x_F = 25 (band 22-28), K = 1.07e9 GeV^-1, g* = 106.75, M_Pl = 1.2209e19,
S = 1.59 (band 1.4-1.7), R_pred = 31/9 * 1.59 = 5.4767. Data: Planck Omega_c h^2 = 0.1200, Omega_b h^2 = 0.02237
(R_obs = 5.364 +/- 0.065), eta_obs = 6.12e-10, m_p = 0.938272 GeV.

Question the test decides: does ANY physical mechanism class reproduce Omega_DM/Omega_b = 5.48 (5%) from the
lane's own inputs with NO new free number, so that R_base x S is a consequence and not an input?

Mechanism classes:
 (I)   both populations symmetric freeze-out relics (Lee-Weinberg ratio; the April 2026 reading), with the
       visible population = baryons (m_p).
 (IIa) shared conserved charge, rational n_DM/n_b (Kaplan-type asymmetric DM): R = (m_DM/m_p)(n_DM/n_b).
 (IIb) same, transfer decoupling at T_d (Boltzmann-suppressed DM asymmetry).
 (IIc) WIMPy conversion of symmetric DM annihilation into baryon number with CP fraction eps.

Pre-registered readings (per class):
 PASS = reproduces R within 5% of 5.48 with zero new free number.
 FAIL = misses by more than a factor 100, OR needs a new free number (T_d, eps, or a non-rational n ratio).
Predicted before running: (I) FAIL by ~6-7 orders (R_sym ~ 1e6-1e7 with lane's alpha; ~1e10 with QCD 1/m_pi^2);
 (IIa) FAIL: needs n_DM/n_b ~ 1.3e-3 at 16 v, or m_DM ~ 5 GeV at rational ratio (contradicts 16 v);
 (IIb) needs T_d ~ m/10 (new number); (IIc) needs eps ~ 1e-9..1e-8 (new number).
Overall wall PASSED only if some class passes. Predicted: no class passes -> R_base x S has no derivational role.

Supporting checks (pre-registered readings):
 C1 R-free headline: Omega_DM h^2 from the relic formula alone at (16 v, alpha_LM, x_F 22-28). Predicted 0.1275
    (band ~0.112-0.143). Reading: if the band contains 0.1200 the lane's DM-side claim needs no R.
    Also confirm the bypass table's "R = 5.48" row equals the INPUT R (circular): Omega_b := Omega_DM / R.
 C2 look-elsewhere on the base: enumerate a fixed family of alternative bases built from the same Casimir data
    (6 weight styles x 6 num/den choices x 7 prefactors = 252). Count alternatives whose R_alt x S lands in
    R_obs +/- 2 sigma for some S in [1.4, 1.7]  (R_alt in [3.079, 3.924]).
    READING: the numerical agreement counts as evidence for the Casimir-adjoint identification only if
    < 5% of alternatives also land there. Predicted: 10-25% do -> weak evidence.
 C3 charge-assignment sensitivity: R_base = (3/5) f_vis/f_dark with f = C3*8 + C2*3 evaluated at the dark state's
    actual charges. Exact fractions for dark = (colour singlet, doublet) / (triplet, doublet) / (triplet, singlet)
    / true singlet. Predicted: 31/9, 3/5, 93/128, undefined. Reading: 31/9 is an output of a charge choice
    that the lane's own step 3 and G1 chain contradict.

## Post-run note (appended after t57_test.out was produced; the pre-registered text above is unchanged)
- (I), IIa, IIb, IIc, C1, C3: came out as predicted (R_sym 4.1e6 lane formula / 6.0e9 hadronic; needed n ratio 1.30e-3; T_d 356-465 GeV;
  eps 1.2e-8; Omega_DM h^2 0.1275, band 0.112-0.143; charge table 31/9, 3/5, 93/128, undefined).
- C2 MISSED my prediction: 3.6% (family A, 252) and 5.1% (family B, 1224) of alternatives land in the S-free window, not 10-25%.
  Against the pre-registered 5% threshold that is borderline (A below, B above). Reported as such: the 2% numerical agreement is a
  modest coincidence (about 1-in-20 to 1-in-30; 1-in-125 with S fixed), not empty, and not informative about which populations R compares.
