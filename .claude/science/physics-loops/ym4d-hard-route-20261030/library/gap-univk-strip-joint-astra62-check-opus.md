# Check of library/gap-univk-strip-joint-astra62.md (FINISH row 1564)

Checker: Claude (Opus 5.5). Account: Ethan Sussman and Levent Alpoge (parts I-III, YM4_sketch_500.tex, YM4_1400.tex = Y).
Text checked: authored by gpt-6.2-astra (Codex); this check written by Claude.

## Plan
1. Read GOAL.md, FINISH.md Rules / Working efficiently.
2. Read the row-1563 note in full, then rows 1557/1559/1561 notes and their checks.
3. Grep each cited account line range; read it.
4. Check positive claims one by one; then lemma (12) and the three attacks.
5. Verdicts; RESULT line.

## Progress
- Step 1 done: read GOAL.md, FINISH Rules / Working efficiently, the row-1563 note (273 lines) in full, row 1559 note sections defining C_{s,h}, Delta_h and (S).
  (S) (row 1559): |log C_B(a)/C_A(a) - a^2 log C_B(1)/C_A(1)| <= C_* l_n; D_h(a) := T_a Delta log C_h is its left side.
- Step 2 (algebra, by hand, before sources): see sections below.
- Step 3 done: sources read (ranges listed per claim below). Step 4: numeric guide (scratch script chk_phi.py in the scratchpad, pure python, `python3 -I`): finite-difference det D_qF on a random 6-anchor row (L=3) agrees with (2) to 4e-11 relative; Phi agrees with the leading term of (3) to 1e-3 relative; (6) and (14) series agree. Guides only, not proof steps.

Provenance: Claude (Opus 5.5), lane commit as checked out at /ym4d-lead clone (not re-pinned), not an audit. Note under check: library/gap-univk-strip-joint-astra62.md (row 1563, gpt-6.2-astra max).

## Verdicts, positive claims

### P1. Which scale enters a joint filing (note lines 22-28). HOLDS.
- O 8342-8349 (QC25 "an identity of local fibre measures", one 3x3 pivot block per coarse bond, u=gy gives (sigma_0 g^3)^{|F|}, (det J_c)^{-1}=L^{-3}(det m_c)^{-1}) read: matches. The factor L^3 per occurrence between |det D_pM|^{-1} and z_c=L^3/|det H_c| is the row-1559 convention: matches.
- O 7481-7496 read: Jacobians divided by sigma_H(0) "are included in P^(k)", sigma_H(0) per nonpivot bond goes into the step constant. Matches.
- Y 83072-83096 read: frame scale theta_j^{-1/2} "scales a fluctuation in the fixed-frame step"; g_j=x_j^{-1/2} is the running coupling. O 20250-20255 (frame conventions) read. CA-III 12179-12191 read: "one and the same prescribed scaffold", theta_s=X+c_0 s, depth s(l)=n-l, levels indexed by A. So at common depth the frame units coincide and sigma_0 theta_s^{-3/2} cancels bond by bond. HOLDS. Row 1417 §5.5 / check 1422 not re-read (cited only for the bare Haar factor, which cancels trivially at a common coordinate value).

### P2. Joint QC25 on a solved row. HOLDS (each item).
- Source: Y 75190-75268 read. F(q)=exp_q(w(q)), w=sum alpha_i log_q H_i, sum alpha=1-L^{-3}, at most L^4-L terms on the regular branch, Haar in the middle bond = Haar in q; B(w) dF = H(w) - sum alpha_i H(v_i) with H(v)=P_v + r cot r (1-P_v); B(w) transverse eigenvalue |w|/sin|w|; det dF >= beta^3 = L^{-9}. Weights L^{-4} per start: QC3 M(U)(c)=exp[L^{-4} sum_x log Z_x]U[c] (O 7963-7987 via check 1562 line 30). Matches the note.
- (1): log_q u = k(t)(u - t q) with k=arccos t/sqrt(1-t^2); balance sum lambda_i log_q u_i = 0 with u_0=W, lambda_0=1 is F(q)=W (|w|<pi by Y). Dotting with u_l gives (1). Jacobian in t at (J,1): d=b, d/dt_m[d t_l] = b delta + (2/3)lambda_m, d/dt_m[sum lambda_i k G_il] = -lambda_m/3, total bI + 1 lambda^T; eigenvalues b on ker lambda^T, 2b on 1 (lambda^T 1 = b). IFT applies. Agreement with the actual branch: d(q,W)=|w| <= (1-b) max_i d(q,u_i) <= (1-b)(max d(u_i,W)+d(q,W)). HOLDS. k(1)=1, k'(1)=-1/3 (t=cos theta, k=theta/sin theta) checked.
- (2): numerator sum lambda_i Hess_i = sum lambda_i [t_i k_i I + p(t_i) e_i e_i^T] = d I + sum lambda_i p_i e_i e_i^T (transverse eigenvalue theta cot theta = t k, radial 1, |e_i|^2=1-t_i^2); denominator det k(t_0)^2; Sylvester det(I_3+AB)=det(I_{N+1}+BA) with e_i.e_l = G_il - t_i t_l. At J: b^3. HOLDS. Phi depends on G alone: an O(4) orbit of a point configuration in R^4 is fixed by its Gram array, and isometries of S^3 preserve |det dF|. So equal Gram arrays give equal pivots with W_A != W_B allowed. HOLDS. Phi >= 0 from the floor; 9 log L - Phi and 12 log L - Phi follow from det = b^3 e^Phi and z_c = L^3/det. HOLDS.
- Linearization and (3): (bI+1lambda^T) tdot = s gives lambda^T tdot = S/(2b), tdot = s/b - S/(2b^2); ddot=(2/3)lambda^T tdot; 3 log d -> S/b^2; bracket -> -S/(3b^2); -2 log k(t_0) -> 2s_0/(3b) - S/(3b^2); sum S/(3b^2)+2s_0/(3b). With g_il=-|u_i-u_l|^2/2, x_i=u_i-W: s_0 = (1/2) sum alpha_i|x_i|^2 and S = b sum alpha|x|^2 + |sum alpha x|^2, giving exactly the coefficients 2/(3b) and 1/(3b^2) of (3). Single repeated anchor check: (2/3)(1-b)b t^2 + (1-b)^2 t^2/3 = (1-b^2)t^2/3, equal to the t^2 term of 2 log(sinc(bt)/sinc t) (power map b x in exp coordinates at u, density sinc^2). HOLDS.
- (4): T_a Delta Phi = int [DPhi(G^a_tau)(delta_a - a^2 delta_1) + a^2 (DPhi(G^a_tau)-DPhi(G^1_tau)) delta_1] dtau; |G^a_tau - G^1_tau| <= max_s |G_s(a)-G_s(1)|; the max-norm ball is convex so all segments stay in it; constants depend on L through the number of entries. HOLDS.
- (5): Gram entries cos(r|X_i|)cos(r|X_l|) + t sinc sinc <X_i,X_l> checked by quaternion product; entire in t=r^2 with |G'|<=C rho^2, |G''|<=C rho^4; (Phi o G)'' = D^2Phi[G',G'] + DPhi G'' <= C_L rho^4; phi(0)=0 and |phi(s)-s phi(1)| <= s(1-s) sup|phi''|/2 with s=a^2. HOLDS. The hypothesis is on the resulting anchors, as the note says.
- (6): Y-independent series: 4 log(sin x/x) = -2x^2/3 - x^4/45; -2 log(3-2x cot x) = -4x^2/3 + 16x^4/45; sum -2x^2 + x^4/3. Pivot factor (3-2x cot x)^{-2} is row 1557 lines 172-174 (eigenvalues w, w(3-2t cot t) twice). Quartic part of T_a Delta H = (a^4-a^2)(t_B^4-t_A^4)/3. HOLDS.

### P3. Differing coordinate units (lines 103-114). HOLDS.
- 3(1-t) log(g_B/g_A) + H_t(z_B) - H_t(z_A) with H_t(z)=J(tz)-tJ(z): unit constant radius-independent, Haar log J(r^2 z). |H_t'(z)| = t|J'(tz)-J'(z)| <= t(1-t) z sup|J''|. |z_B-z_A| = |v|^2|g_B^2-g_A^2| <= 2 max z |log(g_B/g_A)| (integrate d(s^2)=2s^2 d log s). J analytic on [0,z_*], z_*<pi^2. HOLDS, including a=0.
- Scale-only solved row: displacement r|v||g_B-g_A| <= sqrt(z_*)|log(g_B/g_A)| (r<=1); the rest is conditional on the stated agreement of targets, centres, determining data and cutoff map, and on the Lipschitz premise ||d theta|| |H| bounded; then (2)'s gradient gives 2C_L|log| for the two radii. HOLDS as a conditional statement.

### P4. Class-load fit (7). HOLDS.
- CA-III 11994-12056 read: g_frak_j = g_j^2(log x_j)^{2q_flat}, z_i = sup|zeta^B_(i)-zeta^A_(i)|, z^sharp_j = sum_{i<=j} L^{-(j-i)}(z_i+z_{i-1}), and [[delta]]^u_j contains g_frak_j z^sharp_j as a nonnegative summand, so l_n >= g_n^2(log x_n)^{2q_flat} z^sharp_n. CA-III 53953-53963 read: x_(r) = theta_r - zeta_(r). |log(g_B/g_A)| = |log(x_A/x_B)|/2 <= z_j/(2 min x). HOLDS. z^sharp_n >= z_j for n=j (i=j term) and n=j+1 (z_{i-1} at i=j+1). HOLDS.
- Count: CA-III 9809-9814 (R_check least power of L >= (log x)^{r_pr}, so <= L(log x)^{r_pr}), 11578-11586, and 14-21 (q_flat >= p_0 + 10 r_pr + 1 at d=4) read. Per cell cost C_{L,M}(1+R_n)^4 z_j/x_j; with g_n^2 = 1/x_n and x_n/x_j bounded (O 20265-20287, RF5 and the tube, read) it is <= C (log x_n)^{4 r_pr - 2q_flat} g_n^2(log x_n)^{2q_flat} z_j <= C l_n. HOLDS. The note correctly limits it to n in {j, j+1}.

### P5. Unequal pivot occurrences (lines 126-142). HOLDS.
- O 17534 read ("those coarse bonds c of Omega_{j+1} that lie outside Lambda_{j+1}"); O 6055-6067 read (history fixes regions, stored bonds, variables); CA-III 11936-11949 read (aligned label, varpi_0=1/80, pairing pi the identity on H_al); CA-III 12340-12349 read (unpointed unit anchored in lowest zone met); Y 63260-63271 read (free bond with one end in the integration region goes to I); Y 63468-63495 read (quote verbatim, line-wrapped); Y 129399-129424 read (empty-switch recursion, nonempty pieces kept at the parent); CA-I 156848 quote verbatim, the enclosing proposition CA-I 156837 is headed "Proof outstanding"; CA-III 11955-11993 read (outer array indexed by uses of stored units); CA-III 13106-13133 read (stored, reading, own marks). With a common record the region sets coincide, so c -> c is a bijection of occurrences at h. HOLDS, conditional on the common record, which is the setting of (S).
- (8): 9 log L per physical joint pivot and 12 log L per carried z follow from P2. (4,-3) gives 36-36=0. Padding with G=J is exact (Phi(J)=0) and (4) applies with G_A == J. The two violation tests (integer defect with l_n -> 0; 3 Delta|F| log g with g -> 0 and l_n bounded) are correct as stated. CA-I 107383-107430 read: field parts log z - log z|_(1,0) and the field-independent sum are separated as the note says. HOLDS.

### P6. Carried reads and their moves (9). HOLDS.
- (9) is summation by parts: sum w_i p_{i-1} - sum w_i p_i + w_{m+1} p_m = w_1 p_0 + sum_{i=1}^m (w_{i+1}-w_i) p_i. The three special cases follow (all w=1: only p_0; a block of ones: two endpoints; equal Grams: zero). Y 102998-103025 read (quote verbatim, line-wrapped); Y 63651-63673 read (quote verbatim). HOLDS.

### P7. Other scalars sharing the cell. HOLDS.
- (10): -log M(D_0) = -(d/2) log 2pi + (1/2) log det D_0 (row 1559); Delta = (1/2) sum log lambda_nu; radius-independent so T_a gives (1-a^2). Scalar multiples: d(1-a^2)|log(alpha_B/alpha_A)|/2. M(g^2P)^{-1} = g^d M(P)^{-1}. Y 74892-74911 read, quote verbatim. HOLDS.
- (11): F1 (origin/main research/ym4d/library/st1-r4.md, Lemma F1, read) gives Jacobian 1 - theta'(|A'|/delta)<A',H>/(delta|A'|) in [7/8,9/8]; with A' = r g v this is the note's J_s. |log J_B - log J_A| <= (8/7)|J_B-J_A|; |chi'(u_B)-chi'(u_A)| <= sup|u chi''| |log(u_B/u_A)|, and u_B/u_A = (g_B/delta_B)/(g_A/delta_A) is radius-free; weights 1 and a^2. Y 62370-62402 read ("Its logarithm vanishes off the cutoff shell", rank-one determinant 1 - d theta(W' iH)); O 17519-17527 read (cutoff in |log W'|, Jacobian a boundary term). HOLDS. (11) uses only the triangle inequality across radii, so it is an upper bound, not a cancellation; the note does not claim more.
- artanh identity: w_B/w_A = (1+y)/(1-y), y=(w_B-w_A)/(w_B+w_A); artanh y <= y/(1-y^2). HOLDS. The converse remark (one weight -> 0 on B only) is correct.

## Verdicts, sufficient lemma (12)

### L1. (2), (4), (8)-(11) imply (S) from (12). HOLDS.
Write log C_{s,h}(r) = B_s + sum over analytic inputs X of (sign) psi_X(X_s(r)) + incoming log-spectral terms + sum over weights (sign) log w_s(r), which is the definition of C_h in row 1559 after the flat constants of (8) are removed. Then D_h(a) = (1-a^2) Delta B + sum T_a Delta psi_X + T_a Delta(incoming) + T_a Delta log w.
- Pivot, free-Haar input g^2 r^2|v|^2 (psi = J, analytic on [0,z_*]) and cutoff-Jacobian input y = d theta(W' iH) (psi = log(1-y), |y| <= 1/8): the proof of (4) needs only an analytic psi with bounded first two derivatives on a convex set containing both runs' values at both radii, so |T_a Delta psi_X| <= C E_a(X). Inputs outside the analytic ball are moved to the weight list as b^3/|det D_qF|. 
- Incoming and weights: |log u - log v| <= |u-v|/min(u,v), applied at r=a (weight 1) and r=1 (weight a^2); for a radius-independent incoming term the exact (1-a^2) factor is <= 1+a^2.
- Transition multiplicities |w_{i+1}-w_i| from (9) enter as absolute coefficients.
So |D_h(a)| <= max(C_L,1) x (left side of (12)), and (12) gives (S) with C_* = max(C_L,1) C. HOLDS. (11) is not needed for the implication; the analytic-input argument covers the cutoff Jacobian.

### L2. (12) is stronger than (S). HOLDS (as a logical demand).
(12) bounds the sum of absolute values over distinct inputs, with only Delta B kept signed; (S) bounds the signed total. Two pivots at h with opposite equal changes give zero in (S) and a positive term in (12). So (12) implies (S), the converse fails as a statement form, and failure of (12) cannot refute (S). The note does not exhibit a native admitted pair on which (12) fails and (S) holds; it does not claim one. Not equivalent to (S), so the "equivalent is not progress" test is passed; whether (12) is easier than (S) is not shown.

### L3. Last sentence of the paragraph after (12): "For a geometric joint strip on the prescribed common frame with no extra weights, (12) asks only for the sum of errors of the closed traces of its solved rows in (4)." HOLDS AFTER CORRECTION.
The lemma lists the cutoff Jacobian d theta(W' iH_s) as an analytic input, and H_s is run dependent, so if that Jacobian is jointly filed at h its E_a term also remains. Correction: "... with no extra weights and with the cutoff Jacobian at its boundary-term address (O 17526), or with its E_a(d theta(W' iH_s)) added, (12) asks only for ..." In the native O 17526 filing the Jacobian is a boundary term, so the statement is right there. Delta B = 0 (equal geometric counts, P5) and equal free inputs (common frame, P1) are as claimed.

## Verdicts, the three attacks

### A1. Stationary centre, free field varied (lines 216-228). HOLDS as a conditional estimate.
- Bond input: row 1561 (5) and lines 117-119 give every forming bond within C_L B d^{-2}; check 1562 line 27 checked this. Bi-invariance under the assumed common left multipliers keeps it; anchors (pivot-free by Y 75190-75216) and their means inherit it. Chord identity G_il = 1 - |u_i-u_l|^2/2 and ||a|^2-|b|^2| <= (|a|+|b|)|a-b| give the displayed |delta G| bound. Gradient of Phi then gives C_L(B+rho)B d^{-2} per row at each radius. HOLDS.
- Absorption: l_n >= E_0 C (log x_n)^{c_2} L^{-theta_2 n/4} (row 1561 after (6), checked in 1562), count C(1+R_n)^4, c_2 >= 10 r_pr, so the ratio is <= C (B+rho) B L^{-2(j+1) + theta_2 n/4}, with n <= j+1 and theta_2 < 1/4. HOLDS.
- Fresh strip: O 6055-6067 (true test |A_j| < delta_j) and O 17315-17335 (approximate test |V(M U)^{-1} - 1| < 2 delta_k; Omega_t^c from Q_t, P_t, Y; Z^[0] from R_t; S_t contains R_t) read. With x = (1+e) delta, a = (1+e/2)/(1+e): r x in {(1+e/2) delta, (1+e) delta}, both in (delta, 2 delta), and |e^{i r x H} - 1| = 2 sin(r x/2) < r x < 2 delta. So the approximate test passes and the true test fails at both radii; with P,Q,Y empty the R_t hull is in the new strip. HOLDS. The note correctly says this is not an admitted violating sequence.

### A2. Relative target displacement (lines 231-254). HOLDS.
- (13): (1-t^2)D(s) - (1-s^2)D(t) expands to (1-t^2)P(s) - (1-s^2)P(t) + (t^2-s^2)P(1); it kills 1 and r^2; |C_h| <= K(2-s^2-t^2) l_n. HOLDS. Constant P: C_h = 0, D_h = (1-a^2)P != 0. HOLDS.
- f(y) = 2 log(sinc y / sinc(y/b)) is the single-repeated-anchor Phi (power map at u, P2 check), c_b = (b^{-2}-1)/3. P(r) = f(rx) - f(beta - rx). beta = x: P(1/2)=0, P(1)=f(x), D_h(1/2) = -f(x)/4 < 0 for 0 < x < b pi (sinc strictly decreasing on (0,pi)). HOLDS.
- (14): leading P = c_b(2 beta x r - beta^2); the functional on r is (1-t^2)s - (1-s^2)t + (t^2-s^2) = (s-t)(1-s)(1-t). Remainder: R(rx) - R(rx - beta) = beta x int R' = O_L(|beta|(|x|+|beta|)^3). At s=1/4, t=1/2, beta=x: 2 c_b x^2 (-1/4)(3/4)(1/2) = -3 c_b x^2/16. HOLDS. Numeric guide agrees to 1e-8 relative at x = 10^{-3} b.
- Stationarity failure: at r=0 the anchors are 1 and W_B = e^{i beta H}, so q = e^{i(beta/b)H} on the central pivot link. In the commuting case angle(W) = b angle(q) + sum alpha_i angle(u_i), each transverse column (one of the L^3 transverse offsets) holding L starts along the averaging axis, each of weight L^{-4} (QC3), so weight L^{-3} = b per column. Moving -h on the pivot and +h on a face link of another column keeps W. The pivot is in no internal contour (O 8167-8176 via check 1562 line 31); a face-crossing link of c lies on no other coarse bond's contour (my reading of O 7957-7987: contour families stay inside blocks; the note asserts this without a line reference). Plaquettes of the two links are disjoint for a (1,1) transverse offset (parallel edges of one plaquette differ by one unit vector). Derivative -6 sin(beta/b) x (Wilson normalization) < 0 from the central link, 0 from the other. HOLDS under the stated stencil and free-bond premises, and as a one-step statement only; O 7454-7461 read (background is the critical point of V -> A(U_k(V)) on the fibre), so the note's restriction "at greater depth ... does not settle that problem" is correct.

### A3. Transfer, then project onto closed traces (lines 257-269). HOLDS.
- (15): (1/2)Re tr[(cos g + i sin g n_i.sigma)(cos b - i sin b n.sigma)] = cos g cos b + sin g sin b n_i.n, minus cos g. HOLDS. A common left rotation of W and all u_i leaves G unchanged. HOLDS.
- Sources: Y 129510-129566 read (competitor extended by the old root, "can be e^{iB_1}V^W", native padded rows must be matched); Y 131776-131786 read (same field and Jacobians by the same rule); Y 133218-133233 read (O_L(h^2) + O(eta eps_E), h = eta/L) and 133519-133546 (eps_E(r) <= C(eta^alpha r^{-1-alpha} + eta/r), C eta < r < 1) located; Y 134281-134298 read (C b e^{-cD}, tower distance D); CA-II 55884 opens "Assume the following statements."; CA-III 37547-37560 read (zeroth-order reading on exactly paired shells "is not proved"). The stopping point is stated exactly: no cited passage bounds the relative target/anchor projection (second term of (15)) at a newly determined cell, and the local data of (14) are not a native field there. HOLDS.

## Not checked
- CA-III 11866-11886, 12602-12645, 12719-12731 (read only through rows 1559/1561 and their checks); row 1417 §5.5 and check 1422; lit-balaban.md; O 9658-9667 (taken from check 1562). The repo-search section was not re-run.
- No defect found that breaks a stated result. One wording correction (L3).

RESULT: Row 1563 checks. All positive claims HOLD (scale convention, (1)-(6), differing units, (7), equal geometric pivot counts and (8), (9), (10), (11)); lemma (12) implies (S) and is a stronger demand in form (HOLDS; no native pair separating them is exhibited); the closing sentence on geometric joint strips HOLDS AFTER CORRECTION (add the cutoff-Jacobian input or its boundary-term address); attacks 1-3, (13), (14), (15) and the one-step stationarity failure HOLD, and the stated stopping point is exact. (S) and (12) stay open; no admitted violation was constructed.
Checked line by line by Claude (Opus 5.5).
