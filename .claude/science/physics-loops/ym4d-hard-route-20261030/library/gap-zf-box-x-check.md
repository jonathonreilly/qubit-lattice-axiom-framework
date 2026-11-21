lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T15:51Z

# gap-zf-box-x-check: line-by-line check of `library/gap-zf-box-x.md` (FINISH row 685, checks row 677)

Provenance: Claude Opus 5.5, effort high, one session on the Mac mini, at commit 53b90e6c9 (the file under check is at that commit unchanged from 4402ff7ee as far as this run can see). Not an audit. A different model from the author (Claude Fable 5.2 medium), but the same vendor: this is a second reader, not an independent derivation except where a step below is re-derived by a different route (marked).

Duplicate check: `gap-zf-box-x-check` appears only in FINISH row 685; this is a check item, it attacks no open lemma.

Order of checking (row 685): Lemma 2.3, Lemma 2.4, (B2), Theorem A(2), Theorem ZB-chain step 2, Proposition B; then Proposition 0, rest of Lemma 2.1, Lemma 2.2, Theorem A(1), Corollaries A1-A4, Corollaries 3.2, 3.3, Lemma 4.1; then the constants by hand; then A2 vs (TUBE)/(TUBE'); then the literature question.

## 1. Lemma 2.3 (one-link inequality): HOLDS

Checked line by line.
- Orientation. If b enters p inverted, U_p = U_b^{-1} W' up to cyclic order, and Re tr X = Re tr X^{-1} on SU(2); so a_p = 1 - <v, w_p> with w_p a function of the other three links in every case, and the one-link weight is const x exp(beta <v, s_b>). So nu^U = pi_{beta s_b(U)}. Correct.
- Leibniz formula. For one link, D_c(g h) = (D_c g) h + (theta_c g)(D_c h). Iterating over two links c, d gives four terms: (D_{cd} g) h, (theta_d D_c g)(D_d h), (theta_c D_d g)(D_c h), (theta_{cd} g)(D_{cd} h), using D_d theta_c = theta_c D_d for c != d. This is the stated formula with S_2 = {}, {d}, {c}, {c,d}; induction on |S| gives the general case. Linear in the measure, so the integral over v passes through. b is not in S, so D_S commutes with the replacement at b. Correct.
- Vanishing for S_2 not inside N(b): nu^U depends on U only through the links of N(b). Correct.
- S_2 = {}: g(v) = (D_S f)(U^{b->v}); |int g dpi_a| <= delta_S(f) (probability measure); g(v) - g(v') = (D_b^v D_S f)(U^{b->v'}), so the oscillation is at most delta_{S u b}(f); (B1) and Lemma 2.2 give eps delta_{S u b}(f). Correct.
- S_2 non-empty: g(v) = (D_{S_1} f)((U^{S_2->V})^{b->v}) has oscillation at most delta_{S_1 u b}(f) (S_1 u b is non-empty even for S_1 empty). lambda is an alternating sum of 2^{|S_2|} measures of mass 1 with signs summing to 0, so mass 0. Correct.
- [lambda] for S_2 = {c}: by (G2) c and b lie in exactly one common plaquette p (at least one because c is in N(b)), so s' - s = w_p' - w_p, |s' - s| <= 2, and |s|, |s'| <= 6 by (G1). With rho = (pi_{t'} - pi_{a'}) - (pi_t - pi_a), Re lambda = (pi_{a'} - pi_a) + Re rho and Im lambda = Im rho (pi_a, pi_{a'} are real), so [lambda] <= (1/2)(c(x) + 2||rho||_1) <= c(x)/2 + 2 eps. Correct.
- [lambda] for |S_2| >= 2: pairing R with R u {c_0} gives 2^{|S_2|-1} differences of one-link-changed measures, each of total variation at most c + 2 eps by (B3), and [lambda] <= ||lambda||_1. Correct (and not sharp: each piece could be bounded by c/2 + 2 eps in [.]; the author's constant is the weaker one and is still valid).
- |N(b)| = 3 |P(b)| <= 18: two plaquettes of P(b) sharing a further link c would give b and c two common plaquettes, against (G2). Correct.

## 2. Lemma 2.4 (contraction of a sweep): HOLDS

- kappa(S_2) = w^{|S_2|-1} chat(S_2): |(S minus S_2) u b| = |S| - |S_2| + 1. Correct.
- The matrix K_b: e_X with b not in X goes to e_X (coefficient 1); e_{T u b} goes to sum over S_2 inside N(b) minus T, T u S_2 non-empty, of kappa(S_2) e_{T u S_2}; coordinate X with b in X receives nothing (since (K_b m)_X = 0). The term landing on the empty set is dropped. This is correct: the inequality m_S(P_b f) <= (K_b m(f))_S is claimed only for non-empty S, and the empty set is not a coordinate.
- Total mass: eps/w + 18 (c/2 + 2 eps) + sum_{j>=2} binom(18, j) (2w)^j (c + 2 eps)/(2w) = gamma. Checked; with |N(b)| < 18 the sum only drops (all terms >= 0).
- Composition: m(P_{b2} P_{b1} f) <= K_{b2} m(P_{b1} f) <= K_{b2} K_{b1} m(f) because K_{b2} has non-negative entries. Following a unit mass at S: unchanged until the first enumerated link of S (every link is enumerated and S is non-empty), multiplied by at most gamma there, never increased afterwards when gamma <= 1. Correct.
- Last claim: nu^U has mass 1, so (P_b f - f)(U) = int (f(U^{b->v}) - f(U)) nu^U(dv), bounded by ||nu^U||_1 delta_b(f) <= delta_b(f)/(1 - eta), and delta_b <= ||f||_w / w. Correct.

## 3. Lemma 2.1, all three bounds: HOLDS

- (B2), re-derived. d/dtau int f dpi_{a_tau} = Cov_tau(f, <v, a' - a>), and for real |f| <= 1, sd_tau(f) <= 1, so ||pi_{a'} - pi_a||_1 <= |a' - a| sup_tau sd_tau(<v, e>) with |a' - a| = |x| |s' - s| <= 2|x|. |a_tau| <= 6|x| = kappa (convex combination of two vectors of norm <= 6|x|). Var_tau(g) <= E_tau g^2 = E_0[g^2 e^u]/E_0[e^u], E_0 e^u >= e^{E_0 u} = 1 (Jensen), e^u <= 1 + u + (u^2/2) e^{kappa} (Lagrange remainder, |u| <= kappa), E_0 g^2 = 1/4, E_0[g^2 u] = 0 (v -> -v), E_0[g^2 u^2] <= (E_0 g^4)^{1/2} (E_0 u^4)^{1/2} <= kappa^2 E_0 v_1^4. Independent check of E_0 v_1^4: for the uniform law on S^{n-1}, E v_1^4 = 3/(n(n+2)) = 3/24 = 1/8 at n = 4, which agrees with the author's (2/pi) int r^4 sqrt(1 - r^2) dr = (2/pi)(pi/16). So Var_tau(g) <= 1/4 + kappa^2 e^kappa / 16 = (1/4)(1 + 9 x^2 e^{6|x|}) (kappa^2/16 = 9x^2/4). Hence ||pi_{a'} - pi_a||_1 <= 2|x| (1/2) Sigma(x) = c(x). Correct.
- (B1). zeta(t) = E_a[e^{i y <v,s>}] zeta(a); |y <v, s>| <= 6|y| = eta; |E - 1| <= eta, density of pi_t w.r.t. pi_a is e^{iy<v,s>}/E with modulus <= 1/(1 - eta), and |density - 1| <= 2 eta/(1 - eta). Correct.
- (B3). Triangle inequality from (B1) twice and (B2). Correct.

## 4. Theorem A (all parts): HOLDS

- Region. gamma is increasing in eps for fixed w (all coefficients >= 0), eps is increasing in |y|, so each vertical slice of R is a symmetric interval when non-empty. On y = 0, gamma(x, 0, w) = 9 c(x) + c(x)((1+2w)^{18} - 1 - 36 w)/(2w) >= 9 c(x), with limit 9 c(x) as w -> 0; c is increasing in |x|. So R meets the real axis exactly in I = (-x_D, x_D), and T = R n {|Re beta| < x_D} has the form {|x| < x_D, |y| < h(x)} with h > 0; (x, y) -> (x, s y), s in [0, 1], retracts T onto I inside T. So T is open, connected, simply connected and contains 0.
- (1). Locally: gamma <= gamma_0 < 1, eta <= eta_0 < 1 on a neighbourhood O. ||P_b g||_w <= max(1, gamma) ||g||_w = ||g||_w along the sweep (total mass of each K_b at most 1), so sup|P^{n+1} f - P^n f| <= n_L gamma_0^n ||f||_w / (w (1 - eta_0)): uniformly Cauchy in (U, beta in O) for the fixed lattice. delta_S is Lipschitz in the sup norm (delta_S <= 2^{|S|} sup), so delta_S(f_inf) = 0 for every S and f_inf is constant. Analyticity of each iterate: P_b g = int g(U^{b->v}) e^{beta <v,s>} dv / zeta(beta s), zeta != 0 by (B1), numerator analytic by differentiation under the integral over a compact set, and joint continuity in (U, beta) propagates. Uniform limits of analytic functions are analytic. At real beta in R (that is, in I), mu_beta P_b = mu_beta gives mu_beta(f) = c(f, beta). Correct. (The rate constant n_L depends on the lattice; only convergence per lattice is used, so this is harmless. The region does not depend on the lattice; correct.)
- (2). G = sum_p c(a_p, .) is analytic on T, E = exp(-int_0^beta G) is well defined on the simply connected T and never 0. On I, Z' = -mu_beta(A) Z = -G Z, so (Z/E)' = 0 and Z = E on I (I is connected and contains 0, where both equal 1). Z entire, E analytic, T connected, I has accumulation points: Z = E on T, so Z != 0 on T. Correct.
- (3). Both sides analytic on T and equal on I. Correct.
- The application to boxes. A spatial box with free walls and periodic time of period k >= 3 satisfies (G1) (at most 2(d - 1) = 6 plaquettes per link in d = 4) and (G2) (two distinct links of Z^4 share at most one plaquette; periodicity creates a second common plaquette only for a period 2, or 1). Correct. The normalisation of beta used here, exp(-beta sum_p (1 - (1/2) Re tr U_p)), is checked against the plan's definition of Z(k, B; beta) in Section 7 below.

## 5. Theorem ZB-chain: HOLDS (steps 1, 2, 3 all checked)

Read against Theorem ZB of `library/gap-zero-transport.md` (Section 6, lines 84-98: inputs (TM_B), (SC_B), steps 3-4) and its check `library/gap-zero-transport-check.md` 3.4.
- Step 1. The disc D_i = {|beta - x_i| < rho_i} lies in Re beta > 0 (rho_i <= rho_0 <= r_0 <= x_i). There Re L = log|Z| <= log Z(Re beta) <= 0 (A >= 0), L(x_i) in [-2 N' x_i, 0]. The coefficient bound of Proposition 0(i) with A_0 = 0 gives |c_j| <= 2(0 - L(x_i)) rho_i^{-j} <= 4 N' x_i rho_i^{-j}, so |L(beta) - L(x_i)| <= 4 N' x_i sum_{j>=1} (7/8)^j = 28 N' x_i on |beta - x_i| <= 7 rho_i/8, and |L| <= 30 N' x_i. With N_k <= 6k|B|, N_{qk} <= 6qk|B|: |g_q| <= 30 x_i (6k|B| + 6k|B|) = 360 k |B| x_i <= M. Correct. Branches: the union of the chain discs is vertically convex with connected real trace, hence simply connected, and on the first disc (inside |beta| < 2 r_0) the branch real at r_0 is the branch of (SC_B), since two branches real at the same real point coincide. So the defect (C) of `gap-zero-transport-check.md` 3.3 does not arise here.
- Step 2. Base: |beta - r_0| <= rho_0/4 implies |beta| <= 5 r_0/4 <= 2 r_0, so (SC_B) gives e_k. Inductive step: two-constants on the annulus rho_i/4 < |z - x_i| < 7 rho_i/8, harmonic measure of the inner circle omega(z) = log((7 rho_i/8)/|z - x_i|)/log(7/2) (the ratio of radii is (7/8)/(1/4) = 7/2). A point with |z - x_{i+1}| <= rho_{i+1}/4 has |z - x_i| <= rho_i/2 + rho_{i+1}/4 <= 3 rho_i/4 (rho non-increasing), so in the annulus omega(z) >= log((7/8)/(3/4))/log(7/2) = log(7/6)/log(7/2) = omega_*; inside the inner disc the bound e holds directly. Since e <= M, (e/M)^{omega(z)} <= (e/M)^{omega_*}, and M (e/M)^{omega_*} with e = M (e_k/M)^{omega_*^i} is M (e_k/M)^{omega_*^{i+1}}. The last application at i = n covers real y with |y - x_n| <= 3 rho_n/4. Correct.
- omega_* by hand: log(7/6) is in (0.15415, 0.15416), log(7/2) in (1.25276, 1.25277), so omega_* is in (0.12304, 0.12306). Lambda = log(1/omega_*) < 2.1 because e^{-2.1} < 0.1225 < omega_* (e^{2.1} > 8.16 = 1/0.12255). Correct.
- Step 3 (as steps 3-4 of Theorem ZB). At real y, g_q(y) = log(1 + s_k) - (1/q) log(1 + s_{qk}) -> log(1 + s_k) (the check file 3.4: s_{qk} <= r_1^{(q-1)k} s_k). log(1 + s_k) <= R := M^{1-omega} e_k^{omega} with omega = omega_*^{n+1}; R -> 0 as k -> infinity because M = 360 k |B| x_n is polynomial in k and e_k is exponentially small; then e^{-k m_B} <= s_k <= e^R - 1 <= 2R, so m_B >= kappa_0 omega - (1/k) log(2 M^{1-omega} (C_0 |B| k)^{omega}), and k -> infinity. m_B does not depend on k. Correct. No limit of harmonic measures is needed here (the step 3.5 of the check file is avoided), which is a real simplification over Theorem ZB.
- Note (not a defect): the hypothesis "e_k < M" is met for large k, which is the only regime used.

## 6. Proposition B: HOLDS (as an implication; one sentence of its reading is too strong)

- mu(x_0) = m(x_0) >= kappa_1 by Corollary 3.3 at y = x_0 (needs x_0 <= 1/10 - 10^{-7}, which is assumed). kappa_1 is written with Lambda; Corollary 3.2 gives it with Lambda directly. Correct.
- For x < x*: r is positive and non-increasing on [r_0, x] (r_b on [r_0, x_0], then min(r_b, c min(1, mu)^p) with mu non-increasing); zero-free discs: Theorem A on [r_0, x_0], (H_p) on [x_0, x]. Corollary 3.2, with the integral split at x_0, gives m(y) >= kappa_1 exp(-2 Lambda phi(y)), and since phi is non-decreasing, mu(x) >= kappa_1 exp(-2 Lambda phi(x)). Not circular: (H_p) fixes r through the true mu, and the argument only bounds mu.
- r(s) >= min(r_b, c (kappa_1 e^{-2 Lambda phi})^p) = c kappa_1^p e^{-2 Lambda p phi} (kappa_1 <= 1 and c kappa_1^p <= r_b). phi is absolutely continuous with phi' = 1/r a.e., so (e^{-2 Lambda p phi})' >= -2 Lambda p/(c kappa_1^p) a.e., and the integrated inequality and the bound mu^p >= kappa_1^p - (2 Lambda p/c)(x - x_0) follow. Correct.
- End point. If x* < x_reach, then mu >= mu_* > 0 on [x_0, x*) and r >= r_* = c mu_*^p; Theorem ZB-chain with constant radius r_* (all chain discs are inside zero-free discs of radius r(x_i) >= r_*, or r_b >= r_* below x_0) reaches y in [x*, x* + r_*/4] (|y - x_n| <= 3 r_*/4), with n independent of the box. So mu > 0 beyond x*, a contradiction (if x* = X then x_reach = X and nothing is claimed). Correct.
- The reading. "Nothing is obtained beyond x_reach" and the FINISH summary "no hypothesis in which the zero-free radius shrinks with the gap can cross the region of coupling of order one" are claims about this transport, not theorems. What Proposition B proves is: with a transport whose loss is exponential in the number of discs (m >= kappa exp(-Lambda' int ds/r)), any power law r = c mu^p makes phi blow up in finite coupling. A transport with polynomial loss would change this (with m >= kappa (1 + int ds/r)^{-1} and p = 1, phi' <= (1 + phi)/(c kappa) has no blow-up). The two-constants theorem loses exponentially along a thin chain, so the conclusion is correct for every argument that goes through Theorem LP disc by disc, which is the plan's route. Also, the length of the continuation, c kappa_1^p/(2 Lambda p) with kappa_1 <= kappa_0 exp(-2.1 (2 (x_0 - r_0)/r_b + 1)) and r_b <= 10^{-7}, is astronomically small for any x_0 well above r_0: the base Corollary 3.3 already costs a factor exp(-4.2 x 10^7 (x_0 - r_0)). Proposition B is correct as stated; its interpretation in the FINISH row should say "with the two-constants transport".

## 7. Proposition 0, Lemma 2.2: HOLD

- Proposition 0(i). On the disc, |Z(beta)| <= Z(Re beta) <= exp(2N max(0, -Re beta)) and Re beta > x - rho, so Re g <= A_0 = 2N max(0, rho - x). For g = sum c_j z^j, (1/2pi) int Re g(x + r e^{it}) e^{-ijt} dt = c_j r^j/2 (j >= 1), and the mean of A_0 - Re g >= 0 is A_0 - g(x) with g(x) >= -2Nx. So |c_j| r^j <= 2(A_0 - g(x)) <= 4N (max(0, rho - x) + x) = 4N max(x, rho). Correct.
- (ii). The Taylor series of log Z at x (Z(x) > 0) has radius >= 1/C; exp of it equals Z near x, hence on the disc. Correct.
- The equivalence with constants: 4 max(x, rho) rho^{-j} <= C^j with C = max(1, 4 max(beta_1, rho))/rho, since max(1, a)^j >= a for j >= 1. Correct. The union of the open discs of radius 1/C about the interval is its open 1/C-neighbourhood. Correct. The brief's form uses N <= 6k|B|. Correct.
- The normalisation: the plan's Z(k, B; beta) = int exp(-beta sum_p (1 - (1/2) Re tr U_p)) dU (`gap-skeleton-max-b.md` line 536; `gap-zero-transport.md` line 84, with at most 6k|B| plaquettes) is the file's Z. Correct.
- Lemma 2.2. Re lambda, Im lambda have mass 0; for a real mass-zero lambda_1, rotate the phase so that the integral is real, pass to the real part r of e^{i phi} g (oscillation <= d), subtract the mid-range: |int r dlambda_1| <= (d/2) ||lambda_1||_1. Correct.

## 8. Corollaries A1, A3, A4, 3.2, 3.3: HOLD. Corollary A2: HOLDS AFTER CORRECTION

- A1. For 10^{-7} <= x <= 1/10 - 10^{-7} the disc |beta - x| < 10^{-7} lies in Q (Re beta in (0, 1/10], |Im| < 10^{-7}); Proposition 0(i) gives 4N x j! 10^{7j}, and 4N x <= 6k|B| x 4 <= 6k|B|. Correct.
- A3. Within a sweep, sup|g_i - g_{i-1}| <= delta_{b_i}(g_{i-1})/(1 - eta) <= a_i/(w(1 - eta)), with a_i the mass of the majorant M_{i-1} on sets containing b_i; K_{b_i} replaces a_i by at most gamma a_i, so sum a_i <= ||g||_w/(1 - gamma); summing over sweeps with ||P^n f||_w <= gamma^n ||f||_w gives 1/(w(1 - eta)(1 - gamma)^2). Lattice-free. Correct. Numerical constant on Q: 1/(4 x 10^{-4} x (1 - 6 x 10^{-7}) x 0.011^2) = 2.0661... x 10^7 < 2.1 x 10^7. Correct.
- A4. d/dx mu_x(F) = -<F; A>_x = -sum_p <F; a_p>; mu_x(F) = c(F, x) is analytic on T and, by A3, bounded on Q by (1 + 2.1 x 10^7 ((1.0008)^{n_F} - 1)) sup|F|; the closed disc of radius 10^{-7} about x, |x| <= 1/10 - 10^{-7}, lies in Q; Cauchy's estimate. Correct. Remark: the bound grows exponentially in n_F and is in sup|F|, not in sum_b sup|grad_b F|; it is the brief's follow-up form "C ||F||" for local F (gap-skeleton-max-b.md line 541), not the (HS-sup) form.
- **A2: HOLDS AFTER CORRECTION, two defects, neither touches Theorem A.**
  (a) U = interior of Q does not contain beta_1 = 1/10, and the brief asks for an open set containing the closed interval [r_0, beta_1]. Corrected statement: U = T (open, contains Q, hence [r_0, 1/10]); or keep U = interior of Q and take beta_1 any number < 1/10. Proof unchanged: Theorem A(2).
  (b) The domain for Theorem ZB: "a subdomain of T with the shape condition (TUBE), for instance a thin rectangle" is false as written. By `gap-zero-transport-check.md` 3.1, no bounded domain satisfies (TUBE), and a thin rectangle fails at its right end: at beta = X - delta + i y the disc about X - delta of radius |y| leaves the rectangle when |y| > delta. Two correct replacements:
  (b1) With (TUBE') and the corrected Theorem ZB (check file 3.6). Take a Lipschitz lens D = {-2 r_0 < x < X', |y| < h(x)}, X' < 1/10, h piecewise linear, h(x) > sqrt(r_0^2 - x^2) on [-r_0, r_0], h(x) < sqrt(4 r_0^2 - x^2) on (-2 r_0, x_1] with x_1 in (r_0, min(2 r_0, X')), h <= (1/2) 10^{-7} on [x_1, X'), h -> 0 linearly at both ends (possible: near -2 r_0 the bound sqrt(4 r_0^2 - x^2) is of order sqrt(x + 2 r_0), above any linear function near the end). Every point of D is either in |beta| < 2 r_0 (zero-free by (SC_B)) or in Q (zero-free by Theorem A), so (ZF_B) holds on D; D is vertically convex, so (C) holds; (TUBE') holds with theta = (1 + Lambda_h^2)^{-1/2}, Lambda_h the Lipschitz constant of h (large, of order r_0/10^{-7}, harmless: it enters only through a polynomial in k). Conclusion m_B(beta) >= kappa_0 omega_D(beta) > 0 for real beta in (r_0, X'). Needs r_0 < X' so that x_1 exists; if r_0 >= 1/10 the whole interval [0, 1/10] is inside the (SC_B) disc and Theorem A adds nothing. This repair uses only stated results; I checked its geometry, not by a second derivation of Lemma S.
  (b2) With Theorem ZB-chain in place of Theorem ZB: this is Corollary 3.3, which holds (below) and needs no shape condition. Preferred: shorter, and it avoids both Lemma S and the limit of harmonic measures.
  So A2 holds with (TUBE') and with Theorem ZB-chain; it does not hold with (TUBE).
- 3.2. Chain x_{i+1} = x_i + r(x_i)/2, rho_i = r(x_i) (non-increasing, <= r_0), stopped at the first n with y <= x_n + r(x_n)/2; then x_n <= y (for n >= 1, y > x_n by minimality) and |y - x_n| <= rho_n/2 <= 3 rho_n/4; termination because each step is >= r(X)/2 > 0; each completed step has int_{x_i}^{x_{i+1}} ds/r >= 1/2. Correct.
- 3.3. r_b discs about x in [r_0, 1/10 - 10^{-7}] lie in Q. Correct, with two precisions: it needs r_0 <= 1/10 - 10^{-7}, and its range is [r_0, 1/10 - 10^{-7}] (the status block item 4 writes "[r_0, 1/10)"; the chain reaches 1/10 - 10^{-7}/4 at most with discs inside Q; with discs inside T it reaches further, but no explicit radius past 1/10 is stated in the file).

## 9. Lemma 4.1: HOLDS

- (i) On the unit sphere S^3 of R^4, a linear function is a spherical harmonic of degree 1, eigenvalue -l(l + n - 2) = -3 (n = 4). So Delta_b a_p = 3(1 - a_p) for each of the 4 links of p (each enters a_p linearly, by the orientation remark of Section 1), Delta a_p = 12 (1 - a_p), Delta A = 12 (N - A). Correct (with the metric in which SU(2) is the unit sphere for <A, B> = (1/2) Re tr A^* B, as in the file).
- (ii) The spherical gradient of -<v, s> is minus the tangential part of s, |.|^2 = |s|^2 - <v, s>^2. Lgen A = 12(N - A) - beta Q. Correct.
- (iii) Integration by parts on the closed manifold (S^3)^L for mu_beta proportional to e^{-beta A}: <F Lgen H> = -<grad F . grad H>; F = 1 gives 12(N - <A>) = beta <Q>; subtracting <F> times this from the identity for F gives 12 <F; A> = <grad F . grad A> - beta <F; Q>. Re-derived. Correct.
- The remarks after it ((HS-sup) implies the gradient bound; first term Phi = A/12 at beta = 0) are correct. The L^2 bound from Ric + beta Hess A >= 2 - 30 beta is not checked here (it is checked as HOLDS in `gap-zero-transport-check.md` Section 8).

## 10. Remarks 2.5.1-2.5.3

- 2.5.1 (a separate complex coupling per plaquette): the one-link bounds hold unchanged, as stated (|a| <= 6 max|x_p|, |sum_p y_p <v, w_p>| <= 6 max|y_p|, |a' - a| <= 2 max|x_p|). HOLDS AFTER CORRECTION in one step the file omits: the several-variable analogue of Theorem A(2) needs the 1-form sum_p c(a_p, beta) d beta_p to be closed, so that E is defined on Q^P. It is: d c(a_p)/d beta_q and d c(a_q)/d beta_p are analytic on the connected domain and equal at real points (both -<a_p; a_q>), and real points form a totally real set of full dimension, so they agree everywhere; Q^P is convex. Joint analyticity of the limit c(f, .) holds as a locally uniform limit of jointly analytic functions. With that line, the remark holds.
- 2.5.2: the identification with Dobrushin's condition is right: the Dobrushin coefficient C_{bc} is half the total variation of the change of the one-link law when link c is changed, at most c(x)/2, and sum_c C_{bc} <= 9 c(x). The consequence "unique Gibbs state, exponential decay" is Dobrushin's theorem, recalled, not rebuilt in the file (it is not used in any proof there).
- 2.5.3 (U(1), Z_2, adjoint): not checked; no proof in the file depends on it.

## 11. The explicit constants, by hand

No numerical job was run (none needed; every number below is hand arithmetic with displayed digits). Reference values used: e^{0.5} = 1.64872..., e^{0.1} = 1.10517..., e^{0.012} = 1.01207..., e^{0.018} = 1.01816..., e^{0.0128} = 1.01288..., e^{0.3} = 1.34986..., e^{0.32} = 1.37713....

- gamma. gamma(x, y, w) = eps/w + 9 c(x) + 36 eps + (c(x) + 2 eps)((1 + 2w)^{18} - 1 - 36 w)/(2w): the formula of Lemma 2.4 expanded; matches the count of Section 2 above. The bound ((1 + u)^{18} - 1 - 18 u)/u <= 153 u (1 + u)^{16} is the Lagrange remainder f''(xi) u^2/2 of f(u) = (1 + u)^{18}, with 153 = 18 x 17/2. Correct.
- The threshold x_D, root of 9 x sqrt(1 + 9 x^2 e^{6x}) = 1. At x = 0.102: 9 x^2 = 0.093636, e^{0.612} = 1.84412, product 0.172676, sqrt(1.172676) = 1.08290 (1.0829^2 = 1.172672), value 0.918 x 1.08290 = 0.99410 < 1. At x = 0.103: 9 x^2 = 0.095481, e^{0.618} = 1.85521, product 0.177138, sqrt(1.177138) = 1.08496, value 0.927 x 1.08496 = 1.00576 > 1. So x_D is in (0.102, 0.103), about 0.1025. "Near 0.102" is right.
- x_D > 1/10: at x = 1/10, e^{0.6} < 1.6488 x 1.1052 = 1.82226 < 1.83, 9 x^2 e^{0.6} < 0.1647, sqrt(1.1647) < 1.08 (1.08^2 = 1.1664), c < 0.108, 9c < 0.972 < 1. Correct.
- The width 10^{-7} with w = 4 x 10^{-4}: eta <= 6 x 10^{-7}; eps <= 1.2 x 10^{-6}/(1 - 6 x 10^{-7}) < 1.3 x 10^{-6}; eps/w < 3.25 x 10^{-3}; 36 eps < 4.7 x 10^{-5}; 153 x 0.0008 x 1.01288 = 0.12398 < 0.1240; (c + 2 eps) < 0.1081; 0.1240 x 0.1081 = 0.013404 < 0.0135. Sum < 0.972 + 0.00325 + 0.00005 + 0.0135 = 0.9888 < 0.989. So gamma < 0.989 uniformly on Q and Q lies in T. Correct.
- The wider rectangle |x| <= 1/20, |y| <= 3 x 10^{-5}, w = 0.01: c(1/20) = 0.05 sqrt(1 + 0.0225 x 1.34986) = 0.05 x 1.01507 = 0.050754, so 9c = 0.45678 < 0.457 (true; note that the file's intermediate bound c < 0.0508 alone gives only 9c < 0.4572, a slip of no consequence); eps <= 3.6 x 10^{-4}/(1 - 1.8 x 10^{-4}) < 3.7 x 10^{-4}; eps/w < 0.037; 36 eps < 0.014; 153 x 0.02 x 1.37713 x 0.0516 = 0.21744 < 0.218. Sum < 0.4572 + 0.037 + 0.014 + 0.218 = 0.7262 < 0.73. Correct.
- The region T: open, symmetric, vertically convex over I = (-x_D, x_D), simply connected (Section 4 above). Correct.
- Corollary A3 constant on Q: 1/(w (1 - eta)(1 - gamma)^2) < 1/(4 x 10^{-4} x 0.9999994 x 1.21 x 10^{-4}) < 2.067 x 10^7 < 2.1 x 10^7. Correct.
- omega_* = log(7/6)/log(7/2) in (0.12304, 0.12306) and Lambda = log(1/omega_*) in (2.0951, 2.0953) < 2.1 (Section 5). Correct.

## 12. Does Theorem A follow from a known theorem?

What I read for this question: the arXiv API listings and abstracts returned by searches for Dobrushin uniqueness with analyticity, zeros, complex parameters, lattice gauge theory, and correlation decay with zero-freeness (scratch folder /tmp/zfcheck-lit). Hits relevant in kind, abstracts only: Shao and Sun, "Contraction: a unified perspective of correlation decay and zero-freeness of 2-spin systems", arXiv:1909.04244; Liu, Sinclair and Srivastava, "Correlation decay and partition function zeros: algorithms and phase transitions", arXiv:1906.01228; Regts, "Absence of zeros implies strong spatial mixing", arXiv:2111.04809. All three are about finite-spin systems on graphs; none treats a compact continuous spin, plaquette interactions or gauge theory. The repository's earlier literature passes (`library/prior/gap-crux-lit-cross.md` lines 17-19, 51, 106-113; `library/prior/gap-prior.md` lines 211, 217) record the same: no primary page of Dobrushin-Shlosman retrieved, no gauge result found.

Not read (no primary text available by the routes that work on this machine; Springer stops at a bot check): Dobrushin and Shlosman, "Completely analytical Gibbs fields" (1985) and "Completely analytical interactions: constructive description" (J. Stat. Phys. 46, 1987); Dobrushin, "Perturbation methods of the theory of Gibbsian fields" (Saint-Flour 1994, LNM 1648); Osterwalder and Seiler, "Gauge field theories on a lattice", Ann. Phys. 110 (1978); Gross, "Absence of second-order phase transitions in the Dobrushin uniqueness region", J. Stat. Phys. 25 (1981).

Answer, labelled by what it rests on.
- Recalled, `unchecked`: Dobrushin-Shlosman complete analyticity is stated for finite single-spin spaces and finite-range potentials; it includes, among its equivalent conditions, a volume-uniform zero-free complex neighbourhood of the interaction, and their constructive criterion (a Dobrushin-type condition on finite boxes) implies it. If an extension to compact continuous spins (here S^3 with Haar measure) and to plaquette potentials is in the literature, Theorem A would be an instance of it, with the one-link Dobrushin condition 9 c(x) < 1 as the criterion; I did not find such an extension and cannot confirm it.
- Recalled, `unchecked`: Osterwalder-Seiler's strong-coupling expansion gives analyticity, uniformly in the volume, in a complex disc about beta = 0 whose radius is small and, in their text as I recall it, not given as a number like 1/10. Theorem A's interval [0, 1/10] with a tube of width 10^{-7} is a different shape (long and thin) and is not obviously inside their disc.
- So: Theorem A is of the known Dobrushin type in method (the file says so in 2.5.2 and in its credits), it may be a special case of a known continuous-spin extension of complete analyticity, and I could not establish that. Nothing in the chain depends on the answer, since the proof checked above is complete and self-contained.

## 13. Defects, ranked by what each breaks

None breaks Theorem A, Theorem ZB-chain or Proposition B.
1. Corollary A2, domain (TUBE). "A subdomain of T with the shape condition (TUBE), for instance a thin rectangle" names a condition that no bounded domain satisfies (`gap-zero-transport-check.md` 3.1); a thin rectangle fails at its right end. Breaks the second sentence of A2 as written. Repair (checked above, 8 (b1), (b2)): use Theorem ZB-chain (Corollary 3.3), or the corrected Theorem ZB with a Lipschitz lens satisfying (TUBE').
2. Corollary A2, open set. U = interior of Q does not contain beta_1 = 1/10. Repair: U = T.
3. Interpretation of Proposition B (in the file's 3.2 closing paragraph and in the FINISH row 677 summary): "no hypothesis in which the zero-free radius shrinks with the gap can cross the region" holds for a transport whose loss is exponential in the number of discs, that is, for the two-constants route; it is not a theorem about every continuation. Suggested wording: "with the two-constants transport (Theorem ZB-chain), no hypothesis of the form r = c mu^p crosses ...".
4. Remark 2.5.1 (several couplings) omits the closedness of the 1-form sum_p c(a_p, beta) d beta_p; one line (equal mixed derivatives at real points, identity theorem) repairs it.
5. Section 4, status of (HS-sup): "on the base it holds in the integrated form of Corollary A4" is loose. A4 bounds |sum_p <F; a_p>| by a constant times sup|F| that grows like (1.0008)^{n_F}; it does not bound sup|grad_b Phi| and does not give the form C sum_b sup|grad_b F|. (HS-sup) is proved nowhere, on the base or above it.
6. Small precisions: Corollary 3.3's range is [r_0, 1/10 - 10^{-7}] and needs r_0 <= 1/10 - 10^{-7} (status block item 4 says [r_0, 1/10)); in 2.3 the step "c < 0.0508, so 9c < 0.457" needs the sharper c(1/20) = 0.050754 (true). No consequence.

## 14. Table of verdicts

| Statement (file `library/gap-zf-box-x.md`) | Verdict | Note |
|---|---|---|
| Lemma 2.3 (one-link inequality) | HOLDS | Leibniz formula, vanishing terms, mass-zero pairing, [lambda] bounds all checked (Section 1) |
| Lemma 2.4 (sweep contraction) | HOLDS | Dropping the empty-set term is correct (Section 2) |
| Lemma 2.1 (B2) | HOLDS | Variance bound re-derived; E v_1^4 = 1/8 by a second route (Section 3) |
| Lemma 2.1 (B1), (B3) | HOLDS | Section 3 |
| Lemma 2.2 | HOLDS | Section 7 |
| Theorem A (1) | HOLDS | Section 4 |
| Theorem A (2) | HOLDS | Identity-theorem step correct; T simply connected (Section 4) |
| Theorem A (3) | HOLDS | Section 4 |
| Theorem ZB-chain | HOLDS | Steps 1-3 checked; branch issue (C) does not arise; no limit of harmonic measures needed (Section 5) |
| Corollary 3.2 | HOLDS | Section 8 |
| Corollary 3.3 | HOLDS | Range [r_0, 1/10 - 10^{-7}] (Section 8) |
| Proposition B | HOLDS | As an implication; its reading is for the two-constants transport only (defect 3) |
| Proposition 0 (i), (ii), equivalence | HOLDS | Section 7 |
| Corollary A1 | HOLDS | Section 8 |
| Corollary A2 | HOLDS AFTER CORRECTION | U = T; (TUBE) replaced by Theorem ZB-chain or by (TUBE') with a Lipschitz lens (defects 1, 2) |
| Corollary A3 | HOLDS | Constant 2.1 x 10^7 checked |
| Corollary A4 | HOLDS | Constant 10^7 (1 + 2.1 x 10^7 ((1.0008)^{n_F} - 1)) checked |
| Lemma 4.1 (i)-(iii) | HOLDS | Re-derived (Section 9) |
| Remark 2.5.1 | HOLDS AFTER CORRECTION | Closedness of the 1-form (defect 4) |
| Remark 2.5.2 | HOLDS | Dobrushin coefficient sum <= 9 c(x); the consequences are Dobrushin's theorem, recalled, unused |
| Constants: gamma, x_D in (0.102, 0.103), width 10^{-7}, region T, 1/20 by 3 x 10^{-5} rectangle, omega_*, Lambda | HOLD | By hand (Section 11) |
| Theorem A from a known theorem | UNDETERMINED | Dobrushin-Shlosman, Osterwalder-Seiler not read; see Section 12 |

In the vocabulary of the FINISH rules: Theorem A and Theorem ZB-chain ADVANCE (correct, and new statements on the route: an explicit volume-uniform zero-free region for boxes with free walls, and a transport with no shape condition); Proposition B is CORRECT-NO-ADVANCE (it limits the route, it does not extend it); nothing is WRONG beyond the corrected Corollary A2 and the noted wordings.

Status. Checked by Claude Opus 5.5 (high) on the Mac mini at 53b90e6c9; a second reader of the same vendor, with the steps marked "re-derived" done by a different route. Not checked here: (TM_B), (SC_B) (inputs, rows 681 and 683), the three failed ways and the Ising consistency test of 3.3 (reports, not statements), Remark 2.5.3, the Hessian bound of plan 1.4. Open after this check, unchanged by it: (SC_B), (TM_B), (H_p), (HS-sup), any zero-free neighbourhood of a real coupling above x_D.
