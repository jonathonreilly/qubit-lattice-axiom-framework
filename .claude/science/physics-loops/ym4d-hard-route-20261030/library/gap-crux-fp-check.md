lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-12T01:20Z

# Check of `library/gap-crux-fp.md` (row 716, `gap-crux-fp-check`)

Provenance: written by Claude Opus 5.5, high effort, Mac mini worker 2, on branch `claude/ym4d-hard-route` at commit 649a17386, started 2026-11-11T13:20Z. One line-by-line reading by one model of a file written by Claude Fable 5.2 max (row 712). Not an audit. No computer-assisted step; any script below is GUIDE only.

## Status block (kept current)

- Read whole: `gap-crux-fp.md` (503 lines); `gap-transfer.md` lead note of row 671, notation, A0, Section 1 ((1a)-(1c), (1.2), A0 (e)); `gap-crux-restate.md` Sections 1 and 3.4; `gap-mid-max.md` lead note of row 709, Section 6 (Identity FL) and Section 10; `gap-mid-check.md` Section 5. Also read: `gap-seed-check.md` Lemma 1.1 and its Remark F3 point (the twisted slice), `gap-mid-max.md` Lemma 4.1.
- Verdicts written so far: P1, P2, Remark 2.A (a) and (c), T1, T2, T3 and the Corollary, Lemma COV. Next: Lemma REG, Proposition V, Identity L, Proposition TW with the hand test, Lemma P, Corollary C.
- Not covered by this check: Sections 1.1, 1.3 to 2.7 (except Remark 2.A), 3, 3b.1, 3b.2, 3b.4, the GUIDE runs, (AS-bg), (vMF-Lip) and its reductions R-a, R-b, and the Brownian form in 4.2b. Row 716 does not ask for them.

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
