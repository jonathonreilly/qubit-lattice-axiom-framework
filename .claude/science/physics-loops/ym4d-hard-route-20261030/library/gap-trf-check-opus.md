# Check of library/gap-trf-astra.md (FINISH row 795), by Claude Opus 5.5, line by line

- Checker: Claude Opus 5.5, one session, no subagents, 2026-11-12. Cross-provider check of a Codex gpt-6-astra max note.
- Clone read: `/Users/jonreilly/ym4d-lead/clone`, HEAD `5bc6c1fed`.
- File checked (read in full, 633 lines): `.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-trf-astra.md`. The note calls itself FINISH row 793 (line 47). The header uses row 795 as requested.
- Context read: `gap-ext-astra.md` Sections 1, 4 and 5 (lines 78-128, 348-757: (LC), (E18)-(E25), (TR-F)); `gap-ext-check-opus.md` in full; `gap-cf-astra.md` Section 2 (lines 267-350); the Section 2 rows of `gap-cf-check-opus.md`.
- Not checked: the repo search, the PR 10114/10133 citations, the SA outline reads and the source record (lines 1-73, 588-631). They are outside the brief and carry no proof weight.
- Method: by hand. No numerical run, not even as GUIDE.

## 1. (T1) and (T2); the test pair (0, v_13)

**(T1).** The family, the weights and C(T,pi) are exactly (E22). The proof of (E23) shows sum_j pi_j E_mu[S_(m+v)(T_j U) - S_m(U)] = E_nu X + sum_j pi_j D(nu_j||mu) = E_nu X + D(nu||mu) + I_pi. Subtract I_pi: C = E_nu X + D(nu||mu). Then (E21) gives = F + D(nu||mu'). HOLDS. Both equalities were checked in row 791 (items 5a-5b). C >= E_nu X follows from D >= 0. HOLDS. The shifted convention S_k = beta sum(1 - eta s_p) changes Z_k by e^(-beta N_p) only; F is unchanged. HOLDS.

**(T2).** epsilon_a = min{1/96, K(a) eta_*^(a/2)/4} is the right side of (TR-F) (gap-ext line 661-664). HOLDS. The note states 0 < eta_* < 1/16 (line 133). That is the precision row 791 asked for (item 5g). Good.

**The pair.** In frame 1 the crossed list is m spatial with m_2 = 0 and v = v_1i, i = 3, 4. Here m_2 is the v_34 component (row 791 item 2e: x_3 = m_3 = k_24, x_4 = m_4 = k_23, so m_2 = k_34). m = 0 has m_2 = 0. v_13 has i = 3. The cube (a,a,a,a) is the shape c = d = a. So (0, v_13) on the cube is a required pair. (TR-F) must hold on every required pair. Failure on one pair excludes the family as a supplier. HOLDS.

**Representative.** Sigma = {p_13(x): x_1 = x_3 = 0} is closed. A 3-cube in directions 1, 3, mu (mu = 2 or 4) has two 13-faces at x_mu and x_mu + 1. Both lie in Sigma or neither does. Other 3-cubes have no 13-face. So the coboundary vanishes mod 2. It has a^2 plaquettes. It meets the 13-torus with fixed (y_2, y_4) once, so its class is v_13. HOLDS. For m = 0, S_v - S_0 = beta sum_Sigma [(1 + s_p) - (1 - s_p)] = 2 beta sum_Sigma s_p. HOLDS.

Verdict for item 1: HOLDS.

## 2. Section 2: (T3)-(T5)

**Edges of a selected plaquette.** The 13-plaquette at base x = (2j, x_2, 2k, x_4) has direction-1 edges based at x and x + e_3, and direction-3 edges based at x and x + e_1. So its direction-1 edges have base x_1 = 2j and x_3 in {2k, 2k+1}. Its direction-3 edges have base x_3 = 2k and x_1 in {2j, 2j+1}. The other two base coordinates are (x_2, x_4).

**Disjointness, including the periodic boundary.** All coordinates used lie in {0, ..., 2b-1}, and 2b - 1 <= a - 1. So no coordinate wraps. Two selected plaquettes share a direction-1 edge only if 2j = 2j' (both in {0, ..., a-2}, so equal mod a means equal), (x_2, x_4) agree, and {2k, 2k+1} meets {2k', 2k'+1}. The last forces k = k'. The direction-3 case is symmetric. The wrap edges (base coordinate a-1 in direction 1 or 3) never occur: a direction-1 edge needs base x_1 even and <= 2b-2 <= a-2. For even a, a-1 is odd. For odd a, a-1 = 2b > 2b-2. So 2b-2 and 0 are never joined by a selected edge. For even a the vertices at coordinate 2b-1 = a-1 touch the vertices at 0, but no edge is shared. HOLDS. M = b^2 a^2: b values each of j, k and a values each of x_2, x_4. HOLDS.

**Unselected plaquettes have an outside edge.** A plaquette of orientation other than 13 has an edge in direction 2 or 4. The union has only directions 1 and 3. For a 13-plaquette at base y, its direction-1 edge at y lies in the union only if y_1 is even and <= 2b-2. Its direction-3 edge at y lies in the union only if y_3 is even and <= 2b-2. Then y is a selected base. HOLDS.

**Conditional mean zero.** Each edge occurs once in a plaquette boundary (a >= 2). So U_p = A U_e^(+-1) B with A, B free of U_e. The Haar integral of U_e and of U_e^(-1) is 0. So E[s_p | all links except e] = 0, and by the tower property E[s_p | selected links] = 0. HOLDS.

**Conditional Jensen, (T4).** Write Z^0 = int exp(beta sum_sel s_p) E[exp(beta sum_unsel s_p) | sel] dU. Jensen gives the inner factor >= exp(beta E[sum_unsel s_p | sel]) = 1. The selected plaquettes have disjoint edge sets. Their holonomies are independent and each is Haar distributed. So the remaining integral is c_0^M. HOLDS. This is the unshifted convention, as written in (T4).

**Convexity.** f = log Z^0 is smooth on the finite compact integral, f(0) = 0 (normalized Haar), f'' = Var(sum s_p) >= 0. The tangent at beta lies below f at 0: 0 >= f(beta) - beta f'(beta). So f'(beta) >= f(beta)/beta. HOLDS.

**Equal means.** Translations and the 24 axis permutations preserve Haar measure and the untwisted cube action. Orientation reversal does not matter: tr U^(-1) = tr U in SU(2). So every plaquette has the same mean. There are 6 a^4 plaquettes and f' = sum_p E s_p. HOLDS.

**(T5) constants.** E s_p >= M log c_0/(6 a^4 beta) = (b^2/(6a^2)) log c_0/beta >= (b^2/(6a^2)) kappa_I. For a >= 3, b >= (a-1)/2 >= a/3. So b^2/(6a^2) >= 1/54. HOLDS. kappa_I > 0 by the strict-Jensen argument checked in row 791 (item 5f). HOLDS. The gain over (E25) is real: the bound is per plaquette and independent of the volume.

Verdict for item 2: HOLDS.

## 3. Section 3: (T6)-(T9) and (SD)

**Sheet edges.** Each p_13(0, x_2, 0, x_4) has the four edges listed in item 2 with j = k = 0. These plaquettes are among the selected ones of Section 2, so their edge sets are disjoint. Each has four distinct edges. So |E_Sigma| = 4a^2 and each sheet edge lies in exactly one sheet plaquette. HOLDS.

**(T6).** The definition is well posed for measurable g_j. One gauge per output on the whole torus is what (T8) needs. HOLDS.

**(T8).** U~_j is a gauge transform of T_j U. So the holonomy of p is conjugated by g_x and s_p(T_j U) = s_p(U~_j), pointwise. Field dependence of g does not matter. Telescoping: A_1...A_4 - B_1...B_4 = sum_i A_1...A_(i-1)(A_i - B_i)B_(i+1)...B_4, with unitary factors. So ||U~_p - U_p|| <= sum ||A_i - B_i||. ||V^(-1) - U^(-1)|| = ||V^(-1)(U - V)U^(-1)|| = ||U - V||. |tr M|/2 <= ||M||_op for 2 x 2 matrices. HOLDS.

**Cauchy-Schwarz.** Summing (T8) over Sigma gives sum_Sigma |Delta s_p| <= sum_(e in E_Sigma) d_e, since each sheet edge appears once. On the measure pi_j mu_0(dU) x counting(E_Sigma), of total mass 4a^2, Cauchy-Schwarz gives sum_j pi_j E sum_e d_e <= sqrt(4a^2) sqrt(L_Sigma) = 2a sqrt(L_Sigma). HOLDS.

**(T7).** E_nu X = 2 beta sum_j pi_j E_(mu_0) sum_Sigma s_p(T_j U) >= 2 beta [sum_Sigma E_(mu_0) s_p - 2a sqrt(L)] >= 2 beta [r_I a^2 - 2a sqrt(L)], by (T5) on a^2 plaquettes. Then (T1) with D(nu||mu_0) >= 0 gives (T7). HOLDS. The remark on lines 284-287 is (E23)'s mixture identity: sum pi_j D(nu_j||mu_0) - I_pi = D(nu||mu_0). HOLDS. The theorem uses nothing about the maps off E_Sigma, since X depends only on sheet links. HOLDS.

**(SD) and the failure claim.** L <= r_I^2 a^2/16 gives 2a sqrt(L) <= r_I a^2/2. So C >= beta r_I a^2 >= beta_- r_I a^2. Since epsilon_a <= 1/96, the family fails (T2) once a^2 > 1/(96 beta_- r_I). This uses only the constant ceiling, not eta_* < 1. HOLDS. L = o(a^2), uniform on I, enters (SD) for large a. HOLDS.

**(T9).** C <= epsilon_a and (T7) give 2a sqrt(L) >= r_I a^2 - epsilon_a/(2 beta). Square when the right side is positive. HOLDS.

**Precision (scope of the representative).** Theorem 3, (SD) and (T9) are stated for the standard Sigma, used both in the cost and in E_Sigma. The cost with another representative Sigma' equals the Sigma cost of T_b o T_j for a link-sign map T_b. T_b moves its flipped links by 2. So small displacement relative to Sigma does not transfer to Sigma'. The note flags this (lines 530-531). By my hand sketch the analogue holds with Sigma' in both places: |Sigma'| >= a^2 (it meets each of the a^2 disjoint tori T_13(y_2,y_4) an odd number of times), and each edge lies in at most 6 plaquettes of Sigma'. This sketch is not in the note and is not load-bearing.

Verdict for item 3: HOLDS, with the representative precision.

## 4. Section 4: (T10)-(T12)

**Class.** Parallel insertion of conjugated commutators: [h A h^(-1), h B h^(-1)] is four conjugated generators or inverses. A final gauge transformation is undone by choosing that gauge as the alignment. Compositions: moving each interleaved gauge factor through a later multiplication turns it into a conjugation of the generator. So the composite, after one alignment, has form (T10) with the summed count. HOLDS.

**Norm identity.** For V in SU(2), ||V - I||^2 = 2(1 - tr V/2) (checked in row 791, item 3c). (LC) gives 1 - tr A_N/2 <= pi/(2N). So ||A_N - I||^2 <= pi/N, and the same for B_N. ||h G h^(-1) - I|| = ||G - I|| and ||G^(-1) - I|| = ||G^(-1)(I - G)|| = ||G - I||. HOLDS.

**Telescoping both sides.** ||L U R - U|| <= ||L U R - L U|| + ||L U - U|| = ||R - I|| + ||L - I||. For a product, ||G_1...G_k - I|| <= sum ||G_i - I||. So d_(j,e) <= q sqrt(pi/N). HOLDS.

**(T11).** L_Sigma <= 4a^2 q^2 pi/N. So 2a sqrt(L) <= 4a^2 q sqrt(pi/N). (T7) gives C >= 2 beta a^2 {r_I - 4q sqrt(pi/N)}. HOLDS. If q sqrt(pi/N) <= r_I/8 the brace is >= r_I/2 and C >= beta_- r_I a^2. HOLDS. This is the same as (SD): 4 q^2 pi/N <= r_I^2/16.

**(T12).** d_(j,e) <= q_(j,e) sqrt(pi/N) pointwise. Square and average. HOLDS. Mean square count o(N) per sheet edge, uniform on I, gives (SD) for large a. HOLDS.

**Remark on paths (lines 377-380).** Correct. The class bounds final displacement only.

Verdict for item 4: HOLDS. (The GUIDE label on lines 525-527 is more cautious than needed: that sentence is (T11).)

## 5. Section 5: (T13)-(T20)

**(T13) inverse.** V_r = P_r^(-1) C P_r U_r gives U_r = P_r^(-1) C^(-1) P_r V_r. P_r uses U_0, ..., U_(r-1) only. So recovering in increasing r is well defined. Both maps are continuous. HOLDS.

**Haar preservation.** Two valid arguments. (i) Increasing r: (V_0, ..., V_(r-1)) is a function of (U_0, ..., U_(r-1)). Given these, V_r is Haar by left invariance. So V_r is Haar and independent of (V_0, ..., V_(r-1)). Induction gives product Haar. (ii) Decreasing r: each update U_r -> P_r^(-1) C P_r U_r is a shear whose control (U_0, ..., U_(r-1)) has not yet changed. Fubini and left invariance make it Haar preserving. The composite is T_C. HOLDS. The circles have disjoint link sets and other links are fixed, so the full map is a product map. HOLDS.

**Order of updates.** The order does not matter. In place, in increasing r, the current prefix is Q_r = V_0...V_(r-1) = C^r P_r by (T15). Then Q_r^(-1) C Q_r = P_r^(-1) C^(-r) C C^r P_r = P_r^(-1) C P_r. So in-place increasing updates give the same map. This is my observation; the note uses the original prefixes, which is also correct.

**(T14).** P^(-1)[A, B]P = [P^(-1) A P, P^(-1) B P], with [A_a, B_a] = C_a by (LC). HOLDS. Each of the four left multiplications is by a function of the unchanged prefix. Each is a Haar-preserving shear. So T_C is a composition of admissible maps, and lies in class (T10) with q = 4, N = a and the identity alignment. HOLDS.

**(T15).** Base r = 0: I = C^0 P_0. Step: C^r P_r V_r = C^r P_r P_r^(-1) C P_r U_r = C^(r+1) P_(r+1). No link is commuted through C. At r = a: C^a P_a = -P_a, since C_a^a = -I. HOLDS. Polyakov traces from other base points are conjugate. All change sign. HOLDS.

**(T16).** ||P^(-1) C P U - U|| = ||C - I|| = |e^(i pi/a) - 1| = 2 sin(pi/(2a)) <= pi/a. HOLDS.

**(T17).** Only direction-1 links change. Plaquettes in planes 12, 13, 14 contain two direction-1 links. Planes 23, 24, 34 contain none. So 3a^4 plaquettes change, each with two changed links. By (T8) with identity alignment, |Delta s_p| <= 2 pi/a. Sum: beta x 3a^4 x 2pi/a = 6 pi beta a^3. HOLDS.

**(T18).** S_v(V) = beta sum_(p not in Sigma)(1 - s_p(V)) + beta sum_Sigma (1 + s_p(V)). Subtract S_0(U) = beta sum_p (1 - s_p(U)). This gives (T18). HOLDS.

**(T19).** T_C, T_C^(-1) and the identity are Haar-preserving bijections. So rho_j(V) = e^(-S_0(T_j^(-1) V))/Z_0, with T_j^(-1) = T_C for j = T_C^(-1). Z_0 cancels in rho_j/rho. HOLDS.

**(T20).** For each map, each sheet plaquette has two changed links (its two direction-1 edges), each moved by at most pi/a. So sum_Sigma s_p(T_j U) >= sum_Sigma s_p(U) - 2 pi a. The inverse: for input W, (T_C^(-1) W)_e - W_e = U'_e - (T_C U')_e with U' = T_C^(-1) W. Its norm is <= pi/a by (T16) at U'. Directly, it is ||C^(-1) - I|| = ||C - I||. The identity gives zero. Average, use (T5): E_nu X >= 2 beta (r_I a^2 - 2 pi a). (T1) gives (T20). HOLDS. a >= 4 pi/r_I gives r_I a^2 - 2 pi a >= r_I a^2/2, so C >= beta_- r_I a^2. HOLDS. Any weights: yes, the bound is weight independent. HOLDS.

**Precision.** (T18) and (T19) are not used in the proof of (T20). The proof needs only (T1), (T5), (T8) and (T16). The phrase "Applying the exact identity (T1) to (T18)-(T19)" (lines 482-483) overstates their role. (T20) is also a case of Theorem 3: L_Sigma <= 2a^2 (pi/a)^2 = 2 pi^2, which is (SD) for large a.

**Binding-test paragraph.** Consistent with (LC)'s checked binding tests (row 791 item 4b). In U(1) the commutator realization is the identity. In a finite subgroup, generators with 1 - tr/2 <= pi/(2a) are I for large a. The remark that (T13) with an Abelian C flips loops in U(1) too is correct. HOLDS.

**Scope sentence.** "It does not identify the output law with the law twisted by v_13" is correct and worth keeping: T_C flips all direction-1 loops together. In the ordered picture (a heuristic, not used anywhere) the v_13 twist instead favours opposite signs for direction-1 loops on the two sides of x_3 = 0, since the annulus between them contains one sheet plaquette.

Verdict for item 5: HOLDS, with the precision on (T18)-(T19).

## 6. Sections 6-7: scope

**Checkpoint (lines 75-82) and Section 6 first paragraph.** Theorem 3 covers any finite family of Haar-preserving bijections with field-independent weights, with any field dependence and correlation inside each map. (SD), (T10) with q/sqrt(N) -> 0, and T_C all fail for large a. This matches what is proved. "Integrated cost, not pointwise" is correct: (T7) bounds the mean.

**Precision.** The sentence "Arbitrarily correlated, field-dependent Haar transports satisfying (SD) cannot meet (TR-F)" (lines 516-517) should carry its quantifiers: finite mixtures with field-independent weights, the pair (0, v_13) on the cube, and the cost evaluated on the standard representative Sigma that also defines (SD). N1 (lines 556-559) states the first two. The GUIDE sentence at lines 530-531 states the third. No claim in Sections 6-7 goes beyond (SD), (T10) and T_C under these quantifiers.

**GUIDE paragraph.** Its first sentence is (T11), proved. The rest is labelled GUIDE and claims nothing.

**OPEN (T21).** It is (TR-F) restated. "Theorem 3 supplies a necessary displacement bound for one of its pairs" is correct, and nothing more is claimed. (26) and (FQ) stay open. Correct.

**N-list.** N3: the premises listed are the ones used. No mixing, saddle or phase input appears in (T3)-(T20). Correct. N7 names the right escape: coherent accumulation to order-one endpoint changes. N8 preserves the earlier escapes. The closing status block (lines 617-624) is accurate at the time of writing.

**RESULT line (line 633).** "Whole cost at least beta_- r_I a^2 ... for large a" holds for (SD) at every a, for (T10) once q sqrt(pi/N) <= r_I/8, and for T_C once a >= 4 pi/r_I. MATCHES, under the quantifiers above.

Verdict for item 6: MATCHES, with the quantifier precision.

## 7. The lead's reading of (T9)

**The reading is right.** (T9) constrains designs, not the route.

*Argument.* Read C through (T1) as E_nu X + D(nu||mu_0); this is defined for every law nu << mu_0, from maps or not. Let nu be any law with C <= epsilon_a. (T1) gives E_nu X <= C - D(nu||mu_0) <= epsilon_a. Take any coupling gamma of mu_0 and nu, from maps or not, and any measurable periodic alignment. By (T8), sum_Sigma s_p(U) - sum_Sigma s_p(V) <= sum_(e in E_Sigma) d_e(U, V). Take expectations and use (T5): E_gamma sum_e d_e >= r_I a^2 - epsilon_a/(2 beta). Cauchy-Schwarz gives (T9) for gamma. Now suppose the route can succeed on this pair, that is F <= epsilon_a. The target nu = mu_(v_13) has C = F + 0 <= epsilon_a by (T1). So every coupling of mu_0 with the twisted law itself obeys (T9). Equivalently, (E21) at nu = mu' gives E_(mu') X <= F: the sheet mean drops from at least r_I a^2 to at most F/(2 beta). Any correct transport must realize this drop, so it must move sheet links by order one on average (root-mean-square at least about r_I/4 per sheet edge).

If instead F > epsilon_a, no transport meets (T2), for a reason unrelated to (T9). In neither case does (T9) decide (TR-F). It is compatible with small cost: d_e <= 2, so L_Sigma <= 16 a^2, and moves of order one per sheet edge are allowed. So (T9) excludes small-displacement designs, such as bounded uses of (LC) per link and T_C. It does not exclude the route. The note says the same (lines 313-316 and 543-546).

## Verdict table

| # | Statement (lines) | Verdict | Finding |
|---|---|---|---|
| 1a | (T1) from (E21)-(E23) (86-118) | HOLDS | |
| 1b | (T2); (0, v_13) on the cube as a test (120-148) | HOLDS | m_2 is the v_34 component; Sigma closed of class v_13 |
| 2a | Disjoint edges, periodic boundary, odd a (168-178) | HOLDS | No coordinate wraps; wrap edges are never selected |
| 2b | Every unselected plaquette has an outside edge (178-181) | HOLDS | Directions 2, 4; base parity for 13-plaquettes |
| 2c | Conditional Jensen; Z^0 >= c_0^M (183-195) | HOLDS | |
| 2d | Convexity; equal means; b >= a/3; 54 (196-209) | HOLDS | |
| 3a | Sheet edges: 4a^2, each in one sheet plaquette (214-218) | HOLDS | Sheet plaquettes are among the selected ones |
| 3b | (T6), (T8) (220-266) | HOLDS | |
| 3c | Cauchy-Schwarz 2a sqrt(L); (T7) (267-287) | HOLDS | |
| 3d | (SD) and failure for large a (289-301) | HOLDS AFTER CORRECTION (precision) | Relative to the standard Sigma used in the cost |
| 3e | (T9) (303-316) | HOLDS | |
| 4a | (T10) class (320-342) | HOLDS | |
| 4b | (T11): norm identity, telescoping both sides (344-362) | HOLDS | |
| 4c | (T12) averaged version (364-380) | HOLDS | |
| 5a | (T13) bijection and inverse (388-408) | HOLDS | |
| 5b | Haar preservation; order of updates (409-414) | HOLDS | Either order; in-place increasing order gives the same map, by (T15) |
| 5c | (T14) admissible four-factor realization (416-425) | HOLDS | T_C is in (T10) with q = 4, N = a |
| 5d | (T15), (T16) (427-444) | HOLDS | |
| 5e | (T17): 3a^4 plaquettes, two changed links each (446-451) | HOLDS | |
| 5f | (T18), (T19) (453-481) | HOLDS | |
| 5g | (T20) for mixtures of T_C, T_C^(-1), identity (482-500) | HOLDS AFTER CORRECTION (precision) | (T18)-(T19) are not used; inverse bound correct at the preimage |
| 5h | Binding-test scope (502-511) | HOLDS | |
| 6a | Section 6 scope claims (515-549) | MATCHES AFTER CORRECTION (precision) | Add the quantifiers: finite field-independent mixtures, (0, v_13), the cube, standard Sigma |
| 6b | Section 7 N-list and status block (553-624) | MATCHES | |
| 6c | RESULT line (633) | MATCHES | |
| 7 | Lead's reading of (T9) | RIGHT | (T9) holds for every coupling with the twisted law whenever F <= epsilon_a |
| - | Repo search, PR citations, SA outline reads, source record (1-73, 588-631) | NOT CHECKED | Outside the brief; no proof weight |

Checked line by line by Claude Opus 5.5. Nothing FAILS. Three precisions: (SD) and Theorem 3 are relative to the standard representative used in the cost (3d); (T18)-(T19) play no role in the proof of (T20) (5g); the Section 6 scope sentence should carry its quantifiers (6a). None changes a conclusion. Credit Codex gpt-6-astra max for the volume-independent plaquette mean (T5), the full-cost displacement bound (T7) and the triangular coherent map (T13)-(T15).

RESULT: Every item of gap-trf-astra.md in the brief HOLDS under a hand check by Claude Opus 5.5 — (T1)-(T2), the packing bound (T3)-(T5), Theorem 3 with (SD) and (T9), Corollary 4 with (T12), and the coherent map (T13)-(T20) are correct, with three precisions that change no conclusion (the standard representative in (SD), the unused (T18)-(T19), the quantifiers of the Section 6 scope sentence); nothing FAILS, and the lead is right that (T9) binds every correct transport to the twisted law, so it excludes small-displacement designs, not the (TR-F) route.
