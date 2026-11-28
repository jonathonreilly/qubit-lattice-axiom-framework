lead: anthropic/claude-opus-5-5/high laptop-subagent (row 1420)
provenance: check started 2026-11-23T00:43:34Z (date -u). Checked file: the lane's library/gap-rg-step-sizing-astra62.md (row 1418, written by gpt-6.2-astra). Research text only; no status is granted.

Plan: read row 1418 in full; then check items 1-10 of FINISH row 1420 in order, re-deriving where possible with exact rational scripts in a fresh scratch folder (python3 -I); append each item here as it is finished; end with ranked defects, outcome paragraph and RESULT line.

## Item 1. Site tensor, tail bound, N = 2048 benchmark (row 1418 lines 39-56)

Verdict: HOLDS. Re-derived by hand; integer and rational inequalities rerun exactly (scratch script s1.py).

- Character coefficients. With weight exp(beta(cos theta - 1)), exp(beta cos theta) = sum_n [2(n+1) I_{n+1}(beta)/beta] chi_{n/2}. So c_0 = 2 e^{-beta} I_1/beta and b_n = (n+1) I_{n+1}/I_1. Matches line 39.
- GL4 bound. Termwise, I_{nu+1}(x) <= (x/2) I_nu(x)/(nu+1). Iterating, I_{n+1}/I_1 <= (beta/2)^n/(n+1)!, so b_n <= (beta/2)^n/n!. This gives (5/4)^n/n! on [0, 5/2] and 1/n! at beta = 2. Re-derived.
- Haar projector and corner split. The integral over one link of the six oriented representation matrices is the orthogonal projector onto the invariant subspace. Splitting it as sum_alpha |alpha><alpha| over the two link ends and putting b_n^{1/4} on each corner gives back the four-corner weight b_n. A_{0...0} = 1. Standard Oeckl-Pfeiffer. Holds.
- Entry bound. A vertex entry with fixed corner spins is a contraction of eight unit intertwiners along 24 edges. Merging pieces and contracting all shared edges at each merge gives |entry| <= 1 times prod b^{1/4}. The multiplicity on a link is at most the product of its six dimensions. Each corner lies on two link ends. So ||A||^2 <= (sum_n (n+1)^2 b_n^{1/2})^24 <= H^24. The union bound over 24 corners gives ||A - A_{<=N}||^2 <= 24 T_N H^23. Re-derived.
- H^2 <= 300 e^{5/2} < 128^2. Cauchy-Schwarz with weights 2^{-n/2}. The identity sum (n+1)^4/2^n = 300 was checked from the closed form (1+11x+11x^2+x^3)/(1-x)^5 at x = 1/2. 300 e^{5/2} < 16384 checked from e < 2.72. Holds; so H < 2^7 and ||A|| < 2^84.
- N = 2048. Checked exactly: 2049! > 1024^1025; 5^2049 < 2^683 4^2049; 2050^2 < 2^24; the ratio h_{n+1}/h_n < 1/2 at n = 2049 (and it decreases in n). Then (2 h_2049)^2 < 2^{-9516}, so T_N < 2^{-4758}. 24 T_N H^23 < 2^{-4580}, so the tail norm is below 2^{-2290}. Telescoping: 16 (2^84)^15 2^{-2290} = 2^{-1026} < 2^{-1000}. Holds.
- Perturbation tube (line 56). 16 (2^84+1)^15 2^{-1400} is about 2^{-136}; the file's 2^{-121} is a loose but true bound; 2^{-121} + 2^{-1000} < 2^{-120}. Holds. Note: 2^{-120} is an absolute radius in unrenormalised units where the tensor norm can be as large as 2^{1344}; the file says so ("unrenormalised block-tensor units").
- A Bessel-series spot check of b_n <= (beta/2)^n/n! at beta = 1/2, 2, 5/2 for n < 15 agreed (truncated series; guide only, not a proof step).

## Item 2. Inventory D_N and the counts (lines 60-80)

Verdict: HOLDS. Re-derived the formula; recomputed every count by a different route (scripts s2.py and s2b.c).

- Formula. With V_{n/2} carrying weights z^n, z^{n-2}, ..., z^{-n}, the singlet count of W^{(x)6} is [weight 0] - [weight z^2]. z^N chi_W equals the Gaussian binomial (1-z^{N+1})(1-z^{N+2})/((1-z)(1-z^2)) (checked by hand at N = 0, 1, 2). The sixth power is palindromic of degree 12N, so [z^{6N+2}] = [z^{6N-2}], and D_N = [z^{6N}](1-z^2) F^6. This is line 62. Re-derived.
- Exact check of the formula against a direct weight count at N = 1, 2, 3, 4, 7: 51, 977, 9145, 55031, 2733524 by both routes. D_2048 = 7,467,515,903,828,308,564,331,208,705 by the formula, equal to line 70.
- Counts 1, 15, 30, 5 (Catalan singlet multiplicities 1, 1, 2, 5 times C(6,k)); D_1 = 51. Holds.
- Table (line 68-70). 51^8 = 45,767,944,570,401; 51^64 = 1.925e109; 51^96 = 8.447e163; 977^8 = 8.301e23; 977^64 = 2.256e191; 977^96 = 1.071e287; D_2048^8 = 9.670e222; D_2048^64 = 7.643e1783; D_2048^96 = 6.682e2675. All match. 32 x 51^8 bytes = 1.4646e15, "about 1.46 PB" holds.
- Slots. The vertex figure is K_{2,2,2,2} (8 link ends, 24 corners, no edge between +mu and -mu). Even subgraphs: 2^{24-8+1} = 131,072. A brute-force C program over all 2^24 corner subsets, in exact integer arithmetic, gives 131,072 even subgraphs and sum_F prod_v Cat(deg_F(v)/2) = 12,910,079. This route is independent of the file's spanning-tree and signed-quadrature routes. 12,910,079 x 32 = 413,122,528 bytes. Holds.
- Histogram (line 76-78). The same run, grouped by the six-bit pattern at leg +1: vacuum 50,920 (1 label); 3 same-axis pairs 114,551; 12 cross-axis pairs 115,144; 3 four-sets with same-axis complement 262,978 (2 labels each, 6 labels); 12 others 265,805 (24 labels); the full pattern 635,318 (5 labels). First moment 12,910,079; second moment 4,329,800,859,159. Both match. The second moment counts matched pairs of a join along one bond because the reflection of axis 1 is an automorphism of K_{2,2,2,2} carrying the +1 histogram to the -1 histogram.
- Gram entries. ||pair||^2 = sum_{alpha,beta} (A^T A)_{alpha beta} (B B^T)_{alpha beta} = tr(G_A G_B). The 51 x 51 Gram is block diagonal by six-spin pattern with blocks 1, 15 x 1, 15 x 2, 1 x 5: 1 + 15 + 60 + 25 = 101. Each slot meets at most 5 labels in its block, so at most 5 x 12,910,079 multiply-adds. Holds.
- Caveat (not a defect): the brute force is an exact computer count outside Lean, as the file's own count is.

## Item 3. Triangle and square minors, rank bounds (lines 84-104 and 132-143)

Verdict: HOLDS. Re-derived the minor and the magnitudes by hand; all thresholds and big integers rerun exactly (s3.py).

- Diagonality. A selected column (labels on the seven other legs) fixes the six corner spins at leg +1. Each selected six-spin pattern carries exactly one selected row (unique singlet for one-cycle rows; one chosen matching for two-triangle rows). So each selected column meets only its designated row, and distinct patterns give orthonormal rows. Holds.
- Cycle magnitude d_n^{1-k/2} b_n^{k/4}. Each corner pairs a row index with a column index of the plaquette trace. Around a k-cycle the number of (row,row) legs equals the number of (column,column) legs, so the epsilon factors cancel to +-1 and the trace is +-d_n, times d_n^{-k/2} from k unit singlets and b_n^{1/4} per corner. So triangle b^{3/4}/sqrt d and square b/d = I_{n+1}/I_1. Holds. (I checked that the trace cannot vanish: an odd count of epsilons is impossible by this parity.)
- Triangle >= square iff b_n <= d_n^2; true since b_n <= 1/n! at beta = 2.
- Numbers at beta = 2. I_2(2) > 1/2 and I_1(2) < 2 (first term; 1 + 1/2 + 1/11 < 5/3 < 2 with the stated geometric tail). I_3(2) > 1/6 + 1/24 = 5/24. So n = 1 entries > 1/4 and n = 2 entries > 1/8; I_{n+1}(2) > 1/(n+1)! gives > 1/1440 for n <= 5. A rigorous rational enclosure gives I_1(2) = 1.5906..., consistent.
- Rank thresholds by Eckart-Young on the diagonal minor: k = 16, a = 1/4: r >= 16; k = 31, a = 1/8: r >= 31; k = 76, a = 1/1440 > 1/2048: r >= 76. Recomputed exactly.
- 166-row minor. Two triangles meeting only at +1: the row is the product of two unit singlets, the column is a basis label, the entry is u_n u_m. Counts: 15 four-sets (each has at least one cross-axis matching, since four legs from three axes contain a full axis and the matchings avoiding it are cross-axis); 12 x 5 = 60 for (1,2) and 60 for (1,3) (after a cross pair, the remaining four legs contain exactly one same-axis pair). Total 31 + 15 + 60 + 60 = 166. Bounds: u_1 > 2^{-5/4} > 2/5 (625 > 512); u_2 > 1/8 ((3/8)^3 8^4 > 9); u_3 > 1/16 using b_3 > 1/12 (8^4 > 12^3). Smallest product (2/5)(1/16) = 1/40. Holds.
- Rank-128: error^2 > 38/1600, so error > sqrt38/40 > 1/8 (2432 > 1600). Strengthened ranks 67, 142, 166 recomputed exactly.
- Sizes: 67^8 = 406,067,677,556,641 (x 32 bytes = 1.30e16, "about 13 PB"); 67^15 = 2.461e27; 32 x 67^14 = 1.175e27 bytes; 3^15 = 14,348,907; 32 x 3^14 = 153,055,008 bytes; 16^15 = 2^60; 32 x 16^14 = 2^61; 32 x 16^8 = 2^37. All match.
- Scope remark (not a defect): the rank floor is for this presentation (b^{1/4} per corner, raw bond basis). A diagonal reweighting of the bond basis keeps the rank of the flattening but changes HS errors; the file restricts the claim to "the chosen site tensor" (line 16, 102), which is correct.

## Item 4. Derivative of the raw regrouping (line 106)

Verdict: HOLDS. Re-derived by hand.

- At V = e_0^{(x)8}, a perturbation C at site x with nonvacuum legs +1, +2, +3 contributes to the block derivative only if those three legs are external, i.e. x_1 = x_2 = x_3 = 1; x_4 is free. Two sites. On an internal bond the neighbour V offers only vacuum, so the term vanishes otherwise.
- The two outputs are nonvacuum at different microscopic positions of the bundled faces +1, +2, +3, so they are orthogonal; each has norm ||C|| = 1. The vacuum component of each is zero, so z' = 0 and the derivative of Y/z is Y'. Norm sqrt 2. Holds.
- Reflected orientations (s_1, s_2, s_3) use different bundles, so all images are orthogonal and the factor sqrt 2 persists for any normalized combination. A unitary relabelling of each bundled leg keeps the norm. Holds.
- Closed periodic contraction of V + tC: any term with at least one C needs nonvacuum on some incoming leg -mu of a neighbour, which neither V nor C has. So every closed contraction equals 1. Holds. The conclusion (a local HS contraction claim fails at its centre; local HS distance is presentation-dependent) follows.

## Item 5. Certificate (1) and inequality (2) (lines 110-118 and 145-157)

Verdict: HOLDS. Re-derived by hand; constants rerun exactly.

- (1). ||Y - Y_*|| <= ||X - C|| ||Y'|| + ||C|| ||Y' - D|| <= eta(||D|| + xi) + ||C|| xi = e; |z - z_*| <= e. The t^2 line equals ||Y_* - z_* W C'||^2 because W is an isometry. Then ||Y - z W C'|| <= e + t + e ||C'|| and z >= z_* - e > 0, so ||Y/z - W C'|| <= eta'. Holds. The remark that the norm of Y_* must include the complement of the isometries is correct and important.
- (2). From (1), eta'(z_* - e) >= (1 + ||C'||) e >= ||C'|| e, and z_* - e <= z_* <= ||Y_*|| <= ||C|| ||D||. So eta'/||C'|| >= e/(||C|| ||D||) >= eta/||C|| + xi/||D||. Holds.
- Norm bound ||A_2|| <= (sum (n+1)/sqrt(n!))^12. Summing the two copies of each link intertwiner gives the Haar projector; each corner becomes a trace of a product of two unitary representation matrices, modulus <= d_n, times b_n^{1/2}. So ||A||^2 <= (sum d_n b_n^{1/2})^24, with b_n <= 1/n!. Cauchy-Schwarz with sum (n+1)^2/2^n = 12 (closed form (1+x)/(1-x)^3 at x = 1/2) and e^2 < 8 gives 12^6 8^6 = 96^6 = 7.83e11 < 10^12. Holds.
- Leaf ratio. eta >= ||A_2 - C|| > sqrt38/40 > 1/8 for any centre of bond rank <= 128; ||C|| <= ||A_2|| + eta; so eta/||C|| > (1/8)/(10^12 + 1/8) = 1/(8 10^12 + 1) > 2^{-43} (2^43 = 8.796e12). Holds.
- Propagation. By induction over the binary fusion tree, the output relative radius is at least the sum of leaf ratios: > 2^32 2^{-43} = 2^{-11}. A normalized output has ||C'|| >= 1 (vacuum entry one), so eta' > 2^{-11} and ||C' - V|| + eta' > 2^{-11}. Holds. The obstruction is to scalar-radius propagation through (1) over this eight-doubling pilot; the file states its scope correctly (line 157).
- Trial sizes (line 122-124). H(1+8r) = 128 x 1025 = 131,200; 6 r^3 = 12,582,912; 6(Hr^3 + H^2 r^2 + H^3 r) = 4,831,838,208; 6 r^4 = 1,610,612,736; total well under 10^10. Workspace about 0.40 GB for six isometries plus about 13 MB of centres, under 0.6 GB. 16 x 8 x 4 = 512; 512 x 10^10 = 5.12e12; 512 x 12,582,912 x 32 bytes = 206,158,430,208, "about 206 GB". All hold. The mixed-term contraction order (W_e u'_{le} reshaped, then pre- and post-multiplied) gives exactly the stated count.

## Item 6. Endpoint polymer bound and (3) (lines 161-171)

Verdict: HOLDS. Re-derived by hand.

- Expansion. Writing each site as V + (A_x - V), unmarked sites offer only vacuum, so the contraction factors over nearest-neighbour components; polymers are compatible iff disjoint and non-adjacent. A component's weight is a contraction of its tensors with unit vacuum vectors on boundary legs, so |w(X)| <= (2^{-11})^{|X|}. Holds (also for wrapping sets: merging pieces never creates a self-loop).
- Counting. Rooted connected k-sets in a degree-8 graph: at most 8^{2(k-1)} depth-first walks of a spanning tree. Rooted sum with e^{2|X|}: (e^2/2048)/(1 - e^2/32). The claim "< 1/192" is equivalent to e^2 (192/2048 + 1/32) = e^2/8 < 1, i.e. e^2 < 8. True. So < 1/192 < 1/100. This matches the form of (M1a) in the lane's gap-means-astra.md line 409 (sup_x sum_{gamma ni x} |z| e^{2|gamma|} <= 1/100). Holds.
- Kotecky-Preiss with a(X) = d(X) = |X|: incompatible polymers meet at most 9|X| sites, sum <= 9|X|/192 < |X|. Singleton test gives sum_{C ni x} |Phi(C)| e^{d(C)} <= 1. Holds.
- (3). Clusters of total size < m/2 have connected support of extent < m/2, so they do not wrap and are in bijection (q to 1) between the cover and the small torus, with equal Phi when the cover's tensors and saved scalars are lifts. The rest is at most V e^{-m/2} on each torus: q V_s on the small one after multiplying by q, q V_s on the cover. Total 2 q V_s e^{-m/2}. Holds. The lift condition (periodic pattern of tensor types repeated on the cover) is necessary and is stated.

## Item 7. Placement in Theorem T, Proposition CH and (M-neutral) (lines 173-175)

Verdict: HOLDS. Read against the lane's gap-shrink-box-fable.md lines 152-165 and 217-220, gap-shrink-box-check-astra.md lines 32 and 92-96, and gap-seed-astra62.md line 11; arithmetic re-derived.

- Theorem T. KER is (KER)(beta_w; n_w, (2 n_w)^3; log(1 + q_0/5041)) (row 1332 line 161); A2 is the all-coupling clause with N(beta) <= C_1 exp(c(beta - beta_w)) at margin q_0 (line 156); A3 is c < (log L)/kappa + log(1/q)/(4 kappa), equivalently 4 c kappa < 4 log L + log(1/q) as line 173 writes. One doubling per delta gives c = (log 2)/delta. Row 1386's 0.173 is (log 2)/4.0 (row 1386 lines 277, 317), a GUIDE value; "illustrative" is accurate. Geometry: 4 x 2^31 x e^{-64} = 2^{33} e^{-64} < 2^{-59} < 2^{-31} < log(1 + 1/10082). Holds. "KER only" is right: A0-A3 remain.
- Proposition CH. END is L^4 log Z(T_ell) - log Z(T_{L ell}) <= phi_*. With q = L^4, (3) gives 2 L^4 V_s e^{-m/2}. Check 1335 line 32 repairs Theorem T by a working tolerance 0 < p < (L/2) log(13/10); row 1418 uses that p. Check 1335 line 94 confirms CH needs no UNIV-K and no other cutoff. Holds.
- (M-neutral). Quantifiers (one admissible side, n_j = L/a_j, 4 | n_j, n_j >= 2^70, beta_0 <= beta_j <= B_0 log n_j, w_j = floor(n_j/1024), target s(2w_j) <= 4/21) match row 1367 line 11. F(t) = t log lambda_0 + log(1 + S_all(t)) and S_all(2t) <= S_all(t) (all ratios in [0,1] for a positive transfer matrix) give 2F(t) - F(2t) >= log(1 + S_all(t)). The Perron vacuum is centre-invariant, so lambda_0 lies in the neutral range and s_0 <= S_all. Defect <= log(25/21) gives S_all <= 4/21. Example: 4 m b^3 = 2^57 at m = 2^7, b = 2^16; 2^57 e^{-64} < 2^{-7} because e > 2; log(25/21) > 4/25 > 1/128. b/m = 512 matches n/(2w). Holds.

## Item 8. Filter table against row 1386 section 4.5 (lines 179-187)

Verdict: HOLDS. Read against gap-mech-direction2-fable.md lines 353-365; the t2 and t4 statements re-derived.

- t1: the method has no non-Abelian ingredient; the file reports zero established gain, which is the honest reading. On a U(1) intertwiner space of dimension <= 1 all channel projectors commute, so the named commutator line vanishes. Holds.
- t2: in d dimensions the triangle perturbation survives at 2^{d-3} block sites, norm sqrt(2^{d-3}); d = 5 gives 2, d = 4 gives sqrt 2. Holds.
- t3: a reading; correct as stated.
- t4: b_n = E_w[chi_{n/2}] under the normalized single-plaquette law, so b_n -> d_n as beta -> infinity; square entries -> 1, triangle entries -> d_n^{1/4} >= 1. With more than r such rows the error of a rank-r ball exceeds 1/2 for large beta. So the hypothesis dies as beta grows, which is what t4 requires. Holds.
- t5: the method is named (certificate (1)), and the directed-triangle example shows it separates presentations with equal masses. Holds. Wording defect: "the rank-128 trial fails it" means it fails (1)-(2), not t5 (defect 5 below).

## Item 9. Sector design and counts (line 193)

Verdict: HOLDS as a design with correct counts. It proves no radius, as the file says. Re-derived.

- 3^8 = 6,561 sectors (vacuum, retained nonvacuum, complement per leg). Matching on the shared bond: 3^7 x 3^7 x 3 = 3^15 = 14,348,907 pairs.
- Routing. If W maps R^r into retained (x) retained and sends the unit vacuum to e_0 (x) e_0, then a complement input on a bundled leg is orthogonal to the image of W, so it stays complement; vacuum (x) vacuum is the vacuum; the other low products are orthogonal to e_0 (x) e_0 and split into at most two output sectors. Axial legs keep their sector. So at most 2^6 3^15 = 918,330,048 routing terms. Holds. The design needs W(e_0) = e_0 (x) e_0 exactly; "distinguished unit vacuum" (line 110) should be read that way.
- Cost: 3 x 10 x 918,330,048 = 2.75e10 plus the core (< 1e10) is under 5e10; 512 x 5e10 = 2.56e13. Sector norms: 8 x 3^8 x H^2 = 8.6e8 per centre at H = 128. Holds as estimates.
- The zero for a lone high strand: a complement error on the shared bond meets a centre with no complement component, so that term vanishes. Correct.

## Item 10. 2D Haar gluing fixture (lines 196-256)

Verdict: HOLDS. Rerun and recomputed independently (s10.py, exact rationals).

- The five assertions of lines 219-223, copied verbatim, all pass.
- Independent route for the coefficients. Using Catalan moments E[(2u)^{2k}] = Cat(k) under Haar measure, f = 15/16 + u/2 + u^2/4 has character coefficients (1, 1/4, 1/16, 0). Schur orthogonality gives chi_i * chi_j = delta_ij chi_j/d_j, so (f^{*4})_j = f_j^4/d_j^3: 1, (1/4)^4/8 = 1/2048, (1/16)^4/27 = 1/1769472. Recomputed.
- S^3 moments from the spherical moment formula: E q_0^2 = 1/4, E q_0^4 = 1/8, E q_0^2 q_1^2 = 1/24, so E x^2 y^2 = u^2/8 + (1-u^2)/24 = (1 + 2u^2)/24; odd moments vanish. haar_glue then equals to_polynomial(schur_glue) on 200 random rational inputs, a stronger check than the fixture. f is strictly positive (minimum 11/16 at u = -1) and has unit mean.
- Lean fixture (not run in Lean; no Lean used here). Its arithmetic replayed on Python naturals: examples 1 and 2 are true, 3 and 4 false as intended. The cube value b^6/16 at b = 1/16 equals 2^{-28}; b^6 d^{V-E} with V - E = -4 is the unbranched-surface formula. The quadrature weights have moments 1, 0, 1, 0, 2, 0, 5 exactly.
- Minor inconsistency (defect 3 below): the Lean corruption b := 6912 is fundamental coefficient 1/512 (two missing 1/2 factors). The Python wrong output 1/256 drops all three 1/d factors. A single missing 1/d would be 1/1024 (b = 3456). Line 226 calls the test "a missing 1/d". Each fixture still rejects a wrong value.

## What I re-derived and what I only read

- Re-derived (hand, and exact rational or integer scripts where numbers occur): items 1-6, the t2 and t4 rows of item 8, item 9, item 10. Independent routes: a C brute force over all 2^24 corner subsets for the slot count and histogram; a direct weight count for D_N; Catalan moments plus Schur for the 2D coefficients; a generic random-input test of haar_glue against Schur.
- Only read: the repo-search section (lines 1-12); the literature descriptions in lines 24, 33, 35, 192, 193 (Lanford, Koch-Wittwer, the numbers 63, 0.02, 0.96 of Ebel-Kennedy-Rychkov, Oeckl-Pfeiffer, Yosprakob, Yosprakob-Okunishi, Ebel 3D); the SA and CA line citations; the t1, t3 rows of item 8. No paper was fetched. None of these is load-bearing for the ten items.
- No Lean was run. The scripts are scratch checks outside the repository; under the lane's rule they are a guide for the counts, while the inequalities they test are elementary integer comparisons.

## Ranked defects (none breaks a conclusion of row 1418)

1. Scope of the scalar-radius negative (lines 16, 143-157). The 166-row minor binds only centres of bond rank <= 165; the stated kill covers rank <= 128 leaf centres over the eight-doubling pilot. The stronger and general content is (2) itself: for any rank, scalar propagation through (1) needs the leaf relative radii to sum below the end tolerance, here an average below 2^{-43} over 2^32 leaves. The headline should say this; as written a reader may think a rank-256 factored trial escapes. Breaks nothing; sharpens the negative.
2. Sector routing needs W(e_0) = e_0 (x) e_0 exactly and image(W) inside retained (x) retained (lines 110, 193). Both are implicit. If either fails, the "stays vacuum" or "stays high" routing is false and the 2^6 3^15 count is not an upper bound. Breaks the sector design only if the producer violates it; the verifier must check it.
3. Fixture corruption labels disagree (lines 222, 226, 254). Python's wrong value 1/256 drops all three 1/d factors; Lean's b := 6912 is 1/512; neither is "a missing 1/d" (1/1024, b = 3456). Breaks nothing; the acceptance test of next row 1 should name which corruption it tests.
4. No kernel receipt for 12,910,079, the histogram, the 4,329,800,859,159 pairs or the fixtures (the file says so, line 18 and 194). My C count agrees, but it is also outside Lean.
5. Wording at line 185: "the rank-128 trial fails it" refers to (1)-(2), not to the filter t5.
6. Line 56: 2^{-121} is true but loose; the term is about 2^{-136}. Cosmetic.

## Outcome

Both negative conclusions hold. Dense rank: at beta = 2, error <= 1/4 in the chosen site tensor needs bond rank >= 67 by an exact 166-row diagonal minor, and a dense fusion at that rank costs more than 2.46e27 multiply-adds; this rules out the dense implementation. Scalar-radius propagation: inequality (2) is a correct consequence of (1), relative radii add over leaves, and the rank-128 leaf ratio exceeds 2^{-43}, so after eight doublings the radius exceeds the end tolerance 2^{-11} for any centre choice and any precision. The certificate (1), the endpoint bound (< 1/192, matching the form of (M1a)) and the cover estimate (3) all hold, and their placement in Theorem T (KER only), Proposition CH (with check 1335's tolerance p) and (M-neutral) (with s_0 <= S_all) is correct. The sector design holds as a design: the counts 6,561, 3^15 and 2^6 3^15 and the cost estimates are right, under the vacuum and support conditions on W of defect 2; it proves no radius, as the file states. The 2D Haar gluing fixture is correct, and its coefficients 1, 1/2048, 1/1769472 follow from Schur orthogonality. It is a sound first kernel bring-up with a known answer. On its own it tests only the 1/d factor and denominators; it does not touch duals, magnetic-index signs or 4D recoupling, nor the crux. It is the right first build only together with the bundled 4D N = 1 inventory, the signed closed cube and the twist-sign fixtures that next row 1 already requires. The critical-path item is next row 2, the signed 4D inclusion.

RESULT: Row 1418 HOLDS on all ten items (no FAILS, no correction needed to any conclusion; six minor defects, chief one a scope sharpening of the scalar-radius negative). Dense-rank and rank-128 scalar-radius negatives hold; certificate (1), inequality (2), endpoint bound and (3) hold with correct placement in Theorem T, CH and (M-neutral); the sector design holds as a design with correct counts; the 2D Haar fixture passes all five assertions and its coefficients were recomputed by Schur orthogonality. Checked by anthropic/claude-opus-5-5 (laptop subagent, row 1420) against a gpt-6.2-astra file; no Lean run; no status granted.
