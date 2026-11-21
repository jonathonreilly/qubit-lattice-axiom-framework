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

### Step 5 (part 2). (S1), (S2) and the reading (I-loc) (03:05Z)

The outline file `YM4/YM4_sketch_500.tex` at c7fef8b has SHA-256 d7f77d4d...4d6f. That is the hash `library/mu.md` L17 records for the SA outline at 31a47c543775, so SA line numbers apply to it unchanged.

**The form at U = 1 (row 987 L371-380): HOLDS.**
- With all Omega_j equal to the torus, the separation condition pr-lay (1) is vacuous. At depth k the cut sequence has the single scale xi_k = 1, so the row weights a are constant.
- J = 0 at P_0 = (1,0,0). Delta'_pi[J] is linear in J and vanishes, so G = G_0 = G_1 and E_amb[...J] = 0. Row 987's display follows from pr-lay (6)-(7).
- This form is also the outline's own step precision. SA L10200-10206: "Let C_V be the elimination of the pivot bonds, and let G^(2)_V be the quadratic part of the soft axial gauge fixing ... A = C_V^T(G^(2)_V + Delta_k)C_V". SA L14095-14104 says the same.

**(S1), periodization (L393-410): the deduction HOLDS; (I-loc) stays a reading, now partly confirmed.**
- The deduction holds. Suppose every primitive on T_n is the periodization of the same rule on Z^4, i.e. its torus kernel is Per of the infinite-lattice kernel, which holds once the torus is larger than the stencil. Then Lemma P (rectangular (i)-(ii), and (iii) for the four inverses) gives A_{j,K,m} = Per(A_{j,K,m'}). The inverses exist on the larger torus by pr-lay W (L103). The order of operations in pr-lay (6) (G', then R, then G_0, then (Q G_0 Q^T)^{-1}) is respected.
- (I-loc) is confirmed for three primitives by the definitions I read.
  - Pivots: SA L8167-8169, "The pivot of c = (y,y+Le_mu) is b_0(c) = (y+he_mu, y+(h+1)e_mu)". This is one fixed rule per coarse bond. So the pivot pattern on T_m' is the pull-back of the pattern on T_m. That settles the coordinate-set point of Step 5 (part 1).
  - Blocks and torus room: SA L7946-7954, B(y) = {x : |x-y|_inf <= (L-1)/2}. "A sufficient condition for a cubic torus is that its period exceeds 4L+4". Every level-j torus here has side 2L^{m+K-j} >= 2L^{m+1} > 4L+4, the smaller torus included.
  - Soft axial gauge: SA L7180-7182, GF_k(V) = sum_{y,x} [1 - (1/2) Re tr V(y,x)] over block contours. It is block-local and the same in every block, and its Hessian at V = 1 is K_GF.
- Not read here: the straightened averages Q, Q' (SA QC1-QC4, L7943-8001, beyond the block definition) and the weights a on tops. At U = 1 these are block-local linear maps, but I did not check them line by line. The mark ARGUED on (I-loc) is accurate and should stay.

**(S1), scalar part (L412-420): ARGUED, and better supported than row 987 says.**
- The outline states the step constant explicitly. SA L7493-7495: E^(k)(Omega,Lambda) = (log sigma_H(0) - (1/2)(N^2-1) log x_k)|Omega^(k)*| - (L^4-1) log z_G #_{k+1}(Omega) + nu_g |Lambda^(k)*| + sum_X [E^(k+1)+R^(k+1)](X,1).
- YM4_1400 L102650-102656: "the Haar and Gaussian factor is one scalar per nonpivot bond and the gauge-fixing factor is one scalar per cell of the next lattice. The common coupling sequence and fixed choice of gauges give the same two scalars for the two tori".
- Both make the scalars torus-free counts given a common sequence. Row 987's citation "YM4_1400 L102576" points at a different sentence (the cancelling number A_K). The right lines are L102650-102656.
- For the account's own normaliser, the per-cell factors z^(j)(c) are defined only by citation: CA-I (n1), L104002-104005, "the normalisation factors of [B-CMP119]". Their value at U = 1 therefore belongs to (ID).

**(S2) (L422-442): HOLDS as a port, conditional as marked.**
- Gap: pr-lay R applies at U = 1, which has real bound 0 and is block axial (c_b(1;x) = I). So gamma = c_L.
- (A2'): |v|_1 <= 4|v|_inf for the minimising l^inf lift. So sum_y |A(x,y)| e^{(mu_W/4)|x-y|_1} <= sum_{y,omega} e^{mu_W t_omega} m_omega(x,y) <= W. That gives mu_0 = mu_W/4 and C_A = W.
- B = W by Schur. The uniformity is hm L49, and hm L47 says the precision is exactly pr-lay (7).
- Hence nu = mu_0 gamma/(2C_A) = mu_W c_L/(8W), as row 987 L448 writes. With d replaced by d_L/L^4, its c_det at L447 is Corollary B's constant, up to the c_det(0) correction of Step 3.
- **Correction (L436-437).** "torus room ... on the LARGER torus only" is right for (S2), which uses (A2') and (A3') for A' only. But (S1) uses the definitions on the smaller torus as well. The room there holds by the 4L+4 bound above, so nothing breaks.
- The conditionality is stated honestly at L438-442: R and W rest on a2-layers, a2-curved and the h-walk gate repairs. This check did not trace them either.

**(DET) for the repository's step form (L444-452): HOLDS AFTER CORRECTION.** Replace c_det by its m = 0 value (Step 3) and fix the two citations (Step 4: hma Lemma 1 (4); here: YM4_1400 L102650-102656). The mark "PROVED as an implication from (I-loc), R, W" is then accurate.

### Step 6. (ID): can it be settled from files on this machine? No; it can be narrowed (03:20Z)

**Balaban's text is not here.** `~/ym4d-papers` exists on this machine now; it arrived at 00:57Z, after row 987 looked at 00:50Z. It holds cmp96, cmp98, cmp99a, cmp99b, cmp102, cmp122a and cmp122b. Its README lists cmp89, cmp95, cmp109 and cmp119, but those four files are absent, and CMP 116 is not listed. So CMP 119 (3.28) and (3.33), CMP 116 and CMP 109 (1.7) and (2.4)-(2.13) cannot be read here. Row 987's reason for leaving (ID) open still holds.

**What the files here do give: three links, each a reading or a sketch, none a proof.**

1. **The account's normaliser has the (S1) shape, in its own transcription.** CA-I L106125-106131 and L106147-106150 (Step 5, part 1): Z^(k) = exp[-(1/2) log det(C^* Delta^(k) C) + sum_c log z^(k)(c) + const]. The constants are "distributed over the cells and bonds". This is the account's reading of CMP 119 (3.33), not Balaban's text.
2. **The outline identifies Balaban's form with the repository's form.** SA L10208, "(1c.1)": "At the pair (U_{k+1}, J(U_{k+1})) of the step, one has A = C^T Delta^(k) C. In this identification (1c.1), the elimination and the gauge-fixing term are obtained directly from the definitions. The only step of substance is the quadratic term of the action of the background ... This is Balaban's expansion 102, 277, (174), together with 109, (2.4)-(2.8), (2.11)." Here A = C_V^T(G^(2)_V + Delta_k)C_V (SA L10202-10206), which is pr-lay (7). At U = 1 the step's pair is (1, J(1)) = (1, 0), because the Wilson action is stationary at U = 1. So (1c.1) at U = 1 says: Balaban's C^* Delta^(k) C at 1 equals row 987's A_j. This is a sketch with citations, not a proof. CMP 102 (174) is on this machine (`cmp102.txt` L1156); CMP 109 is not.
3. **The repository has a theorem of the same kind for the outline's step.** hma Theorem 8 (L367-372), G-ID(cov). Under M, PH1-PH4 and D2, at every admitted complete physical pair, the Gaussian part (22) of the step has covariance A^Y(P_W)^{-1}. At U_+ = 1, P_W = (1,0,0) = P_0. Whether PH1-PH4 hold at U_+ = 1 was not checked here. These are the BG package, criticality, branch match and normalisation, at the flat background. Theorem 8 concerns the outline's step (22). It does not concern Balaban's Z^(k) of CMP 119 (3.28).

**What (ID) reduces to (OPEN; no attack made here):**
- **(ID-a) Scalars.** At U = 1, every z^(k)(c) of CMP 119 (3.33), and every per-cell constant of its measure, is one number per cell, the same on every torus for a common coupling sequence. In the account, z^(j)(c) is defined only by citation: CA-I (n1), L104002-104005. The 3D analogue is YM3_I II-45-8: the pivot value 6 log L at P_0. The 4D target is YM4_1400 RF61: 36 N_{k+1} log L. Neither is CMP 119.
- **(ID-b) Form.** (1c.1) at U = 1: Balaban's C^* Delta^(k) C at 1 equals pr-lay (7) at P_0. The outline gives only a sketch citing CMP 102 (174) and CMP 109 (2.4)-(2.11). Alternatively, hma Theorem 8's PH1-PH4 at U_+ = 1, together with the statement that the account's step is the outline's step (22).
- Given (ID-b), row 987's (ID)(ii) is no longer separate. The uniform gap and decay of Balaban's form at 1 are then (S2) for pr-lay (7), which row 987 already ported from R and W. Row 987 Step 6 (L489-491) instead sends (ID)(ii) to the flat package of row 95. That route is possible but not needed.

**Verdict on row 987 Step 6 (L454-491): HOLDS AFTER CORRECTION.** (ID) is correctly marked OPEN. CA-I's transcription of CMP 119 (3.33) and the outline's (1c.1) are on this machine, and they narrow (ID) to (ID-a) and (ID-b), both still cited and not proved.

**Correction (L483-484).** "On a torus with no large-field region and U = 1 there is no conditional step and no elimination factor, so only the full determinant S = I occurs (ARGUED)". The first half is right: S = I. The phrase "no elimination factor" is wrong.
- The outline's step operation carries z^(j) at every step (SA L17531): T^(j) = ... z^(j) ∫ dA' .... Its strip identity (SA L17544-17547) reads: sum_c log z^(j)(c) - (1/2) log det(C^T Delta^(j) C restricted to Lambda_{j+1}) = number + sum_X N(X, U_{j+1}).
- CA-I (n1) takes the product over "the cells c of the region where the delta-functions were eliminated". At U = 1 with no large-field region, Lambda_{j+1} is the whole torus, so there is one factor z^(j)(c) for every cell.
- This is harmless to (DET) exactly when (ID-a) holds: the factors are then part of the torus-free c_{j,K} of (S1). Repair: replace the phrase by "the elimination factors z^(j)(c) occur once per cell; (S1) needs them torus-free at U = 1, which is (ID-a)".

### Step 7. Verdict per statement, and RESULT (03:35Z)

Provenance: Claude Opus 5.5, max effort, Mac mini worker 3, at commit 2956379f1. This is one line-by-line reading of row 987 (Claude Fable 5.2 medium). It is a different model of the same provider, not an audit, and not an independent derivation. No numeric run was made. Sources read: Sussman and Alpoge's repository (with Claude and Codex as authors of their text) at HEAD c7fef8b, in scratch `/tmp/gapdetcheck989/sa`, not committed; `~/ym4d-papers` (listing only); the repository notes hma, hm, pr-lay, pd and cv-claude.

| Statement in row 987 (lines) | Verdict | Where / correction |
|---|---|---|
| Lemma A, infinite lattice to torus (L109-202) | HOLDS | Step 2. Not on the path to (DET). |
| Lemma P, periodization (L233-247) | HOLDS | Step 3; the rectangular form needs L \| n, which holds. |
| Lemma A', nested tori (L249-286) | HOLDS | Step 3. |
| Corollary B, c_det and its powers of L (L288-311) | HOLDS AFTER CORRECTION | The sum over u of L^{4u} eps(2L^{m+u}) is right, and so is the bound 15/(4 nu^5) L^{-5m}/(L-1). But c_det at the bottom of the range depends on g through m_T(g_-(g)) (L304, L450-451, L497-498). Use c_det(0) = (d/2) log(2B/gamma) c_eps (15/(4 nu^5))/(L-1). |
| Port: YM3_I II-44-14/16, II-45-8/65, III-7-12 (L329-344) | FAITHFUL | The quote at "L60843-60846" is at L60846-60849. |
| Port: YM4_1400 RF61 (L345-356) | FAITHFUL | "Shape of (S1)" is a reading, and is marked as one. |
| Port: hma D3, D5, Theorem 5 (16), (21) and L277 (L357-367) | FAITHFUL | |
| Quotes of hm (4), L13, L42, L49 and pr-lay R, W, L24, L74, L83 (L422-437) | FAITHFUL | |
| Form at U = 1, "equal at a real axial V to hma's A^Y" (L371-380) | HOLDS AFTER CORRECTION | Cite hma Lemma 1 (4)-(5) (v = I at an axial V), not D2 L30. |
| (S3) (L382-391) | HOLDS | CA-II L64638 and L64666 give side 2L^m and spacing L^{-K}. The pivot pull-back holds by SA L8167-8169. |
| (S1), periodization (L393-410) | Deduction HOLDS; (I-loc) stays ARGUED | Confirmed: pivots (SA L8167-8169), blocks and room (SA L7946-7954), soft gauge (SA L7180-7182). Not read: Q, Q', a. |
| (S1), scalar part (L412-420) | ARGUED; HOLDS AFTER CORRECTION | Cite YM4_1400 L102650-102656 (not L102576). SA L7493-7495 gives the step constant explicitly. |
| (S2) (L422-442) | HOLDS as a conditional port of R and W | The torus room is needed on the smaller torus too, for (S1). It holds, since every period exceeds 4L+4. |
| (DET) for the repository's step form (L444-452) | HOLDS AFTER CORRECTION | As an implication from (I-loc), R and W, with c_det(0). |
| "no elimination factor" at U = 1 (L483-484) | FAILS as stated | z^(j)(c) occurs once per cell (SA L17531, L17544; CA-I (n1) L104002-104005). Harmless exactly when (ID-a) holds. S = I is right. |
| (ID) marked OPEN (L454-491) | HOLDS | It is not settled on this machine. It narrows to (ID-a) and (ID-b) (Step 6). |
| Step 7 items 1-8 (L495-528) | 1: correction as for Corollary B; 2-4, 7 and 8 HOLD | Not re-read: item 5's citation CA-II L141426-141432 and item 6's report of the numeric lock. |

**Defects, ranked by what each breaks.** None breaks Lemma A', Corollary B or (DET) as an implication.
1. The m-dependence of c_det (wording; the fix is c_det(0)).
2. "No elimination factor" (L483-484). It is wrong, and it hides that the per-cell factors z^(j)(c) are part of (ID).
3. The citation for "pr-lay (7) = hma A^Y" (L373).
4. Two line references (L335-338, L419).

**(ID) on this machine.** It cannot be settled. CMP 109, 116 and 119 are absent from `~/ym4d-papers`; the README lists 109 and 119, but the files are not there. Two files narrow it:
- CA-I L106125-106131, the account's transcription of CMP 119 (3.33): Z^(k) = exp[-(1/2) log det(C^* Delta^(k) C) + sum_c log z^(k)(c) + const].
- SA L10208, the outline's (1c.1): A = C^T Delta^(k) C at the step's pair.

What is left:
- **(ID-a)** At U = 1, z^(k)(c) and the measure constants of (3.33) are torus-free numbers per cell.
- **(ID-b)** Balaban's C^* Delta^(k) C at 1 equals pr-lay (7) at P_0. The outline sketches this from CMP 102 (174), which is on this machine at `cmp102.txt` L1156, and from CMP 109 (2.4)-(2.11), which is absent.

Given (ID-b), the uniform gap and decay of Balaban's form need no separate input: they are (S2) for pr-lay (7).

**Next step (for the lead; not done here).** A reading row on a machine with CMP 119 and CMP 109: (ID-a) from CMP 119 (3.28)-(3.33), and (ID-b) from CMP 109 (2.4)-(2.11) with CMP 102 (174) at U = 1. A reading of SA QC1-QC4 (L7943-8001) would close the rest of (I-loc). The gpt-6-astra check of row 987 that FINISH row 989 holds for the Codex reset is still owed. This check does not replace it, being the same provider.

RESULT: Row 989 (Claude Opus 5.5 max, Mac mini worker 3; line-by-line check of row 987; same provider, different model; no numeric run). Lemma A, Lemma P and Lemma A' HOLD. Corollary B HOLDS AFTER CORRECTION: its powers of L and the bound 15/(4 nu^5) L^{-5m}/(L-1) are right, but the m-free constant is c_det(0) = (d/2) log(2B/gamma) c_eps (15/(4 nu^5))/(L-1). The ports are FAITHFUL: YM3_I II-44-14/16, II-45-8/65, III-7-12; YM4_1400 RF61; hma D3, D5, Theorem 5, (21); hm (4); pr-lay R and W. Two line references and one citation are corrected: pr-lay (7) = hma A^Y at an axial V is hma Lemma 1 (4)-(5). (S3) HOLDS. (S1) periodization HOLDS as a deduction from (I-loc); (I-loc) stays ARGUED, confirmed for pivots, blocks and the soft gauge, with Q, Q' and a not read. The (S1) scalars are ARGUED, supported by SA L7493-7495 and YM4_1400 L102650-102656. (S2) HOLDS as a conditional port of R and W. (DET) for the repository's step form HOLDS AFTER CORRECTION as an implication from (I-loc), R and W. Row 987's "no elimination factor" at U = 1 FAILS as stated: z^(j)(c) occurs once per cell, which is harmless only if those factors are torus-free. OPEN: (ID) cannot be settled on this machine, since CMP 109, 116 and 119 are absent. CA-I's transcription of CMP 119 (3.33) and the outline's (1c.1) narrow it to (ID-a), the per-cell factors z^(k)(c) and measure constants being torus-free at U = 1, and (ID-b), Balaban's C^* Delta^(k) C at 1 being pr-lay (7) at P_0. Also open: (I-loc) for the averages Q, Q' and the weights a; the imports R and W; the gpt-6-astra check.
