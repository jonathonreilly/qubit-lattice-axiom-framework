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

### Step 1 (done 13:25Z): inventory of the author file

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

### Step 2 (done 14:05Z): check of (25) and the chain it consumes

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

Row 1254 (9), (7), (6) (read in full, `gap-solve29-astra62.md` lines 59-117). HOLDS as used. (7) at r = 1: the two vectors f - E[f|D] and g - E[g | W outside B] are orthogonal, both in the kernel of the exterior projection, and each has inner product with f equal to its squared norm, so Bessel gives the bound; staples of an interior path link outside V_m lie outside B. (9): the cube inequality passes from mu_c to its W-marginal (more exterior information in the fine law), then from zeta_c to zeta with loss l/u >= theta (variance and each conditional variance are infima of mean square errors), then (7) at r = 1. Interior links of distinct straight paths share no plaquette (checked for perpendicular paths through one root), and their staples are not path links, so they are independent given W. The density bound (5) is cited from Bhattacharjee, Bhattacharya, Lockwood and Romanov (B, v7). Its form agrees with the one-link character contraction I_2(s)/I_1(s) <= s/(3/2 + s) = 4 beta/(1 + 4 beta) at s = 6 beta over b - 4 intermediate links; I did not re-derive the prefactor 48(1 + 6 beta)^{3/2}. Status: cited published input, not rebuilt in this check.

Side conditions: m >= 24 gives 16 <= m for the coarse (6) and (10) at t = 6, 10b < N for (16), and 10b + 2 < N/2 for row 1254 (9). theta_b = ((1 - eta_b)/(1 + eta_b))^{4 m^4} is row 1254's theta with M = 4m^4 straight coarse links.

What (25) is: an implication. A lower bound on the Poincare constant vhat_4(1) of the finite label law of the pinned reduced wall variables gives a lower bound on the gauge-invariant side-(10b+2) cube constant of the ordinary Wilson law. It proves no lower bound on vhat_4(1). The author's own (30) (Abelian Gaussian analogue, checked in step 5) indicates that the analogous constant tends to zero as b grows.

### Step 3 (done 14:25Z): check of (26)-(29) and the cited one-link estimate

**Cited input, row 1145 (1)-(2) (`gap-solve2-astra62.md` lines 18-31), read with its proof. HOLDS.** The multiplier of the normalised central density e^{s Re u} in the d-dimensional representation is I_d(s)/I_1(s) (I recomputed: the integral of sin(d theta) sin(theta) e^{s cos theta} over [0, pi] is pi d I_d(s)/s). The Riccati equation R_k' = 1 - (2k+1)R_k/s - R_k^2 for R_k = I_{k+1}/I_k is right; R_k stays below the increasing positive root u_k = exp(-arsinh((k+1/2)/s)); arsinh x >= x/(1+x) because 1/sqrt(1+x^2) >= 1/(1+x)^2; and (k+1/2)/(s+k+1/2) >= 1/(1+s) for k >= 1. With s <= 6 beta this gives I_d/I_1 <= exp(-(d-1)/(1+6 beta)). Fourier inversion with |tr(A rho_d(g))| <= d |A|_op gives |p - 1|_sup <= sum_{d>=2} d^2 exp(-(d-1)n/(1+6 beta)) for a path with n conditionally independent links. This row was checked as HOLDS in row 1146.

**Selection of I, line 280 and line 369. HOLDS.** Each link shares a plaquette with at most 18 others, so a greedy choice keeps at least length/19 links of the tree return with pairwise disjoint plaquettes; given I^c these are independent one-link Wilson laws (translates of e^{s Re u}, 0 <= s <= 6 beta). The tree return is a simple path in the right cell's tree, so each selected link enters T once. X (the nontree edge e) and the three detour edges (bases in the left cell) are not on the return. The centroid argument for a nontree edge of tree distance > floor(l/8) in the ridge square (line 276) is correct: lattice neighbours at tree distance <= j have a tree path inside lattice distance j, which misses the centroid o, so the retained union (more than half of D) would lie in one component. On the fibre of (25) the first c'b links of the return stay at lattice distance >= b/5 - O(1) - c'b from every straight coarse line, so for c' < 1/5 the constraint is I^c-measurable and the conditional law of I is unchanged.

**(26), lines 373-377. HOLDS.** Given I^c, X and Y are fixed and T has density in [1 - eps_b, 1 + eps_b] against Haar (row 1145 (2) with n >= cb/19). In R^4, w(XT) = <T, X^{-1}> and w(YT) = <T, Y^{-1}>, and <X^{-1}, Y^{-1}> = Re(X^{-1} Y) = w(X Y^{-1}) = c_p. The projection of uniform S^3 onto a 2-plane is uniform on the unit disk (radius r = cos phi, volume element proportional to r dr dt ds). So the law of (A, B) under Haar T is that of (u, c_p u + sqrt(1 - c_p^2) v), and the two-sided measure bound holds for all Borel sets because it holds for the law of T.

**(27), lines 379-385. HOLDS.** A - B = <T, X^{-1} - Y^{-1}> with |X^{-1} - Y^{-1}|^2 = 2 - 2c_p = 2D_p, so Z_p = 2(A - B)^2 = 4 D_p u^2 with u semicircular on [-1,1]. E u^{2k} = Cat_k/4^k, so E(4u^2)^k = (2k)!/(k!(k+1)!). Positivity of Z_p^k and the density bound give the two-sided bound with relative error eps_b for every k.

**(28), lines 386-390. HOLDS.** D_p is I^c-measurable (X, Y in I^c), R = E[Z_p | I^c] - D_p has |R| <= eps_b D_p, and Cov(Z_p, F) - Cov(D_p, F) = E[RF] - E[R]E[F].

**(29), lines 392-398. HOLDS.** With no plaquette meeting two links of I_p union I_q, the two selections stay independent given the joint complement, and E[Z_p Z_q | complement] = D_p D_q (1 + theta_p)(1 + theta_q) with |theta| <= eps_b; the means are handled the same way, giving the factor 2 eps_b + eps_b^2. Binning: A is one reduced matrix and B at most three, so the label readings move A, B by at most d_b and 3 d_b and Z_p by at most 32 d_b. At ab -> L > 0 and beta = O(log(1/a)), b/(1+beta) grows like 1/(a log(1/a)), so eps_b is smaller than every power of a.

**Reflected forms, lines 402-407. HOLDS.** w(Q(X) Q(Y)^{-1}) = w(p_v X Y^{-1} p_v^{-1}) = c_p. For F supported in the negative half (hence off I), |E(conj(F) Delta_p)| <= eps_b E(|F| D_p) by (28)'s conditional bound. Summing with 0 <= D_p <= 2, 0 <= Z_p <= 8 gives the centred reflected form of O' - O at most C eps_b (sum |t|)^2 -> 0; binning at d = o(a^{2K}) adds o(1). The contrast with the single readings follows from (20).

What (26)-(29) show: two fundamental loops that share one long tree return, read jointly by the quadratic Z_p = 2(A - B)^2, carry the elementary plaquette energy D_p = 1 - c_p up to a relative error eps_b, conditionally on everything off the selected links. This is an elementary consequence of the uniform density of a long Haar-mixed transport. It is an obstruction (the reduced wall labels in (25) retain local action-density correlations); it is not a step toward (33).

### Step 4 (done 14:45Z): cited rows, and whether the main comparison restates an earlier row

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
