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

### Step 1 (done 2026-11-20 ~01:30Z). Inventory and sources

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

### Step 2 (done 2026-11-20 ~01:50Z). Theorem 2.1 and the volume-penalty question

**Verdict T2.1: HOLDS. Already on file and trivial. Its headline claim, that it removes the volume penalty of row 1180 Lemma R4, FAILS as a claim of substance (no bound is produced, and the penalty factor sits inside the Doob kernel, see (P) below).**

Line by line.

- (1), L65-66, L76. M is a function of the plaquette traces, so it is gauge invariant. A centre flip multiplies the mu-links of one slice x_mu = c by -1. A plaquette meets that slice in 0 or 2 such links, so M is flip invariant. h_beta is a class function, and it is even under (U_e, V_e) -> (-U_e, -V_e). So C_E(gU, gV) = C_E(U, V) for gauge maps and flips, and C_E commutes with P and P_+. Hence F_+ = M C_E M on H_00. Correct.
- (2), L67-70, L77. The eigen-equation divided by M(U) > 0. psi_0 is continuous and positive because psi_0 = lambda_0^{-1} M C_E M psi_0 with a smooth positive kernel. Both identities of (2.4) follow by multiplying or dividing (2.3) by w_0 = M psi_0. Correct.
- (3), L71-74, L78-80. P_0 f = (lambda_0 psi_0)^{-1} M C_E(w_0 f), and lambda_0 psi_0 = M C_E w_0 by (2.3). So P_0 f = C_E(w_0 f)/C_E w_0. The second form of K_0 in (2.6) follows from (2.3). Its row integral is 1. Correct.

On file (each read at this commit):

- The Doob (ground-state) chain P = psi^{-1} U psi of the transfer, with pi = psi^2 dx and density p_t: row 1161, `library/gap-solve9-astra62.md` L17. Also row 807, `library/gap-block-astra.md` (B6), L178-183, and row 738, `library/gap-means-astra.md` L627-631.
- F = D C D on the gauge-invariant space, h = D psi, lambda = <h, C h>, and "the vacuum equation gives D^{-1} psi = C h / lambda": row 1161 L248. With D = M and h = w_0 this is (2.3) word for word.
- The quadratic form of (2.5), <f, P_0 f>_pi = <M psi_0 f, C_E(M psi_0 f)> / lambda_0: row 1205, `library/gap-agy-solve-argon.md` Theorem 2.1(2), L76, L82-84.
- Smoothness and positivity of psi_0: row 1180 L232-233; row 807 L170-174.

New in row 1207: the names w_0, h_0 and the operator form of row 1205's quadratic form. Nothing else.

**The volume-penalty question (the row's main question).** Answer: no. The Doob representation does not remove the volume penalty of row 1180 Lemma R4, for three reasons.

(a) Theorem 2.1 is an exact identity. It estimates nothing, so it can neither carry nor remove a loss. The loss of Lemma R4 belongs to one bound: lambda_k(F) <= ||D||^2 lambda_k(C), with lambda_0 <= 4 ||D||^2 exp(-2 c_4 n^3) (row 1180 L208-226; it HOLDS by row 1187). Row 1180 names its first failing step at L168-169: "the comparison trace does not carry the vacuum energy of F". The Doob form carries the vacuum energy exactly, but only through the unknown w_0 = M psi_0, that is, through psi_0 and lambda_0. The difficulty moves into w_0. It is not solved.

(b) **(P) The penalty factor is inside the Doob kernel.** From (2.3), (C_E w_0)(U) = lambda_0 w_0(U) / M(U)^2. Put this in (2.6):

    K_0(U, V) = (M(U)^2 / lambda_0) * C_E(U, V) * (w_0(V) / w_0(U)).

So the density of the Doob kernel against the electric kernel is (M(U)^2/lambda_0) (w_0(V)/w_0(U)). On the diagonal V = U it equals M(U)^2/lambda_0. At the flat configuration (all links 1) this is ||M||_inf^2 / lambda_0 >= exp(2 c_4 n^3)/4, by Lemma R4. At the configuration with every spatial plaquette equal to -1 it is exp(-3 beta n^3)/lambda_0. That configuration exists for even n: U_(x,1) = 1, U_(x,2) = (-1)^(x_1), U_(x,3) = (-1)^(x_1 + x_2). Hence any comparison of the Doob chain with the electric chain C_E that is uniform in U loses exactly the factor of Lemma R4. A comparison that is not uniform needs pointwise control of w_0(V)/w_0(U), that is, of psi_0. This is a two-line consequence of the file's own (2.4).

(c) The bounds the file derives from the representation, (2.13) and (2.19), still contain lambda_0. (2.19) is also an expectation under a law built from psi_0 (Step 3). The record already says the exact vacuum subtraction is the Doob chain and that what is missing is an estimate on it: row 962, `library/gap-constraints-max.md` L110, item 16 ("the vacuum is subtracted exactly (lambda_0^a)", FORCED-M; "the Doob chain and (LSI-J) are the exact subtraction"). Row 934 (VAC-SUB) and row 738 (M5-G) state such estimates. Both stay OPEN.

What would count as removing the penalty: a bound on s_+(u; n), or on a neutral eigenvalue ratio, that is uniform in n and does not use ||M||_inf. Row 1207 gives none.

**Step 2 addendum (prior record found after the text above).** All of Theorem 2.1 is already row 863, and so is the answer to the penalty question.

- Row 863, `library/gap-crux-skeleton-max.md` L108-110, I1 (slice chain): "Write T = e^(-V/2) K e^(-V/2) ... With g := e^(-V/2) Omega one has K g = lambda_0 e^(V) g and P(U, dU') = K(U, U') g(U') dU' / (K g)(U). So the slice chain is the product kernel K tilted by g at the arrival point (a Doob transform)." With e^(-V/2) = M, K = C_E (projected) and g = w_0, this is (2.3), (2.5) and (2.6) of row 1207, symbol for symbol. Row 879 (gpt-6-astra) checked row 863 and records no failure for I1.
- Row 895, `library/gap-glue-max.md` L218, Stop 2 ("comparison with the free kernel; PROVED limit"): "P(U, dU') = K(U, U') g(U') dU'/(K g)(U), g = e^(-V/2) Omega (I1) ... Any comparison of the Dirichlet forms of P and K through the oscillation of g (Holley-Stroock), or of cross-ratios (Hopf, B2), has an extensive exponent: log g is a sum over the box. So it gives m_ev at least exp(-c |B|) and nothing at the seed size." This is point (b) above, in general form. Row 896 checked row 895.

So the row's question was answered on 2026-11-13, by rows 863 and 895: the Doob form is the exact vacuum subtraction, and every known comparison through it has an extensive exponent. Row 1207 neither cites nor improves on this. Final verdict for T2.1: HOLDS. Already on file (row 863 I1; also rows 1161 L17 and L248, 807, 738, 1205). Trivial. Its claim to remove the Lemma R4 penalty FAILS: the penalty sits inside the kernel (row 895 Stop 2; (P) above).

