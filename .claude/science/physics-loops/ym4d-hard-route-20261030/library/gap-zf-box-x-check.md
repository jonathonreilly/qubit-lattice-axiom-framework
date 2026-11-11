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

