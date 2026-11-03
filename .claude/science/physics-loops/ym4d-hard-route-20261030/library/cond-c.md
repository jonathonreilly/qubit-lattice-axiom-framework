lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T01:06Z

# cond-c: condition (C) of the box-first WF7 route (queue row 157)

Pinned at commit 75752c07e (branch claude/ym4d-hard-route). Research-stage working state. Not an audit; no status.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Section 1 checks Codex text (`library/wf7-bf.md`), so it is a cross-provider check. Sections 2-7 are proved by Claude and not yet checked by the other model. No numeric job was run. Every step is a hand argument.

Sources read: `library/wf7-bf.md`; `gates/wf7-extension-gate.md` Section 6; `library/wf7-extension.md` Sections 1-4; `library/old-depth.md` Section 2 (Lemma CR); `library/joint-loc.md` Sections 4, 7; `library/assign-adopt.md` Sections 1-2 (Definition A); `library/geo-5.md` Sections 1-3 and `gates/geo-gate.md` (checked by Claude, first failing step none); `library/wf-room-2.md` Sections 1, 3. Outline: Sussman-Alpoge `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder, not copied here. SA line numbers refer to it. Read: SA 6012-6125 (frame, label, R21), 6318-6335 (index maps), 9588-9790 (1b setting, Theorems 1, 2, 6), 13426-13560 (PW), 15707-16360 (WF1-WF15), 17300-17450 (step tests, Proposition 2.3, fates), 17528, 20903-20912.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the windows, WF1-WF15, the label, the step formation, the fates, the nests and the frame. Tadeusz Balaban for the restriction mechanism (CMP 109 (3.18)-(3.25), (3.38)) and for the window scale of the local layer (CMP 119 p. 276, as read in `joint-loc.md` Section 7). Codex for `wf7-bf.md`, `wf7-extension.md` and `geo-5.md`.

## 0. Result

Status: finished 2026-11-03 (worker).

- **Check (Section 1).** `library/wf7-bf.md` checked line by line by Claude, first failing step none. Four defects, none breaks a consumer.
- **Top layer: the outline's windows give (C) (Theorem C1).** If the base point z lies in the level-k member Omega_k, outside a level-k drop-out kept through all N_k stages, then the outline's window R_z lies in Omega_{k-1}. So (C) holds. The reason is the two-cell padding of a step and its fates: the top gap is at least 2 s_k (Lemma T), and s_k >= LM xi_k because Rcheck_k >= L (Lemma F). The distance stays bM/sigma_j.
- **Lower layers: the outline's windows violate (C) (Example C3(a)).** For an old base point in a layer p < k near a seam of level <= j, every box that contains the outline's ball B(z, 2 M xi_k) violates (C), on an explicit admitted label. Near such a seam no box with (C) gives the age factor sigma_j, by any placement or size; the meet keeps (C) but loses the single-scale premise (Lemma N).
- **Filing (Rule W) and Theorem C2.** Use the outline's window at top-layer base points. Elsewhere use a window one level below the local layer p (or at level j if p = j). Then (C) holds for every old base point at every step. The distance is of order M/sigma_j at the top layer and M/sigma_{j,p} in layer p.
- **Consumers (Section 6).** WF13a and WF8-WF10 read Rule W. WF11-WF12 read it at the top layer, with c/L in place of c inside kept nests. For lower layers, Proposition L proves that (WF15) holds with an extra summable age weight, given the layer decay (LD) of the step direction.
- **What stays open.** (LD) at decoupled s, which is the layered form of (O1); it holds at s = 1 by T4, MS and Lemma BC. The analytic inputs of `wf7-bf.md` are unchanged. With Rule W, (C) is discharged as a premise of WF7; what the lower layers add is (LD), read by (WF15).

Proved by Claude, not yet checked by the other model (Sections 2-7).

## 1. Check of `library/wf7-bf.md` (Codex)

Checked line by line by Claude. First failing step: none. Four defects, none breaks a consumer.

| Section | Verdict |
|---|---|
| 1, check of the gate's Section 6 | **CORRECT-NO-ADVANCE.** Items 1-8 are correct clarifications. Item 4 is right: `wf7-extension.md` (4.5) bounds the two-map difference F_R(w)-F_R(v) with beta = w-v, so beta = 0 gives zero. The single-map term is DF_R(v)v', and Section 3 bounds it. |
| 2, identity (2) on contained boxes | **ADVANCE** as an implication from (C), Lemma CR, BG, AX and gauge invariance. Checked: d/dnu exp(i eta (t+nu zeta)H_b) = i eta zeta_b H_b exp(i eta (t+nu zeta)H_b), because zeta_b is a scalar. The chain rule is linear in the direction, and sum zeta = 1 on bonds, so sum_zeta d_nu Phi_zeta = d/dt G(X, F_T(m_T V_t)). At complete physical pairs V_i is regular critical for S^i. It is then also critical for the truncation S^{i,<=j}, which has more constraints, so Pi_j(V_i) = V_i up to residual gauge (BG). Lemma CR with (C) gives F_T(m_T V_i) = V_i on T_0 up to the assigned gauge, with the currents on bonds whose plaquettes lie in T_0. The member is gauge invariant. The sufficient condition R_z in Omega_j^0 cap Omega_j^1 and the aligned case of joint-loc (7.2) follow by nesting. |
| 3, bounds | **ADVANCE** as an implication from T4, AX, AV, MS, PW. Checked: (3); the weighted sum with 2 gamma below the T4 rate and gamma above the MS rate (needs rho >= 32 log L / theta, gate W1); (4) by integration on the complex segment; the node product rule and d(gJg^{-1}) = gJ'g^{-1} + [g'g^{-1}, gJg^{-1}]; the WF8 arithmetic (A E_H / alpha_j^2 <= C rho^2 sigma^{4+alpha_H}, A E_N / alpha_j^2 <= C rho^3 sigma^6 from alpha_j / r_B <= C, A^3 / alpha_j^3 = C rho^3 sigma^6); the tail split (5). |
| 4, heredity and consumers | **ADVANCE.** Checked: the inclusion-exclusion identity f[K\|B] = sum_{A in K} (-1)^{\|K-A\|} f(1_{B cup A}) and the corner coefficient (1-1)^{\|Lambda-B-A\|}; mixed Cauchy with one derivative per parameter; (6) from (4), the Cauchy cost C g_j / alpha_j and the C_M sigma^{-4} count; both WF12 inequalities from e^x >= x^n / n!. The OA7 paragraph claims only the pair estimate and says so. |
| 5, stop at a lower-layer seam | **ADVANCE.** The Cartan example is correct: 4 x 2 x 3^3 = 216 edges, 81 sites, cycle space 216 - 81 + 1 = 136 > 8 rows; d*da = 0 with d*a = 0 forces a = 0 by the flat lattice identity d*d + dd* = componentwise Laplacian and compact support. The first failed inference is named correctly. |

Defects, ranked:

1. **Scope (this note answers it).** Section 5 leaves open whether actual windows satisfy (C). Sections 2-6 below answer that: yes for top-layer base points (Theorem C1), no for the outline's level-k windows at lower-layer base points (Example C3), and yes for every base point under the filing of Section 5 (Theorem C2).
2. **Section 2, stronger than needed.** It requires X and its current stencil inside T_j(R_z). Lemma CR needs only the stencil inside the interior of T_0 = R_z. Harmless.
3. **Section 3, constant.** C_* adds the erosion (rho + L M_frak)/(L-1). The bound D >= bM/sigma - 2 holds without it, since every weight of the box metric is at least xi_j^{-1} and a row carrier has size at most 2 xi_j. Harmless.
4. **Section 3, input name.** "AV and PW give (3)": PW here is the first-order R9 bound of `o1-decoupled.md` Section 5, as `wf7-extension.md` Section 4 defines it, not SA's (PW1)-(PW5). Wording only.

## 2. The condition, the endpoint sequences, four geometric facts

Units are level-k units: xi_i = L^{i-k}, eta = L^{-k}, m_i = M xi_i (an M-cube of level i), s_i = M Rcheck_i xi_i (a cell of level i), sigma_j = xi_j / xi_k, sigma_{j,p} = xi_j / xi_p. Distances are periodic sup distances. For a box R and z in R, r(R,z) = max over x in R of \|x - z\|.

**(C)** (`wf7-bf.md` (C)). T_q(R_z) lies in Omega_q^0 cap Omega_q^1 for 0 <= q <= j. Here T is the Definition A first-rule tower of R_z cut at depth j, and S^0, S^1 are the two endpoint sequences. The boundary rows and the read collars of the box belong to R_z (`wf7-bf.md` Section 2).

**Reduction R0.** T_q(R_z) lies in T_0 = R_z (Definition A (A1)), and Omega_j lies in Omega_q for q <= j. So (C) holds if R_z lies in Omega_j^0 cap Omega_j^1, and in particular if r(R_z,z) < d(z, (Omega_j^0 cap Omega_j^1)^c). Conversely, if a point x of R_z outside Omega_j^i has d(x, R_z^c) > e_j, then x is in T_j(R_z) by (A3), and (C) fails at q = j. Here e_j <= rho xi_j (A3).

**Lemma E (endpoint sequences).** At the step from k to k+1, S^0 and S^1 have the same members Omega_0, ..., Omega_k. These are the determining members of the label S_k after its level-k operations. S^1 adds only Omega_{k+1}.

*Source.* SA Theorem 6(a) (SA 9776: "the sequences of labels to which the domain of the next step has been added") and 6(b) (U_k(V') = U_{k+1}(V) up to gauge). The tests of step k+1 act on the live region Y = Z_k and determine Omega_{k+1} (SA 17317-17321). The operation of level k+1 acts after the integration (SA 7632). This is a reading of definitions, not a lemma to prove.

From now on Omega_q means the common member, q <= k. Then (C) reads T_q(R_z) in Omega_q for q <= j.

**Lemma F (frame).** Rcheck_i >= L for every i. Hence s_i >= L M xi_i = m_{i+1}.

*Proof.* A frame has theta_i >= gamma^{-2} with 0 < gamma < e^{-1/2} (SA 6017-6018). So log theta_i > 1, and (log min_{l<=i} theta_l)^r > 1. Rcheck_i is the smallest power of L not below this number (SA 6024-6027). The only smaller power of L is 1, which is too small. So Rcheck_i >= L. SA 17334 forms Rcheck from the weights x_i instead. The same argument applies there once min x_i > e, which holds above the coupling floor because \|theta_i - x_i\| <= t_i is a small fraction of theta_i (R20). QED.

**Lemma G (consecutive gaps).** In every admitted history, after every step and every operation, and for the action, determining and every retained stopping choice,
  d(Omega_{i-1}^c, Omega_i) >= m_i   (1 <= i <= current level).
Consequently, if z is in Omega_p and j < p, then d(z, Omega_j^c) >= d(z, Omega_{p-1}^c) >= m_p, since Omega_j^c lies in Omega_{p-1}^c.

*Proof.* This is the induction of `geo-5.md` Section 3.3, checked line by line by Claude in `gates/geo-gate.md` Section 5, first failing step none. That note records the bound M xi_{i-1} for this pair. Each of its cases in fact gives at least m_i = L M xi_{i-1}:
- The step that creates level i puts Yhat^{~8} into Omega_i^c, and Y contains Omega_{i-1}^c (SA 17317-17321). So the gap is at least 8 s_i >= m_i (geo-5 Section 3.2).
- The first pair: Omega_0 = Omega_1^~ gives s_1 >= m_1, by Lemma F (geo-5 Section 3.2).
- Inside a prepared interval and at its lower splice, (3.1) of geo-5 gives m_i.
- At the upper splice the retained hole shrinks, so the old gap stays.
- A pair with one point in an operated component Q of level t >= i: geo-5 (3.2) or (3.3) gives 2 s_t >= 2 L M xi_t >= m_i.
- Healing and islands only fill. A change of stopping choice changes only the stage entries.
SA Proposition 2.3 states the same bound in the stronger form dist(Z_{i-1}, Omega_i) >= LM in level-(i-1) units (SA 17402), with equality possible "in the upper part of a nest". QED.

**Lemma T (top gap).** At the label S_k, let z be in Omega_k. Assume z is not in a drop-out X of level k with n(X) = N_k completed stages. Then d(z, Omega_{k-1}^c) >= 2 s_k.

*Proof.* Before the level-k operations, the gap is at least 8 s_k (first case of Lemma G). The operations act on class components X of the live set Z_k. Check each fate (SA 17417-17432).
- X healed or an island: Omega_l becomes Omega_l cup X for l <= k (an island keeps only Lambda_k unchanged). No hole of Omega_{k-1} remains in X. A hole outside X lies in the pre-operation Omega_k^c outside X, so it is at least 2 s_k from X (geo-5 (3.2), from the two-cell padding at SA 17317-17325).
- X a drop-out with n < N_k: the entries change only for k_flat < l <= k_flat + n <= k-1. The new member X minus Z''_l contains the old one, because Z''_l lies in the old hole (geo-5 (3.1)). Omega_k cap X does not change. Holes only shrink, so the 8 s_k gap stays.
- X a drop-out with n = N_k: Omega_k cap X becomes X minus Z''_k. (SA 17421-17431: the Omega entry changes for k_flat < l <= k_flat + n, and the Lambda and S entries only for l < k.) Points of this set are excluded by hypothesis. For a point of Omega_k outside X, the retained holes in X lie in the pre-operation Omega_k^c cap X, which is at least 2 s_k from X^c (geo-5 (3.3)).
- With several components, every pair of points falls under one of these cases. Points outside every operated component keep the old gap. QED.

**Lemma M (base-point margin).** Let z be an old base point of level j in the outline's sense: a unit site one layer of M Rcheck_j-cells inside Lambda_j^+ (SA 20910-20911). Then d(z, Omega_j^c) >= s_j in the determining sequence.

*Proof.* Lambda_j^+ is Lambda_j with its level-j islands. Islands are filled in every determining member through their level (SA 17418), so Lambda_j^+ lies in Omega_j. On a drop-out mark the determining member X minus Z''_l contains the action member, since Z''_l lies in the old hole. One cell layer inside Lambda_j^+ gives d(z, (Lambda_j^+)^c) >= s_j, and Omega_j^c lies in (Lambda_j^+)^c. QED.

*Scope note.* SA 6322-6324 indexes regular terms by z in Lambda_j only. Inside a nest Lambda_j = Omega_j can hold (SA 17402-17404). Under that weaker reading the margin of Lemma M can fail. Lemma M is used only in case (W3) of Section 5. Cases (W1) and (W2) do not use it.

## 3. Theorem C1: the outline's windows at top-layer base points

**Theorem C1.** Let z be an old base point of level j < k with z in Omega_k. Assume z is not in a level-k drop-out with N_k completed stages. Let R_z be the outline's enlarged box X'_k(z), or any box containing z, with r(R_z, z) < 2 s_k. Then (C) holds, with the boundary rows and read collars of the box. So Lemma CR applies to T at both endpoints, and `wf7-bf.md` (2) holds for this member.

The size condition holds for R_z = (Box_k(z))^{~a}, with Box_k(z) a pi_k-cube and a <= 2L - 2, because then r <= (a+1) M xi_k <= (2L-1) M xi_k < 2 L M xi_k <= 2 s_k (Lemma F). For a general box that meets at most C_win cubes of pi_k, r <= C_win M xi_k, so C_win <= 2L - 1 suffices. The outline's R_z contains Box^{~2} and the read collars of the grouped windows within b layers, so a = b + 3, and the condition is b <= 2L - 5.

*Proof.* By Lemma T, d(z, Omega_{k-1}^c) >= 2 s_k > r(R_z, z), so R_z lies in Omega_{k-1}. For q <= j <= k-1, T_q(R_z) lies in R_z, which lies in Omega_{k-1}, which lies in Omega_j and in Omega_q. By Lemma E this holds for S^0 and S^1. The other hypotheses of Lemma CR (`old-depth.md` 2.2):
- Separation: Definition A (A2), gap > rho xi_q.
- Alignment: T_q is a union of aligned M_frak xi_q-cubes (A1). Every Omega_q is a union of aligned cubes of the same nested centred grids: cells of side M Rcheck_q xi_q, or M-cubes inside nests (SA 17398-17399). So every block of every level is whole in both sequences.
- Boundary rows: the bare bonds of T_0 minus T_1, which lie in R_z.
- Read sets: the datum map and the inner-plaquette action read only R_z.
- Regularity: the physical endpoints are regular critical for S^i with restricted datum inside BG's radius (SA Theorem 6(b)).
QED.

*What C1 covers.* Layers above j may vary inside R_z: R_z may meet Omega_{k-1} minus Omega_k and Omega_{k+1}. (C) does not read them. This is the "nonconstant top layer" case of `wf7-bf.md`, now proved for the actual top windows. The distance is unchanged: D >= bM/sigma_j - 2 (defect 3 of Section 1). The inputs are Definition A (A1)-(A3) and Lemmas E, F, T. The half-cell profile (5.1), the face-movement rule, GEO1-GEO3, GEO5, GEO6 and W3 are not used: they concern the component geometry of 2.8, while (C) reads only the step padding and the fates.

## 4. Where the outline's windows fail, and a no-go

**Example C3(a): a lower-layer base point.** Fix j. Take an admitted history with these outcomes (SA 17317-17321). At step j exactly one level-j cell c_0 fails its plaquette test, nothing else fails, and Y = Z_{j-1} is empty. Then Omega_j^c = c_0^{~4} and Z_j = c_0^{~6}. At every later step t <= k, let one plaquette test fail in a cell just outside the margin of this live component, so that the new hole joins it. Then the component has a creation at every level, it is never quiet, and no operation acts on it (SA 17575-17583). A step changes only its own new members, so Omega_j does not change near c_0. A history is any record of outcomes, and each record is one term of the exact sum (SA 17404-17405), so this history is admitted.

Let z be the centre of the level-j cell at offset (8,0,0,0) from c_0. It lies one cell layer inside Lambda_j, so it is an old base point of level j. Its distance to Omega_j^c is delta_z = 3.5 s_j. At step k it lies in layer j: it is within 2 s_j of Z_j, hence inside Yhat^{~8} for the step j+1, so it is not in Omega_{j+1}.

The outline gives z a current window Box_k(z) of level k, and R_z contains Box_k(z)^{~2}, which contains B(z, 2 M xi_k). Take k with 2 M xi_k > 3.5 s_j + rho xi_j, that is 2 L^{k-j} > 3.5 Rcheck_j + rho/M. Let x_0 be in Omega_j^c with \|z - x_0\| = delta_z. Then d(x_0, R_z^c) >= 2 M xi_k - 3.5 s_j > rho xi_j >= e_j, so x_0 is in T_j(R_z) by (A3). But x_0 is not in Omega_j. So **(C) fails at q = j** for both endpoint sequences. Lemma CR does not apply. By the Cartan computation of `wf7-bf.md` Section 5, the pure-tower map then differs from the localised map, which Lemma CR does identify with the physical endpoint. The example does not depend on the side of the current window: for side w xi_k with fixed w > 0, R_z contains B(z, 2 w xi_k), and the same argument works once 2 w L^{k-j} > 3.5 M Rcheck_j + rho.

**Example C3(b): a kept nest at the top.** Let X be a level-k drop-out with N_k completed stages whose nest has gap exactly m_l at every level. SA admits this ("an equality in the upper part of a nest", SA 17402-17404). `geo-2.md` Sections 3-4 build such nests, checked in `gates/geo-gate.md` Section 2. A point z of X minus Z''_k next to Z''_k lies in Omega_k and has d(z, Z''_j) < (m_k + m_{k-1} + ...) + eta < (L/(L-1)) M xi_k + eta for k_flat < j < k. If an old level-j base point sits there, R_z contains B(z, 2 M xi_k), which contains points of Z''_j (a subset of Omega_j^c) at depth > (2 - L/(L-1)) M xi_k - eta > rho xi_j. So (C) fails at q = j. Lemma M allows such base points when s_j <= d(z, Z''_j), for example when Rcheck_j <= L^{k-j-1}. Whether the regular index map puts members inside drop-out nests is a property of the history operation that this note does not settle. The filing of Section 5 covers this case either way.

**Lemma N (no box at the old scale).** Let z be an old base point of level j, and delta_z = d(z, Omega_j^c). Let R be any box containing z whose pure first-rule tower satisfies (C). Then d(z, R^c) <= delta_z + rho xi_j.

*Proof.* Take x_0 in Omega_j^c with \|z - x_0\| = delta_z. If x_0 is not in R, then d(z, R^c) <= delta_z. If x_0 is in R, then x_0 is not in T_j(R), by (C). So d(x_0, R^c) <= e_j <= rho xi_j by (A3), and d(z, R^c) <= delta_z + rho xi_j. QED.

*Consequence.* The pointed window theorem works on a window whose tops have one scale (SA 13472-13473) and whose boundary is at distance comparable with sigma^{-1} from z, in level-j units (SA 13537-13540). By Lemma N, a pure-tower box with (C) has boundary distance at most delta_z / xi_j + rho. So the age factor sigma_j = xi_j / xi_k is available at z only if delta_z >= c M xi_k - rho xi_j for a fixed c > 0. At the base point of Example C3(a), delta_z = 3.5 s_j, so no pure-tower box with (C) gives an age gain at a scale above that of a level-j cell. Lemma N covers every placement and every size of the box. The localisation of SA Theorem 6(a), the meet T_q(R) cap Omega_q, satisfies (C) for every box. But it puts tops of levels below j within delta_z of z, so the single-scale premise fails. Also, Omega_j^c near z is where the level-j test failed, so the physical field there is not small at level j. No Taylor argument at a coarser scale can then hold near z.

So the requirement "the distance stays M/sigma_j" cannot be met at lower-layer base points by window placement, by box size, or by the meet. Section 5 uses the scale of the local layer instead, as Balaban does (CMP 119 p. 276).

## 5. The filing (Rule W) and Theorem C2

**Rule W.** For an old base point z of level j < k, put p = p(z) = max{q <= k : z in Omega_q}, using the common members. Then p >= j.
- **(W1)** p = k, and z is not in a level-k drop-out with N_k completed stages. Use the outline's window: Box(z) = Box_k(z), a pi_k-cube, and R_z = Box(z)^{~a} with 4 <= a <= 2L - 2.
- **(W2)** j < p in every other case. Box(z) is the pi_{p-1}-cube that contains z, and R_z = Box(z)^{~a} in that partition, with 4 <= a <= L - 2.
- **(W3)** j = p. Box(z) is the pi_j-cube that contains z, and R_z = Box(z)^{~a}, with 4 <= a <= L - 2.

In every case the near sum runs over X containing z with X in Box^{~2}, in the partition of Box(z). The grouped directions are the windows of the fixed direction partition that meet the b-layer neighbourhood of Box^{~2}, with 1 <= b <= a - 3. One box map serves every X. The tower is Definition A's first rule, cut at depth j. R_z is a level-j cubical subdomain: a pi_{p-1}-cube is a union of pi_j-cubes when j <= p - 1, because the grids are nested (powers of L, centred).

**Theorem C2.** Under Rule W, (C) holds for every old base point of every level j < k, at every step, for both endpoint sequences.

*Proof.*
- (W1) is Theorem C1.
- (W2): r(R_z, z) <= (a+1) M xi_{p-1} <= (L-1) M xi_{p-1} < L M xi_{p-1} = m_p. Since z is in Omega_p and j <= p-1, Lemma G gives d(z, Omega_{p-1}^c) >= m_p > r. So R_z lies in Omega_{p-1}, which lies in Omega_j. This case includes p = k inside a level-k drop-out with N_k stages.
- (W3): r(R_z, z) <= (a+1) M xi_j < L M xi_j <= s_j <= d(z, Omega_j^c), by Lemmas F and M. So R_z lies in Omega_j.
In each case R0 gives (C). Separation, alignment, boundary rows, read sets and regularity are as in the proof of C1. QED.

**Distances under Rule W.** A complementary row has its carrier at sup distance at least b side(Box) - 2 xi_j from the near region. Every weight of the box metric is at least 1/xi_j. So
- (W1): D >= bM/sigma_j - 2, as in the outline;
- (W2): D >= bM/(L sigma_{j,p}) - 2. For p = k this is bM/(L sigma_j) - 2: the outline's form with b/L in place of b;
- (W3): D >= bM - 2. No age factor is used there (Section 6.2).

So the distance stays of order M/sigma_j at every top-layer base point, (W1) or (W2) with p = k. At a lower-layer base point it is of order M/sigma_{j,p}. A larger scale cannot serve WF8 there: in layer p the field passed the tests of level p and failed those of level p+1, so it is small only at the scale xi_p. Near a seam of level <= j, Lemma N limits the box further, to the distance from that seam.

## 6. The consumers read Rule W

### 6.1 WF13a

WF13a reads Rule W without change of form.
- Declared domain R_z, fine-cube base B_z = Hull_{pi_k} R_z. In (W1) these are the outline's. In (W2) and (W3), R_z has side at most (2a+1) M xi_{k-1} <= (2L-3) M xi_{k-1} < 2 M xi_k, so B_z has at most 3^4 cubes of pi_k. C_win stays a fixed constant, and (WF13c) keeps d_k(Y) <= C_h (m+1).
- One box map for every X of the near sum; the own tent action has support within O(xi_j) of z, inside R_z.
- Long members: a connected X that contains z and leaves Box^{~2} has tree length at least side(Box)/(M xi_j) in old M-cubes. So the long-domain tail (5) of `wf7-bf.md` holds with b_1/sigma_{j,p-1} (W2) or b_1 (W3) in place of b_1/sigma_j.
- If the direction windows are coarser than Box(z), as can happen in (W2) and (W3), every direction that R_z reads is grouped. The complementary term is then zero, and the identity (2) is unchanged, since it holds for any partition of the direction.

### 6.2 WF8-WF10

- **(W1).** Nothing changes. The box, tower, datum and near sum are the outline's. (C) is now proved, not assumed.
- **(W2) with p = k (kept nests).** SA's argument runs at the window scale xi_{k-1}. The Taylor ratio is sigma' = xi_j / xi_{k-1} = L sigma_j, and a window holds at most C_M (L sigma_j)^{-4} old base points. So the base-point sum of (WF8) is at most C_M L^{-4} sigma_j^{-4} C g_j [rho_j^2 L^{4+alpha_H} sigma_j^{4+alpha_H} + rho_j^3 L^6 sigma_j^6] <= C L^2 g_j rho_j^3 sigma_j^{alpha_H}. This is (WF9) with C L^2 in place of C. (WF10) keeps its form: C_M L^{-4} sigma_j^{-4} C d_j rho_j^2 L^4 sigma_j^4 = C d_j rho_j^2.
- **(W2), (W3) with p < k (lower layers).** SA's argument (SA 15996-16084) runs at the local level p in place of k. Its premises hold:
  - the box is a pure tower of one scale with collars, as the pointed window theorem requires (SA 13472-13473);
  - its boundary is at level-j distance at least (a/2) M xi_{p-1} / xi_j, comparable with 1/sigma_{j,p} (SA 13537-13540);
  - R_z lies in Omega_{p-1}, so the local input pair on R_z has resolved levels p-1 or higher, and its affine and Holder sizes are those of a level-(p-1) pair. This costs fixed powers of L.
  The result is WF9_loc <= C g_j rho_{j,p}^3 sigma_{j,p}^{alpha_H} and WF10_loc <= C d_j rho_{j,p}^2, with rho_{j,p} = max{1, alpha_p / alpha_j} <= C (1+p-j)^{1/2}. In (W3) the local age is zero and only Cauchy's inequality is used, as SA does at j = k (SA 16073-16083).

These statements read the box-map package of SA (the "Third" hypothesis, SA 15821-15826: weighted first response, Holder and compatible boundary comparison) for boxes of Rule W. Those boxes are pure Definition A towers of cubes, the same kind of object as the outline's. So the package is the same input as before, at more levels. It is not proved here.

### 6.3 WF11-WF12 at top-layer base points

(W1): unchanged. (W2) with p = k: the factor is e^{-cM/(L sigma_j)}, so (WF11) and (WF12) hold with c/L in place of c. The proof of (WF12) by e^x >= x^n/n! is unchanged (`wf7-bf.md` Section 4).

### 6.4 Proposition L: lower layers, conditional on layer decay

At a lower-layer base point the local (WF9) has the gain sigma_{j,p}^{alpha_H} of the local age p - j, not sigma_j^{alpha_H}. The outline's count of sigma_j^{-4} base points per level-k window then needs a second small factor: the step's direction must be small across the k - p layers between the base point and the integration region. This is the hypothesis below.

**(LD) Layer decay.** On the admitted discs, every datum row c of a Rule W box whose carrier lies in layer p of the common sequence satisfies
  \|v'_c\| <= C_R delta_k (xi_c / xi_p) e^{-theta_L (k-p-1)_+},   with theta_L > 5 log L.

**Proposition L.** Assume (LD) and the inputs of Section 6.2. Then the lower-layer members add to (WF15), per level-k fine cube, at most C s_k sum_{j<=k} omega^L_{k+1-j} g_j, plus the analogous vacuum-only term C s_k sum_j rho_j^2 d_j. Here
  omega^L_n = sum over a + b = n - 1, b >= 1, of (1+a)^{3/2} L^{-alpha_H a} L^{4(b+1)} e^{-(theta_L - 1)(b-1)},
and sum_n omega^L_n < infinity. So (WF15) holds with omega_n replaced by omega_n + omega^L_n, which is still summable.

*Proof.* Fix a lower-layer base point z of level j, with p = p(z) < k.
1. *Room.* R_z meets only the layers p-1, p and p+1: it lies in Omega_{p-1}, and by Lemma G d(z, Omega_{p+2}) >= m_{p+2} > r(R_z, z). On rows in layer p+1 or p-1, (LD) gives the layer-p bound times at most e^{theta_L} or L, fixed factors. So by (LD), T4 and the MS row sum (as in `wf7-bf.md` (3)-(4)), the pair on X moves by at most C_R \|nu\| delta_k sigma_{j,p} e^{-theta_L (k-p-1)_+} per unit nu, in level-j units, with a larger fixed C_R. Divide by the radius alpha_j. Use delta_k / alpha_j = s_k alpha_k / alpha_j <= s_k rho_j, with rho_j <= C (1+k-p)^{1/2} (1+p-j)^{1/2}, and (1+p-j)^{1/2} sigma_{j,p} <= C_age as in (WF2). The normalized displacement is at most C \|nu\| s_k e^{-(theta_L - 1)(k-p-1)_+}. So the substitutions stay in the fixed room on the disc \|nu\| < c_nu e^{(theta_L - 1)(k-p-1)_+} / s_k, by the argument of (WF6).
2. *One Cauchy factor.* Subtract the value at nu = 0. On that disc the window function is bounded by WF9_loc (or WF10_loc). Cauchy's formula gives C s_k e^{-(theta_L - 1)(k-p-1)_+} times WF9_loc for the derivative at zero, exactly as in SA 16087-16099.
3. *Complementary part.* By (4) of `wf7-bf.md` with (LD), it is at most C s_k g_j rho_j sigma_{j,p}^{-3} e^{-cM/(L sigma_{j,p})} e^{-(theta_L - 1)(k-p-1)_+} per window, after the local base count. (WF12) at the local age absorbs sigma_{j,p}^{-3} e^{-cM/(L sigma_{j,p})} into C rho_{j,p}^2 sigma_{j,p}^{alpha_H}.
4. *Count.* A level-k fine cube holds at most (M xi_k / (M xi_{p-1}))^4 = L^{4(k-p+1)} windows of level p-1. Multiply steps 2-3 by this count, put a = p - j and b = k - p >= 1, and sum over p. This gives omega^L. In (W3) a = 0.
5. *Summability.* sum_n omega^L_n <= (sum_a (1+a)^{3/2} L^{-alpha_H a}) (sum_b L^{4b+4} e^{-(theta_L - 1)(b-1)}). Both series converge, the second because theta_L - 1 > 4 log L. QED.

*Standing of (LD).* At s = 1 it follows from T4 (decay e^{-theta d_B} in local units: `wf-room-2.md` Section 1, `a3-derivative.md` 7.3-7.6), the MS row sum, AV, and Lemma BC (`geo-5.md` Section 3.6: d_B(y, E) >= c_g (k-p-1)_+ for a top y of layer p and E in Omega_k). This gives theta_L = theta c_g / 2 >= 32 log L, by the floor theta c_g >= 64 log L. At decoupled s, (LD) is the row-sum bound (O1) of `wf-room-2.md` Section 6 read in the layered metric. It is pending, like (O1). SA 15933-15940 states the outline's own layered room factor 2^nu (1+nu)^{1/2} e^{-c delta_0 M L (nu-1)}, which is the same mechanism.

## 7. What is proved, what stays open, changes for owners

**Proved here (Claude, not yet checked by the other model):**
- Lemma G: consecutive gaps d(Omega_{i-1}^c, Omega_i) >= m_i, a factor L above the bound printed in `geo-5.md`, from the same case list.
- Lemma T: the top gap is at least 2 s_k at the current label, except inside a level-k drop-out with N_k stages.
- Theorem C1: (C) for the outline's windows at every top-layer base point outside such drop-outs. No change of filing is needed there.
- Example C3(a): an admitted label where the outline's level-k window of a lower-layer base point violates (C). Example C3(b): the same at a kept nest, if members sit there.
- Lemma N: near a seam of level <= j, no pure-tower box with (C) reaches farther than delta_z + rho xi_j. So the age factor sigma_j cannot be kept there by any placement or size, and the meet fails the single-scale premise.
- Rule W and Theorem C2: (C) for every old base point at every step, with distance of order M/sigma_j at the top layer and M/sigma_{j,p} in layer p.
- Sections 6.1-6.3: WF13a, WF8-WF10 and, at the top layer, WF11-WF12 read Rule W, with fixed powers of L in their constants.
- Proposition L: given (LD), the lower layers add the summable weight omega^L to (WF15).

**Not used:** the half-cell profile (5.1), the face-movement rule, GEO1-GEO3, GEO5, GEO6 and W3. They describe the component geometry of 2.8. (C) reads only Definition A, the step padding, the fates and the frame.

**Open, in order of difficulty:**
1. (LD) at decoupled s: the layered form of (O1) (`wf-room-2.md` Section 6). It is needed only for lower-layer members. At s = 1 it follows from T4, MS, AV and Lemma BC.
2. The analytic inputs of `wf7-bf.md` are unchanged: T4, AX, AV, MS, PW, Definition D locality, the WF3-WF6 room, and SA's box-map package for WF8. Rule W uses them at more levels, not in a new form.
3. Example C3(b) depends on whether regular members are indexed inside drop-out nests (SA 6322-6324 against SA 20910). Rule W covers both readings, except that (W3) uses Lemma M, which needs the base-point rule of SA 20910.

**Changes for owners (forwarded by the lead):**
- `wf7-bf.md` Result: its premise (C) holds for actual windows of Rule W (Theorem C2), and for the outline's windows at top-layer base points (Theorem C1).
- The WF filing (rank 4): use Rule W. At lower layers, (WF15) carries omega_n + omega^L_n. The readers of (WF15), for example the source bootstrap of SA 16361 onward, need only summability of the weight.
- `geo-5.md` Section 3.3: the induction gives m_i, not only M xi_{i-1}, for the pair (i-1, i).
- `library/t0-skeleton.md`, rank 4 WF7: (C) is no longer the last premise. For lower layers it is replaced by (LD) at decoupled s.
