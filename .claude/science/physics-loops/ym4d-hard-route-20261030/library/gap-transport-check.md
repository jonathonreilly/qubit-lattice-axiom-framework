lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T15:10Z

# gap-transport-check (FINISH row 682; item P5 of `library/gap-skeleton-max.md`)

Provenance: Claude Opus 5.5 at high effort, one session, no subagents, started 2026-11-11T03:10Z at pinned commit b1671559b. This is a line-by-line check by a model that did not write the proofs (the author of `gap-skeleton-max.md` is Claude Fable 5.2). It is not an audit and grants no status. Written section by section; a section that ends with "STOPPED HERE" was cut by the output limit.

Scope (row 682): Lemmas 1, 2, 3 of 1.D (lines 224-250), Lemma 7 of 3.6 (line 524), Lemma 6 of 3.5 (line 515), Facts 1, 2, 3 of 3.4 (lines 501-505); then the question of P5: in the chain model of D.3, is Hess phi_b bounded below uniformly in L?

## Repo search

- `library/open-core.md`: no entry contains "transport", "chain model", "Hess phi" or "T-avg". FINISH: only rows 669 (the author run) and 682 (this item) mention the chain model or Hess phi. So no other row covers the chain-model question.
- `library/gap-skeleton-final.md` (row 676, laptop lead) lists the same statements in its section 6 with this item as their check (lines 155-162), and its own run-2 statements go to a different item, `gap-zero-transport-check`. No proof of the chain-model question there.
- The Sussman-Alpoge account does not treat transport in the coupling or the gap (it proves no gap; `gap-skeleton-max.md` Part 0.3, re-quoted from YM4_1400.tex L3054-3056). Nothing in it to port for this item; it enters only through Lemma 6, whose input is its clause (c)(3)-(4), quoted in the skeleton.

## 1. Lemma 1 (transport), skeleton line 224

Setting checked first (D.1). For f, g smooth, int f (-Delta g) e^{-bA} dvol = int <grad f, grad g> e^{-bA} - b int f <grad A, grad g> e^{-bA}, so int f L_b g d mu_b = int <grad f, grad g> d mu_b with L_b = -Delta + b <grad A, grad .>. Correct. phi_b exists, is smooth and is unique up to a constant, because A - mu_b(A) has mean zero and L_b is elliptic with kernel the constants on a connected compact X (connectedness is used and not stated; SU(2)^links is connected).

Line by line.

1. d/dt mu_t(f) = -Cov_t(f, A): derivative of int f e^{-tA} / Z_t. Correct.
2. Cov_t(f, A) = int f (A - mu_t A) d mu_t = int f L_t phi_t d mu_t = int <grad f, grad phi_t> d mu_t. Correct. Hence d/dt mu_t(f) = int <grad f, Z_t> d mu_t, the weak continuity equation.
3. "The image measure satisfies the same equation ... and the solution is unique for a smooth field on a compact manifold." The uniqueness is cited, not proved. GOAL.md forbids "standard" as a step, so here is the line that replaces it (a direct proof, no comparison of two solutions needed). Z_t is smooth in (t, x): phi_t = L_t^{-1}(A - mu_t A) on mean-zero functions, and t -> L_t is a smooth family of elliptic operators with a uniform gap on mean-zero functions on any compact t-interval (the gap is positive for every t and continuous in t by Lemma 2's Lipschitz bound below), so the resolvent is smooth in t and elliptic regularity gives joint smoothness. Fix g smooth and b; put u(t, x) = g(Phi_{t,b}(x)). Then u is smooth, d/dt u = -<grad u, Z_t>, and d/dt int u(t) d mu_t = int (d/dt u) d mu_t + int <grad u(t), Z_t> d mu_t = 0 (the second term is line 2 applied to f = u(t); the product rule holds because u is jointly C^1 and t -> mu_t has a C^1 density). So mu_b(g) = mu_s(g o Phi_{s,b}). This is the claim.
4. For v carried by the flow, D_t v = grad_v Z_t (covariant derivative along the trajectory), so d/dt |v|^2 = 2 <grad_v Z_t, v> = -2 Hess phi_t(v, v) <= 2c |v|^2, and |D Phi_{s,b}| <= e^{c(b-s)}. Correct.
5. Var_b(f) = Var_s(f o Phi_{s,b}) by 3; Poincare at s; grad (f o Phi) = (D Phi)^T (grad f o Phi), so |grad (f o Phi)|^2 <= e^{2c(b-s)} |grad f|^2 o Phi, and int |grad f|^2 o Phi d mu_s = int |grad f|^2 d mu_b by 3. So Var_b(f) <= gamma(s)^{-1} e^{2c(b-s)} int |grad f|^2 d mu_b for every f, which is gamma(b) >= gamma(s) e^{-2c(b-s)}. Correct.
6. Gauge-invariant version: if a compact group acts by isometries preserving A, phi_t is invariant (uniqueness of the mean-zero solution), Z_t is equivariant, Phi commutes with the action, and f o Phi is invariant when f is. Then 5 runs inside the invariant functions with gamma replaced by the invariant gap. Correct.

**Verdict: HOLDS.** The only gap is the cited uniqueness in line 3; the duality line above closes it. No change to the statement.

## 2. Lemma 2 (four forms of the derivative of the gap), skeleton line 227, and its Corollary (T-avg)

Line by line.

1. "Differentiable almost every b; gamma is a minimum of smooth Rayleigh quotients." A minimum of smooth functions need not be differentiable a.e.; what is needed is a Lipschitz bound uniform in f. It holds: for g >= 0, |Cov_b(g, A)| <= osc(A) mu_b(g). The numerator N_b(f) = mu_b(|grad f|^2) has N' = -Cov(|grad f|^2, A); the denominator V_b(f) = Var_b(f) has V' = -Cov((f - mu_b f)^2, A) (the derivative in the centring constant vanishes at c = mu_b f). So |d/db log R_b(f)| <= 2 osc(A) for every f, log gamma is 2 osc(A)-Lipschitz, and Rademacher gives differentiability a.e. Supplied; the statement is unchanged.
2. At a differentiable b, R_{b'}(f_b) - gamma(b') >= 0 with equality at b' = b, so gamma'(b) = d/db' R_{b'}(f_b) at b' = b, for every eigenfunction f_b of the eigenvalue gamma(b) (degeneracy is harmless). With mu_b(f) = 0: gamma' = [-Cov(|grad f|^2, A) + gamma Cov(f^2, A)] / <f^2>. Correct.
3. Cov(g, A) = <grad g, grad phi> gives the bracket -2 <Hess f(grad f, grad phi)> + 2 gamma <f <grad f, grad phi>>. Correct (grad |grad f|^2 = 2 Hess f(grad f, .)).
4. gamma <f <grad f, grad phi>> = <(L f) <grad f, grad phi>> = <grad f, grad <grad f, grad phi>> = <Hess f(grad f, grad phi)> + <Hess phi(grad f, grad f)>. Correct. Hence (HF1): gamma' = 2 <Hess phi(grad f, grad f)> / <f^2>.
5. (HF2): L(f^2) = 2 f L f - 2 |grad f|^2 = 2 gamma f^2 - 2 |grad f|^2. So |grad f|^2 = gamma f^2 - (1/2) L(f^2), the bracket equals (1/2) Cov(L(f^2), A) = (1/2) <L(f^2) A> = (1/2) <f^2 L A>. L A = b |grad A|^2 - Delta A, mean zero. Correct.
6. (HF3): <f^2 L A> = <grad f^2, grad A> = 2 <f <grad f, grad A>>; with dW/dt = -grad A, d/dt (f o W_t) at 0 = -<grad f, grad A>, so d/dt <(f o W_t)^2> at 0 = -2 <f <grad f, grad A>>. Correct.
7. (HF4): <grad f^2, grad A> = -(1/b) int <grad f^2, grad e^{-bA}> dvol / Z = (1/b) <Delta f^2> = (2/b)(<|grad f|^2> + <f Delta f>). With <|grad f|^2> = gamma <f^2>: b gamma' = gamma - <f(-Delta) f>/<f^2>. Correct.

Independent check on the Gaussian (a different data path: direct computation, not the lemma's algebra). One dimension, A = x^2/2 on R, mu_b = N(0, 1/b), f = x, gamma = b, phi_b = x^2/(4b) (L phi = -1/(2b) + x^2/2 = A - mu_b A), Hess phi = 1/(2b). (HF1): 2 (1/(2b)) (1)/(1/b) = 1. (HF2): L A = b x^2 - 1, <x^2 (b x^2 - 1)> = 3/b - 1/b = 2/b, (1/2)(2/b)/(1/b) = 1. (HF3): <x . x> / <x^2> = 1. (HF4): b gamma' = b - 0. All give gamma' = 1. Agrees.

Constants of the Wilson formulas (line 245, not a lemma, checked because P5 inputs use them): with \|X\|^2 = -2 tr X^2 (the norm of 3.4), SU(2) is the round 3-sphere of radius 2, the fundamental character is an eigenfunction of -Delta with eigenvalue 3/4 in each link variable, and each plaquette has four links, so Delta A = 4 (3/4) sum_p (1 - a_p) = 3 sum_p (1 - a_p). For the link term -(1/2) Re tr(U_l S) with U_l S = rho (cos theta + i sin theta n.sigma), the derivative along X = (i/2) t m.sigma (\|X\| = \|t\|) is (1/2) rho sin theta (m.n), so \|grad_l A\|^2 = rho^2 sin^2 theta / 4. Both agree with the skeleton, in that normalisation (the skeleton states the norm only in 3.4).

**Corollary (T-avg).** By (HF1) and <|grad f|^2> = gamma <f^2>, (T-avg) at b is exactly (log gamma)'(b) >= -2c, and the two other forms are (HF3) and (HF4) rewritten. All three equivalences are correct. The "if and only if" with the bound gamma(b) >= gamma(b_0) e^{-2c(b - b_0)} is correct only when that bound is asked for every pair b_0 <= b in the interval: a bound from one base point b_0 does not control the derivative at interior points.

**Verdict, Lemma 2: HOLDS** (a.e. differentiability supplied by the Lipschitz bound of item 1). **Corollary: HOLDS AFTER CORRECTION.** Corrected statement: on an interval I, gamma(b) >= gamma(b_0) e^{-2c(b - b_0)} for all b_0 <= b in I if and only if (T-avg) holds at almost every b in I. Proof: log gamma is Lipschitz, hence absolutely continuous, so the pairwise bound is equivalent to (log gamma)' >= -2c a.e., which is (T-avg) by (HF1).

## 3. Lemma 3 (product transport in the chain model), skeleton line 248

Setting (D.3). Open chain, sites 0..L, eta_x = theta_{x+1} - theta_x for 0 <= x <= L-1, A = sum_x W(eta_x). Under mu_b the eta_x are i.i.d. with density proportional to e^{-bW} (this needs e^{-bW} integrable: on the line W must grow, as for W = eta^2/2 + lambda w; for W = 1 - cos the increments live on the circle and T is a degree-one monotone circle map; both readings are used by P5). The transport is Theta(theta)_x = theta_0 + sum_{y<x} T(eta_y), with T monotone and T_*(law of eta at b) = law at b'. So Theta_* mu_b = mu_{b'}. Correct.

Line by line.

1. (D Theta v)_x = v_0 + sum_{0<=y<x} t_y (v_{y+1} - v_y). Summation by parts: sum_{0<=y<x} t_y (v_{y+1} - v_y) = t_{x-1} v_x - t_0 v_0 - sum_{1<=y<x} d_y v_y. With v_0 = 0 this is the skeleton's identity. Correct.
2. With v_y = d_y on 1..R and 0 elsewhere: (D Theta v)_x = t_{x-1} d_x - S_{x-1} for 1 <= x <= R, = -S_R for x > R, and = 0 at x = 0, where S_x = sum_{1<=y<=x} d_y^2. The skeleton writes "- sum_{y<x} d_y^2", which is S_{x-1}; correct.
3. "Hence, modulo constants, |D Theta v|^2 >= sum_{x<=R} (S_R - S_x - |t d_x|)^2." **Defect.** Adding S_R to every entry gives u_x = S_R - S_{x-1} + t_{x-1} d_x (1 <= x <= R), u_0 = S_R, u_x = 0 (x > R), and the displayed sum is the norm of this one representative, not the norm modulo constants, which is the minimum over all shifts: min_c sum_x (u_x - c)^2 = sum u_x^2 - (sum u_x)^2/(L+1). For R = L the minimum can be much smaller (the ramp is then the whole vector and its mean is subtracted). Also S_x should be S_{x-1} (harmless: they differ by d_x^2, bounded).
   The quotient norm is the right one: for a gauge-invariant f, grad f is orthogonal to the constant vector 1, D Theta 1 = 1, so |grad (f o Theta)| is controlled by \|P D Theta P\| with P the projection off constants, and \|P D Theta v\| / \|v\| <= \|P D Theta P\| for every v because \|P v\| <= \|v\|.
4. "S_x = delta^2 x (1 + o(1)) with delta^2 = 2 Var T'(eta) > 0" for independent eta: E d_y^2 = 2 Var t, and (d_y^2) is a 1-dependent stationary sequence, so S_x / x -> delta^2 almost surely (law of large numbers for the two interleaved i.i.d. subsequences y even, y odd). This is a statement on typical fields, as the skeleton says. Correct. delta > 0 iff T' is not a.s. constant, i.e. T not affine.
5. "|D Theta| >= c delta R." Not derived in the text from 3-4; the derivation needs the quotient correction and a size condition on R. Supplied below.

**Corrected statement (Lemma 3').** Let K = sup |T'| (sup T' - inf T'), finite since T' is continuous and positive on the support (circle case: compact; line case: assume it, as for the affine-plus-bounded perturbations at hand). Let 1 <= R <= (L-1)/2 and let theta be a field with delta^2 R/2 <= S_R <= 2 delta^2 R and S_{R/2} <= (2/3) S_R (all hold with probability tending to 1 as R -> infinity at fixed b, b', by item 4), and R >= 12 K / delta^2. Then for v as above, \|P D Theta v\| >= (delta R / 34) \|v\|. Hence \|P D Theta P\| >= delta R / 34 on such fields, and the Lipschitz constant of Theta on gauge orbits is at least delta (L-1)/34 on a set of fields of probability tending to 1 as L -> infinity.

Proof. min_c sum (u_x - c)^2 = sum u^2 - (sum u)^2/(L+1) >= sum u^2 (1 - (R+1)/(L+1)) >= (1/2) sum u^2, by Cauchy-Schwarz on the support {0..R} of u and R + 1 <= (L+1)/2. For 1 <= x <= R/2: S_R - S_{x-1} >= S_R - S_{R/2} >= S_R/3, and |t_{x-1} d_x| <= K. Since S_R >= delta^2 R/2, S_R/3 - K >= delta^2 R/6 - K >= delta^2 R/12 for R >= 12 K/delta^2, so u_x >= delta^2 R/12 there and sum u^2 >= (R/2)(delta^2 R/12)^2 = delta^4 R^3/288. With \|v\|^2 = S_R <= 2 delta^2 R: \|P D Theta v\|^2 / \|v\|^2 >= (1/2)(delta^4 R^3/288)/(2 delta^2 R) = delta^2 R^2/1152, and sqrt(1152) < 34. QED

Remarks, not defects. (i) "In the metric of the increments the same map is Lipschitz with constant sup T'": correct, Theta acts on eta componentwise. (ii) "For W = 1 - cos at large b, delta is of order 1/b" is true only for b'/b fixed: at large b, T'(eta) = sqrt(b/b') (1 + O(eps eta^2)) with eps = (b' - b)/b and eta^2 of order 1/b, so delta is of order eps/b. The lemma does not use it.

**Verdict, Lemma 3: HOLDS AFTER CORRECTION.** The conclusion (Lipschitz constant on gauge orbits unbounded, of order delta L on typical fields) is right; the displayed inequality is wrong as a bound on the norm modulo constants when R is close to L, and the corrected statement is Lemma 3' above (R <= (L-1)/2, factor 1/2, explicit size condition R >= 12 K/delta^2, constant 1/34, written S_{x-1} for S_x). Lemma 3 refutes the pointwise bound only for this map, which is not the gradient flow of Lemma 1; the skeleton says so (D.4 (b)).

## 4. Lemma 7 (chain model, first order), skeleton line 524

Setting. Periodic chain Z/L, eta = d theta lies in the hyperplane H = {sum_x eta_x = 0} = range of d; M = d d^T is invertible on H, and M^{-1} means the inverse there. (The open chain of D.3 works the same way, with H = R^L.)

Line by line.

1. phi_0 = (eta, M^{-1} eta)/(4b) = \|P theta\|^2/(4b), with P = d^T M^{-1} d the projection off constants. Direct check: grad phi_0 = P theta/(2b), Delta phi_0 = (L-1)/(2b), <grad A_0, grad phi_0> = <d^T d theta, P theta>/(2b) = \|d theta\|^2/(2b), so L_0 phi_0 = \|d theta\|^2/2 - (L-1)/(2b) = A_0 - mu_0(A_0). Hess phi_0 = P/(2b). Correct.
2. On functions F(d theta): grad_theta F = d^T grad_eta F, Delta_theta F = (d_eta, M d_eta) F, <grad A, grad F> = (grad_eta A, M grad_eta F). So L_lambda = -(d_eta, M d_eta) + b (eta + lambda w'(eta), M d_eta). Correct.
3. Order lambda: L_0 phi_1 + L_1 phi_0 = A_1 - const, L_1 = b (w'(eta), M d_eta). M d_eta phi_0 = M M^{-1} eta/(2b) = eta/(2b) (eta in H), so L_1 phi_0 = (1/2)(w'(eta), eta). Correct. u = w - (1/2) eta w', u' = (1/2) w' - (1/2) eta w'', u'' = -(1/2) eta w'''. So sup \|u''\| = U. Correct.
4. phi_1 = int_0^infinity (P_t g - mu_0 g) dt solves L_0 phi_1 = g - mu_0 g: L_0 is the Ornstein-Uhlenbeck generator of d eta = -b M eta dt + sqrt(2) d dB on H, with gap b lambda_min(M\|_H) > 0 at fixed L, so the integral converges and L_0 of it is g - mu_0 g. Under the flow, eta_t = e^{-btM} eta + zeta_t with zeta_t Gaussian, independent of eta. Correct.
5. Two derivatives along nu = d v: since g is a sum of one-site functions, d_nu^2 (P_t g)(eta) = sum_x E[u''((e^{-btM} eta + zeta_t)_x)] ((e^{-btM} nu)_x)^2. The interchange of d_nu^2 and the t-integral is justified by \|e^{-btM} nu\| <= e^{-bt lambda_min} \|nu\| and \|u''\| <= U. Correct.
6. \|Hess phi_1(v, v)\| <= U int_0^infinity \|e^{-btM} nu\|^2 dt = U (nu, (2bM)^{-1} nu) = (U/(2b)) (v, P v) = (U/(2b)) \|P v\|^2. Correct, and the bound is uniform in theta, v and L.

Two remarks on scope, neither a false line.

(a) The proof computes the first-order coefficient: phi_1 is the solution of L_0 phi_1 = sum_x u(eta_x) - mu_0(.). That it equals d/d lambda phi_lambda at lambda = 0 (in C^2, pointwise) is presupposed, not shown. At fixed L, differentiability in L^2(mu_0) follows from L_lambda (phi_lambda - phi_0 - lambda phi_1) = -[mu_lambda(A_lambda) - mu_0(A_0) - lambda c_1] - lambda^2 L_1 phi_1 and the gap of L_lambda, when w' is bounded; the C^2 statement needs elliptic regularity on top. The class "C^3 with U finite" allows w'' to grow like log \|eta\| and w' like \|eta\| log \|eta\|, so for lambda < 0 the measure can fail to exist; the derivative is then one-sided. Read the lemma as a statement about the coefficient phi_1; so read, it holds.

(b) "True to first order" gives Hess phi_lambda = P/(2b) + lambda Hess phi_1 + R_lambda with \|lambda Hess phi_1\| <= lambda (U/(2b)) \|P v\|^2, but says nothing about R_lambda uniformly in L. Uniformity of the remainder in L is exactly the question of P5, decided in section 7 below.

**Verdict, Lemma 7: HOLDS** (as a statement about the first-order coefficient phi_1 defined by its equation; remark (a)).

## 5. Lemma 6 (upper bound on the gap), skeleton line 515

Source re-read for this check: `YM4_1400.tex` (Sussman and Alpoge) at commit 2bc0658f91d2d03ba44e20bf695067e0a56a2ed9, fetched by URL into a scratch folder; lines 1748-1800 (theorem "Continuum correlations", clauses (a)-(c)(4)) and 1884-1910 (theorem "Canonical components"). Credit: the input of this lemma is their clause (c)(3)-(4) and their component theorem.

Line by line.

1. G(t) = sigma(theta F-bar . tau_t F) - \|sigma(F)\|^2 = int e^{-tE} d rho_F(E) with rho_F the spectral measure of F - <Omega, F> Omega for H. If ker H = C Omega (true for a component: their (3)(iii)) and spec H \ {0} lies in [m, infinity), rho_F lives on [m, infinity). Correct. Then G(t_2) <= e^{-m (t_2 - t_1)} G(t_1) directly (the log-convexity detour is correct but not needed).
2. Geometry: f >= 0 in a ball of radius d centred at time c > d; theta f in the reflected ball. Support distances 2d and 5d are both in the window [d, 6d]; the time shift between them is 3d; point distances are >= 2d in the first case and <= 5d + 4d = 9d in the second, so K_free(t_1)/K_free(t_2) <= (9/2)^8. Correct. The reflected and shifted tests stay in the class T(d; vartheta) (rigid motions preserve the two class conditions int f >= vartheta \|f\|_inf d^4 and Lip f <= \|f\|_inf/(vartheta d), which the skeleton does not list; a fixed rescaled bump satisfies them).
3. **Defect: which clause, for which state.** The hypothesis written in the lemma, zeta(d)^2 C_N g(d)^4 K_free (1 + eps) with \|eps\| <= 1/2, is the account's clause (c)(3) (L1788-1790): a statement at finite cutoff K, for the lattice torus states and, "only with \|eps\| <= 1/2", for periodic Gibbs states at a first-passage datum, under K - s(d) >= n_0. It is not stated for a continuum component. For a component the account gives, in "Canonical components" (3)(ii), "the law (c)(4) in its form on R^4": the factor zeta is absorbed and the error obeys (1 - 1/2)(1 - eta-bar)^4 <= 1 + eta <= (1 + 1/2)(1 + eta-bar)^4 with eta-bar(d) <= 1/3 (L1797-1798). So for a component G(t_1)/G(t_2) <= 3 ((1 + eta-bar)/(1 - eta-bar))^4 (9/2)^8 <= 48 (9/2)^8, and the constant changes.
4. The passage to lattice units converts the gap of the continuum component into lattice units, m a_K. That is not the gap of the Wilson measure at bare coupling beta, which is what the next paragraph of 3.5 uses ("a mechanism that would give m_lat(beta) >= beta^{-p} for the Wilson measure at every large beta contradicts the account"). The lattice statement needs its own proof, and the finite-cutoff clause (c)(3) gives it directly (below). Also "exp(c_AF (beta - 4/g^2)(1 + o(1)))" mixes normalisations: in the account beta and g^{-2} are on the same scale (first passage starts from beta >= g^{-2} + B_sharp); the clean statement is log(1/a_K) = beta (12 pi^2/(11 N^2))(1 + o(1)) uniformly on the first-passage window (their (a), L1757).

**Corrected statement (Lemma 6').** Assume the account (its packages as listed in the two theorems). Fix vartheta and g <= gamma_W(vartheta).
(i) *Component.* Let sigma_xi be a canonical component of a volume-first limit with spec H_xi \ {0} in [m, infinity). Then m <= (log 48 + 8 log(9/2))/(3d) for every d <= d_0; and m <= (log 3 + 8 log(9/2) + o(1))/(3d) as d -> 0, since eta-bar(d) -> 0. In units of the length where the coupling is g: m <= 5.3/d_0.
(ii) *Lattice.* Let (K, beta) be a first-passage datum, nu a periodic Gibbs state of Wilson's weight at beta on the lattice of spacing a_K that is reflection positive at a lattice time mirror, and m_nu the largest m with G_nu(t_2) <= e^{-m(t_2 - t_1)} G_nu(t_1) for all t_2 >= t_1 >= 0 and all F = O(f) as above (this is implied by a gap m of the transfer matrix of nu on the orthocomplement of its invariant vectors, when the invariant vector is unique). If d <= d_0 and K - s(d) >= n_0, then m_nu <= (log 3 + 8 log(9/2))/(3d) in physical units; in lattice units m_nu a_K <= 4.4 a_K/d. Along the first-passage data at fixed g, a_K = exp(-(12 pi^2/(11 N^2)) beta (1 + o(1))), so m_nu a_K <= C(g) exp(-c_AF beta (1 + o(1))) with c_AF = 12 pi^2/(11 N^2), for every large beta (every beta >= g^{-2} + B_sharp has a first-passage datum, their (a)).
Proof. (i) is items 1-3 with the (c)(4) bounds. (ii) is items 1-2 with the clause (c)(3) for periodic Gibbs states (\|eps\| <= 1/2; the same d gives the same zeta_K(d) and g(d) in both pairs, so they cancel), and lattice times t_1, t_2 at the nearest lattice points (an error O(a_K/d) in the distances, absorbed for K large). QED

**Verdict, Lemma 6: HOLDS AFTER CORRECTION.** The bound m <= C/d stands. The corrections: for a component the account gives the (c)(4) form, so C = (log 48 + 8 log(9/2))/3 (about 5.3) instead of (log 3 + 8 log(9/2))/3 (about 4.4); and the lattice bound is a separate statement about the lattice state, proved from the finite-cutoff clause (c)(3), not by converting the continuum gap. The consequence drawn in 3.5 (a lattice gap >= beta^{-p} at every large beta contradicts the account) then holds, as a statement conditional on the account like everything it uses.

