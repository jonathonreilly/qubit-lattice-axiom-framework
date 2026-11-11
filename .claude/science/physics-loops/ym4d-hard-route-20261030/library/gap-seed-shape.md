lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T22:06Z

# gap-seed-shape: how small a box can carry the seed (FINISH row 705)

Written by Claude Fable 5.2 (model id claude-fable-5-2, medium effort), Mac mini worker, one session, no subagents, pinned at commit 95828cfbf. Not checked by another model. Research-stage working state; no mass gap is claimed and the seed at a coupling of order one is not attempted.

## Status block

(Updated in place as targets are done.)

| Target | State |
|---|---|
| 1 Theorem S for shapes | started 2026-11-11T10:06Z, reading sources |
| 2 Free-energy form | not started |
| 3 Limit of the method | not started |
| 4 Ceiling model | not started |
| 5 GUIDE: correlation lengths | not started |
| 6 Strong-coupling test | not started |

## 0. Repo search, sources, credits

- **Repo search (rule 0a).** `grep -n -i "seed\|shape\|S(n" library/open-core.md`: no line. FINISH rows 697 to 706: row 697 (author, Theorem S), 698 and 699 (checks; Lemma E', Corollary S3'), 700 and 703 (limit state; Lemma V), 701 and 704 (strong coupling seed and its check), 702 (literature), 706 (`gap-seed-size`, published lattice numbers for the size of the seed box; GUIDE). None covers the shape of the seed box. Row 706 overlaps Target 5 only in subject: it reads published numbers, Target 5 here counts correlation lengths in a stated model. I attack no lemma that another row covers.
- **Read in full:** FINISH row 705; GOAL.md; `library/gap-crux-restate.md` lines 1 to 232 (Sections 0 to 3, as corrected); `library/gap-seed-limit-check.md` whole (Part B, Lemma V); `library/gap-seed-sc.md` Sections 1, 5, 6; `library/gap-seed-check.md` Lemma 1.1 and Verdict (1). **Not read:** the body of `gap-transfer.md`, `gap-seed-check-astra.md`, every primary paper. Nothing was fetched from the network.
- **Credits.** Lemmas A, K, X, E, Theorem S, Theorem D: Claude Fable 5.2 max (row 697). Lemma E', Corollary S3': Codex gpt-6-astra (row 699). Lemma V: Claude Opus 5.5 (row 703). Transfer operator: Osterwalder and Seiler, Luscher, through rows 667, 671, 698. Sussman and Alpoge with Claude and Codex: the account is the ultraviolet part of the chain; no statement of theirs is used in a proof below. Peierls; Onsager (RECALLED only, Target 4).
- **Marks.** PROVED = proved by hand in this file from the named inputs, not checked by another model. PROVED GIVEN (X). GUIDE = estimate or recalled fact, used in no proof. OPEN.

## 1. Target 1: Theorem S for shapes

### 1.1 Setting and notation

As in `gap-crux-restate.md` Section 1 and 3.4. Z(n_1, ..., n_4) is the partition function of the torus, symmetric under permutations of the sides, all sides at least 3. For a box B = (b_1, b_2, b_3) and a time t >= 3, T_B is the transfer operator (Lemma 1.1 of `gap-seed-check.md`), S(t; B) the thermal sum, and

g(t; B) := log(1 + S(t; B)) = log Z(t, B) - t log lambda_0(B) >= 0.

Facts used (all from the row-697 file, checked in rows 698, 699):
- (T) S(t + t'; B) <= S(t; B) S(t'; B); so g is non-increasing in t and S(it; B) <= S(t; B)^i for integers i >= 1.
- (A) Lemma A (a): for a positive trace-class operator, k -> (Tr S^k)^(1/k) is non-increasing.
- (K), (X) Lemma K and Lemma X for the two-direction function W(x, y) = Z(x, y, c, d) with any fixed c, d >= 3: kappa >= 0, and (y - x) kappa(y) <= g_W(x, y) for 3 <= x < y. Here g_W(x, y) = g(x; (y, c, d)), kappa(y) = e(y) - ell y, e(y) = log lambda_0((y, c, d)), ell = inf log W(x, y)/(x y), which depends on (c, d).

Everything in this section holds in the abstract setting of the lemmas (a symmetric Z with a positive trace-class transfer operator in each direction, integer multiplicities, simple top eigenvalue), so for every gauge group.

### 1.2 Lemma E2 (enlarging one side, with the deficit read at a second time) — PROVED from (A), (K), (X)

**Lemma E2.** Let B be a box, d one of its directions, b its side in that direction, h >= b an integer, and B^h the box with the side b replaced by h. Let t >= 3 and t' be integers with 3 <= t' < b. Then

g(t; B^h) <= (h/b) [ g(t; B) + (t/(b - t')) g(t'; B) ].

Proof. Let (c, d') be the two other sides of B and W(x, y) = Z(x, y, c, d'), with y the side in direction d. By the symmetry of Z, W(t, y) = Tr (T_t)^y, where T_t is the transfer operator in direction d of the box (t, c, d'). By (A) and h >= b: W(t, h) <= W(t, b)^(h/b). Write log W(t, y) = t e(y) + g_W(t, y) = ell t y + t kappa(y) + g_W(t, y). The terms ell t h cancel:

t kappa(h) + g_W(t, h) <= (h/b) (t kappa(b) + g_W(t, b)).

kappa(h) >= 0 by (K). By (X) with x = t' < y = b: kappa(b) <= g_W(t', b)/(b - t'). QED

Remarks. (i) t' = t < b gives Lemma E' of row 699: g(t; B^h) <= (h/(b - t)) g(t; B). (ii) The time t need not be below b. (iii) The gain: the deficit kappa(b) of the ground state is of the size of the thermal sum at the longest time below b for which one has a bound, not at the time t. With t' = q a and a seed s at time a, g(t'; B) <= log(1 + s^q). So the second term is of higher order in s, and the leading factor is h/b, the ratio of the volumes. Lemma E' has the factor h/(b - t).

### 1.3 Proposition B3 (three directions, any order) — PROVED from Lemma E2

**Proposition B3.** Let B = (b_1, b_2, b_3), H = (h_1, h_2, h_3) with h_i >= b_i integers, a >= 3, and integers 1 <= p <= q with q a < min b_i. Put beta_i = b_i/(b_i - q a), Pi = beta_1 beta_2 beta_3, G_p = g(pa; B), G_q = g(qa; B), |H|/|B| = product of h_i/b_i. Then

(B3-q) g(qa; H) <= (|H|/|B|) Pi G_q,
(B3-p) g(pa; H) <= (|H|/|B|) [ G_p + (p/q)(Pi - 1) G_q ].

The bound does not depend on the order in which the three sides are enlarged.

Proof. Enlarge the sides in the order 1, 2, 3; B_k is the box after k steps. Lemma E2 with t = t' = qa: g(qa; B_k) <= (h_k/b_k) beta_k g(qa; B_(k-1)), which gives (B3-q) and the intermediate bounds. Lemma E2 with t = pa, t' = qa and alpha_k := pa/(b_k - qa) = (p/q)(beta_k - 1):

g(pa; B_k) <= (h_k/b_k) [ g(pa; B_(k-1)) + alpha_k g(qa; B_(k-1)) ].

By induction g(pa; B_3) <= (|H|/|B|) [ G_p + (alpha_1 + alpha_2 beta_1 + alpha_3 beta_1 beta_2) G_q ], and (beta_1 - 1) + (beta_2 - 1) beta_1 + (beta_3 - 1) beta_1 beta_2 = Pi - 1. The result is symmetric in the three directions, so every order gives the same bound. QED

### 1.4 Theorem SH (the recursion for a box of any shape, step j) — PROVED from B3 and (T)

**Theorem SH.** Let a >= 3, B = (b_1, b_2, b_3) with min b_i > a, and s = S(a; B). Let j >= 2, and p, q integers with p dividing j, p <= q, q a < min b_i. Put Pi = product of b_i/(b_i - qa), C = (p/q)(Pi - 1), and

phi(x) := [ (1 + x^p)^(j^3) (1 + x^q)^(j^3 C) - 1 ]^(j/p).

Then S(ja; jB) <= phi(s). The pair (ja, jB) has the same shape and the same Pi, so with a_k = j^k a, B_k = j^k B, s_k = S(a_k; B_k): s_(k+1) <= phi(s_k).

Let x_0 > 0 and K > 0 be such that phi(x) <= K^(j-1) x^j for 0 <= x <= x_0, and K x_0 <= 1. If s <= x_0 and K s < 1, then for all k >= 0:

(i) K s_k <= (K s)^(j^k), and m(B_k) >= log(1/(K s))/a + log(K)/(j^k a);
(ii) for every integer L >= max_i b_i, with k the largest integer such that j^k max b_i <= L, and E := (j rmax/(rmin - 1))^3 where rmin = min b_i/a and rmax = max b_i/a: 1 + S(a_k; L^3) <= (1 + s_k)^E, and

m(L^3) >= (1/a) [ log(1/(K s)) - j^(-k) log(e E/K) ];

(iii) inf over L >= max b_i of m(L^3) > 0 and liminf over L of m(L^3) >= log(1/(K s))/a. With L_0 := j^(k_0) max b_i and j^(k_0) >= 2 log(e E/K)/log(1/(K s)) (k_0 = 0 if e E <= K): m(L^3) >= log(1/(K s))/(2a) for every integer L >= L_0.

A sufficient choice: with u_0 := j^3 (x_0^p + C x_0^q), K^(j-1) = [ j^3 (1 + C x_0^(q-p)) exp(u_0) ]^(j/p).

Proof. By (T), g(pa; B) <= log(1 + s^p) and g(qa; B) <= log(1 + s^q). Proposition B3 with H = jB: g(pa; jB) <= j^3 [log(1 + s^p) + C log(1 + s^q)]. So 1 + S(pa; jB) <= (1 + s^p)^(j^3) (1 + s^q)^(j^3 C), and S(ja; jB) <= S(pa; jB)^(j/p) by (T). The hypotheses hold again for (ja, jB): q (ja) < j min b_i, and Pi is unchanged.
(i) Induction: K s_(k+1) <= K^j s_k^j = (K s_k)^j, and K s_k <= (K s)^(j^k) <= K s gives s_k <= s <= x_0, so the bound on phi applies at every step. The top eigenvalue is simple, so exp(-a_k m(B_k)) <= s_k and m(B_k) >= (1/a_k)(j^k log(1/(Ks)) + log K).
(ii) Lemma E' (Lemma E2 with t = t' = a_k) in the three directions, from the side j^k b_i to L >= j^k b_i: each exponent is L/(j^k b_i - a_k) < j^(k+1) max b / (j^k (b_i - a)) <= j rmax/(rmin - 1). So g(a_k; L^3) <= E log(1 + s_k). If E s_k <= 1, then S(a_k; L^3) <= exp(E s_k) - 1 <= e E s_k and m(L^3) >= (1/a_k)(log(1/s_k) - log(e E)) >= (1/a_k)(j^k log(1/(Ks)) + log K - log(eE)). If E s_k > 1, the right side of the claim is negative and m(L^3) > 0.
(iii) Each cube has m > 0 (simple top eigenvalue), the bound of (ii) is positive for all large k, and for k >= k_0 it is at least half of log(1/(Ks))/a.
The sufficient choice: for x <= x_0, u(x) := j^3 (log(1 + x^p) + C log(1 + x^q)) <= j^3 x^p (1 + C x_0^(q-p)) and u(x) <= u_0; e^u - 1 <= u e^u. QED

**The ratio 2 gives back Theorem S, and the ratio 3 the map of the row.** Cube b = 2a, j = 2, p = q = 1: Pi = 8, C = 7, phi(x) = ((1 + x)^64 - 1)^2. Cube b = 3a, j = 2, p = q = 1: Pi = 27/8, C = 19/8, 8 (1 + C) = 27, phi(x) = ((1 + x)^27 - 1)^2. With p = q = 1 and a cube of ratio r = b/a the exponent is (j r/(r - 1))^3.

### 1.5 Explicit thresholds t(r) for cubes — PROVED (each line is checked by hand below)

r = b/a. "t" means: if s = S(a; b^3) <= t (strictly below 1/K), Theorem SH (i) to (iii) hold with the K of the line.

| r = b/a | step (j, p, q) | phi(x) | threshold t | K | sides reached by (i) |
|---|---|---|---|---|---|
| 2 | (3, 1, 1) | ((1+x)^216 - 1)^3 | 1/3500 | 3500 | 3^k b |
| 2 | first b -> 2b at time a (Lemma E three times), then the line r = 4 | | 1/1650 | 1479 (rate log(1/(1479 s))/a) | 2^(k+1) b |
| 3 | (2, 1, 2) | [(1+x)^8 (1+x^2)^104 - 1]^2 | 1/100 | 98 | 2^k b |
| 4 | (2, 2, 3) | (1+x^2)^8 (1+x^3)^336 - 1 | 1/25 | 22.2 | 2^k b |
| 6 | (2, 2, 5) | (1+x^2)^8 (1+x^5)^688 - 1 | 1/10 | 9.48 | 2^k b |
| >= 24 | (6, 6, 12) | at most (1+x^6)^216 (1+x^12)^756 - 1 | 3/10 | 3.03 | 6^k b |
| >= 4j | (j, j, 2j) | at most (1+x^j)^(j^3) (1+x^(2j))^(3.5 j^3) - 1 | tends to 1 as j grows | | j^k b |

For the old shape r = 2 with step 2 (Theorem S itself): t = 31/131072 > 1/4229 in place of 1/5041, with phi(x) <= x^2/t for x <= t.

Hand checks.
- r = 2, (2,1,1): phi(x) <= (64 x e^(64x))^2, so phi(x)/x <= 4096 x e^(128 x). At x = t = (1 - 1/32)/4096: 4096 t e^(128 t) = (1 - 1/32) e^((1 - 1/32)/32) <= (1 - 1/32) e^(1/32) < 1, because (1 - y) e^y < 1. The left side increases with x, so phi(x) <= x^2/t on [0, t]: K = 1/t.
- r = 2, (3,1,1): Pi = 8, j^3 (1 + C) = 27 x 8 = 216. phi(x) <= (216 x e^(216 x))^3 = 216^3 e^(648 x) x^3. For x <= 1/3500: 648/3500 < 0.18515, e^0.18515 < 1.2034 (series: 1 + 0.18515 + 0.01714 + 0.00106 + 0.00005), 216^3 = 10077696, 10077696 x 1.2034 < 12127500 < 12250000 = 3500^2. So phi(x) <= K^2 x^3 with K = 3500.
- r = 3, (2,1,2): beta = 3, Pi = 27, C = 13. For x <= 0.01: u <= 8x + 104 x^2 <= 9.04 x <= 0.0904; e^0.0904 < 1.0947; e^u - 1 <= 9.8961 x; phi <= 97.94 x^2. K = 98, K x_0 = 0.98.
- r = 4, (2,2,3): beta = 4, Pi = 64, C = (2/3) 63 = 42. For x <= 0.04: u <= 8x^2 + 336 x^3 <= 21.44 x^2 <= 0.034304; e^0.034304 < 1.0349; phi = e^u - 1 <= 22.19 x^2. K = 22.2, K x_0 = 0.888. (The three steps written out: g(3a) is multiplied by 2 x 4 = 8 in each direction; g(2a; B_k) <= 2 g(2a; B_(k-1)) + 4 g(3a; B_(k-1)); so g(2a; (2b)^3) <= 8 G_2 + (4 x 4 + 4 x 16 + 4 x 64) G_3 = 8 G_2 + 336 G_3.)
- r = 6, (2,2,5): beta = 6, Pi = 216, C = (2/5) 215 = 86. For x <= 0.1: u <= 8x^2 + 688 x^5 <= 8.688 x^2 <= 0.08688; e^0.08688 < 1.0908; phi <= 9.477 x^2. K = 9.48, K x_0 = 0.948.
- r >= 4j, (j, j, 2j): 2j a <= b/2, so beta <= 2, Pi <= 8, C <= 3.5, and phi(x) <= exp(j^3 x^j (1 + 3.5 x^j)) - 1. j = 6, x <= 0.3: u <= 216 x 0.000729 x 1.0026 < 0.1579, e^0.1579 < 1.1711, phi <= 253.6 x^6, and 3.03^5 > 255. K = 3.03, K x_0 = 0.909.
- The threshold tends to 1: let 0 < t < 1. For x <= t: phi(x) <= 4.5 j^3 exp(4.5 j^3 t^j) x^j. Since j^3 t^(j-1) tends to 0, there is j with 4.5 j^3 exp(4.5 j^3 t^j) t^(j-1) < 1; put K^(j-1) equal to the left factor. Then K t < 1. So for every t < 1 there are j and r_0 = 4j such that a seed S(a; b^3) <= t with b >= r_0 a gives the conclusions of Theorem SH.
- r = 2, two stages: Lemma E three times (or B3 with p = q = 1, H = 2B): 1 + S(a; (4a)^3) <= (1 + s)^64. For s <= 1/1650: 64 s <= 0.03879, e^0.03879 < 1.0396, so s_1 := S(a; (4a)^3) <= 0.0396 < 1/25, and s_1 <= 64 s e^(64 s) <= 66.6 s. The line r = 4 applies to the pair (a, 4a): rate log(1/(22.2 s_1))/a >= log(1/(1479 s))/a.

So at the shape of Theorem S the seed threshold is raised from 1/5041 to 1/1650, and at the ratios 3, 4, 6 it is 1/100, 1/25, 1/10. These are thresholds on S(a; b^3) at a larger box, which is a larger number; Target 5 compares them in one model.

**Other ratios (formula PROVED; fixed points computed by hand to two digits, GUIDE).** For 2 < r <= 3 the step (2, 1, 2) gives phi(x) = [(1+x)^8 (1+x^2)^(4 (beta^3 - 1)) - 1]^2 with beta = r/(r - 2); the fixed point is about 1/1330, 1/430, 1/250, 1/180, 1/140, 1/92 at r = 2.1, 2.2, 2.3, 2.4, 2.5, 3. For r = 5: (2,2,4) gives about 1/12. For r = 8: (4,4,6) gives about 0.18.

### 1.6 Boxes with three different sides — PROVED (Theorem SH as stated)

Theorem SH is stated for any box B = (b_1, b_2, b_3) with min b_i > q a. The shape enters through Pi = product of b_i/(b_i - qa) only, and Proposition B3 shows that the order of the directions is immaterial. Example: a = n, B = (2n, 4n, 4n), (j, p, q) = (2, 1, 1): Pi = 2 x (4/3)^2 = 32/9, exponent 8 Pi = 256/9 < 28.5, phi(x) = ((1+x)^(256/9) - 1)^2, threshold at least 1/880 (phi(x)/x <= (28.5 e^(28.5 x))^2 x, and at x = 1/880 this is 812.25 e^(0.0648)/880 < 0.985). The conclusion (ii) reaches every cube of side L >= max b_i.

Not treated: gap bounds for boxes that are not cubes and not of the form j^k B (the same Lemma E' argument gives them for every box H with h_i >= j^k b_i and h_i < j^(k+1) b_i; I state only cubes).

### 1.7 What stays open in Target 1

- The thresholds are for the recursion of Theorem SH. Whether a seed with S(a; b^3) between t(r) and 1 gives a gap is OPEN (see Targets 3 and 4: above 1 it is false).
- For r <= 2 exactly (b <= 2a) only p = q = 1 is available, since Lemma E2 needs a second time t' >= 2a below b. For 1 < r < 2 the exponent (j r/(r-1))^3 of Lemma E' is all there is; the threshold tends to 0 as r tends to 1. For r <= 1 the lemmas give nothing (Lemma X needs x < y).
