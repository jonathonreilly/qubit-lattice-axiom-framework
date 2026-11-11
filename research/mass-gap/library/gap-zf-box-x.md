lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T13:38Z

# gap-zf-box-x: zeros of Z(k,B;beta) for boxes with free walls (FINISH row 677, node Z6)

Provenance: one session, Claude Fable 5.2 medium, commit d76689eed. Not checked by another model. Written step by step; the status block at the end is the summary.

## 0. Repo search, duplicate check, reading state

- Duplicate check (grep of `library/open-core.md` and the FINISH rows for ZF_B, zero-free, cumulant): the only row for this lemma is row 677 (this one). Neighbours: row 683 `gap-sc-box` owns the winding bound (SC_B) on the disc; row 681 owns (TM_B) and the check of Theorem ZB; row 680 owns the scaling region. Nothing below proves (SC_B) or (TM_B).
- Read in full: the brief (plan Part 4 Item 1), plan sections 1.4, 1.7, 1.9, 2.5, 3.1, `library/gap-zero-transport.md`, section 4.2 of `library/gap-skeleton-final.md`. Not opened: the arXiv papers 1005.1993, 1112.2734 (numerical picture for periodic lattices; nothing below uses them), the Sussman-Alpoge account (nothing below uses it; the object here, a box with free walls at fixed lattice coupling, is outside its estimates, as plan 2.5 says).
- Credits. The uniqueness condition and its contraction argument are Dobrushin's (1968-70; recalled, not read in this run). That a uniqueness condition of this type gives analyticity is the theme of Dobrushin and Shlosman's "completely analytical" papers (1985-87; recalled, not read). The Borel-Caratheodory coefficient bound is classical. The transport theorem ZB that consumes the result is the plan's (Claude Fable 5.2, row 670). The proof of Theorem A below (a hierarchy of mixed oscillations that makes the complex one-link heat-bath kernels contract) was built in this run; I do not know whether it is in the literature in this form. Label for every literature recollection here: `unchecked`; nothing in the proofs rests on one.

Conventions. G = SU(2) with Haar probability measure. A finite set of links L and a finite set of plaquettes P; each plaquette p has four links in L and a_p(U) = 1 - (1/2) Re tr U_p in [0, 2]. Geometric hypotheses, used below and true for a spatial box with free walls and periodic time k >= 3, for a periodic torus with all sides >= 3, and for every sub-family of the plaquettes of such a lattice:
(G1) every link lies in at most 6 plaquettes of P;
(G2) two distinct links lie in at most one common plaquette of P.
(For k = 2 the two time-like plaquettes over a spatial link share both copies of it, so (G2) fails; k >= 3 is assumed.) N = |P| <= 6 k |B| for the box. A = sum_p a_p, Z(beta) = int exp(-beta A) dU, entire in beta; for real beta, mu_beta is the probability measure exp(-beta A) dU / Z.

## 1. Step 0: the real form, proved equivalent with constants

For real beta, kappa_j(beta) = (-1)^j (d/dbeta)^j log Z(beta) is the j-th cumulant of A under mu_beta.

**Proposition 0.** Fix the lattice (L, P), a real x >= 0 and rho > 0.
(i) If Z has no zero in the open disc |beta - x| < rho, then |kappa_j(x)| <= 4 N max(x, rho) j! rho^{-j} for all j >= 1.
(ii) If there are C and any number K (it may depend on the lattice in any way) with |kappa_j(x)| <= K j! C^j for all j >= 1, then Z has no zero in |beta - x| < 1/C.
Consequently, for an interval [r_0, beta_1] and a family of lattices: "there is rho > 0 such that no Z of the family vanishes within distance rho of [r_0, beta_1]" is equivalent to "there is C such that |kappa_j(x)| <= N j! C^j for all j >= 1, all x in [r_0, beta_1] and all lattices of the family", with C = max(1, 4 max(beta_1, rho))/rho in one direction and rho = 1/C in the other. For boxes N <= 6 k |B|, which is the form in the brief. An open set U containing the compact interval contains its rho-neighbourhood for some rho > 0, so this is the equivalence asked for.

Proof. (i) g = log Z is analytic in the disc, with the branch real at x. For beta in the disc, |Z(beta)| <= Z(Re beta) <= exp(2 N max(0, -Re beta)), so Re g <= A_0 := 2 N max(0, rho - x). And g(x) >= -2 N x since A <= 2N. Write g(x + z) = sum_j c_j z^j. For 0 < r < rho and j >= 1: c_j r^j = (1/pi) int_0^{2 pi} Re g(x + r e^{i t}) e^{-i j t} dt (the Fourier coefficient of the real part), and int e^{-ijt} dt = 0, so c_j r^j = -(1/pi) int (A_0 - Re g) e^{-ijt} dt. The integrand A_0 - Re g is >= 0 and its mean is A_0 - g(x). So |c_j| r^j <= 2 (A_0 - g(x)) <= 2 (2N max(0, rho - x) + 2 N x) = 4 N max(x, rho). Let r -> rho; kappa_j = (-1)^j j! c_j.
(ii) The Taylor series S(z) = sum_j (-1)^j kappa_j (z - x)^j / j! + log Z(x) converges in |z - x| < 1/C. Near x it equals log Z, so exp(S) = Z near x, hence on the whole disc (identity theorem; Z is entire). exp(S) has no zeros. QED.

Remark 0.1. The extensive prefactor 6 k |B| is free: by (ii) and then (i), any bound K j! C^j with K depending on the lattice gives 4 N max(x, 1/C) j! C^j. The content of the real form is the uniform radius of convergence alone.

Remark 0.2. As literally written, the statement of the item ("there are r_0 > 0 and beta_1 > r_0 ...") is already satisfied inside the strong-coupling disc. The content is the size of beta_1. Section 2 gives an explicit beta_1 with an explicit tube, by an argument that is not a polymer expansion around beta = 0.

## 2. Step (a): the base. An explicit zero-free tube over [0, 1/10]

Result of this section: **Theorem A.** For every lattice with (G1), (G2), in particular every box with free walls, every size, every k >= 3: Z(beta) != 0 on the rectangle |Re beta| <= 1/10, |Im beta| <= 10^{-7}, and more generally on the region T of 2.5. The base interval is [0, 1/10], which contains [0, 1/15) and passes 1/12. The route differs from the one the brief names: no log-Sobolev inequality and no tree bound on truncated functions is used. The one-link heat-bath kernels at complex coupling are shown to contract in a norm built from mixed oscillations; the contraction constant is Dobrushin's sum plus terms that vanish with Im beta. (Why not the brief's route: a log-Sobolev or Poincare inequality controls log Z only in real directions; the passage to the complex direction needs factorial bounds on all truncated functions, which by Proposition 0 is the statement itself. The contraction below proves the statement directly.)

### 2.1 One link

Identify SU(2) with the unit sphere S^3 in R^4 (quaternions); Haar measure is the uniform probability measure dv; (1/2) Re tr(A^* B) is the Euclidean inner product <A, B>. Fix a link b. For a plaquette p containing b, U_p is, up to cyclic order and inversion (neither changes Re tr), v W_p with v = U_b and W_p a product of the other three link variables or their inverses. So a_p = 1 - <v, w_p> with w_p = W_p^{-1} in S^3, and w_p depends only on the three other links of p. Put P(b) = plaquettes containing b (at most 6), N(b) = the other links of these plaquettes (at most 18; by (G2) each lies in exactly one p in P(b)), s = s_b(U) = sum_{p in P(b)} w_p, a vector in R^4 with |s| <= 6.

For t in C^4 put zeta(t) = int exp(<v, t>) dv (bilinear pairing) and, where zeta(t) != 0, pi_t(dv) = exp(<v, t>) dv / zeta(t), a complex measure of total mass 1. The one-link conditional measure at coupling beta = x + iy is nu_b^U = pi_{beta s_b(U)}, and the heat-bath operator on C(Omega), Omega = G^L, is
(P_b f)(U) = int f(U^{b -> v}) nu_b^U(dv),
where U^{b -> v} is U with U_b replaced by v. P_b f does not depend on U_b. For real beta, mu_beta P_b = mu_beta.

**Lemma 2.1 (three bounds).** Let beta = x + iy, eta = 6|y| < 1, and s, s' in R^4 with |s|, |s'| <= 6, |s' - s| <= 2. Put a = x s, t = beta s, a' = x s', t' = beta s'.
(B1) zeta(t) != 0, ||pi_t||_1 <= 1/(1 - eta), and ||pi_t - pi_a||_1 <= eps := 2 eta/(1 - eta).
(B2) ||pi_{a'} - pi_a||_1 <= c(x) := |x| Sigma(x), with Sigma(x) = sqrt(1 + 9 x^2 e^{6|x|}).
(B3) ||pi_{t'} - pi_t||_1 <= c(x) + 2 eps.
Proof. (B1) zeta(t)/zeta(a) = E_a[e^{i y <v, s>}], where E_a is the expectation of the probability measure pi_a. |y <v, s>| <= eta, and |e^{i r} - 1| <= |r|, so |zeta(t)/zeta(a) - 1| <= eta < 1. The density of pi_t against pi_a is e^{i y <v,s>}/E_a[e^{i y <v,s>}], of modulus at most 1/(1 - eta), and it differs from 1 by at most (|e^{iy<v,s>} - 1| + |1 - E_a e^{iy<v,s>}|)/(1 - eta) <= 2 eta/(1 - eta).
(B2) Let a_tau = a + tau (a' - a), |a_tau| <= 6|x| =: kappa. For real f with |f| <= 1: d/dtau int f dpi_{a_tau} = Cov_tau(f, <v, a' - a>), of modulus at most sd(f) sd(<v, a' - a>) <= |a' - a| sd_tau(<v, e>) for a unit vector e, and |a' - a| <= 2|x|. Variance bound: with g = <v, e>, u = <v, a_tau>, E_0 the Haar expectation, Var_tau(g) <= E_tau[g^2] = E_0[g^2 e^u]/E_0[e^u]. E_0[e^u] >= exp(E_0 u) = 1. e^u <= 1 + u + (u^2/2) e^{kappa} since |u| <= kappa. E_0[g^2] = 1/4 (the four coordinates have equal second moments, summing to 1). E_0[g^2 u] = 0 (v -> -v preserves Haar). E_0[g^2 u^2] <= (E_0 g^4)^{1/2} (E_0 u^4)^{1/2} = kappa^2 E_0[v_1^4] = kappa^2/8 (the density of v_1 on S^3 is (2/pi) sqrt(1 - r^2) on [-1, 1], and int r^4 sqrt(1 - r^2) dr = pi/16). So Var_tau(g) <= 1/4 + kappa^2 e^{kappa}/16 = (1/4)(1 + 9 x^2 e^{6|x|}). Hence |int f d(pi_{a'} - pi_a)| <= 2|x| (1/2) Sigma(x).
(B3) pi_{t'} - pi_t = (pi_{a'} - pi_a) + (pi_{t'} - pi_{a'}) - (pi_t - pi_a); use (B1) twice and (B2). QED.

**Lemma 2.2 (pairing with a measure of mass zero).** Let lambda be a complex measure on G with lambda(G) = 0 and g a complex continuous function with |g(v) - g(v')| <= d for all v, v'. Then |int g dlambda| <= d [lambda], where [lambda] := (1/2)(||Re lambda||_1 + ||Im lambda||_1) <= ||lambda||_1.
Proof. Re lambda and Im lambda are real measures of mass zero. For a real measure lambda_1 of mass zero choose phi with e^{i phi} int g dlambda_1 >= 0; then |int g dlambda_1| = int r dlambda_1 with r = Re(e^{i phi} g), a real function with oscillation at most d; subtract its mid-range value: |int r dlambda_1| <= (d/2) ||lambda_1||_1. Add the two parts. QED.

### 2.2 Mixed oscillations and the one-link inequality

For a link c and v in G put (D_c^v f)(U) = f(U^{c -> v}) - f(U). These operators commute for different links. For a finite non-empty set S of links and V in G^S put D_S^V = prod_{c in S} D_c^{V_c}, and
delta_S(f) = sup over U in Omega and V in G^S of |(D_S^V f)(U)|.
For a weight w in (0, 1] put ||f||_w = sum over non-empty S of w^{|S|} delta_S(f). It is finite for bounded f on a finite lattice (delta_S <= 2^{|S|} sup|f|), and it is a seminorm that vanishes exactly on constants (delta_{c}(f) = 0 for every link c means f is constant).

Constants of the inequality, for beta = x + iy with eta = 6|y| < 1, in the notation of Lemma 2.1:
chat(empty) = eps; chat(S_2) = c(x)/2 + 2 eps for |S_2| = 1; chat(S_2) = 2^{|S_2| - 1} (c(x) + 2 eps) for |S_2| >= 2.

**Lemma 2.3 (one-link inequality).** For every link b, every f in C(Omega), every non-empty S: delta_S(P_b f) = 0 if b is in S, and if b is not in S,
delta_S(P_b f) <= delta_S(f) + sum over S_2 subset of S intersect N(b) (the empty set included) of chat(S_2) delta_{(S minus S_2) union {b}}(f).
Proof. P_b f does not depend on U_b; this gives the first claim. Let b not in S. Write F(U, v) = f(U^{b -> v}). For a link c != b, with U^c short for U^{c -> V_c}:
D_c (int F(U, v) nu^U(dv)) = int [F(U^c, v) - F(U, v)] nu^U(dv) + int F(U^c, v) [nu^{U^c} - nu^U](dv).
Iterating over the links of S (induction on |S|; the differences act on the variables other than U_b) gives the discrete Leibniz formula
D_S^V (P_b f)(U) = sum over S_2 subset of S of int (theta_{S_2} D_{S minus S_2}^V F)(U, v) (D_{S_2}^V nu)^U(dv),
where theta_{S_2} replaces U by U^{S_2 -> V}, and (D_{S_2}^V nu)^U = sum over R subset of S_2 of (-1)^{|S_2 minus R|} nu^{U^{R -> V}}.
Terms with S_2 not inside N(b) vanish: nu^U depends on U only through s_b(U), which does not involve a link outside N(b), so a difference in such a link is zero.
Term S_2 = empty. It is int g dnu^U with g(v) = (D_S^V f)(U^{b -> v}). Split nu^U = pi_a + (pi_t - pi_a) (a = x s_b(U), t = beta s_b(U)). The first part is a probability measure: |int g dpi_a| <= sup|g| <= delta_S(f). The second has mass zero, norm at most eps by (B1), and |g(v) - g(v')| = |(D_b^v D_S^V f)(U^{b -> v'})| <= delta_{S union b}(f); Lemma 2.2 gives eps delta_{S union b}(f).
Terms with S_2 non-empty, inside N(b). lambda = (D_{S_2}^V nu)^U has mass zero (an alternating sum of 2^{|S_2|} measures of mass 1). g(v) = (theta_{S_2} D_{S_1}^V F)(U, v), S_1 = S minus S_2, satisfies |g(v) - g(v')| <= delta_{S_1 union b}(f). Lemma 2.2 gives [lambda] delta_{S_1 union b}(f). Bound of [lambda]: if S_2 = {c}, lambda = pi_{t'} - pi_t where s and s' differ only in the term w_p of the one plaquette p containing b and c (by (G2)), so |s' - s| <= 2; then Re lambda = (pi_{a'} - pi_a) + Re rho, Im lambda = Im rho with rho = (pi_{t'} - pi_{a'}) - (pi_t - pi_a), ||rho||_1 <= 2 eps, hence [lambda] <= c(x)/2 + 2 eps by (B2). If |S_2| >= 2, fix c_0 in S_2 and pair each R not containing c_0 with R union {c_0}: lambda is a signed sum of 2^{|S_2| - 1} differences nu^{U'} - nu^{U''} of configurations that differ only in the link c_0, each of norm at most c(x) + 2 eps by (B3). QED.

**Lemma 2.4 (contraction of a sweep).** Put, for w in (0, 1],
gamma(x, y, w) = eps/w + 18 (c(x)/2 + 2 eps) + (c(x) + 2 eps) ((1 + 2w)^{18} - 1 - 36 w)/(2w).
Let b_1, ..., b_n be an enumeration of all links and P = P_{b_n} ... P_{b_1} (P_{b_1} applied first). If gamma <= 1 then ||P f||_w <= gamma ||f||_w, and sup|P_b f - f| <= ||f||_w / (w (1 - eta)) for every link b.
Proof. Write m_S(f) = w^{|S|} delta_S(f), a vector indexed by the non-empty sets of links. Multiply Lemma 2.3 by w^{|S|}: for b not in S, m_S(P_b f) <= m_S(f) + sum_{S_2} kappa(S_2) m_{(S minus S_2) union b}(f) with kappa(S_2) = w^{|S_2| - 1} chat(S_2); and m_S(P_b f) = 0 for b in S. So m(P_b f) <= K_b m(f) coordinatewise, where K_b is the linear map with non-negative entries that sends the unit vector e_S to e_S if b is not in S, and e_{T union b} (T not containing b) to the sum over S_2 subset of N(b) minus T, with T union S_2 non-empty, of kappa(S_2) e_{T union S_2}. The total mass of the image of e_{T union b} is at most sum over all S_2 subset of N(b) of kappa(S_2) <= eps/w + 18 (c/2 + 2 eps) + sum_{j >= 2} binom(18, j) w^{j-1} 2^{j-1} (c + 2 eps) = gamma. Since the K_b have non-negative entries, m(P f) <= K_{b_n} ... K_{b_1} m(f). Follow a unit mass at a non-empty S through the sweep: the maps K_b with b not in S leave it at S; at the first link b_i of the enumeration that lies in S its total mass becomes at most gamma; every later map does not increase total mass (factor 1 or gamma <= 1). So the total mass of K_{b_n} ... K_{b_1} e_S is at most gamma, and summing, ||P f||_w <= gamma ||f||_w. The last claim: (P_b f - f)(U) = int (f(U^{b -> v}) - f(U)) nu^U(dv), of modulus at most ||nu^U||_1 delta_{b}(f) <= delta_b(f)/(1 - eta), and delta_b(f) <= ||f||_w / w. QED.

### 2.3 The region and the theorem

Region. R = {beta = x + iy : 6|y| < 1 and gamma(x, y, w) < 1 for some w in (0, 1]}. gamma is continuous, even in x and in y, and non-decreasing in |y|. R is open. On the real axis gamma(x, 0, w) -> 9 c(x) = 9 |x| Sigma(x) as w -> 0, so R contains the real interval I = {|x| < x_D}, where x_D is the root of 9 x sqrt(1 + 9 x^2 e^{6x}) = 1. Let T = R intersect {|Re beta| < x_D}. Each vertical line meets T in an interval symmetric about the real axis, so T deforms onto I and is simply connected.

Hand arithmetic for x_D > 1/10: at |x| <= 1/10, e^{0.6} < 1.83 (e^{0.5} < 1.6488, e^{0.1} < 1.1052), 9 x^2 e^{6|x|} < 0.1647, sqrt(1.1647) < 1.08 (1.08^2 = 1.1664), so c(x) < 0.108 and 9 c(x) < 0.972.
Explicit rectangle: for |x| <= 1/10, |y| <= 10^{-7}, w = 4 x 10^{-4}: eta <= 6 x 10^{-7}, eps <= 1.3 x 10^{-6}, eps/w <= 0.00325, 36 eps < 0.00005, ((1+u)^{18} - 1 - 18u)/u <= 153 u (1+u)^{16} with u = 2w = 8 x 10^{-4}, which is at most 153 x 0.0008 x e^{0.0128} < 0.1240, times (c + 2 eps) < 0.1081 gives < 0.0135. Sum: gamma < 0.972 + 0.00325 + 0.00005 + 0.0135 < 0.989.
So the closed rectangle Q = {|Re beta| <= 1/10, |Im beta| <= 10^{-7}} lies in T.
Wider at stronger coupling, same formula: for |x| <= 1/20, c(x) < 0.0508 and 9c < 0.457; with w = 0.01 and |y| <= 3 x 10^{-5} one gets eps < 3.7 x 10^{-4}, eps/w < 0.037, 36 eps < 0.014, 153 x 0.02 x e^{0.32} x 0.0516 < 0.218, sum < 0.73. So {|Re beta| <= 1/20, |Im beta| <= 3 x 10^{-5}} lies in T. The constants are not optimised; the width is set by eps/w against the pair terms.

**Theorem A.** Let (L, P) satisfy (G1), (G2). Then:
(1) For every beta in R and every f in C(Omega), P_beta^n f converges uniformly on Omega to a constant c(f, beta), locally uniformly in beta; c(f, .) is analytic on R, and c(f, beta) = mu_beta(f) for real beta in R.
(2) Z(beta) != 0 for every beta in T. In particular Z(k, B; beta) != 0 for every box B with free walls, every k >= 3, and every beta in Q.
(3) For beta in T: int f exp(-beta A) dU / Z(beta) = c(f, beta).
The region T and the constants do not depend on the lattice.

Proof. (1) Fix beta_0 in R and w with gamma(beta_0, w) < 1; by continuity there are a neighbourhood O of beta_0 and gamma_0 < 1 with gamma <= gamma_0 and eta <= eta_0 < 1 on O. For beta in O and f in C(Omega): by Lemma 2.4, ||P^n f||_w <= gamma_0^n ||f||_w, and sup|P^{n+1} f - P^n f| <= n_L ||P^n f||_w/(w(1 - eta_0)) (telescope over the n_L links of the sweep; the seminorm does not increase along the sweep because every K_b has total mass factor at most 1). So P^n f is uniformly Cauchy, uniformly in beta in O. The limit f_inf is continuous and delta_S(f_inf) = lim delta_S(P^n f) = 0 for all S, so f_inf is a constant c(f, beta). For fixed U, beta -> (P_b f_beta)(U) is analytic when f_beta is (it is int f_beta(U^{b -> v}) e^{beta <v, s>} dv / zeta(beta s) with zeta != 0 by (B1), jointly continuous, analytic in beta), so each (P^n f)(U) is analytic in beta on O, and the uniform limit c(f, .) is analytic. For real beta, mu_beta(f) = mu_beta(P^n f) -> c(f, beta).
(2) Put G(beta) = sum_p c(a_p, beta), analytic on T, and E(beta) = exp(-int_0^beta G), analytic on the simply connected T, never zero, E(0) = 1 = Z(0). On I, Z' = -mu_beta(A) Z = -G Z by (1), so (Z/E)' = 0 and Z = E on I. Z is entire and E is analytic on the connected T, so Z = E on T.
(3) Both sides are analytic on T (the left by (2)) and agree on I. QED.

**Corollary A1 (the real form on the base).** For every lattice with (G1), (G2), every real x with 10^{-7} <= x <= 1/10 - 10^{-7} and every j >= 1: |kappa_j(x)| <= 4 N x j! 10^{7j}; for boxes, |kappa_j(x)| <= 6 k |B| j! (10^7)^j (as 4x <= 1). (Proposition 0(i) with rho = 10^{-7}.) For 0 <= x < 10^{-7} the same with 4 N 10^{-7} in front.

**Corollary A2 (the item's statement, answer (i) of the stop rule).** With r_0 any number in (0, 1/10), beta_1 = 1/10, U = the interior of Q, n_min = 1, k_0 = 3: Z(k, B; beta) != 0 for all beta in U, all boxes with free walls, all k >= 3. With (TM_B) and (SC_B) (rows 681, 683; not proved here) Theorem ZB gives m_B(beta) >= kappa_0 omega_D(beta) > 0 for real beta < 1/10, uniformly in the box, for a domain D inside T joined to the strong-coupling disc (if r_0 of (SC_B) is small the disc lies inside T anyway; then D is a subdomain of T with the shape condition (TUBE), for instance a thin rectangle).

Remarks.
2.5.1 (complex couplings per plaquette). The proof uses beta only through t = sum_p beta_p w_p. With a separate complex coupling beta_p for each plaquette, all in the rectangle Q, every bound holds unchanged (|a| <= 6 max|x_p|, |y <v, s>| replaced by |sum_p y_p <v, w_p>| <= eta, |a' - a| <= 2 max |x_p|). So Z as a function of (beta_p) has no zero on the polyrectangle Q^P, for every lattice. By Cauchy's formula on polydiscs this bounds every truncated function <a_{p_1}; ...; a_{p_j}> at real couplings in the base; it does not by itself give decay in the distances.
2.5.2 (what the bound at real beta is). At y = 0, w -> 0 the condition is 9 c(x) < 1: Dobrushin's uniqueness condition for the one-link specification (18 neighbours, each of influence at most c(x)/2 in total-variation distance). So on [0, x_D) the Gibbs state is unique and local functions decay exponentially; the theorem adds the uniform complex tube.
2.5.3 (tests). U(1) and Z_2: the same proof gives a tube over a small interval at strong coupling and nothing near their transitions, as it must (the contraction is lost before the transition). The fundamental-adjoint action: (G1), (G2) and a one-link bound of the same kind hold at small couplings only. No conflict with the tests K5 to K7 of the plan.
2.5.4 (not claimed). I did not check the literature for the best explicit strong-coupling interval on which a gap is proved; "above 1/12" is the plan's criterion (3.1, result 5), and I take it from there.

**Status of step (a): done, by hand, with explicit U and beta_1 = 1/10.** What a checker should attack first: the Leibniz formula and the vanishing-mass claims in Lemma 2.3; the mass-transport argument of Lemma 2.4 (in particular that a term landing on the empty set is simply dropped, which is correct because the seminorm has no empty-set coordinate); the variance bound in (B2).

### 2.6 A volume-free bound on complex expectations, and the follow-up statement on the base

**Corollary A3.** Let beta be in R, w with gamma = gamma(beta, w) < 1, eta = 6|Im beta|. For every f in C(Omega) and every U:
|c(f, beta) - f(U)| <= ||f||_w / (w (1 - eta)(1 - gamma)^2),
with no dependence on the lattice. If f depends on n_f links only, ||f||_w <= ((1 + 2w)^{n_f} - 1) sup|f|.
Proof. In one sweep, write g_0 = g, g_i = P_{b_i} g_{i-1}. sup|g_i - g_{i-1}| <= delta_{b_i}(g_{i-1})/(1 - eta) <= a_i/(w(1 - eta)), where a_i is the mass that the majorant vector M_{i-1} = K_{b_{i-1}} ... K_{b_1} m(g) carries on sets containing b_i. The map K_{b_i} removes that mass and puts back at most gamma a_i, so |M_i| <= |M_{i-1}| - (1 - gamma) a_i, and sum_i a_i <= |M_0|/(1 - gamma) = ||g||_w/(1 - gamma). So sup|P g - g| <= ||g||_w/(w(1 - eta)(1 - gamma)). Sum over the sweeps with ||P^n f||_w <= gamma^n ||f||_w. The last claim: delta_S(f) = 0 unless S lies in the support, and delta_S <= 2^{|S|} sup|f|. QED.

On the rectangle Q with w = 4 x 10^{-4} (gamma < 0.989): |c(f, beta)| <= sup|f| + 2.1 x 10^7 ||f||_w.

**Corollary A4 (the statement of the follow-up `gap-zf-box-x-2`, on the base).** For every lattice with (G1), (G2), every real x with |x| <= 1/10 - 10^{-7}, and every continuous F that depends on n_F links:
|sum_p <F; a_p>_x| = |d/dx mu_x(F)| <= 10^7 (1 + 2.1 x 10^7 ((1.0008)^{n_F} - 1)) sup|F|.
Proof. mu_x(F) = c(F, x), analytic on T, bounded on Q by Corollary A3; Cauchy's estimate on the disc of radius 10^{-7}. QED.
So on the base the response of a local observable to the coupling is bounded uniformly in the volume, with a constant that does not involve the correlation length. This is the statement that the plan's follow-up asks for; it is proved here only where the one-link contraction holds.

## 3. Step (b): the continuation

### 3.1 What a continuation needs, stated exactly

Notation. For real x put m(x) = inf over all boxes B (sides >= n_min) of the gap m_B(x) of the transfer operator, and mu(x) = inf_{s in [x_0, x]} m(s). The plan's step (b) reads: "from decay with length xi at a real coupling, a zero-free disc of radius c min(1, xi^{-4})". Theorem ZB turns a zero-free domain into a lower bound for m. To close the loop the decay that feeds the disc must be the decay that Theorem ZB produces. So the loop needs this statement:

**(H_p), the continuation hypothesis.** There are c > 0 and p >= 1 such that for every real x in [x_0, X] with mu(x) > 0, every box B with free walls and every k >= k_0(B): Z(k, B; .) has no zero in the disc |beta - x| < r(x) := c min(1, mu(x))^p.

It is the conjunction of two statements of different kinds:
(H-a) (strong mixing gives a disc) if at real x the influence of a boundary link on a block of side l decays like exp(-dist/xi), uniformly in the block and in the boundary configuration, then all Z are zero-free in a disc of radius c xi^{-p};
(H-b) (free-box gap gives strong mixing) a common gap m of the transfer operators of all boxes with free walls gives the decay of (H-a) with xi <= C/m.

### 3.2 The differential inequality, proved as an implication

**Theorem ZB-chain (Theorem ZB along a chain of discs; no shape condition, no global domain).** Assume (TM_B) and (SC_B) with constants r_0, C_0, kappa_0 (for |beta| <= 2 r_0, k >= 4, q >= 1: |g_q| <= C_0 |B| k exp(-kappa_0 k), g_q = log Z(k, B; .) - (1/q) log Z(qk, B; .)). Let x_0' = r_0 < x_1 < ... < x_n be real points and rho_0 >= rho_1 >= ... >= rho_n > 0 radii with rho_0 <= r_0 and x_{i+1} = x_i + rho_i/2. Assume Z(k', B; .) has no zero in each open disc |beta - x_i| < rho_i, for all k' >= k_0. Then for every real y with |y - x_n| <= 3 rho_n/4:
m_B(y) >= kappa_0 omega_*^{n+1}, omega_* = log(7/6)/log(7/2) (about 0.123).
Proof. Step 1 (bound). Fix k >= max(k_0, 4) and q. On the disc D_i = {|beta - x_i| < rho_i} (it lies in Re beta > 0 since rho_i <= r_0 <= x_i) the function L = log Z(k', B; .) is analytic, Re L = log|Z| <= log Z(k', B; Re beta) <= 0, and L(x_i) is real, in [-2 N' x_i, 0], N' <= 6 k' |B|. By the coefficient bound in the proof of Proposition 0(i) (with A_0 = 0), |L(beta) - L(x_i)| <= 2 (2 N' x_i) sum_{j>=1} (7/8)^j = 28 N' x_i for |beta - x_i| <= 7 rho_i/8. So |L| <= 30 N' x_i there. Apply it to k' = k and to k' = qk divided by q: |g_q| <= M := 360 k |B| x_n on every closed disc |beta - x_i| <= 7 rho_i/8, uniformly in q.
Step 2 (induction along the chain). Claim: |g_q| <= M (e_k/M)^{omega_*^i} on |beta - x_i| <= rho_i/4, where e_k = C_0 |B| k exp(-kappa_0 k) (take k so large that e_k < M). For i = 0 the disc |beta - r_0| <= rho_0/4 lies in |beta| <= 2 r_0; (SC_B). Step from i to i+1: on the annulus rho_i/4 < |z - x_i| < 7 rho_i/8, Theorem LP (two constants) gives |g_q(z)| <= e^{omega(z)} M^{1 - omega(z)} with e the bound on the inner circle and omega(z) = log((7 rho_i/8)/|z - x_i|)/log(7/2). A point z with |z - x_{i+1}| <= rho_{i+1}/4 has |z - x_i| <= rho_i/2 + rho_{i+1}/4 <= 3 rho_i/4, so either it is in the inner disc or omega(z) >= omega_*; in both cases |g_q(z)| <= M (e/M)^{omega_*}. The same step gives the bound M (e_k/M)^{omega_*^{n+1}} at every real y with |y - x_n| <= 3 rho_n/4.
Step 3. As in steps 3, 4 of Theorem ZB: for real y, g_q(y) -> log(1 + s_k(y)) as q -> infinity, exp(-k m_B) <= s_k, so with omega = omega_*^{n+1}: m_B(y) >= kappa_0 omega - (1/k) log(2 M^{1 - omega} (C_0 |B| k)^{omega}) for large k; let k -> infinity. QED.

**Corollary 3.2 (gap from a radius function).** Let r be a positive non-increasing function on [r_0, X] with r <= r_0, such that for every x in [r_0, X] no Z(k', B; .), k' >= k_0(B), vanishes in |beta - x| < r(x). Then for every y in [r_0, X] and every box: m_B(y) >= kappa_0 exp(-Lambda (2 int_{r_0}^y ds/r(s) + 1)), Lambda = log(1/omega_*) < 2.1.
Proof. Chain x_{i+1} = x_i + r(x_i)/2, rho_i = r(x_i), stopped at the first n with y <= x_n + r(x_n)/2. Each completed step has int_{x_i}^{x_{i+1}} ds/r >= (r(x_i)/2)/r(x_i) = 1/2 because r is non-increasing, so n <= 2 int_{r_0}^y ds/r. QED.

**Corollary 3.3 (the base, given the two routine inputs).** With (TM_B), (SC_B) and Theorem A (r = r_b := min(r_0, 10^{-7}) on [r_0, 1/10 - 10^{-7}]): for every box with free walls and every real y in [r_0, 1/10 - 10^{-7}], m_B(y) >= kappa_0 exp(-2.1 (2 (y - r_0)/r_b + 1)) > 0. The number is astronomically small; it is a uniform gap, not a useful one. (Dobrushin's condition at real beta gives a far better rate directly; see 2.5.2. The point of the complex tube is only that it is the object the transport uses.)

**(H_p), exact form.** Fix x_0 in [r_0, 1/10 - 10^{-7}], X > x_0, c > 0, p >= 1. For x in [x_0, X] put r(x) = min(r_b, c min(1, mu(x))^p). Hypothesis: for every x in [x_0, X] with mu(x) > 0, every box and every k' >= k_0(B), Z(k', B; .) has no zero in |beta - x| < r(x).

**Proposition B (the continuation, and where it ends).** Assume (TM_B), (SC_B) and (H_p) on [x_0, X]. Put kappa_1 = kappa_0 exp(-Lambda (2 (x_0 - r_0)/r_b + 1)) and assume (shrinking c) c kappa_1^p <= r_b and kappa_1 <= 1. Then
mu(x)^p >= kappa_1^p - (2 Lambda p / c)(x - x_0) for x_0 <= x < x_reach := min(X, x_0 + c kappa_1^p/(2 Lambda p)),
and in particular every box has a gap on [x_0, x_reach). In differential form: d(mu^p)/d beta >= -2 Lambda p/c. Nothing is obtained beyond x_reach.
Proof. Let x* = sup{x in [x_0, X] : mu(x) > 0}; mu(x_0) = m(x_0) >= kappa_1 > 0 by Corollary 3.3. For x < x*, r is positive and non-increasing on [r_0, x] (r = r_b on [r_0, x_0]), so Corollary 3.2 gives m(x) >= kappa_1 exp(-2 Lambda phi(x)), phi(x) = int_{x_0}^x ds/r(s). The right side is non-increasing in x, so mu(x) >= kappa_1 exp(-2 Lambda phi(x)). Then r(s) >= c kappa_1^p exp(-2 Lambda p phi(s)) (this is at most r_b by the choice of c), so phi' = 1/r <= exp(2 Lambda p phi)/(c kappa_1^p) almost everywhere, that is (exp(-2 Lambda p phi))' >= -2 Lambda p/(c kappa_1^p). Integrating, exp(-2 Lambda p phi(x)) >= 1 - 2 Lambda p (x - x_0)/(c kappa_1^p), and mu(x)^p >= kappa_1^p exp(-2 Lambda p phi(x)) gives the bound for x < x*. If x* < x_reach, then on [x_0, x*) mu is bounded below by a positive mu_* and r by r_* = c mu_*^p; apply Theorem ZB-chain with the constant radius rho_i = r_* (allowed: r_* <= r(x_i) <= r_0 for chain points below x*, and the smaller discs are zero-free) and let x_n be the last chain point below x*, so x_n >= x* - r_*/2; every y in [x*, x* + r_*/4] has |y - x_n| <= 3 r_*/4, so m(y) >= kappa_0 omega_*^{n+1} > 0 uniformly in the box there, and mu(y) > 0 beyond x*: a contradiction with the definition of x*. QED.

So the brief's expectation is confirmed in this exact form: under the hypothesis that a gap m buys a zero-free disc of radius c m^p, the transport gives a linear lower bound for m^p that reaches zero at the finite coupling x_0 + c kappa_1^p/(2 Lambda p). The bound is consistent with a transition there and proves nothing beyond it. The largest coupling reached unconditionally is the base, 1/10.

### 3.3 The named lemma (H_p): three ways that failed

Neither half of (H_p) is proved here. (H-a) is the continuous-spin form of the Dobrushin-Shlosman theorem (strong mixing gives analyticity; recalled, `unchecked`) and I judge it provable. (H-b) is not a known theorem and is the real obstruction: Theorem ZB returns a spectral gap of the boxes with free walls, which is decay in the time direction for one boundary condition, and the zero-free disc needs decay of the influence of every boundary configuration on every block.

Way 1: iterate the one-link inequality beyond the base. Lemma 2.3 holds at every beta. At real beta the transport maps K_b have total mass factor 9 c(x) on the first level, which exceeds 1 for x > x_D (about 0.102 with the bounds of Lemma 2.1). The majorant then grows like (9 c)^n over n sweeps, while the true heat-bath dynamics may still contract: an inequality between suprema of oscillations cannot see the cancellations that mixing consists of. Exact failure: there is no norm of this type in which P_b is non-expansive unless the one-link Dobrushin sum is below 1.
Way 2: block heat bath in place of one-link heat bath. The Leibniz formula and the pairing lemma extend to a block Lambda (pair a mass-zero measure on G^Lambda with sum_{b in Lambda} delta_b). The complex perturbation costs eps_Lambda of order |y| times the number of plaquettes of the block, which is the source of a radius l^{-4}. Two failures. (i) The first-level coefficients are the transport distances between block measures for boundary configurations that differ in one link, uniformly in the configuration: this is the hypothesis of (H-a), and (H-b) would have to supply it. (ii) Even with it, a set of links that meets the block in one link near the block's boundary has transport factor of order 9 c(x) > 1; contraction holds only on average over translates of the block, and the average over sets of two or more links needs bounds on mixed (two-link) influences, with weights that force w of order l^{-6} and a radius of order l^{-10} by the crude count. I did not carry this out; it would prove (H-a) with p = 10 at best, and it does not touch (H-b).
Way 3: perturb the real n-sweep operator. If P_x^n contracts at real x, write P_beta^n as P_x^n plus insertions of P_b^beta - P_b^x. Each insertion is bounded by (eps/w)(1 + 2w)^{18} times the mass on sets containing b, and the sum over b of these masses is sum_S |S| m_S(f), which is not bounded by ||f||_w: a factor equal to the number of links appears (the 1/volume width of plan 1.7, point 3, in another form). It can be traded for a loss in the weight w at each order (sum_S |S| w^{|S|} delta_S <= C(w, w') ||f||_{w'} for w < w'), but that needs the real dynamics to contract in the whole scale of mixed-oscillation norms, uniformly in the volume. No decay statement that Theorem ZB returns gives this.
(The plan's own three ways for the periodic statement, 1.7 points 2 to 4, are different from these and are not repeated.)

Consistency test of (H_p), recalled and `unchecked`: for the Ising model at low temperature in a field h > 0, the zeros in h lie on the imaginary axis (Lee and Yang), so the zero-free radius at real h is h; the gap of a box with free walls of volume V is of order h V for small boxes, so inf over boxes with sides >= n_min is of order h. There (H_p) holds with p = 1 and both sides vanish together at the transition. I know no example with a uniform free-box gap and zeros that approach the real axis, and no theorem that excludes one.

## 4. Step (c): an identity for the insertion of the total action

Let Delta = sum_b Delta_b be the Laplacian of (S^3)^L and Lgen = Delta - beta grad A . grad the generator of the Langevin dynamics, symmetric in L^2(mu_beta), with <F Lgen H> = -<grad F . grad H>.

**Lemma 4.1 (exact).** (i) Delta A = 12 (N - A). (ii) |grad_b A|^2 = |s_b|^2 - <U_b, s_b>^2 =: q_b, and with Q = sum_b q_b: Lgen A = 12 (N - A) - beta Q. (iii) For every smooth F:
<F; A> = (1/12) <grad F . grad A> - (beta/12) <F; Q>, and 12 (N - <A>) = beta <Q>.
Proof. (i) As a function of v = U_b, a_p = 1 - <v, w_p> is a constant minus a linear function restricted to S^3, an eigenfunction of the Laplace-Beltrami operator with eigenvalue -3; so Delta_b a_p = 3 (1 - a_p), and each plaquette has four links. (ii) The gradient on the sphere of -<v, s> is minus the tangential part of s, of squared length |s|^2 - <v, s>^2. (iii) <F Lgen A> = -<grad F . grad A> and <Lgen A> = 0; insert (ii). QED.

What it gives and where it stops. The identity turns the insertion of A into a local term (grad F . grad A is supported on the links of F) plus the insertion of another extensive quantity Q, a sum over links of products of two plaquettes at that link. Iterating (Lgen Q brings in grad Q . grad A, and so on) gives a hierarchy that closes only as a series in beta: it is the strong-coupling expansion of the solution Phi of -Lgen Phi = A - <A>, for which <F; A> = <grad F . grad Phi> exactly (first term Phi = A/12). So in the crossing region the identity does not replace a bound. What it does is name the bound that would: 

**(HS-sup).** For real beta in the range in question there is C, independent of the lattice, such that the solution of -Lgen Phi = A - <A> satisfies sup_U |grad_b Phi(U)| <= C for every link b.
(HS-sup) implies |<F; A>| <= C sum_b <|grad_b F|> for every smooth F, which is the follow-up statement with a constant independent of the correlation length. Status: on the base it holds in the integrated form of Corollary A4; from Ric + beta Hess A >= 2 - 30 beta (plan 1.4) one gets only the L^2 bound <|grad Phi|^2> <= <|grad A|^2>/(2 - 30 beta)^2, which is of order N and useless for a local F; a pointwise bound needs a maximum principle for the operator on 1-forms, that is diagonal dominance of beta Hess A against Ric, which is again a one-link condition of Dobrushin type (beta of order 1/10). Beyond that no handle. I did not find an identity that closes in the crossing region; the dilation identity of the scaling region has no analogue here because A is an eigenfunction of Delta only (Lemma 4.1(i)), not of Lgen.

## 5. Status block

Provenance: written by Claude Fable 5.2 (medium) in one session at commit d76689eed; not checked by another model; every proof here is by hand and none rests on a computation. No numerical job was run (none was needed; no claim below is numerical evidence). Literature recollections are marked `unchecked` and are not used in proofs.

**Proved here (label: proved, unchecked by a second model).**
1. Proposition 0: the real form (factorial bounds on the cumulants of the action) is equivalent to a uniform zero-free neighbourhood, with constants (rho -> C = max(1, 4 max(beta_1, rho))/rho; C -> rho = 1/C); the extensive prefactor is automatic.
2. Theorem A (step (a), the base, answer (i) of the stop rule): for every lattice with at most 6 plaquettes per link and at most one common plaquette per pair of links (every box with free walls, k >= 3, every size; also periodic tori with sides >= 3), Z(beta) != 0 on the rectangle |Re beta| <= 1/10, |Im beta| <= 10^{-7}, and on the region T of 2.3 (for example |Re beta| <= 1/20, |Im beta| <= 3 x 10^{-5}). So the item's statement holds with beta_1 = 1/10, U the interior of that rectangle, n_min = 1, k_0 = 3. Method: contraction of the complex one-link heat-bath kernels in a norm of mixed oscillations (Lemmas 2.1 to 2.4). It also holds with a separate complex coupling on each plaquette (Remark 2.5.1).
3. Corollaries A1 (cumulants: |kappa_j| <= 6 k |B| j! 10^{7j} on the base), A3 (complex expectations of local functions bounded uniformly in the volume on T), A4 (the statement of the follow-up `gap-zf-box-x-2`, |sum_p <F; a_p>| <= C sup|F| with C independent of the volume, on the base).
4. Theorem ZB-chain and Corollaries 3.2, 3.3: Theorem ZB along a chain of discs, with no shape condition and no global domain; given (TM_B) and (SC_B) it gives a common gap of all boxes on [r_0, 1/10).
5. Proposition B (step (b)): under the hypothesis (H_p) that a common gap mu buys a zero-free disc of radius c mu^p, the transport gives mu^p >= kappa_1^p - (2 Lambda p/c)(x - x_0), that is d(mu^p)/dbeta >= -2 Lambda p/c, and the continuation ends at x_0 + c kappa_1^p/(2 Lambda p).
6. Lemma 4.1 (step (c)): the exact identity <F; A> = (1/12)<grad F . grad A> - (beta/12)<F; Q>.

**Not proved, open.**
- The inputs (TM_B), (SC_B) (rows 681, 683). Items 4 and 5 above are implications from them; items 1 to 3 and 6 do not use them.
- (H_p), in both halves (3.1). Three ways failed for it (3.3): iterating the one-link inequality past the Dobrushin threshold; the block heat bath (needs influence bounds uniform in the boundary configuration, which a free-box gap does not give, and pair-influence bounds); perturbing the real n-sweep (a factor equal to the volume, or a scale of norms in which the real dynamics is not known to contract).
- Any zero-free neighbourhood of a real coupling above x_D (about 0.102 with the constants of Lemma 2.1; the method's limit is the one-link Dobrushin threshold, which sharper one-link bounds would move by a bounded factor, not to the crossing region near beta = 2).
- No transition was found or proved, and no counterexample. The tests U(1), Z_2 and the adjoint end point are respected (2.5.3).
- Whether beta_1 = 1/10 improves on the literature's explicit strong-coupling intervals was not checked.

**For the checker, in order.** Lemma 2.3 (Leibniz formula for mixed differences of P_b f; the mass-zero pairing; the bound of [lambda] for one link). Lemma 2.4 (mass transport through a sweep). (B2) (the variance bound 1/4 + kappa^2 e^kappa/16). Theorem A(2) (identity-theorem step). Theorem ZB-chain step 2 (the constant omega_*). Proposition B (the choice of c and the end-point argument).

**The one exact next statement.** By Proposition B no hypothesis in which the zero-free radius shrinks with the gap can cross a region; what is needed is a radius that does not depend on the correlation length. In its real, local form (Section 4):
(HS-sup on an interval) For some explicit beta_2 > 1/10 and every real beta in [1/10, beta_2] there is C, independent of the lattice, such that the solution Phi of -Lgen Phi = A - <A> has sup_U |grad_b Phi(U)| <= C for every link b; equivalently in consequence, |sum_p <F; a_p>| <= C sum_b sup|grad_b F| for every smooth F. Prove it, or give a family of lattices and observables on which it fails. (This is the brief's follow-up `gap-zf-box-x-2`; this run proves its integrated form on [0, 1/10) only, Corollary A4. A first concrete target: a block form of Lemma 2.3 for the 4 links of one plaquette, or for the 6 links of a time-like star, verified by hand, to move the threshold above x_D.)
