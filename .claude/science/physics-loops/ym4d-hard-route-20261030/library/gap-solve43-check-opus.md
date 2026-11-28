# Check of row 1334 (gap-solve43-astra62.md), FINISH row 1336

Checker: Claude Opus 5.5, by hand, line by line. File checked: `library/gap-solve43-astra62.md` (row 1334, by gpt-6.2-astra). Line numbers refer to that file as committed on `claude/ym4d-hard-route` at the time of this check. Each step was rederived here. Numerics, if any, guide only.

Verdict scale: HOLDS, HOLDS AFTER CORRECTION (correction given), FAILS (failing step or counterexample given).

Inputs read: row 1334 in full (289 lines); Theorem ZD-c and its (PHYS-SEED) threshold in `gap-phys-seed.md` (L55, L311-L320); row 1131 section 3 (`gap-council-prob-astra.md` L56-L118); row 1321 (12) (`gap-solve38-astra62.md` L127-L134); row 1171 (4)-(8) and its nondegeneracy and shared-error steps (`gap-solve14-astra62.md` L60-L112, L465-L480) with their check (`gap-solve14-check-opus.md` S15-S22); the Bessel-ratio ordering after (16) in `gap-solve4-astra62.md` L222; the electric endpoint in `gap-solve2-astra62.md` section 7, L262; the check RESULT lines of rows 1327 and 1333. Inputs taken from those rows and not rederived here: row 1171 (4) (rectangle bound) and (6)-(7) (frame recursion), row 1145 section 7 (electric endpoint), and the monotonicity of I_{2j+1}/I_1.

## Part 1. The overlap bound (9) and what it rests on

### V1. (4), joint estimate for false pairings, L50-L56, with its proof L65-L73. HOLDS.

Fix one false pairing s_p (not alpha_p or alpha_p + 1) on each face of D. The indicator that every W_p(s_p) >= W_p(alpha_p) is at most prod_p (W_p(s_p)/W_p(alpha_p))^u, u = 1/2. Bound the numerator by w(M_p)^u, M_p the first mixed word, since w <= 1. The difference s_p + alpha_p is not constant on the four links, so at some corner v the mixed word arrives at one lift of v and leaves from the other. The four base vertices are distinct, so the word meets that lift once. A Haar gauge at that lift enters M_p exactly once between fixed elements. Faces of D share no base vertex, so these gauges are independent and touch no other mixed word. The true actions are gauge invariant. Exact gauge averaging gives E[...] = J(beta/2)^{|D|} E exp((beta/2) sum over the 2|D| lifted true faces of a). These lifted faces have one orientation, so (5) bounds the last factor by C_0^{2|D|}. On the split cover the two tori are independent. A union over the 7^{|D|} choices gives q = 7 C_0^2 J(beta/2) <= C(1+beta)^{-3/2}. The bound J(b) <= C(1+b)^{-3/2} follows from (2/pi) sin^2 theta d theta, sin^2 theta <= theta^2 and 1 - cos theta >= 2 theta^2/pi^2 on [0, pi]. Relabelling a link shifts both the actual and the alternative assignments, so ambiguity is label free.

### V2. (5), tilting the true plaquettes, L58-L63. HOLDS.

E exp((beta/2) sum_S a) is exactly Z(couplings beta/2 on S)/Z(beta). Take a direction of the orientation of S as time. Each p in S is one electric factor on one link at one step. The normalized kernel e^{-ba}/J(b) has spin-j multiplier I_{2j+1}(b)/I_1(b). I rederived this: the character integral equals I_{2j} - I_{2j+2} = (2(2j+1)/b) I_{2j+1}. Monotonicity of this ratio in b (row 1149, the paragraph after its (16), checked) gives 0 <= normalized C_{beta/2} <= C_beta. Tensor products and the congruences by magnetic half-weights and the gauge projection keep 0 <= F_i <= F. Hoelder for Schatten norms and min-max give |Tr prod_i F_i| <= prod_i (Tr F_i^h)^{1/h} <= Tr F^h. The scalar normalization gives the factor [J(beta/2)/J(beta)]^{|S|}. The ball of radius (1+b)^{-1/2} gives J(b) >= c(1+b)^{-3/2}, so the ratio is at most C_0. Other homogeneous nonnegative couplings change nothing. Citation note: the ordering is in the paragraph after (16) of `gap-solve4-astra62.md`, not in (16) itself.

### V3. (6), the decision from unordered pairs, L77-L81. HOLDS.

The rule d is one fixed function of the unordered pairs. It uses a Borel order, the argmax of W_p (equivalently the argmin of the summed actions, which does not depend on beta), a fixed tie rule, minimum Hamming distance and a majority. Its error bound is proved in V4-V6.

### V4. The true flat class and the representative a, L83. HOLDS.

The cochain a^c_pq = alpha^c_pe + alpha^c_qe records which lift of the shared vertex lies in lift zero of each square. Around a base vertex this returns to its start, since a small loop has trivial monodromy. Around a time circle it changes sheet exactly when c = 1; around a space circle it does not. Reordering the pair on e adds the same bit to both incidences. Flipping the chosen lift of a square adds a dual vertex coboundary. On an unambiguous square the argmax is the actual assignment or its complement, so a choice of flips makes y = a on every bond whose two squares are unambiguous.

### V5. Minimal flat cochain and the disjoint ambiguous squares, L85. HOLDS.

If the decided time holonomy is wrong, z + a is closed with time holonomy 1. Read as primal links, its support has even degree at every primal vertex (the text's "dual vertex" is the vertex dual to a dual plaquette). Its intersection with a time loop is odd, so its homology class has odd x_1-winding. Some simple circuit gamma in its decomposition has odd x_1-winding and length k >= n. Adding the cochain dual to gamma keeps z closed. On gamma, z differs from a, so exactly one of them equals y. Minimality gives at least k/2 bonds of gamma with y different from a. Each meets an ambiguous square; a square has four bonds, so there are at least k/8 such squares. A square shares a vertex with at most 8 others in its plane, so a greedy choice leaves at least k/72 vertex-disjoint ones. Different (t,1)-planes at different (x_2, x_3) share no vertex.

### V6. Counting and majority, (7), L87-L91. HOLDS.

For a fixed circuit gamma the adjacent squares number at most 2k, so at most 4^k subsets. The circuits from a fixed start number at most 4^k, with nT starts. For m specified planes the selected squares on all circuits form one vertex-disjoint set of one orientation, so (4) applies to their union and the sum factorizes into the m-th power of nT sum_{k >= n} (16 q^{1/72})^k. Since q <= C(1+beta)^{-3/2}, 16 q^{1/72} <= (2+beta)^{-b_1} for large beta, with any b_1 < 1/48. Since 2+beta >= 2, nT is absorbed into (2+beta)^{-epsilon n} at large n, uniformly in beta. A wrong majority needs at least n^2/2 wrong planes; 2^{n^2} choices; the total is at most exp(-b n^3 log(2+beta)) on each cover. This proves (6).

### V7. (8), lower bound, L93-L99. HOLDS.

The seam temporal plaquettes are 3n^3 in number and use 7n^3 links. A maximal r/2-net gives cells of diameter at most r, at most C r^{-3} of them, since the disjoint r/4-balls have volume at least c r^3. The two sheets of the split cover are independent copies with the same law, so the cell words agree with probability sum_j p_j^2 >= 1/#words. On agreement every assignment s moves each of the two words of a seam face by at most 4r (bi-invariance), and a is 1-Lipschitz in the round metric, so m_p/W_p >= e^{-8 beta r} >= e^{-8}. Hence no seam face is selected with conditional probability at least e^{-24 n^3}. With alpha^1 chosen to differ from zero only on the seam faces, F avoiding the seam gives G with u = v = 0. G does not depend on the labelling, since a relabelling changes alpha^1 by a term of the form u_e + v_p. The result is P_0(G) >= exp(-B' n^3 log(2+beta)). For the connected cover, P_1(G) = (Z_0/Z_1) P_0(G) and Z_0/Z_1 = z_T^2/z_{2T} >= z_T >= 1.

### V8. (8), upper bound, L101. HOLDS.

P(p not in F | x) = m_p/W_p(alpha_p) <= (W_p(s)/W_p(alpha_p))^u for any fixed false s, since the ratio is at most 1 and the minimum includes s. Conditional independence and the gauge average of V1 give q^{|D|} for vertex-disjoint unselected faces, with no factor 7. On G, a^1_pq = v_p + v_q on every bond between selected squares; this follows from adding the two incidence equations at the shared link. Subtracting the coboundary of an extension of v leaves a closed cochain with time holonomy 1 supported on bonds that meet an unselected square. A circuit of odd x_1-winding has length k >= n, at least k/4 distinct unselected squares and k/36 vertex-disjoint ones. All n^2 planes must carry such a circuit, so the bound is [nT sum (16 q^{1/36})^k]^{n^2} <= exp(-b' n^3 log(2+beta)) under either law. This is row 1131's dual barrier (its (3)) applied jointly in all n^2 parallel planes, with (4) in place of its chessboard bound (4).

### V9. (9), the optimal overlap, L103-L108. HOLDS. (Item 1 of the brief.)

The equal-prior Bayes error is (1/2) int min(d nu_0, d nu_1) = O/2, and O <= nu_0(d=1) + nu_1(d=0) for any rule d. So (6) gives -log O >= b n^3 log(2+beta) - log 2. For the lower bound: for each F in G, the swap at the links with u_e = 1 preserves Haar, every m_p and every unordered pair, and carries the cover-0 summand to the cover-1 summand. So the summed G-terms push forward to one measure M on observations under both unnormalized covers, of mass Z_0 P_0(G). Then M/Z_0 <= nu_0, and M/Z_0 <= M/Z_1 <= nu_1 because Z_1 <= Z_0. So O >= P_0(G) >= exp(-B' n^3 log(2+beta)) by V7. Hence -log O = Theta(n^3 log(2+beta)) for n >= n_0, beta >= beta_0. Any common part of the two unnormalized laws that preserves each unordered raw pair projects below min(Z_0 nu_0, Z_1 nu_1) <= Z_0 min(nu_0, nu_1), so its mass is at most Z_0 O. A matching test needs a common part of mass above (1650/1651) Z_0, so every such test fails on these boxes. Scope: the observation is the raw, gauge-variant pair on each link, as L48 says. Matchings that use gauge-integrated quantities are outside this bound.

## Part 2. The strip, the positive measure and gauge frames

### V10. (10), a strip suffices, L112-L118. HOLDS AFTER CORRECTION.

The conclusion holds. The proof needs two small repairs.
Correction (a): after "wiring" each boundary, the path between the two remaining odd vertices may use the added boundary arcs, which are not bonds of the strip. Then "flipping this path" and the count of lattice paths from one boundary edge do not apply as written. Replace the wiring step by: each component of the support has an even number of odd vertices, all on the two boundaries; the left boundary carries an odd number, so some component holds an odd number of left odd vertices and hence at least one right odd vertex; take a simple path inside the support between such a left and a right vertex. It crosses all w columns, so k >= w, and flipping it keeps every interior flatness constraint, since its interior vertices have degree two.
Correction (b): the sentence "This reads only the links bounding the strip" should read "This reads only the links of the w T squares of the strip". The decision uses every link of those squares, not only the two boundary lines.
With these changes the count C w T 4^k and (10) hold, and the choice w = 3 + ceil(C_p log(2+n)/log(2+beta)) gives O(n^{-p}) for beta >= beta_0.

### V11. Fixed angular resolution, L120-L125. HOLDS.

Moving four links by at most delta moves a plaquette holonomy by at most 4 delta, so a sum of two actions moves by at most 8 delta, and a falsely preferred pairing has A_false <= A_true + 16 delta. On faces with A_true <= epsilon the first mixed word has action at most 2 epsilon; after the gauge average it is Haar, and the cap has Haar mass at most C epsilon^{3/2}. On faces with A_true > epsilon, (5) on the 2|R| lifted faces and exponential Markov give (C_0^2 e^{-beta epsilon/2})^{|R|}. The true actions are gauge invariant, so the two parts combine; summing over R gives q = 7[C epsilon^{3/2} + C_0^2 e^{-beta epsilon/2}] (the factor 7 on the rough part is harmless). Fix delta, then beta_0, so that 16 q^{1/72} <= 1/2. Then (10) gives O(n^{-p}) with w = 3 + ceil(C_p log(2+n)). Two equal cell indices give equal representatives, so the order of the pair does not matter.

### V12. (11), a single positive measure, L127-L131. HOLDS.

Closed Z_2 1-cochains with zero spatial periods form two classes by time period, each of size 2^{V-1} (connected base, constants in the kernel of the coboundary). The cover from b is isomorphic to the split or connected cover, so its Wilson integral is Z_0 or Z_1. The isomorphism for b + delta f swaps the pair at the tail of each link with f_tail = 1, which preserves Haar, the Wilson weight and the unordered pair. So the conditional observation law given c is nu_c, Q(c) is proportional to Z_c, and E_Q Y = (Z_0 - Z_1)/(Z_0 + Z_1). This is the same number as row 1321 (12), (z_T^2 - z_{2T})/(z_T^2 + z_{2T}), now as the mean of a sign in a Wilson cover measure instead of a replica-slice measure. The file says so at L137.

### V13. (12), what the strip measures, L133-L137. HOLDS.

|E_Q D - E_Q Y| <= 2 max_c nu_c(D differs from Y) = O(n^{-p}) by V10-V11, for every value of Q(c). The map r -> (r-1)/(r+1) is increasing and continuous; it sends 1651/1650 to (1/1650)/(3301/1650) = 1/3301. So limsup E D < 1/3301 if and only if limsup Z_0/Z_1 < 1651/1650. The hypothesis needed is beta_j >= beta_0 for large j; the stated beta_j -> infinity is enough.

### V14. Gauge-invariant observables are constant, L141-L143. HOLDS.

G_0(h) composed with the inverse of its conjugate by the block swap sigma_B acts as (h, h^{-1}) on the two sheets at the incidences of B at v, and trivially elsewhere. Products with h = g, k, (gk)^{-1} give (1, g^{-1}k^{-1}gk). Every element of SU(2) is such a commutator: with d diagonal, g a diagonal square root of d^{-1} and k a Weyl element, k^{-1}gk = g^{-1}, so g^{-1}k^{-1}gk = g^{-2} = d; conjugation handles general elements. So each block has independent gauges on both sheets. For a one-link block the gauge at an end is transitive on each sheet, so the quotient is a point. With single-link blocks every invariant is constant. So the decision D must use gauge frames.

## Part 3. The integrated seam, (13)-(16)

### V15. (13), statement and set-up, L147-L158. HOLDS.

J_beta is symmetric: invert the frames and use a(u) = a(u^{-1}) and conjugation invariance. With pre-seam arrays (x_0, x_1) = (x, y) and post-seam arrays (y_0, y_1) = (x, y), the split closing gives J(x,x)J(y,y) and the crossed closing gives J(x,y)J(y,x) = J(x,y)^2. The slice weights are common and cancel. The two-sided bound is proved in V16-V18. (Reading note: the phrase "(x,y), (x,y)" at L152 means pre-seam arrays (x,y) and post-seam arrays (x,y).)

### V16. Fields and loops, L160-L165. HOLDS.

With 1 - cos theta = 3/(4 beta), every plaquette of flux +-theta has beta a = 3/4. I recomputed the fluxes. For x, the 12 flux is theta Delta F(z_1), the 13 flux is theta Delta P(z_1), and the 23 flux is theta Delta P(z_2). For y the same holds with F replaced by P. All have modulus theta. F and P are periodic for even n, and 0 <= F <= 2k. k is the largest even integer at most theta^{-1/2}, so k^2 theta lies in [1/4, 1] for large beta, and k ~ beta^{1/4}.

### V17. Perimeter bound (14), L167-L170. HOLDS.

A rising run of length 2k gives k+1 good starts. There are at least n/(8k) full blocks, so at least 1/8 of all anchors are good. The x-flux of the k-by-k square is theta times k(F(z_1+k) - F(z_1)), which is k^2 theta. The y-flux is 0 because k is even, and this holds in every gauge. Bi-invariance gives sum over the perimeter of l_e >= k^2 theta >= 1/4. Cauchy-Schwarz on 4k edges gives sum of l_e^2 >= 1/(64k). Each edge lies on at most 2k perimeters of this family. So sum_e l_e^2 >= c V_3/k^2, and 1 - cos l >= 2 l^2/pi^2 gives (14).

### V18. Frame integration, L172. HOLDS.

Half the exponent pays (14). In the other half keep a spanning tree and integrate leaves, which gives J(beta/2)^{V_3 - 1}. The small-ball lower bound on the diagonals gives (c beta^{-3/2})^{V_3} e^{-C V_3}. The log ratio is at most -c beta V_3/k^2 + C V_3 + 3 log(1+beta), and beta/k^2 ~ beta theta ~ sqrt(beta). For the converse, d(x_e, y_e) <= 2k theta <= C/k. The small balls give J(x,y) >= (c beta^{-3/2})^{V_3} exp(-C V_3 (1 + beta/k^2)), and the diagonals are at most 1. The leftover term V_3 log beta is below V_3 sqrt(beta). Both sides of (13) hold. The continuity remark is correct. The file correctly marks the probability of such fields as not estimated.

### V19. (15), restriction by rectangle averages, L176-L181. HOLDS (given row 1171 (4)).

Row 1171 (4) gives E|1 - U_R|^2 = 2 E a(U_R) <= C rs/beta for sides below the periods (checked as S15 in `gap-solve14-check-opus.md`). Markov and translation invariance give a failure probability of at most C/K_beta per test. Since a <= 2, the test is automatic once K_beta rs >= 2 beta. That leaves O(log^2(2+beta)) dyadic shapes, with 4 slices and 3 orientations. The deleted mass is O(log^{-2}(2+beta)) on each closing, so each log partition function moves by o(1) as beta tends to infinity.

### V20. (16), statement and construction, L183-L194. HOLDS.

I recomputed the fluxes. The 12 flux of an r-by-s rectangle is theta [F(z_1+r) - F(z_1)][F(z_2+s) - F(z_2)]; the 13 and 23 fluxes are the products with P. Each elementary flux has modulus theta. Pointwise, beta a <= beta phi^2/2 <= (beta theta^2/2) min(r,2k)^2 min(s,2k)^2 <= C k^2 rs, using min(r,2k)^2 <= 2kr. The P-planes give at most 3/4. Choosing c_* small gives at most K_beta rs/2 for every integer r, s, so (15) holds with slack.

### V21. (16), two-sided bound, L196. HOLDS.

At least 1/64 of the anchors rise in both directions. The x-angle is k^2 theta, which tends to 0 (k^2 ~ log^4 beta, theta ~ beta^{-1/2}), and the y-holonomy is 1. Cauchy-Schwarz gives sum over the perimeter of l^2 >= (k^2 theta)^2/(4k), and dividing by the overlap 2k gives sum_e a >= c V_3 k^2 theta^2. Times beta this is c V_3 k^2. Tree integration gives -log ratio >= c V_3 k^2 - C V_3 - 3 log(1+beta). Conversely d(x_e, y_e) <= (2k+1) theta. Small balls for J(x,y) and tree upper bounds for the diagonals give at most C V_3 (1 + k^2) + 3 log(1+beta). Since k^2 ~ K_beta, (16) holds.

## Part 4. The mean estimate (17) (item 2 of the brief)

### V22. (17), statement, L200-L212. HOLDS.

The hypotheses are beta >= 2 and all periods above C_2 sqrt(beta). They are what the proof uses. The frame construction of row 1171 needs all periods above 100 b, with b <= sqrt(beta), so C_2 >= 100 suffices for that part. The first bound uses only the two marginals, so any coupling of X and Y is allowed. The three bounds are proved in V23-V27.

### V23. Fundamental frames, (18), L214-L220. HOLDS (port of row 1171 (6)-(7) and its nondegeneracy step).

Row 1171 builds C^{[l]} from coordinate-ordered path transports with deterministic weights, for any orthogonal transport. The change from Ad to left multiplication L_U on H = R^4 keeps the transports orthogonal. ||L_H - I||_F = ||L_{H-1}||_F = 2|H - 1|. So each rectangle interchange at scale r costs O(r/sqrt(beta)) in L^2 by row 1171 (4), and the coefficient 1/r at unit scale gives ||E_l||_{L^2} <= C log(2l)/sqrt(beta) and the deterministic C/l, as in row 1171 (7). For nondegeneracy, the collapsed row C_* = sum_z w_z T(v,z) on separate blocks has C_* C_*^T = (sum w_z^2) I_4. Here sum w_z = l^2 with support O(l^4), so sum w_z^2 >= c, and sum w_z^2 <= 1. The path-sorting error is C l/sqrt(beta) per path. The squared block errors sum to C l^2/beta. Weyl's inequality and Markov give Pr(s_l < 2 gamma) <= C l^2/beta for 3 gamma < sqrt(c). Row 1171's check (S17-S19) covers these steps in the adjoint case. Nothing in them uses the dimension 3.

### V24. Squared variation, L222-L232. HOLDS.

F_l F_l^T = sin^2 alpha (DD^T)^{-1/2} DD^T (DD^T)^{-1/2} + cos^2 alpha I = I. I checked the identity ||tA - uB||_F^2 = 4(t-u)^2 + tu ||A - B||_F^2 for row isometries with four rows: both sides equal 4t^2 + 4u^2 - 2tu tr(AB^T). The column blocks of F_l are orthogonal, so H_l = ||Delta B_l||^2 + 4(Delta t_l)^2 + t_l(v) t_l(w) H_{l/2}. The maps D -> B_l and D -> t_l are Lipschitz on contractions and commute with left orthogonal transport, as in row 1171 (checked as S20). So the first two terms are at most C(l^{-2} + E_l^2). Unrolled, the term from scale l < b has coefficient prod_{m >= 2l} t_m(v) t_m(w) <= 1{s_{2l}(v) < 2 gamma}. So its l^{-2} part has mean at most C/beta, and its E_l^2 part has mean at most C log^2(2l)/beta. The bottom term H_1 <= 8 has the same indicator. Summing over the dyadic l <= b gives E H_b <= C[b^{-2} + beta^{-1} log^3(2b)]. The squared recursion has coefficient at most 1. So the errors add in square without Minkowski, and this is the source of the saved logarithm against row 1171 (5), log^4.

### V25. Gaussian rounding and the bound on E beta d_*, L234. HOLDS.

F_b(v) xi is standard Gaussian in R^4 since F_b F_b^T = I. Write (A - B) xi = (A - B) A^T (A xi) + (A - B)(I - A^T A) xi, with independent parts. Then E|(A-B) xi|^2/|A xi|^2 <= ||A-B||_F^2 (1 + E|eta|^{-2}), where E|eta|^{-2} = 1/2 in dimension four. With |a/|a| - b/|b|| <= 2|a-b|/|a| this gives E|h_v - U_e h_w|^2 <= C E H_b(e). With g_v = h^X_v (h^Y_v)^{-1} and a(u^{-1} w) = |u - w|^2/2, the edge term equals |(h^X_v)^{-1} X_e h^X_{v'} - (h^Y_v)^{-1} Y_e h^Y_{v'}|^2/2. This is at most (|X_e h^X_{v'} - h^X_v| + |Y_e h^Y_{v'} - h^Y_v|)^2/2. Summing over 3 V_3 edges, with b^{-2} <= 4/beta, gives E beta d_* <= C V_3 log^3(2+beta). d_* is a minimum, so a random choice of g is allowed, and no change of variables is needed. Conditional sampling of the rest of each history gives the frames when only the slice marginals are given.

### V26. Positivity and the upper bound on L_beta, L236. HOLDS.

The kernel e^{-beta a} has positive Fourier coefficients I_{2j+1}(beta). So the product convolution and its gauge average are positive semidefinite continuous kernels, and J(X,Y)^2 <= J(X,X) J(Y,Y), so L >= 0. Take balls of radius beta^{-1/2} about a minimizing frame. The chord grows by at most 2 beta^{-1/2}, so the summed action is at most 2 d_* + C V_3/beta. Tree upper bounds on the diagonals give L <= 2 beta d_* + C V_3 + C log(2+beta). With V25 this proves (17).

### V27. (17a), independent slices, L238-L246. HOLDS.

Greedy selection at sup-distance at least four removes at most 7^3 anchors per step, so M >= V_3/343. No plaquette contains two designated 1-edges. Since r_p^2 = 2 beta a, (5) on a subset of size M/2 and exponential Markov give a bound of at most 2^M (C_0 e^{-K^2/8})^{M/2} (the sharper exponent K^2/4 is available). Given Y and the other X-links, each designated edge has density proportional to exp(t <u,h>) with t <= 6 beta, bounded by 1/J(t) <= C(1+beta)^{3/2} relative to Haar. The Haar chord density is (2/pi) q^2 sqrt(1 - q^2/4), since q = 2 sin(theta/2) and sin^2 theta = q^2 cos^2(theta/2). A window of width 2 delta/sqrt(beta) at q <= (K+1)/sqrt(beta) has Haar mass at most C (K+1)^2 delta beta^{-3/2}. The product is C (K+1)^2 delta, uniformly. The chord |1 - U| is conjugation invariant, and ||1-A| - |1-B|| <= |A - B| <= the sum of four link chords. On at least M/4 edge-disjoint faces this gives beta d_* >= delta^2 M/32 for every g, outside probability e^{-c_2 M} + 2^{-2M}.

## Part 5. Relative entropy, (21) and the interpolation (22)

### V28. (19), first line, L248-L255. HOLDS.

The symmetrized entropy is E_0 log(f_0/f_1) - E_1 log(f_0/f_1), and the normalizers cancel. With the twist on the seam temporal links, exactly the 3 V_3 seam faces, 6 V_3 lifted plaquettes, differ. Evaluated on the other cover's fields, each foreign word arrives at one lift and leaves from the other at its upper corners. An unmatched Haar gauge there makes it Haar, so E a = 1. The true words have E a <= C/beta. So E_0 log(f_0/f_1) = 6 beta V_3 - O(V_3) and E_1 log(f_0/f_1) = -6 beta V_3 + O(V_3), and the sum is 12 beta V_3 + O(V_3).

### V29. (19), second line, and (20), L257-L262. HOLDS.

Integrating the seam temporal links of sheet i gives J_beta(pre-seam array, post-seam array) for the closing in question. Written through L, the eight half-diagonal terms cancel, which leaves exactly (20). Under either closing each of x_0, x_1, y_0, y_1 is a slice of a periodic Wilson torus with periods n and T or 2T. So (17) gives E_c|B| <= C V_3 log^3(2+beta) once n/2 > C_2 sqrt(beta). The symmetrized entropy of the marginals is E_0 B - E_1 B.

### V30. (21), L264-L270. HOLDS AFTER CORRECTION.

Markov and (17) give mu_c^*(L > V_3 log^{7/2}) <= C log^{-1/2}(2+beta). With V19 this gives mu_c^*(A) = 1 - O(log^{-1/2}(2+beta)). The configurations of (16) have 2L = Theta(V_3 log^4) and are excluded at large beta. The identity holds: E_{mu_0^*}[e^{-B} 1_A] = Z_0^{-1} int_A f_1^* = (Z_1/Z_0) mu_1^*(A). The lower bound exp(-C V_3 log^3) follows by Jensen; on A it also holds pointwise with exponent 2 V_3 log^{7/2}.
Correction: the sentence "Its required lower limit at some fixed physical side is strictly greater than 1650/1651" uses mu_0^*(A)/mu_1^*(A) -> 1. That needs beta_j -> infinity, and it needs (17) on the boxes, which needs n_j/2 > C_2 sqrt(beta_j). Neither is stated in this paragraph. Add: "along a trajectory with beta_j -> infinity and C_2 sqrt(beta_j) < n_j/2". Without these, the sufficient condition is the full product: liminf [mu_0^*(A)/mu_1^*(A)] E_{mu_0^*}[e^{-B} | A] > 1650/1651.

### V31. The interpolation, set-up, L274. HOLDS (given row 1145 section 7).

The strip estimate uses only (t,1)-faces at coupling beta. Its inputs (4)-(5) allow any homogeneous nonnegative couplings, and the cover laws stay gauge invariant. So (10) holds uniformly in s in [0, beta] for beta >= beta_0. At s = 0 the transfer is the projected product of electric convolutions. Row 1145 section 7 (`gap-solve2-astra62.md` L262) gives 1 <= Z_T(0) <= [1 + eta(T/b_beta)]^{3N}, which tends to one on the physical boxes. Then 1 <= z_{2T}(0) <= z_T(0) -> 1, so Z_0/Z_1 -> 1 at s = 0. This step is where beta_j <= B_0 log n_j is used: it makes T/b_beta large against log n. The file states that range.

### V32. (22), L276-L282. HOLDS. (Item 3 of the brief, first part.)

d/ds E_{Q_s} Y = -Cov_{Q_s}(Y, S_sp). Here S_sp is the sum, over base spatial plaquettes, of A_p, the sum of the two lifted actions; A_p is a well-defined function of (b, x). Q_s is invariant under all translations of the base n^3 x T torus, and so is Y. So Cov(Y, S_sp) = V sum_ij Cov(Y, A_ij) with V = n^3 T. The location of A_ij is arbitrary. Replacing Y by D: |Cov(D, A) - Cov(Y, A)| <= 2 * 4 * E|D - Y| = O(n^{-7}). Integrated, the error is O(beta V n^{-7}) = O(beta n^{-3}) -> 0. The sign is right: E Y(beta) = E Y(0) - int_0^beta Cov(Y, S_sp) ds. With E_{Q_0} Y -> 0 this is (22). The last remark is also correct: at s = 0 the decision (6) still has error exp(-b n^3 log(2+beta)), since it uses only (t,1)-faces at coupling beta, while Z_0/Z_1 -> 1. Content note: (22) is the fundamental theorem of calculus along row 1145's real interpolation, plus translation invariance and V13. The file marks the interpolation as prior work.

### V33. The covariance formula in the OPEN paragraph, L284-L286. HOLDS. (Item 3, second part.)

Write Y = 1 on c = 0 and Y = -1 on c = 1, with p_0 + p_1 = 1. Then E[YA] = p_0 E_0 A - p_1 E_1 A, E Y = p_0 - p_1 and E A = p_0 E_0 A + p_1 E_1 A. So Cov(Y, A) = p_0 E_0 A (1 - p_0 + p_1) - p_1 E_1 A (1 + p_0 - p_1) = 2 p_0 p_1 (E_0 A - E_1 A). Here E_{c,s} A_ij is twice the one-plaquette mean on the period-T torus (c = 0) or on the period-2T torus (c = 1). The paragraph's claims that (17) and (19) grow with V_3 are correct. Its claim that the local errors cost o(1) after the sum is correct by V32. This paragraph is labelled OPEN and is not counted below.

## Part 6. Sufficiency for Theorem ZD-c, constants and coupling range (item 4 of the brief)

### V34. From (1) to (PHYS-SEED). HOLDS, with no coupling condition.

ZD-c (`gap-phys-seed.md` L311-L320) asks for one l in P with limsup_j S_j(l/(2a_j); (l/a_j)^3) below 1/1650 when the two-stage line is used. Here S = z_T - 1 with T = n/2. The transfer eigenvalue ratios lie in [0, 1], so z_{2T} <= z_T and Z(n,T)^2/Z(n,2T) = z_T^2/z_{2T} >= z_T. So limsup of the ratio below 1651/1650 gives limsup S_j <= limsup ratio - 1 < 1/1650, strictly. The sides n_j = 2^i l_1/a_j are multiples of 4 and at least 12, as the file's set-up needs (n >= 8, divisible by four). This step uses only the Wilson partition functions. It needs no range of beta_j.

### V35. From the open bound below 1/3301 to (1). HOLDS AFTER CORRECTION.

The constant is right: (r-1)/(r+1) < 1/3301 if and only if r < 1651/1650. The map is increasing and continuous, so the limsup passes through it. The routes through the new objects need hypotheses on the trajectory:
- through (12): beta_j >= beta_0 for large j (for (10));
- through (22): beta_0 <= beta_j <= B_0 log n_j for large j (the upper limit for the electric endpoint, V31);
- through (21): beta_j -> infinity and C_2 sqrt(beta_j) < n_j/2 (V30).
Theorem ZD-c sets no condition on (a_j, beta_j). It does not supply these ranges. This is the same kind of gap that checks 1327 and 1333 found in rows 1325 and 1330. The file states the range for (22) at L274 and beta_j -> infinity for (12) at L133. But the OPEN target at L284 says only "along a matched trajectory", and the RESULT line L289 gives no range.
Correction: at L284 and L289 state the range. For example: "at one fixed physical side, along a trajectory with beta_j -> infinity and beta_j <= B_0 log(L/a_j)". With that range, an upper limit below 1/3301 for the right side of (22), or a lower limit above 1650/1651 in (21), gives (1) and hence (PHYS-SEED). A one-loop trajectory, beta_j about (const) log(1/a_j), lies in this range, but that is GUIDE here. Nothing in this lane proves that the trajectory constructing the continuum theory has it.

## Part 7. Everything else

### V36. GUIDE and OPEN text. Consistent.

- L3-L13: search and credit notes. I did not re-read the external sources. The credits (Sussman and Alpoge with their co-authors; the authors reviewed in row 1218; Kandel and Domany, Niedermayer, Redner, Machta and Chayes, Adhikari and Cao; Bachas) are given.
- L17, the OPEN target: it matches ZD-c's set P and its divisibility condition, with T_j = n_j/2.
- L23: z_{2u} <= z_u and Z^2/Z(2u) >= z_u. Correct.
- L25: a common part of mass above (1650/1651) Z_0 gives Z_1 > (1650/1651) Z_0. Correct.
- L27-L44, (2)-(3): labelled GUIDE as row 1131's argument. I rederived it. Conditional on x the face choices are independent with P(p not in F | x) = m_p/W_p. The u-swap carries each G-term of one cover to the same term of the other, so Z_0 P_0(G) = Z_1 P_1(G). It holds.
- L48, L145: scope notes. Correct.
- L289, RESULT: an accurate summary, with two exceptions. It lacks the coupling range (V35). And "integrating the seam gauge variables gives the actual mean estimate (17)" is loose: (17) is a frame estimate on the slices, and the seam integral enters only through L_beta.

### V37. Restatement of earlier rows.

No main positive step only restates an earlier row. The parts that are prior work, or close to it:
- (2)-(3) are row 1131 section 3 (labelled GUIDE).
- (11)-(12) give the number of row 1321 (12) as the mean of a sign in a new Wilson-cover measure. The new content is the decision D and its accuracy. The file says this at L137.
- (5) is row 1149's normalized-convolution moment bound, extended to many layers by trace Hoelder.
- The frame bound in (17) ports row 1171 (5)-(8) to the fundamental representation. It saves one logarithm by the squared recursion (V24).
- The upper bound in (8) is row 1131's dual barrier, applied jointly in all n^2 planes.
- (22) is the fundamental theorem of calculus along row 1145's real interpolation.
The following appear new: the joint false-pairing bound (4) with its explicit beta rate; the decision (6); the lower bound in (8); the overlap (9); the strip (10) and its fixed resolution; the gauge-invariance proposition; (13), (14), (16); the L_beta bounds and (17a); (19)-(21); and the covariance identity.

## Verdict table (PROVED labels only)

| Label line | Statement | Verdict |
|---|---|---|
| L50, L65, L67 | (4), joint false-pairing bound | HOLDS (V1) |
| L58 | (5), tilting bound | HOLDS (V2) |
| L77, L83, L85, L87 | (6)-(7), decision and its error | HOLDS (V3-V6) |
| L93 | (8), lower bound | HOLDS (V7) |
| L101 | (8), upper bound | HOLDS (V8) |
| L103 | (9), optimal overlap | HOLDS (V9) |
| L112 | (10), strip | HOLDS AFTER CORRECTION (V10: path inside the support; "links of the strip's squares") |
| L120 | fixed resolution | HOLDS (V11) |
| L127 | (11) | HOLDS (V12) |
| L133 | (12) | HOLDS (V13) |
| L141, L143 | gauge invariants are constant | HOLDS (V14) |
| L147, L160, L167, L172 | (13)-(14) | HOLDS (V15-V18) |
| L176 | (15) | HOLDS given row 1171 (4) (V19) |
| L183, L196 | (16) | HOLDS (V20-V21) |
| L200, L214, L222, L234, L236 | (17)-(18) | HOLDS (V22-V26) |
| L238, L244, L246 | (17a) | HOLDS (V27) |
| L248, L257 | (19)-(20) | HOLDS (V28-V29) |
| L264 | (21) | HOLDS AFTER CORRECTION (V30: state beta_j -> infinity and C_2 sqrt(beta_j) < n_j/2) |
| L274, L276 | (22) | HOLDS (V31-V32) |

Counts: 37 PROVED labels; 35 HOLD, 2 HOLD AFTER CORRECTION, 0 FAIL. Not counted: the covariance identity in the OPEN paragraph (HOLDS, V33); the sufficiency chain (V34 HOLDS; V35 HOLDS AFTER CORRECTION at L284 and L289); the GUIDE text (consistent, V36). Inputs not rederived here: row 1171 (4) and (6)-(7); row 1145 section 7, the electric endpoint; the monotonicity of I_{2j+1}/I_1 (row 1149). No numeric run was used. This check grants no status. OPEN: the bound below 1/3301 on (22), or above 1650/1651 in (21); the continuum construction; the mass gap.

RESULT: row 1334 HOLDS AFTER CORRECTION, checked line by line by Claude Opus 5.5; 37 PROVED statements: 35 HOLD, 2 HOLD AFTER CORRECTION (L112 strip-path wording, L264 the coupling hypotheses of (21)), 0 FAIL; main finding: the overlap bound -log O = Theta(n^3 log(2+beta)) (n >= n_0, beta >= beta_0) holds and excludes every matching that preserves unordered raw link pairs, (17) holds under beta >= 2 and periods above C_2 sqrt(beta) with one log saved over row 1171, and (22) and Cov(Y,A_ij) = 2 p_0 p_1 (E_0 A - E_1 A) hold; (1) gives Theorem ZD-c's two-stage seed with no coupling condition (constants 1651/1650, 1/1650, 1/3301 correct), but the routes through (12), (21), (22) need beta_0 <= beta_j <= B_0 log n_j (and beta_j -> infinity for (21)), which ZD-c does not supply and L284/L289 do not state, the same kind of gap checks 1327 and 1333 found; no main step only restates an earlier row.
