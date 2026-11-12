# Check of library/gap-sos-astra.md (FINISH row 830), by Claude Opus 5.5, line by line

Clone `/Users/jonreilly/ym4d-lead/clone` at commit `18e8aa1c9bda55d00d769d159bd3c5a7164c6556` (pulled; already up to date). The note entered the clone in `2a10cd8ef`.
Lane D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target `D/library/gap-sos-astra.md` (655 lines), read in full. Author: Codex gpt-6-astra max. The note names its own assignment FINISH row 827; this check is row 830.
Context read: `D/library/gap-flat-astra.md` (F8)-(F11) at lines 175-240; `D/library/gap-flat-check-opus.md` in full; `D/library/gap-rtail-check-opus.md` in full; `D/library/gap-rtail-astra.md` (R25)-(R26) at lines 610-645 and the anchors of (R12), (R19).

Method. I re-derived every step by hand. After the hand derivation, two small GUIDE scripts (Python, well under 1 GB; `guide/guide.py` and `guide/guide2.py` beside this report) brute-forced the neighbourhood on small 4D tori and re-did the rational arithmetic. They decided nothing. Every GUIDE value agreed with the hand result.

Notation is the note's. Base directions 1,2; transverse direction 3; the other transverse direction 4. c = cosh(beta), s = sinh(beta)/2, q = s c^8.

## 1. The SOS class (S3), closure, wrapping, connectedness

**Construction.** h is an integer function on the A = mn base faces. S(h) has one roof over f at height h_f and, over a base edge e between f and g, the d_e = |h_f - h_g| consecutive walls between the two heights. So |S(h)| = A + k with k = sum_e d_e. HOLDS.

**Boundary form.** On the cylinder, C_h is the mod-two union of unit cubes in the column over f between 0 and h_f. The boundary of C_h is the sum of cube boundaries. Over f, the bottom face cancels P and the top face sits at h_f. A side face over e survives exactly at the levels strictly between the two column tops on the two sides, that is at the d_e wall levels. So S(h) = P + boundary(C_h). P is closed and a boundary is closed, so S(h) is closed. A boundary pairs to zero with the twist cocycle, so S(h) keeps the odd pairing of P. HOLDS.

**Connectedness.** Adjacent roofs share a link when the heights agree. Otherwise the wall stack over e joins them, and consecutive walls share horizontal links. The base adjacency graph is connected. So S(h) is link-connected. HOLDS.

**Finite period n_3.** Admissibility is d_e < n_3 at every edge. I checked that this gives distinct faces and the stated degrees after projection:
- Roofs over different base faces are different plaquettes. Walls over different edges are different plaquettes. The d_e walls over one edge have d_e < n_3 distinct residues. Roofs and walls have different orientations. So no face repeats and the projected chain equals the projected set. Projection commutes with the boundary, so closure and the odd pairing survive. HOLDS.
- A horizontal link over e at level j lies only in the two roofs over f, g and the walls over e with lower endpoints j-1 and j. With d_e <= n_3 - 1, I_e has d_e + 1 <= n_3 distinct residues. The two roof levels are distinct mod n_3, and the end walls never wrap onto the opposite roof. So each used horizontal link has degree exactly two. At d_e = n_3 both roofs coincide mod n_3 and the link has degree four; the note says so. HOLDS.
- A vertical link at v lies only in walls over the four edges at v. Each edge contributes at most one wall per residue. So the degree is at most four, and it is even by closure. HOLDS.

**Lifts.** "All height functions in one fundamental slab" satisfy d_e <= n_3 - 1. Taller lifts with the local inequality are also included. The class therefore excludes exactly height winding without a global lift and walls of length >= n_3; Section 7 lists both. HOLDS.

**(S4).** H = sum_e (d_e + 1) = 2A + k, since the base has 2A edges and residues are distinct. Each wall has two vertical links, so the vertical degree sum is 2k = 2(L - b) + 4b. So L = k - b and |E(S)| = 2A + 2k - b. L >= b gives b <= k/2. Note that b counts degree-four links *after* projection. Example: cyclic heights 0, 2, 4, 2 at one vertex, n_3 = 3. The wall sets mod 3 are {0,1}, {2,0}, {2,0}, {0,1}, so level 0 has degree four, while b_lift = 0 on the cylinder. So b and b_lift do differ, as the note says. HOLDS. GUIDE: on 3x3, 3x4, 4x4 bases with n_3 in {3,4,5,9}, the brute-force H, L, |E(S)| equal (S4) in every trial.

Verdict: HOLDS.

## 2. The height-dependent neighbourhood (S5)-(S9 geometry), and the pillar special case

**(S5), by orientation.** All used links lie at x_4 = 0 and point in directions 1, 2 or 3.
- 12: a horizontal plaquette at level j over f contains only the four horizontal links of f at level j. It meets E(S) iff j lies in some I_e with e in the boundary of f. So the count is sum_f |F_f|. Correct.
- 13, 23: these are e x [j, j+1] at x_4 = 0. Their links are e at levels j and j+1 and the vertical links over v, w at lower level j. So the plaquette meets E(S) iff j lies in I_e, in I_e - 1, in J_v or in J_w. The count is sum_e |K_e|. Correct.
- 14, 24: a plaquette e' x [x_4, x_4+1] meets E(S) iff e' at x_4 = 0 is used, so x_4 in {-1, 0}. Two per used horizontal link, all distinct: 2H. Correct.
- 34: two per used vertical link by the same argument: 2L. Correct.
- 13, 23, 12 plaquettes at x_4 != 0 contain no link at x_4 = 0. Correct.
The orientation classes are disjoint. Every roof is counted in some F_f and every wall in some K_e, so S lies inside the count and subtracting A + k is exact. Taking the level sets mod n_3 before counting identifies plaquettes by (base cell, residue). So (S5) is exact on the torus. HOLDS.

**(S6), by hand.** All I_e around f contain h_f, so F_f is the interval from the minimum to the maximum over f and its four edge neighbours: |F_f| = 1 + r_f. At v, J_v is [min_v, max_v): at each level in that range the cyclic threshold pattern is nonconstant, so some edge carries a wall there. For K_e: I_e union (I_e - 1) = [a_e - 1, z_e]. Each J_v is [min_v, max_v - 1] with min_v <= a_e and max_v >= z_e, so it overlaps or abuts [a_e - 1, z_e]. Hence K_e is the interval [min(a_e^*, a_e - 1), max(z_e^* - 1, z_e)], of size d_e + 2 + (z_e^* - z_e - 1)_+ + (a_e - a_e^* - 1)_+. Substituting into (S5):

A + r + k + 4A + T + 2(2A + k) + 2(k - b_lift) - (A + k) = 8A + 4k + r + T - 2 b_lift.

HOLDS on the cylinder. After projection, a torus plaquette contains a projected used link iff some lift contains a lifted used link. So projected N(S) is the image of lifted N(S), and the faces of S stay distinct. Hence (S6) is an upper bound after projection. HOLDS. Precision P1: nbr(f) in r_f means the four edge neighbours; the vertex-diagonal faces enter only through a_e^*, z_e^*.

GUIDE: on the cylinder (n_3 = 2R + 4) the brute-force count equals (S5) and (S6) in 30 random trials. At small n_3 it equals (S5) in every trial and lies strictly below (S6) in 26 of 30.

**Pillar special case, orientation by orientation.** One face f at height L, all others at 0, L <= n_3 - 2. Then k = 4L, H = 2A + 4L, b = 0, L_vert = 4L.
- 12: f gives 0..L, that is L + 1. Its four edge neighbours give L + 1 each. Others give 1. Total A + 5L. This is (R19)'s 12 count.
- 13, 23: an edge of f has K_e = [-1, L], size L + 2 (four edges). An outward edge at a corner of f has I_e = {0}, I_e - 1 = {-1}, J_v = [0, L), so K_e = [-1, L-1], size L + 1. There are 8 of them; with periods >= 3 no other edge has both ends at corners of f. All other edges give 2. Total 4A + 4L + 8(L - 1) = 4A + 12L - 8. This is (R19)'s count.
- 14, 24: 2H = 4A + 8L. 34: 2L_vert = 8L.
- Sum 9A + 33L - 8. Subtract A + 4L: **8A + 29L - 8**, exactly (R19).

From (S6) directly: r = L (for f) + 4L (neighbours) = 5L; T = 8(L - 1) from the eight outward corner edges (z^* - z - 1 = L - 1); b_lift = 0. So 8A + 16L + 5L + 8L - 8 = 8A + 29L - 8. HOLDS. Binary heights: T = 0, r = M (faces touching a boundary edge), b_lift = v_4, giving (R12)'s first expression 8A + 4k + M - 2v_4. HOLDS. GUIDE: pillars L = 1, 2, 3 on a 5x5 base give 221, 250, 279 by brute force, equal to 8A + 29L - 8.

**(S7).** Each used link has six distinct ambient plaquettes (periods >= 3). Incidences (plaquette, used link) number 6|E(S)|. Faces of S carry four each; each outside face of N(S) carries at least one. So M <= 6(2A + 2k - b) - 4(A + k) = 8A + 8k - 6b, with the projected b. It holds on the torus. For the pillar it reads 8A + 32L >= 8A + 29L - 8, consistent. HOLDS. GUIDE: (S7) held in every trial.

Verdict: HOLDS (precision P1, wording).

## 3. The joint Haar bound (S8)-(S9)

**Input.** (F8) gives |W_m(H)| <= prod u(S) with u(S) = c^{|N(S)\S|} int prod_(p in S) |sinh(beta x_p)| dU_(E(S)). (S1) is this u. (F9) accepts any majorant b(S) >= u(S). (F10) is Finner's inequality; its condition is sum_(p ni e) 1/h_p <= 1 at every link, over faces carrying a function. Only faces of S carry functions. Checked in gap-flat-check-opus section 3. READ, HOLDS.

**Moments.** The recursion (2l+2)M_l = (2l-1)M_(l-1) gives M_1 = 1/4 and M_2 = (3/6)(1/4) = 1/8. HOLDS.

**Exponents, link by link.** Exponent 4 on every wall touching a projected degree-four link; exponent 2 on all other faces of S.
- Horizontal links: degree two (item 1). Their two faces have exponents in {2, 4}, so the sum is at most 1/2 + 1/2. HOLDS.
- Vertical links of degree two: two walls, sum at most 1. HOLDS.
- Vertical links of degree four: the four faces of S there are the four walls over the four base edges at v, all touching that link, all with exponent 4. Sum 4/4 = 1. HOLDS.
- High degree at corners where several walls meet. Inside this class the maximum link degree is four, also after projection: a vertical link meets at most one wall per incident base edge and residue. The projected-only contact of the 0,2,4,2 example is a degree-four link and is covered by the projected b. Degree six cannot occur, since a vertical link has only two non-wall plaquettes (direction 34) and neither is in S. No roof touches a vertical link. HOLDS.
- A wall with exponent 4 also touches degree-two links; there 1/4 + 1/2 or 1/4 + 1/4 is at most one. HOLDS.

**Count of exponent-four faces.** Each degree-four link has four incident walls, so at most 4b; also at most k walls. So min(k, 4b). HOLDS.

**Norms.** |sinh(beta x)| <= |x| sinh(beta) by convexity on [0,1] and oddness. Each U_p is Haar distributed, so the h-norm is a group moment. ||.||_2 <= sinh(beta)(1/4)^(1/2) = s. ||.||_4 <= sinh(beta)(1/8)^(1/4) = 2^(-3/4) sinh(beta) = 2^(1/4) s. So the joint integral is at most s^(A+k) 2^(min(k,4b)/4), and (S9) follows with the exact M of (S5). HOLDS. The bound is for the joint integral; no defect independence enters.

**(S8).** With c >= 1 and (S7), u <= s^(A+k) c^(8A+8k-6b) 2^(min(k,4b)/4) = q^(A+k) c^(-6b) 2^(min(k,4b)/4).
- b <= k/4: factor (2c^(-6))^b, at most max(1, (2c^(-6))^(k/4)).
- k/4 <= b <= k/2: factor 2^(k/4) c^(-6b) <= (2c^(-6))^(k/4).
So u <= q^A [q max(1, 2^(1/4) c^(-3/2))]^k = q^A t^k, with q 2^(1/4) c^(-3/2) = 2^(1/4) s c^(13/2). k = 0 gives q^A. HOLDS.

Verdict: HOLDS.

## 4. The translated comb-tree Hölder bound (S10)-(S14)

**Graph.** With m, n >= 3 the base adjacency graph is a simple 4-regular torus graph: A vertices, 2A edges. HOLDS.

**Comb tree T_H.** n rows of m faces, each a cycle of m horizontal edges. Removing one edge per row leaves n paths with n(m-1) edges. A vertical path in one column adds n - 1 edges. Total mn - 1 = A - 1, connected, so a spanning tree. HOLDS.

**Inclusion probabilities.** The translation group Z_m x Z_n acts transitively on horizontal edges and on vertical edges. So over the mn translates a horizontal edge has probability n(m-1)/(mn) = (m-1)/m, and a vertical edge (n-1)/(mn). T_V by symmetry: (m-1)/(mn) and m(n-1)/(mn) = (n-1)/n. HOLDS. Coinciding translates (if any) are just repeated weights; Hölder is unaffected.

**(S11).** Horizontal probability of the mixture: lambda(m-1)/m + (1-lambda)(m-1)/(mn). Setting it to r_0 and multiplying by mn: (m-1)(1 + lambda(n-1)) = (mn-1)/2. So lambda(n-1) = (mn - 2m + 1)/(2(m-1)), which is (S11). Each tree has A - 1 edges, so the mixture's expected edge count is A - 1. With all horizontal edges at r_0 = (A-1)/(2A), horizontal edges take (A-1)/2 in total. The vertical edges take the other (A-1)/2, equally by transitivity, so also r_0. Positivity: numerator m(n-2) + 1 > 0; 2(m-1)(n-1) - (mn - 2m + 1) = mn - 2n + 1 = n(m-2) + 1 > 0. HOLDS. GUIDE: exact fractions confirm both probabilities equal (A-1)/(2A) and 0 < lambda < 1 for 3 <= m, n <= 7.

**(S12).** sum_T w_T E_T(h) = sum_e |h_f - h_g| (sum_(T ni e) w_T) = r_0 k(h). So t^k = prod_T (u^(E_T))^(w_T) with u = t^(1/r_0) = t^(2A/(A-1)). Hölder with exponents 1/w_T (reciprocals sum to one) gives (S12) on a finite height box. HOLDS.

**Tree sum and pinning.** Orient tree edges away from f_0. With h_(f0) = 0, the map h -> (increments on tree edges) is a bijection from pinned functions onto Z^(A-1). So the tree sum is K(u)^(A-1), K(u) = (1+u)/(1-u), finite for 0 < u < 1. Each box sum is bounded by the full pinned sum; monotone convergence gives the first inequality in (S10). The height translation is pinned once, so no height-range factor enters. HOLDS.

**Per-edge factor and convergence.** 2A/(A-1) > 2 and 0 < t < 1 give u < t^2, and K increases, so K(u) <= K(t^2). The per-edge factor is K(t^2) = (1+t^2)/(1-t^2). The condition is t < 1 for finiteness and rho = q K(t^2) < 1 for decay. HOLDS.

**(S14).** For direction 3 the encoding is (root residue mod n_3, x_4 coordinate, pinned lift): N_perp = n_3 n_4 choices. Direction 4 gives another N_perp. Every admissible surface has at least one encoding, so the class sum is bounded by 2 N_perp q^A Z^ht(t). Extending to all pinned integer functions (also non-admissible ones) only adds nonnegative terms. Then q^A K(t^2)^(A-1) <= (q K(t^2))^A since K >= 1. Flat planes (k = 0) and terraces are included. HOLDS.

Verdict: HOLDS.

## 5. The interval 0 < beta <= 5/11 (S15)-(S19)

**Monotonicity.** s, c increase on beta > 0, so q, both entries of t, and rho = q(1+t^2)/(1-t^2) increase. The endpoint suffices. HOLDS.

**(S16).** x = 5/11, x^2 = 25/121.
- sinh: term ratios x^2/((2n)(2n+1)) <= x^2/6. So sinh x <= x/(1 - x^2/6) = (5/11)(726/701) = 330/701, hence s <= 165/701. HOLDS.
- cosh: ratios from the quadratic term are x^2/((2n+1)(2n+2)) <= x^2/12. So cosh x <= 1 + (25/242)(1452/1427) = 1 + 150/1427 = 1577/1427. And 1577 * 19 = 29963 < 29967 = 21 * 1427. HOLDS.

**Powers.** 21^4 = 194481, 19^4 = 130321: 388962 < 390963, so c^4 < 3/2. 21^5 = 4084101, 19^5 = 2476099: 12252303 < 12380495, so c^5 < 5/3. Then c^8 < 9/4 and c^13 < (9/4)(5/3) = 15/4 = 960/256 < 961/256 = (31/16)^2. 25^4 = 390625 > 388962 = 2 * 21^4, so 2^(1/4) < 25/21. HOLDS.

**(S17).** q < (165/701)(9/4) = 1485/2804; 1485 * 15 = 22275 < 22432 = 8 * 2804, so q < 8/15. Next (25/21)(165/701)(31/16) = 127875/235536 = 42625/78512; 42625 * 11 = 468875 < 471072 = 6 * 78512, so the second entry is below 6/11. Since 8/15 < 6/11, t < 6/11. HOLDS.

**rho.** t^2 < 36/121 and (1+y)/(1-y) increases, so rho < (8/15)(157/85) = 1256/1275 < 1. HOLDS. GUIDE: at beta = 5/11, q = 0.5231, t = 0.5355, rho = 0.9438; rho = 1 near beta = 0.4592. The margin is real and the endpoint is not optimal, as the note says.

**(S18)-(S19).** With N_perp <= 4a^2 and A >= a^2: B_SOS <= 2 N_perp e^(-tau_S A) <= 8a^2 e^(-tau_S a^2). Since a^2 e^(-tau a^2) <= 1/(e tau) <= 1/tau, B_SOS <= 8/tau_S and e^(2B) <= e^(16/tau_S). (S2) then gives (S19). Also |T_m(F_SOS)| <= (e^(2B)-1)/2 <= B e^(2B). The original Z_m and all decorations are kept through (F8)-(F9). HOLDS. Precision P2: the constant e^(16/tau_S), tau_S = log(1275/1256) ~ 0.0150, is about e^1066; the note calls it explicit, not useful, and claims nothing more.

Verdict: HOLDS (precision P2).

## 6. The three-height growth argument (S20)-(S22)

**Admissibility.** Heights in {-1, 0, 1} give d_e <= 2 < 3 <= n_3. With the root at 0 these lifts give distinct surfaces, since -1, 0, 1 are distinct mod n_3. So the majorant sum over this subclass is at least q^A sum_(h in {-1,0,1}, h_(f0)=0) t^(k(h)). HOLDS.

**Expected k.** Under P (independent 1/4, 1/2, 1/4 off the root): for two free neighbours P(|diff| = 1) = 2(1/2)(1/2) = 1/2 and P(|diff| = 2) = 2(1/4)(1/4) = 1/8, so E|diff| = 1/2 + 2/8 = 3/4. At the root E|h| = 1/2. The root has four distinct neighbours (periods >= 3). E k = (2A - 4)(3/4) + 4(1/2) = 3A/2 - 1. HOLDS.

**Entropy and Jensen.** H(1/4, 1/2, 1/4) = (1/2) log 4 + (1/2) log 2 = (3/2) log 2 = log(2 sqrt 2). So H(P) = (A-1) log(2 sqrt 2). P has full support on the A - 1 free faces, so sum_h t^k = E_P[exp(k log t - log P)] >= exp(E k log t + H(P)) = t^(3A/2 - 1)(2 sqrt 2)^(A-1). Multiplying by q^A gives (S20). HOLDS.

**(S21).** cosh(1/2) > 1 + 1/8 = 9/8; (9/8)^6 = 531441/262144 > 2 since 531441 > 524288. So 2c^(-6) < 1, the second entry of t is q 2^(1/4) c^(-3/2) < q, and t = q. sinh(1/2) > 1/2 + 1/48 = 25/48, so s > 25/96. (9/8)^8 exceeds its first five binomial terms: (4096 + 4096 + 1792 + 448 + 70)/4096 = 10502/4096. Then q > (25/96)(10502/4096) = 131275/196608, and 3 * 131275 = 393825 > 393216 = 2 * 196608. HOLDS.

**(S22).** (2 sqrt 2 q t^(3/2))^2 = 8 q^2 t^3 = 8 q^5 > 8 (32/243) = 256/243 > 1. So the right side of (S20) grows like (256/243)^(A/2) up to the 1/(2 sqrt 2 t) prefactor. The general condition 8 q^2 t^3 > 1 is the same computation. HOLDS. GUIDE: q(1/2) = 0.6811, 8q^5 = 1.1725. At beta = 5/11, 8q^2t^3 < 8(8/15)^2(6/11)^3 < 1, consistent with Section 5.

**What it refutes.** It refutes area decay of the sum of the coarse majorant q^A t^k over the admissible class at beta = 1/2, for any summation method, already on three heights. It therefore shows that (S8) plus any exact or sharper summation cannot reach beta = 1/2. HOLDS.

**What it does not refute.** It gives no lower bound on u(S), on (S9) with the exact M of (S5), on D_m(S), on T_m or on R_m. A majorant can grow while the bounded quantity decays. It says nothing about roughening: (S10) keeps every fixed-volume sum finite for t < 1. The note states all of this. HOLDS.

**Precision P3 (scope of "the coarser majorant").** (S20)-(S22) concern the b-maximised form q^A t^k. The intermediate form q^(A+k) c^(-6b) 2^(min(k,4b)/4), from (S9) with (S7), is smaller pointwise when 2c^(-6) < 1, and (S20) does not address it. My own estimate: under P, a vertex away from the root has a four-way contact at level -1 with probability 2(1/4)^2(3/4)^2 = 18/256, and likewise at level 0, so E b = (9/64)A + O(1). With min(k,4b) >= 2b (from b <= k/2), the extra Jensen penalty per face is at most (9/64)(6 log c - (1/2) log 2) ~ 0.053 at beta = 1/2. The (S22) rate per face is (1/2) log(8q^5); the rational bound q > 2/3 gives only 0.026, but the true value 0.080 (GUIDE) exceeds 0.053. So the intermediate majorant very likely grows too, but this is not proved by rational bounds here. The note's OPEN statement concerns only the exact-M (S9), which is accurate.

Verdict: HOLDS (precision P3, scope).

## 7. Section 7: the union class, the remainder, the scope

**(S23).** (R26) gives B_(G_*) <= 6 N_perp e^(-tau' A) with tau' the minimum of the first three entries; (S18) gives 2 N_perp e^(-tau_S A). The union bound gives 8 N_perp e^(-tau A) with tau the minimum of all four, and N_perp <= 4a^2, A >= a^2 give 32 a^2 e^(-tau a^2). Using the smaller majorant on overlaps only helps. The G_* bounds hold on 0 < beta <= 1/2, so the union holds on (0, 5/11]. HOLDS.

**(S24).** B <= 32/tau, so e^(2B) <= e^(64/tau); (S2) with G_** first gives C_0 = 32 e^(64/tau). The order inside G_** does not matter for the class sum of |D_m| bound. HOLDS.

**Input status.** The note says row 823's proofs had no check at its pin `b9dabda`. I confirmed `gap-rtail-check-opus.md` is absent at that pin. It is present at the current clone, and it finds every PROVED step of gap-rtail-astra.md HOLDS, including (R6), (R18), (R22) and (R25)-(R26). So the caveat is now discharged. Precision P4 (dated wording only).

**(S25).** p_m = (1/2Z_m) int C [Xi(w_m) - Xi(w_m^(G**))] + (1/2Z_m) int C [Xi(w_m^(G**)) - Xi(w_m^O)] = T_m(G_**) + R_m^**. Exact. In the (F4) form, R_m^** sums compatible marked families in O not contained in G_**, with unflipped exterior weights; no positivity is asserted. HOLDS.

**(RTAIL-SOS) equivalence.** T_m(G_*) + R_m^* = p_m = T_m(G_**) + R_m^**, so R_m^* - R_m^** = T_m(G_**) - T_m(G_*). Ordering G_* first, (F2) makes this the sum of D_m over G_** minus G_*, bounded by (S24). The maximum of -tau a^2 + kappa a is kappa^2/(4 tau), which absorbs C_0 a^2 e^(-tau a^2) into C a^p eta_*^(a/2). So (RTAIL-SOS) and (RTAIL*) agree on any I in (0, 5/11], up to constants and powers. HOLDS.

**Scope.** G_* contains A_* (all shapes of excess at most A/128), the terraces and the separated pillars. So the complement of G_** has excess above A/128 and is neither a separated-pillar surface nor an admissible one-direction graph. Binary terraces and single pillars of height at most n_3 - 2 are themselves admissible graphs, so they lie in F_SOS; the statement is consistent. HOLDS. The four bullets each name where the scalar-height proof stops:
- Overhangs: no single h_f, so (S3), (S4) and the tree bijection fail. Correct.
- Handles and branchings outside the class: extra sheets are not paid by total variation. Correct.
- Two transverse directions: a link has six ambient plaquettes, and with faces in both 3 and 4 directions all six can be in S; branchings can then touch horizontal faces. The exponent-four assignment of item 3 relies on degree at most four and on roofs avoiding branching links. Correct as a statement of method failure.
- Winding without a lift, full-period walls: outside the class of Section 2. Correct.
No factorisation into independent defects is used anywhere in (S3)-(S24). The pointer to (R23)-(R24) is accurate. HOLDS.

Verdict: HOLDS (precision P4, dated wording).

## 8. Section 8: groups and the seed

**Group use.** Geometry, (S5)-(S7) and (S10)-(S14) use no group. (F7)-(F8) use the central sign, Haar invariance, zero mean and |x| <= 1 (checked in gap-flat-check-opus section 7). The new Haar step uses only E x^2 = 1/4, E x^4 = 1/8 and |x| <= 1. (S20)-(S22) concern a majorant expression in q and t, so they are group-free given the same s, c. HOLDS.

**Binary icosahedral fourth moment.** Values of x: 1 and -1 (one each), 0 (30), plus or minus 1/2 (20 each), plus or minus a and plus or minus b (12 each), a = (1+sqrt5)/4, b = (1-sqrt5)/4. a^2 = (3+sqrt5)/8, b^2 = (3-sqrt5)/8; a^2 + b^2 = 3/4; ab = -1/4, so a^2 b^2 = 1/16; a^4 + b^4 = 9/16 - 2/16 = 7/16. E x^4 = [2 + 40/16 + 24(7/16)]/120 = (2 + 5/2 + 21/2)/120 = 15/120 = 1/8. HOLDS. GUIDE: 0.125. E x^2 = 1/4 was checked before. So (S3)-(S22) transfer unchanged; (S23)-(S24) also transfer, since G_* needs E x^6 = 5/64, which this group shares (gap-flat-check-opus section 7). HOLDS.

**U(1).** E cos^2 = 1/2 and E cos^4 = 3/8. The exponent-two factor becomes sinh(beta)/sqrt2 > s, so (S8)'s constants do not transfer. Only this is claimed. HOLDS.

**Weak coupling.** q >= s > beta/2 >= 1 for beta >= 2. The claim concerns only these estimates. HOLDS.

**Seed.** The paragraph is READ or OPEN. It claims no full-seed extension above 2/9 and states that (RTAIL-SOS) on a higher interval plus the consumer's transfer hypotheses would still be needed. I did not re-check gap-vmf-lip.md or the consumer. Fair.

**Verification paragraph.** It claims hand arguments only and asks for an independent check. Accurate. The `/tmp` source and file-check records were not re-read here; nothing in the mathematics depends on them.

Verdict: HOLDS.

## 9. The RESULT line

Each clause matches a step that HOLDS: the exact neighbourhood (S5)-(S6); the joint Haar bound (S8)-(S9); absolute area decay (S18)-(S19) for every admissible integer-height graph at 0 < beta <= 5/11, with the original Z_m and all decorations, without a density cutoff; exponential growth of the coarse majorant at beta = 1/2 on three heights (S20)-(S22), explicitly not a statement about the sharper majorant or the true weights; group blindness for the binary icosahedral group; the open items; no seed extension, no independent check, no status. "Does not refute the sharper majorant" is fair; P3 adds that the b-retaining intermediate majorant is also not covered by (S20). Fair.

## Verdict table

| Item | Steps | Verdict |
|---|---|---|
| 1 | SOS class (S3), closure, odd pairing, link-connectedness, admissibility d_e < n_3, (S4) with projected b | HOLDS |
| 2 | (S5) by orientation, (S6) intervals and K_e, (S7), pillar 8A + 29L - 8 orientation by orientation, binary (R12) | HOLDS (P1 wording) |
| 3 | (F10) exponents at every link incl. degree four, min(k,4b), E x^4 = 1/8, (S8)-(S9) | HOLDS |
| 4 | Comb trees, (S11) weights, (S12) Hölder, pinned tree bijection, (S10), (S13)-(S14) | HOLDS |
| 5 | (S15)-(S17) rational arithmetic, rho < 1256/1275, (S18)-(S19) | HOLDS (P2 remark) |
| 6 | (S20) Jensen, E k = 3A/2 - 1, entropy, (S21)-(S22), scope of refutation | HOLDS (P3 scope) |
| 7 | (S23)-(S25), (RTAIL-SOS) equivalence, complement scope | HOLDS (P4 dated wording) |
| 8 | Group blindness, icosahedral E x^4, U(1), weak coupling, seed | HOLDS |
| 9 | RESULT line | Fair |

Precisions (none changes a conclusion):
- P1. (S6): nbr(f) means the four edge neighbours.
- P2. (S19): the constant e^(16/tau_S) is about e^1066; explicit but enormous.
- P3. (S20)-(S22) refute only the b-maximised majorant q^A t^k. The b-retaining form q^(A+k) c^(-6b) 2^(min(k,4b)/4) is not covered; a hand estimate with E b = (9/64)A suggests it also grows at beta = 1/2, but the note's rational bound q > 2/3 is too weak to show it.
- P4. Section 7: the check of row 823's proofs (gap-rtail-check-opus.md) now exists and HOLDS; the "not available at the pin" caveat is dated.

No step FAILS. No mathematical correction is needed.

Checked line by line by Claude Opus 5.5. Credit Codex gpt-6-astra max for the note. This is one check, not an audit; it grants no scientific status.

RESULT: Every PROVED step of gap-sos-astra.md HOLDS on a hand re-derivation by Claude Opus 5.5 — the SOS class and its admissibility, the exact neighbourhood (S5)-(S7) with the pillar count 8A + 29L - 8 recovered orientation by orientation, the joint Haar bound (S8)-(S9), the translated comb-tree bound (S10)-(S14), the rational interval 0 < beta <= 5/11 with rho < 1256/1275, the three-height growth (S20)-(S22) of the coarse majorant at beta = 1/2, the union and remainder (S23)-(S25), and the group claims — nothing FAILS, four precisions change no conclusion, and the RESULT line is fair.
