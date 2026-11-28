# Check of gap-solve17-astra62.md (FINISH row 1182)

Checker: laptop Claude subagent, Claude Opus 5.5, max effort. Cross-provider check of row 1177.
Row text: read from FINISH.md (row 1182). The scratch copy of the row held only its title line.

## Plan (at most eight steps)

1. Read the brief, the file under check (all 426 lines, in ranges), and the cited parts of rows 1161-1175 and their checks.
2. Check (7): the claimed equivalence with the planar tension test.
3. Check (8): the competing-branch twist law, and its width window.
4. Check (26): the tension lower bound.
5. Check (32) and (35).
6. Check every other statement in the file.
7. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with lines) and the RESULT line.

## Progress log

### Step 1 (reading) - done

- Read the brief and all 426 lines of the file under check (ranges 1-80, 80-149, 149-218, 218-287, 287-356, 356-426).
- The file's own RESULT (line 426) names five positive claims: (7) at line 93-98; (8) at 102-108 with the width window (13) at 151-156; (26) at 311-316 with proof 318-348; (32)-(33) at 371-401; (35) at 414-420.
- Cited parts of earlier rows are read as each step needs them. Each statement below gets an S-number and a line.

### Step 2: the branch test (7) and its inputs (lines 13-98) - done

Sources read for this step: row 1175 (`gap-solve16-astra62.md`, all 340 lines), row 1161's two alternatives and (19) (`gap-solve9-astra62.md` lines 85-105, 146-148, 215, 264-310), Lemmas K, X, E, E' and Theorem S (`gap-crux-restate.md` 3.4), and the 1/1650 seed form of (W) (`gap-phys-seed.md` line 55, `gap-zd-astra.md` lines 201-210).

- S1 (lines 13-18, trace representations, top of V, Z/8 <= V <= 8Z). HOLDS. Q = (Z - Z_12)/2 is the trace of the odd projection of the direction-2 flip in the 1-frame, and of the direction-1 flip in the 2-frame. V contains Z with weight 1/8, and each of its 64 terms is at most Z. So Z/8 <= V <= 8Z, and long-time roots give the same top eigenvalue.
- S2 (lines 20-32, the limits, (1), the stack bound). HOLDS. For fixed b, (1/a) log A(a,b) is the log of an l^a norm of a nonnegative spectrum, so it is nonincreasing in a. The same holds in b by the other frame. So the scaled log is separately nonincreasing, and the double limit is the infimum. Convexity of e_A in b and its affine minorant give f_A = inf_b e_A(b)/b > -infinity. Then log[(1-z)/2]/(ab) = log(Q/Z)/(ab) tends to f_Q - f_Z = f_Q - f_V, which is (1). The stack bound is row 1175 (14) on an a x b normal plane with ab representatives; with (1-z)/2 <= (1-z)/(1+z) it gives sigma >= -log tanh(beta w^2).
- S3 (lines 34-39, (2)). HOLDS. A(t,jb) <= A(t,b)^j gives e_A(jb) <= j e_A(b), so the proof of Lemma K(d) applies to Q as written; the text's phrase "contrary to kappa_A(b)/b -> 0" is the shorthand of that proof (a positive increment forces e_A(b)/b >= f_A + c/2 for large b, contradicted along multiples of a good b_1). Lemma X in the two frames, with A(t,b) = A(b,t) by the 1-2 exchange (it maps the 12-twist to itself), gives g_A(t;b) - g_A(b;t) = b kappa_A(t) - t kappa_A(b) >= (b-t) kappa_A(b).
- S5 (lines 62-67, the tile estimate (4) and the first line of (3)). HOLDS. Theorem S from S_U(n_0/2; n_0^3) <= q/5041 gives S_U(h/2; h^3) <= q^(h/n_0)/5041 at dyadic h. Lemma E' (a = h/2, b = h) costs 2d_i/h <= 2D/h per spectator, and (2D/h)^2 q^(h/n_0) <= e^(-c h/n_0) once h/n_0 >= K log(2 + D/n_0) with K > 2/(-log q). In the active plane, P(h,h)/lambda^h <= S_U(h/2;h)^2 (sum of squares of nonnegative excited terms), and h kappa_U(h) <= 2 g_U(h/2;h) by (2). With P(r,s) <= P(h,h)^(rs/h^2) and U(r,s) >= e^(rs f_U) this gives P/U <= [S^2 (1+S)^2]^(rs/h^2), which is (4). For the periodic seed with spectators (w,w), h <= 2K n_0 log(2+x) and (1) give sigma >= c/(n_0^2 log(2+x)). Z_B/Z <= 64 P/U follows from Z_B <= 8P and Z >= V/8.
- S6 (lines 69-73, (5)). HOLDS. With b ~ n_0 x^2 all sides of the calibration rectangles lie in [w, 2b] for x >= 2. For any nonzero B take a nonzero entry as spectators; the active pair has product of sides at least w^2 in every case (12, 34 or mixed entry), and h n_0 <= C n_0^2 log(2+x), so (4) gives Z_B/Z <= 64 exp(-c x^2/log(2+x)). Then Q = (Z/2)(1-z) and V = (Z/8)(1 + O(63 eta)) give Q/V = 4(1 + O(eta)).
- S7 (lines 75-78, g_V(r;s) bound and (6)). HOLDS. The Lemma E' factor is (2s/d)(2w/d)^2 <= 64 s/w = O(x) for s <= 2b, d in (w/2, w]; d/n_0 >= x/2 absorbs it. The l^p step needs S_V(d/2) <= 1, which holds. The resulting error e^(-c' r/n_0) with r >= t ~ n_0 x^2/2 is below eta.
- S8 (lines 80-91, second line of (3)). HOLDS. The pairs (t,b) -> (b,b) and (b,t) -> (2b,t) are both calibration rectangles. Q(2r,s) <= e^(r e_Q(s)) Q(r,s) and e_Q <= e_Z = e_V give 0 <= r(e_V(s) - e_Q(s)) <= C eta. Hence g_Q = log 4 + O(eta) at (t,b) and at (b,t). In (2) the two log 4 terms cancel, so kappa_Q(b) <= 2C eta/b. The identity f_V - f_Q = b^(-1)[e_V(b) - e_Q(b) + kappa_Q(b) - kappa_V(b)] follows from kappa_A = e_A - b f_A; with -kappa_V <= 0 and e_V(b) - e_Q(b) <= 2C eta/b it gives sigma <= C eta/b^2 = C eta/(n_0^2 x^4). Checked by hand.
- S4 (lines 45-60, statement (3)). HOLDS, by S5-S8.
- S9 (lines 93-98, the branch test (7)). HOLDS. Ordinary branch: -log sigma = O(log log w) at fixed n_0, so (7) holds along all large w. Competing branch: (log(2+w)/w^2)(-log sigma) >= (log(2+w)/w^2) c x^2/log(2+x) >= c/n_0^2 > 0 for all large w, so (7) fails along every unbounded sequence. The two seeds cannot hold at one cutoff, since the two lines of (3) contradict each other for large x. Row 1161 (lines 215 and 148 there) gives, under the neutral premise at each fine cutoff, a Z-seed or a V-seed at n_0 = n_j with one margin (5041 x 2^(-18) < 1); excluding the V-seed at each fine cutoff leaves the uniform Z-seed, hence (W) by propagation. Conversely (W) is the strict seed below 1/1650 (Theorem SH at shape two, `gap-phys-seed.md` line 55), which propagates to a seed below q/5041 at an enlarged physical side; the first line of (3) at that n_0 then gives (7). The remark that the universal bound gives only -log sigma ~ 2 beta w^2 holds.

### Step 3: the twist law (8) and the width window (13) (lines 100-160) - done

Extra source read: row 1157 (1) (`gap-solve8-astra62.md` lines 23-45).

- S11 (lines 110-114, (9)). HOLDS. With 32 <= w/d < 64 the three Lemma E' factors are 32, < 128, < 128 (absolute). Lemma E at a = u_i, b = s_i = 32 u_i has exponent 64/31 <= 4. Then S_(i+1) <= [(1+S_i)^4 - 1]^2 <= 225 S_i^2 for S_i <= 1, since (1+S)^4 - 1 <= 15 S there. Induction gives 225 S_i <= (225 S_0)^(2^i). For s in [s_i, 2s_i) the final Lemma E' factor is s/(s_i - u_i) < 64/31 < 3. The time condition r >= s/16 >= 2u_i allows the l^p step. Since s_0 = 16d <= w/2 <= s, the case analysis is complete.
- S12 (lines 116-125, (10), the bound on Z_B/V, (11)). HOLDS. (10) is the identity log V = a e_V(b) + g_V(a;b) with e_V(b) = b f_V + kappa_V(b), plus (9) at r = a and kappa_V(b) <= g_V(floor(b/2); b)/(b - floor(b/2)) from (2). Every B outside {0, e_12} has an entry other than 12; that entry is static in the 1-frame (entries 23, 24, 34) or in the 2-frame (13, 14, 34). In that frame each electric character trace is at most the neutral one (all twist integrals are positive), so Z_B <= 8 x (neutral trace at that nonzero m) <= 8 lambda^l S_V, and (9) applies in both frames under b >= w, a/b in [1/2,2]. The 62 remaining terms give (11).
- S13 (lines 127-134, (12)). HOLDS. The two seam terms with no seam in directions 3,4 are (Z - Z_12)/8 = Q/4; the other six have a temporal seam in direction 3 or 4, which is static in the 2-frame, so the bound before (11) applies. Row 1157 (1) with s = 1 and the nontrivial character (odd on direction 2) gives 1 - lambda_(h,2)/lambda >= (1-rho)/4, with rho <= e^(-c/n_0) from (9) by long-time roots. The half-time character trace is at most the neutral periodic trace, hence at most 1 + S_V <= 2. The tail after the top is at most 2 e^(-c' ceil(a/2)/n_0), and a >= b/2. Summing four characters gives (12).
- S14 (lines 136-145, the range b sigma <= epsilon/n_0). HOLDS. The extension of (9)-(12) to aspect [1/3,3] is valid: every time used is at least one sixteenth of its spatial side and every spatial side is at least w/2. Q(r,s) >= e^(rs f_Q) and r kappa_V(s) <= C e^(-cb/n_0) give the lower bound exp(-rs sigma - C e^(-cb/n_0)); with rs <= b^2/2 and epsilon below the decay constant the relative error of (12) is e^(-c'b/n_0). Then g_Q = log 4 + O(e^(-c'b/n_0)) in both frames, (2) gives kappa_Q(b) <= C e^(-c'b/n_0)/b, and E_b = b sigma + kappa_V(b) - kappa_Q(b) gives the stated bound. Then Q/H = (1-z)/(1+z) = e^(-a E_b) + O(e^(-cb/n_0)) by (9), (11), (12), and |a E_b - ab sigma| <= 2C e^(-c'b/n_0).
- S15 (line 147, the remaining range and the tanh form). HOLDS. b_* = floor(epsilon/(2 n_0 sigma)) is finite by sigma > 0 and at least 4w by the second line of (3), uniformly in n_0. At b_*, b_* sigma lies in [epsilon/(4n_0), epsilon/(2n_0)] for large x, so the first range applies and kappa_Q(b_*) <= C e^(-c' b_*/n_0)/b_* <= b_* sigma/2. Since b > b_* and kappa_Q is nonincreasing, E_b >= b sigma/2 >= epsilon/(2n_0), so both exponentials are below e^(-cb/n_0) (using a >= b/2). The map u -> (1-u)/(1+u) has derivative of modulus 2/(1+u)^2 <= 2 on [0,1], and (1-z)/(1+z) lies in [0,1].
- S10 (lines 102-108, statement (8)). HOLDS, by S11-S15. Constants depend only on q, as claimed.
- S16 (lines 151-156, the window (13)). HOLDS. Lower edge: tanh x <= 1 - e^(-2x) and the stack bound give 1 - z <= 2 exp(-N^(2 epsilon)) when beta w^2 <= (1-epsilon) log N, so z > 1/2 there. Upper edge: at w = ceil(A_j sqrt(log N log log N)), x^2 = A_j^2 log N log log N/n_0^2 and log(2+x) <= log log N for large N, so (3) gives sigma <= C N^(-c A_j^2/n_0^2) and N^2 sigma <= N^(-D) when c A_j^2/n_0^2 > D + 3. The hypotheses of (8) hold (N >= 4w, w/n_0 >= X), so z <= tanh(N^2 sigma/2) + O(e^(-cN/n_0)) <= C N^(-D). Existence of the first width follows, with no monotonicity in w.
- S17 (line 158, the prescribed width w_N). HOLDS. At w_N, c x^2/log(2+x) ~ 2c log N log log N/n_0^2, so in the competing branch z(N,N;w_N) is below every inverse power of N for all large N. In the ordinary branch (4) with spectators (w_N, w_N) and h ~ K n_0 log log N <= w_N gives (1-z)/2 <= exp(-c N^2/(n_0^2 log log N)), so z -> 1. Under the neutral premise this gives the stated equivalence with (W).
- S18 (line 160, the crossover read in the normal period). HOLDS. N(w)^2 sigma -> u, N(w)/w -> infinity by (3), and (8) applies; the converse is (8) with error e^(-cN/n_0) -> 0, giving sigma N^2 -> 2 artanh(z_*) = log[(1+z_*)/(1-z_*)].

### Step 4: the tension lower bound (26) (lines 311-348) - done

Extra sources read: row 1169 (7) (`gap-solve13-astra62.md` lines 78-85), row 1171 (9)-(10), (32)-(33) and the Gaussian normalization (`gap-solve14-astra62.md` lines 112-136, 448-466), row 1141 (3)-(7) (`gap-crux2-astra62.md` lines 55-112). The ingredients (17) and (18) of this file are checked in Step 6 (S23, S25) and were used here only after that check.

- S41 (line 318, the tent axes). HOLDS. For the 1D tent t(k) = (1 - |k|/l)_+, sum_k (t(k) - t(k-1))^2 is about 2/l and sum_k t(k)^2 about 2l/3; for a product of tents a unit translation changes only one factor, so the normalized squared difference is at most C/l^2. F(x)F(x)^T = sum_z phi_x(z)^2 T T^T = I. The cube lies at times x_1 - 5l to x_1 - 3l, and the path goes back in time first, so every link read has base time at most x_1 - 1.
- S42 (lines 320-325, (27)). HOLDS. For row isometries A, B the split eta = A^T(A eta) + (I - A^T A) eta, independence of the two parts, E|A eta|^(-2) = 1 for a standard 3D Gaussian, and |u/|u| - w/|w|| <= 2|u - w|/|u| give E|v(x) - T v(y)|^2 <= C||F(x) - T F(y)||_F^2 (as in row 1171, line 112). The block difference splits into the tent difference (C/l^2) and phi_y(z)^2 ||T(x,z) - T_xy T(y,z)||_F^2. For a temporal edge the two paths coincide after one step (zero); for a spatial edge they differ by one to three width-one strips of length O(l). For SU(2), ||Ad_g - I||_F^2 = 8 sin^2(theta) <= 16 min(1 - cos theta, 1 + cos theta), so the bound holds with either sign tau. Telescoping and Cauchy-Schwarz give b_ep >= 0 with sum_p b_ep <= C l^2, supported within C l of e. The bound is pathwise.
- S43 (line 327, the conditional odds). HOLDS. With corridors of width at least three, no plaquette has links in two interiors, so given Y the interiors (links and labels) are independent and |E[parity | Y]| = prod_i tanh(delta_i/2). The label mass is (Z + Z_12)/2 and the parity mean is (1-z)/(1+z).
- S44 (line 329, the profile and the map). HOLDS. The shell flow is the flow of row 1169 (7): uniform mass on shell s goes to uniform mass on shell s+1 (vertex (j, s+1-j) receives [j + (s+1-j)]/((s+2)(s+1)) = 1/(s+2)). Stopping uniformly on shells R..2R-1 gives rho <= 1/(R(R+1)) <= R^(-2), sum rho = 1, and sum u^2 <= sum_(s<2R) 2(s+1) pi^2/(s+1)^2 <= C log(2R). The map is a triangular product of left translations whose multipliers depend only on strictly earlier original layers, so it preserves conditional product Haar and fixes Y. It is used only through the change of variables Z_i(-tau;Y) = Z_i(tau;Y) E[e^(-Delta S) | tau, Y]; no involution is needed, as line 316 says.
- S45 (lines 331-337, (28)). HOLDS. Transporting each inserted rotation to the face base along the boundary path that the holonomy follows changes its axis by at most d (telescoping of the mismatches); with equal axes the product is exp(eps pi(1_o - rho_p) v), and the -1 at o cancels the toggle. Then |1 - B_p|^2 <= C(rho_p^2 + d^2 sum_(e in p) u_e^2). Averaging over eps removes the terms with one or three sine factors; the surviving imaginary parts are of the form sin u_j sin u_k (v_j x v_k) and four-sine terms, which vanish for equal axes and are at most C d sum u_e^2. With |Im(tau U_p)|^2 <= 2(1 - tau w_p) and 2uv <= u^2 + v^2 the averaged increase per face is at most C beta [rho_p^2 + (d_p^2 + s_p) sum_(e in p) u_e^2]. The same holds on mixed faces, where |1 - B| = |sin u_e| |v(x) - Ad v(x+k)| and the eps-averaged imaginary part is -sin^2 u_e (v' x v). Summing with (27) over the w^2 copies gives the two brackets of B_i and sum_p h_ip <= C w^2 (1 + l^2) log(2R), with max h_ip bounded by a function of l, R only.
- S46 (lines 339-348, delta_i <= 2E[B_i|Y], (29), the union bound and (26)). HOLDS. Jensen gives log(Z_i(tau)/Z_i(-tau)) <= E[B_i | tau, Y]; the more probable label has conditional probability at least 1/2 and B_i >= 0. For (29): exp of the mean over random marks is at most the mean of exp (Jensen), then (17) on each deterministic mark set gives 2 prod_p (1 + (C_0 - 1) h_p/H) <= 2 exp((C_0-1) H^(-1) sum h_p). Conditional Jensen passes to E[. | Y]. With C_4 >= 4C the deterministic part of 2E[B_i|Y] is at most K/2, and exponential Markov at parameter c_0/H gives the stated tail once c_0 C_4/4 > (C_0 - 1) C. The union bound over subsets of size ceil(m/2) costs 2^m, absorbed for w^2 large at fixed l, R. On the good exteriors the parity is at most tanh(K/2)^(m/2) <= exp(-m e^(-K)/2). With m >= c ab/(R+l)^2 and ab -> infinity, sigma >= c e^(-K)/(R+l)^2. With l = R = ceil(beta^(1/4)), each term of K/w^2 is O(sqrt(beta) log(2+beta)) and (R+l)^2 <= C beta^(1/2). This is (26).
- S40 (lines 311-316, statement (26) and the extension of (24)). HOLDS, by S41-S46. The extension of (24) to s > C sqrt(beta) log(2+beta) holds: in the proof of (24) replace K by the new K and m by c N^2/(R+l)^2.

### Step 5: the quadratic comparison (32)-(33) and the separation (35) (lines 369-420) - done

- S51 (lines 371-388, (32), the face identities, the deterministic bound in (33)). HOLDS. For a normal face, Re(omega_p Utilde_p) = Re(B_p U_p) with B_p = omega_p Utilde_p U_p^(-1). For a mixed face, Utilde_p = R_i(x) U_p (U_k(x) R_i(x+k) U_k(x)^(-1))^(-1), so Re Utilde_p = Re(S^(-1) R_i(x) U_p) and |1 - B_p| = |R_i(x) - S|, the second sum in (32). The identity replacement gives D = 4 w^2 (one -1 face on each of the w^2 normal planes).
- S52 (line 390, the local alternatives). HOLDS. c_p = omega_p (d eta)_p is cohomologous to omega. If all multipliers at a negative face are within chord 1/8 of their signs, telescoping moves the product by at most 4/8 from -1, so its chord from +1 is at least 3/2. For a negative mixed face, eta_i(x) = -eta_i(x+k) and conjugation fixes the centre, so the mixed term is at least (2 - 2/8)^2 >= 1. If |R - eta| >= 1/8 for the nearer centre eta, then 2(1 - |Re R|) >= 1/64 and |Im R|^2 >= 1/128. There are no negative 34-faces.
- S53 (lines 392-397, the localized cost). HOLDS. |v - Ad_g v|^2 = 4(|h|^2 - (v.h)^2) with h = Im g, so m_x = 4 lambda_min(Gram(h_1, h_2)); lambda_min >= |h_2 perp|^2/2 when |h_1| >= |h_2|. Row 1141 (3) with threshold sqrt(t/2) gives at most M_b t/2 = 2(1+6beta) t for each of the two cases, so 4(1+6beta) t in total, for 0 < t <= 1. The NE and SW plaquettes at x share no link, so a private link exists. Iterated conditioning over disjoint loop pairs is valid because each earlier event is measurable with respect to links outside the current pair. Telescoping R_i(x) - Ad_(U_gamma) R_i(x) into four covariant differences, each a mixed-face term of (32), and Cauchy-Schwarz give at least c_*^2 m_x/4 >= c t. The real part of R_i cancels under conjugation.
- S54 (line 399, the required surface). HOLDS. The negative faces form a closed dual 2-cycle mod two; each component is closed. The total pairing with a normal 12-torus is the pairing of omega, which is odd, so some component has odd pairing; by the strip identity this holds on all w^2 disjoint parallel normal tori, so k >= w^2. If more than k/2 faces had no vertex with m_x < t, bounded overlap would give D >= c t w^2/(2M); so D < c' t w^2 forces at least half of the faces to have a bad vertex.
- S55 (line 401, the count and (33)). HOLDS. Rooted connected candidates: at most 6abw^2 C_5^k. Subsets and vertex choices: at most C_6^k. After greedy thinning, c'k disjoint loop pairs with joint probability at most [4(1+6beta)t]^(c'k). With t = epsilon_A/(1+6beta) and C_5 C_6 (4 epsilon_A)^(c') <= e^(-A-1), the sum over k >= w^2 is at most C abw^2 e^(-A w^2), with constants free of beta and the periods. The m_x are functions of the original 34-links only, so the union over candidates handles any dependence of the replacement on U.
- S56 (line 403, the discriminating geometry). HOLDS. With log(ab) = o(w^2) the probability in (33) tends to zero, and beta/(1+6beta) >= 1/7 for beta >= 1. At a = b = N, w = ceil(sqrt(log N) log log N), w^2 = log N (log log N)^2 is much larger than log(N^2).
- S57 (lines 405-412, (34) and its consequence). HOLDS. Re U - Re(BU) = (1 - Re B) Re U + Im B . Im U = |1-B|^2/2 - (1 - Re B)(1 - Re U) + Im B . Im U; summing over faces with B = 1 on 34-faces gives (34). Averaging (33) over any randomized replacement gives beta E[D] >= (1 - o(1)) c w^2, so a mean signed increase o(w^2) forces beta E[bracket] >= c w^2.
- S58 (lines 414-420, (35)). HOLDS. -log z = 2 artanh((1-z)/(1+z)), and (1-z)/(1+z) <= C_beta exp[-c_beta e^((s - C sqrt(beta) log(2+beta)) w^2)] -> 0 by (24) extended through (26). For A > s, N^2 w^2 e^(-A w^2) <= w^2 e^((s-A) w^2) -> 0, and beta/(1+6beta) >= 1/7.

### Step 6: every other statement - done

Extra sources read: row 1139 (`gap-frameless-2d-astra.md` lines 46-99), row 1161 (19) (`gap-solve9-astra62.md` lines 264-310), row 1171 (9), (33) (lines 114-136, 448-466), the commits named on line 5, and a local copy of the outline and the complete account for the line numbers on line 7.

Records (GUIDE and OPEN).

- S0a (line 3, GUIDE plan). No claim to check.
- S0b (line 5, GUIDE repo search). HOLDS as a record. All seven named commits exist in the clone. Spot checks: PR 10114 `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 4-14 states a one-step plaquette witness at every beta > 0 and contraction at beta <= 1/32; PR 10149 `PROOF_TREE.md` 47-51 lists the third transition and the positive physical gap as OPEN; main `research/mass-gap/library/gap-phys-seed.md` 311-320 is Theorem ZD-c. The PR 10133 and 10134 references were not opened (several files of that name exist at 10133).
- S0c (line 7, GUIDE credits). HOLDS as a record, checked against a local copy of the two Sussman-Alpoge files whose commit I could not confirm: outline 2315-2335 is the gauge-projected transfer, 588-599 the clustering example with d mu = E e^(-E) dE, CA-I 2703-2712 lists "a mass gap" among what is not asserted, and 47244-47251 says the bounds depend only on d and the block size L. Credits to Balaban, Sussman and Alpoge, and Chatterjee are given.
- S0d (line 9, OPEN target). HOLDS as a restatement: it matches row 1161 (line 215 there) and Theorem ZD-c.
- S0e (line 41, GUIDE). No claim.

The separate-insertion bound (14) (lines 162-215).

- S20 (line 171, the ramp). HOLDS. The central jump between rows q and q+1 multiplies the stack faces by -1 and cancels the toggle; mixed faces at row q+1 have B = (-1)(-1) = 1; consecutive ramp angles differ by pi/R; the rotations use only tangential links, so the toggle is an involution preserving Haar.
- S21 (lines 173-179, (15)). HOLDS. For an edge in coordinate i, the coordinate-ordered paths differ by one width-one strip per later coordinate; ||Ad_g - I|| <= 2|1 - g|, telescoping and Cauchy-Schwarz give C l times the strip deficit; the incidence count (one free coordinate whose root coordinate is prescribed, probability about 1/l) gives mean incidence C l. Inter-rectangle edges: at most C R w^2/l, each at most 4.
- S22 (lines 181-187, (16)). HOLDS. For a 1k-face, Re Utilde_p = Re(B tau_p U_p) by cyclicity. For unit quaternions, |Re(BP) - Re P| <= |1-B|^2/2 + |Im B||Im P| <= |1-B|^2 + (1 - Re P), using |Im P|^2 <= 2(1 - Re P). Summing |1-B|^2 <= C w^2/R + C l^2 sum s_p + C R w^2/l gives (16).
- S23 (lines 189-194, (17)). HOLDS. The normalized one-link multipliers I_(l+1)(beta)/I_1(beta) increase with beta, so halving a marked electric coupling lowers the normalized convolution in operator order; the scalar cost per mark is z_(beta/2)/z_beta, bounded (it tends to 2^(3/2) at large beta). Central flips commute with the layer operators and are collected into one unitary for trace Hoelder. Schatten norms are monotone under 0 <= A <= B. The label mass is at least Z/2. Hoelder over four direction classes with exponent four gives c_0 = 1/8.
- S24 (lines 196-200, usability). HOLDS. With 1 + l^2 <= 2 l^2, beta sum s_p <= A R w^2 makes L_i <= K for the stated K. Exponential Markov with (17) bounds k prescribed unusable insertions by 2 exp[-(c_0 A - C') k R w^2]; the union bound costs at most 2^m. Toggling i negates its own log difference and leaves the others unchanged, so usability is orbit invariant.
- S25 (lines 202-207, (18) and (14)). HOLDS. On an orbit the labels are independent with odds e^(Delta_i), so |E[parity | orbit]| = prod tanh(L_i/2) <= tanh(K/2)^(m/2) <= exp(-m e^(-K)/2) on the good orbits. With R = floor(beta^(1/6)), l = floor(beta^(1/3)), each term of K/w^2 is O(beta^(5/6)). The conditions 2 <= R <= l and w >= 4l are the stated thresholds.
- S19 (lines 164-169, statement (14)). HOLDS, by S20-S25.
- S26 (lines 209-215, where (14) stops). HOLDS, with one reading note. Row 1141 (4) and (7) on disjoint 3 x 3 cells of the 34-sheet, with telescoping around the two plaquettes, give sum |v_x - Ad v_y|^2 >= N delta_b/16 >= c w^2/(1+6beta) for every axis field, outside probability e^(-cw^2); signs only flip staple vectors. On a mixed face at a ramp row of angle alpha both multipliers have scalar part cos alpha, so |1-B|^2 = sin^2(alpha) |v - Ad v'|^2. Reading note: "a ramp row has sin^2 alpha >= 1/2" is true for some ramp row (the angle nearest pi/2, sin^2 >= cos^2(pi/(2R)) >= 1/2), not for every ramp row (alpha = pi/R gives sin^2 < 1/2 once R >= 5). The conclusion uses only one such row.

Planar thermodynamics (lines 217-258).

- S27 (lines 219-228, (19)). HOLDS. Ordinary: (9)-(10) applied to Z. Competing: Z = H + Q = H(1 + Q/H), with (11), (10) and (8); the order-limit consequences 0 and 3 log 4 follow because sigma > 0 at fixed w.
- S28 (lines 230-243, (20) and the exponential bound). HOLDS. Z_+ = Tr(F^a P_0) = lambda^a e^(g_+), so H_+ = g_+ + a kappa_Z(b) by definition; (2) for Z and Z <= 8 Z_+ give the upper bound. Z_+ <= Z and Z_+ <= V (it is one term of each), the common planar pressure and (10) give H_+ <= C e^(-cb/n_0); for small aspect ratios the stated change of the start of (9) works with constants depending on the interval.
- S29 (line 245). HOLDS. g_+ <= H_+ gives s_+ <= e^(H_+) - 1. In the other direction row 1161 gives a Z-seed or V-seed with one margin at each fine cutoff, and the exponential bound at aspect 1/512 and w = b = n gives H_+ <= C e^(-c 2^k) at the side 2^k L in either branch.
- S30 (lines 247-256, (21)). HOLDS. In the frame with time along a w-direction and spatial box (N,N,w), 2F(N,N,w,w) - F(N,N,2w,w) = 2g_Z(w) - g_Z(2w), which lies in [g_Z(w), 2g_Z(w)] since S(2w) <= S(w). Lower bound: row 1161 (19) on the rectangle (the same extension was checked for row 1175 (11)) with k = floor(M e^(-Cw)/2) and binom(M,k) >= (M/k)^k gives a neutral trace of at least 2^(k-1), hence tau >= c w e^(-Cw). Upper bound: Lemma E' factors (2N/d)^2 (2w/d) <= 64 (N/w)^2, time monotonicity, and g_Z <= g_(A_0) + log 8.
- S31 (line 258, the local-factor obstruction). HOLDS. The factor 1 + rho_j^(abcd) is common to every twisted and untwisted integral, so z and the twist curve are unchanged exactly, and log(1 + rho^(abcd)) -> 0 at fixed j, c, d preserves the pressures, sigma, the limiting excess and tau. At a = floor(n_j/512), b = c = d = n_j, rho_j^(a n_j^3) = exp(-a_j L^4/512 + o(1)) -> 1, so H_+ gains log 2 in the limit. It is a counterexample to the inference only, as the text says.

The conditional sheet counterexample (22)-(23) (lines 260-282).

- S32 (lines 262-268, the reduction and statement (22)). HOLDS. Given equal tangential fields on both slices, the 1-links of the cut meet only the 1k-faces of the cut, with weight beta Re(p_x A p_y^(-1) A^(-1)), an O(4) spin model with conjugation bonds; the elementary 12-twist on the cut is an antiperiodic 2-bond.
- S33 (line 270). HOLDS. Zero deficit forces one common quaternion on the identity-connected cube (as in row 1139, line 53), and invariance under conjugation by (1+i)/sqrt2 and (1+j)/sqrt2 forces it into span(1,i) and span(1,j), so +-1.
- S34 (line 272). HOLDS. Each H^1 class has the same number of flat sign fields; the bad set is closed and misses the two zeros, so delta > 0; with 24m bonds, a cap of radius rho with 48 rho^2 <= delta/2 in the zero class and Haar cost c_*^(8m) give P(all bad) <= 8 c_*^(-8m) e^(-beta delta m/2) <= e^(-kappa beta m) for large beta.
- S35 (line 274, chessboard with flat signs). HOLDS. Every plaquette of a site-reflection is in one half or in the plane, so the uniform flat-sign measure keeps the two halves conditionally independent with reflected laws; Cauchy-Schwarz, positivity of every P(S), and the doubling argument on dyadic coarse sides (as in row 1139 (1)) give P(S) <= e^(-kappa beta |S|).
- S36 (line 276, the defect area and (22)). HOLDS. The coarse cochain s_x xi^(2)_xy s_y is closed and in the class of xi; after local trivialization a negative edge has endpoints in opposite caps, so every cube containing it is bad; a nonzero class needs at least (w/2)^2 dual faces (b >= w covers the classes in directions 3, 4); connected sets: at most 3m 12^(2k); the sum gives C b w^2 e^(-c beta w^2), and P(trivial class) >= 1/2 under the stated condition gives (22).
- S37 (lines 278-282, (23)). HOLDS. The kernel D^(1/2) e^(beta sum p.p') D^(1/2) is pointwise positive and positive definite, so the top eigenvector is even. With b near e^(c_1 beta w^2), c_1 < c, (22) gives Tr_odd/Tr_even = (1-r)/(1+r) >= 1/3. Tr(K/lambda) <= e^(C_beta w^2), and spending b - 1 steps on lambda_o gives (23). The continuity remark holds.

Actual sign cancellation and the seed-conditional bound (lines 284-307).

- S38 (lines 286-299, (24)). HOLDS. h_beta = e^(-d_beta), so row 1175 (17)-(18) give 1 - E prod|tanh J_x| <= 2 N^2 e^(-d_beta w^2) <= 2 e^(-(d_beta - s) w^2). The signed mean equals (1-z)/(1+z) (row 1175 (14)), and (18) with m >= c N^2/R and K <= C_1 beta^(5/6) w^2 gives the double-exponential bound. |E P_J - E prod tanh J_x| <= E[1 - prod|tanh J_x|]. The cap estimate gives d_beta >= beta - C log(2+beta).
- S39 (lines 301-307, (25)). HOLDS. Row 1171 (33) (lines 448-466 there; rectangular tori allowed, line 117) gives z >= e^(-D_beta w^2) when all periods exceed C_0 sqrt(1+beta). With b >= K_q n_0 D_beta w^2 the error in the tanh form of (8) is at most half of that, and tanh u <= u gives sigma >= b^(-2) e^(-D_beta w^2), with b = O_j(w^2). Under the ordinary seed the limsup is 0 by (3).
- S47 (line 350, the limit of the quadratic cost). HOLDS. The face o has circulation pi; in the one-quadrant flow two of its edges carry pi/2 each, so pi/4 <= |u_e| <= pi/2 and sin^2 u_e >= 1/2; the two mixed faces through the edge give sin^2 u_e times the transverse mismatch, and the row 1141 sheet bound applies to every axis field.
- S48 (lines 352-357, (30) and the barrier). HOLDS. P(|J_x| <= eps w^2) <= e^(eps w^2) E sech J_x <= 2 e^(-(d_beta - eps) w^2), and N^2 <= e^(s w^2). A single link changes each J_x by at most 4 beta. A sign change of J_x must start inside the event. The stationary union bound and the factor 1/nu(P_J = +1) = 2 + o(1) give the claim.

What fixes the first width (lines 359-367).

- S49 (line 361, the plane Z_2 models). HOLDS. On an a x b torus the plaquette images of Z_2 link fields are exactly the even patterns, with equal multiplicity; so Z and Z_tw are [(2cosh J)^(ab) +- (2sinh J)^(ab)]/2 and z = tanh(s ab/2) when tanh J = e^(-s). The profile e^(-k w^2) with small k satisfies (3) (competing), (14), (25), (26) and the stack bound, and crosses at w_* ~ sqrt(2 log N/k). The profile e^(-k w^2/log w) with k > c/n_0^2 satisfies (3), because c x^2/log(2+x) = (c/n_0^2)(w^2/log w)(1 + O(1/log w)), and crosses at w_* ~ sqrt(log N log log N/k) (log w ~ (1/2) log log N).
- S50 (lines 363-367, (31)). HOLDS. At w_*, (8) gives sigma N^2 <= 2 artanh(1/2) + o(1) = log 3 + o(1); (25) with b = O_j(w^2) gives D_beta w^2 >= 2 log N - 4 log w - O_j(1), and log w = O(log log N) by (13).

Summary records (lines 422-426).

- S59 (line 424, OPEN). HOLDS as a summary; each cited equation says what is claimed for it.
- S60 (line 426, RESULT). HOLDS; it matches the body. It omits the threshold w >= w_0(beta) of (26), which line 311 states.

### Step 7: verdict table and result - done

Numeric guide (not a proof step). A scratch script outside the repository (peak memory about 37 MB) tested, on random samples or exactly: |Re(BP) - Re P| <= |1-B|^2 + (1 - Re P) (largest ratio 0.91); ||Ad_g - I||_F^2 <= 16 min(1 - Re g, 1 + Re g) (largest ratio 0.9996); m_x = 4 lambda_min(Gram) (error 4e-15); (1+S)^4 - 1 <= 15 S on [0,1]; the shell flow stays uniform on shells up to 40; z = tanh(s ab/2) for the Z_2 plane model on 2 x 2 and 2 x 3 tori by enumeration; the ramp rows (largest sin^2 at least 1/2 for R = 2..8, smallest 0.345 at R = 5); z_(beta/2)/z_beta rises to 2^(3/2). All agree with the text. None of these runs is used as a proof step.

Not checked: the proofs inside the cited earlier rows beyond the parts named in Steps 2-6 (rows 1139, 1141, 1157, 1161, 1169, 1171, 1175 were read only at the cited statements and proofs; rows 1155 (9) and 1167 (1) were not opened and enter only through row 1175 (17), checked in row 1176, and through the normalizer ratio, which I checked asymptotically and by the guide). The PR 10133 and 10134 references on line 5. The commit of the local Sussman-Alpoge copy used for line 7.

| S | Line(s) | Statement | Verdict |
|---|---|---|---|
| S0a, S0e | 3, 41 | GUIDE plan lines | no claim |
| S0b | 5 | GUIDE repo search | HOLDS (record; commits exist, three file references spot-checked) |
| S0c | 7 | GUIDE credits and citations | HOLDS (record; checked against a local copy) |
| S0d | 9 | OPEN target | HOLDS (restatement) |
| S1 | 13-18 | trace representations, Z/8 <= V <= 8Z, odd sector nonempty | HOLDS |
| S2 | 20-32 | limits e_A, f_A; f_Z = f_V; (1); sigma >= -log tanh(beta w^2) | HOLDS |
| S3 | 34-39 | g_A, kappa_A >= 0, kappa_A nonincreasing; (2) | HOLDS (reading note: "contrary to kappa_A(b)/b -> 0" is the Lemma K(d) argument in short) |
| S4 | 45-60 | (3), both lines | HOLDS |
| S5 | 62-67 | tile estimate (4); first line of (3) | HOLDS |
| S6 | 69-73 | (5); Q/V = 4(1 + O(eta)) | HOLDS |
| S7 | 75-78 | g_V(r;s) <= C e^(-cr/n_0); (6) | HOLDS |
| S8 | 80-91 | kappa_Q(b) <= C eta/b; second line of (3) | HOLDS |
| S9 | 93-98 | branch test (7) equivalent to (W) | HOLDS |
| S10 | 102-108 | twist law (8) | HOLDS |
| S11 | 110-114 | (9) | HOLDS |
| S12 | 116-125 | (10), Z_B/V bound, (11) | HOLDS |
| S13 | 127-134 | (12) | HOLDS |
| S14 | 136-145 | (8) where b sigma <= epsilon/n_0 | HOLDS |
| S15 | 147 | (8) in the remaining range; tanh form | HOLDS |
| S16 | 151-156 | width window (13) | HOLDS |
| S17 | 158 | prescribed width w_N; equivalence with (W) | HOLDS |
| S18 | 160 | crossover in the normal period | HOLDS |
| S19 | 164-169 | (14) | HOLDS |
| S20 | 171 | ramp map | HOLDS |
| S21 | 173-179 | (15) | HOLDS |
| S22 | 181-187 | (16) | HOLDS |
| S23 | 189-194 | (17) | HOLDS |
| S24 | 196-200 | usability and the union bound | HOLDS |
| S25 | 202-207 | (18); proof of (14) | HOLDS |
| S26 | 209-215 | where (14) stops | HOLDS (reading note: "a ramp row has sin^2 alpha >= 1/2" holds for some ramp row, not every; the argument uses one) |
| S27 | 219-228 | (19) | HOLDS |
| S28 | 230-243 | (20); 0 <= H_+ <= C e^(-cb/n_0) | HOLDS |
| S29 | 245 | neutral premise equivalent to small H_+ | HOLDS |
| S30 | 247-256 | (21) | HOLDS |
| S31 | 258 | local-factor obstruction | HOLDS |
| S32 | 262-268 | sheet reduction; (22) | HOLDS |
| S33 | 270 | tile ground states +-1 | HOLDS |
| S34 | 272 | all-bad bound with flat signs | HOLDS |
| S35 | 274 | chessboard bound P(S) <= e^(-kappa beta abs(S)) | HOLDS |
| S36 | 276 | defect area; proof of (22) | HOLDS |
| S37 | 278-282 | (23) | HOLDS |
| S38 | 286-299 | (24) | HOLDS |
| S39 | 301-307 | (25) | HOLDS |
| S40 | 311-316 | (26) and the extension of (24) | HOLDS |
| S41 | 318 | tent axes | HOLDS |
| S42 | 320-325 | (27) | HOLDS |
| S43 | 327 | conditional odds setup | HOLDS |
| S44 | 329 | profile and Haar-preserving map | HOLDS |
| S45 | 331-337 | (28) | HOLDS |
| S46 | 339-348 | delta_i <= 2E[B_i given Y]; (29); proof of (26) | HOLDS |
| S47 | 350 | limit of the quadratic cost | HOLDS |
| S48 | 352-357 | (30) and the mixing barrier | HOLDS |
| S49 | 361 | Z_2 plane models | HOLDS |
| S50 | 363-367 | (31) | HOLDS |
| S51 | 371-388 | (32); deterministic bound and face identities of (33) | HOLDS |
| S52 | 390 | local alternatives on each face | HOLDS |
| S53 | 392-397 | localized cost 4(1+6beta)t | HOLDS |
| S54 | 399 | required surface has at least w^2 faces | HOLDS |
| S55 | 401 | count; (33) | HOLDS |
| S56 | 403 | consequence at log(ab) = o(w^2) | HOLDS |
| S57 | 405-412 | (34) and its consequence | HOLDS |
| S58 | 414-420 | (35) | HOLDS |
| S59 | 424 | OPEN summary | HOLDS (summary) |
| S60 | 426 | RESULT line | HOLDS (reading note: it omits the threshold w >= w_0(beta) of (26)) |


Counts: 58 PROVED statements checked by hand: 58 HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL. Seven records (four GUIDE, two OPEN, the RESULT line) are consistent with the body. Three reading notes (lines 34, 215, 426) change no verdict.

Status: complete for this row.

RESULT (2026-11-19 21:57Z (date -u; started 21:28Z), Claude Opus 5.5 max, laptop subagent; cross-provider check of gpt-6.2-astra row 1177, grants no status): row 1177 HOLDS. 58 PROVED statements checked by hand: all 58 HOLD, none needs correction, none FAILS. The equivalence of (W), given the one-cube neutral bound, with the planar tension test (7); the competing-branch twist law (8) and its window (13); the unconditional tension bound (26); and (32)-(33), (35) hold. Three reading notes (lines 34, 215, 426), no verdict change. Open: the branch selection, the physical neutral bound, (W).
