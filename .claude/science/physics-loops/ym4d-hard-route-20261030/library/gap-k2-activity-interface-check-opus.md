lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T05:05Z

# Check of rows 1480 and 1485 (row 1488)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, at commit f7e33266f. Cross-provider check of two gpt-6.2-astra max rows. Not an audit.

## Plan

- (A) `library/gap-k2-integrated-activity-astra62.md` (row 1480), line by line: contour check on the two period-two fields; compact pinned law; normalized fine-block activity; staggered Cartan source at angle 1/8; exact vacuum and curvature extraction; integrated quartic at fluctuation scale and residual 19 h^4/(729 x); the claim that the violating activity survives the extractions and the field weight of row 1468.
- (B) `library/gap-k2-wilson-interface-astra62.md` (row 1485): eight conditional laws, counts 352 and 312; reduction to four outward rows; lower bound 49/225; positive opposite-face correlation; bound 16 r_1^20 e^(-576 beta) above 2^-2024 (counts 108, 102); arm bound J > 6/5, delta > 1/12; upper bound 7 - (2966/495) 2^-822; certificate margins 122/125 and 257/251 with D < 251/250.
- Verdict per part: HOLDS, HOLDS AFTER CORRECTION (repairs named), or FAILS at the first wrong line.
- Exact arithmetic is redone by hand, or in exact rationals (python fractions / sympy) as a check only, never as a proof step.

## Repo search

Searched `library/open-core.md` and FINISH rows 1460-1489 for `19/729`, `4104`, `staggered Cartan`, `integrated activity`, `2966/495`, `257/251`, `122/125`, `49/225`. The only hits are rows 1480, 1485 and 1488-1490 themselves (the claims under check). No earlier check of either row is on file. Inputs read: row 1480 file in full (277 lines), row 1468 file 4.2 (the norm, lines 238-256) and 5.1 (cut 1/2, line 357), row 1478 check Step 1 (the two period-two fields).


## Part A. Row 1480, `gap-k2-integrated-activity-astra62.md`

Every equation below was rederived by hand from the definitions in the file, not by rereading its text. Where the derivation is mine and differs in route from the author's, that is said.

**A1. The two period-two fields against the 384 contours (file line 23). HOLDS.** Different derivation from the author's: the three-face field is the pull-back, under n -> n mod 2, of a connection on the 1-skeleton of the unit 4-cube (forward step from bit 0 to bit 1 uses the label h, from bit 1 to bit 0 uses h^-1, which is the reverse traversal of the same cube edge). A contour 2y -> 2y+xi -> (two mu-steps) -> 2y+2e_mu+xi -> 2y+2e_mu projects to P, e, e^-1, P^-1 in the cube graph, so its holonomy is 1 for any labels. The commuting field has A_mu(n+e_mu) = -A_mu(n) and is invariant under translation by 2, so the middle pair and the legs cancel. Both agree with row 1478 Step 1 (which was also Opus, so this is not a cross-provider confirmation of 1478, only of 1480). The author's remark that the curves have zero Haar measure and give no lower bound on an integrated activity is correct.

**A2. Integrated Wilson vertices (lines 33-74). HOLDS.**
- Expansion x(1 - Re prod e^{g v_i}) = |sum v|^2/2 + g D_p - g^2 L(G) + O(g^3): checked term by term. Order g^2: Re(sum v_i^2/2 + sum_{i<j} v_i v_j) = -|sum v|^2/2. Order g^3: Re v^3 = 0, Re(v_i^2 v_j) = 0, Re(v_i v_j v_k) = -det(v_i,v_j,v_k). Order g^4, the five partitions: G_ii^2/24; G_ii G_jj/4; Re(v_i^3 v_j) = G_ii G_ij giving (G_ii+G_jj)G_ij/6; v_k^2 scalar so G_kk G_ij/2; Re(v1v2v3v4) = G12G34 - (v1 x v2).(v3 x v4) = G12G34 - G13G24 + G14G23. All five agree with L(G).
- Wick factors 9, 3, 3: E[v_ia v_ja v_kb v_lb] = C_ij C_kl + delta_ab (C_ik C_jl + C_il C_jk), summed over a, b in {1,2,3}. Agrees.
- E(D_p D_q) = 6 sum det C_{I,J}: internal contractions vanish (epsilon with two equal colours); for a cross matching pi, sum over colours of eps_a eps_{a o pi^-1} = 6 sgn(pi). Agrees.
- (1 + Delta/2 + Delta^2/8) L at mean m: exact heat-kernel formula for a quartic. Cov formula with 1/j!: standard Gaussian (Hermite) expansion; internal contractions of D_p and of its gradients vanish by the same colour antisymmetry. Agrees.
- Surviving degree-four part sum L(G_p(m)) + (1/2) sum <grad D_p, C grad D_q>, and on a common Cartan axis grad D_p = 0 and L = |(dm)_p|^4/24 (the order-four coefficient of e^{g (sum s_i) n}). Agrees.

**A3. Compact pinned law (lines 76-91). HOLDS (as a representation; it is not used for any bound).** F(v) = E_Haar e^{v q_0}; principal log = Im q * arccos(q_0)/sqrt(1-q_0^2); clipped log has norm at most arccos(-1+delta) <= pi; Bernstein and Taylor uniform on a compact; dominated convergence. Correct and harmless.

**A4. Normalized fine-block activity, (1)-(3) (lines 93-135). HOLDS.** Counts: fine side 8 on a coarse 4^4 torus means 2^4 fine sites per block, a spanning tree of 15 edges, 64 - 15 = 49 free assigned links, 96 assigned plaquettes, 384 = 24 x 16 contours. Haar in exponential coordinates (2 pi^2)^-1 (sin|A|/|A|)^2 d^3A on |A| < pi. (1) is the identity f_B = f_{B,C} + f_{B,H}. (2): the cold-mark coefficient in E prod[1 + lambda_B (f_{B,C}-1) + mu_B f_{B,H}] is E(f_{B,C}) - 1, and the first derivative of the log at zero marks is the same. The pin ratio k_c/k_0 = e^{-kappa(1-Re MV^-1)} F(kappa)/F(kappa|M|) = e^{-kappa(r-Re MV^-1)} h(kappa)/h(kappa r) with h(s) = e^{-s}F(s) = E e^{-s(1-q_0)}, decreasing. The KP self-term necessity |z_X| <= u_X e^{-u_X} <= 1/e is correct, and the field weight 1 + theta x E is at most 1 + 12 x N_b (six coarse plaquettes per site, 1 - Re V_p <= 2).

**A5. Staggered Cartan source, (4)-(6) (lines 137-176). HOLDS.** Recomputed in the abelian (Cartan) picture before tree fixing, with eps(n_1) = (-1)^floor(n_1/2):
- Curvature F_12(n) = A_2(n+e_1) - A_2(n) (A_1 does not depend on n_2): zero on even layers, -2u eps_y on the odd layer; 8 nonflat plaquettes per block; all (1,mu), (2,mu) plaquettes with mu = 3,4 flat. Wilson quadratic 8 x (2u)^2/2 = 16u^2.
- Direction-2 contours: legs cancel (field independent of n_2), middle 2u eps_y. Direction-1 contours: middle -u eps_y for both values of xi_1 (exactly one of the two links lies on the odd layer of block y); legs give xi_2 u (eps_y - eps_{y+e_1}) = 2 xi_2 u eps_y; total +-u eps_y, half each. So M_1 = cos u, M_2 = exp(2Iu eps_y), (QA)_1 = 0, (QA)_2 = 2Iu eps_y. Agrees with (4).
- Gauge potential -Iu eps_y xi_2: tree (internal) links go to zero; crossing direction-2 links become 2u eps, crossing direction-1 links u eps (2 xi_2 - 1); all logs at most 2|u|. Agrees.
- Normal equation: d*dA on a direction-2 link equals F(n-e_1) - F(n) = 2u eps_y on both layers; zero on all other links. Sum_y eps_y (Q dA)_2(y) = (1/8) sum_n eps dA_2(n) (legs cancel under the shift by 2e_2; each fine direction-2 link is the first straight step for one offset and the second for one offset of the block below in direction 2, weight 2/16). Stationarity 2u + (a/8)(2u - t) = 0 gives 2u = a t/(8+a). Since the functional is invariant under gauge maps that are trivial at block bases and positive definite on the slice, this is the mean for every x. Agrees.
- Rate (5): G_B(m) = 8 (alpha t)^2/2 + a((1-alpha)t)^2/2, S_B = 8(1 - cos alpha t), marked pin cost kappa(1 - cos((1-alpha)t)) for c = 2 and zero exponential cost for c = 1 because the normalized kernel at r = |M_1| = cos u costs only h(kappa)/h(kappa r) in [m_delta e^{-kappa delta}, 1]. Agrees.
- (6): Laplace-type lower bound on a ball whose gamma-mass tends to one (covariance C/x on a fixed torus), f_{B,C} >= 0 elsewhere. For |v| <= 1, v^2/2 - 1 + cos v >= v^4 (1/24 - 1/720) = 29 v^4/720 > v^4/25. Agrees.

**A6. Exact vacuum and curvature extraction, (7) (lines 178-206). HOLDS (sketch-level in places, no wrong line found).**
- Quadratic part of the hybrid phase H_t: Wilson 1 - Re W_p = theta^2/2 + ...; marked pin a(|M| - Re MV^-1) = a |v|^2/(|M| + s) with v = (QA - b) + O(2), so a|QA - b|^2/2. The pieces 1 - |M| go to the amplitude through h(kappa)/h(kappa |M|), as the author says. So the Hessian of H_t at zero is sum_D G_D.
- Unique zero of H_0 on the closed chart: I followed the chain (internal links of B identity from flat group plaquettes and the identity tree; internal links of the other blocks zero from the linear curl; crossing plaquettes based in a block equate the eight crossing links of each outgoing face; each contour is one crossing link times internal links; unmarked linear pins force crossing value 0, the marked pin with |M| = Re M at V = 1 forces the common face element to be 1). Every link is internal or crossing, so A = 0. Correct.
- Coercivity H_0 >= c|A|^2 - K: from sum over all D of G_D >= lambda|A|^2, G_B bounded on D_B, S_B >= 0. Correct.
- Two-derivative dominated convergence in s = sqrt(x) t: the derivative bounds K'(1 + |Y|) and the outside-ball estimates are stated rather than written out. I checked the orders: d/ds = g d/dt, the t-dependence enters through |QA - b(t)|^2 and the marked pin phase, each giving x g O(g(|Y| + |s|)) = O(|Y| + |s|). Consistent. Consequence (log j_x)''(0) = o(x); the (8) expansion even gives O(1).
- Remark (not a defect): the extraction subtracts a quadratic form that is nonlocal in b (the Hessian of log J_{B,x} at zero passes through the Gaussian mean map). The test therefore covers every quadratic extraction, local or not, which is stronger than needed.

**A7. Integrated quartic at fluctuation scale, (8) and 19/729 (lines 208-234). HOLDS.**
- Pin amplitude: -k (log h_0)'(k) -> Gamma(5/2)/Gamma(3/2) = 3/2 by w = k(1 - q_0); log[h_0(kappa)/h_0(kappa r)] = (3/2) log r + O((1-r)/kappa). Correct.
- Degree count: with a collinear (Cartan) centre, U_3 and grad U_3 vanish (rotation by pi about an axis perpendicular to I reverses all vectors of an odd polynomial; rotations about I force the gradient to be parallel to I, and the parallel derivative stays in the collinear set). So U_3(s m(1) + eta, s) = s Q(eta) + U_3(eta, 0), Var has degree two in s (the cross covariance is an odd Gaussian moment), and the only s^4 term is U_4(m(1), 1) = degree-four coefficient of Delta_a. Correct.
- Coefficient: degree four of 8[v^2/2 - 1 + cos v] at v = alpha t is 8 alpha^4/24, and a(1-alpha)^4/24 for the pin; at a = 1, alpha = 1/9: (8 + 8^4)/(24 * 9^4) = 4104/157464 = 171/6561 = 19/729. Correct.
- Field-weight remark: x E_whole(V(h/sqrt x)) <= 2 N_b h^2 (N_b coarse (1,2) plaquettes, angle 2h/sqrt x). Correct; the conclusion (no finite c_1 uniform over all h on a fixed torus) follows since x z -> 19 h^4/729 grows faster than 1 + 2 theta N_b h^2.

**A8. The violating activity (9), hot sectors (10), full free energy (11), external bond (lines 236-270). HOLDS.**
- (9): a = 1, t = 1/8: fine angle 2u = alpha t = 1/72; coarse (1,2) plaquette angle 2t = 1/4, chord 2 sin(1/8) < 1/4; |alpha t| = 1/72 and |(1-alpha) t| = 1/9 lie in [-1, 1], so (6) applies: Delta_1(1/8) >= (8 + 8^4)/(25 * 9^4 * 8^4) = 4104/(25 * 9^4 * 8^4). Combined with (7), (1/x) log(1 + z) has this positive liminf. Since 1 + theta x E is polynomial in x, the KP self-term and its field-weighted form fail for all large x. Correct.
- (10): a hot block has an assigned plaquette with |1 - W| >= 1/2, so 1 - Re W >= 1/8; distinct blocks have distinct assigned plaquettes; rate <= -k/8. Correct.
- (11): per-block rate Delta_a(t) at the periodic mean, Z(1)/c_Lambda of log rate zero, power of x from the determinant. Correct. This is the bridge from the fine-block singleton to row 1468's log-rule norm: any centre equal to the Gaussian action plus a quadratic extraction leaves a residual of order x N_b, which no weight 1 + theta x E can absorb.
- External bond, Wilson curvature centre at x = 100: Z(V)/Z(1) = E_{Pi_1} exp{x[(cos t - 1) m_0 + sin t m_I]} >= e^{-x(1 - cos t)} = e^{-1} (conjugation symmetry gives cosh >= 1, and m_0 <= 1 with cos t - 1 < 0). With six plaquettes, 6x(1 - cos t) = 6, so the activity is at least e^5 - 1, and (e^5 - 1)/(1 + 6 theta) >= (e^5 - 1)/7 > 1/e. Correct. Scope note: the extracted coefficient is x itself. That is the right readout to leading order in k for this pin (at k -> 0 the pin forces QA = b, and classical scale invariance of the 4D Wilson action gives x' = x), so the check is meaningful; it is the rough-field statement that a one-bond kink costs at most the pin energy kappa(1 - cos t).
- Next-row formula: in the stripe ansatz, min over v of 8(1 - cos v) + a(1 - cos(v - t)) = 8 + a - |8 + a e^{-it}| = 8 + a - sqrt(64 + a^2 + 16 a cos t). At a = 1: 81 - 8t^2 + (2/3)t^4 under the root; 9 sqrt(1 + eps) with eps = -(8/81)t^2 + (2/243)t^4 gives t^4 coefficient 9(1/243 - 8/6561) = 9 * 19/6561 = 19/729 and t^2 coefficient 4/9 = 4a/(8+a). Correct.

All arithmetic in Part A was done by hand. Memory free was 37 percent at 17:06Z (below the 50 percent rule), so no exact-rational script was run; the constants are short enough that a hand check is complete.

**Verdict A: HOLDS.** No wrong line found. Scope, as the author states it: the refutation is of the integrated activity about the Gaussian centre (full Gaussian action plus any vacuum and quadratic extraction) with row 1468's fixed real cut 1/2 and field weight. It does not test row 1468's tube with a centre that carries the nonlinear action (Wilson-form or the constrained classical minimum), and the elementary reason is visible: at one plaquette e^{-x(1-cos theta)}/e^{-x theta^2/2} = e^{x theta^4/24 + ...}, and the conditional mean forces theta = 1/72 on eight plaquettes per block. Two remarks, neither a defect:
1. The violating fields have coarse angle fixed (1/8) as x grows, outside any Balaban small-field region (which shrinks like g^{1-eps}); the failure belongs to the fixed cut 1/2 of row 1468 combined with a Gaussian centre, as the row says.
2. The external-bond check (e^5 - 1) is a different activity from (9) and does not depend on the staggered source.


## Part B. Row 1485, `gap-k2-wilson-interface-astra62.md`

**B1. Eight conditional laws and the counts (lines 13-31). HOLDS.**
- Counts: C = {0,1}^4 has 4 x 8 = 32 links; each of the eight neighbours C +- 2e_mu has 32 internal links and 8 crossing links (one per vertex of the three-cube face), so 9 x 32 + 8 x 8 = 352. Internal plaquettes 6 x 4 = 24 per box; single-cut plaquettes one per tangential edge of the face cube, 12 per interface; a plaquette with crossing links in two directions needs a site of C + 2e_mu + 2e_nu, absent. So 9 x 24 + 8 x 12 = 312.
- (1): at v = u_*, A^-1 v r_s D r_t^-1 v^-1 = A_st^-1 u_s D_st u_t^-1, the single-cut plaquette loop; q(a v b v^-1) is a homogeneous quadratic in v in R^4, so the symmetric matrix is unique. Agrees.
- (2): no plaquette joins two arms, so the arms are conditionally independent given X; Cov(f(Q_i), g(Q_j)) = integral of K_i f K_j g d mu_C for centred f, g. Agrees.

**B2. Source-face conventions (3)-(5) (lines 34-62). HOLDS.**
- Transport: gauging the eight neighbour boundary vertices by the crossing links makes the crossing weight beta sum q(A_e^-1 B_e) and leaves the crossing values independent Haar. Agrees.
- (4) rederived: with Nbr_st = u_s B_st u_t^-1, k_s = u_*^-1 u_s and w = u_*^-1 v, cyclicity gives q(Nbr^-1 v r_s Cen r_t^-1 v^-1) = q((B^k)^-1 w A^k w^-1), i.e. Q = D(B^k, A^k)(w) = D(A^k, B^k)(w^-1), using q(U) = q(U^-1). Agrees.
- (5): outward Q = D(A,B)(v u_*^-1) with u_* independent Haar gives H_i; inward Q = J[D(A^k,B^k)(. u_*)] and covariance of the law of B under vertex gauges of A gives P_{F_i minus *} H_i (f o J). The P_S are commuting orthogonal projections because L_i(X_{F_i}) and S_C are invariant under central vertex gauges (a gauge at s is absorbed into u_s). Agrees.
- Pivot rotation and the restriction to invariant probes (lines 60-62): read; consistent with the gauge actions; the supremum over invariant probes is legitimate because averaging a probe over a symmetry that fixes the other matrix preserves the cross covariance and does not raise the variance. I did not reconstruct the SO(4) eigenvalue reduction in full detail; it is used only for the remark that mixed coefficients can be tested on eigenvalues, not for any number in the list below.

**B3. Ordering (6) and the reduction to the four outward rows (lines 65-79). HOLDS.**
- Row sums: a positive face sees 3 positive (p), 3 perpendicular negative (m), 1 opposite (o_1); a negative face 3n + 3m + o_1. With n <= p the maximum is 3p + 3m + o_1, attained on the four outward rows.
- Diagonal reflection positivity, rederived: theta (x_mu <-> x_nu) maps the 352-link union to itself and maps positively oriented links to positively oriented links, so no inversion is needed. A link changes x_mu - x_nu by at most 1, so no link joins the strict halves. A mu-nu plaquette with base difference d has corner differences d, d+1, d, d-1, so it meets both strict halves only for d = 0, with two fixed corners and the two length-two paths exchanged by theta; its factor exp(beta U.V) = sum beta^n/n! <U^{(x)n}, V^{(x)n}> is a positive kernel, and V(omega) = U(theta omega) because theta does not invert links. Every other plaquette lies in one closed half or in the fixed plane. So b(F,G) = E[F theta G] is positive semidefinite. Agrees.
- m <= n <= p: projections P_S at sites outside the partner face act trivially on the partner (links of a face have both ends in that face), so they move across; P at sites of I = F cap theta F commutes with theta (theta fixes those sites) and is an L^2 projection, so b(PG, (1-P)G) = E[PG (1-P) theta G] = 0 and b(G,G) >= b(P_{I minus r} G, P_{I minus r} G) >= b(P_I G, P_I G). The probe family is the same for p, n, m because the inward variance of f equals the outward variance of f o J (by (5)). Cauchy-Schwarz for b turns the two-probe supremum into a one-probe supremum. Agrees.
- o_1 <= m: the outward face x_mu = 1 lies in the closed + half, the inward face x_mu = 0 in the closed - half; Cov = b(G_+, theta G_-) <= sqrt(b(G_+,G_+) b(theta G_-, theta G_-)), and after full central gauge averaging (legitimate for this mixed pair, since its inward root o is outside the outward face) each self-pairing is a fully averaged perpendicular pairing, at most m times the variance. Agrees.

**B4. Resolved-plaquette trial, row sum one (lines 81-89). HOLDS.** Each single summand of (1) is a_0 d_0 + a^t R(v) d, with coefficient matrix a d^t; normalized left Gram a a^t/|a|^2; h(a) = a_1^2/|a|^2 - 1/3 has mean zero. Any two distinct central links form a forest and are independent Haar under the gauge-invariant Wilson law, so the face sums have variance 12 s^2 and perpendicular positive faces share four edges: correlation 1/3, three such faces, row sum 1. The author correctly says this probe is a function of the twelve separate summands, not of Q_i, so it does not refute (6).

**B5. Reference comparison (7) and the upper bound 7 - (2966/495) 2^-822 (lines 92-115). HOLDS.**
- Removed counts, recounted. Perpendicular pair (faces x_mu = 1, x_nu = 1): a central plaquette avoids the face x_mu = 1 iff its plane omits mu and x_mu = 0, so exactly one of the 24 avoids both faces: 23. Each neighbour box: 24 - 6 = 18 plaquettes touch its face (avoiding needs plane without the normal direction and the far layer: 3 x 2 = 6), two boxes 36. Selected crossings 2 x 12 = 24. Other six interfaces: faces x_mu = 0 and x_nu = 0 meet the read central edges in one square each (4 + 4); the four faces x_lambda = 0, 1 (lambda not mu, nu) meet them in two squares sharing one edge (7 each). 23 + 36 + 24 + 36 = 119. The same count holds for the inward and mixed perpendicular pairs by the coordinate reversals that preserve the star. Opposite pair: 24 + 36 + 24 + 6 x 8 = 132.
- Reference coefficients: under nu the read links are independent Haar. The outward field is symmetric in the twelve edges (B i.i.d. Haar), so in the Hoeffding (ANOVA) decomposition the shared fraction at order k is C(4,k)/C(12,k) <= 1/3. For an inward face, proper subsets of the shared square are forests, rooted vertex gauges act transitively on them, so only the order-four component on the full square survives, giving 1/C(12,4) = 1/495. Opposite faces read disjoint sets: 0.
- Transfer: Var_mu(f +- g) >= a Var_nu(f +- g) >= a(1 - rho_nu)(Var_nu f + Var_nu g) >= (a/b)(1 - rho_nu)(Var_mu f + Var_mu g); the smaller sign gives rho_mu <= 1 - (a/b)(1 - rho_nu), a/b = e^{-2 beta N}. Agrees.
- Constants: e < 11/4 so e^2 < 8 and e^{-y} > 2^{-3y/2}; 3 beta 119 = 821.1 and 3 beta 132 = 910.8, so e^{-2 beta 119} > 2^-822 and e^{-2 beta 132} > 2^-911. With o_1 <= m: R <= 3(1 - (2/3)eps) + 4(1 - (494/495)eps) = 7 - (990 + 1976)/495 eps = 7 - (2966/495) eps, eps = 2^-822. Agrees.

**B6. Lower bound 49/225 (lines 118-154). HOLDS.**
- Phi_i = E[R_i | internal links, all r_s]: the pivot u_* enters only through e^{u_*^t Q_i u_*} (no corner plaquettes), so E[S_cut | ...] = M(Q_i); T_i is a function of Q_i. So Phi_i is a probe of Q_i.
- T_i = sum q(A_e) q(B_e) from E_v q(X v Y v^-1) = q(X) q(Y). Under gauges at the face vertices, q(A_e), q(B_e) become h.a, h.b with the same relative gauge h = g_s^-1 g_t; relative gauges of two distinct edges are independent (two edges form a forest), which suffices for variances. E[R_i | gauge orbit] = sum c_e/4 - S_cut/4 = 0, so Var R_i = sum_e E[(1 + 2c^2)/24 - c^2/16] = sum_e E(2 + c^2)/48 <= 3/4. Agrees.
- Y on the shared square: mean 0, Var 4(1/8 - 1/16) = 1/4; shared-edge covariance 3c/24 - c/16 = c/16; E[S_cut Y] = 0; so E[Phi_i Y] = c_bar/4. Phi_i lives on the closed + half of theta (mu <-> nu) and theta Phi_i = Phi_j; Y is theta-fixed; Cauchy-Schwarz for b gives E[Phi_i Phi_j] >= (c_bar/4)^2/(1/4) = c_bar^2/4. Agrees.
- c_bar >= r_1(beta): reflection through x_nu = 1/2 (nu tangential to the selected crossing plaquette) maps the star to itself (C +- 2e_nu exchange, the other boxes have x_nu in {0,1}); the nu-bonds through the plane form a matching; Z(t)/z(t) is a sum of nonnegative squares times products of r_j(t), each nondecreasing (I_{k+1}/I_k is the mean of x under e^{tx}(1-x^2)^{k-1/2}). Agrees with 1348 line 249, checked HOLDS in 1350.
- r_1 = beta/(4 + beta I_3/I_2) from I_1 - I_3 = (4/beta) I_2; I_3/I_2 < beta/6 termwise (1/(l+3) <= 1/3); at beta = 23/10: (23/10)(600/2929) = 1380/2929, and 20700 > 20503. (Floating estimate as guide only: r_1(2.3) is about 0.479.)
- rho >= (c_bar^2/4)/(3/4) = c_bar^2/3 > (7/15)^2/3 = 49/675, three positive partners: 3p > 49/225. With m >= o_1 > 2^-2024 the stated 49/225 + 4 2^-2024 < R follows. Agrees.
- Nondegeneracy (Q = +-12 beta I gives Phi = +-9) and the limitation bound < 1/3 for this family: read, consistent.

**B7. Positive opposite-face correlation and (13) (lines 203-230). HOLDS.**
- Probe B_i(0) = 1/h_1(Q_i); its conditional field on both opposite faces is F = z_2/L(A) (J-invariant and central-gauge invariant, so the inward projection does nothing). E B_i(0)^2 <= Z_i(-1)/Z = 1 by the checkerboard sign flip of the eight crossing links (reverses the twelve crossing traces, touches no other plaquette).
- Reflection through x_mu = 1/2: the star is symmetric (C +- 2e_mu exchange). Slice edges: 7 three-cubes x 12 + 6 neighbours x 4 crossings at that layer = 108; one midplane plaquette per slice edge (inside a box, or a single-cut plaquette of an interface lambda not mu); (312 - 108)/2 = 102 per half, so inf Psi/sup Psi >= e^{-204 beta}.
- l = Cf (the crossing kernel and the midplane kernel are the same normalized one-link convolution on the twelve central face edges); 0 < f, l <= K = e^{24 beta} (z_2 >= 1 by Jensen); <f, q_sq> >= r_1 (1348 line 249: character = 2q, pairing >= 2 r_1), C q_sq = r_1^4 q_sq, ||q_sq||^2 = 1/4, hence ||a - l||^2 >= r_1^10/(1/4) = 4 r_1^10. <U, Cg> = integral Psi (a - l)^2/(a l) >= 4 inf Psi r_1^10/K^2; <g, Cg> <= K^2; Cauchy-Schwarz for C and <Psi, C Psi> <= sup Psi^2 give covariance >= 16 r_1^20 (inf Psi/sup Psi)^2/K^6; rescaled variance <= z^24 <= e^{24 beta}. Exponent 408 + 144 + 24 = 576. Agrees.
- Rational: r_1 > 1/4 and e^{-576 beta} > 2^{-864 beta} = 2^-1987.2, so 16 r_1^20 e^{-576 beta} > 2^{4 - 40 - 1987.2} = 2^-2023.2 > 2^-2024. Agrees.

**B8. Arm bound J > 6/5 and delta > 1/12 (line 205). HOLDS.** J = integral f L/integral L since integral L = z_2 z(beta)^12; 1348 (17) J >= 1 + 24 r_1^6 (HOLDS in 1350; valid for beta <= 7/3, and 23/10 < 7/3); 24 (7/15)^6 > 1/5 iff 120 x 7^6 = 14 117 880 > 15^6 = 11 390 625. If |log L - c| <= delta then J <= e^{2 delta}; log(6/5) > (1/5)(5/6) = 1/6, so delta > 1/12 > 1/100. The 3 delta log-purity transfer (line 207) is the triangle inequality on three masses. Agrees.

**B9. Certificate margins (lines 232-241). HOLDS.** 1348 (13): e^{beta q} = P_beta(q)(1 + R), 0 <= R <= 13 2^-20, valid for 0 <= beta <= 7/3 (HOLDS in 1350), so the per-plaquette density ratio is within 1 + 13 2^-20 and D <= (1 + 13 2^-20)^312 <= (1 - 4056 2^-20)^-1; 251 x 4056 = 1 018 056 < 2^20 = 1 048 576 gives D < 251/250. Upper margin: 7 - (250/251)(7 - 122/125) = 7 - 1506/251 = 1, strict because D < 251/250. Lower margin: 7 - (251/250)(7 - 257/251) = 7 - 1500/250 = 1, strict likewise. The affine-span remark (maximal correlation of span{1,f} and span{1,g} is |corr(f,g)|) makes the comparison valid for fixed trials. Agrees. The scope remark (an upper certificate needs all probes, a moment matrix of chosen probes only bounds the supremum from below) is correct.

**Not checked in detail (outside the row's list):** the eigenvalue reduction for mixed pairs (line 62, read and plausible; Q's with equal spectra are SO(4)-conjugate and left times right unit quaternions give SO(4)); the one-face sufficient test (11) (lines 165-183); the spectral partition-function trial (12) (lines 185-201). None of the listed numbers depends on them.

**Verdict B: HOLDS.** No wrong line found in any listed item. The row's own status is correct: R lies in (49/225 + 4 2^-2024, 7 - (2966/495) 2^-822], an interval containing 1, so the transmission test at beta = 23/10 is undecided; the upper side is the hard one (supremum over all probes), and the gap between 49/225 and 1 is wide.

## Remark for row 1490 (my observation, proved by one inequality)

On the stripe, the per-block Gaussian action is G_*(t) = 4a t^2/(8+a) (at a = 1, (4/9) t^2), and the nonlinear stripe minimum is N(t) = 8 + a - sqrt(64 + a^2 + 16 a cos t) = (4/9) t^2 - (19/729) t^4 + ... at a = 1. The rate in (6) is Delta_a(t) = G_* - [Wilson + pin at the Gaussian mean] <= G_* - N(t), because N is a minimum over the same one-parameter family. So a centre that carries x N(t) per block removes the whole lower bound (6) on this ray, not only its t^4 term, and row 1480's counterexample says nothing about that centre. This agrees with the author's statement that the nonlinear centre is open. It is only the stripe ansatz: transverse colour directions and other coarse fields are untested (row 1490's own task).

## Summary of verdicts

| Item | Lines | Verdict |
|---|---|---|
| A1 two period-two fields, 384 contours | 21-23 | HOLDS |
| A2 integrated Wilson vertices (L, 9/3/3, 6 det C, Cov expansion) | 31-74 | HOLDS |
| A3 compact pinned law representation | 76-91 | HOLDS |
| A4 normalized fine-block activity (1)-(3), KP self-term, weight | 93-135 | HOLDS |
| A5 staggered Cartan source (4), mean 2u = a t/(8+a), rate (5), (6) | 137-176 | HOLDS |
| A6 vacuum and curvature extraction (7) | 178-206 | HOLDS (two-derivative domination sketched; orders checked) |
| A7 integrated quartic (8), 19/729 | 208-234 | HOLDS |
| A8 violation (9), hot (10), free energy (11), external bond e^5 - 1, next-row formula | 236-276 | HOLDS |
| B1 eight conditional laws, 352 and 312 | 13-31 | HOLDS |
| B2 conventions (3)-(5) | 34-62 | HOLDS (eigenvalue reduction read, not rebuilt) |
| B3 ordering (6), four outward rows | 65-79 | HOLDS |
| B4 resolved-plaquette trial sum one | 81-89 | HOLDS |
| B5 reference comparison (7), counts 119/132, 7 - (2966/495) 2^-822 | 92-115 | HOLDS |
| B6 lower bound 49/225, r_1 > 7/15 | 118-162 | HOLDS |
| B7 opposite-face positivity, (13), counts 108 and 102 | 203-230 | HOLDS |
| B8 J > 6/5, delta > 1/12 | 205-207 | HOLDS |
| B9 margins 122/125, 257/251, D < 251/250 | 232-241 | HOLDS |

Row 1480: HOLDS. Row 1485: HOLDS. No correction needed in either. Defects found: none that break a stated claim.

Provenance and independence: Claude Opus 5.5 (high) checking gpt-6.2-astra (max) rows, so cross-provider. Every listed constant was rederived by hand from the definitions; no script was run (memory free 37 percent at 17:06Z, below the 50 percent rule), no Lean, no numerics as evidence (one floating value of r_1(2.3), about 0.479, is labelled as a guide). A1 duplicates row 1478 Step 1, which was also Claude Opus, so A1 confirms row 1480 cross-provider but adds no provider independence to row 1478. The cited inputs 1348 (13), (17) and line 249 were taken from 1348 with the check 1350 (HOLDS), not rebuilt here.

What stays open: (A) the integrated activity bound about a nonlinear constrained classical centre (rows 1490-1491); (B) the row sum R at beta = 23/10, which lies in (49/225 + 4 2^-2024, 7 - (2966/495) 2^-822] (row 1489).

Credit: Tadeusz Balaban for the small-field and large-field renormalization group and the block-spin structure; Roman Kotecky and David Preiss for the polymer criterion; Ethan Sussman and Levent Alpoge, with Claude and Codex, for the outline, the complete account and the contour-kernel construction behind Q2. The two checked rows are by gpt-6.2-astra (Codex). This check grants no status and is not an audit.
