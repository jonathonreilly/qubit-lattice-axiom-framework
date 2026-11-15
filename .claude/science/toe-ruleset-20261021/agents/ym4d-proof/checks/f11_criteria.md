# f11 criteria (lane C, session 8). Written before any f11 script.

Targets: FLOW.md §57 (Q3) (Theorem G-mag (vi), c'_0) and (Q4) (scalar proxy, Lemma S-red, statement (V-IR-S)).
Run rules: one NUMERIC LOCK acquisition for the official run, nice 10, all BLAS threads = 1, plain python3 (no -I), no
`timeout`, load < 8, memory free >= 35% at start, job < 20 min, peak RSS < 1 GB. No process left running.

## Model (fixed here)
- Complex unit-charge scalar on Z^4; constant field of flux f per plaquette in the plane 12, Landau gauge U_{x,2} = e^{i f x_1}
  (other links 1; on a torus or Bloch cell the x_1-wrap link carries e^{-i f a x_2}); covariant Laplacian
  (Delta psi)(x) = sum_mu [2 psi(x) - U_{x,mu} psi(x+mu) - conj(U_{x-mu,mu}) psi(x-mu)].
- Chain of FLOW Proposition COV-sc with L = 3, s = 4 (kappa_j = s L^{2j}), n = 1 (l = 3) and n = 2 (l = 9):
  (Q_k phi)(y') = L^{-4} sum_{y in B_{k+1}(y')} (1/24) sum_sigma P^sigma(y' <- y) phi(y), P^sigma the product of fine link variables
  along the axial path from the centre y' to y in coordinate order sigma (the S4' axial transporters). M := Q_{n-1}...Q_0,
  C_n := sum_j kappa_j^{-1} (A_j A_j^dag)(c, c), A_j := Q_{n-1}...Q_j.
- G_S,n(f) := [log det(Delta_f + C_n^{-1} M^dag M) + N_c log C_n] / V (per fine site); c^S_n := its f^2 coefficient.
- Production evaluation: exact reduction to the plane 12 (two orders, weight 1/2 each) times a plain block average in 34;
  34 by Bloch over l Z^2 with aliases m in (Z/l)^2 (lambda_m, w_m = |D_l|^2), determinant lemma
  log det K(theta) + N_c log C = sum_m sum_j log(e_j + lambda_m) + log det(C + l^{-2} M R M^dag), R = sum_m w_m (H12 + lambda_m)^{-1};
  12 by magnetic Bloch on the cell (l Q') x l at level flux Phi = l^2 f = 2 pi/Q'; shifted Bloch grids (j + 1/2)/K.
  Grids: effective torus >= 60 fine sites (n = 1), >= 144 (n = 2) in each of the four directions.
- Fluxes: Q' in {8, 12, 16, 24, 32} (p = 1), plus f = 0. Fit D(Phi) - D(0) = a1 f^2 + a2 f^4 + a3 f^6 (all five), c^S_n := a1.

## Verdict lines (pre-stated thresholds)
R (implementation, identities; must PASS):
- R1 reduction: n = 1, direct 4D torus (6, 6, 3, 3), one flux quantum on the 6 x 6 plane (f = 2 pi/36), 24 orders built in 4D,
  against the 2D-reduced formula on the same torus: |difference of G_S| <= 1e-12. Also C_1 (4D) vs COV-sc closed form <= 1e-13.
- R2 gauge covariance: same torus, random U(1) gauge transformation of all links (M rebuilt from the transformed links):
  |Delta G_S| <= 1e-12.
- R3 Bloch implementation: cell (12, 3) at f = 2 pi/36 with K = (2, 2) unshifted grid against the direct 2D torus (24, 6):
  sorted spectra and the reduced G_S functional agree to <= 1e-11.
- R4 composite covariance: n = 1, 2 in 2D: A_j A_j^dag diagonal (off-diagonal <= 1e-14) and constant, and C_n against
  the COV-sc closed form sum_j kappa_j^{-1} L^{-4(n-j)} prod_{k=j}^{n-1} N_k(F) with N_k(F) = L^{-4} sum_m cos^2(F L^{2k} m_1 m_2 / 2)
  (F the fine flux): <= 1e-13 relative.
Controls (must FAIL their test):
- R1-ctl: one order only (1 before 2) in the 2D reduction against the 24-order 4D direct value: must differ by >= 1e-6.
- R2-ctl: M without transport phases (plain block average) under the random gauge transformation: |Delta G_S| >= 1e-3.
S (scalar proxy):
- S-grid: |D(grid) - D(1.5 x grid)| <= 1e-10 at f = 0 and at Q' = 8, both n (else the S lines are reported as not
  converged).
- S-IR (IR safety, failure mode S8-F3): the fit D - D(0) = c f^2 + b f^2 log(1/f) + d f^4 on the five fluxes gives
  |b| <= 0.1 c_g for the total, both n (c_g = 1/(96 pi^2)).
- S-stab: a1 from the 3-term fit on the four largest fluxes and on the four smallest agree to <= 1% (both n).
- **S-VIR (prediction, failure mode S8-F2): |(c^S_2 - c^S_1)/(2 c_g log 3) - 1| <= 0.25.**
- Reported (no verdict): c^S_n, rho_n = c^S_n - 2 c_g log l, c^S_n - c_frak^S(l^2) with c_frak^S(T) = (1/2) int_0^T m dt/t,
  and the pieces' f^2 log(1/f) coefficients b_g, b_E (expected near +c_g, -c_g; their grid accuracy is lower, the pieces
  being gapless or nearly so, so no verdict).
G (Theorem G-mag (vi)):
- **G-c0 (prediction, failure mode S8-F1): c'_0 by quadrature of the §57 (Q3)(c) formula against f9's sequence
  (checks/f9_out.txt G2: c'(Q = 512) = 1.387447087e-3, last increment -1.556e-6, ratio 0.509; geometric extrapolation
  1.387447087e-3 - 1.556e-6 * 0.509/0.491 = 1.38583e-3): |c'_0 - 1.38583e-3| <= 5e-6.**
- G-acc: the quadrature changes by <= 1e-9 under halving the tolerances / doubling the upper limit.
- Reported: c'(phi) - c'_0 for the six f9 values (expected O(phi), same sign).

## Reading rules
- R lines and controls are implementation checks, not evidence for (V-IR).
- S-VIR at n <= 2 can support, not prove, the n-uniformity of (V-IR-S): two levels only.
- G-c0 tests the limit formula of Theorem G-mag (vi) against an independent rational-flux computation (f9); it is
  evidence for the formula, not a substitute for the proof.
