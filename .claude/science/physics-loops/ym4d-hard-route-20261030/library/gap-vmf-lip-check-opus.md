# Check of library/gap-vmf-lip.md (FINISH row 790), by Claude Opus 5.5, line by line

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit read: `a9ac34ca1`.
- Target: `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-vmf-lip.md` (609 lines, Codex gpt-6-astra max, written as FINISH row 785). Read in full.
- Context read: `gap-crux-fp.md` Sections 4.2 and 4.2b (Identity L, Proposition TW, (AS-bg), Lemma P, R-a, R-b); `gap-mid-max.md` Sections 6 (Identity FL), 8 (Lemma M, Proposition MIX) and 10 (Lemma DC, Lemma INF, Theorem DOB); `gap-mid-check.md` Sections 5 to 8; `gap-seed-shape.md` Sections 1.4, 1.5 and 2 (Theorem SH, the r = 2 and r = 4 lines, Theorem D-shape), with the row 707 lead note.
- Method: every identity re-derived by hand. No numerical run was made (numpy is not installed on this machine; none was needed). No repository file was edited.
- This is one reading by a model of a different provider from the author (Codex). It is not an audit.

## 1. Theorem V (lines 57-190)

**(1) Normalisations. HOLDS.** sigma is the uniform probability, so sigma = dS/|S^3| with |S^3| = 2 pi^2. By rotation invariance the integral of e^{F.h} against sigma is z(|F|), so mu_F is a probability law. S_k = |S^3| z(k). The vector divergence theorem for the scalar f = e^{F.x} is: the integral over the sphere of f n dS equals the integral over B of grad f = F e^{F.x}. With n = h this is line 93. Then E_F h = (1/(|S^3| z(k))) times F V_k = F V_k/S_k. Rotation about u and the reflection h_v -> -h_v (v perpendicular to u) give E_F h = E_F(h.u) u = (z'(k)/z(k)) u. Comparing, k V_k/S_k = z'(k)/z(k), so V_k/S_k = a(k) and E_F h = a(k) k u = a(k) F. The limit a(0) = 1/4 holds: z(k) = 1 + k^2/8 + O(k^4), because E_0 h_1^2 = 1/4.

**(2) The field. HOLDS.** z(k|x|) is the integral of e^{k x.h} d sigma(h), by rotation; this is entire in x, so b, w, V are smooth on the closed ball. The Laplacian in x of e^{k x.h} is k^2 |h|^2 e^{k x.h} = k^2 e^{k x.h}, so Delta b = k^2 b. On the sphere b = 1, so w = 0. Then (-Delta + k^2) w = (Delta b + k^2 - k^2 b)/k^2 = 1. For the divergence: div(e^{F.x} V) = e^{F.x} (F.V + div V), with F.V = -F.grad w + k^2 w and div V = -Delta w + F.grad w. The two F.grad w terms cancel and the sum is e^{F.x}(-Delta w + k^2 w) = e^{F.x}. The radial derivative: d_r w = -k z'(kr)/(k^2 z(k)) = -z'(kr)/(k z(k)), so at r = 1 it is -a(k). On the sphere w = 0, so V(h) = -grad w(h) = a(k) h and V(h).h = a(k).

**(3) Normal flux. HOLDS.** div J_e = (F.e) e^{F.x} - (F.e) div(e^{F.x} V) = 0 by (2). On the sphere, J_e(h).h = e^{F.h}(h.e - (F.e) a(k)), which is (3).

**(4) Covariance identity. HOLDS, every constant checked.** By (1), E_F(h.e) = a F.e, so Cov(phi, h.e) = E_F[phi (h.e - a F.e)] = (1/S_k) times the sphere integral of Phi J_e.h dS. The divergence theorem for Phi J_e (C^1 on the closed ball) and div J_e = 0 give the ball integral of grad Phi . J_e = V_k times the nu_F-mean of grad Phi . M e. The factor is V_k/S_k = a(k). This is (4).

**(5) M(rh)e. HOLDS.** At x = rh, s = kr: -grad w = (z'(s)/(k z(k))) h and F w = u (1 - b)/k, with b = z(s)/z(k). With F.e = kc: (F.e) V = c[(z'(s)/z(k)) h + (1 - b) u] = c[m(s) b h + u - b u], since z'(s)/z(k) = m(s) b. So M e = e - c u + c b u - c b m h = e_perp + c b (u - m h). This is (5). (Notation: "b(r)" means b at |x| = r; harmless.)

**(6) Conditional law and the bound 1. HOLDS.** In polar coordinates dx = r^3 dr dS(h), so given r the density of h with respect to sigma is proportional to e^{s u.h}: the law mu_{su}, and E(h | r) = m(s) u. Expand |Me|^2 = |e_perp|^2 - 2 c b m (e_perp.h) + c^2 b^2 (1 - 2 m u.h + m^2). The conditional means are E(e_perp.h | r) = m e_perp.u = 0 and E(u.h | r) = m. So the conditional mean is |e_perp|^2 + c^2 b^2 (1 - m^2). Signs: m(s) = E_{mu_{su}}(h.u) lies in [0, 1] for s >= 0, so 0 <= 1 - m^2 <= 1. z(s) is the sigma-mean of cosh(s h_1) (symmetry h -> -h), and cosh(s h_1) is non-decreasing in s >= 0 for each h; so 0 < b(r) = z(kr)/z(k) <= 1 for r <= 1. Hence the mean is at most |e_perp|^2 + c^2 = 1. Cauchy-Schwarz gives E_nu|Me| <= 1, and (4) gives |Cov| <= a(k) sup|grad Phi| E_nu|Me| <= a(k) when |grad Phi| <= 1.

**Extension and smoothing. HOLDS.** Phi(x) = inf_h {phi(h) + |x - h|} is finite (phi is continuous on a compact set) and 1-Lipschitz (an infimum of 1-Lipschitz functions). On the sphere, Phi(h') <= phi(h'), and phi(h) + |h' - h| >= phi(h') by the chord hypothesis, so Phi = phi there. Mollification gives Phi_eps smooth, 1-Lipschitz, so |grad Phi_eps| <= 1, and |Phi_eps - Phi| <= eps. Apply (4) to the trace phi_eps of Phi_eps (Phi_eps is its own smooth extension): |Cov(phi_eps, h.e)| <= a(k). Then |Cov(phi_eps - phi, h.e)| <= eps E|h.e - E h.e| <= 2 eps, which tends to 0. The bound passes to phi. No boundary derivative of a harmonic extension is used.

**Sharpness and a(k) = E_F h_v^2 <= 1/4. HOLDS.** Let R_theta rotate the (u, v) plane. The sigma-integral of (R_theta h)_v e^{k (R_theta h)_u} does not depend on theta. Its theta-derivative at 0 is the integral of (h_u - k h_v^2) e^{k h_u}, so E_F h_u = k E_F h_v^2, and a(k) = (z'/z)/k = E_F h_v^2. Lemma P (its value part: E_F(t^2) is non-decreasing in kappa, equal to 1/4 at 0, so E_F h_v^2 = (1 - E_F t^2)/3 <= 1/4) gives a(k) <= 1/4. I re-derived the monotonicity: Cov_kappa(t^2, t) = (1/2) E[(t - t')^2 (t + t')], and pairing (t, t') with (-t, -t') against the even base law gives a positive multiple of the integral of (t - t')^2 (t + t') sinh(kappa (t + t')) >= 0. Attainment: e = v, phi = h_v (chord-Lipschitz), Cov = Var(h_v) = E h_v^2 = a(k), since E h_v = 0. The case F = 0 is Lemma P with every e orthogonal to F, bound 1/4 = a(0). So the supremum over e and phi is a(|F|), and the radius restriction is not needed.

**Verdict, Theorem V: HOLDS** (all six parts, the extension, and sharpness). No correction.

## 2. Corollary V1 (lines 209-220)

mu_{F_t}(psi) is the ratio of two sigma-integrals of smooth functions of t, with bounded integrands (psi is Lipschitz on a compact set, so bounded). Differentiation under the integral is legitimate. With G = F' - F, the derivative is E(psi h.G) - E(psi) E(h.G) = Cov_{F_t}(psi, h.G) = |G| Cov_{F_t}(psi, h.G/|G|). By (V) its absolute value is at most |G| a(|F_t|) <= |G|/4. Integrating over [0, 1] and taking the supremum over psi with chord-Lipschitz constant at most 1 gives (7). F = F' is trivial. The duality remark (line 206) is not used.

**Verdict: HOLDS.** (It even gives the sharper |G| times the integral of a(|F_t|) dt; not needed.)

## 3. Lemma DC, chord form (lines 222-313)

**Convention.** C_ij bounds the change of the kernel at i when the coordinate j changes. The hypothesis is on row sums: max_i sum_j C_ij <= alpha < 1.

**(9). HOLDS.** delta_i(Gamma_i g) = 0, since Gamma_i g does not depend on w_i. For w, w' that differ at j only (j not i), the split is: the integral of g(xi, w) - g(xi, w') against gamma_i(.|w), at most delta_j(g)|w_j - w'_j|; plus the integral of xi -> g(xi, w'_{not i}) against gamma_i(.|w) - gamma_i(.|w'). That function has chord-Lipschitz constant at most delta_i(g), so by (8) the second term is at most delta_i(g) C_ij |w_j - w'_j| (if delta_i(g) = 0 the term is 0). Measurability of Gamma_i g follows from the measurable kernel, and continuity from the coordinate Lipschitz bounds (finite sum).

**The averaged update and the orientation of R. HOLDS.** delta_j of an average is at most the average of the delta_j. The i = j term contributes 0, so
delta_j(Pg) <= N^{-1}[(N - 1) delta_j(g) + sum_i C_ij delta_i(g)] = sum_i R_ij delta_i(g) = (R^T delta(g))_j,
with R = (1 - 1/N) I + C/N. The orientation is right. **Is "row sums of R at most q" enough? Yes.** For non-negative vectors, Delta(Pg) = sum_j (R^T delta)_j = sum_i delta_i (sum_j R_ij) <= (max_i row sum of R) Delta(g). The l^1 operator norm of R^T is the maximum column sum of R^T, which is the maximum row sum of R. The row sum at i is 1 - 1/N + (1/N) sum_j C_ij <= 1 - (1 - alpha)/N = q. Iteration needs only that R^T is entrywise non-negative, so delta(P^t f) <= (R^T)^t delta(f) and Delta(P^t f) <= q^t Delta(f).

**(10), oscillation with chord diameter 2. HOLDS.** Changing one coordinate changes g by at most delta_i(g) |w_i - w'_i| <= 2 delta_i(g); one coordinate at a time gives osc(g) <= 2 Delta(g). mu(Gamma_i g) = mu(g) because gamma_i is a version of mu's conditional law at i, so mu(P^t f) = mu(f). The value mu(f) lies between inf and sup of P^t f, so sup|P^t f - mu(f)| <= osc(P^t f) <= 2 q^t Delta(f), which tends to 0.

**(11). HOLDS.** mu~(g - Pg) = N^{-1} sum_i mu~(Gamma~_i g - Gamma_i g), using mu~(Gamma~_i g) = mu~(g). Off D the integrand vanishes mu~-almost surely. On D, Gamma~_i g(w) - Gamma_i g(w) is the difference of two probability means of xi -> g(xi, w_{not i}), whose oscillation is at most 2 delta_i(g). This gives (11), with the factor 2 from the chord diameter, not a total-variation constant.

**Telescoping. HOLDS.** mu~(f) - mu~(P^T f) = sum_{t < T} mu~(P^t f - P^{t+1} f). Each term is at most (2/N) sum_{j in D} delta_j(P^t f) <= (2/N) sum_{j in D} ((R^T)^t delta(f))_j. mu~(P^T f) tends to mu(f) by uniform convergence. Rewriting, ((R^T)^t delta)_j = sum_i (R^t)_ij delta_i, so the bound is 2 sum_i delta_i(f) sum_{j in D} (N^{-1} sum_t R^t)_ij.

**The identity N^{-1} sum_t R^t = (I - C)^{-1} = sum_n C^n. HOLDS.** R and C are non-negative with maximum row sums q < 1 and alpha < 1, so both Neumann series converge in the max-row-sum norm. I - R = I - (1 - 1/N) I - C/N = (I - C)/N, so sum_t R^t = (I - R)^{-1} = N (I - C)^{-1}.

**Second inequality. HOLDS.** (C^n)_ij > 0 requires a chain i = i_0, ..., i_n = j with each C_{i_k i_{k+1}} > 0, so the graph distance is at most n; for i in the support and j in D this forces n >= d. Row sums of C^n are at most alpha^n. So sum_{j in D} (sum_n C^n)_ij <= sum_{n >= d} alpha^n = alpha^d/(1 - alpha). The edge cases (empty support, no path, alpha = 0 with alpha^0 = 1) are as stated.

**Verdict, Lemma DC chord form: HOLDS.** No correction. The averaged update removes the need for the mass accounting that `gap-mid-check.md` had to add to the cyclic proof (fact (c), Step 3). The bound is monotone in alpha, which the applications use.

## 4. Lemma INF, chord form (lines 315-350)

**Isometries. HOLDS.** For unit quaternions, (1/2) tr g = Re g, and Re(p conj(q)) = p.q (the Euclidean inner product of R^4). Left and right multiplication by a unit quaternion preserve |.|, and inversion is conjugation, which is an isometry. I did not reread `gap-transfer.md` N.1-N.2; the facts used are the ones above.

**Layer model, (12). HOLDS.** y_b = Re(h_x v_b h_y^{-1} u_b^{-1}) = h_x . (u_b h_y v_b^{-1}), since conj(v h^{-1} u^{-1}) = u h v^{-1}. So y_b = h_x . O_b h_y with O_b orthogonal and fixed by the background. If x is the end point of b, cyclic order and Re(g) = Re(g^{-1}) give the same form. The one-site density at x is proportional to exp(beta sum_b J_b y_b) (the constants -beta cancel), so the law is mu_F with F = beta sum_b J_b O_b h_{y_b}. With |J_b| <= 1 and |O_b h| = 1, |F| <= 6 beta. With sides at least 3, the six neighbours are distinct and each shares one bond with x, so a change of h_y changes one term of F, by at most beta |h_y - h'_y|. By (7), C_xy <= beta/4, and C_xy = 0 for non-neighbours (the kernel depends on the neighbours only). Row sum 6 beta/4 = 3 beta/2.

**Gauge measure, (13). HOLDS.** x_p = Re(U_l V_p) up to cyclic order and inversion, with V_p the staple, so F = s sum_p conj(V_p) and |F| <= 6s. The geometry (two distinct links share at most one plaquette; 18 distinct other links) is the fact checked in `gap-mid-check.md` Section 5, Lemma INF. A link k of the plaquette p_0 enters the staple once, as X U_k^{+-1} Y with X, Y fixed unit quaternions, so |V - V'| = |U_k - U'_k| exactly. Only one term of F changes. By (7), C_lk <= s/4; 18 terms give alpha <= 9s/2. At s = 0 the kernels are Haar and all influences vanish.

**The count 6 and 18. HOLDS.** **Line 349 (radii). HOLDS** but is idle: Theorem V holds for every F.

**Verdict, Lemma INF chord form: HOLDS.**

## 5. R-a: the background-uniform layer twist (lines 352-417)

**Setting.** 0 < beta < 2/3, q = 3 beta/2 < 1, B periodic with sides at least 3.

**(15). HOLDS.** I_0 = I(u, v). The flip c_nu multiplies v_b by -1 on the bonds Sigma_0 that cross one plane (Proposition TW, Step 2, puts them from b_nu - 1 to 0), so y_b -> -y_b there, and exp(-beta(1 - y_b)) becomes exp(-beta(1 + y_b)) = the factor with J = -1. So I_1 = I(u, c_nu v). The exponent is -beta sum_b (1 - J_b y_b), its theta-derivative is beta sum_b (dJ_b/dtheta) y_b = -2 beta sum_{Sigma_0} y_b. So d/dtheta log I_theta = -2 beta sum_{Sigma_0} E_{J^theta} y_b, and integration gives (15). The fixed constant per bond cancels in E and does not matter.

**The flip and (16). HOLDS.** j = floor(b_nu/2) satisfies 1 <= j <= b_nu - 2 for b_nu >= 3, so H = {0 <= x_nu < j} is a proper non-empty slab, and Sigma_0, Sigma_1 are different bond sets. h -> -h on H keeps Haar measure. y_b changes sign iff exactly one end of b lies in H, i.e. iff b is in Sigma_0 or Sigma_1. The weight of J^theta composed with the flip has coefficient -(1 - 2 theta) = 1 - 2(1 - theta) on Sigma_0 and -1 on Sigma_1: it is the weight of K^{1 - theta}, with the same normaliser. Substituting, E_{J^theta} y_b = -E_{K^{1 - theta}} y_b for b in Sigma_0. Integrate over theta, substitute theta -> 1 - theta, and average the two expressions: (16).

**Kernels, D, Delta(y_b). HOLDS.** J^theta and K^theta differ only on Sigma_1, whose bonds have both ends in D = {x_nu in {j - 1, j}}. The one-site kernel at x depends only on the coefficients of bonds at x, so the kernels agree off D. y_b = h_x . O_b h_y is chord-1-Lipschitz in each of its two sites, so Delta(y_b) <= 2 (the old total-variation version had 4).

**Distances. HOLDS.** The influence graph is the nearest-neighbour graph of the periodic box (C_xy > 0 only for neighbours), and a path's length is at least the circular nu-distance. From the planes {0, b_nu - 1} to the planes {j - 1, j} the circular distances are j - 1, j, b_nu - 1 - j, b_nu - j, and (through the wrap) j and j + 1. Since b_nu >= 2j, b_nu - 1 - j >= j - 1, and the minimum is j - 1. For b_nu = 3 this is 0, and the bound is still valid.

**The constant 4 q^{j-1}/(1 - q). HOLDS.** Take mu = the K^theta Gibbs law (kernels at every site) and mu~ = the J^theta Gibbs law (same kernels off D). All coefficients lie in [-1, 1] for every theta, so (12) gives alpha <= q < 1. Lemma DC: |E_{J^theta} y_b - E_{K^theta} y_b| <= 2 . 2 . q^{j-1}/(1 - q). With (16), |integral of E_{J^theta} y_b| <= 2 q^{j-1}/(1 - q), and with (15) and |Sigma_0| = |B|/b_nu (one bond per site of one plane): |log(I_1/I_0)| <= 2 beta (|B|/b_nu) . 2 q^{j-1}/(1 - q) = (4 beta/(1 - q)) (|B|/b_nu) q^{j-1}. This is (14). Line 401 says "bounds the integrand in (16)"; the integrand there is the bracket, with the 1/2 outside the integral, so the line is correct as written.

**(AS-bg). HOLDS.** For 0 < beta <= beta_1: q <= q_1, so q^{j-1} <= q_1^{j-1} and beta/(1 - q) <= beta_1/(1 - q_1). floor(b/2) - 1 >= b/2 - 3/2 and q_1 < 1 give q_1^{floor(b/2) - 1} <= q_1^{-3/2} q_1^{b/2} = q_1^{-3/2} e^{-m b} with m = (1/2) log(1/q_1) > 0. So the bound is C (|B|/b_nu) e^{-m b_nu} with C = 4 beta_1 q_1^{-3/2}/(1 - q_1). beta = 0 gives ratio 1. The case beta_1 = 0 is as stated. Uniform in the background and in the box, because (12) is.

**Verdict, R-a: HOLDS.** (AS-bg) is proved for every beta_1 < 2/3. This closes the statement left OPEN in `gap-crux-fp.md` 4.2 for 1/6 <= beta_1 < 2/3. No correction.

## 6. R-b: the seed for beta < 2/9 (lines 419-593)

**Setting.** 0 < beta < 2/9, q = 9 beta/2 < 1, a >= 3, B with sides at least 3, j = floor(a/2). The normalisation is Z = integral of exp(-s sum_p (1 - x_p)) against Haar probability, as in Theorem D-shape (d) ("dF/dbeta = -6|n| abar_n, F = 0 at beta = 0").

**Cut construction and D. HOLDS (reused).** This is Lemma M of `gap-mid-max.md` Section 8, checked HOLDS in `gap-mid-check.md`. mu~ has the Gibbs one-link kernels of n = (a, B) at every link outside D (space links at times 0 and a - 1, time links from a - 1). mu_n has them everywhere. These are the hypotheses of Lemma DC with mu = mu_n.

**The plaquettes P and Delta(x_p) <= 4. HOLDS.** j >= 1 and j <= a - 1, so the plaquettes at time j and in the slab [j - 1, j] lie in Lambda_0 and do not cross the cut; their mu~-law is their mu'-law. As a function of one of its links, x_p = U . W with |W| = 1 (Section 4 isometries), so x_p is chord-1-Lipschitz in each of its four links: Delta(x_p) <= 4 (old: 8 with osc 2 per link; the factor 2 of chord DC restores the product 8).

**Circular positions and the distance j - 1. HOLDS.** On R/aZ: a space plaquette at time t has all positions t; a time plaquette of the slab [t, t + 1] has positions t, t + 1/2, t + 1 (mod a). For t = a - 1 these are a - 1, a - 1/2, 0, with circular spread 1. So every influence edge (two links of one plaquette of n; C > 0 only there, by (13)) moves the circular position by at most 1. The links of P lie in [j - 1, j]. The circular distances from a point x in [j - 1, j] to 0, a - 1, a - 1/2 have minima min(j - 1, a - j), min(a - 1 - j, j), min(a - 1/2 - j, j - 1/2). With a >= 2j the smallest is j - 1. So d >= j - 1. This is repair (1) of `gap-mid-check.md` Section 5, used explicitly.

**(17). HOLDS.** For 0 < s <= beta, (13) gives alpha <= 9s/2 <= q, and the DC bound is monotone in alpha and in d: |mu_n(x_p) - mu~(x_p)| <= 2 . 4 . q^{j-1}/(1 - q). P holds |B| plaquettes of each of the six orientations. Both tori are invariant under all four translations, so each abar is the mean over P of 1 - x_p (for the long torus, under mu' = mu~ on P). Averaging gives (17). At s = 0 both laws are product Haar and the difference is 0.

**(18), the factor 12 a|B| and 96. HOLDS.** The torus (t, B) has 6 t|B| plaquettes, so dF/ds = -6t|B| abar_{t,B}(s), and F(t, B; 0) = 0. Then Phi_B = integral over [0, beta] of [2(-6a|B| abar_a) + 12a|B| abar_{2a}] ds = 12a|B| times the integral of (abar_{2a} - abar_a). This is D-shape (d). With (17), uniform in s <= beta: Phi_B <= 12a|B| beta . 8 q^{j-1}/(1 - q) = 96 a|B| beta q^{j-1}/(1 - q). Lower bound: Z(t, B) = Tr T^t = lambda_0^t (1 + S(t)), so Phi_B = 2g(a) - g(2a) with g = log(1 + S). The eigenvalues lie in [0, lambda_0) apart from the top one ((TM): positive, trace class, simple top eigenvalue), so S(2a) <= S(a), g(2a) <= g(a), Phi_B >= g(a) >= 0, and S(a; B) <= e^{Phi_B} - 1 (D-shape (a)).

**(19) to (20). HOLDS.** |(2a)^3| = 8a^3, so 96 . 8 = 768 and Phi_B <= x := 768 a^4 beta q^{j-1}/(1 - q). If x <= 3/5000, then S <= e^x - 1 <= sum_{n >= 1} x^n = x/(1 - x) <= 3/4997, and 3/4997 < 1/1650 because 4950 < 4997. Strict, as the corrected r = 2 line of Theorem SH needs.

**Existence of a. HOLDS.** q^{floor(a/2) - 1} <= q^{-3/2} (sqrt q)^a, and a^4 (sqrt q)^a tends to 0, since the ratio of successive terms tends to sqrt q < 1.

**Both halves of the seed. HOLDS.** Identity FL (`gap-mid-max.md` Section 6, checked HOLDS) gives 1 + S_0 = (1 + S)(1 - U) <= 1 + S and 0 <= U <= S/(1 + S). (20) bounds the full thermal sum Tr T^t/lambda_0^t - 1, which contains every flux sector.

**Theorem SH arithmetic to (21). HOLDS.** (i) s_1 <= (1 + s_0)^64 - 1 (three applications of Lemma E, `gap-seed-shape.md` 1.5 two-stage line) < e^{64/1650} - 1 = e^{32/825} - 1. (ii) e^x - 1 <= x/(1 - x/2) for 0 <= x < 2, from n! >= 2^{n-1}. At x = 32/825: (32/825)/(809/825) = 32/809. 32/809 < 1/25 since 800 < 809. So s_1 < x_0 = 1/25. (iii) The r = 4 line: (j, p, q) = (2, 2, 3), K = 22.2 = 111/5, valid on [0, 0.04]; 3a < 4a. E = (j rmax/(rmin - 1))^3 = (2 . 4/3)^3 = 512/27 = 18.96 < 22.2 = K. (iv) K s_1 < 111 . 32/(5 . 809) = 3552/4045, and 3552/4045 < 22/25 since 3552 . 25 = 88800 < 88990 = 22 . 4045. (v) -log y = sum (1 - y)^n/n >= (1 - y) + (1 - y)^2/2; with 1 - y > 3/25 this is > 3/25 + 9/1250 = 159/1250 = 0.1272 > 1/8. (vi) L >= 64a = 2^4 . 4a gives k >= 4 in SH (ii), so j^{-k} <= 1/16. log(eE/K) = 1 + log(2560/2997) < 1 (numerically 0.842). (vii) m(L^3) > (1/a)(1/8 - 1/16) = 1/(16a) > 3/(50a). The corrected SH (ii) includes the case E s_k > 1 (row 707, point 3), so nothing is missing. With the exact values the bound is (0.1272 - 0.0527)/a > 0.074/a, matching `gap-mid-check.md`. Smaller cubes: positive gaps by the simple top eigenvalue.

**Example beta = 1/9, a = 96. HOLDS.** q = 1/2, j - 1 = 47. 768 beta/(1 - q) = 768 . 2/9 = 512/3. 96 = 3 . 2^5, so 96^4 = 81 . 2^20. (512/3) . 81 . 2^20 . 2^{-47} = 27 . 2^{9 + 20 - 47} = 27/2^18. 27/2^18 < 3/5000 iff 45000 < 2^18 = 262144: true. (21) gives m >= 3/(50 . 96) = 1/1600 for L >= 64 . 96 = 6144.

**Verdict, R-b: HOLDS.** Theorem DOB chord form, (17) to (21) and the example all hold. No correction.

## 7. Section 5 against what is proved; scope

**Summary sentence by sentence.**
- "(vMF-Lip) with the sharp constant a(|F|) = E_F(h_perp^2), for all fields": proved (Section 1 above). **Wording correction:** h_perp must mean the coordinate h.v along one unit v orthogonal to F. Read as the squared norm of the orthogonal projection, E_F |h_perp|^2 = 3 a(|F|), and the constant would be wrong by a factor 3. Suggested text: "a(|F|) = E_F((h.v)^2) for any unit v orthogonal to F".
- "(AS-bg) for every beta_1 < 2/3": proved (Section 5 above).
- "the full seed for every 0 < beta < 2/9": proved, both halves, with the gap (21) given the inherited (TM), Identity FL, Lemma M and the corrected Theorem SH (Section 6 above).
- "transfer and shape results inherited; fixed lattice coupling": correct.
- "no numerical run, no certificate, no new premise": I found none in any proof line. The Durhuus-Frohlich and Grok credits, and the repository-search paragraph (lines 1-55), enter no proof. I did not re-run or read the search logs in `/tmp/gap-vmf-lip-3b5f2007e/`.
- The labels "author proof; not independently checked" (line 59) and "remaining action ... independent reading" (line 607) are now out of date by this one reading. Whether a cross-provider reading counts as the independent check is the lead's call.

**Does any step need more than strong coupling?** No. Theorem V is an exact single-site statement, valid for every field, with no coupling restriction. Every lattice consequence uses Dobrushin's condition alpha < 1: beta < 2/3 in the three-dimensional layer model (R-a) and beta < 2/9 in the four-dimensional gauge measure (R-b). The inherited inputs (TM), Identity FL, Lemma M, Theorem D-shape and Theorem SH hold at every fixed coupling; they add no range. Nothing touches the middle range or the continuum.

**What this check does not cover.** The body of `gap-transfer.md` (N.1-N.2, (TM), (TM-c)) and the inherited Theorem SH proof itself (checked in row 707) were not re-derived; only the statements and the arithmetic that this file uses were checked. The geometry facts of Lemma INF were taken from the row 709 check, with a re-reading of their statement.

## 8. Verdict table

| Statement | Verdict | Correction |
|---|---|---|
| Theorem V (1): V_k/S_k = a(k), E_F h = a(k)F | HOLDS | |
| Theorem V (2): Delta b = k^2 b, w, div(e^{F.x}V) = e^{F.x}, d_r w = -a | HOLDS | |
| Theorem V (3): normal flux | HOLDS | |
| Theorem V (4): covariance identity, factor V_k/S_k = a(k) | HOLDS | |
| Theorem V (5): M(rh)e | HOLDS | |
| Theorem V (6): conditional law mu_{su}, bound 1 (0 < b <= 1, 0 <= m <= 1) | HOLDS | |
| Theorem V: extension, smoothing, limit | HOLDS | |
| Theorem V: sharpness, a(k) = E_F h_v^2 <= 1/4 | HOLDS | |
| Corollary V1 | HOLDS | |
| Lemma DC chord form: (9), P, R and its orientation, (10), (11), telescoping, N^{-1} sum R^t = (I - C)^{-1}, second inequality | HOLDS | |
| Lemma INF chord form: (12), (13), counts 6 and 18, isometries | HOLDS | |
| R-a: (14) to (16), flip, distances, 4q^{j-1}/(1 - q) | HOLDS | |
| (AS-bg) for every beta_1 < 2/3 | HOLDS | |
| R-b: cut and D, Delta(x_p) <= 4, circular distance j - 1, (17) | HOLDS | |
| R-b: (18) (12a|B|, 96), (19), (20), existence of a | HOLDS | |
| R-b: both halves of the seed | HOLDS | |
| R-b: Theorem SH arithmetic to (21) | HOLDS | |
| Example beta = 1/9, a = 96 | HOLDS | |
| Section 5 summary | HOLDS AFTER CORRECTION | write E_F((h.v)^2) for one unit v orthogonal to F, not E_F(h_perp^2) |

No statement FAILS. No correction changes a constant, a threshold or a conclusion.

RESULT: Every numbered statement of gap-vmf-lip.md holds on a hand re-derivation (Theorem V with the sharp constant a(|F|) <= 1/4 for all fields, chord Lemmas DC and INF, (AS-bg) for every beta_1 < 2/3, and the seed with the gap m(L^3) >= 3/(50a) for 0 < beta < 2/9), with no FAILS and one wording correction (E_F(h_perp^2) in Section 5 must mean the square of one coordinate orthogonal to F), all strictly within strong coupling.
