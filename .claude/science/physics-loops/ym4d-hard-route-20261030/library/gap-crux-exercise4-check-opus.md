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
- Step 4 done 16:53Z: statement (ii), with the literature finding (two posted proofs of the 2D O(N >= 3) gap).
- Step 5 done 16:58Z: statement (iii).
- Step 6 done 17:02Z: statement (iv), hand check and independent control run (lock acquired and released).

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

### 2.1 Test first: does any theorem make T false for the 2D O(N) model, N >= 3, at some beta?

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
arXiv:2610.16824 (2026-10-12), anisotropic perturbations, BKT phase for lambda < 1. **And a second, independent proof:**
DHY Remark 1.3 (p. 2), Remark 1.5 (p. 3) and their Statement (p. 6): "On Oct 6, 2026, OpenAI released a proof of
(1.4)"; it "relies crucially on the non-commutativity of rotations on S^2 and on a ... constructed family of spin waves
on S^2"; "the two approaches are drastically different". DHY give no bibliographic entry for it; I did not locate or read
it. DHY Theorem 1.1 (p. 2, read): fix N >= 3; for every beta > 0 there is c_beta > 0 with <sigma_o> <= c_beta^(-1)
exp(-c_beta L) on B_L under constant boundary conditions, and, with free boundary conditions,
<sigma_u sigma_v>_(B_L, beta) <= c_beta^(-1) exp(-c_beta |u - v|) for u, v in B_(L/2), uniformly in L. Marks: the
preprints are read at abstract level (Pei, Garban-de Montgolfier) and at pages 1-6 (DHY); DHY is unrefereed and 12 days old; nobody in the lane has read it. Its statement is about
infinite-volume (or free-boundary, uniform in finite subgraphs) spin correlations, not about the lane's T (the seed
S(n; 2n) <= 1/20 on periodic tori, Corollary S2); a bridge from the one to the other is not written in the lane (row
1003 2.2 (e) already notes the same missing bridge for O(2)).

Consequence for row 1003 (to be finished in 2.2): the premise at L102-103, "How T(M') stands: it is OPEN, and believed
TRUE. A gap at fixed N >= 3 and every beta is unproved (row 998 I37, BELIEF about the state of the literature ...)", is
out of date at this pin's date (2026-11-15): a proof is claimed and posted. Row 1003 marked the premise as a BELIEF
about the literature, RECALLED; the belief is now false as a description of the literature. The verdict "not a test"
(2.2 (a)) only gets stronger (T(M') is not known false; it is claimed true). The "price" readings (b)-(d), which rest
on "T(M') is open", need correction.

Lane search for these sources (rule 0a; `grep -rl` over this folder for 2611.04908, 2611.01532, 2610.16824, "Ding,
Huang", "Polyakov's prediction/conjecture", "October 6"): no match outside this file. The nearest lane record is
Ursachi, Research Square rs-11440706/v1 (2026-10-21; a finite seed criterion for the 2D O(3) model on small tori with
"the one inequality that remains"; `prior/gap-crux-lit-2.md` L309, `prior/gap-seed-lit.md` L20): conditional, not a
proof. So the two proofs are new to the lane. **Pointer for the lead, not an attack (W1: no new attack):** the OpenAI
proof is described by DHY as resting on the non-commutativity of rotations on S^2; that is a gap mechanism "from the
group" in an asymptotically free model, which is the kind of input `parts/gap.md` L147 says RA would reopen on. Whether
any of it transfers to a gauge field or to four dimensions is unknown; nobody has read it.

### 2.2 Verdicts on Section 2.2 (a)-(d)

- **(a) L115-118, "not a test in the valid form". HOLDS** (a fortiori). Both parts of step 6c need T(M') false
  (SKILL.md L448-457); T(M') is not known false, and is now claimed true at every beta in two posted proofs. One loose
  clause, not a failing line for (a): L118 "The skill's two exclusion clauses quoted above both apply". "H(M') is not
  known" applies. "The proof also runs for M', and T(M') is true there" applies only as far as T(M') is true: at the
  pin date that rests on two unrefereed proofs of the infinite-volume form, and the lane's periodic form needs a bridge.
  (a)'s three-line argument does not use the clause.
- **(b) L120-139, "a price". HOLDS AFTER CORRECTION. First failing line: L125, "That is the open problem as stated"**
  (and its premise L102-103, "it is OPEN ... A gap at fixed N >= 3 and every beta is unproved"). At the pin date the gap
  of M' at every beta, in the infinite-volume form, has two posted proofs (OpenAI, 2026-10-06; Ding-Huang-Yang,
  arXiv:2611.04908, 2026-11-03), neither refereed, neither read by the lane. **One-line repair:** "That is Polyakov's
  conjecture: claimed proved for every N >= 3 in two posted, unrefereed proofs (OpenAI 2026-10-06; arXiv:2611.04908); in
  the lane's periodic form (the seed of Corollary S2) it needs a bridge that is not written." With the repair, (b)'s
  conclusion that the filter is a cost statement stands. The size of the cost changes a lot. It is no longer "at least
  as hard as an open problem" (L138-139). It is "a further proof, by the transfer-operator route, of a theorem claimed
  twice". The trajectory form (L127-136) is unchanged: the 2D ultraviolet account is still not in the literature cited
  (Kopper 1999 via `RTARGET.md`; not re-read here). The new proofs work directly at each beta and give no first-passage
  account.
- **(c) L141-146, what it binds. HOLDS as logic.** "Would bind as a constraint ... only if T(M') were false". This is
  right in the skill's terms: for a tool with a written proof, a false T(M') can only constrain. For a candidate with no
  written proof, H(M') true together with T(M') false would refute. The filter is stated for steps with proofs, so the
  parenthesis "(never as a refutation)" stands. Factual note: the scenario that would make it bind (Patrascioiu-Seiler,
  T(M') false at large beta) is now contradicted by two posted proofs. If they stand, the filter binds nothing, even
  conditionally. "Easier than the two-dimensional problem" (L145) should read "different from what the two-dimensional
  proofs use". The logic ("a choice of route, not a condition that a correct proof must meet") is unaffected.
- **(d) L148-151, "a price, not a refutation". HOLDS.** The skill lists "it also holds for model X" as a discard reason
  to audit (SKILL.md L353-354, Step 4, the assumptions table, item (d) "Discard tests"). Step 6c makes it valid only with T(M') false. "Test it first where the answer
  is known" now covers the 2D O(N) model at fixed N >= 3 itself, in the infinite-volume form, if the posted proofs stand.

**Also affected (outside (a)-(d); for the lead; not verdicts):** 2.1 table row L111 ("T_fix and T_W are open"); 2.3
L174 ("the step costs at least the open two-dimensional gap"); 7.7 L711 ("A lane on the two-dimensional O(N) model (it
is the open problem ...)"); 7.8 L722 (the mark rests on "the open status of the 2D gap (BELIEF)"); the RESULT line
("because the two-dimensional gap is open and believed true"). W2 (a), which would copy 2.3 into `parts/gap.md` L92,
should take the repaired wording. Row 998 I37 and row 1002 item 6 (the same belief) are out of date in the same way.
I did not check them line by line.

**Verdict on statement (ii): HOLDS AFTER CORRECTION.** The answer to W1's question stands: the 2D filter is not a test
in the form of step 6c. It is a cost statement and a routing rule. The correction is factual: the "open problem" is,
at the pin date, a theorem with two posted, unrefereed proofs. That lowers the cost the filter names, and it removes
the only scenario in which the filter could bind.

## 3. Statement (iii): the column "Q_8, 2T" of the table (Section 3), S2 of 3.1, and Fact T in Q_8

Read: row 1003 L195-262 in full; anchors `gap-crux-restate.md` L53 (Fact T), `gap-crux-exercise2-max.md` L190-194
(properties (a)-(e) of SU(2) and what Q_8, 2T share), `gap-next3-max.md` L39 and `gap-brainstorm2-max.md` L263 (row 8),
`gap-arealaw-opus.md` L186-212 (Lemma S of row 825, the slab law), `gap-crux-exercise-r858-max.md` L155 (row 19),
`gap-brainstorm-max.md` L336 (idea 48, row 5), `gap-crux-exercise2-check-astra.md` L227-240 (check 884: the lane's Q_8
and 2T carry the Wilson weight exp(beta Re Tr/2) of the SU(2) fundamental, so they are subgroups of SU(2) in its
defining representation).

### 3.1 Test first: Fact T in Q_8

**HOLDS (computed).** Q_8 = {+-1, +-i sigma_1, +-i sigma_2, +-i sigma_3} in SU(2); 2T contains Q_8. With A = i sigma_1,
B = i sigma_2: A B = -i sigma_3, A^(-1) B^(-1) = (-i sigma_1)(-i sigma_2) = -i sigma_3, so A B A^(-1) B^(-1) =
(-i sigma_3)^2 = -1. On the torus with the twist stack in the plane (mu, nu), put U = A on the mu-links of the last
mu-layer and U = B on the nu-links of the last nu-layer, all other links 1: every untwisted plaquette is 1 and the one
twisted plaquette per (mu, nu)-plane is A B A^(-1) B^(-1) = -1. So the twisted sector has a configuration of action
zero, inside Q_8 and inside 2T. This is the content of Fact T (`gap-crux-restate.md` L53), and the row's reason (L242)
is the right one.

### 3.2 The column, row by row

| # | Row 1003 cell | Check | Reason |
|---|---|---|---|
| 1 | yes | HOLDS | Z(Q_8) = Z(2T) = {+-1}: flux sectors, (TM-c), twists as for SU(2) |
| 2 | yes | HOLDS | 3.1 above |
| 3 | yes | HOLDS | 2^6 = 64 twists from the centre Z_2; the axis exchange does not see the group |
| 4 | yes; U(1) too | HOLDS | the Bianchi constraint on each 3-cube is group algebra; any compact group |
| **5** | **yes; U(1) too** | **FAILS for the clause "the Gibbs mean of the Hessian is diagonal"** (first failing cell) | Elitzur and "only closed flux": shared, yes. The Hessian clause needs a Lie group and an adjoint action with no fixed vector. Argument: a gauge rotation g at a vertex of link l and not of link l' acts on the block H_(l l') by Ad(g) on the l side only. Gauge invariance then forces <H_(l l')> to map into the Ad-fixed vectors of su(2), which are 0. For a finite group there is no Hessian. For U(1), Ad is trivial and the mean off-diagonal block is +- beta <cos theta_p>, which is not 0 for beta > 0. The 2D O(N) model has no local gauge invariance, and its mean block in the ambient frame is (1 - 2/N + <(s_x.s_y)^2>/N) I, not 0. One-line repair: "yes for Elitzur and closed flux; no for the mean-Hessian clause (no Hessian on a finite group; for U(1) Ad is trivial)". |
| 6 | yes | HOLDS | finite centre, no continuous global symmetry |
| 7 | no (they need integration by parts on the group) | FAILS for half the input | The Ward form of the loop equations needs the Lie algebra: Q_8, 2T lack it (yes). "SU(2) Mandelstam constraints" do not: Cayley-Hamilton gives B + B^(-1) = tr(B) I for det B = 1, so tr A tr B = tr AB + tr AB^(-1) for all A, B in SL(2, C). They hold on Q_8 and 2T in the defining representation. Correct cell: "no for the Ward form; yes for the Mandelstam constraints" |
| 8 | not checked here | **yes** (my check; ARGUED) | Lemma S of row 825 (L186-212), the lane's form of the Durhuus-Frohlich slab comparison. Its (i) and (iii) use only that the action is a sum over plaquettes and that each plaquette in a (rho, nu) plane holds two vertical edges of one slab. That holds for any compact group, Q_8 and 2T included (counting measure in place of Haar). Only (ii), the S^3 form of x_p, is SU(2)'s. The range beta_W < 2/3 is SU(2)'s (Dobrushin on the O(4)-type layer law). For Q_8 the range is that of a 3D Q_8 chiral model with background couplings, not computed here. Durhuus-Frohlich itself not read |
| 9 | yes (and at every time extent) | HOLDS (as RECALLED) | frozen finite groups order at every time extent; the lane's "no seed" for them is the flux/holonomy count (check 884) |
| 10-15 | no | HOLD | 10 discrete (no Ricci, no O'Neill); 11 the group is not S^3, no Bessel sequence c_j; 12 no running; 13 the account is for SU(2); 14-15 need a continuous group |
| 16 | no | FAILS at theorem grade | The theorem part, the beta-derivative identity (Theorem D (f); "the identity yes" in the Order-one column), is calculus on log Z and holds for every group: Q_8, 2T and U(1) included. Only the link to a scale derivative fails for Q_8, and that link is not a theorem at order one. Correct cell: "the identity yes; the scale reading no" |
| 17 | no | not decidable | the input is an OPEN question; S2 does not use it |
| 18 | not applicable | HOLDS | a statement about U(1) |
| 19 | Z_2 part only | HOLDS in one reading (author left it unchecked) | Read "Z_2 part" as the centre-flux part: the Hodge duality of the 64 centre twists, as in row 3. That is shared. Q_8 and 2T lack the Bogomolny bound (no continuous field). Their gauge theories are not self-dual: the Kramers-Wannier-Wegner duality maps a finite abelian group to its dual group, while a non-abelian finite group goes to a model on representations (RECALLED). The cell should say "centre-flux part only (= row 3)" |
| 20 | yes | HOLDS | area-law order parameter, Seiler and Simon-Yaffe bounds: any compact group; Tomboulis-Yaffe: a centre Z_2 and reflection positivity, both present (RECALLED) |

### 3.3 S2 (L237-253) against the corrected column

- **First bullet (gauge kinematics; Q_8 and 2T share every one; Fact T holds for Q_8): HOLDS, with additions.** Every
  listed input is shared, except the mean-Hessian clause of 5 (moved to the third bullet below). Inputs that also
  belong here: 8 (shared, by 3.2), the Mandelstam half of 7, and the identity part of 16. These additions are group-blind
  or inherited by subgroups, and the 2D O(N) model lacks 8.
- **Second bullet (continuous fibre: 10 fibre, 11, 7, 16; "Q_8, 2T and U(1) lack them"): FAILS as written** for two of
  the four. The Mandelstam half of 7 is shared by Q_8 and 2T. The identity part of 16 is shared by every group. Outside
  the Q_8 column: the Ward form of 7 is not lacked by U(1), because integration by parts on U(1) gives Schwinger-Dyson
  equations for U(1) Wilson loops (RECALLED). The bullet holds for 10 (the fibre) and 11, for the Ward form of 7 with
  respect to Q_8 and 2T, and for the scale reading of 16 (which is not a theorem).
- **Third bullet and the conclusion ("Both at once: one input only, the O'Neill term"; "no input on this list
  separates Wilson SU(2) from the frozen groups and from the two-dimensional O(N) model at once, except the O'Neill
  term"): FAILS at "one input only" (L245).** The mean-Hessian clause of input 5 also separates SU(2) from both. SU(2)
  has it at every beta (Elitzur plus an adjoint action with no fixed vector; argued in 3.2, row 5). Q_8 and 2T have no
  Hessian. The 2D O(N) model has no local gauge invariance and its mean block is not 0. U(1) lacks it too, because Ad is
  trivial. **One-line repair:** "Both at once: two clauses, both facts of a gauge quotient of a continuous non-abelian
  group: the O'Neill term of input 10 and the mean-Hessian clause of input 5." The sentence after it (L250-253) needs
  "its only known consumer" changed to "their known consumers". On file, the consumers are the Bakry-Emery route (stops
  near beta 1/8), the averaged-curvature route of row 968 (did not close; its Proposition AVG is the obstruction) and
  idea 48 (d) of row 859 (an idea, no theorem). So the repair adds no input with a consumer, and V1 in Section 4 is not
  touched by it. That is my reading; Section 4 is not re-derived here.

**Verdict on statement (iii): FAILS at L245 ("one input only") and at the row-5 cell "yes; U(1) too" (the mean-Hessian
clause); HOLDS AFTER the one-line repairs above.** Fact T in Q_8 HOLDS (computed). Rows 8 and 19, unchecked by the
author: 8 is "yes" (shared; ARGUED from Lemma S's proof); 19 holds as "the centre-flux part only". Rows 7 and 16: the
cells are wrong for half of each input, in the direction of "shared", and this weakens the second bullet of S2.
Consequence: S2's picture survives in amended form. The exact inputs split into those shared with Q_8 and 2T (now
also 8, Mandelstam, the beta-identity) and those shared with the 2D model (10 fibre, 11, the Ward form). Two clauses
of a gauge quotient of a continuous non-abelian group are lacked by both. No new consumer appears, so the row's
negative result (no input with a consumer) is not changed by this check.

## 4. Statement (iv): Section 5.2 Steps 1-3, the torus gap equation, (ENV), the bond energy

Read: row 1003 L440-575 in full. Everything below is re-derived by hand from the weight exp(N b sum s_x.s_y); the
N = infinity saddle itself stays RECALLED and formal, as row 1003 marks it.

- **The saddle and the gap equation. HOLDS.** sum over bonds of s_x.s_y = 2 sum_x s_x^2 - (1/2) sum over bonds of
  (s_x - s_y)^2 (2 L^2 bonds, each site in 4). With the multiplier lambda and mu := lambda/b - 4, the Gaussian integral
  gives N [(b/2) L^2 mu - (1/2) sum_p log(p^^2 + mu)] plus terms extensive in L^2. phi_L'' = (1/2) sum (p^^2 + mu)^(-2) > 0,
  phi_L -> +infinity at mu -> 0+ (the zero mode, -(1/2) log mu) and at mu -> infinity, so the minimiser is unique and
  solves (1/L^2) sum_p 1/(p^^2 + mu) = b. Matches L455-458.
- **Step 1, the form of delta_L. HOLDS.** delta_L = -(1/2)[sum_p log(p^^2 + mu) - L^2 int log(p^^2 + mu)]: the (b/2) L^2 mu
  terms cancel. Frullani's formula log A = -int (dt/t)(e^(-tA) - e^(-t)) (the e^(-t) terms cancel since sum_p 1 = L^2)
  and the discrete Poisson identity sum over p in (2 pi/L) Z_L^2 of e^(-t p^^2) = L^2 sum over n in Z^2 of K_t(nL)
  (the n = 0 term is the bulk) give delta_L(mu) = (L^2/2) sum over n != 0 of int (dt/t) e^(-t mu) K_t(nL). K_t(x) > 0
  for t > 0 (continuous-time walk), K_t(nL) vanishes faster than any power as t -> 0, so the integral converges and
  delta_L > 0 with delta_L' < 0. The variational form d(L) = min [L^2 psi + delta_L] differs from min phi_L - L^2
  phi_inf(mu_inf) by nothing (identical expressions), and mu_L > mu_inf follows from L^2 psi'(mu_L) = -delta_L'(mu_L) > 0.
- **Step 2 (ARGUED by row 1003; the parts W1 names re-derived). HOLDS as a scaling computation.** With
  int d^2p/(2 pi)^2 (p^^2 + mu)^(-1) = (1/4 pi) log(32/mu) + o(1): mu_inf = 32 e^(-4 pi b) and psi'(mu) = (1/8 pi) log(mu/mu_inf),
  psi as printed; L^2 psi = Psi(x, y). Continuum heat kernel (4 pi t)^(-1) e^(-r^2/4t) and
  int_0^inf t^(nu-1) e^(-a t - beta/t) dt = 2 (beta/a)^(nu/2) K_nu(2 (a beta)^(1/2)) at nu = -1 give
  int (dt/t) e^(-t mu) K_t(r) = (mu^(1/2)/(pi r)) K_1(r mu^(1/2)), hence delta_L = (1/2) sum_(n != 0) (x/(pi |n|)) K_1(x |n|) = c(x).
- **The torus gap equation (L483). HOLDS.** dPsi/dx = (x/2 pi) log(x/y); with d/dz [z K_1(z)] = -z K_0(z),
  c'(x) = -(x/2 pi) sum_(n != 0) K_0(x |n|). Stationarity: log(x/y) = sum_(n != 0) K_0(x |n|). Cross-check by another path:
  the lattice gap equation with Poisson summation, b = G_mu(0) + sum_(n != 0) G_mu(nL), G_mu(0) = (1/4 pi) log(32/mu),
  G_mu(r) = (1/2 pi) K_0(r mu^(1/2)), gives the same equation.
- **(ENV) (L487). HOLDS.** dPsi/dy = (y^2 - x^2)/(4 pi y); the minimiser is unique (strict convexity in mu), so the
  envelope theorem gives y d'(y) = -(x^2 - y^2)/(4 pi) = -(L^2/4 pi)(mu_L - mu_inf) < 0. Cross-check by another path
  (exact on the lattice at N = infinity, no scaling limit): the envelope theorem in b gives
  dd/db = (L^2/2)(mu_L - mu_inf), and in the scaling limit dy/db = -2 pi y, so y d'(y) = -(1/2 pi) dd/db: the same
  identity.
- **The bond energy E_L = 1 - 1/(4b) + mu_L/4 (L564). HOLDS**, with "bond energy" = <s_x . s_(x+e)>. At the saddle
  <s^a_x s^c_y> = delta^(ac) G_L(x - y)/(N b), G_L = (-Delta + mu_L)^(-1), so <s_x . s_y> = G_L(x - y)/b. The equation
  (-Delta + mu) G = delta at 0 gives 4 G(e) = (4 + mu) G(0) - 1, and G(0) = b (the gap equation), so
  <s_x . s_(x+e)> = 1 + mu_L/4 - 1/(4b). Then 2 L^2 (E_L - E_inf) = (L^2/2)(mu_L - mu_inf) = dd/db: the "first half" of
  point 3 (L562-566) is consistent, and its SU(2) counterpart dD/dbeta = 6 n^4 (abar_inf - abar_n) is Theorem D (f) with
  the sign convention of the action sum (1 - s_p).

**Verdict on statement (iv): HOLDS** (by hand; formal at N = infinity as marked; Step 2's lattice corrections dropped,
as marked). No failing line in Steps 1-3, the gap equation, (ENV) or E_L.

### 4.1 Independent control run (GUIDE; W1 allows it). Pre-registered before the run (written 17:01Z by `date -u`)

Implementation, different from row 1003's: no 2D sums. One momentum is summed exactly by the product formula
prod_k (a - 2 cos(2 pi k/L)) = 2 cosh(L theta) - 2, with a = mu + 4 - 2 cos p_1 = 2 cosh theta, so
sum over p_2 of log(p^^2 + mu) = 2 log(2 sinh(L theta/2)) and sum over p_2 of 1/(p^^2 + mu) = L coth(L theta/2)/(2 sinh theta).
The bulk uses the exact inner integral (1/2 pi) int log(a - 2 cos p) dp = theta, and the outer one is a trapezoid sum on
2^15 points (error about exp(-2^15 mu^(1/2)), negligible). Script: `/tmp/row1006-check/scripts/ninf_check.py`.
Tests and criteria:

- T1 (bulk): mu_inf and mu_inf/(32 e^(-4 pi b)) at b = 0.6, 0.7, 0.8 against row 1003's table (1.6776e-2, 4.8179e-3,
  1.3755e-3; 0.9864, 0.9953, 0.9984). PASS if they agree to the printed digits.
- T2 (the lattice form of (ENV), exact at N = infinity, not in row 1003's run): dd/db by central differences with steps
  h = 1e-4 and h/2, against (L^2/2)(mu_L - mu_inf), at b = 0.7, L = 8, 16, 32, 64. Report the relative deviation at both
  steps; PASS if it is below 1e-5 and falls by about 4 when h halves (or is at rounding level).
- T3 (the bond energy, direct): <s_x . s_(x+e)> = (1/(b L^2)) sum_p cos p_1/(p^^2 + mu_L) against 1 - 1/(4b) + mu_L/4, same
  points. PASS at relative deviation below 1e-10.
- T4 (the R3 table): d(L), x = L mu_L^(1/2), d(2L)/d(L) at b = 0.8, L = 4 ... 128, against row 1003's printed values.
  PASS if equal to the printed digits.
- T5 (R1, R2 repeated): largest d(L+1) - d(L) over L = 4 ... 256 at b = 0.6, 0.7 and 4 ... 320 at b = 0.8, and the R2
  ratio, against row 1003 (+7.3e-12, -4.6e-9, -7.3e-7; 1.0174, 1.0084, 1.0047). PASS if the ratios agree to 3 decimals
  and the largest steps agree in sign and order of magnitude (at rounding level for b = 0.6).

**Result (GUIDE; run 2026-11-15 17:01:38Z to 17:01:40Z by `date -u`; numeric lock held by `row1006-check-opus`,
acquired 17:01:33Z and released after the run; memory 69 percent free before the run; exit 0; output
`/tmp/row1006-check/ninf_check.out`, outside git). The criteria above were not changed.**

- T1 PASS: mu_inf = 1.677617e-2, 4.817894e-3, 1.375529e-3; ratios 0.986384, 0.995316, 0.998445 (row 1003: 1.6776e-2,
  4.8179e-3, 1.3755e-3; 0.9864, 0.9953, 0.9984).
- T2 PASS: relative deviation of the central difference from (L^2/2)(mu_L - mu_inf) at b = 0.7, h = 1e-4 / 5e-5:
  L = 8: +1.4e-10 / +3.5e-11; L = 16: -2.7e-8 / -6.8e-9; L = 32: -9.6e-8 / -2.3e-8 (falls by 4.0, 4.0, 4.1 when h
  halves); L = 64: +1.7e-7 / +6.8e-8 (falls by 2.5; rounding of d = phi_L - L^2 phi_inf at L^2 = 4096 is about 1e-8
  relative here). So the lattice form of (ENV), dd/db = (L^2/2)(mu_L - mu_inf), holds to the accuracy of the run. That
  is a data path that row 1003's run did not use.
- T3 PASS: direct <s_x . s_(x+e)> against 1 - 1/(4b) + mu_L/4: relative deviations -1.3e-14, -2.0e-14, -3.0e-14, +4.8e-15.
- T4 PASS: every printed entry of the R3 table is reproduced to its digits (for example b = 0.8, L = 4: y 0.148,
  x 1.358, d 0.73786, ratio 0.8243, last column 0.1966; L = 128: 4.747, 4.842, 0.016825, 0.01155, 4.284; b = 0.6,
  L = 64: d 6.171e-4, ratio 3.44e-4, 7.771).
- T5 PASS: largest steps +1.5e-11 (rounding), -4.63e-9, -7.25e-7, no violation above 1e-9; R2: 0.158161 / 0.155450 =
  1.0174, 0.317669 / 0.315009 = 1.0084, 0.466551 / 0.464390 = 1.0047, equal to row 1003's to the printed digits.

What the run establishes: row 1003's control numbers are reproduced by an independent implementation, and the exact
N = infinity identities (the lattice form of (ENV), the bond energy) hold numerically. What it does not establish:
anything about SU(2), and nothing beyond GUIDE about the scaling form of Steps 2 and 4. The 0.5-1.7 percent R2
mismatch therefore sits in the scaling conversion dy/db = -2 pi y (lattice corrections of relative order mu), not in
(ENV) itself. That agrees with row 1003's reading at L531-532.
