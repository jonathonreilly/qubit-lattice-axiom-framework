# Criteria for the upper-chain numerical checks (written before running)

None of these is load-bearing for a proof. Each tests a statement or a formula in `parts/upper-chain.md`.

## upper-chain_gaussian.py (Gaussian approximation of Theorem 3 and Remark 3.3)

Model: s_p = (1/8) sum_a (F_p^a)^2 on (Z/T)^4, T even. Cov(s_p,s_q) = (3/(2 beta^2)) P_pq^2, P the projector onto exact two-forms. All values below are in units of 1/beta^2.

- G1. Sum rule: (3/2) sum_{p,q} P_pq^2 / T^4 = 9/2 up to the zero-mode term. Pass: |value - 4.5| < 1e-3 at T >= 16 after accounting for the removed k = 0 mode. Fail otherwise.
- G2. Interface: Cov(W_+,W_-) per plane site, with plane plaquettes at weight 1/2, for the two planes of the torus, is 3/4 per plane. Pass: within 3% at the largest T. Fail otherwise.
- G3. Decay: forward energy correlator on the axis, r(x e_1). Pass: local slope d log r / d log x between x = 4 and x = 8 at T = 32 lies in [-9, -7]. Fail otherwise.
- G4. Chessboard at second order: Var(W_B) <= |B| h'' for dyadic closed blocks, and D_B = |B| h'' - Var(W_B) > 0. Pass: holds at all tested ell. Fail on any violation beyond 1e-9.
- G5. Surface law: D_B/(ell^3) tends to a positive constant as ell grows. Pass: the ratio between ell = 8 and ell = 4 values of D_B/ell^3 lies in [0.7, 1.3] at T = 32. Fail otherwise (and record, as finite-T effects are possible at ell = T/4).

## upper-chain_ie2d.py (exact two-dimensional analogue of the interior estimate)

Model: SU(2) on a disc of n plaquettes, boundary holonomy angle theta, Z_n(theta) = sum_j (2j+1) b_j^n chi_j(theta). osc(n,tau) = max_theta E[s_p|theta] - E[s_p|theta=0], with beta = n/tau.

- I1. Uniform bound: sup over n in {10^2, 10^3, 10^4, 10^5} and tau in {0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5} of n^2 osc is at most 6. Fail if larger.
- I2. Classical limit: for tau = 0.02 and n >= 10^3, n^2 osc is within 5% of pi^2/2 (uniform curvature, angle pi over n plaquettes, s = (pi/n)^2/2). Fail otherwise.
- I3. No growth in n: for each tau, n^2 osc changes by less than 5% from n = 10^4 to n = 10^5. Fail otherwise.

## upper-chain_ie4d.py (Monte Carlo test of the sup form of IE in four dimensions)

Model: SU(2) Wilson, closed cube of half-side r with fixed boundary links, interior updated by checkerboard heat bath. Observable: the average of e_a over the inner cube of half-width max(1, floor(r/3)), a scale-invariant fraction of the cube (changed from the central 2^4 sites after timing runs only, before any production run, to improve signal to noise; no production data were seen). Delta(r) = E[e|rough] - E[e|cold], with rough = Haar random boundary links, frozen, averaged over a few draws.

- M1. Sup form plausible: r^4 |Delta(r)| for r = 3, 4, 6, 8 at beta = 4 does not grow: value at r = 8 at most twice the value at r = 3, allowing for one standard error. Fail if it grows beyond that.
- M2. Compare: r^2 |Delta(r)| must decrease if the decay is faster than r^-2. Record the local exponent; a fitted exponent below 2.5 at the largest r counts as evidence against the (a/D)^4 form.
- This cannot prove the estimate. A failure of M1 would rule the sup form out as an interface at this beta and move the request to finite p.

## Added after the G3 miss (before computing)

- G3b. G3 missed narrowly (slope -9.005 against [-9,-7]) in the window x = 4..8 on T = 32. Lattice corrections are the suspect. The continuum kernel gives the on-axis forward-energy correlator 9/(pi^4 x^8) = 0.0924/x^8 in units of 1/beta^2. Pass: x^8 r(x) within 5% of 0.0924 for x in [16, 32] at T >= 256. Fail otherwise, in which case the r ~ x^-8 reading in Remark 3.3 is wrong for this field.

## upper-chain_gaussian_bump.py (the decisive question at Gaussian level, smooth bump; added before computing)

Gaussian model as above, forward energy field, f_T(x) = phi(x/T) with phi a fixed smooth bump of width 1/8 of the torus, and its copy shifted by 3/8 of the torus along one axis (block-like separation). Units 1/beta^2.

- B1. Contact: V(T) = Var(sum_x f_T(x) e(x)) satisfies V/T^4 -> (9/2) ||phi||_2^2. Pass: within 2% at T = 48. Fail otherwise.
- B2. Gradient term: (V - (9/2) ||phi||^2 T^4)/T^2 tends to a negative constant. Pass: values at T = 32, 48 have the same negative sign and agree within 15%. Fail otherwise.
- B3. Separated: C(T) = Cov(sum f_T e, sum f_T(.-shift) e) is independent of T. Pass: |C(48)/C(32) - 1| < 0.05. Fail otherwise.
- B4. Array defect: X(T) = Var(array)/N - V(T), for the periodic array of the same bump with period T/4, N = 4^4. Images touch at the block faces and the bump vanishes there to all orders. X is the sum of the separated and touching covariances per bump, the second-order content of CT3. Pass: |X(48)/X(32) - 1| < 0.10. Fail otherwise.

## Added after B1, B3, B4 missed at T <= 48 (before computing the following)

Raw results: B1 missed narrowly (2.5% against 2%, at T = 48). B2 passed. B3 failed (C(48)/C(32) - 1 = -11.7%). B4 failed (X(48)/X(32) - 1 = -18%). Suspect: bump half-width T/8 is only 6 lattice units at T = 48, where x^8 r(x) is still 1.47 times its limit at x = 6 (from G3b).

- B3'. Let C_cont(T) use r_cont(x) = 9/(pi^4 |x|^8), with periodic images, in place of r, for the same bumps. Pass if C_cont(T) changes by less than 3% from T = 48 to T = 64, and C(T)/C_cont(T) moves toward 1 from T = 32 to T = 48. Fail otherwise. A fail would mean the separated covariance of bumps is not cutoff-independent at Gaussian level, contradicting the reading of Theorem 4 and Remark 3.3.
- B2'. The limit of (V - 4.5 sum f^2)/T^2 is -(M_2/8) ||grad phi||_2^2, by Taylor expansion of the kernel, with M_2 = sum_x |x|^2 r(x). Pass if the value at T = 48 is within 15% of it. Fail otherwise.
- B4'. X_cont(T), as X but built from the separated part only (r_cont for x outside the bump-to-itself pairs) is not defined cleanly when images touch, so B4 is left as failed at these T. Re-test only if T >= 96 is affordable.

## Zero-momentum dominance in the smallest model (no script)

Question Z1 (is two-block zero-momentum dominance, Cov(y_+, y_-) >= 0, a consequence of RP and the Markov property alone?) was planned as a random search and was settled by hand before running anything: outcome A, by the exact example in `parts/upper-chain.md`, Proposition 14.7.

## upper-chain_dia_exact.py (local diamagnetic inequality, exact small system; written before running)

Statement tested, (DIA-B): for every boundary data xi and plaquette p, E[s_p | xi] >= E[s_p | cold]. Model: two free links in one plaquette q, every other link fixed. Link 1 has five further staples a_(1,i) and link 2 has five further staples a_(2,i), all arbitrary unit quaternions, and q has weight (1/2) Tr(U_1 X U_2^-1 Y). Link 1 is integrated in closed form, link 2 by Gauss quadrature on S^3. Cold means all fixed links are 1.

- D1. For beta in {0.5, 1, 2, 4, 8, 16} and 2000 random boundaries per beta (Haar, and near-cold with angles at most 0.3), compute min over xi and over all 11 plaquettes of E[s_p|xi] - E[s_p|cold]. Violation if the minimum is below -1e-6 at a resolved quadrature (grid doubling changes the value by less than 1e-7). Violation means (DIA-B) is false as an exact statement, at the fine boundary level, and the route must be restated. No violation in this small system is only encouragement.
- D2. Quadrature check: the cold value of the total against a higher grid, and the one-free-link analytic formula when q is removed.

## Result of upper-chain_dia_exact.py, and upper-chain_energy_sign.py (written before running)

D1 result: no violation; min over 2000 boundaries of E[s_p|xi] - E[s_p|cold] is positive at every beta (8.6e-4 at beta = 0.5 down to 8.4e-5 at beta = 16), quadrature stable. Encouragement only: two free links.

A sharper target for a counterexample. In the Gaussian theory Cov(s_p, s_q) = (3/(2 beta^2)) P_pq^2, and P_pq vanishes identically for plaquettes in orthogonal planes, p in (1,2) and q in (3,4). So there the sign of Cov(s_p, s_q) is decided at the next order, and plaquette-level positivity could fail.

- E1. Periodic T = 6, SU(2) heat bath, beta in {2.5, 4, 8}, 20000 sweeps each. Measure C_perp(y) = connected <s_12(x) s_34(x+y)> for y in {0, e1, e3, e1+e3}. Report sign and error. A value below -4 sigma at any beta means pairwise positivity of plaquette energies is false, and plaquette-level (DIA) near cold should be expected to fail, so the route must use the clover field or block sums.
- E2. Same run: connected <e_a(x) e_a(x+y)> for y in {e1, 2 e1, e1+e2}. Expected positive. A value below -4 sigma would count against clover-level (DIA) too.

## Casimir test of Proposition 15.2, upper-chain_vacuum_e.py (written before running)

- C1. m = periodic <inner-cube observable> at beta = 4, T = 12, in the same field e_a. With n(r) from upper-chain_ie4d.py: (DIA-B) predicts n(r) <= m for all r. Fail if n(r) exceeds m by more than 3 sigma at any r, which would refute (DIA-B) at that boundary. r^4 (m - n(r)) for r = 3, 4, 6, 8 is expected bounded; report it. T = 12 finite-size shift of e is about 1.8e-5 by the mode count, to be included in the error.

## upper-chain_response.py: the local response profile in the actual model (written before running)

The hidden variable in Text 14 F4 and Text 15 is whether the local response of the fine energy to a coarse observable has large cancelling parts. Let V^(k) be iterated gauge-covariant blocking by 2 (straight path plus six staples, quaternion mean), G_k(y) the clover energy of V^(k) at coarse site y, e the fine clover field, and R_k(x) = Cov(e(y+x), G_k(y)), averaged over coarse sites and over the hypercubic group fixing y. Then sum_x R_k(x) = -d<G_k>/d beta, a constant-coupling quantity. Run: T = 16, beta = 4, periodic, k = 1, 2.

- A1 (sign). (DIA-V) in its mean form predicts R_k(x) >= 0 at all x. Report the most negative orbit in units of its error. A value below -4.5 sigma (allowing for about 500 orbits) refutes this mean form, and then exact (DIA-V) is false for this blocking.
- A2 (cancellation). rho_k = sum_x |R_k(x)| / |sum_x R_k(x)|, counting only orbits resolved at 3 sigma, and the same with all orbits as an upper estimate biased by noise. rho_k close to 1 means no large cancelling parts, which supports (TR_2) at this level. rho_k >> 1 and growing from k = 1 to 2 would be the total-derivative growth of F4, and would count against the small-negative-part form.
- A3 (sum rule). sum_x R_k(x) measured two ways: the sum of the profile, and the covariance of total W with G_k. Fail if they differ by more than 3 sigma; then the script is wrong.

## upper-chain_strip.py: exact check of the strip bound, Lemma 10.1 (written before running)

Model: 2D Z_2 and U(1)-truncated gauge theories are too coarse for the proof's SU(2) step, so the test is of the algebra only. Exact transfer operator of 2D lattice gauge theory on a spatial circle of n links, gauge group SU(2) truncated by Gauss quadrature on class functions is not used; instead Z_2 on n = 4, 6 spatial links and T = 8, 12 time slices. Random bounded F, G on slabs of thickness 1 and 2, |F|, |G| <= 1. T_1 is built from its kernel, not from its claimed form.

- S1. T_1 is symmetric positive semi-definite: smallest eigenvalue >= -1e-12 times the largest. Fail otherwise: the claimed T_1 = K P has a mistake.
- S2. For integers m in (0, N), the direct torus value of < F tau G > by full enumeration equals Z^-1 Tr(F^ T_1^m G^ T_1^(N-m)) to 1e-10. Fail otherwise: the slab operators or the trace identity are wrong.
- S3. |f(x + i y)| <= ||F||_inf ||G||_inf at 2000 random points of the strip. A single violation above 1e-10 fails the lemma.
- S4. |c(m + s) - c(m)| <= ||F||_inf ||G||_inf log(t / (t - |s|)) for all admissible m, s and 200 random F, G. A single violation above 1e-10 fails the lemma.
- S5. Unequal thickness without padding: compute A_F(x) with h_F != h_G on the same torus and record whether it exceeds ||F||^2. This documents why padding is needed. It is not a pass or fail item.

This is a check of the operator algebra in a small model; it does not test SU(2).

## upper-chain_wit_gauss.py: the witness pair in the Gaussian theory (written before running)

Theorem 10.7 uses P_pq at offset (d, d, 2d, 2d) for parallel (1,2) plaquettes, predicted 0.6/(100 pi^2 d^4) in the continuum, and the Maxwell tensor generally. Level 0 only, Wilson form, computed by FFT on T = 48. This tests the tensor and the sign, not the blocked form.

- W1. For d = 3, 4, 5, 6: P_pq has the predicted sign, and P_pq / prediction is within 25% of 1 at d = 6, and closer to 1 at d = 6 than at d = 3. Fail otherwise: the choice of pair in Theorem 10.7 has to change.
- W2. Parallel (1,2) pair at offset (d,d,d,d): |P_pq| at d = 6 is at most one tenth of the value of the (1,2),(1,3) pair at that offset, which is predicted -1/(2 pi^2 x^4). Fail otherwise: my tensor is wrong.
- W3. Sum rule: sum over q of P_pq^2 = P_pp, up to 1e-6, and P_pp = (1/2)(1 - T^-4)-type within 1e-3. Fail means the script is wrong.
- W4 (added before running the script). Normalization of Theorem 10.7 at level 0, against existing data. In `sign.out` (T = 6, Monte Carlo): beta^2 C_e(e1) = 0.259 at beta = 4, 0.245 at beta = 8; beta^2 C_e(e1+e2) = 0.0662, 0.0610. Prediction: (1/16)(3/2) sum P_pq^2 over the 24 x 24 plaquette pairs, with P on T = 6. Pass if the ratio is within 15% of 1 at beta = 8 and closer to 1 than at beta = 4, for both offsets. Fail means the constant (3/2) P^2 is wrong for this field, or the zero modes on T = 6 matter more than I assume.

## upper-chain_dia_lap.py: exact (DIA-B) at order 1/beta (written before running)

Fact used (derived in Text 15). For a closed cube with boundary data xi and a plaquette q with zero curvature at the minimiser V^*, as beta -> infinity at fixed xi, E[s_q | xi] = (1/beta) (1/2) Tr(Q_q G) + O(beta^-2), with Q_q the Hessian of s_q and G the pseudo-inverse of H = sum_q Q_q at V^*. Laplace on a finite-dimensional integral, so this is rigorous when V^* is the unique minimiser up to gauge. And sum_q Tr(Q_q G) = rank H exactly. So delta_q := (1/2)(Tr(Q_q G)_xi - Tr(Q_q G)_cold) has zero sum over q. If delta_q < 0 at a q with zero curvature, then (DIA-B) is false at that q for all large beta.

Model: 4D cube of half-side r = 2, 432 free links, boundary xi = exp(i eps eta), with eta chosen so that the linear curvature vanishes on the target. Target T1: the plaquette (0; 0, 1) at the centre. Target T2: the 24 plaquettes at the centre site, weights 1/4 (the field e_a). D(eta) := delta / eps^2, a quadratic form in eta as eps -> 0.

- L0 (script sanity). Hessian against finite differences within 1e-5 on a random configuration. Zero sum of delta_q over all q below 1e-8. Rank of H equal to 3 (432 - 81). A failure means the script is wrong; no conclusion is drawn.
- L1. Rayleigh-Ritz of D for T1 on 24 random directions, one colour (abelian background), and 12 directions with all colours. Report lambda_min. If lambda_min < -3 tol, with tol the change of D between eps = 0.03 and eps = 0.015 on the worst direction: plaquette-level (DIA-B) is false at large beta.
- L2. The same for T2. If lambda_min < -3 tol: (DIA-B) for the field e_a is false at large beta.
- L3 (only if L1 or L2 finds a negative direction). Check at finite beta by Monte Carlo, with a separate criterion written then.
- If no negative direction appears, this is evidence only: the search is on random subspaces.

## Added after W1 missed (before computing the following)

Raw results at T = 48: ratio to the prediction 0.963, 0.956, 0.928, 0.886 at d = 3, 4, 5, 6. W1 failed as written: the ratio at d = 6 is within 25% but is farther from 1 than at d = 3. W2, W3 passed. W4 did not run: the job had started before the edit. Suspect for W1: periodic images, since the offset at d = 6 has components 12 of T = 48.

- W1'. T = 64, same offsets. Pass if at d = 4, 5, 6 the ratio is closer to 1 than at T = 48. Fail otherwise: then the deviation is not from images, and the tensor in Theorem 10.7 needs a second look.
- W4 as registered above, run now, at T = 6.

## Extended search, upper-chain_dia_lap.py (before running)

Raw results of L1, L2 on 24 + 12 random directions: all eigenvalues of D positive (T1: lambda_min 2.9e-6, T2: 3.9e-5), tol below 3e-7. So no violation in random subspaces. Random directions may miss a direction concentrated next to the target.

- L1', L2'. Rayleigh-Ritz on a structured basis of 80 directions, one colour: the top right singular vectors, within the null space of the target, of the linear curvature restricted to plaquettes sharing a link with the target. If lambda_min < -3 tol, the corresponding (DIA-B) is false at large beta. Otherwise this remains evidence only.
