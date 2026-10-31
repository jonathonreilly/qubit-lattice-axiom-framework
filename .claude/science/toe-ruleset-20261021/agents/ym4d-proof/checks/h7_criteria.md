# h7 criteria (lane D session 4; written before checks/h7_term_an.py exists)

Pre-registered. The script must implement exactly these tests; any deviation is disclosed in HIST_LOG.md.
Numerics: numpy, double precision, scipy.linalg.expm/logm allowed. Seeds fixed (0..). HS norm |.|, op norm ||.||.

## A. Holomorphic continuation of NA-alg (a) and of phi (Lemma TERM-an of HIST §25)
Setting: N in {2, 3}; m in {3, 6} terms; weights w_j uniform random on the simplex; y in {0.005, 0.02, 0.05}.
Real data: Y_j = y * (random su(N), HS-normalised to 1) * u_j, u_j uniform in [0.2, 1].
Complex data: Y_j = A_j + i B_j with A_j, B_j random su(N), scaled so that |Y_j|_HS <= y (same u_j rule).
Construction: M = sum w_j e^{Y_j}, Mc = sum w_j e^{-Y_j}; fixed-point map
  Phi(X) = Ybar + P0( (K(X) - Kc(X))/2 ),  K(X) = e^{-X}M - 1 - (Ybar - X),  Kc(X) = Mc e^{X} - 1 - (X - Ybar),
  P0(Z) = Z - tr(Z)/N * 1; iterate from X = Ybar to |X_{n+1} - X_n| <= 1e-15 (cap 200 iterations).
20 samples per (N, m, y, real/complex).
- **A1 (real agreement).** On real data: (a) X_0 anti-Hermitian and traceless to <= 1e-13; (b) X_0 equals the fixed
  point of NA-alg's real map Phi_R(X) = Ybar + Pi(K(X)), Pi(Z) = (Z - Z*)/2 - tr((Z - Z*)/2)/N, to <= 1e-13; (c) W_0 = e^{X_0}
  maximises Re tr(W^{-1}M): Re tr(W_0^{-1}M) >= Re tr(W^{-1}M) - 1e-13 for 200 random W = W_0 e^{tZ} (Z random su(N),
  |Z|=1, t in {1e-3, 1e-2, 0.1, 1}) and 200 Haar-random W. PASS iff all hold for all samples.
- **A2 (complex fixed point).** On complex data: (a) the iteration converges (<= 200 steps); (b) holomorphic stationarity
  residual |P0((e^{-X}M - Mc e^{X})/2)| <= 1e-13; (c) |X_0 - Ybar| <= 9.2 y^2 and |X_0| <= 3y. PASS iff all hold.
- **A3 (holomorphy).** For F(Y) := X_0(Y) (complex data, N = 2 and 3, m = 3, y = 0.02) and a random complex direction D
  (|D_j| = 1), h = 1e-6: CR defect  |(F(Y + ihD) - F(Y)) - i(F(Y + hD) - F(Y))| / |F(Y + hD) - F(Y)| <= 1e-3.
  Same test for the scalar phi^C(V) at V = W_0 e^{-rho} (rho random complex traceless, |rho| = 0.02), varying Y.
  Control (must FAIL the same test, else the test is vacuous): the non-holomorphic map Y -> NA-alg's REAL Phi_R fixed point
  applied to complex data (with Pi using *) must give CR defect >= 0.1 on the same samples. PASS iff holomorphic cases
  pass and the control fails.
- **A4 (phi).** phi^C(V; M) := (1/2N)[tr(e^{-X_0}M) + tr(Mc e^{X_0}) - tr(V^{-1}M) - tr(Mc V)].
  (a) Real data, V Haar or near W_0: phi^C equals N^{-1}[Re tr(W_0^{-1}M) - Re tr(V^{-1}M)] to <= 1e-13.
  (b) Complex data, V = W_0^C e^{-rho}, rho complex traceless, |rho| in {1e-3, 1e-2, 0.05}: |phi^C + tr(rho^2)/(2N)| <=
      4.6 y^2 |rho|^2 / N + e^{4y + |rho|} |rho|^3 / (6 sqrt(N)) (the bound stated in TERM-an (iii)).
  (c) Global Haar-shift form: for V' Haar-random in SU(N) (500 per sample), Delta := phi^C(W_0^C V') - s(V'),
      s(V') = 1 - Re tr(V')/N: |Delta| <= theta * s(V'), theta := 18.4 y^2 (2 + 2 c_N), c_N := max(pi^3/24, N / r_N^2),
      r_N := min(1, 4/sqrt(N)). PASS iff (a)-(c) hold for all samples.
- **A5 (Haar shift of the normalisation, Lemma NORM-an).** N = 2, complex data (m = 3, y = 0.02): with kappa*u in
  {20, 80}, Monte-Carlo-free quadrature is not available, so use 2e5 Haar samples (fixed seed) and compare
  I1 := mean over Haar V of exp(-kappa u phi^C(V)) with I2 := mean over Haar V' of exp(-kappa u phi^C(W_0^C V')).
  Informational with a soft criterion: |I1 - I2| / |I2| <= 5 standard errors (estimated from the sample) or <= 0.05,
  whichever is larger. Also report |I2/I0 - 1| with I0 := mean exp(-kappa u s(V')) against the bound C_N theta (report only).

## B. Polar vs chart (Lemma POL)
N in {2, 3}; X, Y random su(N) with ||X||_op <= 1/8, ||Y||_op = t in {1e-4, 1e-3, 1e-2, 0.1, 0.125}; 200 samples each.
Compute the polar decomposition e^{X+iY} = V e^{H} (V unitary, H Hermitian): H = (1/2) logm((e^{X+iY})^* e^{X+iY}).
- **B1.** det V = 1 to 1e-12 and tr H = 0 to 1e-12.
- **B2.** ||H||_op <= 4.19 ||Y||_op and ||V - e^{X}||_op <= 9.2 ||Y||_op (the lemma's constants).
- **B3 (informational).** max ||H - iY||_op / (||X|| ||Y|| + ||Y||^2) (first-order behaviour).
PASS iff B1, B2 hold for all samples.

## C. Constants of HIST §26 (Theorem AE ⇐ MS-Sob)
Compute from the displayed formulas of §26 at (N, L, d, kappa) = (2, 3, 4, 1) and (3, 3, 4, 1), with C_S a free input
(report at C_S in {1, 1e2, 1e4}): C_loc, C'_AE, C_natural, C_e, the closing inequality's left side at the chosen eta_AE,
eta_AE (largest value on a factor-2 grid that satisfies every displayed smallness condition), the induced epsilon-tilde,
and C_cone = max(C'_AE/(2N), 2/eta_AE).
- **C1.** The closing inequality holds at the reported eta_AE, and every listed smallness condition holds.
- **C2.** eta_AE <= eps_M^2 / C'_AE (eps_M = 6.9e-6 from MSG (S3)), consistent with REVIEW_HIST_S3's estimate
  C_cone >= ~1e12.
PASS iff C1 and C2 hold for every reported case.

## Overall
PASS iff A1-A4, B1-B2, C1-C2 all PASS (A5, B3 informational/soft). Runtime < 10 min, peak RSS < 1 GB.
