# Check of library/gap-univk-strip-cut-astra62.md (FINISH row 1575)

Checker: Claude (Opus 5.5). Note author: gpt-6.2-astra max (row 1569).
Account: Ethan Sussman and Levent Alpoge (parts I-III, outline O = YM4_sketch_500.tex,
Y = YM4_1400.tex). Text of the note: gpt-6.2-astra (Codex). Text of this check: Claude.

## Plan
1. Read GOAL.md, FINISH.md (Rules, Working efficiently), row 1569/1575.
2. Read the note in full; read predecessor checks 1558/1560/1562/1564 for context.
3. Check each positive claim against the cited account lines.
4. Check native admission section and stopping point.
5. Verdicts, RESULT line.

## Progress
- Step 1 done: GOAL.md, FINISH Rules / Working efficiently, rows 1557-1575 headers, the note (307 lines) in full, check 1564 in full.
- Step 2: algebra of (1)-(8d) by hand; row 1563 (1)-(3),(14) re-read for the Gram expansion.

- Step 2 done (hand algebra, no numerics yet): (1)-(4), contraction, (5), polynomial reconstruction, relaxation, (6), (7), gamma formula, (8), (8a), (8b), Q_*, B_* bounds, (8c), (8d), (9)-(13), Q_D identity, (14), (15) sum, (16) and its example, (17)-(18), artanh weight: all re-derived; details in the verdict sections below.
- Step 3 done: sources read: O 9605-9626 (variational problem, regularity ceilings), O 9658-9667 (Theorem 1), O 7957-7987 (QC1-QC3: up to 24 coordinate-ordered paths, equal weights), O 8167-8176 and 8191-8199 (pivot support), O 17315-17336 (tests, Omega_t^c), O 17516-17534 (strip, Jacobian boundary term), O 9927-9985 (BGD1-BGD4), Y 75190-75268, Y 14649-14663 and 14691-14715, Y 2159-2169, Y 133218-133233, Y 133519-133549, Y 13335-13356, Y 37178-37234, Y 37390-37424, Y 10710-10781, Y 131951-131985, III 11866-11886, III 12045-12054, III 12364-12378, III 6823-6840, I 156835-156858, I 156907-156921.
- Step 4 (numeric guide, `python3 -I cutchk/guide.py` in this scratchpad; floating point and exact rationals, a guide only, not a proof step): the mass-matrix entries of (4) agree exactly (rational arithmetic) for N = 1, 3, 5, 9; the centred site mean (h^2 - eta^2)/12 agrees exactly; the mixed derivative of -log(b H^2) from (9) on a symmetric L = 3 outward row is -0.3111118, against -(4/(3L)) sum_l gamma_l = -0.3111111.

Provenance: Claude (Opus 5.5), by hand against the account (Ethan Sussman and Levent Alpoge; Claude and Codex as authors of their text), lane checkout as found, not re-pinned, not an audit. Note under check: library/gap-univk-strip-cut-astra62.md (row 1569, gpt-6.2-astra max).

## Verdicts, positive claims

### P1. What the two cutoffs prescribe (note lines 21-28). HOLDS.
- O 9607-9625 read: Gamma_j = bonds with an end point in Omega_j and none in Omega_{j+1}; interior or outward; inward bonds carry no constraint; critical = "stationary along the curves in C(B,V)"; regular = curvature below eps eta^2 L(p)^-2 and current below eps L(b)^-3. Matches. O 9658-9667: Theorem 1 states one regular critical orbit; the note takes it as sketched (lane status from check 1562). Matches.
- O 7957-7987 (QC1-QC3: up to 24 coordinate-ordered paths with equal weights, outer log average, weight L^-4 per start), O 8167-8176 and 8191-8199 (pivot support, L segments, J_c = L^-3 I_3), O 17317-17325 (tests, Omega_t^c formula, boxing), O 17516-17534 (strip substitution, Jacobian "contributes to the action as a boundary term") read. They match.
- III 11866-11886 read: V = V' V^c on live components, "triangular bondwise right translation", Haar preserved. I 156837 is headed "Proof outstanding". Y 37178-37234 (alignment lemma: b_1 - b_0 = 0 off C and <= C A_delta on C), Y 129510-129562 (from check 1564), Y 131951-131985 (keep the extra row term when a regional cut changes the relation) read. The descriptions match.

### P2. The boundary test (C) on the signed scalar (lines 30-40). HOLDS.
O_h = (D(x) - D(-x))/2 gives |O_h| <= max(|D(x)|, |D(-x)|). So (S) with constant C_* implies (C) with K = C_* on rays where both orientations pass, and an unbounded quotient in (C) refutes (S). (C) is a consequence of (S), not a sufficient condition. It is not equivalent, because even parts and one-orientation rays are untested, as the note says. Rule "equivalent is not progress": passed, as a necessary test only.

### P3. Stationary transmission equation (1)-(5). HOLDS.
- (1): a horizontal block mean at spacing h_m reads h_m times the site mean of F_i. Under coordinate-ordered contours the end-contour horizontal segments cancel between the two ends for direction-1 rows, and sum to zero over symmetric horizontal displacements for direction-2, 3, 4 rows (centred blocks, L odd). Re-derived.
- (2): the plaquette angle is u_{i+1} - u_i = arcsin(eta^2 p). The Wilson force on u_i is sin(theta_{i-1/2}) - sin(theta_{i+1/2}) = -eta^3 p'_m, constant on J_m including the sites beside a face (both midpoints lie in the closure of J_m). Each bare horizontal link has coefficient N_m^-3 in its row family's constraint: D^-4 times the D covering starts, summed over the two consecutive coarse bonds. The vertex-gradient terms telescope along a periodic line under a multiplier constant along direction 1. Diagonal-conjugation invariance kills the off-Cartan components. Lagrange multipliers suffice for stationarity on the tangent kernel; surjectivity is not needed. HOLDS.
- (3): the hat weights k/N_-, then 1 at the interface, then decreasing, re-derived. The system has unique solutions because M_eta is positive definite. The summed equation then gives zero period increment. HOLDS.
- (4): off-diagonal h/6 - eta^2/(6h) and diagonal h/3 + eta^2/(6h) per interval (the face point split eta/2 to each side). Re-derived; exact rational check in the guide. Row sums H_e, normalized diagonal >= 2/3, off-diagonal sum <= 1/3, so ||A_eta^-1||_inf <= 3. HOLDS.
- Contraction: for |t| <= R <= 1/4, |T' - 1| <= R^2 eta^4. The weights sum to one (the trapezoid sum of a hat equals H_e exactly). The map sends the ball into itself (R/2 + 6R^3 eta^4 <= R) and contracts by 6R^2 eta^4 < 1/2. HOLDS. Regularity: angles <= 2R eta^2, currents <= 2R/min h, both below the O 9616-9623 ceilings for small data. HOLDS. Identification with the history's orbit is through the sketched Theorem 1 only, as the note says.
- (5) and the polynomial reconstruction: ||A_0^-1|| <= 3, ||(A_eta - A_0) r|| <= (2/3) eta^2 ||r|| / (min h)^2, and the remainder is <= 2R^3 eta^4. The midpoint-rule and oscillation bounds were re-derived. HOLDS.
- Relaxation after (5): a constant added to f preserves (2) and all target-relative angles of a row. HOLDS for commuting rays with common Cartan left multipliers.
- Cell cost and load ratio C R L^{-2(j+1)+theta_2 n/4}: the inputs are the ones checked in checks 1562 and 1564. III 12045-12054 and 12364-12378 read (classical floor E_0 C (log x_n)^{c_2} vartheta_2^{n/4}, untruncated on aligned zones; theta_2 = (5 theta_A - 3)/8 lies in (0, 1/4)). HOLDS.
- The sentence "The native triangular translations do not allow this difference to be prescribed independently at the two cutoffs" is a reading of III 11866-11886 (V = V' R_s with R_s the run's own field). It is not a proved statement. Label it as a reading.

### P4. The nonzero mixed coefficient on an outward stationary row, (6)-(8). HOLDS.
- (6): M_eta = M_eta' + ((eta^2 - eta'^2)/6) K, so rdot_B = v^0 + ((eta^2 - eta'^2)/6) M_eta'^-1 d. The sign follows from positive definiteness. HOLDS.
- (7): the site mean of x^2 on a centred interval is (h^2 - eta^2)/12 (exact in the guide). The difference of the J_* mean and the central-subinterval mean is Q''(1 - L^-2)/24, with no mesh term. HOLDS.
- gamma_{s,l}: O 7957-7987 confirms equal weights over the coordinate orders, so each order gets 1/2. The crossing has one end in the new region, so it is omitted from the old determining set (Y 14691-14715 read: "every crossing bond with an endpoint in the new region was omitted from the old determining set"). Only the paths of c use it (the O 8167-8176 argument applies to every link crossing that face, not only the pivot). sum_l Delta gammadot_l = (L/2) Delta gdot^-_0. HOLDS.
- (8): with row 1563 (3), the tau x term of the first sum is (4r L^-4/(3b)) sum gammadot. The second sum vanishes because the full weighted mean is zero (the central column has zero angle). This gives -(2r/3) Delta gdot^-_0. Then (2/3)(1/24)(1/6) = 1/216 and the factor a(1-a). Re-derived; HOLDS. The odd part equals tau x times an analytic function with value (8) at the origin (Delta = 0 at tau = 0). HOLDS.
- Stationarity and admission of that row: stationarity HOLDS exactly (P3). Regularity holds for small data. Admission is NOT established: no history is shown to produce the slab Omega_{j+1}, its failure sets or its two passing points. The note says so (lines 44, 80, 137). (8) carries eta^2 - eta'^2, so it is a matched-data term inside the cost C R eta^2 of P3 and is absorbed by l_n.

### P5. Changing a physical boundary target: B_*, Q_*, (8a), (8b), (8c). HOLDS AFTER CORRECTION.
- M_eta' rdot_B = -d; 2 <= B_* <= 6L (lambda_max <= max row sum <= 1; M >= (min h) I/3); wdot = 1; qdot = 1 + Q_*. Re-derived.
- (8a): sum gammadot_B = (1 + (1 + Q_*))/2 = 1 + Q_*/2, so the coefficient is -(4/(3L))(1 + Q_*/2) a(1-a). HOLDS.
- (8b): sum alpha t_i = b(w - q). With all noncentral t_i shifted by rx, the derivative is (4/(3b) + 2(1-b)/(3b^2)) sum alpha t = 2(1+b)(w-q)/(3b), so the coefficient is 2(1+b) Q_* a(1-a)/(3b). Re-derived, and re-derived again from (9) with kappa = (1-b)/b. HOLDS as algebra.
- Correction (scope of (8b)): the (8b) ray moves every noncentral crossing of an interior horizontal row. It is not an instance of (C), which is defined for one crossing on a complete outward row (lines 32-37). Write: "(8b) is a separate many-crossing odd test; (8c) applies to it by the same disc argument, but it is not a value of O_h in (C)."
- (8c): uniform complex extension (the arcsine series and the same max-norm contraction), analytic odd log vanishing on both axes, Cauchy estimate, coefficients bounded below independently of depth. HOLDS for the stated unshifted reads and filings. As the note says, the lower bound is c|tau x| with tau the imposed difference of prescribed data between the runs. f_A != f_B is not a native adjacent-cutoff pair.

### P6. (8d) for independently moved old data. HOLDS.
||ydot_B|| = 2/(1 + 1/L), ||rdot_B|| <= 6, |L gdot^-_{B,0}| <= 12/24 = 1/2, gdot^+_{B,l} = -1/L, sum gammadot_B = 1 + L gdot^-_{B,0}/2 >= 3/4. Hence |coefficient| >= a(1-a)/L, uniformly in mesh and slab width. Every outward target is identity in both runs (horizontal reflection), and the A row is flat (its odd part is zero by Weyl reflection). HOLDS. What moves is only the old fine data, by -tau/L, between the runs.

### P7. Exact odd part of the transverse Jacobian, (9)-(13). HOLDS.
- Y 75190-75268 read: B(w) dF = H(w) - sum alpha_i H(v_i), with transverse eigenvalue |w|/sin|w| for B and r cot r for H. On a Cartan row this gives the transverse factor sinc(z_0)[k(z_0) - sum alpha k(s_i)] and the axial factor b, so the determinant is b H^2. The increment z on column C (weight b) moves q to q_0 - z, s_i to s_i + (1 + 1_C) z and z_0 to z_0 + z. (9) HOLDS. J_s and (10) HOLD under (C)'s premise that the other factors are even.
- (11): the all-column terms cancel by the symmetry of the multiset and the evenness of k; the residual is the column integral. A symmetric nu gives J = 0. HOLDS.
- (12) under whole-row symmetry with z_0 = 0: re-derived. Guide agreement: 2e-6 relative. Recovering (8), (8a) and (8d) from (12), and (8b) from the kappa form, HOLDS.
- (13): integrate d_z log H over [-rx, rx], Lipschitz in the data. HOLDS for commonly indexed regular rows.

### P8. Averaging the boundary discrepancy, (14)-(15). HOLDS (as a conditional sufficient estimate).
- Q_L Q_D = Q_{LD}: the blocks tile and the segments concatenate. Re-derived. Closed combinations kill vertex gradients, and s_i and z_0 are closed (same endpoints as the corridor). HOLDS in the Cartan chart only, as stated.
- (14): at most D of the D^4 starts use a given link, so the cost is D^-3 eta sum |E| = (eta^4/lambda^3) sum |E|, plus the b^-1 nonpivot term. HOLDS.
- (15): inner layer C(u + eta); shells C[eta^alpha (2^p u)^-alpha + eta]; u = eta^{alpha/(1+alpha)}. HOLDS. The absorption when alpha/(1+alpha) >= theta_2/4 and m_r = 0 HOLDS (n <= j+1, c_2 >= 10 r_pr).
- Sources: Y 133519-133549 read. It proves eps_E(r) <= C(eta^alpha r^{-1-alpha} + eta/r), alpha > 0, for the per-length box coefficient error on complete common rows outside the strip. It does not cover the two native strip reads, as the note says. Y 2159-2169 read ("the new bare boundary layer, where the local scale is eta"). The order-one count eta^4 eta^-3 eta^-1 = O(1) HOLDS. Y 13335-13356, Y 37390-37424 (screening needs distance D >= 2 from changed carriers), O 9927-9985 and Y 10710-10781 (BGD4, TD^-1T = 0) and III 6823-6840 read; they match the note's descriptions. III 7182-7235, II 55882-55946 and III 37547-37560 were taken from checks 1558, 1560 and 1564 and not re-read. The stopping sentence is exact: failure of (14) decides nothing.

### P9. Remaining filings. HOLDS.
- (16): direct substitution re-derived. F(0) = F(1) = 0, F'' = Var <= range^2/4, and the bound t(1-t) range^2/8 + max|d_i| HOLD. The example gives d_i = 0 and D = log(2 sqrt(eps(1-eps))), unbounded. HOLDS. I 156847-156858 and 156907-156921 read (history = "one choice of everything summed over"; real weight on S_omega). The scope limit to stored positive sums by value is correct.
- (17)-(18): the sup bound C eta^2 on the complex ball, the Cauchy estimate along a line segment (uniform in the number of intervals, because the line stays in the sup-norm ball), and the summation by parts of row 1563 (9). HOLD, with every f_i in the half-ball as a stated premise.
- Strip-substitution weight: J_s(+-r) = 1 -+ u_s; odd log -artanh u; even log (1/2) log(1 - u^2); per-bond cost C(1 + a^2)|<v, H_B - H_A>|/delta. HOLDS. Note: this weight is odd, so on any cell where it is filed together with the tested crossing, (C)'s evenness premise fails and this term enters O_h. The note's (C) premise (Jacobian at its boundary address) covers this; no correction needed.

## Native admission and the stopping point

- Diagonal axial representative: a Cartan gauge changes every open angle with fixed endpoints by the same endpoint phase. Target-relative angles and the crossing increment are preserved. HOLDS.
- The simplest A history: with Y empty and the tests passing (strict inequalities, O 17317), P_t = Q_t = empty and Omega_t^c = Q'^~2 u P'^~4 u Yhat^~8 is empty (O 17319-17325 read). R_t enters only Z^[0], not Omega_t. So this start cannot produce the slab. HOLDS.
- The list of what a native disproof needs (aligned label, first index > n_c, varpi <= 1/80; the fresh cell; both runs' xi_a and xi_1 with their tests; both orientations; x shrinking with thresholds; an UPPER control of the whole l_n) is correct. III 12045-12054 read: l_n = [[delta]]^u + [[delta]]^c. The unknown part holds differences of stored terms (S^+[E], S^+[R], boundary loads y_j, y'_j, z^#, b_i; III 11963-12044 read). No summand of l_n is the difference of the runs' assigned fields R_B R_A^-1, so the account read here neither bounds nor exceeds a native tau by l_n.
- What is open, stated exactly: (i) an admitted adjacent-cutoff history realizing a boundary-datum displacement tau (outgoing (8a, 8b) or old (8d)) with |tau x|/l_n unbounded at passing points; (ii) the one-crossing estimate (C) on native reads; (iii) general cut-boundary (S). The three attacks on (C) (stationary transmission, exact Jacobian, L^1 averaging) are distinct, and each failure point is stated exactly. HOLDS.
- Is the surviving stationary mixed term a candidate violation of (S), or bounded by l_n? Answer from this check: (a) at matched determining data and common multipliers, (8) is O(eta^2) and bounded by l_n with ratio C R L^{-2(j+1)+theta_2 n/4}. (b) The depth-uniform terms (8a), (8b) and (8d) are exactly linear in the two-run boundary-datum displacement tau: |O_h| = c_{L,a}|tau x|(1 + O(|tau| + |x|)). They are bounded by l_n if and only if the native tau is O(l_n/|x|) at the passing points. That holds, for example, if R_B R_A^-1 on the boundary and old rows is O(eta^2), as for matched stationary data. Neither the note nor the passages read prove that bound or construct its failure. So the mixed term is a conditional candidate violation: it refutes (S) only together with item (i), and it does not refute (S) as it stands. The note's RESULT is consistent with this.

## Defects (ranked)
1. (8b) is not an instance of (C): it is a many-crossing ray on an interior horizontal row. Correction as in P5.
2. Line 95, last sentence: a reading of III 11866-11886, not a proved statement. Label it as a reading.
No defect breaks a stated result.

## Not checked
III 11811-11835, 11929-11949, 7182-7235; II 55882-55946; III 37547-37560; III 595-601, 1919-1921, 9809-9814, 11578-11586 (taken from checks 1562 and 1564); Y 133450-133497; Y 62370-62401 and O 17521-17526 (from check 1564); the repo-search section (not re-run); the sketched Theorem 1 and the outstanding common-support proposition (status as in their sources).

RESULT: Row 1569 HOLDS AFTER CORRECTION. The prescriptions of the two cutoffs, test (C) (a necessary consequence of (S), not equivalent), the exact stationary solutions (1)-(5) (stationarity checked on all links), (6), (7), (8), (8a), (8c), (8d), the exact Jacobian (9)-(13), the averaging estimates (14)-(15), the matched Cartan slab bound (S) for the stated filings, (16)-(18), the strip-weight formula and the native-admission section HOLD. Corrections: (8b) is a separate many-crossing test, not an instance of (C); line 95's closing sentence is a reading. Stationarity of the outward rows is exact, but their admission is not established. The surviving mixed term is O(eta^2) at matched data and c|tau x| for a two-run boundary-datum displacement tau. It is a candidate violation only if an admitted history makes tau|x|/l_n unbounded, which stays open with (C) and general cut-boundary (S).
Checked line by line by Claude (Opus 5.5).
