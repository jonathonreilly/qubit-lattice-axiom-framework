# Check of gap-solve15-astra62.md (FINISH row 1174)

Checker: laptop Claude subagent, Claude Opus 5.5, max reasoning. Check of row 1173.
File under check: `library/gap-solve15-astra62.md` (500 lines).
Status: complete. Sections were appended as the check proceeded.

## Plan (at most eight steps)

1. Read the setting (`library/gap-council-brief.md`) and the whole file under check, in ranges.
2. Read the parts of rows 1161-1171 (`gap-solve9` ... `gap-solve14`) and their checks that the file cites.
3. Check the sparse-endpoint recovery (4), (17), the physical test (18) and the alternatives (23).
4. Check the sharp reversal cost (2 + o(1)) beta N^2 and the decoder exponent (27).
5. Check the endpoint-only case (31) and the obstruction (30).
6. Check everything else, statement by statement.
7. Optional numeric guide (guide only, under 2 GB).
8. Verdict table and the RESULT line.

## Step 1-2 (done): sources read

- Read in full: `library/gap-council-brief.md` (122 lines) and `library/gap-solve15-astra62.md` L1-L500, in three ranges.
- Read the cited parts: row 1155 (`gap-solve7-astra62.md` L44-L213: (3)-(4), (9), (11), (15)); row 1161 (`gap-solve9-astra62.md` L95-L204, L358-L368: the alternatives (9), (13)-(14), (25)); row 1167 (`gap-solve12-astra62.md` L1-L145: (1)-(3), (5), (6)-(7), (9)-(10), the neutral kernel inequality and the rounded charged sign); row 1169 (`gap-solve13-astra62.md` L1-L125, L188-L200: (1)-(9), (14)); row 1171 (`gap-solve14-astra62.md` L36-L46: (2)).
- RESULT lines of the checks of rows 1155, 1161, 1163, 1165, 1167, 1169, 1171 read; S12-S18 of the row-1169 check exist at the cited place.
- All cited lane files exist (prior search files, `parts/gap.md`, `sa-index/`, `gap-phys-seed.md`, `gap-zd-astra.md`, `gap-frameless-2d-astra.md`).

Conventions below. "L" is a line of `gap-solve15-astra62.md`. Unit quaternions carry the R^4 dot product, w_p = (1/2) tr U_p, a_p = 1 - w_p, and |p - q|^2 = 2(1 - p.q).

## Step 3: the sparse-endpoint recovery (4), (17), the test (18) and the alternatives (23)

### C1. Exchange law (1), L17-L23. HOLDS.
- Raw or gauge-fixed exchange of a box layer between two copies drawn given the same E preserves product Haar, since the copies have the same reference given E.
- A plaquette cannot have unobserved edges in two different boxes: a unit face with integer corners never straddles a boundary plane. So the box boundaries separate every face.
- Spatial faces at time s carry one bit eta_s. Their two-copy sum is invariant.
- A temporal face between s and s+1 has bottom edge and temporal links on bit eta_s and top edge on bit eta_{s+1}. Aligned: beta(a^1.v^1 + a^2.v^2). Crossed: beta(a^1.v^2 + a^2.v^1). The difference is beta(a^1 - a^2).(v^1 - v^2) = 2 J_s. This is the zero-field Ising weight exp(J_s sigma_s sigma_{s+1}) with J_s as in (1).
- Swapping layer s swaps (a^1, a^2) together with the temporal links, and swapping layer s+1 swaps (v^1, v^2). Each flips the sign of J_s. So |J_s| is orbit invariant and the sign depends on the representative.
- A top edge on the boundary has v^1 = v^2 and contributes zero. Boundary temporal links are observed and common.

### C2. Arm formula, L25. HOLDS.
- With fixed ends +, the bond variables tau_s = sigma_s sigma_{s+1} are independent with means tanh J_s, conditioned on prod tau = +1. With T_1, T_2 the two arm products (means u, v): E[T_1 | T_1 T_2 = 1] = E[T_1 (1 + T_1 T_2)/2] / P(T_1 T_2 = 1) = ((u+v)/2)/((1+uv)/2).
- The TV between the middle law and its complement is |P(+) - P(-)| = |u+v|/(1+uv) <= 2 delta/(1 - delta^2). Labels of distinct boxes are independent given the orbit, so the costs add.

### C3. Gauge match (2) with (3), L30-L49. HOLDS.
- Axial gauge g_ax = p_U gives \bar U_i(e) = p_U(i,z) U_e p_U(i,z')^{-1} and B(e) = \bar U_0(e). Consecutive \bar U_i differ by the (axial, transverse) plaquette, and squared chord = 2 x deficit.
- (3): |\bar U_i - B|^2 <= 2 i sum_k a_k(e) by Cauchy-Schwarz. Summing over i <= l gives at most (l+1)^2 sum_k a_k <= 2(l+1)^2 S_U. The top bound 2 l S_U follows the same way.
- Top faces agree, so H_z \bar U_l H_{z'}^{-1} = \bar V_l and |H_z - B H_{z'} B^{-1}| <= |\bar V_l - B| + |\bar U_l - B|. Squaring gives C b (S_U + S_V).
- On the transverse boundary p_U = p_V, so H_z = 1. |h_z - h_{z'}| <= |H_z - B H_{z'} B^{-1}|, since |B H B^{-1} - 1| = |H - 1|. Row sums and Cauchy-Schwarz give max h_z^2 <= C b^2 (S_U+S_V) and sum h_z^2 <= C b^3 (S_U+S_V).
- g = p_V^{-1} H^{i/l} p_U equals 1 at i = 0, at i = l (H_z p_U(l) = p_V(l)) and on the transverse boundary. Normal links: |U^g_e - V_e| = |H_z^{-1/l} - 1| <= C h_z / l, total C l^{-1} sum h_z^2 <= C b^2 (S_U+S_V). Transverse links: |U^g_e - V_e| = |H_z^{t} \bar U_i H_{z'}^{-t} - \bar V_i| <= |\bar U_i - B| + |\bar V_i - B| + C|H_z - B H_{z'} B^{-1}|, using (BHB^{-1})^t = B H^t B^{-1} and the Lipschitz power map on the small ball. Summing gives (2).

### C4. Common representative, L51. HOLDS.
- Under an internal gauge q, p_U -> p_U q^{-1} (q = 1 at (0,z) and (l,z)), H_z is invariant, g -> g q^{-1}, and (U^q)^{g q^{-1}} = U^g. So U -> U^g is a section of the internal orbits.
- V depends only on the common boundary data of the layer. Hence the section is the same function for both copies, the reference is the same pushforward in each copy, and exchange preserves it. This is the reason given in the text, and it is correct.

### C5. (5), L68-L72. HOLDS.
- S_U + S_V <= 2 S^alpha + 1/beta <= (2K+1) b^3/beta <= c/b^2 when b^5 <= c_0 beta with c_0 = c/(2K+1).
- (2) for each copy against the common V: sum |v^1 - v^2|^2 <= C K b^5/beta. sum |a^alpha - v^alpha|^2 = 2 T^alpha. So sum |a^1 - a^2|^2 <= C K b^5/beta, and Cauchy-Schwarz in (1) gives |J_s| <= (beta/2)(C K b^5/beta) = C K b^5.
- The top end slice uses raw links, so (2) is not available there. Omitting that interface is correct.

### C6. Usable interfaces, L74. HOLDS.
- Violation at an interface means S^1+T^1 or S^2+T^2 exceeds K b^3/beta, hence their sum does. The faces of m distinct interfaces are distinct, at most C_1 m b^3.
- Each copy is marginally Wilson. Markov at parameter c beta/2, Cauchy-Schwarz and row 1155 (9) (constant c = 1/8 there) give exp[-(cK/2) m b^3] C^{C_1 m b^3}. Fewer than r/3 usable means at least 2r/3 - 1 bad interfaces among r. 2^r subsets and n^3 boxes give C n^3 e^{-c' r b^3}.

### C7. Proof of (4), L56-L66, L76. HOLDS.
- tanh x <= 1 - e^{-2x} <= exp(-e^{-2x}). At least r/3 usable interfaces per arm give |u|, |v| <= exp[-(r/3) e^{-2CKb^5}].
- |J_s| is orbit invariant, so this bound is an orbit-measurable event. Its complement has probability at most C n^3 e^{-c' r b^3}.
- Total TV <= C n^3 exp[-(r/3) e^{-2CKb^5}] + C n^3 e^{-c' r b^3}. With r >= C_A e^{C_0 b^5} log n and C_0 > 2CK this is below n^{-A}.
- Swapping all middles maps (X^1, O^1, E) to (X^2, O^1, E), and X^2 is conditionally independent of O^1 given E. This is exactly L(E,O) L(X|E).

### C8. Size of the observation, L78. HOLDS.
- b^5 = o(min(beta, log n)) gives e^{C_0 b^5} = n^{o(1)}. At slope [kappa_0, kappa_1], b = c_gamma (log n)^{1/5} with c_gamma small gives e^{C_0 b^5} log n <= n^gamma and b^5 <= c_0 beta. Box face area O((n/b)^3 b^2) = O(n^3/b) per layer.

### C9. (6) forward, L83-L93. HOLDS.
- Two applications of (4) and kernel contraction give TV(P_X, (K_0 x K_t) L(E_0,E_t)) <= 2 n^{-A}. The same channel maps the product of skeleton marginals to the exact product of middle marginals. Affinity increases under channels. Changing one argument by TV eps costs at most ||sqrt p - sqrt q|| <= sqrt(2 eps), since 1 - Aff <= TV. So H_X >= H_E - 2 n^{-A/2}.
- sqrt of the pair density is the kernel U^t/sqrt(Tr U^{2t}), so H_X <= ||U^t||/sqrt(Tr U^{2t}) = (Tr U^{2t})^{-1/2}.
- Excited sum < 1/2 at 2t. With k = floor(n/(4t)) >= 256 and 2tk <= n/2: sum lambda_i^{n/2} <= sum lambda_i^{2tk} <= (sum lambda_i^{2t})^k < 2^{-256} < 1/1650.

### C10. (6) necessity, L95. HOLDS.
- Relative to two independent stationary segments, the periodic density of the four ends is p_s(x_+, y_-) p_s(y_+, x_-)/X(2t) (vacuum factors telescope). Each connector has independent stationary arguments, so E(p_s - 1)^2 = X(2s) - 1 = delta. E|FJ - 1| <= 2 sqrt(delta) + delta by Cauchy-Schwarz, and 0 <= X(2t) - 1 <= delta. This matches the checked row-1167 shape argument.

### C11. Recovery (17), L244-L259. HOLDS.
- Bad large components: a component meeting S_i with at least k_0 = floor(w/10) faces contains a rooted connected k_0-set within distance k_0 of S_i, inside the observed region. Row 1167 (2) applies to it (both paths Wilson, adjoints equal there, opposite traces on B so a_p + a'_p = 2). C n^4 roots and C^{k_0} shapes give C n^4 (C sqrt(h_beta))^{k_0}.
- Small components: all their incident 3-cubes lie in the observed region, so each is closed by d^2 = 0. Adjacency through common 3-cubes puts every B-face of such a cube in the same component. A dual 2-cycle in a box shorter than the periods has a dual 3-chain filling in the box. In dual terms the boundary is computed globally, so dc_j = component_j holds on the whole torus.
- The switch (U, U'_0, U'_t) -> (c_0 c_t U, c_0 U'_0, c_t U'_t): it fixes all adjoints and all relative cochains (the buffered regions are disjoint since w << t - 2r), so the selection is unchanged and the map is an involution. On a selected face the two traces are opposite, and both flip, so the weights exchange. Z(A_i) is unchanged. So the three-path law is preserved.
- On the good event d(a + c) = 0 on every 2-face of S_i, since every B-face on S_i lies in a selected component.
- H_1: the pair (T^3, coarse 2-skeleton) has zero relative cellular chains in degrees 1 and 2, so H_1 of the 2-skeleton maps isomorphically onto H_1(T^3; Z/2) = (Z/2)^3. Subdivision and the time interval do not change this. A closed Z/2 cochain on S_i is a flat flip plus a vertex coboundary. So the entire fundamental skeletons agree modulo vertex gauges and G.
- Winding change: the row-1167 six-face argument (three transverse coordinate lines through the winding, two distinct jumps each) gives d_* >= max(6, k/2) for a component whose filling changes the winding. Rooting within C(k+1) of n links gives C' n h_beta^6.
- Equivariant K_i (averaging over vertex gauges and flips) factor through the quotients. The coupling uses that the switched original has the Wilson law. Total errors are as in (17).
- At fixed slope kappa > 0, n^4 (C sqrt(h_beta))^{w/10} ~ n^{4 - kappa w/20 + o(1)}, so a fixed w > 80/kappa suffices.

### C12. Physical test (18), L261-L269. HOLDS.
- Sufficiency: Hellinger contraction and (17) give d_G <= d_wall + O(sqrt(eps_G)). Row 1167's kernel inequality needs 2 sqrt(m)/(1+m) - d_G > sqrt(2/3) with m = 8^{-1/2}. Numerically 0.87859 - 0.03125 = 0.84734 > 0.81650 (Step 7). So the neutral trace at u is below 3/2. The checked rows 1161/1167 then give the seed or a chi_1-odd sign with opposite-middle correlation at least (2/3)(1 - 2^{-46})(1 - 81 2^{-46}) = 0.6667 > 3/5.
- Under the identical channels the conditional mean is s_i f(A_i): flipping the supplied sign moves the output by the nontrivial G/H coset. E[s_0 s_t f f] = E[m f f] <= (E m^2)^{1/2}, and 2 p_wall = 1 - E m^2. p_wall > 8/25 gives (E m^2)^{1/2} < 3/5, a contradiction up to 2 eps_H = o(1).
- Necessity: the segment comparison of C10 at radius r + w + 2 = o(n) makes the full collars TV-close to their product. Then d_wall <= sqrt(2 TV) -> 0. The global chi_1-odd flat flip fixes A_i and flips s_i, so E|m| <= 2 TV and p_wall -> 1/2.
- Slope: n h_beta^6 <= C n (1+beta)^9 e^{-6 beta} -> 0 when liminf beta/log n > 1/6. The J_R^0 replacement costs 2 C n t h_beta^6 = o(1) at slope > 1/3 (row 1167 (9) with |R| = n t).

### C13. Alternatives (23), L332-L347. HOLDS (given the checked row-1161 premise and propagation).
- Exact recovery: equal B_i gives U'_e = eps_e U_e on S_i with d eps = 0 on its faces, hence eps = flip + coboundary (C11). So E_i agrees modulo gauge and G exactly.
- Screening at fixed beta (L327): |J_s| <= (beta/2) 4 x 3(2b)^3 = C beta b^3 deterministically, so each arm product is at most exp(-r e^{-2C beta b^3}). With r = floor(N/16) the two-collar TV is C N^3 exp(-c M_N). Then p_B <= p(Y) + C N^3 e^{-c M_N} <= (1/2) sum_{chi_1(h)=-1} zeta_h + C N^3 e^{-c M_N} by (20)-(21) (checked in Step 6).
- Competing seed (row 1161 alternative II): with direction 2 as time on N^4, a twist h with chi_1(h) = -1 has a nonzero static 41 flux m; its 42 part is a commuting temporal insertion g with |eigenvalues| = 1, so |Tr(g F_m^N)| <= Tr F_m^N <= 8 Tr(P_0 F_m^N) by row 1161 (3). Row 1161 (14) gives X_{m,0}(N; N^3) <= (1/71) exp[-N log(1/q_*)/(2n_j)]. So each zeta_h <= C_j e^{-c_j N}.
- Periodic seed (alternative I): both gaps are N/2 - 2r >= 3N/8, so 2s >= 3N/4 >= N/2 and delta = X(2s) - 1 <= S_per(N/2; N^3) <= C_j e^{-c_j N} by the checked propagation. TV <= C sqrt(delta). Under the product, s_i is uniform given B_i (the chi_1-odd flat flip is flat, so it fixes plaquette signs). So |p_B - 1/2| = E m^2/2 <= TV.
- Exclusion: at fixed b, M_N grows linearly, so sublinear -log p_B along a subsequence contradicts C_j e^{-c_j N} + C N^3 e^{-c M_N}. With b^3 = c' log N and C beta c' <= 1 - alpha, M_N >= N^alpha and liminf -log p_B / N^alpha = 0 suffices.

## Step 4: the sharp reversal cost (24)-(25) and the decoder (26)-(27)

### C14. Lower bound (24), L356-L367. HOLDS.
- Both completions are lifts of the same adjoints, so they differ by a sign cochain a, and D = da vanishes on every face of both S_i (equal face signs).
- Small components (size < N/100): each is closed, lifts to a box of width < N/4, and has a global filling c_j with dc_j = D_j. Since D_j has no face on S_i, c_j restricted to S_i is closed. A direction-1 line on a grid plane with x_3 outside the filling box misses supp c_j, and all parallel direction-1 lines on S_i are homologous in S_i (also across time). So c_j has zero period on the chosen winding. a' = a - sum c_j keeps both periods, and D' = da' is the union of the large components.
- g(y,z,s) = sum_{x_1} a'_1(x_1,y,z,s). A jump across a transverse edge forces an odd number of faces of D' in the unit strip swept by the winding, all containing direction 1. Distinct edges give disjoint strips.
- On grid planes in a collar, g equals the collar period (C11 cohomology). Disagreement of the two products makes the two collar periods differ.
- Paths: for y = Y + k, 0 <= k < 2b, the path (Y,z,k) -> (y,z,k) -> (y,z,N/2-k) -> (Y,z,N/2-k). Endpoints lie in the collars since k + 1 <= 2b < r. Vertical parts sit at distinct (y,z); horizontal arms in one strip sit at distinct times k; strips are disjoint half-open x_2 ranges. The second family uses times -k-1 and N/2+k+1 and the other arc, and its times never equal k' or N/2 - k' because k, k' < 2b < N/2. So 2N^2 edge-disjoint paths, each with a jump: d_1(D') >= 2N^2.
- Probability: {D' = S} is contained in {S subset of the relative curvature}. Row 1167 (2) gives h_beta^{d_*(S)} <= h_beta^{max(2N^2, |S|/2)}. Unions of large components of total size k: at most 100k/N pieces, compositions <= 2^k, shapes <= C_0^k, roots (6N^4)^{100k/N} <= C^k for large N. The sum over k in [2N^2, 4N^2] is at most 2N^2 (C_1^2 h_beta)^{2N^2}, and the tail is geometric with ratio C_1 sqrt(h_beta). With h_beta <= C(1+beta)^{3/2} e^{-beta} this gives (24).
- Precision (reading only): the paths need the grid planes x_2 = Y to be common to the two collars. This holds for the single tiling of (23) (L332, "tile") and of (17) (L244). No change.

### C15. Arbitrary centre updates, L369. HOLDS.
- A mu-preserving transition with F(U') = F(U) has U and U' each with conditional law mu(.|F). Two Bernoulli(v) variables differ with probability at most 2 min(v, 1-v) <= 4 v(1-v), and E[2 v(1-v)] = p_fix.

### C16. Axes, L378-L383. HOLDS.
- Crossing a box boundary has chance O(1/l) and costs at most 4. Inside a box the closed word (tree path, edge, reverse tree path) contracts through O(l) faces (strips of width one past the later coordinate runs), hence certainly through C l^2 faces. Bi-invariance and Cauchy-Schwarz give E|W-1|^2 <= C l^2 sum E|U_p - 1|^2 <= C l^4/beta, and |Ad_W v - v| <= 2|W - 1|. The stated bound is valid (not sharp). l = min(beta^{1/5}, N^{1/4}) and w = min(N^{1/3}, delta^{-1/2}) give delta -> 0, w -> infinity, w delta -> 0, w = o(N).

### C17. Two trial maps, L385. HOLDS.
- Phi_1: left rotation of the interface temporal links by exp(eps a(x_1) v_x); the axes use only spatial adjoints of the lower slice, which are fixed. So Phi_1 is a Haar-preserving bijection for fixed auxiliaries.
- Phi_2 adds the central flip of the direction-1 cut links on the slices between the two interfaces that contain middle 0. This flip is flat on spatial faces (a 12- or 13-face at the cut holds two flipped links) and on temporal faces inside the interval. Its curvature is the N^2 + N^2 cut faces at the two interfaces, which are the critical faces of the jump.
- Both maps fix all spatial adjoints and all face signs on S_i (the interfaces lie in the gaps), and change the interface temporal adjoints identically. So they induce one bijection j on F. Given F, the two image paths stay independent.

### C18. Single-path cost, L387. HOLDS.
- D(Phi_* mu || mu) = beta E_mu[S(Phi U) - S(U)] for a Haar-preserving bijection.
- New holonomy at a face with lower edge xy: exp(-eps a(x) v_x) exp(eps a(y) v') W with v' = Ad_{U_xy} v_y. |exp(a v') - exp(a v)| <= |v' - v|. With equal axes the eps-average multiplies w by cos(a(x) - a(y)).
- Critical face: a(x) = 0, a(y) = pi/2, so the new trace is eps Re(v' W) up to the central sign; its eps-average is exactly 0. The mean cost is beta E w_old <= beta. There are 2N^2 such faces.
- Ramp faces: at most C w N^2, each costing at most beta[(Delta a)^2/2 + |v - v'|] with Delta a <= pi/(2w). Total C beta N^2 (1/w + w delta) = o(beta N^2).

### C19. Common marginal, L389-L394. HOLDS.
- After either map a critical face has holonomy (unit imaginary) x W, so |w_new| = |v'.Im W| <= |Im W| <= |1 - W|, uniformly in the axes. E|1 - W| <= (2 E a_p)^{1/2} = O(beta^{-1/2}).
- V <= sum_{D_0} a_p and all D_0 faces contain direction 1, so row 1167 (1) gives log E e^{beta V} <= 2N^2 log(1/z_beta) = O(N^2 log(2+beta)).
- Donsker-Varadhan with f = beta V: D(j_* mu_F || mu_F) >= 2 beta N^2 (1 - C beta^{-1/2}) - C N^2 log(2+beta) = (2 - o(1)) beta N^2.

### C20. Upper bound in (25), L396; statement L372-L376. HOLDS.
- Chain rule: D(Q||P) = D_F + E[D_1(.|F) + D_2(.|F)] and D_k = D_F + E[D_k(.|F)]. So D(Q||P) = D_1 + D_2 - D_F, with average at most (4 + o(1)) beta N^2 - (2 - o(1)) beta N^2.
- Under Q the disagreement event has probability exactly 1 - p_fix: Phi_1 changes no spatial link, and Phi_2 reverses s_0 only. Data processing to this event: (1 - p_fix) log(1/p_fix) - log 2 <= D(Q||P). With p_fix -> 0 from (24), -log p_fix <= (2 + o(1)) beta N^2. Together with (24) this is (25), with no condition on the relative rates.

### C21. Decoder (26), L401-L412. HOLDS.
- Lifts of fixed adjoints are 2^{#links} sign choices; the constraint is the face signs on S_i. Finite, independent of the enumeration, gauge invariant.

### C22. Maximality inequality, L414-L419. HOLDS.
- If J differs from Z, some maximizer V has the wrong product (in a tie the rule returns +1, and both classes attain the maximum). With a = rel(U,V) the small-component removal of C14 applies verbatim. V' = a'V is admissible (d a' = D' has no face on S_i), equals V off D', and has w_p(V') = -w_p(V) = w_p(U) on D' because D' is part of da. Maximality gives sum_{D' in P_1} w_p(U) + (K/beta) sum_{D' off P_1} w_p(U) <= 0. The disjoint paths give m >= 2N^2.

### C23. Error bound in (27), L421-L426. HOLDS.
- The event is beta sum_1 a + K sum_o a >= beta m + K l. Hoelder with weights alpha, 1-alpha, alpha = 1 - 8K/beta: the first factor is (E e^{beta sum_1 a})^alpha <= z_beta^{-alpha m} (row 1167 (1)); the second has exponent alpha K/(1-alpha) = alpha beta/8 <= beta/8, so row 1155 (9) with c = 1/8 gives C^{(1-alpha) l}. Exponential Markov gives the displayed bound.
- With at most C_1^{m+l} placements and K > 4(1 + log C_1), the l-sum is bounded and the m-sum from 2N^2 gives exp{-2N^2[beta - 8K - log C_1 - log(1/z_beta)]} <= exp{-2N^2[beta - C log(2+beta)]}.
- J is F-measurable, so Pr(J != Z) >= E min(v, 1-v) >= E v(1-v) = p_fix/2. With (25) the exponent is exactly 2.
- Two completions given only B: each is marginally mu, so |P(J != J') - p_B| <= 2 Pr_mu(J != Z).

### C24. Conditional variance identity, L428. HOLDS.
- With m_F = E[Z|F] and m_B = E[m_F|B]: 2 p_B = 1 - E m_B^2 = 1 - E m_F^2 + E Var(m_F | B) = 2 p_fix + E Var(m_F | B).

## Step 5: the endpoint-only case (31) and the obstruction (30), with (28), (29), (32)

### C25. (31), L476-L483. HOLDS.
- The map is row 1169's two-profile map (checked, S12-S18 of the row-1169 check). Its noncentral part lies in the profile boxes, which sit wholly in the time gaps. Elsewhere it is the central multiplier sigma on the direction-1 cut links over an interval containing exactly one collar. Inside the collars sigma is flat, so it fixes all adjoints and all fundamental face signs of S_i, including temporal faces. So B (and also the padded walls A_i, when the boxes avoid the padding) is fixed pointwise, and s is reversed at one end.
- Applied to the first completion only: given the image first path, the second path still has law mu(.|B), so the joint entropy equals D(Phi_* mu || mu). Row 1169's cost with b = R ~ beta^{1/3} is C N^2 beta^{1/3} log(2+beta) on average over signs and axes, hence for some fixed choice.
- The image disagreement probability is exactly 1 - p_B. Data processing gives d(1 - p_B || p_B) <= cost. p_B = (1 - E m^2)/2 <= 1/2. For p <= 1/4, (1 - 2p) >= 1/2 and (1-p)/p >= 1/(2p), so d(1-p||p) >= (1/2) log(1/(2p)). If p_B > 1/4 the bound is trivial. This gives the first inequality.
- With (25): log(p_B/p_fix) = (2 + o(1)) beta N^2 - O(N^2 beta^{1/3} log(2+beta)), so the ratio tends to 2.

### C26. Margin (28), L433-L439. HOLDS.
- Both classes occur: a central cut on an interval holding one collar fixes F and reverses the product.
- For a best wrong-class lift V, V' = a'V differs from U by the compact fillings only, which have zero period on both S_i. So V' has the true product and M_Z >= M_{-Z} + 2 sum_{D'} t_p w_p(U).
- On the event, beta sum_1 a + K sum_o a >= beta m + K l - beta gamma N^2. The Markov bound of C23 gains a factor e^{alpha beta gamma N^2}; the m-sum from 2N^2 then gives exp{-(2-gamma) beta N^2 + C N^2 log(2+beta)}.

### C27. Stability (29), L441-L453. HOLDS.
- Equal adjoints on S_i and g = 1 there allow the same representatives on S_i. The constraints and the winding lines lie in S_i, so the feasible sign assignments and their class labels coincide for U and (U')^g. J is gauge invariant.
- For a common assignment, |Re X - Re Y| <= |X - Y| <= sum over the four edges, so the objectives differ by at most D(U,U') (plus the infimum allowance). Class maxima move by less than gamma N^2. A margin above 2 gamma N^2 for U then forces J(U') = Z, so Z' != Z needs J(U') != Z'. Union bound with (28) for U and (27) for U' (marginally mu). No independence is used.

### C28. Obstruction (30), L455-L460. HOLDS.
- For beta >= K, t_p <= 1; a link lies in six faces; the chord is at most 2. So o(N^2) changed adjoint links (in a gauge equal to 1 on both S_i) give D <= 12 o(N^2) < gamma N^2 eventually. (29) gives -log Pr{Z != Z'} >= (2 - gamma) beta N^2 - C N^2 log(2+beta) - log 2. Let gamma -> 0.
- Precision (reading only): (30) inherits the hypotheses of (29): U' is marginally mu and B_0, B_{N/2} are preserved. The text says "In particular" after (29), so this is the intended scope.
- Attainment: redrawing the centre lift given F changes no adjoint link and has Pr{Z != Z'} = p_fix, rate 2 by (25). The m-step statement is linearity of expectation under stationarity.

### C29. Proposal cost (32), L486-L493. HOLDS.
- The proof of (29) leaves {margin(U) <= 2 gamma N^2} and the event {J(U') != Z'} under nu. Data processing to that event: p log(1/q) - log 2 <= D(nu||mu) with q = Pr_mu(J != Z) <= exp{-2N^2[beta - C log(2+beta)]}. This is (32).
- If Z' = -Z surely and D(nu||mu) = o(beta N^2), then Pr{D < gamma N^2} -> 0 for each gamma < 2.

### C30. Binary comparison, L496. HOLDS.
- p_fix = 2 e_N (1 - e_N) for any v_N. u_N = v_N (1 - e_N) + (1 - v_N) e_N = e_N + (1 - 2 e_N) v_N and p_B = 2 u_N (1 - u_N). For v_N = e^{-sigma N}: log(p_B/p_fix) = 2 beta N^2 - sigma N + O(1), ratio -> 2. For v_N = 1/2: p_B = 1/2 and the ratio -> 2. Both hold for beta ~ log N.

## Step 6: everything else

### C31. Header, L3-L11. GUIDE and OPEN as marked; consistent.
- L3, L5, L7, L11 are GUIDE. The cited lane files exist. External PR and outline line ranges were not re-read here (reading only). The credits (Sussman-Alpoge with Claude and Codex as authors of their text, Balaban, Chatterjee) match rows 1167 and 1169.
- L9 (OPEN) restates the seed threshold 1/1650 at n/2 and the repaired (W) exactly as in the council brief and row 1167 L9. "Row 1171's estimates are unchecked at this pin" is true of the pin. Row 1171 now has a HOLDS check (row 1172), but this file never uses its twist estimates (L15, L311, L347 say so). No change.
- L15 (GUIDE): the cited contents of rows 1155 (3)-(9) and 1169 (15)-(18) are as described.

### C32. Box cost (7), L102-L106, proof L123-L133. HOLDS.
- L(theta) = log int exp(-(1-theta)W - theta W o tau) d(ref); L(0) = L(1) since tau preserves the reference. L'' = Var_theta(D_*). L'' >= k gives L(1/2) - (L(0)+L(1))/2 <= -k/8, and this is the log affinity.
- The (2)-representative depends only on boundary and direction-1 links (p_U, p_V, H_z and the cut-locus rule). So stride-four direction-2 edges keep Haar reference.
- The marked v couples to a in W and to the other lower spin in W o tau; its interpolated field is h + lambda beta a with |H| <= 6 beta. For a one-layer interval the second interface adds a linear term absorbed in w and h. For D perpendicular to w and H_0, Pi_D d = Pi_D a. Case |H| <= 2|H_0|: |d wedge H| = |d wedge H_0| gives |Pi_{H perp} d| >= eta/2, and the transverse term of (8) gives beta^2 Var >= c. Case |H| > 2|H_0|: |H| < 2 beta |d| and the radial term gives the same. H = 0: isotropic. No face holds two marked spins, so the conditional variances add.

### C33. One-link variance (8), L108-L114. HOLDS.
- Var(d.z) = d_par^2 Var(cos theta) + |Pi_perp d|^2 E[sin^2 theta]/3, by rotational symmetry about H. The normalizer is at most C(1+h)^{-3/2}; each angular interval [1,2]/(8 sqrt(1+h)) and [4,5]/(8 sqrt(1+h)) has mass at least c; their values of 1 - cos theta are at most 1/(32(1+h)) and at least 1/(8(1+h)) - O((1+h)^{-2}). So Var(cos) >= c (1+h)^{-2} and E sin^2 >= c/(1+h).

### C34. Plane projection (9), L116-L121. HOLDS.
- Haar density of u = |Pi_D a| is 2u. The tilt factor is I_0(|H_D| u) I_0(|H_{D perp}| sqrt(1-u^2)); I_0 is increasing with |(log I_0)'| <= 1. On [0, 2 eta], 6 beta x (u'^2 - u^2) stays below 1, so the second factor changes by at most e. The annulus [eta, 2 eta] has Haar mass 3 eta^2 against eta^2 for the disk. So P(u >= eta) >= c.

### C35. Label refresh (10), L135-L139. HOLDS.
- Removing a maximal flipped interval changes only the two boundary bonds, ratio exp(-2J_{s_1-1} - 2J_{s_2}) = d(tau_* P)/dP. min(1, L) <= sqrt(L), so the mean is at most the affinity (7). At most r^2 intervals. The end labels are fixed, so the neighbours of a maximal interval lie in the collar, as (7) requires.

### C36. Scalar comparison, L144-L154. HOLDS.
- Bridge means solve f_{s+1} + f_{s-1} = (2 + lambda + mu^2) f_s; middle value (f_r + f_{-r})/(2 cosh(alpha r)); Dirichlet lambda >= c/b^2 gives alpha >= c'/b. Precision ||Q|| <= 16 + mu^2 in four dimensions, so the bridge covariance is at least (16 + mu^2)^{-1} I. End-data differences have mean square at most C n^3 mu^{-2}. Gaussian translation TV <= (1/2)||Sigma^{-1/2} d||. With mu^{-1} = n^2/L^2 this gives (4) at r = C_{A,L} b log n.
- Mode 2 pi/n: alpha <= m ~ 2 pi/n, t alpha <= 2 pi/1024 < 1/100. rho = 1/cosh(t alpha), sqrt(1 - rho^2) = tanh(t alpha). The Gaussian affinity is det(S_1)^{1/4} det(S_2)^{1/4}/det((S_1+S_2)/2)^{1/2} = (1-rho^2)^{1/4}/(1-rho^2/4)^{1/2} <= (1/10)/(sqrt(3)/2) = 1/(5 sqrt 3). Projection raises affinity, and the channel bound of C9 carries it to the skeletons.

### C37. Twist screening bound (11), L159-L165. HOLDS.
- No h-odd cycle on the observed graph makes h a vertex coboundary sigma there; sigma-gauge times the flat flip fixes every observed link, preserves the measure and acts as h on both middles. So L(X_0|E) is h-invariant and the product reconstruction is invariant under flipping X_0 alone. TV(P, phi_* P) <= 2 x error. Aff(P, phi_* P) = int int U^t(x,y) U^t(hx,y)/Tr U^{2t} = zeta_h(2t), and TV >= 1 - Aff.

### C38. Observed twist (12), L167-L171. HOLDS.
- Equivariant channels; each reconstructed pair is within 2 n^{-A} of the true one; fibre Cauchy-Schwarz and two square-root costs sqrt(4 n^{-A}) give zeta_h + 4 n^{-A/2}.

### C39. Zero-curvature obstruction, L173. HOLDS.
- (2) at S_U = S_V = 0 would give a global gauge matching 1 and h, but their odd windings are 1 and -1. In the slab with two fixed end faces the transport q between the faces is invariant under boundary-fixed gauges and the curvature is zero.

### C40. Moving interfaces (13), L178-L184. HOLDS.
- Every column of a stride-four transverse edge goes from bit 0 at the collar end to bit 1 at the middle, so a first change exists. At that face, v couples to a in W and, in W o tau, to the other copy's lower spin transported by temporal links with arbitrary prescribed bits. The coefficient of v in D_* is beta(a - w) with w independent of a, v (other faces of v contribute linear terms without a). Exchanging freely sampled links preserves the product reference. (8)-(9) and C32 give (13).

### C41. Information bound (14), L186-L191. HOLDS.
- E_P[min(1, L)] <= affinity. For a reference T' independent of Y, the flag has mean at most e^{-c b^3}. D(Bern(p)||Bern(q)) >= p log(1/q) - H(p) >= p log(1/q) - log 2, and data processing to the flag bounds it by I(T;Y). L193 (OPEN) is a correct scope statement.

### C42. Three-step exponent (15), L198-L215. HOLDS.
- c_i = (q_i + q'_i)/2, d_i = (q_i - q'_i)/2 give c.d = 0, |c|^2 + |d|^2 = 1; the endpoint swap is d_3 -> -d_3; fields and c-bonds are common; the remaining exponent is 2 beta F.
- w with <w d_i, c_i> = 0 (i = 1,2) exists in Im H (two linear equations in three unknowns). exp(+-k pi w/3) keeps d_k in c_k-perp with its radius, fixes d_0 and reverses d_3. Bond dots average to half. So max F' >= max F/2; max F >= 0 (the uniform mean of F is zero); max F - max F' <= 3/2.
- Caps: d_i ranges over a 2-sphere in c_i-perp when c_i != 0 and over S^3 when c_i = 0. A cap of angular radius 1/(1+beta) has probability at least c(1+beta)^{-3} in both cases, so the stated bound is the correct uniform one. Lower bound: ends x = y = -x' = -y' give max F = 3 and max F' = max_z (sqrt(2+2z) - z) = 3/2 at z = -1/2.

### C43. Uniform consequence, L217. HOLDS.
- Birkhoff contraction tanh(D/4) = (sqrt R - 1)/(sqrt R + 1) with R = e^D, by the same chord argument as row 1155. 1 - tanh((3 beta + O(log))/4) >= c (1+beta)^{-C} e^{-3 beta/2}. At slope below 2/3 the number of three-step blocks needed is n^{1 - epsilon} polylog = o(n).

### C44. Column with long memory (16), L222-L239. HOLDS.
- Summation by parts on the circle: beta sum (q_{i+1} - q_i).(c_{i+1} - c_i) = sum h_i.q_i with h_i = beta(2c_i - c_{i-1} - c_{i+1}), |h_i| <= 2 beta.
- Zero energy forces q_i - c_i = z with |z + c_i| = 1 for all i; the differences of the c_i span Im H, so z is real and z = +-sqrt(3)/2. On {Re x Re y <= 0} the energy has a positive minimum, so T <= e^{-c beta} there.
- Palindrome c_0..c_6 = (i, -i, j, k, j, -i, i)/2 gives T = A A^T >= 0, invariant under Re-reflection. The ball test gives lambda >= c (1+beta)^{-9}. The odd trial psi sgn(Re q) has Rayleigh quotient >= lambda - 2 e^{-c beta} (int psi <= 1). This is (16). L239's contraction contradiction follows.

### C45. Reverse channel (19), L274-L285. HOLDS.
- Q has density FJ/X(2t) and \hat Q has density M^2/X(2t) against two independent stationary segments. E[F | x,y] = p_{2R+d}(x,y) = p_t(x,y) = M; E F^2 = X(2d); E M^2 = X(2t); so E(F - M)^2 = X(2d) - X(2t). Given the middles, F and J are independent, so the middle marginal is exact. (F-M)J + M(J-M) and Cauchy-Schwarz give (1/2)(1 + sqrt q) sqrt(q - 1).

### C46. Small error, L287-L291. HOLDS.
- Log-convexity of X: 2t - 4R = (4R/t) t + (1 - 4R/t) 2t. Each character trace is (1/8) sum_h chi(h) Tr(h U^t) <= Tr(P_+ U^t), since Tr(h U^t) >= 0. So X(t) <= 8 Tr(P_+ U^t).

### C47. Charged comparison (20), L293-L303. HOLDS.
- 2 p(B) = min_{|f|<=1} E(Z - f(B))^2 at f = E[Z|B]. A predictor built from a channel of B is admissible, and the loss lies in [0,4], so the minima differ by at most 4 TV.
- A -> Y with Z carried: the (17) H-channel's neutral output depends on A_i only and its output sign equals the input sign (the winding is in the skeleton and K_i keeps it). Error eps_H.
- Y -> A with Z carried: the (19) channel's adjoint output has the same law over the G-orbit of the middle and keeps s_i at the centre. Error eta(q).

### C48. Deck bounds (21), L305-L311. HOLDS.
- w_z proportional to U^t(x, zy)^2; zeta_h = E sum_z sqrt(w_z w_{z+h}); p(Y) = 2 E u(1-u).
- For chi_1(h) = -1: sum_z sqrt(w_z w_{z+h}) = 2 sum_{chi_1(z)=1} sqrt(w_z w_{z+h}) <= 2 sqrt(u(1-u)); Jensen gives zeta_h^2 <= 2 p(Y). Sum over the four odd h of sum_z w_z w_{z+h} is 2u(1-u), and w_z w_{z+h} <= (1/2) sqrt(w_z w_{z+h}). Reading note: row 1171 (2) is a different observable (p_h for one h, three windings); the shared item is the deck identity for zeta_h, as the text says. L313 (OPEN) is a correct scope statement.

### C49. Optimal power (22), L318-L325. HOLDS.
- Angles <= C a/b, deficits <= C delta^2/beta, total <= C b^3/beta. Boundary-to-boundary transport exp(i l_2 a) is gauge fixed; |e^{i l_2 a} - 1|^2 >= c b^2 a^2 for l_2 a <= 1; Cauchy-Schwarz over at least c b^2 disjoint lines gives beta sum >= c b^5. With constant time extension, a^alpha = v^alpha and J_s = (beta/2) x mismatch, so (5) is sharp in power.

### C50. Fixed-beta regime, L327. HOLDS.
- Deterministic |J_s| <= C beta b^3 (C13). Matching powers with (10) for b^3/log n. The scope sentences are correct.

### C51. Geometric cost, L349. HOLDS.
- The relative sign cochain on S_i is a flat flip plus a coboundary, so its period is chi_1(h) on every direction-1 line of S_i. Lines on grid planes give at least c N^2/b link-disjoint lines; an odd period forces a raw difference on each. L351 (OPEN) is correct.

### C52. Local centre examples, L465-L471. HOLDS.
- C_6 example: convolution by the uniform measure on {+-1} is an orthogonal projection, so the transfer is positive semidefinite after the flatness and gauge sandwich. A central cut flip on an interval holding one collar keeps all constraints, adjoints and S_i face signs and reverses one product: the two-completion probability is exactly 1/2. The C_3 winding is conserved in time and uniform. |tr|/2 of the winding is 1 or 1/2 with masses 1/3, 2/3, read by both walls. Affinity (1 + 2 sqrt 2)/(3 sqrt 3) = 0.7368; d = sqrt(2(1 - Aff)) = 0.725 > 1/32 (Step 7).
- C_2 example: all adjoints are pure vertex gauge, so disjoint walls are independent; flatness in spacetime gives equal windings, so p_B = p_wall = 0. The text correctly says these are not Wilson counterexamples.

### C54. Scope statement L97 (OPEN). Consistent.
- (4)-(6) indeed reduce the test to sparse skeletons but bound nothing between the two skeletons. A partial exchange without the common boundary changes spatial faces at the box walls, as stated.

### C53. Closing OPEN L498 and RESULT L500. HOLDS as a summary.
- Every positive item in L500 is checked above: (4), (17), (18), (23), (25), (27), (31), (30). The OPEN items (order-one charged probability, physical neutral bound, (W), the Jaffe-Witten gap) are correctly left open.

## Step 7: numeric guide (GUIDE only; proves nothing)

Three scratch scripts (pure Python and numpy, not committed; peak memory under 250 MB, each under 4 s):
- Ising middle mean (u+v)/(1+uv) against brute force on chains of up to 8 bonds: maximal error 8e-16 (L25).
- Constants: (2/3)(1 - 2^{-46})(1 - 81 2^{-46}) = 0.66667 > 3/5; 2 sqrt(m)/(1+m) - 1/32 = 0.84733 > sqrt(2/3) = 0.81650 for m = 8^{-1/2}; sqrt(9/25) = 3/5 (L269).
- C_6 example: affinity (1 + 2 sqrt 2)/(3 sqrt 3) = 0.73678, square-root distance 0.7256 > 1/32 (L469).
- Gaussian pair affinity: the determinant formula equals (1-rho^2)^{1/4}/(1-rho^2/4)^{1/2}; at t alpha = 2 pi/1024 = 0.00614 it is 0.0902 < 1/(5 sqrt 3) = 0.1155 (L154).
- max over unit vectors of x.u + u.v - v.x is 1.5000 and of x.u + u.v + v.x is 3.0000 (L215).
- d(1-p||p) - (1/2) log(1/(2p)) >= 0.20 on p <= 1/4 (L483); D(Bern p || Bern q) >= p log(1/q) - log 2 on 2e5 samples (L191, L396).
- Deck bounds of (21) on 2e4 random weight vectors on (Z/2)^3: both inequalities hold to rounding (L311).
- max of (z-1)(R-z)/(z(R-1)) equals (sqrt R - 1)/(sqrt R + 1) for R = 1.5, 4, 50, 1e4 (L217).
- (8): min (1+h)^2 Var(cos) = 0.25 and min (1+h) E sin^2 = 0.75 for h in [0, 3e4] (L108).
- (9): min P(|Pi_D a| >= 1/(8 sqrt(1+beta))) = 0.954 over beta <= 1000 and all splits of a field of length 6 beta (L118).
- z_beta (1+beta)^{3/2} decreases to 0.798 at beta = 1e4 (row 1167 (1), used in (24), (25), (27)).
- H^1 over Z/2 of a box-boundary skeleton times a time interval, computed by GF(2) ranks on four complexes (N = 8, 9, 10; time steps 0 to 3; unequal box sides): dimension 3 in every case, and 120 random closed cochains all had equal periods on every direction-1 line of the skeleton (L255, L345, L363).
- (15) lower-bound configuration (zero fields, x = y = -x' = -y'), by one-dimensional log-domain quadrature: 2 log(B(x,x)/B(x,-x)) - 3 beta = -2.8, -6.6, -9.8, -12.7, -14.1 at beta = 1, 4, 16, 64, 128; the ratio to log(2+beta) stays between -3.8 and -2.5. This is 3 beta - O(log(2+beta)), as claimed.

## Step 8: verdict table and result

| Item | Statement | Lines | Verdict |
|---|---|---|---|
| C1 | exchange law (1) | L17-L23 | HOLDS |
| C2 | arm formula, TV 2 delta/(1-delta^2) | L25 | HOLDS |
| C3 | boundary-fixed gauge match (2), (3) | L30-L49 | HOLDS |
| C4 | common representative | L51 | HOLDS |
| C5 | (5) | L68-L72 | HOLDS |
| C6 | usable-interface probability | L74 | HOLDS |
| C7 | screening (4) | L56-L66, L76 | HOLDS |
| C8 | size of the observation | L78 | HOLDS |
| C9 | seed test (6), forward | L83-L93 | HOLDS |
| C10 | (6), necessity | L95 | HOLDS |
| C11 | wall recovery (17) | L244-L259 | HOLDS |
| C12 | physical test (18) | L261-L269 | HOLDS |
| C13 | fixed-bare alternatives (23) | L332-L347 | HOLDS (given the checked row-1161 premise and propagation) |
| C14 | area bound (24) | L356-L367 | HOLDS (reading precision: common grid planes) |
| C15 | arbitrary centre updates | L369 | HOLDS |
| C16 | axes | L378-L383 | HOLDS (bound valid, not sharp) |
| C17 | two trial maps | L385 | HOLDS |
| C18 | single-path cost | L387 | HOLDS |
| C19 | common-marginal entropy | L389-L394 | HOLDS |
| C20 | sharp cost (25) | L372-L376, L396 | HOLDS |
| C21 | decoder (26) | L401-L412 | HOLDS |
| C22 | maximality inequality | L414-L419 | HOLDS |
| C23 | decoder exponent (27) | L421-L426 | HOLDS |
| C24 | variance identity | L428 | HOLDS |
| C25 | endpoint-only (31) | L476-L483 | HOLDS |
| C26 | margin (28) | L433-L439 | HOLDS |
| C27 | stability (29) | L441-L453 | HOLDS |
| C28 | obstruction (30) | L455-L460 | HOLDS (scope precision: hypotheses of (29)) |
| C29 | proposal cost (32) | L486-L493 | HOLDS |
| C30 | binary comparison | L496 | HOLDS |
| C31 | header | L3-L11 | GUIDE and OPEN as marked; consistent |
| C32 | box cost (7) | L102-L106, L123-L133 | HOLDS |
| C33 | one-link variance (8) | L108-L114 | HOLDS |
| C34 | plane projection (9) | L116-L121 | HOLDS |
| C35 | label refresh (10) | L135-L139 | HOLDS |
| C36 | scalar comparison | L144-L154 | HOLDS |
| C37 | twist screening bound (11) | L159-L165 | HOLDS |
| C38 | observed twist (12) | L167-L171 | HOLDS |
| C39 | zero-curvature obstruction | L173 | HOLDS |
| C40 | moving interfaces (13) | L178-L184 | HOLDS |
| C41 | information bound (14) | L186-L193 | HOLDS |
| C42 | three-step exponent (15) | L198-L215 | HOLDS |
| C43 | uniform consequence | L217 | HOLDS |
| C44 | long column memory (16) | L222-L239 | HOLDS |
| C45 | reverse channel (19) | L274-L285 | HOLDS |
| C46 | small error | L287-L291 | HOLDS |
| C47 | charged comparison (20) | L293-L303 | HOLDS |
| C48 | deck bounds (21) | L305-L313 | HOLDS (reading note on row 1171 (2)) |
| C49 | optimal power (22) | L318-L325 | HOLDS |
| C50 | fixed-beta regime | L327 | HOLDS |
| C51 | geometric cost | L349-L351 | HOLDS |
| C52 | local centre examples | L465-L471 | HOLDS |
| C53 | closing OPEN and RESULT | L498, L500 | HOLDS as a summary |
| C54 | scope statement | L97 | OPEN as marked; consistent |

Counts: 54 items. 52 HOLD (C13 conditional on the checked row-1161 inputs, as the text states). 2 GUIDE/OPEN items are consistent as marked. None HOLDS AFTER CORRECTION. None FAILS.

Reading precisions (no change to any statement or constant):
1. L365 (and its reuse at L414, L438): the 2N^2 disjoint paths need the grid planes x_2 = Y to be common to the two collars. This holds for the single tiling of (23) (L332) and of (17) (L244).
2. L455-L460: (30) inherits the hypotheses of (29): U' marginally ordinary and B_0, B_{N/2} preserved.
3. L311: row 1171 (2) is a different observable (p_h for one h, with three windings). The shared content is the deck identity for zeta_h, which is what the text claims.
4. L383: the closed word passes through O(l) faces, so the stated C(l^{-1} + l^4/beta) is valid but not sharp.

Not re-read here: the external PR and outline line ranges in L5-L7 (GUIDE, reading only).

RESULT: HOLDS - check of row 1173 (`library/gap-solve15-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort) as FINISH row 1174, positive claims first: 54 statements, 52 HOLD, 2 GUIDE/OPEN as marked, none HOLDS AFTER CORRECTION, none FAILS; the sparse-wall screening (4) (|J_s| <= C K b^5 on usable interfaces from the boundary-fixed match (2)) and the recovery (17) (switching plus H^1 of the box-boundary skeleton = (Z/2)^3) hold, (18) is equivalent to (W) at slope > 1/6, and (23) holds given the checked row-1161 premise; with all intervening adjoints and the wall face signs shared, (24) holds from 2N^2 edge-disjoint jump paths and (25) -log p_fix = (2 + o(1)) beta N^2 holds from D_1 + D_2 - D_F, as does the decoder exponent (27); (31) -log p_B <= C N^2 beta^{1/3} log(2+beta) and log(p_B/p_fix)/(beta N^2) -> 2 hold; (28)-(30) and (32) hold, so updates moving o(N^2) adjoint links have rate at least 2; four reading precisions (L365 common grid planes, L455 scope of (30), L311 row 1171 (2) observable, L383 non-sharp axis bound); guide runs (pure Python and numpy, under 250 MB) agree and prove nothing; an order-one charged probability, the physical neutral bound, (W) and the four-dimensional SU(2) mass gap remain OPEN.
