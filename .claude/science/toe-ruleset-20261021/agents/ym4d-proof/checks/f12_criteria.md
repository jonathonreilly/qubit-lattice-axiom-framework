# f12 criteria (lane C, session 9). Written before any f12 script.

Targets: FLOW.md §64 (S1) Lemma S-2pt (the scalar proxy in two-point form at U = 1), (S2) Proposition S-tel (the
increments phi_k = c^S_{k+1} - c^S_k), (S4) (V-IR-S) with a rate; REVIEW_FLOW_S8 §10 item 1.
Run rules: one NUMERIC LOCK acquisition for the official run, nice 10, all BLAS threads = 1, plain python3 (no -I), no
`timeout`, load < 8, memory free >= 35% at start, job < 20 min, peak RSS < 1 GB. No process left running.

## Model (fixed here)
- The scalar proxy of FLOW §57 (Q4) / §64: L = 3, s = 4, kappa_j = s L^{2j}, n = 1, 2, 3, 4 (l = 3, 9, 27, 81); S4' axial
  averages (24 orders), M = A_0, covariance C_n(U) = sum_{j=1}^n kappa_j^{-1} A_j A_j^dag (diagonal), G_S,n(U) =
  tau log(Delta_U + M^dag C_n^{-1} M) + l^{-4} tau_n log C_n (per fine site).
- Background: plane wave U_{x,1} = exp(i eps cos(p x_2 + theta)), other links 1. h_n(p) := [eps^2] G_S,n.
- Evaluation (FLOW §64 (S1) (b)): h_n(p) = (1/4) avg_K l^{-4} [T_n(K,p) - I_n(K,p)], K in the level Brillouin zone, traces
  over the alias fibre of the extended matrix [[Delta, M^dag], [M, -C_n]] at U = 1 and its first/second-order vertices
  (block-digit form factors in closed form). Fibre sums over the l^4 aliases by a proper-time representation that
  factorises over the four directions (direction 2, which carries the momentum transfer p, in closed form per alias).
- K integral: shifted periodic trapezoid grid N_K per direction (the integrand is periodic and analytic in K); the p = 0
  value of the integrand is subtracted pointwise (it integrates to zero; gauge invariance at constant A_1).
- c^S_n := lim_{p -> 0} h_n(p)/(2 sin^2(p/2)), from l p in a fixed set of small values by a polynomial fit in p^2.
- rho_n := c^S_n - 2 c_g log l, c_g = 1/(96 pi^2); phi_k := c^S_{k+1} - c^S_k (c^S_0 := 0).

## Verdict lines (pre-stated thresholds)
Implementation (must PASS):
- I1 brute-force check: for n = 1 on a small 4D torus with an exactly periodic plane wave, the momentum-space formula for
  h_1(p) (at the torus' discrete K and p) agrees with a direct finite-difference second derivative of the torus G_S
  (eps-derivative by central differences of the exact log det) to <= 1e-7 relative. Torus and p fixed in the script.
- I2 Ward: the momentum-space h_n at p -> 0 extrapolates to 0 (|h_n(p_min)| / (2 sin^2(p_min/2)) is finite and the fitted
  constant term of h_n(p) in a fit with a free constant is <= 1e-3 * |c^S_n| p_min^2 / 2 in magnitude), n = 1, 2.
- I3 convergence: |c^S_n(N_K) - c^S_n(N_K')| <= 1e-9 between the two K grids, and the proper-time quadrature change
  under halving its step is <= 1e-10, for every n reported; else the n is reported as not converged (no verdict).
- I4 p-fit stability: c^S_n from the full p set and from the set without its largest member agree to <= 1e-9.
Predictions:
- **P-a (S9-F1): |c^S_1 - 7.123425e-4| <= 1e-8 and |c^S_2 - 2.885494e-3| <= 1e-8** (f11's recorded values; an
  independent test of the F-id link in the proxy and of f11).
- **P-b (S9-F2): |rho_3 - rho_2| <= 4.9e-5** (REVIEW_FLOW_S8 §10: bounded with an approach at least as fast as l^{-1},
  against a log drift of about 1.46e-4).
- Reported (no verdict): c^S_n, rho_n, phi_k, the increments rho_{n+1} - rho_n and their ratios (S9-F3 reading:
  geometric decrease or not), phi_k - 2 c_g log 3.
- Vector rho^V_n: not attempted in f12 (reported as such).

## Reading rules
- I lines are implementation checks, not evidence for (V-IR-S).
- P-a tests Lemma S-2pt (two-point form at U = 1) against f11's constant-field computation; agreement is evidence for both
  implementations and for the F-id link, not a proof.
- P-b and the increments up to n = 4 can support, not prove, (S4): four levels.
