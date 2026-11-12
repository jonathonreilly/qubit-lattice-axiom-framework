# Check of library/gap-rtail-astra.md (FINISH row 826), by Claude Opus 5.5, line by line

Clone `/Users/jonreilly/ym4d-lead/clone` at commit `fa909a016a6e0414e4595f336cd64d6d8042f4b3` (pulled; already up to date).
Lane D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
Target `D/library/gap-rtail-astra.md` (805 lines), read in full. Author: Codex gpt-6-astra max. The note names its own assignment FINISH row 823; this check is row 826.
Context read: `D/library/gap-flat-astra.md` lines 60-459 and 590-649 ((F1)-(F23), (F27)-(F28), RTAIL); `D/library/gap-flat-check-opus.md` in full.

Method. I re-derived every step by hand. After the hand derivation, one small GUIDE run (Python, under 1 MB, script `guide/guide.py` beside this report) re-did the rational arithmetic, the binary icosahedral moments, the neighbourhood counts (R12) and (R19) on small 4D tori, and the sum (R15) on 3x3 and 4x4 bases. It decided nothing. Every GUIDE value agreed with the hand result.

Notation is the note's. Directions 1,2 are horizontal, 3 is the bump direction, 4 the other transverse direction. c = cosh(beta), h = sinh(beta)/2.

## 1. The exploration code (R4) and (R5)-(R9)

**Root.** Lemma M (READ) puts at least one horizontal face over each base face. The first one over a fixed base face is determined by S. Its transverse site has at most N_perp values. HOLDS.

**Decoder determinism.** The queue, the processed-link set and the next link are functions of the data already decoded. The decoder knows the direction of the next link. At a horizontal link it reads the next flag. At a transverse link it reads the next label. Each step is determined. HOLDS.

**Recovery and injectivity.** Every face of S has its four links processed. Every face of S at a processed link enters the queue. Link-connectedness then puts every face of S in the queue. The decoder applied to the encoder's output returns S. So the decoder is a left inverse, and the code is injective. Discarding inconsistent codes is harmless. HOLDS.

**Default rule.** Let e be a horizontal link that meets no nonhorizontal face of S. The faces of S at e are then among its two horizontal faces. The discovering face is one of them. Closure forces even degree, so both are in S. The decoder adds the other horizontal face. HOLDS.

**Horizontal exceptions at most 2V.** An exceptional horizontal link meets a nonhorizontal face of S. A purely transverse face has no horizontal link. A mixed face has exactly two. So the exceptional horizontal links number at most 2V. HOLDS.

**Labelled links at most 4V.** Every labelled link (horizontal exception or transverse link) lies in a nonhorizontal face of S. Each such face has four links. So at most 4V labels. With V <= k <= K this is at most 4K. HOLDS.

**Sixteen choices.** A link has six incident plaquettes, distinct at periods at least three. One is known (the face that caused processing). Even degree forces an odd subset of the other five: 5 + 10 + 1 = 16. HOLDS.

**Processed links.** Every used link has degree at least two, and S has 4|S| face-link incidences. So at most 2|S| <= 2(A+K) used links, and every processed link is used. The flag string has at most 2V <= 2K ones. HOLDS.

**Padding.** The decoder stops when the queue empties and reads no symbol past that point. Padding therefore adds no ambiguity. Precision P1: the padding symbol must be one of the sixteen symbols; a seventeenth symbol would give 17^(4K). The note says "a fixed symbol", which is consistent with this. The count is N_perp 16^(4K) sum_(b<=2K) binom(2(A+K),b). HOLDS.

**(R5).** For b <= 2K and 0 < t <= 1, t^(b-2K) >= 1. So the sum is at most t^(-2K) sum_b binom(n,b) t^b = t^(-2K)(1+t)^n. HOLDS. The entropy order with t = epsilon/(1+epsilon) follows from log(1+t) <= t. HOLDS.

**(R6)-(R8).** By (R3), u(S) <= q^A gamma^k <= q^A gamma^(K_0). With t = 1/256, (1+t)^(2(A+K_0)) <= exp((A+K_0)/128). Also 16^(4K) gamma^K < 16^(5K) = 2^(20K) and t^(-2K) = 2^(16K). With q < e^(-1/4) from (F14) this is (R7). Next, log 2 < 3/4 because e^(3/4) > 1 + 3/4 + 9/32 = 65/32 > 2. Then (A+K_0)/128 <= 129A/16384 and 36 K_0 log 2 < 27A/128 = 3456A/16384. The sum is 3585A/16384. The comparison 3585/16384 < 9/40 is 3585*40 = 143400 < 9*16384 = 147456. Then -A/4 + 9A/40 = -A/40. K_0 = 0 is the flat class, with B <= N_perp q^A. HOLDS. The dressed consequence and the window K(a) < k <= floor(A/128) follow, since A >= a^2 and N_perp <= 4a^2. HOLDS.

**(R9).** With t = epsilon and K <= epsilon A, the logarithm of the bound, less log N_perp, is at most A[log q + epsilon log(16^4 gamma) + 2 epsilon log(1/epsilon) + 2(1+epsilon) log(1+epsilon)] = -A Psi_beta(epsilon). Each K-dependent cost is nonnegative for epsilon <= 1, so the replacement K -> epsilon A is valid. HOLDS.

Verdict: HOLDS (precision P1, wording).

## 2. The terrace class (R10)-(R18)

**(R10).** Mod two, the boundary of a union of cubes is the sum of the cube boundaries. Over f in D the bottom faces cancel P there, the top faces sit at height 1, and the side face over a base edge survives exactly when one neighbour lies in D. So S(D) has one horizontal face per base face at height 1_D(f), plus the vertical faces over boundary edges of D. P is closed and the added chain is a boundary, so S(D) is closed. A boundary pairs to zero with the twist, so the odd pairing of P is kept. Adjacent base faces lift to faces joined directly (equal heights) or through the vertical face (unequal heights). The base torus is edge-connected, so S(D) is link-connected. |S(D)| = A + |dD|, and 0 <= k <= 2A since the base has 2A edges. HOLDS.

**(R11).** The four base edges at a vertex separate cyclically consecutive faces. So the transition number d equals the degree of the vertex in dD; a cyclic binary list has d in {0,2,4}. The vertical link over the vertex lies exactly in the vertical faces over the boundary edges there, so its degree is d. Summing degrees gives 2k = 2v_2 + 4v_4, hence v = k - v_4. Horizontal used links have degree two: at height sigma over edge e, the faces of S are two horizontal faces (both neighbours at sigma), or one horizontal and one vertical face (a transition), or none. A degree-four vertical link occurs exactly at a checkerboard vertex. HOLDS.

**(R12), by orientation.** All used links lie at x_4 = 0. Used horizontal links: one over each base edge, two at a transition, so 2A + k. Used vertical links: v, over the boundary vertices, on [0,1].
- 12: a horizontal plaquette contains only horizontal links. At its own height each base face gives one face (A in all). The plaquette at the other height over g contains a used link exactly when g has a neighbour of the other height, that is, when g touches a boundary edge. Total A + M. Correct.
- 13, 23: these are e x [s,s+1] at x_4 = 0. One used horizontal link at height sigma gives s in {sigma-1, sigma}: two. Both heights give s in {-1,0,1}: three. Total 4A + k. A plaquette through a used vertical link is e x [0,1], which contains a used horizontal link at height 0 or 1. So it is already counted. Correct.
- 14, 24: each used horizontal link lies in two, at x_4 in [-1,0] and [0,1]. Each such plaquette has only one link at x_4 = 0, so no double count. Total 4A + 2k. Correct.
- 34: two per used vertical link, by the same argument. Total 2v. Correct.

The sum is 9A + 3k + M + 2v. Subtract A + k and use v = k - v_4: 8A + 4k + M - 2v_4. Each boundary edge touches two base faces, so M <= 2k. Coincidences only lower the union count. For one bump, k = 4, M = 5, v_4 = 0 gives 8A + 21, as in (F19). HOLDS. GUIDE: on the torus (4,4,5,5) the brute-force count equals 8A + 4k + M - 2v_4 exactly for six D, including the checkerboard (k = 32, v_4 = 16).

**(R13).** The moment recursion (2l+2)M_l = (2l-1)M_(l-1) gives M_2 = (3/6)(1/4) = 1/8. Exponents: two on horizontal faces and on vertical faces with no degree-four link; four on vertical faces touching a degree-four link. At a degree-four link all four incident faces of S touch it, so the sum is 4/4 = 1. At a degree-two link the sum is at most 1/2 + 1/2. Only faces of S carry functions, so these are the conditions of (F10). HOLDS.

An exponent-two face gives at most sinh(beta)(1/4)^(1/2) = h. An exponent-four face gives at most sinh(beta)(1/8)^(1/4) = 2h 2^(-3/4) = 2^(1/4) h. Faces touching a degree-four link number at most 4 v_4. So the Haar integral is at most h^(A+k) (2^(1/4))^(4v_4) = h^(A+k) 2^(v_4). With c >= 1 and (R12), c^(8A+6k-2v_4) h^(A+k) 2^(v_4) = (hc^8)^A (hc^6)^k (2c^(-2))^(v_4) = q^A t^k R^(v_4). HOLDS.

**(R14).** dD is an even subgraph. Its vertex-connected components are vertex-disjoint connected even subgraphs, and the decomposition is unique. A vertex-disjoint family of even subgraphs has even union. k and v_4 add over components, since a degree-four vertex lies in one component. dD = dD' exactly when D + D' has empty boundary, that is, D' = D or D' is the complement (connected base torus). D and its complement differ, since A >= 1. An even subgraph is a boundary exactly when its mod-two homology class vanishes. So the D-sum is twice the sum over compatible families with null-homologous union. The constraint is on the union. HOLDS. Precision P2: in the display the token `{\rm compatible}` has lost its backslash-r and renders as `{` then a new line `m compatible}`. This is a typesetting slip only. The same slip appears in (F4) of gap-flat-astra.md.

**(R15).** Under the uniform product measure on A height bits, prod_x f_x = t^(sum d/2) R^(v_4) = t^k R^(v_4), since sum_x d(x) = 2k. Each bit is one of the four faces at each of its four corners, so it enters four vertex factors. Exponent four on every factor gives reciprocal sum 1 at each bit, so (F10) applies on this product probability space. The four faces at a vertex are distinct, so E f^4 is over four independent fair bits. Cyclic patterns: d = 0 for 2, d = 4 for 2 (0101, 1010), d = 2 for C(4,2)*2 = 12. So E f^4 = (2 + 12t^4 + 2t^8R^4)/16. The base has A vertices. Multiplying by 2^A = 16^(A/4) gives (R15). HOLDS. GUIDE: on 3x3 and 4x4 bases at t = 0.7, R = 1.9 the exact sum is below the bound.

**(R16)-(R17).** q^4 = h^4c^32; q^4 * 12t^4 = 12h^8c^56; q^4 * 2t^8R^4 = 2*16 h^12 c^(32+48-8) = 32h^12c^72. The expression increases in h and c, so beta = 1/2 suffices. With h < 4/15, c^8 <= e < 11/4:
- 2h^4c^32 < 2(11/15)^4, and 2(11/15)^4 < 7/12 is 24*11^4 = 351384 < 7*15^4 = 354375.
- 12h^8c^56 < 12*4^8*11^7/(15^8*4^7) = 48*11^7/15^8, and < 3/8 is 128*11^7 = 2494357888 < 15^8 = 2562890625.
- 32h^12c^72 < 32*4^12*11^9/(15^12*4^9) = 2048*11^9/15^12, and < 1/25 is 51200*11^9 = 120726921779200 < 15^12 = 129746337890625.
- 7/12 + 3/8 + 1/25 = (350 + 225 + 24)/600 = 599/600.
HOLDS. GUIDE: the left side is about 0.661 at beta = 1/2.

**(R18).** Per plane translate and signed direction, the sum is at most q^A (2 + ...)^(A/4) = [q^4(2 + ...)]^(A/4) < (599/600)^(A/4). There are N_perp translates and four signed directions. Overcounting is harmless. The checkerboard on even base periods has k = 2A and d = 4 at every vertex. HOLDS.

Verdict: HOLDS (precision P2, typesetting).

## 3. Pillars (R19)-(R22)

**Pillar surface.** S = P + d(f x [0,L]). Its faces are P minus f, the top face at height L, and 4L side faces. So |S| = A + 4L and k = 4L. Every link has degree two. HOLDS.

**Used links.** Horizontal: the 2A base edges at height 0 (each still borders an unremoved plane face), and the four edges of f at heights 1 through L. The side faces e x [s,s+1] contain the horizontal links over e at heights s and s+1, so the intermediate heights are used. Total 2A + 4L. Vertical: four corners times L segments, 4L.

**(R19), by orientation.**
- 12: height 0 gives A. At each height 1..L, the plaquettes containing an edge of f are f and its four edge neighbours: 5L. Total A + 5L. Correct.
- 13, 23: an edge of f has used horizontal links at heights 0..L and used vertical links over both endpoints on [0,L]. So s runs over -1..L: L + 2 plaquettes, L more than the base count. Each corner has two outward base edges (8 in all). Each has a used horizontal link only at height 0 and a used vertical link over the corner on [0,L]. So s runs over -1..L-1: L + 1 plaquettes, L - 1 more. All other edges give two. Total 4A + 4L + 8(L-1) = 4A + 12L - 8. Correct. Precision P3: the note's split "Horizontal used edges account for 4A+4L" means 4A from the base plus L extra beside each edge of f. The words are terse; the total is right.
- 14, 24: two per used horizontal link, 4A + 8L. Correct.
- 34: two per used vertical link, 8L. Correct.

Sum 9A + 33L - 8; subtract A + 4L: 8A + 29L - 8. L = 1 gives 8A + 21, as in (F19). At L = 2 the increment is 50 > 6k = 48. With M = 5 the sharper form 8A + 4k + M gives only 37. So the binary-height count does not extend. The count needs L <= n_3 - 2 for the heights -1..L to be distinct, which the class imposes. HOLDS. GUIDE: on the torus (5,5,7,5) the brute-force count is 221, 250, 279, 308 for L = 1..4, equal to 8A + 29L - 8.

**(R20).** Vertex-disjoint bases make all added links distinct, also across different signed directions, since their projections lie over disjoint base vertices. Every plane link stays used, because two adjacent base faces cannot both be pillar bases. So N(P) lies in each single-pillar neighbourhood, and N(S) is the union of these. Union counting gives |N(S)| <= 9A + sum(33L - 8), and |N(S)\S| <= 8A + sum(29L - 8). Every link has degree two, so exponent two on all faces gives h^(A + 4 sum L). Then u(S) <= q^A prod w_L with w_L = h^(4L) c^(29L-8) = w_1 v^(L-1). Check: h^4c^21 h^(4L-4)c^(29L-29) = h^(4L)c^(29L-8). HOLDS.

**(R21).** Dropping separation and the height cap only adds nonnegative terms. Each base face contributes 1 + 4 sum_(L>=1) w_1 v^(L-1) = 1 + 4w_1/(1-v). Times q^A and N_perp translates. HOLDS.

**(R22).** e^(5/8) <= 569/304 < 15/8 is 569*8 = 4552 < 15*304 = 4560. c^21 <= e^(21/8) = e^2 e^(5/8) and c^29 <= e^3 e^(5/8). Then w_1 < 256*121*15/(50625*16*8) = 3630/50625 = 242/3375, and v < 256*1331*15/(50625*64*8) = 1331/6750 < 1. Hence w_1/(1-v) < (242/3375)(6750/5419) = 484/5419. Then (11/15)(1 + 1936/5419) = (11/15)(7355/5419) = 80905/81285 < 1 (= 16181/16257). HOLDS. GUIDE: the true value at beta = 1/2 is about 0.865. The excess claim: A/4 bases at common height L give excess 4L*A/4 = LA, and L can grow up to n_j - 2 >= a - 2. HOLDS.

Verdict: HOLDS (precision P3, wording).

## 4. (R23)-(R24): the Kotecky-Preiss failure

The unit squares sharing a vertex with a fixed unit square have lower-left corners at offsets in {-1,0,1}^2: nine, distinct at periods at least three. Vertex-disjointness is the compatibility, so the fixed square is incompatible with itself, as in the standard criterion. Summing (R23) over the A elementary roots and dropping other nonnegative terms gives 9t^4 sum e^(a') <= sum a. Dividing by A and using Jensen (convexity of exp) gives 9t^4 e^b <= b with b the mean. Since b e^(-b) <= 1/e, this forces 9e t^4 <= 1. HOLDS.

At beta = 1/2: sinh(1/2) > 1/2 gives h > 1/4; cosh(1/2) > 1 + 1/8 gives c > 9/8; e > 1 + 1 + 1/2 + 1/6 = 8/3. The binomial terms: 1 + 3 + 276/64 + 2024/512 = (256 + 276 + 253)/64 = 785/64 > 12, with C(24,2) = 276 and C(24,3) = 2024. So t^4 = h^4c^24 > 12/256 and 9e t^4 > 9(8/3)(12/256) = 288/256 > 1. HOLDS. GUIDE: 9e t^4 is about 2.01. (The contradiction survives even without the self term: 8e t^4 > 256/256 strictly.)

The scope paragraph is fair: z is a majorant, and (R15) sums the same majorant directly. The (R9) failure at epsilon = 1/8: q(1/2) > (1/4)(9/8)^8 > 1/4 gives -log q < log 4; epsilon log(16^4 gamma) > (1/8)*16 log 2 = log 4 since gamma > 1; H(epsilon) > 0. So Psi < 0. HOLDS. The (R19) limit is as in item 3. The three failures are failures of bounds only. Fair.

Verdict: HOLDS.

## 5. (R25)-(R28): joint class, containment, telescoping

**(R25)-(R26).** (599/600)^(A/4) = exp(-(A/4) log(600/599)) and (80905/81285)^A = exp(-A log(81285/80905)). So B_(G_*) <= N_perp e^(-A/40) + 4N_perp(599/600)^(A/4) + N_perp(80905/81285)^A <= 6N_perp e^(-tau A). With N_perp <= 4a^2 and A >= a^2 this is at most 24a^2 e^(-tau a^2). From e^x >= x, a^2 e^(-tau a^2) <= 1/tau, so B <= 24/tau and e^(2B) <= e^(48/tau). Then (F9) gives C_0 = 24 exp(48/tau). HOLDS.

**Containment of G.** A_(K(a)) lies in A_* when K(a) <= floor(A/128), which needs 100 log(2a) >= 128. For a >= 3, log(2a) >= log 6. e^(4/3) = e * e^(1/3) < (11/4)(3/2) = 33/8 < 6, so log 6 > 4/3 > 1.28. Precision P4: the step e^(1/3) < 3/2 is not stated; it follows from (3/2)^3 = 27/8 > 11/4 > e. The bump family B(P) is the L = 1 case of P_*, with the empty choice giving P; L = 1 <= n_j - 2 since n_j >= 3. So G lies in G_*. HOLDS.

**(R27).** By (F2) with F = O, p_m(v) = (1/2Z_m) int C[Xi(w_m) - Xi(w_m^O)]. Add and subtract Xi(w_m^(G_*)). This is p_m = T_m(G_*) + R_m^*. In the (F4) form, R_m^* sums marked families with at least one surface outside G_*, with unflipped exterior weights. HOLDS.

**(R28).** R_m^* = p_m - T_m(G_*) >= -sum_(G_*) |D_m| uses p_m(v) >= 0, the READ fact 0 < Z_(m+v) <= Z_m of (J1). R_m = p_m - T_m(G), so R_m = R_m^* + T_m(G_*) - T_m(G). Order G first inside G_*. The first-block D's then equal those of the G-first ordering, and by (F2) their sum is T_m(G). So T_m(G_*) - T_m(G) is the sum of D_m(S) over G_* minus G, bounded by (R26). HOLDS.

**(RTAIL*) equivalence.** If RTAIL* holds, R_m <= C a^p eta_*^(a/2) + C_0 a^2 e^(-tau a^2). The maximum of -tau a^2 + kappa a is kappa^2/(4 tau), at a = kappa/(2 tau). So e^(-tau a^2) <= e^(kappa^2/(4tau)) eta_*^(a/2), with kappa = (1/2) log(1/eta_*). The converse uses the same bound. So RTAIL*, RTAIL and (E17) agree up to constants and powers. HOLDS.

**Stronger target.** With F = O ordered G_* first, (F5) and (F8) give |D_m(S)| <= b(S) prod_(T earlier)(1 + 2b(T)) <= b(S) e^(2(B_(G_*) + B_out)). Summing over S outside G_* gives the stated bound, and it bounds |R_m^*|. HOLDS. The claim that no B_out estimate is proved is accurate.

Verdict: HOLDS (precision P4, a missing one-line step).

## 6. Section 7: groups

**Binary icosahedral fourth moment.** The 120 elements have x = 1 (1), -1 (1), 0 (30), 1/2 (20), -1/2 (20), and plus or minus c_+, c_- (12 each of the four values). c_+^2 = (3 + sqrt5)/8 and c_-^2 = (3 - sqrt5)/8. Their sum is 3/4 and their product (9 - 5)/64 = 1/16. So c_+^4 + c_-^4 = 9/16 - 2/16 = 7/16. Then E x^4 = [2 + 40/16 + 24(7/16)]/120 = (2 + 5/2 + 21/2)/120 = 15/120 = 1/8. HOLDS. GUIDE: E x^2, E x^4, E x^6 = 0.25, 0.125, 0.078125.

**Group blindness.** The new estimates use the central sign and zero Haar mean (through (F6)-(F8)), |x| <= 1, and E x^2 = 1/4, E x^4 = 1/8 (R13), E x^6 = 5/64 (through (R3) = (F13)). For independent Haar links on any compact group, U_p is Haar distributed, so each face moment is the group moment of x. The gap-flat check section 7 confirmed -I in the group, mean zero, and the moments through degree six. (R4), (R10)-(R12), (R14), (R15), (R19) are combinatorial. So every new class bound transfers unchanged. HOLDS.

**U(1).** E cos^2 = 1/2. cos^4 = (1 + 2cos 2theta + cos^2 2theta)/4 averages to (1 + 1/2)/4 = 3/8. The good-face factor becomes sinh(beta)/sqrt2, larger than h. The note claims only that (R3), (R16), (R22) do not transfer unchanged. That is fair: for instance the first term of (R16) alone exceeds 1 at beta = 1/2 with the U(1) factor. No U(1) conclusion is claimed. HOLDS.

**Weak coupling.** q >= sinh(beta)/2 > beta/2 >= 1 for beta >= 2. HOLDS.

**Seed and continuation.** These paragraphs are READ or conditional. They claim no extension of the seed beyond 2/9. I did not re-check Theorem DOB or the consumer. Fair.

Verdict: HOLDS.

## 7. The RESULT line

Each claim matches a step that HOLDS: (R6) for excess at most A/128; (R18) for one-step terraces in one signed direction, with overlaps and four-way contacts; (R22) for separated pillars, with excess LA beyond order A; all at 0 < beta <= 1/2 with the original Z_m through (R2). "Removes the transverse-position log(a) loss" is fair: (R4) has the prefactor N_perp only, against (4N_p)^K in (F16). Precision P5: "a finite defect-contour sum controls the terrace class" is fair because (R14) shows the D-sum equals that contour polynomial; the bound itself is the binary-height Hoelder (R15) on the D-sum. Group blindness, the open status of RTAIL, the absence of a new seed above 2/9, and "not independently checked" are all accurate. Fair.

## Verdict table

| Item | Steps | Verdict |
|---|---|---|
| 1 | (R4) decoder, default rule, 2V and 4V counts, 16 choices, padding, 2|S|; (R5)-(R9), 143400 < 147456 | HOLDS (P1 wording) |
| 2 | (R10)-(R11); (R12) by orientation; (R13) moments, Hoelder exponents, 2^(1/4)h, 4v_4, R = 2c^(-2); (R14) with homology; (R15), 16 patterns; (R16)-(R18) integer comparisons | HOLDS (P2 typesetting) |
| 3 | (R19) 8A + 29L - 8 by orientation; (R20)-(R22) | HOLDS (P3 wording) |
| 4 | (R23)-(R24): nine squares, Jensen, b e^(-b) <= 1/e, 9e t^4 > 1; (R9) failure at 1/8 | HOLDS |
| 5 | (R25)-(R28), C_0, containment of G, telescoping, RTAIL* equivalence | HOLDS (P4 missing step) |
| 6 | Section 7: icosahedral E x^4 = 1/8, trace pair, U(1) 1/2 and 3/8, group blindness | HOLDS |
| 7 | RESULT line | Fair (P5 wording) |

Precisions (none changes a conclusion):
- P1. (R4): the padding symbol should be one of the sixteen symbols, or the count becomes 17^(4K).
- P2. (R14) display: `{\rm compatible}` lost its backslash-r and renders broken. The same slip is in (F4) of gap-flat-astra.md.
- P3. (R19): the split "4A+4L" means two intervals per base edge plus L extra beside each edge of f.
- P4. Section 6 containment: e^(1/3) < 3/2 is used unstated; (3/2)^3 = 27/8 > e.
- P5. RESULT line: the terrace bound is the binary-height Hoelder sum (R15) of the D-sum, which (R14) identifies with the contour polynomial.

No step FAILS. No mathematical correction is needed.

Checked line by line by Claude Opus 5.5. Credit Codex gpt-6-astra max for the note. This is one check, not an audit; it grants no scientific status.

RESULT: Every PROVED step of gap-rtail-astra.md HOLDS on a hand re-derivation by Claude Opus 5.5 — the injective exceptional-link code (R4) with (R5)-(R9), the terrace class (R10)-(R18) with its orientation count, joint Haar exponents, contour identity and the 599/600 constant, the pillar count 8A + 29L - 8 and (R20)-(R22), the Kotecky-Preiss failure (R23)-(R24), the joint class and telescoping (R25)-(R28), and the group claims of section 7 — nothing FAILS, five wording or typesetting precisions change no conclusion, and the RESULT line is fair.
