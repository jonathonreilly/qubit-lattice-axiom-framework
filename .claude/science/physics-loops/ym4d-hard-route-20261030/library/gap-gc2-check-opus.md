# Check of row 1445 (`library/gap-gc-astra62.md`)

- Row: 1452. Checker: Claude Opus 5.5 (laptop subagent). Date: 2026-11-23T22:08Z (date -u).
- Author of the checked note: gpt-6.2-astra max (row 1445). Results marked HOLDS are the author's; credit is theirs.
- File moved by the lead from gap-gc-check-opus.md (name collision with the committed row-758 check) to this path.
- Method: reading and hand derivation. Small exact or float guides with `python3 -I` in /tmp/gcchk (outside the repo). Floats decide nothing.

## Plan
1. Read the note in full; read (GC) in gap-mini-solve-g-fable.md 2.6 and brief row 1445.
2. Section 1: (1)-(2), quantifiers.
3. Section 2: (3), disjoint fine faces, board and neutral normalizations.
4. Section 3: (4), plaquette fixed before the event, two pins, phi=1/8, a=phi/l^2, entropy bound, (7).
5. Section 4: event, gauge invariance, measurability, chessboard direction, b_k, averaged probe.
6. Section 5 and t1, t2, t4, t6.
7. Judgement and verdict.

## Findings (appended item by item)

### F1. Section 1, (1)-(2) (note L25-52): HOLDS
- Field bound: each of the six incident plaquettes gives (1/2)tr(u S_i) = u.v_i with |v_i| = 1, so |H| <= 6 beta for any pin. Correct.
- Angle density C sqrt(1+|H|): prior 1155 L305-315; its check (gap-solve7-check-opus.md row 46) says HOLDS. I re-derived the scale (tilt concentrates at radius |H|^(-1/2); Z >= c e^|H| (1+|H|)^(-3/2)). Accepted.
- |cos t| <= eps has t-measure 2 arcsin eps <= 4 eps for eps <= 1/2. So p_beta = min(1, 4C h sqrt(1+6beta)/beta) -> 0 iff h = o(sqrt beta). Correct.
- Disjoint selection: a face shares a link with at most 4*5 = 20 others; greedy gives q/21. With link-disjoint faces, the free link of face j lies in no other selected face, so the other tests are measurable for the conditioning on "all but u_j". Iteration gives p^(q/21). Correct.
- Counting: Delta = 6*3^4 = 486 includes the plaquette itself, so it also covers the "return" move of the doubled spanning-tree walk; Delta^(2(k-1)) holds. Roots <= 6(l+1)^4, weak subsets <= 2^k. Term <= r^k / Delta^2 <= r^k; sum over k >= k_0 gives (2). Correct.
- Limit: for 2r <= 1, r^n <= 2r 2^(-n) with n >= alpha l, so sup_l 6(l+1)^4 r^n/(1-r) <= C_alpha r -> 0. (1) holds uniformly in l >= 8 and in every pin y (pins enter only through |H| <= 6 beta). Quantifiers as stated are right.
- Board: conditioning on the complement of one cell keeps the other cell events measurable (shared boundary links are pins, cell free links are not boundary links). M-th root <= sup_y bound. Correct; no RP needed for an upper bound.
- Frustrated sign weight (L50-52): log W(z)/W(tau z) = 2 sum_D j_p z_dp, correct. Character expansion: given the face products on an edge-disjoint class kappa, E z_dq = 0 for q in D\kappa because a 4-edge boundary is a mod-2 sum of edge-disjoint 4-edge boundaries only if it equals one of them, i.e. q in kappa. All faces of D have all links free, so no pinned sign enters. Hence sup >= 2 sum_D J_p/21, so at least half of D has J_p <= 21 B_beta, and (2) applies with eta = 1/2. Correct.

### F2. Section 2, (3) (note L54-107): HOLDS
- Disjoint fine faces: same grid, collinear mesh edges give coplanar rectangles sharing only a column; perpendicular edges give different orientations; different grids differ in x_3. Faces disjoint, bonds may be shared. Correct.
- Prior (9) of 1155 (gap-solve7-astra62.md L129-134): c = 1/8 from half coupling and Hoelder exponent four. Matches t = 1/8.
- Disk bound 1 - W_e <= A sum a_p: chord |g - 1|^2 = 2(1 - w); peeling and bi-invariant triangle inequality give sqrt(1-W) <= sum sqrt(a_p); Cauchy-Schwarz gives the factor A. Correct.
- q: Markov at t beta/2 and Cauchy-Schwarz over the two marginals give exp(-t beta d k/(2A)) C^(Ak). With b_d = t d/(4 log C), A^2 <= b_d beta gives A log C <= t d beta/(4A). Correct.
- Separator: grid with m cells per side has m+1 disjoint left-right rows, so a dual path has k >= m+1 >= m edges; parity argument for a bottom-top dual component is right. Fewer than m/2 good edges in the cut forces >= k/2 bad edges on the path. Sum m sum_{k>=m} (8 sqrt q)^k correct (4 steps x 2^k subsets x q^(k/2)).
- Planes: ribbon faces of different planes are disjoint, so a union of marks has bound q^(#marks); 2^m plane choices; with beta/A >= sqrt(beta/b_d), the terms 2^m (2m)^(rho m) are absorbed: log(2m) <= 2m and m <= m^2. (3) holds with c = rho t d/16 for large beta. M-cell version: same union bound. Correct.
- Neutral ensemble: 1155 L420 gives int exp(c beta sum a^b) dM_b <= C^|S| with M_b = twisted measure / Z_0. Mixture expectation = sum_b Z_0 int(...)dM_b / sum Z_b' <= 8 C^|F| since sum Z_b' >= Z_0. One factor 8 per union of marks after Cauchy-Schwarz (8^(1/2) 8^(1/2)). Central signs keep the peeling bound for a^b = 1 - tau w. Correct. Note: L420's constant c is "absolute", not 1/8; the note says "adjusting b_d, c, beta" which covers this.
- One-copy consequence: P(G) = E P_y(G), so ess inf_y P_y(G) <= (3). Correct, read as essential infimum.
- Centre move: eps_e = product of four side signs; path sign = prod eps_e (inner columns twice); eps_e = -1 gives W_e(U') = -W_e(U), deficits sum to 2 >= d. Every left-right path meets a pair-bad edge, so the bad set separates: D holds for the pair. Kernel preserves P_y, so U' is Wilson; r P(G) <= Pr(D). Board: no plaquette holds free bonds of two cells (perpendicular bonds at a shared site are collinear); laws factor given shared bonds; r^M factor. Partial-move completion gamma + (P - gamma_1)x(P - gamma_2)/(1-u) has marginals P. Correct.

### F3. Section 3, (4)-(7) (note L109-167): HOLDS
- Calibration: U_2(x) = exp(a x_1 T): 12-plaquette exp(a(x_1+1)T)exp(-a x_1 T) = exp(aT), angle a; 2mu and 1mu plaquettes flat. Perimeter of each full 12-square is tangential, so pinned; holonomy exp(a l^2 T), angle phi = 1/8. Correct.
- Only boundary links enter the cell law (every plaquette with a free link lies in the closed cube), so "extend arbitrarily" is right.
- Peeling: class angle = bi-invariant distance to 1, so sum_square theta_p >= phi for every filling. Correct.
- (5): with v = u - a, LHS = cos a (1 - cos v) + sin a (sin v - v); 1 - cos v >= 2v^2/pi^2 for |v| <= pi; v - sin v <= v^2/2; cos a >= 3/4, sin a <= 1/8 give >= (3/32 - 2/32) v^2. Correct.
- (6): linear term per square sum(theta_p - a) >= 0; N_12 = l^2 (l+1)^2; other orientations >= 0. Trivial pin: a = 0, f(u) >= u^2/8 >= u^2/32. Correct.
- Entropy: on the product of radius-1/beta balls each plaquette angle moves <= 4/beta, f is 1-Lipschitz, ball mass >= b beta^(-3). 0 <= -beta E S - log Z gives E(S - S_*) <= (4P + N log(beta^3/b))/beta <= C_1 l^4 log(2beta)/beta. Correct.
- Inner cube: M = (l/4)^2 (l/4+1)^2, M a^2 >= phi^2/256. Averaging gives a deterministic p with the stated epsilon (C_2 = 64*256*C_1/phi^2). p depends on (l, beta, the two pins) only, so it is fixed before the event. Correct.
- (4): errors 4E_0 theta^2/a^2 and 4E_phi (theta-a)^2/a^2; conditioning divides by c_0 at each pin; the indicator 1{theta_p > a/2} gives TV >= 1 - 4 eps/c_0. Correct, C = 4 C_2. Quantifier "every G with P_{y_i}(G) >= c_0 at both pins" is right.
- Mean contrast: E_0 f <= eps a^2/2; |E_phi f - f(a)| <= a E|theta-a| + E(theta-a)^2/2, and E(|theta-a| | G) <= a sqrt(eps/c_0) by Cauchy-Schwarz; f(a) >= 2a^2/pi^2. Ratio 1 + O(sqrt(eps/c_0) + eps/c_0). Correct.
- Continuity in pins (L156): sketched, not needed for (4) at the two pins.
- (7): tilted density <= e^|H|/Z with Z >= c e^|H| (1+|H|)^(-3/2) gives C(1+beta)^(3/2); the cap theta_p <= a/2 is a ball of radius a/2 in the free link, Haar mass <= C a^3 = C' l^(-6). So P_y(theta_p <= a/2 | G) <= (C/c_0)(sqrt(1+beta)/l^2)^3 at every pin. Correct. The inference (the indicator cannot separate once l >> beta^(1/4)) is right.
- Consistency with Section 4 (my own, rigorous by (4) itself): for k = 1 and the plaquette of (4), the Section-4 event G has TV <= 1 - b_1 at all pins, so (4) forces min(P_{y_0}(G), P_{y_phi}(G)) <= 4 eps/b_1. No conflict: Section 4 only claims the chessboard root. Scope sentence L158 is right: (4) lives at bare sides l << beta^(1/4), far below the first-passage band.

### F4. Section 4 (note L169-179): HOLDS AFTER CORRECTION (one scope sentence)
- **Defect D1, L171 (first failing line).** "Fix k distinct elementary plaquettes ... Choose distinct marked links, one on each plaquette, so that no action plaquette contains two marks" reads as if such marks always exist. They do not. Counterexample: the six faces of one elementary 3-cube. Each cube edge lies on exactly two of the six faces, so the mark of face F also lies on a second face F', which then contains two marks. Correction: state the class as k-sets of plaquettes that admit such a mark system (for example pairwise link-separated plaquettes at distance >= 2). Nothing else in the note uses the false reading; the averaged probe uses one plaquette.
- Event G (L173): the passing condition depends only on non-mark links, because no incident face of a mark holds a second mark. min over u of max deficit is continuous in the other links, so the event is closed, hence measurable. Deficits are gauge invariant and the minimization over u absorbs g_x u g_y^(-1). Correct.
- Failure: the actual mark value is a candidate, so failure implies some incident face with a_p > K/beta. (9) with |F| = 1 and c = 1/8 gives P <= C e^(-K/8) per face, union over 6k faces. Valid for every beta. Correct.
- Chessboard direction: AM6 (sa-index/chunk-03.md rows 2887-2942: slab copying with shared boundary bonds, positive slab functions, geometric-mean bound) with 1_G + eps in one slab and 1 elsewhere gives P(G) + eps <= (disseminated)^(1/2M); four directions in turn; eps -> 0. So the root is >= P_per(G) >= 1/2. Direction right. G depends only on links strictly inside the cell. I checked AM6 through the index only; outline L23668-23699 not read.
- Overlap b_k: chord bound |u - v_i| <= beta^(-1/2) + 2 sqrt(2K/beta) on the ball about the selected target gives all deficits <= C(K+1)/beta; normalizer <= C beta^(-3/2) from the selected face alone; ball mass >= c beta^(-3/2). These hold for every beta >= 2 (prior 1155/1197 statements say "beta large"; the note's own argument does not need it). Translation to the identity ball is an isometry; marks are conditionally independent; mixing over exposed data on G keeps the common component b(K)^k. Correct.
- Averaged probe (L177): 1262 (10) (gap-solve30-astra62.md L105-109) holds for every exterior of an even side-s update, s >= 4; s = l/2 >= 8 contains the central cube with margin l/8 >= 2. Each face is in at most two (note: four) stars; probes >= (l/4)^4; with l >= 4 beta the mean star sum is <= C'/beta; Markov with K >= 8C' gives mean d_y >= 7/8; common component sum_p M^(-1) b min(d_y, d_y') >= b(7/8 + 7/8 - 1) = 3b/4. Correct. Equivalence with averages of F_p(w_p) is right.
- Scope sentence L179 is right: neither statement controls the inner sigma-field of (GC).

### F5. Section 5 and tests (note L181-207)
- Carry (L187-194): HOLDS. The Section-4 overlap degrades as b(K(k))^k, and (3) bounds normalized probabilities, not the neutral trace. (M-neutral) needs a spectral sum; no finite-observable TV bound gives it. (t4) settles this decisively: the variant survives beta -> infinity at a fixed box while the neutral excited trace diverges (1215 (5), confirmed by check 1387 at gap-mech-direction2-check-astra62.md L149).
- First-passage arithmetic (L183): NOT CHECKED (CA-I L56442-56459 not read). The note cites CA-I L56486-56510 at L23 and L56442-56459 at L183 for the same arithmetic; I did not reconcile them. The conclusion that (4) ends far below the band is safe: (4) needs l^4 log beta << beta, while the first-passage side grows exponentially in beta under those inputs.
- L185 correctly keeps the 1197 claim "(GC) holds at most at xi-size cells" as guessed and open. The brief asked whether it can be made rigorous; the note does not do so and says so.
- (t1) HOLDS. Generating function e^(u cos v) = sum I_n(u) e^(inv). I_1/I_0 increasing (derivative = Var cos v), I_(j+1)/I_j increasing for j >= 1 (1149 (16), gap-solve4-astra62.md L216-220), so I_j/I_0 increasing. Then c_n(beta/2) <= R c_n(beta) with R = e^(beta/2) I_0(beta/2)/I_0(beta). Guide: R = 1.51, 1.47, 1.42, 1.417 at beta = 2, 5, 20, 60 (limit sqrt 2). Link-balanced currents have nonnegative weights, so the marked moment is <= R^|F|. The variant therefore fails the (t1) filter: the gain does not vanish for U(1). The note says this (L200, L198).
- (t2) HOLDS at sketch level. The one-face electric replacement is the 1149 (16) argument and does not see the number of transverse directions; the five-group Hoelder for many marks (L207) is the 1155 (9) argument with exponent five. I did not rewrite the 5D layer argument. The note correctly says it gives no estimate of the sixteen sectors (1443's (t2) reading).
- (t4) HOLDS as stated (see Carry). b_k is uniform in beta >= 2.
- (t6) HOLDS. e^(-beta r^2/2) <= v_beta <= C e^(-beta r^2/2): excess (u - 2 pi j)^2 - u^2 >= 4 pi^2 |j|(|j| - 1); the |j| = 1 term can tie (guide: C = 2.0 at beta = 2, 5, at u = pi). Fourier coefficient (2 pi beta)^(-1/2) e^(-n^2/(2 beta)) with the 1/(2 pi) normalization; half coupling costs <= sqrt 2. Integer-current sum is nonnegative. Matches 1443's (t6) reading (gap-mech-direction3-check-astra62.md L121-124): the variant is not selective against the massless Villain state. The note does not claim more.
- Guides (floats, decide nothing): /tmp/gcchk/g.py; minimum slack of (5) on a 201 x 2001 grid is 0 (equality at u = a); I_n/I_0 increasing for n <= 7 on (0, 30].

### F6. Judgement
- The note closes classes only. The classes: (1) weak bare centre cuts of positive density, uniform in l >= 8 and in every pin; (3) ribbon cuts with A^2 <= b_d beta, in the ordinary and the neutral mixture, for one copy, centre moves and partial moves; (4) every event of positive mass at both pins, but only at bare sides with l^4 log(2 beta) = o(beta); Section 4 positive variants for prescribed probe lists (chessboard only) and for the averaged probe (every exterior, G = everything). Each is stated with its quantifiers, except D1.
- (GC) on the band and (M-neutral) remain open, as the note says. Smooth cell-scale flux, collective adjoint events and interscale orientation events are not covered, as L185 says.
- No-carry claim: right.

## Verdict: HOLDS AFTER CORRECTION
- First failing line: L171 (D1, mark systems need not exist; restrict the class). All proofs in Sections 1-3 and the Section 4 arguments hold as written.
- Verified by hand: (1), (2), the frustrated-sign step, (3) with disjoint faces, separator, board and neutral factor 8, centre and partial moves, (4) to (7), Section-4 event, chessboard direction, b_k, averaged probe, (t1), (t4), (t6).
- Accepted from prior checked work, not rederived: angle density (1155 L305-315, check item 46), (9) of 1155, the twisted estimate 1155 L420, 1262 (10), AM6 (index only), 1215 (5).
- Not checked: CA-I first-passage lines; outline L23668-23699; (t2)/5D many-mark layer argument beyond sketch level; continuity-in-pins remark L156; (t3), (t5) (not assigned).
