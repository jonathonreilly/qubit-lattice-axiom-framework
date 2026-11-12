# Check of library/gap-shape-exercise-astra.md (FINISH row 824), by Claude Opus 5.5, line by line

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `eb89fb1396d7ef44e6a02aee6cb3a387f719b4f3` (pull --ff-only: already up to date).
- Target: `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-shape-exercise-astra.md`, 900 lines, by Codex gpt-6-astra max (FINISH row 814). Steps 2 to 9 (lines 141-900) read in full; lines 1-140 read for the contract.
- Context: `library/gap-gamma2-astra.md` Sections 1-3 (lines 73-347) and its check `library/gap-gamma2-check-opus.md` (all).
- Method: every identity re-derived by hand. No numerical run, not even a GUIDE run. No repository file edited.
- Provenance: one reading by a model of a different provider from the author. It is not an audit.

## 1. Lemma D1, (D1)-(D8)

**Metric (D2).** Put x = q_0, q_vec = r omega, r = (1 - x^2)^(1/2), omega in S^2. Then dr = -x dx/r, so |dq|^2 = dx^2(1 + x^2/r^2) + r^2 dOmega^2 = dx^2/r^2 + r^2 dOmega^2. The volume factor is (1/r) r^2 = r. Check: 4 pi times the integral of r over [-1,1] is 2 pi^2. The Laplacian is (1/r) d_x(r^3 d_x) + r^(-2) Delta_(S^2) = r^2 d_x^2 - 3x d_x + r^(-2) Delta_(S^2). Check: Delta x = -3x. The density is exp(hx), so V = -hx and <grad V, grad f> = -h r^2 f_x. Hence L_h = -r^2 d_x^2 + (3x - h r^2) d_x - r^(-2) Delta_(S^2). This is (D2). The rotation of h to (h,0,0,0) is an SO(4) isometry. Correct.

**Completeness.** Restrictions of harmonic homogeneous polynomials give the eigenspaces of -Delta_(S^2) with l(l+1). Every polynomial splits into harmonic pieces times powers of |y|^2. Restricted polynomials are dense (Stone-Weierstrass). L_h commutes with the SO(3) that fixes the h-axis, so each finite-dimensional eigenspace splits into angular sectors. No mode is lost. Correct.

**Sector operator (D3).** With F = r^l u: (r^l)' = -l x r^(l-2) and (r^l)'' = -l r^(l-2) + l(l-2) x^2 r^(l-4). Collecting terms of L_h(r^l u Y_l)/r^l: the u'' coefficient is -r^2; the u' coefficient is 2lx + 3x - h r^2 = (2l+3)x - h r^2; the u coefficient is l + hlx + [l(l+1) - (l(l-2) + 3l) x^2]/r^2 = l + hlx + l(l+1) = l(l+2) + lhx. This is (D3). The weight is r^(2l) e^(hx) r = w_l. In Sturm-Liouville form A_l u = -(1/w_l)(p u')' + (l(l+2) + lhx)u with p = r^2 w_l = e^(hx) r^(2l+3): indeed p'/w_l = h r^2 - (2l+3)x. So A_l is symmetric in L^2(w_l), and <f, L_h f> = <u, A_l u>_(w_l). Correct.

**Ground-state transform (D4).** Put u = phi psi. Then integral of p u'^2 = integral of p phi^2 psi'^2 - integral of (p phi')' phi psi^2 + [p phi phi' psi^2]. Add the potential term. This gives (D4). The two boundary terms are [p u u'] and [p phi' u^2/phi]. Both vanish, because p = e^(hx) r^(2l+3) tends to 0 and u, u', phi, phi', 1/phi are bounded. Correct.

**Regularity.** Near a pole, use q_vec in R^3 as coordinates. The degree-l component of a smooth function on R^3 is |q_vec|^l g(|q_vec|^2) with g smooth (classical). Since r^2 = 1 - x^2, u(x) = g(1 - x^2) is smooth up to x = 1; the same holds at x = -1. I checked the excluded branch: for l = 0 the indicial roots at a pole are 0 and -1/2. The branch s^(-1/2) (s = 1 - x) is square integrable against r dx, but its Dirichlet integral diverges. The note says exactly this (lines 795-796). Correct.

**(D5).** With phi = exp(-alpha h x): A_l phi/phi = -alpha^2 h^2 r^2 - alpha h((2l+3)x - h r^2) + l(l+2) + lhx = l(l+2) + alpha(1-alpha) h^2 r^2 + hx(l - alpha(2l+3)). With alpha = l/(2l+3), in [1/5, 1/2), the linear term is 0 and alpha(1-alpha) > 0. For l >= 1 this is at least 3. Correct.

**(D6).** Differentiate -r^2 u'' + (3x - h r^2) u' = lambda u, using (r^2)' = -2x: -r^2 v'' + 2x v' + (3x - hr^2) v' + (3 + 2hx) v = lambda v. This is (D6). Its principal part equals that of A_1, so it is symmetric for e^(hx) r^3 dx. With phi = exp(-2hx/5): M phi/phi = 3 + (2/5)(3/5) h^2 r^2 + hx(2 - 5(2/5)) = 3 + (6/25) h^2 r^2. v = u' is smooth and nonzero (u constant forces lambda = 0). So lambda ||v||^2 = <v, Mv> >= 3 ||v||^2. Correct.

**Conclusion and sharpness.** Every nonconstant eigenfunction has lambda >= 3. Discrete spectrum, smooth eigenfunctions and kernel = constants hold on the compact sphere with a smooth positive density. Expansion gives (D1). At h = 0, L x = 3x. So 3 is the infimum over h of the gap. "Sharp uniformly in h" means exactly this; the gap at a fixed large h is larger. Correct.

**(D8).** A_0 = -(1/w_0)(w_1 u')' with w_1 = a w_0. One integration by parts gives ||A_0 u||^2_(w_0) = integral of w_1 u' (A_0 u)' = <v, M v>_(w_1), and integral of a|u'|^2 w_0 = ||v||^2_(w_1). Then (D4) with phi = e^(-2hx/5) and phi^2 |(v/phi)'|^2 = |v' + (2h/5) v|^2 gives (D8). The angular form identity follows the same way with |u' + alpha h u|^2. Correct. (D8) is a Gamma_2-type form; it is stronger than needed and holds for every smooth radial u.

**(D7).** The conditional law of one link is exp(H_e . q_e) times Haar, for every exterior and every center sign (checked in `gap-gamma2-check-opus.md` item 4). Integrate Var_e f <= (1/3) nu_h(|grad_e f|^2) and sum. If sum_e mu(Var_e f) >= g Var f, then E >= 3g Var. Correct. Combined with (14) of `gap-gamma2-astra.md` this gives 3(1 - 9beta/2): a better prefactor, the same endpoint 2/9. Step 6 says this. Correct.

**Verdict, item 1: HOLDS.**

## 2. Route C, (C1)-(C7)

**Gauge vectors.** With U_e -> g_s U_e g_t^(-1), the infinitesimal action of a in Im H is a U_e at the source and -U_e a at the target. Each map J_ve: Im H -> T_(U_e) S^3 is a bijective isometry, since T_U S^3 = (Im H) U = U (Im H). Invariance of f gives sum_(e incident v) <g_ve, a> = 0 for all a. Correct.

**Connection identity.** At the source, the ambient derivative of X_a(U) = aU along X_b is abU = -(a.b)U + (a x b)U. Its tangent part is X_(a x b). At the target, Y_a(U) = -Ua, and the derivative along Y_b is U b a, with tangent part U(b x a) = -U(a x b) = Y_(a x b). So nabla_(Jb)(Ja) = J(a x b) at both ends. Also [a,b] = 2 a x b. Correct.

**Row sums.** Differentiate df(K_v^a) = 0 along J_ve b. In a product the fields on other factors have zero covariant derivative. So sum_j <b, B_ej a> + <g_ve, a x b> = 0. Now <g_ve, a x b> = b . (g_ve x a) = <b, [g_ve]_x a>. Hence sum_(j incident v) B_ej = -[g_ve]_x. Correct. B_ej^T = B_je by symmetry of the Hessian.

**Skew parts and (C2).** B_ee is a Hessian block, so symmetric. K_ej = (B_ej - B_je)/2 is skew in (e,j). The skew part of the row-sum identity gives C_e = sum_(j != e) K_ej = -[g_ve]_x, and sum_e C_e = -[sum g_ve]_x = 0. For (C2): P_ej = (C_e - C_j)/D is antisymmetric with row sums ((D-1)C_e + C_e)/D = C_e. The residual R = K - P is antisymmetric with zero row sums, hence zero column sums. Then sum <R_ej, C_e - C_j> = sum_e <row sum, C_e> - sum_j <column sum, C_j> = 0. The norm of P is D^(-2)(2D sum ||C_e||^2 - 2||sum C_e||^2) = (2/D) sum ||C_e||^2. Correct. Precision remark: the orthogonality uses the zero column sums, which come from antisymmetry; the note cites only the row sums.

**HS norm and A_f.** ||[g]_x||_HS^2 = 2|g|^2. ||B_ej||_HS = ||H_ej||_HS and ||B_ej||^2 >= ||K_ej||^2 (sym/skew are HS-orthogonal). So at v: sum_(e != j at v) ||H_ej||^2 >= (4/D) sum_(e at v) |g_e|^2. In a simple graph two distinct links share at most one vertex, so summing over v counts each adjacent ordered pair once and each link twice. A_f >= (8/D) e_f, and D = 8 on the 4D torus. Correct (periods at least 3 make the graph simple; the note assumes this).

**Neighbourhood and matching.** For e = (0, e_1), W = {-e_1, 2e_1, +/-e_nu, e_1 +/- e_nu : nu = 2,3,4}: 7 + 7 = 14 vertices, distinct when every period is at least 4 (-e_1 = 2e_1 at n_1 = 3). Each z has exactly one link to {0, e_1}: a second one would need a difference of 2e_1 to be a unit vector, so n_1 <= 3. Edges inside W: e_nu with e_1 + e_nu and -e_nu with e_1 - e_nu (difference e_1); -e_1 with 2e_1 iff 3 = +/-1 mod n_1, i.e. n_1 = 4 at periods at least 4; e_nu with -e_nu needs 2 = +/-1 mod n_nu, false at n_nu >= 4. All other differences have two nonzero coordinates or a coordinate +/-2 in a direction of period at least 4. So the induced graph is a matching. Correct.

**(C3).** The field K_z^a involves only links at z, and e is not one of them. So Hess f(w, K_z^a) = 0 for every w in T_e: sum_(k at z) H_ek J_zk = 0. This is (C3). The 7 links k != j(z) at z are not adjacent to e, since j(z) is the only link from z to {0, e_1}. Correct.

**BB* bound.** B maps the array (H_ek), k not adjacent to e and touching W, to ((BH)_z)_z. BB* has diagonal block sum_k J_zk^* J_zk = 7I. An off-diagonal block needs a link k with both ends z, z' in W, that is a matching edge, and equals right multiplication by J_(z'k)^* J_(zk), an isometry of Im H (J_(z'k) is a bijective isometry, so J^* = J^(-1)). Each 2 x 2 block [[7I, T], [T^*, 7I]] has norm at most 8; isolated vertices give 7. The z -> j(z) map is a bijection from W onto the 14 links adjacent to e. So sum_(j ~ e) ||H_ej||^2 = ||BH||^2 <= 8 sum_(k not ~ e, k != e) ||H_ek||^2. Summing in e gives A_f <= 8 N_f, so h_m = A_f + N_f >= (9/8) A_f >= (9/8) e_f. This is (C4). Correct, pointwise, on the full product manifold.

**(C5).** For fixed exterior, the e-block of the product Hessian of f is the Hessian of the restricted function, and the e-block of Hess S is Hess V_e. The one-sphere Bochner identity, integrated, gives mu((L_e f)^2) = mu ||H_ee||^2 + 2 mu |grad_e f|^2 + mu Hess_e S(grad_e f, grad_e f). Summing gives H_d + 2E + C_d. Subtracting from Q = H + 2E + C (`gap-gamma2-astra.md` (3)) leaves H_m + C_m. Correct. The gap 3 of D1 gives lambda^2 >= 3 lambda on each conditional spectrum, so sum_e mu((L_e f)^2) >= 3E. Correct.

**Mixed bound.** Each ordered mixed block of beta eta_p q_p has operator norm at most beta (`gap-gamma2-astra.md` (6)). Per plaquette, sum over 12 ordered pairs of |g_e||g_j| = (sum |g_e|)^2 - sum |g_e|^2 <= 3 sum_(e in p) |g_e|^2. Six plaquettes per link give C_m >= -18 beta E. Correct; it matches the row sum 18 beta of (11) there.

**(C6).** Q >= 3E + (9/8)E - 18 beta E = (33/8 - 18 beta)E. Positive iff beta < 33/144 = 11/48. The spectral step is that of `gap-gamma2-astra.md` (5). Center signs enter only through |eta_p| = 1, and the twisted law is still gauge invariant. Correct for all periods at least 4.

**(C7).** At a = 3 the shapes are (3,3,c,d), c,d in {3,6}: four shapes. The largest has 324 sites and 6 x 324 = 1944 plaquettes. The log-density relative to Haar lies in an interval of length 2 beta |P| <= 3888 beta. Product Haar has gap 3. Holley-Stroock as written gives 3 e^(-3888 beta). For a >= 4 all periods are at least 4, since c, d >= a. So (C7) holds on every compact I in (0, 11/48). Arithmetic: 11/48 - 2/9 = 33/144 - 32/144 = 1/144; 33/8 - 18(9/40) = 165/40 - 162/40 = 3/40; 2/9 < 9/40 < 11/48. Correct.

**Consistency remark (by hand).** C6 dominates the old bound 2 - 9 beta on all of [0, 11/48), since they cross at beta = 17/72 > 11/48. No contradiction with the sharp 2/9 threshold of `gap-gamma2-astra.md` 5.2: that threshold concerns the worst-exterior chord row sum, not the invariant Rayleigh quotient.

**Verdict, item 2: HOLDS** (precision remark on the orthogonality step of (C2)).

## 3. Route A, (A1) and its operator realization

**Positivity.** If alpha_i <= 0 then w_i - eps alpha_i >= w_i > 0; otherwise eps alpha_i < w_i by the choice of eps. rho has mass 1. So nu_1 is a positive probability measure. Correct.

**Moments.** For 0 <= k <= K, x^k = sum_i x_i^k l_i(x) on the K+1 nodes. So sum_i alpha_i x_i^k = integral of x^k d rho, and the eps-terms cancel. nu_0 and nu_1 have equal moments of orders 0 to K. Correct. Wording: "first K moments, including total mass" means orders 0..K.

**Operator realization.** On C Omega + L^2(nu_1), T = 1 on Omega and multiplication by x on the second summand. T is a positive contraction, with no atom at 1, so Omega is the only eigenvector at 1. A Omega = f = 1 and <Omega, A Omega> = 0, so <A Omega, T^n A Omega> = integral of x^n d nu_1, a truncated correlation. The cyclic subspace of f is the closure of the polynomials, which is all of L^2(nu_1) (Weierstrass plus density of C[0,1]). The spectrum of H = -log T there contains -log y_j -> 0, and x > 0 keeps the logarithm finite. nu_0 gives a gap at least -log q_0. Truncating rho to J atoms and renormalizing gives finite atomic nu_1^(J) with the same moments and gap -log y_J -> 0; one eps works for all large J since alpha_i^(J) -> alpha_i. The Krylov remark is right: K >= 2N+1 fixes G and M, and <p, Mp> = integral of x p^2 d nu_0 <= q_0 <p, Gp> carries over unchanged. The scope sentence (not a Wilson measure) is right. Correct.

**Verdict, item 3: HOLDS.**

## 4. Route B, (B1)-(B4)

**(B1).** U_p = A_p B_p^(-1), so q_p = Re(A_p conj(B_p)) = <A_p, B_p> in R^4. |T_p|^2 = beta(1 + 1 + 2 eta q_p), so |T_p|^2/2 = beta(1 + eta q_p). The Gaussian moment generating function gives integral of exp(Q.T) d gamma = exp(|T|^2/2). Multiplying over p and by e^(-beta|P|) gives (B1). Correct.

**Conditional law and normalization.** The joint mass is Z_m, so the U-marginal is the original twisted Wilson law. Given U, the Q-density is proportional to exp(Q.T - |Q|^2/2), which is N(T(U), I). R = Q - T(U) has conditional law N(0, I) for every U, so R is independent of U. Correct.

**Gauge equivariance.** A_p and B_p both run from x to x + mu + nu, so each transforms as g_x (.) g_(x+mu+nu)^(-1). T_p is linear in them, so it transforms the same way. Left and right multiplication by unit quaternions is orthogonal on R^4 and preserves gamma and Q.T. Correct.

**(B2).** |D T_p(v)| <= sqrt(beta)(|DA_p v| + |DB_p v|) <= sqrt(beta) sum_(e in p) |v_e|. Squaring and Cauchy-Schwarz give 4 beta sum_(e in p) |v_e|^2; six plaquettes per link give ||DT||^2 <= 24 beta. The variance split, the Gaussian Poincare inequality (constant 1) for Q given U, Jensen for grad g, and |a + Mb|^2 <= (1 + ||M||^2)(|a|^2 + |b|^2) give (B2). The Wilson inequality applies to g because g is invariant: g(GU) = E_R F(GU, R + G T(U)) = E_R F(U, G^(-1)R + T(U)) = g(U), by invariance of F and of gamma. Correct. Precision remarks: the note does not state the invariance of g, and the noncompact Q factor needs a stated test class (for example smooth F with polynomially bounded derivatives) to justify differentiating under E_R and to define lambda_ext by closure.

**(B3).** The lower bound is the reciprocal of the constant in (B2). The upper bound restricts the Rayleigh quotient to F = f(U). Correct. The equivalence on a compact beta interval follows. The note says it is not a gap estimate. Correct.

**(B4).** With all U = I, each of the six plaquettes at e has A_p or B_p equal to U_e(s), the other factor equal to I. So T_p'' = -sqrt(beta) I at s = 0. With Q_p = -tI, V'' = -sum Q_p . T_p'' = -6 t sqrt(beta). The curve is a unit-speed geodesic of the product, so this is Hess V(v,v). Ric(v,v) = 2. The sum is 2 - 6t sqrt(beta), and Gaussian Q gives every t positive density. The scope sentence (not an invariant gradient) is right. Correct.

**Verdict, item 4: HOLDS** (two precision remarks on (B2)).

## 5. Step 5 comparisons, Step 9 scope, the U(1) location

**Citations to the context file.** `gap-gamma2-astra.md`:103-111 is the Bochner identity (3); 192-209 is the equivalence (8); 229-347 contain the gap 2, the mixed bound 18 beta, (15) with 2 - 9 beta and the 2/9 range. These match the uses in Steps 4, 5 and 9. The `gap-vmf-lip.md` Theorem V at lines 58-78 is the chord-covariance bound a(|F|) <= 1/4, a different inequality from D1, as stated.

**Prior constants.** I searched the lane at HEAD for 11/48 and 33/8. The only other hits are unrelated (`dr.md`:150, `drlocp.md`:169, `gates/dr-gate.md`, `gates/sr1-gate.md`). Rows 818-825 postdate the exercise's comparison window (rows 743-817). I did not read their outputs for D1 or C4. This is a constant search, not an absence theorem.

**SZZ arithmetic.** Ours is beta tr(U_p)/2 = (beta/2) Re Tr U_p; theirs N beta_S Re Tr U_p. So beta_W = 2N beta_S, which equals N^2 beta_S = 4 beta_S at N = 2. With |beta_S| < 1/48 this gives beta_W < 1/12. Correct for SU(2). The general formula depends on reading "ours" as tr/N; at N = 2 both readings agree.

**Step 6 and Step 8 tables.** D improves only the prefactor with heat-bath contraction (checked in item 1). C survives for periods at least 4 plus the four a = 3 shapes (item 2). 33/8 - 9 = -39/8 at beta = 1/2, and the note correctly says this refutes nothing. A and B failures are as stated (items 3, 4). Correct.

**Step 9 scope.** The claims are: the auxiliary invariant diffusion gap for beta < 11/48 on the task family; (G2) on that family by the existing equivalence (8); the same-measure covariance bound by the existing locality theorem; no comparison of the twist normalizers, no (T), no fixed eta_* rate, no continuum gap. These match what is proved. The RESULT line's "H_m >= 9E/8" needs periods at least 4, which the body states. Fair.

**U(1).** The nonzero row sums in (C2) come only from the connection term J(a x b), that is from the bracket. For U(1) the gauge flows commute, the term vanishes, C_e = 0, and (C2) gives no lower bound. The propagation (C3)-(C4) would still give A_f <= 8 N_f, but there is nothing to propagate. In addition Ric = 0 and the Haar circle gap is 1. So the failure is located at the right step. The binary icosahedral group has no tangent space, so (C1)-(C5) are undefined, as stated. Correct.

**Verdict, item 5: HOLDS.**

## Verdict table

| Item | Content | Verdict | Remark |
|---|---|---|---|
| 1 | D1: metric, (D2), completeness, (D3), (D4) with boundary terms and pole regularity, (D5), (D6) with 3 + (6/25)h^2 r^2, sharpness at h = 0, (D8), (D7) | HOLDS | |
| 2 | Route C: J_ve, connection identity, row sums -[g_ve]_x, (C2), HS norm 2|g|^2, A_f >= e_f, 14-vertex matching, (C3), BB* norm <= 8, (C4) 9/8, (C5), C_m >= -18 beta E, (C6) 11/48, (C7) 1944 / 3888 beta / gap 3 | HOLDS | precision: (C2) orthogonality also uses the zero column sums from antisymmetry |
| 3 | Route A: (A1) positivity, moment matching, operator realization, finite-dimensional approximants | HOLDS | wording: "first K moments" means orders 0..K |
| 4 | Route B: (B1), conditional law, equivariance, (B2), (B3), (B4) | HOLDS | precision: state invariance of g; state the test class on the Q factor |
| 5 | Step 5 comparisons, Step 9 scope, U(1) location | HOLDS | SZZ: beta_W = 2N beta_S in general, = N^2 beta_S only at N = 2 |

No item FAILS. No correction changes a constant, a threshold or a conclusion.

RESULT: Every checked statement of gap-shape-exercise-astra.md holds on a hand re-derivation (the tilted-S^3 gap 3 uniform in h, the gauge reserve h_m >= (9/8)e_f at periods at least 4, (C6) with endpoint 11/48 and (C7) on the task family, the moment counterexample A1, and the Gaussian lift B1-B4), with no FAILS and four precision remarks.
