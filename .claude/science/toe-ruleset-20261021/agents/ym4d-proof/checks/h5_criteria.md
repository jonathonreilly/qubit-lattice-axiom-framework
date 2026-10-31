# h5 criteria (written 2026-10-28, BEFORE the script h5_cone_and_dM.py; HIST.md §13 pre-states h5)

Purpose: (A) the real-space inequalities of the local linear lower bound (HIST §15, Lemma E-loc) and (B) the HIST/FLOW
comparison d(M) of HIST §14.2 (c1). Instances only; the statements are proven in the text.

## A (abelian, linear, real fields; d = 4, L = 3, one colour)
Setting: fine torus side n·T with T = 3 coarse cells per direction; straight average Q_str^{(n)} (block side n, leg n):
(Q A)(X, mu) = n^-4 sum_{y in B(X)} sum_{j<n} A_mu(y + j e_mu). Plaquette d as usual (periodic).
- **A1 (composite identity).** For random A: (i) Q_str^{(3)} applied twice equals Q_str^{(9)} (side 27 torus), max abs
  difference <= 1e-10 * max|A|; (ii) d(Q^{(n)}A)(P) = n^-4 sum_{y in B(X)} Phi(sq_y) (flux of dA through the n x n square
  at y in P's plane) for n = 3 and n = 9, max abs difference <= 1e-10 * max|dA|. PASS if both hold.
- **A2 (counting).** By enumeration, for n = 3 and 9: max over fine plaquettes p of #{y in B(X): p in sq_y} equals n^2
  (bound n^2), and max over fine links l of #{y in B(X): l in boundary(sq_y)} is <= 2n. PASS if both bounds hold.
- **A3 (cone inequality).** Depth k = 1 (n = 3, fine side 9) and k = 2 (levels 0, 1, 2; fine side 27). Chains
  B_{i+1} := Q_str^{(3)}B_i - r_i (r_i arbitrary level-(i+1) link fields; the root-map version differs by gradients and
  has the same curvatures). Cone energy E_C(P) := (1/2) sum_{p in R_0(P)} |dB_0(p)|^2 + sum_i (kappa/2) sum_{l in R'_i(P)}
  |r_i(l)|^2, with R_0(P) := the fine plaquettes of P's plane lying in some sq_y (y in B(X), side L^k), and R'_i(P) := the
  level-(i+1) links lying on the boundary of some square sq_y of side L^{k-1-i} (y in the level-(i+1) block of X). kappa = 1.
  Ratio Rho(P) := |dB_k(P)|^2 / E_C(P). Instances: 5 random chains per depth (Gaussian B_0, residual scales 0, 0.3, 1, 3,
  10 relative to B_0), plus adversarial: (a) constant flux in plane 12, r = 0 (predicted ratio 2n^2/(2n-1)^2 = 0.72 at
  n = 3); (b) a residual supported on one coarse line pattern (r = +c on mu-links in the lower half of each block in the
  nu direction, -c in the upper half); (c) 200 steps of random-search ascent of the max ratio from random starts at k = 1.
  **PASS if max Rho(P) <= C_loc = ((2L-1)/(L-1)) * max{2, 16/kappa} = 40 in every instance.** Report the max ratio.
- **A4 (informational).** sum_P |dB_k(P)|^2 / E(chain) against 12 * C_loc = 480 (global form).

## B (non-abelian algebra; SU(2), SU(3))
M := (1/J) sum_j exp(Y_j), J = 8, Y_j in su(N) random with |Y_j|_HS = y * u_j, u_j uniform in [0.2, 1].
W, P the polar decomposition (W in U(N)); W_0 the SU(N) maximiser of Re tr(W^-1 M) (fixed-point iteration of NA-alg (a)
followed by Newton/BFGS polishing; maximiser verified by 200 random SU(N) competitors near and far);
d(M) := N^-1 (tr P - Re tr(W_0^-1 M)).
- **B1.** SU(2): max d(M) <= 1e-13 over 200 samples at each y in {0.02, 0.04, 0.08, 0.16}.
- **B2.** d(M) >= -1e-13 for all samples (both groups).
- **B3.** SU(3): the median over 50 samples of the log-log slope of d(M) against y (sample-wise, the same Y-directions
  rescaled, y in {0.02, 0.04, 0.08, 0.16}) lies in [5.5, 6.5] (prediction: d = O(y^6), from arg det M = O(y^3)).
- **B4.** For 50 random V in SU(N) per sample (20 samples), |[N^-1 Re tr((1 - V^-1 W)P)] - phi_M(V) - d(M)| <= 1e-12
  (k-tilde = phi + d, V-independent shift).
- **B5 (informational).** ratio d(M) / [(tr P / N) * alpha^2 / (2 N^2)], alpha := arg det M.

Resources: numeric lock, nice 10, OPENBLAS/OMP/MKL/VECLIB threads 1, load < 8, >= 25% free memory, peak < 1 GB. No
criterion edited after the script is written; deviations are disclosed in HIST_LOG.md.
