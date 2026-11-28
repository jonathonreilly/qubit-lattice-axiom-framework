lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-12T01:20Z

# Check of `library/gap-crux-fp.md` (row 716, `gap-crux-fp-check`)

Provenance: written by Claude Opus 5.5, high effort, Mac mini worker 2, on branch `claude/ym4d-hard-route` at commit 649a17386, started 2026-11-11T13:20Z. One line-by-line reading by one model of a file written by Claude Fable 5.2 max (row 712). Not an audit. No computer-assisted step; any script below is GUIDE only.

## Status block (kept current)

- **Complete for this run (2026-11-11).** Every statement the row names has a verdict below. None FAILS. Ten HOLD: P1, P2, Remark 2.A (a), T1, T2, Lemma COV, Lemma REG, Identity L, Proposition TW, Lemma P. Corollary C also HOLDS, but it is not new. Four HOLD AFTER CORRECTION: Remark 2.A (c) (citation), T3 (one hypothesis), the Corollary of 3b.3 (two words), Proposition V (threshold, and the mark in 3b.2). Corollary C is Proposition P (a) of `gap-seed-limit.md` (row 700), so the file's claim that the form (C) is new is wrong. The independent hand test of the example of Proposition TW passes (three routes give 1.4901 x 10^(-4)).
- Read whole: `gap-crux-fp.md` (503 lines); `gap-transfer.md` lead note of row 671, notation, A0, Section 1 ((1a)-(1c), (1.2), A0 (e)), and 2.2-3.3 for the weight in Proposition V; `gap-crux-restate.md` Sections 1 and 3.4; `gap-mid-max.md` lead note of row 709, Section 6 (Identity FL) and Section 10; `gap-mid-check.md` Section 5. Also read: `gap-seed-check.md` Lemma 1.1 and its Remark F3 point (the twisted slice); `gap-mid-max.md` Lemma 4.1; the Theorem SH statement and lead note of `gap-seed-shape.md`; `gap-seed-limit.md` Section 5 and Theorem L, with the status block and A10 of `gap-seed-limit-check.md`; the arXiv source of van Enter and Shlosman, cond-mat/0306362 v1 (gauge section and Theorems 1, 2).
- Not covered by this check: Sections 1.1, 1.3 to 2.7 (except Remark 2.A), 3, 3b.1, 3b.2, 3b.4. Also not covered: the GUIDE runs, (AS-bg), (vMF-Lip) with its reductions R-a and R-b, the Brownian form in 4.2b, and Remark 2.A (b) and (d). Row 716 does not ask for them. (TM) for a general weight is row 717's; this check notes only that the Gram expansion carries over to the weight of Proposition V. The published version of van Enter and Shlosman (CMP 2005) was not read. No numeric run was made.

## Repo search

Grep of `library/open-core.md` and the FINISH rows for the objects of this check: no other row checks `gap-crux-fp.md`. Row 717 (`gap-ves-read`) reads the paper of van Enter and Shlosman in full and checks (TM) for a general weight; this check does not repeat that, and says below only what Proposition V takes from the paper. No lemma is attacked here; this is a check item.

## Verdicts

### P1 (Section 1.2). HOLDS.

The top eigenvalue is simple, so r_1^n <= S(n; B) < t, and n m(B) = n log(1/r_1) > log(1/t). log 1650 = 7.41, so the time side n is more than 7.4 inverse masses of the box (2n)^3, and the side 2n more than 14.8. With the threshold 1/5041 of Theorem S (used in Lemma REG, Proposition V and Corollary C) the numbers are log 5041 = 8.53 and 17.1. The last sentence ("no statement at a smaller size can be the seed") is a reading of P1, not a further claim.

### P2 (Section 1.2). HOLDS.

Re-derived. C_nu = composition with the flip Z_nu: unitary involution, commutes with T, maps positive functions to positive functions (Lemma 1.1 (iv) of `gap-seed-check.md`). C_nu Omega is a unit eigenvector of lambda_0, so C_nu Omega = c Omega with abs(c) = 1, and c = 1 because both are positive. C_nu commutes with the compact self-adjoint T, so a joint eigenbasis exists with C_nu = eps_i = +-1. Then Z - Z^(1 nu) = 2 sum over odd i of lambda_i^(n_1) <= 2 lambda_0^(n_1) S, and Z = lambda_0^(n_1)(1 + S). The twisted weight is the corrected one of rows 698, 699 (exp(-beta(1 + (1/2) tr U_p)) on the stack); P2 uses Z^(1 nu) only as Tr(T^(n_1) C_nu), so the wording does not matter. With S < 1/1650: 1 - Z^tw/Z < 2/1650 = 1/825 = 0.121 percent ("less than 0.13 percent" is true).

Remark on Section 5.1 and Part 3 ("weaker than Identity FL"; "Identity FL ... stronger"). For a single twist P2 is the sharper bound: Identity FL gives 1 - Z[k]/Z <= 8U <= 8S/(1 + S) (its consequence (3)), P2 gives 2S/(1 + S). Both follow from (1 - C_nu)/2 <= 1 - P_0. Identity FL is the stronger statement as an identity for the sum. No proof depends on this comparison.

### Remark 2.A (a) (Section 2.1). HOLDS.

The C_i commute (each multiplies by -1 the links of one direction on one plane, and -1 is central), so P_0 = product of (1 + C_i)/2 = (1/8) sum over k of C^k, and Tr(T^a P_0) = (1/8) sum over k of Tr(T^a C^k) by linearity (T^a is trace class, C^k bounded). For a unit k, Tr(T^a C^k) is the partition function with one twisted stack in the plane (1, nu) (Lemma 1.1 (iv)). For two or three flips the same proof (kernel A_T(u, Z^k w), then (1.3)) gives the partition function with one stack in each flipped plane; the file uses only the trace, so (a) does not need this.

### Remark 2.A (c) (Section 2.1). HOLDS AFTER CORRECTION (citation only).

Re-derived. Write Z(n | e, m) for the partition function with electric twists e in the planes (1, nu) and magnetic twists m in the three spatial planes, time direction 1.
- Permutation invariance of the sum over all 64 twists: a permutation sigma of the axes maps the stack of the plane (mu, nu) to a stack of the plane (sigma mu, sigma nu) and keeps the Haar measure and the weights (Lemma 1.1 (v)); the position of each stack does not matter (the change of variables of Lemma 1.1 (v) acts on the plaquettes of one plane only, so it works with several stacks present). So the map from twist tensors to twist tensors is a bijection, and the sum is a symmetric function of the four sides. Holds.
- The trace form: for fixed m, T^(m) (the transfer operator with the twisted spatial potential V' = beta sum over p of (1 - (1/2) eps_p tr u_p)) is positive and trace class with a simple positive top eigenvector; this is the checked extension in the Remark F3 point of `gap-seed-check.md`. The flips: V'(Z_k u) = V'(u), because every spatial plaquette has an even number of flipped links, and Z_k(h.u) = h.(Z_k u); so C_k commutes with T^(m) and Tr((T^(m))^a C^k) = Z(n | k, m) by the proof of Lemma 1.1 (iv) word for word. Then the sum over all 64 = sum over m of sum over k of Tr((T^(m))^a C^k) = 8 sum over m of Tr((T^(m))^a P_0) = 8 Tr((direct sum over m of T^(m) P_0)^a). Holds.
- **Correction (citation).** The input is not Lemma 1.1 of `gap-seed-check.md` (that lemma is for the untwisted action); it is the Remark F3 point of the same file (line 177, "(TM) for the twisted action ... follows from `gap-transfer.md` word for word"), plus the extension of Lemma 1.1 (iv) to a twisted slice and to several flips, which is the two lines above. Replace "Lemma 1.1 of `gap-seed-check.md`" by "the Remark F3 point of `gap-seed-check.md` and Lemma 1.1 (iv), (v) there, extended to a twisted slice and several flips".
- (b) and (d) are not asked. (d) is marked RECALLED in the file and is not proved.

### Proposition T1 (Section 3b.3). HOLDS.

It is the contrapositive of "H(M') implies Seed(M')" for M' in the class of the tool.

### Proposition T2 (Section 3b.3). HOLDS (as a statement about the literal wording).

Example 1 is enough. The hypothesis of Theorem DOB is alpha = 18 beta < 1. For U(1) the one-link exponent changes by s Re(e^(i theta)(z - z')) with abs(z - z') <= 2 when one neighbour changes, so its oscillation is at most 4 s, and the proof of Lemma INF gives alpha <= 18 s; for Z_2 the same. So the hypothesis holds for U(1) and Z_2 at beta < 1/18, and the tool gives the SU(2) seed there (Theorem DOB, checked row 709). So the literal sentence "a tool that also holds for U(1) cannot give the seed" is false. Two notes. (1) The sentence "both are sound because their hypothesis fails for U(1) at every coupling where the U(1) seed fails" needs the whole chain of Theorem DOB (Lemma M, Proposition MIX, Theorem SH, and (TM)) for U(1). That is not written; T2 does not need it. (2) Part 3 of the file itself reports that 13.12 already reads the test as "cannot give the seed at every coupling". So T2 refutes the short wording, not the form the earlier work used; the file says so in its table (C6, "Partly"). Example 2 (the cluster expansion) was not re-checked here.

### Proposition T3 (Section 3b.3). HOLDS AFTER CORRECTION.

The proof by T1 needs M' to be in the class of the tool (the proof of "H implies Seed" must run for M'). The statement leaves it implicit. **Correction:** "Let M' be in the class of the tool, and let H be blind ...". With this, if H(M at beta) held, H(M' at beta) would hold, and the tool would give Seed(M' at beta), against the assumption.

The four uses, checked by hand:
- Maximal torus: an element with eigenvalues e^(+-i phi) has (1/2) tr U = cos phi, so the SU(2) weight is exp(beta cos phi) up to a constant, the U(1) Wilson weight at the same beta. Holds. beta_U finite: RECALLED (F8). About 1.01: GUIDE.
- Centre: on {1, -1} the weight is exp(beta x), x = +-1, the Z_2 weight at the same beta. Holds. The self-dual point of the four-dimensional Z_2 gauge theory is (1/2) log(1 + 2^(1/2)) = 0.4407 in this normalisation; that its seed fails above it is GUIDE.
- K7 end point (1.48, 0.90): log w = beta_F x + beta_A (4x^2 - 1)/3. Minimum at x = -3 beta_F/(8 beta_A) = -4.44/7.2 = -0.6167, value -0.9127 + 0.9 x 0.5212/3 = -0.7563. Maximum at x = 1: 1.48 + 0.90 = 2.38 (at x = -1 the value is -0.58). Oscillation 3.136, the Wilson oscillation 2 beta at beta = 1.568. Lipschitz constant 1.48 + 2.40 = 3.88. All hold. The conclusion "the tool ends near 1.6" also needs either H monotone in the oscillation or a K7 point with larger oscillation where the seed fails; both are GUIDE-level and the file marks the end point GUIDE.
- Dimension, N: logic as above; GUIDE inputs.

### Corollary of 3b.3 ("what the tests forbid"). HOLDS AFTER CORRECTION.

The logical part is T3 with GUIDE numbers. Two words go too far. (1) "is sound": a tool of this kind is sound only if its proof "H implies Seed" is written. That is so for Theorem DOB and the cluster expansion. It is not so for Bakry and Emery: `gap-mid-max.md` Proposition BE is a counterexample above beta = 1/3; no proof of the seed from a curvature bound exists in the repository. **Correction:** "if sound (as Theorem DOB is)". (2) "These tools stop at 0.1 to 0.33": the proved stops are 1/18 (Theorem DOB) and 1/12800 (`gap-seed-sc.md`); 0.1 is an unported sharper bound and 1/3 is only where Proposition BE's counterexample begins. Mark the range GUIDE. The conclusion of the paragraph (in the range where these tools stop, the tests explain nothing) is unaffected.

### Lemma COV (Section 4.1). HOLDS.

Re-derived line by line.
- Trace formula with a layer insertion (the point the file leaves "not re-proved"). By (1.2), exp(-S) = product over t of T_0(U(t), g_t . U(t+1)), and g_t occurs in one factor only. For A a bounded measurable function of (U(t_A), g_(t_A), U(t_A + 1)), integrate g_(t_A) against A times its factor: this gives A_T^A(U(t_A), U(t_A + 1)) = integral over h of A(u, h, v) T_0(u, h . v), jointly measurable by Fubini, with abs(A_T^A) <= A_T. The other g_t give A_T as in 1.3. The result is a cyclic product of D bounded kernels in the slices. A product of bounded-kernel integral operators is an integral operator with a bounded kernel (Fubini), so the integral over the slices is Tr(S_k S_l) of two operators with L^2 kernels, by A0 (e). A0 (e) needs only L^2 kernels; continuity is not used. Gauge invariance of A is not needed: the trace is over L^2(X), on which T_P = T P has the kernel A_T and is 0 off H_inv. So Z<AB> = Tr(T_A T^a T_B T^b), Z<A> = Tr(T_A T^(D-1)), Z = Tr T^D, with a = d - 1 and b = D - 2 - a. Holds.
- Norm of That_A: abs(<f, T_A g>) <= <abs f, T abs g> <= lambda_0 norm(f) norm(g). Holds.
- Step 2. The expansion into four terms is exact (That^j = P_0 + Rhat^j for j >= 1, P_0 Rhat = 0). Term 2 = <Omega, That_B Rhat^b That_A Omega>, at most r^b; term 3 at most r^a; term 4 at most r^a S(b) (operator norm times trace norm) and at most (S(2a) S(2b))^(1/2) (two Hilbert-Schmidt norms). The case split: if b >= D/2 then r^a S(b) <= S(D/2) = sigma (S(k) is non-increasing in k). If b < D/2 then b <= D/2 - 1 (D even), and a <= b with a + b = D - 2 forces a = b = D/2 - 1; then (S(2a) S(2b))^(1/2) = S(D - 2) <= S(D/2) because D >= 4. **The case a = b = D/2 - 1 holds.** abs(E_A) <= S(D - 1) <= sigma, N_1 = 1 + S(D) with S(D) <= sigma. Holds.
- Step 3. N_AB N_1 - N_A N_B = alpha gamma S(D) + E_AB(1 + S(D)) - alpha E_B - gamma E_A - E_A E_B: expanded by hand, holds. The sum of bounds is sigma + (2 r^a + sigma)(1 + sigma) + 2 sigma + sigma^2 = 2(1 + sigma) r^a + 4 sigma + 2 sigma^2, and 2 sigma^2 <= sigma for sigma <= 1/2. N_1 >= 1. Holds.
- If A, B are complex, alpha, gamma lie in the unit disc and nothing changes.

### Lemma REG (Section 4.1). HOLDS (given (TM-gen) for the weight; for the Wilson weight the inputs are checked).

Re-derived line by line.
- f = inf over n of F(n)/abs(n) is the limit along the cubes D_k: F(n)/abs(n) is non-increasing in each side separately (Lemma A (a) gives (Tr S^k)^(1/k) non-increasing for all k, not only along multiples), so for any torus n' and D_k >= max n'_i, F(D_k^4)/D_k^4 <= F(n')/abs(n'). Holds. abs(f) <= 6 beta, so f is finite.
- f_k'' = D_k^(-4) Var(sum_p phi_p), and by translation invariance it is the sum over the six orientations o of the sum over p' of Cov(phi_(p_o), phi_(p')): there are D_k^4 plaquettes of each orientation. Holds.
- Theorem S with n_k = 2^k n and 2 n_k = D_k: S(D_k/2; D_k^3) <= (5041 s)^(2^k)/5041 <= q^(2^k)/5041. Corollary S3' at L = D_k >= 2n: r <= q^(1/n). Both hold. sigma_k <= 1/5041 <= 1/2 and D_k >= 6 even, so Lemma COV applies; 2(1 + sigma_k) <= 2.0004 <= 2.001.
- Layers: for a direction mu, a plaquette in a plane through mu, based at x, is a function of the slices x_mu, x_mu + 1 and the two mu-links between them; a plaquette in a plane without mu is a function of the slice x_mu. So with the direction of the largest cyclic distance delta >= 2 as time, Lemma COV applies with d = delta. Holds.
- delta <= 1: abs(Cov) <= (Var Var')^(1/2) <= 1, since phi in [-1, 1] has Var <= 1. The count 6 x 3^4 = 486 includes p_o. **The plaquette count holds.** For delta = j >= 2: (2j + 1)^4 - (2j - 1)^4 = 64 j^3 + 16 j (expanded by hand), and 16 j <= 8 j^3 for j >= 2; the torus count is at most this. Per orientation: 486 + 6 x 72 x 2.001 x sum of j^3 q^((j - 1)/n) + 5 sigma_k x 6 D_k^4, and 6 x 72 x 2.001 = 864.4 <= 865. Holds. D_k^4 sigma_k <= 16 n^4 2^(4k) q^(2^k)/5041 is bounded in k because q < 1. So f_k'' <= C(n, q) on I, uniformly in k.
- **From the bound on f_k'' to differentiability of f.** abs(f_k') <= 6 (6 D_k^4 plaquettes, abs(phi) <= 1). Taylor with f_k'' <= C on the segment [x, y] in I, limit along a subsequence with f_k'(x) -> g: f(y) <= f(x) + g(y - x) + C(y - x)^2/2. A subgradient g' of the convex f at x gives (g' - g)(y - x) <= C(y - x)^2/2 for y on both sides of x, so g' = g; a convex function with one subgradient at an interior point is differentiable there. Adding the inequality at x and at y gives 0 <= f'(y) - f'(x) <= C(y - x) for y > x. **The step holds.** It needs I open (x interior), which the statement assumes.
- Inputs for a weight other than Wilson: (TM), the symmetry of Z, Theorem S, Corollary S3' and the layer form (1.2) for that weight. This is (TM-gen); see Proposition V below.

### Proposition V (Section 4.1). HOLDS AFTER CORRECTION, as an implication from two inputs that are not checked here.

**(a), the weight is in the class.** Holds. (1 + x)/2 = (2 chi_0 + chi_(1/2))/4 with chi_(1/2) = tr U = 2x; powers of characters are sums of characters with non-negative integer multiplicities (Clebsch-Gordan, `gap-transfer.md` 2.5); the exponential series keeps the signs for beta >= 0. For p = 1: exp(beta (1 + x)/2) = e^(beta/2) exp((beta/2) x). phi = ((1 + x)/2)^p takes values in [0, 1], inside [-1, 1] as Lemma REG asks.

**Is the class (TM-gen) right for this weight?** Yes, as far as the weight goes. w_p is a strictly positive, continuous, real class function with w_p(g^(-1)) = w_p(g), and its one-link kernel is positive definite. One more remark, not a check of (TM-gen): the Gram expansion of `gap-transfer.md` 2.2 carries over to this weight. For g = u_l v_l^(-1), x = (1/2) sum over a, b of (u_l)_ab conj((v_l)_ab). So exp(beta ((1 + x)/2)^p) is a power series in this Gram kernel with non-negative coefficients, and it converges absolutely because abs(x) <= 1. Then (2b) and (3) follow as in 2.3 to 3.3. Statement (4) uses only continuity and the two-sided bound of the kernel. Lemma 4.1 (a) of `gap-mid-max.md` uses only the traces p_n(beta). It gives continuity of lambda_0, and so of S(a; B) = p_a/lambda_0^a - 1; the file's gloss "the thermal sum ... is continuous" is this one-line consequence. The full check of (TM) for a general weight is row 717's (`gap-ves-read`). It is not repeated here.

**(b), the proof.** Re-derived. If S(a; (2a)^3; beta_t) < 1/5041 for one a, then by continuity at that fixed size there are an open I around beta_t and q < 1 with 5041 S <= q on I (take q = (1 + 5041 S(beta_t))/2). Lemma REG then gives f differentiable at beta_t, against the cited theorem. Holds.

**Correction 1 (threshold).** (b) proves S(a; (2a)^3; beta_t) >= 1/5041 for every a >= 3. That is the failure of the seed of Theorem S. It is not the failure of the seed of Theorem SH, threshold 1/1650. But 3b.3 defines Seed(M) with the threshold of Theorem SH, and 3b.2, 4.1 ("What Proposition V excludes") and 5.1 say "the seed fails at every size". A tool that proves S < 1/1650 is not refuted by S >= 1/5041. **Repair (one line; uses Theorem SH (i), checked row 707, for this weight, which is part of (TM-gen)):** if S(a; (2a)^3; beta_t) < 1/1650, then by SH (i) at the shape r = 2 (with its step j and constant K, K s < 1), K s_k <= (K s)^(j^k), so s_k = S(a_k; (2 a_k)^3) < 1/5041 at some size a_k = j^k a. Continuity at that size and Lemma REG then give the same contradiction. With this line (b) holds with the threshold 1/1650. Otherwise, write 1/5041 in every summary.

**Correction 2 (marks).** The table of 3b.2 marks this row "THM (van Enter and Shlosman; Proposition V of Part 4)". It is PROVED GIVEN the cited theorem in a reading and (TM-gen); it is not a theorem. The 4.1 marks paragraph and 5.1 say so correctly.

**What exactly is taken from van Enter and Shlosman.** I fetched the arXiv source of cond-mat/0306362 (v1, TeX file `entshl4a.tex`, dated 13 June 2003) into a scratch folder and read the gauge section and the two theorems. The paper is credited to A. C. D. van Enter and S. B. Shlosman.
- Statement (their Theorem 2, quoted): "For lattice gauge models with plaquette action ((1+L(U_P))/2)^p, (where L(U_P)=Tr(U_P+U_P^*)) in dimension 3 and more and p high enough, there is a first order transition, that is there exists a temperature at which the free energy is not differentiable in the temperature parameter." Their Hamiltonian is H = -J sum over P of L(U_P), with the p-th power inside L (their equation for U(1)). So the Gibbs weight is exp(beta ((1 + .)/2)^p) with beta = J/T, as Proposition V uses it. Non-differentiability in the temperature at T > 0 is the same as non-differentiability of f in beta. The file's quote is faithful.
- Normalisation. As printed, L = Tr(U_P + U_P^*) is 4x for SU(2), with values in [-4, 4]. Then (1 + L)/2 has values in [-3/2, 5/2], and its p-th power is not a single narrow well. So the printed formula must be read with a normalised trace. The file's reading (1 + x)/2 with x = (1/2) tr U is the natural one: it matches their U(1) formula (1 + cos)/2 and their remark that the well has width of order p^(-1/2). It is still a reading, as the file says. The source also keeps a draft comment next to the theorem ("You mean adjoint here?").
- Proof. Only a sketch is written, "in the simplest case of a U(1)-invariant interaction in 3 dimensions", for "the toy model where the potential L(U) is chosen to be 1 if ... between -eps/2 and +eps/2 and zero otherwise". The step to smooth wells is referred to their earlier paper ("can then be done in the same way as in [EntShl]"). Nothing is written for SU(2), or for dimension 4. On SU(n) in d = 4 they add: "we conjecture that confined phases exist on both sides of the phase transition". So the file's mark "stated, not written" is right for the preprint. The published version (Commun. Math. Phys. 255 (2005)) was not read here; row 717 reads it.
- Free energy. Chessboard estimates work on periodic tori. So their free energy is the periodic limit, which is the f of Lemma REG. For bounded interactions the limit does not depend on the boundary condition (RECALLED, standard), so this is not a further gap.

**What Proposition V excludes (4.1, the paragraph after the proof): the arithmetic and the logic hold.** ((1 + x)/2)^p is increasing in x, so log w_p has its only local maximum at U = 1. For K7: d/dx log w = beta_F + (8/3) beta_A x, which is negative at x = -1 exactly when beta_A > 3 beta_F/8 = 0.555. At the end point 0.90 > 0.555, so U = -1 is a second local maximum there. "On its whole line" rests on the GUIDE shape of the line. The step "so what separates the Wilson weight is a number" is a reading, not a proved statement. The comparison "the same quadratic form at the identity up to the factor p" holds: ((1 + x)/2)^p = 1 - p eps/2 + O(eps^2) at x = 1 - eps.

### Identity L (Section 4.2). HOLDS.

Re-derived. Z_k := the flip of the links (x, nu) with x_nu = 0 for each nu with k_nu = 1. It is an involution that keeps du. So T C^k is the integral operator with kernel A_T(u, Z_k w) (substitute w' = Z_k w). Tr(T^(t-1)(T C^k)) is the cyclic integral with A_T(u_(t-1), Z_k u_0) in the last factor (A0 (e); the same proof as Lemma 1.1 (iv) of `gap-seed-check.md`, for one or several flips). A_T > 0 by (1a), so dividing by Z gives the expectation, under the slice marginal of the torus measure (1.3), of A_T(u_(t-1), Z_k u_0)/A_T(u_(t-1), u_0). In (1a), A_T(u, v) = exp(-(V(u) + V(v))/2) I(u, v), with I exactly the layer integral of the file. V(Z_k v) = V(v), because every spatial plaquette has an even number of flipped links. So the ratio is I(u, c^k v)/I(u, v). The kernel needs only t >= 2 (Lemma 1.1 (ii)); the file's t >= 3 is safe. The sentence after the proof also holds: the flip changes y_b to -y_b on the bonds (x, nu) with x_nu = 0 and nowhere else, so I(u, c_nu v) is the layer model with one antiperiodic seam in direction nu, and U = (1/8) sum over k != 0 of E(1 - I(u, c^k v)/I(u, v)) follows from Identity FL.

### Proposition TW (Section 4.2). HOLDS.

Re-derived step by step.
- **Step 1.** For b = (x, i) with x as start, y_b = (1/2) tr(h(x) M) with M = v_b h(x + e_i)^(-1) u_b^(-1) in SU(2). For x as end, y_b = (1/2) tr(h(x)^(-1) M'), M' = u_b^(-1) h(x - e_i) v_b, and tr(g^(-1)) = tr(g) gives the form (1/2) tr(h(x) M'^(-1)). A change of the neighbour changes M by a quaternion of length at most 2. (1/2) tr(h(x) Q) is the R^4 inner product of h(x) and conj(Q), so it lies in [-abs(Q), abs(Q)], and the exponent beta J_b y_b changes by a function of oscillation at most 4 beta abs(J_b) <= 4 beta. The step d <= osc/4 is the one of Lemma INF (checked, row 709). Sides at least 3 give six distinct neighbours, one bond each. So alpha <= 6 beta, for every background and every coupling vector in [-1, 1]. Holds.
- **Step 2.** With J = -1 on Sigma_0, exp(-beta(1 - J y_b)) = exp(-beta(1 - y_b(c_nu v))). So I_1 = I(u, c_nu v), and d/dtheta log I_theta = -2 beta sum over Sigma_0 of <y_b>_(J^theta). Holds.
- **Step 3 (the flip maps J^theta to K^(1 - theta)).** H = {0 <= x_nu <= j_1 - 1} with j_1 = floor(b_nu/2) >= 1. The direction-nu bonds with one end in H: from b_nu - 1 to 0 (Sigma_0; b_nu - 1 is not in H since j_1 - 1 < b_nu - 1) and from j_1 - 1 to j_1 (Sigma_1; j_1 <= b_nu - 1). Bonds of the other directions keep x_nu. Under h -> -h on H, y_b -> -y_b on exactly these bonds, and Haar measure is kept. So the weight with couplings J^theta becomes the weight with couplings -J on Sigma_0 and Sigma_1: on Sigma_0, -(1 - 2 theta) = 1 - 2(1 - theta); on Sigma_1, -1; elsewhere 1. That is K^(1 - theta). **Holds.** Since y_b(-h) = -y_b(h) on Sigma_0, <y_b>_(J^theta) = -<y_b>_(K^(1 - theta)). Then theta -> 1 - theta in half of the integral gives the displayed identity. Holds.
- **Step 4 (the distance).** J^theta and K^theta differ only on Sigma_1, so the one-site laws agree off D = {x_nu in {j_1 - 1, j_1}}. f = y_b, b in Sigma_0, has delta <= 2 at each of its two sites, so Delta(f) <= 4. In the neighbour graph each edge changes x_nu by at most 1 cyclically. The cyclic distances from {b_nu - 1, 0} to {j_1 - 1, j_1} are j_1 - 1 (from 0) and min(b_nu - 1 - j_1, j_1) (from b_nu - 1). Since b_nu - 1 - j_1 = ceil(b_nu/2) - 1 >= j_1 - 1, the distance is at least j_1 - 1 = floor(b_nu/2) - 1. **Holds.** (At b_nu = 3 it is 0 and the bound is the trivial 4/(1 - alpha); the statement is still true.) Lemma DC (checked, row 709, with the corrections of `gap-mid-check.md` Section 5) applies to sites in place of links, with mu the J^theta law (alpha <= 6 beta) and mu~ the K^theta law.
- **Step 5.** 2 beta x abs(Sigma_0) x (1/2) x 4 alpha^(floor(b_nu/2) - 1)/(1 - alpha) = 4 beta (abs(B)/b_nu) alpha^(...)/(1 - alpha). Holds.
- **Step 6.** For two or three flips the ratio telescopes into one-flip ratios with backgrounds c_(nu_1) v and so on. The one-flip bound is uniform in the background, so the logarithms add. 0 < Z[k] <= Z (Identity L gives Z[k] > 0; a joint eigenbasis gives Z[k] <= Z). 1 - x <= -log x for 0 < x <= 1. abs(log E R) <= sup abs(log R). The number of flips summed over the seven k != 0 is 3 x 4 = 12. So U <= (12/8) x 4 beta b^2 alpha^(floor(b/2) - 1)/(1 - alpha) = 6 beta b^2 alpha^(floor(b/2) - 1)/(1 - alpha). Holds, for every time extent.

**Independent hand test of the example (beta = 1/12, a = 25).** Route 1, the file's closed form: 6 beta (2a)^2 (1/2)^(a - 1)/(1/2) = 8 a^2 2^(-a). 8 x 625 = 5000, and 2^25 = 33,554,432, so U <= 1.4901 x 10^(-4). Route 2, the general bound with b = 50 and no closed form: floor(50/2) - 1 = 24; (1/2)^24 = 1/16,777,216 = 5.9605 x 10^(-8); 6 x (1/12) x 2500/(1/2) = 2500; 2500 x 5.9605 x 10^(-8) = 1.4901 x 10^(-4). Route 3, by flips: one flip costs at most 4 x (1/12) x 2500 x 5.9605 x 10^(-8) x 2 = 9.934 x 10^(-5); 12 flips over 8 give 1.4901 x 10^(-4). All three agree. 1.4901 x 10^(-4) < 1.5 x 10^(-4) < 1/4950 = 2.0202 x 10^(-4) = t/3 with t = 1/1650. **The example holds.**

**A consistency test of the form of the bound (GUIDE, by hand; not a proof).** Flat background u = v = 1, small beta. Expand in characters: exp((beta/2) chi_(1/2)) = sum over l of a_l chi_l, with a_0 = 1 + O(beta^2) and a_(1/2) = beta/2 + O(beta^3). A straight line of b bonds that wraps direction nu contributes (a_(1/2)/a_0)^b 2^(2 - b), about 4 (beta/4)^b. The seam changes its sign. So log(I(1, c 1)/I(1, 1)) is about -8 (beta/4)^b (abs(B)/b) at leading order. The bound of Proposition TW is 4 beta (abs(B)/b)(6 beta)^(floor(b/2) - 1)/(1 - 6 beta), larger by many orders for small beta. The bound decays with rate (1/2) log(1/(6 beta)) per unit length, against the leading rate log(4/beta). There is no conflict.

### Lemma P (Section 4.2b). HOLDS.

Re-derived. R (h_e -> -h_e) keeps S^3, the uniform law and <h, F> because e is orthogonal to F, so it keeps mu_F, and E_F(h_e) = 0. E(phi h_e) = (1/2) E((phi(h) - phi(Rh)) h_e) and abs(h - Rh) = 2 abs(h_e) give abs(Cov) <= E(h_e^2). By the O(3) symmetry about F, E(h_e^2) = (1 - E t^2)/3. d/dkappa E_kappa(t^2) = Cov_kappa(t^2, t) = (1/2) E((t - t')(t^2 - t'^2)) = (1/2) E((t - t')^2 (t + t')). **The sign of Cov(t^2, t).** The base law of t (density proportional to (1 - t^2)^(1/2) on [-1, 1]) is even. Average the integral of (t - t')^2 (t + t') e^(kappa(t + t')) with its image under (t, t') -> (-t, -t'). This gives the integral of (t - t')^2 (t + t') sinh(kappa(t + t')) against the base law, up to the positive factor Z_kappa^(-2). Since s sinh(kappa s) >= 0 for kappa >= 0, the derivative is >= 0. **The sign holds.** E_0(t^2) = 1/4, so E_F(h_e^2) <= 1/4. F = 0 is covered (every e is orthogonal).

### Corollary C (Section 4.3). HOLDS. Not new: it is Proposition P (a) of `gap-seed-limit.md` (row 700).

The proof holds. At each j, q_j = 5041 S(N_j; (2N_j)^3; beta_j) <= 5041 s < 1, and Corollary S3' gives m(L^3; beta_j) >= log(1/q_j)/N_j >= log(1/(5041 s))/N_j for every integer L >= 2N_j. The reading also holds. With 2 N_j a_j = ell, the physical gap m/a_j is at least 2 log(1/(5041 s))/ell on every cube of physical side at least ell. limsup in (PHYS-SEED) gives this for all large j. The doubling remark holds too: (1 + x)^64 - 1 <= 71 x for x <= 1/640 gives the bound 5041 s^2 at 2 ell. A small point: with the threshold 1/5041, P1 gives ell above 17.1 inverse physical masses, not 14.8 (14.8 is for 1/1650). The text says "at least 14.8", which is still true.

**Correction (repo first; changes the "new" claims of Part 3, 4.3, 5.1 and the RESULT of row 712).** The form (C) is already in the repository. `library/gap-seed-limit.md` (row 700), Section 5 ("Step 6: the scaling form"), states:
- (SEED-phys): there are ell_* and s_* < 1/5041 such that for every cutoff iota there is n_iota >= 3 with n_iota a_iota <= ell_* and S(n_iota; (2 n_iota)^3) <= s_*.
- Proposition P: the lattice gap of every cube of side 2^(k+1) n_iota is at least M_* a_iota, with M_* = log(1/(5041 s_*))/ell_*. Corollary C is Proposition P (a). The check of row 703 (`gap-seed-limit-check.md`, A10 and Part B) extends it to every integer side L >= 2 n_iota.
- Proposition P': the uniform passage to a continuum limit.

(PHYS-SEED) is (SEED-phys) with n a fixed in place of n a <= ell_*. Both are checked as conditional statements (row 703, A10, Claude Opus 5.5; same provider as the author of row 700, a different model). So three sentences are wrong as written:
- the Part 3 table ("(C) ... Not found ... New");
- 4.3 ("the uniform version is not written anywhere that I read");
- the RESULT of row 712, finding (1).
Credit row 700 for the form. The new content of 4.3 is the remark drawn from it: lattice results at fixed beta, from 1/18 to about 2, neither give (SEED-phys) nor are needed for it. That remark holds as logic. It does not say that such results cannot help as a model for the end point of a flow.

**Does the continuum statement need anything beyond Corollary S3' and the limit step? Yes. The limit step is Proposition P' of `gap-seed-limit.md` Section 5 (checked, row 703), and P' has open hypotheses of its own.** The full list:
1. (SEED-phys) along the cutoffs of the T0 continuum limit itself: the couplings beta_iota and the spacings a_iota of the T0 trajectory. A sequence chosen for (SEED-phys) alone says nothing about T0's limit. OPEN, the crux.
2. Corollary S3' (checked, rows 698, 699). It turns the seed into the gap on every cube; Proposition P and its all-sides form use it.
3. The limit step, Proposition P'. Sup norms do not survive the continuum limit, because renormalised observables have sup norms that grow with the cutoff. So the gap is carried by the transfer operator in the reflection-positivity norm (Proposition P (c), Theorem L3 (e)), then by `gap-os-equiv.md` (5a) to (5c). Checked as an implication, row 703.
4. **What P' still asks, all from the T0 chain:**
   - a continuum time-reflection datum D_inf with (P1) to (P3);
   - time continuity (P4);
   - (H2): the diagonal truncated reflected functions of the lattice versions of each observable converge at each t > 0;
   - (TOT): the vacuum and the vectors of the observable class are total in the Hilbert space of D_inf.

   All four are OPEN (`gap-seed-limit.md` Section 5, input (4)). The observable class of the existence account is the tr(F^2) sector only. So the gap that P' gives is a gap on the Hilbert space that this class generates, and (TOT) names that space.

The file's Corollary C plus "the passage from uniform gaps of periodic cubes to the limit theory" names item 3 but not item 4. Item 1, the coupling to T0's own cutoffs, is implicit in its "trajectory beta_j = beta(a_j)". **Name to use: (SEED-phys) + Proposition P' with its inputs (P1)-(P4), (H2), (TOT).** The compatibility of tori sides, an open input in row 700, is removed by row 703 Part B.

### P3 and P4 (Section 1.2; not named by the row, verdicts for completeness)

P3's identity log(1 + S(n; B)) = F(n, B) - n log lambda_0(B) HOLDS: it is Z = lambda_0^n (1 + S). The sizes after "GUIDE" are guides. P4's first sentence HOLDS: it is the last claim of Theorem S. The rest of P4 is a reading.

## Summary

| Statement | Verdict |
|---|---|
| P1 | HOLDS |
| P2 | HOLDS (for one twist it is sharper than consequence (3) of Identity FL, not weaker) |
| Remark 2.A (a) | HOLDS |
| Remark 2.A (c) | HOLDS AFTER CORRECTION: cite the Remark F3 point of `gap-seed-check.md` and Lemma 1.1 (iv), (v), extended to a twisted slice and several flips (two lines, written above) |
| Proposition T1 | HOLDS |
| Proposition T2 | HOLDS (it refutes the short wording; the earlier work used the "at every coupling" form) |
| Proposition T3 | HOLDS AFTER CORRECTION: M' must be in the class of the tool |
| Corollary of 3b.3 | HOLDS AFTER CORRECTION: "is sound" becomes "if sound"; Bakry and Emery has no proof of the seed; the stop range 0.1 to 0.33 is GUIDE |
| Lemma COV | HOLDS (the case a = b = D/2 - 1 and the trace formula with a layer insertion re-derived) |
| Lemma REG | HOLDS given (TM-gen) (plaquette count and the step to differentiability re-derived) |
| Proposition V | HOLDS AFTER CORRECTION, as an implication from van Enter and Shlosman's Theorem 2 in a reading (stated for SU(n), proof sketched for U(1) in d = 3 only) and (TM-gen): (b) proves S >= 1/5041; add the line through Theorem SH (i) to get the 1/1650 seed, or write 1/5041 in the summaries; the mark "THM" in 3b.2 becomes PROVED GIVEN |
| Identity L | HOLDS |
| Proposition TW | HOLDS (Step 3 and the distance in Step 4 re-derived; example passes three hand routes) |
| Lemma P | HOLDS (the sign of Cov(t^2, t) re-derived) |
| Corollary C | HOLDS; not new: Proposition P (a) of `gap-seed-limit.md` (row 700), checked row 703 |

**Defects, ranked by what they break.**
1. **The form (C) is claimed as new, and it is not** (Part 3 table, 4.3, 5.1, RESULT finding (1)). (SEED-phys), Proposition P and the uniform limit step P' are in `gap-seed-limit.md` Section 5 (row 700, checked row 703). Credit row 700. No proof breaks. Item 5 of 5.2 (the lead note) should cite (SEED-phys) and P', not record (PHYS-SEED) as new. The limit step the file leaves unnamed is P', with its open inputs (P1)-(P4), (H2), (TOT) from the T0 chain.
2. **Proposition V's threshold** (3b.2, 4.1, 5.1). As written, the seed of Theorem SH (1/1650) is not excluded, only the seed of Theorem S (1/5041). The one-line repair through Theorem SH (i) is above. Until it is added, a tool aimed at 1/1650 is not refuted by Proposition V.
3. **The inputs of Proposition V** are unchanged from the author's own marks. Theorem 2 of van Enter and Shlosman is stated for SU(n) but sketched only for U(1) in three dimensions with a square well. Its printed normalisation has to be read. (TM-gen) for this weight is not checked (row 717). Proposition V is an implication from these, not a theorem.
4. T3 and the Corollary of 3b.3: wording (one hypothesis, two words). The logic is unchanged.
5. Remark 2.A (c): citation only.

RESULT: check of `library/gap-crux-fp.md` (row 716; Claude Opus 5.5 high, checking Claude Fable 5.2 max): no statement fails. P1, P2, Remark 2.A (a), T1, T2, Lemma COV, Lemma REG, Identity L, Proposition TW (with the hand test of its example, 1.4901 x 10^(-4) < 1/4950) and Lemma P hold. Remark 2.A (c), T3, the Corollary of 3b.3 and Proposition V hold after correction; Proposition V needs one line through Theorem SH to exclude the 1/1650 seed, and it still rests on van Enter and Shlosman's Theorem 2, stated but sketched only for U(1) in d = 3, and on (TM-gen). Corollary C holds but is Proposition P (a) of `gap-seed-limit.md` (row 700): the form (C) is not new. The continuum gap needs, beyond Corollary S3', the limit step P' and its open T0 inputs (P1)-(P4), (H2), (TOT), with (SEED-phys) proved along T0's own cutoffs. Open: (SEED-phys), (TM-gen) (row 717), and the full text of van Enter and Shlosman (row 717).
