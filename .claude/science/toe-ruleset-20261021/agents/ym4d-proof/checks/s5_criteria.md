# s5 criteria (lane F, session 5). Written BEFORE any s5 script exists. Criteria are not edited after the script exists.

Script: checks/s5_sf.py (python3, numpy/scipy; nice 10; BLAS threads 1; under the numeric lock). Seed fixed (20261028).
Gauge group SU(2) (and SU(3) where stated). Lattices: periodic d = 2 (and d = 3 where stated), block side L = 3.
Each criterion is PASS/FAIL unless marked REPORT (printed, no verdict). OVERALL PASS iff every PASS/FAIL criterion passes.

## A. Lemma MSG_0 (block-local axial-type gauge g_ax(x) = hol_U(γ_x)^{-1} hol_{U_0}(γ_x))
Model: background U = a random gauge transform of exp(small random) (plaquettes small), U_0 = random gauge (in G_V, g(c_X) = 1)
applied to exp(small noise)U; amplitudes spanning 1e-3..2e-2 (op norm per link).
- A1 (evidential): for every intra-block link b: ||(g_ax U_0)_b - U_b|| <= 2 A_d tau_p, where tau_p := max over the plaquettes of the
  block of max(||1 - U_0,p||, ||1 - U_p||). d = 2 and d = 3. 0 violations required.
- A2 (evidential; the ladder geometry of MSG step (4)): for every inter-block link b = (x, y), x in B(X), y in B(Y), with π := γ_x b γ_y^{-1}
  and S_c the straight centre segment: ||hol_W(π) - hol_W(S_c)|| <= A_d tau_p(W) for W = U_0 and W = U, tau_p(W) the max plaquette
  defect of W over B(X) ∪ B(Y). 0 violations.
- A3 (evidential; identity): for every inter-block link, ||(g_ax U_0)_b - U_b|| = ||hol_{U_0}(π) - hol_U(π)|| to <= 1e-12.
- A4 (exact locality): re-drawing U_0 on links outside B(X) ∪ B(Y) leaves (g_ax U_0)_b unchanged (<= 1e-12), 20 trials.
- A5 (exact orbit invariance): replacing U_0 by g'U_0 (g' random in G_V, O(1) size) leaves A^0 unchanged (<= 1e-10).
- A6 (non-vacuity): the maximal ratio in A1 and in A2 is >= 0.05 (the bounds are not vacuous by orders of magnitude).
- A7 (negative control, REPORT + FAIL-if-absent): with a root NOT at c_X (root at a block corner, g(c_X) != 1), A5's invariance fails
  (max change >= 1e-3). Required: failure observed.

## B. Lemma GF-dec (d = 2, SU(2) adjoint, torus of 5 x 5 blocks, L = 3; also 4 x 4 blocks)
Backgrounds: (i) U = 1; (ii) U = random Haar on every link (NOT small); (iii) U = smooth small-curvature.
- B1 (evidential): lambda_min(D_U^T D_U restricted to Lambda) >= c_D = 1/(d h L^d) (= 1/18) for all three backgrounds.
- B2: ||D_U||^2 <= 4d.
- B3 (evidential): for every block, sigma_min(M_U restricted to Lambda_X) >= L^{-d}.
- B4 (evidential): for every pair of blocks, ||G_res^{-1}(X,Y)||_op <= q^{|X-Y|_inf}/c_D (q = (4d - c_D)/(4d + c_D)).
- B5 (identity): the formula (chi Gamma)^{-1}(eta, omega) = M^+ eta + G_res^{-1}(omega - P D^T D M^+ eta) solves chi Gamma lambda = (eta, omega)
  to relative residual <= 1e-9, 5 random right-hand sides per background.
- B6 (REPORT): the measured decay rate of max ||G_res^{-1}(X,Y)|| in |X-Y| against m_FP; the measured block row sum against the bound G_inf.

## C. Lemma BCH-L
- C1 (evidential): for random anti-Hermitian triples P, P' in su(2) and su(3) with l1 op-size <= r, r in {1e-3, 1e-2, 0.1, 0.3}:
  ||g(P) - g(P')|| <= c_g r |P - P'|_l1 (c_g = G(0.6)/0.09). 0 violations in >= 2000 pairs.
- C2 (non-vacuity, REPORT): max ratio ||g(P) - g(P')|| / (r |P - P'|_l1) (expected O(1), well below c_g).

## D. Proposition FP-uniq (numerical Newton on the d = 2, SU(2), 4 x 4-block torus; background (iii))
- D1 (evidential): for axial representatives |A^0|_inf = s_0 in {1e-3, 1e-2} and omega with ||omega||_Binf <= s_0, Newton from lambda = 0
  converges (residual <= 1e-11) and the solution obeys ||lambda_*||_Binf <= 2 G_meas (X_inf s_0 + ||omega||) with G_meas := the measured
  block row sum of (chi Gamma)^{-1}. 
- D2 (evidential; uniqueness): Newton from 10 random starts with ||lambda||_Binf <= 5 ||lambda_*||_Binf (all inside a small ball) converges
  to the same zero (max difference <= 1e-9).
- D3 (control, FAIL-if-absent): from random starts of O(1) size (||lambda||_inf ~ 1), at least one Newton run converges to a zero
  different from lambda_* (difference >= 1e-2) with a representative of size >= 0.1: Gribov copies exist outside the ball, so the
  localisation in FP-sh is load-bearing. If no run converges, D3 is reported as INCONCLUSIVE and counts as FAIL.

## E. Lemma KF (SU(2) and SU(3))
M = S avg_j e^{Y_j} (S Haar, 4 terms, |Y_j| <= y, y in {1e-3, 1e-2, 1/20}); V Haar and V near W_0(M) (||V - W_0|| in [1e-4, 1]).
W_0 computed by the fixed-point iteration X <- X + Pi(e^{-X} M') on M' = S^{-1}M (stationarity residual <= 1e-13).
- E1 (evidential): phi(V; M) >= ||V - W_0||^2/(4N) - 1354.3 y^4. 0 violations in >= 4000 samples.
- E2 (evidential): phi(V; M) <= ||V - W_0||. 0 violations.
- E3 (REPORT): violations of the uncorrected bound phi >= ||V - W_0||^2/(4N) (whether the y^4 term is ever used).

## F. Arithmetic (non-evidential; ARITHMETIC labels)
- F1: d = 4, L = 3, N = 3: A_d, C_0, c_D, q, m_FP, S_4(q), the G_inf bound, X_inf, c_g, C_W, n_R, n_1 printed.
- F2: the radius chain: zeta := the largest value for which (I1)-(I4) hold with s_0 = zeta/X_inf, r = the smallest admissible radius
  (as a multiple of G_inf zeta); then tau_c = s_0/(sqrt(N) C_0), r_sol, rho_band (without the rho_*, a_theta entries, which are symbolic).
  PASS iff (I1)-(I4) and (S0) hold at the printed values (consistency of the chain).
- F3: kappa_0 + 3 kappa~_0 + 5 = 807.46 (kappa_0 = 151.315, kappa~_0 = 217.0472); RSF4-fix item.
