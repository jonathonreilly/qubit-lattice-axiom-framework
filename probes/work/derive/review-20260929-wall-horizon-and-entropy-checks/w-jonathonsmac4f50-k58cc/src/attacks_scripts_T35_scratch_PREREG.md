# T35 pre-registration (written before tests B, C, D and the pairing check were run)

Only the repo's own m_t compression script (repo_compression_copy.py) had been run
when this file was written. That run gave: scenario B (Ward partner = canonical
g_LM = 1.067) base 168.9 GeV, pole bracket 114.4..196.6; scenario A (Ward
partner = continuum g3(M_Pl) = 0.490) base 105.1 GeV.

Route R1 (cross-field, outside the lane's vocabulary): replace the lattice Ward
boundary + matching Delta_R + Yukawa colour selector kappa_Y + tadpole lift by
Planck-scale Higgs criticality, lambda_MSbar(M_Pl) = 0 AND beta_lambda(M_Pl) = 0
(multiple-point principle: Froggatt & Nielsen, Phys.Lett.B368 (1996) 96,
hep-ph/9511371). lambda(M_Pl)=0 is already the lane's own admitted boundary
(docs/HIGGS_CLASSICALITY_BOUNDARY_OPERATOR_ABSENCE_NO_GO_NOTE_2026-05-10.md); the new
premise is only beta_lambda(M_Pl)=0. Given the gauge couplings this fixes y_t(M_Pl)
with no lattice matching.

TEST A  (validate the runner I use for beta_lambda)
  Run the lane's beta_full (3-loop) from SM boundary values at mu = m_t to M_Pl.
  PASS: y_t(M_Pl) in [0.36, 0.42] and lambda(M_Pl) in [-0.025, +0.005].
  FAIL: outside -> do not trust the runner for B/C; fall back to 1-loop analytic.

TEST B  (does R1 reproduce the Ward-chain y_t(v) without any lattice matching?)
  Inputs = the lane's own: alpha_s(v)=0.1033, g1(v)=0.4644, g2(v)=0.6480 (kappa_EW=0),
  v=246.28. Solve beta_lambda(M_Pl; lambda=0)=0 for y_t(v) at loop order 1, 2, 3.
  PASS (R1 reproduces): 3-loop and 2-loop y_t(v) agree within 1.0%, AND the 3-loop
  value lies within 1.0% of the Ward-chain value 0.9176.
  FAIL: any of these violated.

TEST C  (is R1 more robust than the Ward route to the lane's OTHER open premises?)
  Shared open premises: kappa_EW in {0,1} (g1,g2 divided by sqrt(9/8) at kappa=1),
  alpha_s(v) in {0.0907 (alpha_LM), 0.1033 (CMT), 0.1179 (observed, diagnostic only)}.
  Route-specific open premises: Ward: boundary in {1/sqrt6=0.4082, 0.4358}, kappa_Y in {0,1},
  Delta_R in {-0.5, 0, +0.5}; R1: loop order 2 vs 3, lambda(M_Pl) in {-1e-3, 0, +1e-3}.
  Measure: total spread (max/min - 1) of y_t(v) over each route's own corners
  (shared premises included in both).
  PASS (R1 is the better-controlled route): spread(R1) <= 1/3 of spread(Ward) AND
  spread(R1) <= 10% (i.e. R1 is not itself dominated by the shared premises).
  FAIL: otherwise. If spread(R1) > 10% the reading is "R1 just moves the wall to
  the shared premises (T30/T33)".

TEST D  (information content of the Ward hit; the misframing question)
  Prior: y_t(M_Pl) log-uniform on [0.22, 0.65] (the +-50% Delta_R range around 0.4358).
  Using the 1-loop run of the repo compression script, compute the prior probability
  that m_t(pole-proxy) falls within +-3% of the value produced by y_t(M_Pl)=0.4358.
  Report bits = -log2(p). PASS (hit carries >= 5 bits): bits >= 5. FAIL: bits < 5,
  reading: the m_t agreement is a ~few-bit coincidence test, not a sub-percent
  bullseye, and the wall's cheaper replacement is a +-10% target on y_t(M_Pl).

PAIRING CHECK  (does the June-16 "+1.9% K-series" equal sqrt(8/9) x K-series x running?)
  Compute r_run = y_t(m_t)/y_t(v) with the lane's runner, K = 1.0619 (docs
  YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md:534-540).
  HYPOTHESIS: sqrt(8/9) * K * r_run is within [1.010, 1.030].
  If it is not, the two pairings in L07-W8 stay unreconciled and I say so.

## Addendum (post-hoc, written AFTER tests A-E; exploratory, not pre-registered)
Test F: (i) pole masses of R1 at kappa_EW = 1 and alpha_s(v) alternatives;
(ii) "protected-ratio" reading: Ward applied to the RG-consistent g3^MS(M_Pl) with a
Clebsch C in y = g/C: which C reproduces the top? Label: numerology, look-elsewhere
applies (the June-2026 hostile probe already found 8 of 11 O(1) C values look top-like).
