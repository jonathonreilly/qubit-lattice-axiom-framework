lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T14:46Z

# Check of row 1211, `library/gap-solve22-astra62.md`

Row 1214. Claude Opus 5.5 max, Mac mini Claude worker 2, started 2026-11-20T02:46Z (date -u). Cross-provider check of a gpt-6.2-astra max note. Pinned at branch commit d53039673. Check by hand, line by line. No numeric step is used as a proof step.

Verdict scale per statement: HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line.

## Plan (at most eight steps)

1. Read the note in full; list its numbered statements and every earlier row it cites.
2. Check the comparison (10): the propagated transfer spectrum against the singular values of the wall correlation operator. Read the cited setup statements first.
3. Check the recovery (18)-(20) of the neutral heat trace from two wall observations.
4. Check the remaining statements in order of their labels (PROVED first, then ARGUED).
5. Check each cited earlier row where a step depends on it (read the cited statement and its proof).
6. Check the OPEN claims and the scope sentence: what the note does and does not show about the strict infrared bound and the mass gap.
7. Grep `library/open-core.md` and the FINISH rows for any statement the note calls new; record matches.
8. Verdict table and RESULT line.


## Step 1. Inventory

The note has 341 lines and one RESULT line (L341). Line numbers below are those of `library/gap-solve22-astra62.md` at d53039673. The author is gpt-6.2-astra max (row 1211). The last OPEN paragraph says "The hand arguments in this note are by Codex"; the RESULT line of row 1211 names the author as gpt-6.2-astra. I treat these as the same author.

**Positive claims, checked first.**

| Label | Lines | Content | Depends on |
|---|---|---|---|
| (10) | L150-162 | singular values of the two-wall correlation operator against z_j^{t-r} | (9), (8), (7), (6), row 1155 (3) and (9), row 1149 (16), row 1173 (1) |
| (18) | L280-300 | H_d between (1-16 sqrt eps) e^{-2 eps} D_+(2d+2r) and D_+(2d) | (8), (10)'s operator, periodic version of (8), row 1155 (9) |
| (19)-(20) | L306-326 | exact-time circle law; reciprocal-density test | (8), stationary pair density |

**Other statements, in order.** (1)-(2) conditional ribbon action and zero-action paths (L17-36); majority reading (L40); (3) barrier (L42-49); K = BB* and Perron-Frobenius (L51); (4) (L53-57); (5) (L59-64); physical separation (L66); finite periods (L70); exterior cost (L72); (6) open slab (L78-92); application (L94); (7) one-box diameter (L100-123); (8) (L127-138); (9) (L140-148); (11) short collar (L166-179); (12) straight transports (L185-199); (13) KL resolution (L201-212); (14) local replacement (L216-226); (15) sparse sampling (L234-245); (16) Gaussian all-vector bound (L249-259); alias reading (L261); gapless local weight (L263); (17) OPEN and its consequences (L267-274); one-cube sufficient bound (L302); ARGUED pressure test (L330); (21) massless margin (L332-337); OPEN (L339).

**Cited earlier rows (files verified against the FINISH rows).** Row 1145 = `gap-solve2-astra62.md` ((1) Bessel comparison, (18) static charge); row 1149 = `gap-solve4-astra62.md` ((16) Bessel-ratio order); row 1151 = `gap-solve5-astra62.md` (section 3); row 1153 = `gap-solve6-astra62.md` ((3)-(6), (16) pressure); row 1155 = `gap-solve7-astra62.md` ((3) Birkhoff contraction, (3)-(5) columns, (9) marked-face moment); row 1161 = `gap-solve9-astra62.md` (one-cube criterion; (23)-(24)); row 1173 = `gap-solve15-astra62.md` ((1) geometric cut, (4), (6), Gaussian comparison); rows 1192, 1204 (records only). Outline: GL3 (2197-2231), GL8-GL10 (2313-2381), PL5 (3307-3321, 3400-3428). Earlier checks of these rows, by Claude: rows 1146, 1150, 1154, 1156, 1162, 1174 returned HOLDS or HOLDS AFTER CORRECTION (credit only). I read each cited statement again where a step of row 1211 depends on it.

## Step 2. The comparison (10) and its inputs (6)-(9)

(10) reads (9), (9) reads both lines of (8), and (8) reads (6) and (7). I check them in that order. Cited inputs read again here: row 1155 (9) and its proof (L130-134 of `gap-solve7-astra62.md`); row 1155 (3), the tanh(D/4) contraction (L55-59 there); row 1149 (16), the one-link order (L214-226 of `gap-solve4-astra62.md`).

**Row 1155 (9), the periodic marked-face moment. HOLDS.** Sort the marks into four classes by one direction mu that each mark contains. Take mu as time. Then every mark in the class is an electric face. Halving its coupling multiplies the normalized one-link convolution by I_d(beta/2)/I_1(beta/2) <= I_d(beta)/I_1(beta) on each irrep, by row 1149 (16) (each I_{j+1}/I_j increases). So 0 <= T_i <= K^{m_i} F as operators, with K = z_{beta/2}/z_beta <= C for beta >= 1. Then Tr T_i^b <= K^{b m_i} Tr F^b by min-max, and Schatten Hoelder gives Tr(T_1...T_b) <= K^{sum m_i} Tr F^b. Hoelder with exponent 4 over the classes gives c = 1/8. The proof needs a periodic torus, of any time length. It uses no property of the slab.

**(6), open slab, L78-92. HOLDS.** Put M_H = M exp((alpha beta/2) sum_{f in H} d_f), so M_H C_J M_H carries the full insertion on H. Spatial marked faces keep coupling beta/2 - beta/16 > 0 in each half weight, and C_J has coupling (1 - alpha) beta on J. So D_{H,J} = M_H C_J M_H >= 0. It is trace class: the Wilson weight is a class function with positive character coefficients, k(1) = sum_d d^2 c_d is finite, and there are finitely many links. Tr D^b / Tr F^b is the periodic expectation of exp(alpha beta sum d_f) over b(|H| + |J|) faces. Row 1155 (9) bounds it by C^{b(|H|+|J|)}. With ||D||^b <= Tr D^b and Tr F^b <= lambda_0^{b-1} Tr F, the b-th root as b -> infinity gives ||D_{H,J}|| <= lambda_0 C^{|H|+|J|}. For a step, ||M_{H_i} C_J M_{H_{i+1}}|| <= ||M_{H_i} C_J^{1/2}|| ||C_J^{1/2} M_{H_{i+1}}|| = ||D_{H_i,J}||^{1/2} ||D_{H_{i+1},J}||^{1/2}. The product over steps counts each interior spatial mark twice with weight 1/2 and each temporal mark once. End slices carry no marks, as (6) requires. The second line follows from 1{sum >= x} <= exp(alpha beta (sum - x)) and norm monotonicity for nonnegative kernels: |<f, K g>| <= <|f|, K'|g|> when 0 <= K <= K'. The constants depend on neither the volume, nor r, nor beta >= 1.

**(7), one-box diameter, L100-123. HOLDS.**
- Gauge facts. The filled box is contractible, so a flat field on it is pure gauge. If its boundary links are the identity, the trivializing gauge is constant on the connected boundary, and a global constant makes it the identity there. The lateral complex is the product cell complex of the box surface (a 2-sphere) and [0,s], so it is simply connected and a flat lateral field is pure gauge. The approximate versions follow by compactness, as written; there are finitely many box shapes. A boundary gauge, extended arbitrarily inside, is a Haar-preserving change of variables at intermediate times and a relabelling of the ends, so it leaves D(K_E) unchanged.
- Upper bound on I_E. Identity interior links give I_E <= C_b(1 + s delta^2). For unit quaternions d_f = |U_f - 1|^2/2, so four links within delta of 1 give d_f <= 8 delta^2.
- Exchange. There are s - 2 interior steps and s - 2 >= s/2 for s >= 4. So at one step the sum, over the two minimizers, of top-slice spatial action and step temporal action is at most 2 C_b (1 + s delta^2)/(s - 2) <= C'_b(1/s + delta^2). The boundary-fixed spatial gauge at slice t+1 acts at interior vertices only. It keeps both ends and the action. With |a - v|^2 = 2 d_f, the exchange that keeps the crossing temporal links below changes the action sum by sum_e [d(a1,v2) + d(a2,v1) - d(a1,v1) - d(a2,v2)] = sum_e (a1 - a2).(v1 - v2). I verified this identity. Tangential links give zero, because a1 = a2 and v1 = v2 there. So I(x,y') + I(x',y) <= I(x,y) + I(x',y') + tau. The same argument from minimizers of (x,y') and (x',y) gives the reverse inequality.
- Laplace. Haar is a probability, so log K <= -beta I. Balls of radius (1+beta)^{-1} have Haar mass >= c (1+beta)^{-3}, and the faces are Lipschitz. This gives log K >= -beta I - C_{b,s} log(2+beta). Hence D <= tau beta + 2 C_{b,s} log(2+beta) <= 2 tau beta for beta >= beta_0. The note writes 4 C_{b,s}, which is a weaker bound and also true.

**(8), L127-138. HOLDS.**
- Tiling. Put m = floor(n/b) >= 2 and split n into m parts of floor(n/m) or ceil(n/m). Since n/m < b(m+1)/m <= 2b, every part lies in [b, 2b].
- First line. The windows [1 + i(s+1), (i+1)(s+1)], 0 <= i < k, are disjoint and lie in [1, r - 2] since k(s+1) <= r - 2. So their spatial lateral faces lie on interior slices, as (6) needs. A failing box has more than k/2 bad windows, each with a lateral face of deficit > eta. These faces are distinct, so sum_D d_f >= eta k/2 with |D| <= C_{b,s} k. By (6), the kernel of each failing box is at most exp[-k(alpha beta eta/2 - C_{b,s} log C)]. Since 1_{G^c} <= sum over boxes of 1_{box fails} and the kernels are nonnegative, the norm bound sums over at most n^3 boxes. With beta -> infinity and k ~ n^gamma/(s+1), the bound is below n^{-A} for any fixed A.
- Second line. Given E, every face lies in one closed box or is a wall face, so K^all_E is a tensor product over boxes. Wall-only factors and end magnetic factors cancel in the cross ratio. The first step has diameter <= C_b beta, since -beta C_b <= log K <= 0. Row 1155 (3) proves the Birkhoff bound tanh(D/4) for any positive kernel whose cross ratio is bounded by D. I rechecked the total variation bound (sqrt D' - 1)/(sqrt D' + 1), D' = e^D, from the chord bound, with maximum at z = sqrt D'. A good window has D <= 2 tau beta by (7), so it contracts by tanh(tau beta/2) <= 1 - e^{-tau beta}. Other steps do not expand the Hilbert metric. Hence D(K_box) <= C_b beta exp(-k e^{-tau beta}/2). Since e^{-tau beta} >= n^{-tau B_0} > n^{-gamma/2}, the exponent is at least c n^{gamma/2}. Log cross ratios add over the boxes, and the sum over n^3 boxes is still super-polynomially small. Here (7) needs beta >= beta_0, which holds since beta -> infinity.

**(9), L140-148. HOLDS.**
- Conditional law. Given E, the unobserved ends have density proportional to psi_0(x_0, E_0) K^all_E(x_0, x_r) psi_0(x_r, E_r). This uses the Markov property at slices: every face lies in the past or the future of a slice, or on the slice. So the cross ratio equals that of K^all_E, which is at most e^epsilon on G.
- Product bound. Integrating p(x,y) p(x',y') >= e^{-epsilon} p(x,y') p(x',y) over (x', y') gives p >= e^{-epsilon} p_1 p_2. Put F_1 = f(., E_0) and F_2 = f(., E_r). Then E[|F_1(X_0) - F_2(X_r)|^2 | E] >= e^{-epsilon}(Var_1 F_1 + Var_2 F_2 + (m_1 - m_2)^2) >= e^{-epsilon} Var_1 F_1.
- Bad walls. E[1_{G^c} |f(X_0) f(X_r)|] = <|f| psi_0, lambda_0^{-r} F_{[0,r]}(1_{G^c}) |f| psi_0>_Haar <= epsilon ||f||_pi^2. Then u^2 <= epsilon ||f||^2 + u w <= epsilon ||f||^2 + (u^2 + w^2)/2.
- Sum. ||(1-Q) J_0 f||^2 <= e^epsilon w^2 + u^2 <= (1 + e^epsilon) w^2 + 2 epsilon ||f||^2, with w^2 = 2 <f, (1 - P^r) f>_pi since P is self-adjoint. This is (9).

**(10), L150-162. HOLDS.**
- The operator. By the Markov property at X_r and at X_t, E[phi(E) chi(E')] = <J_r^* phi, P^{t-r} J_0^* chi'>, where chi' is chi translated back to [0, r]. So the joint expectation operator is Q J_r P^{t-r} J_0^* Q.
- Exact case. J_r is an isometry and J_0^* J_0 = 1, so s_j(J_r P^{t-r} J_0^*) = z_j^{t-r} exactly.
- Left insertion. Apply (9) to P^{t-r} g with g = J_0^* chi, ||g|| <= ||chi||. Since sup_{0 <= z <= 1} z^{2(t-r)}(1 - z^r) <= r/(2e(t-r)), we get ||(1-Q) J_r P^{t-r} J_0^*||^2 <= (1 + e^epsilon) r/(e(t-r)) + 2 epsilon.
- Right insertion. Take the adjoint and use (9) at the end i = 0.
- Singular values. ||A - QAQ|| <= ||(1-Q)A|| + ||A(1-Q)||. Then s_j(A) = inf{||A - R|| : rank R <= j} gives |s_j(A) - s_j(B)| <= ||A - B||. P is compact and positive, since F = MCM >= 0 is trace class, and C_{E,t} is compact. So the lists are well defined, with zeros appended.
- Symmetry sectors. Gauge transformations at boundary vertices map wall links to wall links. Simultaneous center flips multiply links by -1 and keep the wall sigma-algebra. Both preserve the measure, so Q commutes with the averaging projections, and J_i intertwines the slice and slab actions. The same proof runs inside the invariant subspaces. Centering splits off z_0 = s_0 = 1, because C 1 = 1 and C^* 1 = 1.
- Quantifiers. (10) holds at every sufficiently large n on the sequence (beta -> infinity, beta <= B_0 log n, r = ceil(n^gamma)). C_1 is absolute. The diagonal choice b(n) -> infinity is a valid way to choose thresholds.

Precision (no correction needed): (10) is a finite-volume, fixed-cutoff comparison for each large n. It says nothing about a limit of the z_j, as L228 itself says.

Step 2 result: (6), (7), (8), (9), (10) HOLD. Row 1155 (9) and (3) and row 1149 (16) HOLD as used.
