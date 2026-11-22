# Check of `library/gap-seed3-astra62.md` (FINISH row 1374)

Checked by Claude Opus 5.5 (laptop Claude subagent), cross-provider check of a gpt-6.2-astra row; grants no status.

Status: complete. 51 statements (38 PROVED paragraphs, 2 OPEN, 10 GUIDE, 1 RESULT): 51 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL. The note nowhere claims the seed proved or disproved. Main remark: the sufficient estimate (17) is equivalent to the seed with a strict margin (S40).

## Verdicts

Method. I read the note in full, then row 1367 (`gap-seed-astra62.md`) and row 1371 (`gap-seed2-astra62.md`) in full, and the cited parts of rows 1151, 1153, 1161, 1231, 1272, 1337, 1339, with the relevant verdicts in their checks (`gap-solve5-check-opus.md`, `gap-solve6-check-opus.md`, `gap-solve45-check-opus.md`, `gap-seed2-check-opus.md`). I did not read `gap-seed4-astra62.md`. I redid each step by hand. One small numeric guide (not a proof step): a one-dimensional quadrature gives c = 0.1078 in (9). Line numbers L refer to the target note.

### A. The test and the finite-circle threshold (positive claims, first group)

**S1. L13, OPEN, the test on the cube. Accurate.** s(t) decreases in t since 0 <= lambda_a/lambda_0 < 1, so w = floor(n/1024) is the most favorable allowed time, and a_j w -> L/1024. The remark on row 1161 (19) restates row 1367 L21-27. The continuum hypotheses are as in row 1349. Restates the target of rows 1367 and 1371.

**S2. L21-33, (1)-(2), exact retained fraction. HOLDS.** With B_i(x,h) = sqrt(j_i(x,h)), A_i = B_i B_i^* and ||B_i||_HS^2 = int j_i = 1, so A_i >= 0, Tr A_i = 1, A_i(x,x) = l(x). At i = 0 the kernel is sqrt(l(x) l(x')), so r_0 = int l = 1. At i = m, F^w(x,y) >= 0 pointwise and F^w is symmetric, so int sqrt(J(x,y) J(x',y)) dy = F^{2w}(x,x')/Z_{2w}, and r_m = lambda_0^{2w}/sum_a lambda_a^{2w} = (1+s(2w))^{-1}. A_m = B^2 for the kernel B of row 1367, so r_m is row 1367's sigma^2.

**S3. L35-39, one-link decrement. HOLDS.** j_i(x,(h,v)) = j_{i-1}(x,h) p_{x,h}(v), so A_i inserts c_i in the h integral, and 0 < c_i <= 1 by Cauchy-Schwarz. For a nonnegative kernel the top of the Rayleigh quotient is attained on nonnegative vectors, and there the pointwise order A_i <= A_{i-1} gives r_i <= r_{i-1}. Trace one gives the 4/25 remark: r >= 21/25 leaves at most 4/25 for the other eigenvalues, and r_m >= 21/25 is s(2w) <= 4/21.

**S4. L41-52, (3), finite copies. HOLDS.** Integrating each h_a gives A_{i-1}(x_a, x_{a+1}); the cyclic product integrates to Tr A_{i-1}^k = C_{i-1,k}, so the law is normalized. Factoring j_i = j_{i-1} p gives C_{i,k}/C_{i-1,k} = E_{i-1,k} prod_a c_i(x_a,x_{a+1};h_a) <= 1, hence the nonnegative increment. C_{m,k} = Tr(F^{2w}/Z_{2w})^k = Z_{2kw}/Z_{2w}^k, and G_{0,k} = 0 since A_0 is a rank-one projection. In terms of s, G_{m,k} = log(1+s(2w)) - k^{-1} log(1+s(2kw)), the form used at L212. New: a thermal k-replica telescoping identity; row 1371 (22) is the vacuum-likelihood analogue.

**S5. L54-59, (4), sharp error at the threshold. HOLDS.** C >= r^k gives G <= g, so the left inequality. If r >= q: the other eigenvalues sum to 1 - r, so C <= r^k + (1-r)^k and G >= g - k^{-1} log(1 + ((1-r)/r)^k) >= g - eps_k, since (1-r)/r <= 4/21. If r <= q: either r in [1/2, q], where C <= phi(r) <= phi(q) with phi(t) = t^k + (1-t)^k increasing on [1/2,1], or r < 1/2, where C <= 2^{1-k} = phi(1/2) <= phi(q). Both give G >= theta - eps_k, since q^k + (1-q)^k = q^k (1 + (4/21)^k). Equality holds for the spectrum (q, 1-q). For k >= 5 log n / log(21/4), (4/21)^k <= n^{-5}, so eps_k <= n^{-5}/k. The inequality is strict for r < q, so G + eps_k <= theta already forces g <= theta.

**S6. L61, projected one-link data. HOLDS.** The six-plaquette mixture with |b| <= 6 beta and the bounds e^{-12 beta} <= p <= e^{6 beta} restate row 1367 L94-101. The Taylor bound e^{6 beta} 2^{-(d+1)} for d+1 >= 24 e beta restates row 1367 L115-121; the factor 1 + sqrt(dim Pi_d) restates row 1371 L407. I checked the new degree choice: 2^{d+1} >= e^{30+30 beta} n^{22}, which exceeds (1 + (d+1)^{3/2}) e^{18 beta} n^9 for all n >= 2 in the band, so ||Pi_d p - p||_inf <= n^{-9} e^{-12 beta} and Pi_d p / p lies in [1 - n^{-9}, 1 + n^{-9}]. The geometric mean in c_i keeps that relative error, the k-fold product and its expectation keep it to the k-th power, and -k^{-1} log costs at most 2 n^{-9} per link, so 6 n^{-6} over 3 n^3 links. The history laws stay exact, as stated.

### B. What the near-face exterior can predict, (5)-(6)

**S7. L67-74, statement (5). HOLDS, given rows 1151, 1231 (8), 1339 (2) and 1371** (proof S8-S15). The error terms match the proof: sqrt(d Delta) from the linear comparison, d(1/b + b/n + b/w) from omitted shifts, d e^{-c beta/b^8} from bad boxes; the smoothing terms C sqrt(d/b) and the truncation C d e^{-c beta} are absorbed since Delta >= 1/b. R_beta is invariant under conjugation and inversion, so E-measurable frames do not change the reference. New: row 1371 (7) and row 1339 (3) gave conjugacy angles against the opposite face only; here the matrices are compared with E, which adds all axial links and the distant same-face links.

**S8. L76, neutral domination. HOLDS.** The 64 seam pairs have positive masses and the 8 equal pairs have ordinary mass, so Z_{2w} >= Z_ord/8. Each arc from X to Y contains one projection, so the raw two-face law is J; a translated sheet differs by a vertex gauge, so J is translation invariant. All dropped actions, including the signed seam terms beta(1 -+ Re U_p), are nonnegative, so the density ratio is at most prod Z_B / Z_{2w} <= 8 prod Z_B / Z_ord <= 8 e^{C V Delta}. This restates row 1371 L287 and row 1339 (1); like row 1371 L174 (row 1372 remark) it uses the row 1151 gluing comparison at period 2w without re-deriving it.

**S9. L78, colouring and conditional independence. HOLDS.** A plaquette reading internal edges of two boxes needs the boxes adjacent; bounded degree allows a greedy colouring. Given D (all edges outside the colour's boxes, their raw trees, the seams), the action splits box by box, so same-colour boxes are independent. Under the open-box reference each box measure is invariant under its own vertex gauges, so the raw tree is product Haar and independent of the tree-gauged variables.

**S10. L80-86, (6). HOLDS.** Under the reference, Z_B is independent of D with density at most 1 + e^{C b^3} relative to g_B (good chart from row 1151 L313, plus one Gaussian copy for the bad part). The domination 8 e^{C V Delta} passes through the completion kernel. So the joint density relative to Q_D (x) prod g_B is at most 8 e^{C V Delta} (1 + e^{C b^3})^{V/b^4}, and (V/b^4) C b^3 = C V/b <= C V Delta. The chain rule removes D(L(D) || Q_D) >= 0. Given D the boxes of one colour are independent, so the entropy is a sum; adding the other same-colour boxes to the conditioning does not change each box's law, which gives each box conditioned on its full exterior. Summing over the bounded set of colours gives (6). New: rows 1339 (1) and 1371 L287 conditioned on the cuts only.

**S11. L88, one projected vector per mark. HOLDS.** N(w-1) shifts; the omitted fraction is C d (1/b + b/n + b/w). Marks more than 4b+4 apart lie in boxes more than 2b apart, so the boxes are not neighbours and are conditionally independent given their common exterior, trees and seams; each box's law given that exterior equals its law given its own exterior.

**S12. L90, linear curls. HOLDS.** v_p = (1 - c_0/b)^{-1} Pi_pp with Pi_pp >= 1/6 (row 1339 V7). sum_p P_p <= (min v_p)^{-1} L^* L <= C I. Row 1339 (2) applies conditionally. Row 1151 §12 gives sum_{p in B} (v_p - 1/2)^2 = O(b^3) per box (O(b^2) from the dilution). A face is the j-th mark at one shift, so at most d times. Summing over shifts: entropy at most C d V Delta for the conditional law and C d V/b for the variances; Pinsker and Jensen over about V/2 shifts give C sqrt(d Delta). Restates the method of row 1339 L44-48 with the conditioning of (6).

**S13. L92, return to matrix holonomy. HOLDS.** The raw U_j is P^{-1} U~_j P with P the raw tree transport, measurable in the conditioning. |U~_j - exp(sum +- X_e)| <= C (sum |X_e|)^2 <= 4C b^{-7/2} sum |X_e| on the good chart (row 1371 L254-258). Row 1231 (8) gives sum |X_e|^2 <= C b^5 sum (1 - Re U_p) on a good box. Each edge is counted at most 4d times over shifts and marks, so beta times the squared error, averaged over shifts, is at most C d b^{-2} E beta (1 - Re U_p) <= C d/b^2. Restates row 1371 L254-263 for one plaquette.

**S14. L94, the two Wilson estimates for the neutral law. HOLDS.** E_+ H = Z_+^{-1} int k_+ k e by moving the projection to the last bond and invariance of k_+; Cauchy-Schwarz and conditional Jensen give (8 E_ord H^2)^{1/2}. The internal action and the box chart test are invariant under a flat centre change inside a contractible box (it is a vertex gauge there). Restates row 1371 (6) and L214, L294.

**S15. L96-98, smoothing and its removal. HOLDS.** TV of two radially projected Gaussian translates is at most D_0/(2 tau); with E D_0^2 <= C d/(beta b^2) and tau = (beta b)^{-1/2} the replacement costs C sqrt(d/b). In a 23 square away from the comb planes all four edges are non-tree; one chosen edge per mark, in non-neighbouring boxes, has the one-link density with |h| <= 6 beta given everything else, Fisher information 3 E h.v <= 18 beta, and the right increment acts on it by a Haar isometry. So removing smoothing costs C tau sqrt(beta d) = C sqrt(d/b) (restates row 1371 L250-252). The truncated reference has Fisher information C beta: the radial multiplier has O(1) derivative in log coordinates, the Gaussian part O(beta), the Jacobian O(1). Truncation costs C e^{-c beta} per mark. Each component of E is outside the marked boxes or an internal direction-1 tree link, so marginalizing to E is a contraction.

### C. Charging a prefix, (7)-(8)

**S16. L102-106, (7). HOLDS.** For the second law the square-root kernel is B_H I^* with I f(h,u) = f(h) sqrt(r(u|h)) an isometry, so its Gram operator is B_H B_H^* and its top singular value is sqrt(r_H). ||B_{H,U} - B_H I^*||_HS^2 = int (sqrt p_1 - sqrt p_2)^2 <= int |p_1 - p_2| = 2 TV <= 2 eta, and the operator norm is at most the HS norm. Cauchy-Schwarz in u gives A_{H,U} <= A_H pointwise, so r_{H,U} <= r_H. The rank-one remark: int sqrt(mu nu) >= 1 - TV gives r_{H,U} >= (1 - eta)^2. Applying (5) to H a function of near-face pins is a pushforward of (5). New.

**S17. L108-113, (8). HOLDS.** The fundamental cycle of the chord at z_j is root, along the line to z_j, three square edges, the chord, back; its based holonomy is P_j U_j^{+-1} P_j^{-1} with P_j a product of direction-1 links in E. By (5) and the conjugation and inversion invariance of R_beta, (X, based holonomies) is within eta of L(X) (x) R_beta^{(x)d}. Given X, the Y law is gauge invariant; root-fixed gauges fix the based holonomies and act freely and transitively on the tree, so the tree is product Haar given X and the holonomies, under both laws. (Tree, chords) and (tree, holonomies) correspond bijectively. So (X, prefix) is within eta of a product, and (7) gives r_{i_*} >= (1 - eta)^2; G <= g gives (8). With d = floor(sqrt b) and spacing 5b+10, eta -> 0 and the line has length O(b^{3/2}) = o(beta). The count 2n^3 + 1 - d is right. Extends row 1371 L176-178, whose last sentence left exactly this joined case open; the tree step restates row 1371 L202.

### D. The next reveal with a neighbouring plaquette known, (9)-(10)

**S18. L119-126, (9). HOLDS** (proof S19-S21). With t_mu = e^{i k_mu} - 1, the curl projection at k != 0 is d d^*/|t|^2 (d t = 0), so its (12,13) entry is t_2 conj(t_3)/|t|^2 (only a_1 is shared). Its real part is (1 - cos k_2)(1 - cos k_3) + sin k_2 sin k_3, and the sine product integrates to zero, which gives (9). The shared edge (z,1) enters both curls with sign +1, so c > 0. The denominator is at most 16 and the numerator integrates to 1, so c >= 1/16. The diagonal is E[(u_1+u_2)/sum u] = 1/2. Guide only: quadrature gives c = 0.1078, rho = 2c = 0.216. A shared base gives a common conjugation.

**S19. L128, ellipticity of the two-row curl. HOLDS.** The edges (z+1,2) and (z+1,3) each lie in one of the two squares only. Their curl field has squared norm at most 24 |u|^2 (the bound is generous: the 23 face at z+1 holds both), and its pairing with the two-square cochain is |u|^2, so both eigenvalues are at least 1/24. Summed row-space projections over translates are bounded since each face is counted a bounded number of times.

**S20. L130, limit covariance. HOLDS.** The squared HS bound O(b^3) of row 1151 §12 controls the mixed entries as well as the diagonals. The b-periodic symbol is t_2 conj(t_3)/|t|^2, bounded by 1/2 and continuous off zero, so the Riemann sums converge to (9). The test field of S19 also lies in the periodic curl image, so v_b - c_b >= 1/24 and in the limit c <= 1/2 - 1/24 < v.

**S21. L132, nonlinear step for two matrices. HOLDS.** Edges (z+1,2) and (z,3) have x_1 coordinates z_1+1 and z_1; a plaquette holding both would be a 23 plaquette at one x_1, so none exists. Neither is in E or in the other square. The correlated Gaussian with covariance Sigma (x) I_3 has Fisher information O(beta) after truncation, and it is invariant under the common rotation.

**S22. L134, local predictor. HOLDS.** The conditional normal law is N(rho V_q', v(1 - rho^2) I_3). Replacing only the (V_q', E) marginal costs at most the joint error, so the mean conditional TV is at most twice it. The same channel without X gives the X-free statement, and (7) applies with eta equal to twice the joint error.

**S23. L136-142, (10). HOLDS.** D = beta theta^2/2 and A = beta(1 - cos theta): D <= (pi^2/4) A and |D - A| <= D^2/(6 beta). Under the Gaussian, E[D_p | D_q'] = (3/4)(1 - rho^2) + rho^2 D_q' (v = 1/2). Risks of [0,M]-valued predictors change by at most M^2 TV, so the excess risk of the clipped predictor under the true law is at most the Gaussian excess plus 2 M^2 TV. The uniform exponential moment (half tilt plus the insertion bound of S14) removes the clips and the D to A change in L^2. Projection to a smaller history is an L^2 contraction.

**S24. L144, size of the effect. HOLDS.** D = chi^2_3/4 under N(0, I_3/2), so Var -> 6/16 = 3/8. Var of the predictor is rho^4 (3/8) = 6 c^4 >= 6/16^4 = 3/32768. Cov(|V_p|^2, |V_q'|^2) = 6 c^2, so Cov(D_p, D_q') = 3c^2/2 >= 3/512. Guide values: 6c^4 = 8.1e-4, 3c^2/2 = 0.0174.

### E. A patch after a dense exterior, (11)-(12)

**S25. L150-159, (11). HOLDS** (proof S26-S28). Same bound as row 1371 (12); the new content is that the distant same-face links O join X in the conditioning. The smallness condition (s+1)^5 log beta = o(b) is what makes the first term vanish.

**S26. L161, patch curl projection. HOLDS.** A box of side b containing Q has all its links within b of Q, so E' lies in its exterior and (6) applies. D^* a = d_1^* a extended by zero, so ||P a|| >= ||d_1^* a||/||D||; the kernel of L L^* is ker d_1^*, and on its complement the path Laplacians give ||d_1^* a||^2 >= (s+1)^{-2} ||a||^2. Multiplicity O((s+1)^3) gives sum_v P_v <= C (s+1)^5 I and the cost C (s+1)^{5/2} sqrt(Delta). Restates row 1371 L232-244 with (6) in place of the cut conditioning.

**S27. L163, words and smoothing. HOLDS.** With tau = h (beta b)^{-1/2}: smoothing removal C tau sqrt(18 beta k_0) and replacement C sqrt(k_0 h^4/(beta b^2))/(2 tau) are both C sqrt(k_0) h/sqrt(b) <= C (s+1)^{5/2} b^{-1/2}. Keeping the reference smoothed is legitimate since it is only a stand-in for a product law. Restates row 1371 L246-265.

**S28. L165, orbit channel. HOLDS.** Gauges at patch vertices move only links touching the patch, none of which are in O or X. The marginal of (D_Q, E') is invariant, its orbits are simultaneous conjugacy classes of the based words, and the conditional law on an orbit is the unique invariant one. Restates row 1371 L270.

**S29. L167-171, (12). HOLDS.** Under the product law, U given (X, H) depends only on the patch part of H; swapping in the true (X, H) marginal doubles the error, so eta = 2 zeta. min(theta, -2 log u) is 2/sqrt(q)-Lipschitz on [0,1], (7) moves sqrt(r) by at most 2 sqrt(zeta), and (4) at the two ends adds eps_k: total 4 sqrt(zeta)/sqrt(q) + eps_k. The buffer has O(b^3) links, so 3n^3 - O(b^3) outside links can come first. The closing caveat (buffer pins are not covered) is accurate.

### F. Arbitrary locations, (13)-(14)

**S30. L177-184, (13). HOLDS** (proof S31-S35). The links of every marked box lie within b of S, so O_S and X are in the common exterior. d^5 log beta = o(b) makes every term vanish; d <= beta^alpha with 5 alpha < gamma < 1/12 gives alpha < 1/60. Partial earlier observations of S are handled as in S29.

**S31. L186, forest and words. HOLDS.** Each fundamental word uses its own chord once and tree paths of length below d, so h = 2d+1 is safe and there are at most d words. A component with at most d < b/4 edges has diameter below n and lifts. Bounding rectangles have total span O(d), so the omitted fraction is O(d(1/b + b/n + b/w)).

**S32. L188-194, (14). HOLDS.** The chain rule with a product reference is exact; C and the earlier Y_B are functions of D_{B_j} and the independent completion noises, which do not change the law of Y_{B_j} given D_{B_j}; convexity of relative entropy lowers the mean when the conditioning is reduced. No independence between touching boxes is used. New.

**S33. L196, word eigenvalues. HOLDS.** Var(sum u_c circ_c) = sup_a (sum u_c circ_c(a))^2/((1 - c_0/b)||Da||^2), and any edge field is allowed since circulations and curls are gauge invariant. The chord-supported field gives numerator (sum u_c^2)^2 and ||Da||^2 <= 4 * 6 * sum u_c^2, so the eigenvalues are at least about 1/24.

**S34. L198, fillings. HOLDS.** For a filling with m <= h^2 signed faces, sum_v <f, tau_v phi>^2 <= m * m ||f||^2 = h^4 ||f||^2. Composed with the bounded whitened curl and summed over at most d words, sum_v P_{v,B} <= C d h^4 I; (2) and (6) give C d h^4 Delta per placement and, with h = 2d+1, the term d^{5/2} sqrt(Delta). The filling construction restates row 1371 L216.

**S35. L200, orbits and the end of (13). HOLDS.** The Taylor and smoothing costs count word occurrences, giving C sqrt(d) h/sqrt(b) = C d^{3/2}/sqrt(b). Taking orbits per component removes the different root frames, also for correlated components in one box. No link of O_S touches a vertex of S, so the S-vertex gauges preserve E_S and give the invariant law on the product of orbits. For a forest the orbit is everything and D_S is exactly independent of E_S (restates row 1339 V1 and row 1367 L92).

### G. The whole-face test, (15)-(16)

**S36. L204, what a reveal order can cover. HOLDS.** Take two covered links in one cell of side at most b, the later with patch Q_2. The earlier is within b < 2b+2 of Q_2, so the rule puts it inside Q_2; hence all covered bases in a cell have coordinate ranges at most s+1, giving at most 3(s+2)^3 links per cell and C n^3 (s+2)^3/b^3 in all. For s < b/4 this is a small fraction of 3n^3. The caveat about removing pins is accurate.

**S37. L206-208, the log 8 comparison. HOLDS.** The ordinary Perron vector is unique and positive and the centre maps commute with T and preserve positivity, so it is neutral and both traces share lambda_0. Tr(P_0 T^t) <= Tr(T^t) (positive T, projection), and Tr(P_0 T^t) = (1/8) sum_g Tr(U_g T^t) >= (1/8) Tr(T^t) since each Tr(U_g T^t) = int T^t(gx, x) dx >= 0. A trace-level analogue of row 1371 (6).

**S38. L210-216, (15). HOLDS, given row 1153.** Row 1153 L101 gives 0 <= g_s <= J_s <= 2 g_s with J_s = 2 g_s - g_{2s}, and (23) there bounds J at the even m nearest e_beta^{-1/4} by C n^3 e_beta^{3/4} (row 1153 check, 6.18: HOLDS). Since u < t eventually and g_ord decreases, g_+(t) <= g_ord(t) <= g_ord(u) <= J_u. With G_{i_*} >= 0 and G_{m,k} = g_+(t) - k^{-1} g_+(kt) <= g_+(t), (15) follows; e_beta^{3/4} = beta^{-3/16} [log(2+beta)]^{3/4}. The bound diverges in the band, as stated. The quoted loss (7) of row 1153 is accurate (row 1153 L111-114). Imports row 1153.

**S39. L218-224, (16). HOLDS, given row 1153 (5).** With 2 gamma < kappa < 1/16: b^2/w' = beta^{2 gamma - kappa} -> 0, so Delta = O((log beta)/b), and (k t')^4 e_beta = O(beta^{4 kappa - 1/4} log beta) -> 0, so row 1153 (5) gives g_ord(m) = (pi^2/15 + o(1)) n^3/m^3 at m = t' and k t'. The log 8 gap is negligible against n^3/t'^3. Then G_{m,k}(t') = (pi^2/15)(1 - k^{-1} k^{-3}) n^3/t'^3 (1 + o(1)), which is (16). The local estimates hold at w' because their w-dependence is only through b/w' and the shift count: for (13), d b/w' = beta^{alpha + gamma - kappa} -> 0 since kappa > 2 gamma > gamma + 5 alpha. So the total diverges while every local bound holds. This has the structure of row 1371 L276 (there w' = floor(sqrt(log n)) and row 1161 (19)); the leading constant is new. The closing sentences are accurate: a_j w' -> 0, and row 1161 (19) gives c n^3 e^{-2Cw} -> 0 at the physical w.

### H. The sufficient estimate (17) and its implication

**S40. L226-232, OPEN, (17) and the claimed implication. Accurate; the implication HOLDS.** Direction and constants. Let Sigma_j be the sum in (17). By (3), G_{m,k_n} = G_{i_*,k_n} + Sigma_j. The prefix term is exactly 0 for the spanning-tree order (root-fixed gauges, restating row 1367 L92), or at most -2 log(1 - eta_j) -> 0 for the connected order (8), which needs beta_j -> infinity and the regime of (5). If limsup Sigma_j < theta = log(25/21), pick delta > 0 with Sigma_j <= theta - 3 delta eventually; the prefix term and eps_{k_n} <= n^{-5}/k_n are each at most delta eventually. Then (4) gives min(theta, g_m) <= G_{m,k_n} + eps_{k_n} <= theta - delta, so g_m = log(1 + s(2w)) < log(25/21), that is s(2w) < 4/21, at every late cutoff. The projected readings change Sigma_j by at most 6 n^{-6} (S6). k_n -> infinity is what lets a margin below theta suffice; any fixed k would need a margin eps_k. All hypotheses are met as stated.

Remark (important, not a correction). For the tree order, Sigma_j = G_{m,k_n} = g_+(2w) - k_n^{-1} g_+(2 k_n w) exactly, and 0 <= g_+(2 k_n w) <= g_+(2w), so (1 - 1/k_n) g_+(2w) <= Sigma_j <= g_+(2w). Hence (17) is equivalent to limsup_j s(2 w_j) < 4/21, the seed with a strict asymptotic margin; for the connected order the same holds since G_{i_*} -> 0. (17) is therefore the strict seed rewritten as a sum of per-link terms, not a weaker sufficient condition. The note does not claim more, and L232 states that no upper estimate for (17) is known. The same is true of row 1371 (23), and the row 1372 check left the same open target.

The closing sentences of L232 are accurate: a disproof needs failures on a cofinal subsequence for every admissible side; the claims are author-only.

### I. GUIDE lines, RESULT

**S41. L3, GUIDE. Accurate where checked.** The five-ref search results and the PR line numbers were not refetched; they match rows 1367 and 1371. Not leaned on.

**S42. L5, GUIDE. Accurate.** On origin/main, `compact-forest-exchange.md` (7) is Cov = (1/2) E[D tanh(Delta_R/2)]; `research/mass-gap/library/gap-ds-gauge.md` (also in this folder) has Theorem W under the weighted hypothesis (W).

**S43. L7, GUIDE. Accurate.** Row 1337 (1) is the crossed affinity with A(0) = Z_{2T}/Z_T^2; row 1339 bounds part of its integral; `gap-compress-opus.md` §2.3 states I(X_A; X_{A^c}) <= 2 beta_W |P_d|; `gap-afield-b-max.md` B4 poses (CMI) as a hypothesis; the row 1207 cross-ratio check exists as cited.

**S44. L9, GUIDE. Accurate where checked.** The SA index gives the transfer operator and GL8 at 2315-2335 (the note writes 2313-2335), 3712-3720 and 31871-31882 as described. CA-I, CA-III and the Balaban lines were not reread; not leaned on.

**S45. L15, GUIDE. Accurate.**

**S46. L19, GUIDE. Accurate.** Row 1337's A(0) = Z_{4w}/Z_{2w}^2 is C_{m,2} here, the two-copy case at full observation. The Eckart-Young reference is row 1356 as in row 1367 L13.

**S47. L65, GUIDE. Accurate.** Row 1371 (7) and the open question at its L178; row 1272 (31)-(32) bound a long private transport by e^{-c r/(1+beta)}.

**S48. L117, GUIDE. Accurate.** SA index chunk 02 lists the curl symbol at 1735-1747, 1749-1762, 1771-1778.

**S49. L148, GUIDE. Accurate.** Row 1231 (37)-(40) and row 1371 (10)-(12) are as described.

**S50. L175, GUIDE. Accurate.** Row 1231 (37) and the grid of patches after (40) are as described.

**S51. L234, RESULT. Accurate.** OPEN; the threshold recovery is (3)-(4) with eps_{k_n} -> 0; the decoupling is (13) with E_S, for beta_j -> infinity; the full sum is left open. The note nowhere claims the seed proved or disproved.

## Restatements of earlier rows

- S1 (L13) restates the one-box target of rows 1367 L11 and 1371 L11, and the row 1161 (19) exclusion of row 1367 L21-27.
- S2: r_m = (1+s(2w))^{-1} is sigma^2 of row 1367 (3).
- S6 (L61): the six-plaquette mixture, the Taylor bound and the projection factor restate row 1367 L94-121 and row 1371 L407; the projected-sum argument parallels row 1371 (23).
- S8 (L76) restates row 1371 L287 and (6), built on row 1339 (1).
- S12-S15 (L90-98) reuse row 1339 L44-48 (projections, variances), row 1371 L250-263 (Fisher bound, smoothing channel, Taylor error) and row 1231 (8); S14 (L94) restates row 1371 (6), L214 and L294.
- S17 (L108): the tree-Haar step restates row 1371 L202 and row 1367 L92; the joined prefix itself is new (row 1371 L178 left it open).
- S26-S28 (L161-165) restate row 1371 L232-270 with (6) as the conditioning; only the dense exterior O is new.
- S34-S35: the filling restates row 1371 L216; the forest statement restates row 1339 V1 and row 1367 L92.
- S38 (15) imports row 1153 (23) and L101; S39 (16) has the structure of row 1371 L276 with row 1153 (5) in place of row 1161 (19).
- S40 (17) parallels row 1371 (23): both are exact sum forms of the log trace at the physical time.
- New and checked here: the thermal k-replica identity (3) with the clipped threshold bound (4); (6) with each box conditioned on its full exterior; (5) for matrices with E-measurable frames and dense distant pins; the charging inequality (7); the joined prefix (8); (9)-(10) and S24; (11)-(12) with a dense exterior; (13)-(14) for arbitrary, touching placements; the coverage count S36; the log 8 trace comparison S37.

## Summary table

| S | Lines | Statement | Verdict |
|---|---|---|---|
| 1 | 13 | the test on the cube (OPEN) | HOLDS (accurate) |
| 2 | 21-33 | (1)-(2), retained fraction, r_0 = 1, r_m = (1+s)^{-1} | HOLDS |
| 3 | 35-39 | one-link decrement, r_i <= r_{i-1} | HOLDS |
| 4 | 41-52 | (3), k-replica increments, C_{m,k} = Z_{2kw}/Z_{2w}^k | HOLDS |
| 5 | 54-59 | (4), clipped error eps_k, k_n choice | HOLDS |
| 6 | 61 | projected one-link data, 6 n^{-6} | HOLDS |
| 7 | 67-74 | (5), statement | HOLDS |
| 8 | 76 | neutral domination by 8 e^{C V Delta} | HOLDS (remark: period-2w gluing quoted from row 1151) |
| 9 | 78 | colouring, conditional independence, raw tree | HOLDS |
| 10 | 80-86 | (6) | HOLDS |
| 11 | 88 | shifts and non-neighbouring boxes | HOLDS |
| 12 | 90 | linear curls, C sqrt(d Delta) | HOLDS |
| 13 | 92 | matrix holonomy error C d/b^2 | HOLDS |
| 14 | 94 | plaquette moment and bad box, neutral law | HOLDS |
| 15 | 96, 98 | smoothing, its removal, proof of (5) (two PROVED paragraphs) | HOLDS |
| 16 | 102-106 | (7) | HOLDS |
| 17 | 108-113 | (8) | HOLDS |
| 18 | 119-126 | (9), c >= 1/16, c < v | HOLDS |
| 19 | 128 | two-row ellipticity | HOLDS |
| 20 | 130 | open to periodic, symbol, limit | HOLDS |
| 21 | 132 | nonlinear step for two matrices | HOLDS |
| 22 | 134 | local Gaussian predictor | HOLDS |
| 23 | 136-142 | (10) | HOLDS |
| 24 | 144 | 3/8, 6c^4 >= 3/32768, 3c^2/2 >= 3/512 | HOLDS |
| 25 | 150-159 | (11), statement | HOLDS |
| 26 | 161 | patch curl projection | HOLDS |
| 27 | 163 | words, Taylor, smoothing | HOLDS |
| 28 | 165 | orbit channel | HOLDS |
| 29 | 167-171 | (12) | HOLDS |
| 30 | 177-184 | (13), statement, alpha < 1/60 | HOLDS |
| 31 | 186 | forest words, omitted fraction | HOLDS |
| 32 | 188-194 | (14) | HOLDS |
| 33 | 196 | word eigenvalue bound | HOLDS |
| 34 | 198 | fillings, sum of projections | HOLDS |
| 35 | 200 | orbits, end of (13), forest charge zero | HOLDS |
| 36 | 204 | coverage C n^3 (s+2)^3/b^3 | HOLDS |
| 37 | 206-208 | g_ord - log 8 <= g_+ <= g_ord | HOLDS |
| 38 | 210-216 | (15) | HOLDS, given row 1153 |
| 39 | 218-224 | (16) | HOLDS, given row 1153 (5) |
| 40 | 226-232 | (17) and the implication (OPEN) | HOLDS (accurate); remark: (17) is equivalent to the strict seed |
| 41-50 | 3, 5, 7, 9, 15, 19, 65, 117, 148, 175 | GUIDE | accurate (L3, L9 only spot-checked) |
| 51 | 234 | RESULT | accurate |

## What remains open

A cutoff-uniform upper bound below log(25/21) for the sum (17) at w = floor(n/1024) on one admissible side, equivalently limsup_j s(2 w_j) < 4/21 there. The local estimates (5), (8), (11)-(13) cover sparse or buffered reveals only: S36 shows any order priced by (11) covers at most C n^3 (s+2)^3/b^3 links, (15) is an upper bound that grows like n^3 beta^{-3/16}, and (16) shows the local bounds alone cannot close the sum. Hence the one-box Wilson seed and the mass gap remain open. No step of the note is a counterexample to the checked chain.

RESULT: Row 1373 (`library/gap-seed3-astra62.md`) checked line by line by hand by Claude Opus 5.5 (laptop Claude subagent, FINISH row 1374; cross-provider; grants no status): 51 statements (38 PROVED paragraphs, 2 OPEN, 10 GUIDE, 1 RESULT), 51 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL; no corrections to the mathematics; remarks only: the sufficient estimate (17) is, through the telescoping identity (3), equivalent to the seed with a strict margin (limsup s(2w_j) < 4/21), so it restates the target rather than weakening it; L76 uses the row 1151 gluing comparison at period 2w without re-deriving it (as row 1372 noted for row 1371 L174); L9 writes 2313-2335 where the index gives 2315-2335; holds as stated: the k-replica identity (3) and clipped threshold bound (4), (5)-(6) with full-exterior conditioning, (7), the joined prefix (8), (9)-(10) with c >= 1/16 (guide value 0.108), (11)-(14), the coverage count, (15) from row 1153 and the short-time test (16); the implication (17) plus (4) plus the prefix bound gives s(2w) < 4/21 with the right direction and constants; open: a cutoff-uniform bound on (17) at w = floor(n/1024) on one side, hence the Wilson seed and the mass gap; the note nowhere claims the seed proved or disproved.
