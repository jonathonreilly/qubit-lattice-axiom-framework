lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:15Z

# Check of row 1272 (`library/gap-solve31-astra62.md`), FINISH row 1282

Started 2026-11-20T13:15Z (date -u). Checker: Claude Opus 5.5, max effort, Mac mini Claude worker 3, cross-provider check of a gpt-6.2-astra author row. Pinned at commit 4e5eb6512 on branch claude/ym4d-hard-route. Hand check; no numeric run is a proof step here.

## Plan (at most eight steps)

1. Read FINISH.md (efficiency rules, build-on-published-work section) and the whole of `library/gap-solve31-astra62.md`; list its numbered statements with author labels.
2. Check (25), the finite-volume estimate on gauge-reduced cell boundaries, line by line, with every earlier statement it consumes ((1)-(24) as needed).
3. Check (26)-(29), recovery of elementary curvature correlations from paired long loops, line by line.
4. Read each cited earlier row (statement and proof) where a step depends on it; record whether the main comparison restates an earlier row (grep `library/open-core.md` and the FINISH rows).
5. Check the remaining statements ((30)-(33) and anything else in the file), including the OPEN labels.
6. Cross-check against published work (the Sussman-Alpoge account, `library/prior/gap-onebound-read-sol.md`) for credit and for prior appearance of the claims.
7. Verdict table: HOLDS / HOLDS AFTER CORRECTION / FAILS per statement, with line numbers.
8. RESULT line.

## Progress log

(Each step appends below as it finishes.)

Provenance: Claude Opus 5.5, max effort, commit 4e5eb6512, one reading by one other-provider model; not an audit and not human review. Verdict labels follow the queue row: HOLDS, HOLDS AFTER CORRECTION, FAILS. Line numbers refer to `library/gap-solve31-astra62.md` at this commit (481 lines).

### Step 1: inventory of the author file

The author file has these numbered statements (label as written by the author; all are PROVED unless noted).

| Stmt | Lines | Content |
|---|---|---|
| partition | 17-21 | Borel cells of chord diameter at most delta = 1/(5 sqrt(1+beta)), inversion-equivariant |
| (1) | 23-28 | Dobrushin coefficients c_ij = beta delta^2 m_ij / 4 of the fixed-label law, row sum <= 9/50 < rho = 1/5 |
| (2) | 30-36 | boundary coupling bound with B^D = sum_k C_DD^k C_{D,D^c}, row sums <= rho^dist |
| (3) | 38-49 | (1-rho) E Var(f given labels) <= E_s(f) |
| (4) | 51-55 | spectral corollary |
| (5) | 59-64 | label prediction across a collar |
| sep. ins. | 66 | two separated insertions |
| (6) | 68-78 | density of joint law of U_A, U_Z given labels off A within e^{+-h_r} |
| (7) | 82-94 | v_t lower bound from label constant with volume factor |
| (8) | 96-100 | gauge-sector comparison, cited from row 1254 (8) |
| (9) | 102-106 | conditional consequence |
| (10)-(13) | 110-155 | volume-free comparison v_t >= vbar_s/(K^2 (t/s)^4 + vbar_s/(1-rho)) |
| (13a) | 161-169 | label-law single-link Dobrushin test fails |
| (14)-(15) | 173-193 | unsigned conditional label correlations > 2 with probability -> 1 |
| (16) | 199-207 | cell disintegration: E_{(k+4)b}(f) >= (k/(k+4))^4 [E^Y_k(M_W f) + norm((I-M_W)f)^2] |
| wall factor | 209 | oscillation of log K_C at most 72 beta b^3 d |
| (17) | 211-224 | v_b/16 <= vtilde_2, v_{8b} >= c_1 vtilde_2, c_1 = 1/1056 |
| (18) | 228-251 | adjacent wall-label blocks strongly dependent |
| (19) | 255-266 | tree-reduced variables Q: vhat_4 >= v_b/256, v^inv_{10b} >= vhat_4/200 |
| (20) | 270-280 | for every tree choice, adjacent reduced groups have max correlation -> 1; distant covariance bound |
| (21)-(22) | 286-308 | one-link averaging norm in fixed representation; product suppression |
| (23)-(24) | 310-349 | finite-band versions |
| unrestricted | 321-333 | count of Haar-centred components cannot replace angular restriction |
| **(25)** | 353-369 | **main positive claim 1**: pinned straight coarse transports, v^inv_{10b+2} >= theta_b (10b/(10b+2))^4 vhat_4(1)/200 |
| pinned (20) | 369 | adjacent invariant correlation persists in the pinned law |
| **(26)-(29)** | 373-398 | **main positive claim 2**: joint law of (A,B) given I^c; moments of Z_p; covariance transfer |
| reflected forms | 402-407 | reflection seminorm comparison |
| (30) | 413-428 | Abelian Gaussian comparison: vanishing coarse constant |
| (31)-(32) | 434-460 | Lovasz local lemma selection; Haar averaging along long tree segments |
| (33)-(34) | 464-479 | conditional mass gap bound H >= v_*/(78125 e^2 L) from liminf vhat_4(1) > 0 plus a matched continuum |

Dependency chain of (25): (1) -> (2) -> (6) -> (10) with (11)-(13), applied on the coarse lattice (line 222) -> (16) -> (17) -> (19) -> (25), plus row 1254 (9) (straight-path density estimate of Bhattacharjee, Bhattacharya, Lockwood and Romanov) and row 1254 (6).
Dependency chain of (26)-(29): the one-link Fourier/convolution estimate of row 1145 (1)-(2) as used in (20) (line 280), with the private-link selection of line 280 and line 369.

### Step 2: check of (25) and the chain it consumes

I redid each step by hand. The author writes delta, d_b for chord diameters of bins in R^4 (unit quaternions); w = half-trace = real part.

**(1), lines 23-28. HOLDS.** In a plaquette holding links i and j, w is multilinear in the quaternion entries and the other factors have norm one, so the mixed difference over two values of U_i and two values of U_j in their cells is at most |U_i - U_i'| |U_j - U_j'| <= delta^2. The interpolation bound |Cov_t(1_A, D)| <= osc(D) P_t(A)(1 - P_t(A)) <= osc(D)/4 (centre D at the midpoint of its range) gives TV <= beta m_ij delta^2 / 4. Each link is in 6 plaquettes with 3 other links, so sum_j m_ij = 18 and sum_j c_ij <= 4.5 beta/(25(1+beta)) <= 9/50.

**(2), lines 30-36. HOLDS.** The random-scan maximal coupling started from the two stationary conditional laws gives p' <= [(1 - 1/M) I + C_DD/M] p + C_{D,J} 1_J / M coordinatewise; the telescoping through intermediate configurations is legitimate because every intermediate configuration keeps each link in its assigned cell. The limit is (I - C_DD)^{-1} C_{D,J} 1_J = B^D 1_J. The row-sum bound rho^{dist(i,J)} is the substochastic-walk argument as written (each step has total mass at most 9/50 < 1/5).

**(3), lines 38-49. HOLDS.** d_j(P_x f) <= d_j(f) + sum_{i in D_x} B_ij d_i(f) (direct exterior argument plus (2) with J = {j}); summing with the row sums of B gives sum_j d_j(Kf) <= [1 - (1 - rho)(s/N)^4] sum_j d_j(f), since each link lies in exactly s^4 cubes. Sup-norm decay of K^k on centred bounded functions, self-adjointness and positivity of K, and density of bounded functions give K <= 1 - (1 - rho)(s/N)^4 on the centred fibre space. The last step (conditioning also on the labels inside D_x lowers the integrated variance) is correct.

**(6), lines 68-78. HOLDS.** A plaquette cannot meet both A and Z (base separation >= r + 1 >= 2). The density of the joint law relative to the product of marginals is an average of the cross ratio J(u,z)J(u',z')/(J(u,z')J(u',z)) against a probability weight in (u',z'), so it lies in [e^{-h}, e^{h}] once the cross ratio does. The derivative of log J along the linear interpolation of the inner boundary terms is the interpolated mean of D; (2) on the collar with J inside Z gives |E_z D - E_z' D| <= sum_i d_i(D) rho^{dist(i,Z)}; d_i(D) <= 12 beta delta (6 plaquettes, 2 inner configurations); at most b_s = 4[(s+2)^4 - s^4] such collar links; graph distance >= r. Interpolation keeps the mixed bound (convex combination of two terms each <= beta delta^2).

**(10)-(13), lines 110-155. HOLDS.** Checked: A_x = M - E[. | eta_{A^c}] is an orthogonal projection, so <g, f> = |g|^2; F_k decreases in k, so g - g_0 is orthogonal to L^2(F_0) and g_{k-1} - g_k to L^2(F_k); the bound |g_k| <= (e^{h_{r+kt}} - 1)|g| follows from (6) on the enlarged collar by Cauchy-Schwarz against the density minus one, and e^{uz} - 1 <= u(e^z - 1) for 0 <= u <= 1. In (13), maximal correlation <= e_0 follows from |density - 1| <= e_0; the norm bound 1 + e_0 for (u,v) -> u + v and its adjoint gives (1 - e_0) Var f <= E Var(f|X) + E Var(f|Y); (11) is the proof of (3) on L = V_k \ A. The count ((2k+2)t)^4 is right ((2k+1)t + t - 1 <= (2k+2)t). Numerics: sqrt(1 + 20(k+1)^4) <= 9(k+1)^2; sum_{k>=1} (k+1)^2 5^{-(k-1)} = 6.72... < 8. The second inequality of (10) follows from Var f = |Mf|^2 + |(I-M)f|^2 and (3) at side t.

**(16), lines 199-207. HOLDS.** Given W, private fields of distinct closed cells are independent (a plaquette with a private link of a cell lies in that closed cell). A closed cell whose vertex set misses the cube of bases contains no link of A, so given W \ A the private fields outside J_z are independent of A; hence P_z maps L^2(W) to L^2(W \ A) by the marginal conditional expectation, and P_z commutes with M_W. On (I - M_W) f the product (Efron-Stein) components over cells give the count (k+1)^4 >= k^4. J_z has bases in bz - b1 + [0,(k+1)b)^4, inside each fine cube of side (k+4)b with origin bz - b1 - h, 0 <= h_nu < b; these origins partition the fine origins.

**Wall factors, line 209. HOLDS.** At most 3b^3 links per direction (some transverse coordinate on the lower wall), so at most 12b^3 per group; the count sum over changed links of (plaquettes containing it) <= 6 * 12 b^3 handles plaquettes with several changed links; a pointwise bound on the log integrand survives integration over private links.

**Coarse application, line 222 and line 262. HOLDS.** c_{zz'} <= 16 * 2 * 72 kappa_0 / 4 = 576 kappa_0 even for arbitrary changes of Y_{z'} (each factor's oscillation in Y_z over its bin is <= 72 kappa_0 whatever its other arguments); 80 neighbours give row sum 46080 * 2^{-32} < 1/5. Factors have coarse range one, so the separation and distance counts of (6) and (10) transfer. h_1 (side 2 core) = 240 * 2304 * 2^{-32}/5 ~ 2.6e-5 and h_1 (side 4 core) = 1040 * 2304 * 2^{-32}/5 ~ 1.1e-4, both < 2^{-12}. Constants: 1/66, 1/1056, 1/22 and 1/200 are valid (with K^2 < 4; the true K is about 1.016, so 1/200 has slack, about 1/50 would also follow).

**Tree reduction, lines 255-264 (lower bound of (19)). HOLDS.** The triangular change of variables maps product Haar on wall links to product Haar on (p, Q); K_C is invariant under gauge rotations at vertices of its closed cell, so K_C(U_W) = K_C(tree links = 1, Q), with Q of nontree edges equal to U_e in that gauge. For gauge-invariant f, M_W f is a function of Q; sigma(Y outside a group cube) is contained in sigma(all p, Q outside), and p is independent of Q, which gives E^Y_6(M_W f) >= E^Q_6(g).

**(25), lines 353-367. HOLDS.** Each arm from root bz in direction nu lies on a coarse line, so it is in group z; its first b - 1 links join wall vertices of the half-open cell and can be put in the tree; the last link ends at the root b(z + nu), so Q_e = p_v U_e = C_{z,nu}. Hence the C's are individual Haar coordinates of Q, and the fibre C = 1 has density prod_C K_C(Q, C = 1) against Haar on the other Q's, times Haar on p (the constraint is on Q only). This agrees with the canonical disintegration of row 1254 (both are the normalised restriction of a continuous density). Nonroot gauge rotations preserve the fibre, so M_W f depends only on Q there; the private fields are still independent given W with unchanged laws. So (16) at k = 6 and the coarse (10) at s = 4, t = 6 give the side-10b fine inequality on the fibre with constant (6/10)^4 min(1, vhat_4(1)/22) >= vhat_4(1)/200 for restrictions of fully gauge-invariant tests.

Row 1254 (9), (7), (6) (read in full, `gap-solve29-astra62.md` lines 59-117). HOLDS as used. (7) at r = 1: the two vectors f - E[f|D] and g - E[g | W outside B] are orthogonal, both in the kernel of the exterior projection, and each has inner product with f equal to its squared norm, so Bessel gives the bound; staples of an interior path link outside V_m lie outside B. (9): the cube inequality passes from mu_c to its W-marginal (more exterior information in the fine law), then from zeta_c to zeta with loss l/u >= theta (variance and each conditional variance are infima of mean square errors), then (7) at r = 1. Interior links of distinct straight paths share no plaquette (checked for perpendicular paths through one root), and their staples are not path links, so they are independent given W. The density bound (5) is cited from Bhattacharjee, Bhattacharya, Lockwood and Romanov (B, v7). Its form agrees with the one-link character contraction I_2(s)/I_1(s) <= s/(3/2 + s) = 4 beta/(1 + 4 beta) at s = 6 beta over b - 4 intermediate links; (5) is re-derived in step 6, item 1, without B, on the range eta_b < 1 that (25) uses.

Side conditions: m >= 24 gives 16 <= m for the coarse (6) and (10) at t = 6, 10b < N for (16), and 10b + 2 < N/2 for row 1254 (9). theta_b = ((1 - eta_b)/(1 + eta_b))^{4 m^4} is row 1254's theta with M = 4m^4 straight coarse links.

What (25) is: an implication. A lower bound on the Poincare constant vhat_4(1) of the finite label law of the pinned reduced wall variables gives a lower bound on the gauge-invariant side-(10b+2) cube constant of the ordinary Wilson law. It proves no lower bound on vhat_4(1). The author's own (30) (Abelian Gaussian analogue, checked in step 5) shows that the analogous constant tends to zero as b grows in the massless Gaussian model. Step 5 explains why this does not decide (33) for SU(2).

### Step 3: check of (26)-(29) and the cited one-link estimate

**Cited input, row 1145 (1)-(2) (`gap-solve2-astra62.md` lines 18-31), read with its proof. HOLDS.** The multiplier of the normalised central density e^{s Re u} in the d-dimensional representation is I_d(s)/I_1(s) (I recomputed: the integral of sin(d theta) sin(theta) e^{s cos theta} over [0, pi] is pi d I_d(s)/s). The Riccati equation R_k' = 1 - (2k+1)R_k/s - R_k^2 for R_k = I_{k+1}/I_k is right; R_k stays below the increasing positive root u_k = exp(-arsinh((k+1/2)/s)); arsinh x >= x/(1+x) because 1/sqrt(1+x^2) >= 1/(1+x)^2; and (k+1/2)/(s+k+1/2) >= 1/(1+s) for k >= 1. With s <= 6 beta this gives I_d/I_1 <= exp(-(d-1)/(1+6 beta)). Fourier inversion with |tr(A rho_d(g))| <= d |A|_op gives |p - 1|_sup <= sum_{d>=2} d^2 exp(-(d-1)n/(1+6 beta)) for a path with n conditionally independent links. This row was checked as HOLDS in row 1146.

**Selection of I, line 280 and line 369. HOLDS.** Each link shares a plaquette with at most 18 others, so a greedy choice keeps at least length/19 links of the tree return with pairwise disjoint plaquettes; given I^c these are independent one-link Wilson laws (translates of e^{s Re u}, 0 <= s <= 6 beta). The tree return is a simple path in the right cell's tree, so each selected link enters T once. X (the nontree edge e) and the three detour edges (bases in the left cell) are not on the return. The centroid argument for a nontree edge of tree distance > floor(l/8) in the ridge square (line 276) is correct: lattice neighbours at tree distance <= j have a tree path inside lattice distance j, which misses the centroid o, so the retained union (more than half of D) would lie in one component. On the fibre of (25) the first c'b links of the return stay at lattice distance >= b/5 - O(1) - c'b from every straight coarse line, so for c' < 1/5 the constraint is I^c-measurable and the conditional law of I is unchanged.

**(26), lines 373-377. HOLDS.** Given I^c, X and Y are fixed and T has density in [1 - eps_b, 1 + eps_b] against Haar (row 1145 (2) with n >= cb/19). In R^4, w(XT) = <T, X^{-1}> and w(YT) = <T, Y^{-1}>, and <X^{-1}, Y^{-1}> = Re(X^{-1} Y) = w(X Y^{-1}) = c_p. The projection of uniform S^3 onto a 2-plane is uniform on the unit disk (radius r = cos phi, volume element proportional to r dr dt ds). So the law of (A, B) under Haar T is that of (u, c_p u + sqrt(1 - c_p^2) v), and the two-sided measure bound holds for all Borel sets because it holds for the law of T.

**(27), lines 379-385. HOLDS.** A - B = <T, X^{-1} - Y^{-1}> with |X^{-1} - Y^{-1}|^2 = 2 - 2c_p = 2D_p, so Z_p = 2(A - B)^2 = 4 D_p u^2 with u semicircular on [-1,1]. E u^{2k} = Cat_k/4^k, so E(4u^2)^k = (2k)!/(k!(k+1)!). Positivity of Z_p^k and the density bound give the two-sided bound with relative error eps_b for every k.

**(28), lines 386-390. HOLDS.** D_p is I^c-measurable (X, Y in I^c), R = E[Z_p | I^c] - D_p has |R| <= eps_b D_p, and Cov(Z_p, F) - Cov(D_p, F) = E[RF] - E[R]E[F].

**(29), lines 392-398. HOLDS.** With no plaquette meeting two links of I_p union I_q, the two selections stay independent given the joint complement, and E[Z_p Z_q | complement] = D_p D_q (1 + theta_p)(1 + theta_q) with |theta| <= eps_b; the means are handled the same way, giving the factor 2 eps_b + eps_b^2. Binning: A is one reduced matrix and B at most three, so the label readings move A, B by at most d_b and 3 d_b and Z_p by at most 32 d_b. At ab -> L > 0 and beta = O(log(1/a)), b/(1+beta) grows like 1/(a log(1/a)), so eps_b is smaller than every power of a.

**Reflected forms, lines 402-407. HOLDS.** w(Q(X) Q(Y)^{-1}) = w(p_v X Y^{-1} p_v^{-1}) = c_p. For F supported in the negative half (hence off I), |E(conj(F) Delta_p)| <= eps_b E(|F| D_p) by (28)'s conditional bound. Summing with 0 <= D_p <= 2, 0 <= Z_p <= 8 gives the centred reflected form of O' - O at most C eps_b (sum |t|)^2 -> 0; binning at d = o(a^{2K}) adds o(1). The contrast with the single readings follows from (20).

What (26)-(29) show: two fundamental loops that share one long tree return, read jointly by the quadratic Z_p = 2(A - B)^2, carry the elementary plaquette energy D_p = 1 - c_p up to a relative error eps_b, conditionally on everything off the selected links. This is an elementary consequence of the uniform density of a long Haar-mixed transport. It is an obstruction (the reduced wall labels in (25) retain local action-density correlations); it is not a step toward (33).

### Step 4: cited rows, and whether the main comparison restates an earlier row

**Cited statements read, with proofs, where a checked step depends on them.**

- Row 1254 (`gap-solve29-astra62.md`), (5)-(10), lines 59-117: read in full; (6), (7), (9) re-derived in step 2 (HOLD); (8) re-derived here: the vertex projections G_y commute with every exterior projection, the exterior is fixed by rotations at the (s-1)^4-cube interior vertices, and the expansion in G_y, 1 - G_y gives the factor (1 - 1/s)^4. HOLDS. Row 1254 was checked as HOLDS in row 1261.
- Row 1254 (1)-(4), lines 18-50 (used by (34) of row 1272): read. The reflection-positivity interpolation (4) and the use of B's finite-torus covariance theorem are as row 1261 checked them; (3) rests on that cited theorem.
- Row 1145 (1)-(2): read and re-derived in step 3. HOLDS (row 1146 checked it).
- Row 1222 (`gap-solve24-astra62.md`) (1), lines 15-23: read. Its cell factorization (each plaquette reads private links of at most one cell; given the walls the private fields are independent) is what (16) uses. Row 1222 was checked as HOLDS in row 1226.

**Is the main comparison a restatement?** No, but most of its frame is earlier work, which the author credits.

- The inequality (16) is the cell-interior form of row 1254 (7) (there for straight-path interiors), built on row 1222 (1). Row 1222 (1) bounds only the averaged private term b^{-4} sum_s d_{W_s}(f) by E_b(f). (16) adds, on one fixed grid, the heat-bath term of the wall marginal. The author says so at line 197.
- The transfer from the pinned fibre to the ordinary law in (25) is row 1254 (9) applied verbatim with c = 1, and theta_b is row 1254's theta.
- New in row 1272: the fixed-label Dobrushin comparison (1)-(13) (a Poincare constant of the continuous law, uniform in the volume, from the Poincare constant of the finite label law at a slightly smaller side), its coarse-group version (17), the tree reduction (19), and the combination (25).
- Search record. `library/open-core.md` (564 lines) has no statement on cube Poincare constants, angular labels or wall labels (grep for Dobrushin, angular, label, wall link, pinned, heat bath). In FINISH.md, "finite label" and "gauge-reduced" occur only in rows 1272 and 1282. "Dobrushin" occurs in many earlier rows (661-1138, 1258). The closest are row 1135 (a Dobrushin cross-ratio bound at beta <= 1/48 on the raw links) and row 1258 (the Dobrushin-Shlosman hypothesis (W)). Neither uses label bins of size c/sqrt(1 + beta), where the fixed-label law satisfies Dobrushin's condition at every beta.

**Credit notes (literature recalled from memory, not re-read in this check).** (2) is the Dobrushin comparison theorem in coupling form. Föllmer (J. Funct. Anal. 1982) gives the matrix form B = sum_k C^k. (3) is the classical argument (Aizenman-Holley, 1987) that Dobrushin's condition gives a heat-bath gap. The split Var f = E Var(f | eta) + Var E(f | eta) into a fibre gap and a projected gap, as in (10), follows the decomposition theorems for Markov chains of Madras and Randall (Ann. Appl. Probab. 2002) and of Jerrum, Son, Tetali and Vigoda (Ann. Appl. Probab. 2004). The row credits Dobrushin for (1) only. These are credit additions; no step depends on them.

### Step 5: the remaining statements

**Partition, lines 17-21. HOLDS.** h = 2/ceil(4/delta) <= delta/2, so a cube has diameter 2h <= delta; cubes meeting S^3 lie in an annulus of volume O(h), so there are O(h^{-3}) = O((1+beta)^{3/2}) of them; the grid on [-1,1] is symmetric, so q -> conj(q) = q^{-1} permutes cubes off boundaries.

**(4), lines 51-55. HOLDS.** (1 - rho)|(I - M)g|^2 <= E_s(g) = <g, H_s g> <= lambda |g|^2 by (3).

**(5), lines 59-64. HOLDS.** With H = sigma(eta on S^[r], U off S^[r-1]), G is H-measurable; E[F|H] depends only on the shell values, which move within their cells; (2) with D = S^[r-1] and dist(S, shell) >= r gives oscillation <= 2|S| |F|_inf rho^r, and F_r = E[E[F|H] | eta on S^[r]].

**Separated insertions, line 66. HOLDS.** For dist(S_F, S_G) > 2r, G is off S_F^[r-1] and F_r (a function of U on S_F^[r]) is off S_G^[r-1]; apply (5) twice. Inversion equivariance of the partition makes the predictions commute with the lattice reflection.

**(7), lines 82-94. HOLDS.** vbar_s >= v_s because sigma(eta off D_x) is contained in sigma(U off D_x). For the second inequality: given eta off D_x, (6) and Cauchy-Schwarz give |A_x P_V f| <= (e^{h_r} - 1) times the conditional L^2 norm of the centred exterior function; |A_x (I - P_V) f| <= |(I - P_V) f|; the l^2 triangle inequality over x gives the displayed bound with (t/s)^2 and eps (N/s)^2; then |f| <= |Mf| + |(I-M)f| with the label inequality and (3) at side t, rearranged and squared.

**(8), lines 96-100. HOLDS** (step 4).

**(9), lines 102-106. HOLDS** as a conditional statement. h_r is O(beta^{1/2} s^3 5^{-r}); with N <= a^{-P}, s ~ (log 1/a)^2 and r = C log(1/a), eps (N/s)^2 = o(as) and t/s -> 1; the ratio in (7) increases in sqrt(vbar_s) (its derivative is 2(x - e)(T + ke)/(T + kx)^3 > 0).

**Scope, line 157, and collar size, line 116. HOLDS.** h_r <= 2^{-12} needs r >= C(1 + log(2+beta) + log(s+1)); then t/s -> 1 at s ~ beta^2, and (10) gives v_t >= c'(at)^2 from vbar_s >= c(as)^2.

**(13a), lines 161-169. HOLDS.** The varied staple runs over S^3; b on the 2-sphere in S_0-perp gives |S_0 + b|^2 = 1 + |S_0|^2 and directions n_b on a 2-sphere of radius >= 1/sqrt(26); actual neighbours within their cells give |S - (S_0 + b)| <= 18 delta. The one-link law is proportional to exp(-beta|S| |u - S/|S||^2/2); the cap of radius beta^{-1/2} gives a normaliser >= c beta^{-3/2}, so mass outside radius l/2 is O(beta^{3/2 - L^2/128}) <= C beta^{-2}. The label law of eta_i given the other labels is the average of this one-link law over exact configurations consistent with the labels (tower property). A maximal 3l-separated set has >= c l^{-2} points; one of them has original mass <= C l^2.

**(14)-(15), lines 173-193. HOLDS.** beta E_beta S <= -log Z(beta) <= C N^4 log(2+beta) (caps of radius beta^{-1/2}: 1 - w_p <= 8/beta, 6N^4 plaquettes); translation and axis symmetry give E(1 - w_p) <= C log(2+beta)/beta uniformly in N; compactness gives near-pure-gauge frames on a fixed box with probability -> 1. Two neighbouring links share exactly one plaquette, so 11 traces; the quadratic forms Re u = 1 - |x|^2/2 + O(|x|^4) and Re(u v^{+-1}) = 1 - |x +- y|^2/2 + ... give L = [[6, tau],[tau, 6]] (x) I_3, L^{-1} = [[6, -tau],[-tau, 6]]/35, correlation -tau/6. The uniform Laplace step, the total-covariance step (centres move by C kappa) and the kappa-replacement by label representatives are correct; frames chosen from a representative completion are functions of the other labels. 18 pairs times (1/6 - C kappa - o(1)) > 2 for small kappa.

**(17), upper direction, line 224. HOLDS.** A fine side-b cube with origin bz + h meets only groups in z + {0,1}^4, so the fine exterior fixes all other labels; summing over the b^4 offsets gives E_b(f(L)) <= 16 Etilde_2(f).

**(18), lines 228-251. HOLDS.** The ridge pairs (v, v + 3hat) and the three-link detours through x_1 = 2b - 1 are wall links of the two blocks; every link at v or w has its base in the union, so independent rotations at the v_j and w_j preserve the conditional law and make X product Haar. Cov(Re X, Re Y | B) = E[w(X Y^{-1}) | B]/4 by E_g[g g^T] = I/4. For the information bound: D(P||Q) >= P h - log Q(e^h) (Gibbs/Donsker-Varadhan variational inequality; not named in the row) with u = beta/log(2+beta); |Xhat - y|^2 >= |X - y|^2/2 - d_b^2; the Haar factor E exp(-u(1 - cos theta)) <= C u^{-3/2}. If the bracket is negative the bound is trivial since I >= 0.

**(19), upper direction, line 264. HOLDS.** Changing links in a fine side-b cube changes frames only in cells z + {0,1}^4 and reduced edges with base in z + {-1,0,1}^4, inside a side-4 coarse cube; summing over offsets gives E_b(f(L^Q)) <= 256 Ehat_4(f).

**(20), lines 270-280. HOLDS.** Centroid argument checked in step 3. Both traces are gauge invariant (same root cell); the left-cell frames cancel along the detour; A - B = Re((X - Y)T) gives |A - B| <= |X - Y| and E|A - B|^2 = 2E(1 - w_p) <= C log(2+beta)/beta. Reduced labels outside the two blocks read no frame of the distinguished cell (its immediate predecessors (1,1,1,1), (2,0,1,1), (2,1,0,1), (2,1,1,0) are in the blocks), so they are measurable off its tree links. Row 1145 (2) on >= cb/19 selected links gives the conditional density bound, hence conditional means -> 0, second moments -> 1/4, and the covariance bound for F off the selected links.

**(21), lines 286-300. HOLDS.** Conjugation averaging keeps the mean, does not increase the norm, and maps V_d to multiples of chi_d. R_k' > 0 because R_k stays below the positive root of its Riccati right side, so log(m_d/m_2) increases; m_d' = Cov(chi_d, w), m_2' = 2 Var w, and Cauchy-Schwarz give Var chi_d/m_d^2 >= Var w/(E w)^2. The density of x = 1 - w is proportional to e^{-sx} sqrt(x(2-x)); the two intervals give Var w >= c(1+s)^{-2}.

**(22), lines 302-308. HOLDS.** The averaging functional on the Hilbert tensor product of the V_{d_i} has norm equal to the product of the one-factor norms; H_s >= I - P_{I^c} by the product decomposition given I^c (each link of I lies in s^4 cubes); splitting a spectral unit vector at P_{I^c} gives the second bound. The proof is self-contained; the reference to row 1254 (36) is a credit only.

**(23), lines 310-317. HOLDS.** 1 - |Pi_D 1|^2 = |P|^2 with P = 1 - Pi_D 1 a degree <= D polynomial in w of Haar mean one (so sup |P| >= 1); D + 1 subintervals of length h/(4(D+1)) each carry p_s-mass >= c/(4(D+1)), so each holds a point with |P| <= C sqrt(D+1)|P|; Lagrange interpolation finishes. The matching upper example (1 - w)^D/E_Haar(1 - w)^D is right. The many-link version: |Q_k 1|^2 = P(sum B_i <= k) <= exp(k - (1 - e^{-1}) M_0 d) <= exp(-(1/2 - e^{-1}) M_0 d) for k <= M_0 d/2.

**Unrestricted functions, lines 321-333. HOLDS.** The orthogonal complement of the Haar-centred space in L^2(p_s) is spanned by dH/dp_s = Z(s)e^{-sw}, with squared norm Z(s)Z(-s) = Z(s)^2 (w(-q) = -w(q)); the projection of 1 is 1 - e^{-sw}/Z. The product G: discarded sites have sum over p of (1 - w_p) >= eps/4 (six traces sum to U_i . S_i <= |S_i|); on E_i the density is <= C(1+beta)^{3/2} e^{-2(6-eps)beta}; E h_i in [1 - d, 1], E h_i^2 <= 1 + d, and E(prod h - 1)^2 <= e^{M_0 d} - 1 + 2M_0 d -> 0 because log M_0 <= (12 - 2eps - eta)beta eventually. The centring step is right (mu(BG) = mu(B(G-1)), |.| <= |G - 1|).

**(24) and the growing-bandwidth corollary, lines 337-349. HOLDS.** (1+s)h >= 1 and sh <= D at h = D/(D+s); point separations >= |j-k| h/(4(D+1)); the weight sum is [16(D+1)/h]^D/D! <= (C/h)^D. D log(C(1 + 6 beta/D)) increases in D (derivative log(C(1+y)) - y/(1+y) >= 0, y = 6 beta/D), and 2 alpha log(C(1 + 6/alpha)) -> 0.

**Pinned (20), line 369. HOLDS.** Ridge vertices with x_3, x_4 in the middle 3b/5 of [b, 2b) are at lattice distance >= b/5 - O(1) from every straight coarse line (a line vertex has three coordinates on the grid, so y_3 or y_4 is on it). The first c'b return links (c' < 1/5) avoid the pinned paths, so the constraint is a function of their complement. The plaquette XY^{-1} uses no path link, so E_{zeta_c}(1 - w_p) <= (sup dzeta_c/dzeta) E_zeta(1 - w_p) <= theta_b^{-1} E_zeta(1 - w_p) (inf <= 1 <= sup and inf/sup >= theta).

**(30), lines 413-428. HOLDS.** If dA = 0, A is a gradient on the cover; its periods are sums of straight coarse arms, hence zero; the potential is constant on each cell tree and equal at adjacent roots, so A = 0. f is gauge invariant (summation in x_1). The test field has f(A^0) >= N^4/2 - N^4/b^3 and |dA^0|^2 <= C N^4(N^{-2} + b^{-3}). The antiderivative J (periodic because the cosine sums to zero over a period) and the sum of (dh)_21 over the torus being zero give |f(h)|^2 <= C q^6 |dh|^2 for h supported in a side-q cube; the conditional variance of a linear reading of a Gaussian is that variational supremum. So E_{8b}(f) <= C N^4 b^2, Var(f | W_lin) <= (N/b)^4 C b^6, (16) at k = 4 gives E_4(g) <= 16 E_{8b}(f), and the ratio is C[(b/N)^2 + 1/b]. The finite-bin approximation (martingale convergence for both projections) is correct.
Scope (my reading, not a defect of the row): the 1/b term comes from Var f ~ N^4 b^3, which needs a massless Gaussian (variance per unit volume growing like b^3). A massive comparison would bound Var f by C N^4/(m a)^2 and give no small constant. So (30) shows that the straight-path pinning, the walls, fine resolution and the curl action alone do not give (33); it does not show that (33) fails for SU(2). The row's own wording at lines 411 and 428 says this.

**(31), lines 434-442. HOLDS.** Each bad event (two selected links of distinct groups on one plaquette) has p = 256^{-2} and shares a group with at most 2 * 256 * 18 = 9216 others; with x = 2p, (1 - x)^D >= 1 - Dx = 0.71875 >= 1/2, so p <= x(1-x)^D; the inductive proof of the symmetric local lemma is the standard one. The density of each segment product is 1 + O(e^{-cr/(1+beta)}) by row 1145 (2) with floor(r/256) selected links, and |prod p_k - 1| <= e^{CJ eps} - 1 gives (31).

**Tree readings, line 444. HOLDS** (qualitative). Bounded segment count: at most 2k + 1 segments between the root, at most k leaves and k branch points, plus two splits per used edge. Independent Haar rotations of components project a multilinear contraction onto each component's invariant subspace; a single adjoint vector has none.

**(32), lines 446-458. HOLDS.** B_alpha expands as stated (Ad is orthogonal; the common prefix cancels in T_x^{-1}T_y). For each omitted pair, after excluding the eight links of the two end plaquettes (so v_x, v_y are measurable off the selection), E[Ad(T_xy) | complement] has norm <= C eps; summing over pairs gives (sum |alpha|)^2.

**ARGUED, line 460.** Correctly labelled; it is a reading of (31)-(32) and (27), not a proof step.

**(33)-(34), lines 464-477. HOLDS** as a conditional implication. From (25) with theta_b -> 1 (m^4 eta_b -> 0: eta_b <= C beta^{3/2} exp(-(b-4)/(1+4 beta)) and (b-4)/(1+4 beta) ~ L/(4a log(1/a))), any v < v_*/200 holds at side n = 10b + 2, physical size -> 10L. Row 1254 (3) needs N >= 2n + 4 (true for m >= 24, b >= 2) and the growth condition o(N/n), which is o(N/b). Arithmetic: 16 (v_*/200)/(625 e^2 * 10 L) = v_*/(78125 e^2 L). (33) itself is OPEN, as labelled.

**OPEN, lines 400 and 479; RESULT line 481.** Accurate. The statement at line 400 ("at fixed exterior their joint prediction is a function of one ordinary plaquette trace") is what (26) proves up to the factor 1 +- eps_b.

### Step 6: published work, credit, and what (25) reduces

Sources read: the row 1218 reading `library/prior/gap-onebound-read-sol.md`, section B (lines 127-197); the outline index `library/sa-index/chunk-02.md` (GL3); row 1261's check of row 1254 (`library/gap-solve29-check-opus.md` lines 273-290). The four-author TeX (B, v7) is not in this checkout or in the papers folder. I did not fetch it. Statements about B below rest on the row 1218 reading.

1. **B's path-density bound (5), used for theta_b in (25), now holds without B.** Row 1261 re-derived it, and I checked that derivation. Put q = 4 beta/(1 + 4 beta). Row 1145 (1) gives u_1 <= s/(s + 3/2) <= q for s <= 6 beta, and each interior link contracts the d-dimensional coefficient by q^{d-1}. With x = q^{b-2} <= 1/8, sum_{d>=2} d^2 x^{d-1} <= 5.43x <= 6x. If eta_b < 1 then q^{b-4} < 1/48, so 6 q^{b-2} <= eta_b. Step 2 points here. (25) uses no unchecked published input.

2. **Credit: the two-scale form.** B's Corollary 102 asks, at each scale, for a two-term inequality (S) (reading, lines 189-195): mu'(Var(f|c))/C_A + E_n^c(E[f|c])/C_B <= E'_{n'}(f), for coarse variables c. Row 1272 proves inequalities of exactly this form for two other coarse variables, at every beta and uniformly in the volume:
   - (16): c = all wall links, with C_A = C_B = ((k+4)/k)^4.
   - (3) with (10): c = the angular labels, with C_A = 2/(1 - rho) and C_B = 2K^2 (t/s)^4.
   B uses (S) with straight-path variables, where its H2 is open at weak coupling (reading, line 197). Row 1272 credits rows 1222 (1) and 1254 (7) for the decomposition but not B's (S). A citation of B's Corollary 102 should be added; no step depends on it.

3. **What B already covers, and what (33) asks.** B's Corollary 166 proves BP(n, 1/2) for the law of the straight-path products on a restricted window of torus sizes (reading, lines 182-188). (25) pins exactly those products to 1. (33) asks for the Poincare constant of everything else on the cell walls (all remaining reduced wall matrices, binned). So B's Corollary 166 does not touch (33), and (33) is not in B.

4. **(33) is a reformulation of the physical-scale cube estimate, not a weaker input.** Checker's remark, ARGUED, not part of the row.
   - The row's own (19) shows two directions for the unpinned labels: vhat_4 >= v_b/256 and v^inv_{10b} >= vhat_4/200.
   - For the pinned law of (25) a converse follows the same way. Suppose the ordinary Wilson law has invariant constant v at side b. Row 1254 (10) gives the fibre mu_1 a constant v' >= min{1 - b/m', theta (b/m')^4 min(v, (1 - 1/b)^4)} on all functions, at side m' = 3b + 4.
   - A fine cube of side m' changes frames and reduced labels only inside a coarse cube of side 6. Summing over the b^4 offsets, as in (19), gives vhat_6(1) >= c theta_b v with an absolute c > 0.
   - The proof of (25) runs unchanged at coarse side 6 ((10) with s = 6, t = 8; (16) with k = 8; fine side 12b + 2).
   So, up to fixed changes of cube side and constants, a uniform lower bound on vhat_k(1) is equivalent to a uniform fine cube constant at physical scale of order L. The second is B's sufficient input (B-BP). (25) turns that input into a statement about a finite-state Markov chain on wall data. It does not make the input easier. The row says only "sufficient", which is accurate.

5. **Sussman-Alpoge.** The citation of GL3 to outline lines 2197-2231 is consistent with the index (chunk-02: GL3 at lines 2210-2213, "The Bessel recurrence gives (GL3)", proved in detail). I re-derived the identity in step 3. The scope citations (CA-I 2704-2712: no mass-gap assertion) agree with GOAL.md's method section. The row's credit of Sussman and Alpoge (with Claude and Codex as authors of their text) is correct as written.

6. **Other credit additions** (literature recalled, not re-read): the Gibbs/Donsker-Varadhan variational inequality in (18), line 251; Catalan moments of the semicircle law in (27); the items listed in step 4 (Dobrushin-Follmer comparison, Aizenman-Holley, Madras-Randall, Jerrum-Son-Tetali-Vigoda).

### Step 7: verdict per statement

Checked line by line by hand by Claude Opus 5.5 (max), Mac mini worker 3, 13:15Z-13:42Z on 2026-11-20. This is a cross-provider check of a gpt-6.2-astra row and grants no status. No numeric run was made. Line numbers are those of `library/gap-solve31-astra62.md` at 4e5eb6512.

| Statement | Lines | Verdict |
|---|---|---|
| angular partition | 17-21 | HOLDS |
| (1) fixed-label Dobrushin coefficients | 23-28 | HOLDS |
| (2) boundary coupling bound | 30-36 | HOLDS |
| (3) fibre gap | 38-49 | HOLDS |
| (4) | 51-55 | HOLDS |
| (5) label prediction across a collar | 59-64 | HOLDS |
| separated insertions | 66 | HOLDS |
| (6) collar density | 68-78 | HOLDS |
| (7) | 82-94 | HOLDS |
| (8) (row 1254 (8)) | 96-100 | HOLDS |
| (9) conditional consequence | 102-106 | HOLDS (conditional, as labelled) |
| (10)-(13) and (11), extension of (6) | 110-155 | HOLDS |
| scope at s ~ beta^2 | 116, 157 | HOLDS |
| (13a) | 161-169 | HOLDS |
| (14)-(15) | 173-193 | HOLDS |
| (16) | 199-207 | HOLDS |
| wall-factor oscillation | 209 | HOLDS |
| (17), both directions | 211-224 | HOLDS |
| (18) | 228-251 | HOLDS |
| (19), both directions | 255-266 | HOLDS |
| (20) | 270-280 | HOLDS |
| (21) | 286-300 | HOLDS |
| (22) | 302-308 | HOLDS |
| (23) and the many-link bound | 310-317 | HOLDS |
| unrestricted Haar-centred functions | 321-333 | HOLDS |
| (24) and growing bandwidth | 337-349 | HOLDS |
| **(25)** | 353-367 | **HOLDS** |
| pinned form of (20) | 369 | HOLDS |
| **(26)** | 373-377 | **HOLDS** |
| **(27)-(28)** | 379-390 | **HOLDS** |
| **(29)** | 392-398 | **HOLDS** |
| OPEN | 400 | label correct |
| reflected forms | 402-407 | HOLDS |
| (30) and its finite-bin approximation | 413-428 | HOLDS |
| local-lemma selection and (31) | 434-442 | HOLDS |
| tree readings | 444 | HOLDS |
| (32) | 446-458 | HOLDS |
| ARGUED | 460 | label correct |
| (33)-(34) | 464-477 | HOLDS as an implication. Inputs: (33), the matched continuum hypotheses, and B's finite-torus covariance theorem through row 1254 (3); B's theorem is cited and not rebuilt (row 1261 also took it as cited). |
| OPEN, RESULT | 479, 481 | accurate |

0 FAILS. 0 HOLDS AFTER CORRECTION: no proof step needed a correction. Several constants have slack (for example 1/200 in (19) and (25); about 1/50 also follows).

**Notes, ranked by what they change. None breaks a statement.**

1. Scope of (25). (25) is sufficient, as labelled. Its input (33) is, up to fixed changes of cube side and constants, equivalent to a uniform fine cube constant at physical scale of order L, which is B's sufficient input (B-BP). See step 6, item 4 (checker's ARGUED remark). The row's own (19) already shows both directions for the unpinned labels. So (25) reformulates the open estimate as a finite-state chain on wall data; it does not reduce it.
2. Credit to add. The two-term form of (16) and of (3) with (10) is the step (S) of B's Corollary 102 (row 1218 reading, lines 189-195), here proved for wall links and for angular labels at every beta. Also add the Dobrushin-Follmer comparison for (2), Aizenman-Holley for (3), and the Gibbs/Donsker-Varadhan inequality in (18). These are recalled, not re-read; no step depends on them.
3. (34) uses B's finite-torus covariance theorem (TeX lines 5850-6077, through row 1254 (3)) as a cited published input. Under FINISH rule 2 it stays unchecked until rebuilt.
4. (30) concerns the massless Gaussian. The b^{-1} term comes from variance growing like N^4 b^3. It shows that pinning, walls and the curl action alone do not give (33). It does not show that (33) fails for SU(2) (step 5).

**Restatement question.** The main comparison (25) is not a restatement of an earlier row. Its frame is credited earlier work: row 1222 (1) cell factorization, the row 1254 (7) decomposition, and row 1254 (9) pinning transfer, applied verbatim with c = 1. New in row 1272: the fixed-label Dobrushin comparison (1)-(13) and its coarse-group version, the wall decomposition (16) at one grid, the tree reduction (19), and their combination (25). (26)-(29) are new: no earlier library file has the paired-loop reading with a common tree return. They extend (20) of the same row.

RESULT: row 1272 HOLDS, checked line by line by Claude Opus 5.5 max (Mac mini worker 3, 13:15Z-13:42Z; cross-provider check of a gpt-6.2-astra row; grants no status). Every statement HOLDS: 0 FAILS, 0 corrections. That includes the finite-volume comparison (25) with its chain (1)-(3), (6), (10)-(13), (16), (17), (19) and row 1254 (6)-(9), with B's path-density bound (5) re-derived without B, and the paired-loop recovery (26)-(29) with row 1145 (1)-(2). (25) is not a restatement but is sufficient only: its input (33) is, up to cube side and constants, equivalent to the physical-scale cube estimate (B-BP) (checker's argued remark). Credit B's two-scale step (S) of Corollary 102. (34) rests also on B's cited covariance theorem. OPEN: (33), the matched nontrivial continuum construction, the mass gap.
