# Kill tests for `library/witness-by-hand.md`: criteria written before the first run

Written 2026-11-01 at commit f3aa2a8c5, before any script in this folder ran. These runs can refute a formula of the written proofs or guide a guess. They discharge nothing, and no step of the note rests on them.

A FAIL below means the written step has an error and must be fixed or withdrawn, not that the tolerance should move.

## W1. Lemma 3.6 and the steps of its hand proof

Random real k^1, k^2 in [-pi, pi]^4, k^3 = -k^1 - k^2, random complex polarisations, 200 samples, d = 4.

- W1a. V_p of Text 2.1 equals the triple sum of determinants of the four increment columns, each plane, relative 1e-11.
- W1b. V_p is unchanged by a cyclic shift of the four links and by reversing the path, relative 1e-11.
- W1c. Plane formula with the two monomial families and the coefficient claimed in the proof, relative 1e-11.
- W1d. Sum over mu < nu equals -2i times the closed form of Lemma 3.6, relative 1e-11.
- W1e. Negative control: with k^3 shifted by 2 pi in one component (sum not exactly zero), W1d must FAIL, because the half-angle form needs the exact sum. If it passes, the remark on representatives is wrong.

## W2. The form: Ward identity and (3.4)

Same sampling.

- W2a. The trigonometric lines: Y_12 = D_2 khat_1 - D_1 khat_2, khat_3 = -(D_2 khat_1 + D_1 khat_2), Y_12 . khat_3 = khat_2^2 - khat_1^2, sum over cyclic orders of cos(k^l_mu / 2) sin((k^i_mu - k^j_mu) / 2) = 0.
- W2b. form(a^1, a^2, khat_3) = (j_2, D_3 a^1) - (j_1, D_3 a^2), j = khat^2 a - khat (khat, a), and form(khat_1, khat_2, khat_3) = 0, relative 1e-10.
- W2c. Brute contraction of the colour indices against the right side of (3.4), with random complex h_i, v_i in khat_i^perp, relative 1e-9.

## W3. Fixed-momentum representation (Theorem S of the note)

D(k) = c_0 + sum_i c_i 2 w_i / (w_i^2 + k^2), several w_i, c_i > 0.

- W3a. Quadrature of formula (4) of the note at random complex zeta, zeta', Re > 0, against the sum over the atoms, relative 1e-7.
- W3b. Formula (6): E(zeta) = c_0 / 2 + sum_i c_i / (zeta + w_i), relative 1e-7.
- W3c. Formula (7): Poisson integral of D at height v and point x against the closed form, relative 1e-6.
- W3d. Shift form: B(S_a psi, psi) at psi = exp(-t), a = 0.5, against the integral over mu, relative 1e-5.
- W3e. Sign of the longitudinal test: for a single atom w_0, the reflected form computed in the time domain equals the Fourier form -|p|^2 int (k^2 + |p|^2) D phi-hat^2, relative 1e-6, with phi a narrow bump at t = 3. This is the one sign the whole argument turns on.
- W3f. Negative control: the discretised Hankel form of the bounded even D = exp(-k^2), not of the form of Theorem S, must have a negative eigenvalue below -1e-6 of its largest.

## W4. Clip and the free bound

- W4a. Moments: E (chi^2_3)^4 = 945 by sampling to 2 percent, and the clip inequality Delta <= 2 m_(2 + r) b^(-r), for r = 1, 2, at b in {2, 5, 10, 20}, on correlated scaled chi-squares, within two standard errors of the sampled left side.
- W4b. Blocked weights of (B-1): w_p <= n^-2 and sum_p w_p = n^2 exactly, n = 1, 3, 5, 7.
- W4c. P_(n,S)(x, x) from (B-3) is at most 1, n in {1, 3, 5}, S in {6, 8}, and near 1/2 at n = 1.

## W5. The order of choice

Sample constants A, alpha, r, a_0, A', alpha', C_s, kappa, M_*. Evaluate 2 tau_b at b = b(L) and the smoothing error at L >= L_1 on a grid of log L up to 1e4 times log L_1. Every value must meet its bound a_0 / 4.

## Report

Each check prints PASS or FAIL. A search or a sample that finds nothing proves no bound. Limits: the script stops itself above 2 GB RSS, single thread, one job under the numeric lock.
