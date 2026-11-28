lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T08:45Z

# Check of row 1017 (gap-compact-rigidity-max), work item W1

FINISH row 1019, `gap-compact-rigidity-check-opus`. Checker: Claude Opus 5.5, max effort, Mac mini worker 2. Same provider as the author (Claude Fable 5.2), so this is not an independent check in the sense of the working rules; it is a second reading by a different model. No subagents. Started 2026-11-15T20:45Z (from `date -u`).

Source under check: `library/gap-compact-rigidity-max.md` at commit 0d3b45d91 (499 lines), work item W1 at L459 and following.

**Provenance.** Claude Opus 5.5, max effort, Mac mini worker 2; source file at commit 0d3b45d91; one reading by one model of the same provider as the author; not an audit.

**Summary (read first).** First failing step: none. Every statement in W1's list is CORRECT-NO-ADVANCE, re-derived by hand (verdict table 8.1). Theorem CR is a correct equivalent form of (W), given Theorem ZD-c, once its limit set Omega is built with D_0 a bound of (BDD-Delta) (D2). Three scope repairs are needed in the text around it: Corollary TRI (III) (D3), the sentence in 3.6 (iii) and the proposed change 1 to `parts/gap.md` (D4), and the hypothesis of Lemma PT-inf (D12). Ten ranked defects in 8.2; none breaks a statement once repaired. (W), (LIOU) and (BDD-Delta) stay open.

## Plan (at most eight steps; one per response)

1. Read W1 exactly and the whole of row 1017's file; record the statements to check, the tests W1 asks first, the verdict scale and the stop rule. Read the cited definitions in `parts/gap.md` (Corollary Z4, Theorem ZD-c, (W), (PHYS-SEED), (BDD-Delta), the engine axioms).
2. Tests first: run the tests W1 names (counterexamples, edge cases) against the statements before any line-by-line reading.
3. Lemma UF and Theorem CE (compactness, kept properties, the numeric bounds 2.47 x 10^(-5), 256 D_0 + 34.11).
4. Proposition OM (compact limit set, doubling invariance, uniformly recurrent element, stalling functionals).
5. Theorem CR, both directions, with the most care (new equivalent form of (W)).
6. Corollary TRI, Lemma LV, and the FAILS claims (constants log m critical, Lemma PT-inf, Proposition SI).
7. Seeds (a)-(c) and the consumer claim, as far as W1 asks.
8. Verdict table and RESULT line.

(Superseded by the revised plan in Step 1. All eight steps are done.)

## Step 1: what W1 asks (read at L459 of the source)

W1 (verbatim scope): check line by line Sections 3.1-3.7 and 6.1 of `library/gap-compact-rigidity-max.md`: Lemma UF, Theorem CE (i), (ii)(a)-(e), Proposition OM (a)-(e), Theorem CR, the data A_(m,eps), Lemma PT-inf, Proposition NR, Proposition SI (4.1), Lemma LV, Corollary TRI (5.1). Read first: `gap-crux-restate.md` L29-45, L170-203; `gap-phys-seed.md` L253-257 (Lemma Z), L283-294 (Lemma Z3), L311-323 (Theorem ZD-c, Corollary Z4); `gap-mid-max.md` L63 (Proposition Delta); `gap-crux-exercise3-max.md` L690-713 (Lemma PT). Test first the six points of 5.1 (L348). Then judge: (i) is Theorem CR's equivalence right as stated, with (BDD-Delta) as the only extra hypothesis; (ii) is the admissible-sequence definition right for a trajectory (j_i -> infinity); (iii) does Lemma PT-inf (ii) need more than Lemma Z3. Report the first failing step, or none. Stop rule: no new attack.

Output name: W1 says `library/gap-compact-rigidity-check.md`; FINISH row 1019 and the worker prompt both say `library/gap-compact-rigidity-check-opus.md`. I write the latter only.

Report format (FINISH, Rules): one provenance line, a verdict per statement (ADVANCE, CORRECT-NO-ADVANCE, WRONG), then only the defects that break something, each with its explicit failure.

**Revised plan (replaces the provisional one above).**

1. Read W1 and the cited inputs (this section). Record each input statement as the check uses it.
2. The six test points of 5.1, each with a verdict.
3. Section 3.1 definitions, Lemma UF, Theorem CE (i).
4. Theorem CE (ii) Steps 1-6, with (a)-(e).
5. Proposition OM (a)-(e) and Lemma LV.
6. Theorem CR (most care), judgements (i) and (ii), Corollary TRI.
7. The data A_(m,eps), Lemma PT-inf (judgement (iii)), Proposition NR, Proposition SI.
8. Verdict table, defects ranked, RESULT line.

### 1.1 Inputs, as read at commit 0d3b45d91

All read in full at the lines W1 names. These are the forms the check uses; their own lane marks are not re-checked here.

- **(TM), (TM-c), Lemma A, (LB)** (`gap-crux-restate.md` L29-45). Z(n) = Tr T^(n_mu) with T positive, trace class, top eigenvalue simple with a strictly positive eigenfunction. C_nu commutes with T and Tr(T^(n_mu) C_nu) = Z^(mu nu)(n) > 0. Lemma A (a): k -> (Tr S^k)^(1/k) is non-increasing; Tr S^(jk) <= (Tr S^k)^j. So F(n)/abs(n) is non-increasing in each side, f is finite, Delta >= 0, and multiplying one side by an integer j multiplies Delta by at most j.
- **Theorem S** (L192-203): for n >= 3 and s = S(n; (2n)^3), S(2n; (4n)^3) <= ((1 + s)^64 - 1)^2; for x <= 1/640 the map is at most 5041 x^2. **Corollary S3'** (L217-219). **Lemma K, X, E, E'** (L176-213).
- **Lemma Z** (`gap-phys-seed.md` L255-260): for integers T_0 >= 3, b >= T_0, T >= T_0: S(T; b^3) <= (exp((b/T_0)^3 D(T_0)) - 1) exp(-(T - T_0) m(b^3)). PROVED GIVEN Proposition Delta (row 708, checked row 709).
- **Lemma Z3** (L283-294): if s = S(N; (2N)^3) < 1/5041, q = 5041 s, then for L >= 2N with D_k = 2^(k+1) N <= L < 2 D_k: D(L) <= 1024 q^(2^k)/5041. The bound depends on q only.
- **Theorem ZD-c** (L311-320) in the setting P = {2^i l_1}, l_1/(4 a_j) an integer at least 3 for large j: (PHYS-SEED) iff (PHYS-SEED-Delta) iff (Z-SEED) iff [(BDD-Delta) and (Z-UNB)]. (PHYS-SEED) has the threshold 1/5041 or 1/1650; the proof turns the second into the first at a larger size. **Corollary Z4** (L322-323).
- **Proposition Delta** (`gap-mid-max.md` L63): S(a; b^3) <= exp(r^3 D(a)) - 1, r = b/a > 1. Row 1017 uses it only at integer ratios (2 and 4), where its two-line proof (Theorem CE Step 5) needs only E_0 <= 0 and Lemma A (a). I re-derived that proof: log(1 + S(a; B)) = Delta(a, B) + a E_0(B) holds by the definitions, so it is right.
- **Lemma PT** (`gap-crux-exercise3-max.md` L690-713): for a product of two lattice models, Z = Z_1 Z_2, f = f_1 + f_2, D = D_1 + D_2, 1 + S = (1 + S_1)(1 + S_2), m = min(m_1, m_2).
- **(W)** (`parts/gap.md` L18-20, quoting row 998): "There is a physical size L in P with z^-(L) > 256 D_0 + 30, where D_0 bounds D^+ on the sizes from L/4 on." Note: (W) carries its own bound D_0 on the sizes from L/4 on.

Facts re-derived in Step 1 because the check leans on them (each is two lines; I wrote them out):

- (F1) Every datum in the sense (E1)-(E3) satisfies Lemma A (a) for its diagonal operators: (sum_r lambda_r^k)^(1/k) is non-increasing in k. So A2 (Delta multiplied by at most j when a side is multiplied by j), "F(n)/abs(n) non-increasing in each side", and f = lim_N F(N^4)/N^4 hold for abstract data, not only for lattice models.
- (F2) Hence Lemma PT (a), (c) hold for products of abstract data with the same proofs: f = f_1 + f_2 because both quotients tend to their infima along N^4, N -> infinity.
- (F3) (W) implies (PHYS-SEED) without assuming (BDD-Delta) separately: (W) gives D^+(L/4) <= D_0 and z^-(L) > 256 D_0 + 30, so for large j, (C_b) holds at b = L/a_j (256 x 10^(-3) < 0.36), Corollary Z1 gives S_j(b/2; b^3) <= 1/1650, and ZD-c's two-stage line gives the 1/5041 form. The converse is ZD-c. So (1) iff (2) in Theorem CR holds with no extra hypothesis.

## Step 2: the six test points of 5.1 (source L348), tested first

Each point re-derived by hand. No run.

1. **Tail bound of CE Step 3 at time T/2; domain.** PASSES. Step 1 at the time T/2 gives #{r : e_r <= E} <= exp(T E/2 + C'), C' = C(T/2, B). R(E) = floor(exp(T E/2 + C') + 1) is larger than that count, and the list is sorted, so every r >= R(E) has e_r > E. Then exp(-T e_r) = exp(-(T/2) e_r) exp(-(T/2) e_r) <= exp(-T E/2) exp(-(T/2) e_r), and the sum over all r of exp(-(T/2) e_r) is exp Delta(T/2, B) <= exp C'. The pair (T/2, B) is in the domain once 2^(-k_i) <= min(T/2, min B), and C' is valid once i >= i(m') with 2^(m') the least entry of (T/2, B); both hold for large i because k_i -> infinity. The same tail bound passes to the limit levels through finite partial sums.
2. **E_0 <= 0; the count for negative E.** PASSES. E_0(B) <= 0: k E_0(B) = log(1 + S(k; B)) - Delta(k, B) <= log(1 + S(k; B)), and S(k; B) -> 0 as k grows (dominated convergence: each ratio is below 1 by (E2), and the sum is finite at k = 3). The count in Step 1 holds for every real E without this fact: each level with e_r <= E adds at least exp(-T E) to exp Delta(T, B) <= exp C. What E_0 <= 0 is needed for is the upper bound e_0 <= 0, which keeps e_0^* finite, and Proposition Delta.
3. **Lemma UF, the margin c_S < 1/5041.** PASSES. 64/5041 < 0.012696; e^x - 1 <= x + x^2/2 + x^3/6 + ... < 0.012777 < 0.01278 for that x; 0.01278^2 = 1.6333 x 10^(-4) < 1.64 x 10^(-4) < 1/5041 = 1.9837 x 10^(-4). The map x -> ((1 + x)^64 - 1)^2 is increasing, so the bound holds at every x < 1/5041.
4. **Step 5: d_min and 34.11; one scale each.** PASSES. d_min = (1/8) log(1 + 1/5041) >= (1/8)(x - x^2/2) with x = 1/5041, which is 2.4794 x 10^(-5) > 2.47 x 10^(-5). 4 log 5041 = 8 log 71, and e^4.2627 > 71: e^4 > 2.71828^4 > 54.598, e^0.2627 > 1.30043 (the first six terms of its series), and 54.598 x 1.30043 > 71.0008. (A first draft of this line used 1.3004, whose product with 54.598 is 70.9992 < 71; corrected.) So 8 log 71 < 34.102 < 34.11. The lower bound reads (H2) at the scale b and D at b/2 (Proposition Delta at ratio 2); the gap bound reads (H2) at b and D at b/4 (Lemma Z with T_0 = b/4, T = b/2, ratio 4). Each is a non-strict inequality between finitely many values at one scale, so each passes to the limit (the scale b and the index condition i >= i(log_2 b) are fixed before the limit).
5. **Proposition OM (a): the diagonal choice keeps (H1), (H2).** PASSES, with one omission. Choosing, for the n-th element E_n, an index of its admissible sequence with k >= n, rescaled values within 1/n of E_n on the first n quadruples, and (H1), (H2) at abs(m) <= n with 1/n, gives (H1), (H2) with i(m) = abs(m). The proof does not say "and j >= n". After the second-pass correction the definition asks j_i -> infinity, so this must be added; it is available, because each admissible sequence has j_i -> infinity. Defect D1 below (repair: one clause).
6. **Lemma PT-inf (ii): Lemma Z3 uniform in j.** PASSES. Lemma Z3's bound 1024 q^(2^k)/5041 depends on q alone. (PHYS-SEED) gives one q' < 1 with 5041 S_j <= q' at the size l for all large j, so q <= q' for all those j. Along a sequence with j_i -> infinity and k_i -> infinity the rescaled D^2 at each fixed b is at most 1024 q'^(2^(k_i + log_2(b/l)))/5041 once 2^(k_i) b >= l, which tends to 0. See Step 7 for what else (ii) reads.

Result of Step 2: no point fails. One omission (point 5).

## Step 3: Section 3.1 (definitions), Lemma UF, Theorem CE (i)

### 3.1 Definitions (source L131-158)

Checked line by line.

- exp Delta(k, B) = sum over r of exp(-k E_r(B)): Z(k, B) exp(-f k abs(B)) = sum over r of exp(k log lambda_r - k f abs(B)). Right.
- E_0(B) <= 0 and S(k; B) = sum over r >= 1 of exp(-k (E_r - E_0)), m(B) = E_1 - E_0 = log(lambda_0/lambda_1): right (Step 2, point 2).
- Rescaling. For x in DD^4 with x_i >= 2^(-k), 2^k x_i is a positive integer, so 2^k u_j x_i is an integer at least u_j >= 3. exp Delta^(j,k)(T, B) = sum over r of exp(-T e_r^(j,k)(B)) follows by putting k' = 2^k u_j T in the line above. z^(j,k)(b) = (2^k u_j b) m_j((2^k u_j b)^3), the gap of the lattice cube times its side. Right.
- Domain remark (not a failure). s^(j,k)(b) reads the time 2^k u_j b/2, which is an integer only if 2^k u_j b is even, and Theorem S needs it at least 3. In ZD-c's setting u_j = l_1/a_j is a multiple of 4 and at least 12, so every size of P is fine. For an abstract family with u_j odd (the data A_(m,eps) use u = 3) only the scales with 2^k b >= 2 are defined; every use in Sections 3.3-3.7 is at large k, so nothing breaks. Defect D7 (wording: say "u_j even and at least 6", or "large k").
- Critical element (L158). The definition reads s_*, z_* "from the levels of the limit in Theorem CE (b)". For an eternal datum that is not known to be a limit, it must first say that the datum has the spectral form of CE (b) in each direction; then Lemma LV (6.1) makes the levels functions of Delta_*. With that clause the definition is consistent. Defect D8 (wording).
- Constants: checked in Step 2, point 4.

### 3.2 Lemma UF (source L160-166): CORRECT

Statement: if, for every l in P, the upper limit over j of S_j(l u_j/2; (l u_j)^3) is at least 1/5041, then along a subsequence every l in P has S_j >= 1/5041 for all large j.

Check. (a) Seeds go up: Theorem S at n = l u_j/2 gives S at the size 2l at most ((1 + s)^64 - 1)^2 <= 5041 s^2 < s when 5041 s < 1 (the estimate inside Theorem S's proof, valid for s <= 1/640). So the set of seeded sizes of P is closed upwards and equals {l >= l*_j}. (b) If l*_j <= L for all large j, then S_j at L is below 1/5041 and S_j at 2L is at most c_S < 1/5041 (Step 2, point 3) for all large j, so the upper limit at 2L is at most c_S, against the hypothesis at the size 2L of P. (c) So for each i the set {j : l*_j > 2^i} is infinite, and j_1 < j_2 < ... with l*_(j_i) > 2^i exist. For l in P and i with 2^i >= l, l < l*_(j_i), so l has no seed: S_(j_i) >= 1/5041. Right.

The lemma uses the hypothesis only at sizes 2L. It reads the 1/5041 form of (PHYS-SEED); the failure of the 1/1650 form implies the failure of the 1/5041 form, so either reading of "(PHYS-SEED) fails" is enough. Verdict: CORRECT-NO-ADVANCE (a compactness tool, sound; it moves no open item by itself).

### 3.3 Theorem CE (i) (source L170, L180): CORRECT

(i)(a), one datum in branch G. With Z_j = Z, u_j = u, any k_i -> infinity, and j_i = i (the index is a dummy for a constant family, so the corrected requirement j_i -> infinity costs nothing): (H1) holds once 2^(k_i + m) u >= a_0, and (H2) holds at every size because no size has a seed. Right. The identification "branch G = no seed at any size" when D is bounded is Theorem ZD ((A) iff (D)) with Corollary Z4; I re-read both and it is right.

(i)(b), a trajectory. Lemma UF gives J with l*_j -> infinity. With 2^(i_0) >= L_0 and k_i = 2i + i_0: for abs(m) <= i the sizes 2^(k_i + m) are at least 2^(i + i_0) >= L_0, so by (BDD-Delta) each of the finitely many values D_j(2^(k_i + m) u_j) is at most D_0 + 1/i for all large j (an upper limit at most D_0); and l*_j > 2^(k_i + i) for all large j in J. So j_i exists, larger than j_(i-1). Then (H1) at the scale m holds for i >= abs(m), and (H2) holds because 2^(k_i + m) <= 2^(k_i + i) < l*_(j_i). The sizes are at least 2 for i >= 1, so the times are integers in ZD-c's setting. Right.

Verdict: CORRECT-NO-ADVANCE.

## Step 4: Theorem CE (ii), Steps 1-6 and the claims (a)-(e) (source L172-198)

**Step 1, bounds.** Right. For x in DD^4 with least entry mu = 2^m, each side is mu times a power of 2, so A2 (valid for any datum, fact (F1)) gives Delta^(j,k)(x) <= (x_1 x_2 x_3 x_4/mu^4) D^(j,k)(mu) <= C(x) for i >= i(m). exp(-T e_0) <= exp Delta(T, B) <= exp C gives e_0 >= -C/T; E_0 <= 0 gives e_0 <= 0. The count #{r : e_r <= E} <= exp(T E + C) holds for every real E (Step 2, point 2).

**Step 2, extraction.** Right. Countably many quantities, each eventually in a compact interval ([0, C(x)] or [-C/T, +infinity]); a diagonal subsequence makes all converge. Each quantity is defined once k_i is large, which is all that a pointwise limit needs.

**Step 3, spectral form.** Right (Step 2, point 1). The finite part over r < R(E) converges term by term in (-infinity, +infinity], the two tails are at most exp(-T E/2 + C') each, and E is arbitrary, so exp Delta_*(T, B) = sum over r of exp(-T e_r^*(B)). Order of the levels and e_0^* in [-C/T, 0] pass to the limit. By (a), the same holds in each of the four directions.

**Step 4, thermal sums.** Right. S^(i)(T; B) = exp(Delta^(i)(T, B) + T e_0^(i)(B)) - 1 because exp Delta = exp(-T e_0)(1 + S); both terms converge, and the limit is sum over r >= 1 of exp(-T (e_r^* - e_0^*)).

**Claim (c), the transfer of inequalities.** The three examples are right: A2; Theorem S rescaled (n = 2^k u b); Proposition Delta at ratio 2. The general sentence ("every non-strict inequality between finitely many values ... holds in the limit") is right for inequalities whose two sides are continuous functions of finitely many values of Delta, S and e_r, with e_r taken in (-infinity, +infinity] and the inequality closed there. As written it is a meta-claim with no such clause. Defect D9 (wording; every use in the file is one of the examples or Step 5).

**Step 5, (d).** Right (Step 2, point 4). Lower bound: (H2) at b and Proposition Delta at ratio 2 with a = 2^k u b/2 give D^(i)(b/2) >= d_min for i >= i(log_2 b), so D_* >= d_min at every scale. Upper bound: (H1). Gap: Lemma Z at T_0 = b/4, T = b/2 (ratio 4, an integer; T_0 >= 3 for large k) gives S(b/2; b^3) <= exp(64 D(b/4) - (b/4) m(b^3)); with (H2), z^(i)(b) <= 256 D^(i)(b/4) + 4 log 5041, and both sides converge. z^(i)(b) bounded gives e_1^* finite on cubes.

**Step 6, (e).** Right, with one unstated fact. The three flips C_2, C_3, C_4 multiply disjoint sets of links by -1, so they commute with each other and with T_B; T_B is compact and self-adjoint, so one orthonormal eigenbasis diagonalises all four, and each level carries three signs at once. The source lists the signs one nu at a time and calls the result "a Z_2^3 grading" (3.4); the joint grading needs the commuting, which holds. eps_0 = +1: C_nu psi_0 is a positive eigenvector for the simple top eigenvalue, so C_nu psi_0 = psi_0. Quotients Z^(1 nu)/Z lie in (0, 1] because Z^(1 nu) > 0 (TM-c) and Z^(1 nu) = sum eps_r lambda_r^k <= Z. Signs take two values, so a diagonal subsequence fixes eps_r^(i) for each (r, B, nu) eventually; the signed tail is bounded by the unsigned tail, so Step 3 gives the signed formula. When levels merge in the limit, a merged level can carry mixed signs; only index 0 is forced even. That is what the source says ("vacuum even"). Defect D10 (wording: state the commuting).

**Claims (a), (b).** Right: symmetry by (E1); the bound by Step 1 and (H1); (b) by Steps 3 and 4.

Verdict on Theorem CE (ii)(a)-(e): CORRECT-NO-ADVANCE. No step fails. Remark (3) (Theorem SH's sharper constants pass to the limit "with five more doublings") was not checked; it is not used.

## Step 5: Proposition OM (a)-(e) (source L223-237) and Lemma LV (source L394-398)

**Unstated step, true.** Omega is "the set of all limits of admissible sequences". The first sentence of OM (b) and the use of CE (ii) need: a subsequence of an admissible sequence is admissible. It is: with i_l strictly increasing, i_l >= l, so D_0 + 1/i_l <= D_0 + 1/l, and (H1), (H2) at the scale m hold for l >= i(m); j and k still tend to infinity.

**OM (a): CORRECT, with D1.** Every element of Omega obeys CE (a), so Omega lies in the product of the intervals [0, (x_1 x_2 x_3 x_4/mu^4) D_0] over the countable set DD^4, which is compact and metrisable. Closed: the diagonal of Step 2, point 5, with "j >= n" added (D1). sigma: (j_i, k_i + 1) is admissible with i'(m) = i(m + 1), and Delta^(j,k+1)(x) = Delta^(j,k)(2x), so sigma maps Omega into Omega; (j_i, k_i - 1) is admissible with i'(m) = i(m - 1) (k_i - 1 still tends to infinity, and Delta^(j,k-1)(x) = Delta^(j,k)(x/2) is defined for x_i >= 2^(-(k-1))), so sigma^(-1) maps Omega into Omega. sigma permutes the coordinates of the product (x -> 2x is a bijection of DD^4), so it is a homeomorphism of Omega onto itself.

**OM (b): CORRECT, with D2 on the hypothesis.** First sentence: CE (ii) and the unstated step above. Second sentence, the direction "(PHYS-SEED) gives Omega empty": with q' < 1 and 5041 S_j <= q' at the size l for all large j, Theorem S gives 5041 S_j <= q'^(2^k) at 2^k l. Given any admissible sequence, k_i -> infinity puts 2^(k_i) in {2^k l : k >= 0} for large i, and j_i -> infinity puts j_i among the "large j", so (H2) fails at m = 0 for all large i. This direction holds for every D_0 and uses j_i -> infinity (judgement (ii), Step 6). The direction "(PHYS-SEED) fails gives Omega non-empty" is CE (i)(b), which needs D_0 to be a bound of (BDD-Delta). If D_0 is smaller than every such bound, Omega(D_0) can be empty while (PHYS-SEED) fails; for example D_0 < d_min gives Omega(D_0) empty for every family, because every element has D_* >= d_min (CE (d)). The text fixes "the family and D_0" in OM and says "for a trajectory with (BDD-Delta)" in (b) without tying the two. D2: state that D_0 is a (BDD-Delta) bound (any one; Omega grows with D_0, and the conclusion is the same for each).

**OM (c): CORRECT.** Lambda continuous on Omega and sigma continuous, so Lambda - Lambda o sigma is continuous on the compact non-empty Omega; if it were positive everywhere it would have a positive minimum delta and Lambda(sigma^n E) <= Lambda(E) - n delta would contradict boundedness. Lambda(E) = E(1, 1, 1, 1) is a coordinate, hence continuous, and Lambda(sigma E) = E(2, 2, 2, 2) = D_E(2).

**OM (d): CORRECT.** Zorn on the closed non-empty sets A with sigma(A) = A (a chain has non-empty intersection by compactness, and sigma of the intersection is the intersection because sigma is a bijection). In a minimal M the two-sided orbit closure of each point is closed, non-empty and invariant, so it is M. The open cover {sigma^(-n) U}, a finite subcover n_1, ..., n_p, and the gap bound 2 max abs(n_l) are right. Uniform recurrence in the sense of the definition (finite set of quadruples, eps) follows because those sets are a base of neighbourhoods.

**OM (e): CORRECT, with a loose parenthesis.** The proof needs n_i -> +infinity with sigma^(n_i) E -> E. That follows at once from uniform recurrence: the return times to each neighbourhood have bounded gaps in Z, so they are unbounded above, and a countable base of neighbourhoods gives the sequence. The parenthesis "(the forward limit set of E is closed, invariant and not empty, so it is M)" refers to the M of (d), but (e) is stated for every uniformly recurrent element; read with "M = the orbit closure of E, which is minimal" it is true, but that is a further fact (Birkhoff) the text does not prove. D11 (wording; the direct argument above replaces it). The rest is right: Lambda(sigma^n E) is non-increasing in n >= 0 with limit Lambda(E), so constant for n >= 0; sigma^(-n) E is uniformly recurrent too (apply the homeomorphism sigma^(-n) to the neighbourhoods), which gives n < 0; continuity extends the constant to the orbit closure.

**Lemma LV: CORRECT.** Uniqueness: multiply by exp(T e_0) with T = 2^i -> infinity. The left side tends to the multiplicity of e_0 (dominated convergence: the terms with e_r > e_0 decrease in T and are summable at one T). The right side tends to 0, to the multiplicity of e'_0, or to +infinity as e'_0 > e_0, = e_0, < e_0 (the first case again by dominated convergence). So e'_0 = e_0 with equal multiplicities; remove them and repeat. "Finitely many entries below each bound" makes the induction reach every finite entry; the rest are +infinity on both sides. Continuity: every element of Omega obeys the bound of CE (a) with D_0, so Step 1's bounds hold uniformly on Omega; any subsequence has a further subsequence with converging levels; Step 3 makes the limit levels a spectral form of the limit datum; uniqueness identifies them. So e_r^*, s_*, z_* (finite on Omega by CE (d)) are continuous on Omega, and OM (c), (e) and CR (5) apply to Lambda = s_*(1) and z_*(1). LV also repairs D8: it makes "the levels of an eternal datum" well defined whenever a spectral form exists.

Verdicts: OM (a)-(e) CORRECT-NO-ADVANCE (with D1, D2, D11, none breaking); Lemma LV CORRECT-NO-ADVANCE.

## Step 6: Theorem CR (source L239-249), judgements (i) and (ii), Corollary TRI (source L350-354)

### 6.1 Theorem CR, link by link

Setting read: a trajectory in ZD-c's setting (P = {2^i l_1}, u_j = l_1/a_j a multiple of 4 and at least 12 for large j), with (BDD-Delta) holding with the bound D_0 from L_0 on, and Omega = Omega(D_0) built with that D_0.

- **(1) iff (2).** Right, and it needs no extra hypothesis: fact (F3) gives (1) => (2) from (W)'s own bound; ZD-c gives (2) => (BDD-Delta) and (Z-UNB), and then L in P with L/4 >= L_0 and z^-(L) > 256 D_0 + 30 is (W). The source says "by Theorem ZD-c given (BDD-Delta)"; the hypothesis is harmless and unused here.
- **(2) => (3).** Right (Step 5, OM (b)), for every D_0. Uses j_i -> infinity and k_i -> infinity.
- **(3) => (2).** Right, with D_0 a (BDD-Delta) bound (D2). If (2) fails, CE (i)(b) gives an admissible sequence for this D_0, and CE (ii) gives an element of Omega.
- **(3) => (4), (3) => (5).** Trivial (any Lambda for (5)).
- **(4) => (3).** Right: OM (d) needs only Omega compact and sigma a homeomorphism of Omega (OM (a)).
- **(5) => (3).** Right: OM (c) gives, for every continuous Lambda on a non-empty Omega, an E with Lambda(sigma E) >= Lambda(E). "Continuous" means continuous on Omega for the pointwise topology; D_E(1), and by Lemma LV s_E(1) and z_E(1), are such functions.

Attempts to break it. (a) D_0 below d_min with D_0 free: Omega(D_0) is empty for every trajectory, so "(3) iff (2)" would fail. Excluded once D_0 is a (BDD-Delta) bound: then (3) => (2) is CE (i)(b), which builds the sequence from that bound; and if such a bound is below d_min < 6.1 x 10^(-4), (PHYS-SEED-Delta) holds, so (2) and (3) are both true. (b) (BDD-Delta) false: (1), (2) false, while Omega(D_0) can be empty for every D_0 (for instance if D_j(L u_j) grows without bound in L uniformly in j); so the hypothesis cannot be dropped from "(3) => (2)". (c) Bounded j: excluded by the definition (judgement (ii)). (d) The two thresholds of (PHYS-SEED): ZD-c makes them equivalent, and every step above reads the 1/5041 form. (e) A uniformly recurrent element of Omega that is not a limit of an admissible sequence: impossible, Omega is the set of such limits and is closed (OM (a)). (f) Lambda that is continuous on Omega but not on the whole product: OM (c) needs only continuity on Omega. No attempt breaks it.

**Verdict on Theorem CR: CORRECT-NO-ADVANCE, given Theorem ZD-c and its inputs, with D2 made explicit.** It is a true equivalent form of (W) on a trajectory with (BDD-Delta). It moves no open item: each of (3)-(5) is equivalent to (W), as the source says itself (L249).

### 6.2 Judgement (i): is CR's equivalence right as stated, with (BDD-Delta) as the only extra hypothesis?

Yes, with one precision. The hypotheses are (BDD-Delta) and ZD-c (with ZD-c's setting and inputs, lane check row 727). The precision: Omega must be built with D_0 a (BDD-Delta) bound (any one; Omega(D_0) grows with D_0 and the conclusion is the same for each). (BDD-Delta) is used only for (3)/(4)/(5) => (2); (1) iff (2) holds without it. Read with D_0 free, the statement is false for D_0 < d_min (D2).

### 6.3 Judgement (ii): is the admissible-sequence definition right for a trajectory (j_i -> infinity)?

Yes. j_i -> infinity is necessary: (PHYS-SEED) speaks only of large j, so without it a sequence that stays at one lattice model with no seed at any size would give a non-empty Omega while (PHYS-SEED) holds, and (2) => (3) would fail (the source's own reason, L392). It costs nothing in (3) => (2): CE (i)(b) produces j_i -> infinity, and for one datum the index is a dummy. k_i -> infinity is necessary as well: (2) => (3) needs the sizes 2^(k_i) to pass the seeded size l, OM (a) needs k_i - 1 -> infinity for sigma^(-1), and it is what makes the limit defined at every dyadic scale. Per-scale eventual bounds in (H1), (H2) are the right form: they are what CE (i)(b) can produce, and they are kept by subsequences and by the shifts k_i +- 1 (Step 5). The only place the corrected definition was not carried through is OM (a)'s diagonal (D1).

### 6.4 Corollary TRI: CORRECT, with a scope repair (D3)

As written, (III) "there is a uniformly recurrent critical element" names neither the family nor D_0. Read over abstract eternal data it is true for every family once D_0 >= log 2: the constant log 2 is then a critical element fixed by sigma (source 3.7), hence uniformly recurrent. (A constant is a critical element only if it is log m for an integer m >= 2: by Lemma LV a T-independent sum of exponentials has all its finite levels at 0.) Then "(I) excludes (III)" would be false. The intended reading, which the proof uses, is: (III) for some D_0, Omega(D_0) of this family has a uniformly recurrent element. With it: if (I) and (II) fail, (BDD-Delta) holds with some D_0, CE (i)(b) and OM (d) give (III); (I) gives (BDD-Delta) by Lemma Z3 (D_j <= 1024/5041 from the seeded size on, for all large j); (I) gives Omega(D_0) empty for every D_0 by the direction of OM (b) that holds for every D_0. Lemma Z3 and Theorem S apply to abstract data: their setting (a symmetric W with W(a, b) = Tr T_b^a) is (E1)-(E2). "For every family of data with units" needs the time l u_j/2 to be an integer at least 3 (D7). Verdict: CORRECT-NO-ADVANCE after D3.

### 6.5 The text around CR (source L245-249)

- (i) "no rate is needed": right as a reading of (5) => (3); by compactness a strict decrease on every element of Omega is automatically uniform.
- (ii) "they are fixed points only if a monotone exists (OM (e))": not what OM (e) says. OM (e) gives that Lambda is constant on the orbit closure (Lambda-stationary), not that the element is fixed; Way 3 (L369) words it correctly. D5 (wording).
- (iii) "the wall holds as soon as no critical element has a doubling on which its Casimir free energy does not fall": must read "no element of Omega" (no critical element of the trajectory). Over all critical elements with D_0 >= log 2 the premise is always false (log 2 is critical and has D(2) = D(1)), so the sentence is vacuous as written; for any D_0 it is not the statement CR proves, which is about Omega. The same scope is missing in the proposed change 1 to `parts/gap.md` (L414) and in 8.6. D4. Repaired wording: "(W) holds if and only if (BDD-Delta) holds with a bound D_0 and Omega(D_0), the set of blow-down limits of the trajectory, is empty; equivalently it has no uniformly recurrent element; equivalently every element E of Omega(D_0) has D_E(2) < D_E(1)."
- "A caution on (5)": "a Casimir free energy that falls strictly along the trajectory, to a positive limit, gives a limit object with constant D" is not proved: D^+(L) is an upper limit over j at fixed L, and the values D_(j_i)(2^(k_i) u b) along an admissible sequence are not tied to D^+(2^(k_i) b) without uniformity in j. The logical point of the caution (monotony of D^+ does not give (5)) stands without the example. D6 (mark the example ARGUED).

## Step 7: the data A_(m,eps), Lemma PT-inf (judgement (iii)), Proposition NR, Proposition SI

### 7.1 The data A_(m,eps) and the critical elements log m (source L253): CORRECT

Z(n) = 1 + (m - 1) exp(-eps abs(n)). (E2): T_B = diag(1, t, ..., t) on C^m, t = exp(-eps abs(B)) < 1, and Z(k, B) = 1 + (m - 1) t^k because abs(n) = k abs(B); top level 1, simple. (E3): every log Z(n)/abs(n) is positive and tends to 0 as abs(n) grows, so f = 0. Levels: E_0 = 0, E_1 = ... = E_(m-1) = eps abs(B), the rest +infinity. With u = 3: Delta^(j,k)(x) = log(1 + (m - 1) exp(-81 eps_j 16^k abs(x))) and e_r^(j,k)(B) = 81 eps_j 16^k abs(B) for 1 <= r <= m - 1. Choose k_i -> infinity, then j_i increasing with 81 eps_(j_i) 16^(k_i + i) <= 1/i. For fixed x, abs(x) <= 16^i for large i, so Delta^(i)(x) -> log m and e_r^(i) -> 0 for r < m. (H1): D^(i) <= log m = D_0. (H2): s^(i)(2^m') = (m - 1) exp(-81 eps_(j_i) 16^(k_i + m')/2) -> m - 1 >= 1 (the time (3/2) 2^(k_i + m') is an integer once k_i + m' >= 1). The limit is the constant log m: spectral form with m levels at 0, s_* = m - 1, z_* = 0, D_* = log m in [d_min, D_0], z_* <= 256 log m + 34.11, and sigma fixes it. Right. The lattice realisations (Ising, frozen Z_2) are recalled in the source and were not checked.

### 7.2 Lemma PT-inf (source L257-262): CORRECT after D12; judgement (iii)

Main claim. For abstract data, Lemma PT (a) and (c) hold by the same proofs (fact (F2)), so Delta = Delta^1 + Delta^2 on every torus, and the rescaled product converges to the sum. The spectral form of each limit needs only pointwise convergence to finite values and k_i -> infinity (a convergent sequence is bounded, which replaces (H1) in Step 1 of CE); Lemma LV then identifies the product's limit levels with the sorted sums e_r^1 + e_q^2, and 1 + S_* = (1 + S_*^1)(1 + S_*^2). Right.

(i) Critical plus bounded is critical. S_* >= S_*^1 >= 1/5041; D_* = D_*^1 + D_*^2 lies in [d_min, D_0^1 + sup D_*^2]; the gap of the sum is min(z^1, z^2) because the second level is the smaller of e_1^1 + e_0^2 and e_0^1 + e_1^2; and z_* <= z_*^1 <= 256 D_*^1(b/4) + 34.11 <= 256 D_*(b/4) + 34.11. Right. (It is not claimed that the sum lies in the Omega of the product family, and that is not needed.)

(ii) Seeded factors are forgotten. Lemma Z3 with N = l u_j/2 gives, for all large j, D_j^2 <= 1024 q'^(2^k)/5041 at every lattice size from 2^k l u_j on. At a fixed b, the rescaled size 2^(k_i) u_j b passes 2^k l u_j for every k once k_i is large, so D_*^2(b) = 0; A2 gives Delta_*^2(x) <= (x_1 x_2 x_3 x_4/mu^4) D_*^2(mu) = 0, and Delta >= 0. Right.

**Judgement (iii): does PT-inf (ii) need more than Lemma Z3?** It needs four further inputs, all available, one of them unstated. (1) j_i -> infinity and k_i -> infinity along the sequence: the hypothesis of PT-inf says only "a sequence along which both rescaled families converge". Without j_i -> infinity the seed of (PHYS-SEED), which holds for large j only, does not apply; without k_i -> infinity the sizes do not pass the seeded size. Both hold when the sequence is admissible for the first family; for "one model at one coupling" only k_i -> infinity is needed. D12: add these to the hypothesis. (2) A2, to pass from the symmetric tori to all quadruples (cited in the proof). (3) Lemma PT (a) for abstract data, for "the limit of the product is Delta_*^1" ((F2); the source cites Lemma PT, which is stated for lattice models). (4) The uniformity of Lemma Z3 in j, which holds because its bound depends on q alone (Step 2, point 6). Nothing else.

### 7.3 Proposition NR (source L264): CORRECT

Any CC that contains the limit of every admissible sequence of every family of data contains the limit log m of the family A_(m, eps_j) (7.1). So "CC contains no critical element" is false for every such CC. Right; it is close to a tautology, which is its point. The conditional half ("if the photon limit exists ... CC contains it and all its sums with other limits") holds for sums along a common sequence that is admissible for the product family; "all its sums" is loose. Folded into D13 (wording).

### 7.4 Proposition SI (source L280-282): CORRECT; one reading sentence too strong

Omega = sigma^t Omega (OM (a)) gives Omega in sigma^t QQ for every t. Right. The reading that follows ("A condition 'at small scales the datum looks like X' is, on Omega, the condition 'at every scale ...'"; "No boundary condition at one end of the scale axis is a kept property") is right for a condition on a fixed range of small scales (b <= b_0), and wrong for an asymptotic condition as b -> 0, which is already invariant under sigma, so SI says nothing about it. Example: "D_E(b) converges as b -> 0" is invariant and holds on every Omega made of constants. What actually keeps the trajectory's ultraviolet behaviour (D growing as the coupling falls) out of Omega is CE (d) (D_* <= D_0 at every scale), together with the fact that the small scales of a blow-down limit are large physical sizes of the trajectory. The conclusion of the paragraph stands on those; the sentence as worded is too strong. D14 (reading, breaks no statement).

Verdicts: A_(m,eps) CORRECT-NO-ADVANCE; Lemma PT-inf CORRECT-NO-ADVANCE after D12; Proposition NR CORRECT-NO-ADVANCE; Proposition SI CORRECT-NO-ADVANCE (reading sentence D14).

## Step 8: verdicts, defects, what was not covered

### 8.1 Verdict per statement (first failing step: none)

Defect labels are those used in Steps 2-7; 8.2 ranks them.

| Statement (source section) | Verdict | Defects |
|---|---|---|
| Lemma UF (3.2) | CORRECT-NO-ADVANCE | D7 (domain) |
| Theorem CE (i)(a), (i)(b) (3.3) | CORRECT-NO-ADVANCE | - |
| Theorem CE (ii)(a)-(e) (3.3) | CORRECT-NO-ADVANCE | D8, D9, D10 |
| Proposition OM (a)-(e) (3.5) | CORRECT-NO-ADVANCE | D1, D2, D11 |
| Theorem CR (3.6) | CORRECT-NO-ADVANCE, given Theorem ZD-c, with Omega built at a (BDD-Delta) bound D_0 | D2, D4, D5, D6 |
| Data A_(m,eps); constants log m critical (3.7) | CORRECT-NO-ADVANCE | - |
| Lemma PT-inf (3.7) | CORRECT-NO-ADVANCE after D12 | D12 |
| Proposition NR (3.7) | CORRECT-NO-ADVANCE | D13 |
| Proposition SI (4.1) | CORRECT-NO-ADVANCE; its reading sentence is too strong | D14 |
| Lemma LV (6.1) | CORRECT-NO-ADVANCE | - |
| Corollary TRI (5.1) | CORRECT-NO-ADVANCE after D3 | D3 |

No statement advances an open item: Theorem CR is an equivalent form of (W), as its author says. (W), (LIOU) and (BDD-Delta) stay open.

**Judgements W1 asks for.** (i) Theorem CR is right as stated, with (BDD-Delta) as the only extra hypothesis beyond Theorem ZD-c and its setting, once Omega is built with D_0 a (BDD-Delta) bound; (BDD-Delta) is used only for "Omega empty => (PHYS-SEED)", and (W) iff (PHYS-SEED) needs none (fact (F3)). (ii) The definition with j_i -> infinity (and k_i -> infinity) is the right one for a trajectory; it was not carried into OM (a)'s diagonal (D1). (iii) PT-inf (ii) needs, besides Lemma Z3, only A2, Lemma PT (a) for abstract data, and j_i, k_i -> infinity, the last not stated in its hypothesis (D12).

### 8.2 Defects, ranked by what each would break (none breaks a statement once repaired)

1. **D2, Theorem CR and OM (b): D_0 is not tied to (BDD-Delta).** OM fixes "the family and D_0"; CR says "for a trajectory with (BDD-Delta)". Failure if D_0 is read as free: for D_0 < d_min, Omega(D_0) is empty for every trajectory (CE (d) forces D_* >= d_min), so (3) holds while (1) and (2) may fail. Repair: "Omega = Omega(D_0), D_0 a bound of (BDD-Delta) (any one)". Then CR holds.
2. **D4, scope of 3.6 (iii), proposed change 1 to `parts/gap.md` (L414) and 8.6.** "No critical element has a doubling on which its Casimir free energy does not fall" quantifies over all critical elements; once D_0 >= log 2 the constant log 2 (D(2) = D(1)) is one of them, so the premise is never met and the sentence is vacuous; for any D_0 it is not what CR proves. It must read "no element of Omega(D_0)". Repaired wording in 6.5. This is the text the lead would place in `parts/gap.md` under W2.
3. **D3, Corollary TRI (III).** As written, (III) names neither the family nor D_0; for D_0 >= log 2 it is always true (log 2 is a critical element fixed by sigma), and then "(I) excludes (III)" is false. Repair: "(III) for some D_0, Omega(D_0) of this family has a uniformly recurrent element". The proof then holds.
4. **D12, Lemma PT-inf hypothesis.** Add "j_i -> infinity and k_i -> infinity" (only k_i for one model at one coupling), and note that Lemma PT (a), (c) are used for abstract data (fact (F2); PT is stated for lattice models).
5. **D1, OM (a) closedness.** Add "and j >= n" to the diagonal choice; the corrected definition asks j_i -> infinity.
6. **D5, 3.6 (ii).** "They are fixed points only if a monotone exists (OM (e))": OM (e) gives Lambda-stationarity on orbit closures, not fixed points (as Way 3, L369, says).
7. **D11 and D6.** OM (e)'s parenthesis about "M" refers to the minimal set of (d); the needed fact (returns at arbitrarily large positive times) follows from bounded gaps. The example in "A caution on (5)" (a strictly falling D^+ gives a limit with constant D) is not proved, because D^+ is an upper limit over j at fixed size; mark it ARGUED.
8. **D14, reading after Proposition SI.** "No boundary condition at one end of the scale axis is a kept property" is false for asymptotic conditions as b -> 0, which are already sigma-invariant (for example "D_E(b) converges as b -> 0" holds on an Omega of constants). That the trajectory's ultraviolet growth is not kept rests on CE (d), not on SI.
9. **D7, D8, D10, domain and definitions.** The time l u_j/2 must be an integer at least 3 (u_j even, at least 6; ZD-c's setting gives a multiple of 4, at least 12). The definition of a critical element must presuppose the spectral form of CE (b) in each direction (Lemma LV then fixes the levels). The joint Z_2^3 grading of CE (e) needs the three flips to commute, which they do (disjoint sets of links).
10. **D9, D13, wording.** CE (c)'s general sentence needs "two sides continuous in finitely many converging values, closed inequality"; NR's "all its sums with other limits" means sums along a common admissible sequence of the product family; 3.4 cites "3.6" for the data A_eps, which are in 3.7.

### 8.3 What this check did not cover

- The inputs were read at the lines W1 names (statements and proofs), and their proofs were followed where the check leans on them (Proposition Delta at integer ratio, Lemma Z, Lemma Z3, ZD-c's two directions, Lemma PT (a), (c)); they were not re-checked as a whole. Their own checks: rows 698, 699 (Theorem S), 709 (Proposition Delta), 727 (ZD-c), 999 (Lemma PT).
- Not in W1 and not checked: Remark (3) of 3.3 (Theorem SH's constants), Remark MON, Sections 3.4 and 3.7 beyond consistency with the theorems (the lattice realisations of log m, the NP and five-dimensional readings are recalled in the source), Sections 4.2-4.4, 5.2-5.4, 6.2, 7.
- The account's TeX (Sussman and Alpoge, with Claude and Codex as authors of their text) was not read: no statement in W1's scope cites it. The source's credits stand.
- Repo search: `origin/main` is not a ref of this checkout (`git rev-parse`, 2026-11-15T20:58Z), so main and the open PR branches were not searched. This row derives nothing new, so the rule has no derivation to guard.
- No numeric run (none needed; the numeric lock was not taken, and memory was not measured). No subagents. The checker (Claude Opus 5.5) is the same provider as the author (Claude Fable 5.2): a second reading by a different model, not an independent check in the working rules' sense.

### 8.4 Run record

Started 2026-11-15T20:45Z; RESULT first written 2026-11-15T21:00Z; final read-through and one arithmetic correction (Step 2, point 4) ended 2026-11-15T21:01Z (all from `date -u`). No file other than this one was written. No commit, no push.

RESULT: Row 1019 (Claude Opus 5.5 max, Mac mini worker 2; check of row 1017's W1, same provider as the author, so not independent; no numeric run, no subagents). First failing step: none. Lemma UF, Theorem CE (i) and (ii)(a)-(e), Proposition OM (a)-(e), Theorem CR, the data A_(m,eps) (the constants log m are critical elements), Lemma PT-inf, Propositions NR and SI, Lemma LV and Corollary TRI are CORRECT-NO-ADVANCE, each re-derived by hand. Judgement (i): Theorem CR is a correct equivalent form of (W) given Theorem ZD-c, with (BDD-Delta) the only extra hypothesis, provided Omega is built with D_0 a (BDD-Delta) bound (D2; with D_0 free and below d_min it fails); (BDD-Delta) is used only for "Omega empty implies (PHYS-SEED)", and (W) iff (PHYS-SEED) needs none. Judgement (ii): j_i -> infinity (with k_i -> infinity) is the right definition; OM (a)'s diagonal must add j >= n (D1). Judgement (iii): PT-inf (ii) needs, besides Lemma Z3, only A2, Lemma PT (a) for abstract data, and j_i, k_i -> infinity, which its hypothesis must state (D12). Scope repairs: TRI's (III) and the wording of 3.6 (iii) and of proposed change 1 to `parts/gap.md` must be restricted to Omega of the trajectory (as written, with D_0 >= log 2, they are false or vacuous because log 2 is always a critical element); smaller wording defects in 8.2. Open, not moved: (W), (LIOU), (BDD-Delta).
