# f15 criteria (lane C, session 12; written before any f15 script)

Pre-statement: FLOW.md §94 (W2)-(W6). Jobs < 20 min, < 1 GB; one NUMERIC LOCK acquisition per run; load < 8 and memory
free >= 35% checked inside the lock before starting; nice 10, BLAS threads = 1. Every line below is a PASS/FAIL verdict;
a FAIL is reported as such (no re-thresholding after the run).

## Part A: Lemma CL-V ((W2))

Conventions. S_W = (beta/N) sum_P Re tr(1 - U_P), beta = N; U_b = B_b e^{t X_b}, B_b = exp(a_b H_1); plane wave
a_{x,1} = eps cos(p x_2 + theta), other a = 0. Root alpha = e_i - e_j, E_alpha = e_ij, X_b = phi_b e_ij - conj(phi_b) e_ji.
(W2) (b) quadratic form Q(phi) (normalised by H(1) = d^*d); the exact Hessian is d^2/dt^2 S_W at t = 0, computed by the
product rule on the matrices (no expansion). Prediction: Hess = 2 Q(phi) (= (2 beta/N) Q).

- **A1** Torus (3, 6, 2, 2), eps = 0.7, p = 2 pi/6, theta = 0.3. SU(2): H_1 = i diag(1/2, -1/2) (q = 1, hbar = 0); SU(3):
  H_1 = i diag(0.7, -0.2, -0.5), roots (1,2), (1,3), (2,3) (q = 0.9, 1.2, 0.3; hbar = 0.25, 0.1, -0.35). Four random complex
  root fluctuations per root (fixed seed). PASS if max |Hess - 2Q| / |Hess| <= 1e-11 (one line for SU(2), one for SU(3)).
- **A1x** (SU(3)) cross terms: |Hess(X_a + X_b) - Hess(X_a) - Hess(X_b)| / (|Hess(X_a)| + |Hess(X_b)|) <= 1e-12 for every
  root pair (alpha != +-beta) and for root/Cartan (random traceless anti-hermitian diagonal X).
- **A1c** (control) the (W2) (b) formula with the sin-term dropped must FAIL the A1 comparison: max rel >= 1e-3.
- **A2** (SU(3), each root) (D_U omega)_alpha = e^{-i q a_{x,mu}} omega(x) - omega(x + e_mu) against the derivative at t = 0 of
  X(t) = log(U^{-1} e^{t w(x)} U e^{-t w(x+mu)}) (w = omega e_ij - conj(omega) e_ji; central differences h = 1e-4 and 5e-5,
  Richardson), on every link: max rel <= 1e-8.
- **A3** (continuum limit; Bloch chain: one site in directions 1, 3, 4 with Bloch phases, a periodic chain of N_2 sites in
  direction 2, p = 2 pi/N_2 =: s, theta = 0). O := H + D_U D_U^* from the (W2) formulas. V+^lat[mu, nu] :=
  2 d/d eps <u_mu e^{i(k + p e_2)x}, O v_nu e^{ikx}>/N_2 at eps = 0 (central differences eps = 1e-5); O2^lat :=
  d^2/d eps^2 <v e^{ikx}, O v e^{ikx}>/(2 N_2) (matrix; eps = 1e-3), at k = s khat. Continuum prediction (O^c = -D^2 delta -
  2 i q F, D = d + i q a): Vc(khat) = 2 q khat_1 * 1 - 2 q (E_12 - E_21) (pphat = 1), O2c = (q^2/2) * 1.
  Three fixed directions khat (seeded), two roots: SU(2) (q = 1, hbar = 0) and SU(3) (1,2) (q = 0.9, hbar = 0.25);
  N_2 = 157, 314, 628. E1(s) := ||V+^lat/s - Vc||_F / ||Vc||_F, E2(s) := ||O2^lat - O2c||_F / ||O2c||_F.
  PASS: E1(s at N_2 = 628) <= 0.03 and E1(628) <= 0.7 E1(314), every (khat, root); E2(628) <= 0.03 every (khat, root);
  O0 sanity: <v e^{ikx}, O(eps = 0) v' e^{ikx}>/N_2 = lambda(k) delta (max abs <= 1e-12).
- **A3c** (control) Vc with spin coefficient 1 in place of 2: E1(628) >= 0.2 for every (khat, root).

## Part B: (W4)-(W6) at U = 1 (level units of FLOW §94; L = 3)

Alias sums over m in {0..l-1}^4, k_m = (K + 2 pi m)/l, 1/lambda and 1/lambda^2 by proper time (trapezoid in u = log T,
h_u = 0.3; step control 0.15). K_a = (0.7, 0.4, 0.3, 0.2), K_b = (2.1, -1.3, 0.9, 2.8), K_c = (0.06, 0.04, 0.03, 0.02).

- **B0** (linear algebra) (i) the (W5) (a) one-step closed form M_L(k) against direct contour sums of the S4' contours
  T^sigma_y (all 24 orders, all 81 y, abelian, plane-wave input), 3 random k: max abs <= 1e-12; (ii) the composite closed
  form against the ordered product of one-step symbol matrices, n = 2, 3, 4, 3 random k: max rel <= 1e-11; (iii) covariance
  M^(n)(k) s(k) = Dhat_l(l k), n = 1..4: max abs <= 1e-11.
- **B1** (VC-T0) T_n(K) := P_{T,l} diag(x^blk_{n,mu}(K)) P_{T,l}, n = 1..6; Delta_n := ||T_n - T_{n-1}||_F. PASS if
  Delta_n / Delta_{n-1} in [0.07, 0.16] for n = 5 and 6, at each of K_a, K_b, K_c (6 lines); the C-part: ||s_i||_F/||s_{i-1}||_F
  in [0.07, 0.16] for i = 4, 5 at each K (one line); step control max rel change of x^blk <= 1e-9 (one line).
- **B2** ((W6), ARGUED) L_n(K) := <V, N_n[M] V>, N_n[M] := l^-4 sum_m M P_T M^dag / lambda for the actual composite S4'
  symbol, n = 1..6, K_a and K_b; delta_n := L_n - L_{n-1}. PASS if delta_5 > 0, delta_6 > 0 and |delta_6/delta_5 - 1| <= 0.10
  (one line per K).
- **B3** (control) straight single-path map: T^sp_n := P_{T,l} diag(l^-4 sum_m |S_mu|^2/lambda) P_{T,l}; PASS (= diverges)
  if Delta^sp_n / Delta^sp_{n-1} >= 2 for n = 5, 6 at K_a and K_b (one line per K).
- **B4** ((W4), proven; a check of the proof) c_n(K) := kappa <V, C_n V> = sum_{i<n} L^-4i sum_m |V^dag M^(i)(kappa_m)|^2
  (Pi = 1, composite S4' symbols), n = 1..6, K_a, K_b, K_c: PASS if c_n(K) >= 1 + (n - 1)|Dhat_l(K)|^2/8 - 1e-12 for all n, K
  (one line); report increments.

Failure modes: FLOW §94 S12-F1..F5.
