# Check of library/gap-gamma2-astra.md (FINISH row 815), by Claude Opus 5.5, line by line

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `e11ce7727f754f1d6d82d7c6ca8570762c4c88ed`.
- Target: `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-gamma2-astra.md`, 679 lines, by Codex gpt-6-astra max (FINISH row 812). Read in full.
- Context read: `gap-vmf-lip.md` Section 2 (Corollary V1, Lemma DC chord form with (9)-(11), Lemma INF (12)-(13)) and its check `gap-vmf-lip-check-opus.md` (all of it); `gap-tu-retry.md` Sections 1 (statement of Theorem V), 2 (Lemma L, (13)-(17)), 3 ((18)-(23)), 4-5, and its check `gap-tu-check-opus.md` (all of it); `gap-tree-astra.md` Section 1 (route B, (G2)) and `gap-tree-check-opus.md` Section 4 (route B correction). `gap-ac-lat.md` lines 40, 130-132 for the metric and the reconstruction argument.
- Method: every identity re-derived by hand. No numerical run was made, not even a GUIDE run. No repository file was edited.
- This is one reading by a model of a different provider from the author. It is not an audit. Inputs reused at their checked status (Theorem V of `gap-vmf-lip.md`, Lemma DC, Lemma INF, Villain Theorem V of `gap-tu-retry.md`) were not re-derived; only their statements and the way this note uses them were checked.

## 1. Items (1)-(5): Bochner identity, sign of the generator, spectral implication

**Ricci.** The unit 3-sphere has Ric = (n - 1)g = 2g. A product of Einstein factors with the same constant has Ric = 2 g_product. The note's warning (not 2|E| g) is right.

**Sign of the generator.** For L = -Delta + <grad S, grad .>, integration by parts against e^{-S} gives mu(f L g) = mu(<grad f, grad g>). So L is symmetric and nonnegative, and P_t = e^{-tL} is the semigroup of dX = -grad S dt + sqrt2 dW. Correct.

**Bochner (3).** With A = -L = Delta - <grad S, grad .>, the Bakry-Emery formula is (1/2) A|grad f|^2 - <grad f, grad Af> = ||Hess f||^2 + (Ric + Hess S)(grad f, grad f). Invariance gives mu(A g) = 0. Integration by parts gives mu(<grad f, grad Af>) = -mu((Af)^2). Integrating, mu((Lf)^2) = H + 2E + C. Correct. The Hessian is the full product Hessian, with the mixed blocks; in a product the mixed blocks are plain mixed partials along geodesics of distinct factors.

**(G2) and (4).** Q - (1 - theta)H - kappa E = C + theta H + (2 - kappa)E by (3). So (G2) and (4) are the same inequality. The remark on negative theta is right: H >= 0, so validity with theta < 0 implies validity with theta = 0.

**Spectral implication (5).** Gauge transformations act by left and right multiplication, isometries of each S^3 that fix S and Haar measure. The averaging projection commutes with L. The compact connected manifold gives discrete spectrum, smooth eigenfunctions and kernel = constants. For L f = lambda f, Q = lambda^2 mu(f^2) and E = lambda mu(f^2), so Q = lambda E. Then (4) gives lambda E >= kappa E with E > 0, so lambda >= kappa. Expansion in an invariant eigenbasis gives (5). Correct.

**Metric remark.** `gap-ac-lat.md` line 130 uses |X|^2 = -2 tr X^2. For a unit imaginary quaternion as a 2 x 2 matrix, X^2 = -I, so |X|^2 = 4. Under g' = 4g, Delta' = Delta/4, L' = L/4, and the Ricci endomorphism is 2/4 = 1/2, which matches the value 1/2 quoted there. Correct.

**Verdict, item 1: HOLDS.**

## 2. Items (6)-(8): plaquette Hessian bound, (7), equivalence

**(6).** On the unit sphere a unit-speed geodesic is U(t) = cos(|v|t)U + sin(|v|t)v/|v|, so U'' = -|v|^2 U in R^4. A product geodesic is a geodesic of the product, so the second t-derivative is the Hessian form. q_p = Re(U_1 U_2 U_3^{-1} U_4^{-1}) is multilinear in the four ambient vectors (inversion = conjugation is linear on R^4). Diagonal term: Re of the product with U_e replaced by -|v_e|^2 U_e, which is -|v_e|^2 q_p. So the diagonal term of (1 - q_p) is +q_p |v_e|^2, bounded by |v_e|^2. Mixed term: each unordered pair appears twice in the second derivative, as 2 Re(product with v_e and v_e' inserted). The product of unit quaternions and two tangent vectors has norm |v_e||v_e'|, and |Re| <= norm. So |Hess(1 - q_p)(v, v)| <= (sum_{e in p} |v_e|)^2 <= 4 sum_{e in p} |v_e|^2 by Cauchy-Schwarz over four links. Correct. Inversion is an isometry, so the orientation does not matter.

**(7).** Each link (x, mu) lies in the plaquettes (x, mu, nu) and (x - nu, mu, nu) for the three nu != mu: six occurrences. With every period at least 2 these are six distinct indexed plaquettes, and each contains four distinct links ((x, mu) != (x + nu, mu) because n_nu >= 2). So |Hess S(v, v)| <= beta sum_p 4 sum_{e in p} |v_e|^2 = 24 beta |v|^2. A center sign epsilon_p changes no absolute value. Correct. At period 2 two parallel links can share two plaquettes (for example (x, mu) and (x + nu, mu) lie in both (x, mu, nu) and (x + nu, mu, nu)); the count by occurrences still gives 6 per link.

**(8).** If the invariant gap is at least lambda_*, the invariant eigen-expansion gives Q >= lambda_* E. From (3) and (7), Q >= H + 2E - 24 b_+ E >= H - 24 b_+ E. The convex combination gives delta H + [lambda_* - delta(lambda_* + 24 b_+)] E. With delta = lambda_*/(2(lambda_* + 24 b_+)) the bracket is lambda_*/2. So Q >= (1 - theta)H + kappa E with theta = 1 - delta in [1/2, 1) and kappa = lambda_*/2. This is (4). Constants depend only on lambda_* and b_+. Correct. With (5), the two existence statements are equivalent.

**Verdict, item 2: HOLDS.**

## 3. The fixed-volume remark

At one torus the density e^{-S_beta}/Z_beta relative to Haar satisfies max/min <= e^{2 beta |P|} <= e^{2 b_+ |P|}, since 0 <= S_beta <= 2 beta |P|. Holley-Stroock: Var_mu f <= mu((f - c)^2) <= rho_max Haar((f - c)^2) with c the Haar mean, then Haar Poincare with gap 3 (first eigenvalue of the unit S^3 Laplacian, also the product gap), then Haar(|grad f|^2) <= rho_min^{-1} E(f). So the gap is at least 3 e^{-2 b_+ |P|} for all beta in [0, b_+]. It is uniform on the interval at that volume, and (8) gives (G2) constants there. Hence a refutation needs a sequence of volumes leaving every finite set, with invariant Rayleigh quotients tending to zero. The sentence "Fixed constants can be tested at one volume" is also right.

**Verdict, item 3: HOLDS.**

## 4. Items (9)-(11): the sphere identity, the gap 2, the conditional law, (11)

**Hess V and Delta V.** For a linear function l(x) = h.x restricted to the unit sphere, along the geodesic cos t x + sin t w, l = cos t (h.x) + sin t (h.w), with second derivative -(h.x) at t = 0. So Hess l = -(h.x) g and, for V = -h.x, Hess V = (h.x) g, Delta V = 3 h.x. Correct.

**(9), first equality.** div(e^{-V} |v|^2 a) = e^{-V}[-|a|^2|v|^2 + <grad |v|^2, a> + |v|^2 Delta V], with <grad|grad u|^2, a> = 2 T(a, v). The integral over the closed sphere is 0, so nu_h(|a|^2|v|^2 - 2T(a, v)) = 3 nu_h((h.x)|v|^2) = 3 nu_h(Hess V(v, v)). Correct.

**(9), second equality.** ||T - a (x) v||^2 = ||T||^2 - 2<T, a (x) v> + |a|^2|v|^2, and <T, a (x) v> = T(a, v). Correct; symmetry of a (x) v is not used.

**(10).** The first inequality drops the square. For the gap: the one-sphere Bochner identity gives nu_h((L_h u)^2) = nu_h(||T||^2) + 2 nu_h(|v|^2) + nu_h(Hess V(v, v)) >= (2/3) nu_h(||T||^2) + 2 nu_h(|v|^2). On eigenfunctions lambda^2 >= 2 lambda, so the gap is at least 2, for every h. Correct. Consistency: at h = 0 the true gap is 3 >= 2; for large |h| the law concentrates where Hess V = |h| g, so the true gap grows. No contradiction.

**Conditional law.** Given all links except e, the density of U_e is proportional to exp(beta sum_{p contains e} epsilon_p Re(U_e W_p)), and Re(U_e W) = U_e . conj(W) in R^4 (the inverse orientation gives the same form). So the law is nu_h with h = beta sum_p epsilon_p conj(W_p), a sum of six unit staples times beta. The sphere metric of the factor is the unit round metric used in (9). Correct, for every exterior and every fixed center sign.

**C_d >= -H_d/3.** The e-block of Hess S is the Hessian in U_e of S with the other links frozen. That function is const - h.U_e = const + V. Apply (10) conditionally with u = f(., rest) and integrate. Correct.

**Mixed blocks, (11).** One plaquette's (e, e') block is the bilinear form (v, w) -> beta Re(product with v and w inserted), with operator norm at most beta. Each link has 6 x 3 = 18 occurrences of another link in its plaquettes (with multiplicity at period 2), so the absolute row sum is at most 18 beta. Then |C_m| <= sum B_ee' mu(|grad_e f||grad_e' f|) <= 18 beta E by 2xy <= x^2 + y^2 and symmetry. So Q >= H_d + H_m + 2E - H_d/3 - 18 beta E = (2/3)H_d + H_m + (2 - 18 beta)E >= (2/3)H + (2 - 18 beta)E. With theta = 1/3 and 2 - kappa = 18 b_+, (G2) holds for b_+ < 1/9. Correct. This is the SU(2) analogue of `gap-tu-retry.md` (21), with the single-link square retained.

**Verdict, item 4: HOLDS.**

## 5. Items (12)-(16): chord influence, K, the spectral step, (14), (15), (16)

**(12).** d_Lip(nu_h, nu_h') <= |h - h'|/4 is Corollary V1 (checked HOLDS). For periods at least 3, C_ee' <= beta/4 and the row sum 9 beta/2 are Lemma INF (13) (checked HOLDS); the normalisation exp(-s sum(1 - x_p)) with x_p = Re U_p is the same as (1) here. Period-2 extension: if e and k share n_ek = 2 plaquettes, changing U_k changes two staples, each by exactly |U_k - U_k'| (k occurs once in each plaquette, the other factors are fixed isometries). So |h - h'| <= n_ek beta |U_k - U_k'| and C_ek <= beta n_ek/4. The occurrences sum to 18 per row, so alpha = 9 beta/2 still. Correct. Only parallel pairs can have n_ek = 2.

**K.** Pi_e is conditional expectation given the other links, an orthogonal projection in L^2(mu). K = N^{-1} sum Pi_e is the averaged update P of Lemma DC, acting through the continuous kernel version on continuous functions. It is a positive self-adjoint contraction. Correct.

**(13).** This is Lemma DC (10): osc(P^t f) <= 2 q^t Delta(f), with Delta = D_ch the sum of coordinate chord-Lipschitz seminorms and q = 1 - (1 - alpha)/N. Smooth f has finite seminorms (chord and geodesic distances are comparable). Correct when alpha < 1.

**The spectral argument after (13).** For centered f, mu(K^t f) = mu(f) = 0, so K^t f takes values on both sides of 0 and ||K^t f||_inf <= osc(K^t f). Then 0 <= <f, K^t f> <= ||f||_1 ||K^t f||_inf <= 2 ||f||_1 D_ch(f) q^t. The lower bound uses K >= 0. If the spectral measure of f put mass c > 0 on [q + eps, 1], then <f, K^t f> >= c (q + eps)^t, which beats C q^t for large t. So the spectral projection E_K([q + eps, 1]) kills every centered smooth f. These are dense in the centered subspace, and the projection is bounded, so it kills the whole centered subspace. K preserves constants and their complement. Hence K <= qI on the complement. Correct.

**(14).** mu(Var_e f) = <f, (I - Pi_e) f>, so sum_e mu(Var_e f) = N <f, (I - K) f> >= N(1 - q) Var f = (1 - alpha) Var f. Applied to f - mu(f). Correct.

**(15).** Conditional (10): Var_e f <= (1/2) nu_h(|grad_e f|^2). Integrate and sum: sum_e mu(Var_e f) <= E(f)/2. So E >= 2(1 - alpha) Var = (2 - 9 beta) Var. Correct, for every f, invariant or not, and with center signs (Corollary V1 holds for every field).

**(16).** On [0, 1/5]: lambda_* = 2 - 9/5 = 1/5, b_+ = 1/5. delta = (1/5)/(2(1/5 + 24/5)) = (1/5)/10 = 1/50. theta = 49/50, kappa = 1/10. Exact. The direct Poincare bound is 1/5. Correct. Only b_+ enters (8); the inclusion of beta = 0 is harmless.

**Verdict, item 5: HOLDS.**

## 6. Items (17)-(21): the sphere Lemma L and the reconstruction paragraph

**B in (17).** The diagonal block of Hess S at e is Hess V_e = (h.U_e) g, with norm at most |h| <= 6 beta. The off-diagonal blocks have norms at most beta n_ee'. So B is symmetric (the norm of a transpose), entrywise nonnegative, zero beyond graph distance 1, with row sums at most 6 beta + 18 beta = 24 b_+. Correct.

**(19).** I re-derived it. In the product, (1/2) Delta_j |grad_e u|^2 = |grad_j grad_e u|^2 + <grad_e u, grad_e Delta_j u> for j != e (flat directions for a T_e-valued field), and for j = e the one-sphere Bochner adds Ric_e = 2|grad_e u|^2. The drift parts give <grad_e u, grad_e <grad S, grad u>> - (1/2)<grad S, grad |grad_e u|^2> = sum_j grad_e grad_j S(grad_e u, grad_j u), after the two Hess u(grad S, grad_e u) terms cancel. So (1/2) A|w_e|^2 = sum_j |grad_j w_e|^2 + 2|w_e|^2 + <w_e, grad_e A u> + sum_j grad_e grad_j S(w_e, w_j). With d_t u = A u, (d_t + L)|w_e|^2 = 2<w_e, grad_e A u> - A|w_e|^2, which is (19). The -4 is 2 x Ric_e. Correct.

**Chain rule and the comparison.** With phi_e = (|w_e|^2 + eps^2)^{1/2} and psi = |w_e|^2, L phi = phi^{-1}(L psi)/2 + |grad psi|^2/(4 phi^3), and |grad psi|^2 <= 4|w_e|^2 sum_j |grad_j w_e|^2. So the gradient terms total at most phi^{-1}(|w_e|^2/phi^2 - 1) sum_j |grad_j w_e|^2 <= 0. The Ricci term is -2|w_e|^2/phi <= 0. The rest is at most sum_j B_ej |w_e||w_j|/phi <= sum_j B_ej phi_j. So (d_t + L) phi_e <= sum_j B_ej phi_j. Correct.

The note's comparison paragraph ("at a first positive maximum ... prevent a crossing") is a sketch. The standard complete form: put d_e = e^{-lambda t}(phi_e - z_e(t)) with lambda > max row sum of B. Then (d_t + L) d_e <= sum_j B_ej d_j - lambda d_e. At the first time a level eta > 0 is reached by max_{e,x} d_e, the left side is >= 0 (spatial maximum: Delta <= 0, gradient 0; time derivative >= 0), and the right side is <= (row sum - lambda) eta < 0. Contradiction. The initial order holds: phi_e(0) <= ||grad_e F||_inf + eps = z_e(0). B_ee >= 0 also enters the right side; nonnegativity of all entries, not only off-diagonal ones, is what is used. With this completion (20) follows as eps -> 0. Precision remark, not a change.

**Path bound.** (B^k)_ei != 0 needs r(e, i) <= k, and row sums of B^k are at most (24 b_+)^k. So sum_i e^{r(e,i)} (e^{tB})_ei <= exp(24 e b_+ t) <= e^{vt}. Hence (e^{tB})_ei <= e^{-r(e,i) + vt} and ||grad_e P_t F||_inf <= D(F) e^{-r(e,X) + vt}. Correct.

**(21) and (18).** d/dt mu(P_t F . G) = -mu(<grad P_t F, grad G>) by reversibility; integrate and use mu(P_T F) = mu(F). Correct. With T = r/(2v): the integral is at most D(F) D(G) e^{-r}(e^{vT} - 1)/v <= v^{-1} D(F) D(G) e^{-r/2}. P_T preserves invariance; the invariant gap gives |Cov(P_T F, G)| <= e^{-kappa T} sqrt(Var F Var G) <= ||F||_inf ||G||_inf e^{-kappa r/(2v)}. Overlap: T = 0. Correct. The torus link graph is connected, so the "disconnected components" sentence is idle.

**Fixed-spacing implication.** Covariances of fixed local continuous F, G pass to local limits; constants do not depend on the periods; r grows at least like lattice separation minus a constant. Correct.

**Reconstruction paragraph (conditional).** Granted a reflection-positive limit state and the reconstruction from local invariant functions, the matrix element of T^n between centered vectors is Cov(Theta F, tau_n F), bounded by (18) by C_F e^{-mn}. The spectral measure of the positive contraction then has no mass on (e^{-m}, 1], and centered local vectors are dense in the vacuum's complement. So the Hamiltonian has no spectrum in (0, m) and a simple vacuum. Correct as a conditional statement; it is the same moment argument as `gap-ac-lat.md` line 40. The note states the premises and does not identify stochastic and Euclidean time.

**Verdict, item 6: HOLDS** (precision remark: the maximum-principle comparison needs the standard e^{-lambda t} shift, supplied above).

## 7. Items (22)-(24): the central configuration and the attained influence

**Every plaquette is -I.** With s_mu(x) = (-1)^{sum_{lambda < mu} x_lambda} and mu < nu: s_mu(x + nu) = s_mu(x) and s_nu(x + mu) = -s_nu(x). So U_p = s_mu(x)(-s_nu(x)) s_mu(x) s_nu(x) I = -I. Even periods make s well defined. Correct.

**(22).** Left translates U e^{tX} of one-parameter subgroups are geodesics of the bi-invariant round metric, with speed |X|. The central factors commute out: U_p(t) = -e^{tX_1} e^{tX_2} e^{-tX_3} e^{-tX_4}. To second order, Re(prod e^{t sigma_i X_i}) = 1 - (t^2/2)|sum sigma_i X_i|^2, because X_i^2 = -|X_i|^2 and Re(X_i X_j) = -X_i . X_j. So 1 - q_p = 2 - (t^2/2)|(dX)_p|^2 and Hess S(X, X) = -beta sum_p |(dX)_p|^2. Correct.

**Test vector and (23).** With eps(x) = (-1)^{sum x}, eps(x + mu) = -eps(x), so (dX)_{mu nu} = eps[a_mu - a_nu + a_mu - a_nu] T = 2 eps (a_mu - a_nu) T. For a = (1, -1, 0, 0) the six squared differences are 4, 1, 1, 1, 1, 0: sum 8. Per site, sum_p |dX|^2 = 4 x 8 = 32 and sum_mu |X_mu|^2 = 2. Ratio 16. So (Ric + Hess S)(X, X) = (2 - 16 beta)|X|^2, negative for beta > 1/8. Correct. (16 is the largest eigenvalue of d*d on 1-forms, at momentum (pi, pi, pi, pi) with sum a_mu = 0; the note does not need this.)

**Invariant gradients vanish there.** Global conjugation fixes the central configuration and acts on each tangent copy of the imaginary quaternions by SO(3), which has no nonzero fixed vector. An invariant f has an invariant gradient there, so it is 0. Correct. So (23) is not a counterexample to (G2), as stated.

**5.2 and (24).** Each plaquette through e has two side links and one opposite parallel link: 12 + 6 = 18 neighbours, each in exactly one of those plaquettes for periods at least 3. All side links I, three opposite links -I and three I: the six staples are three +I and three -I, so h = 0 and the conditional law is Haar. Varying one neighbour along a unit-speed geodesic changes one term of h with derivative of norm beta, in direction w. For the chord-1-Lipschitz test function x . w, d/ds nu_{h(s)}(x . w) = Cov_Haar(x . w, x . h') = beta Haar((x . w)^2) = beta/4. The chord displacement over s tends to 1. So the optimal constant C_ek is at least beta/4. With the upper bound (12) it equals beta/4, and the optimal row sum is 18 x beta/4 = 9 beta/2. Correct. The conclusion is scoped right: the worst-exterior, chord-metric, one-link row-sum condition alpha < 1 stops at beta = 2/9. This does not exclude other metrics, block updates or column-sum versions; the note claims none of those.

**Verdict, item 7: HOLDS.**

## 8. The plaquette test, (25), (26), (27)

**Plaquette test.** As a function of one link, q_p = U_e . W with W a unit vector, so |grad_e q_p|^2 = 1 - q_p^2, and over four links |grad q_p|^2 = 4(1 - q_p^2). Correct. Conditioned on the other links, the density of U_e relative to Haar is e^{h.x}/z(h) >= e^{-2|h|} >= e^{-12 beta}, and Haar(q_p^2) = Haar((x . W)^2) = 1/4. So mu(1 - q_p^2) >= (3/4) e^{-12 beta}, and E(q_p) >= 3 e^{-12 beta}, Var(q_p) <= 1. Correct. Wording: the conditioning must be done for each of the four edges in turn (one per term of 4(1 - q_p^2)); the note says "one edge", which gives the bound for one term only. Precision remark.

**Delta A = 12 sum q_p?** Yes. A linear function on the unit S^3 has Delta(x . W) = -3 x . W, and q_p is such a function in each of its four links, so Delta q_p = -12 q_p and Delta A = -sum Delta q_p = 12 sum q_p. The sign is right.

**(25).** L_beta A = -12 sum q_p + beta |grad A|^2, and mu(L_beta A) = 0. So beta mu(|grad A|^2) = 12 mu(sum q_p) = 12 |P| p'. Var(A) = Var(sum q_p) = |P| p''. The ratio is 12 p'/(beta p''). Correct for beta > 0. With (5), (G2) implies p'' <= 12 p'/(beta kappa). Correct as a necessary condition.

**(26).** By (9) conditionally, C_d = (1/3)(R - H_d), with a = grad_e S. So Q = H_d + H_m + 2E + (R - H_d)/3 + C_m = (2/3) H_d + H_m + R/3 + 2E + C_m. Correct.

**(27).** With delta = 1 - theta, (4) is (2/3)H_d + H_m + R/3 + 2E + C_m >= delta(H_d + H_m) + kappa E, which is (27). So (27) is an exact rewrite of (G2) for theta in (0, 1), not a reduction. The note says so ("not a new solved reduction"). Correct.

**Remark.** The sentence "No probability estimate for a bad configuration can replace (27)" is a heuristic. It is placed under OPEN and proves nothing. Bad-set arguments with test-function-dependent weights are not excluded by any argument in the note. It should read as a judgement, not a claim. Precision remark.

**Verdict, item 8: HOLDS** (two precision remarks).

## 9. Section 6: (28), (29), the binary icosahedral remark

**(28).** On unit circles Ric = 0, so Q = H + C and (4) becomes C >= -theta H + kappa E. Correct. At beta = 0, C = 0; on a flat torus of unit circles a mean-zero f has H = sum |k|^4 |f^_k|^2 >= sum |k|^2 |f^_k|^2 = E (integer k != 0). So theta H >= theta E >= kappa E when kappa <= theta. This matches the route-B correction in `gap-tree-check-opus.md` Section 4.

**(29).** Theorem V of `gap-tu-retry.md` (checked HOLDS) gives gamma_M -> 0 at fixed beta >= 2^14. The invariant gap is attained by a smooth invariant eigenfunction f_M (discrete spectrum). Q = gamma_M E, so C = gamma_M E - H. Then C + theta H - kappa E = (gamma_M - kappa)E - (1 - theta)H < 0 when gamma_M < kappa, since E > 0 and H >= 0. Correct, for every theta < 1 and kappa > 0 once M is large. Q = gamma_M E also violates Q >= kappa E. The note keeps the scope: a Villain theorem, the Wilson cosine case not imported, and the fixed-action obstruction of that source's Section 3 cited, not rebuilt.

**Binary icosahedral group.** Counting measure on 120 points has no tangent bundle, no Levi-Civita Hessian and no Laplacian; (3) and (9) are not defined. Extension-dependence of ambient derivatives is right. This is inapplicability, as stated. Correct.

**Verdict, item 9: HOLDS.**

## 10. Is the RESULT line fair?

The RESULT line: "OPEN at order one; proved (G2) in the existing beta<2/9 range, its equivalence to a uniform invariant Langevin gap, and the sphere locality bridge; the joint estimate (27) remains missing."

- "(G2) in the existing beta < 2/9 range": proved on every compact interval with b_+ < 2/9, from Corollary V1, Lemma DC and Lemma INF (all checked HOLDS) plus (10), (14), (15) and (8). The constants degenerate as b_+ -> 2/9. "Existing" correctly signals that no new range is claimed. Fair.
- "Equivalence": Section 2, item 2. Fair.
- "Sphere locality bridge": (18), item 6. Fair; it is conditional on a uniform gap, which the line implies by "bridge".
- "(27) remains missing": true, and (27) is equivalent to (G2), as the body says. The RESULT line does not call it a reduction. Fair.
- The line claims nothing new at order one, no twist seed, no (FQ) or (V). This matches Section 7.

**Verdict: the RESULT line is fair.**

## Verdict table

| Item | Content | Verdict | Remark |
|---|---|---|---|
| 1 | (1)-(5): Ric = 2g, sign of L, Q = H + 2E + C, (G2) = (4), spectral implication; metric remark | HOLDS | |
| 2 | (6) diagonal q_p|v_e|^2, mixed |v_e||v_e'|, factor 4; (7) with 24 beta; (8) | HOLDS | |
| 3 | Fixed-volume uniformity on a compact interval | HOLDS | gap >= 3 e^{-2 b_+ |P|} by Holley-Stroock |
| 4 | (9) divergence identity, Hess V = (h.x)g, Delta V = 3h.x; (10) gap 2 for every h; conditional law nu_h; (11) with 18 beta | HOLDS | |
| 5 | (12) incl. period 2; K; spectral step K <= qI; (14); (15) 2 - 9 beta; (16) theta = 49/50, kappa = 1/10 | HOLDS | |
| 6 | (17)-(21): (19) with -4|w_e|^2, (20), path bound, (21), (18); reconstruction (conditional) | HOLDS | precision: the comparison needs the e^{-lambda t} shift, lambda > max row sum of B |
| 7 | (22), (23) with 2 - 16 beta; vanishing invariant gradients; (24) beta/4 attained, alpha = 9 beta/2 | HOLDS | |
| 8 | Plaquette test; Delta A = 12 sum q_p (yes); (25); (26); (27) | HOLDS | precision: condition on each of the four edges; "no probability estimate can replace (27)" is a heuristic |
| 9 | (28); (29) Villain failure; binary icosahedral inapplicability | HOLDS | |
| 10 | RESULT line | FAIR | |

No item FAILS. No correction changes a constant, a threshold or a conclusion.

RESULT: Every numbered statement of gap-gamma2-astra.md holds on a hand re-derivation (the Bochner identity and the equivalence of (G2) with a volume-uniform invariant gap, (G2) for b_+ < 2/9 with theta = 49/50 and kappa = 1/10 at beta <= 1/5, the sphere Lemma L, the sharp tests (23)-(24), (25)-(27) and the Villain failure (29)), with no FAILS and three precision remarks, and the RESULT line is fair.
