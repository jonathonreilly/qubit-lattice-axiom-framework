lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T01:26Z

# Check of row 1032 Section 7 (`library/gap-afield-b-max.md`), FINISH row 1049 `gap-afield-b-check-opus`

Written by Claude Opus 5.5 at max effort on Mac mini worker 3, started 2026-11-16 13:26Z,
from commit eb05ae6aa of branch `claude/ym4d-hard-route`. Same provider as the author of
row 1032 (Claude Fable 5.2 max), so this is not an independent check in the sense of the
working rules; row 1050 is the cross-provider check. A research check, not an audit; no
mass gap is claimed. No new attack (row 1049: "No new attack").

Status: done 2026-11-16 13:44Z (date -u), all eight steps. Verdicts and the RESULT line are in
Step 8. Section 7 has no failing line. Two statements hold after a correction (GS-eq, GS), and
three wording fixes are listed.

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

### Step 1 (done 2026-11-16, before 13:40Z): sources read, and what each says on file

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

### Step 4 (done): Lemma BAR, Lemma CHAIN-4, Corollary NUC

**Lemma BAR: HOLDS.**
- Step 0. Theorem D (a) uses only Lemma A (a) in each direction, so it holds for every datum. Subtract
  f (2a)^4 = 16 f a^4: D(2a) <= 16 D(a). It passes to D^+. (It also follows from RISE and Gamma_1 <= D.)
- (1) => (2). With D_* = D_0 + 1 the premise of (BAR) never holds on L >= L_0. Correct, and vacuous, as the text says.
- (2) => (1). Taking L_2 >= L_1 is allowed, because (BAR) on a tail stays true on a smaller tail. L_2 = 2^k L_1,
  since both are in P, and so D^+(L_2) <= 16^k D^+(L_1) < infinity. Induction with M_0 = max(D^+(L_2), 16 D_*)
  covers both branches. A negative or zero D_* is harmless: the second branch then never occurs.
- (BAR-lat). For fixed i and j >= max over i' < i of j_0(2^(i') L_2), the induction runs inside the one datum Z_j
  over i' = 0, ..., i - 1. Every side 2^(i') L_2/a_j is an integer at least 12 under (S0). The upper limit of
  max(D_j(L_2/a_j), 16 D_*) is max(D^+(L_2), 16 D_*). Correct.
- The text after the lemma. "(BAR) alone is (BDD-Delta) in other words" agrees with the lemma. The three tries at
  (INV) are marked ARGUED. They are not checked here as proofs. The use of Lemma PT (D adds over products) matches K1
  on file. One reading point: (MONO-Delta) of row 720 is monotony in the coupling at a fixed lattice size. Along the
  trajectory it gives D^+(2L) <= D^+(L) at all levels (`gap-phys-seed.md` L361). So the comparison "monotony
  everywhere" against "monotony above D_*" is fair. The Ising failure (L369) is at levels near log 2.

**Lemma CHAIN-4: HOLDS.**
- (1). Gamma_0(a) = a^4 M(a^4) = D(a). m_(i+1) <= m_i, because the set for m_(i+1) contains k_(i+1) = a. m_4 = 0 by
  the definition of f.
- (2). The telescoping sum gives D = G_0 + ... + G_3 with each G_i >= 0. Also Gamma_1 = G_1 + G_2 + G_3, so
  D = G_0 + Gamma_1, which 7.2c uses.
- (3). The inner limits are monotone by (M1), so each infimum over i free sides is a limit along equal sides k. The
  identity g = Delta(a, B_(i,k)) - a c(B_(i,k)) is (M2). Delta(a, B_(i,k))/k^i = a^(4-i) M(k^i, a^(4-i)) ->
  a^(4-i) m_i(a). Next, c(B_(i,k))/k^i = abs(B_(i,k)) k^(-i) inf over T of M(T, B_(i,k)) =
  a^(3-i) inf over T of M(T, k^i, a^(3-i)). This does not increase in k, and its limit is the infimum over T and k.
  By (M1) that is the infimum over all (T, k_1, ..., k_i), which is m_(i+1)(a). Both limits are finite. Multiplying
  by a^i gives G_i. Correct.
- (4). Gamma_1(a) = a^4 inf over T of Delta(T, a^3)/(T a^3) = a c(a^3) by (M2). i = 3: Gamma_4 = 0, so
  G_3 = Gamma_3 = a^3 lim k^(-3) g(a; k^3). That is a^4 times the vacuum-subtracted pressure at temperature 1/a,
  which is pi(a) of Q4 (`gap-phys-seed.md` L195). Subtracting lambda_0(k^3) instead of the bulk changes nothing,
  because c(k^3)/k^3 -> 0. i = 0: G_0 = g(a; a^3).

**Corollary NUC: HOLDS.** "=>": 0 <= G_i <= D. "<=": the upper limit of the sum is at most the sum of the upper
limits, so D^+ <= 4 D_0'. The sentence "(NUC) of idea B5 is (BDD-Delta) exactly" is right for the upper-limit
reading, which is the reading of (BDD-Delta) (an upper limit over j at each L). **Wording m5**: B5's (NUC), at
L145, reads "for all large j and all large L in P". If the threshold in j is meant to be uniform in L, that is
stronger than (BDD-Delta). Write it with upper limits, as Corollary NUC does. B5 also names the lemma "Lemma NUC-4".
Section 7 calls it "Lemma CHAIN-4".

**m1 (wording, in the standing inputs L282 and in CHAIN-4's "Not new", L324).** "I call c(B) the deficit ... it is
kappa of Lemma K in two variables" and "the monotony of the deficit in one side is Lemma K" are not right as written.
Lemma K's kappa(b) = e(b) - ell b is measured against ell = inf over (a, b) of log Z(a, b, c, d)/(ab). That infimum
has the two other sides fixed. c(B) is measured against f abs(B). Since ell >= f c d, kappa <= c((b, c, d)), with
equality only when ell = f c d. Also b -> c((b, c, d)) is convex and grows like (ell - f c d) b. So c(B) itself is not
non-increasing in a side when ell > f c d. c(B)/abs(B) is non-increasing in each side, by (M1). No proof in
Section 7 uses the wrong form: RISE and CAS-0 use (M1). Repair: replace the two phrases by "kappa of Lemma K is
c(B) minus (ell - f c d) b. What Section 7 uses is (M1): c(B)/abs(B) is non-increasing in each side."

### Step 5 (done): Proposition CAS-0 and Corollary GS (given Theorems CE and CR)

**The setting paragraph of 7.2b: HOLDS.** The spectral form with e_0^*(B) finite and at most 0, and with multiplicities
that are non-negative integers, is CE (ii)(b) at CRm L175. Symmetry is CE (ii)(a). Two facts are not stated as such
on file. (M1) for E is a non-strict inequality between two values, so CE (ii)(c) carries it. Directly: the rescaled
data satisfy Delta^(j,k)(x)/abs(x) >= Delta^(j,k)(y)/abs(y) when y >= x side by side, and pointwise limits keep this.
-e_0(B) = lim over T in DD of E(T, B)/T follows from the spectral form, since the sum over the levels above e_0 is
finite at one T.

**Proposition CAS-0: HOLDS.**
- Step 1. (M1) for E with B >= (b, b, b) side by side gives E(T, B)/(T abs(B)) <= E(T, b^3)/(T b^3). The limit in T
  gives -e_0(B)/abs(B) <= 0, so e_0(B) = 0. Correct.
- Step 2. With all e_r(B) >= 0, T -> sum of exp(-T e_r(B)) does not increase. By symmetry this holds in each side.
  Correct.
- Step 3. Correct, with one reading point that does not break it. The text uses "R unbounded above and below".
  The definition (`gap-dichotomy.md` 1.4, CRm L230) says "bounded gaps". Proposition OM (d)'s proof (CRm L236) gives
  every t in Z within max abs(n_l) of a return time, which is syndetic in Z. So both directions hold for the elements
  Corollary GS uses, and a fixed point returns at every t. Also, Step 4 uses Step 3 only for t >= 0. For that,
  "R unbounded above" is enough: h is non-increasing, so h(t) >= h(t') > h(0) - eps for some t' >= t in R, and
  h(t) <= h(0). So the proposition holds under the weakest reading too.
- Step 4. The chain E(x) >= E(2^s x_1, x_2, x_3, x_4) >= E(2^s x) = E(x) holds for s >= 0. So E does not change when
  one side is multiplied by 2^s, s >= 0. Two elements of DD differ by such a factor in one direction or the other.
  Correct.
- Step 5. exp(c) = sum of exp(-T e_r) for every T in DD, with every e_r >= 0. If some e_r were above 0, the right
  side would decrease strictly in T. So all levels are 0 and exp(c) = m, finite. The thermal sum of the limit is
  exp(Delta_* + T e_0^*) - 1 (CE Step 4, L192) = m - 1. Criticality (CE (ii)(d)) gives m - 1 >= 1/5041, so m >= 2.
  This matches Proposition CONST (i), "only if" (`gap-uv-rigidity-max.md` L727-735).

**Corollary GS: HOLDS AFTER CORRECTION (m3, a citation; nothing false).**
- "(W) fails => (a) or (b)". Theorem CR, (1) iff (4), with D_0 a bound of (BDD-Delta), gives a uniformly recurrent
  element. By CAS-0 it is either the constant log m, or it has e_0(b^3) != 0, hence < 0, for one b. Correct.
- "(a) or (b) => (W) fails". The constant is fixed by sigma, so it is uniformly recurrent. CR gives "not (W)".
  Correct.
- "In lattice terms". By CRm L139 and L149, e_0^(j,k)(b^3) = 2^k u_j E_0^(j)((2^k u_j b)^3) and E_0 = -c. So
  e_0^(j,k)(b^3) = -2^k u_j c_j((2^k u_j b)^3) = -Gamma_(1,j)(2^k u_j b)/b. Correct. **Citation m3**: the text says
  "by Step 4 of Theorem CE the rescaled ground levels converge". The convergence of the levels is in the statement
  of CE (ii) and in its Step 2 (extraction, L184); Step 4 is the thermal sums. The full sequence converges too, not
  only a subsequence: the levels of E are fixed by E (Lemma LV), and e_0^(i) lies in [-C/T, 0].
- "(GS-CAS) and (NO-CONST) give (W)". The physical side of the lattice cube is 2^(k_i) u_(j_i) b a_(j_i) =
  2^(k_i) b l_1. It lies in P for large i and tends to infinity, and j_i -> infinity. So (GS-CAS) gives
  e_0(b^3) >= -eps/b for every eps. Correct. (GS-CAS) is uniform in L and j, which is more than this step uses.
- "(W) gives both". Lemma Z3 is uniform in the size from 2^k l on, for all large j. With Gamma_1 <= D this gives
  (GS-CAS). OM (b), first half, gives an empty Omega(D_0), hence (NO-CONST). Correct.
- Reading. "(GS-CAS) is not easier than (Z-UNB)" is a judgement, not a proved comparison. No implication between
  them is shown. I agree with the reason given: the upper bound on lambda_0 is not variational.

### Step 6 (done): Lemma NOCS and Lemma FP-U1

**Lemma NOCS: HOLDS.**
- (1). X = SU(2)^E = (S^3)^E is simply connected, so its first de Rham group is 0, and a closed 1-form omega is dW_0.
  The averaged W := integral over G of W_0 o phi_g is smooth, and dW = integral of phi_g^* omega = omega. W is
  G-invariant, because Haar measure on a compact group is right-invariant: W o phi_h = integral of W_0 o phi_(gh) dg = W.
  Correct.
- (2). Q_omega u = exp(-W) d(exp(W) u) is right. So phi = exp(-W) > 0 has Q_omega phi = 0 and H phi = c phi. The
  text's route uses the strict positivity of the kernel of exp(-tH) on a compact connected manifold with a smooth
  potential. That is a standard fact, cited and not rebuilt here. **Optional simpler route (no defect)**: H - c =
  (g^2/2) Q^* Q >= 0 as forms gives E_0 >= c, and phi gives E_0 <= c, so c = E_0. Every ground state u is smooth (by
  elliptic regularity) and has ||Q_omega u||^2 = 0, so d(exp(W) u) = 0 and u = const x exp(-W), since X is connected.
  So the ground state is simple and equals phi, without Perron-Frobenius. Either route gives omega = -d log Omega.
- (3). This follows. It answers (CS-lat) as B10 states it at L185: "a closed and not exact gauge-invariant 1-form". Part
  (1) alone excludes that. Part (2) adds that the exact case is only the ground-state transform.
- Remark (i). The Riccati form checks: Q^* eta = d^* eta + <omega, eta>, so
  Q^* Q u = -Lap u + (abs(omega)^2 + d^* omega) u = -Lap u + (abs(omega)^2 - div omega) u.
- Remark (iii) reads (TM): T_B is self-adjoint with a strictly positive top eigenfunction. Correct.
- Remarks (ii) and (iv) are about the continuum and are not claimed as proofs. "SU(2)^V is connected" is true.

**Lemma FP-U1: HOLDS.**
- Setting. The Hessian at omega = 0 of -sum cos(theta_l + omega_x - omega_y) is sum cos(theta_l) D_l D_l^T. This is
  right, because (omega_x - omega_y) = -D_l . omega and (-cos)'' = cos. M kills the constants. It is positive
  definite on their complement when all cos(theta_l) > 0 and the graph is connected.
- (i). c -> log det' M_c is concave (it is linear into positive operators on 1^perp, and log det is concave there).
  dR/dc_l = D_l^T M_c^(-1) D_l >= 0, with D_l in 1^perp. Composing a concave function that is non-decreasing in each
  variable with concave cos(theta_l) on (-pi/2, pi/2) keeps concavity, by the standard two-line argument. Correct.
- (ii). The sum over l of R_l(1) is the trace of M_1^(-1) M_1 on 1^perp, which is N - 1 (Foster's first theorem). For
  n >= 3 the torus has dN distinct links. Translations and the hyperoctahedral group are graph automorphisms. They
  act transitively on unoriented links and commute with M_1, and R_l does not change under D_l -> -D_l. So
  R_l(1) = (N - 1)/(dN). Independent check at d = 1: the effective resistance between neighbours on an n-cycle is
  (n - 1)/n, which agrees. The Taylor step with c_l - 1 = -theta_l^2/2 + O(theta_l^4) gives the stated expansion.
  Correct.
- The "Consequence for B8" matches the kill-table entry L235: -log det' M = const + ((N - 1)/(2dN)) sum theta_l^2 +
  O(theta^4). The SU(2) sentence is marked ARGUED and is not checked here.

### Step 7 (done): Lemma TRI, Proposition SPH, Corollary SPH-LC

**Lemma TRI: HOLDS.** Line by line: (n_1 . sigma)(n_2 . sigma) = n_1 . n_2 + i (n_1 x n_2) . sigma gives
(1/2) tr(g_1 g_2) = cos(theta_1) cos(theta_2) - sin(theta_1) sin(theta_2) t. Conjugation by Haar elements makes n_2
uniform on S^2 (the image of Haar measure under SU(2) -> SO(3)), so t is uniform on [-1, 1] by Archimedes. cos(theta_12)
is then uniform on [cos(theta_1 + theta_2), cos(theta_1 - theta_2)], and the density is sin(theta_12) over the length
2 sin(theta_1) sin(theta_2). Case split: if theta_1 + theta_2 <= pi, the bound theta_12 <= 2 pi - theta_1 - theta_2
follows from theta_12 <= pi. If theta_1 + theta_2 > pi, the bound theta_12 <= theta_1 + theta_2 follows. Both cases
give exactly the inequalities of T. Correct.

**Proposition SPH: HOLDS.**
- The conditional step. g_(k+1) is independent of (g_1, ..., g_k). Given its class angle it is uniform on its class.
  All earlier variables are functions of (g_1, ..., g_k, theta_(k+1)). So TRI with h_(k-1) held fixed gives the
  conditional density of alpha_k given everything earlier. It depends only on (alpha_(k-1), theta_(k+1)).
- The sentence "given these three angles h_1 is uniform on its class" is true, and the proof does not use it.
- The product. There are n - 2 factors 1/2: one at k = 1, then k = 2, ..., n - 3, then the last step. Each
  sin(alpha_k) cancels once. Each sin^2(theta_i), i <= n - 1, loses one power. sin(theta_n) enters once. Dimension
  check: (n - 1) + (n - 3) + 1 = 2n - 3. Independent check at n = 3: the constant (2/pi)^2/2 = 2/pi^2 matches B12's
  L194. The density integrates to 1 by construction (a chain of conditional densities). Correct.

**Corollary SPH-LC: HOLDS.** (log phi)'' = -1/sin^2(theta) - beta cos(theta) =
(1/sin^2(theta))(-1 + beta u (1 - u^2)) with u = -cos(theta). The maximum of u(1 - u^2) on (0, 1) is 2/(3 sqrt 3), at
u = 1/sqrt 3. So the threshold is beta = 3 sqrt(3)/2 = 2.598. "If": a product of log-concave factors with the
indicator of a convex set is log-concave, and Prekopa gives the marginal. "Only if": the point (2.186, 1.5, ..., 1.5)
is interior to P_n for every n >= 3. The checks are 2.186 < 3, 1.5 < 3.686, 5.186 < 6.283, 4.5 < 6.283, and all
entries lie in (0, pi). theta_1 enters only the first triple, and along theta_1 the log-density has a positive second
derivative there. One plaquette: (log sin^2)'' = -2/sin^2 gives beta <= 3 sqrt 3. Correct.

The text after it is not checked here as proofs. The cube surface as two-dimensional theory on a sphere and the
Wishart remark are marked ARGUED. The exponent of the Wishart remark agrees with the Wishart density exponent
(n - p - 1)/2 = -1/2 at n = p = 3.

### Step 8 (done): what GS-eq means, verdicts, defects, scope

**Does GS-eq move (W)? No. It restates (W) at one size.** It is an equivalence, and its proof reads only Theorem ZD-c
(with Lemma Z3) and Lemma AMP, which holds for every datum. It adds no input about Wilson SU(2). Concretely:

1. Its s = 0 term is the old criterion. eps_*(d) >= 6.1 x 10^(-4) - d, so D^+(L) < 3.05 x 10^(-4) at one size
   already satisfies GS-eq. That is (PHYS-SEED-Delta) with half its threshold.
2. Its new range is D^+(L) in [3.05 x 10^(-4), log 2). There the deficit has to sit far below the count. Each term of
   eps_* is at most 6.1 x 10^(-4) 16^(-s). Two values, by hand as in Step 2 (b): eps_*(0.01) = 2.380 x 10^(-6)
   (s = 2; the s = 1 term is negative, since log(1 + x^2) = 1.010 x 10^(-4) > 7.625 x 10^(-5)), and
   eps_*(log(3/2)) = 5.745 x 10^(-10) (s = 5). So the deficit must be about 4,000 times below D^+ at D^+ = 0.01, and
   about 7 x 10^8 times below at D^+ = log(3/2).
3. Who lives in the new range (GUIDE, not proved). A count of order one with a tiny deficit means nearly degenerate
   ground levels with almost no finite-size shift of the vacuum energy. The two-level data of Step 2 (c), at a fixed
   eps, are an abstract example: D < log 2, deficit 0, and a seed at a larger size. In a model with a mass gap m and
   one vacuum, which is the expected Wilson SU(2) picture, G_0 and Gamma_1 both fall like exp(-mL) times powers of L.
   G_0 counts one-particle states. Gamma_1 is the finite-size shift of the vacuum energy, from particles that wind
   around the torus (Luscher's finite-size formulas, recalled and not rebuilt). Their ratio is a power of mL, not an
   exponential in it. Where D^+ is still above 3.05 x 10^(-4), mL is moderate, so the ratio stays far from the
   10^(-3) to 10^(-9) that item 2 asks for. So such a model meets GS-eq first through the s = 0 term, which is the
   old criterion. The new freedom does not help the expected mechanism.

**Is either side closer to a proof than (W)? No.**
- The deficit side, Gamma_1^+(L) < eps_*(D^+(L)), is an upper bound on lambda_0 of the periodic cube against the bulk.
  It must hold at one physical size where the running coupling is of order one, with precision at most
  6.1 x 10^(-4), and far finer unless D^+ is already small. It is not variational, as row 1032 says. None of the
  lane's tools bounds it: Theorems S and SH, Lemmas Z and Z', and Proposition Delta bound counts by D and gaps.
  Gamma_1 enters D only additively. It also contains f, so it is less finite than the f-free forms on file: (C'_b) of
  Corollary Z1' (`gap-phys-seed.md` L274-279) and the doubling defect of (ES). As a finite-volume test it is a step
  back from those.
- The count side, D^+(L) < log 2, is much weaker than D^+ < 6.1 x 10^(-4), but it is not shown to suffice alone. GS-eq
  makes that side pay through the deficit. Along the trajectory D is large at small physical sizes (the toron valley,
  Lemma FV of row 1028). So D^+ < log 2 is again a statement at a physical size with coupling of order one.
- What GS-eq does add (agreeing with row 1032's own "a form of the wall, not a mechanism"): the threshold log 2 for the
  count is sharp (Step 2 (c)), and the proof is short and needs no compactness. Lemma RISE puts branch (II) in the same
  variables: deficits not summable along the doublings (with the m4 correction).

**Verdicts** (first failing line in Section 7: none)

| Statement (row 1032 Section 7) | Verdict |
|---|---|
| (M1), (M2) (standing facts) | HOLDS |
| Lemma BAR, with (BAR-lat) | HOLDS |
| Lemma CHAIN-4 | HOLDS |
| Corollary NUC | HOLDS (wording m5 concerns B5, not NUC) |
| Proposition CAS-0 (given CE (ii)) | HOLDS |
| Corollary GS (given CR, CE, Z3, OM (b)) | HOLDS AFTER CORRECTION (m3: citation) |
| Lemma RISE (constant 15) | HOLDS |
| Lemma AMP | HOLDS |
| Theorem GS-dir (given ZD-c and (I) iff (W)) | HOLDS |
| Corollary GS-eq | HOLDS AFTER CORRECTION (m2: one missing line) |
| log 2 sharp for limit objects | HOLDS (also for abstract families, Step 2 (c)) |
| even-seed variant "in five lines" and the comparison with (ES) | HOLDS as a description (m4: wording) |
| Lemma NOCS | HOLDS (optional simpler proof of (2), Step 6) |
| Lemma FP-U1 | HOLDS |
| Lemma TRI | HOLDS |
| Proposition SPH | HOLDS |
| Corollary SPH-LC | HOLDS |

**Defects, ranked by what they break (none breaks a consumer):**
1. m2, GS-eq "In particular": add "eps_* is non-increasing in d (each term of the supremum is)". Without it the
   corollary's last sentence is not justified as written. With it, it is.
2. m3, Corollary GS: "by Step 4 of Theorem CE the rescaled ground levels converge" should read "by Theorem CE (ii)
   (Step 2), and for the whole sequence because the levels of E are fixed by Lemma LV".
3. m4, 7.2c last paragraph: branch (II) needs non-summable deficits "at every size of P where D^+ is finite; or
   D^+ = +infinity at every size of P".
4. m1, L282 and L324: c(B) is not Lemma K's kappa, which is measured against ell >= f c d, so kappa <= c. c(B) is not
   non-increasing in a side in general. c(B)/abs(B) is, by (M1), and that is all Section 7 uses.
5. m5, B5 at L145: state (NUC) with upper limits over j, as Corollary NUC does. "Lemma NUC-4" there is "Lemma
   CHAIN-4" in Section 7.

**For the lead (not a defect of row 1032).** Rows 1049 and 1050 attribute "D(2a) at most D(a) + 15 Gamma_1(a)" to
Theorem ZD-c. That inequality is Lemma RISE of row 1032, which reads only (E1), (M1) and (M2). ZD-c enters GS-dir only
as (PHYS-SEED-Delta) => (PHYS-SEED).

**Not covered by this check.**
- The inner proofs of Theorem ZD-c (Theorems S, SH, Lemma E', Corollary S3', Proposition Delta), and of Theorem CE,
  Proposition OM and Theorem CR. They are taken as on file with checks 727 and 1019, which are both same-provider.
- The ARGUED and GUIDE parts of Section 7: the three tries at (INV), the SU(2) part of FP-U1, the cube surface as a
  sphere, the Wishart remark, and the weak-coupling reading of G_0.
- Sections 1-6 and 8 of row 1032, except the idea statements that Section 7 names.
- No numeric run. All arithmetic is by hand and shown above.
- The Sussman-Alpoge repository was not read. Section 7 reads no line of it. Their trajectory enters only through
  (S0), which the lane records as not verified (`gap-dichotomy.md` 1.2).

**Credit.** Every statement checked is by Claude Fable 5.2 (row 1032), built on the lane's rows 697-731, 1017 and 1028
(Lemma A, Theorem D, Lemma K, Theorem ZD-c, Lemma Z3, Theorems CE, CR, Proposition OM, Proposition CONST). The
trajectory is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text), built on
Balaban's renormalisation group. Named classical inputs: Foster's first theorem (effective resistances), Archimedes
(the uniform projection of the sphere), Weyl's integration formula, Prekopa's theorem, the Wishart density, and
Luscher's finite-size formulas (recalled, GUIDE only).

RESULT: Row 1049 (Claude Opus 5.5 max, Mac mini worker 3, same provider as row 1032's author, not an audit, no numeric run): Section 7 of row 1032 has no failing line. HOLDS: BAR (with BAR-lat), CHAIN-4, NUC, CAS-0, RISE, AMP, GS-dir, NOCS, FP-U1, TRI, SPH, SPH-LC. HOLDS AFTER CORRECTION: GS-eq (add that eps_* is non-increasing), GS (cite CE (ii) Step 2, not Step 4). Wording fixes: m1 (c(B) is not Lemma K's kappa and is not monotone in a side; only c(B)/abs(B) is, which is what is used), m4, m5. Hand tests: 15 = 1 + 2 + 4 + 8 is right; it is Lemma RISE, not Theorem ZD-c. eps_*(log(3/2)) = 5.745 x 10^(-10) at s = 5, so the 5.7 x 10^(-10) instance holds. log 2 is sharp on the constant log 2, and also on an explicit family of two-level data. Meaning: GS-eq restates (W) at one size. Its s = 0 term is (PHYS-SEED-Delta) at half the threshold. Its new range (D^+ from 3.05 x 10^(-4) up to log 2) needs a cube deficit far below D^+: 4,000 times below at D^+ = 0.01, and 7 x 10^8 times below at log(3/2). The deficit needs the bulk f and an upper bound on lambda_0 that is not variational. So neither side is closer to a proof than (W). OPEN, not moved: (W), (BDD-Delta), (LIOU), (INV), (GS-CAS), (NO-CONST).
