# Check x2: criteria (written 2026-10-27, session 2, before checks/x2_lap_gauss.py exists)

Purpose: (A) exact instance of the one-link anti-concentration lemma LAP-1 (EXISTENCE.md §9, X-NTAF lower bound) in a
model where its hypothesis H-Bal-3L holds exactly; (B) exact instance of the Gaussian two-grid lemma X-CONT-G and of the
"no single-step smallness" finding (X-2GRID remark). Float64, numpy, one process, nice 10, BLAS/OMP threads = 1.

## A. 2D open-boundary SU(2) Wilson model (plaquette variables i.i.d., density ∝ exp(-(1/g²)|U - 1|²) w.r.t. Haar)
Lemma constants for this model: n_p = 2 plaquettes per link, alpha = 1, A_1 = n_p · 2√N · (e^alpha - 1), E_1 = 0,
eta_L = 0, C_* = (4/3)(A_1 + gamma² E_1)/alpha², delta_* = e^{-2 C_*}/(288 π² N), N = 2.
g in {0.05, 0.1, 0.2, 0.3, 0.5} (all ≤ alpha/2).
- A1: E[1 - P] ≥ delta_* g²/2 for every g.
- A2: P(1 - P < delta_* g²) ≤ 1/4 for every g.
- A3 (pre-registered expectation, sharpness only): at g = 0.05, |E[1 - P]/g² - 3/8| < 0.05 (Gaussian limit
  (N²-1)/(4N) for this 2D model).
- A4: the core pair inequality of the proof, nu(T_u S) + nu(T_{u^{-1}} S) ≥ 2 c_s nu(S), with S = {|V_p - 1| < rho},
  rho = r g, u = exp(sX), |X|_HS = 1, and c_s = exp(-(4/3)(A_1/g²) s²/alpha²) (q ≡ 1 in this model, so the factor 1/3
  of the general lemma is not needed), for g in {0.1, 0.3}, r in {0.05, 0.15}, s in {g/4, g/2, g}.
  nu(T_u S) = P(|V_p - u| < rho) is computed by 2D quadrature on S³ (angle from 1, angle to the axis of u); relative
  quadrature error is estimated by halving the grid and must be < 1e-3 for the test to count.
Pass A = A1, A2, A4 all hold (A3 reported separately as an expectation).

## B. Free abelian 4D Gaussian model, linearised S4' block curvature, exact variance by Fourier symbol
Law of F = dA: N(0, beta^{-1} Pi_ex) on exact 2-forms; Var <psi, F> = beta^{-1} ||Pi_ex psi||², with
||Pi_ex psi||² = n^{-4} Σ_{k≠0} (λ_mu + λ_nu)/λ · |psi_hat(k)|² for a single-component (mu nu) test form
(λ_a = 4 sin²(k_a/2), λ = Σ_a λ_a). Block test form psi_0 = average over y in the level-r block (side l = 3^r) of the
indicator of the straight l × l square at y (separable: tent in the two plane directions, indicator in the other two).
Torus side n = 2l, L = 3, r in {1, 2, 3}; shift s = j e_0, j = 1..l-1, w := j/l.
Two orientations: (mu nu) = (1,2) (shift perpendicular to the square) and (0,1) (shift in the plane).
- B1: V(j) := ||Pi_ex(psi_s - psi_0)||² ≤ 4w for every r, orientation, j (absolute tolerance 1e-12).
- B2: ||Pi_ex psi_0||² ≤ 1 for every r and orientation (printed: scale invariance of the block-plaquette variance).
- B3 (pre-registered expectations; informational):
  (a) one step (r = 1), j = 1: V(1)/||Pi_ex psi_0||² ≥ 0.1 (the single-step two-grid discrepancy is O(1));
  (b) fixed j = 1: V decreases strictly from r = 1 to r = 2 to r = 3;
  (c) fixed w = 1/3 (j = 3^{r-1}): V at r = 3 is within a factor 1.5 of V at r = 2.
Pass B = B1 and B2 hold. B3 items are reported individually.

Overall PASS = Pass A and Pass B. Any failure is recorded as a failure; criteria are not changed after running.
Resource limits: peak memory < 1 GB (B loops over k_0 slices), load < 8 at start, memory free ≥ 25%.
