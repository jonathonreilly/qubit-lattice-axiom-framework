# Check of row 1367: gap-seed-astra62.md (FINISH row 1369)

Checker: Claude Opus 5.5, by hand, line by line.

Status: complete. Verdicts are in Section 10; the RESULT line is last.

## Reading record

Pinned at the lane head after `git pull --ff-only` (`1f82019e7`). Read in full: `library/gap-seed-astra62.md` (248 lines), `GOAL.md`, the FINISH rows 1367 and 1369. Read in the cited ranges: row 1161 `gap-solve9-astra62.md` L1-112 (setup, (3)-(7)), L111-151 ((8)-(10), the line-150 enlargement), L213-311 ((17)-(20), (19), its range), L341-421; row 1162 `gap-solve9-check-opus.md` S20-S27; row 1356 `gap-mini-mneutral-fable.md` Sections 1-2 (M1, M2); row 1355 `gap-mini-neutral-step-check-astra.md` in full; row 1359 `gap-mini-mneutral-check-astra.md` (M1, M2, JF lines); row 667 `gap-transfer.md` N.1-N.8, Lemmas A0-A3, Sections 1-4, 9.3; row 1155 `gap-solve7-astra62.md` L410-512 ((29)-(34) and the projected pair law); row 1169 `gap-solve13-astra62.md` L205-266 ((15)-(18), the kernels); row 1165 `gap-solve11-astra62.md` L40-77 ((3)-(5)) and L281-324 ((19)-(21)); row 1163 `gap-solve10-astra62.md` L125-157 ((11)-(12)); row 1283 `gap-solve32-astra62.md` L346-401 ((29)-(32)) and L236 (Haar-ball cutoff); GC2 header in `gap-crux-exercise-astra.md` L1276-1299; row 1204 `gap-solve21-astra62.md` L11-15, L236-260; row 1339 `gap-solve45-astra62.md` L96-113. The file `library/gap-agy-seed-neon.md` was not opened.

Method: every inequality below was re-derived by hand. A small guide run (Section 8) evaluated a few of the same identities numerically; it is not a proof step.

## 1. Row 1161 (19) and consequence (1), lines 21-27

**S1 (L21-24). HOLDS.** Row 1161 (19) (its L267-271, L308; checked as S25 in row 1162) gives, for absolute c, C, every n with 4 | n large enough and every beta >= 1, at least (1/2) binom(M,k) excited neutral levels with -log(lambda_i/lambda_0) <= Ck, M >= c n^3. Its k = 1 case is at least M/2 >= (c/2) n^3 excited levels with -log(lambda_i/lambda_0) <= C. Row 1161 defines s(v) = X_{0,0}(v) - 1, the vacuum-normalized trace of the periodic (m = 0) transfer in the electric character q = 0 (its L48). This is exactly s_{n,beta} of L11 (zero spatial twist, range of P_0). Each such level contributes at least e^{-2Cw} to s(2w), so s(2w) >= (c/2) n^3 e^{-2Cw}; renaming c/2 as c gives (1). Row 1161 already states this inequality at its L271 ("s(u) >= c n^3 e^{-Cu}").

**S2 (L27, the volume quantifier). HOLDS.** At a fixed late cutoff j with beta_j >= 1, a proposed physical time W gives the fixed lattice time w = W/a_j. Then c n^3 e^{-2Cw} > 4/21 exactly when n^3 > [4/(21c)] e^{2Cw}. Dyadic enlargement keeps 4 | n and n >= 2^70, keeps beta_j fixed, and keeps beta_j <= B_0 log n because log n grows. The constants of (19) do not depend on beta >= 1, so the enlarged cube fails the test. No fixed time therefore serves all volumes at one cutoff. The two disclaimers also hold. At fixed physical side the bound is c (L/a_j)^3 e^{-2C floor(n_j/1024)}, which tends to zero because the exponent is linear in n_j, so (1) says nothing about the one-cube statement. Nothing is said about a volume-dependent cutoff floor.

Restatement: S1 restates row 1161 L271 and S2 is its immediate quantifier consequence. The note says so ("The underlying level count belongs to row 1161"). The FINISH lead note for row 1367 records the same reading.

## 2. The one-cube statement and the test time, lines 11-13

**S3 (L11, the reading of (M-neutral)). HOLDS.** Row 1356 Section 2 (its L83-84) states (M-neutral): an admissible L and, for all late j, an integer w_j <= n_j/1024, a unit phi_j and c_j > 0 with HS distance at most 2/5 from P_0 T_j^{w_j}/c_j to the rank-one projection. Lemma M1 and Corollary M2(i) (row 1356 L86-109, checked by row 1359 L15-17) make this equivalent at each w to s(2w) <= 4/21. Each x_a = lambda_a/lambda_0 lies in [0,1], so s(2w) does not increase with w. Hence some w <= n_j/1024 passes exactly when w_j = floor(n_j/1024) passes. Since n_j a_j = L, a_j floor(n_j/1024) lies in (L/1024 - a_j, L/1024] and tends to L/1024. The side conditions (4 | n_j, n_j >= 2^70) are those inherited by row 1359 L17. The coupling range beta_0 <= beta_j <= B_0 log n_j is the lead note after Theorem ZD-c (`gap-phys-seed.md` L322). The simple top eigenvalue lambda_0 > lambda_1 is row 667 (4b) with the sector split of row 667 9.3.

**S4 (L13, the prior implications). HOLDS, as a summary of checked rows.** (a) M1 arithmetic: s/(1+s) <= (2/5)^2 = 4/25 is 21 s <= 4. (b) Row 1355 L51 records "a factor four of slack" between the two BT2 time caps on the same box, and L55 the repair by Wilson shape propagation for existence on some side. Remark: row 1356 M2(ii) (row 1359 L17: w = ceil(3u/2)) already reduces the same-box loss to at most threefold (up to one step of rounding), so "can increase fourfold" is a valid but loose bound. (c) The gap-clause consumer and its premises match row 1349's RESULT ("Either branch supplies (G_ev-phys), which suffices for the matched gap clause") and its premise list ((H2), (TOT), (P4) at row 1349 L29 and L102).

Restatement: S3 and S4 restate rows 1356, 1355, 1359 and 1349, with attribution.

## 3. The spatial-translate Gram bound and inequality (2), lines 31-59

**S5 (L31, transfer used). HOLDS.** Row 667 Sections 1-4 give the gauge-projected transfer T_P = T P with real symmetric continuous kernel bounded below by e^{-12 beta N^3}, positivity (2c), trace class (3), the trace identity with slice insertions (1c), and the simple positive gauge-invariant vacuum (4b)-(4d). Section 9.3 gives the three sheet flips Z_k commuting with T_P and fixing Omega. Remark: row 667 is written for the cubic slice (Z/N)^3. The proofs of (1)-(4) use no equality of sides, so they apply verbatim to the slice (Z/n)^2 x (Z/m) of the direction-1 transfer used at L35. This holds for m >= 3, and m tends to infinity here.

**S6 (L33). HOLDS.** Each 23-plaquette has 0 or 2 links flipped by any sheet flip, so W_i commutes with the flips. Omega is flip invariant by simplicity (row 667 9.3). Hence v_i = D_i Omega is gauge invariant and centre neutral. Translations commute with T_P and fix the simple positive vacuum, so <Omega, W_i Omega> does not depend on i, and v_i is orthogonal to Omega. Next, g = int (W_0 - W_1)^2 Omega^2 <= 4 since |D_0| <= 2 and ||Omega|| = 1. Also g > 0, because Omega >= e^{-12 beta n^3} > 0 (row 667 (4c)) and W_0 - W_1 is continuous and nonzero at some configuration (trace 1 on p_0, trace -1 on p_1).

**S7 (L35-42, convexity). HOLDS.** With direction 1 as transfer direction, the slice x_1 = c contains the links of directions 0, 2, 3 at x_1 = c. The 23-plaquette at x_1 = c lies in it, and row 667 (1c) gives C_m(d) = Tr(S^{n-d} W S^d W)/Tr S^n for 0 <= d <= n. The case d = 0 is (1c) with t_1 = t_2; the case d = n equals d = 0. S >= 0 is trace class, and W is a bounded real multiplier. In an orthonormal eigenbasis the numerator is sum alpha^{n-d} gamma^d |W_{alpha gamma}|^2, a sum of nonnegative terms. Re-derived second difference: f(d-1) + f(d+1) - 2 f(d) = alpha^{n-d-1} gamma^{d-1} (alpha - gamma)^2 >= 0 for f(d) = alpha^{n-d} gamma^d and 1 <= d <= n-1. I also checked the kernel cases gamma = 0 or alpha = 0 with 0^0 = 1, for example alpha^n at d = 1 when gamma = 0. The three series have nonnegative terms and finite sums, so termwise subtraction is legitimate. In the direction-0 frame, E_m[W_0 W_d] = Tr(M_{W_0 W_d} T_P^m)/Tr T_P^m. Its distance from <Omega, W_0 W_d Omega> is at most ||W_0 W_d||_inf times 2 s_full(m), where s_full is the excited sum over all sectors; this tends to zero as m grows, by simplicity and trace class. Convexity in d therefore survives the limit.

**S8 (L44-48, Gram matrix). HOLDS.** C(d) = <Omega, W_0 W_d Omega> is n-periodic and even in d, by translation invariance and commutativity of multipliers. Expanding gives G_ij = 2C(d) - C(d-1) - C(d+1) with d = j - i mod n. This equals g at d = 0 and is <= 0 for 1 <= d <= n-1 by S7. Telescoping around the period gives sum_i D_i = 0, so each row sums to zero and the absolute row sum is g + g = 2g. For V: C^n -> H with V e_i = v_i one has V^*V = G and VV^* = sum_i |v_i><v_i|. Then ||VV^*|| = ||G|| <= max absolute row sum = 2g, and ran V lies in ran P_exc, so VV^* <= 2g P_exc.

**S9 (L50-55, inequality (2)). HOLDS.** R = T_P/lambda_0 commutes with P_0 and with |Omega><Omega|, R^t >= 0, and Tr(R^t P_exc) = s(t). Conjugating S8 by R^{t/2} and tracing gives sum_i <v_i, R^t v_i> <= 2g s(t). Each summand equals <v_0, R^t v_0> by translation invariance, so n <v_0, R^t v_0> <= 2g s(t), which is (2).

**S10 (L57, the cube test and the plane forms). HOLDS.** (a) Since s(2w) <= 4/21 and (2) gives s(2w) >= (n/2) rho, a seed forces rho <= 8/(21n), where rho is the ratio in (2). (b) Every b-th plane. Read "one plane" as the time-zero plane {x_0 = 0, x_1 = c}; only then is F a multiplier on one slice in both transfer frames. Re-derivation: with S^b, the weights (alpha^b)^{k-d}(gamma^b)^{d} have the same nonnegative second difference on {0, ..., k}, k = n/b. Centre invariance of F puts D_i Omega in the neutral sector, and gauge invariance puts it in the physical space. The row sums still vanish by telescoping over the k chosen planes. Hence s(t) >= (k/2) <v_0, R^t v_0>/g whenever g > 0. (c) A ratio above 8/(21k) at t = 2 floor(n/1024) gives s(2w) > 4/21 at w = floor(n/1024). By monotonicity it then fails at every w <= n/1024, so the cube fails at that cutoff. Remark: k >= 3 is harmless but not needed; at k = 2 the bound reduces to the trivial s(t) >= rho.

**S11 (L57, last two sentences, comparison with row 1204). HOLDS AFTER CORRECTION (credit only).** Row 1204 L11-15 does use a spatial difference in a continuum norm. But row 1204 (22)-(23) (its L248-260) also works on the finite periodic cube. It uses the translates f_x psi of one centered 23-plaquette function along axis 1 and resolves them by axial momentum, and the identity before its (6) (L75-86, used again at L197) writes spatial correlations through the direction-1 transfer. Correction: cite row 1204 (22)-(23) as the nearest finite-box antecedent. It bounds the Gram matrix from below (conditional variance) and fixes an energy moment by a sum rule, whereas (2) bounds the Gram matrix from above by reflection-positivity convexity and traces against R^t. No mathematics changes.

**S12 (L59, OPEN). HOLDS.** No lower bound of order 1/n on the normalized plane-difference correlation at time 2 floor(n/1024) is supplied. The level count (19) concerns energies of order one in lattice units.

Restatement: (2) is new as far as I can find. Its Gram step uses an upper bound (convexity), whereas row 1161 (17)-(19) and row 1204 (23) use lower Gram bounds.

## 4. The boundary-link upper test (3)-(7), lines 61-147

**S13 (L63, prior projected law). HOLDS.** Row 1169's kernel paragraph (its L220) defines K_+ = p_{+,s}/sqrt(X_+(2s)), of HS norm one, whose pointwise square is the pair law. Its (15) takes the affinity of that law to the product of marginals after omitting k separated raw links (L209). Row 1155 after (34) (L503-511) uses the square of a projected kernel in the twist-summed ensemble. In Haar coordinates the pair law B(x,y)^2 dx dy of L68 is the same law, since multiplication by Omega is unitary from L^2(Omega^2 dx) onto L^2(dx).

**S14 (L65-72, definitions and realization). HOLDS.** P_0 commutes with T_P and both are positive, so B = P_0 T^w/||P_0 T^w||_HS is positive semidefinite and symmetric. Up to the HS normalization its kernel is (1/8) sum_e A^{(w)}(x, C^e y), a positive average of the strictly positive Wilson kernel, so B > 0 pointwise, and int int B^2 = ||B||_HS^2 = 1. Since B(y,x) = B(x,y), J(x,y) = B(x,y)B(y,x) is the boundary law of a 2w-torus with an independent uniform seam average on each slab. Given (x,y), the two seams have posterior weights proportional to the two slab factors. Tr B^2 = 1 normalizes Z_+(2w) = lambda_0^{2w}(1 + s(2w)) in either flux alternative.

**S15 (L74-81, the affinity bounds (3)). HOLDS.** The eigenvalues of P_0 T^w are lambda_a^w on the neutral sector, and ||P_0 T^w||_HS^2 = lambda_0^{2w}(1 + s(2w)); hence sigma = (1 + s(2w))^{-1/2}. B >= 0 pointwise gives sqrt(J Q) = B(x,y) sqrt(l(x)) sqrt(l(y)), so A = <sqrt l, B sqrt l>, with ||sqrt l||_2^2 = int l = 1 and A <= sigma. For the lower bound: B Omega = sigma Omega and Omega >= 0; Cauchy-Schwarz in y gives sigma Omega(x) <= l(x)^{1/2}, so <sqrt l, Omega> >= sigma. B minus sigma |Omega><Omega| is positive semidefinite, so A >= sigma <sqrt l, Omega>^2 >= sigma^3. Consequences: D <= 1 - tau gives sigma >= A >= tau, i.e. 1 + s <= 25/21 and s <= 4/21. Conversely s <= 4/21 gives sigma >= tau and D <= 1 - tau^3. Restatement: the upper half is the square-root-marginal trial vector of row 1165 (3) (L49-52) and (19). The lower half sigma^3 <= A has no antecedent that I found.

**S16 (L83-90, the exact sum of losses (4)). HOLDS.** Put A_i = int sqrt(J_{<i} Q_{<i}). Both x-marginals equal l, so A_1 = int l = 1, and A_{N+1} = A with N = 3n^3. Factoring J_{<i+1} = J_{<i} p_i and Q_{<i+1} = Q_{<i} q_i gives A_i - A_{i+1} = int d gamma_i int [(p+q)/2 - sqrt(pq)] = (1/2) int d gamma_i int (sqrt p - sqrt q)^2. The sum telescopes to 1 - A = D, and int d gamma_i = A_i <= 1. All densities are strictly positive, so the conditionals are defined everywhere. The sentence on row 1283 matches its (29)-(32): two-sided information of order (N/k)^3 at k <= beta^delta, 0 < delta < 1/48, a time of vanishing physical duration (its L350, L398-401).

**S17 (L92, the tree terms). HOLDS.** The kernel A_T is invariant under separate gauge transformations of each argument (row 667 (1a)), and l is gauge invariant. So, given x, the J-law and the Q-law of y are invariant under the vertex gauges acting on y. For any fixed y, the tree links of h.y under Haar h have product Haar law: integrate the frame at a leaf, which appears in one tree link only, then remove that leaf. A gauge-invariant law is the average of its h-images. Hence, given x and earlier tree links, each tree link is exactly Haar under both J and Q, and p_i = q_i = 1. The count of the remaining links is 3n^3 - (n^3 - 1) = 2n^3 + 1.

**S18 (L94-101, one-link conditional mixtures). HOLDS.** A spatial link at the gluing slice lies in 4 spatial plaquettes and 2 temporal plaquettes. After gluing, the two half-weights e^{beta A(y)/2} add to the full weight. Each plaquette term beta eta_p (1/2) tr(...) is beta eta_p a_p . v with |a_p| = 1, including signs from a flipped seam. So, given every other variable of the contributing torus (other links, temporal links, interiors, seams), the link has density g_h with |h| <= 6 beta, and Z(h) >= 1 by Jensen. Disintegration gives p_i (J-torus, x observed) and q_i (an independent torus for y; x is independent of y under Q) as mixtures of such g_h, for every history. The cited outline lines are in the index: chunk-01 L50 (427-434, the DLR specification) and chunk-02 L113 (2475-2498, GL14).

**S19 (L103-121, the degree bound (5)). HOLDS.** With u = s + h.v in [0, 12 beta] and s = |h| <= 6 beta, one has g_h(v) = Z^{-1} e^{-s} e^u. The omitted part of the degree-d Taylor sum is g_h(v) P(Poisson(u) >= d+1). The Chernoff bound with e^theta = (d+1)/u is (eu/(d+1))^{d+1} e^{-u}. It is at most 2^{-(d+1)} since d+1 >= 24 e beta >= 2 e u. Also g_h <= e^{6 beta}/Z <= e^{6 beta}, and 2^{-(d+1)} <= e^{-6 beta} n^{-5} by the second condition on d. So the sup error is at most n^{-5}. Mixing polynomials of degree <= d stays in that space, and best L^2 approximation on a probability space gives (5). The Poisson-tail device is row 1163 (11) (its L129, L144); here it is applied to one conditional link rather than to the whole transfer, as the note says.

**S20 (L123-135, clipping and (6)). HOLDS.** (Pi_d p)_+ is at least as close as Pi_d p to p >= 0 pointwise. Also (sqrt x - sqrt y)^2 <= |x - y|, and ||.||_1 <= ||.||_2 on Haar probability, which gives the display. Write 2D and 2D_d as squared norms of (sqrt p_i - sqrt q_i)_i and of its clipped version in the direct sum of the L^2(d gamma_i dv) over non-tree i. The reverse triangle inequality, applied once for p and once for q, gives |sqrt(2D_d) - sqrt(2D)| <= 2 ((2n^3+1) n^{-5})^{1/2}, using int d gamma_i <= 1 and (5) for every history. The tree terms remain zero because Pi_d 1 = 1.

**S21 (L137, counting). HOLDS.** dim P_k - dim P_{k-2} = binom(k+3,3) - binom(k+1,3) = (k+1)[(k+3)(k+2) - k(k-1)]/6 = (k+1)^2. The restrictions of degree <= d polynomials to S^3 form the direct sum of H_0, ..., H_d, of dimension sum_{k<=d}(k+1)^2, which is O(d^3). At beta <= B_0 log n the least allowed degree is O_{B_0}(log n), giving O_{B_0}((log n)^3) moments per history and link.

**S22 (L139-145, (7) and its converse). HOLDS, given the cited Wilson propagation.** Sufficiency: (6) changes sqrt(2D) by O(1/n), so limsup D_{d_j} < 1 - tau gives D <= 1 - tau eventually, and S15 gives s(2 w_j) <= 4/21. Converse, re-traced. (i) The one-cube seed gives s(u) <= 4/21 < 1/2 at u = 2 floor(n/1024), and 3 <= u <= n/512. (ii) Row 1161 L215 (K = 512) then gives the Pfaffian seed S_kappa < 2^{-18} < 1/5041. (iii) Row 1161 L150 with Theorem S-w, as adapted in row 1355 L55 and checked in row 1162, gives on a large fixed dyadic enlargement an arbitrarily small cutoff limsup of the neutral excess at floor(n/K) for each fixed K. (iv) With K = 2048 one has 2 floor(n/1024) >= floor(n/2048) for large n, and s decreases in time, so s(2w) is small. Then sigma^3 is near one, D <= 1 - sigma^3 is small by (3), and (6) makes D_d small. The enlarged side still satisfies the coupling range. The equivalence is existential in L, as stated.

**S23 (L147, OPEN). HOLDS.** (6) bounds the high-degree tail only. The low coefficients are conditional moments given the opposite face and earlier links, and nothing bounds them.

## 5. The angular-moment reduction and the test of fewer moments, lines 123-137 and 149-188

The reduction itself (only the conditional moments through degree d = O(log n) of each non-tree boundary link matter, up to the error (6)) is S19-S21 above. It HOLDS. This section checks the claim that structural properties alone cannot shrink that degree.

**S24 (L151-158, statement (8)). HOLDS.** The construction in S25-S28 has the listed properties, which I re-derived. Since Pi_{d'} = Pi_{d'} Pi_{d_n} for d' <= d_n, the zero persists at every smaller degree. Every o(log n) sequence of degrees therefore also gives zero, while s_cmp(2w) -> 1 forces D >= 1 - sigma, which tends to 1 - 2^{-1/2} > 1 - tau.

**S25 (L160-167, the hidden mode). HOLDS.** Multiplier: the character coefficient of e^{s cos theta} on chi_j is (1/pi) int e^{s cos theta}[cos j theta - cos (j+2) theta] = I_j - I_{j+2} = 2(j+1) I_{j+1}/s. Schur orthogonality divides by j+1, and normalizing by the constant mode gives r_j = I_{j+1}/I_1. This agrees with row 1162 S21. Then 2 cos k theta = chi_k - chi_{k-2} from sin((k+1)t) - sin((k-1)t) = 2 cos kt sin t. chi_j = U_j(v_0) has degree j and satisfies (d^2/dtheta^2 + 2 cot theta d/dtheta) chi_j = -j(j+2) chi_j, so it lies in H_j. For k >= 2, int cos^2 k theta dHaar = 1/2, so v_f = epsilon^2/2. f lies in H_k + H_{k-2}, and f^2 - v_f = (epsilon^2/4)(chi_{2k} - chi_{2k-2}). Since k - 2 > d_n, both are orthogonal to degree <= d_n. With k even, theta -> pi - theta fixes cos k theta. ||C^{-1} f||_inf <= (epsilon/2)[(k+1)/r_k + (k-1)/r_{k-2}] <= epsilon k/r_k = k/(2(k+1)) < 1/2. Hence 1 +- f = C(1 +- C^{-1} f) with mixing densities in [1/2, 3/2] of integral one.

**S26 (L169-175, Bessel bounds). HOLDS.** I_j - I_{j+2} = (2(j+1)/s) I_{j+1} gives I_j/I_{j+1} = 2(j+1)/s + I_{j+2}/I_{j+1} <= 1 + 2(j+1)/s. Then 1/r_k = prod_{j=1}^k I_j/I_{j+1} <= exp((2/s) sum_{j=1}^k (j+1)) = exp(k(k+3)/s). The ratio I_{j+2}/I_{j+1} is the mean of t under e^{st}(1-t^2)^{j+1/2}, as in row 1359 L65 with d = j+1, so it lies in (0,1). Here k = (1/2) sqrt(b) log n + O(1) and s_0 = 3 b log n, so 2k(k+3)/s_0 = (1/6) log n + O(1). Then v_f = r_k^2/(8(k+1)^2) >= n^{-1/6 - o(1)}/(8(k+1)^2) >= n^{-1/3}/(8(k+1)^2) eventually.

**S27 (L177-184, the transfer). HOLDS.** The 3n^2 straight loops partition the 3n^3 links. Their holonomies under product Haar are independent and Haar. a_+- are class functions, invariant under inversion and under the central sign (k even). Each sheet flip multiplies only the holonomies of the loops in its direction by -1, so Phi_+- are gauge and centre invariant, and cubic symmetries permute the loops. ||Phi_+-|| = 1. The overlap is h = prod int a_+ a_- = [(1 - v_f)/(1 + v_f)]^M <= e^{-2 M v_f}, because log((1-x)/(1+x)) = -2 artanh x <= -2x. Here 2 M v_f >= (3/4) n^{5/3}/(k+1)^2. The eigenvalues are 1 +- h on Phi_+ +- Phi_-, so s_cmp(2w) = ((1-h)/(1+h))^{2w} >= 1 - 4hw -> 1. The kernel Phi_+(x)Phi_+(y) + Phi_-(x)Phi_-(y) is strictly positive (a_+- >= (1 - epsilon)/sqrt(1 + v_f) > 0) and positive semidefinite.

**S28 (L186-188, conditional laws and the mixture bound). HOLDS.** T^w = sum (G^{w-1})_{ij} |Phi_i><Phi_j| with G = [[1,h],[h,1]] entrywise nonnegative. B(x,y)^2 expands into y-products Phi_+^2, Phi_-^2, Phi_+ Phi_-, which are loop-product laws with per-loop densities a_+^2, a_-^2, (1 - f^2)/(1 - v_f) (normalizers 1, 1, h). The weights are nonnegative given x, and are fixed after integrating x for Q. A link whose loop still has an unrevealed link is exactly Haar in each component (integrating the unrevealed link integrates the loop density to one). At the last link the density is rho(A v B') with A, B' known, and an orthogonal map of R^4 preserves each H_k. Each rho is 1 plus terms in degrees k-2, k, 2k-2, 2k. So Pi_{d_n} p_i = Pi_{d_n} q_i = 1, the clipped densities are 1, and D_{d_n} = 0 in every order. Each rho is proportional to a_i a_j, a product of two positive mixtures of e^{s_0 z.u}, hence a mixture of e^{h.u} with |h| <= 2 s_0 = 6 beta. Isometries preserve |h|, and conditioning and normalizing keep the mixture form. The note correctly states that this is not a Wilson counterexample.

**S29 (L158, comparison with row 1161). HOLDS AFTER CORRECTION (wording).** Row 1161 L404-413 hides a neutral eigenvalue c||k||^2 from any finite family of tests. Its L413 says "The tests and the time can be chosen anew at each cutoff", so its hidden level can also survive a time proportional to n. Correction: what (8) adds is the single-link mixture bound |h| <= 6 beta and exact agreement of all conditional moments through a growing degree in every reveal order, not the length of time. No mathematics changes.

Restatement: the device of modifying a kernel by functions of straight winding loops is row 1161 (21) (L316-321). A neutral level invisible to tests is row 1161 L404-413, with the sign-product comparison at L375. The comparison (8) with its degree statement is new.

## 6. Equations (9) and (10), lines 190-246

**S30 (L192-200, the score identity). HOLDS.** Write omega for all variables of the J-torus other than Y_i. Then p_i(v) = int g_{H(omega)}(v) dP(omega | X, Y_{<i}), and grad_v g_h = g_h h^T with h^T = h - (h.v)v. Differentiation under the integral is allowed since |h| <= 6 beta. Bayes' rule gives grad log p_i(v) = E_J[H_i^T | X, Y_{<i}, Y_i = v]. Under Q, Y has the Y-marginal of J and is independent of X, so q_i is the J-conditional density of Y_i given Y_{<i} with X integrated, and grad log q_i = E_J[H_i^T | Y_{<=i}]. Their difference is Delta_i. Both conditional means are tangent at v because v is in both sigma-fields.

**S31 (L202-207, Poincare step). HOLDS.** Each g_h has sup/inf = e^{2|h|} <= e^{12 beta}, and a mixture keeps this ratio. p <= e^{6 beta} since Z >= 1, and q >= e^{-12 beta} since Z(h) <= e^{|h|}. With phi = sqrt(p/q): E_q phi^2 = 1 and E_q phi = A, so Var_q phi = 1 - A^2. The Haar Poincare constant on unit S^3 is 1/3 (first eigenvalue 3). Then Var_q phi <= (sup q) Var_Haar phi <= (sup q/inf q)(1/3) int |grad phi|^2 q, and |grad phi|^2 q = (1/4) p |grad log(p/q)|^2. This gives the display.

**S32 (L209-217, inequality (9)). HOLDS.** F(u) = 2u^2 log u - u^2 + 1 has F(1) = F'(1) = 0 and F'' = 4 + 4 log u <= 4 + 2 log K for u <= sqrt K. Taylor's formula with integral remainder (F'' <= 4 also on (0,1)) gives r log r - r + 1 <= (2 + log K)(sqrt r - 1)^2 on [0, K]. K = e^{18 beta} bounds p/q. Hence KL(p||q) = int q(r log r - r + 1) <= (2 + 18 beta) int (sqrt p - sqrt q)^2 = (2 + 18 beta) 2(1 - A) <= (2 + 18 beta) 2(1 - A^2) <= (2 + 18 beta)(e^{12 beta}/6) E[|Delta_i|^2 | history]. The chain rule, with equal x-marginals and zero tree terms, sums these. For the first inequality: log(1 + s) = -2 log sigma <= -2 log A by (3), and -log E_J sqrt(Q/J) <= (1/2) D_KL(J||Q) by Jensen. This is row 1165 (3) (L44-54) on the projected law, as credited.

**S33 (L219-225, the local fluctuation). HOLDS.** Delta_i is E[H^T | F_1] minus its projection onto L^2(F_2), with F_2 contained in F_1, so E|Delta_i|^2 <= E|E[H^T | F_1]|^2 <= E|H^T|^2. On S^3, int div(g_h grad(h.v)) = 0, grad g_h = g_h h^T and Laplacian(h.v) = -3 h.v give E_{g_h}|h^T|^2 = 3 E_{g_h}[h.v]. Averaging, E|H_i^T|^2 = 3 E[H_i.Y_i] <= 3 E|H_i| <= 18 beta. The same identity is used in row 1161 L273.

**S34 (L227-244, (10)). HOLDS.** (i) The torus has V = 2w n^3 sites, 4V links and 6V plaquettes. Z(beta) averages over product Haar and both uniform seams, so Z(0) = 1, and its two-slice marginal is J by S14. (ii) Keep the untwisted seam pair (weight 1/64). Restrict every link to geodesic radius beta^{-1/2}; each ball has Haar mass (2/pi) int_0^r sin^2 >= c r^3. A plaquette then has holonomy angle d <= 4 beta^{-1/2}, and 1 - cos d <= d^2/2 <= 8/beta (this holds for every real d, so it is fine even when 4r > pi at beta near 1). This gives -log Z <= log 64 + 48V + 4V log(beta^{3/2}/c). (iii) d/dbeta(-log Z) = E_beta[E] and its derivative is -Var(E) <= 0. Concavity with value 0 at 0 gives beta E[E] <= -log Z(beta). (iv) Equal means: the law of the signed variables (eta_p W_p)_p is unchanged when a sheet is moved one step. To move a temporal sheet one step in time, flip the j-links at x_j = c on the next slice; to move it in x_j, flip the temporal links at x_j = c+1. Each flip preserves Haar and every signed plaquette value. Two independent uniform seams give seam weights proportional to Z_{e+e'}, so the mixture equals the single uniform seam mixture, which is invariant under all translations. Cubic rotations permute the summed labels. (v) sum_i e_i <= 4E because a spatial plaquette has 4 spatial links, a temporal one has 2, and 1 - eta_p W_p >= 0. So 3V E e_i <= 4 E[E]. (vi) H_i.Y_i = beta sum_{p contains i} eta_p W_p = beta(6 - e_i). So E|H_i^T|^2 = 18 beta - 3 beta E e_i >= 18 beta - 4(log 64/V + 48 + 6 log beta + 4 log(1/c)) >= 18 beta - C(1 + log beta) for beta >= 1, with C absolute. The asymptotics along beta_j -> infinity follow.

**S35 (L246, OPEN). HOLDS.** With (9), log(1 + s) <= log(25/21) follows from sum E|Delta_i|^2 <= 6 e^{-12 beta} log(25/21)/(2 + 18 beta), and log(1 + s) <= log(25/21) is s <= 4/21. By (10) the unconditioned substitute exceeds this by a factor of order beta^2 n^3 e^{12 beta}. Remark: at beta = b log n the threshold carries n^{-12b}, so (9) is a very demanding route; the note does not claim otherwise.

Restatement: the first inequality of (9) is row 1165 (3); the Haar-ball lower bound on Z is GC2 and row 1283 L236; the one-link integration by parts is row 1161 L273. All are credited. The per-link chain rule against the whole opposite slice was already used by row 1339 (6) (`gap-solve45-astra62.md` L98-113, entropy chain rule over the links of one slice). The note does not cite it; see S37. The score identity with the S^3 Poincare bound, and (10), have no antecedent that I found.

## 7. Everything else

**S36 (L3, repo pin and registry). HOLDS.** `library/prior/` has no row-specific file for this row (only `gap-seed-lit.md` and `gap-seed-size.md`, which belong to other rows). `library/open-registry.md` has no entry matching M-neutral, N-phys, neutral seed or mass gap. `research/mass-gap/library/gap-flux-exercise-check.md` exists on origin/main at `8b11ae2bb`.

**S37 (L5, the search record). HOLDS AFTER CORRECTION (credit only).** I did not re-run the cross-branch search. The refs listed do not include this lane's branch, and the lane holds two method antecedents that the note does not cite. (a) Row 1339 (6) (`gap-solve45-astra62.md` L98-113) reveals the links of one slice in a fixed order, compares each true one-link conditional with a reference, and sums by the entropy chain rule against the whole opposite slice. This is the per-link chain rule used in (4) and (9). (b) Row 1204 (22)-(23) uses finite-cube translates of a 23-plaquette observable (S11). Correction: add both citations next to (4), (9) and (2). No mathematics changes.

**S38 (L7, closest cross-branch hits). HOLDS at the spot check; the rest was not checked.** PR 10114 at `f76f6c649`, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` (11) (its L162-168), reads v_N^2 exp[-4 beta(p_B+b)]/(1+v_N/r_f(beta)^b), with b = 4 and p_B = 13, hence e^{-68 beta}, for an elementary plaquette. This matches the note. The ZD-c citation on main matches `gap-phys-seed.md` L311 at origin/main. The PR 10133, 10134 and 10141 passages were not re-read; commit `c73ad7b17` is not in this clone.

**S39 (L15, guide). HOLDS** as a description of the note's content and status.

**S40 (L17, published sources). HOLDS as GUIDE, spot-checked against the index only.** The index has 588-599 (chunk-01 L233: polynomial clustering does not give a gap), 3712-3720 (chunk-03 L206), and 31871-31882 (chunk-29 L76: the measure E e^{-E} dE, Laplace transform (1+t)^{-2}, support reaching zero). I did not check the quoted sentence against the primary text.

**S41 (L248, RESULT of the row). HOLDS.** It matches the statements checked above. No step of the cited chain is disproved, and the seed and the gap stay open.

## 8. Guide run (GUIDE only; no verdict above depends on it)

One script in the scratchpad, double-precision numpy/scipy, about 2 s and 100 MB. It found: the multiplier of e^{s z.v} on degree j equals I_{j+1}(s)/I_1(s) (error 2e-16 for j = 0..8 at s = 7.3); r_k >= e^{-k(k+3)/s_0} and ||C^{-1} f||_inf <= 1/2 at (s_0, k) = (3,4), (12,6), (30,10); int cos^2(6 theta) dHaar = 1/2, with cos 6 theta orthogonal to chi_0..chi_3; sigma^3 <= A <= sigma on 200 random positive kernels; the inequality of S32 on (0,K] for K = 3, 1e3, 1e8; the Poisson Chernoff bound; and convexity of Tr(S^{n-d} W S^d W) on 100 random positive semidefinite S. These agree with the hand derivations and prove nothing.

## 9. Restatements of earlier rows

- (1) and the volume consequence restate row 1161 L271 (s(u) >= c n^3 e^{-Cu}) and its range remarks (L263, L310). The note attributes them.
- The reading of the one-cube statement, the 4/21 threshold, the time cap and the consumer restate rows 1356, 1359, 1355 and 1349, with attribution.
- (2): new as far as I found. Nearest antecedents are row 1204 (22)-(23) (finite-cube translates, uncited) and row 1161 (17)-(19) (Gram and min-max).
- (3): the upper half is row 1165 (3)/(19) (credited). The lower half sigma^3 <= A is new.
- (4) is the standard affinity telescoping. The per-link chain rule over one slice against the opposite slice was used in row 1339 (6) (uncited). The tree vanishing is the leaf-integration device also used in row 1283 L503.
- (5) adapts row 1163 (11)-(12) (credited). (6), (7) and the degree count are new as written. The converse of (7) restates the enlargement of rows 1161 L150 and 1355 L55 (credited).
- (8) is new. Its ingredients (winding-loop kernels, a hidden neutral level) are row 1161 (21) and L404-413; see S29 for the wording of the comparison.
- (9): the first inequality is row 1165 (3) (credited); the chain rule as in row 1339 (6); the score identity and the Poincare bound are new.
- (10): the Haar-ball bound is GC2 and row 1283 L236, and the integration by parts is row 1161 L273 (both credited). The equal-mean argument and (10) are new.

## 10. Verdict table

| Id | Statement (lines) | Verdict |
|---|---|---|
| S1 | (19) gives (1) (L21-24) | HOLDS |
| S2 | No fixed time for all volumes at one cutoff (L27) | HOLDS |
| S3 | Reading of (M-neutral), w_j = floor(n_j/1024) (L11) | HOLDS |
| S4 | Prior implications (L13) | HOLDS (fourfold is loose; M2(ii) gives threefold) |
| S5 | Transfer used (L31) | HOLDS |
| S6 | v_i neutral, orthogonal to Omega, 0 < g <= 4 (L33) | HOLDS |
| S7 | Spatial-transfer trace formula and convexity (L35-42) | HOLDS |
| S8 | Gram matrix, row sums, synthesis bound (L44-48) | HOLDS |
| S9 | Inequality (2) (L50-55) | HOLDS |
| S10 | Cube test, plane and every-b-th-plane forms (L57) | HOLDS |
| S11 | Comparison with row 1204 (L57) | HOLDS AFTER CORRECTION (credit) |
| S12 | OPEN (L59) | HOLDS |
| S13 | Prior projected law (L63) | HOLDS |
| S14 | B, J, l, Q and the two-slab realization (L65-72) | HOLDS |
| S15 | (3) (L74-81) | HOLDS |
| S16 | (4) and the row 1283 remark (L83-90) | HOLDS |
| S17 | Tree terms vanish (L92) | HOLDS |
| S18 | One-link mixtures, abs(h) at most 6 beta (L94-101) | HOLDS |
| S19 | (5) (L103-121) | HOLDS |
| S20 | Clipping and (6) (L123-135) | HOLDS |
| S21 | Moment count (L137) | HOLDS |
| S22 | (7) and its converse (L139-145) | HOLDS (given cited propagation) |
| S23 | OPEN (L147) | HOLDS |
| S24 | Statement (8) (L151-158) | HOLDS |
| S25 | Hidden mode (L160-167) | HOLDS |
| S26 | Bessel bounds, v_f (L169-175) | HOLDS |
| S27 | Comparison transfer (L177-184) | HOLDS |
| S28 | Conditional laws, D_{d_n} = 0, mixture bound (L186-188) | HOLDS |
| S29 | Comparison with row 1161 (L158) | HOLDS AFTER CORRECTION (wording) |
| S30 | Score identity (L192-200) | HOLDS |
| S31 | Poincare step (L202-207) | HOLDS |
| S32 | (9) (L209-217) | HOLDS |
| S33 | E abs(H^T)^2 = 3 E[H.Y], at most 18 beta (L219-225) | HOLDS |
| S34 | (10) (L227-244) | HOLDS |
| S35 | OPEN threshold (L246) | HOLDS |
| S36 | Repo pin and registry (L3) | HOLDS |
| S37 | Search record (L5) | HOLDS AFTER CORRECTION (credit) |
| S38 | Cross-branch hits (L7) | HOLDS at the spot check; rest not checked |
| S39 | Guide (L15) | HOLDS |
| S40 | Published sources (L17) | HOLDS as GUIDE, index only |
| S41 | Row RESULT (L248) | HOLDS |

Counts: 41 statements; 38 HOLD (S38 and S40 only spot-checked); 3 HOLD AFTER CORRECTION (S11, S29, S37; credit or wording only, no mathematics changes); none FAILS.

RESULT: Row 1367 checked by hand by Claude Opus 5.5 (FINISH row 1369): 41 statements, 38 HOLD (two GUIDE lines, 7 and 17, only spot-checked), 3 HOLD AFTER CORRECTION (credit or wording only: lines 5 and 57 should cite row 1339 (6) for the per-link chain rule and row 1204 (22)-(23) for finite-cube plaquette translates; line 158 should say that row 1161 also allows a time proportional to n, so what is new in (8) is the single-link mixture bound and the conditional low-degree tests), 0 FAIL; main finding: every positive claim holds as stated, namely (1) from row 1161 (19) (no fixed time serves all volumes at one late cutoff), the one-cube reading at w_j = floor(n_j/1024), the new spatial-translate Gram bound and inequality (2) with its plane and every-b-th-plane forms (via convexity of the spatial-transfer correlation), the boundary-link test (3)-(7) including the new lower bound sigma^3 on the affinity, the comparison (8), and (9)-(10); (1), the first inequality of (9) and the Poisson-tail step of (5) restate rows 1161, 1165 and 1163; the Wilson neutral seed, the low-moment estimate and the mass gap remain OPEN.
