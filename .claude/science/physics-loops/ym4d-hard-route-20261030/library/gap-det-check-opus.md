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

### Step 4. The ports of row 987 Step 4 (L324-367), re-read at the source (02:20Z)

Sources re-read. Sussman and Alpoge's repository (with Claude and Codex as authors of their text) was shallow-cloned at HEAD c7fef8b into my own scratch folder `/tmp/gapdetcheck989/sa`; this is the same HEAD rows 986-987 used. The repository's own notes were read at 2956379f1: `library/hma.md`, `library/hm.md`, `library/pr-lay.md`.

**Port 1, YM3_I II-44-37 and II-45 (L329-344): FAITHFUL; two line references need correcting.**
- "f_b(Y;P) = 3 log c_N - sum (1/n) tr T_Y^n(b,b)", T_Y = 1 - c_N^{-1} A_{Y,N}, ||T_Y|| <= q_N < 1: YM3_I L40737-40748 (eq. II-44-14). Verbatim.
- The Moebius inversion is eq. II-44-16 (L40751-40754), inside the proof of II-44-37 (statement L40673-40716). The statement itself is about the field-dependent part: its local terms vanish at P_0, and Phi_t(P) = log Z_k[P] - log Z_k[P_0] (II-44-40). The trivial-background numbers are a separate definition, II-45-8 (L60818-60826): n^(j)(X,b) = -(1/2) E^N(X;P_0,b). Their bound is II-45-65 (L60833-60836). Row 987 quotes both correctly.
- **Line correction.** The quote "The same change of coordinates ... does not introduce a choice of a larger torus" is at L60846-60849, not L60843-60846. Row 986's range L60813-60846 also stops one sentence short. Nothing depends on this.
- III-7-12 (statement L65353-65371). It compares two tori: the per-volume extensive coefficients cancel, "depend on the common coupling sequence and fixed constants alone. Their contributions per volume therefore cancel" (L65450-65452). The common-domain local terms also cancel, through a common function on the infinite grid (L65454-65463), and the noncommon terms are bounded. Row 987's "compares two tori term by term" is a fair summary.
- **One point the port leaves out.** YM3's extensive coefficients II-192-10 (L60870-60876) are not all Gaussian. co^s_j = -(L^3-1) log z(x_j, eps_j) is a restricted Haar integral, and co^b_j depends on x_j. They are torus-free only for a common coupling sequence. Row 987's (S1) scalar part does assume a common sequence (L417-419), so this is consistent.

**Port 2, YM4_1400 eq:flow-RF61 (L345-356): FAITHFUL.**
- The display (L86270-86282) and the explanatory text (L86283-86297) match the quotes.
- RF61 writes log(c_k(theta_k) Z^(k)(1)) = N^(k) + sum_X sum_z n^(k+1)(X,z), and n_k^tot = 36 N_{k+1} log L - (1/2) log det(C^T Delta^(k) C)|_1.
- "Has the shape of (S1)" is a reading, and fairly marked as one, with two conditions. First, log c_k(theta_k) must be a count times a torus-free scalar; the quoted lines name c_k ("the actual change-of-variable normalization") but do not define it. Second, n_k^tot must be the total of the local numbers. The name suggests this; RF61 does not state it.
- The bound |log det| <= #coordinates x max(|log gamma|, |log B|) is the form |n_k^tot| <= C N_{k+1}, with C depending on L. Correct given (S2), and marked ARGUED. The local family and the first-step sign are correctly listed as not addressed.

**Port 3, hma D3, D5 and Theorem 5 (L357-367): FAITHFUL.**
- D3 (3) is quoted verbatim (hma L37-44). D5 (L190): S = I for the full Gaussian. Theorem 5 (16) (L211-215) holds "at every complete admitted pair", so at P_0 in particular.
- The text after (21) (L275) and the remark at L277 ("SA 17528-17545 uses the compressed determinant in (21), together with elimination factors z^(j)"; "this determinant theorem does not prove the z^(j) bounds") are quoted correctly.
- Row 987 uses only D3's form and the (21) scalars, and does not use N_S or (19). The claim "this row does not depend on hma's premise list M beyond the two statements quoted in Step 5" is right.

**hm (4) and pr-lay R (quoted in row 987 Step 5): FAITHFUL.**
- hm Lemma 1 (4) (L53-59): there are labelled majorants m_omega with max(sup_x sum_{y,omega}, sup_y sum_{x,omega}) e^{mu_W t_omega} m_omega(x,y) <= W, t_omega >= d(x,y), and W >= max(1, c_L). d is the periodic l^inf distance of base points (hm L13).
- hm L42 (import W): "At global pairs the resulting fixed-region expansion sums to the actual symmetric precision (7) of pr-lay". hm L49: "All imported constants/floors are uniform in depth, volume, region shape and larger admitted layer gaps."
- pr-lay R (L99) is quoted verbatim. pr-lay W (L103): "all inverses in (6)-(7) exist". pr-lay L24: twelve coordinates. pr-lay L74: imported maps. pr-lay L83: SA 10200-10208.
- **Citation correction (row 987 L373).** Row 987 says pr-lay (7) "equal at a real axial V to hma's A^Y (hma D2, L30: 'At a real axial V it is SA 7181-7182')". The cited sentence is about the nonlinear Y factor, not about the two precisions. hma D3 (L46) says its form is "PR-lay (6)-(8) with the Y gauge term", so the two forms differ only in the gauge term, K_GF against G^Y_V. They agree at a real axial V by hma Lemma 1 (4)-(5) (L58-68). At an axial V, v = I, so Phi^Y_V(D) = GF(e^{iD}V), and Hess_0 Phi^Y_V = K_GF. U = 1 gives V = 1, which is axial. The claim holds after this citation change. Lemma 1 (5) also gives J_GF = 0 at V = 1, so pr-lay's completed form (9) equals (7) there and import F is not needed.

### Step 5 (part 1). (S3), and what the account itself writes for the step normaliser (02:45Z)

**(S3) (row 987 L382-391): HOLDS.**
- CA-II L64638: "Consider the torus T_m at cutoff K, with lattice spacing eps = L^{-K}". L64666 puts reflection hyperplanes at x_0 = 0 and x_0 = L^m, so T_m has physical side 2L^m. The level-j spacing is L^{j-K}, so the level-j lattice has 2L^{m+K-j} sites per side, as row 987 says.
- The step-j free coordinates are level-j bonds (pr-lay L24: "non-pivot level-k bonds" at depth k = j; hm L11-13). The free set is periodic under L-block translations. Replacing d n^4 by #X_n = d_L (n/L)^4 in Lemma A' is harmless. The proof uses only a free Gamma-action and the base-point distance, as row 987 says (L388-391).
- **Missing point.** The coordinate set must itself be Gamma-invariant: the pivot pattern on T_m' must be the pull-back of the pattern on T_m. Row 987 lists this under (I-loc) (L405-408), so it is not hidden. It belongs to (S3) as well.

**A source row 987 did not use: the account transcribes Balaban CMP 119 (3.33).** CA-I `4.24:prf-bond-densities` (L106091-106165, file `YM4/Old/theorem_0_complete_account_raw_I.tex` at c7fef8b), proof, L106125-106131:

> "In [(3.33)]{B-CMP119} the normalising integral is written, in the notation used there, in the form exp[-(1/2) log det(C^* Delta^(k) C) + sum_c log z^(k)(c) + const], where C is the map by which the delta-functions are eliminated; the same place states that the first term already has the localised form."

L106147-106150: const_s is "(N/2) log 2 pi plus the constants of the measure of [(3.33)]{B-CMP119} for the cells of Z^s. These are numbers, and they are distributed over the cells and bonds of Z^s."

The repository already had this pointer. `library/pd.md` L1195-1197 says "The scalar logarithm in (26) agrees with Balaban CMP 119 (3.33)-(3.36), as identified in CA-I 106109-106150". `library/cv-claude.md` L137-146 describes CMP 119 (3.28)-(3.38) from a reading of the scan on another machine. Its account: (3.28) is the step's integral; (3.34)-(3.36) write the log determinant of C^* Delta^(k) C as a resolvent integral; (3.33) carries a real constant.

**Consequence for row 987 (to be weighed in Step 6).** The account's normaliser has the (S1) shape in its own words: per-cell factors z^(k)(c), plus a constant spread over cells and bonds, times det^{-1/2}(C^* Delta^(k) C). But its form is Balaban's C^* Delta^(k) C, with C the delta-elimination map. Row 987 instead ports (S2) from pr-lay (7), which is C_V^T[... + K_GF]C_V, with C_V the pivot-graph derivative and K_GF the soft-gauge Hessian. These are two parametrisations of the step. Their determinants are not equal without a further identity. A gap for pr-lay's form does not give a gap for C^* Delta^(k) C: K_GF >= 0 (hma Lemma 1 (5) writes G^Y as a sum of squares), and removing a positive term can close a gap. So (S2) as ported covers the repository's form, not the account's form (ID). Row 987 says this in Step 6 (L486-491), so the mark "OPEN input" stands. Step 6 below checks how much of (ID) the files here settle.
