lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T12:58Z

# Row 989, `gap-det-check-opus`: line-by-line check of row 987 (`library/gap-det-fable.md`)

Queue row 989 (FINISH.md L1067). Check item, no new attack. Checker: Claude Opus 5.5 max, Mac mini worker 3. Source checked: `library/gap-det-fable.md` at commit 2956379f1 (33905 bytes, written by Claude Fable 5.2 medium, row 987). Started 2026-11-15T00:58Z. No numeric run planned.

## Plan (at most eight steps)

1. Read FINISH.md rules (efficiency, build on published work), row 987's file in full, and the (DET) statement of row 986 that it claims to prove.
2. Check Lemma A (Step 2 of row 987).
3. Check Lemma P, Lemma A' and Corollary B (Step 3), with c_det and its powers of L.
4. Check the ports of Step 4: re-read the quoted lines of YM3_I II-44-37 and III-7-12, hm (4), pr-lay R and hma D3; faithful or not, each.
5. Check Step 5 (S1)-(S3), including the reading (I-loc) of the imported definitions as stencil operators.
6. (ID): can the account's step normaliser (Balaban CMP 119 (3.28)) be identified with hma's A_S from any file on this machine?
7. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with line), and the RESULT line.

## Step log

(Each step appends below when done.)

### Step 1. Inputs read (01:10Z)

- Read in full: `library/gap-det-fable.md` (556 lines). Its header says "Pinned at commit 708bcda9e"; the copy checked here is the one at 2956379f1.
- (DET) as row 986 states it (`library/gap-detlemma-read-opus.md` Step 6, L136-140): N = 2, notation of CA-II Definition 8.22, m, m' >= m_T(g_-(g)), G_m := sum_{j<K} G^(j)(T_m), and |G_m/(2L^m)^4 - G_m'/(2L^m')^4| <= c_det with c_det depending only on L and p, not on K, g_0, g, m, m'. The one-sided form for m' >= m suffices for (TH).
- Rules applied: FINISH "Working efficiently" and "Rules" (check report: provenance, verdict per statement, only defects that break something). This is a check of Claude Fable 5.2's text by Claude Opus 5.5: a different model of the same provider, one reading, not an audit.
- Overlap (rule 0a): this row checks row 987. It attacks no open lemma, so no open-core grep is owed. FINISH rows naming `gap-det`: 986, 987, 989 (this one) only.

### Step 2. Lemma A (row 987 L85-218): HOLDS (01:25Z)

Each step redone.

- (a) Schur: row sums of |A| are at most C_A by (A2) (the weight is >= 1); columns by (A0). So ||A|| <= C_A, and (A3) extends to l^2 by density. 0 <= T <= q = 1 - gamma/B. Correct.
- (b) |e^u - 1| <= e^{|u|} - 1 for real u, and the chord bound e^{rt} - 1 <= (r/mu_0)(e^{mu_0 t} - 1) on 0 <= r <= mu_0 (convex, zero at r = 0). So |A_theta - A|(x,y) <= (|theta|_inf/mu_0)|A(x,y)| e^{mu_0|x-y|}. A_theta - A is not symmetric, but its column sums are bounded by (A0) with the same weight. At |theta|_inf <= nu = mu_0 gamma/(2C_A): ||A_theta - A|| <= gamma/2, so ||T_theta|| <= q + gamma/(2B) = q'. The tilt of the identity kernel is the identity. Correct.
- (c) The multi-index sum for (T^k)_theta converges absolutely, because |theta|_inf <= mu_0 and the weighted row sums multiply. Kernel product equals operator product on l^2 for kernels with finite row and column sums (Fubini). The matrix element is at most q'^k. theta = nu sign(s-t) gives theta.(s-t) = nu|s-t|_1, and theta may depend on the pair (x,y). (A.2) is correct.
- (d) Per_n is well defined on classes (covariance in x; re-indexing in y). The interchange of sums is absolutely convergent. Per_n(1) = 1 because Gamma_n acts freely. The symmetry of S uses A1 with -v in Gamma_n, contained in lZ^4 because l divides n. Correct.
- (e) For each i >= 0, the two half-open intervals (a-(i+1)n, a-in] and [a+in, a+(i+1)n) each hold one multiple of n. So sum_w e^{-nu|a-nw|} <= 2/(1-e^{-nu n}), and c_0 is correct. The power argument gives |lambda| <= (d n^4 c_0)^{1/k} q' for every k, so |lambda| <= q'. Eigenvalues of A_n lie in [B(1-q'), B(1+q')] = [gamma/2, 2B - gamma/2]. Correct. (The weaker interval [gamma/2, 2B] is honest. Lemma P (iv) cannot be used here, because pi^* f is not in l^2(Z^4).)
- (f), (g) T^k is lZ^4-covariant, and T_n is (n/l)^4 disjoint translates of the cell C. The sum over w in Z of r^{|w|} is (1+r)/(1-r), so eps(n) = ((1+r)/(1-r))^4 - 1 = coth(nu n/2)^4 - 1. Its quotient by r is a series with non-negative coefficients, so eps(n) <= c_eps e^{-nu n} for n >= 1. Then sum_k q'^k/k = log(1/(1-q')) = log(2B/gamma). Both series sum_k tau_k/k and the wrap part converge absolutely. Correct.

**Verdict: HOLDS** as stated (L109-113). Remark 1 is correct but unused. Remark 3 is not written out and is not used. Lemma A is not on the path to (DET): Corollary B uses Lemma A' only (row 987 L308, L525-526).
