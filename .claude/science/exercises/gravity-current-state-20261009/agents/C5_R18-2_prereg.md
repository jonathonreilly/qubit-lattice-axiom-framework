# R18-2 pre-run declarations (written 2026-10-13 ~02:00Z, before any stability run)

All numerical inputs below are RECALLED (from memory, not fetched). Nothing downloaded.

Primary inputs (RECALLED):
- M_h = 125.20 +- 0.11 GeV (PDG 2024 average)
- alpha_s(M_Z) = 0.1180 +- 0.0009 (PDG 2024)
- M_W = 80.369 GeV (PDG 2024 average; enters g2, gY only weakly)
- M_t (primary) = 172.57 +- 0.29 GeV (PDG 2024 average of direct measurements)
- pole-mass ambiguity (MC-mass vs pole-mass interpretation), primary +-0.5 GeV (RECALLED range 0.3-1 GeV);
  sensitivity rows at 0, 0.3, 0.5, 1.0 GeV.
- alternatives (sensitivity only): ATLAS+CMS Run-1 combination 172.52 +- 0.33; cross-section pole mass 172.4 +- 0.7.

Matching at mu = M_t: Buttazzo et al. 2013 NNLO fit formulas (RECALLED, labelled), with their quoted th errors.
Running: two-loop SM RGEs for gY,g2,g3,yt,lambda (V = lambda(|H|^2 - v^2/2)^2), my own transcription (RECALLED).
Effective potential: one-loop Landau-gauge lambda_eff(h) at mu = h (top, W, Z; Goldstone/Higgs dropped), times exp(4 Gamma).

Stability criterion: min over h in [1 TeV, M_P] of lambda_eff(h) >= 0, with M_P = 1/a = 1.2209e19 GeV (a = l_P).
(Reduced Planck mass 2.435e18 used as a sensitivity row.)

Tension: n_sigma = (M_t - M_t,crit) / sqrt(s_mt^2 + s_amb^2 + s_th^2 + (dMtc/das s_as)^2 + (dMtc/dMh s_Mh)^2),
s_th = 0.3 GeV for my 2-loop-running + 1-loop-V implementation (declared; RECALLED NNLO th ~0.15 GeV).
Reading rule (TESTS FIXED): n_sigma <= 2 -> SM absolute stability within 2 sigma (SM-STABLE condition);
n_sigma > 2 -> metastability beyond 2 sigma (NEEDS-STABILIZER condition, plus explicit stabilizer).
The PRIMARY row decides; the sensitivity rows are reported and, if they straddle 2 sigma, that is stated.

Tuning criterion for (d): a parameter is "held to better than O(1)" if the stable window, in the natural
variable (log of a mass ratio, or the coupling itself), has relative width < 0.1 of its natural range; dimensionful
scales far below 1/a are assessed separately against the lattice (relevant-operator) counting.
