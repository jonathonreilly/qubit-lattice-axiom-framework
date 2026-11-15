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
- Steps 1-3 done (plan fixed; statement (i) tests and verdict written).

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

### 1.2 Line-by-line read and verdicts

- **(i2) L354-355.** D(2n) = F((2n)^4) - 16 f n^4 = 16 F(n^4) - Phi(n) - 16 f n^4 = 16 D(n) - Phi(n). Correct.
- **(i3) L356-357.** From (i2): D(n) = sum_(i<k) 16^(-(i+1)) Phi(2^i n) + 16^(-k) D(2^k n), and 16^(-k) D(2^k n) =
  n^4 (F((2^k n)^4)/(2^k n)^4 - f) -> 0 because F(N^4)/N^4 decreases to f (I3). Correct; Proposition R as cited.
- **(i5), (i6) L362-366. Citation note (not a failing line).** (i6) is written for a model "with no seed" and cited to
  `gap-mid-max.md` L63, whose text states it for a model "with no uniform gap". The two premises are not known to be
  the same: whether a uniform gap forces a seed is left open (`gap-phys-seed.md` L309; row 727's check L106 points to
  (NS-gap) of row 700). The "no seed" form is Theorem ZD, (B) gives (A) (`gap-phys-seed.md` L296-303: D(a) <= 6.1 x
  10^(-4) gives S(a; (4a)^3) < 1/25, then Theorem SH (i) at r = 4 and S(2k; B) <= S(k; B)^2 give S(N; (2N)^3) < 1/5041;
  Theorem ZD HOLDS in check row 727, `gap-phys-seed-check.md` L62; the same citation correction was made there for
  Proposition NM, L96). I re-checked the three lines: exp(64 x 6.1 x 10^(-4)) - 1 = 0.0398 < 1/25, and
  S(2k) = sum rho_i^(2k) <= (sum rho_i^k)^2. For M both premises hold anyway: no seed by Lemma PT (d) and (i5); no
  uniform gap by Lemma PT (c) (m = min(m_g, m_I)) and (i5). So Proposition NP (a) stands under either citation.
- **Lemma NP0 L368-381. HOLDS.** Tests (a), (b) above. The lower bound needs only the existence of beta(n) from the
  O(beta^(4n+1)) remainder of Theorem 2, which is how it is used. All sizes used are >= 4 (upper) and >= 5 (lower).
- **Proposition NP L383-406. HOLDS** (with the citation note on (i6)). Tests (c), (d) above. The choice of beta_s is a
  finite set of conditions, each true for small beta_s (0.03 n_j (6.5536 x 10^8 beta)^(4 n_j) -> 0). (c): if (b) held for
  all j >= 0, D_M(n_j) <= theta^j D_M(n_0) -> 0, against (a). Correct.
- **Corollary NP1 L408-412. HOLDS AFTER CORRECTION. First failing line: L411-412, "Take theta_0 = min(theta, theta')
  in Proposition NP: (b) gives the hypothesis, and (c) with (a) contradicts the conclusion."** Proposition NP (c) run
  at theta_0 gives one j >= J with D_M(n_(j+1)) > theta_0 D_M(n_j). When theta' > theta (so theta_0 = theta < theta'),
  this does not contradict the conclusion "D(n_(j+1)) <= theta' D(n_j) for every j >= J". Counter-reading: theta = 0.1,
  theta' = 0.9, a j with D(n_(j+1)) = 0.5 D(n_j) satisfies (c) at theta_0 = 0.1 and the conclusion at 0.9. **One-line
  repair:** "(b) at theta gives the hypothesis; if the conclusion held, D_M(n_j) <= theta'^(j-J) D_M(n_J) would tend to
  0, against (a)" (the argument of (c), not its statement, at theta'; equivalently, (c) holds for every theta'' in
  (0, 1) with the same proof). The corollary's statement is true; its last sentence ("no class-wide induction step for
  (CAS) reads only the history of D on finitely many scales") is a reading of the statement and is fair as such.
- **Remarks 1-6 L414-435.** Checked the two that assert something: Remark 2, J < k(D_M(n_0), theta): from (b) and (a),
  theta^J D_M(n_0) >= D_M(n_J) > 6.1 x 10^(-4); correct. Remark 4, concavity of j -> log D_M(n_j) is false in M: the
  increments delta_j = log D_M(n_(j+1)) - log D_M(n_j) satisfy delta_0 <= log theta and, by the argument of (c) at
  theta, delta_j > log theta for some j >= J, so they are not non-increasing; correct. Remark 5: 1 + S_M =
  (1 + S_g)^K (1 + S_I) by Lemma PT (c) and induction; correct.
- **Section 6.1 L579-594. HOLDS.** Test (e). Its heading says "(a) and (c) without Theorem SH": the first half of (a)
  ("no seed") never used Theorem SH; the second half becomes D_M > 1.2 x 10^(-5) by Theorem D (b), (i3), Lemma PT (c),
  Corollary S3' and the Peierls fact. The list of inputs at L592-594 is complete for (b), (c). Corollary NP1 with the
  threshold 1.2 x 10^(-5) needs the same one-line repair as above.
- **Mark at L383 and L728** ("the only input that is not rebuilt in the lane is the Peierls bound"): accurate. What
  that input must give is "no uniform gap on the periodic cubes" (inf_L m(L^3) = 0 at J >= J_P), i.e. Peierls plus the
  tunnelling step from long-range order to lambda_1/lambda_0 -> 1; `gap-seed-shape.md` L218 records both as RECALLED.

**Verdict on statement (i): HOLDS AFTER CORRECTION.** Lemma NP0 HOLDS; Proposition NP HOLDS (citation of (i6) should
add Theorem ZD (B) => (A), checked row 727); Corollary NP1 HOLDS AFTER CORRECTION (one line, L411-412); Section 6.1
HOLDS. No number, threshold or conclusion changes. The Peierls input stays RECALLED (not rebuilt here; W1 does not ask).
Independence: same provider as the author (Anthropic); tests (a), (e) were re-derived by a different path (direct
arithmetic; the four-thermal-term decomposition instead of Lemma A (b)).

## 2. Statement (ii): Section 2.2 (a)-(d), the 2D O(N) filter against the skill's step 6c

Read: row 1003 L82-194 in full; the exercise skill at main 8b11ae2bb9 (`docs/ai_methodology/skills/exercise/SKILL.md`,
703 lines, fetched by raw URL into `/tmp/row1006-check/SKILL.md`), L437-490 (step 6c) and L354 (the discard reason
"it also holds for model X"); `gap-crux-restate.md` L205 (Corollary S2).

### 2.1 Test first: does any theorem make T false for the 2D O(N) model, N >= 3, at some beta? (in progress)

Method: the lane's notes (`gap-crux-lit-cross.md` L79 points to the Patrascioiu-Seiler dissent; nothing proved), then
three arXiv API queries (`export.arxiv.org/api/query`, results in `/tmp/row1006-check/arx1.xml` ... `arx5.xml`).

**Result. No theorem makes T false. The opposite is now claimed in a preprint.** J. Ding, F. Huang, P. Yang,
"Exponential decay for the two-dimensional Heisenberg model", arXiv:2611.04908 (posted 2026-11-03, v1, math.PR):
abstract, quoted: "we prove exponential decay for the spin correlation of the spin O(N) model for N >= 3 at every
inverse temperature beta > 0. In particular, our work confirms Polyakov's prediction in 1975 on the Heisenberg model".
Method (abstract): a loop soup on the metric graph with intensity N/2 conditioned on the local times, Lupu's
isomorphism, random signs on clusters; "exponential decay for every real-valued N > 2"; the mechanism "does not
necessarily rely on the rotation symmetry". Two companion preprints confirm that the claim is current: Y. R. Pei,
arXiv:2611.01532 (v2, 2026-11) "Polyakov predicted ... and proofs of this have recently been posted" (it uses "the
annulus crossing bound of Ding, Huang and Yang"; it mentions "another isotropic proof"); C. Garban, N. de Montgolfier,
arXiv:2610.16824 (2026-10-12), anisotropic perturbations, BKT phase for lambda < 1. Marks: the three are read at
abstract level only; DHY is unrefereed and 12 days old; nobody in the lane has read it. Its statement is about
infinite-volume (or free-boundary, uniform in finite subgraphs) spin correlations, not about the lane's T (the seed
S(n; 2n) <= 1/20 on periodic tori, Corollary S2); a bridge from the one to the other is not written in the lane (row
1003 2.2 (e) already notes the same missing bridge for O(2)).

Consequence for row 1003 (to be finished in 2.2): the premise at L102-103, "How T(M') stands: it is OPEN, and believed
TRUE. A gap at fixed N >= 3 and every beta is unproved (row 998 I37, BELIEF about the state of the literature ...)", is
out of date at this pin's date (2026-11-15): a proof is claimed and posted. Row 1003 marked the premise as a BELIEF
about the literature, RECALLED; the belief is now false as a description of the literature. The verdict "not a test"
(2.2 (a)) only gets stronger (T(M') is not known false; it is claimed true). The "price" readings (b)-(d), which rest
on "T(M') is open", need correction.
