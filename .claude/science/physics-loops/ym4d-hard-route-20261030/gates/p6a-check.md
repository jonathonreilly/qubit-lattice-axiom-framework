lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:20Z

First failing step: none.

# p6a-check: library/port/p6-correlation.md, first half (5.6:lem-weight, 5.5:lem-weight, 5.3:lem-driven-flow)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, 2026-11-06. Repository commit b05bc0e47. Source: CA-I, CA-II and CA-III fetched by raw URL at upstream 31a47c543775 (CA-II sha256 6a1f74b05f74...4b2b8f, 145,624 lines), and the outline YM4_sketch_500.tex for searches. One reading, not an audit, not human review. Credit: the lemmas and proofs checked here are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban's papers (CMP 98, 102, 109, 116, 119, 122a/b) are cited inputs of their proofs. The port is Codex's.

Kind of result: a check of their proofs as ported, plus a check of the port's fills, corrections and input tables. Nothing here is a new proof. No numerics were run.

## Verdicts

| Statement | Port lines | Verdict |
|---|---|---|
| 5.6:lem-weight (B2a) | 19-169, 733-1191 | **ADVANCE (faithful).** Proved as an implication from (H_o), (pi1)-(pi3) and its stated decay hypothesis. Its actual-term supplier B1 (5.6:prop-polydisc-holomorphy) is "Proof outstanding" at CA-II 46167, as the port says. Correction W6-C1 is right. |
| 5.3:lem-driven-flow (B4a) | 643-678, 2534-2643 | **ADVANCE (faithful).** A closed elementary implication from its displayed hypotheses; both 5.2 lemmas it uses are proved in full in CA-II. |
| 5.5:lem-weight (B2b) | 172-457, 1193-2527 | **ADVANCE as an implication (faithful), with inventory repairs F1-F7 below.** Every step I redid holds given the W5 inputs plus the inputs named in F1-F5 and F7. Correction W5-C3 (their (e) overclaims its block total) is right, and so are W5-C1 and W5-C2. |

All 17 quoted LaTeX blocks of the first half are exact copies of CA-II (table below). By the port's own convention (port line 731) every result invoked in a quoted proof is kept as a named hypothesis. So no step fails. The findings are about the port's input inventory, which the open-input lists will be built from, and about unstated constants.

## Findings (ranked by what each breaks)

None is fatal. None changes a printed constant except the optional repair in F6.

- **F1 (B2b (e); port line 2320 and table 1195-1214). An input of (e) is missing from the inventory and I could not locate it in the account.** Step: CA-II 36600-36607 takes the core and short-single paired bounds (5.5:eq-machine-differences-2)-(3) from "the paired rows of the two-machine comparison at the rim ... as stated there with rho replaced by Theta rho". These include |delta i_y| <= C_I''(S + n a) nu^3 (Theta rho)^2 (1 + Theta rho) t^{4+a}. (The own-read bound (4) comes from input (i)(e), which the port does name.) Step 4' takes two more items from the same source: its paired counterterm-coefficient row (36656) and the off-chart clause of its paired Wilson row (36710-36712). What is wrong: this statement is not among the inputs (i)-(v) of 5.5:def-weight-inputs, nor among the "two further results" (35226-35228). The phrase "comparison at the rim" occurs only in this proof (36526-36738) and at 40464, in CA-I, CA-II, CA-III and the outline. The nearest candidates are the unstated "lemma stating the pair bounds (A^x), (M^x), (Pi^x), (I^x), (d^x), (F^x), (W^x)", which 5.5:lem-pair-bounds assumes as its hypothesis (b) (41461) with no locus, and the two-run comparison inside the proof of 5.2:prop-two-slot-preparation (13616). The W5 table names neither. W5-pair covers closure under the moves and the paired-chart majorants, not these quantitative rows. Repairable: add an input "W5-rim: paired rows of the two-machine comparison at the rim (Cauchy, counterterm-coefficient, core with remainder line, Wilson with off-chart clause), read at Theta rho; locus not found in CA at 31a47c543775". Mark it open.
- **F2 (B2b (c), (c'), (d); port lines 1865, 1928, 1947 and W5-geometry). Their text cites in a circle; the port's "assumed" is right, but it should say these inputs have no supplier.** Step: the proofs take four facts from "the facts stated with Definition 5.5:def-data-factor". They are: (i) "square in O+ or exceptional", with rho(square) >= R_k - 4 and k - n_0 + 1 <= N_* + rho (CA-II 36224-36225, 36267-36268, 36297); (ii) s = 0 on O+ (36439); (iii) the level bound n_0 + 1 (36161); (iv) "a residual cell ... has t <= n_0 - 3" (36243). What is wrong: the definition says its facts (f1)-(f2) "are established in the weight lemma" (34610-34611), and the weight lemma only uses them. Facts (iii) and (iv) are not in the definition at all. "Residual cell" and the constant N_* are defined nowhere in CA-II (grep finds only these uses). Repairable: list them in the open-input inventory as open statements of the account with no supplier, not as cited results.
- **F3 (B2b (a2), (a3); port lines 1302, 1387). The weight lower bound w >= 1 is used with a wrong pointer.** The proof cites Notation 5.5:not-weight-notation, which gives only upper bounds on w (CA-II 34103-34112). The (a3) step 2(2c. + 5.6 K) w_Q alpha_Q <= K_loc w_Q alpha_Q also uses w_Q >= 1 silently. Repairable: name "weights are >= 1" as part of W5-setting (the weight definition of the large-field operations).
- **F4 (B2b (a3); port lines 1335, 1352). The bound of w alpha by A_w(gamma) is unnamed.** The uniqueness smallness 1.4 w(Delta) alpha~ <= 2.8 A_w(gamma) needs w(Delta) alpha_{0,l(Delta)} <= A_w(gamma). Display (5.5:eq-box-regularity-3) needs w_Q alpha_Q <= (12/5.6) A_w(gamma). The account states w_Q alpha_Q <= 2 A_w(gamma) only elsewhere (CA-II 42829, 42855-42857, "the statement on localisation constants of cubes of level at least p"). With that factor 2 both spends still close: 11.2 <= 12, and 5.6 A_w <= K_loc A_w because K_loc >= 24. Repairable: name that statement as an input.
- **F5 (B2b (a2); port line 1279).** The bound a_flat <= 5 A_w(gamma) is stated without a source. Repairable: name it under W5-local or W5-setting.
- **F6 (B2b (b) step (iv); port lines 1650-1665). An unstated condition 10 C_M M >= 1.** The step (10 C_M M)^{-2-a/2} >= (10 C_M M)^{-5/2}, and its partner with exponent -1/2, hold only if 10 C_M M >= 1. Here C_M = 2d C_a/c_3 (CA-II 4742), and no lower bound on C_a/c_3 is stated among the weight constants. If x := 10 C_M M < 1, the printed argument gives only the lower bounds 4C(kappa) x^{(1-a)/2} n and 2C' x^{(1-a)/2} n z^2 t^4 for the two halves. For small x these fall below the trivial bound 2C(kappa) n + C' n z^2 t^4 that they must dominate, so the argument as written does not cover x < 1. Repairable: in C_I' (CA-II 34716) replace (10 C_M M)^{5/2} and (10 C_M M)^{1/2} by max{1, 10 C_M M}^{5/2} and max{1, 10 C_M M}^{1/2}. Then the step holds for every value, and no other constant moves. Very likely moot, since M >= 1 and these constants are normally >= 1.
- **F7 (B2b (b); port line 1571). Wrong attribution.** The proof takes eta_p <= t^5 for the near constituents of straddling cores "by the own-read membership hypothesis". Input (i) of 5.5:def-weight-inputs does not contain it. The lemma's own statement derives it differently: X does not meet the block (2 nu + 3 < L^{nu-1} for nu >= 2, which I checked), then the own-level distance bound, then a "level floor". That floor is not in the explicit floor list of 5.5:def-weight-constants. Definition 5.5:def-weight-constants (iii) assumes it as "the row of the near constituents of straddling cores". Repairable: carry it under W5-rows as that assumed row.
- **F8 (stale standings, no proof effect).** Port line 3 says "Not yet checked by another model" (this check now exists). Port line 13 lists P5 as "ported", but gates/p5-induction-gate.md checked it (first failing step none). Port line 15 says library/ph.md is absent; at b05bc0e47 it exists (Codex, ends in **Open lemma**; gates/ph1-gate.md). B1 therefore stays open, so the port's treatment of B1 is unchanged.
- **F9 (cosmetic).** The B4a header (port line 645) repeats the B2 sentence about "the weight machinery"; the driven flow lemma has none. W5-F3 (port line 2197) says "in the exceptional case", but N_0(t) >= 2 holds in all of case (ii), old blocks included. 5.6:lem-tree-cells assumes an acyclic T ("each bond ... once in each direction"), while "tree graph" allows cycles; walking a spanning tree gives the same bound, and the only use takes an optimal, hence acyclic, T.

Confirmed corrections and fills: W6-C1 (zero decay rate), W6-F1-F3, D-F1, D-F2, W5-C1 (degree majorisation; min(1, a^2 u^2) <= a^2 min(1, u^2)), W5-C2 (constant aliases), W5-C3 (scope of the (e) block total), W5-F1-F4. Each is correct as written.

Side observation for p6b, not this port's text. The copy of 5.5:lem-weight (c) quoted in section 5.2 (CA-II 13806-13809) lists a third kind of preparation, "m for the completed preparation of a live region (Y,m)". The 5.5 statement and proof define t_c only for arrests and for running or sibling preparations. A consumer that reads the 5.2 copy reads more than the 5.5 proof shows, unless such a preparation can never carry thin strata in the doubled block; Notation lines 34117-34121 suggest it cannot. I did not settle this.

## Quotation check

Every fenced `latex` block of the port's first half (port lines 24-2634) was compared line by line with CA-II by a plain text comparison. All 17 are exact copies:

| Port lines | CA-II lines | Content |
|---|---|---|
| 24-169 | 45154-45299 | 5.6:lem-weight statement |
| 177-457 | 35258-35538 | 5.5:lem-weight statement |
| 648-678 | 26201-26231 | 5.3:lem-driven-flow statement |
| 750-815, 831-883, 891-951, 961-1069, 1079-1188 | 45301-45366, 45425-45477, 45583-45643, 45774-45882, 46020-46129 | 5.6 proofs (a), (b), (c), (d), (e)-(f) |
| 1223-1306, 1314-1429, 1439-1725, 1741-1953, 1961-2194, 2206-2517 | 35543-35626, 35628-35743, 35748-36034, 36037-36249, 36251-36484, 36486-36797 | 5.5 proofs (a1)-(a2), (a3)-(a4), (b), (c), (c')-(d), (e) |
| 2543-2634 | 26233-26324 | 5.3 proof |

A text comparison checks quotation only. The mathematics was redone by hand, as follows.

## B2a: 5.6:lem-weight (port lines 19-169, 733-1191)

- (a), CA-II 45301-45366. The slice G_s is continuous and separately holomorphic on P_W(e^{kappa_1}) with |G_s| <= b, since [0,1]^{V\W} x P_W(e^{kappa_1}) lies in P_V(e^{kappa_1}). 5.6:lem-cauchy-estimates (45008-45152; I reread its proof: iterated Cauchy formula by induction on |W| with Fubini, differentiation under the integral, then r_w -> R) gives |d^W F_t| <= b r(kappa_1)^m on the real cube. The probability measure costs 1, and the supremum over data is taken last, so no datum regularity is used. 5.6:lem-cauchy-factor (44941-45006): x/(x-1)^2 <= e/x for x >= e reduces to x(sqrt e - 1) >= sqrt e, which increases in x; at x = e it is (e-1)^2 >= e, true since e > 8/3 > 21/8 > (3 + sqrt 5)/2. Correct.
- (b), 45425-45477. (pi1) gives |W(p)| = n. (pi2) gives at most lambda^n pieces, since ordered partitions are maps N' -> I. With r <= 1 the sum is <= b (lambda r)^n, and both floors are the stated logarithms. Correct.
- (c), 45583-45643. (pi3) gives exactly the hypotheses of (TL)_{c'} with Y_1 = Y_1(t), so l(Y) <= l(Y_1) + c'n and -a l(Y_1) <= -a l(Y) + a c' n. With (b) this is the first inequality of (5.6:eq-weight-d). Also 16 kappa + 1 >= 1 + log 3 + 8 kappa iff 8 kappa >= log 3, which covers c' = 1 too. "a <= 2 kappa" is written as a hypothesis in the statement. Correct, with W6-C1 for a = 0 (the source's "forces b = 0" at 45597-45598 needs a > 0).
- (d), 45774-45882. A path in Y from a component C_i of Y \ Y_1 first leaves C_i into Y_1, so each C_i meets the outer boundary of Y_1 and its least such cell roots it. The code (root set, sizes, rooted sets) is injective. Counts: at most 2^{D_d #Y_1} root sets, at most C(n-1, q-1) <= 2^{n-1} size vectors, and at most (4 D_d)^{m-1} rooted connected sets each. The last bound is 5.6:lem-rooted-sets (45645-45701): a depth-first word of 2(m-1) letters and m-1 neighbour ranks; on an up-step the parent is the cell before the first visit, so the code determines C. Then the sum is at most 2 * 2^{D_d #Y_1} b for kappa_1 >= 1 + log(16 lambda D_d). 5.6:lem-tree-cells (45703-45772) gives #Y_1 <= 3^d(2 d^fr + 1) <= 3^d(2 d^sub + 1), and the absorption holds iff eps a >= 2c''. Correct.
- 5.6:lem-tree-length-adjunction (45479-45581). Order the new cells breadth-first. (i) Each new cell is reached by a monotone path of at most dM bonds. (ii) Under face adjacency, at most M - 1 bonds inside the old cell plus one bond across the face. Correct.
- (e)-(f), 46020-46129. F_y is the product-form piece with base point 0. d^y kills F(1;d) when y is nonempty. E^1 = E^0 + I holds in each coordinate, the operators commute on C^infinity of the closed cube (Clairaut, Fubini), and expanding the product gives the identity. Correct. (f): I found no parameter beyond those listed.
- Input table (port 735-743): the loci are right. (pi1)-(pi3) are hypotheses in the source's own words (44846-44847).

## B4a: 5.3:lem-driven-flow (port lines 643-678, 2534-2643)

- omega_k, v_k >= 0. The identity history is admissible, so the hypothesis supplies a driver bounded by v_k; hence d_k >= 0.
- Induction: |xi_j| <= (4/3)|zeta| < (4/3) rho <= (1/2) d_*(K-1) <= (1/2) d_j. So xi lies in the closed half polydisc, and zeta_{k+1} is holomorphic on the same disc D(0, rho).
- f-increment: integrate along the segment in the convex half polydisc. 5.2:lem-polydisc-gradient (CA-II 3023-3087, reread: rescale, recentre each coordinate by a Moebius map with phi'(0) = 1 - |a_j|^2 >= 3/4, rotate phases, apply one-variable Schwarz) gives sum_j d_j |d_j f| <= (4/3) omega, with no dimension factor. Hence (4/3)(4/3) = 16/9, the printed coefficient.
- Driving increment: 5.2:lem-disc-bounds (a) (CA-II 2974-3021) gives (2 v_k / rho)|zeta|.
- Summation: |zeta_{k+1} - zeta| <= (sum_i d_i)|zeta| <= (1/3)|zeta|. D-F1 and D-F2 are correct.

## B2b: 5.5:lem-weight (port lines 172-457, 1193-2527)

### (a1)-(a4) (CA-II 35543-35744)

- (a1): the source-class condition with arrest factor F <= 1 + 2 beta = 1.4 (beta = 1/5) and w^+ r_2(l^+) <= theta_2. These are cited scaffold facts at 35553-35567, inside the W5-local and W5-setting loci.
- (a2): finer constraints are functions of coarser ones, so a critical point under the coarse data is critical under its own B*_j data. Uniqueness modulo gauge (Balaban CMP 109 (3.39), CMP 102 Theorem 1) gives W' = W^g; then n(g) <= 2 and 2.8 * 5/4 + 1/4 = 3.75 <= 4. This uses w >= 1 (F3) and a_flat <= 5 A_w (F5).
- (a3): 1.4 * 2 = 2.8; 2 * K_ax M * 2.8 = 5.6; CMP 102 Proposition 9; then BCH gives 2(2 c. + 5.6 K_h K_ax M C_M^av) w_Q alpha_Q <= K_loc w_Q alpha_Q (11.2 <= 12). The four smallness spends are paid by K_loc A_w <= c_h with K_loc >= 12 C_M^av >= 24. This uses F3 and F4.
- (a4): 4 C_M^av w alpha~ (l_i/l_l)^2 <= 8 C_M^av w_Q alpha_Q t_p^2 L^{2(i-j)} <= c_1 a_Q t_p^2, since l(x) >= p and K_loc >= 8 C_M^av; and |e_rim| <= 2d(1+|b-y|) + d|b-y| <= 4d(1+|b-y|) times c_1 a_Q t_p^2. Correct.

### (b) (CA-II 35748-36034)

- Own box: the sides are <= max{(2 nu + 3) L^{-(nu-2)}, 1 + 5 L^{-(nu-2)}} <= 13/8, so Q_v has at most 7 cubes a side and Q_v^(1) at most 9. The reach is 6/L < 1, so w_{Q_v} <= w^v(y).
- Majorants: with t_p = Lt and Theta >= 2 c_1 K_loc L^3 alpha_{0,n} w^v / a_n, the two displayed inequalities are equalities in the worst case. They give |B^ax| <= L^{-1}|B^ax|_*, |F| <= |F|_*, |e_mu| <= |e_mu|_* (since c_1 >= 1), and |e_rim| <= |e_rim|_* for cores. For singles the rim bound holds with D_X in place of D; the rim is used only for cores.
- Short single: on |sigma'| < S*, |sigma' B^ax| < alpha_{3,j}; with phi'(0) = 0, lem-disc-bounds (b) gives 2n S*^{-2}.
- Rim (iii): kappa d + delta_0 M (nu - 1 - d)_+ >= kappa d/2 + mu_0(nu - 1); D <= 5M nu; (5M nu)^{d+1} L^{(a-5)(nu-1)} is bounded. Correct.
- Regimes (iv): S* <= 1 for a read core forces C_M D t^2 z > 1/2, and then t^2 > (10 C_M M nu z)^{-1}. The two halves of C_I' dominate 2C(kappa) n + C' n z^2 t^4 under F6. The complement gives S* >= 2.
- Degree (v): z^2(1+z) <= Theta^3 rho^2 (1 + rho); S*^{-2} = Theta^2 x_v; W5-C1's three-case check is right. "(b')" at 36026 is a stale label, read correctly by W5-C1.

### (c) (CA-II 36037-36249)

- Step one: the comparison of X_a with X_c gives dist_m(y, X_a) >= 3 when l(y) > k_a, by k_c < k_a, by separation R >= 38, or by the three sub-cases 3 R_m, L, 3. With n <= l(y), dist_{l(y)} <= dist_n < 1, which forces t(Delta) = k_a >= l(y).
- Step three: n_0 - 1 < n_0 <= t_inner <= h_outer < k_0(outer) <= n_0 - 2 is absurd, so the preparation is unique.
- Steps four to six follow from separation, nesting order, the layer statement and the facts of F2. The logic is right given W5-geometry and F2.

### (c') and (d) (CA-II 36251-36484)

- (i): (6L)^d + 2 * 6^d <= 2(7L)^d; w^3 <= L_o^{6s}, or w^3 <= L^{3 N_0(t)} <= L^{12}(T_k + 3 + c_{k-t})^{6r} <= C_pr e^{rho - 2}.
- (ii): substituting m = k_0 + q and using L_o^6 L^{-4} <= (27L)^{-1} gives a series <= 27/26. Also L_o^{6(N_0 - 1)} <= L^{4 N_0} and n_0 - k_0 <= N_0(t), so the sum is <= 3 * 7^d L_o^6 L^{d N_0}. With y = L^{N_0 - 1} < L max{1, T^r}, y^d <= y_*^d + L^d 2^{dr} b_t^{dr}, which gives C_tile e^{rho - 1}.
- (d): group by the anchor's unit cell; w^v(y) <= w^v(Delta'); kappa_R^act and linearity give a total <= kappa_R c_W^3 K N_0 <= l^2 N_0. Then L_o^{6s} d <= l^2 <= L_o^{6s} d#, using L_o^{6s} <= K# in both cases ((f1) at O+, s <= N_0(k) at an exceptional block). Finally a + b e^u <= 1 + (a + b) e^u, and delta_P w / 8 >= 1 suffices (the source asks for >= 2). Correct.
- W5-F2, W5-F3, W5-F4 and W5-C2 are correct.

### (e) (CA-II 36486-36797)

- Step 3: the Cauchy bounds, the three Schwarz bounds and the vanishing derivatives at the base point all pass to the difference of two bounded holomorphic functions. The companion identity (5.5:eq-machine-differences-5) holds since beta is linear. In Step 5, N_0/E_0 = c_alpha C_R e^{C_2 kappa_1} theta(square). Correct.
- W5-C3 is right. The statement excludes the n*a companion item at nu <= 2 with chart radius > 1 ("for that item no claim is made", 35489-35493). Yet the closing sentence "Consequently ..." (35496, port line 415) and the proof's last sentence (36789-36791) claim the block total for all pieces. In that sub-case only the raw bound C n alpha_{3,j}^{-2} a holds (36708-36725), without the factor (C D Theta a_n t^2)^2, so the block total needs W5-low.
- The per-unit paired bounds rest on F1.
- Closure under M8 is "by construction" in the proof (36490) and in input (iii) (35170-35171); the port keeps it as assumed. No issue.

## What stays open

The three statements are checked as implications. What they rest on is open:
- B1 (polydisc holomorphy of actual terms; library/ph.md ends at an open lemma) and (pi1)-(pi3) for B2a;
- the drivers q_{k+1} at the consumer for B4a;
- for B2b, every W5 input. These include the CMP 119 p.276 transfer (printed without proof), the unwritten 5.11:lem-sixth-family behind C_M^av, W5-low for the full (e) total, and the inputs of F1 and F2, which have no supplier in the account.

Checked line by line by Claude (Mini worker).
