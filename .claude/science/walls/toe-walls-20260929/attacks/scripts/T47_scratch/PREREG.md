# T47 attack: pre-registration (written BEFORE any of the tests below were run)

Attacker: Claude Sonnet 5.5 (same family as supervisor Opus 5.5). Same-family check, not an independent referee.
Wall T47 = L09-W6 (up-quark amplitude/ratios) + L09-W7 (Route-2 E-center readout, target (-1,-2,21/4)).

## Test A (decides W7): infinite-volume limit of the Route-2 readout ladder
Object: the repo's own runner module `frontier_quark_route2_honest_gravity_metric_rhoe_characterization`
(imported read-only) with (i) its original max-abs floor and (ii) two smooth replacements
(signed xx trace-free component at probe 0; Frobenius norm at probe 0), extended from N=11..21
(lane's ladder) to N up to ~61 with the physical probe radius 4.25 held fixed.
Rows reported: q_T = gT(center)/gT(shell) (target 5/6), s_TE = gT(shell)/gE(shell) (target -2),
rho_E (target 21/4).
Physics prediction made BEFORE running (from reading adm_metric): the metric is the isotropic-Schwarzschild
form (lapse (1-phi)/(1+phi), spatial psi^4), which is vacuum at LINEAR order for harmonic phi, so G^TF is
second order in phi and eta_floor(q) is ~ a quadratic form in q. Its q-derivative is then a
monopole x (dipole or quadrupole) cross term. The center source E0 and the shell source S_UNIT carry the
same monopole (total charge 1); they differ only at l>=4. Hence for a smooth functional at large N:
  P1: q_T -> 1 (i.e. b_T/a_T = 6(q_T-1) -> 0, NOT -1);
  P2: q_E -> 1, so rho_E = 6(q_E-1) -> 0 (|rho_E| < 1), NOT 21/4;
  P3: box-wall image charges (Dirichlet) drive the sign changes seen at N=13..21; they decay with N.
PASS reading (Route 2 readout survives): for the three largest N (>=45) some functional gives
  q_T within 2% of 5/6, s_TE within 5% of -2, rho_E within 5% of 21/4, with successive-N differences <1%.
FAIL reading (Route 2 is a finite-box coincidence): the ladder converges elsewhere (e.g. P1, P2), or does not converge.
Extra check A2: probe-radius scan R in {3.5,4.0,4.25,5.0,6.0} at fixed large N: if the triple is a
derived rational it should be a plateau; if it is a supplied-geometry number it moves with R.

## Test B (decides W6 edge): is the "up ratios inverted from CKM" edge predictive?
Object: the repo's minimal Schur-NNI carrier (`frontier_quark_mass_ratio_full_solve.py`, imported read-only):
inputs = atlas |Vus|,|Vcb|,|Vub| + Phase-1 down ratios (R_DB, R_SB) + four NNI coefficients
(C12_U,C23_U,C12_D,C23_D = 1.48,0.65,0.91,0.65), output = (m_u/m_c, m_c/m_t).
The historical note says the four coefficients were FITTED to observed CKM angles with observed masses.
B1 sensitivity: perturb each coefficient by +-5% and re-invert. 
B2 coefficient-blind prior: sample log-uniform coefficients in [0.5,2]^4, invert, record the spread of (r_uc,r_ct).
PASS reading (edge predictive): B1 moves both ratios by <3% AND B2 puts >=30% of the prior mass within 10% of both observed ratios.
FAIL reading (edge carried by the calibrated coefficients): B1 moves a ratio by >10% per 5% coefficient change AND B2 puts <5% of
prior mass within 10% of both observed ratios. In between: report as wounded.
Consequence if FAIL: the "landing near observation" is a round trip of a fit; the up-ratio pair is not a framework output until the four coefficients are derived.

## Addendum written after Tests A and B were run, BEFORE Tests C/D were run
(Tests A, B are reported as they came out; the prereg above was written first.)

Test C (ray_blind.py): in the reduced projector-ray carrier with a_d=1/sqrt42, phi=-1/42 supplied, drop the observed-ratio residuals and
invert (m_u/m_c, m_c/m_t) from CKM+J alone at a_u = RPSR and at neighbouring a_u.
  Hypothesis H_C: the ratios depend on a_u (elasticity >= 1), i.e. the a_u law is what carries the mass ratios.
  FAIL of H_C: both ratios move by < 5% across a_u in [0.72,0.85] (18% window) -> a_u is not the mass-carrying variable.

Test D (common_scale_carrier.py): the carrier's down ratios (R_SB=0.02239) are on the mixed threshold-local convention (sibling T46: common-scale
m_s/m_b = 0.01887). Feed the CARRIER the common-scale down ratios (m_s/m_b = 0.01887, m_d/m_s unchanged) with the lane's coefficients, invert the up ratios,
compare with common-scale up comparators (m_u/m_c = 1.975e-3, m_c/m_t = 3.71e-3, from T46's own QCD runner, MSbar m_t(m_t)=162.5).
  PASS (landing is convention-robust): both ratios within 10% of the common-scale comparators.
  FAIL (landing is a mixed-convention artifact): either ratio off by >30%.
