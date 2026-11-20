lead: anthropic/claude-opus-5-5/max laptop-subagent

# FINISH row 1307: line-by-line check of `library/gap-solve34-astra62.md` (row 1298)

Checker: Claude Opus 5.5, max effort, laptop subagent. Checked by hand.
Target author: gpt-6.2-astra max (row 1298). Status before this check: unchecked.

## Plan (at most eight steps; one step per response, result appended below)

1. Read the target file in full. List every PROVED statement with line numbers and every cited earlier row.
2. Check positive claim 1: the stationary resampling (29)-(31) of a positive density of links, with uniform control on every normalized physical slow state.
3. Check positive claim 2: the physical-scale estimates (34) and (37), which would exclude the remaining collective states.
4. Read each cited earlier row (statement, and proof where a step depends on it). Check the dependent steps.
5. Check every remaining statement in the file.
6. Restatement search: FINISH RESULT lines, the `library/gap-solve*-astra62.md` files and their checks. Say whether the main comparison restates an earlier row.
7. Optional numeric guide (under 1 GB, BLAS threads 1, outside the repository, `python3 -E -P`). Guide only.
8. Counts, per-statement verdicts, what was not checked, RESULT line.

## Step results

(appended below as each step finishes)

### Step 1. Inventory (done)

Target read in full: 483 lines, clone at `92083e673` on `claude/ym4d-hard-route`.
Labels: 59 PROVED blocks, 6 OPEN, 7 GUIDE, 37 tagged equations (1)-(37), final RESULT line 483 (OPEN).

PROVED blocks by line: 3, 15, 23, 29, 48, 62, 72, 79, 87, 89, 96, 104, 118, 125, 132, 139, 141, 146, 157, 164, 177, 183, 196, 207, 209, 211, 218, 226, 234, 243, 255, 266, 273, 284, 291, 297, 312, 316, 323, 332, 334, 343, 355, 366, 372, 380, 389, 397, 404, 406, 413, 421, 429, 447, 449, 458, 461, 470, 479.

Cited earlier rows and files: row 1236 (11) `gap-solve27-astra62.md`; row 1290 (3), (11) `gap-solve33-astra62.md`; row 944 Lemmas TG, EF `gap-sgstep-opus.md`; row 1167 (11) `gap-solve12-astra62.md`; row 1169 (15)-(18), (21) `gap-solve13-astra62.md`; row 1155 (9) `gap-solve7-astra62.md`; row 1149 (16) `gap-solve4-astra62.md`; row 1215 `gap-solve23-astra62.md`; row 1145 `gap-solve2-astra62.md`; row 1218 `prior/gap-onebound-read-sol.md`; `gap-avgcurv-max.md`.

### Step 2. Positive claim 1: stationary resampling (29)-(31) (done)

Dependencies checked first.

- Line 21 (setup, GUIDE). Checked: the kernel exp(beta sum x_e.y_e) is a positive definite kernel (tensor-power expansion), so T >= 0; P is reversible for nu = psi^2 dx and unitarily equivalent to T/lambda. Gauge covariance of P on invariant functions verified by the substitution y -> g y.
- Line 23 (three-slice law, Hessian 18 beta). HOLDS. Given X the neighbours are i.i.d. P(X, .) by reversibility; psi(x) cancels in nu(dx)P(x,du)P(x,dy), leaving exp(-S_{u,y}(x)). Along a product geodesic |x_p''| <= sum|g_j''| + 2 sum_{j<k}|g_j'||g_k'| = (sum|v_j|)^2 <= 4 sum|v_j|^2; four plaquettes per spatial link give 16 beta; each temporal term gives |x_e''.c| = |v_e|^2 |x_e.c| <= |v_e|^2, two terms give 2 beta. Total 18 beta. n >= 3 keeps the four plaquettes distinct.
- Lines 29-46, (1)-(2). HOLDS. delta_{U,Y}V = delta_nu V - s_V(X,U) - s_V(X,Y) because the middle law given (U,Y) is nu(dx)P(x,U)P(x,Y). Cross terms vanish by E[s_V | X] = 0 and conditional independence. (2) rederived: Ricci identity gives -V^j nabla_j nabla_i V^i = -V^j nabla_i nabla_j V^i + Ric(V,V); integration by parts in i produces the term that cancels V^j A_i nabla_j V^i. tr(M M) <= |M|_HS^2, Ric = 2g on unit S^3 products.
- Lines 48-55, (3). HOLDS. <Ph, delta_nu V> = E[(h(Y)-Ph(X)) s_V(X,Y)], E|h(Y)-Ph(X)|^2 = |h|^2-|Ph|^2 <= (r^{-2}-1)|f|^2.
- Lines 226-232, (16). HOLDS. With g = P(I+P^2)^{-1} f: E|f(X)-g(U)-g(Y)|^2 = |f|^2 - 4<f,Pg> + 2<g,(I+P^2)g>, minimized value <f,(I-P^2)(I+P^2)^{-1} f>. Recomputed by hand.
- Lines 96-102 (conditional product law of the hidden links given U,Y,Z). HOLDS for plaquette-separated I: each plaquette through a hidden link is linear in that link, so q_e(x) = exp(beta p.x)/Phi(beta p), p = h_e + u_e + y_e, independently over e in I.

Verdicts.

- Line 355, (29). HOLDS. The flag mixture has marginal eps_e rho_e + (q_e - eps_e rho_e) = q_e, so the triple law is exact. Given (U,Y,Z,F,X_{I\F}) the flagged spins are i.i.d. rho_e(.|Z); this law is A-measurable, so it is also the law given A, and X is conditionally independent of (U,Y) given A. K_I = Pi* Pi with Pi = E[.|A] is positive and self-adjoint, <f,(I-K_I)f> = E Var(f(X)|A) = E Var(f(X)|A,U,Y) <= E|f(X)-g(U)-g(Y)|^2, minimized by (16). (1-t^2)/(1+t^2) <= 2(1-t) on [0,1] reduces to 0 <= 1 - t + 2t^2. The statement holds for all f in L^2(nu), not only physical f.
- Line 15, consequence 2 tanh(aE). HOLDS: E|f(X'')-f(X)|^2 = 2<f,(I-K_I)f> <= 2<f, tanh(a H_lat) f> <= 2 tanh(aE) on the band.
- Line 366 (local choice of flags). HOLDS. |p| >= H + 2 - 2B_1/sqrt(beta) >= 3; |p/|p| - t_e| <= 2|w|/|p| <= (4/3)B_1/sqrt(beta); on the cap beta(|p| - p.x) = beta|p||p/|p|-x|^2/2 <= 3(CB_1+1)^2; Phi(s t) = 2 I_1(s)/s ~ sqrt(2/pi) e^s s^{-3/2} gives q_e >= c beta^{3/2} exp(-C(1+B_1)^2); cap mass (2/pi) int_0^{beta^{-1/2}} sin^2 >= c' beta^{-3/2}. eps = c c' exp(-C(1+B_1)^2) works, independent of the grid.
- Lines 372-378, (30) spatial part. HOLDS, given the common-direction trace comparison (checked in Step 4). 1_A <= exp(c beta sum(1-w) - c B m_I/3) pointwise; the gauge-projected trace integrand is positive, so the pointwise bound passes to Tr[(1_A P^2)^l]. 4 m_I distinct marks per marked slice, all containing the direction of I (I parallel, line 321). ||1_A P||^{2l} = ||1_A P^2 1_A||^l <= Tr[...]; Tr P^{2l} -> 1 at fixed grid. ||f - Pf||^2 = <f,(I-P)^2 f> <= D(f).
- Line 380, (30) temporal part. HOLDS. G is invariant under simultaneous gauge transformations, so P_G preserves the invariant space; its kernel 1_G psi T psi is symmetric. The marked temporal faces lie in the (0, direction of I) planes, so they also contain the direction of I. ||P_G||^{2l} <= Tr P_G^{2l}. E[|f(X)|^2 1_G(X,U)] = <f,P_G f> + E[conj f(X) 1_G (f(X)-f(U))] gives the displayed bound; ||f(X)-f(U)||^2 = 2D(f). The weight change costs ||f(U)-f(X)||_2 * || |f(U)|+|f(X)| ||_2 <= 2 sqrt(2 D(f)). Union of three events with thresholds B m_I/3 each.
- Line 389, (31). HOLDS. Total six-plaquette deficit <= B m_I implies at most m_I/2 links have individual sum > 2B. A low-sum link has H_e >= 4 - 2B/beta, |x_e - t_e|^2 = 2(1 - t_e.x_e) <= 4B/(3 beta), |u_e - x_e|^2 <= 4B/beta, so it passes with B_1 = C sqrt(1+B). The flags are not independent of X given (U,Y,Z); the note correctly moves the weight to |f(U)|^2, which is (U,Y,Z)-measurable, applies Chernoff to Bin(N_pass, eps) with N_pass >= m_I/2 and delta = eps/4, and moves the weight back at cost 2 sqrt(2 D(f)). The checkerboard colour (direction 1, x_2 + x_3 even, n even) is plaquette-separated.

Claim 1 verdict: HOLDS. The construction is an exact Nummelin-type splitting of the conditional product law; (29) is an operator inequality on all of L^2(nu); (30)-(31) have constants independent of n, m_I and beta >= beta_1.

### Step 3. Positive claim 2: physical-scale estimates (34) and (37) (done)

- Line 429, (34). HOLDS (as a sufficient criterion). log P(x,y) = -S(x)/2 + beta sum x_e.y_e - S(y)/2 + log psi(y) - log lambda - log psi(x); the x-only terms are fixed by E[s_v | x] = 0, giving s_v = beta sum v_e.(y_e - E[Y_e|x]) with conditional covariance A_x. <h(Y)-Ph(x), s_v> = v(Ph)(x), so the projection onto the score span has squared norm <grad Ph, A_x^{-1} grad Ph>, and its nu-integral is at most |h|^2 - |Ph|^2. Ph is smooth and gauge invariant, and centred when h is. Hence |P|_{centred phys}|^2 <= C_A/(1+C_A) and, with P >= 0, H_lat >= (2a)^{-1} log(1 + C_A^{-1}). If C_A <= C/a uniformly, the bound tends to 1/(2C). The lattice result and the implication are proved; the estimate C_A = O(1/a) is not (line 481 says so).
- Line 447 (size of the elementary estimate). HOLDS. |sum v_e.y_e| <= sum|v_e| <= sqrt(m)|v|; osc log psi <= beta m + 2 beta m (half-action over m = 3n^3 plaquettes, electric log kernel over m links); S^3 first eigenvalue l(l+2) = 3, tensorized Haar Poincare constant 1/3; C_A <= beta^2 m e^{6 beta m}/3. Gaussian mode recomputed: score variance r^2/((1-r^2) sigma^2), C_A = r^2/(1-r^2), (34) gives exactly -a^{-1} log r.
- Line 461, (36). HOLDS. Per slice one bad (cube, orientation) has about d^3 marks of one orientation, all containing a common direction; Markov with the coupling weakened by a fixed fraction gives Tr[(1_bad P^2 1_bad)^l] <= (C^{Cd^3} e^{-c' B d^3})^l Tr P^{2l}; roots give ||1_bad P||^2 <= e^{-c d^3} for B large; band vector v = Ph with |h| <= r^{-1}|v|; union over 3n^3 (cube, orientation) pairs.
- Line 470, (37). HOLDS. The censored chain is nu(.|G_d)-reversible and gauge covariant (G_d is gauge invariant). Recomputed: <f,(I-K)f> >= nu(G_d) gamma_d Var_{nu(.|G_d)}(f), and with nu f = 0, |int_{G_d} f|^2 <= nu(G_d^c) ||1_{G_d^c} f||^2, so nu(G_d) Var >= ||f||^2 - ||1_{G_d^c} f||^2 / nu(G_d). The closing inference also HOLDS: with d^3 >= K_0 log n and K_0 > 3/c, (36) gives ||1_{G_d^c} f||^2 <= 3 e^{2a Delta} n^{3 - c K_0} -> 0; the upper bound from (29) is tanh(a Delta) < a Delta; so gamma_d >= c a would leave no centred physical band state for Delta < c at small cutoff. Notation: the letter c is used both for the exponent in (36) and for the hypothesis gamma_d >= ca; the conclusion refers to the second one.
- Line 478 (OPEN). Checked the stated example: constant abelian U_1 = exp(i alpha/n) has zero deficit and winding trace 2 cos alpha. The hypothesis gamma_d >= ca is not established.
- Line 479 (passage to a continuum limit). HOLDS as an implication. On the dense set, |<v_a^c, P^{floor(t/a)} w_a^c>| <= e^{-m_* a floor(t/a)} |v_a^c||w_a^c| passes to the limit; on v = w, mass delta in [0, m_* - eps] would give a lower bound delta e^{-(m_*-eps)t}. Continuity extends the norm bound on e^{-tH} minus the vacuum projector, which also gives vacuum uniqueness. The construction and convergence hypotheses are assumptions, as the note says.

Claim 2 verdict: (34) and (37) HOLD as finite-lattice inequalities and as sufficient criteria. Neither physical-scale input (C_A = O(1/a), gamma_d >= ca uniformly in box and cutoff) is proved; the note labels both OPEN (lines 478, 481, 483). No physical gap follows from this note.

### Step 4. Cited earlier rows, read where a step depends on them (done)

Load-bearing inputs.

- Row 1155 (9), `gap-solve7-astra62.md` lines 129-134 (statement and proof read). The marked-plaquette moment E exp{c beta sum_{p in S}(1-w_p)} <= C^{|S|}: common direction as transfer time, marked electric couplings halved, normalized one-link convolutions ordered by row 1149 (16), order kept by gauge projection and the magnetic sandwich, normalizer ratio z_{beta/2}/z_beta, Schatten Hoelder around the circle, Hoelder over four directions for arbitrary marks. Checked HOLDS in row 1156 (`gap-solve7-check-opus.md` line 533). The target uses it in (10) (line 139), (18) (line 248), (22) (line 295), (30) (lines 378, 380), (33) (line 419) and (36) (line 468), always with all marks containing one direction. With one common direction no Hoelder over directions is needed, so any weakening factor below one works; this justifies the exponent 8/9 in (22) and the fixed fractions in (30), (36). Consistent.
- Row 1149 (16), `gap-solve4-astra62.md` lines 216-222 (statement and proof read). I_{j+1}(v)/I_j(v) increasing: v^{-j} I_j(v) is a positive multiple of int_{-1}^{1} e^{vx}(1-x^2)^{j-1/2} dx, whose log-derivative is the tilted mean of x and equals I_{j+1}/I_j by I_j' = I_{j+1} + (j/v) I_j; its derivative is a variance. Multipliers I_{2l+1}(s)/I_1(s) are products of these ratios, so normalized C_{s'} <= C_s for s' < s. I rederived the multiplier formula: int e^{s cos theta} chi_j dg = (2(2j+1)/s) I_{2j+1}(s), normalized by 2 I_1(s)/s. Checked HOLDS in row 1150 (`gap-solve4-check-opus.md` line 805). Used in (22), (25), line 139. Consistent.
- Row 1290 (11), `gap-solve33-astra62.md` lines 156-161 (statement and proof read). The every-other-slice marking, Tr[(1_E U^2 1_E)^l]/Tr U^{2l} <= C^l e^{-cul}, l-th roots, and U^2 >= (1-delta)^2 1_{[1-delta,1]}(U). The target's line 139 and (30), (36) use the same argument with r in place of 1 - delta. Checked HOLDS in row 1297 (`gap-solve33-check-opus.md` line 519).
- Row 1215, `gap-solve23-astra62.md` line 447: b_* = 11/(3 pi^2) in the Wilson convention. Line 141's arithmetic: 5 b_* = 55/(3 pi^2) < 2 iff 55 < 6 pi^2 (= 59.2); with pi > 3.1, 6(3.1)^2 = 57.66 > 55. HOLDS. Also consistent with the one-loop value beta = 4/g^2, b_0 = 11/(24 pi^2) for SU(2), giving beta / log(1/a) -> 8 b_0 = 11/(3 pi^2).
- Row 944, `gap-sgstep-opus.md` Lemmas TG, EF and Identity HV (2.2), lines 94-142 (read). The score formula used in (34) is proved inline in the target and agrees with Lemma TG/EF. Credit addition: the target's (35) (line 449) is row 944's Identity HV (2.2) rewritten. With F = log psi + S/2, (2.2) reads A_x = Hess F + beta sum_e |v_e|^2 x_e.E[Y_e|x]; multiplying by -2 and adding Ric = 2g gives (35) exactly. Row 945 checked HV as HOLDS (`gap-sgstep-check-astra.md` line 126). The target cites row 944 for (34) but not at (35).

Comparison remarks (GUIDE text, not load-bearing), read for accuracy.

- Row 1167 (11) (`gap-solve12-astra62.md` line 145): I - Q <= cosh^2(k beta)(I - P^2), proved through a four-point log cross ratio bounded by 4k beta (line 149). The description at target line 94 is accurate.
- Row 1169 (`gap-solve13-astra62.md`): (15)-(18) thermal test with the common minorant delta = exp[-C(k+M)] (16); line 311 proves the exponential cost in k is unavoidable for such a minorant; (21) is the bounded-reading estimate. The descriptions at target lines 94, 175, 312, 364 are accurate.
- Row 1236 (11) (`gap-solve27-astra62.md` line 145): a per-link bound int |D_e(f/psi)|^2 dnu <= C beta^2 (1-q)^{-3} D(f). Description at line 17 accurate.
- Row 1290 (3) (`gap-solve33-astra62.md` line 48) and its OPEN line 52 (Poincare on the midpoint law omega with C_a = O((a beta)^{-1})). Description at lines 9, 17 accurate.
- Row 1145 (`gap-solve2-astra62.md` lines 34-51): straight coarse transports tested against the temporal transfer. Description at line 478 accurate.
- Row 1155 line 53: the direction-one bonds with x_2 + x_3 even, n^3/2 of them. Matches target line 255.
- Row 1218 (`prior/gap-onebound-read-sol.md` lines 25-27, 264) and row 968 (`gap-avgcurv-max.md`): names and topics as described at lines 9 and 456.

### Step 5. Every remaining statement (done)

Each item gives line, label and verdict, then the hand check.

- L3 PROVED (checkout observation). HOLDS: `library/prior/` has no `gap-solve34` file in the clone now.
- L62, (4). HOLDS. B_t is triangular in the inputs; integrating x_m, ..., x_1 in turn with left invariance shows it preserves product Haar; for fixed input the curve t -> B_t x is a product geodesic of speed b(x). Taylor gives S(B_{-t}x) <= S(x) - tD + 9 beta t^2 b^2, and E[exp(S(X) - S(B_{-t}X)) | U,Y] = 1 by the change of variables. The bound phi(t) <= 1 = phi(0) for all real t gives E[D|U,Y] = 0 and E[D^2|U,Y] <= 18 beta E[b^2|U,Y].
- L72, (5). HOLDS. div(a_i(x_{<i}) x_i) = 0 (left-multiplication Killing field, coefficient free of x_i), so D = delta_{U,Y}V. E[D|X] = delta_nu V(X), E[D|X,Y] = delta_nu V(X) - s_V(X,Y). Jensen (b is X-measurable), then Cauchy-Schwarz with parameters 2t, -2t: 9 beta (2t)^2 = 36 beta t^2. The variance form follows from (1) and E D^2 <= 18 beta E b^2.
- L79, (6). HOLDS. |<f, delta_nu V>|^2 <= (r^{-2}-1)|f|^2 E|s_V|^2 <= 9 beta (r^{-2}-1)|f|^2 E b^2; duality over predictable a gives the left side of (6). The density step needs continuity of s_V in a, which holds because d_x log P is bounded at fixed grid. Putting a set J last and using coefficients measurable in x_{J^c} is a special case, by contraction of conditional expectation.
- L87. HOLDS. E[(D_1 g_1) g_2] = E[D_1 g_1] E[g_2] = 0; E[D_2 g_2] = 0 by Haar invariance. Class functions are not needed.
- L89. HOLDS. For link blocks i != j one of nabla_i V_j, nabla_j V_i vanishes, so only diagonal blocks enter the trace term of (2), and tr(M^2) <= |M|^2.
- L96, (7). HOLDS (see Step 2). b_z(u) = psi(u) e^{-S(u)/2} exp(beta sum_{e not in I} z_e.u_e) recomputed from nu(dx)P(x,du)P(x,dy).
- L104, (8). HOLDS. Upper bound log Phi <= |w|; cap of radius (1+|w|)^{-1/2} with exponent drop at most 1/2 and Haar mass >= c(1+|w|)^{-3/2}. The replacement error is O(log(2+beta)) even where |h+u+y| is near zero. H + t.v <= |h+v| <= H + t.v + |v|^2/(2H); the four-point sum is at most (|u+y|^2 + |u'+y'|^2)/(2H) <= 4/H. Extremal points recomputed: |h+2u|^2 = (H-2/H)^2 + 4(1-H^{-2}) = H^2, |h+u+u'| = H - 2/H >= 0 for H >= sqrt 2. Additivity over e holds because K_z is a product of factors in separate pairs (u_e, y_e).
- L118 and L125, (9). HOLDS. Chord bound (G-v)_+ <= (d-v)(G-1)/(d-1) on [1,d]; max_v (v-1)(d-v)/(v(d-1)) at v = sqrt d equals (sqrt d - 1)/(sqrt d + 1) = tanh(D/4). L_z is symmetric since K_z(u,y) = K_z(y,u). A_z A_z^* = L_z because U, Y are i.i.d. given X; E Var(f|Y,Z) <= E Var(f|Y) = |f|^2 - |Pf|^2.
- L132, (10). HOLDS. (1 - tanh(D/4))^{-1} <= e^{D/2} <= e^{2k beta/s} (2+beta)^{Ck}; times 1 - e^{-2aE} <= 2LE/n gives n^{2kb/s - 1 + o(1)} (log n)^{O(1)} -> 0. Bad z: H_e < s forces a plaquette deficit > (4-s)/4 for every completion, mass <= 4k r^{-2} C e^{-c beta (4-s)/4} -> 0.
- L139. HOLDS (Step 4 inputs).
- L141. HOLDS (Step 4).
- L146, (11). HOLDS. L_z = (inclusion) L_red E[.|U_I], so the nonzero spectrum is that of L_red. For product weights the pairs are independent, each pair operator is a Gram kernel through the middle spin, and the centred norm of a tensor product is the largest factor centred norm. Comparison: with omega = a_z / prod b_e in [1, e^B], the numerator does not decrease and the denominator grows by at most e^{2B}; L_z >= 0, so gap = 1 - ||L_z||_0.
- L157, (12). HOLDS. Substituting lambda psi(u) = int T(u,w) psi(w) dw combines the half-weights; each hidden u_e appears linearly through its four spatial staples and the forward temporal link w_e; |c_e| <= 4 + 1.
- L164. HOLDS. Mixed derivatives of a log-Laplace transform are beta^2 times covariances (no Christoffel term across factors). Telescoping from an anchor with geodesic lengths <= pi gives |R| <= pi^2 sum J_ef and osc <= 2 pi^2 sum J_ef. osc log a_z <= 5 beta * 2 * k.
- L177-L211, (14) (main comparison). HOLDS. Checked: F_alpha(t) = 1; the expansion of a is a positive mixture with fields 2t, 4t; the masses are s^N for equal and z^N for unequal labels; chart limits (precision 4 for the middle, F_alpha -> exp(-alpha|v|^2/(2(alpha+1))) from |alpha t + x|^2 = (alpha+1)^2 - 2 alpha (1 - t.x)); A_F - B_F = det(w_1,w_4) det(w_2,w_3) by the 2D Binet-Cauchy identity; strict Cauchy-Schwarz gives z/s <= r_* < 1; the pairing symmetry groups act transitively on four positions and (2 3) maps A to B fixing position 1, so one-coordinate marginals coincide; Gaussian majorants (1 - cos theta >= 2 theta^2/pi^2, (sin theta/theta)^2 <= 1) give L^1 convergence; the symmetric relative-entropy argument gives distinct limiting neighbour marginals; error sum <= affinity^N; P(unequal) <= (z/s)^N; disagreement <= r_1^N + r_*^N; Rayleigh quotient >= 1 - 2(r_1^N + r_*^N) - O((r_1^N + r_*^N)^2). Precision: "class functions" holds because t = 1 makes t.u_i = (1/2) tr u_i.
- L218, (15). HOLDS. R(Bx) = exp(S(Bx) - S(x)); E R^p = E exp((p-1)(S(BX) - S(X))) <= e^{9 beta (p-1) b_0^2} E e^{(p-1)D}, and (4) at t = p-1 gives E e^{(p-1)D} <= e^{9 beta (p-1)^2 b_0^2}; total exp(9 beta p(p-1) b_0^2). Jensen for random maps.
- L226, (16). HOLDS (Step 2).
- L234, (17). HOLDS. Gauge invariance: h g h^{-1} has the law of g. E[R_e | X] = 1 + j_e(X) by testing against g(X). Precision: the one-link conditional action -beta p.x has Hessian bound 6 beta, so the one-link proof gives E R_e^2 <= e^{6 kappa^2}; the stated K_kappa = e^{18 kappa^2} - 1 is a valid, weaker constant.
- L243, (18). HOLDS. <T_e, j_f> = 0 for e != f (p_e contains no other link of I); E_a exp(kappa a/sqrt beta) = cos(kappa/sqrt beta), also for inverted occurrences; 1 - cos u >= u^2/4 on |u| <= 1; at most eps|I| Gram eigenvalues exceed C/eps; ||Jc|| >= c'_kappa sqrt(eps/C) ||c||.
- L255, (19). HOLDS. (1-r^2)/(1+r^2) = tanh(aE) at r = e^{-aE}; divide (17) by (18).
- L266, (20). HOLDS. Mixture density 1 + theta_e(R_e - 1); independent centred factors.
- L273 and L284, (21). HOLDS. d = (|v|^2 - (r_0 - H)^2)/(2H) recomputed; d <= (2/H)(6 - r_0); |p_perp|^2 = d(r_0 + t.p) <= 12 d; excess of |24t - p| <= |p_perp|^2/(2(24 - t.p)) <= d/3; rate d + d/3 <= (8/9)(6 - r_0) for H >= 3; 6 - r_0 <= 6 - p.x_e = sum of six deficits; r_0 in [1,6], |24t - p| in [18,30] keep the prefactors bounded.
- L291, (22). HOLDS (Step 4): coupling beta -> beta/9, normalizer ratio z_{beta/9}/z_beta bounded (limits 1 and 27), period limit at fixed box.
- L297, (23)-(24). HOLDS. E R^2 = sum_J theta^{2|J|} E prod K'_e <= (1 + C_0 theta^2)^{m_I}; f(X') is conditionally independent of X given O, so E Var(f(X)|O) <= E|f(X) - f(X')|^2; E|f(U)-f(X')|^2 = E[R |f(U)-f(X)|^2] <= (E R^2)^{1/2} (8 ||f||_inf^2 D(f))^{1/2}; constants 4 and 4 sqrt 2 recomputed. (24) is (16) with D_0 = R - 1.
- L312. HOLDS. P(H_e < 3) <= 4 C e^{-c beta/4}; (1 + C_0/m_I)^{m_I/2} bounded; (1 + C_0 eta log n/m_I)^{m_I/2} <= n^{C_0 eta/2}.
- L316, L323, L332, (25)-(26). HOLDS. High H: excess <= 12d/228 = d/19, rate <= (20/19)(2/H)(6-|p|) <= (160/171)(6-|p|) for H > 9/4, |p| > 1/4. Low H: 1 + K_e = Phi(beta(h+v)) Phi(beta(h-v))/Phi(beta h)^2; |h+v| + |h-v| <= 2 sqrt(H^2 + 4); g(H) = 4 + H - 2 sqrt(H^2+4) is concave with g(0) = 0, g(9/4) = (25 - 2 sqrt 145)/4, so g(H) >= cH with c = (25 - 2 sqrt 145)/9 (about 0.102); the three sub-cases recomputed. Deletion: coupling 0 gives the projection on constants, below C_beta; cost z_0/z_beta <= C(1+beta)^{3/2}, four deletions times (1+beta)^{-3} give C(1+beta)^3.
- L334, (27). HOLDS. P(A in M_0) = (s)_{|A|}/(m_I)_{|A|} <= (s/m_I)^{|A|}; sum_A (s/m_I)^{2|A|} [C_2(1+beta)^3]^{|A|} <= exp(C_2 (1+beta)^3 s^2/m_I); s ~ n^{3/2}/log n at beta ~ log n.
- L343, (28). HOLDS. Clipping does not increase D; |f - f_b|^p <= b_n^{p-2}|f|^2; L^p contraction of Q; the p = 2 tail bound uses ||I - Q|| <= 1.
- L397 (trapped set). HOLDS. Periodicity needs 4 | n; all three oriented plaquettes are exp(i pi/2); the two staples in each transverse plane give e^{i pi/2} + e^{-i pi/2} = 0, so H_e = 0; cap-only kernels never flag links with H_e < 3, so K_I 1_S >= 1_S on S and reversibility gives K_I 1_S = 1_S.
- L404 (second flag kind). HOLDS. q_e/rho_e^0 in [e^{-4 beta}, e^{4 beta}]; half of each minorant sums below q_e; gauge covariance as stated.
- L406, (32). HOLDS. Posterior base-flag probability >= e^{-8 beta}/2, new value density >= e^{-8 beta}; six colours partition the m = 3n^3 links (n^3/2 each); K^6 >= 6^{-6} times the ordered sweep; int int |f(x)-f(y)|^2 nu(dx) dy = ||f||_nu^2 + ||f||_Haar^2 for centred f; 1 - t^6 <= 6(1-t); final constant 6^{-6}/24 recomputed.
- L413 and L421, (33). HOLDS. P(pass) >= 1 - C^6 e^{-(16/9)B} >= 1/2 for large B; given A each marked plaquette is fixed or equals v_e(Z).x_e of its own cap draw; Var(beta v.x) is about (v.t)^2 Var(|V|^2/2) + beta |v_perp|^2 Var(V_1) >= c'; c_0 = c' eps/2. Spectral split gives ||1_{(delta_0/a, inf)} T_b||^2 >= (c_0 - (C/eta) tanh delta_0) ||b||^2. The all-plaquette remark: the flagged dependence is -beta h_e.x_e with H_e >= 3.
- L449, (35). HOLDS. With Psi(x) = int e^{beta sum x.y} e^{-S(y)/2} psi(y) dy, Hess log Psi = -beta sum |v_e|^2 x_e.E[Y_e|x] + A_x; V = S - 2 log Psi + const. Credit (see Step 4): this is row 944 (2.2). The curvature criterion: solve delta_nu grad u = g; (2) with Hessian term >= 0; weighted Cauchy-Schwarz gives C_A <= 1/(ca).
- L458. HOLDS. ij i^{-1} j^{-1} = (ij)^2 = -1 and likewise for the other planes; w = -1 is the minimum of each w, so grad S = 0; four incident traces -cos t give Hess S(v,v) = -4 beta; Hess S annihilates orbit directions at a critical point; right side of (35) at v_perp <= 2|v_perp|^2 - 4 beta + 2 beta |v_perp|^2 <= (2 - 2 beta)|v_perp|^2 since |v_perp| <= 1; on an odd cube the windings +-i, +-j have centralizer {+-1}.

GUIDE and OPEN items checked for accuracy: L5 is consistent with row 1290 L3-L5 and the cited search file (the PR heads were not refetched); L7 links not opened; L9, L17, L21, L94, L175 accurate (Step 4); L13, L57, L166 (13), L213, L478, L481 are correctly labelled OPEN; (13) agrees with (9) and (11). RESULT L483 accurately summarizes the note.

Wording precisions (no change of verdict).
- W1 (L15, L394): the probability that a positive fraction is redrawn is under the state-weighted law |f(X)|^2 nu (and |f(U)|^2 in the proof); say so.
- W2 (L470-L476): the letter c denotes two different constants (the exponent of (36) and the hypothesis gamma_d >= ca).
- W3 (L241): the one-link proof gives the sharper K = e^{6 kappa^2} - 1.
- W4 (L449): credit row 944, Identity HV (2.2), at (35).

### Step 6. Restatement search (done)

Searched: the 641 RESULT entries in `FINISH.md`, every `library/gap-solve*-astra62.md` with its check, and the whole `library/` for the target's constructions (fixed-string greps: the two-neighbour predictor g(U)+g(Y), (I-P^2)/(I+P^2), tanh(aH), minorant, minoriz, resampl, flag, Nummelin, residual density, the pairing polynomials m(u_1,u_2) and det(w_1, ...), equal pair, one-sided weight, A_x^{-1}, inverse covariance, score covariance, Cramer, holding step, G_d, six-colour, 6^{-6}, trapped, refill, erasure, descending factorial, quaternion units, Ric + nabla^2, pointwise curvature, Bakry). Hits were read at the matching lines.

Main comparison.

- (29), the quadratic-form comparison I - K_I <= (I - P^2)/(I + P^2) <= 2(I - P) (L355), is NOT a restatement. No earlier row has the two-neighbour predictor (16) or the tanh(aH) form. The nearest rows are different estimates, and the target names both: row 1167 (11) bounds the full erasure, I - Q <= cosh^2(k beta)(I - P^2), with a constant exponential in k; row 1169 (16)-(18) uses one common minorant delta = exp[-C(k+M)] for a prescribed product of links and pays delta^{-1}. The per-link splitting with revealed flags gives constant one and is new in the lane by grep.
- The labelled comparison (14) (L177-L211) is NOT a restatement. Row 1167's two-well test (`gap-solve12-astra62.md` L248-L262) separates the centre-sign configurations, which have different one-link laws, and gives tanh(k beta). Row 1169's minorant limitation (`gap-solve13-astra62.md` L311) compares two prescribed histories at +-i/sqrt(beta). Neither has identical one-coordinate marginals with a block-pairing label. No earlier file has the pairing construction.

Restatements and credit additions found.

- R1. (35) (L449) restates row 941 (A6) (`gap-lsivac-max.md` L127-L135): (Ric + Hess Phi)(v,v) = 2|v|^2 + Hess_M V(v,v) + 2 beta [sum_l E<w_l, x_l>|v_l|^2 - beta Var(<v,w>)], the same identity with V = S and Phi = -log psi^2. Row 943 checked A6 as HOLDS (`gap-lsivac-check-astra.md` L203). It is also row 944 (2.2) rearranged (Step 4). The target cites neither at (35); it cites only row 968.
- R2. The negative-curvature statement L458 has the same bound and conclusion as row 941's method ceiling (i) (`gap-lsivac-max.md` L176-L178): pointwise Bakry-Emery for nu fails for every beta > 1, (Ric + Hess Phi)(v,v) <= (2 - 2 beta)|v|^2. Row 941 flips one link of the flat field; the target uses the constant i, j, k field and adds a horizontal-projection and regular-orbit argument. This refines row 941's ceiling, and the target should credit it. Row 1254 (38) (`gap-solve29-astra62.md` L476-L490) proves the analogous failure, with quotient -> -infinity at weak field, for the Euclidean Wilson measure rather than for nu.
- R3. (34) (L429) is not a restatement but follows the method of row 931's Theorem E (`gap-direction-max.md` L329-L338): chain rule with stationarity, a score Cauchy-Schwarz, and a functional inequality for nu applied to Pg, giving the contraction Theta/(1+Theta). Theorem E is the entropy form with a scalar sub-Gaussian proxy. (34) is the L^2 form with the exact score covariance A_x as the metric, and gives C_A/(1+C_A). Row 941's Proposition W (`gap-lsivac-max.md` L238-L248) uses the same score Cauchy-Schwarz with a scalar variance bound. If A_x <= sigma^2 I and nu has Poincare constant lambda, then C_A <= sigma^2/lambda, the Poincare analogue of Theta_H. Credit row 931 Theorem E and row 941 Proposition W at (34).
- R4. The method of (30) (marking every other slice, trace roots, moving the state weight by Cauchy-Schwarz) is that of row 1290 (11) and row 1169 (17) (`gap-solve13-astra62.md` L245-L252). The extensive threshold B m_I, all physical f, and the temporal-face part with P_G are new. The target cites row 1290 at L139 but not at (30).
- R5. The three-slice conditional law (L23) is row 1169's local conditional laws (`gap-solve13-astra62.md` L224). This is a standard building block; there is no priority issue.
- Not restatements by grep or reading: (6), (11)-(12), (16), (17)-(19), (20)-(28), (32), (33), (36)-(37), the trapped set L397. The "holding step" hit in row 1283 (`gap-solve32-astra62.md` L110) is a killed random walk. Row 1272 (3)/(25) compares cube-update Poincare constants for the Euclidean Wilson measure. Both are unrelated to (37).

### Step 7. Numeric guide (done; guide only, no proof weight)

Two scripts were run in a scratch directory outside the repository with `python3 -E -P`, BLAS threads 1 and a virtual-memory cap. Peak memory was 0.30 GB and 0.02 GB; run times were 2.5 s and 2.3 s.

- (8): random local search for the four-point sum of |h+u+y| at H = sqrt 2, 2, 3, 4 never exceeds 4/H, and the stated extremal points give exactly 4/H.
- Phi(s) = 2 I_1(s)/s at s = 3.7 to 9 digits; I_{j+1}/I_j increasing on (0.01, 60] for j = 1..11; spin multipliers I_{2j+1}(s)/I_1(s) match quadrature for j = 1/2, 1, 3/2.
- c = (25 - 2 sqrt 145)/9 = 0.10187, and 4 + H - 2 sqrt(H^2+4) >= cH on [0, 9/4].
- (21), (25), (26): 200000 random samples each, no violation of d <= (2/H)(6 - r_0), |p_perp|^2 <= 12d, excess <= d/3, rate <= (8/9)(6 - r_0); of the high-H rate (160/171)(6 - |p|); or of the low-H rate (4 - H) - cH.
- (9): max over v of (v-1)(d-v)/(v(d-1)) equals tanh(D/4) at D = 0.3, 2, 7.5.
- (14): the 2D Binet-Cauchy identity holds on random vectors. Precision found by the guide and then computed exactly: in the Gaussian limit, 1 - z/s = (E det^2)^2 / (2 (E (w_1.w_2)^2)^2) with E det^2 = 2[(28/15)^{-3/2} - (41/30)^{-3}]. Its value is 9.93e-8. Finite-beta Monte Carlo at beta = 20, 80 gives z/s = 1.000000 to six digits. So r_* < 1 holds, but r_* is about 1 - 1e-7, and the decay constant c in (14) is of that size. The statement is qualitative and stays true; the bound bites only for N of order 1e7 or more blocks. Recorded as wording precision W5.
- L397, L458: the abelian field on n = 4 is periodic and has all staple sums H_e = 0 to 1e-15; the i, j, k field has all three oriented plaquettes equal to -1.
- (32): log(q_e/rho_e^0)/beta stays in [-3.15, 2.87] over random samples, inside the stated [-4, 4].
- (29), independent implementation: a finite toy chain on {0,1,2}^3 with the same structure (PD product electric kernel, two hidden coordinates coupled only to the third, z-dependent proposals rho_e, eps_e = shrink * min q_e/rho_e, posterior flags). K_I is nu-reversible (error < 1e-15) and positive. min eig[(I-P^2)/(I+P^2) - (I - K_I)] >= -2e-15 and min eig[2(I-P) - (I-P^2)/(I+P^2)] >= -3e-16 in L^2(nu), for four parameter sets. This agrees with the hand proof and finds no counterexample.

### Step 8. Counts, verdicts, scope (done)

Source: `library/gap-solve34-astra62.md`, 483 lines, sha256 prefix 87a8e197712cece6. The file is unchanged between clone commits `92083e673` (read) and `3fac99ede` (at the end of the check).

Counts. 59 PROVED statements. 59 HOLDS, 0 HOLDS AFTER CORRECTION, 0 FAILS. Also 7 GUIDE and 6 OPEN items, all read and correctly labelled. 37 tagged equations checked.

Per-statement verdicts by line (all HOLDS). L3, L15, L23, L29 (1)-(2), L48 (3), L62 (4), L72 (5), L79 (6), L87, L89, L96 (7), L104 (8), L118 (9), L125, L132 (10), L139, L141, L146 (11), L157 (12), L164, L177 (14), L183, L196, L207, L209, L211, L218 (15), L226 (16), L234 (17), L243 (18), L255 (19), L266 (20), L273 (21), L284, L291 (22), L297 (23)-(24), L312, L316 (25), L323 (26), L332, L334 (27), L343 (28), L355 (29), L366, L372 (30), L380, L389 (31), L397, L404, L406 (32), L413 (33), L421, L429 (34), L447, L449 (35), L458, L461 (36), L470 (37), L479.

Positive claims. (29)-(31) HOLD: an exact per-link splitting of the conditional product law of a plaquette-separated set, I - K_I <= (I-P^2)/(I+P^2) <= 2(I-P) on all of L^2(nu), and a positive fraction of flags with state-weighted failure probability <= C e^{-c m_I} + C sqrt(D(f)), uniformly in n, m_I and beta >= beta_1. (34) and (37) HOLD as finite-lattice inequalities and as sufficient criteria. Their physical-scale inputs, C_A = O(1/a) and gamma_d >= ca uniformly in box and cutoff, are not proved, as the note says.

Main comparison. (29) is not a restatement of an earlier row. (14) is not a restatement either.

Credit additions (no change of verdict).
- R1: (35) is row 941 (A6), and row 944 (2.2) rearranged.
- R2: L458 refines row 941's method ceiling (i), with the same bound (2 - 2 beta)|v|^2. Row 1254 (38) is the Euclidean-measure analogue.
- R3: (34) is the L^2, covariance-metric form of row 931 Theorem E; it uses row 941 Proposition W's score Cauchy-Schwarz.
- R4: (30) uses the method of row 1290 (11) and row 1169 (17).

Wording precisions W1-W5 (Steps 5 and 7).
- W1: the flag-count probability is under |f|^2 nu.
- W2: c is overloaded in (36)-(37).
- W3: the sharper K_kappa = e^{6 kappa^2} - 1 holds.
- W4: credit row 944 at (35).
- W5: r_* in (14) is about 1 - 1e-7 (exact Gaussian-limit value 9.93e-8).

Not checked.
- The PR heads and the main commit cited at L5 were not refetched.
- The external links at L7 and L139 (Sussman-Alpoge outline lines) were not opened.
- Rows 1155 (9), 1149 (16) and 1290 (11) were read at the cited statements and proofs; their full files rest on their own checks (rows 1156, 1150, 1297).
- The dominated-convergence limits in (14) and the period limit in (22) were checked at the level of the stated majorants and compactness, without explicit error rates.
- The numeric runs are guide only.
- Nothing was committed; this file is untracked in the clone.

RESULT (2026-11-20T17:23Z, Claude Opus 5.5 max, laptop subagent, row 1307 check of row 1298 by gpt-6.2-astra max, cross-provider, by hand): all 59 PROVED statements of `library/gap-solve34-astra62.md` HOLD, 0 HOLDS AFTER CORRECTION, 0 FAILS. Positive claims HOLD: the stationary resampling (29)-(31) of a positive density of links, with uniform control on every normalized physical slow state, and the finite-lattice criteria (34) and (37). The main comparison (29) does not restate an earlier row, and neither does (14). Credit additions: (35) restates row 941 (A6) and row 944 (2.2); L458 refines row 941's ceiling (i); (34) is the L^2 covariance-metric form of row 931 Theorem E; (30) uses the method of rows 1290 (11) and 1169 (17). Five wording precisions, including r_* about 1 - 1e-7 in (14). OPEN: C_A = O(1/a), gamma_d >= ca uniformly in box and cutoff, the continuum construction, and the four-dimensional SU(2) mass gap.
