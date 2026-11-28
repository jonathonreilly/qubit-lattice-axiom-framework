lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T22:42Z

# Check of `library/gap-seed-shape.md` (row 707)

Written by Claude Opus 5.5, high effort, on the Mac mini worker 2, at commit 43010014c. This is one line-by-line reading by one model of a file written by Claude Fable 5.2 medium (row 705). It is not an audit and not human review. Same provider family as the author, so it is not a cross-provider check. No mass gap at a coupling of order one is claimed here.

## Status

Complete for this run (2026-11-11). Every numbered statement of `library/gap-seed-shape.md` has a verdict (Section 9). No statement FAILS. Lemma E2, Proposition B3, Theorem SH (i)-(iii), Theorem D-shape and Theorem 4' HOLD. Six statements HOLD AFTER CORRECTION, and the mark of 4.1 must name its two recalled facts; none of the corrections changes a threshold, a used constant or a conclusion. The ceiling 1 (4.1, 3.5) holds given two RECALLED facts, (P1) long-range order and (P2) a vanishing tunnelling gap, not the Peierls bound alone. The independent hand test agrees: r = 3 fixed point about 1/92 (author's 1/100 valid), r = 2 two-stage cut near 1/1500 (author's 1/1650 valid).

**Read in full:** `library/gap-seed-shape.md` (whole, 325 lines); `library/gap-crux-restate.md` Sections 1, 3.1, 3.4 (lines 29-46, 86-123, 170-231, with the corrections of rows 698 and 699 printed there); `library/gap-seed-check.md` verdict table and points 5, 6; `library/gap-seed-check-astra.md` final verdict table, "Exact inputs", constants of point 7; `library/gap-seed-sc.md` Theorems 1 to 4 and their proofs (lines 34-60, 136-150, 193-227); `library/gap-seed-sc-check.md` status (every statement HOLDS, row 704). **Not covered:** the body of `gap-transfer.md` (input (TM), taken as checked in rows 671, 698, 699); the author's scripts (not in the repository, and no proof uses them); the Villain interpretation sentence of 4.2 (no proof uses it); the Peierls input of 4.1 (RECALLED by the author, not rebuilt here either).

**Repo search (rule 0a).** `grep -n "gap-seed-shape"` in FINISH.md: rows 705 (author) and 707 (this check) only. No other row checks this file. `library/open-core.md` has no line on the seed shape. Nothing here attacks an open lemma; this is a check item.

**Order of work, said plainly.** The row asks for the independent hand test before reading the author's arithmetic. The row also asks to read the file whole, and I read it whole first. So the test below is not blind. It uses a different route from the author's: it evaluates phi exactly at the threshold and locates the fixed point of phi, where the author bounds phi by u e^u.

**No numeric job was run.** Every number in this file is by hand.

## 1. Independent hand test (from the formula of Theorem SH)

**What the best threshold of one step is.** In Theorem SH, phi(x)/x^j has a power series with non-negative coefficients (phi = (e^u - 1)^(j/p), u a sum of logarithms of 1 + x^m with positive weights, lowest order x^p). So K(x_0) := sup over [0, x_0] of (phi(x)/x^j)^(1/(j-1)) equals (phi(x_0)/x_0^j)^(1/(j-1)), and the hypotheses "s <= x_0, K s < 1" can be met at s = x_0 exactly when phi(x_0) < x_0. So the step's best threshold is the smallest positive fixed point x* of phi, and any x_0 with phi(x_0) < x_0 is a valid threshold with K = (phi(x_0)/x_0^j)^(1/(j-1)).

**r = 3, (j, p, q) = (2, 1, 2).** beta = 3a/(3a - 2a) = 3, Pi = 27, C = (1/2)(27 - 1) = 13, j^3 C = 104, j/p = 2. So phi(x) = [(1+x)^8 (1+x^2)^104 - 1]^2, as in the file.
- x = 0.01: 8 log 1.01 = 0.0796026; 104 log(1.0001) = 0.0103995; sum 0.0900021; e^0.0900021 - 1 = 0.0941765; phi = 0.0088692. So K(0.01) = 88.69, and 0.01 is a valid threshold with K s <= 0.887.
- x = 0.0108: sum of logs 0.0859368 + 0.0121297 = 0.0980665; e^. - 1 = 0.1030361; phi = 0.0106164 < x.
- x = 0.011: sum 0.0875195 + 0.0125833 = 0.1001028; e^. - 1 = 0.1052845; phi = 0.0110848 > x.
- So x* is in (0.0108, 0.011), about 1/92.

Comparison: the author's threshold 1/100 with K = 98 is valid (98 >= 88.69), and the GUIDE fixed point "about 1/92" at r = 3 agrees.

**r = 2, two stages.** Stage 1 (Proposition B3 with p = q = 1, B = (2a)^3, H = (4a)^3; |H|/|B| = 8, Pi = 8): 1 + s_1 <= (1 + s)^64, s_1 = S(a; (4a)^3). Stage 2 is the step (2, 2, 3) at r = 4: beta = 4, Pi = 64, C = (2/3)(63) = 42, j^3 C = 336, j/p = 1, phi_4(x) = (1+x^2)^8 (1+x^3)^336 - 1.
- Fixed point of phi_4: x = 0.040: 8 log(1.0016) = 0.0127898, 336 log(1 + 6.4e-5) = 0.0215031, sum 0.0342929, phi_4 = 0.0348877 < x. x = 0.043: sum 0.0147785 + 0.0267143 = 0.0414928, phi_4 = 0.042365 < x. x = 0.044: sum 0.0154728 + 0.0286218 = 0.0440946, phi_4 = 0.045081 > x. So x*_4 is in (0.043, 0.044).
- K at x_0 = 0.04: phi_4(0.04)/0.04^2 = 21.80.
- Two-stage threshold of the method: s_1 < x*_4 needs 64 log(1 + s) < log(1.043) = 0.04210, so every s <= 1/1521 works; the exact cut is near 1/1500.
- At s = 1/1650: s_1 <= e^(64/1650) - 1 = e^0.0387879 - 1 = 0.039550 < 0.04, and K s_1 <= 21.80 x 0.03955 = 0.862 < 1. Also s_1 <= 64 s e^(64 s) <= 66.53 s, so K s_1 <= 21.80 x 66.53 s = 1451 s.

Comparison: the author's 1/1650 is valid and below the method's cut (about 1/1500); the author's rate constant 1479 is a valid upper bound for 1451. Agreement.

## 2. Verdicts, Section 1 of the file

Legend: HOLDS = every line re-derived here. HOLDS AFTER CORRECTION gives the text. FAILS gives the line. NOT CHECKED gives the reason.

**1.1 Setting, facts (T), (A), (K), (X). HOLDS AFTER CORRECTION (scope sentence only).** (T): S(t + t') = sum r_i^t r_i^(t') <= S(t) S(t'), and g is non-increasing since 0 <= r_i < 1 for i >= 1 (simple top). (K), (X) are quoted as checked (rows 698, 699; Lemma K (d) on b >= 3, Lemma X on 3 <= x < y, one spectator pair per use). Correction: the last sentence "so for every gauge group" must read "for every model in the abstract setting; for Wilson SU(2) the setting is Lemma 1.1 of `gap-seed-check.md`; for other groups (TM) is not checked here". The check of row 699 says the general group's transfer construction was not checked, and row 698 corrected the same kind of scope sentence in Corollary S2.

**Lemma E2. HOLDS.** Re-derived. W(x, y) = Z(x, y, c, d') with x the time and y the side in direction d; W(t, y) = Tr T_t^y with T_t the transfer operator in direction d of the box (t, c, d') (this is (TM) in direction d; the symmetry is not even needed here). Lemma A (a), h >= b: W(t, h) <= W(t, b)^(h/b). log W(t, y) = t e(y) + g_W(t, y) with e(y) = ell y + kappa(y); ell is finite (input 3 of row 699). The terms ell t h cancel exactly. Then g_W(t, h) <= (h/b)(t kappa(b) + g_W(t, b)) - t kappa(h), and -t kappa(h) <= 0 by Lemma K (b). Lemma X with x = t', y = b (3 <= t' < b, same spectator pair (c, d')) gives kappa(b) <= g_W(t', b)/(b - t'). The point named in the row: Lemma X uses Lemma K (d) only as kappa(t') >= kappa(b) for t' < b, inside Lemma X; no relation between t and t' is used anywhere, so t' > t, t' = t and t' < t are all covered. The factor h/b: it is the exponent of Lemma A (a) and multiplies the whole bracket; correct. g_W(t', b) = g(t'; B) because T_b of W is the transfer operator in the time direction of the box B. Remark (i) (t' = t gives Lemma E', since (h/b)(1 + t/(b - t)) = h/(b - t)) HOLDS; remarks (ii), (iii) HOLD.

**Proposition B3. HOLDS.** The three points of the row:
- *The time qa against the sides.* At step k Lemma E2 is used on the box B_(k-1) in direction k, whose side there is still the original b_k (sides 1 to k-1 are already h_i >= b_i; sides k+1 to 3 are b_i). The condition t' = qa < b is needed only for the side being enlarged, and that side is b_k > qa. The spectator sides need only be >= 3. So qa < min b_i is enough; the stronger reading "below every side of every intermediate box" also holds, since sides only grow. Each step uses its own ell (its own spectator pair), and only the final inequality of one step feeds the next, as in row 699.
- *The q-recursion.* t = t' = qa: g(qa; B_k) <= (h_k/b_k)(1 + qa/(b_k - qa)) g(qa; B_(k-1)) = (h_k/b_k) beta_k g(qa; B_(k-1)). Product: (B3-q).
- *The p-recursion and the product of the factors.* t = pa, t' = qa: alpha_k = pa/(b_k - qa) = (p/q)(qa/(b_k - qa)) = (p/q)(beta_k - 1). With X_k := g(pa; B_k)/prod_(i<=k)(h_i/b_i): X_k <= X_(k-1) + alpha_k beta_1 ... beta_(k-1) G_q, so X_3 <= G_p + (p/q)[(beta_1 - 1) + (beta_2 - 1) beta_1 + (beta_3 - 1) beta_1 beta_2] G_q, and the bracket telescopes to beta_1 beta_2 beta_3 - 1 = Pi - 1. (B3-p) follows.
- *The order.* The final bound depends on the beta_i only through Pi and on the h_i/b_i only through |H|/|B|, so every order gives the same bound. Correct as a statement about the bound (not about the true value).

**Theorem SH, recursion. HOLDS.** g(pa; B) <= log(1 + s^p) and g(qa; B) <= log(1 + s^q) by (T); B3 with H = jB (|H|/|B| = j^3), coefficients non-negative, gives 1 + S(pa; jB) <= (1 + s^p)^(j^3)(1 + s^q)^(j^3 C); (T) with p | j gives S(ja; jB) <= S(pa; jB)^(j/p) = phi(s) at most. Next scale: q(ja) < j min b_i, and Pi is invariant under B -> jB, a -> ja. a_k = j^k a >= 3.

**Theorem SH (i). HOLDS.** K s_(k+1) <= K^j s_k^j = (K s_k)^j while s_k <= x_0; K s_k <= (K s)^(j^k) <= K s < 1 gives s_k <= s <= x_0. Simple top: r_1^(a_k) <= s_k, so m(B_k) >= log(1/s_k)/a_k >= (j^k log(1/(Ks)) + log K)/(j^k a). Note: the hypothesis K x_0 <= 1 is not used; it is harmless.

**Theorem SH (ii). HOLDS (one line supplied for the case E s_k > 1).**
- *The constant E.* k >= 0 exists since L >= max b_i. Lemma E' (E2 with t = t' = a_k) from j^k b_i to L in each direction: a_k = j^k a < j^k b_i and L >= j^k max b_i >= j^k b_i. Exponent L/(j^k(b_i - a)) < j^(k+1) max b/(j^k(b_i - a)) = j rmax/(r_i - 1) <= j rmax/(rmin - 1). The product of the three exponents is below E, so 1 + S(a_k; L^3) <= (1 + s_k)^E.
- *Case E s_k <= 1.* (1 + s_k)^E - 1 <= e^(E s_k) - 1 <= E s_k e^(E s_k) <= e E s_k; then m(L^3) >= (1/a_k) log(1/S(a_k; L^3)) and the stated bound follows with log(1/s_k) >= j^k log(1/(Ks)) + log K.
- *Case E s_k > 1.* The file says only "the right side of the claim is negative". It is true, by this line (supplied here): (Ks)^(j^k) >= K s_k > K/E, so j^k log(1/(Ks)) < log(E/K) < log(eE/K), so log(1/(Ks)) - j^(-k) log(eE/K) < 0. And m(L^3) > 0 by the simple top. So the claim holds in both cases.

**Theorem SH (iii) and the explicit L_0. HOLDS.** For L >= L_0, k >= k_0, so j^(-k) log(eE/K) <= log(1/(Ks))/2 when log(eE/K) > 0, and <= 0 when eE <= K (k_0 = 0). The infimum: finitely many L have k < k_0 and each has m > 0; the rest have m >= log(1/(Ks))/(2a). liminf: k tends to infinity with L.

**Sufficient choice of K. HOLDS.** For x <= x_0, q >= p: u(x) <= j^3(x^p + C x^q) <= j^3 x^p (1 + C x_0^(q-p)) and u <= u_0; e^u - 1 <= u e^u; raise to j/p. The user must still check K x_0 <= 1 (unused, see (i)) and K s < 1.

**"The ratio 2 gives back Theorem S, the ratio 3 the map of the row". HOLDS.** r = 2, (2,1,1): Pi = 8, C = 7, exponent 8(1 + 7) = 64. r = 3, (2,1,1): beta = 3/2, Pi = 27/8, C = 19/8, 8(1 + 19/8) = 27. p = q = 1: j^3(1 + C) = j^3 Pi = (jr/(r-1))^3.

### 2.1 Section 1.5: the arithmetic, line by line

Every line below was redone by hand. "Strict" means: where t = 1/K, the hypothesis K s < 1 of Theorem SH needs s < t, not s <= t. The file's sentence "if s <= t (strictly below 1/K)" says this, but the two lines with t = 1/K should carry "<" in the table.

- **Table, phi column. HOLDS.** (3,1,1) at r = 2: 27 x 8 = 216, exponent j/p = 3. (2,1,2) at r = 3: 8 and 8 x 13 = 104, square. (2,2,3) at r = 4: 8 and 336, power 1. (2,2,5) at r = 6: beta = 6, Pi = 216, C = (2/5)(215) = 86, 8 x 86 = 688. (6,6,12) at r >= 24: 12a <= b/2 gives beta <= 2, Pi <= 8, C <= 7/2, 216 x 3.5 = 756. Each step has p | j and qa < b.
- **r = 2, step 2, t = 31/131072 > 1/4229. HOLDS (strict).** phi(x)/x^2 <= 4096 e^(128x). At x = t: 4096 t = 31/32 and 128 t = 31/1024 < 1/32, so 4096 t e^(128 t) < (1 - 1/32) e^(1/32) < 1. Hence phi(x) < x^2/t on [0, t], K = 1/t. 131072/31 = 4228.1, so t > 1/4229.
- **r = 2, step 3, 1/3500, K = 3500. HOLDS (strict).** 648/3500 = 0.1851429 < 0.18515. e^0.18515: terms 1, 0.18515, 0.0171403, 0.0010578, 0.0000490, 0.0000018, sum 1.2033989 < 1.2034. 216^3 = 10077696. 10077696 x 1.2034 = 12127499.4 < 12127500 < 12250000 = 3500^2. So phi(x) <= K^2 x^3 on [0, 1/3500]. This margin is thin (0.6 in 1.2 x 10^7) but correct.
- **r = 2, two stages, 1/1650, K = 22.2, rate log(1/(1479 s))/a. HOLDS.** 64/1650 = 0.0387879 <= 0.03879. e^0.03879 = 1.0395522 < 1.0396. s_1 <= e^(64 s) - 1 <= 0.0396 < 0.04. s_1 <= 64 s e^(64 s) <= 66.534 s <= 66.6 s. K s_1 <= 22.2 x 0.0396 = 0.879 < 1, so the line r = 4 applies to (a, (4a)^3) (qa = 3a < 4a, a >= 3). 22.2 x 66.6 = 1478.5 <= 1479. Sides reached by (i): 2^k (4a) = 2^(k+1) b. My independent value (Section 1): method cut near 1/1500, constant 1451.
- **r = 3, 1/100, K = 98. HOLDS.** u <= 8x + 104x^2 <= 9.04x <= 0.0904 for x <= 0.01. e^0.0904 = 1.094612 < 1.0947. 9.04 x 1.0947 = 9.8961. 9.8961^2 = 97.93 <= 97.94 <= 98. K x_0 = 0.98. My exact value: K(0.01) = 88.69.
- **r = 4, 1/25, K = 22.2. HOLDS.** u <= x^2(8 + 336 x) <= 21.44 x^2 <= 0.034304. e^0.034304 = 1.0348989 < 1.0349. 21.44 x 1.0349 = 22.188 <= 22.19. The three written steps: (2 G_2 + 4 G_3) -> (4 G_2 + 8 G_3 + 32 G_3) -> (8 G_2 + 80 G_3 + 256 G_3) = 8 G_2 + 336 G_3; the file's 16 + 64 + 256 = 336 is the same sum. My exact value: K(0.04) = 21.80.
- **r = 6, 1/10, K = 9.48. HOLDS.** u <= x^2(8 + 688 x^3) <= 8.688 x^2 <= 0.08688. e^0.08688 = 1.090766 < 1.0908. 8.688 x 1.0908 = 9.4769 <= 9.477 <= 9.48. K x_0 = 0.948.
- **r >= 24, 3/10, K = 3.03. HOLDS AFTER CORRECTION (one rounded product; K unaffected).** x^6 <= 0.3^6 = 0.000729, 1 + 3.5 x 0.000729 = 1.0025515. u <= 216 x 0.000729 x 1.0026 = 0.157873 < 0.1579. e^0.1579 = 1.171049 < 1.1711. With the rounded factors as printed, 216 x 1.0026 x 1.1711 = 253.62, which is above the printed "253.6". With the unrounded factors, 216 x 1.0025515 x 1.171049 = 253.59 <= 253.6. Corrected text: "phi <= 253.62 x^6". Since 3.03^5 = 255.40 > 253.62, K = 3.03 stands, and K x_0 = 0.909.
- **Threshold tends to 1. HOLDS.** For x <= t < 1: x^j <= 1, so u <= 4.5 j^3 x^j <= 4.5 j^3 t^j, and phi <= u e^u <= 4.5 j^3 e^(4.5 j^3 t^j) x^j. With K^(j-1) equal to that factor, K t < 1 iff 4.5 j^3 e^(4.5 j^3 t^j) t^(j-1) < 1, true for large j since j^3 t^(j-1) -> 0. r_0 = 4j makes 2ja <= b/2.
- **Sentence "So at the shape of Theorem S the seed threshold is raised from 1/5041 to 1/1650 ... 1/100, 1/25, 1/10". HOLDS.** The file's own caveat (these are thresholds on S at a larger box) is right.
- **Other ratios (2.1 to 2.5, 5, 8). Labelled GUIDE; no proof uses them. HOLDS as labelled.** One spot test at r = 2.2, step (2,1,2): beta = 11, exponent 4(11^3 - 1) = 5320. At x = 0.0023: logs 0.018379 + 0.028143 = 0.046522, phi = 0.047621^2 = 0.0022677 < x; at x = 1/430: phi = 0.0023517 > x. So the fixed point is about 1/433, which agrees with "about 1/430". But the table of Section 5 gives "1/392 (fixed point)" at r = 2.2, and at x = 1/392 this phi is 0.0031973 > x. The two GUIDE values disagree, unless Section 5 used another step; the file does not say which. GUIDE only, no proof affected. Also, 1.5 says these fixed points were "computed by hand" and Section 5 says "found by the script, not checked by hand". One of the two provenance sentences is wrong.

**1.6 Boxes with three different sides, example (2n, 4n, 4n). HOLDS.** Pi = 2 x (4/3)^2 = 32/9, 8 Pi = 256/9 = 28.44 < 28.5. phi(x)/x^2 <= 812.25 e^(57x); 57/880 = 0.064773 < 0.0648; e^0.0648 = 1.066946; 812.25 x 1.066946/880 = 0.98481 < 0.985. So K(1/880) < 0.985 x 880 and K/880 < 1: threshold at least 1/880. (ii) reaches every cube L >= 4n. The "Not treated" sentence is an unproved remark and is labelled as not stated.

**1.7 What stays open. HOLDS.** For b <= 2a, q >= 2 needs qa < b <= 2a, impossible, so only p = q = 1. The sentence "the exponent (j r/(r-1))^3 is all there is" is a statement about the moves of this file with times that are multiples of a; read so, it holds. For r <= 1, Lemma X needs a < b.

**1.8 The run. GUIDE; HOLDS as labelled.** No proof uses it. Not re-run.

## 3. Verdicts, Section 2 of the file (free-energy form)

**Theorem D-shape (a) to (f). HOLDS.** log Z(t, B) = t e(B) + g(t; B) for every t >= 3 (definition of S with the top eigenvalue of the box B).
- (a) 2(a e + g(a)) - (2a e + g(2a)) = 2 g(a) - g(2a). g(2a) <= g(a) gives Phi_B >= g(a); g(2a) >= 0 gives Phi_B <= 2 g(a). Exponentiate: S(a; B) <= exp(Phi_B) - 1 <= (1 + S)^2 - 1.
- (b) (a + 2a - 3a) e cancels; Psi_B = g(a) + g(2a) - g(3a) >= g(a) since g(2a) >= g(3a); Psi_B <= g(a) + g(2a) <= g(a) + log(1 + S(a)^2) by (T).
- (c) F(a, B) - (a/k)[F(k+l, B) - F(l, B)] = a e + g(a) - (a/k)[k e + g(k+l) - g(l)] = g(a) + (a/k)[g(l) - g(k+l)]. The bracket is >= 0 (g non-increasing) and <= g(l) = log(1 + S(l; B)).
- (d) dF(n)/dbeta = -6|n| abar_n (6|n| plaquettes; Haar normalised, F = 0 at beta = 0). d Phi_B/d beta = -12 a|B| abar_(a,B) + 12 a|B| abar_(2a,B). Same pattern as Theorem D (f): 16 x 6 n^4 = 96 n^4.
- (e) Phi_B >= g(a) >= log(1 + r_1^a) = log(1 + exp(-a m(B))).
- (f) F(2n, (2n)^3) = F((2n)^4), so Phi(n) - Phi_B(n) = 16 F(n^4) - 2 F(n, (2n)^3) = 2[8 F(n^4) - F(n, 2n, 2n, 2n)] >= 0 by Lemma A (a) in three directions.

**"The seed in free energies". HOLDS AFTER CORRECTION (one phrase).** The two sufficient conditions are right: Phi_B <= log(1 + t) or Psi_B <= log(1 + t) gives S(a; b^3) <= t. Correction: "this loses at most the factor 1 + t(r) against the true thermal sum" must read "at most the factor 1 + t(r) + t(r)^2". Reason: exp(Psi_B) - 1 <= (1 + S)(1 + S^2) - 1 = S(1 + S + S^2). Also, for the two lines of 1.5 with t = 1/K (31/131072 and 1/3500 at r = 2), the conclusion needs S < t, so "<= log(1 + t)" must be "< log(1 + t)" there. At r = 2 this changes nothing in practice, since the line 1/1650 covers every S <= 1/1650.

**Numbers. HOLDS.** log(1 + 1/1650) >= 6.0606 x 10^(-4) - 1.84 x 10^(-7) = 6.0588 x 10^(-4) > 6.05 x 10^(-4). log 1.01 = 0.009950 > 0.0099. log 1.04 = 0.039221 > 0.0392. log 1.1 = 0.095310 > 0.0953. "Phi_B(n) <= Phi(n)" is (f).

**"How much each form loses". Labelled GUIDE; no proof uses it. HOLDS as labelled.**

## 4. Verdicts, Section 3 of the file (the limit of the method)

**3.1 Order of directions. HOLDS** (Proposition B3, as a statement about the bound).

**3.2 Two-step against one-step enlargement. HOLDS, read as stated: a comparison of bounds.** Let the first step from b to h' use the pair (t, t'). The two-step bound is (h/h')[bound for g(t; h') + (t/(h' - t'')) x (bound for g(t''; h'))] for whatever second time t'' < h' is used. The second term is >= 0 whatever t'' is, and the bound for g(t; h') is (h'/b)[g(t; b) + (t/(b - t')) g(t'; b)]. So the two-step bound is at least the one-step bound with the first step's pair (t, t'). This also covers a second time t'' >= b, which a reader might think could help. It does not conflict with the two-stage gain at r = 2 (1/1650 against 1/3500): that gain comes from changing the times of the recursion (p = 2, q = 3 at r = 4), not from enlarging one side at a fixed time in two steps.

**3.3 Leading order. HOLDS.** q > p: u = j^3 x^p + O(x^(2p)) + O(x^q), so phi = (j^3 x^p)^(j/p)(1 + O(x^min(p, q-p))) = j^(3j/p) x^j (1 + ...). q = p: 1 + C = Pi, phi = (j^3 Pi)^(j/p) x^j (1 + O(x^p)). Leading threshold j^(-3j/(p(j-1))); p = j gives j^(-3/(j-1)): 1/8, 0.192, 0.250, 0.299, 0.341 for j = 2 to 6, tending to 1. The constraint p = j < q < r is qa < b. The formula for C at a cube is right.

**3.4 What a better use gave. HOLDS** for the PROVED items (r = 3: 1/100; r = 4: 1/25; r = 6: 1/10; r = 2: 1/3500 and 1/1650). "About 1/729" at r = 3 for the map of the row is the leading order (729 = 27^2); its fixed point is somewhat lower: phi(x) = 729 x^2 (1 + 26 x + O(x^2)), so x* is about (1/729)(1 - 26/729), about 1/756 (my estimate; the file makes no claim on it). The leading-order list at r = 2 with p = q = 1, (2j)^(-3j/(j-1)): 4^6 = 4096, 6^4.5 = 3174.5, 8^4 = 4096, 10^3.75 = 5623; HOLDS. The other first stages are labelled GUIDE. The two-direction convexity item is labelled a sketch and no proof uses it.

**3.5 The supremum over shapes is 1. Lower half HOLDS; upper half HOLDS GIVEN the recalled input of 4.1, which I name more exactly there.** Lower half: the last check of 1.5. Upper half: in the Ising model of 4.1, S(a; b^3) -> 1 as J -> infinity at every shape, so a theorem "S < t gives a uniform gap" with t > 1 would need a gap in a model that (by the recalled input) has none.

**3.6 OPEN items. HOLDS as an honest statement.** The parenthetical "4.2 gives one below 1 only for r up to about 1.4, GUIDE" is labelled.

## 5. Verdicts, Section 4 of the file (ceilings)

**Definition of the class. HOLDS** as the list of hypotheses of Lemmas A, K, X, E2 and Theorem SH: a symmetric family Z; in each direction Z = Tr T^(n_mu) with T positive, trace class, depending only on the other sides, eigenvalues counted with integer multiplicity; simple top; ell finite for each spectator pair. (Row 699's "exact inputs" 1 to 4 are the same list.)

**4.1 The Ising model at large J.** Hypothesis by hypothesis:
- *Symmetry under permutations of the axes.* The isotropic nearest-neighbour Ising weight on the 4-torus is invariant under permuting coordinates. The normalisation exp(-4J|n|) is symmetric. HOLDS.
- *Transfer matrix.* In a box B with V sites, the spatial bonds of one slice number 3V and contribute J(3V - 2D); the time bonds between two slices number V and contribute J(V - 2d). Splitting the spatial part half to each slice gives T(sigma, sigma') = exp(4JV) exp(-J[D + D' + 2d]). HOLDS (each side >= 3, so the bonds are distinct).
- *Positive, trace class.* T = e^(-JD) M e^(-JD) with M the V-fold tensor power of (1, e^(-2J); e^(-2J), 1), eigenvalues 1 +- e^(-2J) > 0, so M and T are positive definite. Finite state space. HOLDS.
- *Simple top.* All entries > 0; Perron-Frobenius. HOLDS.
- *ell finite.* Not argued in the file beyond the list. Supplied: with the normalisation, Z = sum over configurations of exp(-2J (number of broken bonds)), so 1 <= Z <= 2^|n|; hence 0 <= log W(a, b)/(ab) <= cd log 2. HOLDS.
- *S -> 1 as J -> infinity at fixed a >= 1 and B.* T(+,+) = T(-,-) = 1, T(+,-) = e^(-2JV); a non-constant sigma has D >= 1 (the box graph is connected), so the other entries are <= e^(-J). Eigenvalues of a symmetric matrix are continuous in the entries (Weyl), the limit matrix has eigenvalues 1, 1, 0, ..., 0, so lambda_1/lambda_0 -> 1, the others -> 0, and S -> 1. HOLDS.
- *No gap for J >= J_P.* RECALLED by the author; not rebuilt there or here. What is recalled is more than the Peierls bound: it is (P1) long-range order at large J, uniform in the torus, and (P2) that it forces lambda_1/lambda_0 of the cube L^3 to tend to 1 (the tunnelling splitting of the two phases). (P2) does not follow from (P1) by the lemmas of this file: the obvious route bounds a two-point function by the gap only after a bound on the number of states, which is not available. Correction: the mark "PROVED GIVEN the Peierls bound" should read "PROVED GIVEN (P1) and (P2), both RECALLED".
- *Consequence "no threshold above 1 at any shape". HOLDS GIVEN (P1), (P2).* The GUIDE run values and the Z_2 remark are labelled.

**4.2 The free massless field. HOLDS.** prod over p_1 = 0..n_1-1 of (2 cosh eps - 2 cos(2 pi p_1/n_1)) = 2 cosh(n_1 eps) - 2 = (2 sinh(n_1 eps/2))^2, and prod over p_1 = 1..n_1-1 of (2 - 2 cos(2 pi p_1/n_1)) = n_1^2 (standard; both follow from z^n - 1 = prod(z - w^p)). So D(n) = (1/n_1) prod over k != 0 of 1/(2 sinh(n_1 eps_k/2)) = (1/n_1) prod e^(-n_1 eps_k/2)/(1 - e^(-n_1 eps_k)). The factor 1/n_1 is not Tr T^(n_1) for any positive trace-class T (that would decay like m_0 lambda_0^(n_1) or be at least m_0 >= 1 when lambda_0 = 1; 1/n_1 does neither). So the field fails the class exactly at trace class with a top atom. Its S values are GUIDE. HOLDS.

**4.2 The compact Gaussian model Z_R.** Hypothesis by hypothesis:
- *Symmetry.* |n|, Theta (permute the w_mu with the sides) and D are symmetric. HOLDS.
- *The cancellation of the prefactor.* Poisson: sum over w of exp(-pi A w^2) = A^(-1/2) sum over P of exp(-pi P^2/A), with pi A = 2 pi^2 R^2 V/n_1, A = 2 pi R^2 V/n_1. So the w_1 sum is (n_1/(2 pi R^2 V))^(1/2) sum_P exp(-n_1 P^2/(2 R^2 V)). Prefactor: R (2 pi n_1 V)^(1/2) x (1/n_1) x (n_1/(2 pi R^2 V))^(1/2) = R x R^(-1) x (2 pi)^0 x V^0 x n_1^(1/2 - 1 + 1/2) = 1. HOLDS.
- *Trace form.* |n|/n_mu^2 = n_1 V/n_mu^2 for mu >= 2, so each winding factor is exp(-n_1 x 2 pi^2 R^2 w_mu^2 V/n_mu^2). With the oscillator traces, Z_R = Tr exp(-n_1 H) with H as printed, on the basis (P, w_2, w_3, w_4, (N_k)), each state once; H depends only on the other three sides. HOLDS.
- *Positive, trace class, simple top.* All three sums converge (Gaussian in P and w; finitely many k with eps_k > 0); the minimum of H is at P = 0, w = 0, N = 0 only. HOLDS.
- *ell finite.* HOLDS AFTER CORRECTION. The printed bound log Z_R >= -(|n|/2) log 16 needs Theta >= 1, D >= 16^(-(|n|-1)/2) (each p-hat^2 <= 16) and 4R(2 pi |n|)^(1/2) >= 1, so it holds for R >= 1/(4 (2 pi |n|)^(1/2)) and can fail for very small R. Corrected text: "log Z_R >= log(4R (2 pi |n|)^(1/2)) - (|n|/2) log 16, so log W(a, b)/(ab) >= -(cd/2) log 16 - |log(4R (2 pi 81)^(1/2))|/9 and ell is finite for every R > 0". ell <= log W(3, 3)/9 < infinity.
- *No gap.* The states P = +-1 lie 1/(2 R^2 L^3) above the ground state, so m(L^3) <= 1/(2 R^2 L^3) -> 0. HOLDS.
- *Exact thermal sum.* Normalise by e^(-a E_0), E_0 = sum eps_k/2: theta(a/(2R^2 b^3)) from P; theta(a x 2 pi^2 R^2 b^3/b^2) = theta(2 pi^2 R^2 a b) for each of the three windings; (1 - e^(-a eps_k))^(-1) per oscillator. HOLDS. The product of the two arguments: (a/(2R^2 b^3))(2 pi^2 R^2 a b) = pi^2 a^2/b^2 = pi^2/r^2. HOLDS.
- *Values.* Labelled GUIDE (continuum dispersion, best R). Not checked. The large-r law log(1 + S) -> (pi^2/90) r^3 for the oscillator part: (r^3/(2 pi^2)) x 2 zeta(4) = pi^2 r^3/90; HOLDS as a limit, GUIDE as used.
- *The Villain reading.* No proof uses it. NOT CHECKED.

**4.3 Reading table. HOLDS as labelled:** the entry 1 at r >= 2 is "given (P1), (P2)"; the other ceiling entries are GUIDE values. Small GUIDE mismatch: Section 4.2 says log(1 + S) = 2.3 at r = 3, which gives S = 9.0, and the table says 9.1; no proof uses either.

## 6. Verdict, Section 5 of the file (GUIDE)

**Labelled and unused. HOLDS.** The section opens "Everything in this section is GUIDE. Nothing here is used in a proof." A search of the file for "Section 5" and "Target 5" finds only the status table, the cross-references in 1.5 and 4.3, and Section 7, none inside a proof. Theorem 4' uses 1.5, not Section 5. The numbers were not checked, per the row. One inconsistency noted in 2.1 above: r = 2.2 is "about 1/430" in 1.5 and "1/392 (fixed point)" here.

## 7. Verdicts, Section 6 of the file (strong coupling)

Inputs, each checked against its source:
- `gap-seed-sc.md` Theorem 1 (iii), line 37: |Phi(n; beta)| <= 0.16 n^4 (12800 |beta|)^e(n), and e(n) = 4n for n >= 4 (Theorem 1 (ii)). Row 704 checked it: HOLDS. The file's Section 6 says so; its Section 7 table still says "(unchecked)", which is out of date.
- Theorem D (b) of `gap-crux-restate.md`: s = S(n; (2n)^3) <= exp(Phi(n)) - 1. Checked in rows 698, 699.
- The line "r = 2, two stages" of 1.5 and Theorem SH (ii): checked above.

**Theorem 4'. HOLDS.**
- 0.247^2 = 0.061009, 0.061009^2 = 0.0037221 < 0.00373. Phi(n) <= 0.16 (n theta^n)^4 <= 0.16 x 0.00373 = 5.968 x 10^(-4) < 5.97 x 10^(-4).
- The constant 1.0004: the file writes s <= exp(Phi) - 1 <= 1.0004 Phi. Phi e^Phi would give only 1.0006 here, so the step needs (e^x - 1)/x = 1 + x/2 + x^2/6 + ... <= 1 + x/2 + x^2/2 <= 1.0003 for x <= 6 x 10^(-4). With that, 1.0004 holds. So s < 1.0004 x 5.97 x 10^(-4) = 5.9724 x 10^(-4) < 5.98 x 10^(-4) < 1/1650 = 6.0606 x 10^(-4).
- n >= 4 >= 3, so a = n is admissible; B = (4n)^3, (j, p, q) = (2, 2, 3), qa = 3n < 4n.
- E = (2 x 4/(4 - 1))^3 = 512/27 = 18.963 < 19. eE/K = 2.71828 x 18.963/22.2 = 2.3219 < 2.33. log 2.33 = 0.8459 < 0.85.
- The constant 237: 22.2 s_1 <= 1479 s <= 1479 x 1.0004 x 0.16 n^4 theta^(4n) = 236.73 n^4 theta^(4n) < 237 n^4 theta^(4n). Then (1/n) log(1/(22.2 s_1)) >= 4 log(1/theta) - (4 log n + log 237)/n, and the term 2^(-k) x 0.85/n is from Theorem SH (ii).
- The constant 0.85 is log(eE/K), checked above.
- *The range L >= 4n.* Theorem SH (ii) needs L >= max b_i = 4n, and k is the largest with 2^k 4n <= L. HOLDS. For 2n <= L < 4n only Theorem 4 of `gap-seed-sc.md` applies, as the file says.

**Comparison with Theorem 4. HOLDS.** Theorem 4 as quoted matches `gap-seed-sc.md` line 57-59 (n theta^n <= 0.18, L >= 2n, log 1614). Numbers at theta = 1/2: 4 log 2 = 2.7726 > 2.772; 4 log 5 = 6.4378 < 6.44; log 1614 = 7.3865 < 7.39; log 237 = 5.4681 < 5.47. n = 5: 5/32 = 0.156 <= 0.247. Old bound: 2.772 - 13.83/5 = 0.006. New: 2.772 - 12.76/5 = 0.220 (k = 0); 2.772 - 12.335/5 = 0.305 (k >= 1, since 0.85/2 = 0.425); limit 2.772 - 11.91/5 = 0.390. n = 40: 4 log 40 = 14.7555; old 2.7726 - 22.142/40 = 2.219; new limit 2.7726 - 20.224/40 = 2.267. n = 4: 4/16 = 0.25 > 0.247. Gain 7.39 - 6.32 = 1.07 and 7.39 - 5.47 = 1.92. All HOLD.

**The last bullet (liminf against 4 log(4/beta)). HOLDS, with one input not named in the theorem's list.** It uses Theorem 2 of `gap-seed-sc.md` (Phi(n) = 192 n^3 (beta/4)^(4n)(1 + O(beta)) for n >= 5; checked in row 704), not only Theorem 1 (iii). As beta -> 0, Phi -> 0, so the factor 1.0004 can be dropped in the limit, and 1479 is still an upper bound for 22.2 x 64 (1 + o(1)) = 1420.8 (1 + o(1)). So the liminf bound with log(192 x 1479) holds for n >= 5. The leading mass 4 log(4/beta) is RECALLED, and the file says so. Correction: add "and Theorem 2 of `gap-seed-sc.md`, for n >= 5" to the inputs of that bullet.

**"Not done (OPEN)". HOLDS as an honest statement.**

## 8. Verdict, Section 7 of the file (final status table)

**HOLDS AFTER CORRECTION.** Every mark matches the verdicts above, except: (1) Theorem 4' row: "Theorem 1 (iii) (unchecked)" should read "(checked, row 704)"; (2) the Peierls row: "RECALLED (Peierls)" should name both (P1) long-range order and (P2) the vanishing tunnelling gap; (3) "Thresholds ... r = 2: 1/4229 (step 2), 1/3500 (step 3)" should say "s < t" for those two; (4) "Compact Gaussian model Z_R: in the class" holds for every R > 0 after the corrected bound on ell. The "For the checker" list: point (1) HOLDS (Lemma E2), (2) HOLDS (B3), (3) HOLDS with the supplied line (SH (ii)), (4) HOLDS with the one rounding correction (r >= 24), (5) HOLDS (Z_R prefactor).

The file's RESULT line: consistent with the verdicts, except "given unchecked gap-seed-sc Theorem 1" is out of date (now checked, row 704), and "given Peierls" should read "given (P1), (P2), both RECALLED".

## 9. Verdict table

| Statement of `gap-seed-shape.md` | Verdict |
|---|---|
| 1.1 setting, (T), (A), (K), (X) | HOLDS AFTER CORRECTION: "for every gauge group" -> "for every model in the abstract setting; Wilson SU(2) by Lemma 1.1 of `gap-seed-check.md`" |
| Lemma E2 (with x = t', y = b, any t; Lemma K (d) inside Lemma X; factor h/b) | HOLDS |
| Proposition B3 (qa below the enlarged side; the order; the product of b_i/(b_i - qa)) | HOLDS |
| Theorem SH: recursion, phi, the induction on j^k B | HOLDS |
| Theorem SH (i) | HOLDS (K x_0 <= 1 unused) |
| Theorem SH (ii): the constant E; the case E s_k > 1 | HOLDS; the line for E s_k > 1 is supplied in Section 2 above |
| Theorem SH (iii), explicit L_0, sufficient choice of K | HOLDS |
| Ratios 2 and 3 as special cases | HOLDS |
| 1.5: 31/131072 > 1/4229 (r = 2, step 2) | HOLDS, with s < t strict |
| 1.5: 1/3500, K = 3500 (r = 2, step 3) | HOLDS, with s < t strict |
| 1.5: 1/1650, price (1+s)^64, rate log(1/(1479 s))/a | HOLDS (independent value: cut near 1/1500, constant 1451) |
| 1.5: 1/100, K = 98 (r = 3) | HOLDS (independent value: K(0.01) = 88.69, fixed point about 1/92) |
| 1.5: 1/25, K = 22.2 (r = 4) | HOLDS (exact K(0.04) = 21.80) |
| 1.5: 1/10, K = 9.48 (r = 6) | HOLDS |
| 1.5: 3/10, K = 3.03 (r >= 24) | HOLDS AFTER CORRECTION: "253.6 x^6" -> "253.62 x^6"; K unaffected (3.03^5 = 255.4) |
| 1.5: threshold tends to 1 | HOLDS |
| 1.5: other ratios | GUIDE, labelled, unused; r = 2.2 value differs from Section 5 (1/430 against 1/392; 1/430 is right for step (2,1,2)) |
| 1.6: example (2n, 4n, 4n), threshold 1/880 | HOLDS |
| 1.7 | HOLDS |
| 1.8 run | GUIDE, labelled, unused |
| Theorem D-shape (a) to (f) | HOLDS |
| Seed in free energies | HOLDS AFTER CORRECTION: factor 1 + t + t^2, not 1 + t; strict inequality on the two lines with t = 1/K |
| Section 2 numbers | HOLDS |
| 3.1, 3.2, 3.3, 3.4 (PROVED items) | HOLDS (3.2 as a comparison of bounds, which also covers a second time above b) |
| 3.5 supremum 1 | lower half HOLDS; upper half HOLDS GIVEN (P1), (P2), both RECALLED |
| 3.6 | honest OPEN statement |
| 4.1 Ising in the class | HOLDS, every hypothesis (ell finite supplied: 1 <= Z <= 2^|n| after normalisation) |
| 4.1 S -> 1 | HOLDS |
| 4.1 no gap | RECALLED: (P1) long-range order and (P2) tunnelling gap -> 0; mark should name both |
| 4.2 free massless field outside the class | HOLDS |
| 4.2 Z_R in the class: symmetry, prefactor cancellation, trace form, simple top | HOLDS |
| 4.2 Z_R: ell finite | HOLDS AFTER CORRECTION: printed lower bound needs R >= 1/(4 (2 pi |n|)^(1/2)); ell finite for every R > 0 with the corrected bound |
| 4.2 exact thermal sum, A A' = pi^2/r^2 | HOLDS |
| 4.2 m(L^3) <= 1/(2 R^2 L^3) | HOLDS |
| 4.2 values; Villain reading | GUIDE / NOT CHECKED (no proof uses them) |
| 4.3 | HOLDS as labelled |
| Section 5 | GUIDE, labelled, unused |
| Theorem 4' (237, 0.85, 0.247, L >= 4n) | HOLDS (1.0004 needs (e^x - 1)/x <= 1 + x/2 + x^2/2, not x e^x) |
| Comparison with Theorem 4, numbers at theta = 1/2 | HOLDS |
| Liminf bullet | HOLDS AFTER CORRECTION: add Theorem 2 of `gap-seed-sc.md` (n >= 5) to its inputs |
| Section 7 table, RESULT line | HOLDS AFTER CORRECTION: Theorem 1 (iii) is now checked (row 704); name (P1), (P2) |

**No statement FAILS.** No correction changes a threshold, a constant that a proof uses, or a conclusion of Theorem SH, Theorem D-shape or Theorem 4'.

**Defects, ranked by what each breaks (none breaks a consumer).**
1. 4.1 / 3.5: the ceiling 1 rests on two RECALLED facts, (P1) and (P2), not on "the Peierls bound" alone. Any consumer of "the supremum over shapes is exactly 1" reads a conditional upper half.
2. 1.1: scope "every gauge group" is not proved; only Wilson SU(2) has the setting (Lemma 1.1).
3. Theorem SH (ii): the case E s_k > 1 was asserted without its one-line proof (supplied here).
4. 1.5 and Section 2: the two r = 2 lines with t = 1/K need s < t.
5. Section 2: the loss factor is 1 + t + t^2.
6. 4.2: the printed lower bound for log Z_R fails for very small R; ell is finite anyway.
7. 1.5, r >= 24: one rounded product, 253.62 not 253.6.
8. Section 6 last bullet: Theorem 2 of `gap-seed-sc.md` is an unnamed input.
9. GUIDE consistency: r = 2.2 is 1/430 in 1.5 and 1/392 in Section 5; provenance "by hand" against "by the script".
10. Section 7 and RESULT: "unchecked" for `gap-seed-sc.md` Theorem 1 is out of date.

**What this check does not show.** It does not check (TM) itself, the Peierls facts, the GUIDE numbers, the scripts, or the Villain reading. It is one reading by one model of the same provider as the author. It proves no mass gap and says nothing about (SEED) at a coupling of order one.
