# Check of library/gap-purity-bootstrap-compare-astra62.md (FINISH row 1594)

Checker: Claude (Opus 5.5). Target: row 1592, author gpt-6.2-astra max.

## Plan
1. Read GOAL.md, FINISH.md Rules and Working efficiently.
2. Read the target note in full.
3. Read the lane sources it relies on (gap-crux-restate, gap-seed-shape,
   gap-flux-exercise, gap-solve9-astra62 and its check, row 1161 lines 215-227,
   gap-agy-seed-approaches-neon-check-astra62).
4. Fetch primary texts where needed (OpenAI Haldane note, Grover, Lu) into dl-1594/.
5. Check each part; record verdicts.
6. RESULT line.

## Progress

### Step 1. Primary texts (row §1). Sources read: OpenAI build/bootstrap.tex, transfer.tex, initialization.tex, assembly.tex at adc7f1241b42; Grover arXiv:2611.07400v1 html §§II-IV; Lu arXiv:2611.11049v1 pdf (text extracted by hand script). Copies in dl-1594/ (scratch only).

- (1a) OpenAI Prop. "Uniform gap from two initial purities": hypotheses (non-scalar finite-dim self-adjoint H_L for even L >= 4; shift a; real list with sum |lambda|^4 < inf and Z_L = sum |lambda|^L), staggered seeds S(n0,b0), T(2n0,b0) >= 1-u0, conditions 0<u0<1/6, G(u0) <= C, r = C u0 < 1, C(1-3u0) > 3, u_j = r^{2^j}/C, gap > log(1/r)/b0 for every even L >= n0. Matches the row. Transfer: compact self-adjoint Hilbert-Schmidt X_b with Z_n = sum lambda_i^n (n >= 4) and twisted Z_n(b,g) = Tr(X_b^n U_g). The two parameter rows and both gap values match ((4/105) log(80/79); log 20/784). Initialization uses the twisted traces Z_n(b,g) for the sector moments I_n, O_n, N_n; the final purities are of the full Z_n. **HOLDS.**
- (1b) Grover squaring identity 1-P' = 2 sum_{i<j}(w_i w_j)^2/P^2 <= (1-P)^2/(2P^2) = f(1-P): OpenAI Lemma "Squaring probabilities" proves it; Grover eq. (3) restates it. Cross-direction identity S(L,2b)T(L,b)^2 = S(L,b)^2 T(2L,b): both sides equal Z(2L,2b)/Z(L,b)^4. 1D rule (5): u <= 1/100 -> 5u^2, gap > log 20/b0. **HOLDS.**
- (1c) Grover d dimensions: hypothesis (7) per-direction Hermitian transfer, each list independent of its own length at fixed transverse geometry, all allowed sizes and all beta; successive staggered ratios; a = 2^{d+1}-1; u <= 1/(2a^2) -> a^2 u^2; d = 2 values 1/98 and 49; Q = Z(2L,2beta)/Z(L,beta)^{2^{d+1}} is the weighted product with powers 2^d,...,1, so Q >= 1-1/(2a^2) suffices (eq. 14), and conversely Q >= (1-e)^a. Gap > log 2/beta0 on every even l >= L0. **HOLDS.** (Grover writes out the update only for d = 2, Appendix A.2; for d >= 3 he states it in one paragraph. The row's own d = 3 port in §2 is checked separately below.)
- (1d) Sector caveat and Ising example (§IV.1): projected untwisted classical Ising trace (A^L + B^L)/2 with A = 2cosh(bJ), B = 2sinh(bJ); ratio 2(A^{2L}+B^{2L})/(A^L+B^L)^2 > 1 iff (A^L - B^L)^2 > 0: rechecked by hand. Z_k of eq. (16), the two hypotheses (Hermitian A_0, A_1 independent of L with Z_k = Tr A_0^L + k Tr A_1^L; untwisted lowest energy no higher than twisted in each sector), the plus-sector spatial purity of A_0 (+) A_1, the signed minus sum, both time ratios genuine purities, 0.99 tests, eq. (19) splitting (12/(5 b0)) e^{-(log 20) l/(2 L0)} and gap > log 8/b0. General finite Abelian group: Appendix B.3 in one dimension; Grover only "expects" higher dimensions. The row says "in one spatial dimension". **HOLDS.**
- (1e) Lu: reflection-positive form (S71) (real basis, real symmetric involution F, o = o^T with FoF = o, -h = sum C_a (x) F C_a F with C_a real symmetric or antisymmetric), Gram transfer F^T F >= 0 at finite Trotter number M, Trotter limit at fixed (L, beta) before doubling (Sec. SI.C); asymmetric rational update in the order p' then q'; certificate (S83): r^{2^j} z_j < 1 - z_j for j < J, p_J, q_J <= eps <= 1/100, 5 eps r^{2^J} <= 1; seed (36, 49/4) with 47916/10^6, 181521/10^6; six steps to (2304, 784); 0.0729 for even L >= 36 (lifted seed); Lean: mixed-field Ising seed kernel-checked, spin-1 ring leaves short-ring trace totals 5 <= n <= 12 as hypotheses. All match the row. **HOLDS.**

### Step 2. Crossing of Z_+ and the three completions (row §2, first part). Sources: library/gap-flux-exercise.md §§3.1, 8.3-8.5; Lemma W, Theorem S-w, Proposition X16, Corollary SR.

- (2a) Z_+(a;b,c,d) = (1/4) Tr A^b over the sixteen sectors X: this is (*) of Proposition X16 word for word (one old temporal bit stays electric, two become magnetic; the electric sum inserts 2 x (1+C)/2, so 1/8 becomes 1/4). Hence the rotated ratio is 4 Tr A^{2b}/(Tr A^b)^2 <= 4, and a rescaled 4 Z_+ has time purity <= 1/4: rechecked. Sum rule 3 Z_{0,0} at a = b: Corollary SR. **HOLDS.**
- (2b) W_per = sum_chi Z_{chi,0} (= Z), W_full = sum_m Z_{0,m} = (1/8) sum_k Z^k, W_kappa = sum_m Z_{m,m} = (1/8) sum_k (-1)^{Pf(k)} Z^k: the sector sets of Proposition CL. Positive direct-sum trace in every frame (Lemma W (a), (b)); periodic vacuum present and dominant (Lemma W (c)); extra copies of the top counted in S_w (definition in Theorem S-w). **HOLDS.**

### Step 3. Port of Grover's d = 3 update to W (row §2, "Grover's update"). Checked by hand.

- Telescoping Q = W(2x)/W(x)^16 = R_1^8 R_2^4 R_3^2 R_4 on the four staggered boxes: rechecked. h = 15, threshold 1/(2h^2) = 1/450, a^2 = 225.
- Update. Reorder so that the direction to improve is doubled last; Q is order independent, the three earlier factors are <= 1 (Lemma W: genuine purities), so the last ratio >= Q >= (1-e)^15 >= 1-15e; one more squaring along that direction at fixed transverse box gives defect <= f(15e) <= 225 e^2 for e <= 1/450 ((1-15e)^2 >= (29/30)^2 > 1/2). I wrote out the four cycles: base boxes x, D_x x, D_y D_x x, D_z D_y D_x x; the last boxes are (L,2L,2L,2t), (4L,L,2L,2t), (4L,4L,L,2t), (4L,4L,4L,t); after squaring they are exactly the four test boxes at 2x. Each later cycle uses old ratios and improved ones, all <= e since 225 e <= 1. e_j = (225 e_0)^{2^j}/225 <= 2^{-2^j}/225. **HOLDS.**
- Intermediate cubes. W(B^3, t_j) <= W(x_j)^{(B/L_j)^3} and W(B^3, 2t_j) >= W(2x_j)^{(B/2L_j)^3} (moment inequality applied one direction at a time, transverse sides fixed at each step); since 2(B/L_j)^3 = 16 (B/2L_j)^3 the time purity is >= Q_j^{(B/2L_j)^3} >= Q_j >= (1-e_j)^15. Top weight > 1/2, so simple; ratio <= 15e_j/(1-15e_j) <= (2/29) 2^{-2^j} < 2^{-2^j}; gap > log 2/t. **HOLDS.**
- Minor: the row states the port for even L, t >= 4. For W all transfers are positive (Lemma W (b)), so the moment inequalities and the squaring need no evenness; sides >= 3 suffice. The later use at x = (N,N,N,N), N >= 3 arbitrary, is covered by this remark. **HOLDS AFTER CORRECTION** (correction: replace "even L, t >= 4" by "integer L, t >= 3", justified by positivity of T^w; nothing else changes).

### Step 4. Q = exp(-Phi_W(N)), the relaxed bound and the separating model.

- Q at x = (N,N,N,N) equals W((2N)^4)/W(N^4)^16 = exp(-Phi_w(N)) with Phi_w as defined in Theorem S-w (gap-flux-exercise.md §8.4); the periodic case is Phi of gap-crux-restate.md (F = log Z, Theorem D). The printed S-w sufficient bound 1.9 x 10^-4 and Theorem D (b) form 1 + S_w <= exp(Phi_w) are in Theorem S-w. The 1/1650 shape threshold is the r = 2 line "first b -> 2b, then r = 4" of gap-seed-shape.md §1.5 (rate constant 1479). Its use for W rests on Lemmas E2/B3/SH holding for W_w; their inputs (A), (K), (X), (T) hold for W_w by Lemma W and Theorem S-w, and B3 for W_w is already used in check 1527 (ii) and check of row 1161 S11. Grover's gate is Phi_W <= log(450/449) = log(1+1/449). **HOLDS** (as a comparison of two sufficient numerical gates on one observable; the conclusions differ: gap > log 2/N against log(1/(5041 s))/N).
- Model W(x) = 1 + q^{V(x)}: in direction i the transfer is diag(1, q^{V/x_i}), positive, independent of x_i. y = 1/16000: Q = (1+y^16)/(1+y)^16; lower bound (1+y)^-16 >= 1-16y = 999/1000 > 449/450; upper bound (1+y)/(1+16y) = 16001/16016 = 1 - 15/16016 < 1 - 1/1651 = 1650/1651, so Phi_W > log(1+1/1650) > 1.9 x 10^-4. Rechecked. Note (true, and the row says so): in this model the actual seed s(N) = y^8 is tiny; the model separates the Phi gates only, not the seeds. **HOLDS.**

### Step 5. Equivalence of the four-ratio criterion and Theorem S-w after a bounded change of side.

- Theorem S recursion s(2N) <= ((1+s)^64 - 1)^2 <= 5041 s^2 for s <= 1/640 (gap-crux-restate.md 3.4, line 203: (1+x)^64 - 1 <= 71x); dyadic bound and rate; Corollary S3' for all sides >= 2N. Lean: `wilson_theoremS` in lean/gapchain/GapChain/Assembly.lean is stated for the periodic torusData, beta > 0, N >= 3, seed < 1/5041; RECEIPT-1f.md lists only [propext, Classical.choice, Quot.sound]. I read the statement and receipt; I did not rerun Lean. **HOLDS.**
- Forward. Four ratios >= 449/450 at (N,N,N,N): e_3 <= (1/2)^8/225 = 1/57600. At x_3 = (8N)^4 the time ratio is the time purity at time 8N on (16N)^3; top weight w_0 >= 1 - e_3 and it is lambda_0 (Lemma W (c)); s(8N) = (1-w_0)/w_0 <= e_3/(1-e_3) = 1/57599 < 1/5041. Also from Q >= 449/450 (Q <= every R_i). **HOLDS.**
- Converse. s = s(N) < 1/5041, N >= 3. The four tests at (2N)^4: in the frame of the direction being doubled, time 2N, transverse boxes (2N)^3, (4N,2N,2N), (4N,4N,2N), (4N)^3. B3 with p = q = 1, a = N, base (2N)^3: beta_i = 2, Pi = 8, volume ratio <= 8, so g(N;H) <= 64 log(1+s), i.e. 1 + s_W(N;H) <= (1+s)^64 (qa = N < 2N, a >= 3: hypotheses met). (T): s_W(2N;H) <= ((1+s)^64 - 1)^2 <= (71 s)^2 < (71/5041)^2 = 1/5041. Purity >= (1+v)^-2 >= 1 - 2v since W(4N) >= lambda_0^{4N}. Defects < 2/5041 < 1/1800 <= 1/450. One round: 225/1800^2 = 1/14400; Q at (4N)^4 >= (1 - 1/14400)^15 >= 1 - 15/14400 = 1 - 1/960 > 449/450. All constants rechecked. B3 for W_w: see Step 4. **HOLDS.**
- Remark on W_per (two torus integrals) and W_kappa (64 twists): correct by the definitions. **HOLDS.**

### Step 6. Comparison with (PUR-io).

- (6a) Same box. Grover's x = (n/2,n/2,n/2,u): R_4 is the time purity at time u on n^3. R_4 >= 449/450 gives w_0 >= 449/450, s_W(u;n^3) <= 1/449; s_+ <= s_W because (0;0) is in every Sigma and all terms are >= 0 (Corollary EV); P_+ >= (1+s_+)^-2 >= (449/450)^2 > 457/625. Spectrum (1, 4/21): P = (457/441)/(625/441) = 457/625 exactly. **HOLDS.**
- (6b) Aspect transfer. W(y) <= W(x_j)^{V(y)/V(x_j)}, W(D_i y) >= W(2^h x_j)^{V(D_i y)/V(2^h x_j)}, V(2^h x_j) = 16^h V(x_j): gives the bracket to the power 2V(y)/V(2^h x_j) <= 1; telescoping into prod_k Q(x_{j+k})^{16^{h-1-k}}; exponent sum 15 (16^h - 1)/15 = 16^h - 1. Choice of c in 1024N (needs upper bounds on L_K/b^K, t_K/b^K), of h independent of K and j (needs lower bounds), of j uniform in K (e_j does not depend on K). P_+(n', n'/512) >= R_t(y)^2 since 1 + s_W = 1/w_0 and w_0 >= R_t. l' = 2^j c in 1024N, n'/512 even. All rechecked. **HOLDS AFTER CORRECTION.** First imprecise line: "Suppose on an infinite set of original cutoffs the four tests hold". Correction: "on an infinite set of passing original least-root cutoffs, at the calibrated coupling beta_K, with L_K, t_K integers >= 3"; PUR-io's quantifier is over passing cutoffs, and the conclusion "on the same cutoffs" needs this.
- (6c) Which completion is equivalent. Row 1161 (library/gap-solve9-astra62.md lines 215-227): hypotheses 4 | n, n >= 2^70, s(u) <= 1/2 for an integer 3 <= u <= n/512, with s(u) = X_{0,0}(u) - 1 the periodic neutral excited sum; conclusion on (n/2; n^3): S_per < 2^-19, or S_full < 2^-18; S_kappa < 2^-18 in both cases. The floor 1/10 only selects branch I; it is not a hypothesis of the S_kappa conclusion. Its check (library/gap-solve9-check-opus.md, S12) recomputes every constant and ends HOLDS. Fact PUR (457/625 -> s_+ <= 4/21 <= 1/2) and l in 1024N give 4 | n; n >= 2^70 holds eventually. 2^-18 < 1/5041, so Step 5 converse gives the Pfaffian four tests at n^4 at every cutoff where PUR-io passes; pigeonhole gives one of W_per, W_full on an infinite subset; (6b) gives PUR-io back from each. So over the allowed sides and infinitely many depths: Pfaffian test <=> PUR-io, and (periodic test) or (full test) <=> PUR-io. **HOLDS.**
- (6d) Frozen Z_2: flat untwisted mass 2^{V+3}/2^{4V} = 8 x 2^-3V (matches gap-solve10-astra62.md (29)); twisted flat mass 0 (plane cocycle not a coboundary); neutral mass 2^-3V; W_per purities 8/64 = 1/8, neutral time purity 1. Zero coupling: Z^k = 1 for all 64 twists, W_full = 8, purities 1/8, neutral purity 1 (and W_per purity 1, consistent with the disjunction). Continuity at finitely many boxes (finite sums for Z_2; Haar integrals at small beta for SU(2)). These refute "PUR-io => specified periodic test" (Z_2 class, structural) and "PUR-io => specified full test" (SU(2) at beta = 0), not anything on the calibrated SU(2) trajectory; the row says this. **HOLDS.**
- (6e) Lower thresholds. P = (1 + sum x^2)/(1+s)^2 <= 1/(1+s) forces s < 1; (1+s^2)/(1+s)^2 = 1/2 + (1-s)^2/(2(1+s)^2) gives s <= (1 - sqrt(2 eps))/(1 + sqrt(2 eps)); equality at one excited weight. 457/625: sqrt(2 eps) = 17/25, s <= 4/21. 5/9: sqrt(2 eps) = 1/3, s <= 1/2. So 5/9 at u = n/512 meets the s <= 1/2 hypothesis of row 1161: **HOLDS.** Against check 1527 (ii) (library/gap-agy-seed-approaches-neon-check-astra62.md lines 47-55; row 1368 lines 22-23): n/34 for s_0 = 4/21 and n/60 for s_0 = 1/2, general A = 2 ceil(log 10^6 / log(1 + sqrt(2 eps))), l in 4A N, one infinite set of passing original cutoffs, recovery of the shorter-time test on an enlarged box: the row reports these correctly. Purity is non-decreasing in time (d/du log P = 2(<E>_u - <E>_{2u}) >= 0 with E = -log(lambda/lambda_0)), so a bound at n/60 is a weaker hypothesis than at n/512, and the row's 5/9 at n/512 is a special case already covered by 1527 (ii) plus row 1161, not a new threshold. Example (2/21, 2/21): P = (449/441)/(625/441) = 449/625 < 457/625. Rate m_phys >= (2/l) log(2^18/5041): matches 1527 (ii) with l the side used. **HOLDS.**

### Step 7. Search claim (row §3).

grep over library/ and FINISH.md for Grover, 449/450, "rotated purity", "spatial purity" finds only row 1577's literature note (library/prior/gap-band-neutral-lit-luna.md), FINISH.md queue text, and the row itself. No earlier lane text derives the staggered four-ratio update with 225 or the 449/450 test. The four-cube defect Phi, the crossing loss of Z_+ (X16/EVL) and the three completions predate it, as the row says. Main's PXP note (docs/PERIODIC_PXP_AND_STAGGERED_LINK_RING_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-10-07.md at 8b11ae2bb) has the one-dimensional two-purity bootstrap, as the row says. **HOLDS** (the derivation is new to the lane; its content is equivalent to Theorem S-w, Step 5).

### Step 8. Equivalent is not progress: is anything strictly weaker than (PUR-io)?

No. Item by item:
- Grover's Q gate on W at one cube is a weaker numerical gate than the printed S-w gate Phi_W <= 1.9 x 10^-4, but the four-ratio criterion is equivalent to the S-w seed after a bounded change of side (Step 5), and the Pfaffian version is equivalent to PUR-io over the allowed sides and infinitely many cutoffs (6c).
- 5/9 at u = n/512 is weaker than 457/625 at the same box (one excited weight 1/2 has P = 5/9 < 457/625), but over the allowed sides it implies PUR-io (Fact-PUR algebra, row 1161, Step 5 converse, 6b) and is implied by it: equivalent. Check 1527 (ii) already holds the weaker longer-time variants, also equivalent.
- The specified periodic or full tests are stronger than PUR-io (6d).
The row's own RESULT ("The Wilson seed remains open") agrees.

## Verdicts

Provenance: Claude Opus 5.5, laptop subagent, by hand; lane checkout as found 2026-11-26; primary texts OpenAI at adc7f1241b42, Grover v1 html, Lu v1 pdf; not an audit. Lean not rerun.

| Part | Verdict |
|---|---|
| OpenAI proposition, hypotheses, seeds, transfer | HOLDS |
| Grover squaring, 1D rule, d-dim staggered rule, Q test | HOLDS |
| Grover sector caveat and Ising example | HOLDS |
| Lu RP form, asymmetric recurrence, certificate, Lean scope | HOLDS |
| Crossing of Z_+ (factor 4, cap 1/4, sum rule) | HOLDS |
| Three completions as positive traces in every frame | HOLDS |
| d = 3 port (225, 449/450, intermediate cubes, gap log 2/t) | HOLDS AFTER CORRECTION (evenness unnecessary; integer sides >= 3) |
| Q = exp(-Phi_W(N)); relaxed gate log(450/449); 1/1650 | HOLDS |
| Separating model 1 + q^V | HOLDS |
| Four-ratio <=> S-w (57600, 5041, 1800, 14400, B3) | HOLDS |
| Same-box comparison, P_+ >= (449/450)^2; (1, 4/21) | HOLDS |
| Aspect transfer to literal PUR-io | HOLDS AFTER CORRECTION (quantify over passing original least-root cutoffs) |
| Pfaffian test <=> PUR-io; periodic-or-full <=> PUR-io | HOLDS |
| Frozen Z_2 and zero-coupling counterexamples | HOLDS (structural; not on the trajectory, as stated) |
| Lower thresholds; 5/9 at n/512; vs check 1527 (ii) | HOLDS (not new: covered by 1527 (ii) Theorem 2(1) and row 1161) |
| Search claim (staggered update new to lane) | HOLDS |
| Anything strictly weaker than PUR-io | No: each candidate is equivalent over the allowed sides and cutoffs |

RESULT — Row 1592 holds: every positive statement checks (two wording corrections: the d = 3 port needs no evenness, and the aspect transfer must quantify over passing original least-root cutoffs); the Pfaffian four-purity test and the periodic-or-full disjunction are each equivalent to (PUR-io) over the allowed sides and cutoffs, 5/9 at n/512 is also equivalent, so under "Equivalent is not progress" the row gives no progress; the staggered update is new to the lane only as a derivation; the Wilson seed remains open.
Checked line by line by Claude (Opus 5.5).
