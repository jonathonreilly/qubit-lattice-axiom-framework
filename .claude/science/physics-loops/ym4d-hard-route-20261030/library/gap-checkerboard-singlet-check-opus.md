lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1086

# Check of row 1084 (gap-checkerboard-singlet-astra.md), line by line

File under check: `library/gap-checkerboard-singlet-astra.md` (row 1084, written by gpt-6-astra max).
Checker: anthropic/claude-opus-5-5, max effort, laptop subagent. Cross-provider check.

## Plan (eight steps; one step per response; results appended below)

1. Read row 1086 in FINISH.md and the file under check in full; list its claims.
2. Read the context: brief P1 (section 7.3) and section 6.2 of `gap-bridge-vectors-max.md` (row 1076), and the check `gap-bridge-vectors-check-astra.md` (row 1079).
3. Test first, by hand: Lemma DEC (the Haar integral over v_e as a function of rho_x . rho_y), its U(1) analogue, and (DEC3), (DEC5)-(DEC7).
4. Fetch OpenAI's paper (pin of row 1009) and Ding-Huang-Yang arXiv:2611.04908 into new empty folders under /tmp; check the dependency map of step 2 and the exact form of OpenAI Theorem 3.1 used in (DEC4).
5. Check step 4: Lemma STRIP, Theorem A, and which observables are covered.
6. Check steps 5 and 6: P4-NA, P4-SIGN, P4-LIFT, the multi-site singlet example, GH-NA, (GH5)-(GH6).
7. Check step 7: the controls (compact U(1), frozen Q_8 and 2T, PT, SHEET, D2, five dimensions), the marks and the stop claim.
8. Verdict table and the RESULT line.

## Step results

### Step 1 result: row 1086 and the claims under check

Row 1086 (FINISH.md line 1167) asks for a line-by-line check of row 1084's file, test first Lemma DEC by hand and its U(1) analogue, then: the step-2 dependency map against OpenAI and Ding-Huang-Yang (DHY); Lemma DEC and the port of step 3; all torus sizes and the conclusion of step 4; the three failed singlet attempts of step 5; the multi-site example; the positive-beta_L extension of step 6; the controls of step 7. Verdicts HOLDS, HOLDS AFTER CORRECTION, FAILS. No new attack.

The file under check: `library/gap-checkerboard-singlet-astra.md`, 763 lines, 43,954 bytes, mtime 2026-11-16 22:15 local. It says it was written by Codex (GPT-6 Astra, max) from checkout `e7595fa2c78e`. Its own RESULT: (a) PROVED GIVEN OpenAI Theorem 3.1; (b), (c) OPEN; P4-SING-PORT FAILS in three ways; GH-NA at small b.

Claims, numbered for the verdict table:

- C1 (step 1, lines 49-104). Prior-work search; the row 1079 corrections it retains (CB-T, P4-ORB, GH2-0, CB-CH, RIG). Bookkeeping.
- C2 (step 2, lines 106-185). OpenAI map (nine rows, sections 3.1-3.12); Theorem 3.1 states free subgraphs with strengths in [0,b] and tori with both sides at least C Xi(b); p. 29 restricts full-observable mixing to the untwisted zero-field ferromagnet; DHY map (seven rows); the DHY local-time identification of the subdivided grid (lines 178-181).
- C3 (step 3, lines 187-300). Lemma DEC: (DEC1) lift, (DEC2) Haar integral, exact marginal with normalization; the grid embedding and the torus doubling; (DEC3) covariance, Lipschitz, support and distance under the lift; (DEC4) as a consequence of OpenAI Theorem 3.1; (DEC5)-(DEC6) the literal substitution is wrong; (DEC7) coupling derivative and cuts.
- C4 (step 4, lines 302-400). Lemma STRIP (ST1)-(ST3); the threshold switch W = ceil(C Xi(b)) + 4; Theorem A (A); weak limits.
- C5 (step 5, lines 402-606). P4 density; Lemma P4-NA (NA1)-(NA4); Lemma P4-SIGN (SG1)-(SG2) and its open-set extension; Lemma P4-LIFT; the multi-site singlet example; the RIG remark.
- C6 (step 6, lines 608-709). (GH1); Lemma GH-NA (GH2)-(GH4); (GH5)-(GH6) and the plaquette-trace remark.
- C7 (step 7, lines 711-761). Controls table; marks table; consumer and stop; credits.
- C8 (line 763). The RESULT line.

### Step 2 result: the context, and C1

Read: row 1076 (`gap-bridge-vectors-max.md`) lines 224-231 (VB-11), 348-381 (section 6.2), 434-442 (brief P1, section 7.3); row 1079 (`gap-bridge-vectors-check-astra.md`) lines 189-300 (tests 4 and 5) and 454-488 (checkerboard decisions); row 1053 (`gap-wall-vectors-max.md`) lines 247-252 (Lemma RIG statement) and 300-305 (section 6.9).

Facts used below, from those sources:

- GH2_n (Lemma CB-L, row 1076 line 355): density prod_p e^(beta_L x_p(a)) prod_(i,bonds) exp(beta_i Re(Phi_i(u)^(-1) a(u,u') Phi_i(u'))), Haar reference. Local gauge a -> g(u) a g(u')^(-1), Phi_i -> g(u) Phi_i. Far-end rigid groups Phi_i -> Phi_i k_i.
- GH2-0 (line 367-371): at beta_L = 0 and n = 2 the reduced model is an O(4) model in rho = Phi_1^(-1) Phi_2 with bond weight f(t) = omega((beta_1^2 + beta_2^2 + 2 beta_1 beta_2 t)^(1/2)). Row 1079 test 4 checked it (HOLDS, with omega(0) = 1 and the non-mixture claim for c > 0).
- P4 (Lemma CB-T, line 360): exp(sum_i beta_M(l_i) sum_bonds Re(Phi_i(u) Phi_i(u')^(-1)) + beta_T sum_u Re(Phi_1 Phi_2 Phi_3^(-1) Phi_4^(-1))(u)). The corner group (P4-ORB, line 364) is Phi_1 -> g_1 Phi_1 g_2^(-1), Phi_2 -> g_2 Phi_2 g_3^(-1), Phi_3 -> g_4 Phi_3 g_3^(-1), Phi_4 -> g_1 Phi_4 g_4^(-1), with one element per corner for the whole longitudinal plane (frozen planes, line 350). So every sheet bond energy Re(Phi_i(u) Phi_i(u')^(-1)) is corner invariant.
- Brief P1 (line 436): targets (a), (b), (c) exactly as row 1084 quotes them. Inputs: OpenAI section 3, DHY, row 1076 6.2, row 1053 RIG and 6.9.
- Row 1079 test 5 (lines 247-260): OpenAI's twisted bond is Re(q_y U_e q_x^(-1)) with common LEFT rotations; the pin repair conditions on the complement of a union of coarse cells; finite tori keep the requirement that each periodic side is at least C s(b).
- Row 1079 decisions (lines 459-462): CB-T holds after correction (isolated single sheets at free transverse boundaries); P4-ORB holds for one longitudinal site only; CB-CH holds after the conditioning repair, GIVEN (3.61).

**C1 (file lines 49-104). HOLDS as bookkeeping.** The five retained items at lines 90-101 match row 1079 lines 459-462 and test 5, and row 1053 Lemma RIG (twists in G; any G-invariant on-site term) and 6.9 (singlets left open). The target statements at lines 31-37 match brief P1. I did not re-run the repository search of lines 51-85; its scratch files are on the Mac mini and are not in this checkout. That part is not checked.

### Step 3 result: the tests first, by hand (Lemma DEC, its U(1) analogue, DEC3, DEC5-DEC7)

**Test 1: the Haar integral of (DEC2), by hand.** Let w be in R^4. The integral of exp(w . v) over normalized Haar measure on S^3 = SU(2) depends on |w| only, since SO(4) acts transitively on each sphere and keeps Haar measure. Take w = |w| e_0. Under Haar measure, x = Re v has density (2/pi) sqrt(1 - x^2) on [-1, 1] (row 1079, test 4). Poisson's integral I_1(s) = (s/pi) int_{-1}^{1} sqrt(1 - x^2) e^(s x) dx gives

  int_{S^3} e^(w . v) dv = (2/|w|) I_1(|w|) = omega(|w|),  omega(0) = 1.

With w = b(rho + rho'), |w|^2 = b^2 (2 + 2 rho . rho'). So the edge integral is omega(b (2 + 2t)^(1/2)) = omega((2b^2 + 2b^2 t)^(1/2)) = f(t), t = rho . rho'. This is the bond weight of target (a), as a function of rho . rho' only. At t = -1 it is 1. **(DEC2) HOLDS.**

**The marginal (DEC1).** At fixed rho the integrand of (DEC1) is prod_e exp(b v_e . (rho_x + rho_y)). The v_e appear in disjoint factors. Tonelli's theorem (positive continuous integrand on a compact product) gives the rho marginal density prod_e f(rho_x . rho_y) / Z_f, and the two normalizations agree. A self-loop on a period-1 side gives exp(2b rho . v), whose integral is the constant omega(2b) = f(1). Each original edge needs its own v_e; then multi-edges are reproduced edge by edge. **HOLDS.**

**The grid embedding (file lines 216-225).** rho at (2i, 2j), horizontal v at (2i+1, 2j), vertical v at (2i, 2j+1). Each half-edge joins two nearest neighbours of Z^2 and carries b q . q'. Unused odd-odd sites are free Haar spins with no bonds; they are independent and change no marginal. A free subgraph G lifts to a free subgraph of Z^2 inside the doubled box. An n x m torus lifts to Z/2n x Z/2m, with the wrap edge's midpoint at (2n - 1, 2j). **HOLDS.** Whether OpenAI's torus statement needs even sides, and which strengths it allows, is checked against the source in step 4.

**(DEC3).** F-hat(rho, v) = F(rho). Because mu is the rho marginal of mu-hat, every expectation of F, G, FG is the same, so the covariances agree. The lift does not depend on any v_e, so its Lipschitz constant in each v_e is zero and its constants in each rho_x are those of F; ||F-hat||_inf = ||F||_inf. Supports keep their size. The l-infinity distance between (2i, 2j) and (2i', 2j') is 2 max(|i - i'|, |j - j'|), also periodically. **HOLDS**, for any norm of the form sup norm plus per-site Lipschitz constants; the exact norm of OpenAI Theorem 3.1 is checked in step 4.

**Test 2: the U(1) analogue of DEC, by hand.** For spins in S^1, int_{S^1} e^(w . v) dv/(2 pi) = I_0(|w|). With w = b(rho + rho') and relative angle delta, |w| = 2b |cos(delta/2)|. So the U(1) version of DEC holds exactly: the circle model with bond weight I_0(2b |cos(delta/2)|) is the marginal of an XY model with strengths b on the same subdivided grid. This is the weight that row 1076 line 379 names. DEC itself makes no claim about decay. It transfers decay in both directions for functions of rho, because the covariances are equal. So the U(1) analogue gives the U(1) model a gap only through an exponential-mixing theorem for the two-dimensional XY model at large b, and no such theorem is available. Fröhlich and Spencer proved power-law lower bounds for the standard XY and Villain models at large coupling. I did not check that their proof covers this decorated graph; row 1076 marks the massless behaviour of this reduced model as belief. So the place where the U(1) analogue stops is the input theorem, not DEC. This agrees with the file's U(1) control row (line 715). What that row says about OpenAI (3.28) and (3.43) is checked against the source in step 4.

**(DEC5).** Put q_x^(-1) q_y = t + s (t real, s imaginary) and rotate q_y -> q_y e^(delta a), a a unit imaginary. Then Re((t + s)(cos delta + a sin delta)) = t cos delta - (s . a) sin delta. The first derivative of -V at delta = 0 is V'(t)(s . a), and the second is V'(t) t - V''(t)(s . a)^2. For V(t) = b t this is b t, the contact term w_e t_e. The file writes the second derivative times delta^2 (no factor 1/2); that is a notation choice and changes nothing. **HOLDS.**

**(DEC6).** From the series omega(s) = sum_k (s^2/4)^k / (k! (k+1)!) and s^2/4 = b^2 (1 + t)/2:
f_b(t) = 1 + (b^2/4) u + (b^4/48) u^2 + O(u^3), u = 1 + t. So f(-1) = 1, f'(-1) = b^2/4, f''(-1) = b^4/24, and V''(-1) = b^4/24 - b^4/16 = -b^4/48. **HOLDS.** "By continuity" (line 274): V'' is continuous and negative on [-1, -1 + eta); for t > -1 there, |s|^2 = 1 - t^2 > 0, and a parallel to s makes V''(t)(s . a)^2 nonzero. **HOLDS.** The two-circle remark (lines 276-280) **HOLDS**: q_x . q_y = c_x c_y cos(theta_e) + s_x s_y cos(psi_e), and f(A + B) does not split as g(A) h(B), since d_A d_B log f(A + B) = V''(A + B) is not identically zero. On the lift every bond is exponential, so the two circle systems are independent given all amplitudes, auxiliary ones included.

**(DEC7).** int exp(v . (b_1 rho + b_2 rho')) dv = omega(|b_1 rho + b_2 rho'|) = omega((b_1^2 + b_2^2 + 2 b_1 b_2 t)^(1/2)). Differentiation under the integral (smooth integrand, compact domain) gives d_(b_1) log f = E[rho . v | rho, rho']. One cut gives omega(b_2), both cuts give omega(0) = 1. **HOLDS.**

**GUIDE run (not a proof; a different data path).** `guide_dec_na.py`, log `guide_dec_na.log`, both in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/row1086-scripts/`; numpy, BLAS threads 1, one job, under a minute. Monte Carlo over 4 x 10^6 Haar points matches (DEC2) to the sampling error at b = 0.5, 2, 2.5 (for example 3.66019 against 3.65727 at b = 2.5). A 2 x 10^5-point circle quadrature matches the U(1) analogue to eight digits. Finite differences give V''(-1 + 0.002) = -0.005001 (b = 0.7) and -0.33267 (b = 2), against -b^4/48 = -0.005002 and -0.33333.

**Checker's remark on scope (hand identity; not a verdict on the file).** GH2_2 at beta_L = 0 in unitary gauge is the lift (DEC1) itself. With a' = Phi_1(u)^(-1) a Phi_1(u') and rho = Phi_1^(-1) Phi_2, the Higgs exponent of one edge is b <a', 1 + rho(u) rho(u')^(-1)>. Put v_e = a'_e rho(u'), a Haar-preserving change at fixed rho. Right multiplication by rho(u') is an isometry, so the exponent is b v_e . (rho(u) + rho(u')), which is (DEC1). Phi_1 is then independent Haar. So the import of step 4 would also cover the gauge-invariant Lipschitz local observables of GH2_2 at beta_L = 0 that involve links (for example plaquette traces and Higgs-link energies), not only functions of rho. The file claims only functions of rho, which is what target (a) asks for.

### Step 4 result: the primary sources; C2 and (DEC4)

**Copies.** OpenAI, *Sharp mass bounds for the two-dimensional O(4) model*, at the pin of row 1009 (commit `4eaee87548250b2682affda7d05d947c05554bae`, the same pin as the file), fetched into the new empty folder `/tmp/row1086-o4.W1Wxh0/` (961,282 bytes, 102 pages). Jian Ding, Fenglin Huang and Peng Yang, arXiv:2611.04908v1, fetched into the new empty folder `/tmp/row1086-dhy.fZaG6U/` (864,742 bytes, 74 pages). Both SHA-256 values equal the ones in the file (lines 126 and 132). Text was extracted by pypdf under `python3 -I`; the extraction script is in my scratch `row1086-scripts/`, apart from the downloads. Nothing is copied into the checkout. Read: OpenAI pp. 12-33 (section 3 in full, the stiffness induction of pp. 16-25 at the level of its equations and their stated hypotheses); DHY pp. 1-5, 7, 18-20, 29-31 and the statements on pp. 33 and 39-40.

**OpenAI Theorem 3.1 (p. 12), as stated.** Spins in S^3 with normalized Haar measure; density proportional to exp(sum_e beta_e q_x . q_y) on a finite graph in the square lattice, each unoriented edge once; a free subgraph has the other bonds absent and no pins. L_F = ||F||_inf + max_(x in A) Lip_x(F), round distance on S^3, other spins fixed; distances in the maximum norm, periodic on a torus. With Xi(beta) as in (3.1): on every unpinned rectangular torus with each side at least C Xi(beta) and all 0 <= beta_e <= beta, |Cov(F, G)| <= C (1 + beta + |A| + |A'| + d)^20 L_F L_G e^(-c d / Xi(beta)); the same on every unpinned free subgraph with ambient distance. (3.67) on p. 32 repeats this for all couplings in [0, b], intermediate weakenings included.

**(DEC4). HOLDS GIVEN OpenAI Theorem 3.1.** The lift is a density of exactly this form on a subgraph of Z^2, with beta_e in {0, b}: on a free subgraph it is a free subgraph; on a torus it is the 2n x 2m torus. The norm L_F is the one in (DEC3). With d replaced by 2d, (3.2) gives (DEC4) with the same absolute C, c. The torus clause needs both lifted sides 2n, 2m >= C Xi(b), as the file says.

**C2, the OpenAI map (file lines 144-164). HOLDS AFTER CORRECTION (one wording point; nothing load-bearing).** I located every cited place and compared it with the row:
- (3.4)-(3.8), pp. 13-14: bond t_e + s_e = q_y U_e q_x^(-1), signed |b_e| <= b, half weights on tangent edges, H_Q <= bI (3.5), the left-rotation derivatives (3.6), the bracket (3.7), the Ward identity (3.8). Matches row 1.
- (3.11)-(3.12), (3.13)-(3.16), (3.19), (3.28), (3.43) (whose second formula uses the factor two of (3.28)), (3.50), (3.53)-(3.54) (uniform over the signed, twisted, pinned class, from H_1 <= bI). Match rows 2-5.
- (3.55)-(3.62), pp. 25-29: fixed right twists keep common left rotations (p. 27); (3.61) on p. 28; on p. 29, free subgraphs by zero padding and periodic sides at least C s. Matches row 6.
- p. 29, section 3.11: the restriction to the untwisted zero-field ferromagnet with 0 <= b_e <= b, called essential. Matches line 160.
- (3.63), p. 29: the covariance inequality for associated variables, a double sum of products of individual Lipschitz constants times Cov(X_i, X_j). The two-replica Ginibre step with weight exp(sum 2 J_e cos phi_e cos psi_e), and FK with p_e = 1 - e^(-2 J_e). Matches row 7.
- Sections 3.11.2-3.11.3, pp. 30-31: the XY sign split; q = (cos alpha z, sin alpha w); couplings b_e cos alpha_x cos alpha_y and b_e sin alpha_x sin alpha_y; the alpha marginal associated in the order "alpha increasing at every site"; both cuts keep the full amplitude marginal fixed. Matches rows 8-9.
- (3.69)-(3.70) and section 3.12.2, pp. 32-33: matches rows 10-11. The file is right that (3.70) and the homogeneous statements are not needed for (a).

Correction: line 222-223 says the doubling meets "the source's even-period requirement". Bound (3.2) has no parity condition. Even sides appear only in (3.3) and in the reflection-positivity part of section 3.12.2-3.12.3, which (a) does not use. Replace by: "Bound (3.2) needs no parity; the doubled torus is even in any case." Nothing else changes.

**C2, the DHY map (file lines 166-185). HOLDS at the level checked.** (1.9) on p. 4 is the XY projection with couplings beta r_u r_v. (2.2)-(2.3) on p. 7 have coupling 2 J_uv (beta_u beta_v)^(1/2) with max J_e <= 1. So local time b/2 on used sites, 0 on unused sites, and J = 1 give coupling b on every half-edge and 0 elsewhere. Every Z^2 edge between two used sites of the doubled grid is a half-edge: two retained sites are never adjacent, two midpoints are never adjacent, and each odd-odd site is unused. So lines 178-181 hold. Lemma 2.10 (p. 18) and (2.41) (p. 19): the Ginibre step for Hamiltonians -sum t_alpha cos(alpha . theta) with t_alpha >= 0 and alpha integer vectors; a positive four-angle cosine is in that class (used at file line 552). Theorem 3.6 (p. 29) is association in the copywise order, and Remark 3.7 (p. 30) conditions the other copies. Remark 1.2 allows site strengths 0 <= J_u <= 1. For 2 < N <= 3 the last copy has intensity proportional to c = N + 1 - ceil(N) = N - 2, which is zero at N = 2 (p. 7 and the abstract). Not checked line by line: the contents of (2.11), (2.22)-(2.30), Theorem 4.2 and the section 5 formulas of file line 175 (I checked only their locations). The file does not use DHY for (a), so these rows are not load-bearing.

### Step 5 result: C4 (Lemma STRIP, Theorem A, the covered observables)

**Why STRIP is needed (lines 304-306). HOLDS.** Theorem 3.1 covers a torus only when each side is at least C Xi(b). A torus with one short side and one long side is not covered, and its diameter is not bounded. So a separate argument is needed, as the file says.

**(ST1). HOLDS.** Between consecutive columns there are at most w bonds, each with |b_e q . q'| <= b. So K_j lies in [e^(-bw), e^(bw)]. Within-column factors, the wrap bond of the short cycle included, are bounded positive functions and go into nu_j.

**(ST2). HOLDS.** Given the two end columns of an interval, the inner columns form a Markov chain (the density is a product of nearest-column factors). Its transition is K_j(X, Y) h(Y) nu(dY) / int K_j(X, Z) h(Z) nu(dZ), with h the continuous positive right message. The lower bound K >= e^(-bw) in the numerator and the upper bound K <= e^(bw) in the denominator give P_j(X, .) >= e^(-2bw) Q_j with Q_j = h nu / int h nu, which does not depend on X. Since w <= W, epsilon = e^(-2bW) works.

**The coupling. HOLDS.** Two chains with the same right end use the same P_j. Each step draws from the common part epsilon Q_j with probability at least epsilon and then agrees forever. So after k steps they differ with probability at most q^k, q = 1 - epsilon. The bridge is a Markov chain in both directions, so the right end is treated by the reversed chain. Two changes add by the triangle inequality for total variation. If |J| = 1, the single arc has both ends at the same column; the two-stage change (left end, then right end) still applies, since the arc law with two different end values is well defined.

**(ST3). HOLDS.** Given X_J the arcs are independent. In an arc the leftmost and rightmost required I columns are at least D steps from the ends, so one arc contributes at most q^D + q^D to the probability of a disagreement on its I columns. With at most |I| arcs, |E[F | X_J] - E[F | X'_J]| <= 2 ||F||_inf . 2 |I| q^D. Then Cov(F, G) = E[(E[F | X_J] - E F) G] gives (ST3). If G is constant the covariance is 0.

**The case split (lines 360-365). HOLDS.** If d > W, the short periodic distance is at most floor(w/2) <= W/2 < d, so the long distance of every pair is at least d; hence D >= d and I, J are disjoint. If d <= W, |Cov| <= 2 ||F|| ||G|| <= 2 q^(-W) ||F|| ||G|| q^d. Together: |Cov| <= 4 q^(-W) ||F||_inf ||G||_inf max(|A|, 1) q^d for all d. Parallel edges or self-loops on very small tori only change the bound K_j to e^(+-2bw), so the remark of lines 370-371 holds with that constant.

**The threshold switch (lines 367-372). HOLDS.** If a lifted side is below C Xi(b) it is at most W = ceil(C Xi(b)) + 4, and STRIP applies to the lifted torus at lifted distance 2d. If both lifted sides are at least C Xi(b), (DEC4) applies.

**Theorem A. HOLDS GIVEN OpenAI Theorem 3.1.** (1 + b + |A| + |A'| + 2d) <= (1 + b)(1 + |A| + |A'|)(1 + 2d), and sup_d (1 + 2d)^20 e^(-c d / Xi(b)) is finite. So (DEC4) gives (A) with rate c/Xi(b). STRIP gives (A) with rate -2 log q, since L_F >= ||F||_inf and |A| <= (1 + |A| + |A'|)^20. Take m_b the smaller rate. Weak limits: F, G, FG are continuous on finite compact products, so (A) passes to every local weak limit of free or periodic measures. Lean: Tonelli, a graph embedding, a Doeblin coupling and elementary limits; nothing computer-assisted.

**Scope remark (an addition, not a correction).** The uniform rate m_b is the thin-torus rate. It is -2 log(1 - e^(-2bW)), about 2 e^(-2bW) with W of order C Xi(b), so it is doubly exponentially small in b. On free subgraphs and on tori with both lifted sides at least C Xi(b), the rate is c/Xi(b) from (DEC4). The file does not claim any rate, so this changes no verdict.

**Which observables are covered.** All local functions of finitely many rho spins with finite L_F = ||F||_inf + max_x Lip_x(F) (round metric). That includes every function invariant under the global O(4) action, such as the bond energies rho_x . rho_y, so (A) is more than the spin two-point corollary (line 251-252 HOLDS). Bounded measurable observables that are not Lipschitz are not covered with these constants. In GH2_2 at beta_L = 0, the lift is the unitary-gauge law (the remark of step 3), so the same import also reaches the Lipschitz gauge-invariant observables that involve links; the file does not claim this.

**Answer to row 1086's question for step 4.** Yes: a mixing estimate for the subdivided O(4) model at coupling b (OpenAI Theorem 3.1, applied with strengths in {0, b}) gives Lipschitz-observable decay for (GH2_2) at beta_L = 0. On free subgraphs and large tori the constants are those of (3.2), with d replaced by 2d. On all tori they are C_b, m_b as above. The covered observables are the local Lipschitz functions of rho.

### Step 6 result: C5 (step 5 of the file) and C6 (step 6 of the file)

**The P4 density (lines 404-417). HOLDS.** It is Lemma CB-T's density with beta_M(l_i) = b on all four sheets and beta_T = kappa. A single longitudinal site keeps only the on-site factor exp(kappa Re H).

**Lemma P4-NA. HOLDS.** Checked by hand:
- y(q) = e . R(q)e with e = i equals q_0^2 + q_1^2 - q_2^2 - q_3^2 = cos(2 alpha) in OpenAI's splitting q = (cos alpha z, sin alpha w). Also y(q^(-1)) = y(q), since R(q^(-1)) = R(q)^T.
- Integrating any one q_i: int exp(kappa Re(q_1 g)) dq_1 = omega(kappa |g|) = omega(kappa). So any three of the q_i are iid Haar. Hence all proper sub-products of the y_i have mean 0, and the alpha_i are pairwise (indeed three-wise) independent.
- (NA2): y(g^(-1) h) = <R(g)e, R(h)e>, and for u = R(g)e uniform on S^2, E[u_a u_b] = delta_ab/3. So y * y = y/3.
- (NA1): E[y_1 y_2 y_3 y_4] = (1/27) int y(h) e^(kappa Re h) dh / omega(kappa). The averaged rotation int R(h) e^(kappa Re h) dh commutes with every R(g), so it is lambda I_3. With the spin-one character chi_1(theta) = sin 3theta / sin theta and dh = (2/pi) sin^2 theta dtheta: 3 lambda = (1/pi) int_0^pi (cos 2theta - cos 4theta) e^(kappa cos theta) dtheta = I_2 - I_4 = (6/kappa) I_3. Also omega(kappa) = I_0 - I_2 = (2/kappa) I_1. So M_kappa = I_3(kappa) / (27 I_1(kappa)), positive for kappa > 0 by the series of I_3.
- (NA3)-(NA4): the partial derivatives 1 - y_2, 1 - y_1, 1 + y_4, 1 + y_3 are nonnegative on [-1, 1]; E F = E G = 0; in E[FG] only -y_1 y_2 y_3 y_4 survives. So Cov(F, G) = -M_kappa < 0.
- The alpha order and (3.63): y is decreasing in alpha, so -F, -G are increasing in alpha with the same covariance. (3.63) (p. 29) bounds |Cov| by a double sum of Lipschitz constants times Cov(alpha_i, alpha_j) over i in {1, 2}, j in {3, 4}; each such covariance is 0. So (3.63) fails, and the alpha law is not associated.
- Robustness (checker's addition): every coordinatewise reversal of the order also fails. With an even number of reversed coordinates, E[prod of the reversed y_i] = M_kappa and (NA3) works unchanged. With an odd number it is -M_kappa, and F = y'_1 + y'_2 + y'_1 y'_2, G = y'_3 + y'_4 + y'_3 y'_4 give Cov = -M_kappa.
- Scope (lines 504-508) is stated correctly: the test functions are not corner singlets, and a same-site covariance is not a failure of spatial mixing.
- Not checked: the cross-reference to Sussman-Alpoge GL3 (outline 2210-2231) at line 475. The outline is not in this checkout. (NA1) does not need it.
- GUIDE (step 3 script): Monte Carlo E[y_1 y_2 y_3 y_4] = 0.00144, 0.00491, 0.01258 against I_3/(27 I_1) = 0.00145, 0.00495, 0.01266 at kappa = 1, 2, 4. The sign of Cov(F, G) is negative in all three, with magnitude matching up to sampling error.

**Lemma P4-SIGN. HOLDS.** Haar is invariant under q -> -q, so tau = sign(Re q) is a fair sign independent of v = tau q. Real signs are central, so the on-site term equals tau_1 tau_2 tau_3 tau_4 Re(v_1 v_2 v_3^(-1) v_4^(-1)). This gives (SG1) with normalization 8e^J + 8e^(-J) = 16 cosh J. At tau_3 = 1, tau_4 = -1 the pair weight is e^(-J tau_1 tau_2), and the ratio is e^(-4J) < 1, which is (SG2). E[tau_1 tau_2 tau_3 tau_4 | v] = tanh J; every proper sub-product has mean 0 (flip one sign inside it and one outside it). So the (NA3) covariance is -tanh J. The open-set version (lines 539-548): Haar is invariant under the reflection q_0 -> -q_0, so the scalar signs are uniform given the magnitudes and the imaginary signs. At magnitudes (1, 0, 0, 0) the weight is exp(kappa sigma_1 sigma_2 sigma_3 sigma_4), and continuity keeps the ratio below 1 on an open set. Conditioning on some coordinates preserves the FKG lattice condition. So this failure also refutes the lattice condition for the full sign system of the natural extension of OpenAI section 3.11.2 to P4. A four-body term J sigma_1 sigma_2 sigma_3 sigma_4 fails the lattice condition under every coordinatewise flip, since some conditioning on (sigma_3, sigma_4) always makes the pair antiferromagnetic. The scope sentence (lines 550-554) is correct: (2.41) of DHY allows positive multi-angle cosines.

**Lemma P4-LIFT. HOLDS.** If each bond weight is a function of q_x . q_y and the auxiliary reference is Haar, then rotating all spins by one O ∈ O(4) keeps the weight and the reference. So the terminal marginal is invariant under a common rotation. j^(-1) = -j, k^(-1) = -k, and 1 . i . (-j)(-k) = ijk = -1. Left multiplication by i gives (i, -1, k, -j), and i(-1)(-k)(j) = ikj = 1. The continuous densities differ by e^(2 kappa). GUIDE: the script prints -1.0 and 1.0. The argument covers any real strengths and any O(4)-invariant pair weights, so the stated scope (untwisted, same terminals, Haar auxiliaries) is if anything narrower than what is proved. The non-claims of lines 585-588 are correct.

**The multi-site example (lines 590-597). HOLDS.** The corner group of P4-ORB uses one element per corner for the whole longitudinal plane. So Re(q_1(u) q_1(v)^(-1)) -> Re(g_1 q_1(u) g_2^(-1) g_2 q_1(v)^(-1) g_1^(-1)) is invariant. With q_1 = q_4 = a(u) and q_2 = q_3 = 1, every x_p(u) = Re(a a^(-1)) = 1, while Re(a(u) a(v)^(-1)) varies. So the multi-site singlet algebra is not generated by the x_p field, as row 1079 says.

**The RIG remark and the stop claim (lines 599-606). HOLDS.** It agrees with row 1053 (twists in G only; section 6.9 leaves the singlets open). The three failures are at three distinct written places ((NA4), (SG2), the common-rotation contradiction), each with a counterexample. That meets the stop rule of row 1084 as written. The file does not claim that P4-SING-PORT or P4-MIX is false.

**(GH1) and the beta_L = 0 remark (lines 610-624). HOLDS.** (GH1) is Lemma CB-L's GH2_n with beta_i = b. At beta_L > 0 the plaquette factor couples the four links of a face, so edgewise integration no longer factorizes.

**Lemma GH-NA. HOLDS.** The gauge change g(u) = Phi_1(u)^(-1) is Haar-preserving and makes the density free of Phi_1. At b = 0 the four links have the law exp(kappa Re(a'_12 a'_23 a'_34 a'_41)), which is the one-site P4 law after inverting two links; y(a^(-1)) = y(a), so (GH2) follows from (NA1)-(NA4). |S| <= 4n. Because e^(-Mb) <= e^(bS), E_0 e^(bS) <= e^(Mb), the density ratio lies in [e^(-2Mb), e^(2Mb)], so |ratio - 1| <= e^(2Mb) - 1 pointwise. With ||F||, ||G|| <= 3, |E_b[FG] - E_0[FG]| <= 9 eps and |E_b F E_b G| <= 9 eps^2, which is (GH3). (GH4) gives eps <= delta/36, so 9 eps + 9 eps^2 <= delta/4 + delta^2/144 < delta/2 (delta <= 1/27, since |y| <= 1 in (NA1)). Hence Cov_b(F, G) < -delta/2. Non-association of the link amplitudes implies non-association of any larger amplitude vector that contains them. The scope (unitary gauge, one plaquette, b below (GH4); nothing at the window, no refutation of GH2-MIX) is stated correctly.

**(GH5)-(GH6). HOLDS.** Given a, the species are independent twisted sheets with partition functions Z_i(a), so the a-marginal is (GH5). (GH6) is the law of total covariance. For two plaquette traces the conditional covariance is 0, so the whole covariance sits in the annealed gauge term, which the charged estimate does not reach.

### Step 7 result: C7 (controls, marks, stop, credits) and C8 (the RESULT line)

Read for the controls: Lemma PT in `gap-crux-exercise3-max.md` lines 690-723 (row 998); Lemma SHEET in `gap-sepinput-check-astra.md` lines 162-214; the D2 check in `gap-tiltproof-check-astra.md` lines 63-80 and 150-168 (the rest of that range was not read).

**Compact U(1) (line 715). HOLDS.** The U(1) analogue of DEC is exact (step 3: weight I_0(2b |cos(delta/2)|), lift an XY model on the doubled grid). OpenAI Theorem 3.1 is stated for S^3 only. The places named in the OpenAI argument are correct: in (3.28), F' = -a x F is the bracket term, which is zero for an abelian group, and the second formula of (3.43) uses the factor two of (3.28). In DHY the extra copy has intensity proportional to N - 2, which is zero at N = 2. So the U(1) analogue does not give the U(1) model a gap; the step that stops is the input mixing theorem, as row 1086 asked. The phrase "neither method proves false all-temperature XY mixing" is correctly worded: it says the methods do not prove it, not that XY mixing is refuted by them.

**Frozen Q_8 and 2T (line 716). HOLDS.** For a finite subgroup Gamma of SU(2) with counting measure, sum over v in Gamma of exp(b v . (rho + rho')) equals g(rho^(-1) rho') after v = rho w, and g is a class function on Gamma; so the auxiliary identity exists as the file says. The input fails: Haar integration by parts in (3.8) needs infinitesimal rotations, which do not act on Gamma. STRIP's rate tends to 0 as W grows, so STRIP does not conflict with ordered sheets in two dimensions.

**Lemma PT (line 717). HOLDS.** PT (row 998) says a tool that reads only one factor of a product with a massless U(1) factor cannot imply the seed. Theorem A reads the whole rho law through an exact marginal and claims nothing for a product with an extra factor.

**Lemma SHEET (line 718). HOLDS.** The corrected SHEET lower bound uses plaquette couplings B tending to infinity on side faces in four dimensions, and a supremum over coupling fields. (A) is at one fixed b with pair bonds in [0, b], with no supremum.

**Theorem D2 (line 719). HOLDS.** (A) is stated on unpinned free subgraphs and tori only. The pins inside the argument are OpenAI's own cell-boundary pins (inside the black box) and STRIP's conditioning on columns of the same measure, which is not an external pin. No gauge pin geometry enters.

**Five dimensions (line 720). HOLDS.** It agrees with row 1076's T4: the models are the same in the split 2 + 3, and no binding test is claimed.

**Marks table (lines 726-732). HOLDS.** Each PROVED item was checked here and holds (steps 3, 5, 6). The PROVED GIVEN and ARGUED items are scoped as the sources allow. "Not independently checked" is now out of date for the hand lemmas; this check is the cross-provider check of them.

**Consumer and stop (lines 734-740). HOLDS.** (a) does not reach n = 4: the unitary-gauge link exponent for n = 4 is <a', sum_i rho_i(u) rho_i(u')^(-1)>, which is not a sum of single-site terms, so the n = 2 rewriting of step 3 has no n = 4 analogue in this form. The stop rule is met as written. No counterexample to P4-MIX or GH2-MIX is claimed, and none is implied.

**Credits (lines 742-752). HOLDS.** OpenAI; Jian Ding, Fenglin Huang and Peng Yang; Jean Ginibre; Ethan Sussman and Levent Alpoge; Balaban: all named, as row 1084 asks. Cosmetic: the file's first heading is "# Repo search", not a title. Suggest "# Row 1084: checkerboard singlet (gap-checkerboard-singlet-astra)".

**C8, the RESULT line (line 763). HOLDS AFTER CORRECTION (scope wording only).** "P4-SING-PORT FAILS in three specified ways" can be read as "the supplier is false", which line 421-422 of the file denies. Corrected text:

> RESULT: (a) PROVED GIVEN OpenAI Theorem 3.1 by an exact subdivided-lattice O(4) marginal, including thin tori; (b) and (c) OPEN; three specified ports of the singlet step to P4 FAIL (amplitude association, conditional ferromagnetic signs, same-terminal O(4) auxiliary network), each with an exact hand counterexample, and the association failure extends to GH2 at small positive b and fixed beta_L > 0; P4-SING-PORT itself and P4-MIX remain OPEN; research only, no status or Yang–Mills mass gap claimed.

### Step 8 result: verdict table

| Item (file lines) | Verdict | Note |
|---|---|---|
| C1 prior work, retained corrections (49-104) | HOLDS (bookkeeping) | The repository search itself was not re-run. |
| C2 OpenAI map (144-164) | HOLDS AFTER CORRECTION | Every cited place found and matched. Correction at 222-223: "Bound (3.2) needs no parity; the doubled torus is even in any case." |
| C2 DHY map and local-time identification (166-185) | HOLDS at the checked places | (2.2) coupling 2 J (beta_u beta_v)^(1/2); site strengths b/2 and 0, J = 1. The section 5 formulas, (2.11), (2.22)-(2.30) and Theorem 4.2 were checked for location only; not load-bearing. |
| Lemma DEC: (DEC1), (DEC2), embedding, (DEC3) (189-252) | HOLDS | Haar integral by hand: omega(b (2 + 2t)^(1/2)), a function of t = rho . rho' only; normalization exact. |
| (DEC4) (242-249) | HOLDS GIVEN OpenAI Theorem 3.1 | Same C, c; d -> 2d; both lifted torus sides at least C Xi(b). |
| (DEC5)-(DEC7), two-circle remark (254-300) | HOLDS | V''(-1) = -b^4/48. |
| U(1) analogue of DEC (test of row 1086) | DEC holds for U(1); the input theorem is what stops | Weight I_0(2b |cos(delta/2)|); no XY mixing theorem; the (3.28) bracket and the DHY N - 2 copy vanish. |
| Lemma STRIP (308-372) | HOLDS | Doeblin coupling with epsilon = e^(-2bW). |
| Theorem A (374-400) | HOLDS GIVEN OpenAI Theorem 3.1 | Uniform rate is the thin-torus rate, doubly exponentially small in b; c/Xi(b) on free subgraphs and large tori. Covers local Lipschitz functions of rho. |
| P4 density and kappa = 0 remark (404-417) | HOLDS | |
| Lemma P4-NA (426-508) | HOLDS | (NA1) by the spin-one character; robust to every coordinatewise order reversal. |
| Lemma P4-SIGN (512-554) | HOLDS | Also refutes the lattice condition for the full sign system of the natural extension of section 3.11.2. |
| Lemma P4-LIFT (558-588) | HOLDS | The proof covers any O(4)-invariant pair weights. |
| Multi-site singlet example (590-597) | HOLDS | Corner group is global along the plane. |
| RIG remark and stop at P4-SING-PORT (599-606) | HOLDS | |
| (GH1), Lemma GH-NA, (GH5)-(GH6) (610-709) | HOLDS | Threshold (GH4) checked. |
| Controls U(1), Q_8 and 2T, PT, SHEET, D2, 5D (711-724) | HOLDS | |
| Marks, consumer, stop, credits (726-761) | HOLDS | Cosmetic: the first heading "# Repo search" is not a title. |
| RESULT line (763) | HOLDS AFTER CORRECTION | Corrected text in step 7: three ports FAIL; P4-SING-PORT itself and P4-MIX stay OPEN. |

No line of row 1084 FAILS in this check.

**Not checked here.** The repository search of lines 51-85 (its files are on the Mac mini); the Sussman-Alpoge outline and CA-I readings of lines 108-119 and the GL3 cross-reference of line 475 (the outline is not in this checkout; (NA1) does not depend on it); the DHY contents named above; the D2 check lines 81-149; the internal proof of OpenAI Theorem 3.1 (imported, unrefereed, ARGUED). Whether Fröhlich and Spencer's power-law bound covers the decorated XY graph of the U(1) analogue was not checked; nothing here depends on it.

**Provenance.** Checker: anthropic/claude-opus-5-5, max effort, laptop subagent of the lead session. The file under check was written by gpt-6-astra max (row 1084). This is a different provider and a different derivation for DEC, (NA1) and STRIP. The GUIDE run is a third data path (Monte Carlo and quadrature) for DEC2, its U(1) analogue, DEC6, NA1 and P4-LIFT. It is not a proof. No file other than this one was edited. Nothing was committed or pushed.

Credits: OpenAI (the O(4) paper and its Theorem 3.1); Jian Ding, Fenglin Huang and Peng Yang (arXiv:2611.04908); Jean Ginibre (the cosine-character inequality); Fortuin and Kasteleyn (the random-cluster form used in OpenAI section 3.11.1); Ethan Sussman and Levent Alpoge (the account behind the lane); Balaban (the constructive context); Fröhlich and Spencer (the XY power-law bound named in the U(1) control).

RESULT: Row 1086 (Claude Opus 5.5 max, cross-provider check of row 1084): no line FAILS. Lemma DEC HOLDS: by hand, the Haar integral over v_e of exp(b v_e . (rho_x + rho_y)) is omega(b (2 + 2 rho_x . rho_y)^(1/2)), so the marginal is exactly (GH2_2) at beta_L = 0. (DEC4) and Theorem A HOLD GIVEN OpenAI Theorem 3.1 (statement read at the row 1009 pin), on free subgraphs and all tori; STRIP HOLDS for thin tori, at a rate doubly exponentially small in b. The covered observables are the local Lipschitz functions of rho. The U(1) analogue of DEC is exact and stops at the input theorem (the bracket of OpenAI (3.28) and DHY's N - 2 copy vanish), not at DEC. P4-NA, P4-SIGN, P4-LIFT, the multi-site singlet example, GH-NA and (GH5)-(GH6) HOLD. The OpenAI and DHY maps HOLD at the checked places, with two wording corrections: bound (3.2) has no even-period requirement; and in the RESULT line, three ports FAIL while P4-SING-PORT and P4-MIX stay OPEN. (b) and (c) remain OPEN; no mass gap is claimed.
