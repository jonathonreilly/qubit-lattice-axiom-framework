lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T04:42Z

# Check of row 1003 (`gap-crux-exercise4-max.md`), work item W1 — row 1006

Row: 1006 `gap-crux-exercise4-check-opus`, queued 2026-11-15 16:42Z, Mac mini worker 1.
Checker: Claude Opus 5.5 (max), Anthropic. Checked file: `library/gap-crux-exercise4-max.md` (row 1003), written by
Claude Fable 5.2 (Anthropic). **Same provider: this is not a cross-provider check** (FINISH row 1006 says so).
Pinned commit: e299f9765 on `claude/ym4d-hard-route`. Started 2026-11-15 16:42:51Z (`date -u`).

## 0. Plan (at most eight steps; one step per response; result appended before the next)

Fixed from W1 (`gap-crux-exercise4-max.md` 7.7, L683-704). Verdict scale of W1: HOLDS, HOLDS AFTER CORRECTION,
FAILS (at the first failing line), OPEN. Stop rule: the first failing line of each statement; no repair beyond one
line. No new attack. (FINISH L344 asks check reports for ADVANCE / CORRECT-NO-ADVANCE / WRONG; the row names W1's
scale, so W1's scale is used, and the FINISH reading is given once in the verdict table.)

1. (done) Read W1, fix the plan.
2. Statement (i), tests first: (a) arithmetic 0.176 x 32/192 < 0.03 and 12800^2 x 4 = 655,360,000; (b) Theorem 1 (iii)
   of `gap-seed-sc.md` for real beta in [0, 1/12800] with exponent 4n, n >= 4, and A_n > 0 in Theorem 2 for n >= 5;
   (c) Lemma PT (a), (c), (d) of `gap-crux-exercise3-max.md` L690-713 with one factor the Ising model on sites;
   (d) the choice of K and the line that gives (b); (e) Section 6.1's bound D >= (1/16) log(1 + S).
3. Statement (i), the line-by-line read of Lemma NP0, Proposition NP, Corollary NP1, Section 6.1 against
   `gap-seed-sc.md` L30-47, `gap-mid-max.md` L63 and L230, `gap-seed-shape.md` L207-221, `gap-phys-seed.md` L283-294;
   verdict.
4. Statement (ii): fetch the exercise skill (main 8b11ae2bb9, L437-490) into /tmp scratch; test first whether any
   theorem makes T false for O(N), N >= 3, at some beta; then Section 2.2 (a)-(d); verdict.
5. Statement (iii): Section 3.1 S2, the column "Q_8, 2T", row by row (rows 8, 19 unchecked), and "Fact T holds in
   Q_8"; verdict.
6. Statement (iv): Section 5.2 Steps 1-3: delta_L, the torus gap equation, (ENV), E_L = 1 - 1/(4b) + mu_L/4; control
   run only if memory and the numeric lock allow; verdict.
7. Statement (v): ten anchors of Sections 3 and 4, chosen by me, each printed and compared.
8. Verdict table, defects (at most ten, ranked), RESULT line.

## Status log

- 2026-11-15 16:42:51Z: file created (step 0).

## 1. Statement (i): Lemma NP0, Proposition NP, Corollary NP1, Section 6.1 (row 1003 L342-438, L579-594)

Read in full: row 1003 L55-80, L330-438, L577-610; `gap-seed-sc.md` L1-60 (Theorems 1-4); `gap-crux-exercise3-max.md`
L680-720 (Lemma PT, Corollary PT1); `gap-mid-max.md` L36-46, L60-67, L224-232; `gap-seed-shape.md` L200-222;
`gap-phys-seed.md` L280-305 (Lemma Z3, Theorem ZD); `gap-crux-restate.md` L37, L95-102, L192-219 (Lemma A, Theorem D
(b), Theorem S, Corollary S3').

### 1.1 Tests first (W1 (i) (a)-(e))

- **(a) Arithmetic. PASS.** 0.176 x 32/192 = 0.176/6 = 0.02933 < 0.03. 12800^2 = 163,840,000; x 4 = 655,360,000 =
  6.5536 x 10^8. The quotient itself, recomputed: with A_n/32 = 6 n^3 4^(-4n),
  0.176 n^4 (12800 beta)^(8n) / (6 n^3 4^(-4n) beta^(4n)) = (0.176/6) n (12800^2 x 4 x beta)^(4n). Equal to L380.
  The geometric step: 0.16/16 = 0.01 per term (16^(-(i+1)) x 16^i = 1/16); sum over i of t^(4m 2^i) <= sum over
  k >= 1 of t^(4mk) = t^(4m)/(1 - t^(4m)); with t <= 1/2, m >= 4: t^(4m) <= 2^(-16), factor 1.0000153 < 1.1.
  At m = 2n: 0.011 x 16 = 0.176. Section 6.1: log(1 + 1/5041) = 1.98354 x 10^(-4); /16 = 1.2397 x 10^(-5) > 1.2 x 10^(-5).
- **(b) Theorems 1, 2 of `gap-seed-sc.md`. PASS.** L33-34: e(n) = 4n for n >= 4; Theorem 1 (iii) (L39) states
  |Phi(n; beta)| <= 0.16 n^4 (12800 |beta|)^e(n) "for |beta| < R, and for real beta in [0, R]", R = 1/12800; (i) gives
  Phi real and >= 0 on [0, R]. Theorem 2 (L44-46): Phi = A_n beta^e(n) + O(beta^(e(n)+1)), A_n = 192 n^3 4^(-4n) > 0 for
  n >= 5. Row 1003's (i4) quotes both exactly. Lemma NP0 uses Theorem 1 (iii) only at sizes 2^i m with m >= 4 (upper
  bound, m = n and m = 2n with n >= 5) and Theorem 2 only at n >= 5 (lower bound): inside the ranges. Theorem 1 is
  for the action sum of (1 - s_p); D does not change under an additive constant in the action (it shifts F(n^4) and
  f n^4 by the same amount), so no normalisation issue.
- **(c) Lemma PT (a), (c), (d) with the Ising model on sites as one factor. PASS (the proof runs; the statement of
  Lemma PT is written for two gauge factors, so this is an extension by its own proof, as row 1003 (i1) says).**
  (a) the two systems are independent on the same torus, so Z = Z_g Z_I and Z is symmetric because both are. f = f_g
  + f_I needs I3 for the Ising factor: F(n)/abs(n) non-increasing in each side. It holds: the Ising T of each
  direction is positive definite (`gap-seed-shape.md` 4.1, L212), so by Lemma A (a) of `gap-crux-restate.md` (L37),
  (Tr T^k)^(1/k) does not increase in k, and by the symmetry of Z any side can be the time. (c) T_B = T_g (x) T_I on
  L^2(gauge-invariant) (x) C^(2^V); Tr T_B^k = Tr T_g^k Tr T_I^k; top eigenvalue lambda_0 mu_0, simple; so
  1 + S = (1 + S_g)(1 + S_I) and S >= S_g, S >= S_I. (d) follows from S >= S_i. The class conditions of the product
  (symmetric Z, positive trace-class T, simple top eigenvalue, ell finite, `gap-seed-shape.md` L207) hold factor by
  factor. Induction to K + 1 factors: same lines.
- **(d) The choice of K and the line giving (b). PASS.** K >= (32/theta) v(n_j)/u(n_j) is a finite condition
  (u(n_j) > 0 by Lemma NP0, finitely many j). It gives 16 v(n_j) <= (theta/2) K u(n_j). With u(n_(j+1)) <= (theta/2)
  u(n_j) (Lemma NP0 and the choice of beta_s) and v(n_(j+1)) <= 16 v(n_j) ((i2): D(2n) = 16 D(n) - Phi(n), Phi >= 0,
  recomputed from the definitions), D_M(n_(j+1)) <= theta K u(n_j) <= theta (K u(n_j) + v(n_j)) = theta D_M(n_j);
  the last step uses v >= 0 (D >= 0 since f is the infimum). Correct as printed (L402-403).
- **(e) Section 6.1, D >= (1/16) log(1 + S(n; (2n)^3)). PASS.** Cited as Theorem D (row 998 I5 = Theorem D (b) of
  `gap-crux-restate.md` L95, proof L102 by Lemma A (b)). I re-derived it by another path: Phi(n) = 8 d_1 + 4 d_2 +
  2 d_3 + d_4 (the four thermal terms of Lemma Z3, `gap-phys-seed.md` L286-288), each d_i = 2 g(n; B_i) - g(2n; B_i)
  >= 0 because (sum_i rho_i^n)^2 >= sum_i rho_i^(2n), and d_4 >= g(n; (2n)^3) because g(2n; B) <= g(n; B) (rho_i <= 1).
  So Phi(n) >= log(1 + S(n; (2n)^3)); with D(n) >= Phi(n)/16 ((i3), all terms >= 0) the bound follows, in every model
  of the class. The use in 6.1: S_M >= S_I (Lemma PT (c)); S_I(n; (2n)^3) >= 1/5041 for all n >= 3, else Corollary
  S3' (`gap-crux-restate.md` L217) gives m(L^3) >= log(1/q)/N > 0 on all L >= 2N, against inf_L m(L^3) = 0 (Peierls,
  RECALLED in `gap-seed-shape.md` L218). Correct.

