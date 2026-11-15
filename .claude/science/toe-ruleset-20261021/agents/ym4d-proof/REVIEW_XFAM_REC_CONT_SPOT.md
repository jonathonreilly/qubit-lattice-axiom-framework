# Cross-family spot review of REC-CONT: exhaustion and how it uses E0′ (2026-10-29)

**Reviewer:** Claude (Anthropic). The note was written by Codex and reviewed twice by Codex, so this is a cross-family check. **Scope:** part (2) of REC_CONT.md only, the sparse-coordinate exhaustion and its use of E0′. Part (1), the seed constants (3.2)–(3.3), is out of scope. Every conclusion here is conditional on that part.

**Verdict: SOUND.** I found no gap and no error in part (2). The checks below are mine, not adopted from the earlier reviews. Line numbers refer to REC_CONT.md at the PR head.

1. **Constant recursion (6.6) and majorant (7.1), l.527–532, l.659–670.** Cauchy–Schwarz at each cut, together with (m!)² ≤ (2m)! and r! ≤ r^r, gives A_{n,N} ≤ D K^n n^{γn} Q^{nN} with Q = 16^t 2^γ. The growth in N is exponential, not super-factorial.
2. **Geometric factor (6.7), l.562–565.** |P′| ≤ (25/2)|P| holds.
3. **Sparse-support induction (8.3), l.701–725.** Both cases hold: support of size 2h−1 and support of size 2h, the latter averaged over the two middle cuts. The induction uses convexity of the closure and radial shrinking (l.693–697). The radius r_{h,N} = P(Bin(N,1/2) ≥ h), so the tail bound 2^{h−1}(3/4)^N is correct.
4. **Entrance depth (8.1), l.743–753.** N ≤ 1 + [h log 2 + log π + log(R/δ)]/log(4/3) holds. Minor: ε < 1/π always, so the ε = 1 case at l.740 is vacuous.
5. **Final bound (8.2), l.755–767.** The exponent p_n = tn + 2n log Q/ℓ_0 is linear in n. The bound is polynomial in 1/min τ_j, as tempered boundary values require.
6. **Quantifiers and the use of E0′.** SEED in degree 2^N n requires hierarchy-wide constants; (3.2) states them "uniformly in n" (l.171–175, l.1010). The linear seminorm order is load-bearing (l.567–569): a superlinear order would turn the bound into a power of R/δ.
7. **Domain.** The §8 union is exactly the product of right half-planes in the time gaps, so no envelope-of-holomorphy step is needed. The tube comes from §9 by Fourier–Laplace. I spot-checked §9.2 (rotation → boost identities and spectral support); it is valid. §9.3 was not checked.
8. **RC-LIFT mixed angles.** The solidity of U supplies them (l.460–466).

**Non-blocking notes.**
- (a) B_n ~ Q^{O(n²)} (l.775). This is acceptable only because L-CONT allows constants that depend on n, so a later step that needs bounds uniform in n cannot reuse it.
- (b) Part (1), the seed constants, still needs cross-family review.
