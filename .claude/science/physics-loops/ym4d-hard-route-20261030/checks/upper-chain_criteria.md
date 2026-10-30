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
