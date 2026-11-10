lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:40Z

# ypath-port: the real finer-collar path of Y and its three estimates (registry row Y-PATH)

Port by Claude Opus 5.5 (high), Mac mini worker 2, 2026-11-10, at commit 850c442f0. It is not yet checked by another model. It is a port: a check of Y's proof, with the calculations Y gives as one sentence written out. It is not a new proof.

Source: `YM4_1400.tex` at commit 2bc0658f91d2 of the Sussman-Alpoge repository (`/tmp/ym4_1400.tex`, 136,637 lines). "Y n" means line n of that file. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the argument, the constructions and every Y statement used here.

## 0. Result

Stop condition (i): the port is complete. Statements P1-P7 (section 3) are written with their hypotheses, constants and Y lines, and each step was checked as written. No step failed and no counterexample was found. Five points that Y gives as a sentence are calculated here: the anchor bound (P3.1), the pivot bound from the averaging formula (P3.2), the one-row contraction (P3.4), the scaled plaquette estimate (P5.3), and the ratio of thresholds eps_j/eps_i <= C_eps(1 + sqrt(j-i)) (P7.1). One point needs care and does not break the argument: the factor e^{-c(M/M_1)(j-i)} of (E2) needs each intervening shell to add at least a fixed multiple of M to d_B (input G-W), and the response rate a to be fixed before M (P7.3). The smallness condition on the ceiling is (S-e) in section 2.

Order of dependence (step 0): **no cycle.** The path (P4) reads the promoted-datum bound only through the fixed prospective orbit U^+ and its radius e. (E2) does not use the removal of the preceding guard; that removal reads (E1)-(E3). Section 1 gives the lines.

What stays open: the inputs listed in section 4. They are Y's statements, cited and not proved here. Of these, the response bound (IN-RESP) and the joined response polydisc (IN-POLY) are the substantial ones; (IN-POLY) is in the scope of `yjoin-port` (row 627).

## Repo search

- `library/prior/ypath-read.md` (gpt-6-luna, not checked) sections 1, 2, 4: used as a map only. Its line numbers agree with the file; its summaries agree with what I read, except that it does not give the calculations below.
- `library/inset-chart.md` section 5.3: the consumer. It reads (Y-PATH) with hypotheses "H-GEO; U^+(omega) exists with radius below the fixed ceiling; weak coupling", and conclusions "pivot unique in the regular chart; old datum in the continuation polydisc; regular old orbit U^-(omega,B) exists; (E1), (E2), (E3)".
- `library/open-registry.md` row Y-PATH: OPEN, this row is a named port. `library/open-core.md`: no entry for Y-PATH or the collar path. No other FINISH row attacks these statements (rows 617, 622, 623, 627 are a consumer, its check, the reading, and the joined-datum port).
- The Sussman-Alpoge outline: the prior reading found SA 9783-9789 and 9913 related but not a supplier. I did not repeat that search.

## 1. Order of dependence (step 0)

The five steps, with what each reads.

- (a) Promoted-datum bound on the entering support (Y 65417-65491, 134201-134205). On the entering support, where the preceding guard is still a carried factor, each datum test of the global and joined prospective datum is at most C e_q, e_q = R_q^2 eps_q. With bgc:proper-background (Y 35634-35646) this gives the admitted prospective orbit U^+ with radius e <= C_B C max_q e_q (inset-chart Lemma 5.2). As used downstream, (a) is a statement about the fixed prospective datum omega only: the certificate I(omega) of inset-chart 5.2.
- (b) The path (Y 64860-64978). Its hypotheses read: the admitted prospective datum and U^+ (Y 64863-64867); the ceiling on e (Y 64868-64869, 64929-64932, 64951-64953); the approximate collar bound 2 delta'_j on the released nonpivots, which defines the ball (Y 64902-64907, 64970-64972); the common rows at their prescribed values (Y 64871-64872, 64894, 64966-64967). No clause of the preceding guard is read at a point (omega, B) of the ball. Y says so: "This constructs the old datum without using the preceding guard on that ball" (Y 64976-64977).
  **Decision 1: yes, step (b) reads (a) only at the fixed prospective orbit U^+, through its radius e.** The bound of (a) is used once, to admit U^+ at the fixed datum omega. Every later quantity of the path (the induced field M^j U^+, the anchors, the pivot inverse, the response) is evaluated at U^+ or at a point of the ball defined from U^+.
- (c) (E1) (Y 64979-65014): reads the path (b), the response bound (IN-RESP) at the points of the path, and the plaquette estimate. No guard.
- (d) (E3) (Y 64437-64455) and (E2) (Y 64234-64251): read the decaying form of (c) (Y 65000-65004), the shell geometry (G-W) and threshold arithmetic. (E2) is stated inside the paragraph `hi:preceding-guard-support`, but it is a premise of that paragraph's conclusion, not a consequence of it: Y 64265-64268 "On admitted real data the collar response fits these reserves, by its weighted bound on the old shells".
  **Decision 2: no, the derivation of (E2) does not use the conclusion of (e).** It reads the response at the fixed U^+ over the whole ball and the thresholds of the two guards as numbers. It never evaluates the preceding guard.
- (e) Removal of the preceding guard on the enlarged support (Y 64221-64455). Reads (E1)-(E3), the reserves, and the passing of the prospective guard at the fixed datum (Y 64306-64332, 64382-64394, 64422-64435, 64456-64463). Conclusion: the preceding guard equals one on the whole admitted real collar chart.

The order is (a) -> (b) -> (c) -> (d) -> (e). No step reads a later one. In the consumer this is the fibre lemma (inset-chart Lemma 5.1): (F1) is (a), and (F2) is (e), which is proved at every omega with I(omega) = 1 and every B of the ball, from (b)-(d).

## 2. Setting, norms and constants

**Setting (Y 64860-64867).** A transition from level j to q = j+1 of the stages; Y = Z''_q; K = the exterior collar of Y in Omega_q^c cap X. omega is a fixed prospective real datum V^+, admitted, with its regular critical orbit U^+ for the new (prospective) joined determining set, in the frame of the approximate collar test. The common stored rows are fixed in that frame. S := M^j U^+ is the j-fold average of U^+, the centre of the approximate collar test (Y 64032-64034, 65025-65027).

**The ball.** Ball(omega) is the set of released nonpivot values n with |n(b) S(b)^{-1} - 1| < 2 delta'_j for every nonpivot b of the mask (Y 64902-64907, 64970-64972). The pivots and common rows are not coordinates of the ball.

**Norms.** |g - 1| is the operator norm of the 2x2 matrix. d(g,h) is the geodesic distance of the unit round 3-sphere SU(2), so d(g,h) = |log(g h^{-1})| for the principal logarithm and d is bi-invariant. Then |g h^{-1} - 1| = 2 sin(d(g,h)/2), and since (2/pi) x <= sin x <= x on [0, pi/2],

  (N) (2/pi) d(g,h) <= |g h^{-1} - 1| <= d(g,h).

In particular |n(b) S(b)^{-1} - 1| < 2 delta'_j gives d(n(b), S(b)) < pi delta'_j. The operator norm is unitarily invariant: |u A u^{-1} - 1| = |A - 1| and |A - B| = |A B^{-1} - 1| for unitary B. If Y's norm is the Hilbert-Schmidt norm, every constant below changes by a factor at most 2.

**Scales.** Bare units, xi_l = L^l, eta_l = L^{-l} (Y 64996, 593). eps_l = g_l p_0(g_l), p_0(g) = A_0 (log g^{-2})^{p_0}, delta'_l = g_l A_1 p_1(g_l), so delta'_l / eps_l = (A_1/A_0)(log x_l)^{-(p_0 - p_1)} with x_l = g_l^{-2} (Y 63836, 63876, 61905, 1115).

**Constants of the inputs** (section 4 gives the Y lines). Each depends only on L and the fixed geometry (M_1, R_1, the separation), not on M, j, depth or volume, unless said.

- C_av: level-n plaquette defects of M^n U^+ are at most C_av e in level-n units (IN-AV).
- m_L: the largest number of fine bonds in a contour of a double block; N_L: the number of nonpivots in a double block.
- C_mean: Lipschitz constant of the block mean on its regular chart (IN-MEAN).
- rho_reg(L): the radius about S, bond by bond in d, on which the double block is admitted to the regular branch (IN-REG).
- r_1(L), r_2(L), Lambda(L): radius in the pivot, radius in the nonpivots, and nonpivot-derivative bound of the regular one-row map (IN-ROW).
- C_R, a: constant and rate of the real Landau response (IN-RESP); S(a'), a' in {a, a/2}: the top sum (IN-TOP).
- r_B: the radius of the joined response polydisc (IN-POLY); a_0, a_1, C_B of bgc:proper-background (IN-BG).
- w: every shell of the prepared nest crossed by a path from an old shell to the changed rows adds at least w M to its d_B-length (G-W).
- C_fr: the frame clause -C_fr <= x_i - x_j <= C_fr (j - i), i <= j (IN-FR).

**Constants of the port**, defined in section 3: C_2 = 6 pi m_L^2 C_av + (1 + 2 C_mean) pi m_L; C_3 = L^3 C_2 + pi L; C_4 = 2 pi L^3 Lambda (with C_4 >= pi); C_5 = 16 S(a) C_R C_4; C_5' = 16 S(a/2) C_R C_4; C_L = 10 C_5; C_L' = 10 C_5'; C_eps = 2(1 + sqrt(C_fr)); kappa = a w M / 2.

**Order of choice.**
1. L, beta_s, M_1, R_1 and the separated geometry; then the constants of the inputs above.
2. C_2, C_3, C_4, C_5, C_5', C_L, C_L', C_eps. None depends on M.
3. M, with kappa = a w M/2 >= 2 ln 2. This needs a fixed before M (see the remark in P7).
4. The regularity ceiling e_* (it may depend on M, as Y 4391 asks M alpha_0 small):

   (S-e) m_L^2 C_av e_* <= 1 and C_3 e_* <= (1/2) min(rho_reg, r_1), together with the ceilings of IN-BG, IN-REG and IN-RESP, and a radius small enough that |dU^+(p) - 1| <= xi^{-2} at local scale xi (used in P5.4).

5. A_1/A_0 and the weak-coupling floor, so that for every j:

   (S-d) C_3 delta'_j <= (1/2) min(rho_reg, r_1); pi delta'_j <= min(r_2, r_1/(2 L^3 Lambda)); C_4 delta'_j < r_B; C_5' delta'_j <= 1/4; x_j log x_j >= C_fr p_0 / ln 2;
   (S-r) delta'_j / eps_j <= beta_s / (16 C_L' C_eps).

(S-e) is the smallness condition on the regularity ceiling that step (3) of the row asks for. (S-r) is possible because delta'_j/eps_j = (A_1/A_0)(log x_j)^{-(p_0-p_1)} with p_0 > p_1, as Y 63876 says.

## 3. The port

### P1. Restriction (Y 64860-64892)

**Hypotheses.** H-GEO for the preceding and the prospective joined sequences (they have the same bare domain and differ only by the enlargement at level q). U^+ is constrained-critical for the prospective set at V^+, with radius e <= e_*.

**Definition.** V^0 := the datum read from U^+ on the preceding determining set.

**Conclusions.** (i) The common rows of V^0 have their prescribed values. (ii) U^+ is regular in the old units. (iii) The old datum radius of V^0 is at most C_av e. (iv) U^+ is critical for the old set at V^0.

**Proof.** As Y 64870-64892. (i): the common rows are rows of both sets, and U^+ has the prescribed values there (Y 64871-64872). (ii): the old curvature and current scales are no larger (Y 64878-64879). (iii): a tested old plaquette at level q >= 1 has its full order-q carrier in the member of level q - 1 (gap between members), and its holonomy is a plaquette of M^q U^+, so (IN-AV) gives C_av e; at level zero, the bare curvature bound of U^+ (Y 64880-64888). (iv): Y 64889-64891 gives N^- subset N^+, where N^+ = {U : the new rows of U equal V^+} and N^- = {U : the old rows of U equal V^0}, because each new coarse row is the composition of averages on its old fine blocks. U^+ lies in N^- by the definition of V^0. Criticality of U^+ on N^+ means dS(U^+) is zero on the tangent space of N^+ at U^+. That space contains the tangent space of N^- at U^+, so U^+ is critical on N^-. (Both sets are smooth submanifolds near U^+ on the regular chart; if criticality is defined by multipliers, the same tangent inclusion gives it.)

**Check.** Each step holds as written. The nested restriction (old inward bonds are absent from the new no-inward set) is used only for (iv), through N^- subset N^+.

**Inputs.** IN-AV (Y 10993-11001), H-GEO (`library/h-geo.md`; Y 64874-64877, 64882-64884), the definition of constrained-critical (IN-BG, Y 35634-35646).

### P2. Nonpivot change (Y 64894-64908)

**Hypotheses.** P1. n in Ball(omega). The inherited coarse rows at their prescribed values.

**Conclusions.** For every newly imposed coarse row c with double block D(c): (i) both endpoint blocks of c are outside the old Omega_q and inside the old member of level j; (ii) every nonpivot b of D(c) has d(n(b), S(b)) < pi delta'_j; (iii) the coarse value of S on D(c) is W := V_q(c), the coarse value prescribed for the actual field.

**Proof.** (i): as Y 64895-64901 (alignment on the level-q grid; at the first stage the new face is three level-q cells from the bottom core; later, the gap between prepared faces exceeds the width of a double block). (ii): a nonpivot of D(c) either meets K, and then the approximate collar test gives |n(b) S(b)^{-1} - 1| < 2 delta'_j, so d < pi delta'_j by (N); or it belongs to the common fine rows across dY, and then n(b) = S(b), because both equal the prescribed common value (P1(i)) (Y 64902-64907). (iii): c is a row of the prospective set, so (M^q U^+)(c) = V_q(c); and M^q U^+ = M(M^j U^+) on c, so the coarse value of S on D(c) is V_q(c) (Y 64908).

**Check.** Y states the bound as "at most 2 delta'_j"; in the distance d this is pi delta'_j by (N). Nothing else changes.

**Inputs.** The approximate collar test (Y 64032-64038); the alignment and gap geometry (H-GEO).

### P3. The pivot (Y 64910-64958)

Fix c and D(c). Write the straight corridor product as q = P_- b P_+, with b the middle (pivot) bond and P_-, P_+ the products of the other corridor bonds. A superscript + means the value at S.

**Input IN-AVF (Y 75190-75214, 75215-75225).** On either logarithmic branch, with the other fine bonds fixed, the coarse value is F(q) = exp(X(q)) q, X(q) = sum_r alpha_r log(H_r q^{-1}), with alpha_r > 0, sum_r alpha_r = 1 - L^{-3}, anchors H_r independent of b, and |X(q)| <= pi (1 - L^{-3}). On the literal branch the anchors are literal transports; on the regular branch the end pieces are block means of contours. If neither case applies, F(q) = q.

**P3.1 (anchors).** d(H_a, W) <= C_2 (e + delta'_j) for every anchor, on either branch.

*Calculation* (Y 64929-64940 give it in three sentences). (1) The induced anchors H_a^+ and q^+ are transports of S along paths of at most m_L steps with the same ends, in a box whose plaquette size is at most C_av e (P1(iii) at level j). By IN-TRANS, they differ by at most (1 + C_av e)^{m_L^2} - 1 <= 2 m_L^2 C_av e, using (1+x)^N - 1 <= e^{Nx} - 1 <= 2 N x for N x <= 1, which is (S-e). With (N), each such transport is within pi m_L^2 C_av e of q^+. On the regular branch an anchor is mean_i(T_i) T_mid mean_k(T'_k), where each T_i T_mid T'_k is a literal path with the ends of q, and the T_i (and the T'_k) have common ends. Geodesic balls of radius below pi/2 on the 3-sphere are convex, and the mean is the unique zero of sum_i log(T_i V^{-1}) near the family, so d(mean_i T_i, T_1) <= max_i d(T_i, T_1) <= pi m_L^2 C_av e, and the same for the T'_k. Bi-invariance then gives d(H_a^+, q^+) <= d(H_a^+, T_1 T_mid T'_1) + d(T_1 T_mid T'_1, q^+) <= 3 pi m_L^2 C_av e. (2) W = F^+(q^+) on the regular branch (P2(iii)), so d(W, q^+) = |X(q^+)| <= max_a d(H_a^+, q^+). Hence d(H_a^+, W) <= 6 pi m_L^2 C_av e. (3) A literal anchor of the actual field is a product of at most m_L nonpivots, each moved by less than pi delta'_j (P2(ii)). By bi-invariance and the triangle inequality, d(H_a, H_a^+) <= pi m_L delta'_j. An averaged end contour is a block mean of such transports; it reads no pivot and stays in its regular mean chart, so by IN-MEAN it moves by at most C_mean pi m_L delta'_j. A regular anchor has two end means and one literal piece, so it moves by at most (1 + 2 C_mean) pi m_L delta'_j. Sum: d(H_a, W) <= C_2 (e + delta'_j).

**P3.2 (coarse bound for the pivot).** Every pivot value b with F(q) = W satisfies d(b, b^+) <= C_3 (e + delta'_j).

*Calculation* (Y 64941-64951 give it in one display and two sentences). If F(q) = W on a logarithmic branch, then exp(X) = W q^{-1} with |X| <= pi(1 - L^{-3}) < pi. The principal logarithm inverts exp on |X| < pi, so d(q, W) = |log(W q^{-1})| = |X|. Since alpha_r > 0,

  d(q, W) = |X| <= sum_r alpha_r d(H_r, q) <= sum_r alpha_r (d(H_r, W) + d(W, q)) <= (1 - L^{-3}) (C_2 (e + delta'_j) + d(q, W)).

So L^{-3} d(q, W) <= (1 - L^{-3}) C_2 (e + delta'_j), that is d(q, W) <= (L^3 - 1) C_2 (e + delta'_j). If neither logarithmic case applies, q = F(q) = W. In both cases, with step (2) of P3.1, d(q, q^+) <= d(q, W) + d(W, q^+) <= L^3 C_2 (e + delta'_j). Then b = P_-^{-1} q P_+^{-1} and b^+ = (P_-^+)^{-1} q^+ (P_+^+)^{-1}. Bi-invariance, invariance under inversion and the triangle inequality give d(b, b^+) <= d(q, q^+) + d(P_-, P_-^+) + d(P_+, P_+^+) <= L^3 C_2 (e + delta'_j) + (L - 1) pi delta'_j <= C_3 (e + delta'_j).

**P3.3 (regular branch).** Under (S-e) and (S-d), every bond of D(c) is within rho_reg of S: the nonpivots by P2(ii), since pi delta'_j <= C_3 delta'_j, and the pivot by P3.2. So D(c) is on the regular branch (IN-REG; Y 64951-64953).

**P3.4 (one-row inverse; the sharper increment).** Input IN-ROW (Y 64953-64958; derivative formula Y 75226-75240): in a fixed double-block gauge of S and log coordinates about S, let G_n(b) be the regular coarse value. On {max_b d(n(b), S(b)) <= r_2} x {d(b, b^+) <= r_1}: ||D_b G_n(b) - L^{-3} I|| <= L^{-3}/2 and ||D_n G_n(b)|| <= Lambda. (At the flat point Y's formula B(w) dF_q = H(w) - sum_i alpha_i H(v_i) gives dF_q = 1 - sum alpha = L^{-3}.)

*Calculation.* Put T_n(b) = b - L^3 (G_n(b) - W). Its derivative in b is I - L^3 D_b G_n, of norm at most 1/2. Also |T_n(b^+) - b^+| = L^3 |G_n(b^+) - G_S(b^+)| <= L^3 Lambda pi delta'_j <= r_1/2 by (S-d). So T_n maps the closed ball of radius r_1 about b^+ into itself and contracts by 1/2. Its unique fixed point Phi(n) is the unique solution of G_n(b) = W there, and |Phi(n) - Phi(n')| <= 2 L^3 Lambda |n - n'|. By P3.2 and (S-e), (S-d), every solution of F(q) = W lies in that ball, so the pivot is Phi(n), and d(b, b^+) <= 2 L^3 Lambda pi delta'_j = C_4 delta'_j.

**Check.** Each inequality was checked as written. Y's "C(L)" in d(H_a, W) <= C(L)(e + delta'_j) is C_2; the coarse pivot bound is C_3; the sharper increment is C_4.

**Inputs.** IN-AVF, IN-TRANS (lem:averaging-1a-1-2, Y 3717-3727: rearranging m steps in a box of plaquette size varpi changes the transport by at most (1+varpi)^{m(m-1)/2} - 1), IN-MEAN (lem:averaging-1a-1-1, Y 3714: the mean is holomorphic with bounds independent of the number of members; Cauchy estimates on a smaller ball give the Lipschitz constant C_mean), IN-REG (Y 10998-11001), IN-ROW.

### P4. The path and the full ball (Y 64960-64977)

**Hypotheses.** P1-P3, (S-e), (S-d).

**Construction.** For n in Ball(omega) and each nonpivot b, x_b := log(n(b) S(b)^{-1}), so |x_b| < pi delta'_j. Put n_t(b) := exp(t x_b) S(b) and b_t := Phi(n_t) in each double block, for t in [0, 1]. The common rows stay at their prescribed values. B_t denotes the plain determining logarithms of the resulting old datum V_t relative to V^0.

**Conclusions.** (i) n_t is in Ball(omega) for all t. (ii) |B_t(row)| <= C_4 delta'_j and |dB_t/dt (row)| <= C_4 delta'_j for every row. (iii) V_0 = V^0 and V_1 is the actual old datum. (iv) If C_4 delta'_j < r_B, the path lies in the joined response polydisc, and the regular old critical orbit U_t exists along it, with U_0 the orbit of U^+. (v) The same holds at every point of Ball(omega). The construction reads no clause of the preceding guard.

**Proof.** (i): the ball is, bond by bond, a ball about 0 in the log coordinate x_b, by (N); it is convex, and |t x_b| <= |x_b|. (ii): a nonpivot row has B_t = t x_b, with |x_b| < pi delta'_j <= C_4 delta'_j. A pivot row has |B_t| = d(b_t, b^+) <= C_4 delta'_j by P3.4, and |dB_t/dt| <= 2 L^3 Lambda sup_b |x_b| <= C_4 delta'_j by the Lipschitz bound of Phi. Each double block contains only its own pivot (Y 64962), so the pivots are solved block by block. (iii): at t = 0, n_0 = S and Phi(S) = b^+, since b^+ solves G_S(b) = W (P2(iii)) and the solution in the ball is unique; so V_0 = V^0. At t = 1 the pivot is the actual one, by P3.4. (iv): IN-POLY (Y 13344-13350) gives the orbit on the polydisc; the initial orbit is that of U^+ by P1(iv) and uniqueness at radius a_0 (IN-BG). (v): for any n in the ball, apply (i)-(iv) to the path from S to n.

**The radius and bound the extension needs** (asked in step (4) of the row): the implicit inverse Phi must be defined on the nonpivot ball of radius r_2 >= pi delta'_j about S, with values in the pivot ball of radius r_1 about b^+, and Lipschitz constant 2 L^3 Lambda; this is (S-d). The row logarithms must stay in the polydisc: C_4 delta'_j < r_B.

**Check.** Y's "row logarithms and their derivatives along the path are O_L(delta'_j)" is (ii) with constant C_4. Existence of a regular old orbit at each point also follows from IN-BG alone if, in addition, C_av e_* + 4 C_4 delta'_j <= a_1: a datum plaquette meets at most four changed rows, each changed by at most C_4 delta'_j. That route gives existence, not the response form used in P5, so P5 still needs IN-POLY.

**Inputs.** P3, IN-POLY (scope of `yjoin-port`, row 627), IN-BG.

### P5. The weighted response and (E1) (Y 64979-65017)

**Hypotheses.** P4, (S-e), (S-d).

**Input IN-RESP (Y 64979-64986, resting on mb:datum-response-system Y 13140-13145, mb:point-response Y 13158-13164, mb:extended-source Y 13180-13188).** On the joined response polydisc the old orbit is (e^{i H(B)} U^+)^{u_B} in bare units, with u_B a real node gauge, and for each row c with top y_c and every top y,

  xi_y |d_c H(B)(y)| <= C_R e^{-a d_B(y, y_c)},  xi_y^2 |nabla_{U^+} d_c H(B)(y)| <= C_R e^{-a d_B(y, y_c)},

per unit of the plain row logarithm B_c. The metric d_B and the tops are those of the preceding joined sequence. (If Y's bound is in nabla_{U_t}, then |nabla_{U_t} Z - nabla_{U^+} Z| <= 2 |H| |Z| by the commutator bound below, and the change is absorbed in C_R under (S-d).)

**Input IN-TOP (Y 64989-64991).** sup_y sum_{tops y'} e^{-a' d_B(y, y')} <= S(a') for a' in {a, a/2}, uniformly on the separated sequences, and at most eight rows use one top.

**P5.1 (response bound).** On the old level-j plaquette carriers at the new prepared face, xi_j ||H|| + xi_j^2 ||nabla_{U^+} H|| <= C_5 delta'_j, with xi_j = L^j.

*Calculation* (Y 64987-64997). H(B_1) = integral over t in [0,1] of sum_c d_c H(B_t) dB_t(c)/dt, since H(B_0) = H(0) = 0. By P4(ii), |dB_t(c)/dt| <= C_4 delta'_j, and it is zero on the common rows. So xi_y |H(y)| <= C_R C_4 delta'_j sum_c e^{-a d_B(y, y_c)} <= 8 S(a) C_R C_4 delta'_j, and the same for xi_y^2 |nabla_{U^+} H(y)|. The sum of the two is at most C_5 delta'_j. At the face the local scale is xi_j.

**P5.2 (decaying form; Y 65000-65004).** If every changed row top is at d_B-distance at least D from a stencil whose local scale is at least xi_s, then on that stencil xi_s ||H|| + xi_s^2 ||nabla_{U^+} H|| <= C_5' delta'_j e^{-a D/2}.

*Calculation.* For changed c, e^{-a d_B(y, y_c)} <= e^{-a D/2} e^{-(a/2) d_B(y, y_c)}; sum with IN-TOP at rate a/2. Since xi_y >= xi_s, the weights xi_s, xi_s^2 are at most xi_y, xi_y^2.

**P5.3 (the scaled plaquette estimate; Y 65006-65009 give it in one sentence).** Let p be a bare plaquette with corner x and directions mu, nu, and U' = e^{iH} U on its links (H Hermitian, su(2)-valued). Write ||H||_p for the largest |H| on the four links and ||nabla_U H||_p for the larger of |nabla_mu H_nu(x)| and |nabla_nu H_mu(x)|, where nabla_nu H_mu(x) = U_nu(x) H_mu(x+nu) U_nu(x)^{-1} - H_mu(x). If 4 ||H||_p <= 1, then

  |dU'(p) dU(p)^{-1} - 1| <= 2 ||nabla_U H||_p + 4 |dU(p) - 1| ||H||_p + 16 ||H||_p^2.

*Proof.* Write the plaquette as four oriented links l_1, ..., l_4 and U'(l_k) = e^{i H_k} U(l_k); for a link run backwards, H_k = -U(b)^{-1} H(b) U(b). With T_k = U(l_1) ... U(l_{k-1}) and h_k = T_k H_k T_k^{-1}, induction on k gives U'(l_1) ... U'(l_k) = e^{ih_1} ... e^{ih_k} T_{k+1}, so dU'(p) dU(p)^{-1} = e^{ih_1} e^{ih_2} e^{ih_3} e^{ih_4}. Using dU(p) = U_mu(x) U_nu(x+mu) U_mu(x+nu)^{-1} U_nu(x)^{-1}, one finds h_3 = -dU(p) [U_nu(x) H_mu(x+nu) U_nu(x)^{-1}] dU(p)^{-1} and h_4 = -dU(p) H_nu(x) dU(p)^{-1}. Hence

  h_1 + h_2 + h_3 + h_4 = -nabla_nu H_mu(x) + nabla_mu H_nu(x) + R,  R = (1 - Ad_{dU(p)}) [U_nu(x) H_mu(x+nu) U_nu(x)^{-1} + H_nu(x)].

For unitary g, |g Z g^{-1} - Z| = |(g - 1) Z - Z (g - 1)| <= 2 |g - 1| |Z|, so |R| <= 4 |dU(p) - 1| ||H||_p. Expanding each exponential, the terms of the product of total degree at least 2 are bounded by the same terms of e^{s}, s = sum |h_k| <= 4 ||H||_p <= 1, so |prod e^{ih_k} - 1 - i sum h_k| <= e^s - 1 - s <= s^2. Combine. QED.

**P5.4 ((E1)).** For every bare plaquette p of the old level-j carriers at the new prepared face, at every point of Ball(omega),

  (E1) | |dU^-(p) - 1| - |dU^+(p) - 1| | <= C_L delta'_j L^{-2j}.

*Proof.* The node gauge u_B conjugates dU^-(p), so |dU^-(p) - 1| = |d(e^{iH} U^+)(p) - 1|. With A = d(e^{iH} U^+)(p) and B = dU^+(p) unitary, | |A - 1| - |B - 1| | <= |A - B| = |A B^{-1} - 1|. Apply P5.3 with ||H||_p <= C_5 delta'_j xi_j^{-1}, ||nabla H||_p <= C_5 delta'_j xi_j^{-2} (P5.1), and |dU^+(p) - 1| <= xi_j^{-2} (regularity of U^+ under (S-e), at local scale xi_j >= 1). Then 4 |dU^+(p) - 1| ||H||_p <= 4 C_5 delta'_j xi_j^{-2}, and 16 ||H||_p^2 <= 4 C_5 delta'_j xi_j^{-2} since C_5 delta'_j <= 1/4. Total: 10 C_5 delta'_j xi_j^{-2} = C_L delta'_j L^{-2j}.

**Reserve (Y 65015-65017).** C_L delta'_j L^{-2j} <= beta_s F_j eps_j L^{-2j}/4 holds when delta'_j/eps_j <= beta_s/(4 C_L), since F_j >= 1. (S-r) implies this, because C_L' >= C_L and C_eps >= 2.

**The constants in C_L** (step (5) of the row): C_L = 160 S(a) C_R C_4 with C_4 = 2 pi L^3 Lambda. So C_L depends on the response constant C_R and rate a (IN-RESP), the top sum S(a) and the eight rows per top (IN-TOP), and the one-row inverse bound Lambda(L) (IN-ROW). Through the conditions under which these hold it depends on L, M_1, R_1 and the ceilings. It does not depend on M, j, the depth, the volume or the coupling.

**Check.** Each step was checked as written. Y's "scaled plaquette estimate" is P5.3; I found no statement of it under that name in Y, so it is written out here.

**Inputs.** P4, IN-RESP, IN-TOP, IN-POLY, regularity of U^+ (IN-BG).

### P6. (E3) from (E1) (Y 64437-64455)

**Hypotheses.** P5; a crossing plaquette p of dZ''_{s+1}, s < j, assigned to shell s and retained (Y 64437-64441); input G-W.

**Input G-W (Y 64444-64450, 64246-64248; H-GEO).** The stencil at this face has local scale at least L^s. Up to a bounded stencil enlargement, its d_B-distance to the newly changed rows is at least that of the adjoining shell, and each intervening layer adds at least w M to it. So D >= w M (j - s - 1).

**Conclusion.** (E3) the defect change at p is at most C_L' delta'_j L^{-2s} e^{-kappa (j - s - 1)}, kappa = a w M/2.

**Proof.** P5.2 with D >= w M (j - s - 1) and weights xi_s; then P5.3 as in P5.4, with xi_s in place of xi_j and C_5' in place of C_5 (the regularity bound |dU^+(p) - 1| <= xi^{-2} <= xi_s^{-2} holds since the local scale is at least xi_s). Total 10 C_5' delta'_j e^{-a D/2} L^{-2s}, and e^{-a D/2} <= e^{-kappa (j - s - 1)}.

**The fit (Y 64456-64463, a sentence in Y).** The coefficient of p drops by beta_s 2^{-(n+2)}, n = j - s >= 1, against the base G_s eps_s L^{-2s} with G_s >= 1. Write delta'_j = (delta'_j/eps_j) eps_j and use eps_j <= C_eps (1 + sqrt n) eps_s (P7.1). If kappa >= 2 ln 2, then (1 + sqrt n) <= 2^n (true at n = 1, and sqrt(n+1) - sqrt n <= 1 <= 2^n) and e^{-kappa (n-1)} <= 4^{-(n-1)}, so the change is at most 4 C_L' C_eps (delta'_j/eps_j) 2^{-n} eps_s L^{-2s}. This is at most beta_s 2^{-(n+2)} eps_s L^{-2s} by (S-r).

Y's rate "c(M/M_1)" is kappa: in Y the response rate a is of order 1/M_1 (walk cubes of side M_1), so a w M/2 = c M/M_1.

**Inputs.** P5, G-W, IN-FR (through P7.1).

### P7. (E2) (Y 64234-64251)

**Hypotheses.** P5; a plaquette p on a shell of index i < j already present at stage j (Y 64235-64237); G-W in the form: the shells i+1, ..., j lie between shell i and the changed collar rows, so D >= w M (j - i).

**P7.1 (ratio of thresholds; Y 63876 states it, citing the order of constants at Y 72868).** Input IN-FR (Y 4583): -C_fr <= x_i - x_j <= C_fr (j - i) for i <= j, with x_l = g_l^{-2} >= 1. Then eps_j/eps_i <= C_eps (1 + sqrt(j - i)), C_eps = 2(1 + sqrt C_fr), once x_l log x_l >= C_fr p_0 / ln 2 for all l.

*Calculation.* eps_l = A_0 x_l^{-1/2} (log x_l)^{p_0}. First, x_i/x_j <= (x_j + C_fr (j-i))/x_j <= 1 + C_fr (j - i), so (x_i/x_j)^{1/2} <= 1 + sqrt(C_fr (j-i)) <= (1 + sqrt C_fr)(1 + sqrt(j-i)). Second, x_j <= x_i + C_fr, so log x_j <= log x_i + C_fr/x_i, and (log x_j / log x_i)^{p_0} <= (1 + C_fr/(x_i log x_i))^{p_0} <= e^{p_0 C_fr/(x_i log x_i)} <= 2.

**P7.2 ((E2)).** The weighted response from the changed collar rows on shell i is at most

  (E2) C_L' C_eps (delta'_j/eps_j)(1 + sqrt(j - i)) e^{-kappa (j - i)} eps_i L^{-2i}.

*Proof.* As P6 with s = i and D >= w M (j - i): the change is at most C_L' delta'_j L^{-2i} e^{-kappa (j-i)} = C_L' (delta'_j/eps_j)(eps_j/eps_i) e^{-kappa (j-i)} eps_i L^{-2i}. Apply P7.1. Y's prefactor C_L is C_L' C_eps here.

**P7.3 (the choice of M/M_1 and the reserve; Y 64246-64252).** The later coefficient on shell i is smaller by beta_s 2^{-(j-i+2)}: with c(i, J) = 1 - beta_s (1 - 2^{-(J-i+1)}), c(i, j) - c(i, j+1) = beta_s 2^{-(j-i+2)}. The geometric factor G_i = L_flat^{2(i - k_sharp - 1)_+} >= 1 and any overlap factor are the same at both stages and at least one. Choose M with kappa = a w M/2 >= 2 ln 2. Then (1 + sqrt n) e^{-kappa n} <= 2^n 4^{-n} = 2^{-n}, n = j - i, and (E2) is at most C_L' C_eps (delta'_j/eps_j) 2^{-n} eps_i L^{-2i}. This fits the reserve beta_s 2^{-(n+2)} G_i eps_i L^{-2i} when delta'_j/eps_j <= beta_s/(4 C_L' C_eps), which (S-r) implies.

**Remark on the order (the one point that needs care).** The choice kappa >= 2 ln 2 is made by taking M large. It is valid only if the response rate a, the response constant C_R and the top sum S(a/2) are fixed before M and do not get worse as M grows; otherwise e^{-kappa} could not beat the factor 2 per shell. Y's text supports this order: "For M large, the decay e^{-c(M/M_1)(j-i)} across the shells dominates 1+(j-i)^{1/2}" (Y 63876), and the response constants are stated for separated sequences with M_1, R_1 fixed (Y 16100-16106). The ceiling, which Y lets depend on M (Y 4391), comes after M and only makes the bounds better. I record this as part of the input IN-RESP; it is not a gap in the argument.

**Inputs.** P5, G-W, IN-FR, the threshold coefficients (Y 63876, 64236-64238).

## 4. Inputs from outside the argument (cited, not proved here)

| Input | What is used | Y lines | Used in |
|---|---|---|---|
| H-GEO | the two joined sequences: same bare domain, enlargement only at level q, separation, alignment on the level-q grid, gap between prepared faces | 64872-64884, 64895-64901; `library/h-geo.md` | P1, P2 |
| IN-BG | `bgc:proper-background`: existence of the regular critical orbit for an eps-regular datum, eps <= a_1, radius <= C_B eps, uniqueness at a_0; definition of constrained-critical | 35634-35646 (proof 35651 on) | P1, P4, P5 |
| IN-AV | `mb:uniform-real-average`: level-n defects of M^n U bounded by the average bound; admission of every one-step regular mean branch | 10980-11001 | P1, P3 |
| approximate collar test | compares V_j with S = M^j U^+ on the nonpivot mask at 2 delta'_j | 64032-64038, 65025-65027 | P2 |
| IN-AVF | the real averaging formula: two logarithmic branches, alpha_r > 0, sum 1 - L^{-3}, anchors independent of the pivot, exponent norm <= pi(1 - L^{-3}); else F(q) = q | 75190-75225 | P3 |
| IN-TRANS | `lem:averaging-1a-1-2`: rearranged transports differ by at most (1+varpi)^{m(m-1)/2} - 1 | 3717-3727 | P3.1 |
| IN-MEAN | `lem:averaging-1a-1-1`: the block mean is holomorphic with bounds independent of the number of members | 3714 | P3.1 |
| IN-REG | admission radius rho_reg(L) of the regular branch about an admitted induced field | 10998-11001, 64951-64953 | P3.3 |
| IN-ROW | the regular one-row inverse: D_b G close to L^{-3} I and D_n G bounded on balls of radii r_1, r_2 | 64953-64958, 75226-75240; seed `px:one-row-seed` 22323 | P3.4, P4 |
| IN-POLY | the joined response polydisc of radius r_B; real points of it carry regular critical orbits | 13344-13350 (in the scope of `yjoin-port`, row 627) | P4, P5 |
| IN-RESP | the real Landau response: value and covariant first-difference bounds C_R xi_y^{-1}, C_R xi_y^{-2} times e^{-a d_B}; a, C_R fixed before M | 64979-64986; 13140-13188; 16100-16122 | P5-P7 |
| IN-TOP | the top sum at rates a, a/2 is uniformly bounded; at most eight rows per top | 64989-64991 | P5 |
| G-W | each intervening shell adds at least w M to d_B; stencil scale at least L^s; bounded stencil enlargement | 64444-64450, 64246-64248 | P6, P7 |
| IN-FR | frame clause -C <= x_i - x_j <= C (j - i); eps_l = g_l p_0(g_l) | 4583, 61905, 1115 | P7.1 |
| thresholds | c(i, J) = 1 - beta_s (1 - 2^{-(J-i+1)}), G_i >= 1; crossing coefficients and reserve beta_s F_j eps_j L^{-2j}/4 | 63876, 64236-64238, 64380-64388, 64441-64444 | P5.4, P6, P7 |

## 5. What this gives the consumer, and what stays open

For `library/inset-chart.md` 5.3 (Y-PATH): its stated hypotheses (H-GEO at both stages, U^+(omega) with radius below the fixed ceiling, weak coupling) are the hypotheses of P1-P7, once "the fixed ceiling" is read as (S-e) and "weak coupling" as (S-d) and (S-r). Its conclusions are P3.4 (one pivot value in the regular chart), P4 (iv)-(v) (the old datum in the continuation polydisc, the regular old orbit U^-(omega, B) on the whole ball), and (E1), (E2), (E3) as P5.4, P7.2, P6. Two precisions for the consumer:

- (E2) holds with rate kappa = a w M/2 and prefactor C_L' C_eps; the fit needs kappa >= 2 ln 2, chosen through M after the response constants (P7.3).
- The argument uses the radius of U^+ and no clause of the preceding guard (section 1). This confirms inset-chart Proposition 5.3 for (Y-PATH), as far as this reading goes.

Open: the inputs of section 4. Of these, IN-RESP (with IN-TOP and the uniformity in M) and IN-POLY carry the analysis; IN-POLY is the joined-datum comparison of `yjoin-port` (row 627). The others are elementary or are proved in Y at the lines given. I did not check those proofs.
