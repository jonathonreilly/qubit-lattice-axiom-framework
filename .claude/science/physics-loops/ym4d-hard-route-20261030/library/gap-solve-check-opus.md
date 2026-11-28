# Check of library/gap-solve-astra62.md (FINISH row 1144)

Checker: Claude Opus 5.5 (laptop subagent), max effort. File under check: row 1143, by gpt-6.2-astra.

Status: complete (Steps 1-6). Result: all 24 checked statements HOLD; none FAILS (Step 6).

## Plan (six steps)

1. Read the file under check, the council brief, and the cited passages of rows 1028 (Section 4.1) and 667.
2. Check comparison (1): comb tree, telescoping, interior shelling, winding rectangle.
3. Check (2)-(6): four-holonomy asymptotics, (4), bulk subtraction.
4. Check (7)-(11): gap bound via (8), ribbon moments, cube spectrum, joint moment (9), seven-sector bound (10), sharp asymptotics (11), largest-radius law.
5. Check (12), the open-box Gaussian comparison (14)-(15), the gluing, (16), (17), Section 8.
6. Verdict table and RESULT line.

## Step 1. Sources read

- The file under check, `library/gap-solve-astra62.md`, 293 lines, read in full. Line numbers below refer to it.
- `library/gap-council-brief.md` in full, for the setting.
- `library/gap-uv-rigidity-max.md` (row 1028), Section 4.1 (Lemma FV: comb tree, shelling (A2), (A3), (A4), tree gauge (B1), flat points (B2)), lines 539-669.
- `library/gap-transfer.md` (row 667), Sections N, A, 1-9, in full: the trace identities (1b), (1c), positivity (2), trace class (3), the vacuum (4), the limit T to infinity (6a), and the flux sectors (9.3).
- Inputs the file names, read at the cited lines: `library/gap-phys-seed.md` (row 720) L55 (f is the infimum of F/|n| over tori), L416 (E3) and L451 (item 6); `library/gap-crux-restate.md` L31 (tori have all sides at least 3), L33-39; `library/gap-outside-box-check.md` (row 1008) L419-421 (the W2 count).
- Sussman-Alpoge outline `YM4_sketch_500.tex` (local copy of the lead's fetch at `31a47c543775`): L2205-2231 (GL3, c_l = 2 e^(-beta) I_(2l+1)(beta)/beta > 0), L6844-6861 (a_K = L^(-K), x_0 = beta, first passage), L20781-20801 (RF24, RF25), L9568-9577 (flat estimate is not a physical gap). They say what the file says they say.
- Provenance lines spot-checked, all as cited: `gap-brainstorm2-max.md` L470, `gap-measured-vectors-max.md` L131, `gap-fusion-astra.md` 5.3 (a Polyakov trial function, variance half), `gap-zd-astra.md` item 18, `prior/gap-small-volume-lit.md` (exists). Not checked: the other PR 10114 files and the repo-search claims of L3 (GUIDE; no proof step uses them). The PANEL_P3.md credit line is checked in Step 5.

Conventions used in the check. Quaternion norm |q|; a(u) = 1 - (1/2) tr u = |u - 1|^2/2 (checked: |u - 1|^2 = 2 - 2 x_0 for u = (x_0, vector)). For unit quaternions |ab - cd| <= |a - c| + |b - d| and |u^(-1) - 1| = |u - 1|. Haar on SU(2) in exponential coordinates X, |X| < pi: (1/(2 pi^2)) (sin|X|/|X|)^2 d^3X.

## Step 2. Comparison (1), L19-44

**Setting, L19.** Signs sit on the ij plaquettes with x_i = n_i - 1, x_j = n_j - 1: one stack of n_k n_l plaquettes, as in (TM-c) of `gap-crux-restate.md` L35. Since -1 is central, A_epsilon is gauge invariant and the tree gauge of row 1028 (B1) applies with no residual factor.

**Comb tree and counts, L31.** The tree has (n_1 - 1) n_2 n_3 n_4 + (n_2 - 1) n_3 n_4 + (n_3 - 1) n_4 + (n_4 - 1) = V - 1 edges. The parent of x is x - e_k, with k the least index with x_k > 0. So it is a spanning tree. M = 4V - (V - 1) - 4 = 3V - 3. Checked.

**B and its plaquettes, L31.** In an ij plaquette at x, both i-edges have i-coordinate x_i, so both are wrapping or both are interior; the same holds for the j-edges. So B_p = a_i a_j a_i^(-1) a_j^(-1) with a_i in {1, h_i}, a_j in {1, h_j}. It is [h_i, h_j] exactly when x_i = n_i - 1 and x_j = n_j - 1, and 1 otherwise. These doubly wrapping plaquettes are exactly the signed ones; there are n_k n_l <= Q of them in the plane ij. Checked.

**Telescoping, L33.** U_e = Y_e B_e on every edge (Y_e = 1 on the tree and the kept edges). For each factor, |Y_e B_e - B_e| = |Y_e - 1| and |(Y_e B_e)^(-1) - B_e^(-1)| = |Y_e - 1|. So |U_p - B_p| <= sum over the four edges of |Y_e - 1|, and the displayed inequality follows because epsilon_p is a central sign. Checked.

**The 30 and the 5Q, L35.** (t_0 + ... + t_4)^2 <= 5 (t_0^2 + ... + t_4^2) gives a(epsilon_p U_p) <= 5 a(epsilon_p B_p) + 5 sum_(e in p) a(Y_e). With sides at least 3, each edge (x, i) lies in the six distinct plaquettes (x, ij) and (x - e_j, ij), j not i. Summing over p gives 30 sum_e a(Y_e) + 5 sum_(i<j) n_k n_l a(epsilon_ij [h_i, h_j]) <= 30 sum_e a(Y_e) + 5Q sum_(i<j) a(...). Given h, the M variables Y_e are independent Haar (right translates of the non-tree links), and h is Haar. Integration gives the left side of (1). Checked.

**Interior shelling, L37.** For an interior non-tree e = (x, i), k < i is the least index with x_k > 0. The ki plaquette at x - e_k has edges (x - e_k, k), (x, i), (x - e_k + e_i, k), (x - e_k, i). Both k-edges start at sites whose coordinates below k are zero (those of x, as i > k) and have k-coordinate x_k - 1 <= n_k - 2: they are tree edges. The edge (x - e_k, i) is interior, with coordinate sum one lower. This is row 1028 (A2). Checked.

**Wrapping shelling, L37.** For a wrapping e = (x, i), x_i = n_i - 1, not the kept edge, k is the least index other than i with x_k > 0. The two k-edges of the ki plaquette at x - e_k have k-coordinate x_k - 1 <= n_k - 2, so they are interior. The edge (x - e_k, i) wraps in i and has transverse sum one lower; the chain ends at the kept edge, the only wrapping i-edge with transverse sum 0. Checked.

**Distinct, unsigned faces, L37.** An interior face has its base coordinate x_k - 1 <= n_k - 2 in direction k and x_i <= n_i - 2 in direction i: it wraps in no direction. A wrapping face wraps in direction i only. So no selected face is signed. From a face one recovers the plane {k, i}, the pivot direction (the larger index for an interior face, the wrapping direction otherwise) and the pivot (y + e_k, i) from the base y. So the map from pivots to faces is one-to-one. Count: interior non-tree edges 3V + 1 - sum_i V/n_i, wrapping non-kept edges sum_i V/n_i - 4, total M. Checked.

**Triangular change of variables, L37.** In the stated order each selected face contains its pivot once and otherwise only tree edges, kept edges or earlier pivots. Each face product is a left and right translate of the pivot or of its inverse. So the map from the M pivots to the M face products is a Haar-preserving bijection given h. Since a >= 0, A_epsilon >= sum_e a(p_e). Checked.

**Winding rectangle, L39-43.** Along the i-axis from the root, the edges (m e_i, i), 0 <= m <= n_i - 2, are tree edges and the last one is the kept h_i; the same holds on the j-axis. So the boundary of the n_i x n_j rectangle has transport h_i h_j h_i^(-1) h_j^(-1) = [h_i, h_j], in the same orientation as the plaquettes. The boundary-product formula is an identity of words in the free group on the cover's edges (each addition inserts a conjugate of the face word), so it survives the substitution of the torus link values. The rectangle contains exactly one signed plaquette (base (n_i - 1) e_i + (n_j - 1) e_j). Hence epsilon_ij [h_i, h_j] is a product of n_i n_j conjugates of the signed plaquettes, and the triangle inequality with Cauchy-Schwarz gives a(epsilon_ij [h_i, h_j]) <= n_i n_j sum_(p in R_ij) a(epsilon_p U_p). The six rectangles use six disjoint plaquette sets. Averaging the two lower bounds gives A_epsilon >= (1/2) sum_e a(p_e) + (1/(2Q)) sum_(i<j) a(epsilon_ij [h_i, h_j]), and integration gives I(beta/2)^M J_epsilon(beta/(2Q)). Checked.

**Verdict on (1): HOLDS, L27-28,** on every rectangle with sides at least 3, at every beta >= 0, for every sign choice.

## Step 3. The four-holonomy integrals (2), (3); the estimates (4), (5), (6), L46-108

**Commutator and radial law, L52.** For h = (x, u), k = (y, v): hk - kh = (0, 2 u x v), and |[h,k] - 1| = |hk - kh| (right multiplication by kh is an isometry). So a([h,k]) = 2|u x v|^2. With h = (cos t, omega sin t), angle density (2/pi) sin^2 t, the two preimages t, pi - t of r = sin t give w(r) = 4r^2/(pi sqrt(1 - r^2)); its integral over (0, 1) is (4/pi)(pi/4) = 1. Checked.

**Comparison near commuting tuples, L54.** |u_1 x u_j|^2 = r^2 |v_j|^2. For 2 <= j < k: u_j x u_k = alpha_k (u_j x e) + u_j x v_k, with |u_j x e| = |v_j|, |alpha_k| <= r, |u_j| <= r, so |u_j x u_k| <= r(|v_j| + |v_k|). (The file states the bound without this line; it is immediate.) The three such pairs give at most 2r^2 sum over pairs of (|v_j|^2 + |v_k|^2) = 4 r^2 sum_j |v_j|^2. So the full sum lies between r^2 sum |v_j|^2 and 5 r^2 sum |v_j|^2. Checked.

**The angular integral, L56-58.** For y in [0, 1], 1 - y <= 1 - y^2 <= 2(1 - y), and int_0^1 e^(-c(1 - y)) dy = (1 - e^(-c))/c lies between (1 - e^(-1))/(1 + c) and 2/(1 + c). With |v_j|^2 = rho_j^2 (1 - y_j^2), y_j uniform on [-1, 1] and independent of the radius, each factor is comparable to (1 + s r^2 rho_j^2)^(-1); the constants 2 and 10 in the exponent change only absolute constants. This gives the display at L60-61. Checked.

**The inner integral and the logarithm, L64-69.** Lower bound: on [r/2, r], w(v) >= 4v^2/pi >= r^2/pi and 1 + s r^2 v^2 <= 1 + s r^4, so the inner integral is at least r^3/(2 pi (1 + s r^4)). Upper bound: v = rt gives int_0^r w <= (4 r^3/pi) int_0^1 t^2 (1 - t^2)^(-1/2) dt = r^3, and int_0^r w(v)/(s r^2 v^2) dv <= (4/(pi s r)) (pi/2) = 2/(sr). Since min(r^3, 2/(sr)) <= 4 r^3/(1 + s r^4), the inner integral is comparable to r^3/(1 + s r^4), and J_+ is comparable to the 1D integral at L66-67. The substitution x = s r^4 gives r^11 dr = (1/4) s^(-3) x^2 dx, upper limit s/16. For x >= 1, x^2/(1 + x)^3 lies between 1/(8x) and 1/x. For s >= 32, the part r <= 1/2 lies between (1/32) s^(-3) log(s/16) and s^(-3)(1 + log(s/16)), which are comparable to s^(-3) log(2 + s). The part r >= 1/2 is at most 16^3 s^(-3) int_(1/2)^1 (1 - r^2)^(-1/2) dr. Continuity covers [0, 32]. Checked.

**Verdict on (2): HOLDS, L50.**

**The twisted plane, L71-80.** a(-g) = 2 - a(g), so the 12 action is 2(1 - |u_1 x u_2|^2). It vanishes iff |u_1| = |u_2| = 1 and u_1 is orthogonal to u_2; then u_3 and u_4 are parallel to two orthonormal vectors, so u_3 = u_4 = 0. The zero set lies inside the open neighbourhood, so the complement (compact) has action at least c_0 > 0. Expanding 1 - (1 - x_1^2)(1 - x_2^2)(1 - y^2) gives the display at L77; on the neighbourhood x_1^2 x_2^2 <= x_1^2/16 and (1 - x_1^2)(1 - x_2^2) >= (15/16)^2, so it is comparable to x_1^2 + x_2^2 + y^2. For the u_3, u_4 terms: |u_1 x v|^2 + |u_2 x v|^2 = v^T [sum_i |u_i|^2 (I - e_i e_i^T)] v. The matrix e_1 e_1^T + e_2 e_2^T has eigenvalues 1 + y, 1 - y on e_1 +- e_2 and 0 on their normal; so the bracket is at least (15/16)(1 - |y|) I >= (15/32) I and at most 2I. The 34 term is between 0 and 2|u_3|^2 |u_4|^2 <= |u_3|^2/8. The densities of x_1, x_2 (2 sqrt(1 - x^2)/pi), y (1/2) and u_3, u_4 ((pi^2 sqrt(1 - |u|^2))^(-1), both scalar signs) are bounded above and below on the neighbourhood; the direction of u_1 and the azimuth of u_2 have compact range and do not enter the action. Gaussian integration over the nine coordinates gives the upper bound for s >= 1. On the ball of radius 1/(8 sqrt s), which lies in the neighbourhood, the action is O(1/s), so the lower bound is c s^(-9/2). Checked.

**Verdict on (3): HOLDS, L73.**

**GUIDE run (no proof step uses it).** Pure-Python importance sampling (scratch scripts outside the repo; memory 13 MB; seeds fixed). (a) For (2): with u_1 = r e_z the largest vector part, Simpson quadrature in r and Gaussian proposals in the directions transverse to e_z. The scaling limit of Section 6 predicts s^3 J_+(s) = kappa log s + O(1) with kappa = I_b/(2 pi^4), I_b = int over [-1,1]^3 of (1 + |b|^2)^(-2) db = 2.4674, kappa = 1.2665e-2. The run gives s^3 J_+ = 0.1251, 0.1564, 0.1858, 0.2152, 0.2440, 0.3028 at s = 1e2, 1e3, 1e4, 1e5, 1e6, 1e8 (relative standard errors near 2e-3). The slope in log s between 1e4 and 1e8 is 1.2693e-2. The ratio of J_+ to the 1D integral of L66-67 falls slowly from 0.090 to 0.061, towards 4 kappa = 0.051, as expected for a comparison with absolute constants. (b) For (3): Gaussian proposal at the twisted minimum. Prediction from the Hessian (eigenvalues 2, 2, 2 for x_1, x_2, y and 2, 2, 4 for each of u_3, u_4): s^(9/2) J_eps -> 2^(-9/2) pi^(-3/2) = 0.007937. The run gives 0.008039, 0.007947, 0.007938, 0.007937 at s = 1e2, 1e3, 1e4, 1e5. Both runs agree with (2) and (3), including the borderline logarithm.

**Estimate (4), L84-92.** I(t) comparable to (1 + t)^(-3/2): upper bound from sin^2 theta <= theta^2, 1 - cos theta >= 2 theta^2/pi^2 and I <= 1; lower bound from theta <= (1 + t)^(-1/2), where t(1 - cos theta) <= 1/2 and sin theta >= 2 theta/pi. Then I(beta/2)^M <= C^M beta^(-3M/2) and I(30 beta)^M >= c^M beta^(-3M/2) for beta >= 1. For J_+ at beta/(2Q): log(2 + beta/(2Q)) <= log(2 + beta) and (1 + beta/(2Q))^(-3) <= 8 Q^3 beta^(-3). At 5 Q beta: 1 + 5 Q beta <= 6 Q beta and log(2 + 5 Q beta) >= log(2 + beta). The same holds for (3) with the power 9/2. Adding the logs, -(3M/2) log beta - 3 log beta = -(9/2) V log beta + (3/2) log beta, and -(3M/2) log beta - (9/2) log beta = -(9/2) V log beta. All other terms are O(M + log Q) = O(V). Both lines of (4) follow for beta >= 2 with one absolute C. Checked.

**Verdict on (4): HOLDS, L87-90.**

**Bulk subtraction (5), L94-101.** Row 720 (L55, notation of `gap-crux-restate.md` L31) defines f as the infimum of F/|n| over tori with all sides at least 3, so the first line of (4) bounds every quotient in the infimum, and B(beta) > 0 for beta >= 2. Cubes of growing side give f <= -(9/2) log beta + C, consistent with row 1028 (A4), f <= 3.42 - (9/2) log beta. Subtracting n^4 |f + (9/2) log beta| <= C n^4 from the first line of (4) gives the first line of (5). For Phi_rho, rho^4 (B + O(C n^4)) - (B + O(C rho^4 n^4)) = (rho^4 - 1) B + O(2 C rho^4 n^4). At rho = 2: 15 B = (45/2) log beta + 15 log log(2 + beta), and log log(2 + beta) - log log beta -> 0. Row 720 item 6 (L451) asks for (45/2) log beta + O(log log beta); (5) gives this with the log log coefficient. (5) holds for beta >= 2, inherited from (4); L95 does not repeat the range. Checked.

**Verdict on (5): HOLDS, L97-100.**

**One-plane twist (6), L103-106.** The difference of the two lines of (4) is B(beta) + O(V); for beta >= 2, |log log(2 + beta) - log log beta| <= 0.7. Row 1008 L419 states this count as an argued Laplace count; (6) proves it at fixed shape with an O(V) remainder. The two remarks at L106 are correct consequences of (5). Checked.

**Verdict on (6): HOLDS, L104.** The OPEN paragraph at L108 is accurate: the remainder in (5) is 2C n^4, which is extensive at fixed physical size.

## Step 4. The gap bound (7) via (8); (9), (10); (11) and the largest-radius law, L110-201

**Local input, L121-126.** For one plaquette orientation there are V plaquettes with mean 1 - u each (translation invariance), and a >= 0, so V(1 - u) <= <A>. F = log Z_+ is convex with F' = -<A>, so F(beta/2) >= F(beta) + (beta/2) <A>_beta. By (4) at beta and beta/2 (needs beta >= 4) and B(beta/2) <= B(beta): F(beta/2) - F(beta) <= V((9/2) log 2 + 2C). So <A> <= K V/beta with K = 9 log 2 + 4C, an absolute constant, on every rectangular box with sides at least 3. Checked.

**The positive transfer, L128.** B_* is row 667's T (rows 698-699 and `gap-crux-restate.md` (TM), L33, extend it to boxes with sides at least 3). It is positive (row 667 (2c)), trace class (3), and commutes with vertex gauges (4.3). It is injective: C_E acts on the Peter-Weyl blocks by products of c_l = 2 e^(-beta) I_(2l+1)(beta)/beta > 0 (outline GL3, L2205-2231; row 667 (2d) gives the same positivity by hand), and e^(-V_s/2) is bounded with bounded inverse; so <f, B_* f> = <g, C_E g> > 0 for g = e^(-V_s/2) f, f nonzero. So both restrictions are positive, trace class and injective, and their eigenvectors form complete orthonormal bases. Checked.

**The ribbon identity (8), L130-135.** (i) B_* x id preserves the covariant space: (B_* G)(hU) = int b(hU, hV) G(hV) dV = h_x (B_* G)(U) h_y^(-1). (ii) J is isometric since (1/2) tr(U(gamma)^* U(gamma)) = 1, and J^* G = (1/2) tr(U(gamma)^* G) is gauge invariant. (iii) Projected kernel: substituting V -> h^(-1) V and then h -> h^(-1) in int b(U, V) int h_x^(-1) G(hV) h_y dh dV gives int dV [int b(U, hV) sigma(h) dh] G(V). Checked. (iv) Iterating, the k kernels carry the links h_1, ..., h_k of the transfer direction, as in row 667 (1.2)-(1.3); sigma(h_1)...sigma(h_k) G = P_x G P_y^(-1), with P_x, P_y the straight transports from slice 0 to slice k at x and y. J^* then gives (1/2) tr(U^(0)(gamma)^* P_x U^(k)(gamma) P_y^(-1)), the half-trace of the ribbon. The other N - k steps carry scalar averages. Integrating all slices gives Z times the ribbon expectation. (v) At k = N: J P_0 = P_xy J (direct computation), so J^* B_xy^N J P_0 = J^* B_xy^N J on the full space; this is the statement at L135. Checked.

**Two uses, L137.** Tr_0(B_0^(N-k) J^* B_xy^k J) = sum over a, b of lambda_a^(N-k) mu_b^k |<b, Ja>|^2. The weights Z^(-1) lambda_a^N |<b, Ja>|^2 sum to one because sum_b |<b, Ja>|^2 = |Ja|^2 = 1 and sum_a lambda_a^N = Tr B_0^N = Z. So W(k) is the k-th moment of mu_b/lambda_a >= 0, and Jensen for x^k on [0, infinity) gives W(k) >= W(1)^k for 1 <= k <= N. At k = N, J J^* is a projection, so W(N) <= Z^(-1) Tr B_xy^N. The trace of A -> H_x A H_y^(-1) on 2 x 2 matrices is tr H_x tr H_y^(-1), and tr H^(-1) = tr H for SU(2), so the bound is <tr H_x tr H_y> = 4 <P_x P_y>. Checked.

**Passage to the cube spectrum, L139.** Transfer in spatial direction i, period n, on the slice of sides (n, n, T); gamma the time line from (x, 0) to (x, t), t < T, so x and y differ. Then 4 <P_0 P_t> >= W(n) >= W(1)^n, and W(1) is the 1 x t rectangle. Read with time as transfer direction (period T >= t) and gamma' one i-link, this rectangle is W'(t) >= W'(1)^t = u^t, where u is the (0, i) plaquette mean of the box n^3 x T; u >= 1 - K/beta >= 1/2 in the range. Row 667 (6a) applies to the bounded gauge-invariant P_i: the T -> infinity limit is lambda_0^(-t) <P Omega, T^t P Omega>. P_i flips sign under Z_i (its loop has exactly one i-link at x_i = 0) and is invariant under Z_j, j not i; Omega is invariant (row 667 9.3). So P Omega lies in the sector of m_i, is orthogonal to Omega, has norm at most 1, and the matrix element is at most e^(-t m_i). Hence 4 e^(-t m_i) >= (1 - K/beta)^(nt) for every t; the t-th root and t -> infinity give m_i <= -n log(1 - K/beta). -log(1 - x) <= 2x on [0, 1/2]. m_beta <= m_i because the full gap minimizes over all eight sectors. Checked.

**Verdict on (7) with (8): HOLDS, L113-115 and L131-133.** The sentence on sizes, L141, follows: n m <= 2 K n^2/beta, so n m > 30 needs n^2 > 15 beta/K.

**Joint moment (9), L145-156.** At beta = 0 the three loops share only the base vertex, so they are independent Haar, with <P^2> = 1/4 each. For i in S, G = prod over S \ {i} of P_j^2 is a nonnegative gauge-invariant function of the slice x_i = 0 (those loops do not move in direction i). With one adjoint index at the base vertex the same kernel computation as in (8) gives Tr_adj(M_G B_adj^(n_i)) = Z <G chi_1(H_i)>, and Tr(M_G B^n) = Tr(B^(n/2) M_G B^(n/2)) >= 0 since M_G >= 0. With chi_1 = 1 + 2 cos 2 theta and P = cos theta, 4P^2 = 1 + chi_1. So <G P_i^2> >= <G>/4. Induction on |S| gives (9) on every periodic rectangle; the cube vacuum follows from row 667 (6a) for the bounded slice observable. Checked.

**Verdict on (9): HOLDS, L147.**

**Seven sectors (10), L158-172.** F_e = prod over S of P_i transforms by the character e (same parity count as above). With H' the next-time loop transported back along the time bond, |P(1) - P(0)| = |Re(H' - H)| <= |H' - H| and |H' - H|^2 = 2(1 - (1/2) tr(H^* H')). The half-trace equals the winding n x 1 ribbon of (8) (equal traces of mutually inverse SU(2) words), so its mean is at least u^n >= (1 - K/beta)^n. Telescoping with |P_i| <= 1, then (sum of k terms)^2 <= k sum, gives <|F_e(1) - F_e(0)|^2> <= 2k^2 [1 - (1 - K/beta)^n] <= 2 k^2 K n/beta, for every T, hence in the limit. In the limit the left side is 2|F_e Omega|^2 - 2 lambda_0^(-1) <F_e Omega, T F_e Omega> >= 2(1 - r_e)|F_e Omega|^2 (F_e real, F_e Omega in sector e). With |F_e Omega|^2 >= 4^(-k) from (9), 1 - r_e <= 4^k k^2 K n/beta. Checked.

**Verdict on (10): HOLDS, L170.** The consequences at L172 follow (-log(1 - x) <= 2x on [0, 1/2]; the largest prefactor is 4^3 x 9 = 576).

**Rescaling, L184-186.** At p = 1 the selected faces of B(h) are 1 (they wrap at most once), so uniqueness of the triangular reconstruction gives B(h). By induction along the wrapping chain (schematically U_e = (k-edge)^(-1) p_e (previous i-edge) (k-edge), up to orientation, with interior k-edges), h_i -> -h_i at fixed p negates exactly the wrapping i-edges; each plaquette holds zero or two of them, so the action is unchanged and the 16 hemisphere branches are equal. The indicator versions of (1) hold by the same conditional integrations. The region r <= beta^(-1/4) has h-measure O(beta^(-3)), so it gives O_n(beta^(-3M/2 - 3)) = O_n(beta^(-(9V-3)/2)). The region r >= 1/2 gives the same order by the r >= 1/2 part of the 1D integral of Section 2 at s = beta/(2Q). Checked.

**Scaled limit, L188-197.** Jacobians: d^3u_1 = r^2 dr de with dr = r log(beta) dv; d^3u_j = r db_j (beta r^2)^(-1) d^2 w_j. Product beta^(-3) log beta. Exponential coordinates give beta^(-3/2) (sin/.)^2 d^3 xi_e per face. For fixed 0 < v < 1/4, |b_j| < 1, xi, w: r -> 0, beta r^4 -> infinity, so every domain eventually contains the point. sqrt(beta)(W_p(p, h) - W_p(1, h)) -> D_p W_p(1, 1)[xi] by the fundamental theorem along p(t) and continuity of the derivative (h -> 1 on the positive hemispheres). On an ij double seam, sqrt(beta)(h_i h_j - h_j h_i) = 2 e x (b_i w_j - b_j w_i) + 2 w_i x w_j/(sqrt(beta) r^2), and the last term tends to 0. Majorant: beta A >= (beta/2) sum a(p_e) + (beta/(2Q)) sum_j a([h_1, h_j]) >= (1/pi^2) sum |xi_e|^2 + (1/Q) sum |w_j|^2, using beta a(p_e) >= 2|xi_e|^2/pi^2 and beta a([h_1, h_j]) = 2 beta |u_1 x u_j|^2 = 2|w_j|^2. The Haar factors are bounded for r <= 1/2. The v, b, e domains have finite measure. Dominated convergence gives a finite limit, positive since the limit integrand is positive. Checked.

**Verdict on (11), first assertion: HOLDS, L178.**

**Largest-radius law, L199.** The majorant survives multiplication by a bounded continuous phi(v); the limit integrand does not depend on v on (0, 1/4); the two cut regions have normalized mass O(1/log beta). So v = -log r/log beta tends in law to the uniform law on [0, 1/4]. P(r > r_0) <= P(v < delta) for large beta, whose limit is 4 delta. The 16 sign images are equally likely by the sign symmetry above. Checked.

**Verdict on the largest-radius law: HOLDS, L199.**

**Twisted integral, L201.** Outside the neighbourhood of (3), the indicator version of the upper bound of (1) gives I(beta/2)^M e^(-beta c_0/(2Q)). Inside it, the coordinates (x_1, x_2, y, u_3, u_4) plus the compact pair (direction of u_1, azimuth of u_2) are smooth because u_1 and u_2 are near orthogonal; h_3, h_4 have two scalar signs each. At the origin, h_1, h_2 are anticommuting unit imaginary quaternions, [h_1, h_2] = (h_1 h_2)^2 = -1, so all signed plaquettes are 1 for every value of the compact pair. Each signed plaquette is a smooth function of the scaled variables, so sqrt(beta)(epsilon_p U_p - 1) converges to its differential. Majorant: (1/2) sum a(p_e) plus (1/(2Q)) times the quadratic lower bound from the proof of (3), a Gaussian in the 3M + 9 scaled coordinates. Jacobian beta^(-3M/2) beta^(-9/2) = beta^(-9V/2). Dominated convergence gives d_n in (0, infinity). Checked.

**Verdict on (11), second assertion: HOLDS, L178-180.**

## Step 5. (12), (13), the open box (14)-(15), the gluing, (16), (17), Section 8, L203-293

**Secant lemma and (12), L203-210.** F is convex (F'' = Var A >= 0; the same for log Z_eps with A_eps). Convexity gives (F(beta) - F(beta/b))/(beta(1 - 1/b)) <= F'(beta) <= (F(b beta) - F(beta))/(beta(b - 1)). From Z ~ c beta^(-p) (log beta)^q, F(b beta) - F(beta) -> -p log b, since log(log(b beta)/log beta) -> 0. So beta F' has liminf at least -p b log b/(b - 1) and limsup at most -p log b/(b - 1); both tend to -p as b -> 1. With p = (9V - 3)/2 for the two periodic tori: -rho^4 (9n^4 - 3)/2 + (9 rho^4 n^4 - 3)/2 = (3/2)(rho^4 - 1). With p = 9V/2 for the twist: 9V/2 - (9V - 3)/2 = 3/2. F' = -6 n^4 abar_n gives d Phi_rho/d beta = 6 rho^4 n^4 (abar_(rho n) - abar_n). Checked.

**Verdict on (12): HOLDS, L204-208.**

**Open box and (14), L222-229.** The open box has 4(b - 1) b^3 internal links and a comb tree of b^4 - 1 links, so m_b = 3b^4 - 4b^3 + 1, the count of row 1028 (A2). For a non-tree e = (x, i), the selected plaquette has both k-edges on the tree, so U_p = U_e U_(e')^(-1) up to orientation, with e' = (x - e_k, i): |U_e - U_(e')| = |U_p - 1|, and linearly X_e - X_(e') = +-(dX)_p. The chain of predecessors stops at the tree or at a link of S after at most 4(b - 1) steps (the coordinate sum drops by one), and uses distinct plaquettes. Cauchy-Schwarz gives |U_e - 1|^2 <= 4b sum |U_p - 1|^2 = 8b A_box, and |X_e|^2 <= 4b |dX|^2. Summing over at most 3b^4 free links gives |X|^2 <= 12 b^5 |dX|^2, that is K_S >= b^(-5)/12. |(dX)_p|^2 <= 4 sum_(e in p) |X_e|^2 and each link lies in at most six internal plaquettes, so K_S <= 24. Checked.

**Verdict on (14): HOLDS, L226-227.**

**Gaussian estimate (15), L231-238.** Exterior: some |X_e| > eta gives |U_e - 1| = 2 sin(|X_e|/2) >= 2 eta/pi, so A_box >= eta^2/(2 pi^2 b) by (14), and the exterior integral is at most e^(-c s eta^2/b) with s eta^2/b >= c_1 beta^(1/2)/b. Since det K_S <= 24^m, log G >= -C b^4 log beta, and beta^(1/2)/b >> b^4 log beta for b = ceil((log beta)^2). Interior: e^(+-X) = 1 +- X + rho, |rho| <= |X|^2 for |X| <= 1; every product of two or more increments has an extra factor C eta. So |R_p| <= C eta sum_(e in p) |X_e|, |R| <= C eta b^(5/2) |dX| by (14), and A_box lies within (1 +- delta)|dX|^2/2 with delta = C' eta b^(5/2) = C' beta^(-1/4) (log beta)^5 -> 0. The Haar ratio (sin|X|/|X|)^2 lies in [e^(-C eta^2), 1]. Under either Gaussian each coordinate has variance at most C b^5/s, so the union bound with Markov gives C m b^5/(s eta^2) <= C b^9 beta^(-1/2) -> 0. The log errors are O(m delta) + O(m eta^2) + o(1) = o(b^4), uniformly in S and in s in [c_1 beta, c_2 beta]. Checked.

**Verdict on (15): HOLDS, L233-234.**

**Gluing, L240-256.** Upper bound: for a box with sides n_mu and the other sides fixed, Z = Tr T^(n_mu) and (Tr T^N)^(1/N) is the l^N norm of the eigenvalues, nonincreasing in N; so F/|n| is nonincreasing in each side (`gap-crux-restate.md` L39 states the same input), and the cubes of side kb tend to the infimum f_s. Dropping the crossing plaquettes (weights at most 1) factorizes the integral into k^4 open boxes; the crossing links then integrate to 1; the open-box integral equals Z^open_(b, empty) by its tree gauge. Lower bound: after the tree gauge in every box, all other links (crossing links included) are Haar given the trees. Per box at most 8 x 3b^3 face-tangent links and 4b^3 outgoing crossing links are restricted to |U_e - 1| <= 1/s, each with Haar mass at least s^(-3)/12 (row 1028 (B4)). In U^0 every crossing plaquette is 1 (one-boundary plaquettes: two joining links and two face-tangent links, tree or restricted; two-boundary plaquettes: four joining links). Telescoping, (v + w)^2 <= (1 + eps) v^2 + (1 + 1/eps) w^2, (sum of four)^2 <= 4 sum of squares, and at most six plaquettes per link give A(U) <= (1 + eps) sum A_box(U^0) + C(1 + 1/eps) k^4 b^3 s^(-2). Integrating: f_s >= b^(-4) log Z^open_(b,S)(s(1 + eps)) - C(1 + log s)/b; the term s (1 + 1/eps) b^3 s^(-2)/b^4 is at most C/b. Schur complement: its form is the minimum of the full form over the other variables, so its eigenvalues lie in [b^(-5)/12, 24]; block elimination gives |log det K_empty - log det K_S| <= C|S|(1 + log b). The normalization changes by O(|S|(1 + log s)) and the shift s -> s(1 + eps) by O(b^4 eps). Divided by b^4 all these are o(1), since b >> log beta and |S| = O(b^3). Checked.

**Verdict on the gluing (L240-256): HOLDS.**

**Cancellation and (13), L258-263.** With the same b at s = beta and s = t beta, b^(-4)(log G(t beta) - log G(beta)) = -(3 m_b/(2 b^4)) log t -> -(9/2) log t. f is convex as a pointwise limit of the convex F/|n| along cubes. The secant lemma with p = 9/2 gives beta f'_(+-) -> -9/2. With beta F'(n^4) -> -(9n^4 - 3)/2 from (11) and the secant lemma: beta d_(+-) D -> -(9n^4 - 3)/2 + 9n^4/2 = 3/2. D = F - n^4 f is locally absolutely continuous (convex functions are locally Lipschitz), and both one-sided derivatives are positive beyond a threshold depending on n, so D is strictly increasing there. Checked.

**Verdict on (13): HOLDS, L216.** The threshold depends on n, as L218 and L283 say.

**Quantitative remainder (16), L265-273.** With b = ceil(beta^gamma), gamma < 1/12, eta = b^(-7/2): the exterior exponent is c s eta^2/b = c s b^(-8) >= c beta b^(-8)/2, and beta/b^8 >> b^4 log beta because beta^(1 - 12 gamma) >> log beta. delta = C eta b^(5/2) = C/b. Each coordinate has variance at most C b^5/s, so a one-dimensional Gaussian tail with a union bound over at most 9b^4 coordinates gives C b^4 exp(-c beta/b^12): faster than every power of beta. Per site: precision error O(1/b), Haar error O(b^(-7)), boundary and Schur costs O((1 + log beta)/b), shift O(beta^(-1/4)) <= O(log beta/b). So |f_s - b^(-4) log G_(b,empty)(s)| <= C log beta/b on [beta, 2 beta]. For g = f + (9/2) log s: g(t beta) - g(beta) = (3/2)(3 - m_b/b^4) log t + O(log beta/b), and 3 - m_b/b^4 = (4b^3 - 1)/b^4. Dyadic telescoping with b_k = ceil((2^k beta)^gamma) sums to C_alpha beta^(-alpha) since gamma > alpha. So g -> c_inf with rate beta^(-alpha). The secants over [beta(1 - h), beta] and [beta, beta(1 + h)] give beta f'_(+-) = -9/2 + O(h) + O(beta^(-alpha)/h), and h = beta^(-alpha/2) gives (16). Checked.

**Verdict on (16): HOLDS, L267-269.**

**Constant (17), L275-281.** log Z_+(n^4) = log c_n - ((9n^4 - 3)/2) log beta + log log beta + o(1) by (11), and n^4 f = -(9/2) n^4 log beta + n^4 c_inf + o(1) by (16). Subtracting gives (17). The remark on growing n is correct: (16) controls only the bulk term. Checked.

**Verdict on (17): HOLDS, L277-279.**

**Section 8, L287-291.** Outline L6845 gives a_K = L^(-K) (L is the blocking factor, renamed b_RG in the file), and L6855 gives x_0 = beta. RF25 (outline L20787-20797, "proved conditionally" on the account's construction inputs) gives (beta - h)/B_sharp - 1 <= K, that is beta_j <= h + B_sharp + B_sharp K_j. Hence n_j = L b_RG^(K_j) grows exponentially in K_j while beta_j grows at most linearly; since K_j -> infinity, n_j exceeds every fixed power of beta_j. On the symmetric torus Q = n^2, so the arguments of J are beta_j/(2 n_j^2) -> 0 and 5 n_j^2 beta_j -> infinity. (7) gives n m <= 2K n_j^2/beta_j, which tends to infinity, so no lower bound and no obstruction. Group remarks: for U(1) every commutator is 1, so J = 1; for a finite subgroup with normalized counting measure J(s) -> c_4(G)/|G|^4 (as in row 1028 Proposition FRZ (i)); a decoupled spectator tensors the transfer operators. Checked, given the account's input as the label says.

**Verdict on Section 8: HOLDS (given the account's RF25 and first-passage definitions), L287-289.** The OPEN paragraph L291 and the RESULT line L293 claim no more than is proved.

**Credit line checked.** PR 10114 at `f76f6c649c`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/PANEL_P3.md` L64 cites Chatterjee, "The leading term of the Yang-Mills free energy" (2016), for U(N), as L220 says. The file proves its SU(2) pressure comparison itself and uses the citation only for credit.

## Step 6. Verdict table and result

Checked line by line, by hand, by Claude Opus 5.5 (one check of row 1143, cross-provider). The guide runs of Step 3 prove nothing.

| # | Statement (line in `gap-solve-astra62.md`) | Verdict |
|---|---|---|
| 1 | (1), lower side: comb tree, B(h), telescoping, Cauchy-Schwarz on five terms, factors 30 and 5Q (L27-35) | HOLDS |
| 2 | (1), upper side: interior and wrapping shelling, distinct unsigned faces, triangular Haar map, winding rectangle (L37-44) | HOLDS |
| 3 | (2), J_+(s) comparable to log(2 + s)/(1 + s)^3 (L50-69) | HOLDS |
| 4 | (3), one twisted plane, J_eps(s) comparable to (1 + s)^(-9/2) (L73-80) | HOLDS |
| 5 | (4), uniform errors for log Z_+ and log Z_eps, beta >= 2 (L84-92) | HOLDS |
| 6 | (5), bulk subtraction; doubling defect (45/2) log beta + 15 log log beta + O_n(1) (L94-102) | HOLDS |
| 7 | (6), one-plane twist (3/2) log beta + log log beta + O(V) (L103-106) | HOLDS |
| 8 | Local input u >= 1 - K/beta, K absolute (L121-126) | HOLDS |
| 9 | (8), ribbon as a moment; Jensen; the bound 4<P_x P_y> at k = N (L128-137) | HOLDS |
| 10 | (7) via the passage to the cube spectrum (L113-117, L139) | HOLDS |
| 11 | Sizes ruled out: n^2 > 15 beta/K needed for n m > 30 (L141) | HOLDS |
| 12 | (9), joint winding moment (L145-156) | HOLDS |
| 13 | (10), seven-sector bound and its consequences (L158-172) | HOLDS |
| 14 | (11), periodic asymptotic c_n beta^(-(9V-3)/2) log beta (L176-197) | HOLDS |
| 15 | Law of the largest radius, uniform on [0, 1/4] (L199) | HOLDS |
| 16 | (11), twisted asymptotic d_n beta^(-9V/2) (L201) | HOLDS |
| 17 | Secant lemma and (12); abar_n < abar_(rho n) eventually (L203-210) | HOLDS |
| 18 | (13), beta d_(+-) D -> 3/2 at fixed n (L214-218, L258-263) | HOLDS |
| 19 | (14), K_S between b^(-5)/12 and 24; max |U_e - 1|^2 <= 8b A_box (L222-229) | HOLDS |
| 20 | (15), open-box Gaussian estimate (L231-238) | HOLDS |
| 21 | Gluing: f_s = b^(-4) log G_(b,empty)(s) + o(1) (L240-256) | HOLDS |
| 22 | (16), f_beta = -(9/2) log beta + c_inf + O(beta^(-alpha)), alpha < 1/12 (L265-273) | HOLDS |
| 23 | (17), the constant log c_(n,n,n,n) - n^4 c_inf (L275-281) | HOLDS |
| 24 | Section 8, given the account's RF25 and first-passage data; group remarks (L287-291) | HOLDS |

No statement FAILS. No correction is needed for any statement. Notes on wording (none changes a statement):

- L37, "its unique upper transverse edge": the recovered pivot is the edge in the wrapping direction with the larger coordinate in the face's other direction.
- L54: the bound |u_j x u_k| <= r(|v_j| + |v_k|) has a one-line proof (u_j x u_k = alpha_k (u_j x e) + u_j x v_k) that the file omits. In the next sentence the letter v also denotes a radius.
- L95-101: (5) holds for beta >= 2, inherited from (4); the range is not restated.
- L128: "spatial Wilson action" means the action of the plaquettes inside the transverse slice; for a spatial transfer direction it includes time-like plaquettes.
- L139 and L163: "(8) bounds ... below" means (8) together with the Jensen step at L137.

Not checked: the GUIDE paragraphs L3, L5, L9, L11, L119, beyond the spot checks of Step 1 and the credit line of Step 5.

RESULT — check of row 1143 (`library/gap-solve-astra62.md`), checked line by line by hand by Claude Opus 5.5: all 24 statements HOLD and none FAILS; (1), (2), (3), (4)-(6), (7) with (8), (9), (10), (11) with the largest-radius law, (12), (13), (14)-(15) with the gluing, (16), (17) and Section 8 are correct as written; guide runs agree with (2) (slope of s^3 J_+ in log s 1.2693e-2 against the predicted 1.2665e-2) and with (3) (s^(9/2) J_eps -> 0.007937, as predicted); these are fixed-lattice results; Wall (W) at fixed physical size and the mass gap stay OPEN.
