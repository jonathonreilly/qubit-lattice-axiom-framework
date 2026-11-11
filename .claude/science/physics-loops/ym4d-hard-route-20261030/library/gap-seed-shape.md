lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T22:06Z

# gap-seed-shape: how small a box can carry the seed (FINISH row 705)

Written by Claude Fable 5.2 (model id claude-fable-5-2, medium effort), Mac mini worker, one session, no subagents, pinned at commit 95828cfbf. Not checked by another model. Research-stage working state; no mass gap is claimed and the seed at a coupling of order one is not attempted.

## Status block

(Updated in place as targets are done.)

| Target | State |
|---|---|
| 1 Theorem S for shapes | done (Section 1): Lemma E2, Proposition B3, Theorem SH, thresholds 1/1650 (r = 2), 1/100 (3), 1/25 (4), 1/10 (6), tending to 1; PROVED, not checked |
| 2 Free-energy form | done (Section 2): Theorem D-shape, PROVED |
| 3 Limit of the method | done (Section 3): supremum over shapes is 1; fixed ratio OPEN |
| 4 Ceiling model | done (Section 4): ceiling 1 (two phases; given Peierls, RECALLED); compact Gaussian model in the class, formula PROVED, values GUIDE |
| 5 GUIDE: correlation lengths | done (Section 5), GUIDE |
| 6 Strong-coupling test | done (Section 6), PROVED GIVEN `gap-seed-sc.md` Theorem 1 (unchecked) |

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

### 1.8 A run that tried to refute Lemma E2 (GUIDE; a run can refute, not prove)

Pass and fail were written first: fail if any instance has left side > right side. Two-dimensional Ising model, transfer matrices of rings of length 3 to 11, couplings 0.2, 0.3, 0.38, 0.4407, 0.5, 0.7; all 6480 instances of g(t, h) <= (h/b)[g(t, b) + (t/(b - t')) g(t', b)] with 4 <= b <= h <= 11, 3 <= t' < b, 3 <= t <= 11. No violation. The largest ratio of left to right side was 0.99974, so the lemma is close to sharp in this model. Script: /tmp/gap-seed-shape-scratch/e2check.py on the Mac mini (not in the repository), run under the numeric lock at 59 percent free memory. The proofs do not use the run.

## 2. Target 2: the seed in terms of free energies

F(n) = log Z(n). For a box B and a time a >= 3 put

Phi_B(a) := 2 F(a, B) - F(2a, B),  Psi_B(a) := F(a, B) + F(2a, B) - F(3a, B).

**Theorem D-shape (PROVED from (TM); exact identities).**
- (a) Phi_B(a) = 2 g(a; B) - g(2a; B). So g(a; B) <= Phi_B(a) <= 2 g(a; B), that is

 S(a; B) <= exp(Phi_B(a)) - 1 <= (1 + S(a; B))^2 - 1.

- (b) Psi_B(a) = g(a; B) + g(2a; B) - g(3a; B). So g(a; B) <= Psi_B(a) <= g(a; B) + log(1 + S(a; B)^2).
- (c) In general, for integers k, l >= 3: F(a, B) - (a/k)[F(k + l, B) - F(l, B)] = g(a; B) + (a/k)[g(l; B) - g(k + l; B)] >= g(a; B), and the excess is at most (a/k) log(1 + S(l; B)).
- (d) Phi_B(a; beta) = 12 a |B| times the integral over s in [0, beta] of (abar_(2a, B)(s) - abar_(a, B)(s)), with abar_n the mean plaquette action on the torus n.
- (e) Read backwards: Phi_B(a) >= log(1 + exp(-a m(B))).
- (f) Against Theorem D (b): for B = (2n)^3 and a = n, Phi(n) - Phi_B(n) = 2 [8 F(n,n,n,n) - F(n,2n,2n,2n)] >= 0, where Phi(n) = 16 F(n^4) - F((2n)^4).

Proof. log Z(t, B) = t e(B) + g(t; B) with e(B) = log lambda_0(B), for every t >= 3. The terms with e(B) cancel in (a), (b), (c). g is non-increasing in t and g(2a) <= log(1 + S(a)^2) by (T). (d) dF/dbeta = -6 |n| abar_n and F = 0 at beta = 0 (run 2, Lemma 2, as in Theorem D (f)). (e) g(a) >= log(1 + r_1^a). (f) Lemma A (a) three times: Z(n, 2n, 2n, 2n) <= Z(n^4)^8. QED

**The seed in free energies (PROVED GIVEN Theorem SH).** For a cube of ratio r = b/a in the table of 1.5: if 2 F(a, b, b, b) - F(2a, b, b, b) <= log(1 + t(r)), the conclusions of Theorem SH hold. With three tori, F(a, b^3) + F(2a, b^3) - F(3a, b^3) <= log(1 + t(r)) is enough, and this loses at most the factor 1 + t(r) against the true thermal sum.

Numbers: log(1 + 1/1650) > 6.05 x 10^(-4) (r = 2, against 1.9 x 10^(-4) for Phi(n) before; and Phi_B(n) <= Phi(n)); log(1.01) > 0.0099 (r = 3); log(1.04) > 0.0392 (r = 4); log(1.1) > 0.0953 (r = 6).

**How much each form loses (GUIDE; ideal gas with F = f|n| + sum over mu of (|n|/n_mu) w(n_mu), w(2n) much smaller than w(n)).** g(n; (2n)^3) = 8 n^3 w(n). Phi_B(n) = 16 n^3 w(n), twice the truth. Phi(n) = 64 n^3 w(n), eight times the truth: the symmetric torus n^4 counts the winding in all four directions, each with the volume of 16 small tori. Psi_B(n) is the truth up to second order. So the form with the tori (a, B), (2a, B), (3a, B) gains a factor of about 8 over Theorem D (b) at the same thermal sum, and the form Phi_B a factor of about 4.

## 3. Target 3: the limit of the method

"The method" = the two moves (T) (time multiplied, thermal sum raised to the power) and Lemma E2 (one side enlarged; Lemma E' is the case t' = t), which is every use of Lemmas A, K, X made so far.

**3.1 The order of the three directions is immaterial (PROVED).** Proposition B3: the bound is symmetric.

**3.2 Enlarging a side in two steps is never better than in one (PROVED, as a comparison of the bounds).** Direct: g(t; h) <= (h/b)[g(t; b) + (t/(b - t')) g(t'; b)]. Through h' with b <= h' <= h: g(t; h) <= (h/h')[g(t; h') + (non-negative term)], and the bound for g(t; h') is (h'/b) times the same bracket. So the two-step bound is the direct bound plus a non-negative term.

**3.3 Leading order (PROVED from Theorem SH: the expansion of phi at x = 0).** For q > p: phi(x) = j^(3j/p) x^j (1 + O(x^min(p, q-p))). For q = p: phi(x) = (j^3 Pi)^(j/p) x^j (1 + O(x^p)). So enlarging at the time pa costs, at leading order, only the ratio of the volumes j^3, once a second time qa > pa below the side is available, and the leading threshold is j^(-3j/(p(j-1))). It is largest for p = j: j^(-3/(j-1)), which is 1/8, 0.19, 0.25, 0.30, 0.34 for j = 2, ..., 6 and tends to 1. The constraint is j = p < q < r. The term C x^q, with C = (p/q)((r/(r-q))^3 - 1), is what lowers the true threshold at a given r: the table of 1.5.

**3.4 What a better use of the same lemmas gave.**
- Reading the deficit at a second time (Lemma E2 instead of Lemma E'): raises the threshold at r = 3 from about 1/729 (the map of the row, ((1+x)^27 - 1)^2) to 1/100, and gives 1/25 at r = 4 and 1/10 at r = 6. PROVED.
- A step by a factor 3 at r = 2: 1/3500 instead of 1/4229 (step 2, sharp constant) and 1/5041 (as printed). PROVED. At leading order the threshold with p = q = 1 is (2j)^(-3j/(j-1)) at r = 2: 1/4096, 1/3175, 1/4096, 1/5623 for j = 2, 3, 4, 5; so j = 3 is the best single step there.
- Two stages at r = 2 (enlarge to r = 4 first, at the price (1+s)^64): 1/1650. PROVED. The other first stages I tried by hand give less: to r = 3, about 1/2700; to r = 5, about 1/1500 to 1/1650; to r = 6, about 1/2160 (GUIDE values).
- Another order of the directions: nothing (3.1). 
- Convexity in two directions at once: I computed the joint version (deficit kappa(y, z) of two sides, split as kappa_1(y; z) + y delta(z), each part bounded by a crossing identity) and got the same bound as two successive uses of Lemma E2 with the same second time: the factor 1 + beta. This computation is a sketch (the monotonicity of delta was not written out); I found no gain and do not claim a proof that none exists.

**3.5 The limit over all shapes (PROVED for the lower half; the upper half PROVED GIVEN the Peierls bound, RECALLED, see 4.1).** For every t < 1 there is a ratio r_0 such that S(a; b^3) <= t with b >= r_0 a gives a uniform gap on all large cubes (1.5, last check). For no shape can a threshold above 1 be right (4.1). So the supremum over shapes of the threshold of the best theorem of this kind is exactly 1, and the method reaches it.

**3.6 OPEN.** At a fixed ratio r, the largest threshold that the lemmas give. I have no proof that the entries of the table in 1.5 are optimal for the moves (T) and E2; they are the best of the (j, p, q) I tried. Between t(r) and 1 (for example between 1/1650 and 1 at r = 2) nothing is known: no proof and no gapless model in the class (4.2 gives one below 1 only for r up to about 1.4, GUIDE). I also could not show that the leading coefficient j^3 is attained by a model in the class (the integer gas of Remark N2 has a far smaller coefficient).

## 4. Target 4: ceilings

A ceiling at the shape (a, b): a model that meets every hypothesis the lemmas use (symmetric Z; in each direction Z = Tr T^n with T positive and trace class; simple top eigenvalue; ell finite) and has inf over L of m(L^3) = 0. A theorem "S(a; b^3) < t gives a uniform gap" that uses only these hypotheses is false for every t above the value of S(a; b^3) in that model.

### 4.1 Two phases: the ceiling 1 at every shape (PROVED GIVEN the Peierls bound, RECALLED)

Model: the Ising model on the four-dimensional torus, coupling J > 0, spins on sites. Transfer matrix of a box B with V sites, in symmetric form and divided by exp(4 J V):

T(sigma, sigma') = exp(-J [D(sigma) + D(sigma') + 2 d(sigma, sigma')]),

D = the number of broken bonds of the box, d = the number of sites where sigma and sigma' differ.

- In the class (PROVED): Z is invariant under permutations of the axes; T = exp(-J D) M exp(-J D) with M the V-fold tensor power of the matrix (1, e^(-2J); e^(-2J), 1), which is positive definite; all entries of T are positive, so the top eigenvalue is simple (Perron); the state space is finite.
- S tends to 1 (PROVED): fix a >= 1 and B. As J tends to infinity, T(+,+) = T(-,-) = 1, T(+,-) = exp(-2JV) tends to 0, and every other entry is at most exp(-J) (a configuration that is not constant has D >= 1). The eigenvalues of a symmetric matrix are continuous in its entries. So lambda_0 and lambda_1 tend to 1 and all others to 0: S(a; B) tends to 1 for every a and every box.
- No gap (RECALLED, Peierls; not rebuilt here): there is J_P, independent of the box, such that for J >= J_P the model has long-range order and inf over L of m(L^3) = 0 (lambda_1/lambda_0 of the cube tends to 1).

Consequence: for every shape (a, b) and every eps > 0 there is a model in the class without a gap and with S(a; b^3) < 1 + eps. No theorem of this kind has a threshold above 1, at any shape. (In the run of 1.8, two dimensions, J = 0.7: S(3; 6) = 1.005, S(3; 11) = 1.042. GUIDE.) The gauge analogue is Z_2 at large beta with its flux sectors, S >= 7 - o(1) (RECALLED in the row-697 file); it gives a weaker ceiling.

### 4.2 A massless field: the compact Gaussian model with windings (formula PROVED; values GUIDE)

**The free massless lattice field and the zero mode.** With p-hat^2 = sum over mu of (2 - 2 cos(2 pi p_mu/n_mu)) and the zero mode removed, D(n) := product over p not 0 of (p-hat^2)^(-1/2). In direction 1, with spatial momenta k and 2 cosh(eps_k) = 2 + k-hat^2:

D(n) = (1/n_1) times the product over k not 0 of exp(-n_1 eps_k/2)/(1 - exp(-n_1 eps_k)).

(Used: the product over p_1 of (2 cosh eps - 2 cos(2 pi p_1/n_1)) = (2 sinh(n_1 eps/2))^2, and the product over p_1 not 0 of (2 - 2 cos(2 pi p_1/n_1)) = n_1^2.) The oscillator factors are traces of a positive operator with integer multiplicities. The factor 1/n_1 = the integral of exp(-n_1 E) dE over E > 0 is not: it is the free motion of the zero mode, a continuous spectrum. **So the free massless field meets the symmetry and the positivity of the spectral measure, and fails exactly: trace class, and the simple top eigenvalue (there is no atom at the top).** Lemma A (b), (LB) and Lemma K (b) need the atom. The value of its thermal sum is therefore a GUIDE and not a ceiling.

**A model in the class (PROVED).** Let R > 0 and

Z_R(n) := R (2 pi |n|)^(1/2) Theta(n) D(n),  Theta(n) := sum over w in Z^4 of exp(-2 pi^2 R^2 sum over mu of w_mu^2 |n|/n_mu^2).

(This is the Gaussian measure on real fields with phi(x + n_mu e_mu) = phi(x) + 2 pi R w_mu, summed over w, modulo global shifts by 2 pi R: the Villain model with no vortices.) Z_R is symmetric in the sides. By Poisson summation in w_1, with V = n_2 n_3 n_4: sum over w_1 of exp(-2 pi^2 R^2 w_1^2 V/n_1) = (n_1/(2 pi R^2 V))^(1/2) sum over P in Z of exp(-n_1 P^2/(2 R^2 V)). The prefactors cancel: R (2 pi n_1 V)^(1/2) (1/n_1) (n_1/(2 pi R^2 V))^(1/2) = 1. So

Z_R(n) = Tr exp(-n_1 H),  H = P^2/(2 R^2 V) + sum over mu >= 2 of 2 pi^2 R^2 w_mu^2 V/n_mu^2 + sum over k not 0 of eps_k (N_k + 1/2),

on the space with basis (P, w_2, w_3, w_4, (N_k)), every state once. exp(-H) is positive and trace class, the top eigenvalue is simple, and log Z_R >= -(|n|/2) log 16, so ell is finite. The model has no gap: m(L^3) <= 1/(2 R^2 L^3). Its thermal sum is, exactly,

1 + S(a; b^3) = theta(a/(2 R^2 b^3)) theta(2 pi^2 R^2 a b)^3 times the product over k not 0 of (1 - exp(-a eps_k))^(-1),  theta(A) := sum over P in Z of exp(-A P^2).

The two arguments A, A' of theta have the product A A' = pi^2/r^2: one cannot make both the momentum of the zero mode and the windings heavy when r is large.

**Values (GUIDE: continuum limit eps_k -> 2 pi |k|/b at fixed r, R chosen best, by hand to two digits).** inf over R of S: 0.32 at r = 1, 0.58 at r = 1.2, 0.93 at r = 1.4, 1.15 at r = 1.5, 3.1 at r = 2 (hand values, confirmed by the script of Section 5). The oscillator factor alone (a massless scalar with the zero mode dropped; not in the class) gives S about 0.013 at r = 1, 0.63 at r = 2, and log(1 + S) = 2.3 at r = 3 and 6.2 at r = 4 (script of Section 5), approaching (pi^2/90) r^3 = 0.11 r^3 from below for large r. For the photon double the exponent (12 exp(-pi) = 0.52 is its first term at r = 2, as in the row-697 file).

### 4.3 Reading

| r = b/a | proved threshold (1.5) | ceiling in the class | massless scalar, zero mode dropped (GUIDE, not in the class) |
|---|---|---|---|
| 1 | none (the lemmas need a < b) | about 0.32 (4.2, GUIDE value) | 0.013 |
| 1.4 | about 1/40000 (step (3,1,1), GUIDE fixed point) | about 0.93 (4.2) | 0.10 |
| 2 | 1/1650 | 1 (4.1) | 0.63 |
| 3 | 1/100 | 1 | 9.1 |
| 4 | 1/25 | 1 | 470 |
| 6 | 1/10 | 1 | about exp(22) |
| large | tends to 1 | 1 | exp(0.11 r^3) |

At large ratio the criterion is sharp in S and separates a massless theory from the threshold by a factor that grows like exp(0.11 r^3). The price is the volume: S(a; b^3) of a massive theory grows with b^3 too. Target 5 weighs the two.

## 5. Target 5 (GUIDE): how many correlation lengths the seed box needs

Everything in this section is GUIDE. Nothing here is used in a proof.

**Model, stated as a model.** One free scalar particle of mass m in the periodic box b^3, continuum dispersion: g(a; b^3) = - sum over k in Z^3 of log(1 - exp(-a sqrt(m^2 + (2 pi k/b)^2))). For m a large this is close to b^3 (m/(2 pi a))^(3/2) exp(-m a) (1 + 15/(8 m a)): the thermal sum is the volume times the density of one-particle states, not exp(-m a) alone. Flux states: three winding directions, energy sigma b with transverse momenta, sigma = m^2/13.7 (so m/sqrt(sigma) = 3.7, of the size reported for SU(2); the published numbers are the subject of row 706). No interaction, no lattice artefacts, one species. Scripts: /tmp/gap-seed-shape-scratch/guide.py, guide2.py on the Mac mini, run under the numeric lock at 59 to 61 percent free memory. The thresholds marked "fixed point" are fixed points of phi of Theorem SH, found by the script, not checked by hand; those of the table in 1.5 are proved.

**Two ways to count.**
- Rate filter only (what the row quotes as 8.5 and 17): s >= exp(-m a), so m a >= log(1/t) and m b >= r log(1/t). This is a lower bound for every theory.
- The model above, which also counts the states.

| shape r | threshold t | rate filter: m a, m b | model: m a, m b |
|---|---|---|---|
| 2 | 1/5041 (Theorem S as printed) | 8.5, 17.1 | 11.7, 23.4 |
| 2 | 1/3500 (step 3; proved) | 8.2, 16.3 | 11.3, 22.6 |
| 2 | 1/1650 (two stages; proved) | 7.4, 14.8 | 10.4, 20.8 |
| 1.2 | 1/192000 (fixed point) | 12.2, 14.6 | 14.1, 16.9 |
| 1.5 | 1/12600 (fixed point) | 9.4, 14.2 | 11.8, 17.6 |
| 2.2 | 1/392 (fixed point) | 6.0, 13.1 | 9.1, 20.0 |
| 2.3 | 1/249 (fixed point) | 5.5, 12.7 | 8.7, 20.0 |
| 3 | 1/100 (proved) | 4.6, 13.8 | 8.6, 25.7 |
| 4 | 1/25 (proved) | 3.2, 12.9 | 8.0, 31.9 |
| 6 | 1/10 (proved) | 2.3, 13.8 | 8.4, 50.2 |
| 24 | 3/10 (proved) | 1.2, 28.9 | 12.0, 288 (asymptotic formula; the script's momentum cut-off is too low at this ratio) |

The flux states change no entry by more than 0.1 at this sigma (the boxes are long enough that sigma a b is above 12).

**Reading.**
- The time extent: the best ratio is about 4, with m a about 8 in the model (3.2 by the rate filter), against 11.7 (8.5) now. Beyond r = 4 the gain in the threshold is eaten by the volume factor r^3.
- The space extent: in the model the smallest side is m b about 17 at r about 1.2 to 1.3 (with a longer time, m a about 13 to 14), and about 20 at r = 2 to 2.3. Against 23.4 now. If the seed is read from free energies by Phi_B, the second torus has time 2a, so the largest side of the two tori is max(2a, b): about 20 to 21 at r = 2 to 2.3, and more for r below 2. So the largest side of the tori that carry the seed goes from about 23.4 to about 20 correlation lengths, a gain of about 15 percent.
- The way the seed is read matters as much as the threshold. In the gas of Section 2, the printed criterion Phi(n) <= 1.9 x 10^(-4) of Theorem S needs m a = 14.1, m b = 28.1 in the model (it overstates the thermal sum 8 times). Phi_B with t = 1/1650 needs 11.2 and 22.4; Psi_B (three tori) needs 10.4 and 20.8. So against the printed seed inequality the side of the box falls from about 28 to about 20 to 21 correlation lengths.
- Why the gain is not larger: the thermal sum falls like exp(-m a), so a factor 3 in the threshold moves a by 1.1/m only. Of the 20 correlation lengths in space, about 13 to 15 are forced by the rate filter at these thresholds and the rest by the number of states. A threshold of order one (r large) removes the first cost and raises the second.
- So the infrared end of the open range moves down by a modest factor. This section gives no reason to expect that a criterion of this kind can hold on a box of a few correlation lengths: by 4.1 the threshold in S cannot exceed 1 at any shape, and S = 1 at r = 2 in this model is at m a = 1.3, m b = 2.7 without the flux states and at m a = 4.1, m b = 8.2 with them (script values; the model is not to be trusted at such sizes). That is a floor for any theorem of this kind at that shape, in this model.

## 6. Target 6: the test at strong coupling

Inputs: `library/gap-seed-sc.md` Theorem 1 (iii): Phi(n; beta) <= 0.16 n^4 theta^(4n) for n >= 4, theta = 12800 beta < 1 (PROVED GIVEN there; its check, row 704, is not yet in). Theorem D (b): s = S(n; (2n)^3) <= exp(Phi(n)) - 1. That file bounds only the symmetric defect Phi(n), so only the shape r = 2 can be tested.

**Theorem 4' (PROVED GIVEN `gap-seed-sc.md` Theorem 1 (iii), Theorem D (b), and the line "r = 2, two stages" of 1.5).** Let 0 < beta < 1/12800, theta = 12800 beta, and n >= 4 with n theta^n <= 0.247. Then for every integer L >= 4n, with k >= 0 the largest integer such that 2^k 4n <= L:

m(L^3) >= 4 log(1/theta) - (4 log n + log 237 + 0.85 x 2^(-k))/n.

Proof. 0.247^4 < 0.00373, so Phi(n) <= 0.16 x 0.00373 < 5.97 x 10^(-4), and s <= exp(Phi) - 1 <= 1.0004 Phi < 5.98 x 10^(-4) < 1/1650 = 6.06 x 10^(-4). By 1.5, s_1 = S(n; (4n)^3) <= 66.6 s < 1/25, and Theorem SH applies to the pair (n, 4n) with (j, p, q) = (2, 2, 3), K = 22.2, E = (2 x 4/3)^3 < 19, e E/K < 2.33, log 2.33 < 0.85. Theorem SH (ii): m(L^3) >= (1/n)[log(1/(22.2 s_1)) - 2^(-k) 0.85], and 22.2 s_1 <= 1479 s <= 1479 x 1.0004 x 0.16 n^4 theta^(4n) < 237 n^4 theta^(4n). QED

**Comparison with Theorem 4 of `gap-seed-sc.md`** (m(L^3) >= 4 log(1/theta) - (4 log n + log 1614)/n for L >= 2n, under n theta^n <= 0.18).
- The rate 4 log(1/theta) is the same. The shape of the box and the threshold do not enter the exponential rate; they enter the additive term and the range of n.
- The additive term falls from log 1614 = 7.39 to log 237 + 0.85 x 2^(-k), which is 6.32 for 4n <= L < 8n and tends to 5.47. The gain is between 1.07/n and 1.92/n.
- The range of seeds grows from n theta^n <= 0.18 to n theta^n <= 0.247.
- Numbers at theta = 1/2, by hand (log 5 < 1.61, log 237 < 5.47, 4 log 2 > 2.772): n = 5 qualifies (5/32 = 0.156). Old bound: 2.772 - (6.44 + 7.39)/5 > 0.006. New: for 20 <= L < 40, 2.772 - (6.44 + 5.47 + 0.85)/5 = 0.22; for L >= 40, at least 0.305; in the limit 0.39. At n = 40: old 2.22, new 2.26 for large L. n = 4 at theta = 1/2 has n theta^n = 0.25 and is still excluded, by a hair.
- The cost: the new bound starts at L = 4n, the old at L = 2n. For 2n <= L < 4n Theorem 4 stands.
- Against the exact leading term (Theorem 2 there: Phi(n) = 192 n^3 (beta/4)^(4n) (1 + O(beta)) for n >= 5): liminf as beta -> 0 of (m(L^3; beta) - 4 log(4/beta)) >= -(3 log n + log(192 x 1479) + 0.85 x 2^(-k))/n for L >= 4n. The recalled leading mass is 4 log(4/beta); the bound stays below it and the difference vanishes with the seed size. So Theorem SH passes the same test as Theorem S: it claims no more than the known gap.

**Not done (OPEN).** A strong-coupling bound for the shape defect Phi_B(a) = 2 F(a, b^3) - F(2a, b^3) at r > 2. With it the thresholds 1/100, 1/25, 1/10 could be tested, and by Section 2 the factor 8 of the symmetric defect would be avoided. `gap-seed-sc.md` does not contain it and I did not attempt it.

## 7. Final status

| Statement | Mark |
|---|---|
| Lemma E2 (one side enlarged, deficit read at a second time t' < b) | PROVED from Lemma A (a), Lemma K, Lemma X; not checked. A 2D Ising run found no violation (GUIDE) |
| Proposition B3 (three sides, any order, any box) | PROVED from Lemma E2 |
| Theorem SH (recursion phi for any box, step j, times pa and qa; gap on every cube of side >= max b_i, explicit L_0) | PROVED from B3 and (T) |
| Thresholds: r = 2: 1/4229 (step 2), 1/3500 (step 3), 1/1650 (two stages); r = 3: 1/100; r = 4: 1/25; r = 6: 1/10; r >= 24: 3/10; tends to 1 | PROVED (hand checks in 1.5) |
| Thresholds at other ratios (2.1 to 2.5, 5, 8, below 2) | formula PROVED, values GUIDE |
| Theorem D-shape: Phi_B = 2g(a) - g(2a), Psi_B = g(a) + g(2a) - g(3a); seed in free energies of the tori (a, B), (2a, B), (3a, B) | PROVED from (TM) |
| Order of directions immaterial; two-step enlargement never better; leading order j^(3j/p) x^j | PROVED |
| Supremum over shapes of the threshold is 1 | lower half PROVED; upper half PROVED GIVEN Peierls (RECALLED) |
| Largest threshold at a fixed ratio; any seed with t(r) < S < 1 | OPEN |
| Two directions at once | sketch, no gain found, not a proof |
| Ceiling 1 at every shape (Ising, two phases): in the class, S -> 1 | PROVED; "no gap" RECALLED (Peierls) |
| Free massless field: fails trace class and the simple top eigenvalue (zero mode), meets the rest | PROVED |
| Compact Gaussian model Z_R: in the class, no gap, exact S | PROVED; values GUIDE (below 1 only for r up to about 1.4) |
| Correlation lengths (Section 5) | GUIDE |
| Theorem 4' (strong coupling, additive term log 237 + 0.85 x 2^(-k) in place of log 1614, seeds n theta^n <= 0.247) | PROVED GIVEN `gap-seed-sc.md` Theorem 1 (iii) (unchecked), Theorem D (b), Theorem SH |
| Strong-coupling bound for Phi_B at r > 2 | OPEN, not attempted |
| (SEED) at a coupling of order one | OPEN, not attempted; no mass gap is claimed |

**For the checker (what to attack first).** (1) Lemma E2: the use of Lemma X with x = t' and y = b for the function W(x, y) = Z(x, y, c, d'), when t' > t; Lemma X as printed is for all x < y, and Lemma K (d) is used for kappa(t') >= kappa(b). (2) Proposition B3: that the time qa stays below every side of every intermediate box (the sides only grow). (3) Theorem SH (ii): the case E s_k > 1, where the stated bound is negative. (4) The arithmetic of 1.5. (5) 4.2: the cancellation of the prefactors in Z_R.

**Not verified in this run.** No second model read this file. The fixed points marked GUIDE and all of Section 5 are script or two-digit hand values. The Peierls bound and the strong-coupling inputs are taken as stated. Nothing was committed or pushed; the only files written are this one and scratch scripts under /tmp/gap-seed-shape-scratch.

RESULT: Theorem S extended to every box shape and step (Lemma E2, Proposition B3, Theorem SH, PROVED, unchecked): seed thresholds on S(a; b^3) of 1/1650 at b/a = 2 (was 1/5041), 1/100 at 3, 1/25 at 4, 1/10 at 6, tending to 1 at large ratio, with gap on every cube of side >= b; seed readable as 2F(a,b^3) - F(2a,b^3) <= log(1+t) (PROVED); ceiling 1 at every shape (two-phase Ising, given Peierls RECALLED), so the supremum over shapes is exactly 1; GUIDE: seed box about 20 correlation lengths in space (was 23.4, or 28 with the printed Phi(n)) and 8 in time at ratio 4; strong-coupling test passes with additive term log 237 in place of log 1614 (given unchecked gap-seed-sc Theorem 1). Open: best threshold at a fixed ratio, seeds with t(r) < S < 1, a strong-coupling bound for the shape defect, and (SEED) itself.
