lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T12:11Z

# Row 981, `gap-ladder-check-opus`: line-by-line check of row 978 (`library/gap-ladder-max.md`)

Check item, N1 of `library/gap-ladder-max.md` Section 8. Checker: Claude Opus 5.5, max effort, Mac mini worker 2, fresh session started 2026-11-15T00:11Z at commit 5093baf30 on `claude/ym4d-hard-route`. Author of the checked text: Claude Fable 5.2 (row 978). This is a different model from the author, but the same vendor; it is not an independent check in the sense of a different derivation unless stated per step. No new attack (row 981 scope). No numeric run.

## Plan (at most eight steps; one per response)

1. Read FINISH.md rules (build on published work, efficiency, rules) and `library/gap-ladder-max.md` Sections 5.1, 5.2, 5.6, 5.7, 8 and the (R2) claim; record the exact statements under check with line numbers.
2. Check Lemma IHC (5.1) line by line.
3. Check Corollary CU (5.2) and the derivation of (TH); read `library/gap-phys-seed.md` 1.1.5 (iii) and its conditional check (row 727).
4. Read in the account (CA-I/II/III at 31a47c543775) the two assumptions left by row 727: (a) V = E_m in one normalisation of Z; (b) delta_vac-bar uniform in the cutoff; quote file and line.
5. Check 5.6 (a).
6. Check 5.7 (the square-root test).
7. Check (R2): the size test K_a grows like 3 log(1/a) + log beta in physical units.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with the line) and RESULT line.

## Progress log

- 2026-11-15T00:11Z: file created; step 1 starting.
- 00:12Z: step 1 written. 00:15Z: step 2 written (Lemma IHC, its remarks, 5.6 (a)). 00:17Z: step 3 written (Corollary CU, (TH)). 00:22Z: step 4 written (account lines for (a), (b)); step 5 of the plan (5.6 (a)) was done inside step 2.

## Step 1. What is under check (read 00:11Z-00:12Z)

Read in full: `library/gap-ladder-max.md` at 5093baf30 (283 lines, 52,293 bytes; last relay commit 0bb19c7ce). FINISH.md sections Joining, Working efficiently, Rules, How we work. Line numbers below are of `gap-ladder-max.md` at that commit.

| Item | Lines | Claim |
|---|---|---|
| Lemma IHC, statement | L121-123 | (HC-vac)_alpha on B gives X(2s + 2m; B) <= theta_m X(2s; B), theta_m = 1 - tanh(alpha m), for all integers s >= 1, m >= 0 |
| Lemma IHC, proof (i)-(iv) | L125-128 | Chapman-Kolmogorov and self-adjointness; Holder between L^1 and L^2; Jensen; (5.3) |
| Lemma IHC, remarks | L131-135 | s = 1 gives Proposition HC with 36 beta abs(B); odd times; necessity of the rate; sharpness; Renyi remark (not used) |
| Corollary CU | L139-148 | (TH) and (HC-phys) give X(n; B) <= 2 Theta e^(-M_H (ell - tau_0 - a_iota)), hence (SEED-phys) under (SIZE-phys) |
| (TH) from two-sided stability | L150 | X(t_0; B) <= 2 c_F abs(B) t_0 (a/a_*)^4 = 16 c_F ell^3 tau_0/a_*^4 |
| What changes for the lane | L152 | K_phys(ell) = log(2 Theta/x_*)/(ell - tau_0) replaces K_a |
| (TH) from the account | L228-232 | Theta = 8 C ell^3 l from row 720, 1.1.5 (iii); (PHYS-SEED) once M_H (ell - l - a_iota) >= log(16 C ell^3 l/log(1 + s_*)) |
| 5.6 (a) | L182-186 | IHC needs (HC-vac) only on the functions p_s(u, .): (HC-traj)_(alpha, s) |
| 5.7, CU with (APR) | L197-201 | Proposition Delta and (APR) give (TH) with tau_0 = L_0, Theta = (2 ell/L_0)^3 A |
| 5.7, square-root test | L203 | slice restriction of a 4D inequality gives rate 2 sinh^2(omega/2), about omega^2/2, against the true omega |
| 5.7, defective form | L205 | defect D gives X(2s + 2m) <= 2D + theta_m X(2s), then the gap half |
| (R2) | L59, mark L254; restated L152, L244, L283 | K_a times the physical seed size grows like 3 log(1/a) + log beta |

Inputs to read for the check: (5.3), (HC-vac), Lemma HOT and Proposition HC (row 931, `gap-direction-max.md`); Theorem BR (`gap-fc-max.md`); K_a and Lemma RATE (`gap-trajtest-opus.md`, row 974); (SEED-phys) and Proposition P (`gap-seed-limit.md` Section 5); `gap-phys-seed.md` 1.1.5 (iii), Lemma Z, (APR), Proposition MB; Proposition Delta (`gap-mid-max.md`, row 709); `gap-phys-seed-check.md` (row 727); the account's lines for (a) and (b).

## Step 2. Lemma IHC (5.1, L119-135) and 5.6 (a) (L182-186): checked line by line (00:15Z)

**Inputs read.** Row 931, `gap-direction-max.md` L170-321: the setting of Step 5 (L262-270), (5.3) (L276), Lemma HOT (L201-206), Proposition HC (L305-320). Definitions used: T is the gauge-invariant transfer operator (all flux sectors), positive, with kernel T(u, w); nu = Omega^2 dU; P = Omega^(-1) (T/lambda_0) Omega; p_s(u, v) = sum_i r_i^s phi_i(u) phi_i(v), with phi_i = psi_i/Omega orthonormal in L^2(nu), phi_0 = 1, r_0 = 1.

**(5.3), re-derived (it is cited, not part of row 978).** ||p_s(u, .)||_2^2 = sum_i r_i^(2s) phi_i(u)^2 by orthonormality; the nu-mean of phi_i^2 is 1; so E_u ||p_s(u, .)||_2^2 = sum_(i >= 0) r_i^(2s) = 1 + S(2s). The sums converge for s >= 1 because T is trace class (bounded continuous positive kernel on a compact space). HOLDS.

**Statement (L121-123).** 1 - tanh(x) = 2 e^(-x)/(e^x + e^(-x)) = 2/(1 + e^(2x)); with x = alpha m this is theta_m, and theta_m <= 2 e^(-2 alpha m). HOLDS.

**(i) (L125).** (P^m f)(v) = integral of p_m(v, w) f(w) nu(dw). Spectrally, P^m p_s(u, .) = sum_i r_i^(m + s) phi_i(u) phi_i(.) = p_(s+m)(u, .). The phi_i are gauge invariant, so p_s(u, .) is a gauge-invariant function, and (HC-vac) applies to it for the given m. At m = 0, q' = 2 and the inequality is an identity. HOLDS.

**(ii) (L126).** p_s(u, .) >= 0: p_1(u, w) = T(u, w)/(lambda_0 Omega(u) Omega(w)) > 0, and p_s > 0 by Chapman-Kolmogorov. ||p_s(u, .)||_1 = (P^s 1)(u) = 1, since T Omega = lambda_0 Omega. The interpolation ||g||_(q') <= ||g||_1^(1 - theta) ||g||_2^theta with 1/q' = 1 - theta/2 is Lyapunov's inequality: write g^(q') = g^(q'(1 - theta)) g^(q' theta) and apply Holder with exponents 1/(q'(1 - theta)) and 2/(q' theta), whose reciprocals sum to q'(1 - theta/2) = 1. Solving: theta = 2 (q' - 1)/q' = 2 e^(-2 alpha m)/(1 + e^(-2 alpha m)) = theta_m, in (0, 1]. HOLDS.

**(iii) (L127).** Squaring (i) and (ii): ||p_(s+m)(u, .)||_2^2 <= (||p_s(u, .)||_2^2)^(theta_m) for every u. x -> x^theta is concave on [0, infinity) for 0 < theta <= 1; Jensen under u ~ nu, with E_u ||p_s(u, .)||_2^2 = 1 + S(2s) finite. HOLDS.

**(iv) (L128).** (5.3) at s + m and at s; logarithm. HOLDS.

**Independent cross-checks (different derivations, by hand).** (1) Symmetric two-point space, P = T_r (Bonami-Beckner): (HC-vac)_alpha holds iff alpha <= -log r; the lemma reads log(1 + x y) <= (2y/(1 + y)) log(1 + x), x = r^(2s), y = r^(2m); spot values x = 1, y in {0.1, 0.5, 1} pass (0.095 <= 0.126; 0.405 <= 0.462; equality at y = 1). (2) One Gaussian mode (L97): re-derived f'(x) = y (1 - y)(1 + x)/((1 + y)(1 - x)(1 - x y)), numerator 2(1 - x y) - (1 + y)(1 - x) = (1 + x)(1 - y). HOLDS.

**Remarks (L131-135).**

- L131 (s = 1): ||p_1(u, .)||_2^2 <= sup p_1(u, .) times ||p_1(u, .)||_1 = sup p_1, so X(2) <= log sup p_1 <= 36 beta |B| (Lemma HOT), and X(2m + 2) <= 72 beta |B|/(1 + e^(2 alpha m)) < 72 beta |B| e^(-2 alpha m). HOLDS.
- L132 (odd times): 0 <= r_i < 1 for i >= 1 (T positive, lambda_0 simple), so S is non-increasing; valid for t >= 2. HOLDS.
- L133 (necessity): r_1^(2s + 2m) <= S <= X e^X; m-th roots give r_1 <= e^(-alpha). HOLDS.
- **L134 (sharpness): FAILS as worded; HOLDS AFTER CORRECTION.** It says that in one Gaussian mode the two sides "differ by at most the factor 2/(1 + e^(-2 alpha m))". The direction is wrong. With L(z) = -log(1 - z), convex with L(0) = 0, L(x y) <= y L(x). So the ratio (theta_m X(2s))/X(2s + 2m) = (2y/(1 + y)) L(x)/L(x y) is **at least** 2/(1 + y), with equality only in the limit x -> 0 (cold start). For x -> 1 at fixed y the ratio is unbounded. Correct wording: "in one Gaussian mode the bound exceeds the truth by a factor at least 2/(1 + y), and tends to that factor as x -> 0; so theta_m cannot be replaced by any constant below y = e^(-2 alpha m)". Step 3's own sentence (L97, "as x -> 0 ... differ by the factor 2/(1 + y)") is correct. Nothing downstream uses L134.
- L135 (Renyi start value): marked ARGUED and not used. Consistent: log ||g||_(q')^2 = theta_m D_(q')(g), with D_q the Renyi divergence. The averaged step needs log E_u exp(theta_m D_(q')) to be about theta_m E_u D_(q') as theta_m -> 0, which holds to first order only. So "about" is the right word. No verdict needed.

**5.6 (a) (L182-186).** The proof above applies (HC-vac) only to h = p_s(u, .), for the given m, and only for nu-almost every u (step (iii) averages over u). So (HC-traj)_(alpha, s) gives X(2s + 2m) <= theta_m X(2s). (HC-traj) is implied by (HC-vac), so it is logically weaker. The sentence "the roughness at the lattice scale is gone" (L186) is a reading, not a step. **HOLDS.**

**Verdicts.** Lemma IHC: **HOLDS** (statement and proof, L121-128). Remarks L131-133: HOLD. Remark L134: **HOLDS AFTER CORRECTION** ("at most" must be "at least"; unused). 5.6 (a): **HOLDS.**

## Step 3. Corollary CU (5.2, L137-152), (TH) from the account (L228-232), and CU with (APR) (5.7, L197-201) (00:17Z)

**Inputs read.** `gap-seed-limit.md` L186-204 ((SEED-phys), Propositions P, P'). `gap-phys-seed.md` L53-96 (1.1, 1.1.5, Proposition 1.1), L243-272 (Lemma Z, Z'), L340-365 (Lemma DIL, Proposition MB, Corollary MB1). `gap-mid-max.md` L10 (row 709 note) and L144 (Proposition Delta: for integers a >= 3 and b >= a, g(a; b^3) <= (b/a)^3 Delta(a, a, a, a)). `gap-phys-seed-check.md` (row 727) in full. Notation: g(k; B) = log(1 + S(k; B)) = X(k; B); D(a) = Delta(a^4) = F(a^4) - f a^4, f = inf F(n)/abs(n).

### 3.1 Corollary CU (L139-148)

The (SEED-phys) quoted at L47 is `gap-seed-limit.md` L186 word for word in content. The proof, step by step:

1. t_0 is even and t_0 <= tau_0/a_iota < ell/a_iota <= n, so t_0 <= 2 floor(n/2), and m := floor(n/2) - t_0/2 >= 0 is an integer. Lemma IHC applies with s = t_0/2 if t_0 >= 2.
2. (HC-vac)_alpha implies (HC-vac)_alpha' for alpha' <= alpha (the L^q norms of a probability measure increase in q). So alpha = M_H a_iota can be used.
3. 2 alpha m >= M_H a_iota (n - 1 - t_0) >= M_H (n a_iota - a_iota - tau_0) >= M_H (ell - tau_0 - a_iota), using n a_iota >= ell.
4. X(2 floor(n/2)) <= theta_m X(t_0) <= 2 e^(-2 alpha m) Theta, and X(n) <= X(2 floor(n/2)) by monotonicity.
5. X(n) <= log(1 + s_*) if and only if S(n) <= s_*. So (SIZE-phys) gives the seed bound at n_iota, with n_iota a_iota <= ell (or <= ell + sup a_iota after rounding up).

**Verdict: HOLDS AFTER CORRECTION (two missing side conditions, no change of a constant).** (C1) (TH) must ask t_0 >= 2: Lemma IHC needs s >= 1, and X(0) is infinite. (C2) (SEED-phys) asks n_iota >= 3; with n_iota = ell/a_iota (or rounded up) this needs a_iota <= ell/3 for every iota. On the tail of a family with a_iota -> 0 it is automatic, which is all Proposition P' reads (R3); for "every iota" it must be assumed. (SIZE-phys) is a condition per iota because it contains a_iota; for all iota at once read it with sup a_iota.

### 3.2 (TH) from two-sided stability (L150)

Re-derived. X(t_0; B) = log Z(B x t_0) - t_0 log lambda_0, and log lambda_0 = lim over t' of (1/t') log Z(B x t') because Z(B x t') = lambda_0^(t') (1 + S(t')) and S(t') -> 0. The upper half at t_0 and the lower half at every t' >= t_0 give X(t_0) <= 2 c_F abs(B) t_0 (a_iota/a_*)^4. With abs(B) = 8 (ell/a_iota)^3 and t_0 <= tau_0/a_iota this is at most 16 c_F ell^3 tau_0/a_*^4. **The implication HOLDS.** Its hypothesis is a bound on the non-symmetric tori B x t for all t >= t_0 with one bulk constant e_iota; the account states bounds on tori of four equal sides only (1.1.2), so this paragraph is a hypothetical, as written ("Suppose").

**The sentence "(SIZE-phys) holds for every large ell" (L150): HOLDS AFTER CORRECTION.** (HC-phys) is a statement on the box of half side ell, so M_H may depend on ell. The sentence needs M_H bounded below uniformly in ell (it suffices that M_H(ell) ell/log ell -> infinity). Text to use: "if M_H can be taken independent of ell, (SIZE-phys) holds for every large ell".

### 3.3 "What changes for the lane" (L152)

A reading, not a step. Two slips of notation, neither used later: K_phys(ell) := log(2 Theta(ell)/x_*)/(ell - tau_0) uses the threshold x_* = log(22/17) of the lane's Form W box (a; (24a)^3), while Corollary CU is written for the (SEED-phys) box (n; (2n)^3), whose threshold is log(1 + s_*) <= 1.98 x 10^(-4); and it drops the a_iota of (SIZE-phys). The proof of Corollary CU works for any box and any threshold, so either form is a correct test once box and threshold match. "gap >= M_H" is remark L133 (E_1 >= alpha). "CT4 is its lower half": CT4 (GOAL.md L71) has the form log Z_L >= e abs(L) - c_F abs(L)(a/a_*)^4 with e = log Z_Tor/abs(Tor), which is the lower half on symmetric tori; on the tori B x t it is not stated. **HOLDS as a reading.**

### 3.4 (TH) from the account (L228-232) and CU with (APR) (L197-201)

- **Arithmetic.** In the account's unit the torus side is l = 2 L^m and the spacing a = L^(-K), so the start time t_0 = l/a = 2 L^(m+K) is an even integer (C1 holds). With b = 2n = 2 ell/a_iota, Proposition Delta needs b >= t_0, that is 2 ell >= l, which (SIZE-phys) forces anyway. 1.1.5 (iii) gives g(t_0; b^3) <= (b/t_0)^3 C l^4 = 8 C ell^3 l = Theta. Then 2 Theta = 16 C ell^3 l, and L230 is (SIZE-phys) with tau_0 = l. **HOLDS** given 1.1.5 (iii).
- **CU with (APR) (L197-199).** Proposition Delta with a = L_0/a_iota (an even integer >= 4) and b = 2 ell/a_iota >= a gives X(a; b^3) <= (2 ell/L_0)^3 D(a) <= (2 ell/L_0)^3 A. If n is rounded up, Theta = (2 n a_iota/L_0)^3 A <= (2 (ell + a_iota)/L_0)^3 A. The condition at L199 is 2 Theta = 2 (2 ell/L_0)^3 A. **HOLDS** (with the rounding remark). (APR) is used on the family iota, not on the geometric set N of Proposition MB; this is a hypothesis of the corollary, so nothing is lost.
- **L201** (MB1 needs (APR); here (APR) is the only ultraviolet input): agrees with row 727 L94. HOLDS.
- **L232, "(SEED-phys) follows from the account's own stability statements ... and (HC-phys)".** HOLDS AFTER CORRECTION, as in 3.2: it needs (HC-phys) at one half side ell that satisfies (SIZE-phys) with Theta = 8 C ell^3 l, where M_H is the constant of that box. The family must be the account's first-passage family, with lengths in its unit (row 727 L92 makes the same remark). Since l >= l_*(g) >= 2 L^11 and Theta >= 8 C l^4, the condition at ell = 2l reads M_H l >= log(128 C l^4/log(1 + s_*)), about 4 log l + 8.5 + log(128 C); a larger ell trades this for 3 log ell. So the needed rate in the account's unit is at least of order (log l)/ell, which is small, but M_H must hold on a box of half side ell > l, at least 2 L^11 unit lengths.
- **The input (TH) itself** is 1.1.5 (iii): checked as a conditional in row 727 (L20), with (a) and (b) unchecked. Step 4 reads (a) and (b) in the account.

## Step 4. The two assumptions of row 727 read in the account (00:22Z)

**Source.** Sussman and Alpoge's complete account (with Claude and Codex as authors of their text), commit 31a47c543775, fetched by URL into a new scratch folder `/tmp/gapladder981.WaBbSo/` (not committed): `theorem_0_complete_account_raw_I.tex` (166,711 lines), `..._II.tex` (145,624 lines), `..._III.tex` (111,583 lines), and the outline `YM4_sketch_500.tex` (32,992 lines). Line numbers below are TeX lines of these files. I read the statements and the lines named. I did not read the proofs of the correlation theorem.

### 4.1 What the account states

1. **The partition function and its normalisation.** CA-I L464 and L479: A(U) = sum over plaquettes of [1 - Re tr U(dp)], tr 1 = 1, and the bare density rho_0 = exp[-g_0^(-2) A(U)], no constant. CA-II Definition 8.22 (`8.22:not-partition-sources-cells`, L140873): Z_m(v) = integral of exp[-x_0 A(U) + O(v)] dU, with normalised Haar measure; "no normalising constant is included" (L140886).
2. **(UV-Z) with an explicit vacuum number.** CA-II L140891-140892: "For m >= m_T(g_-(g)) the correlation theorem supplies on T_m the following." Item (b), L140909-140910: abs(Z~_m(v)) <= e^(E_+^sharp (2L^m)^4) and Z~_m(0) >= e^(-C_low (2L^m)^4). L140918-140921: Z~_m(v) = e^(-E_m - calE_m(v)) Z_m(v), with E_m = sum over j < K of E^(j)_vac(T_m, T_m), "Balaban's normalisation constant of the bare density". calE_m(0) = 0 (L140895-140899). L140927: "The constants E_+^sharp and C_low do not depend on K, g_0 or m". L140932-140933: B = E_+^sharp + C_low <= C_B (1 + log g^(-2)).
   So at v = 0, with l = 2L^m: **E_m - C_low l^4 <= log Z_m(0) <= E_m + E_+^sharp l^4.** This is (UV-Z) with V = E_m (the E_m of Definition 8.22), C_- = C_low, C_+ = E_+^sharp, in the normalisation of item 1.
3. **The torus-independence lemma.** CA-II `8.22:lem-vacuum-energy-density`, L141276-141387 (index: PROVED). Conclusion, L141376-141386: delta_vac := abs(E_m/(2L^m)^4 - E_m'/(2L^m')^4) <= delta-bar_vac := 2(E_0 + 1) K_* sum over u >= 0 of L^(4u) exp[-(kappa/2)((1/2) L^11 L^u - 2)] < infinity, "and delta-bar_vac depends only on L and p; it does not depend on K, g_0, g, m or m'" (L141385-141386). Hypotheses: m, m' >= m_T(g_-(g)), and (a)-(c) (L141281-141375).
4. **But the lemma's E_m is another number.** Hypothesis (a), L141286-141291: "E_m'' denotes Balaban's normalisation constant of the bare density on T_m'', as in the normalisation of Z~_m'' in Definition 8.22, **less the Gaussian normalisers of the K steps**, the Gaussian normaliser of step j being the logarithm of the Gaussian integral of step j at the trivial background; the Gaussian normalisers of the two tori are compared by the determinant lemma." The proof (L141426-141432) explains why: the Gaussian normaliser is "the one torus-wide number per level", and "Were hypothesis (a) to admit even a bounded number of torus-wide numbers per level, they would contribute to delta_vac a term of order K(2L^min(m,m'))^(-4), which is not uniform in K at fixed m'." The remark after the lemma (L141531-141534): "The determinant lemma, which compares the Gaussian normalisers of the steps excluded by hypothesis (a), contributes a further constant, depending on L and p only (in particular not on K, g_0, g, m or m'), to the zero-source comparison of the two tori."
5. **The determinant lemma is not located.** I searched all four files for statement titles containing "determinant", "Gaussian", "normalis" or "torus", and the phrases "determinant lemma" and "Gaussian normaliser". The phrase "determinant lemma" occurs only at CA-II L141291 and L141531. The only statement with "determinant" in its title is CA-I L105992 (`4.24:prf-single-determinant`, the survivors' block), which is not a comparison of two tori. CA-I L3966-3985 compares the Gaussian normaliser with reference determinants for the coupling increment (a background-dependent coefficient), not the trivial-background value on two tori. The label index `sa-index/ca-full/index.tsv` has no other determinant entry. So the comparison of the Gaussian normalisers of two tori is asserted in a remark and not located as a statement of the account at this commit.
6. **The outline's V.** SA L23778-23786, (ST5): abs(Z_(a,l)(W)) <= exp[V_(a,l) + ... + C_+ l^4], Z_(a,l)(0) >= e^(V_(a,l) - C_- l^4); "The source-independent vacuum number V_(a,l) is real." (ST5) is a hypothesis with V existentially given; it does not define V.

### 4.2 Verdicts on the two assumptions

**(a) "V of (ST5) is E_m of CA-II 141374-141386, with the same normalisation of Z": FAILS as worded; HOLDS AFTER CORRECTION.** As worded it identifies V with the E_m of the lemma. That E_m excludes the Gaussian normalisers (item 4), so it does not satisfy (UV-Z) in general: log Z_m(0) - E_m^(lemma) contains the sum of the K Gaussian normalisers, and nothing bounds that sum by a multiple of l^4 uniformly in K. Correct form: (UV-Z) holds with V = E_m^(Def 8.22) (item 2, CA-II L140909-140921, C_- = C_low, C_+ = E_+^sharp, constants free of K, g_0, m). And E_m^(Def 8.22) = E_m^(lemma) + (sum over j < K of the Gaussian normaliser of step j) (CA-II L141286-141291). The normalisation of Z is not a problem: the account's Z_m(0) and the lane's Tr T^n differ by the exactly extensive factor e^(-x_0 x (number of plaquettes)) (item 1, if x_0 = beta), which cancels in Delta(n^4) = F(n^4) - f n^4 and in X = log(1 + S).

**(b) "delta-bar_vac is uniform in the cutoff": HOLDS, as a statement of the account (CA-II L141385-141386), for the E_m of the lemma, under its hypotheses (a)-(c).** For V = E_m^(Def 8.22) the density comparison needs in addition the determinant lemma, whose constant the remark at L141531-141534 asserts to be free of K, g_0, g, m, m'; the statement itself is not located (item 5).

### 4.3 What this changes in (TH) and in row 978

1.1.5 (iii) of row 720, read in the account: Delta(n^4) <= (C_+ + C_- + delta) l^4 holds with C_+ + C_- = B = E_+^sharp + C_low (CA-II L140927-140933) and **delta = delta-bar_vac + c_det**, where c_det is the constant of the determinant lemma. All are free of the cutoff K by the account's statements; c_det rests on a statement not located. So (TH) of Corollary CU, with Theta = 8 C ell^3 l and C = B + delta-bar_vac + c_det, is uniform in the cutoff **given** the correlation theorem (which supplies Definition 8.22 (b)), the hypotheses (a)-(c) of the lemma, and the determinant lemma. Row 978's L258 mark ("its assumptions (a) V = E_m in one normalisation, (b) delta_vac-bar uniform in the cutoff, both unchecked") should read: "(a) holds with V = E_m of CA-II Definition 8.22 (L140909-140921), not the E_m of the lemma at 141374-141386; (b) holds for the lemma's E_m (CA-II L141385-141386); the Gaussian normalisers need the determinant lemma, cited at CA-II L141291 and L141531 and not located in CA-I, II or III at 31a47c543775." This adds one named input, the determinant lemma, to the reduction "(SEED-phys) from the account plus (HC-phys)". By rule 0a I only name it; I do not attack it.
