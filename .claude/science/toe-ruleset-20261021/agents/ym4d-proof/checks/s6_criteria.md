# s6 criteria (lane F, session 6) -- written BEFORE checks/s6_sf.py exists

Pre-registered after SF.md §18 (PRE-STATED session 6, 07:16:13 UTC) and before any session-6 proof. One run under the numeric lock
(`until mkdir .../locks/numeric`; nice 10; BLAS threads 1; python3 without -I; no `timeout`; one rmdir). Budget < 20 min, < 1 GB.
OVERALL PASS iff every item marked PASS/FAIL passes. REPORT items carry no verdict. "Rigorous" below means: exact rational arithmetic
(fractions.Fraction), or floating point with a priori rounding bounds (Higham, gamma_n = n u/(1 - n u), u = 2^-53) and an explicit
upward inflation, or mpmath with >= 50 digits and an explicit upward margin. Any other float number is evidence, not proof.

## A. Every-background tier (Lemmas CD, CHEB, RINV; Proposition GF-A)
- A1 (rigorous, exact): H := the 80x80 integer matrix of the block-internal Neumann Laplacian of {0,1,2}^4 restricted to the
  non-centre sites (Dirichlet at the centre). H - (2663/31250) I is positive definite: all pivots of its exact Fraction LDL^T are > 0.
  PASS iff all > 0.
- A1n (negative control, exact): with c = 853/10000 (above the float lambda_min 0.0852175) the exact LDL^T has a pivot <= 0. PASS iff so.
- A2 (evidence, Lemma CHEB on the real operator): d = 2, L = 3, SU(2) adjoint, torus 6x6 blocks; backgrounds U = 1, two Haar-random,
  one smooth (a Haar gauge times exp of a smooth field of amplitude 0.05). a := the d = 2 Kato block gap (float eigenvalue of the
  8x8 analogue of H) times (1 - 1e-12), b := 4d = 8. Check (A2b) lambda_min(G_res) >= a and lambda_max <= b + 1e-9; (A2) for every
  pair of blocks ||G_res^-1(X,Y)|| a T_D(sigma) <= 1 + 1e-9 (D = block l^inf distance on the torus; T_0 := 1).
  PASS iff both hold for every background.
- A2n (negative control): the same with theta replaced by 10 theta (claimed decay e^{-10 theta D}): PASS iff violated for at least
  one pair in at least one background.
- A3 (evidence, Lemma RINV at d = 2, same backgrounds): ||M_U R_U - 1|| <= 1e-12; | ||R_U(X,X)|| - L^d/sqrt(2d) | <= 1e-12 for every X;
  measured |||P_res D_U^* D_U R_U||| <= c_R(d=2) (1 + 1e-12), c_R(d) := (L^d/(2d))(sqrt(8d^3 + 8d(d-1)) + 2d). PASS iff all hold.
  REPORT the ratio measured / c_R.
- A4 (rigorous arithmetic, mpmath): d = 4, L = 3: sigma, theta, Gamma_1 (sum to D = 20000 plus an explicit tail bound), c_R, G^A.
  PASS iff the tail bound is < 1e-30 of Gamma_1 and G^A < 5.8954e23 (GF-dec (e)'s number). REPORT the improvement factor.

## B. Locally small backgrounds (Lemma KKT; Proposition GF-B, computer-assisted)
- B1 (evidence): the relabelling: for 6 non-representative Z with |Z|_inf <= 5, the torus kernel computed directly agrees with the
  relabelled representative to <= 1e-12 (max entry difference / max entry of K(0)). PASS iff so.
- B2 (rigorous certificate, d = 4, R_t = 5, torus of 11 blocks for K~): compute E(Z) = sum_W K^sc(W) K~(Z+W) - delta_{Z0} 1 for every
  |Z|_inf <= 6 (28561 blocks), with entrywise rounding bounds; certified upper bounds k_0, k_1, k_3, k_4, e_1, e_2 (block op norms
  bounded by min{Frobenius, sqrt(||A^T A||_inf)}, both with rounding margins; final inflation (1 + 1e-9)) for each
  w in {1, 10, 100, 1000}. G^sharp(0) := min over these w of k_0 + k_1 e_2/(1 - e_1).
  PASS iff, at the minimising w, e_1 < 1/2 and G^sharp(0) <= 1000.
- B3 (consistency): the float estimate of the true U = 1 value G_est := sum_{|Z|<=5} (L^d ||K_{lam,eta'}(Z)|| + ||K_{lam,om}(Z) Q||_op)
  (Q an orthonormal basis of the sum-zero vectors, i.e. Lambda_res at U = 1). PASS iff G^sharp(0) >= G_est. REPORT G^sharp(0)/G_est.
- B4 (evidence, end-to-end test of GF-B at d = 2): the same certificate at d = 2 (R_t = 5, torus 11x11 blocks for K~), giving
  k's and e's. Background on a 13x13-block torus (n_T = 2R_t + 3): a Haar-random gauge times exp of iid link fields of amplitude 1e-6.
  eps := max plaquette ||1 - U_p||; delta := (d - 1)(L(R_t + 1) + h) eps. Measured G_meas(U) := max_X sum_Y (L^d ||K_{lam,eta'}(X,Y)|| +
  ||K_{lam,om}(X,Y) Q_Y||_op) from the dense inverse of K_U (bordered form), Q_Y an orthonormal basis of Lambda_res,Y^U.
  PASS iff, for some w in {1, 10, 100, 1000} with e_1 + c_Delta(w) delta k_3 < 1, G_meas(U) <= G^sharp(delta).
- B4b (evidence): |G_meas(U) - G_meas(1)| <= 1e-3 G_meas(1) (gauge covariance + smallness). PASS iff so.
- B4c (control, the gauge step is load-bearing): max entry of |K_U - K_1| in the ORIGINAL (non-axial) gauge >= 0.1, i.e. a perturbation
  argument without Lemma BOXG would fail. PASS iff so.
- B4n (REPORT): G_meas at a Haar-random (rough) background on the same torus, where GF-B's hypothesis fails.

## C. Corollary CHAIN-6 (rigorous arithmetic, mpmath)
- C1: with G := G^sharp(delta) at delta from eps := tau_c/2 (iterated to self-consistency, d = 4, N = 3) re-solve the radius chain
  (I1)-(I4), (S0) (maximise zeta over rho on a grid, bisection in zeta), operate at 0.99 zeta_max; report zeta, s_0, r_*, r_sol, tau_c,
  rho_band, eps_bg^(TH-bg) (a_p entry), the (TH-ch') eps_1 ceiling with C_bg = 1.39e40, the derived-constant table, m_FP^A, FD-1's
  M/L. PASS iff (I1)-(I4), (S0) hold at the operating point and the GF-B hypothesis e_1 + c_Delta delta k_3 < 1 holds at eps = tau_c/2.
- C2: the same with G := G^A. PASS iff (I1)-(I4), (S0) hold at its operating point.
- C3 (REPORT): the DX'-1 ceilings and the DX-rel hole ceiling rescaled to the new tau_c.

## D. Lemma FH (frozen holes), evidence
- D1: d = 2, 6x6 torus, U = 1 and one Haar background, hole = 3 fixed blocks. The compressed G_res^h has spectrum in [a, 8 + 1e-9] and
  ||(G_res^h)^-1(X,Y)|| a T_D(sigma) <= 1 + 1e-9 for all non-hole pairs. PASS iff so.
- D2 (REPORT): measured frozen-hole G_meas^h (U = 1) vs G_meas (no hole), to inform (GF-B^h).

## F. STEP-1 arithmetic
- F1: reproduce the [RSF5-fix] numbers to 3 significant digits: rho_band 2.280e-61, a_sh N' 1.759e-64, R_sh 1.610e12,
  g_DX'^2 C_Omega N'^2 1.49e-237 and 1.58e-309, hole ceiling 1.6e-126 (2 digits), FS-1 g_0^2 1.8e-113 (2 digits), band window 5.1e-67
  (2 digits), a_*^B N_r^2 1.08e-123, C_bg 1.39e40, eps_1 ceiling 1.81e-102, n_* (SU(2)) 2.9e205 (2 digits), final levels 108 (integer
  part 107 or 108). PASS iff all reproduced.

## Expected / failure modes (recorded before the run)
- If B2's e_1 >= 1/2 at R_t = 5, the certificate is reported FAIL; a second run with R_t = 6 would be a separate, labelled run.
- If B4 fails, GF-B's proof or its implementation is wrong and GF-B is not used.
