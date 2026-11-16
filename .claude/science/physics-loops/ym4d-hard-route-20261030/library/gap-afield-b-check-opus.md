lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T01:26Z

# Check of row 1032 Section 7 (`library/gap-afield-b-max.md`), FINISH row 1049 `gap-afield-b-check-opus`

Written by Claude Opus 5.5 at max effort on Mac mini worker 3, started 2026-11-16 13:26Z,
from commit eb05ae6aa of branch `claude/ym4d-hard-route`. Same provider as the author of
row 1032 (Claude Fable 5.2 max), so this is not an independent check in the sense of the
working rules; row 1050 is the cross-provider check. A research check, not an audit; no
mass gap is claimed. No new attack (row 1049: "No new attack").

Status: in progress. Sections are appended step by step; text below the plan is the only
record that survives an error.

## Plan (at most eight steps)

1. Read Section 7 of `library/gap-afield-b-max.md` in full, and the cited on-file
   statements it uses: Theorem ZD-c, Theorems CE and CR (row 1017), the even seed (ES),
   the definitions of D, D^+, Gamma_1, (W), (BDD-Delta), (LIOU) in `parts/gap.md` and
   `library/gap-dichotomy.md`. Record exact locations and wording.
2. Hand tests first: (a) the constant 15 in D(2a) <= D(a) + 15 Gamma_1(a) against
   Theorem ZD-c as written; (b) one value of eps_*(D^+) at D^+ = log(3/2); (c) the
   sharpness of log 2 on one limit object.
3. Line-by-line check of Lemma RISE, Lemma AMP, Theorem GS-dir and Corollary GS-eq
   (most care): constants, direction of each implication, quantifiers over sizes,
   cited theorems; the even-seed variant in five lines.
4. Line-by-line check of Lemma BAR, Lemma CHAIN-4 and Corollary NUC.
5. Line-by-line check of Proposition CAS-0 and Corollary GS (given CE, CR of row 1017).
6. Line-by-line check of Lemma NOCS and Lemma FP-U1.
7. Line-by-line check of Lemma TRI, Proposition SPH and Corollary SPH-LC.
8. Meaning of GS-eq (does it move (W) or restate it at one size; is either side closer to
   a proof than (W)), verdict table, RESULT line.

## Step log

(appended below as each step completes)

### Step 1 (done 2026-11-16 ~13:45Z): sources read, and what each says on file

Read in full: Section 7 of `library/gap-afield-b-max.md` (L263-437), and the idea statements B5, B8, B10, B12, B15
(L141-218) that Section 7 names. Read for the cited statements:

| Cited in Section 7 | Where on file | Says what is used? |
|---|---|---|
| Datum (E1)-(E3) | `gap-dichotomy.md` L84-87; `gap-compact-rigidity-max.md` (CRm) L133-140 | yes |
| Lemma A (a) | `gap-crux-restate.md` L37 | yes: k -> (Tr S^k)^(1/k) non-increasing, limit lambda_0 |
| Theorem D (a) | `gap-crux-restate.md` L101 (proof line) | yes: Z((2n)^4) <= Z(n^4)^16, from Lemma A (a) only |
| (TM-int), S(k+k') <= S(k) S(k') | `gap-crux-restate.md` L129 | yes |
| Lemma K | `gap-crux-restate.md` L174-180 | says it for kappa = e - ell b (deficit against the infimum with two sides fixed), **not** for c(B); see defect m1 |
| Theorem ZD-c, (PHYS-SEED-Delta) | `gap-phys-seed.md` L311-320; `gap-dichotomy.md` L144-147 | yes: "there is l' in P with D^+(l') < 6.1 x 10^(-4)" is equivalent to (PHYS-SEED); proof "(B) gives (A)" with uniform constants |
| (I) iff (W) | `gap-dichotomy.md` L160, L245-247 (fact (F3) of check 1019) | yes, without (BDD-Delta) |
| Lemma Z3 | `gap-phys-seed.md` L283-294; `gap-dichotomy.md` L200 | yes: D_j <= 1024 q'^(2^k)/5041 from the size 2^k l on, all large j, uniform in the size |
| Theorem CE (ii), spectral form, e_0 <= 0, integer multiplicities | CRm L170-178 (statement), L180-196 (proof) | yes; level convergence is in the statement of (ii) and Step 2, not Step 4 (defect m3) |
| Proposition OM (d), uniform recurrence | CRm L230, proof L236 | yes; the proof gives return times syndetic in Z (both directions) |
| Theorem CR | CRm L241-243; `gap-dichotomy.md` L180-184 | yes: (1) (W) iff (4) no uniformly recurrent element, given (BDD-Delta) with D_0 a bound |
| Proposition CONST | `gap-uv-rigidity-max.md` L725-738 | yes: the constant c is critical with bound D_0 iff c = log m, m >= 2, log m <= D_0 |
| even seed (ES) | `gap-means-max.md` L29 | yes: even thermal sum and additivity defect of the vacuum energy (cubes a, 2a) both below 10^(-7) |
| Theorem LB | `gap-es1-opus.md` L27, L88-117 | yes (long-box form; cited only as standing) |
| Q4, pressure pi(a) = a^4 p(1/a) | `gap-phys-seed.md` L195 | yes; equals G_3(a) of Lemma CHAIN-4 |
| 2D Ising ordered phase (GUIDE) | `gap-phys-seed.md` L369 | yes: D rises above log 2 and falls to log 2 (run, GUIDE) |
| Lemma PT (K1) | `gap-afield-b-max.md` L79 (from `gap-invent-selective-max.md` L50-65) | D adds over products: yes |

Not re-derived here: the inner proofs of Theorem ZD-c (Theorems S, SH, Lemma E', Corollary S3', Proposition Delta),
of Theorem CE and of Proposition OM. They are taken as on file with their checks (727 and 1019, both same-provider).

### Step 2 (done): the three hand tests asked first

**(a) The constant 15 in D(2a) <= D(a) + 15 Gamma_1(a).** It is not in Theorem ZD-c as written: ZD-c holds no such
inequality. It is Lemma RISE of row 1032 itself, which reads only (E1), (M1) and (M2). The queue row's phrase "given
Theorem ZD-c: D(2a) at most D(a) + 15 Gamma_1(a)" joins two inputs. GS-dir reads ZD-c only for
(PHYS-SEED-Delta) => (PHYS-SEED). Lemma RISE does not read ZD-c.

Rederivation (independent of the text's order). Double the sides of a^4 one at a time. B_1 = (a,a,a),
B_2 = (2a,a,a), B_3 = (2a,2a,a), B_4 = (2a,2a,2a). Each step has time a and box B_i. By (E1),
D(2a) - D(a) = sum over i of [Delta(2a, B_i) - Delta(a, B_i)]. By (M2) each bracket is
g(2a; B_i) - g(a; B_i) + a c(B_i) <= a c(B_i), because S(k; B) does not increase in k. By (M1),
c(B)/abs(B) = inf over T of M(T, B) does not increase in any side of B. So c(B_i) <= (abs(B_i)/a^3) c(a^3) =
2^(i-1) c(a^3). The sum is at most a c(a^3)(1 + 2 + 4 + 8) = 15 Gamma_1(a). **15 is right.** It is also the sum of
the weights 8 + 4 + 2 + 1 of Lemma Z3 Step 1 (`gap-phys-seed.md` L289), which uses the same four boxes. Consistency
check: RISE is equivalent to Phi(a) = 16 D(a) - D(2a) >= 15 (D(a) - Gamma_1(a)) = 15 G_0(a), and Phi >= 0 is on file.
Gamma_1 <= D holds because c(a^3) = inf over T of Delta(T, a^3)/T <= D(a)/a. So RISE refines D(2a) <= 16 D(a).

**(b) One value: eps_*(log(3/2)).** Here x := exp(d) - 1 = 1/2, so x^(2^s) = 2^(-2^s). The s-th term of the
supremum is t_s := 2^(-s) [6.1 x 10^(-4) 8^(-s) - log(1 + 2^(-2^s))].
- s = 0..4: t_s < 0. Use log(1 + y) >= y - y^2/2. For s = 4: log(1 + 2^(-16)) > 1.525 x 10^(-5) > 6.1 x 10^(-4)/4096
  = 1.490 x 10^(-7). For s = 3: 3.89 x 10^(-3) > 1.19 x 10^(-6). For s <= 2 the log is above 0.06 and the first
  term is below 6.1 x 10^(-4).
- s = 5: t_5 = 6.1 x 10^(-4)/2^20 - log(1 + 2^(-32))/32. The first part is 5.8174 x 10^(-10). The second lies in
  (2^(-32) - 2^(-65), 2^(-32))/32, that is 7.276 x 10^(-12) to 4 digits. So t_5 = 5.7446 x 10^(-10).
- s >= 6: t_s <= 6.1 x 10^(-4) 16^(-s) <= 6.1 x 10^(-4)/16^6 = 3.64 x 10^(-11) < t_5.

So **eps_*(log(3/2)) = t_5 = 5.7446 x 10^(-10)**, attained at s = 5. The row's sufficient value
Gamma_1^+(L) <= 5.7 x 10^(-10) is below it, so the strict inequality of GS-eq holds. Its worked instance checks too:
2^(-17) + 2^20 x 5.7 x 10^(-10) = 7.629 x 10^(-6) + 5.9769 x 10^(-4) = 6.0532 x 10^(-4) < 6.1 x 10^(-4).
The margin is 4.7 x 10^(-6).

**(c) The sharpness of log 2 on one limit object.** Object: the constant E = log 2 on DD^4. It is a critical element
with every bound D_0 >= log 2 (Proposition CONST (i); directly, it has two levels 0 in each direction, so
s_*(b) = 1 >= 1/5041, D_*(b) = log 2 in [d_min, D_0], and z_*(b) = 0 <= 256 log 2 + 34.11). Its cube ground level is
e_0(b^3) = 0, so the limit form of Gamma_1, -b e_0(b^3), is 0, and D = log 2 at every scale. The limit form of
Lemma AMP holds for it (log 2 <= 8^s log 2), and it has no seed. So no criterion "D < c and deficit < eps(D)" with
c > log 2 and eps(log 2) > 0 can exclude critical elements. **The claim holds as stated.**

It also holds one level lower, for families of abstract data (an addition, not in row 1032). Put
Z_j(n) := exp(f abs(n)) (1 + exp(-eps_j abs(n))), with u_j := 4(j + 3) and eps_j := u_j^(-5). Each Z_j is a datum:
(E1) holds; (E2) holds with the two eigenvalues exp(f abs(B)) > exp((f - eps_j) abs(B)); (E3) holds with inf = f.
Its deficit is c_j = 0. So Gamma_1^+ = 0, D_j(L/a_j) = log(1 + exp(-eps_j (L/a_j)^4)) -> log 2, and D^+ = log 2 at
every L in P. The gap times side is (L/a_j) m_j = eps_j (L/a_j)^4 -> 0, so z^- = 0 and (W) fails directly; the thermal
sum tends to 1, so (PHYS-SEED) fails as well. So the strict "D^+(L) < log 2" of GS-eq cannot become "<=", and cannot be
raised, for families of abstract data. For Wilson SU(2) trajectories sharpness is neither shown nor claimed.

### Step 3 (done): Section 7.2c line by line (Lemma RISE, Lemma AMP, Theorem GS-dir, Corollary GS-eq)

First, the two standing facts, since every statement below reads them.

- **(M1) HOLDS.** F(k, B)/k = log (Tr T_B^k)^(1/k) does not increase in k (Lemma A (a)). Divide by abs(B) and subtract f:
  M(k, B) does not increase in k. By (E1) the same holds in each side. M >= 0 because f is the infimum.
- **(M2) HOLDS.** By (E2), F(k, B) = k log lambda_0(B) + log(1 + S(k; B)). Subtracting f k abs(B) gives
  Delta(k, B) = k c(B) + g(k; B). S(k; B) is a sum of k-th powers of numbers in [0, 1). It is finite for k >= 3,
  because Z(3, B) is finite. It does not increase in k, and it tends to 0 by dominated convergence against k = 3.
  So g(k; B)/k -> 0, and inf over k of Delta(k, B)/k = c(B) = lim. Delta >= 0 gives c >= 0.

**Lemma RISE: HOLDS.** First line: g(2T; B) <= g(T; B), so Delta(2T, B) <= Delta(T, B) + T c(B). Second line: see
Step 2 (a), with the constant 15 rederived. The use of (M1) is the right one: c(B)/abs(B) does not increase in a side
of B. (c(B) itself can increase in a side; see m1.) Consequence paragraph: D^+(2L) <= D^+(L) + 15 Gamma_1^+(L), since
the upper limit of a sum is at most the sum of the upper limits, in [0, +infinity]. Induction from L_1 gives
D^+(2^k L_1) <= D^+(L_1) + 15 x (the sum over i < k of Gamma_1^+(2^i L_1)). So the bound of (BDD-Delta) is right, with
L_0 = L_1.

**Lemma AMP: HOLDS.** Line 1: S(2k; B) = sum r_i^(2k) <= (sum r_i^k)^2, since the cross terms are non-negative. So
S(2^s a; a^3) <= S(a; a^3)^(2^s). Line 2 is (M2) at time 2^s a and box a^3, with 2^s a c(a^3) = 2^s Gamma_1(a).
Line 3 is (M1) applied to sides 2-4 (from a up to 2^s a), which gives D(2^s a) <= (2^s a)^4/(2^s a x a^3) x
Delta(2^s a, a, a, a) = 8^s Delta(2^s a, a, a, a). Line 4: G_0(a) <= D(a). The shorter reason is (M2) with c >= 0:
D(a) = g(a; a^3) + a c(a^3) >= g(a; a^3). The bound is monotone in S, so S <= exp(D) - 1 may be inserted.

**Theorem GS-dir: HOLDS (given Theorem ZD-c and (I) iff (W)).** The checks, line by line:
1. Sizes. Under (S0), n = L/a_j is an integer at least 12 for every L in P and all large j, so Lemma AMP applies. The
   size 2^s L is in P.
2. Phi(d, gamma) = 8^s [log(1 + (exp(d) - 1)^(2^s)) + 2^s gamma] is continuous on [0, infinity)^2 and does not
   decrease in either argument. D^+(L) is finite by hypothesis, and Gamma_1^+(L) <= D^+(L). For eta > 0 and all large
   j, D_j(n) <= D^+(L) + eta and Gamma_(1,j)(n) <= Gamma_1^+(L) + eta. So
   D^+(2^s L) <= Phi(D^+(L) + eta, Gamma_1^+(L) + eta) for every eta, and continuity gives the stated bound.
3. Conclusion. D^+(2^s L) < 6.1 x 10^(-4) is (PHYS-SEED-Delta) at l' = 2^s L. On file it is strict, and so is the
   hypothesis here. Theorem ZD-c gives (PHYS-SEED). Then (I) iff (W) (fact (F3), no (BDD-Delta) needed) gives (W).
4. Direction. Only "hypothesis => seed" is claimed, and it is the one proved. If D^+(L) >= log 2, the hypothesis
   fails for every s, because 8^s log 2 > 6.1 x 10^(-4). So nothing is claimed there.

**Corollary GS-eq: HOLDS AFTER CORRECTION (m2, one missing line; nothing false).**
1. eps_*(d) > 0 for d in [0, log 2). With x = exp(d) - 1 in [0, 1), 8^s log(1 + x^(2^s)) <= 8^s x^(2^s) -> 0. So
   some term of the supremum is positive.
2. "If". If Gamma_1^+(L) < eps_*(d), some s has Gamma_1^+(L) < 2^(-s)[6.1 x 10^(-4) 8^(-s) - log(1 + x^(2^s))].
   Multiply by 16^s: this is the hypothesis of GS-dir. D^+(L) < log 2 makes D^+(L) finite.
3. "Only if". (W) gives (PHYS-SEED) by (I) iff (W). Lemma Z3 gives D^+(2^k l) <= 1024 q'^(2^k)/5041 -> 0, and
   Gamma_1^+ <= D^+. The s = 0 term is exactly 6.1 x 10^(-4) - d. At a size with d < 3.05 x 10^(-4):
   Gamma_1^+ <= d < 6.1 x 10^(-4) - d <= eps_*(d). Correct.
4. Quantifiers. Both sides are "there is one L in P". The equivalence is between two one-size statements. Each is
   equivalent to (W).
5. "In particular". It needs eps_*(D^+(L)) >= eps_*(D_0) > 0 at the sizes used. That holds because eps_* does not
   increase in d: each term of the supremum decreases in d. The text does not say this. **Correction m2**: add
   "eps_* is non-increasing in d, since each term of the supremum is", before "In particular".

**The even-seed variant "in five lines" (7.2c, "Standing against the lane"): HOLDS as a description.** The new proof is
Lemma AMP (three sentences) plus GS-dir (three sentences). It needs no compactness and no flux sector. The comparison
with (ES) is accurate. (ES) at `gap-means-max.md` L29 has two thresholds of 10^(-7): the even thermal sum, and the
defect of additivity of the vacuum energy over one doubling. GS-eq has the full thermal sum below 1 with any margin,
and the deficit against the bulk below eps_*. The sentence "branch (II) needs deficits of the cubes that are not
summable along the doublings" omits a case. **Correction m4**: write "branch (II) needs, at every size of P where
D^+ is finite, deficits of the cubes that are not summable along the doublings; or D^+ = +infinity at every size of
P". RISE's consequence holds only from a size with D^+ finite.
