lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:20Z

# p6a-check: library/port/p6-correlation.md, first half (5.6:lem-weight, 5.5:lem-weight, 5.3:lem-driven-flow)

Status: in progress (started 2026-11-06T05:20Z). Sections are written as the check proceeds.

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session. Repository commit b05bc0e47. Source: CA-I and CA-II fetched by raw URL at upstream 31a47c543775 (sha256 of CA-II 6a1f74b05f74...4b2b8f; 145,624 lines). One reading, not an audit, not human review.

## Quotation check (all three statements)

Every fenced `latex` block of the port in its first half (port lines 24-2634) was compared line by line with CA-II by a plain text comparison. All 17 blocks are exact copies of the source:

| Port lines | CA-II lines | Content |
|---|---|---|
| 24-169 | 45154-45299 | 5.6:lem-weight statement |
| 177-457 | 35258-35538 | 5.5:lem-weight statement |
| 648-678 | 26201-26231 | 5.3:lem-driven-flow statement |
| 750-815, 831-883, 891-951, 961-1069, 1079-1188 | 45301-45366, 45425-45477, 45583-45643, 45774-45882, 46020-46129 | 5.6 proofs (a), (b), (c), (d), (e)-(f) |
| 1223-1306, 1314-1429, 1439-1725, 1741-1953, 1961-2194, 2206-2517 | 35543-35626, 35628-35743, 35748-36034, 36037-36249, 36251-36484, 36486-36797 | 5.5 proofs (a1)-(a2), (a3)-(a4), (b), (c), (c')-(d), (e) |
| 2543-2634 | 26233-26324 | 5.3 proof |

So the check below is a check of the account's own proofs as ported, plus the port's annotations (fills, corrections, input tables). A text comparison is a check of quotation only; it proves nothing about the mathematics.

## B2a: 5.6:lem-weight (port lines 19-169, 733-1188)

Kind: check of their proof. Verdict: **faithful; proved as an implication from its named inputs.** First failing step: none.

What I redid by hand:

- (a), CA-II 45301-45366. The slice G_s is continuous and separately holomorphic on P_W(e^{kappa_1}) with |G_s| <= b, since [0,1]^{V\W} x P_W(e^{kappa_1}) lies in P_V(e^{kappa_1}). Lemma 5.6:lem-cauchy-estimates (45008-45152; I reread its proof: iterated Cauchy formula by induction on |W| with Fubini, then differentiation under the integral, then r_w -> R) gives |d^W F_t| <= b r(kappa_1)^m on the real cube. The probability measure costs 1. The supremum over data is taken last, so no datum regularity is used. Lemma 5.6:lem-cauchy-factor (44941-45006): x/(x-1)^2 <= e/x for x >= e reduces to x(sqrt e - 1) >= sqrt e, increasing in x, and at x = e to (e-1)^2 >= e, true since e > 8/3 > 21/8 > (3+sqrt 5)/2. Correct.
- (b), 45425-45477. (pi1) gives |W(p)| = n; (pi2) gives at most lambda^n pieces (ordered partitions = maps N' -> I). With r <= 1 the sum is <= b (lambda r)^n. The two floors are the stated logarithms. Correct.
- (c), 45583-45643. (pi3) gives exactly the hypotheses of (TL)_{c'} with Y_1 = Y_1(t), so l(Y) <= l(Y_1) + c'n, and -a l(Y_1) <= -a l(Y) + a c' n. Combined with (b) this is the first inequality of (5.6:eq-weight-d); the floor is the stated logarithm. The comparison 16 kappa + 1 >= 1 + log 3 + 8 kappa iff 8 kappa >= log 3 is right, and it covers the c' = 1 case too (14 kappa >= log 3). The "a <= 2 kappa" reading needs beta <= 1/3, which the statement writes as a hypothesis ("With lambda = 3, a <= 2 kappa ..."), so nothing is claimed beyond it.
- (d), 45774-45882. The rooting argument is right: a path in Y from a cell of a component C_i of A = Y \ Y_1 to Y_1 leaves C_i first into Y_1, so each C_i meets the outer boundary of Y_1, and the least such cell roots C_i. The code (root set, sizes, rooted components) is injective. Counts: at most 2^{D_d #Y_1} root sets, at most C(n-1,q-1) <= 2^{n-1} size vectors, at most (4 D_d)^{m_s - 1} rooted connected sets each (5.6:lem-rooted-sets, 45645-45701: depth-first walk, a word of 2(m-1) up/down letters and m-1 neighbour ranks; the parent on an up-step is the cell before the first visit, so the code determines C). Product <= 2^{D_d #Y_1}(8 D_d)^n. Geometric series <= 2 when kappa_1 >= 1 + log(16 lambda D_d). Prefactor: 5.6:lem-tree-cells (45703-45772) gives #Y_1 <= 3^d(2 d^fr + 1) <= 3^d(2 d^sub + 1), so 2^{D_d #Y_1} <= e^{c''_d} e^{2 c''_d l(Y_1)}, and e^{-(a - 2c'')l} <= e^{-(1-eps) a l} iff eps a >= 2 c''. All correct.
- 5.6:lem-tree-length-adjunction (45479-45581), read for (TL)_{c'}: breadth-first order from Y_1; (i) each new cell is joined by a coordinate-monotone path of at most dM bonds (each coordinate of the nearest site moves by at most M, since |a_mu - a'_mu| <= 1); (ii) under face adjacency a path of at most M-1 bonds inside the old cell plus one bond across the shared face, all inside the union. Correct. No claim for d^sub under closure-touching, as the source says.
- (e)-(f), 46020-46129. The bound: F_y is the product-form piece with W = y and base point 0, so (a) applies; for the second choice of N(F), d^y kills the constant F(1;d) when y is nonempty. The identity: E^1 = E^0 + I in each coordinate, operators of distinct cells commute on C^infinity of the closed cube (Clairaut, Fubini), expand the product, and the y-summand is F_y. Correct. (f) is a reading of the constants of (a)-(e) and the five lemmas; I found no other parameter.

Port annotations:

- **W6-C1 (port line 954) is a correct correction.** CA-II 45597-45598 says that l(Y_1(t)) = infinity "forces b = 0". That holds only for a > 0. For a = 0 the factor e^{-a l} must be read as 1 on both sides, and then (c) is (b). The repair changes no constant.
- W6-F1, W6-F2, W6-F3 are correct fills of steps the source writes out.
- Input table (port lines 735-743): loci checked. B1 = 5.6:prop-polydisc-holomorphy (46131-46165) is "Proof outstanding" at 46167, as the port says, and (H_o) is a hypothesis of the lemma, not a consequence of anything proved. (pi1)-(pi3) are hypotheses by the source's own words at 44846-44847 ("They are not proved here and enter as hypotheses wherever they are used").

One cosmetic point, not a failing step: 5.6:def-linear-sizes defines a "tree graph" as any finite connected subgraph, not an acyclic one, and the proof of 5.6:lem-tree-cells says the depth-first walk crosses "each bond of T ... once in each direction". For a T with a cycle that is false, but walking a spanning tree gives at most 2|T| steps and the same bound. The consequence (the only use, in (d)) takes an optimal T, which is acyclic. Nothing changes.

## B4a: 5.3:lem-driven-flow (port lines 643-678, 2534-2643)

Kind: check of their proof. Verdict: **faithful; proved as an implication from its displayed hypotheses.** First failing step: none.

What I redid by hand (CA-II 26233-26324):

- omega_k >= 0 and v_k >= 0: the identity history is admissible, so the adaptive hypothesis gives a driver bounded by v_k on a nonempty disc. Hence d_k >= 0, which the last step needs.
- Induction P(k). The point xi = (zeta_j(zeta))_{j<=k} has |xi_j| <= (4/3)|zeta| < (4/3) rho <= (1/2) d_*(K-1) <= (1/2) d_j, from (8/3) rho <= d_*(K-1). So xi lies in the closed half polydisc, the composite with f_{k+1} is holomorphic, and zeta_{k+1} is defined on the same disc D(0, rho).
- f-increment: the segment from 0 to xi lies in the convex half polydisc; |f(xi) - f(0)| <= max_j |xi_j| times sup of sum_j |d_j f|. 5.2:lem-polydisc-gradient (CA-II 3023-3087, reread: rescale to the unit polydisc, recentre each coordinate by a Moebius map with phi'(0) = 1 - |a_j|^2 >= 3/4, rotate the phases, Schwarz for one variable) gives sum_j d_j |d_j f| <= (4/3) omega. Dividing by d_*(k) <= d_j gives (4/3) omega_k / d_*(k). Times (4/3)|zeta| this is (16/9)(omega_k/d_*(k))|zeta|, the printed coefficient. Summing per-coordinate Cauchy bounds instead would give a factor k+1; the source correctly avoids it.
- Driving increment: 5.2:lem-disc-bounds (a) (CA-II 2974-3021; removable singularity of (q(z) - q(0))/z, maximum principle on |z| = r < rho, then r -> rho) gives (2 v_k / rho)|zeta|. The radius is rho at every step.
- Summation: |zeta_{k+1} - zeta| <= (sum_{i<=k} d_i)|zeta| <= (1/3)|zeta|, using d_i >= 0. This closes P(k+1).

Port annotations: D-F1 (port lines 2636-2641) is a correct summary of the source's gradient proof, and its remark that a coordinate-wise sum would bring a dimension factor is right. D-F2 (port line 2643) is correct, including the strictness of the half-polydisc inclusion when (8/3) rho = d_*(K-1). The inputs line (port line 2536) names the two 5.2 lemmas at the right loci; both are unqualified CA statements with full proofs, which I reread.

Cosmetic, no proof effect: the B4a header (port line 645) repeats the B2 sentence "For B2, the assembly nevertheless counts the weight machinery as incomplete ...". It does not apply to the driven flow lemma, which has no weight machinery and no open input of its own. The lemma is a closed elementary implication; what stays open is the supply of its adaptive drivers q_{k+1} at the consumer, as the port says.

## B2b: 5.5:lem-weight (port lines 172-457, 1193-2527)

Kind: check of their proof, with its very many cited inputs kept as the port's named inputs W5-*. This section is written part by part.

### (a1)-(a4) (CA-II 35543-35744)

Proved as an implication from the W5 inputs; the arithmetic is right. What I redid:

- (a1): the source-class condition at (k, square_0, B^+) with the arrest factor F <= 1 + 2 beta = 1.4 (beta = 1/5) and w^+ r_2(l^+) <= theta_2. All three are cited scaffold facts at CA-II 35553-35567, covered by the locus range of W5-local/W5-setting.
- (a2): W minimises under the coarse data, so it minimises under its own finer B*_j data (finer constraints define a smaller set), and uniqueness modulo gauge (Balaban CMP 109 (3.39), CMP 102 Theorem 1) gives W' = W^g. Then n(g) <= 2, and the perturbation step gives 2.8 * 5/4 + 1/4 = 3.75 <= 4.
- (a3): data bound 1.4 * 2 = 2.8; axial gauge 2 * K_ax M * 2.8 = 5.6; representation by CMP 102 Proposition 9; layer and BCH give 2(2 c. + 5.6 K_h K_ax M C_M^av) w_Q alpha_Q <= K_loc w_Q alpha_Q (11.2 <= 12); the four smallness spends are paid by K_loc A_w(gamma) <= c_h, since K_loc >= 12 C_M^av >= 24.
- (a4): rim deviation 4 C_M^av w alpha~ (l_i/l_l)^2 <= 8 C_M^av w_Q alpha_Q t_p^2 L^{2(i-j)} <= c_1 a_Q t_p^2, using l(x) >= p; and |e_rim| <= |B^ax| + d|b-y||F| <= 4d(1+|b-y|) c_1 a_Q t_p^2. Correct.

Three facts are used without a name or with a wrong pointer. None of them makes a step fail (findings F3-F5 below):

- **w(x) >= 1** (CA-II 35621-35622, and silently in (a3) for 4 c. alpha_Q <= 4 c. w_Q alpha_Q). The proof cites Notation 5.5:not-weight-notation, but that notation gives only upper bounds on w (34103-34112). The lower bound must come from the definition of the weights, which the port keeps under W5-setting without naming this property.
- **w alpha <= A_w(gamma)**. The uniqueness smallness "1.4 w(Delta) alpha~ <= 2.8 A_w(gamma)" (35649) needs w(Delta) alpha_{0,l(Delta)} <= A_w(gamma). Display (5.5:eq-box-regularity-3) needs w_Q alpha_Q <= (12/5.6) A_w(gamma). The account states w_Q alpha_Q <= 2 A_w(gamma) only elsewhere (CA-II 42829, 42855-42857, "from the statement on localisation constants of cubes of level at least p"). With the factor 2 both spends still close (11.2 <= 12, and 5.6 A_w <= K_loc A_w since K_loc >= 24). So nothing fails, but the input is not named in the port.
- **a_flat <= 5 A_w(gamma)** (35599) is stated without a source.

### (b) (CA-II 35748-36034)

Proved as an implication from the W5 inputs (W5-cover carries the CMP 119 p.276 transfer, printed without proof there). What I redid:

- Own-box geometry: sides of r_v are at most max{(2 nu+3) L^{-(nu-2)}, 1 + 5 L^{-(nu-2)}} <= 13/8 cubes of pi_{n-1} (decreasing in nu; 9/L and 1 + 5/L at nu = 3, L >= 8). So the box Q_v has at most 7 cubes a side, Q_v^(1) at most 9, and every point of Q_v^(1) lies within 6/L < 1 level-n unit of y, so w_{Q_v} <= w^v(y). Correct.
- Majorants: with t_p = Lt and Theta >= 2 c_1 K_loc L^3 alpha_{0,n} w^v / a_n, the two displayed inequalities are exact, and they give |B^ax| <= L^{-1}|B^ax|_*, |F| <= |F|_*, |e_mu| <= |e_mu|_* (using c_1 >= 1) and, for a core, |e_rim| <= |e_rim|_*. For a short single the rim bound holds with D_X in place of D, but the rim is used only for cores, so nothing breaks.
- Short single: |sigma' B^ax| < S* |B^ax|_* <= alpha_{3,j} on |sigma'| < S*, phi'(0) = 0, and 5.2:lem-disc-bounds (b) gives 2n S*^{-2}. Correct.
- Rim (iii): kappa d + delta_0 M (nu-1-d)_+ >= kappa d/2 + mu_0 (nu - 1); D <= 5 M nu; D^{d+1} t^4 e^{-mu_0(nu-1)} <= t^{4+a} (5 M nu)^{d+1} L^{(a-5)(nu-1)}, bounded in nu. Correct.
- Regime split (iv): a read core with S* <= 1 has C_M D t^2 z > 1/2; then t^2 > (10 C_M M nu z)^{-1}, and nu^3 z^2(1+z) t^{4+a} >= (10 C_M M)^{-2-a/2} nu^{1-a/2} z^{-a/2}(1+z). The complement gives S* >= 2. Correct, with one unstated assumption (F6 below).
- Degree in Theta (v): z^2(1+z) <= Theta^3 rho^2(1+rho); S*^{-2} = Theta^2 x_v; min(1, a^2 u^2) <= a^2 min(1, u^2) for a >= 1 (the port's W5-C1 check of the three cases is right). Correct.
- The stale label "(b')" at CA-II 36026: the lemma has no clause (b'). The port's W5-C1 reading (the remainder rows of (b)) is the only sensible one.

### (c) (CA-II 36037-36249)

The logic is right given the cited scaffold geometry (W5-geometry). What I redid:

- Step one: the three-way comparison of X_a with X_c (strictly inside, disjoint, containing) gives dist_m(y, X_a) >= 3 when l(y) > k_a, from k_c < k_a, from the separation R >= 38, or from the three sub-cases 3 R_m, L^{k_c - m} >= L, 3. The consequence uses n <= l(y), so dist_{l(y)} <= dist_n < 1, which forces t(Delta) = k_a >= l(y). Correct.
- Step three: n_0 - 1 < n_0 <= t_inner <= h_outer < k_0(outer) <= n_0 - 2. A contradiction, so the preparation is unique. Correct.
- Step five: in the three cases the step uses separation, the ordering of nested regions (k_a <= h_c contradicts k_a >= h_c + 1), and the layer statement. Correct as cited.

**Circular citation in their text, retained correctly by the port but not flagged** (finding F2). Three facts are cited to "the facts stated with Definition 5.5:def-data-factor": (i) the dichotomy "square in O+ or exceptional" with rho(square) >= R_k - 4 and k - n_0 + 1 <= N_* + rho (CA-II 36224-36225, 36267-36268, 36297); (ii) the level bound n_0 + 1 (36161); (iii) "a residual cell ... has t <= n_0 - 3" (36243). But that definition says its facts (f1)-(f2) "are established in the weight lemma" (34610-34611). The weight lemma never proves them; it only uses them. Fact (ii) and the residual-cell fact are not in (f) at all. "Residual cell" and the constant N_* are defined nowhere in CA-II (grep finds only these uses). The port lists "data-factor (f),(h)" and "residual-cell" under W5-geometry as assumed. That is the honest treatment, but they are open inputs with no supplier in the account, not cited results, and the open-input inventory should say so.

Side observation for the p6b check (not this port's text): the copy of this clause quoted in section 5.2 (CA-II 13806-13809) lists a third kind of preparation, "m for the completed preparation of a live region (Y,m)". The 5.5 statement and proof define t_c only for arrests and for running or sibling preparations. A consumer reading the 5.2 copy reads more than the 5.5 proof shows, unless such a preparation can never carry thin strata in the doubled block (Notation lines 34117-34121 suggest completed operations leave no strata on Z). I did not settle this.

### (c') and (d) (CA-II 36251-36484)

Correct. What I redid:

- (i): (6L)^d + 6^d + 6^d <= 2(7L)^d. A cell raised in the present R_k gives w^3 <= L_o^{6s}. An inherited cell gives w^3 <= L^{3 N_0(t)} <= L^{12}(T_k + 3 + c_{k-t})^{6 r} <= C_pr e^{rho - 2}, with c increasing, k - t <= n(rho) and T_k <= rho + 4 (W5-depth).
- (ii): with m = k_0 + q, the bound is 7^d L_o^6 L^{d(n_0 - k_0)} sum_q (L_o^6 L^{-4})^q + 7^d L_o^{6 N_0}. Here L_o^6 L^{-4} <= (27L)^{-1}, the series is <= 27/26, L_o^{6(N_0 - 1)} <= (L^3/27)^{N_0 - 1} <= L^{4 N_0}, and n_0 - k_0 <= N_0(t), which gives 3 * 7^d L_o^6 L^{d N_0}. Next y = L^{N_0 - 1} < L max{1, T^r}, so y^d <= y_*^d + L^d 2^{dr} b_t^{dr} and b_t <= rho + 5 + c_{n(rho)}, which gives C_tile e^{rho - 1}. Correct.
- (d): groups by the unit cell of the anchor, w^v(y) <= w^v(Delta'), kappa_R^act then linearity give total <= kappa_R c_W^3 K N_0 <= l^2 N_0. Then L_o^{6s} d <= l^2 <= kappa_R c_W^3 K# = L_o^{6s} d#. This uses L_o^{6s} <= K#: case (i) directly; case (ii) through s = 0 on O+ (f1) or s <= N_0(k) at an exceptional block. The final a + b e^u <= 1 + (a + b) e^u, and the floor delta_P w / 8 >= 1 (the source asks for >= 2) gives e^{rho - 1} <= e^{delta_P d/8}. Correct.
- Port fills W5-F2 (sum (nu+2) q^{nu-1} = 3/(1-q) + q/(1-q)^2), W5-F3 and W5-F4 are correct. W5-F3 says "in the exceptional case"; the bound N_0(t) >= 2 holds in all of case (ii), old blocks too. Cosmetic.
- W5-C2 (constant aliases) is a correct reading. The proof's C^dat_pr is the C^data_0 of (5.5:eq-data-factor-2) and the C^data_pr of the maximum before (5.5:eq-weight-constants-b). The text never names one constant three ways explicitly, but the defining supremum is the same.

### (e) (CA-II 36486-36797)

The difference principle (Step 3) is right: Cauchy, the three Schwarz bounds and the vanishing derivatives at the base point all pass to the difference of two bounded holomorphic functions. The identity (5.5:eq-machine-differences-5) for the companion is right, and so is the l^J normalisation in Step 5 (N_0/E_0 = c_alpha C_R e^{C_2 kappa_1} theta(square)).

- **W5-C3 (port line 2522) is a correct correction of their text.** The statement of (e) excludes the n*a item of the companions at nu <= 2 when the chart radius exceeds one ("for that item no claim is made", CA-II 35489-35493). Yet its closing sentence "Consequently the two-machine differences of the pieces ... satisfy that bound in its two-machine form" (35496, port line 415), and the last sentence of the proof (36789-36791), claim the block total for all pieces. In that sub-case only the raw bound C n alpha_{3,j}^{-2} a holds (36708-36725). It lacks the small factor (C D Theta a_n t^2)^2 of the table item, so the row sums at the constants K_r are not shown. The block total is therefore conditional on W5-low (the low-order variation bound at the second cube size), as the port says.
- **Unnamed and unlocated input** (finding F1). The per-unit paired bounds (5.5:eq-machine-differences-2)-(4), including |delta i_y| <= C_I''(S + n a) nu^3 (Theta rho)^2 (1 + Theta rho) t^{4+a}, come from "the paired rows of the two-machine comparison at the rim ... as stated there with rho replaced by Theta rho" (36600-36611, port line 2320). Step 4' takes two more items from the same source: the paired counterterm-coefficient row (36655-36657) and the off-chart clause of its paired Wilson row (36710-36712). This statement is not among the inputs (i)-(v) of 5.5:def-weight-inputs, and not among the "two further results" (35226-35228). Under that name it occurs nowhere in CA-I, CA-II, CA-III or the outline (grep for "comparison at the rim", "paired ... row" and "two-machine": only these six lines). 5.5:lem-pair-bounds (41456-41475) assumes the same family as its hypothesis (b), "the lemma stating the pair bounds (A^x), (M^x), (Pi^x), (I^x), (d^x), (F^x), (W^x)", also with no locus. The port's convention (port line 731) keeps every invoked result as a named hypothesis, so the implication stands. But the W5 table does not list this input. W5-pair covers closure under the moves and the paired-chart majorants, not these quantitative rows, so the open-input inventory misses the main supplier of (e).
- The proof says closure under M8 "holds by construction of K^rd" (36490). The statement takes it as assumed. Input (iii) itself asserts it "by construction" (35170-35171), so the two agree, and the port keeps it as assumed (W5-pair). No issue.
