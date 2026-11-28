# Check of row 1689 (gap-purity-rh-strategy-astra62.md), FINISH row 1704

lead: anthropic/claude-opus-5-5 laptop subagent

Started Sat Nov 28 15:22:02 UTC 2026, pinned at commit 2e718fc6f. Checked by Claude Opus 5.5; author of the checked file gpt-6.2-astra max.

## Plan

1. Read the crux card (target, (Y4) filter in section 3).
2. Read the whole row 1689 file.
3. Check every PROVED item: equations (1)-(12), Lemmas A, B, C, Haar-tail bound (move 8), bulk-cancellation comparison, auxiliary-edge count. Check hypotheses against Stage0.lean, Transfer.lean, Purity.lean.
4. Check at least ten Part 1 citations of rh-outline-v1.5.tex by line number.
5. Check the Part 3 on-file verdicts for measurements A, B, C by searching the lane library.
6. Key question: do A and C read the non-abelian law, or only an operation that is trivial for U(1)? Concrete U(1) test.
7. Verdict table and RESULT line.

## Findings (appended as I go)

### Progress log

- Read in full: `gap-purity-crux-card.md` (60 lines), `gap-purity-rh-strategy-astra62.md` (346 lines), the (Y4) filter `gap-purity-rh-strategy-fable-check-astra62.md` section 4 (L93-104), check 1698 `gap-purity-afield-astra62-check-opus.md` (141 lines).
- Read Lean anchors: `Stage0.lean` L55-80 (centreTranslation, neutralProj = (1/8) sum over the subsets of the three spatial axes), L145-155 (betaAt); `Purity.lean` L1-40 (purity); `Transfer.lean` L540-680 (temporal, transferKernel, transferKernel_apply, transfer_positive). The transfer kernel is exp(-beta(S(u)+S(v))/2) times a vertex-gauge integral of prod_e exp(-beta(1 - halfTrace(g_x v_e g_y^{-1} u_e^{-1}))). So each spatial edge e carries exactly one temporal factor per step, and it reads u_e and v_e once each.
- Read `PurIo.lean` L389-405: `su2_fixed_observable_cutoffs_at_fixed_offset` gives, for every infinite set of cutoffs, a subsequence with betaAt/(K log L) -> 11/(3 pi^2). So, as row 1683 L59-64 says, beta_k <= (11/(3 pi^2) + eps) k log L for all late k.
- Guide script (exact integers and fractions, never proof): scratchpad `lemmaA1704.py`, run with `python3 -I`. Output: 15 matchings; Gram rank 5; overlaps with one matching: 1 (once), 1/2 (6 times), 1/4 (8 times); G^2 = 3G, Tr G = 15; E v_i = F v_i = 0 for all i; ker E on weight zero has dimension 5; for a random integer positive A on C^64, sum_{i<j} D_ij = 8017 = 9 e_2(A_W).

## Item 1. The PROVED items

All verdicts are by hand, by Claude Opus 5.5, at 2e718fc6f. Line numbers are those of the row 1689 file.

**Common measurement, L60 (trace identities). HOLDS.** u = n/512 = 2 (l/1024) L^k is even, because 1024 | l. P_0 is the (1/8) average of the centre translations over the subsets of the three spatial axes (`Stage0.lean` L71-72). Each translation commutes with T. So P_0 is a self-adjoint projection and B = P_0 T^{u/2} is self-adjoint with B B^* = P_0 T^u = A. The kernel is real and continuous, because `transferKernel` (`Transfer.lean` L548-551) is a product of continuous real functions and P_0 is a finite average of measure-preserving pullbacks. Purity = Tr(P_0 T^{2u})/Z^2 = Tr rho^2 by P_0^2 = P_0 and [P_0, T] = 0 (`Purity.lean` L25-29). I did not locate the definition of `tracePW` in the lane's Lean folder (it comes from an import). I accept the file's reading that it is the basis trace of a positive trace-class operator.

**Exterior-square identity and (1), L62-76. HOLDS.** sum_{i<j} p_i p_j = (1 - sum p_i^2)/2 because sum p_i = 1. The target 457/625 is the same as Tr wedge^2 rho <= 84/625. E_pi R_x = (1/Z) int |B(.,x)><B(.,x)| dx = B B^*/Z = rho. ||R_x||_HS = 1, so Var(R_x) = 1 - Tr rho^2. (1/2)||R_x - R_y||_HS^2 = 1 - |<v_x,v_y>|^2, so the Dirichlet form of x -> R_x is D_Q. The scalar Poincare inequality, applied in a real orthonormal basis of self-adjoint HS operators and summed, gives (1).

**Lemma A, L228-238. HOLDS** (hand proof checked; the exact guide above agrees). Weight-zero dimension 20, weight-two dimension 15, F injective on weight two, so dim W_0 = 20 - 15 = 5. The cycle count gives |<v_i,v_j>| = 2^{c-3} with c = 3, 2, 1 for 1, 6, 8 matchings. Tr S^2 = 15(1 + 6/4 + 8/16) = 45 and ||S - 3I||_HS^2 = 45 - 90 + 45 = 0. The minor identity follows from wedge^2(X X^*) = 9 I and the basis independence of e_2. The competing lower bound: t^2/9 - t^2/36 = t^2/12, and 9/12 > 9/16. Comment (not an error): the identity is the general fact that for a tight frame with constant c, sum_{i<j} D_ij = c^2 e_2(A_W). The factor 9 is the frame constant squared. It carries no Wilson information.

**Omitted-minor bound and budget, L99. HOLDS.** Each omitted minor is at most rho_ii rho_jj; charge it to an omitted index; the sum is at most t sum_j rho_jj = t. 1/32 + 1/12 = 11/96 < 84/625.

**Physical embedding, orthogonality of translates, (6), (7), L240-256. HOLDS.** Schur orthogonality gives the orthonormal products of sqrt2 U_ij. Each loop has a private link, so the three holonomies are independent Haar. The loops are contractible, so each centre cut flips 0 or 2 of their edges and W is neutral. An edge in one translate's packet only enters linearly in one fundamental factor, so its Haar integral is zero. Translation invariance of rho on the gauge-invariant space gives (6). The block-circulant structure gives (7) by e_2 of a union of spectra.

**Separation, L260. HOLDS.** A_W = I gives 10/25 = 2/5.

**Lemma B toy constants, L105, L268, move 8 L150. HOLDS.** sum_{d>=2} d^{-4} <= 1/16 + 1/24 = 5/48; purity >= (48/53)^2. One-coordinate scan: largest nonconstant eigenvalue (N - 1 + 1/4)/N = 1 - 3/(4N). Tail: sum_{d>=2} d^{2-2m} <= 2^{2-2m} + 2^{3-2m}/(2m-3). Parallel refresh: purity >= (1 + B_u)^{-2N} >= 1 - 2N B_u with B_u <= 3 * 2^{2-2u}.

**Lemma B (8)-(9), L270-285. HOLDS.** With t <= 1/512 and d^2 <= 4^{d-1}, eta <= 4t/(1-4t) = 1/127 < 1/64. The two selected far sides share no plaquette, so their conditional densities multiply. The push-forward to the word law keeps the factor [1 - Delta, 1 + Delta]. ||w||_2^2 = sum_{d>=1} d^{-2} <= 2. Bessel gives sum_{d>=2} d^2 |c_d - d^{-2}|^2 <= 2 Delta^2. Delta = 129/4096, so 2 Delta^2 < 0.002 < 1/256. Single-link tilt 6 beta: a link of 4D spacetime lies in 6 plaquettes. The application on the calibrated cutoffs (L287) HOLDS by `PurIo.lean` L389-405 (beta_k = O(k), h = s L^k).

**Robustness, L289-296. HOLDS.** |c_{i,d}| <= 1/4 + 1/32 = 9/32 for d >= 2; (9/32)(17/16) = 153/512; (153/512)^2 < 1/10; purity >= 100/121. For central laws on SU(2) the c_d are real, since the characters are real.

**(10), L298-308. HOLDS.** The pointwise minimum of two measures is monotone, so the accepted measure keeps the factors 1 +- Delta. The fixed-entrance increment law is ARGUED in the file at the level of "condition on everything except the pivots"; I accept it, since the pivots miss the entrance slice and the chord.

**(11), L310-327. HOLDS.** Z_neutral >= Z_untwisted/8; Haar chance of angle <= beta^{-1/2} is >= (6 pi)^{-1} beta^{-3/2}; plaquette deficit <= 8/beta; -log Z <= beta V b_beta (the log 8 term is overcounted by a factor V, which is harmless). Convexity of log Z gives E S <= -log Z/beta. mu(B_a) <= 1 - cos t = a^2/2. With r = b^{1/4}: 2(1 + Delta) + 4 <= 7. The median indicator of |Tr U_e| changes only under moves on e, so N gamma <= 2 alpha_e. Comment: the same argument works for every compact group, because it reads only that weak-coupling plaquettes are near the identity.

**Relative-test counterexample, L338. HOLDS** (orders checked: crossing <= C eps^3, staying >= c' eps^2 on average over the ball).

**Lemma C (4) and the Wilson calculation, L181-206. HOLDS.** The Lean kernel confirms the key step: `transferKernel_apply` has one factor exp(-beta(1 - halfTrace(g_x v_e g_y^{-1} u_e^{-1}))) per spatial edge e. With g fixed, (1/2) Re Tr(g_x v g_y^{-1} u^{-1}) = u . O v in R^4, with O orthogonal. So the cross ratio is 4J = beta (U^+ - U^-) . O (U'^+ - U'^-), and all one-cut factors cancel. The reflection of v_3 in span(v_1, v_2) is diag(1, R) on R^4, so it preserves Haar; it changes the private link by chord 2h. Hence |J_i| <= beta h_i h_{i+1}. Birkhoff's formula: the sup of |f_K'| is |ad - bc|/(sqrt(ad) + sqrt(bc))^2 = tanh(|log(ad/bc)|/4), and f_{KL} = f_K o f_L. tanh t <= exp(-2 e^{-2t}) because 2 artanh z >= 2z.

**Correction to the use of (4) (PROVED here).** Since h_i <= |v_{3,i}| <= 1, (4) gives on **every** history q(H_h) <= exp(-2 r e^{-2 beta}) with r = u/2 = l L^k/1024. On the calibrated cutoffs, 2 beta_k <= (22/(3 pi^2) + 2 eps) k log L and 22/(3 pi^2) < 3/4. So r e^{-2 beta_k} >= (l/1024) L^{k/4} for late k, which tends to infinity. Thus q(H_h) <= 1/16 on every history at every late cutoff, with no Wilson input. The GUESSED test of (4) at L222, and the block test prod q(K_i) <= 2^{-m} at L133 for m up to a fixed multiple of r e^{-2 beta}, are settled by Lemma C and `PurIo.lean` L389-405 alone. The "per-cut local gain" reads neither the group nor the law. The whole Wilson content of C is in the common centre delta and the bad mass eta of (5). The decision paragraph's remark (L342) that large beta "can make (4)'s bound ineffective" does not apply on the calibrated trajectory.

**Lemma C (5), L208-218. HOLDS.** A ratio of positive integrals over the good set is a weighted mean of good ratios; the bad mass changes the ratio by a factor in [1 - eta, 1/(1 - eta)]. B is real symmetric, so rows equal columns. (E r)^2/E r^2 >= 4ab/(a+b)^2 by ((a+b)m - 2ab)^2 >= 0, and 1 - 4ab/(a+b)^2 = tanh^2(log(b/a)/2). Numbers: artanh(1/16) < 1/15, log(64/63) < 1/63, D < 1/2, tanh(1/4) < 1/4.

**Separation examples, L131, L220. HOLDS.** aa^T and bb^T have cross ratio 1; the sum has rows with overlap 4t(1+t^2)/((1+t^2)^2 + 4t^2) -> 0. Binary toy: eigenvalues 1, 1/2; purity (1 + 1/64)/(1 + 1/8)^2 = 65/81 > 457/625; (1+x^2)/(1+x)^2 has derivative 2(x-1)/(1+x)^3 <= 0. Spectator: 65/(81M).

**Bulk-cancellation comparison, L153. HOLDS** (one line: log purity = E_{2u} - 2E_u, and |E_{2u} - 2E_u| <= 4 eps n^3 u).

**Auxiliary-edge counting, L155. HOLDS.** If the mean over e of sum_j r_j(e)^2/eta_j^2 is < 1, some e has the sum < 1, so every r_j(e) < eta_j. A square of side h has 4h edges, all private to the third petal.

**Heat-bath contribution and D <= 1/sqrt(2N), L222. HOLDS** (tanh^2(D/2) <= D^2/4 = 1/(8N); times 2p(1-p) <= 1/2).

**Item 1 verdict: every PROVED item HOLDS.** One correction of use: (4) is automatic on the calibrated cutoffs, so the GUESSED test of (4) is not an open Wilson estimate.

## Item 2. Part 1 citations of the v1.5 guide (rh-outline-v1.5.tex, 1464 lines)

I read each range with sed -n. "Matches" means the cited lines say what the row reports.

| # | Row claim (move) | Guide lines read | Verdict |
|---|---|---|---|
| 1 | Sernau and collaborators made the shortening; Poisson summation gives the sieve estimate; the product formula for a Gram determinant replaces slopes; Vandiver-type bound avoided; Galois representations, Euler systems remain (moves 6, 9; L29) | 118-125 | HOLDS |
| 2 | Definition of S_d(y), R(y), c_d (move 1) | 177-188 | HOLDS |
| 3 | Only the one-sided upper bound on R is needed (move 1) | 223-236 | HOLDS. The guide's goal is R(y) <= y^{-1/2+eps} for large y; the row's constant C_{d,eps} is equivalent. |
| 4 | Poles of the twists carry residues with a sign in each family (move 1) | 255-270 (Prop. res: residue (N(z) - N_d(z))/(phi(Q) z(1-z))) | HOLDS as paraphrase (ARGUED in the row) |
| 5 | One-sided criterion on a box Re s >= beta, abs Im s <= H (move 1) | 288-300 | HOLDS |
| 6 | Choose one d per box; a count of failed choices is cheaper than GRH for twists (move 1) | 319-326, 352-372 | HOLDS. Failures <= K X^{1-delta/2}; the count uses the average sum_v J(alpha_v,T) << T^{2+delta} (a first moment of J, itself from a mean-square theta bound). |
| 7 | The lemniscate is an illustration only (move 2) | 476-478 | HOLDS |
| 8 | Normal form theta(varpi z) = W(z) exp(varpi^{p+1} Xi(z)/p) (move 3) | 553-562 | HOLDS |
| 9 | Partner residue couples tau to -p^h tau (move 3) | 427-461 (Lemma partner) | HOLDS |
| 10 | Gaussian norm, norm of z^j squared = j! (move 4) | 570-578 | HOLDS |
| 11 | Data a = xb, m in [sqrt x, 2 sqrt x], f = phi(q), (M) m rem <= fa(log b)^5 (moves 7, 8) | 838-858 | HOLDS |
| 12 | Two-scale identity rem/a = B_0[R(x) - R(x_1)] + A_0 R_1(x_1) (move 8) | 874-876 | HOLDS |
| 13 | Theorems A, B, C; Hadamard c = n(h - m rem + E_0); (n - D)h <= 0 drops h; C supplies Dh (move 7) | 913-951 | HOLDS |
| 14 | Theorem B: second moment of P^*gP, unfolding and repeated Poisson summation, mass factor cancels, greedy translates, abs T dim S <= 5D log(1+2b^2) (move 6) | 1151-1176 | HOLDS |
| 15 | Theorem C: fixed untwisted determinant, twist per place, exchange identities to one-step lifts, Galois/Selmer/Euler systems; cost O(fm^2 b log b) against fa(log b)^3 gives m of order sqrt x (moves 8, 9) | 1179-1202 | HOLDS |
| 16 | Division by m gives x^{-1/2+eta} (move 8) | 983-998 | HOLDS |
| 17 | The small models show bookkeeping only (move 2) | 1405-1417 (A.4 "What the model does not show"; A.5) | HOLDS as paraphrase. A.4 says the model does not show the matching of main terms; "upper-side bookkeeping only" is the row's reading (ARGUED). |

Long guide (zeta-paper_v2.tex, 13700 lines), spot checks: L12885-12895 (census "proves nothing. It is a list."), L13355-13362 (Group J, abelian varieties, rows 152-165), L1223-1230 (summary of what is proved where). HOLDS. I did not verify the counts "all 14 rows ... all 20 rows passed only to S6".

**Item 2 verdict: HOLDS** (17 citations by line number, no mismatch). The Wilson comparisons in Part 1 are the row's proposals (ARGUED), as it says.

## Item 3. Part 3 on-file verdicts

Cited items, read at their locators: row 1418 `gap-rg-step-sizing-astra62.md` L189-193 (noncrossing singlet pairings of sizes 1, 1, 2, 5 for the Haar projector) yes; `gap-tree-astra.md` (G8) L219 (norm of PQ = 1/2) yes; row 1161 `gap-solve9-astra62.md` L229-235 (c n^3 excited neutral trial states) yes; row 778 `gap-vortex-astra.md` (6), (7), (12) L305-505 yes; `gap-brainstorm-max.md` G19 L506 yes; row 1286 `gap-owner-tiling-astra62.md` L13-20 yes; row 1132 `gap-council-op-astra.md` L23-30 yes; `gap-positivity-fable.md` Remark FR L398-410 yes (it says the triple product "vanishes identically for an abelian group"); row 1178 `gap-solve18-astra62.md` L23-31 yes; row 1608 `gap-wmix-wall-astra62.md` L9-20 ("when a handedness sign is released") yes; row 1258 `gap-mini-solve-ag-opus.md` Prop. RR L349 yes; `gap-solve7-astra62.md` contraction q = tanh beta (L57) yes; registry `open-registry.md` R10 L1017, TWO-PER L1020, WMIX-SLICE L1030 yes.

My own search of the lane library (file counts by grep -il): "perfect matching / singlet pairing / six-end / six-valent" 15 files; "tight frame / frame operator" 3; "triple product" 11; "orientation sign / handedness sign" 13; "Birkhoff / projective metric" 26; "commutator law / [X,Y]" 42; "half-slab column / column angle" 0 outside the row. I read the matching lines.

**A. "New restricted measurement" — HOLDS AFTER CORRECTION.** No file bounds thermal minors of a six-end singlet frame (the matching hits are recoupling bases, dimer patterns and Pfaffians). Correction: the frame identity is the generic tight-frame identity, and its group content is SU(2) recoupling (dim 5, constant 3), which is on file (row 1418, (G8)). The new part is only the GUESSED test (2) and the momentum split (7). See item 4 for its U(1) form.

**B. "Word mixing on file" — HOLDS.** The file's own Lemma B shows (3) follows from the straight-bond estimate of row 1145; (11) is the weak-coupling plaquette concentration of `gap-newmath-astra62-max.md`. Only (12) is new, and it is GUESSED.

**C. "New conditional measurement" — HOLDS AFTER CORRECTION.** Two uncited priors own parts of C: `gap-loop-grow-astra.md` L364-374 and `gap-channel-astra.md` L402-410 (scalars, dot products and oriented triple products separate gauge orbits; the triple product fixes the orientation, which is the two-orbit object of C). Birkhoff contraction of slab kernels with tanh(eta/4) submultiplicative is on file (`gap-fr-opus.md` L99; `gap-mini-solve-ah-opus.md` L52, which also records that the diameter stays extensive). With item 1's correction, (4) is automatic. The only new content is the endpoint-bias inputs (delta, eta) of (5) on a binary fibre. They are GUESSED.

## Item 4. Do A and C read the non-abelian law, or only an operation that is trivial for U(1)?

Comparison model for both tests (the one Y4 item 4 asks for): weak 4D compact U(1) with the cosine Wilson action beta sum_p (1 - cos theta_p), the same box n = l L^k, the same aspect u = n/512, the same beta_k (or any fixed large beta), and the three half-turn cuts (eight-term projection). Its purity fails at this aspect (massless photons; crux card section 2).

### C. The U(1) orientation sheet (PROVED here, by the file's own steps)

**The file's U(1) claim FAILS.** L123 and L342 say that for U(1) "all three vectors are collinear and the fibre has one point". That count uses the SU(2) gauge group on U(1) configurations. In the U(1) theory the base gauge acts trivially on holonomies. Take the file's own data for three U(1) petals z_j = e^{i theta_j}: scalar traces cos theta_j and pair traces cos(theta_i + theta_j) fix |sin theta_j| and the products sin theta_i sin theta_j. The fibre is {theta, -theta}: **two points** off a null set. In SU(2) the global flip v -> -v is a rotation by pi, hence gauge; in U(1) it is charge conjugation, not gauge.

**A simpler U(1) sheet with the same bounds.** Take one contractible spatial square of side h = s L^k with a private edge e, holonomy W = U_e R (R the product of the other links). Put sigma(U_e) = conj(U_e) conj(R)^2, so W -> conj(W). This is a Haar-preserving involution of U_e at fixed R (inversion, then translation). It commutes with each half-turn cut (a cut flips 0 or 2 edges of the square; if it flips U_e and one edge of R, then sigma(-U_e) = -sigma(U_e)). The quotient keeps cos theta and all other links. The fibre is {theta, -theta}, two points with conditional Haar weights 1/2.
- The U(1) transfer has one temporal factor per spatial edge, exp(beta Re(U_{e,i} g_x conj(U_{e,i+1}) conj(g_y)) - beta) = exp(beta U_{e,i} . O U_{e,i+1} - beta) in R^2 with O a rotation. Hence 4J_i = beta (U^+ - U^-) . O (U'^+ - U'^-), and |U^+ - U^-| = |W - conj W| = 2 |sin theta| =: 2h_i <= 2. So |J_i| <= beta h_i h_{i+1}: this is (4) verbatim.
- The matrix calculation, (5) and the auxiliary-edge count use no group structure. They hold verbatim.
- By item 1's correction, q(H_h) <= exp(-2 r e^{-2 beta}) on every U(1) history, so q <= 1/16 at every late n, at any fixed beta or at beta_k.

So every proved line of C holds, with the same constants, in weak 4D U(1), where (PUR-io)'s analogue fails. The non-abelian structure enters C only in how a discrete fibre is built (three loops in SU(2), one in U(1)). It enters no estimate. The U(1) bit is the sign of the magnetic flux through the loop, which is charge-conjugation odd and couples to the photon. Whether the GUESSED inputs delta <= 1/16 and eta <= 1/64 of (5) fail for U(1) is a dynamical question; the row states no line that decides it. **Verdict for C: the proved part reads no non-abelian law; the U(1) "void" is an artefact of the gauge group used to count the fibre. Same failure type as row 1683 (check 1698, item 2).**

### A. The U(1) singlet packet (PROVED here, by the file's own steps)

**The file's U(1) claim FAILS as a selectivity claim.** L101 and L342 say that for U(1) the fixed-weight coefficient space is one-dimensional and its exterior square vanishes. That is true only for the choice of charge +1 on every loop. The SU(2) fundamental restricted to U(1) is charge +1 plus charge -1. The U(1)-appropriate packet is W^U = span{ z_1^{a_1} z_2^{a_2} z_3^{a_3} : a in {+1,-1}^3 }, one charge +-1 coefficient per loop, as in the SU(2) W. Then:
- dim W^U = 8. Every element is gauge invariant (the base gauge acts trivially in U(1)) and neutral (each half-turn cut flips 0 or 2 edges of each loop). The eight characters of U(1)^3 are orthonormal under Haar.
- Translates are orthogonal by the file's argument: an edge in one packet only enters as z or conj z, and its Haar integral is zero. So (6) holds verbatim, and (7) holds with 8 x 8 blocks M_p.
- Lemma A holds with frame constant 1 (an orthonormal basis): sum_{i<j} D_ij = e_2(A_W). The lower-bound argument at L238 holds verbatim (t^2/12 > t^2/16).
- The test (2) in U(1) form, e_2(A_W) <= (Tr A_W)^2/16, is not void: A_W = I gives 28/64 > 1/16.

So every proved line of A holds in weak 4D U(1). The non-abelian content of A is the recoupling count (dimension 5, frame constant 3), which is group algebra and not the Wilson law. The law enters A only through the compression A_W of P_0 T^u, and only in the GUESSED test (2), which has the exact U(1) form above. **Verdict for A: the proved part reads no non-abelian law; the U(1) "void" is an artefact of the fixed-weight choice. Same failure type as row 1683.**

### B (brief, ARGUED)

B's U(1) "void" (L113, L338) is real for the commutator move, because [X,Y] = 1 in U(1). That is again an operation that is trivial for U(1). A U(1)-appropriate move (multiply a chord by the product W_X W_Y of two transverse loops, which is non-trivial in U(1)) keeps (1), the comparison (10) with its reference law, and (11): weak-coupling plaquettes are near the identity, so accepted changes are rare in both groups. (11) reads no group structure (item 1).

### Y4 item 4 applied to A and C

No line of A or C has a noncommuting Wilson weight that yields a net gain. The U(1) comparison is stated in the row only through operations that are trivial or degenerate for U(1). With the U(1)-appropriate operations above, all proved lines hold in U(1). The neutral-spectator test fails for both, as the row itself shows (L220, L260). The 5D test fails for the finite lemmas, as the row itself says (L342).

## Verdict table

| Item | Verdict | Note |
|---|---|---|
| 1. Trace identities, wedge^2 identity, (1) | HOLDS | |
| 1. Lemma A, (6), (7), separation | HOLDS | exact guide agrees; factor 9 is a tight-frame constant squared |
| 1. Toy constants, Haar tail (move 8), parallel refresh | HOLDS | |
| 1. Lemma B (8)-(9), robustness, (10), (11), relative counterexample | HOLDS | (11) is group-blind |
| 1. Lemma C (4), Birkhoff formula, (5), separation examples | HOLDS | checked against `transferKernel_apply` |
| 1. Use of (4) | HOLDS AFTER CORRECTION | (4) is automatic on the calibrated cutoffs: q <= exp(-2 r e^{-2 beta_k}) -> 0 on every history, since 2 beta_k < (3/4) k log L; the GUESSED test of (4) is not open |
| 1. Bulk cancellation, auxiliary-edge count | HOLDS | both one-line |
| 2. Part 1 citations (17 checked) | HOLDS | two paraphrases ARGUED (rows 4, 17 of the table) |
| 3. Part 3, A | HOLDS AFTER CORRECTION | recoupling on file; new part is the GUESSED (2), (7) |
| 3. Part 3, B | HOLDS | |
| 3. Part 3, C | HOLDS AFTER CORRECTION | uncited priors `gap-loop-grow-astra.md` L364-374, `gap-channel-astra.md` L402-410, Birkhoff in `gap-fr-opus.md` L99, `gap-mini-solve-ah-opus.md` L52 |
| 4. A reads the non-abelian law | FAILS | U(1) packet of dimension 8 (charges +-1 per loop): all proved lines hold; "exterior square vanishes" is the fixed-weight choice |
| 4. C reads the non-abelian law | FAILS | U(1) sheet theta -> -theta: (4), (5) verbatim with h = abs(sin theta); the file's own three-loop data also give a two-point U(1) fibre |

(PUR-io) stays open. This check grants no status. No Lean run was made; the Lean files were read only.

RESULT: Check 1704 (Claude Opus 5.5) of row 1689. Every PROVED item holds, including (1)-(12) and Lemmas A, B, C; Lemma C matches transferKernel_apply. Correction: (4) is automatic on the calibrated cutoffs (2 beta_k < (3/4) k log L gives q <= exp(-2 r e^{-2 beta}) -> 0 on every history), so C's only Wilson content is the GUESSED delta, eta of (5). Seventeen v1.5 citations hold. Part 3 holds; A and C need prior credits. Key question FAILS for A and C: a U(1) packet (charges +-1, dimension 8) and a U(1) sheet theta -> -theta satisfy every proved line verbatim; the U(1) void comes from operations trivial for U(1), as in row 1683. (PUR-io) open.
