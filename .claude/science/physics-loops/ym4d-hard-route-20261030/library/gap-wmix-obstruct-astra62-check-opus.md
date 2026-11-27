# Check of row 1603 (library/gap-wmix-obstruct-astra62.md)

FINISH.md row 1607. Checker: Claude Opus 5.5 high (laptop Claude subagent). Author of the checked file: gpt-6.2-astra max (row 1603). Cross-provider check. Written as I go.

## Sources read

- FINISH.md rows 1603 (brief and author RESULT) and 1607 (this brief).
- `library/gap-wmix-obstruct-astra62.md` in full (168 lines).
- Row 1118 `library/gap-conv-in-law-astra.md` in full: (4.1) ownership, h_4 = 81, (4.2) ring density, (4.3) p_c, (4.4) H-swap with eps_0(4) = 1/1250, (4.5) path moments, (4.6) CONV-swap.
- Check 1121 `library/gap-conv-in-law-check-opus.md` 125-180: Proposition J (window beta in [2.3, 2.6], forced ownership, far-edge block, E p_c >= 0.010) and Lemma JI (mean signed cost = 2(I + L)).
- Check 1123 `library/gap-l3-closure-check-astra.md` 120-180: JI's extrapolation to all ownerships FAILS as a deduction; the binary mean-to-probability counterexample (lines 130-143); TS3(a,b) HOLDS; the sign-mixture example separating N1 from full TV.

## Step 1. Section 1 (raw-block swap budget)

Further sources read for this step: check 1121 8.2-8.4 (far-edge proof, convexity lower bound on Pbar); check 879 `library/gap-crux-skeleton-check-astra.md` line 100 (electric-only lower bound `Z >= c(beta)^(3V)`, zero spatial mean); check 1453 `library/sa-ym4-lean-trajectory-check-astra62.md` lines 26-35, 72, 107 (beta_K = g_K^(-2) the calibrated root, independent of the physical side; BND-1 `H + lambda K - c_r <= beta_K <= W' + 2BK`, so beta_K -> infinity and beta_K = O(log n)); row 1018's cell convention as recorded in check 1121 line 84 (a link (x, x+e_i) is a core link iff x_i in [0, l-1] and x_j in [1, l-1] for j != i; so every link of a cell-interface hyperplane x_rho = 0 mod l in a direction other than rho is a ring link).

**L13-L18, bound (1). HOLDS.** P has density proportional to prod_c A_c against the product reference of the blocks. The block-z swap S_z is an involution that preserves the reference, so dQ_z/dP = prod_c A_c(S_z(omega, eta)) / A_c(omega, eta). Only c in N_z are changed, and for those T = {z} is admissible in (4.3), so each ratio is at least m_c/A_c = 1 - p_c. Each 1 - p_c lies in (0, 1], so the product of lower bounds is at most min(1, dQ_z/dP). TV = 1 - E_P min(1, dQ_z/dP) in the sup convention. The second inequality is 1 - prod(1 - x_i) <= sum x_i. New as a written bound; it is the bounded conversion that check 1123 (lines 128-143) found missing in Lemma JI.

**L20-L24, one split plaquette (2). HOLDS.** rho is the ring marginal of a gauge-invariant law, so it is invariant under every vertex gauge acting on the ring links at that vertex, in each replica separately. Under Q_z replica one is (omega off z, eta on z). The label changes at least twice along the four-cycle; at one change vertex x only one of the two plaquette links at x is an eta-link, so an independent Haar g_x applied to eta alone enters the hybrid holonomy once (possibly inverted). Hence the hybrid trace has the Haar law, mean 0. With the test tr(U_p)/2 in [-1, 1], TV >= |m_p - 0|/2. The Haar-randomization step is on file (check 1121 8.2 and 8.4, check 1123 line 120).

**L26-L32, pressure bound (3). HOLDS.** Electric-only partition function: integrating time links projects each slice onto gauge-invariant states, so Z_el = z(beta)^(3V) Tr((P_G K~)^t) >= z(beta)^(3V) (constant eigenvector, eigenvalue one; t even, or positivity of the character coefficients). Flipping one spatial bond and all its time translates by the centre element -1 preserves every temporal plaquette (each contains two flipped links) and reverses each spatial plaquette through that bond once; Haar is invariant, so E_el[spatial action] = 0. Jensen: Z_Wilson >= z^(3V). Convexity of log Z with log Z(0) = 0: 6V beta mbar >= log Z >= 3V log z(beta), i.e. mbar/2 >= log z(beta)/(4 beta). On file as row 879 (check line 100); the constants are new. Constants checked by hand: M_2 = 1/4, M_4 = 1/8, M_6 = 5/64 give the terms x/2, x^2/12, x^3/144 with x = 529/400; 0.66125 > 0.661, 0.14575 > 0.145, 0.01606 > 0.016; z > 911/500; q > 0.822/2.822 = 0.29128 > 291/1000; 2 artanh(q) >= 2(q + q^3/3) > 0.598; 0.598/9.2 = 0.065 exactly, strict by q > 291/1000. Guide value (mpmath, 30 digits): log z(2.3)/9.2 = 0.065340 > 13/200 = 0.065 > 81/1250 = 0.0648. The margin is small (5.4e-4) but the hand chain is exact. log z(t)/t nondecreasing by convexity with value 0 at 0: so (3) holds for every beta >= 23/10.

**L34, coverage of partitions. HOLDS.** For each orientation (mu nu) choose rho not in {mu, nu}; the 2-torus of that orientation inside a hyperplane x_rho = 0 mod l consists of ring plaquettes (cell convention above). If no plaquette of it is split, edge-adjacent plaquettes share a block, and connectedness puts the whole 2-torus in one block. So under the stated hypothesis some plaquette of the chosen orientation (one with m_p >= mbar, chosen before the block) is split. Then sum over N_z of E p_c >= mbar/2 > 81/1250 with |N_z| <= 81, so some E p_c > 1/1250 = eps_0(4), against the singleton cases of (4.4) and (4.5). Blocks inside ownership cubes of side l < torus side satisfy the hypothesis. The cell side and partition may depend on K because the bound depends only on beta. Correct scope: ordinary periodic 4D Wilson tori, every side >= 4, even time length (the calibrated n^3 x u and n^3 x 2u qualify: u = n/512 is even since 1024 | n).

**L36-L43, typical pairs (4). HOLDS.** Relative entropy to product Haar gives beta E S <= -log Z^ <= 48 beta V r^2 + 4V log(1/h_r) (angle subadditivity of the bi-invariant metric; 1 - cos(4r) <= 8r^2; 6V plaquettes). Per-plaquette mean deficit of one orientation <= E S/V, so <= 48 r^2 + 4 log(1/h_r)/beta, uniformly in the rectangle. With beta_K -> infinity (check 1453 BND-1) the event {1 - tr U_p/2 <= s} has P-probability -> 1, Q_z-probability = Haar cap mass -> 0 as s -> 0. So TV -> 1 uniformly in plaquette and partition. Then E prod(1 - p_c) <= 1 - TV -> 0, and on {max p_c <= 1 - eta} the product is >= eta^81, so P(max p_c > 1 - eta) -> 1. This upgrades check 1121 8.4's ARGUED typical-pair item to a proof, for split-plaquette ownerships. New. One plaquette concentration as a separate fact is on file (rows 1131, 1282), not re-read here; the displayed proof is self-contained.

**L45, other budgets. HOLDS.** sum over N_z of E p_c <= m_K eps_K; limsup m_K eps_K < 1 contradicts TV -> 1. Cells sharing block z pairwise intersect, so they form a clique: m_K <= D_K + 1. The path-count budget eps <= 1/(2(D+1)) gives m eps <= 1/2.

**L47, scope. HOLDS.** (4.4) implies (4.5) (row 1118 L193; check 1121 correction), so failing (4.5) fails (4.4). The caveats (gauge-aligned exchanges, whole cylinder ends) are stated correctly; nothing in section 1 tests them.

Step 1 verdict: no failing line. Claims 1 and 2 of the brief HOLD.

## Step 2. Section 2 (buffered core, (5))

Sources read: row 1375 `library/gap-seed4-astra62.md` lines 45-55 and 140-144; check 1376 `library/gap-seed4-check-opus.md` S7-S11, S28, S30 (all HOLDS, given rows 1151, 1231, 1339, 1371 and 1153 (5)).

**L51, input. ON FILE, accurately stated.** Row 1375 L47: for beta_j -> infinity in the band, the scaled based chords of a fixed finite connected graph in a contractible box (temporal edges allowed) converge in total variation to three copies of the Gaussian circulation law with a common colour frame; the periodic sums converge to the Brillouin integral (L51), so the limit is the infinite-lattice free field. The band beta_K <= B_0 log n holds on the calibrated trajectory (check 1453 line 107).

**L53-L63, statement (5). HOLDS.** D^(1) <= D^TV pointwise since 0 <= F <= 1.

**L65, the readings. HOLDS.** At fixed R the words lie in one fixed finite graph; BCH and tightness give remainder O_R(beta^(-1/2)) after scaling, so by Slutsky the pair (Z(0), conjugated Z(R)) converges in law to the linear readings. |Z| is invariant under all vertex gauges (common root conjugation) and under electric flips (even crossings; check 1376 S28).

**L67-L72, V_R(s). HOLDS.** In quaternion coordinates beta(1 - tr U_p/2) ~ |z_p|^2/2, so the limit has unit-normalized curl covariance per colour: the (12,12) entry of the exact-2-form projection is (h_1 + h_2)/(h + 2 - 2 cos k_0). The time transform solves (h + 2) g_s - g_(s+1) - g_(s-1) = 1_(s=0); with cosh E = 1 + h/2, E = 2 arsinh(sqrt(h)/2) and g_0 = 1/(2 sinh E) = 1/sqrt(h(h+4)). So the displayed V_R(s) is correct. (Even a wrong overall normalization would only change the constant c_phi, not its sign: for variance c V_R(0) the covariance is ((1+c)^2 - c^2 r^2)^(-3/2) - (1+c)^(-3) > 0.)

**L72-L78, the limit r_phi. HOLDS.** h_i <= k_i^2 and h_1 + h_2 <= h give R(h_1+h_2)/sqrt(h(h+4)) <= R sqrt(h)/2 <= |p|/2. The summation-by-parts bound |a^_R(p/R)| <= C_j R^3 (1 + |p|)^(-j) follows from |Delta^j a_R| <= C R^(-j) and |e^(i p_i/R) - 1| >= 2|p_i|/(pi R). R E(p/R) -> |p|. Dominated convergence after division by R^2 gives r_phi = int W e^(-|p|) / int W, which lies strictly in (0, 1) since W >= 0 is nonzero and integrable.

**L80, covariance and order of limits. HOLDS.** For a centred normal X with covariance Sigma, E exp(-|X|^2/2) = det(I + Sigma)^(-1/2): per colour det = 4 - r^2 for the pair and 2 for one reading, giving (4 - r_R^2)^(-3/2) - 1/8, which tends to c_phi = (4 - r_phi^2)^(-3/2) - 1/8 > 0. Cov(F, G) = E[(m_Omega(F) - EF) G] since G is measurable outside the cell and the cell interior depends on the exterior only through the ring (the cell is seam-free). |E[Y G]| <= E|Y| for 0 <= G <= 1, and Jensen gives E|m_Omega(F) - EF| <= E|m_Omega(F) - m_Omega'(F)| <= D^(1). This is TS3(a,b) (check 1123) applied to one test. The order is lim inf over K first at fixed R, then R: correct as displayed. The refutation of cutoff-uniform lattice-unit clustering with prefactor min(|A|, |B|) follows (support <= C R^3, separation of order R).

**L82, ARGUED. Accurate.** The argument does not reach a cell of physical size R ~ b^K, and the paragraph says so.

Step 2 verdict: claim 3 of the brief HOLDS. The statement is new as written; its inputs are on file (row 1375, check 1376). Physically it is the expected divergence of the lattice-unit correlation length as beta_K -> infinity.

## Step 3. Section 3 (complete faces)

Sources read: check 1527 (ii) `library/gap-agy-seed-approaches-neon-check-astra62.md` lines 45-56 (Theorem 2(1), the handoff with (22.2/25)^(2^j)/22.2 and the B3 enlargement to N = 128B); row 1368 `library/gap-agy-seed-neon.md` lines 278-290 (Corollary 5: 4 | n, integer u >= 3, n >= 34u, s(u; n^3) <= 4/21 imply S_kappa(n/2; (2n)^3) < 0.0324 < 1/25); check 1453 line 72 and check 1527 line 53 (the calibrated root is the least root on the original reference torus, the same at every evaluation side).

**L86-L90, affinity identity. ON FILE (row 1526), rechecked.** a(x, x') = k_2v(x, x')/sqrt(k_2v(x, x) k_2v(x', x')) uses pointwise positivity of k_v; E a^2 = Z_+(4v)/Z_+(2v)^2. E_nu e^(-J) is the four-kernel cycle, also Z_+(4v)/Z_+(2v)^2.

**L92-L96, sandwich (6). HOLDS.** 1 - TV = int min(f, g) <= a; TV = (1/2) int |sqrt f - sqrt g|(sqrt f + sqrt g) <= sqrt(1 - a^2) by Cauchy-Schwarz. Then E a^2 >= E(1 - TV)^2 >= (1 - d)^2 and E a^2 <= 1 - E TV^2 <= 1 - d^2. New as a written two-sided bound; elementary.

**L98-L105, equivalence (7). HOLDS.** Reverse: d <= eta <= 1/8 gives P >= 49/64 > 457/625 on the same side. Forward: (1 + s^2)/(1 + s)^2 >= 457/625 gives 168 s^2 - 914 s + 168 >= 0, so s <= (914 - 850)/336 = 4/21 (Fact PUR, row 1468). n = 512u >= 34u, u >= 3 eventually, 4 | n: Corollary 5 applies. The doubling bound (111/125)^(2^j)(5/111) is check 1527's (22.2/25)^(2^j)/22.2; the B3 multiplier is fixed; so log(1 + s_N(N/512)) -> 0 as j -> infinity, uniformly on the late passing set. P >= (1 + s_N)^(-2) >= 1 - eta^2 and (6) give d <= eta at side l_eta = 128 * 2^(j+1) l, a multiple of 1024, with the same g_0 and the same passing cutoffs. The coupling is the original root at both sides, which is the seed's own convention (check 1453), so the second line is the seed-type statement at side l_eta. The row labels (7) a restatement. It is one: by the lane rule, equivalent is not progress.

**L107-L111, short periods. HOLDS, given row 1375 L144 (check 1376 S30, given row 1153 (5)).** s(2v) is nonincreasing in v since the neutral eigenvalue ratios lie in [0, 1]; P(2v) = (1 + s(4v))/(1 + s(2v))^2 <= 1/(1 + s(2v)); (6) gives d >= 1 - (1 + s(2v'))^(-1/2) -> 1 uniformly on 1 <= v <= v'. Jensen gives E J >= -log P. The only new step is the use of (6). The limitation at L111 is stated correctly.

**L113, ON FILE (rows 1573, 1579). Accurate as a summary.** Not rechecked beyond the identity P = E e^(-J).

**L115-L120, typical log cost. HOLDS.** The complete-face swap has likelihood ratio k(x1,y2)^2 k(x2,y1)^2 / (k(x1,y1)^2 k(x2,y2)^2) = e^(-2J), so E e^(-2J) = 1 and E(1 - e^(-J))^2 = 2 - 2P. On {J > t}, (1 - e^(-J))^2 > (1 - e^(-t))^2. Conversely P >= e^(-t)(1 - nu(J > t)); at t = log(10/9) with tail <= 1/10, P >= 81/100 > 457/625. Forward: on the enlarged side, choose j with 1 - P <= 1/2000. nu(J < -A) <= e^(-2A) by Markov on e^(-2J). The equivalence is over sides and is again a restatement, as the row says.

**L124-L130, one bounded observable. HOLDS.** The signs xi_i of disjoint contractible plaquettes are i.i.d. fair signs under product Haar, gauge and centre invariant. The one-step kernel prod(1 + t xi_i(x) xi_i(y)) = sum_I t^|I| xi_I(x) xi_I(y) is pointwise positive (t < 1) and positive semidefinite with neutral eigenvectors; its v-th power has r = t^v. The squared endpoint law has density prod(1 + r^2 + 2r xi xi)/(1 + r^2)^M with Haar marginals; q_x acts on the sign chaos with factor rho^|I|, rho = 2r/(1 + r^2), so Var q_x(F) <= rho^2 and E|q_x(F) - q_x'(F)| <= sqrt(2) rho -> 0 uniformly in |F| <= 1. Purity ((1 + r^4)/(1 + r^2)^2)^M <= exp(-2 M r^2/(1 + r^2)^2) -> 0 since M r^2 = M^(1/2). (6) gives d -> 1. Smooth version: the tanh functions are mean zero (central symmetry of tr/2 under Haar), independent on disjoint plaquettes, normalized; the eigenvalues t^|I| and hence the purity are unchanged; L1 convergence of the squared endpoint laws at fixed n and the 6e bound on covariances (2e + 2e + 2e) preserve the N1 bound. The example changes the action, as L130 says. Relation to file: check 1123 (lines 168-176 as cited; the sign-mixture example at its TS3 paragraph) already separates the N1 coefficient from mean TV on general bipartite laws; the new content is a realization by positive, positive-semidefinite, neutral transfer kernels on the actual slice space at the actual aspect u = n/512.

Step 3 verdict: claims 4, 5 and 6 of the brief HOLD.

## Step 4. Section 4 (consumers, (8))

Sources read: row 1468 `library/gap-k2-tool-design-fable.md` 126-170 (Q2: contours from 2y to 2y + 2e_mu, M_c = mean of 384 contour holonomies, K = prod exp(kappa Re(M_c V(c)^(-1)))/Zc(kappa |M_c|)); row 1510 `library/gap-seed-solve-fable.md` 223-236 ((FL)); row 1122 `library/gap-l3-direction-fable.md` 60-92 (the table of forms); check 1598 `library/gap-direction6-check-astra62.md` lines 63, 96, 99.

**L134-L146, L157-L159, ON FILE paragraphs. Accurate where spot-checked.** (H-two-col) is as in row 1122 line 74; the 2/9 pass and weak-U(1) failure of row 1573 (2) are as in check 1598 line 99; 2 I_3 = 2 x 0.50546 = 1.0109 (Watson's integral). The repeated-event remark is row 1118 L150. (FL) is as in row 1510 L223-L227, with the joint-law mean.

**L148-L155, identity (8). HOLDS.** A fine gauge at 2y multiplies each contour holonomy starting at 2y on the left (ending at 2y on the right); passages through 2y as an interior vertex cancel. So M_c -> g M_c (resp. M_c g^(-1)), |M_c| is unchanged, and Re(M_c V(c)^(-1)) is unchanged when V(c) -> g V(c) (resp. V(c) g^(-1)). Hence K(g~W, gV) = K(W, V) and, the fine Wilson law being gauge invariant, mu^(gV) = g~_* mu^V. Differentiating the quotient gives Cov(f, sum over c at y of <S_c, xi_c>); differentiating the pushforward gives E D_(2y,A) f. Cauchy-Schwarz over the 8 fine links at 2y (each tangent of norm |A|) and Jensen give the factor 8. Correct and elementary (a Ward identity). The remark that it does not reach a single-bond score is correct. New as written; no bearing on (FL) beyond the vertex directions.

**L161, ARGUED (selection). Accurate.** The split-plaquette test, the pressure bound, (6)-(7) and (8) are group-blind and dimension-blind; the row says none is a selective input and that nothing withdraws the pause under WB1-WB3.

Step 4 verdict: claim 7 of the brief HOLDS.

## Step 5. Which forms of (W-mix) the row closes

Closed (as obstructions, with these classes):
- (H-swap) of row 1118, i.e. the premise (4.4)/(4.5) of CONV-swap: false at every beta >= 23/10 on ordinary periodic 4D Wilson tori (sides >= 4, even time length), for every partition of the usual separating ring into raw-link blocks with incidence <= 81 and no block containing a whole coordinate 2-torus of the ring; cell side and partition may vary with K. At the late calibrated roots (n^3 x u, n^3 x 2u) the same holds for any split ring plaquette, with max incident p_c -> 1 in probability, and any per-cell budget with limsup m_K eps_K < 1 fails. This extends Proposition J (check 1121: forced ownership, window [2.3, 2.6]) and closes, for this family, the gap check 1123 found in Lemma JI's "no other ownership helps". Not covered: gauge-aligned or smoothed exchanges, exchanges of whole cylinder ends, non-raw variables, blocks containing a whole ring 2-torus.
- Two-sample core forms at a cell of fixed lattice size (H-two in TV, and the N1-type coefficient with the supremum over core-supported neutral tests outside the expectation): bounded below by c_phi > 0 in the order lim inf_R lim inf_K; cutoff-uniform lattice-unit exponential clustering is false. Not covered: cells of physical size, a comparison of c_phi with a consumer tolerance, (H-two-col) with a fixed outside.
- Whole-face two-sample TV at half-periods <= floor(beta_K^alpha), 0 < alpha < 1/16: tends to one.
- At the target aspect: whole-face mean TV <= eta (any eta <= 1/8) and the log-cost tail nu(J > log(10/9)) <= 1/10 are each equivalent to (PUR-io) over the allowed physical sides. These are restatements, so a proof of either is no progress over the seed.
- The inference "positivity + neutrality + one-observable (N1-type) whole-face mixing => passing purity" is false (non-Wilson positive neutral kernels at the actual aspect).

Left open (the row says so): Wilson whole-face mixing at the physical period (equivalent to the seed); the signed-mean and angular B_K bound of row 1573 (2) (its equivalence with (PUR-io) unknown); the Rbar form of (H-ent); (H-two-col); (DS-W) of row 691; (CONV-two); (FL) beyond vertex-gauge directions; (CM_k); (T-mix); (PUR-io); the gap.

New in this row: bound (1); the extension of Proposition J via (1)-(3) to all beta >= 23/10 and all nonwrapping raw-link ownerships; (4) and the general-budget corollary; (5) with its free-field computation; (6); the use of (6) in (7) and at short periods; E e^(-2J) = 1 and the tail equivalence; the transfer-kernel realization of the N1 separation; (8). On file: the mixed-plaquette Haar law (check 1121 8.2/8.4, check 1123, rows 1131/1282), the electric-only pressure bound (row 879), beta_K -> infinity and beta_K = O(log n) (check 1453), the fixed-graph Gaussian limit (row 1375, check 1376), the short-period asymptotic (row 1375 L144, row 1153 (5)), the affinity identity (row 1526), P = E e^(-J) (row 1573), Fact PUR (row 1468), Corollary 5 and the enlargement handoff (rows 1368, check 1527 (ii)), the N1-versus-TV separation on general laws (check 1123).

Who checked what: every line of the checked file was read and each PROVED item checked by hand by Claude Opus 5.5 (high), a cross-provider check of a gpt-6.2-astra max text. ON FILE items were checked against their cited files only at the lines named above. One mpmath evaluation of log z(2.3)/9.2 was a guide only; the hand chain carries the proof. Nothing is formalized. No other file was written; nothing committed or pushed.

## RESULT

Row 1603 checked line by line by Claude Opus 5.5 high (cross-provider). No line FAILS; no correction needed.
(1) beta >= 23/10 swap-budget failure: HOLDS (bound (1), split-plaquette (2), pressure (3) with exact constants, plane coverage), on ordinary 4D tori with even time length, for nonwrapping raw-link ownerships with incidence <= 81; extends Proposition J.
(2) max incident p_c -> 1 in probability at the calibrated roots: HOLDS (beta_K -> infinity, check 1453).
(3) Buffered fixed-size core, (5): HOLDS in the order lim inf_R lim inf_K; V_R(s), r_phi in (0, 1) and c_phi > 0 verified.
(4) Whole-face TV -> 1 at half-periods <= floor(beta_K^alpha), alpha < 1/16: HOLDS given row 1375 L144.
(5) Mean-TV and log-cost-tail equivalences with (PUR-io) over sides: HOLD; restatements, no progress.
(6) Positive neutral transfer counterexample to the one-observable inference: HOLDS (non-Wilson kernels).
(7) Q2 identity (8): HOLDS; vertex-gauge directions only.
Overall: outcome (c) is upheld as a scoped obstruction. It closes the microscopic forms (raw-block H-swap, fixed-lattice-size cells, short periods) and shows the bounded target-aspect forms equal the seed.
It does not show that any physical-scale form of (W-mix) fails. Open: physical-period Wilson mixing, Rbar, (H-two-col), (DS-W), (FL), (PUR-io), the gap.
