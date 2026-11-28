lead: anthropic/claude-opus-5-5/max laptop-subagent

# Check of row 1304 (`library/gap-positivity-astra62.md`), FINISH row 1308

Checker: Claude Opus 5.5, max effort, laptop subagent. Hand check, line by line.
Target: `library/gap-positivity-astra62.md` (row 1304, written by gpt-6.2-astra max, unchecked before this row).
Comparison: row 1213 Lemma FKG-NO (`library/gap-mini-solve-n-fable.md`) and its check in batched check 1247.

## Counts

- Target: 192 lines, read in full. 34 PROVED paragraphs, 1 OPEN, 9 GUIDE, 1 RESULT line.
- Verdicts on the 34 PROVED statements: 34 HOLDS, 0 HOLDS AFTER CORRECTION, 0 FAILS.
- OPEN paragraph: accurate. RESULT line: accurate. GUIDE: 7 of 9 checked against lane files and accurate. L5 and L11 cite sources outside the lane folder and were not checked.
- Source revision: clone HEAD a084d7b24 on `claude/ym4d-hard-route`. The target is tracked and unmodified there (its own pin line says e1176ef2d).
- Cited lane files read at the cited ranges: 10. That is 8 listed in step 4, plus `gap-mini-solve-ag-opus.md` section 6 and `gap-ws-check-astra.md`, both by grep in step 5. I also grepped `open-registry.md`. Not read: `gap-means-max.md` (row 737) and `prior/repo-search-2026-11-08.md`; no PROVED step depends on them.
- Independent checks by a different route: S34 (tensor networks) against S7 (disk convolution) for (1); a script recount by Lemma PAR on the actual lattice networks (step 6); the U(1) consistency check (step 2).
- Numeric guide: 2 scratch scripts outside the repository, peak 57 MB, guide only.
- Checker's remarks added: 2 (the centre-even state for S15, step 4; the degree-one adjoint pair at beta = 0, step 7). Neither is needed for a verdict.

## Per-statement verdicts (target line numbers)

| No. | Lines | Verdict | | No. | Lines | Verdict |
|---|---|---|---|---|---|---|
| S1 | 15-19 | HOLDS | | S18 | 109-117 | HOLDS |
| S2 | 25-30 | HOLDS | | S19 | 119 | HOLDS |
| S3 | 32 | HOLDS | | S20 | 121-127 | HOLDS |
| S4 | 34 | HOLDS | | S21 | 129-140 | HOLDS |
| S5 | 36 | HOLDS | | S22 | 142 | HOLDS |
| S6 | 38 | HOLDS | | S23 | 144 | HOLDS |
| S7 | 40 | HOLDS | | S24 | 150 | HOLDS |
| S8 | 44-55 | HOLDS (claim 1, adjoint) | | S25 | 152 | HOLDS |
| S9 | 57-69 | HOLDS | | S26 | 154-160 | HOLDS |
| S10 | 71-76 | HOLDS | | S27 | 162 | HOLDS |
| S11 | 78-84 | HOLDS | | S28 | 164 | HOLDS |
| S12 | 86 | HOLDS | | S29 | 166 | HOLDS |
| S13 | 88 | HOLDS | | S30 | 168 | HOLDS (claim 2) |
| S14 | 90 | HOLDS | | S31 | 172-176 | HOLDS |
| S15 | 96-103 | HOLDS (claim 1, fundamental) | | S32 | 178 | HOLDS |
| S16 | 105 | HOLDS | | S33 | 180 | HOLDS |
| S17 | 107 | HOLDS | | S34 | 182 | HOLDS |

The reasons are in steps 2, 3 and 5. The comparison with FKG-NO is in step 4, and the classes ruled out or left open are in step 7.

## Plan (save protocol; each step appends its result below)

1. Read the target in full. List every PROVED statement with line numbers. Record the cited rows.
2. Check the claim 1 proof (adjoint and fundamental plaquette fields violate association at every finite homogeneous coupling, large tori), line by line.
3. Check the claim 2 proof (no boundary orientation makes all mixed neutral slab minors nonnegative at positive coupling), line by line.
4. Read the cited rows where a step depends on them. Compare with row 1213 Lemma FKG-NO and check 1247.
5. Check the remaining statements of the target.
6. Optional numeric guide (under 1 GB, BLAS threads 1, outside the repository, `python3 -E -P`). Guide only.
7. Say which classes of sign-definite objects the results rule out, and which stay open.
8. Write counts, per-statement verdicts, what was not checked, and the RESULT line.

## Step results

### Step 1. Inventory of the target (done)

The target has 192 lines. I read all of them. Labels: 34 PROVED paragraphs, 1 OPEN, 9 GUIDE, 1 RESULT line.
I number the PROVED paragraphs S1 to S34 by line.

| No. | Lines | Label in the target | Content |
|---|---|---|---|
| S1 | 15-19 | PROVED | integral of chi_1(g^2) chi_1(g) is -1 |
| S2 | 25-30 | PROVED | 104 plaquettes P, E_0 prod chi_1 = -3^{-102}, tori of side >= 5 |
| S3 | 32 | PROVED (lattice attachment) | 36-square Moebius band, core C |
| S4 | 34 | PROVED (cap and new disk) | 52-face cap, A = 88 faces, cut disk with word C^2 |
| S5 | 36 | PROVED | D = 16 faces, common links of A and D are the links of C |
| S6 | 38 | PROVED (disk integration) | interior integration gives convolution |
| S7 | 40 | PROVED (evaluation) | chi_1 * chi_1 = chi_1/3, gives (1) |
| S8 | 44-55 | PROVED | (2), adjoint association fails |
| S9 | 57-69 | PROVED (squared-loop Jacobian) | (3), (4) |
| S10 | 71-76 | PROVED (one convolution coefficient) | (5), lambda_n = n/(n+2) |
| S11 | 78-84 | PROVED (the Haar estimate) | (6), bound 294/(n+2) |
| S12 | 86 | PROVED (comparison to the actual measure) | factor K^2, E G >= 1/K |
| S13 | 88 | PROVED (which character inequalities fail) | negative monomial mean and covariance |
| S14 | 90 | PROVED (a response to positive adjoint sources) | negative Cov(Y_p*, Y_p) with sources tY |
| S15 | 96-103 | PROVED (two successive double boundaries) | (7), fundamental association fails |
| S16 | 105 | PROVED (where the second surface fits) | M = punctured second plane plus tube, 99 faces |
| S17 | 107 | PROVED | M meets the first set only in the links of the boundary of p_*; spans 7,4,6,2 |
| S18 | 109-117 | PROVED (the weight contributed by M) | (8), W_t = k_t^{*99} * rho |
| S19 | 119 | PROVED (behaviour at the two roots) | k_t^{*m} concentrates at I |
| S20 | 121-127 | PROVED | (9) |
| S21 | 129-140 | PROVED (evaluation at the marked face) | (10), (11) |
| S22 | 142 | PROVED (finite parameters and homogeneous base law) | choice of t, r; negative covariance |
| S23 | 144 | PROVED (an ordinary Wilson response) | negative trace covariance at nonnegative inhomogeneous couplings |
| S24 | 150 | PROVED (exchange obstruction) | no alternating sign with nonnegative mixed minors |
| S25 | 152 | PROVED (almost-everywhere version) | same, almost everywhere, also two signs |
| S26 | 154-160 | PROVED (strict Gram matrices) | kernel (12) on the neutral orbit space, full support |
| S27 | 162 | PROVED | quadratic form of C strictly positive |
| S28 | 164 | PROVED | Gram matrices of every K_t strictly positive definite |
| S29 | 166 | PROVED (exchange within the neutral quotient) | an exchange path of distinct neutral orbits |
| S30 | 168 | PROVED (scope of the determinant result) | claim 2 for all t >= 1, k >= 2 |
| S31 | 172-176 | PROVED (size of the association failure) | no constant c > 0; no increasing image of an associated law |
| S32 | 178 | PROVED (straight square Wilson loops) | same for l x l loops |
| S33 | 180 | PROVED (second evaluation of (1)) | edge projectors delta/3 and epsilon/6 |
| S34 | 182 | PROVED | vertex factors, monodromy sign, Euler count |

GUIDE lines: 3, 5, 7, 9, 11, 21, 94, 148, 190. OPEN: 184-188. RESULT: 192.

Cited rows and files in the lane: row 1127 (`gap-w-astra62.md`, step 3); row 737 (`gap-means-max.md`, section 2.4); row 1213 (`gap-mini-solve-n-fable.md`, section 4, Lemma PAR, disk gluing, Lemma FKG-NO); row 1247 (`gap-solve-batch4-check-astra.md`, section N); row 1081 (`gap-descent-sign.md`, section 5.1); council note (`gap-council-conf-fable.md`, V1-V4); row 667 (`gap-transfer.md`, N.3-N.7 and sections 1-2); neutral criterion (`gap-mini-neutral2-fable.md`, section 1.1); slab criterion (`gap-mini-solve-ag-opus.md`, section 6); row 1265 check (`gap-ws-check-astra.md`); `prior/gap-lit-assoc.md`; `prior/repo-search-2026-11-08.md`. External sources: the Sussman-Alpoge outline and CA-I on GitHub, and the Alpoge remark. The external sources are outside the lane folder. I do not check them.

Which steps depend on a cited row: S3-S4 restate row 1127 in full, so the check below uses the target's own text and compares it with row 1127. S6 restates the disk identity of row 1213 with its own proof. S33 cites Lemma PAR of row 1213. S26-S27 cite the kernel convention of row 667 and re-prove positivity. No other PROVED step needs a cited row.

### Step 2. Claim 1: association fails for both plaquette fields (S1-S23) (done)

I redid each computation by hand. Line numbers refer to the target.

**S1 (15-19). HOLDS.** At angle theta, chi_1(g^2) = 1 + 2cos 4theta = chi_2 - chi_1 + chi_0. Orthonormality of real characters gives -1. The exterior-square remark is the identity chi_V(g^2) = chi_{S^2V} - chi_{Lambda^2V} with S^2V = spin 2 + spin 0 and Lambda^2V = spin 1.

**S3 (32). HOLDS.** Left half of C_0 has 8 unit edges, fibre WE has 2: 16 squares. Same on the right: 16. Four quadrant squares at v_+ and v_-: 36 in all. I traced the rim: E-side, then N at v_+, then W at v_-, then S at v_+, then E at v_-. So the rim is one circle that covers the base twice, and the fibre end E returns as W. I checked the vertex links at (v_+, o) (a 6-cycle: left[o,E], EN, right[o,N], right[S,o], WS, left[W,o]) and at (v_+, E) (a 4-cycle with the cap). Both are circles, so the band is a surface there.

**S4 (34). HOLDS.** {b} x Q has 4 squares. The four rectangles [b, v_pm] x arc have 4 squares each. The four half-squares have 8 each. Total 4 + 16 + 32 = 52. Each rectangle attaches along one arc of {b} x boundary(Q). Each half-square attaches along the arc [v_-, v_+] x {E}, {W}, {N} or {S}. Each of these is one connected boundary arc made of two rectangle sides. So each attachment keeps a disk. The free boundary is (left half of C_0) x {E, W}, (right half) x {N, S}, and the four outer quadrant arcs. That is exactly the band rim. Cap and band share no vertex with second coordinate o, so the core misses the cap. A = Moebius band plus disk = projective plane with 88 faces. Cut along C, it is a disk with word C^2.

**S5 (36). HOLDS.** D meets the band exactly in C. D meets the cap only in (b, o), because the rectangles and half-squares have second coordinate on boundary(Q). D faces lie at (z,w) = o, the half-squares at E, W, N, S, so the 104 faces are distinct. Spans 4, 4, 2, 2, so side >= 5 gives an injective embedding.

**S6 (38). HOLDS.** The merge step: integrating f(Xu) h(u^{-1}Y) over u with v = Xu gives (f*h)(XY). Euler for a disk gives E_int = V_int + F - 1, so V_int unused interior edges remain. The unused edges contain no cycle and no path between two boundary vertices; both would cut the dual tree. A forest on V_int + V_b vertices with V_int edges has V_b components. Each holds at most one boundary vertex, so each holds exactly one. Leaf stripping then reduces the merged word freely to the boundary word. Inversion invariance removes the dependence on plaquette orientation. In SU(2) every central function is inversion invariant. The identity holds for each fixed value of the boundary links, so it survives identifying the two copies of each core link.

**S7 (40). HOLDS.** The projector argument gives chi_1 * chi_1 = chi_1/3. The core holonomy g is a product of 16 independent Haar links, so it is Haar. 3^{1-88} 3^{1-16} (-1) = -3^{-102}.

**S2 (25-30). HOLDS**, by S3-S7. Sign-flip invariance holds because chi_1(-g) = chi_1(g).

**S9 (57-69). HOLDS.** 4cos^2 theta sin^2 theta = sin^2 2theta. Each half-interval of theta contributes one half of the integral of q. With 4x(g)^2 = 2(1 + x(g^2)), (3) applied to q/(2(1+x)) gives the first equality of (4). The epsilon limit uses monotone convergence and needs q >= 0, which is assumed. The average of 1/(2(1+x)) and 1/(2(1-x)) is 1/(2(1-x^2)). The last step is Jensen for 1/z.

**S10 (71-76). HOLDS.** Beta functions give I_{n+1}/I_n = (2n+1)/(2n+4) for I_n = integral over [0, pi/2] of sin^2 cos^{2n}. The derivative identity in the target gives the same. So c_{n+1}/c_n - 1 = 3n/(n+2) and lambda_n = n/(n+2). Checks: lambda_0 = 0, lambda_1 = 1/3.

**S11 (78-84). HOLDS.** E_0 F_n = Z and E_0 [F_n G] = Z + lambda^15 (1 - Z), so (6). With 1 - x^2 = (3 - chi_1)/4 and the integral of chi_1 q equal to 3 lambda^88, (4) gives 1/Z <= (3/2)(1 - lambda^88). Then (6) is at most 15(1-lambda) + 132(1-lambda) = 294/(n+2).

**S12 (86). HOLDS.** The conditional density of the links of L relative to product Haar lies in [1/K, K]. F_n G and F_n depend only on L, so their conditional Haar integrals do not depend on the exterior. s <= 6 x 4 x 104.

**S8 (44-55). HOLDS**, by S9-S12. If n + 2 > 294 K^3, then E[F_n G]/E[F_n] < 1/K <= E[G], so the covariance is negative. F_n and G are nonnegative and increasing on [-1,3]^P. The proof covers inhomogeneous couplings of either sign with |beta_p| <= b_0. This is more than the headline needs.

**S13 (88). HOLDS.** All binomial and tensor-product coefficients are nonnegative, so some term carries the negative sign.

**S14 (90). HOLDS.** For h_t proportional to exp(tY), d lambda/dt = Var(Y)/3 >= 0 and lambda(0) = 0, so lambda(t) is in [0,1]. It tends to 1 by the stated tail bound. The comparison of S12 applies to e^{t sum Y} G and e^{t sum Y}. The mean value theorem then gives a negative derivative, which is the sum of covariances.

**S16 (105). HOLDS.** [-2,-1] x [0,1] x {W} is a face of the half-square (left half of B) x {W}. Translated by (3,0,4,0), it is [1,2] x [0,1] x {(3,0)}, directly over p_* = [1,2] x [0,1] x {(0,0)}. The tube is the boundary of p_* times [0,3] in z: 12 faces. 87 + 12 = 99.

**S17 (107). HOLDS.** Over the closed square [1,2] x [0,1] at w = 0, the first set has z = 0 only: the right band has fibre SN at z = 0, the cap pieces there are at N, S (z = 0), the E and W pieces have x_1 <= 0, and the radii have x_1 = 0. First-set vertices with (z,w) = (1,0) all have x_1 <= 0, so the tube vertices at z = 1 are new. The second plane has z >= 3. So the common links are exactly the four links of the boundary of p_*. Each edge of the removed face lies in one remaining face and one tube face. The tube corners close the vertex links. So M is a surface with boundary the boundary of p_*. The removed face is at z = 3; the second core is at z = 4. Spans: x_1 in [-2,5], x_2 in [-2,2], z in [-1,5], w in [-1,1].

**S18 (109-117). HOLDS.** Gauge changes at three rim vertices act only on M's interior variables, so W_t is central. The 100-face cut disk gives the first equality of (8). The first equality of (4) gives the pushforward density rho; I checked that rho integrates to 1. The adjoint step is Fubini with k_t(y^{-1}) = k_t(y). Both sides are continuous and central, so they agree everywhere.

**S19 (119). HOLDS.** The sets {x > u} form a neighbourhood base at I. If z is outside V and U^m lies in V, one of the m factors lies outside U. The union bound over the position of that factor gives m terms, each bounded by ||k 1_{U^c}||_sup.

**S20 (121-127). HOLDS.** rho(I) = 1/4. rho(-v) = 1/(2(1 - x(v))) is unbounded near I. The point I is Haar-null, so the punctured neighbourhood carries the full kernel mass. W_t(-I) is finite for each t.

**S21 (129-140). HOLDS.** The normalizer is the integral of k_r^{*88} rho >= 1/4, since rho >= 1/4. The squaring map has two preimages near I, at plus and minus I, each with density 1/8 against rho(I) = 1/4. So each root carries mass 1/2, which matches g -> -g. With f = 1 + x, the root -I contributes 0 to the numerator and W_t(-I)/2 to the denominator. That gives (11).

**S22 (142). HOLDS.** Both integrands are nonnegative and depend only on the 203-face links. s' <= 24 x 203. The order is t first, then r. eta < 1/K' then gives a negative covariance.

**S23 (144). HOLDS.** The couplings beta + s t_p are nonnegative. The mean of 1 + x(U_p*) is >= 1/K' at s = 0 and < eta at s = 1. Here b_0 >= beta is needed, which the construction allows.

**S15 (96-103). HOLDS**, by S16-S22. F = exp(sum t_p x_p) with t_p > 0 and 1 + x_p* are nonnegative and increasing in the fundamental plaquette field.

Independent sanity check (a different derivation, by hand): for U(1) the squaring map has constant Jacobian, so rho = 1 and the right side of (11) is 1. The construction then gives no violation. This agrees with Ginibre's inequalities for U(1). The SU(2) effect comes from the whole equatorial sphere squaring to -I. That is the singularity of rho at -I.

No FAILS and no corrections in S1-S23.

### Step 3. Claim 2: no orientation gives nonnegative mixed neutral slab minors (S24-S30) (done)

**S24 (150). HOLDS.** An orientation is a sign e on ordered tuples with e(sigma P) = sgn(sigma) e(P). D(P_s, P_s') is continuous in (s, s') and positive on the diagonal. So it is positive for s' near s. Nonnegativity of e(P_s) D e(P_s') then forces e(P_s) = e(P_s'). A locally constant sign on [0,1] is constant. But e(P_1) = e(tau P_0) = -e(P_0). The argument is pointwise. It needs no measurability of e.

**S25 (152). HOLDS.** On U x U, D > 0 and e(P) e(Q) >= 0 almost everywhere. By Fubini, e is almost everywhere one constant on U. Full support makes every nonempty open subset of the distinct-tuple space (open in X^k) positive for the product measure. So the constant is unique and agrees on overlaps. The transposition preserves the product measure and maps U to tau U, so the local sign alternates. With separate signs e_in, e_out, Fubini gives e_in = e_out = c almost everywhere on U, and the same path argument applies.

**S26 (154-160). HOLDS.** H (vertex gauges and the three seam flips) acts by isometries of R^4 on each link, so the minimum distance between orbits is a metric on X. The quotient map is continuous and onto, and product Haar has full support, so m has full support. For H-invariant psi, the kernel w(u) C(u,v) w(v) on B_s can be averaged over H, because psi and w are H-invariant. Pushed to X, it gives (12). A spatial plaquette contains 0 or 2 links that cross a given seam, so w is flip invariant. The flips commute with each other and normalize the vertex gauge group. The identification of flip-invariant functions with the zero-electric-flux sector is the usual 't Hooft labelling. I accept it as the target's definition of the neutral sector; step 4 compares it with row 667.

**S27 (162). HOLDS.** exp(beta <U,V>) is the sum over j of (beta^j / j!) times the sum over ordered index strings I of m_I(U) m_I(V). The series converges uniformly because |<U,V>| <= |E_s|. Its form on sigma is the sum of (beta^j / j!) (integral of m_I against sigma)^2. With beta > 0, a zero form kills all moments, including the total mass. Then the integral of exp(r <U,V>) against sigma vanishes for every r > 0 and every V. Normalized, that kernel is the product of k_r(u_e v_e^{-1}). This is an approximate identity on B_s by the proof of S19, applied link by link. So the integral of every continuous phi against sigma is zero, and sigma = 0.

**S28 (164). HOLDS.** The orbit-uniform lift projects back to nu, and w > 0, so w times the lift is nonzero when nu is. The form of K_1 on nu equals the form of C on w times the lift. Here C(h_1 u, h_2 v) = C(u, h_1^{-1} h_2 v) and w is H-invariant. T nu is continuous and nonzero, so (T nu) m is a nonzero measure by full support. Induction gives the even and odd cases as stated. Point masses at distinct orbits give strictly positive definite Gram matrices, so D(P,P) > 0 on all distinct tuples.

**S29 (166). HOLDS.** chi_1(U_p) = 4cos^2 alpha - 1 is gauge and flip invariant. It is strictly decreasing on (0, pi/2). So (alpha_1, alpha_2) maps injectively and continuously into X. A half-turn of an antipodal pair on a small circle in the rectangle is an exchange path with no collision. The other k - 2 points sit at distinct parameter points off the circle.

**S30 (168). HOLDS**, by S24-S29 for every t >= 1 and k >= 2. For k = 1 the kernel is strictly positive, so k >= 2 is the right range. The stated scope is accurate: the result is about pointwise (or almost-everywhere) signs of mixed minors for each pair of boundary tuples. Cauchy-Binet composition across a slab cut is consistent with it.

Comment on strength (not a defect). S24-S25 use only three facts: K is continuous, its principal minors are positive, and two points can be exchanged without collision. So the obstruction applies to every strictly positive definite continuous symmetric kernel on a space where such an exchange path exists. It is the topological form of the known fact that total positivity needs a linear order of the labels. It is correct, but it uses nothing specific to Yang-Mills except strict positivity (S27-S28) and the existence of a two-parameter family of neutral orbits (S29).

No FAILS and no corrections in S24-S30.

### Step 4. Cited rows, and comparison with row 1213 Lemma FKG-NO and check 1247 (done)

Read in full: row 1213 (`gap-mini-solve-n-fable.md`, 117 lines). Read in the cited ranges: check 1247 section N (`gap-solve-batch4-check-astra.md` L181-239 and L463-502); row 1127 step 3 (`gap-w-astra62.md` L83-87); row 667 (`gap-transfer.md` N.3-N.7, sections 1-2, L40-48 and L108-157); the neutral criterion (`gap-mini-neutral2-fable.md` section 1.1, L56-72); row 1081 section 5.1 (`gap-descent-sign.md` L88-95); the council note V1-V4 (`gap-council-conf-fable.md`, found by grep); `prior/gap-lit-assoc.md` L187-354.

**Row 1127 (input to S3-S4).** Pieces 1-2 of step 3 describe the same band and cap, with 32 + 4 band squares and 4 + 16 + 32 cap squares. That matches the target's 36 + 52 = 88. A grep finds no check file for row 1127 in the lane. So S3-S4 above is, as far as the lane record shows, the first hand check of this 88-face plane by a reader other than its author. I checked it from the target's own text, which is complete. Step 6 recounts it by script.

**Row 1213 Lemma PAR (input to S33-S34).** PAR states I(P) = 3^{-E_2} 6^{-E_3} times the product of the site values A_v, for complexes whose links lie in two or three plaquettes. Check 1247 has PAR as HOLDS, with one correction: an odd slot reordering changes signs only at a three-valent link. The 104-face complex fits PAR: 16 core links lie in three plaquettes and all other links in two. The vertex (b, o) carries two separate index loops, so A_v = 9. The target's "split the common vertex" is the same count. The 16 core sites carry theta networks with A_v = 6 sgn(sigma_v). With one fixed slot order per core link, the product of the sgn(sigma_v) is the sign of the monodromy of the three sheets around C. That monodromy is a transposition, so the sign is -1. This is exactly the parity criterion of row 1213 L80 ("a negative value needs an odd number of sites whose local network is negative"). S33-S34 are consistent with PAR as checked in 1247.

**Row 1213 section 4 and check 1247 (the open sign).** Row 1213 asked whether I(P) >= 0 for every finite P, found three positive branched examples, and left the sign OPEN. Check 1247 (L486) kept it open. S2 gives I(P) = -3^{-102} on a 104-face branched complex. If S2 holds (it does, by step 2), the open sign question of row 1213 section 4 is settled negatively. Row 1213 section 4.2 (i) found only the positive term +3^{-91} on S_0 and "no kill". The target gets the kill from a different complex (projective plane plus the core disk D) and from large powers.

**Row 1213 Lemma FKG-NO against the target.**

| | FKG-NO (row 1213; HOLDS given NS0 in check 1247) | target, fundamental field (S15) | target, adjoint field (S8) |
|---|---|---|---|
| variables | x_p = (1/2) tr U_p | x_p | Y_p = chi_1(U_p) = 4x_p^2 - 1 |
| couplings | 0 <= beta_p <= 2^{-291} | abs(beta_p) <= b_0, every b_0 < infinity | abs(beta_p) <= b_0 |
| support | 92 faces (S_0 of row 737) | 203 faces | 104 faces |
| tori | sides >= 5 | sides >= 8 | sides >= 5 |
| increasing pair | fixed products of (1 + x_p)/2 | exp(sum t_p x_p), 1 + x_p*; t_p depend on b_0, eta | prod (1 + Y_p)^n, 1 + Y_p*; n > 294 K^3 - 2 |
| mechanism | sign -1 of spin 1/2 on a crosscap, then perturbation from Haar | large sources pin the faces; the squaring density rho is singular at -I; two doubled boundaries | large powers pin the faces near plus or minus I; rho averaged over the two lifts is singular there |
| needs NS0 | yes | no | no |

So the target removes the small-coupling restriction of FKG-NO for the fundamental field and adds the adjoint field. It pays with a larger torus and with test functions whose size grows with b_0: n and the source strengths grow like exp(c s b_0) with s up to 24 x 203. Check 1247 (L465-471) listed what FKG-NO does not rule out: every Holley comparison, every monotone coupling, association of other observables, and association only at large beta. The target closes the last item for the two plaquette fields and, by S32, for straight l x l loops. The other items in that list stay as 1247 states them.

Checker's remark (not in the target; my own short argument). Check 1247 also proved FKG-NO in the centre-even state. The same holds for S15. The centre-even state is a positive mixture of Wilson laws whose couplings have absolute value at most b_0 (check 1247, L196-198). For each component, E[F G'] < eta E[F]. Summing with the nonnegative weights keeps this. Each component also has E[G'] >= 1/K'. So the mixed covariance is still negative. For S8 nothing is needed: F_n and G are invariant under every link sign change.

**Row 667 (input to S26-S27).** Row 667 has T_0 = e^{-V/2} K_0 e^{-V/2}, K_0 = prod c(u_l v_l^{-1}), c(g) = e^{-beta(1 - tr g/2)}, and the gauge-averaged kernel A_T. Since (1/2) tr(u v^{-1}) is the R^4 dot product of unit quaternions, K_0 = e^{-beta abs(E)} C. So (12) is row 667's kernel, with the further average over the three seam flips. Row 667 (2b) proves positive semidefiniteness by the same Gram expansion. S27 adds strictness. Consistent.

**Neutral sector.** `gap-mini-neutral2-fable.md` 1.1 defines it as the joint +1 eigenspace of the flips C_1, C_2, C_3 on gauge-invariant slice functions. That is L^2(X, m) in S26. The OPEN paragraph's trace criterion matches 1.1 (X(u) - 1 <= 1/2, 3 <= u <= n/K).

**Row 1081 and the council note (GUIDE line 148 only).** Row 1081 5.1 uses Karlin-McGregor on the ordered spin labels n_1 < n_2 of a one-plaquette problem. The council note V1-V4 uses normalized second exterior powers. The target's descriptions of both are accurate. S24-S30 show that the ordered-label positivity of row 1081 cannot be carried to the actual neutral boundary configurations, because those admit exchange paths.

**Literature record.** `prior/gap-lit-assoc.md` L340 lists periodic unconditioned elementary-plaquette association (EP) as open and no theorem found. If S8 and S15 hold, the association form of (EP) fails for both plaquette fields at every finite coupling, on tori of sides >= 5 (adjoint) and >= 8 (fundamental). I did not search the literature again.

No cited statement that a PROVED step depends on was found false or misquoted.

### Step 5. Remaining statements (S31-S34, GUIDE, OPEN, RESULT) (done)

**S31 (172-176). HOLDS.** E(F_n G)/(E F_n E G) <= (294 K^2/(n+2)) / (1/K) = 294 K^3/(n+2). For (7) the quotient is below eta K', which tends to 0. If Y_p = phi_p(xi) with xi associated and each phi_p nondecreasing, then F(Y) and G(Y) are nondecreasing in xi, so their covariance is >= 0 (Esary-Proschan-Walkup). That contradicts S8 and S15. The 2 x 2 "mixed source determinant" is Cov(F, G). The last sentence is a remark.

**S32 (178). HOLDS.** Scaling by l turns each old link into a straight path of l fine links. Distinct old links get disjoint paths. A product of l independent Haar elements is Haar, so the coarse links are independent Haar at zero coupling and every Haar computation of S2-S23 carries over. The test functions depend only on path links. The conditional density of the path links, given all other links, lies in [1/K_l, K_l] with s_l <= 6 x 4l x (number of old faces). The torus must contain the scaled set (sides >= 4l + 1 for the adjoint set, >= 7l + 1 for the fundamental set), as the target says.

**S33 (180). HOLDS.** The degree-2 and degree-3 invariants of the real spin-1 representation are delta (norm squared 3) and epsilon (norm squared 6). The half-turn argument: a nonzero entry T_abc must have n_1 + n_2, n_1 + n_3 and n_2 + n_3 even with n_1 + n_2 + n_3 = 3. So n_1 = n_2 = n_3 = 1. A signed quarter-turn then forces alternation. Reversed links only transpose indices (row 1213 PAR, check 1247).

**S34 (182). HOLDS.** Smooth sites give 3. Core sites give 6 sgn(sigma_v). The sheet monodromy around C swaps the two sides of the cut disk and fixes the sheet of D, so the product of signs is -1. After splitting (b, o), chi = 1 + 1 - 0 = 2, so V - E = -102 and the total is -3^{V-E} = -3^{-102}. This is a second derivation of (1) through a different route (local tensor networks instead of disk convolution). The two agree. Step 6 recounts V and E by script.

**GUIDE paragraphs.** L3, L21, L94, L148 and L190 are accurate descriptions of what follows. L7 agrees with row 1213 and check 1247 (three positive examples: 3^{-8}, 3^{-15}/2, 6^{-16}). A grep of `open-registry.md` finds no owner for adjoint or plaquette association, as L7 says. L9 agrees with row 1127, row 737 (via row 1213) and the literature record. L5 and L11 cite main, other PRs and external texts. I did not check them (outside the lane folder).

**OPEN (184-188). Accurate.** The trace criterion matches the neutral criterion 1.1. (RR) in `gap-mini-solve-ag-opus.md` section 6 is a bound eta_* <= h on the absolute log cross-ratio of the slab kernel. Check 1265 has its two-way reading. For k = 2 the mixed minor is K(P_1,Q_1) K(P_2,Q_2) - K(P_1,Q_2) K(P_2,Q_1). Its sign is the sign of the log cross-ratio. So S30 says this log cross-ratio has no orientation-consistent sign. (RR) asks only that its absolute value be small. The two are compatible, as the target says. The AK33 citation (outline 29467-29482) is external, and I did not check it.

**RESULT line (192).** It states exactly what S8, S15 and S30 prove, and it keeps (N-phys) and the gap OPEN. Accurate.

No FAILS and no corrections in S31-S34. No misstatement in the GUIDE, OPEN or RESULT text that I could check.

### Step 6. Numeric guide (done; guide only, not a proof step)

Two scratch scripts, outside the repository, run with `python3 -E -P`, BLAS threads 1. Peak memory 16 MB and 57 MB. Run time a few seconds. Both are independent re-implementations from the target's text. They use no file of the lane.

**Script 1 (combinatorics of the plaquette sets).** It builds the faces in Z^4 from the target's coordinates and recounts:
- band 36, cap 52, D 16; A has 88 distinct faces and P has 104;
- in A every link lies in exactly two faces and every vertex is a manifold point; V = 89, E = 176, chi = 1; A is not orientable (a projective plane);
- the links common to A and D are exactly the 16 links of C; the only common vertex off C is (b, o) = (0,0,0,0);
- in P, 184 links lie in two faces and 16 in three; V = 97, E = 200, so V - E = -103, and -102 after splitting (b, o);
- spans 4, 4, 2, 2;
- Lemma PAR of row 1213 evaluated on the actual lattice networks, with one fixed slot order per three-valent link: value -1 x 3^{-102}. The sign comes from the product of the 16 theta-network permutation signs. This is a third evaluation of (1). It agrees with S7 and S34;
- second surface: the face [1,2] x [0,1] x {(3,0)} is a face of the translated plane; M has 99 distinct faces and shares none with the first set; the common links are exactly the 4 links of the boundary of p_*; the common vertices are exactly the 4 corners of p_*;
- M plus p_* is a closed non-orientable surface with chi = 1 and no singular vertex; the second core lies in M and misses the removed face;
- the 203-face set has spans 7, 4, 6, 2.

**Script 2 (one-variable integrals on SU(2) class functions).** Midpoint rule with 2^14 nodes, exact for the trigonometric polynomials involved:
- (3) and the first equality of (4), for a centre-asymmetric test q: agree to 12 digits;
- (5): lambda_n = n/(n+2) to 12 digits for n = 1, 2, 5, 10, 50, 200;
- (6): Z by the character sum, by quadrature of q(g^2) and by (4) agree. The integral of chi_1(g) q(g^2) equals 1 - Z. The formula 1 - lambda^15 + lambda^15/Z equals the direct quotient. Values: 0.952 (n = 50), 0.572 (n = 150), 0.261 (n = 400), each below 294/(n+2). Half-integer coefficients of h_n vanish (below 1e-14);
- S14: lambda(t) for h_t proportional to exp(tY) rises from 0 toward 1 (0.204, 0.721, 0.949, 0.990 at t = 0.5, 2, 10, 50);
- (9): with kappa_j(t) = I_{2j+1}(t)/I_1(t), W_t(I) = 0.604, 0.2695, 0.2547 and W_t(-I) = 1.51, 10.5, 40.8 at t = 100, 1000, 4000. So W_t(I) tends to 1/4 and W_t(-I) grows roughly linearly in t;
- (10)-(11): at t = 1000 the Haar quotient is 0.05068 (r = 1e5) and 0.05014 (r = 4e5), against the limit 2W_t(I)/(W_t(I) + W_t(-I)) = 0.04996. At t = 100: 0.5765, 0.5725 against 0.5721. The normalizer is >= 1/4 and tends to 1/4.

The guide agrees with every hand computation. The growth is slow: the adjoint Haar quotient is still 0.26 at n = 400, and the fundamental quotient is about 0.05 at t = 1000. The proofs need only finiteness, so this costs nothing logically. But the witnesses are very large objects. At coupling b_0 the needed n exceeds 294 K^3 with K = exp(2 s b_0) and s up to 2496.

### Step 7. Which sign-definite objects are ruled out, and which stay open (done)

All PROVED statements hold (steps 2-5). So the target rules out the following classes.

**Ruled out.**
- **R1. FKG association of the elementary plaquette field in the coordinatewise order.** This holds for both the fundamental traces x_p and the adjoint traces chi_1(U_p). It holds at every finite coupling: homogeneous or not, of either sign, with abs(beta_p) <= b_0. The tori need sides >= 8 (fundamental) or >= 5 (adjoint). It also holds in Gibbs states with the same specification, and for traces of straight l x l loops of fixed side l (S32). The same examples exclude:
  - the FKG lattice condition (log-supermodularity) for the joint law of these variables;
  - any weakened form E(FG) >= c E(F) E(G) with c > 0 (S31);
  - any realization of either field as coordinatewise increasing functions of an associated auxiliary law. This covers any random-cluster, random-current or random-surface representation that is associated and monotone onto plaquette traces.
- **R2. Griffiths-type signs of adjoint character moments.** Haar moments of products of distinct elementary adjoint characters are not all >= 0 (S2: -3^{-102}). This settles the open question of row 1213 section 4 negatively. At each finite coupling, some product of powers of adjoint characters has negative Wilson mean. Some pair of such monomials on disjoint plaquette sets has negative covariance (S13).
- **R3. Ginibre-type pair inequalities for all nonnegative couplings.** Cov(x_p, x_q) >= 0 fails for some Wilson law with nonnegative, spatially varying couplings (S23). Equivalently, the mean of one plaquette trace is not monotone in the couplings of the other plaquettes. The adjoint pair version fails under positive adjoint sources (S14). Monotonicity in one homogeneous coupling is not affected: that derivative is a variance.
- **R4. Sign-definite mixed minors of the neutral slab kernel.** Take k >= 2, any thickness t >= 1 and 0 < beta < infinity. Then no orientation of k-tuples of actual neutral boundary configurations makes every mixed k x k minor of K_t nonnegative, pointwise or almost everywhere. This also holds with separate orientations on the two boundaries (S24-S30). So no total positivity (TP_k or sign regularity) holds on that label space. No oriented mixed minor with fixed boundary tuples is an integral of nonnegative weights (Karlin-McGregor or Lindstrom-Gessel-Viennot type).

Checker's remark (my own short argument, not in the target). At beta = 0 the degree-one pair already fails. Take F_1 = prod over p != p_* of (1 + Y_p) and G = 1 + Y_p*. A subset S of P that contains p_* has a nonzero Haar moment only if every link of S lies in two or more faces of S. The interior links of D lie only in D. Every other non-core link lies only in A. Both A and D are connected surfaces once cut along C. So S = P is the only such subset, and Cov_0(F_1, G) = E_0 prod_P Y_p = -3^{-102}. This is the adjoint analogue of FKG-NO at small coupling with a fixed pair. S8 makes it uniform in the coupling at the price of large n.

**Left open by the target (not touched by any statement in it).**
- **O1. Bounded test classes and other variables.** The witnesses need n > 294 K^3 - 2, or source strengths that grow with b_0, with K = exp(2 s b_0). So the following are not excluded: inequalities on a fixed class of increasing functions of bounded strength at a fixed large coupling; association or FKG for other variables (block or smeared variables at a physical scale, flux or Polyakov variables, link variables in a fixed gauge, spin-network or surface labels); association in other partial orders.
- **O2. Positive structures that are not association.** Monotone couplings and Holley comparisons that are not association (check 1247 L465-468). Positive mixture forms such as the lift-sum marginal of check 1247 (L479-483).
- **O3. Determinant positivity in other forms.** Positivity after changing the boundary observables. Positivity after projecting onto a smaller family with a linear order: there the exchange path is absent, as for the ordered spin labels of row 1081. Constructions that use cancellation between different boundary tuples. Two-sided bounds with no sign, such as (RR) of `gap-mini-solve-ag-opus.md` section 6. The target states all of these limits itself (L168, L188).
- **O4. Positivity that is already true.** Reflection positivity, the positive principal Gram determinants of the exterior powers of T (S28), and the positive spectral measures they give. These are sign-definite but give no gap by themselves. A positivity criterion of explicit-formula (Weil) type would be a quadratic form whose positivity is equivalent to the gap. The target does not address one.
- **O5.** (N-phys), the continuum construction and the Jaffe-Witten gap.

In one sentence: the target excludes the two most direct sign-definite objects. These are monotone (FKG or Griffiths) positivity of local plaquette data in the natural order at any coupling, and one-signed mixed minors of the neutral slab kernel on its actual boundary configurations. It does not test positivity on a restricted or ordered label set, or a positive-definite (Weil-type) quadratic form.

### Step 8. Counts, verdicts, what was not checked (done)

The counts and the per-statement table are at the top of this file. Checked line by line, by hand, by Claude Opus 5.5 (max effort, laptop subagent). This is one reader's check. The script recount in step 6 is a separate implementation from the target's coordinates. The second evaluation of (1) (S34, PAR) is a different derivation from S7.

## Not checked

- Sources outside the lane folder: the Sussman-Alpoge outline (lines cited at target L11, L160, L188), CA-I 2698-2711, the Alpoge remark, main at 8b11ae2bb9, and PRs 10114, 10133, 10134, 10141 (target L5). The target uses none of them in a PROVED step. L160 cites the outline only for the same one-bond expansion that row 667 proves in the lane.
- Row 737 (`gap-means-max.md` section 2.4) and `prior/repo-search-2026-11-08.md`. These are cited only in GUIDE lines.
- The rest of row 1127 beyond pieces 1-2 of step 3.
- The physical reading of flip-invariant slice functions as the zero-electric-flux sector. I took it as the definition, and it agrees with `gap-mini-neutral2-fable.md` 1.1.
- No Lean formalization. The scripts of step 6 are a guide outside the repository. They are not a compute verification in the lane's sense.
- Questions the target does not claim, for example association on a bounded class of test functions at a fixed large coupling (step 7, O1).

RESULT (2026-11-20T17:32Z by date -u; anthropic/claude-opus-5-5/max laptop-subagent): row 1304 `gap-positivity-astra62.md` checked line by line by hand; 34 of 34 PROVED statements HOLD, 0 HOLD AFTER CORRECTION, 0 FAIL; claim 1 holds (adjoint and fundamental plaquette fields violate association at every finite coupling with abs(beta_p) <= b_0, on tori of sides >= 5 and >= 8, via the 104- and 203-face doubled-boundary sets, which a script recount and a second PAR evaluation of -3^{-102} confirm); claim 2 holds (for k >= 2, t >= 1, 0 < beta < infinity no orientation makes all mixed neutral slab minors nonnegative, pointwise or a.e.); this extends row 1213 FKG-NO (0 <= beta_p <= 2^{-291}, given NS0) to all finite couplings and to the adjoint field, and settles row 1213's open adjoint Haar sign negatively; ruled out: FKG/Griffiths/Ginibre positivity of local plaquette data in the natural order, and one-signed mixed slab minors on the actual neutral boundary configurations; open: bounded-strength or other-variable inequalities, non-association positive structures, determinant positivity on ordered or projected label sets, Weil-type quadratic forms, (N-phys) and the mass gap.
