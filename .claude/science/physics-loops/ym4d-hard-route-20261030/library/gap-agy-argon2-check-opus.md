lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T13:11Z

# gap-agy-argon2-check-opus — cross-provider check of row 1207 (`library/gap-agy-solve2-argon.md`)

Started 2026-11-20T01:11Z (date -u). Worker: Mac mini Claude worker 3, branch `claude/ym4d-hard-route` pinned at `beea72f25`.
Queue row: FINISH.md row 1208.

## Plan (at most eight steps; each step appended below as it finishes)

1. Read the row 1207 file, FINISH.md rules (Build on published work, efficiency), GOAL.md, and the row 1180 file with Lemma R4; list every PROVED statement of row 1207.
2. Check Theorem 2.1 line by line: does the Doob representation remove the volume penalty of row 1180 Lemma R4?
3. Check Theorems 2.2-2.4 (cross-ratio bound on s_+) line by line.
4. Check Theorems 3.1-3.3 line by line.
5. Novelty: grep library/open-core.md and the FINISH rows; classify each statement as new / on file (row) / trivial / wrong.
6. Optional numeric guide (only if memory_pressure shows at least 50 percent free; guide only, not proof).
7. Rate the file against the lane plain-brief rows 1188-1190 (as checked in row 1196).
8. Verdict table and RESULT line.

## Step log

### Step 1 (done). Inventory and sources

Provenance: Claude Opus 5.5 (max effort), Mac mini worker 3, commit `beea72f25`. This is one cross-provider check by one model of a gemini-4-argon-high text (row 1207). It is not an audit.

Read in full: `library/gap-agy-solve2-argon.md` (row 1207, 328 lines). Read for the questions: row 1180 `library/gap-mini-neutral-fable.md` Step 3a (Lemma R4, L208-226; Lemma R7, L228-239); FINISH.md rows 1180, 1205-1208. The row 1206 check of row 1205 (`library/gap-agy-argon-check-opus.md`) does not exist at this commit, so nothing here rests on it.

Statements the file labels PROVED (or PROVED GIVEN), in its order:

| # | Statement | Where |
|---|---|---|
| S1.1 | Reduction of the Jaffe-Witten gap to (N-phys) plus the continuum datum (PROVED GIVEN rows 1161, 1179, 1183) | L19-25 |
| T2.1 | (1) F_+ = M C_E M on H_00 without projections; (2) pointwise eigen-identity (2.3), (2.4); (3) Doob form (2.5)-(2.6) of P_0 | L62-80 |
| T2.2 | (1) Dirichlet form (2.7); (2) two-step identity (2.8), conditional variance (2.9) | L88-102 |
| T2.3 | (1) centred-kernel formula (2.11); (2) pointwise chi-square bound (2.12), two-step trace bound (2.13) | L104-122 |
| T2.4 | (1) t-step Doob form (2.15)-(2.16); (2) cross-ratio identity (2.17); (3) identity (2.18) and two-replica bound (2.19) | L130-155 |
| T3.1 | (1) backward-plaquette forces (3.2) and n_z cancellation (3.3); (2) decomposition (3.4); (3) two-link marginal equation (3.6) | L169-194 |
| T3.2 | (1) exclusivity of the backward corner links; (2) locking (3.7), (3.8); (3) read-set criterion (3.9) | L200-213 |
| T3.3 | (1) invariance of S^+_mu, A^0_in,mu, L_mu under the two-link shift; (2) kernel constraints (3.14), (3.15) | L223-237 |
| T4.1 | multi-tree Jacobian formula (4.2) and Bessel bounds (4.3), (4.4) | L247-259 |
| T4.2 | Casimir eigen-identity (4.6), commutators (4.7), (4.8), Casimir-force identities (4.9), (4.10) | L267-287 |
| Tab5.1 | "PROVED (Exact Verification Against Comparison Models)" table | L295-302 |

The row asks for 2.1-2.4 and 3.1-3.3 first. Theorems 4.1, 4.2 and the Table 5.1 label are checked after them, because the row asks for every PROVED statement.

First reading, to be verified in Steps 2-4: all of Section 2 is the ground-state (Doob) transform of F = M C_E M, written out. Every identity there is exact and elementary. No estimate of any eigenvalue ratio is derived. Both inequalities, (2.13) and (2.19), still contain lambda_0, and (2.19) is an expectation under a law built from psi_0.

### Step 2 (done). Theorem 2.1 and the volume-penalty question

**Verdict T2.1: HOLDS. Already on file and trivial. Its headline claim, that it removes the volume penalty of row 1180 Lemma R4, FAILS as a claim of substance (no bound is produced, and the penalty factor sits inside the Doob kernel, see (P) below).**

Line by line.

- (1), L65-66, L76. M is a function of the plaquette traces, so it is gauge invariant. A centre flip multiplies the mu-links of one slice x_mu = c by -1. A plaquette meets that slice in 0 or 2 such links, so M is flip invariant. h_beta is a class function, and it is even under (U_e, V_e) -> (-U_e, -V_e). So C_E(gU, gV) = C_E(U, V) for gauge maps and flips, and C_E commutes with P and P_+. Hence F_+ = M C_E M on H_00. Correct.
- (2), L67-70, L77. The eigen-equation divided by M(U) > 0. psi_0 is continuous and positive because psi_0 = lambda_0^{-1} M C_E M psi_0 with a smooth positive kernel. Both identities of (2.4) follow by multiplying or dividing (2.3) by w_0 = M psi_0. Correct.
- (3), L71-74, L78-80. P_0 f = (lambda_0 psi_0)^{-1} M C_E(w_0 f), and lambda_0 psi_0 = M C_E w_0 by (2.3). So P_0 f = C_E(w_0 f)/C_E w_0. The second form of K_0 in (2.6) follows from (2.3). Its row integral is 1. Correct.

On file (each read at this commit):

- The Doob (ground-state) chain P = psi^{-1} U psi of the transfer, with pi = psi^2 dx and density p_t: row 1161, `library/gap-solve9-astra62.md` L17. Also row 807, `library/gap-block-astra.md` (B6), L178-183, and row 738, `library/gap-means-astra.md` L627-631.
- F = D C D on the gauge-invariant space, h = D psi, lambda = <h, C h>, and "the vacuum equation gives D^{-1} psi = C h / lambda": row 1161 L248. With D = M and h = w_0 this is (2.3) word for word.
- The quadratic form of (2.5), <f, P_0 f>_pi = <M psi_0 f, C_E(M psi_0 f)> / lambda_0: row 1205, `library/gap-agy-solve-argon.md` Theorem 2.1(2), L76, L82-84.
- Smoothness and positivity of psi_0: row 1180 L234-235; row 807 L170-174.

New in row 1207: the names w_0, h_0 and the operator form of row 1205's quadratic form. Nothing else.

**The volume-penalty question (the row's main question).** Answer: no. The Doob representation does not remove the volume penalty of row 1180 Lemma R4, for three reasons.

(a) Theorem 2.1 is an exact identity. It estimates nothing, so it can neither carry nor remove a loss. The loss of Lemma R4 belongs to one bound: lambda_k(F) <= ||D||^2 lambda_k(C), with lambda_0 <= 4 ||D||^2 exp(-2 c_4 n^3) (row 1180 L208-226; it HOLDS by row 1187). Row 1180 names its first failing step at L167-168: "the comparison trace does not carry the vacuum energy of F". The Doob form carries the vacuum energy exactly, but only through the unknown w_0 = M psi_0, that is, through psi_0 and lambda_0. The difficulty moves into w_0. It is not solved.

(b) **(P) The penalty factor is inside the Doob kernel.** From (2.3), (C_E w_0)(U) = lambda_0 w_0(U) / M(U)^2. Put this in (2.6):

    K_0(U, V) = (M(U)^2 / lambda_0) * C_E(U, V) * (w_0(V) / w_0(U)).

So the density of the Doob kernel against the electric kernel is (M(U)^2/lambda_0) (w_0(V)/w_0(U)). On the diagonal V = U it equals M(U)^2/lambda_0. At the flat configuration (all links 1) this is ||M||_inf^2 / lambda_0 >= exp(2 c_4 n^3)/4, by Lemma R4. At the configuration with every spatial plaquette equal to -1 it is exp(-3 beta n^3)/lambda_0. That configuration exists for even n: U_(x,1) = 1, U_(x,2) = (-1)^(x_1), U_(x,3) = (-1)^(x_1 + x_2). Hence any comparison of the Doob chain with the electric chain C_E that is uniform in U loses at least the factor of Lemma R4. A comparison that is not uniform needs pointwise control of w_0(V)/w_0(U), that is, of psi_0. This is a two-line consequence of the file's own (2.4).

(c) The bounds the file derives from the representation, (2.13) and (2.19), still contain lambda_0. (2.19) is also an expectation under a law built from psi_0 (Step 3). The record already says the exact vacuum subtraction is the Doob chain and that what is missing is an estimate on it: row 962, `library/gap-constraints-max.md` L110, item 16 ("the vacuum is subtracted exactly (lambda_0^a)", FORCED-M; "the Doob chain and (LSI-J) are the exact subtraction"). Row 934 (VAC-SUB) and row 738 (M5-G) state such estimates. Both stay OPEN.

What would count as removing the penalty: a bound on s_+(u; n), or on a neutral eigenvalue ratio, that is uniform in n and does not use ||M||_inf. Row 1207 gives none.

**Step 2 addendum (prior record found after the text above).** All of Theorem 2.1 is already row 863, and so is the answer to the penalty question.

- Row 863, `library/gap-crux-skeleton-max.md` L108-110, I1 (slice chain): "Write T = e^(-V/2) K e^(-V/2) ... With g := e^(-V/2) Omega one has K g = lambda_0 e^(V) g and P(U, dU') = K(U, U') g(U') dU' / (K g)(U). So the slice chain is the product kernel K tilted by g at the arrival point (a Doob transform)." With e^(-V/2) = M, K = C_E (projected) and g = w_0, this is (2.3), (2.5) and (2.6) of row 1207, symbol for symbol. Row 879 (Codex astra xhigh) checked row 863: I1 HOLDS and I2 HOLDS (`library/gap-crux-skeleton-check-astra.md` L230, L235), and B2 HOLDS AFTER CORRECTION.
- Row 895, `library/gap-glue-max.md` L218, Stop 2 ("comparison with the free kernel; PROVED limit"): "P(U, dU') = K(U, U') g(U') dU'/(K g)(U), g = e^(-V/2) Omega (I1) ... Any comparison of the Dirichlet forms of P and K through the oscillation of g (Holley-Stroock), or of cross-ratios (Hopf, B2), has an extensive exponent: log g is a sum over the box. So it gives m_ev at least exp(-c |B|) and nothing at the seed size." This is point (b) above, in general form. Row 896 checked row 895 as a whole: "FAILS as written overall", and its RESULT does not name Stop 2. Point (P) above rederives the part used here from (2.4), so this verdict does not rest on row 895. Row 896's check (`library/gap-glue-check-astra.md` L45) also describes the soft route's ground-state transform with a minorization, lambda/lambda_0 <= 1 - exp(-2 beta n_s). That exponent also grows with the volume. I did not read that file myself.

So the row's question was answered on 2026-11-13, by rows 863 and 895: the Doob form is the exact vacuum subtraction, and every known comparison through it has an extensive exponent. Row 1207 neither cites nor improves on this. Final verdict for T2.1: HOLDS. Already on file (row 863 I1; also rows 1161 L17 and L248, 807, 738, 1205). Trivial. Its claim to remove the Lemma R4 penalty FAILS: the penalty sits inside the kernel (row 895 Stop 2; (P) above).

### Step 3 (done). Theorems 2.2, 2.3, 2.4

**T2.2: HOLDS. Already on file in substance, and trivial.**

- (2.7), L90, L96-99. ||f||_pi^2 = lambda_0^{-1} \int w_0 (C_E w_0) f^2 dH by (2.4). <f, P_0 f>_pi = lambda_0^{-1} <w_0 f, C_E(w_0 f)>. Expand C_E w_0 as a double integral, symmetrize in (U, V) with C_E symmetric, and subtract. Correct. It is the usual Dirichlet form (1/2) \iint (f(U) - f(V))^2 pi(dU) K_0(U, dV), because pi(dU) K_0(U, V) dH(V) = lambda_0^{-1} w_0(U) C_E(U, V) w_0(V) dH dH.
- (2.8), L92, L100-102. Substitute (2.5) and (2.4). Correct.
- (2.9), L94, L102. The law of total variance for one step of the stationary chain. It uses \int P_0(f^2) d pi = \int f^2 d pi, which holds because f^2 is again invariant. Correct.
- On file: row 863 B3, `library/gap-crux-skeleton-max.md` L208-211, has the increment (Dirichlet) form of the slice chain. Row 738 (M5-G), `library/gap-means-astra.md` L633-636, has the form (1/2) \int pi(dx) P(x, dy) |f(x) - f(y)|^2. Row 1205 Theorem 2.1(2) has the one-step quadratic form. New: only the w_0 notation.

**T2.3: HOLDS as mathematics. Trivial. Its descriptive claims FAIL: it is not "without volume loss", and it does not "eliminate" psi_0 in any sense that matters.**

- (2.11), L108, L115. Subtracting the rank-one term adds zero, because \int w_0 (C_E w_0) f dH = lambda_0 \int f d pi = 0. Correct.
- (2.12), L110, L116-118. The kernel of P_0 against pi is k(U, V) = lambda_0 C_E(U, V) / ((C_E w_0)(U) (C_E w_0)(V)), with \int k(U, V) d pi(V) = 1. Pointwise Cauchy-Schwarz in L^2(pi) gives (2.12). Correct.
- (2.13), L112, L118-122. First equality: F_+ = M (P_+ P C_E) M is the restriction of F to H_00, so \iint M^2 Cbar_E^2 M^2 dH dH = Tr_{H_00} F_+^2 = lambda_0^2 (1 + s_+(2; n)). Correct. Inequality: k is the Doob density of the unprojected F = M C_E M on all of L^2(H). Its top eigenvector is psi_0 by Perron-Frobenius, and psi_0 lies in H_00. So the right side equals Tr_{L^2(H)}(F^2)/lambda_0^2 - 1, the sum of (lambda_i/lambda_0)^2 over every excited eigenvalue of F in all gauge and centre sectors. The inequality is Tr(Q F^2 Q) <= Tr(F^2) for the projection Q = P_+ P. Correct.
- What the statement really is. The first equality is the definition of s_+(2; n), written as a squared Hilbert-Schmidt norm. Row 863 I2 (L112-114) has it in chi-square form: S(2s; B) is \iint (p_s - 1)^2 nu nu. The inequality only enlarges the trace from H_00 to L^2(H). The trace Tr_{H_00}(F_+^2)/lambda_0^2 never contained psi_0, so nothing is "eliminated" (L113). lambda_0, the vacuum energy that row 1180's R4 is about, is still in both sides. Neither side is estimated. So "without volume loss" (title, L104) describes nothing proved. Correction: drop the claim, and read (2.13) as "s_+(2; n) <= sum over all excited states of F on L^2(H) of (lambda_i/lambda_0)^2".
- GUIDE, not used in any verdict. At fixed beta the two-step trace counts every local excitation of the cube. At strong coupling the single-plaquette states alone give about 3 n^3 (beta/4)^8. So s_+(2; n) grows with n, and no route can carry (N-phys) at u = 2. (N-phys) is useful at u_j near n_j/K (L23).

**T2.4: HOLDS as stated in (2.14)-(2.19). Two claims around it FAIL: that psi_0, lambda_0 and M cancel from the bound (L128, L137, L324), and that the chi-square bound is "equivalent" to (N-phys) (L324).**

- (2.14), L131. F_+^t = (M Cbar_E M)^t = M Cbar_E (M^2 Cbar_E)^{t-1} M, with Cbar_E = P_+ P C_E. The kernel is positive, because P and P_+ are averages over measure-preserving group actions. Correct.
- (2.15), L134, L145. M (K_t^int w_0) = F_+^t psi_0 = lambda_0^t psi_0. Then (2.3) gives lambda_0^{t-1} C_E w_0. Correct.
- (2.16), L136, L145. M/psi_0 = M^2/w_0 = lambda_0/(C_E w_0) by (2.4), so p_t = K_t^int / (lambda_0^{t-2} (C_E w_0)(U) (C_E w_0)(V)). Correct.
- (2.17), L138, L146. A cross-ratio is unchanged by diagonal rescaling alpha(U) K alpha(V). Correct.
- (2.18), L140, L147-152. It uses \int p_t(U, .) d pi = 1, the symmetry of p_t, and \iint p_t d pi d pi = 1. Correct.
- (2.19), L142, L153-154. p_t(U, V') p_t(U', V) d pi(U') d pi(V') is a product of two probability measures. Apply Jensen, then integrate. s_+(2t; n) = \iint (p_t - 1)^2 d pi d pi holds because p_t - 1 is the pi-kernel of P_0^t on (invariant functions) minus constants. P and P_+ are orthogonal projections in L^2(pi) as well, since pi is invariant. Correct. The right side is E_swap[R_t^2] - 1, because E_swap[R_t] = 1.
- On file: (2.15)-(2.16) are I1 of row 863 at t steps. The cross-ratio cancellation (2.17) is row 863 B2, L202-203: "The cross-ratio of T(U,U') = e^(-V(U)/2) k_orb(U,U') e^(-V(U')/2) does not contain V". Row 863 used it with Hopf's theorem, and row 895 Stop 2 (L218) records that the cross-ratio route has an extensive exponent. s_+(2t) = \iint (p_t - 1)^2 is row 863 I2. New in form: the identity (2.18) and the two-replica bound (2.19). My grep of `library/` and FINISH.md for cross-ratio, replica and chi-square found no earlier copy. Both are elementary (one line of algebra plus Jensen).
- **Correction 1 (L128, L137, L324: "free of lambda_0^t, psi_0(U), and boundary M(U)").** Only the integrand R_t is free of them. The law in (2.19), P^swap = p_t(U, V') p_t(U', V) d pi^4, is built from pi = psi_0^2 dH and from p_t, which contains psi_0 and lambda_0. The joint law P_{pi,t}(dU, dV) = lambda_0^{-t} psi_0(U) F_+^t(U, V) psi_0(V) dH dH is the vacuum's two-slice law. So the bound is a psi_0-free function averaged under the full vacuum law. The vacuum is not removed.
- **Correction 2 (L324: "proving (N-phys) ... is equivalent to bounding the two-replica chi-square variance ... below 1/2"). FAILS.** (2.19) gives one direction only: chi^2 <= 1/2 implies s_+(2t; n) <= 1/2. The converse is false for reversible chains in general. Counterexample, by hand. Take the two-state chain on {0, 1} with pi = (1/2, 1/2) and p_t(x, y) = 1 + mu eps(x) eps(y), eps = +-1, 0 < mu < 1. Then s(2t) = mu^2. Put a = 1 + mu, b = 1 - mu. Enumerating the 16 quadruples gives E_swap[R^2] = (a^2 + b^2 + 4ab + a^4/b^2 + b^4/a^2)/8. At mu = 1/2 this is (9/4 + 1/4 + 3 + 81/4 + 1/36)/8 = 29/9. So chi^2 = 20/9 > 1/2, while s = 1/4 <= 1/2. The proof of Theorem 2.4(3) uses no Wilson structure, so the file gives no converse for the Wilson chain either. Size of the loss, by first-order expansion: p_t = 1 + sum_i mu_i phi_i(U) phi_i(V) gives R_t - 1 = sum_i mu_i (phi_i(U) - phi_i(U'))(phi_i(V) - phi_i(V')) + O(mu^2). Hence chi^2 = 4 s_+(2t; n) + (higher order) when the mu_i are small. For a product of N independent copies, 1 + chi^2 is about (1 + 4 s_1)^N against 1 + s = (1 + s_1)^N. So the criterion chi^2 <= 1/2 asks for roughly s <= (3/2)^(1/4) - 1, about 0.107, instead of 1/2. Only the last sentence is GUIDE.

Section 2 overall: every identity and inequality holds. Each is the ground-state (Doob) calculus of rows 863, 895, 1161 and 1205, or one line beyond it. None estimates s_+ or any neutral eigenvalue ratio. None touches (N-phys).

### Step 4 (done). Theorems 3.1, 3.2, 3.3

Conventions are those of row 1034 (`library/gap-sym-reg.md` L35-44). SU(2) is the unit quaternions. U_p = U_(x,mu) U_(x+e_mu,nu) U_(x+e_nu,mu)^(-1) U_(x,nu)^(-1). R_(l,a) is the derivative along U_l -> e^(eps e_a) U_l. R_(l,a) A = -N_l^a. D_l n = n_tail - Ad(U_l) n_head. Re(e_a q) = -e_a . Im(q).

**T3.1: FAILS as written. HOLDS AFTER CORRECTION.** The backward plaquette is transcribed with its factors in the wrong order. The n_z cancellation survives, and it is gauge invariance at z.

- The backward plaquette p^-_(mu nu) = (x; mu, nu), x = z - e_mu - e_nu, is the loop x -> z - e_nu -> z -> z - e_mu -> x. So U_p = U_Ptilde U_(l_nu) U_(l_mu)^(-1) U_Qtilde^(-1). With X := U_Ptilde^(-1) U_Qtilde (L169) and taking inverses and cyclic shifts under Re,

      A^-_(mu nu) = beta Re(U_(l_mu) U_(l_nu)^(-1) X) = beta Re(Z),   Z := U_(l_nu)^(-1) X U_(l_mu).

  Z is the holonomy of p^- based at z. L169 writes beta Re(U_(l_mu) X U_(l_nu)^(-1)) instead. That expression is not gauge invariant: under U_l -> g_tail U_l g_head^(-1) the factor g_z^(-1) g_(z - e_nu) does not cancel. Row 1205 (3.5) has the correct form, beta Re(U_(l_lambda) U_(l_kappa)^(-1) W^-) with W^- = U_Qtilde^(-1) U_Ptilde, which equals beta Re(Z). Row 1207 mis-transcribed it.
- Counterexample to the L169 formula: U_(l_mu) = i, U_(l_nu) = j, U_Ptilde = k, every other link 1. The true value is beta Re(k j (-i)) = beta Re(i i) = -beta. L169 gives beta Re(i (-k)(-j)) = beta Re(i k j) = +beta.
- Correct forces. Differentiate beta Re(U_(l_mu) U_(l_nu)^(-1) X) in U_(l_mu), and beta Re(U_(l_nu) U_(l_mu)^(-1) X^(-1)) in U_(l_nu). This gives N^(p-)_(l_mu) = beta Ad(U_(l_mu)) Im(Z) and N^(p-)_(l_nu) = beta Ad(U_(l_nu)) Im(Z^(-1)) = -beta Ad(U_(l_nu)) Im(Z). (3.2) has Z' := X U_(l_nu)^(-1) U_(l_mu) in place of Z. The proof (L188) uses one form of A^- for l_mu and a different one for l_nu. Only the second is correct. Its last step claims U_(l_mu)^(-1) U_(l_nu) X^(-1) is "conjugate to" U_(l_mu)^(-1) X^(-1) U_(l_nu) "by U_(l_nu)". That is false: conjugating the second by U_(l_nu) gives U_(l_nu) U_(l_mu)^(-1) X^(-1). Even true conjugacy would rotate Im, not keep it.
- Counterexample to (3.2) and (3.3): U_(l_mu) = 1, U_(l_nu) = i, U_Ptilde = j, U_Qtilde = 1. Then X = -j, Z = (-i)(-j) = k and Z' = (-j)(-i) = -k. Direct differentiation of A^- = beta Re(j i e^(-eps e_a)) gives N^(p-)_(l_mu) = beta k. (3.2) gives -beta k. Take n_(z - e_mu) = k, n_(z - e_nu) = i and any n_z. Using Ad(i) k = -k, the left side of (3.3) is beta (k - i) . k = beta. The right side of (3.3) is beta (k - i) . (-k) = -beta.
- Correction. Replace Im(U_Ptilde^(-1) U_Qtilde U_(l_nu)^(-1) U_(l_mu)) by Im(U_(l_nu)^(-1) U_Ptilde^(-1) U_Qtilde U_(l_mu)) = Im(Z_(mu nu)) in (3.2), (3.3), (3.4), (3.6), and in the proof of 3.2. With that change I rederived (3.3), (3.4) and (3.6) line by line, including the integration by parts in (U_(l_mu), U_(l_nu)) for (3.6). They hold. W^(2) is a function of (U_(l_mu), U_(l_nu), U_ext). Its U_(l_alpha)-dependence through A^0_(in,mu nu), which reaches l_mu and l_nu through the backward plaquettes p^-_(kappa mu) and p^-_(kappa nu), sits inside the total derivative R_(l_alpha,a)(e^(A_rest) W_alpha^a). So the derivation is right.
- Why n_z cancels. The gauge generator at z is G_a = sum_out e_a . R_l - sum_in (Ad(U_l) e_a) . R_l (row 1034 L76-79). It annihilates every plaquette. A backward plaquette has no outgoing link at z, so G_a A^- = 0 reads sum over alpha in {mu, nu} of (Ad(U_(l_alpha)) e_a) . N^(p-)_(l_alpha) = 0. Contract with n_z^a. That is the whole content of (3.3)'s cancellation. It is the plaquette-by-plaquette form of the STAR proof, so it is trivial and on file in substance. New in row 1207: the decomposition (3.4) by plaquette type, and the marginal (3.6).

**T3.2: HOLDS as stated. It is Lemma PRIV's elimination applied to the backward corner link: new as an instance, elementary.** One hypothesis must be added, below.

- (1) Exclusivity, L201, L211. The tails of the links of the other 17 plaquettes are z - e_kappa, z, z - e_kappa + e_lambda and z - e_kappa - e_lambda with {kappa, lambda} != {mu, nu}. For L >= 3 none of them equals z - e_mu - e_nu. A link with another tail is another link. Correct for L >= 3. The file says L >= 4.
- (2) Locking, (3.7) and (3.8). The conclusion does not use the form of the plaquette holonomy. Under the hypothesis, every term of (3.6), and of (3.4) for (3.8), except the p^-_(mu nu) term is independent of U_Ptilde. That term is v . Im(Z) with v free of U_Ptilde. As U_Ptilde runs over SU(2), Z = U_(l_nu)^(-1) U_Ptilde^(-1) (U_Qtilde U_(l_mu)) runs over SU(2), and Im(Z) is linear in U_Ptilde in R^4. An affine function on R^4 that vanishes on a subset of S^3 of positive measure vanishes on S^3. So v = 0, which is (3.7). The same holds for (3.8) and with U_Qtilde in place of U_Ptilde. The equivalent form of (3.8), D_(l_mu) n = Ad(U_(l_mu) U_(l_nu)^(-1)) D_(l_nu) n, is correct. The step is right after the T3.1 correction, and the conclusion does not change. Hypothesis to add: as in Lemma PRIV (row 1034 L216), the open set must have the form Omega'' x SU(2) with the last factor U_Ptilde, or at least have fibres of positive measure in U_Ptilde. Otherwise "does not depend on U_Ptilde" and the fibre argument are not defined.
- (3) Read-set sets (3.9), L207-213. Ptilde lies in z + D, z - e_mu + D or z - e_nu + D exactly when D contains (-e_mu - e_nu, mu), (-e_nu, mu) or (-e_mu, mu). The same check works for Qtilde with direction nu. Correct.
- On file and new. The method is row 1034's (A2), "eliminate through an extreme link variable. This is the proof of Lemma PRIV" (L358-360). Lemma PRIV (L214-232) is the forward case. The backward corner instance, which gives a locking relation in place of D_l n = 0, is not in row 1034 or row 1205 (grep of `library/gap-sym-reg.md` for "backward": only L246 and L255, both about other statements). The value is limited. (3.7) and (3.8) are constraints that a frame can satisfy, so on their own they exclude no frame, and they do not move Lemma O1 (row 1034 L349).

**T3.3: HOLDS, and it is empty. Its conclusion follows from row 1205's single-link equation with no further input. The claim at L45 that ker L_mu is finite-dimensional FAILS.**

- (1), L228, L236. Theta_h is the gauge map at y = z - e_mu + e_nu restricted to the two links Q_(mu nu) (head y) and P_(mu nu) (tail y). (U_Q h^(-1))(h U_P) = U_Q U_P, and U_P^(-1) U_Q^(-1) is unchanged. So S^+_mu and L_mu are invariant. Neither link lies in A^0_(in,mu): I checked all 15 plaquettes for L >= 3, which is row 1205 Theorem 3.2(2). Theta_h preserves Haar measure. Correct.
- (2), (3.13)-(3.15), L229-237. Correct. X_b^(mu nu) = R_(P,b) - (Ad(U_Q) e_b) . R_Q is the derivative of Theta_(e^(eps e_b)), because U_Q e^(-eps e_b) = e^(-eps Ad(U_Q) e_b) U_Q.
- Why it is empty. For almost every U_ext, W^0(.; U_ext) lies in ker L_mu[S(U_ext)] (row 1205 (3.7)). S(Theta_h U_ext) = S(U_ext), and Theta_h preserves the measure. So W^0(.; Theta_h U_ext) lies in the same kernel, and so does the difference Delta_h W^0. The theorem restates that the solution set of a linear equation is invariant under a symmetry of its coefficients. (3.15) is its derivative. No frame satisfies (3.14)-(3.15) without already satisfying row 1205 (3.7). The theorem adds no constraint.
- L45 says "the finite-dimensional kernel of L_mu on SU(2)". FAILS. L_mu W = 0 means the field Y = e^(Re(U S)) W satisfies sum_a R_a Y^a = 0. Counterexample family: for any F in C^inf(S^2), put f(U) = F(Ad(U^(-1)) e_1). Then R_1 f = 0, because Ad(e^(-eps e_1)) fixes e_1. So W = e^(-Re(U_(l_mu) S^+_mu)) (f, 0, 0) lies in ker L_mu. The kernel is infinite-dimensional.

Section 3 overall: no statement moves Lemma O1. Rows 1034 and 1205 already hold its two working tools, the gauge generator identity and extreme-variable elimination.

### Step 5 (done by 2026-11-20T01:33Z, date -u; Steps 1-5 ran from 01:11Z). Theorems 4.1 and 4.2, the Table 5.1 label, Section 1.1, and the novelty search

**T4.1: HOLDS AFTER CORRECTION (one sign). A trivial extension of row 1205 Theorem 3.3. Its last clause is conditional, not proved.**

- (4.2), L251, L258. Row 1207 (3.1) and row 1205 (3.10), (3.15) give div j(z) = -sum_in (D_l n) . N_l and rho_z = div(d - j)(z). Hence div d(z) = -sum_in sum_a R_(l,a) (D_l n)^a. This is also row 1034's STAR, with div d = sum_out d_l - sum_in d_l (L223). For w = Ad(P^(T_k)) v_k: D_l w = 0 on tree edges. On an incoming chord l, P_tail and P_z do not depend on U_l, and sum_a (R_(l,a) Ad(U_l) u)^a = sum_a (2 e_a x Ad(U_l) u) . e_a = 0. So div d^w(z) = **minus** sum_k sum over chords sum_a ((Ad(P_tail) - Ad(U_l P_z)) R_(l,a) v_k)^a. (4.2) has a plus sign. It inherits the sign of row 1205 (3.11), which contradicts row 1205's own (3.10) and (3.15). The sign is harmless for (4.3) and (4.4), which use squares.
- (4.3), (4.4), L253-255, L259. ||Ad - Ad|| <= 2, so |sum_a (M R_a v)^a| <= 2 sqrt(3) |R v|. There are at most 4 chords per site, and the chord sets in(z) \ T are disjoint over z. So the bound is 48 per tree. Cauchy-Schwarz over the m trees, or convexity when v_k = alpha_k v, gives the rest. Correct.
- Last clause, L256. Given (1/V) sum |div j^w|^2 >= c_w b^2 and (1/V) sum |div(j^w - d^w)|^2 <= (c_w/4) b^2, the triangle inequality gives sum |div d^w|^2 >= (c_w/4) b^2 V. With (4.4) this gives c_w/192, so the stated c_w/384 follows. But the lower bound on div j^w is an extra hypothesis with an unnamed constant. Row 1141's event bounds min over T and unit v_0 for one tree. A superposition sum_k alpha_k div j^(T_k, v) can cancel across trees. Correction: label the clause PROVED GIVEN that hypothesis. Scope: w_x is not a unit vector, so it is not a frame in row 1034's sense. Normalizing it destroys the linearity the proof uses.
- New only as an instance. On file: row 1205 Theorem 3.3 and row 1141's question. Trivial: linearity plus Cauchy-Schwarz.

**T4.2: (4.6), (4.7) and (4.9) HOLD. (4.8) FAILS (sign). The display at L279 FAILS for every beta > 0. (4.10) FAILS as derived.**

- (4.6), L271, L283. w_q = Re U_q is linear, as a quaternion, in each of its four links. For f(U) = Re(q U), R_a^2 f = Re(q e_a^2 U) = -f, so -Delta_e w_q = 3 w_q for e in q and 0 otherwise. Total 12. Correct. That 12 is the minimum on H_00 minus constants is row 1205 Theorem 2.2. That is row 1206's to check, not mine.
- (4.7), L273, L284. By the Leibniz rule, [-Delta, S] psi = (-Delta S) psi - 2 sum (R S)(R psi) = 12 S psi + 2 sum_e N_e . R_e psi. Correct.
- **(4.8), L275, L284. FAILS.** [[-Delta, S], S] psi = [-Delta, S](S psi) - S [-Delta, S] psi = 2 sum_e N_e . (R_e S) psi = -2 sum_e |N_e|^2 psi. So (1/2)[[-Delta_E, S], S] = **-** sum_e |N^sp_e|^2, a non-positive multiplication operator. The correct positive form is (1/2)[S, [-Delta_E, S]] = sum_e |N^sp_e|^2. Check on the circle: [[-d^2/dx^2, x], x] = -2. Counterexample on X: rotate one link to U_e = cos(phi) + i sin(phi) and set every other link to 1. The four plaquettes through e then have U_(q,e) = U_e, so N^sp_e = 4 sin(phi) i. Applied to psi = 1 at that point, the left side of (4.8) is -sum_(e') |N^sp_(e')|^2 <= -|N^sp_e|^2 = -16 sin^2(phi) < 0 for phi not in pi Z. (4.8) claims the value +sum_(e') |N^sp_(e')|^2 >= 16 sin^2(phi) > 0.
- (4.9), L277, L285-287. Expand |R(S psi)|^2, then subtract <S^2 psi, -Delta psi> = sum \int [2 S (R S) psi R psi + S^2 (R psi)^2]. Correct. It is the standard identity <psi, (1/2)[S, [L, S]] psi> = \int |grad S|^2 psi^2.
- Exact identity (proved here, for every smooth real psi): <S psi, (-Delta)(S psi)> = 12 \int S^2 psi^2 dH + sum \int S^2 |R psi|^2 dH. Proof: the first two terms of the expansion of |R(S psi)|^2 sum to sum_a \int (R_a S) R_a(S psi^2) = \int (-Delta S) S psi^2 = 12 \int S^2 psi^2.
- **L279 FAILS for every beta > 0.** Cancel E_pi[sum |N|^2] from both sides and use the exact identity. L279 then becomes 2 sum \int S^2 |R psi_0|^2 dH = 0. But psi_0 is smooth and not constant for beta > 0. Row 1180 L234-239: psi(0)/psi(pi) >= e^(2 beta) along a one-link geodesic, so R psi_0 is nonzero on an open set. S is a nonzero trigonometric polynomial, so S^2 > 0 on an open dense set. The integral is positive.
- **(4.10), L281, L287. FAILS as derived.** The proof's step "integrating the first two terms ... by parts ... yields (4.10)" yields 12 E_pi[S^2] with **no** middle term (exact identity above). (4.10) adds the term sum_e \int N_e . R_e(psi_0^2) S dH. By parts, that term equals E_pi[sum |N_e|^2] - 12 E_pi[S^2]. So (4.10) holds iff E_pi[sum_e |N^sp_e|^2] = 12 E_pi[S^2]. The file does not prove this. It holds at beta = 0, where pi is Haar and psi_0 = 1. GUIDE: at the flat configuration N = 0 while 12 S^2 = 108 n^6, so the equality is not expected once the vacuum concentrates near flat fields. Correction: drop the middle term.
- New in this form. My grep found no earlier copy, and "Casimir", "commutator" and "carre du champ" have no match in `library/open-core.md`. They are standard Leibniz-rule identities. Nothing downstream uses them.

**Table 5.1 (L295-302), labelled "PROVED (Exact Verification Against Comparison Models)": the label FAILS. Reclassify it as GUIDE.** Its entries are unproved assertions about other models. Examples: the cross-ratio "fails to concentrate ... because the massless photon mode persists"; "the chi-square variance in (2.19) is bounded below by the spectator variance chi^2_spec > 1/2"; "lowest non-zero eigenvalue of -Delta_E is O(1/n^2)" for a non-compact Gaussian field, where -Delta on R^E has spectrum from 0 and no gap. No entry has a proof in the file. Some may be true. None is PROVED.

**Section 1.1 (L19-25), PROVED GIVEN: HOLDS as a citation, already on file.** It matches the RESULT lines of rows 1161 (check 1162: HOLDS AFTER CORRECTION, credit only), 1179 (Theorem BP) and 1183 (main chain HOLDS AFTER CORRECTION). One correction from row 1183 is missing: the continuum datum needs (P1)-(P4), (H2) and (TOT) on the intended physical Hilbert space, not only (P4), (H2), (TOT) (L20). New: none.

**Novelty search (rule 0a).** I grepped `library/open-core.md` for Doob, cross-ratio, Lemma O1, backward, Casimir, commutator, spanning tree, chord, carre du champ, N-phys and chi-square: zero matches. That file is from 2026-11-06 and predates the gap lane, so it settles nothing. I grepped the FINISH rows and `library/` for Doob, cross-ratio, replica, chi-square, Dirichlet form, backward, carre du champ and double commutator, and read the hits named in Steps 2-4. Classification:

| Statement | Classification |
|---|---|
| T2.1 | on file: row 863 I1 (L108-110), also rows 1161 L17 and L248, 807 (B6), 738, 1205 Thm 2.1(2); trivial |
| T2.2 | on file in substance: rows 863 B3, 738 (M5-G), 1205 Thm 2.1(2); law of total variance; trivial |
| T2.3 | first equality = definition of s_+(2; n) (row 863 I2 form); inequality = restriction of a trace; trivial |
| T2.4 | (2.15)-(2.17) on file: row 863 I1, B2 (cross-ratio free of V); (2.18)-(2.19) new in form, elementary |
| T3.1 | wrong as written; after correction the n_z cancellation is gauge invariance at z (row 1034 STAR proof, L76-79); (3.4) and (3.6) new in form |
| T3.2 | new instance of row 1034's method (A2) and Lemma PRIV; elementary; constraint only |
| T3.3 | new in form, empty (follows from row 1205 (3.7)) |
| T4.1 | new instance of row 1205 Thm 3.3; trivial |
| T4.2 | new in form; standard; three of six displays wrong ((4.8), L279, (4.10)) |

### Step 6 (done 2026-11-20T01:33Z, date -u). Numeric guide (GUIDE only; no verdict rests on it)

Memory free was 63 percent (memory_pressure). The run held `scripts/lab_ops.py numeric-lock` (acquire confirmed; released after). It used nice, BLAS threads 1, a 2 GB RSS guard and python3 -I, and took seconds. The script and log are scratch files on the worker, `/tmp/ym4d-w3-argon2check/`, and are not committed. Pass criteria were written before the run: each hand counterexample must reproduce, and each corrected formula must match to finite-difference accuracy. Results:

- 200 random configurations. |A_true - A_(L169)| reaches 1.58, while |A_true - beta Re Z| <= 7e-16. Forces by central differences: the corrected (3.2) matches to 2e-10, and the file's (3.2) is off by up to 1.79. The corrected (3.3) matches to 3e-10, and the file's (3.3) is off by up to 2.90.
- The L169 example gives true -1 and file +1. The (3.2)/(3.3) example gives N_(l_mu) = (0, 0, 1) = beta k, left side of (3.3) = 1, and the file's right side = -1.
- (4.8) sign, one-link test with S = Re(q U): [[L, S], S] 1 = -0.977 = -2 |grad S|^2, and L S / S = 3.
- Two-state chain: chi^2 = 2.222222 = 20/9 at mu = 1/2, where s = 1/4. chi^2/s = 4.001, 4.030, 4.122 at mu = 0.01, 0.05, 0.1.

The run is a second derivation path for the algebra: finite differences of the plaquette action as defined, not my formulas. It agrees with Steps 3-5 at every point.

### Step 7 (done). Rating against the plain-brief rows 1188-1190 (as checked in row 1196)

Sources: the RESULT lines of rows 1188, 1189, 1190 and 1196, and the verdict headings of `library/gap-solve-abc-check-astra.md`. The "proved statements" sections (L22-134) have 23 verdicts: 18 HOLD, 5 HOLD AFTER CORRECTION, 0 FAIL. Every FAIL of row 1196 is in the "route verdicts" sections (L135-208), that is, on ARGUED deductions.

| Measure | Rows 1188-1190 (Fable 5.2 max, 51-59 min each) | Row 1207 (Argon high, 18 min) |
|---|---|---|
| Crux moved ((N-phys), Lemma O1, (BS), (W)) | none | none |
| PROVED statements that fail as written | 0 of 23 | 3 of 11 items: T3.1 (plaquette formula, (3.2), (3.3)); T4.2 ((4.8), L279, (4.10)); Table 5.1's PROVED label. T4.1 needs a sign fix |
| False headline claims | none among their PROVED statements; row 1196's FAILs hit ARGUED route deductions | five: penalty of Lemma R4 removed; "without volume loss"; psi_0, lambda_0, M cancel from the bound; chi-square bound "equivalent" to (N-phys); ker L_mu "finite-dimensional" |
| Record check before claiming new | yes; each lists its on-file matches (row 1190: 17 attacks screened, "the chi-square form" flagged as a restatement with no consumer) | no; Section 2 is row 863 I1, B2, I2 and row 895 Stop 2, none cited; Theorem 2.4's chi-square form is the restatement row 1190 flagged |
| New, correct, non-trivial content | Lemma PC (theorem-grade form of an ARGUED count), A7, A8 (pin-uniform Mermin-Wagner step, power-law bound), the Z_cube sum | (2.18)-(2.19) and T3.2: correct and new in form, but elementary, and neither has a consumer |
| Label discipline | PROVED / ARGUED / OPEN used as defined | a heuristic table labelled PROVED; a conditional clause (T4.1) inside a PROVED theorem |

Rating: row 1207 is below each of rows 1188-1190 on correctness, calibration and value, and ahead only on speed. Its correct material is the ground-state calculus already on file, restated with confident claims of novelty. One clear strength: the Section 2 algebra is clean and every identity in it is right. As a second data point after row 1205: no check of row 1205 (row 1206) exists at this commit, so I cannot say whether the error rate is stable across the two Argon sessions.

### Step 8 (done 2026-11-20T01:35Z, date -u). Verdicts, ranked defects, RESULT

Provenance: Claude Opus 5.5 max, Mac mini worker 3, commit `beea72f25`. One cross-provider check of row 1207 (gemini-4-argon-high), by hand. Not an audit. It grants no status. The numeric run of Step 6 guides only.

| Statement (row 1207) | Verdict | New / on file / trivial / wrong |
|---|---|---|
| T2.1 (1)-(3), (2.1)-(2.6) | HOLDS | on file (row 863 I1, L108-110; rows 1161 L17, L248; 807; 738; 1205); trivial |
| T2.1 claim: removes the volume penalty of row 1180 Lemma R4 | FAILS | wrong: the R4 factor is the diagonal density M(U)^2/lambda_0 of the Doob kernel against C_E (Step 2 (P)); row 895 Stop 2 has this |
| T2.2 (2.7)-(2.9) | HOLDS | on file in substance (rows 863 B3, 738, 1205); trivial |
| T2.3 (2.11)-(2.13) | HOLDS | trivial (definition of s_+(2; n), plus restriction of a trace) |
| T2.3 claims "without volume loss", "eliminating psi_0" | FAIL | wrong: nothing is estimated, and lambda_0 stays in both sides |
| T2.4 (2.14)-(2.19) | HOLDS | (2.15)-(2.17) on file (row 863 I1, B2); (2.18)-(2.19) new in form, elementary |
| T2.4 / L324 claims: the bound is free of psi_0, lambda_0, M, and "equivalent" to (N-phys) | FAIL | wrong: the law contains psi_0. Converse false: two-state chain, s = 1/4, chi^2 = 20/9 |
| T3.1 (1)-(3), L169, (3.2)-(3.6) | FAILS as written; HOLDS AFTER CORRECTION | wrong transcription of row 1205 (3.5). Replace by Z = U_(l_nu)^(-1) U_Ptilde^(-1) U_Qtilde U_(l_mu). The n_z cancellation is gauge invariance at z (row 1034 L76-79); (3.4), (3.6) new in form |
| T3.2 (1)-(3) | HOLDS (add: Omega a product in U_Ptilde, as in Lemma PRIV) | new instance of row 1034 (A2) and Lemma PRIV; elementary; excludes no frame |
| T3.3 (1)-(2) | HOLDS, empty | follows from row 1205 (3.7) alone; the claim at L45 of a finite-dimensional ker L_mu FAILS (infinite family given) |
| T4.1 | HOLDS AFTER CORRECTION (sign of (4.2); last clause PROVED GIVEN an unproved lower bound) | new instance of row 1205 Thm 3.3; trivial |
| T4.2 (4.6), (4.7), (4.9) | HOLD | standard |
| T4.2 (4.8) | FAILS (sign: (1/2)[[-Delta, S], S] = -sum_e N_e . N_e) | wrong |
| T4.2 display L279 | FAILS for every beta > 0 | wrong |
| T4.2 (4.10) | FAILS as derived (holds iff E_pi[sum_e N_e . N_e] = 12 E_pi[S^2], unproved) | wrong derivation; correct identity in Step 5 |
| Table 5.1 "PROVED" | FAILS as a label; GUIDE | unproved assertions |
| Section 1.1 PROVED GIVEN | HOLDS as a citation (add (P1)-(P3), row 1183) | on file (rows 1161/1162, 1179/1183) |

Ranked defects (what each breaks):

1. The main claim, that the Doob form removes the Lemma R4 penalty, is false. The penalty is the kernel's own diagonal density. Rows 863 and 895 had recorded this, so the strategy of the file (1.2 item 1, 5.3 item 1) starts from a known dead end.
2. "Equivalent" (L324) is false. (2.19) is sufficient only, and it loses a factor near 4 at small s.
3. The bound (2.19) is not free of the vacuum. Its law is the vacuum's two-slice law.
4. T3.1 has the wrong backward plaquette (not gauge invariant). Every displayed formula of 3.1 is wrong as written. The corrected forms are given.
5. T4.2: (4.8) has the wrong sign, L279 is false, and (4.10) is mis-derived.
6. T3.3 is empty, and its kernel claim is false.
7. Table 5.1 is labelled PROVED but contains no proofs.
8. T2.3's descriptive claims are unsupported.
9. T4.1 has a sign error, and its last clause is conditional.
10. Section 1.1 omits (P1)-(P3).

RESULT: Row 1208 (Claude Opus 5.5 max, Mac mini worker 3, cross-provider check of row 1207 gemini-4-argon-high, by hand, not an audit; numeric run guide only): Theorems 2.1-2.4 HOLD as identities and inequalities but are the ground-state (Doob) calculus already on file (row 863 I1, B2, I2; row 895 Stop 2; rows 1161, 807, 738, 1205, 1190) and estimate nothing; the claim that the Doob representation removes row 1180 Lemma R4's volume penalty FAILS (the R4 factor is the Doob kernel's own diagonal density M(U)^2/lambda_0), and so do "without volume loss", "psi_0/lambda_0/M cancel from the bound" and the "equivalence" of (2.19) with (N-phys) (two-state counterexample, s = 1/4, chi^2 = 20/9); Theorem 3.1 FAILS as written (non-gauge-invariant backward plaquette; explicit counterexamples) and HOLDS AFTER CORRECTION with Z = U_(l_nu)^(-1) U_Ptilde^(-1) U_Qtilde U_(l_mu), its n_z cancellation being gauge invariance at z; Theorem 3.2 HOLDS (Lemma PRIV's method on the backward corner link, new instance, elementary); Theorem 3.3 HOLDS but is empty, and its finite-dimensional-kernel claim FAILS; Theorem 4.1 HOLDS AFTER CORRECTION (sign; last clause conditional); Theorem 4.2's (4.6), (4.7), (4.9) HOLD, while (4.8) (sign), the display at L279 (false for every beta > 0) and (4.10) (mis-derived) FAIL; the Table 5.1 PROVED label FAILS (GUIDE); Section 1.1 HOLDS as a citation. Nothing in row 1207 moves (N-phys), Lemma O1, (BS) or (W), which stay OPEN with the continuum datum and the mass gap. Rating against the plain-brief rows 1188-1190 (checked in row 1196: 23 proved statements, 0 FAIL): row 1207 rates below each of them on correctness (3 of 11 PROVED items fail as written, plus 5 false headline claims), on calibration (no record check; on-file results claimed as new) and on value (no new non-trivial statement with a consumer); it is faster (18 min against 51-59 min). Output library/gap-agy-argon2-check-opus.md.
