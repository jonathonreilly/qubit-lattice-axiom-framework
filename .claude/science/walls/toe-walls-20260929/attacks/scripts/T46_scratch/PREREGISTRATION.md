# T46 pre-registration (written before any script was run)

Wall: L09-W5. Down-quark bridge |V_cb| = (m_s/m_b)^(5/6) (unit prefactor) and the
choice of energy scale for the masses. Claude Sonnet 5.5, same family as supervisor.

Facts I will NOT test (taken from the lane): R_pred = (alpha_s(v)/sqrt6)^(6/5) = 0.0223897,
V_cb,atlas = 0.0421736. The lane's claim: +0.20% against m_s(2 GeV)/m_b(m_b) = 93.4/4180,
+14 to +15% against the common-scale ratio m_s(m_b)/m_b(m_b).

Inputs (recalled from PDG-style sources, same central values the repo uses; NOT fetched
online in this session): m_s(2 GeV, nf=4 above 2 GeV) = 93.4 +- 0.8 MeV; m_b(m_b) =
4.180 +0.030/-0.020 GeV (symmetrised 0.025); m_c(m_c) = 1.27 +- 0.02; alpha_s(M_Z) =
0.1180 +- 0.0009. V_cb comparator range 0.0391 (exclusive) to 0.0422 (inclusive).
The atlas number 0.0421736 is used as "theory V_cb".

## Test P1 -- RG-covariant QCD surface (script t46_p1_rgi_discriminator.py)
Question: does 5/6 survive when both masses are taken at the SAME scale?
Build: 4-loop MS-bar alpha_s and mass running, nf thresholds at m_c, m_b, m_t.
Check A: R(mu) = m_s(mu)/m_b(mu) is mu-independent over mu in [m_b, 1 TeV] to better than 0.5%
  (this is the statement that the "scale choice" is not physical inside QCD).
Check B: Delta = R_pred / R_common - 1, Monte Carlo sigma from input errors.
PASS for the bridge as stated: |Delta| < 3 sigma. FAIL: Delta > 3 sigma at every common mu.
Reading of FAIL: the lane's +0.20% is a cross-scale coincidence and the scale wall is a
convention artefact, not a law to derive.
Check C (look-elsewhere): for the nine group exponents used by the July discriminator PLUS a
  wider natural set (all p = a/b, b <= 9 in [0.5,1.7]) count how many hit the threshold-local
  comparator within 0.2% and within the RG-covariant 1-sigma window; compute the chance rate.
  Reading: if chance hit rate over (surfaces x candidates) exceeds 5%, the +0.2% carries no evidence.
Check D (prefactor): c = V_cb / R^(5/6) on the common surface. The 5/6 claim carries the
  hidden premise c = 1. Report c and c's distance from 1 in sigma.

## Test P2 -- does a framework-named UV scale rescue the exponent? (t46_p2_sm_rge.py)
The bridge is called a lattice (g=1) statement, and the axioms' only scale is a^-1 = M_Pl
(scale_reference_primitive). QCD running is flavour-blind, but the top Yukawa is not: it
changes m_s/m_b and V_cb above m_t. Question: is there a natural scale mu_F where
p(mu) := ln V_cb(mu) / ln[(m_s/m_b)(mu)] equals 5/6?
Build: full 3-generation one-loop SM Yukawa RGE with one-loop gauge running (plus a
2-loop gauge variant for sensitivity), start at mu = m_t with QCD-run masses and PDG-like CKM.
Sensitivity: y_t(m_t) +- 0.01, alpha_s +- 0.001, 1-loop vs 2-loop gauge.
PASS (a scale rule exists in the framework's vocabulary): |p(mu_F) - 5/6| < 0.010 for
  mu_F = v (246 GeV) or mu_F = M_Pl (1.22e19 GeV), computed from data-evolved V_cb and R.
FAIL: neither. Then report mu*, the scale at which p = 5/6, and whether mu* is a named scale.
If mu* is unnamed the "scale rule" is one fitted number (PRICED), not a derivation.
Assumption flagged in advance: SM desert up to M_Pl (a hidden premise; no new physics).

## Decision rule for the report
- If P1 FAILS and P2 FAILS: outcome MISFRAMED (scale wall dissolves into a convention
  artefact; the exponent wall is unsupported at RG-covariant precision).
- If P1 FAILS and P2 PASSES: outcome PRICED at "SM desert to M_Pl + bridge stated at a^-1",
  not PASSED, because the exponent derivation (alignment law) is still open.
- If P1 PASSES: outcome STANDS.
