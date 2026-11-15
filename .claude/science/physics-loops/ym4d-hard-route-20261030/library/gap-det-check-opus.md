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

### Step 3. Lemma P, Lemma A', Corollary B (row 987 L220-322) (01:45Z)

**Lemma P (L233-247): HOLDS.**
- (i) The sum over y in X_n' splits into classes. Covariance makes the inner sum depend on x through xbar only. pi is onto, so pi^* is injective, and the matrix is unique.
- (ii) Uniqueness from (i) gives the product rule. Per(1) = 1 because Gamma acts freely. Per(K^T)(xbar,ybar) = sum_g K(y+g,x) = sum_g K(y,x-g) = Per(K)(ybar,xbar).
- (iii) K commutes with the permutation matrices of Gamma, so K^{-1} does too. Then (ii) applies to K K^{-1} = 1.
- (iv) Each fibre of pi has (n'/n)^4 points, so <pi^*f, pi^*h> = (n'/n)^4 <f,h>. With (i), <f,Per(K)f> = (n/n')^4 <pi^*f, K pi^*f>, and the bounds pass to Per(K).
- Rectangular form: (i)-(ii) carry over with pi on each index set. A coarse lattice needs L | n, so that Gamma preserves the coarse sites. In Corollary B this holds because n = 2L^{m+K-j} and K - j >= 1. (iii) and (iv) are used only for square matrices.

**Lemma A' (L249-286): HOLDS.**
- (A2') at y = x and (A3') at delta_x give gamma <= A'(x,x) <= C_A. So nu <= mu_0/2, and the chord bound applies with r = nu.
- Decay. |.|_n' is a pseudometric on X_n' (zero between two coordinates at one site), so |rho(z) - rho(w)| <= |z-w|_n'. E 1 E^{-1} = 1. The Schur bound uses (A2') and the symmetry of A'. (E^{-1} M E)(x,y) = e^{nu rho(x)} M(x,y) e^{-nu rho(y)}, with rho(x) = 0. (A'.1) is correct.
- Trace. Every lift of g in Gamma = nZ^4/n'Z^4 lies in nZ^4, because n | n'. So |x - (x+g)|_n' = |v(g)|_1, with v(g) a minimal lift. Distinct g give distinct v(g), and v(g) = 0 only for g = 0. The wrap part is at most #X_n q'^k eps(n). The diagonal part is (n/n')^4 tr T'^k by Gamma-invariance alone (row 987 Step 7.2 is right that LZ^4 is not needed).
- Logarithm. Lemma P (iv) applied to 0 <= T' <= q gives 0 <= S <= q < 1. The two series converge and subtract term by term. The bound is sum_k q'^k eps(n)/k = log(2B/gamma) eps(n). Correct.

**Corollary B (L288-311): HOLDS as an implication; the constant needs one wording correction.**
- Algebra. (S1) and (S3) give G^(j)(T_m)/(2L^m)^4 = L^{4(K-j)}[c_{j,K} - (d/2)(d n^4)^{-1} log det A_{j,K,m}]. The factor L^{4(K-j)} is the same at m and m', and c_{j,K} cancels exactly.
- Lemma A' applies with l = L, n = 2L^{m+K-j} and n' = 2L^{m'+K-j}: n | n', both are multiples of L since K - j >= 1, A' = A_{j,K,m'}, and Per(A') = A_{j,K,m} by (S1).
- Powers of L. With u = K - j in {1,...,K}, the error is (d/2) log(2B/gamma) sum_u L^{4u} eps(2L^{m+u}). Then eps(n) <= c_eps e^{-nu n}, and e^{-t} <= 5!/t^5 at t = 2 nu L^{m+u} gives L^{4u} e^{-2 nu L^{m+u}} <= (120/(32 nu^5)) L^{-5m} L^{-u}. Finally sum_{u>=1} L^{-u} = 1/(L-1). So c_det = (d/2) log(2B/gamma) c_eps (15/(4 nu^5)) L^{-5m}/(L-1) is right, and it is free of K and m'.
- What the volume factor costs. The step with u = K - j has volume factor L^{4u}, but its error is exp(-2 nu L^{m+u}), super-exponentially small in u. That makes the sum free of K. Any torus-wide O(1) term per step that (S1) did not absorb would instead cost K/(2L^m)^4. So (S1)'s exact "scalar times count" form carries the K-uniformity. That is a question about the inputs, checked in Steps 5-6 below, not about this corollary.
- **Correction (wording, L497-498 and L450-451).** "at the bottom of the range it is a number depending on L and p only" is not literally true. The bottom m_T(g_-(g)) depends on g, so c_det(m_T) does too. Repair: L^{-5m} <= 1 for m >= 0, so c_det(m) <= c_det(0) = (d/2) log(2B/gamma) c_eps (15/(4 nu^5))/(L-1). That value depends only on d, mu_0, C_A, gamma, B, L. Use c_det(0) as the (DET) constant. Nothing downstream changes.
- Two-sided. The tori 2L^m and 2L^m' are always nested, so the bound holds for every pair with min(m, m'). Correct.
