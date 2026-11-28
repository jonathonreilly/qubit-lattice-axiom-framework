Checked by Claude Opus 5.5 (laptop Claude subagent), cross-provider check of a gpt-6.2-astra row; grants no status.

# Check of `library/gap-seed4-astra62.md` (FINISH row 1375), FINISH row 1376

Status: complete. 74 statements: 73 HOLD, 1 HOLD AFTER CORRECTION (wording), 0 FAIL. The note nowhere claims the seed proved or disproved. The final target is not weaker than the seed (S57).

Method. I read the note in full (307 lines). I read in full row 1367 (`gap-seed-astra62.md`), row 1371 (`gap-seed2-astra62.md`), row 1373 (`gap-seed3-astra62.md`) and its check, row 1374 (`gap-seed3-check-opus.md`). I read the cited parts of: row 1231 (`gap-solve26-astra62.md`: (1), (7), (8), the cube-update section); row 1252 (`gap-solve-fresh-astra62.md`: L253-L272, (20)-(21) and the applications paragraph); row 1173 (`gap-solve15-astra62.md`: the propagating-mode comparison, L144-L154); `gap-compress-opus.md` (Propositions Q and TB2) and its check `gap-compress-check-astra.md` (literature input); `gap-phys-seed.md` (Theorem ZD-c); `lit-balaban.md`; the SA index chunks 02 and 30; the row 1369 verdict S22 on row 1367 (7); the row 1372 RESULT. I did not read `gap-seed5-astra62.md`. I redid each step by hand. Line numbers L are lines of the target note. No numerical or Lean computation was used. The five-ref search claims were not refetched (this clone has no PR refs).

Statements are the labelled paragraphs (GUIDE, PROVED, ARGUED, OPEN, RESULT): 74 in all.

## A. The physical test

**S1. L17, OPEN, the physical test. Accurate.** The neutral transfer F = P_0 T is positive with a strictly positive kernel, so 0 <= lambda_a/lambda_0 < 1 and s(t) decreases in t. Hence w = floor(n/1024) is the most favourable time allowed by FINISH row 1375. The remark on row 1161 (19) restates row 1367 L21-L27. The continuum hypotheses are those of row 1349. Restates the target of rows 1367 L11, 1371 L11 and 1373 L13.

## B. A punctured slice and the dense single-link influence, L25-L67

**S2. L25-L30, the separator (1). HOLDS.** Take a plaquette that is not inside the closed box but has an edge e' inside it. Then some vertex of the plaquette lies outside, so e' lies on a hyperface x_nu = +-R and is tangent to it. Hence e' is in D. With the seams outside the box, the box plaquettes carry no seam sign. The density is exp(-S_box(box links)) times a sum over labels of exp(-S_ext(exterior links, D; labels)). So, given D, the box links are independent of X, of H outside H_R, and of the labels. This gives L(V | H, X, D) = L(V | H_R, D). Convexity of total variation in its first argument, with Q_R measurable in H, gives (1). The same holds without X. X is outside the box since R < w. Moving a seam is allowed because P_0 commutes with T (row 1373 L76; check 1374 S8). New (a Markov property across the box boundary).

**S3. L32-L39, (2). HOLDS** (proof S4-S6). With Z = sqrt(beta) X the Wilson action is (1/2)||dZ^a||^2 per colour to leading order, so a cycle has Var(J) = <J, Delta^{-1} J>. The integrand of kappa is at most sqrt(12 * 16) and is positive on a set of positive measure, so kappa is finite and positive. New.

**S4. L41, free upper bound. HOLDS.** The time integral is int dk_0/(2 pi) (h + 2 - 2 cos k_0)^{-1} = 1/sqrt(h(h+4)) = c(k). With r + 1/r = 2 + h, the profile c r^{|t|} solves the difference equation: off zero, (2 + h - r - 1/r) c r^{|t|} = 0; at zero, (2 + h - 2r) c = c(1/r - r) = 1. Lower bound: for a transverse J with coefficient one on e, 1 = |int <P_s e_i, J-hat>|^2 <= kappa int c |J-hat|^2. The minimizer c^{-1} P_s e_i / kappa has weighted norm 1/kappa. Approximation: away from zero a smooth transverse u equals d^*(t wedge u / h); trigonometric approximation of that two-form is uniform; c ~ 1/(2|k|) is integrable. The coefficient on e moves by at most sqrt(kappa) times the weighted error. Each finite approximant minus C_e is a cycle of the punctured patch for large R.

**S5. L43, boundary lower bound. HOLDS.** For a cycle J, |J(b)|^2 <= Var(J) ||db||^2 (transverse projection, then Cauchy-Schwarz in Fourier). So a b vanishing on H_R and D with C_e(b) = 1 gives Var(C_e | H_R, D) >= 1/||db||^2. Energy check, per spatial mode with u-hat transverse and profile r^{|t_0|}: the spatial curls give h(1+r^2)/(1-r^2), the time differences give 2(1-r)/(1+r); with h = (1-r)^2/r the sum is (1-r^2)/r = 1/r - r = sqrt(h(h+4)). So the total is kappa. The gradient term restores delta_e on the slice and changes no curl. Square summability: sum r^{2|t_0|} = (1+r^2)/(1-r^2) = O(1/|k|) and |phi-hat|^2 <= 1/h = O(|k|^{-2}), both integrable in three dimensions. Truncation keeps the trace and converges in l^2, so the curl energy converges. With v'_R <= v_R, limsup v_R <= 1/kappa and liminf v'_R >= 1/kappa, both tend to 1/kappa.

**S6. L45, Gaussian channel error. HOLDS.** The two conditionals are N(m', v' I_3) and N(m, v I_3) with E|m' - m|^2 = 3(v - v'). The mean relative entropy is (3/2)[v'/v + (v - v')/v - 1 + log(v/v')] = (3/2) log(v/v'). Pinsker and Jensen give sqrt((3/4) log(v/v')).

**S7. L47, finite spacetime graph input. HOLDS, given rows 1151, 1231 (1), 1339 (1)-(2) and 1371 (6)** (proof S8-S11). Remark, no correction: L47 states the result for a graph strictly inside one arc, while the uses at L57, L84, L110, L140, L181 and L196 put the graph around the near face, where the two arcs meet. L53 proves time and space translation invariance of these readings (for a local insertion the two projections combine to one, and moving a seam across a contractible graph is a vertex gauge by -1, which fixes based words and keeps tree links Haar). So the result transfers to those placements.

**S8. L49, weak convergence, linear part. HOLDS.** The O(N_4 Delta) entropy restates row 1371 L232 and L172-L174 at period 2w. Covariance lower bound: the one-form on the chord edges with values u_c has circulation u_c on loop c and curl squared norm at most 24 sum u_c^2 in four dimensions, so the circulation covariance is at least I/24 per colour. Then P_v <= C_G M_v^* M_v. Young's inequality bounds the sum over shifts of squared pairings by the squared l^1 norm of the filling times the curl array norm. Carlen and Cordero-Erausquin (row 1339 (2)), Pinsker and Jensen over about N_4/2 shifts give O_G(sqrt(Delta)). Restates the method of row 1373 L90 and L196-L198.

**S9. L51, covariance limit and nonlinear error. HOLDS.** Row 1231 (1) is stated for sides n, n, n, M with M >= n. At period 2w the recount adds the leftover time strip (fraction at most b/(2w)) and the cut layers (fraction 1/w), which gives O(N_4(1/b + b/n + b/w)), as the note says. The coupling on one white noise and the dilution term O(1/b^2) are as in row 1231 L28. Riemann sums of a bounded symbol continuous off zero give the Brillouin integral. The word Taylor bound and sum |A_e|^2 <= C b^5 sum (1 - Re U_p) restate row 1371 L254-L263 and row 1231 (8). Summed over shifts, beta (C h b^{-7/2} sum |A_e|)^2 is at most C_G b^{-2} N_4.

**S10. L53, frames and the neutral circle. HOLDS.** The law of the based words is invariant under simultaneous conjugation (root vertex gauge). The Gaussian limit is invariant under common colour rotation. So tests averaged over conjugation suffice. The neutral transfer of a bounded test error is the Cauchy-Schwarz step of row 1371 (6), with Z/Z_+ <= 8.

**S11. L55, strengthening to variation. HOLDS.** Given all other links, the Fisher information of the chord coordinates is 3 sum E[h.v] <= 18 k beta (restates row 1371 L246-L250). Fisher information is convex under mixtures, and Haar isometries preserve it. In z = sqrt(beta) log H, the chain rule gives int over |z| <= M of |grad sqrt(f_j)|^2 <= C_{M,G}; the Jacobian term is O(M^2/beta^2). A uniform H^1 bound on compact sets makes sqrt(f_j) precompact in L^2 there, hence f_j precompact in L^1. Weak convergence identifies the limit; tightness removes the cutoff. The Gaussian covariance is nonsingular by S8. Tree links Haar: restates row 1371 L202 and row 1373 L108.

**S12. L57-L67, (3). HOLDS, given S7-S11.** By (1), E d_TV(L(U_e | H, X), Q_{R,j}) <= E d_TV(L(U_e | H_R, D), Q_{R,j}). The graph H_R with D and e is connected and fixed for fixed R. Its tree extends the tree of H_R, so the fundamental cycle of e and its based word are the same for both observations. If the joint laws are within delta_j, the mean conditional distance is at most 2 delta_j (replace the history marginal, then use the triangle inequality); this step is correct. The two Gaussian conditionals pass through the same exponentiation and transport map, so their mean distance is at most sqrt((3/4) log(v_R/v'_R)). The triangle inequality with and without X, then R to infinity after j, gives (3). The condition 2R + 4 < w holds eventually since w grows like n. New.

## C. Many dense histories in one reveal order, L71-L110

**S13. L71, uniform statement. HOLDS** (proof S14-S17). New.

**S14. L73-L78, (4). HOLDS.** The detour is known, so C_f(a) = a_f. a_f is a signed sum of (d_s a) over a filling of at most (D_0+1)^2 plaquettes. Only bonds f within distance O(D_0) of a plaquette use it, so the overlap is bounded. Cauchy-Schwarz gives ||a||^2 <= C_{D_0} ||d_s a||^2. The symbol of d_s^* d_s is h P_s, and sqrt(h(h+4)) >= h, so K >= d_s^* d_s. K is bounded by sqrt(192). The minimum exists in the equivalent norm. Variations with zero e coordinate give (K a_*)|_M = lambda delta_e, and testing a_* gives lambda = kappa_M <= kappa. The filling restates row 1371 L216.

**S15. L80, upper variance. HOLDS.** J_* = K a_*/kappa_M is transverse, equals delta_e on M, and int c |J_*-hat|^2 = <a_*, K a_*>/kappa_M^2 = 1/kappa_M. The correction sum u_f C_f is d_s^* of the weighted fillings Phi. Its covariance norm is at most int c h |Phi-hat|^2 <= ||Phi||^2, since c h = sqrt(h/(h+4)) <= 1. Since c >= 1/sqrt(192), weighted convergence implies l^2 convergence, so sum |u_f|^2 tends to zero. The known graph is connected because every missing bond has a detour.

**S16. L82, lower variance. HOLDS.** For a finite trace a-hat the extension of S5 has energy int c^{-1} |P_s a-hat|^2 = <a, K a>. It is square summable since a-hat is bounded. It vanishes on known edges and, after truncation, on a far boundary.

**S17. L84, uniformity. HOLDS.** Local stabilization of patterns along a subsequence is a diagonal argument. Detours pass to the limit since there are finitely many candidate paths and the pattern agrees near each bond. Each component of the known patch reaches the boundary of B_R, so the union with D is connected. (1) holds with the smaller predictor since H_0 is contained in the known edges of the box. The nested Gaussian channel error and the finite-graph comparison contradict the assumed failure.

**S18. L86, coverage. HOLDS.** The direction-1 bond at (x_1, x_2+1, x_3) has the other parity of x_2 + x_3, so it is known. With two direction-2 bonds it gives a three-edge detour. There are n^3/2 omitted bonds (n even). The detours use only bonds that are never omitted, so every later history keeps them.

**S19. L88, suffix. HOLDS.** Hybrid argument: the k-th hybrid uses the true kernels for the first k missing bonds and the X-free kernels after. Its distance to the previous hybrid is E_true d_TV(L(f_k | X, H, f_{<k}), L(f_k | H, f_{<k})) <= eta_j(D_0). Every history H with f_{<k} satisfies the detour condition, since the detours lie in H. The X-free kernels compose to L(f | H). With m_j <= min(n, eta_j^{-1/2}), m_j eta_j <= sqrt(eta_j) -> 0.

**S20. L90-L94, (5). HOLDS.** This is row 1373 (7) with eta = m_j eta_j(D_0), and r = (1+s(2w))^{-1} at the full face (row 1373 (2)). Cauchy-Schwarz gives A_{H,f} <= A_H pointwise, which is the left inequality. Restates row 1373 (7) applied to a detoured suffix.

**S21. L96-L101, (5a), the two inputs. HOLDS.** Cap bound: Z(b) >= e^{|b|} e^{-1/2} c (1+|b|)^{-3/2}, so the one-link maximum is at most C(1+6 beta)^{3/2}. Mixtures keep this. The Lebesgue density in z = sqrt(beta) log(.) is the Haar density times (2 pi^2)^{-1} (sin theta/theta)^2 beta^{-3/2}, so p, q <= C for beta >= 1. Exponential moment: |z|^2 = beta theta(H_C)^2 <= C m sum_p beta(1 - Re U_p), by subadditivity of the angle and 1 - cos theta >= 2 theta^2/pi^2. Hoelder and the half tilt (row 1371 L111-L115; row 1334) moved to the neutral circle by row 1371 (6) with a doubled exponent give it.

**S22. L103-L108, (5a), the proof. HOLDS.** int W^b dQ = E int p^b q^{1-b} <= C^{b-1} E_H int q^{2-b} <= C^{b-1} int f_Z^{2-b}, by Jensen since 0 < 2 - b < 1. Hoelder against the Gaussian weight makes the last integral finite. (3) says (1/2) int |W - 1| dQ -> 0. Interpolation gives every a < b. W log W <= C(1 + W^b) is uniformly integrable, so I -> 0. The chain rule gives the block bound. The b = 2 remark is accurate.

**S23. L110, variance in Wilson units. HOLDS.** The risk given (H, X) lies between the risk given (H_R, D) (by (1) and adding D) and the risk given H_R. Truncation: predictors may be restricted to the ball, so the optimal risk moves by at most 8 M^2 times the joint variation. Removing truncation: distance to a closed subspace is 1-Lipschitz in L^2. The exponential moment and Gaussian tails make the truncation error uniformly small. The limits are 3 v_R and 3 v'_R, then 3/kappa.

## D. The full-face comparison (6), the single-edge rate (7) and the Gaussian example, L116-L155

**S24. L116-L128, (6). HOLDS** (proof S25). The threshold: s/(1+s) <= 4/25 exactly when s <= 4/21. The remark on row 1373 (17): by the check 1374 remark the (17) sum is at most g_+(2w) = log(1+s(2w)), so a strict margin for s gives a strict margin for (17). Since 1 - A^2 <= 2(1 - A) <= 2 d_TV, (3) gives sup_e d_e = o(1); all near-face edges are equivalent by translation and cubic symmetry. New.

**S25. L130, proof of (6). HOLDS.** h_x(y) = B(x,y)/sqrt(l(x) l(y)), so ||h_x||_{2,mu} = 1 and Var_mu(h_x) = 1 - (B sqrt(l))(x)^2/l(x). Integrating, D_face = 1 - ||B sqrt(l)||^2 >= 1 - sigma^2 = s/(1+s). The identity: E_e h_x = sqrt(l_x(H)) A_{x,H}, with l_x the history likelihood ratio and A the conditional affinity; integrating gives int ||(I - E_e) h_x||^2 dmu(x) = E[1 - A^2] = d_e. The kernel is gauge and centre invariant in each argument, so h_x is invariant; E_e preserves invariant functions because both actions act link by link. On a fixed lattice, Efron-Stein under Haar and the density bounds give lambda_sp >= min l / max l > 0. Rowwise Cauchy-Schwarz gives sqrt(l) >= sigma Omega, so 1 - D_face >= sigma^2 <Omega, sqrt(l)>^2 >= sigma^4 = r^2. Hence 1 - r <= D_face <= 1 - r^2. The first inequality uses the trial vector of row 1367 (3).

**S26. L132-L136, (7). HOLDS** (proof S27-S29). The caveat that lambda_sp is the gap of an auxiliary single-face sampler, not of the transfer, is accurate. Row 1231 (7) is the transported packet and row 1231 L355 tests cube updates on it, as cited.

**S27. L138. HOLDS.** For J = d_s^* A, one component is a direction-1 difference of phi(x/R), of size about |d_1 phi|/R on c R^3 sites, so ||J||^2 >= c_phi R. Second differences give sum_k ||grad_k J||^2 = O(R^3 R^{-4}) = O(1/R). Since h <= 12, c = 1/sqrt(h(h+4)) >= 1/(4 sqrt(h)). Jensen for the convex h^{-1/2} gives int h^{-1/2} dnu >= (int h dnu)^{-1/2} >= c R, so V_J >= c'_phi R ||J||^2.

**S28. L140. HOLDS.** All transported squares are conjugated by the same anchor gauge, so |Z| is invariant. Each based loop crosses an electric flip plane an even number of times. For fixed R the finite-graph limit gives |Z|/sqrt(V_J) -> |N(0, I_3)| in law, so Var f -> v_* > 0.

**S29. L142. HOLDS.** ||(I - E_a) f||^2 <= E(f - f^(a))^2 since f^(a) is measurable off a. f is (1/sqrt(V_J))-Lipschitz in Z. In the linear limit Z - Z^(a) equals J_a times a square circulation (stem traversals cancel), with mean squared norm 3/2 <= 3. Stem-only edges give zero in the limit. The Rayleigh quotient then gives limsup_j lambda_sp <= 3 ||J||^2/(v_* V_J) <= C/R for each R.

**S30. L144, the short-time test. HOLDS, given row 1153 (5).** Delta -> 0 since alpha > 2 gamma, and b/w' -> 0. (2w')^4 beta^{-1/4} log(2 + beta) = 16 beta^{4 alpha - 1/4} log(2 + beta) -> 0 exactly when alpha < 1/16. The log 8 comparison restates row 1373 L206-L208 (check 1374 S37). The time scale and the asymptotic restate row 1373 (16) with kappa = alpha. New: (3), uniformly over the dense histories of S13-S17, at that time.

**S31. L146, statement. HOLDS** (proof S32-S33). Row 1173 L154 indeed computes the antipodal covariance ratio 1/cosh(t alpha) of one spatial cosine mode to test collar screening.

**S32. L148. HOLDS.** Per mode the action per time step is cosh(omega)(x^2 + y^2)/2 - xy with 2 cosh(omega) = 2 + h + n^{-2}. Completing the square, psi(x) = exp(-sinh(omega) x^2/2) maps to a multiple of itself, and x psi gets the extra factor e^{-omega}, since cosh(omega) - e^{-omega} = sinh(omega). The positive kernel makes psi the top vector. At zero momentum sinh(omega_0/2) = 1/(2n), so omega_0 <= 1/n and s(2w) >= e^{-2w/n} >= e^{-1/512} > 4/21.

**S33. L150-L155. HOLDS.** Periodizing e^{-|t| omega}/(2 sinh omega) gives coth(w omega)/(2 sinh omega) at t = 0 and 1/(2 sinh(omega) sinh(w omega)) at t = w. For the joint block, c_d^2 - c_o^2 = 1/(4 sinh^2 omega), so the near-face block of the inverse is 2 sinh(omega) coth(w omega). coth - tanh = 2/sinh(2x). With omega_k between fixed multiples of (1+|u|)/n, each summand is at most C n^{-1} (1+|u|) e^{-c'|u|}, so b - a = O(n^{-4}). Then -2 log A <= D and 1 - A^2 <= -2 log A give sum_e d_e <= n^3 (1/2) log(b/a) <= n^3 (b-a)/(2a) = O(1/n). Remark: the constant is large (the summand is about 2/w for |u| up to about 512), so the bound is asymptotic only; the statement claims only a limit. New.

## E. The coarse grid: (8), (9) and the repair test, L161-L181

**S34. L161, the prefix S. HOLDS AFTER CORRECTION (wording only).** The title says "bounded detour lengths". The construction gives detours of length O(r), where r = ceil(C_A (1 + 6 beta) log n) grows with the cutoff; the paragraph and L168 say so. In this note "bounded" means a fixed D_0, as in S13-S22, so the title misleads: (3) and (5a) do not apply to the bonds left after S. Correction: read "detour lengths O(r)". The rest holds: subdividing edges and attaching trees keep the cycle rank 3q_1q_2q_3 - q_1q_2q_3 + 1 = 2q_1q_2q_3 + 1, every vertex is within 2r steps of the grid (6r is generous), and the O(r) detours exist.

**S35. L163-L168, (8). HOLDS.** Selected links are the interior links of each coarse segment. Collinear links share no plaquette. Parallel segments are at least r >= 4 apart. In a plaquette every i-link meets every j-link at a vertex, so links of two perpendicular segments in one plaquette would both touch a coarse vertex, which is excluded. A temporal plaquette contains one time-zero spatial link. Each segment has at least r - 2 selected links, each with multiplier norm at most e^{-(d-1)/(1+6 beta)} (row 1145 (1)), so eta <= C n^{-C_A + o(1)} and (1 + eta)^{3 n^3} - 1 <= n^{-A}. The orbit channel: given X, or a gauge-invariant reading measurable without the selected links, the law of Y_S is gauge invariant, so on each orbit it is the unique invariant probability. Orbits are the coarse products modulo coarse-vertex gauges. The density bounds pass through this channel. Tree edges of S inside a reading are allowed because they are not selected. Restates row 1252 (`gap-solve-fresh-astra62.md`) L272, straight coarse edges with b - 2 private links and the first and last omitted, and the orbit and tree channel of row 1371 L196-L202.

**S36. L170-L179, (9). HOLDS.** g_S^2 = dL(Y_S | x)/dmu_S <= (1+xi)/(1-xi) by (8), and m_S <= g_S by Jensen. <sqrt(l), B sqrt(l)> = int E_mu[h_x] dmu(x) = double integral of m_S. So ||B|| >= <sqrt(l), B sqrt(l)> >= double integral of m_S^2 / u = (1 - D_S)/u. The conditional Poincare remark and "cannot in general be factored" are accurate. Threshold: limsup D_S < 1 - sqrt(21)/5 and u_j -> 1 give (1 + s)^{-1/2} > sqrt(21)/5 eventually, so s < 4/21. Restates the upper half of row 1367 (3), A = <sqrt(l), B sqrt(l)> <= sigma, with A bounded below through D_S. Remarks: A^2 <= 1 - D_S <= u A, so D_S is comparable to row 1367's D = 1 - A; with S empty, (9) reads (1+s)^{-1/2} >= 1 - D_face, weaker than (6).

**S37. L181, the repair test. HOLDS.** For fixed R the packet fits in one grid cell, whose sides are at least r, which tends to infinity. Both assertions of (8) and Bayes give dL(f | Y_S)/dL(f) between (1-xi)/(1+xi) and its reciprocal. So Var_{mu_H} f >= (1 - o(1)) Var f >= v_*/2. Disintegration gives E_{mu_S} of the conditional Dirichlet energy equal to the sum over e not in S of ||(I - E_e) f||^2, which is at most C/R in the limit (S29). Markov gives Pr(lambda_H > z) <= 2C/(z v_* R).

## F. Whole directions, (10)-(11), L187-L212

**S38. L187-L194, (10). HOLDS** (proof S39-S41). Remark: Gamma is on the near face (time zero), as the proof uses. The constant 1 does not depend on Gamma, f or the side. New.

**S39. L196, available variations. HOLDS.** Adding X, D and the exterior to the conditioning lowers the expected conditional variance. By the separator the result is E Var(f | H^(i)_R, D). Each plane of known directions meets the box boundary and D is connected, so the union is connected. Bounded prediction risks change by O(||f||_inf^2) times the joint variation.

**S40. L198-L203, (11). HOLDS.** The test with time-zero trace a = a_i e_i vanishes on the observed graph and has energy int c^{-1} (P_s)_ii |a_i-hat|^2. J(b) = int conj(J_i-hat) a_i-hat. Weighted Cauchy-Schwarz gives the supremum int c |J_i-hat|^2/(P_s)_ii; the maximizer lies in L^2 of the bounded weight, so trigonometric tests attain it in the limit. For transverse J, <J-hat, Pi_i J-hat> = |J_i-hat|^2/(P_s)_ii. sum_i (P_s e_i)(P_s e_i)^* = P_s and |P_s e_i| <= 1 give sum_i Pi_i >= P_s = I on transverse fields.

**S41. L205-L210, nonlinear Gaussian tests. HOLDS.** In whitened coordinates the conditional covariance is at least I - A_i, so the cross covariance B_i of two conditional replicas satisfies 0 <= B_i <= A_i <= I. Mehler: E f(Z) f(Z') = sum_m <f_m, B^{(x)m} f_m>. B^{(x)m} <= A^{(x)m} by telescoping with positive factors. I^{(x)m} - A^{(x)m} = sum_k A^{(x)k} (x) (I - A) (x) I^{(x)(m-k-1)} >= (I - A) (x) I^{(x)(m-1)}. Summing over i gives at least I^{(x)m} for m >= 1, because sum_i (I - A_i) >= I. So sum_i E Var(f_G | obs_i) >= Var(f_G) at every limit point; compactness of the covariance matrices handles R -> infinity.

**S42. L212, OPEN. Accurate.** The identity of S25 with a block response gives d_i^dir = int E_mu Var(h_x | H^(i)) dmu(x). If Var(h_x) <= (1 + o(1)) sum_i E Var(h_x | H^(i)) held, then D_face <= (1 + o(1)) 3 d_1^dir, and (6) gives the seed when limsup 3 d_1^dir < 4/25. The stated obstacles are the real ones: h_x depends on the cutoff and on x, and its graph fills the face.

## G. The gauge-invariant test of the fully pinned comparison, L216-L257

**S43. L218-L222, flat conditional law. HOLDS.** With every non-1 link equal to one, the (1, mu) plaquette is u_x u_{x+mu}^{-1}, and Re(u v^{-1}) = u.v. The other plaquettes are constant. No plaquette joins two layers. Frames: a transported summand T_{l,z} u T_{l+1,z}^{-1} changes by g_{root l} ( . ) g_{root l+1}^{-1}, so the cyclic product is conjugated. A direction-1 flip changes the sign of one layer mean and of P_t. A transverse flip gives the same sign to the two identical tree paths. So R_t is gauge and centre invariant. Restates the layer identification of TB2 (`gap-compress-opus.md` section 3.4).

**S44. L224-L229, (12). HOLDS.** Shift component a by G f/beta. The cross term is <u^a, Delta G f> = <u^a, f> for mean-zero f; the quadratic term is <f, G f>/(2 beta); and Z(shift) <= Z(0). The reflection sketch is the standard argument of Froehlich, Simon and Spencer: a positive-definite crossing kernel, Cauchy-Schwarz, and a maximizer with the fewest unequal bonds (one of 2N_L, 2N_R is below N_L + N_R + N_cross). All periods n, n, T are even. Credited as in T2 and TB2; the check of TB2 confirms the FSS bound for unit S^3 spins.

**S45. L231-L243. HOLDS.** Since T < n, h_3 >= c|q|^2/n^2; so ||G|| <= C n^2 and Tr G <= C n^3 = C' V. Gaussian integration gives E exp(theta ||P u^a||^2) <= prod (1 - 2 theta/(beta h_3))^{-1/2} <= exp(2 theta Tr G/beta), using -(1/2) log(1 - x) <= x on [0, 1/2]. sum_a ||P u^a||^2 = V(1 - |u-bar|^2). The exponent is c_0 T (2C - 7 beta/64), which gives e^{-c beta n}. For the time modes <f_t, G f_t> = V^{-1} sum_q 1/(4 sin^2(pi q/T)) = (T^2 - 1)/(12 V), so E|M_t - u-bar|^2 <= C T^2/(beta V) = O(1/(beta n)). Normalization is 4-Lipschitz where |M| >= 1/2.

**S46. L245, the neutral signal. HOLDS.** O(4) invariance makes each g Haar and E[g_0 g_w^*] a real scalar alpha = 1 - E|g_0 - g_w|^2/2. Integrating inner pairs first gives E[P_0 P_w^*] = alpha^n and E|P_0 - P_w|^2 = 2(1 - alpha^n) <= n E|g_0 - g_w|^2 = O(1/beta). The density of cos^2 theta under Haar is (2/pi) sqrt((1-r)/r). Coupled law: Pr(|R_0 - R_w| > delta) <= 4 E|P_0 - P_w|^2/delta^2 = O(beta^{-1/2}). Product law: Pr(|R_0 - R_w| <= delta) <= C sqrt(delta) = O(beta^{-1/8}). The two-bin bound sends the affinity to zero. Data processing and E[A_x^2] <= E[A_x] give a whole-direction loss tending to one, at the flat background, as beta -> infinity. New.

**S47. L247, ARGUED. Accurate as ARGUED.** At a fixed cutoff the conditional density is continuous in the pinned background, so a small affinity persists on neighbourhoods of positive finite-cutoff measure. The note makes no claim about their Wilson weight.

**S48. L249-L255, (13). HOLDS.** m_z . m_z' is the real part of the loop u_z, the plane-(l+1) tree path from z to z', u_z'^{-1}, and the plane-l tree path back (common stems cancel). A four-dimensional edge shares a plaquette with 18 others, so the plane-l path, of length at least d(z, z'), has a greedy independent set of at least d(z, z')/19 links. They occur once in the loop. Given all other links they are independent with fundamental multiplier at most e^{-1/(1+6 beta)} (row 1145 (1); row 1252 L255). So each z gives sum_k C(k+1) e^{-k/(19 B)} <= C B^2, and the total is n^{-4} n^2 C B^2.

**S49. L257. HOLDS.** Union bound over n layers: n C B^2/(n^2 eps^2). Markov for the background probability. (12) for the flat background. The closing caveats are accurate.

## H. The normalized winding (14) and the growing family, L263-L295

**S50. L263-L267, private links in all layers. HOLDS.** For withheld direction-1 links at z_2 + z_3 even, a (1,2) or (1,3) plaquette pairs opposite parities and a (1,0) plaquette pairs time zero with time +-1; no other plaquette has two direction-1 links. So the withheld links are conditionally independent with tilted densities, |b| <= 6 beta. Jensen and (13) give E[|m_l|^2 | X] <= E[n^2 |M_{l,0}|^2 | X] <= C B^2. Markov over layers gives Pr(more than n/2 bad | X) <= 2 C B^2/D_n^2 = O((log n)^{-2}).

**S51. L269-L273, one tilted spin. HOLDS.** The maximum density is at least one since Z(b) <= e^{|b|}. Within 5 eps of the maximum the log density drops by at most 6 beta 25 eps^2/2 < 1. The Haar element is sin(theta) dx d omega. The retained set gives an x-interval of length at least c eps^2 with x-density at least c eps^3 (sin theta >= sin eps), so a uniform component of mass c' eps^5. Its variance contribution is p L^2/12 = c eps^9 = c B^{-9}. Then |phi(t)| <= 1 - p(1 - |sin y / y|). Large frequency: integrating by parts, with total variation of the x-density at most C(B^{3/2} + 6 beta B^{3/2}) = C B^{5/2}. The stated C B^3/|t| is weaker and true.

**S52. L275, Fourier estimate. HOLDS.** Sigma = n^{-2} sum Cov(m_z) lies between (c/2) B^{-9} I and I/2. For |t| <= n^{1/16} the log remainder is O(|t|^3/n), integrated error O(n^{7/16 - 1}). For n^{1/16} <= |t| <= n the product is at most exp(-c B^{-9} |t|^2/2), whose tail integral tends to zero. For n <= |t| <= K n B^3 it is at most exp(-c n^2 B^{-9}), times a polynomial volume. Above K n B^3 it is at most (C n B^3/|t|)^N with N = n^2/2, whose integral is at most C (K n B^3)^4 (C/K)^N -> 0. The Gaussian density on the ball is at least (2 pi)^{-2} exp(-c_1^2/(2cB)).

**S53. L277, angular mixing. HOLDS.** |tau v - m_l| <= tau rho + |tau - |m_l|| <= r/8 + r/2 < r. Polar integration gives a component of mass at least c (r/4)^4 times the cap area, about c r^4 rho^3, equal to q times the uniform cap law at the identity. rho and p are at least inverse powers of log(2 + n).

**S54. L279-L291, (14). HOLDS.** nu_rho is conjugation invariant. The shell rho/2 <= theta <= rho has mass 7/8. On the shell: if d theta >= 2 the character ratio is at most theta/(2 sin theta), about 1/2; if d theta < 2, 1 - chi_d/d = d^{-1} sum_m (1 - cos(m theta)) >= c theta^2 (d^2 - 1)/3. So every nontrivial multiplier is at most 1 - c rho^2. Peter-Weyl: ||f^{*k} - 1||_2^2 = sum_{d>=2} d^2 |a_d|^{2k} <= (1 - c rho^2)^{2(k-1)} ||f||_2^2, with ||f||_2^2 = 1/Haar(ball), of order rho^{-3}. Binomial: Pr(fewer than np/4 ball factors) <= 16/(np). Centrality moves the ball factors to the end (right to left, each conjugated by fixed factors), and convolution with the rest contracts variation and fixes Haar. n p rho^2 >= n (log n)^{-C}. The bad-exterior bound is uniform in X. The remarks on R_0, on adding the reading after any history inside E (convexity of variation), and on its singular-value cost (row 1373 (7)) hold. "Including bounded beta" holds: no step uses beta -> infinity. New.

**S55. L293, many windings. HOLDS.** Exponents rechecked: K of order (n/m)^2 = n^{1/4}; per cell E[|sqrt(A) M|^2 | X] <= C B^2; bad cells: K 2 C B^2/D_n^2 = O(n^{-1/20} B^2); rho >= c B^{-5} n^{-3/20} and p >= c n^{-9/20} B^{-35}; K/(np) = O(n^{-3/10} B^{35}); n p rho^2 >= c n^{1/4} B^{-45}. The withheld sets of different cells are disjoint parts of one independent set, so given E the K products are independent, and product telescoping gives the joint bound. The total is O(n^{-1/20} (log n)^2). New.

**S56. L295, physical scope. HOLDS.** (13) and (14) need only w >= 1 and the band. At w', (9) gives 1 - D_S <= u (1 + s(2w'))^{-1/2} -> 0, since s(2w') -> infinity (S30).

## I. The final sufficient target, L299-L305

**S57. L299-L305, OPEN, the final target. Accurate; the implication HOLDS.** (8) holds in the whole band: r << n and xi <= n^{-A} -> 0, with no need for beta -> infinity. If limsup D_{S,j} < 1 - sqrt(21)/5, choose delta > 0 with 1 - D_{S,j} >= sqrt(21)/5 + delta eventually. Then (9) gives (1 + s(2 w_j))^{-1/2} >= (sqrt(21)/5 + delta)/u_j > sqrt(21)/5 eventually, that is s(2 w_j) < 4/21. The summary of what (3), (7), (10) and (14) control is accurate.

Weaker than the seed, or equivalent? **Not weaker.** On a fixed side the target implies the strict seed. The converse needs a larger margin. Since E Var(h_x | Y_S) <= Var(h_x), D_S <= D_face <= 1 - (1 + s)^{-2} (S25). So limsup s(2 w_j) < (25/21)^{1/4} - 1, about 0.0446, implies the target on the same side. But s <= 4/21 only gives D_S <= 1 - (21/25)^2 = 184/625, about 0.294, which is above 1 - sqrt(21)/5, about 0.0835. So on a fixed side the target lies between the seed and a stronger seed. It is not an exact rewriting of the seed, unlike row 1373 (17) (check 1374 S40). Over sides it is equivalent to the seed: the seed on any side gives, on a fixed dyadic enlargement, arbitrarily small limsup s(2 w_j) at this aspect (rows 1161 and 1355, as used in the converse of row 1367 (7) and checked in row 1369 S22), hence the target there. This is the structure of row 1367 (7): D <= 1 - sqrt(21)/5 suffices, and a passing side needs only D <= 1 - (sqrt(21)/5)^3.

## J. GUIDE lines, prior results and RESULT

**S58. L3, GUIDE. Accurate where checked.** Hashes and five-ref searches not refetched; they match rows 1367, 1371 and 1373. Not leaned on.

**S59. L5, GUIDE. Accurate** (a heading line).

**S60. L7, PROVED (prior). Accurate.** `gap-phys-seed.md` L311 states Theorem ZD-c as "PROVED GIVEN Theorem ZD and its inputs"; the lead note at L322 follows. Restates rows 1367 L7 and 1373 L3.

**S61. L8, GUIDE. Accurate.** Restates rows 1367 L7, 1371 L5 and 1373 L3.

**S62. L9, PROVED (prior). HOLDS for what the note uses.** The PR line 52 was not refetched. Both facts used are correct: given all non-pivot links, pivots with no common plaquette are independent; each one-link density is at least e^{-12 beta} times Haar, so every nontrivial multiplier is at most 1 - e^{-12 beta}. The sharper multiplier e^{-(d-1)/(1+6 beta)} is row 1145 (1), as used in row 1252 L255.

**S63. L10, GUIDE. Accurate where checked.** `gap-compress-check-astra.md` L9 and L79 confirm T2 and the FSS bound for unit S^3 spins. The S^2 remark and TQ55 section 2.2 were not checked; not leaned on.

**S64. L11, GUIDE. Accurate.** `lit-balaban.md` L147 lists CMP 122b Theorem 1 (ultraviolet stability under g_0, ..., g_K in (0, gamma]).

**S65. L12, GUIDE. Accurate** description of rows 1371 and 1373.

**S66. L13, GUIDE. Accurate where checked.** The SA index gives the transfer operator at 2315-2328 (the note writes 2313-2335, as row 1373 did), and 32487-32490 is the entry where any mass-gap estimate remains separate. The CA-I and CA-III lines were not reread.

**S67. L19, GUIDE. Accurate.**

**S68. L23, GUIDE. Accurate.** Row 1321 (`gap-solve38-astra62.md`, unordered slice pairs) and row 1351 (`gap-blockstep4-astra62.md`, strips) exist as cited.

**S69. L114, GUIDE. Accurate** (row 1367 (3) uses sqrt(l) as the trial vector).

**S70. L159, GUIDE. Accurate** (row 1252 L255-L272; row 1371 (9)).

**S71. L185, GUIDE. Accurate.**

**S72. L216, GUIDE. Accurate.** TB2 identifies the flat layer with the 3D O(4) model and bounds 1 - Z_anti/Z_per through the magnetization.

**S73. L261, GUIDE. Accurate.**

**S74. L307, RESULT. Accurate.** OPEN; (3) holds for beta_j -> infinity; (14) and the growing family hold throughout the band; the seed and the mass gap stay open. The note nowhere claims the seed proved or disproved, and states that no counterexample or failure of the checked chain was found.

## Restatements of earlier rows

- S1 (L17) restates the one-box target of rows 1367 L11, 1371 L11 and 1373 L13, with the row 1161 (19) exclusion of row 1367 L21-L27.
- S8-S11 (L49-L55) reuse the open-box machinery of rows 1151, 1339 (1)-(2) and 1371 L232-L263 (entropy, projections, word Taylor bound, Fisher bound), row 1231 (1) and (8), and row 1371 (6) for the neutral transfer. New there: a fixed finite graph with temporal edges, and variation convergence through Fisher information and compactness instead of smoothing.
- S14 (L73): the plaquette filling restates row 1371 L216.
- S20 (5) is row 1373 (7) applied to a detoured suffix.
- S21: the cap bound and the half-tilt transfer restate row 1371 L111-L115 and (6).
- S25: the first inequality of (6) uses the trial vector sqrt(l) of row 1367 (3).
- S26-S28: the packet is row 1231 (7), with its coordinate paths.
- S30 (L144): the short time w' and the log trace asymptotic restate row 1373 (16) with kappa = alpha, and the log 8 comparison restates row 1373 L206-L208.
- S31 (L146) builds on row 1173 L154 (antipodal covariance of one spatial mode).
- S35 (8) restates row 1252 L272 (straight coarse edges with b - 2 private links) and the orbit and tree channel of row 1371 L196-L202, here on a spatial grid with attached trees.
- S36 (9) is the upper half of row 1367 (3), A <= sigma, with A bounded below through D_S; S57's target has the same structure as row 1367 (7).
- S43-S44: the flat layer as an O(4) model is TB2 of `gap-compress-opus.md`; (12) is the FSS bound (T2, TB2).
- S48 (13) and S50-S54 (14) use the private-link multiplier of rows 1145 (1) and 1252 L255.
- S54: the singular-value cost of an added reading is row 1373 (7).
- New and checked here: the separator (1); kappa in (2) with its free and pinned bounds; (3); the uniform detour version (4) and S17; (5a); the exact identity for d_e and (6); (7); the Gaussian example of S32-S33; (9) in its D_S form; the repair test S37; (10)-(11) with the Mehler step; the flat-layer neutral signal S46; (13); the local limit and angular mixing behind (14); the growing winding family S55.

## Summary table

| S | Lines | Statement | Verdict |
|---|---|---|---|
| 1 | 17 | the physical test (OPEN) | HOLDS (accurate) |
| 2 | 25-30 | separator (1) | HOLDS |
| 3 | 32-39 | (2), kappa | HOLDS |
| 4 | 41 | free upper bound | HOLDS |
| 5 | 43 | boundary lower bound, energy kappa | HOLDS |
| 6 | 45 | Gaussian channel error | HOLDS |
| 7 | 47 | finite spacetime graph input | HOLDS, given rows 1151, 1231, 1339, 1371 (remark: placement at the near face covered by L53) |
| 8 | 49 | linear part, O(sqrt(Delta)) | HOLDS |
| 9 | 51 | covariance limit, nonlinear error | HOLDS |
| 10 | 53 | frames, neutral circle | HOLDS |
| 11 | 55 | variation via Fisher information | HOLDS |
| 12 | 57-67 | (3) | HOLDS |
| 13 | 71 | uniform over detoured sets | HOLDS |
| 14 | 73-78 | (4), kappa_M | HOLDS |
| 15 | 80 | upper variance 1/kappa_M | HOLDS |
| 16 | 82 | lower variance | HOLDS |
| 17 | 84 | uniformity by compactness | HOLDS |
| 18 | 86 | n^3/2 detoured bonds | HOLDS |
| 19 | 88 | suffix, m_j eta_j | HOLDS |
| 20 | 90-94 | (5) | HOLDS |
| 21 | 96-101 | (5a), inputs | HOLDS |
| 22 | 103-108 | (5a), proof | HOLDS |
| 23 | 110 | variance 3/kappa | HOLDS |
| 24 | 116-128 | (6) | HOLDS |
| 25 | 130 | proof of (6), 1-r <= D_face <= 1-r^2 | HOLDS |
| 26 | 132-136 | (7) | HOLDS |
| 27 | 138 | packet norms, V_J >= cR ||J||^2 | HOLDS |
| 28 | 140 | packet test f | HOLDS |
| 29 | 142 | detour substitution, lambda_sp <= C/R | HOLDS |
| 30 | 144 | short-time test | HOLDS, given row 1153 (5) |
| 31 | 146 | Gaussian example, statement | HOLDS |
| 32 | 148 | zero mode, s(2w) > 4/21 | HOLDS |
| 33 | 150-155 | b - a = O(n^{-4}), sum d_e = O(1/n) | HOLDS (remark: large constant) |
| 34 | 161 | prefix S | HOLDS AFTER CORRECTION (title: detour lengths O(r), not bounded) |
| 35 | 163-168 | (8) | HOLDS |
| 36 | 170-179 | (9) | HOLDS |
| 37 | 181 | lambda_H -> 0 in probability | HOLDS |
| 38 | 187-194 | (10) | HOLDS |
| 39 | 196 | available variations | HOLDS |
| 40 | 198-203 | (11), sum Pi_i >= I | HOLDS |
| 41 | 205-210 | Mehler step | HOLDS |
| 42 | 212 | likelihood version (OPEN) | HOLDS (accurate) |
| 43 | 218-222 | flat conditional law, R_t | HOLDS |
| 44 | 224-229 | (12) | HOLDS |
| 45 | 231-243 | magnetization concentration | HOLDS |
| 46 | 245 | neutral signal, loss -> 1 | HOLDS |
| 47 | 247 | scope (ARGUED) | HOLDS (accurate as ARGUED) |
| 48 | 249-255 | (13) | HOLDS |
| 49 | 257 | small layer means | HOLDS |
| 50 | 263-267 | private links in all layers | HOLDS |
| 51 | 269-273 | one tilted spin | HOLDS (remark: B^{5/2} would do for B^3) |
| 52 | 275 | Fourier estimate | HOLDS |
| 53 | 277 | angular mixing | HOLDS |
| 54 | 279-291 | (14) | HOLDS |
| 55 | 293 | K windings jointly | HOLDS |
| 56 | 295 | physical scope, D_S -> 1 at w' | HOLDS |
| 57 | 299-305 | final target (OPEN) | HOLDS (accurate); not weaker than the seed; same-side sufficient, existentially equivalent |
| 58-73 | 3, 5, 7, 8, 9, 10, 11, 12, 13, 19, 23, 114, 159, 185, 216, 261 | GUIDE lines and two prior PROVED items | accurate (L3, L9, L10, L13 only spot-checked) |
| 74 | 307 | RESULT | accurate |

Counts: 74 statements (55 PROVED, 1 ARGUED, 3 OPEN, 14 GUIDE, 1 RESULT); 73 HOLD; 1 HOLD AFTER CORRECTION (S34, wording only); 0 FAIL.

## What remains open

A cutoff-uniform bound limsup_j D_{S,j} < 1 - sqrt(21)/5 at w_j = floor(n_j/1024) on one admissible side, or any other route to limsup s(2 w_j) < 4/21 there. The note's estimates cover single links with dense histories (3), detoured suffixes of size m_j with m_j eta_j -> 0 ((5), (5a)), local tests for whole-direction blocks (10), and the K winding products (14). None bounds the full likelihood h_x after the coarse grid, the passage of (10) to h_x is open (S42), and (7) and S37 show that single-edge relaxation rates vanish. Hence the one-box Wilson seed and the mass gap remain open. No step of the note is a counterexample to the checked chain.

RESULT: Row 1375 (`library/gap-seed4-astra62.md`) checked line by line by hand by Claude Opus 5.5 (laptop Claude subagent, FINISH row 1376; cross-provider; grants no status): 74 statements (55 PROVED, 1 ARGUED, 3 OPEN, 14 GUIDE, 1 RESULT), 73 HOLD, 1 HOLD AFTER CORRECTION, 0 FAIL; main correction: L161's title "bounded detour lengths" should read "detour lengths O(r)", since r grows with the cutoff and the uniform screening (3), (5a) needs a fixed D_0 (the note's L168 says this; no mathematics changes); remarks only: the finite-graph input stated inside one arc is used around the near face, which L53's translation invariance covers; L269's C B^3 can be C B^{5/2}; the O(1/n) in the Gaussian example has a large constant; holds as stated: the separator (1), kappa in (2), the dense single-link decoupling (3) for beta_j -> infinity, its uniform detoured form (4) with the suffix bound (5) and (5a), the exact identity for d_e and the full-face bound (6) with 1 - r <= D_face <= 1 - r^2, lambda_sp -> 0 in (7), the Gaussian example with sum d_e -> 0 and s(2w) > 4/21, the coarse grid (8) (a restatement of row 1252 L272 with the row 1371 orbit channel), (9), lambda_H -> 0, the three-direction inequality (10)-(11), the flat-layer signal and (12)-(13), (14) throughout the band and the joint decoupling of K of order n^{1/4} windings with error O(n^{-1/20} (log n)^2); final target limsup D_{S,j} < 1 - sqrt(21)/5: the implication to s(2 w_j) < 4/21 holds with every hypothesis met, and the target is not weaker than the seed: on a fixed side it implies the strict seed and is implied only by the stronger limsup s(2 w_j) < (25/21)^{1/4} - 1 (about 0.045), so unlike row 1373 (17) it is not an exact rewriting of the seed, while over sides it is equivalent to the seed through the shape propagation of rows 1161 and 1355 (as in row 1367 (7)); open: that bound, or the seed by any route, at w_j = floor(n_j/1024) on one admissible side, hence the Wilson seed and the mass gap; the note nowhere claims the seed proved or disproved.
