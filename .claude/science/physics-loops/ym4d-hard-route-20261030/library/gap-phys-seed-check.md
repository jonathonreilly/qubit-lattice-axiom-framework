lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-12T02:34Z

# Check of `library/gap-phys-seed.md` (row 727)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, commit 258009092. This is one line-by-line reading by a model that did not write the file (author: Claude Fable 5.2 max, row 720). It is not an audit and not human review.

## Status

Started 2026-11-11T14:34Z. Read whole: `gap-phys-seed.md` (455 lines); `gap-crux-restate.md` Sections 1, 3.1, 3.2, 3.4; `gap-seed-shape.md` lead note, 1.1 to 1.6; `gap-mid-max.md` lead note of row 709 and Section 4.3. Verdicts below are written one section at a time.

**Not covered by this check.** The proofs of the inputs (Lemma A, Lemma K, Lemma X, Lemma E', Theorem S, Corollary S3', Theorem SH, Proposition Delta) are taken as checked in rows 698, 699, 707, 709; I re-read their statements and the lines used, not their proofs. Sections 1.1.1 to 1.1.4, 1.2, 1.4, 2.2, 2.3, 3.3 and 4 are outside the item (RECALLED and GUIDE text) and get no verdict. The Ising runs were not re-run. No numeric job was run.

## 1. Section 1.1.5 and Proposition 1.1

**1.1.5 (i), upper side.** HOLDS. F(n)/abs(n) is non-increasing in each side for every integer side, not only multiples: for a positive trace-class operator, (Tr S^k)^(1/k) is non-increasing over all integers k >= 1 (Lemma A (a)). So F(n') <= (abs(n')/n^4) F(n^4) for every n' with sides at least n, and (UV-Z) gives the stated bound. "Multiples of l/a" is more than needed.

**1.1.5 (ii), lower side.** HOLDS ((LB)).

**1.1.5 (iii), the count of states.** HOLDS as a conditional. Check of the steps: f (lattice units) times n^4 equals f_phys l^4; f = inf over tori of F/abs(n) equals the limit along cubes, because every torus is dominated by a cube with a larger side (monotony in each side); the lower half of (UV-Z) on the allowed sides l' -> infinity then gives f_phys >= v(l) - delta - C_-; so Delta(n^4) <= (C_+ + C_- + delta) l^4, and Proposition Delta gives the bound for g. Two inputs are assumptions of the file and stay unchecked here: (a) that the vacuum number V_(a,l) of (ST5) is the vacuum energy E_m of CA-II 141374-141386, with the same normalization of Z; (b) that delta_vac-bar is uniform in the cutoff. The file states (a) as "assume"; (b) is not stated. Correction (wording): add (b) to the assumption.

**Proposition 1.1.** HOLDS AFTER CORRECTION. It is a statement about the size of the error terms, not a theorem about what (UV-Z) cannot imply. What is proved: (a) the bound S(n; b^3) <= exp((b/n)^3 C l^4) - 1, given (UV-Z), Proposition Delta and the density assumption of (iii); (b) this bound is above every threshold of Theorem SH as soon as C l^4 >= log 2, since (b/n)^3 >= 1 and every proved threshold is below 1. Not proved: "the only bound for a thermal sum that follows from (UV-Z) by the lemmas above", and "C_+ and C_- are of order one by their construction". The first is a description of the lemmas at hand; the second is a reading of CA-I 157033, not a lower bound on C_+ + C_-. A theorem form would need a model of the class that satisfies (UV-Z) with the same V and C and violates the seed; the file gives none. Text to use: "Proposition 1.1 (PROVED as a comparison of sizes). Under (UV-Z) and the assumption of (iii), the lemmas of this target give S(n; b^3) <= exp((b/n)^3 C l^4) - 1; this exceeds every threshold t(r) when C l^4 >= log 2. That no other argument from (UV-Z) gives the seed is not proved."

One numeric slip: "log(1 + t(r)) <= log(1.1) < 0.1" is false for the lines r >= 24 (t = 3/10, log 1.3 = 0.262) and for the lines r >= 4j (t tends to 1). Replace by "log(1 + t(r)) < log 2". The conclusion does not change. The bound l^4 >= 16 L^44 needs M R >= 1 in l_*(g) = 2 L^11 M R(.); true for the account's constants, stated here for completeness.

## 2. Section 1.3

**P1 for every shape.** HOLDS. If S(a; b^3) <= t, then exp(-a m) = r_1^a <= S <= t, so a m >= log(1/t) and b m >= r log(1/t). Table re-computed: 2 x 7.4085 = 14.82; 3 x 4.6052 = 13.82; 4 x 3.2189 = 12.88; 6 x 2.3026 = 13.82; 24 x 1.2040 = 28.90. The minimum over the table is 12.88 (r = 4). The general lines r >= 4j of `gap-seed-shape.md` 1.5 are not in the table; for them the proved threshold t satisfies t^(j-1) < 1/(4.5 j^3), so 4j log(1/t) > 4 log(4.5 j^3) >= 4 log 36 > 14.3. So "no cube below 12.9 of its own correlation lengths" holds for every proved threshold. It does not cover the GUIDE fixed points (at r = 5 the GUIDE value 1/12 would give 5 log 12 = 12.4); the file says "present thresholds", which I read as the proved ones.

**The flux half at the large end.** HOLDS. 1 - Z^(1 nu)/Z = 2 Tr(T^n P_odd)/Tr T^n with P_odd = (1 - C_nu)/2; the top eigenvector is even (Theorem D (e) of row 697), so the numerator is at most 2 lambda_0^n S and the denominator is lambda_0^n (1 + S). x/(1 + x) is increasing, so S <= t gives the bound. The same line gives the fragment of 1.2, S >= (1 - zeta)/(1 + zeta), which I also checked.

**(PHYS-SEED-Delta).** HOLDS AFTER CORRECTION. Two points.
(a) From limsup D_j <= 6.1 x 10^(-4) one gets D_j <= 6.1 x 10^(-4) + eps for large j, not D_j <= 6.1 x 10^(-4). The margin is enough: exp(64 x 6.1 x 10^(-4)) - 1 = 0.03981, and exp(64 (6.1 x 10^(-4) + eps)) - 1 < 0.0399 for eps < 1.3 x 10^(-6). Write "S(n_j; (4 n_j)^3) < 0.0399 for all large j".
(b) "every cube of side at least 4 n_j has m >= 0.12/n_j" is not what Theorem SH gives. Theorem SH (i) gives m >= log(1/(22.2 x 0.0399))/n_j >= 0.121/n_j on the dyadic cubes of side 2^k 4 n_j only. For a general side L, (ii) gives m(L^3) >= (1/n_j)(0.1213 - 2^(-k) log(e E/K)) with E = (2 x 4/3)^3 = 18.96 and log(e E/K) = 0.843; this is negative for k <= 2. So for all cubes the uniform bound starts later: (iii) gives m(L^3) >= 0.06/n_j for every integer L >= 64 n_j (2^(k_0) >= 2 x 0.843/0.1213 = 13.9, k_0 = 4), as in Corollary TR1 of row 708. Text to use: "every cube of side 2^k 4 n_j has m >= 0.12/n_j, and every cube of side at least 64 n_j has m >= 0.06/n_j. In physical units the gap is at least 0.06/l_1 on every cube of side at least 64 l_1, uniformly in j." Nothing downstream in the file uses the constant 0.12 or the side 4 n_j.

## 3. Section 2.1, Lemma FLOW

HOLDS. One line is implicit and should be written: q_(k+1) >= sigma(q_k) > q_k >= u_0 while q_k is in I, so the sequence never falls below u_0, and leaving I means passing u_1. With it: if q_0, ..., q_K all lie in I, then u_1 >= q_K >= u_0 + K delta, so K <= (u_1 - u_0)/delta, and some k <= floor((u_1 - u_0)/delta) + 1 has q_k > u_1. delta > 0 because sigma - id is continuous and positive on a compact interval.

## 4. Section 3.1, Attempt 1

**Lemma Z.** HOLDS. r_i <= r_1 <= 1 for i >= 1, so S(T; b^3) = sum r_i^(T - T_0) r_i^(T_0) <= r_1^(T - T_0) S(T_0; b^3), and r_1 = exp(-m(b^3)). Proposition Delta needs integers T_0 >= 3 and b >= T_0, as stated. Its proof uses Z(a, b, b, b) <= Z(a, a, b, b)^(b/a) with b/a not an integer; this is right, because Tr S^(k') <= (Tr S^k)^(k'/k) for all integers k' >= k (Lemma A (a) over all integers).

**Corollary Z1.** HOLDS. With T_0 = b/4 >= 3 and T = b/2: S <= exp(64 D(b/4) - (b/4) m(b^3)) <= exp(-7.41) = 1/1652.4 < 1/1650 (log 1650 = 7.4085).

**Remark (other shapes).** HOLDS, for T_0 = theta b/r an integer at least 3. The condition is (1 - theta)(b/r) m >= (r/theta)^3 D + log(1/t), which is the printed one. Constants re-computed: 6 x 27 = 162 and 6 log 1650 = 44.45; 8 x 512 = 4096 and 8 log 25 = 25.75.

**Lemma Z'.** HOLDS. Care point 1 (the two uses of the monotony of F(n)/abs(n)):
- Upper bound for (T_0, b^3): F(T_0, b, b, b)/(T_0 b^3) <= F(T_0^4)/T_0^4, from three sides raised from T_0 to b >= T_0. Multiplying by T_0 b^3 > 0 gives F(T_0, b^3) <= (b/T_0)^3 F(T_0^4). The sign of F is not used.
- Lower bound for (2 T_0, b^3): F(2 T_0, b^3)/(2 T_0 b^3) >= F(b^4)/b^4, from the time side raised from 2 T_0 to b; this needs 2 T_0 <= b, that is rho >= 2, which is assumed. Multiplying by 2 T_0 b^3 gives F(2 T_0, b^3) >= (2 T_0/b) F(b^4). For odd rho, b is not a multiple of 2 T_0; the monotony over all integers covers it.
- Lemma A (b) for the transfer operator of b^3 in the time direction gives lambda_0^(T_0) >= Z(2 T_0, b^3)/Z(T_0, b^3), so g(T_0; b^3) <= 2 F(T_0, b^3) - F(2 T_0, b^3). The two bounds give 2 rho^3 F(T_0^4) - (2/rho) F((rho T_0)^4) = (2/rho) Phi_rho(T_0). Checked.
Remark: since Phi_rho(n) = rho^4 D(n) - D(rho n), Lemma Z' is Lemma Z with the factor 2 rho^3 D(T_0) - (2/rho) D(rho T_0) in place of rho^3 D(T_0); it is weaker by at most a factor 2 and needs no infinite lattice. This is consistent.

**Corollary Z1'.** HOLDS. rho = 4, T_0 = b/4, T = b/2: S <= exp(Phi_4(b/4)/2 - (b/4) m(b^3)), and (C'_b) gives (b/4) m >= Phi_4(b/4)/2 + 7.41. The identities of line 281 hold: Phi_4(n) = 256 D(n) - D(4n) (insert F = D + f abs(n)); D(n) = sum over k of 256^(-(k+1)) Phi_4(4^k n), because 256^(-K) D(4^K n) = F/abs - f along the cubes 4^K n tends to 0 (f is the limit along cubes, see 1.1.5 (iii) above).

**Lemma Z3.** HOLDS. Care point 2.
- Step 1, the split. 16 F(n^4) = 8 [d_1 + F(2n, n, n, n)]; 8 F(2n, n, n, n) = 4 [d_2 + F(2n, 2n, n, n)] with time the second side and B_2 = (2n, n, n); 4 F(2n, 2n, n, n) = 2 [d_3 + F(2n, 2n, 2n, n)] with B_3 = (2n, 2n, n); 2 F(2n, 2n, 2n, n) = d_4 + F((2n)^4) with B_4 = (2n)^3. Each step uses the symmetry of Z to put the doubled side in the time slot. Sum: Phi(n) = 8 d_1 + 4 d_2 + 2 d_3 + d_4. And d_i = 2 g(n; B_i) - g(2n; B_i) <= 2 g(n; B_i), because the terms n e(B_i) cancel. The weights 16, 8, 4, 2 sum to 30. Checked.
- Step 2, the range of the sides. Theorem S gives S(D_k/2; D_k^3) <= s_k (n_k = 2^k N, 2 n_k = D_k). Lemma E' needs h >= b > a >= 3: a = D_k/2 = 2^k N >= 3, b = D_k, h = h_i >= D_k. It is applied three times, each time in the direction whose side is still D_k, with the two other sides fixed at their current values (Lemma E' holds for any fixed pair of other sides, by its setting W(x, y) = Z(x, y, c, d)). The exponent in direction i is h_i/(D_k - D_k/2) = 2 h_i/D_k < 8 because h_i < 4 D_k. Product < 512. With all h_i <= 2 D_k each exponent is at most 4 (for h_i = D_k it is 2; Lemma E' at h = b is a valid weakening), product <= 64. Checked.
- Step 3. For D_k <= L < 2 D_k the sides L and 2L lie in [D_k, 4 D_k). The time L >= D_k/2, and g(t; B) is non-increasing in t because every r_i <= 1. So each g(L; B_i) <= 512 s_k, and Phi(L) <= 30 x 512 s_k = 15360 s_k. At L = D_k the sides are D_k or 2 D_k and the factor is 64: Phi <= 1920 s_k.
- Step 4. D(L) = sum over i of 16^(-(i+1)) Phi(2^i L) (the tail 16^(-K) D(2^K L) tends to 0 as for Phi_4 above). 2^i L lies in [D_(k+i), 2 D_(k+i)), and s_(k+i) <= s_k because q < 1. Sum: 15360/15 = 1024 and 1920/15 = 128. Checked.

**Theorem ZD.** HOLDS. Care point 3. The chain (A) <=> (B), (A) => (D), (D) => (C), (D) => (C'), (C) => (A), (C') => (A) closes the five forms.
- (A) => (B): Lemma Z3 at L = D_k; 128 q^(2^k)/5041 tends to 0 because q < 1 strictly.
- (B) => (A), from the shape r = 4 to r = 2: Proposition Delta gives s'_0 = S(a; (4a)^3) <= exp(0.03904) - 1 = 0.03981 < 1/25 = x_0 of the line r = 4, and K s'_0 <= 0.886 < 1. Theorem SH (i) with (j, p, q) = (2, 2, 3) has a_k = 2^k a and B_k = 2^k (4a)^3, so s'_k = S(2^k a; (2^(k+2) a)^3) and 22.2 s'_k <= 0.886^(2^k). With N = 2^(k+1) a = 2 a_k, the box (2N)^3 = (2^(k+2) a)^3 is B_k, and (T) gives S(N; (2N)^3) = S(2 a_k; B_k) <= S(a_k; B_k)^2 = (s'_k)^2. For large k this is below 1/5041. Checked.
- (A) => (D): Lemma Z3 gives D(L) <= 1024 s_0 < 1024/5041 for every L >= 2N; Corollary S3' gives b m(b^3) >= b log(1/q)/N, unbounded. Checked.
- (D) => (C): the supremum of b m(b^3) over multiples of 4 is infinite, and each finite set of b has a finite maximum, so the supremum over b >= max(4 a_0, 12) is infinite too; for such b, D(b/4) <= D_0. Checked.
- (C) => (A): Corollary Z1 gives s := S(b/2; b^3) <= 1/1650. The line "r = 2, two stages" (Lemma E three times with a = b/2, exponent 4 each) gives S(b/2; (2b)^3) <= 64 s e^(64 s) < 0.0396 < 1/25. This is the seed at r = 4 with a = b/2 >= 6; then as in (B) => (A). Checked.
- (D) => (C') and (C') => (A): Phi_4(b/4) = 256 D(b/4) - D(b) <= 256 D_0. Checked.
Scope: "a model of the class" means the abstract setting of `gap-seed-shape.md` 1.1 with (LB) (f finite); every input holds there.

**Corollary Z2.** HOLDS. If liminf D(a)/a = c < m_0/64, there are arbitrarily large a with D(a)/a < m_0/64 - eps', and for a >= 0.116/eps' this gives D(a)/a <= m_0/64 - 0.116/a. Then b = 4a: b m(b^3) >= 4 a m_0 > 256 D(a) + 29.64 (256 x 0.116 = 29.70 > 29.64). The second sentence is in fact proved for every a >= max(3, b_0/4), not only for large a: if (C) fails at b = 4a, then D(a) > (m_0/64) a - 0.1158.

**Theorem ZD-c.** HOLDS. Care point 4, the uniformity in j. Every constant is fixed before j is taken large:
- (PHYS-SEED) => the rest: limsup below 1/5041 gives one q' < 1 with 5041 S_j <= q' for all large j. Lemma Z3 at N = l/(2 a_j) (an integer at least 6, since l/(4 a_j) is an integer at least 3) gives D_j <= 1024 q'^(2^k)/5041 at every physical size from 2^k l on, the same bound for all large j. Corollary S3' gives (L/a_j) m_j >= (L/a_j)(2 a_j/l) log(1/q') = 2 (L/l) log(1/q'), independent of j. With the threshold 1/1650 one first uses the two-stage line and the line r = 4: K s'_0 <= 22.2 x 0.0396 < 0.88 for all large j, so the size 2^(k+1) l of P carries S below 1/5041 with one bound for all large j.
- (BDD-Delta) and (Z-UNB) => (PHYS-SEED): L_1 >= 4 L_0 in P, so L_1/4 is in P and at least L_0. For large j: z_j > 256 D_0 + 30 and D_j(L_1/(4 a_j)) <= D_0 + 10^(-3), so 256 D_j + 29.64 <= 256 D_0 + 29.90 < z_j, and b = L_1/a_j is a multiple of 4 and at least 12. Then (b/4) m - 64 D_j > 7.5 - 0.064 = 7.436, so S_j <= exp(-7.436) uniformly, and the upper limit is strictly below 1/1650. (The file writes "<= 1/1650"; the strict form is what (PHYS-SEED) asks, and it holds.)
- (PHYS-SEED-Delta) => (PHYS-SEED): D^+(l') < 6.1 x 10^(-4) gives one d < 6.1 x 10^(-4) with D_j <= d for large j; the recursion of the line r = 4 then has one rate for all large j.
- (Z-SEED) <=> (PHYS-SEED): psi^+(L) <= 256 D^+(L/4) because D >= 0; the rest as above. If psi^+(L) is infinite, (Z-SEED) fails at L, which is consistent.
One point of wording: D^+ and psi^+ may be infinite; the statement handles this correctly as written.

**Corollary Z4.** HOLDS AFTER CORRECTION. The dichotomy is right for multiples b of 4 with b >= max(4 a_0, 12) (for b = 4 or 8, D(b/4) is a torus with sides below 3 and is not defined). The last sentence over-reaches: "every periodic cube of side b has a level within (256 D_0 + 29.64)/b of its ground state" is proved only for b a multiple of 4 with b >= max(4 a_0, 12). Text to use: "every periodic cube whose side b is a multiple of 4, b >= max(4 a_0, 12), has a level within (256 D_0 + 29.64)/b of its ground state."
