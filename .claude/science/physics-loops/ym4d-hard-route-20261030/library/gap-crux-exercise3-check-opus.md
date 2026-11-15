lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T02:08Z

# Check of row 998 (gap-crux-exercise3-max), work item W1

Queue row 999 (`FINISH.md` line 1078), queued 2026-11-15 14:08Z. Checker: Claude Opus 5.5, max effort, Mac mini worker 3, started 2026-11-15 14:08Z at commit f75650fe8 on `claude/ym4d-hard-route`. The checked file `library/gap-crux-exercise3-max.md` was written by Claude Fable 5.2. Same vendor, different model; this is not an independent check in the sense of the working rules (a different derivation counts only where the derivation below differs from theirs, and each test says whether it does).

## Plan (at most eight steps; one step per response; each result appended before the next)

1. Copy W1 of `library/gap-crux-exercise3-max.md` 9.7 (L895-910) into this file. DONE below.
2. Read the files W1 names (the checked file's 1.2, 3.2 (L5), 6c, 6d, 8.1, 8.2, 8.5, and the outside line ranges); record what each says that the tests use.
3. Tests (a) and (b): Lemma PT (b) transfer operator and gauge projection under (TM-gen); Lemma PT (a) f = f_1 + f_2.
4. Test (c): Corollary PT1, "massless phase" to "no seed" for compact U(1) Wilson, and the published theorem.
5. Test (d): Proposition KF (c), "first-passage data" for a general weight; can a constant sequence meet it.
6. Test (e): Corollary KF1 against row 988.
7. Items (iii), (iv), (v): the 6c table rows, the 6d rows, the two 8.5 corrections.
8. Verdicts per item with the line, stop rule, RESULT line.

## Step 1. W1 as written (copied from `library/gap-crux-exercise3-max.md` L895-910)

> **W1. Check of this file (a model that did not write it; a cross-provider model if one is free; high effort).**
> *Statement to check:* `library/gap-crux-exercise3-max.md`: (i) Lemma PT and Corollary PT1 (8.1); (ii) Proposition KF
> and Corollary KF1 (8.2); (iii) the rows of the table in 6c for "Product with a massless factor", "w_p", "K7 line"
> and "Frozen Q_8, 2T"; (iv) 6d rows 24, 28, 30, 33 and the last two rows; (v) the two corrections of 8.5.
> *Read:* this file, Sections 1.2, 3.2 (L5), 6c, 6d, 8.1, 8.2, 8.5; `library/gap-crux-restate.md` L36-56 (definitions,
> (TM)) and L170-222 (Theorem S); `library/gap-phys-seed.md` L296-323 (Theorems ZD, ZD-c); `library/gap-crux-fp.md`
> L356-364 (Proposition V); `library/gap-unit-max.md` L231-246 and L357 (Route 3, N2); `library/gap-mid-max.md` L64-67,
> L226-229 ((CAS), the product device); `library/gap-crux-exercise2-check-astra.md` L227-259.
> *Test first:* (a) in Lemma PT (b), that the transfer operator of the product model is the tensor product,
> including the gauge projection, for the general weights of (TM-gen); (b) in Lemma PT (a), f = f_1 + f_2;
> (c) in Corollary PT1, the step from "massless phase" to "no seed" for compact U(1) with the Wilson weight, and
> which published theorem covers it; (d) in Proposition KF (c), whether "first-passage data" is a well-defined
> clause for a general weight, and whether the clause can be met by a constant sequence; (e) whether Corollary KF1
> changes any conclusion of row 988 other than the wording of (c) and N2.
> *Verdict per item:* HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. No new attack.
> *Stop rule:* one reading; stop at the list. *Output:* `library/gap-crux-exercise3-check-<model>.md`, ending with one RESULT line.

Provenance of the check. W1 asks for "a model that did not write it; a cross-provider model if one is free". The author is Claude Fable 5.2; this checker is Claude Opus 5.5. That meets "a model that did not write it" and does not meet "cross-provider" (FINISH row 999 says a gpt-6-astra check is held). W1 asks for high effort; this run is at max. The derivations below are written out by me; where a test only re-reads the author's argument rather than re-deriving it, the test says so.

No-new-attack rule: W1 says "No new attack". Nothing below attacks an open lemma; where a test needs a fact that is open in the lane, it is named and left open. Grep of `library/open-core.md` and the FINISH rows is therefore not triggered (no open lemma is attacked).

State after step 1: done 2026-11-15T14:10Z.

## Step 2. Sources read, and what the tests use from each

Read in this run (2026-11-15, 14:09Z to 14:15Z, times from `date -u`), at commit f75650fe8:

- Checked file `library/gap-crux-exercise3-max.md`: L1-890 in full (status, Steps 0-8, 9.1-9.6), and 9.7-9.9. So Sections 1.2, 3.2 (L5 at L276-288), 6c (L529-566), 6d (L568-590), 8.1 (L690-722), 8.2 (L724-744), 8.5 (L794-818) were read in full.
- `library/gap-crux-restate.md` L30-56 (definitions; (TM) at L32; (TM-c) L34; Lemma A L36; "F(n)/|n| is non-increasing in each side", (LB), Delta at L38-44) and L170-222 (Theorem S, Lemmas K, X, E, E', Corollaries S2, S3, S3').
- `library/gap-phys-seed.md` L290-330 (Lemma Z3 end, Theorem ZD, Corollary Z2, Theorem ZD-c, Corollary Z4, the (Z-UNB) flux remark).
- `library/gap-crux-fp.md` L315-366 (setting with (TM-gen) at L319; Lemma COV; Lemma REG; the van Enter-Shlosman reading; Proposition V at L356-359; "What is left as the separating property" L363).
- `library/gap-unit-max.md` L225-246 (Route 3 (a)-(c) and its verdict) and L350-362 (N1-N3; N2 at L357).
- `library/gap-mid-max.md` L58-70 ((CAS) at L64, its verdict L67) and L205-236 ((NOCRIT), 5.2 "(CAS): why it is not attacked", Identity FL, "The two parts are independent in the class": the product device at L226-229).
- `library/gap-crux-exercise2-check-astra.md` L222-262 (section 7, "The Q8/2T test narrowing -- FAILS as an argument for exempting ES", with (FG1), (FG2)).
- Located by grep, because test (a) names it: `(TM-gen)` is defined at `library/gap-crux-fp.md` L319 ("the statements (TM) and Lemma 4.1 (a) of `gap-mid-max.md` ... hold for this weight ... This is an unchecked input") and restated in the check of that file, `library/gap-crux-fp-check.md` L82 ("(TM), the symmetry of Z, Theorem S, Corollary S3' and the layer form (1.2) for that weight"), with L88 (the w_p kernel is of positive type) and L182 ("(TM-gen) for this weight is not checked (row 717)").

What the tests use:

| Test | Uses |
|---|---|
| (a) | (TM) as stated at restate L32 (an abstract statement: a positive trace-class T with Z = Tr T^(n_mu), simple top eigenvalue, strictly positive eigenfunction); the layer form (1.2) of `gap-transfer.md` as quoted in Lemma COV (fp L329: exp(-S) is a product over layers of T_0(U(t), g_t . U(t+1)), each g_t in one factor); (TM-gen) at fp L319; the product device of row 708 at mid L226-229 (Wilson SU(2) x Ising, checked row 709). |
| (b) | restate L38-40 ("F(n)/|n| is non-increasing in each side"; f := inf). |
| (c) | Corollary PT1 (checked file L715-718); I28 (L213); the U(1) row of 6c (L538); Theorem S, Corollary S3' (restate); Lemma COV (fp); whatever published theorem is found. |
| (d) | Proposition KF (L726-738); I22 (L202); Theorem ZD-c (phys-seed L311-319); Proposition V (fp L356-359). |
| (e) | Corollary KF1 (L740-744); Route 3 and N2 (unit L231-246, L357); the RESULT line of row 988 in `FINISH.md`. |

State: step 2 done 2026-11-15T14:15Z. Next: step 3, tests (a) and (b).

## Step 3. Tests (a) and (b): Lemma PT (b) and (a)

Additional source read for (a): `library/gap-transfer.md` L34-51 (notation N.1-N.8), L108-131 (Statement (1), the layer form (1.2)), L168-180 (Statement (4)). There T is built on H = L^2(X), X = G^E (spatial links of one slice, product Haar measure); P is the gauge projection (Pf)(u) = integral over the gauge group G^V of f(h . u) dh; T_0(u, v) = exp(-V(u)/2) K_0(u, v) exp(-V(v)/2) with K_0(u, v) = product over spatial links of c(u_l v_l^(-1)); T_P = P T P = T P has the kernel A_T(u, v) = integral of T_0(u, h . v) dh; Z_T = Tr(T_P^T) (1b). The file is written for G = SU(2) and the Wilson one-bond kernel c.

### Test (a). Lemma PT (b): the transfer operator of the product is the tensor product, gauge projection included

**My derivation (written before comparing with the author's two lines; it follows the construction of `gap-transfer.md`, so it is the same route, written out).** Let the factors have compact groups G_1, G_2 and one-bond kernels c_1, c_2 of the form required there (real, positive, bounded below by a positive constant, c_i(g^(-1)) = c_i(g), conjugation invariant, of positive type). For M take G = G_1 x G_2 and c(g_1, g_2) = c_1(g_1) c_2(g_2).

1. Slice space. X = (G_1 x G_2)^E = X_1 x X_2 with the product of the two product Haar measures, and L^2(X_1 x X_2) is the Hilbert tensor product L^2(X_1) (x) L^2(X_2) (finite measure spaces).
2. Gauge projection. The gauge group (G_1 x G_2)^V = G_1^V x G_2^V acts coordinatewise, h . (u_1, u_2) = (h_1 . u_1, h_2 . u_2). The normalized Haar measure of a product of compact groups is the product of the normalized Haar measures (the product measure is invariant and normalized, and Haar measure is unique). So by Fubini (Pf)(u_1, u_2) = double integral of f(h_1 . u_1, h_2 . u_2) dh_1 dh_2, that is P = P_1 (x) P_2, and Ran P = Ran P_1 (x) Ran P_2.
3. Kernel. The spatial action is V = V_1 + V_2 and K_0 = K_0^(1) K_0^(2) (one product over links of c = c_1 c_2). So T_0 = T_0^(1) T_0^(2) as a function of ((u_1, u_2), (v_1, v_2)), and by Fubini A_T((u_1, u_2), (v_1, v_2)) = A_T^(1)(u_1, v_1) A_T^(2)(u_2, v_2). An integral operator with a bounded product kernel on a product of probability spaces agrees with the tensor product of the two integral operators on product vectors f_1 (x) f_2, whose span is dense, and both are bounded. So T_P = T_P^(1) (x) T_P^(2).
4. Spectral statements. Each T_P^(i) is positive, compact and trace class with an orthonormal eigenbasis of L^2(X_i) (eigenvalue 0 included). The products of the basis vectors form an orthonormal basis of the tensor product, so the eigenvalues of T_P, with multiplicity, are the products lambda_i mu_j. T_P is positive (a tensor product of positive operators) and trace class with Tr T_P^k = Tr (T_P^(1))^k Tr (T_P^(2))^k. Since mu_0 > 0 and lambda_i < lambda_0 for i >= 1 (and the same for mu), every product other than lambda_0 mu_0 is strictly smaller: lambda_i mu_j <= lambda_i mu_0 < lambda_0 mu_0 if i >= 1, and symmetrically. So lambda_0 mu_0 is simple. Its eigenvector Omega_1 (x) Omega_2 is the function Omega_1(u_1) Omega_2(u_2), strictly positive, and gauge invariant by step 2.
5. Weight class. If c_1 and c_2 are of positive type, so is c (the product of two positive-type kernels on G_1 x G_2 is of positive type: Schur's product theorem for kernels; in characters, the irreducible characters of G_1 x G_2 are the products chi_rho chi_sigma, so non-negative coefficients multiply to non-negative coefficients). Symmetry under inversion, conjugation invariance and the two-sided bounds pass to the product. So the product weight lies in the class that the general-weight statement (TM-gen) (`gap-crux-fp.md` L319) describes, whenever both factor weights do.

**A second route, abstract (a different derivation; it needs no construction).** (TM) at restate L32 is an abstract statement. Given operators T_1 on L^2(X_1) and T_2 on L^2(X_2) with the properties of (TM) for M_1 and M_2, the operator T := T_1 (x) T_2 satisfies Tr T^(n_mu) = Z_1(n) Z_2(n) = Z(n) and every property of (TM), by step 4. Moreover the engine reads only spectral data, and these are fixed by Z: if two positive trace-class operators have equal Tr T^k for all k >= 3, they have the same non-zero eigenvalues with the same multiplicities (divide by the larger top eigenvalue to the power k and let k grow; dominated convergence identifies the top eigenvalue and its multiplicity; remove it and repeat). So S(k; B) and m(B) of M are those of T_1 (x) T_2 whichever realization of (TM) is used for M.

**Comparison with the author's proof (checked file L708-713).** The author's (b) is steps 2-4 in one line each. It is right. It says "the kernel of T_B is the product of the two kernels; the gauge projection is the tensor product of the two projections"; steps 2 and 3 above supply the two Fubini steps and the uniqueness of Haar measure that this uses.

**What the test finds besides.** Lemma PT assumes (TM) for each factor. That is a hypothesis of the lemma, so (b) is correct as stated. But Corollary PT1 applies the lemma with M_1 = compact U(1) with the Wilson weight. (TM) for that model is not proved in the lane: `gap-transfer.md` is written for SU(2) (N.1), and (TM-gen) at `gap-crux-fp.md` L319 is an unchecked input (row 717), stated there for weights on the same group. My reading of `gap-transfer.md` Statements (1)-(4) is that they use only compactness of the group, invariance of Haar measure, and a one-bond kernel that is symmetric, conjugation invariant, of positive type and bounded between two positive constants. U(1) with exp(beta cos theta) has these (exp(beta cos theta) = sum over n of I_n(beta) e^(i n theta), I_n(beta) > 0). This reading is not a check: I did not read Statements (2), (3) and the lemmas A0-A3 in full. Statement (5), the strict gap at a fixed box, uses SU(2) polynomials (L194) and is not needed here: a simple top eigenvalue of a compact operator already gives lambda_1 < lambda_0.

**Verdict (a): HOLDS** (Lemma PT (b), checked file L698-700 and L708-711), for any two factors that satisfy (TM) through the layer construction, and also with (TM) read abstractly. **Correction to the marks downstream (Corollary PT1, L715):** its inputs are I28 **and (TM) for compact U(1) with the Wilson weight** (with the trace formula with insertions, if the step to "no seed" goes through correlations; see test (c)). The second is not in the lane; the mark "PROVED given I28" should read "PROVED GIVEN I28 and (TM) for U(1) Wilson".

### Test (b). Lemma PT (a): f = f_1 + f_2

**Derivation (mine; the same idea as the author's, with the step written out).** Z(n) = Z_1(n) Z_2(n) by Fubini (the normalized Haar measure of the product group is the product measure, step 2 above, and the weight is a product over plaquettes), so F = F_1 + F_2.

- f >= f_1 + f_2: for every n, F(n)/|n| = F_1(n)/|n| + F_2(n)/|n| >= f_1 + f_2.
- f <= f_1 + f_2: let eps > 0 and choose n^(i) with F_i(n^(i))/|n^(i)| <= f_i + eps. Let n be the coordinatewise maximum of n^(1) and n^(2). F_i(n)/|n| is non-increasing in each side (restate L38, from Lemma A (a) for T_i, so from (TM) for the factor i), so raising the four sides one at a time gives F_i(n)/|n| <= F_i(n^(i))/|n^(i)| <= f_i + eps for i = 1, 2. So f <= F(n)/|n| <= f_1 + f_2 + 2 eps.

So f = f_1 + f_2 and D(a) = F(a^4) - f a^4 = D_1(a) + D_2(a). The author's sentence "along tori whose four sides all grow, both quotients tend to their infima together" is also right: by the second bullet, F_i(n)/|n| <= f_i + eps as soon as every side of n is at least the matching side of n^(i). Both f_i are finite (restate L38).

**Verdict (b): HOLDS** (checked file L697 and L705-708). Inputs: (TM) for each factor (for the monotonicity in each side), which is a hypothesis of the lemma.

**Lemma PT (c), (d)** (not asked by a test, read once): (c) follows from Tr T^k = Tr T_1^k Tr T_2^k divided by (lambda_0 mu_0)^k, and the second eigenvalue of T is max(lambda_1 mu_0, lambda_0 mu_1), so m = min(m_1, m_2). (d): S >= S_i since S_j >= 0; and S <= 2t + t^2. Both HOLD.

State: step 3 done. Next: step 4, test (c).

## Step 4. Test (c): Corollary PT1, from "massless phase" to "no seed" for compact U(1) with the Wilson weight

**Sources read for this test** (no network fetch was needed: the lane has a reading of the papers): `library/prior/gap-lit-u1.md` (42 lines, in full; row 782's literature reading: Frohlich-Spencer read in full from the IHES scan, Guth from the APS abstract only); `library/gap-u1-audit-opus.md` (105 lines, in full; row 784); `library/gap-tu-retry.md` L198-252 (Section 1.3) and L490-526 (W-score, final status) (row 786, Codex gpt-6-astra max); the RESULT lines of rows 784, 786, 794 in `FINISH.md` (L861, L863, L871); `library/gap-crux-exercise2-check-astra.md` L32 and L184 (check 884 on the use of row 786). I did not re-read Frohlich-Spencer or Guth myself; what they prove is taken from the row-782 reading, and is marked so.

**What Corollary PT1 needs.** If M = U(1) x M_2 had a seed at N, Lemma PT (d) gives a seed of the U(1) factor at N. So the corollary needs: (NS-U1) compact U(1) with the Wilson weight, at the chosen coupling, has no seed S(N; (2N)^3) < 1/5041 at any N >= 3, on periodic tori. The corollary's mark is "PROVED given I28", and I28 reads: "Compact U(1) in four dimensions has a massless, deconfined phase at large beta (Guth 1980; Frohlich and Spencer 1982). So it has no seed there."

**The step "So it has no seed there" is not a published theorem.** Reasons, each with its source:

1. Guth 1980 does not cover it at all. Its abstract (the only part the lane read) gives a Wilson-loop lower bound for the **Villain** action at g^2 < 0.168 (`prior/gap-lit-u1.md` L15). A perimeter law (no area law) does not contradict a gap: a Higgs-like phase, or frozen Z_2, has both (row 784, (OBS), `gap-u1-audit-opus.md` L22).
2. Frohlich and Spencer 1982 (CMP 83, 411-454) prove, for the Villain weight, and state with the derivation omitted for the Wilson cosine weight, at sufficiently large beta (existential threshold), a non-summability lower bound for the two-point function of the field-strength plaquette observables (`prior/gap-lit-u1.md` L9-12). The state is the infinite-volume state on Z^4 obtained from finite boxes **with fixed boundary links** (Ginibre inequalities); the paper says the method is not tied to the boundary condition, which is not a theorem about periodic tori (same lines). A seed is a statement about periodic tori.
3. So the step needs (BRIDGE) of row 784 (`gap-u1-audit-opus.md` L19-23, L101): "the infinite-volume fact on Z^4 with fixed boundary implies that the periodic seed fails". Row 784 found it proved nowhere.
4. The lane has since proved a periodic form for **Villain** only: row 786, `gap-tu-retry.md` Section 1.3, (10)-(12): at every fixed beta >= 2^14, in **every** periodic local limit (any sequence M -> infinity, any local weakly convergent subsequence), the bounded smooth gauge-invariant plaquette score s_p has a non-summable two-point function. Checked by row 794 (Claude Opus 5.5, cross-provider for this Codex row): every step of Sections 1-3 HOLDS. For the Wilson cosine the same statement is exactly (W-score), equation (24) at `gap-tu-retry.md` L495-507, "not claimed here"; L524: "The missing Wilson statement is exactly (24)."
5. From the periodic non-summability to "no seed" there is one more link, the seed form of (BRIDGE). I did not find it written in the lane as one statement (row 786 RESULT: "the periodic-torus non-summability that the BRIDGE step of row 784 asks for (dynamical form, not the seed form)"). It is the contrapositive route that row 784 names (L101). Written out, with every input named (ARGUED here, my composition, not checked):
   - Suppose Villain U(1) at beta has a seed at N, q = 5041 S(N; (2N)^3) < 1. By Theorem S and Corollary S3' (restate L192-222; they need (TM) for this model and the symmetry of Z), the tori of side D_k = 2^(k+1) N have r := lambda_1/lambda_0 <= q^(1/N) and sigma_k := S(D_k/2; D_k^3) <= q^(2^k)/5041.
   - By Lemma COV (`gap-crux-fp.md` L323-336; it needs the trace formula with insertions for this model), for the plaquette scores s_p(0), s_p(x) rescaled to absolute value at most 1, with delta = |x|_inf >= 2 and the direction of largest distance as time (as in Lemma REG): abs Cov <= 2.001 r^(delta - 1) + 5 sigma_k on the torus of side D_k.
   - Along any local weakly convergent subsequence of these tori the bound passes to the limit with sigma_k -> 0, so x -> Cov(s_p(0), s_p(x)) is summable in that periodic local limit. This contradicts row 786 (12). So Villain U(1) at every beta >= 2^14 has no seed at any N >= 3.
   Inputs of this composition: row 786 Section 1.3 (checked, row 794); Theorem S and Corollary S3' (checked, rows 698, 699); Lemma COV (checked, `gap-crux-fp-check.md`, row 716 check); **(TM) and the trace formula with insertions for Villain U(1), which the lane has not written** (`gap-transfer.md` is for SU(2); see test (a)).
6. The citation of row 786 for a U(1) test needs care: check 884 (`gap-crux-exercise2-check-astra.md` L32, L184) found that exercise 2 cited row 786 as a "Villain twist theorem", and that is a miscitation (row 786 Theorem V is a Langevin-gap theorem; it gives no twist statement). The use in item 5 is a different one: the static non-summability of Section 1.3, not Theorem V and not a twist.

**Answer to test (c).**

- For compact U(1) **with the Wilson weight**, no published theorem covers "massless phase implies no seed": Frohlich-Spencer cover Z^4 with fixed boundary links (and print no Wilson derivation); Guth covers deconfinement only. The step is (BRIDGE) of row 784 for the Wilson cosine, and its periodic half is (W-score) of row 786, open.
- For **Villain** U(1) at a fixed beta >= 2^14 the step is covered by lane results (row 786 Section 1.3, checked by row 794) plus the three-line composition of item 5, which rests on (TM) and the trace formula for Villain U(1). No published theorem is needed beyond what row 786 uses (its analytic input (5) is "prior repository work", the main-branch note PERIODIC_FINITE_CLOCK_VILLAIN, an adaptation of Frohlich-Spencer, `gap-tu-retry.md` L514-516 and L7; not re-read here).
- The rest of Corollary PT1 is logic and holds: if M has no seed, then for a tool (H, "H implies the seed") valid on a class that contains M, H(M) is false; if H(M) depends only on the factor M_2, then H is false at every M_2 that can be paired with the U(1) factor, so H gives nothing class-wide. (The corollary's word "valid on the engine's class" carries the condition that the tool's class contains the product; a tool stated for simple gauge groups only is not bound. The checked file says this in L5 and C6 by "class-wide".)

**Verdict (c) and Corollary PT1: HOLDS AFTER CORRECTION.** Line: checked file L715-718 (Corollary PT1) and L213 (I28, "So it has no seed there"). Correction: (1) take M_1 = Villain U(1) at a fixed beta >= 2^14, and mark the corollary "PROVED GIVEN row 786 Section 1.3 (checked row 794), Lemma COV, Theorem S, Corollary S3', and (TM) with the trace formula for Villain U(1) (not written in the lane); the seed-form link (item 5) is unchecked"; or (2) keep the Wilson weight and mark it "PROVED GIVEN (BRIDGE) for the Wilson cosine, open: (W-score) of row 786". In I28 and in the 6c U(1) row, "So it has no seed there" is not a published theorem; Guth should not be cited for it. With correction (1), L5's trajectory clause also holds: a fixed Villain factor at beta >= 2^14 beside the account's SU(2) trajectory has no seed at any j, so (W) fails along the product sequence (Theorem ZD-c, (W) gives (PHYS-SEED)).

State: step 4 done. Next: step 5, test (d).

## Step 5. Test (d): Proposition KF (c), the clause "first-passage data"

**Source for the clause.** The checked file defines it only by pointing to I22 (L202). The lane's quotation of the account is `library/gap-phys-seed.md` 1.1.1 (L60-66, read in this step), from SA L6844-6869, L6913, L21518-21532: "Wilson SU(2), torus T_l ..., spacing a_K = L^(-K) ... The unit of length is the scale at which the running inverse coupling x_k first enters the window g^(-2) <= x <= g^(-2) + B_sharp; a pair (K, beta) with this property is a first-passage datum (SA L6854-6861)", with g one fixed small number ("for one g' below the ceilings of Theorem 0", L66) and sides l >= l_*(g). I did not re-read the SA lines; this test uses the lane's quotation.

**(d1) Is the clause well defined for a general weight?** No, not as written. A first-passage datum is a pair (K, beta) for the account's action, Wilson SU(2), and x_k is the running inverse coupling of the account's renormalization group for that action. For w_p, K7, U(1), Z_2, Q_8, 2T or a product, the account defines no x_k. So for these models the clause is either undefined, or, read literally ("a first-passage datum of the account"), false because the model is not Wilson SU(2). To be a clause on a class K it needs a stated extension: a running inverse coupling x_k(beta) for each weight of K (for example the same construction carried to that weight). The checked file states none.

**(d2) Can a constant sequence meet it?** Not if the clause says what the account's data say: cutoffs K_j -> infinity, with each (K_j, beta_j) a first-passage datum at the one fixed g. Argument (mine; it needs only the word "first"): for one weight and one bare coupling beta, the sequence k -> x_k(beta) is fixed, so the step at which it **first** enters the window is unique if it exists. A constant sequence beta_j = beta_t therefore has at most one first-passage cutoff K(beta_t), and K_j cannot tend to infinity. This holds for every extension in which x_k at a fixed bare coupling depends only on k. If the clause does not ask for K_j -> infinity (only that each term is a first-passage datum), the constant sequence (K(beta_t), beta_t) repeated meets it, and then KF (c) fails. So the clause must carry "K_j -> infinity" (equivalently a_j -> 0 at fixed g).

**(d3) The proof's stated reason.** KF (c)'s proof says "first-passage data require running couplings that enter a window at arbitrarily small g". That misstates the account: g is fixed and small; what tends to zero along the account's family is the bare coupling at the cutoff (beta_j tends to infinity, F4 of the checked file), and what the argument of (d2) uses is only K_j -> infinity. The conclusion of (c) survives with the reason of (d2).

**(d4) Consequence for the asymmetry that KF1 and 6c draw (needed for test (e)).** Under the literal reading of (d1), the clause is false for **every** model other than Wilson SU(2): for U(1), the free photon, Z_2, Q_8, 2T, w_p and K7 alike. The reasoning of KF (c) ("H(M') is false by that clause, whatever the rest of H says, so M' gives no constraint on the rest of H") then applies to the single-model U(1), free-photon and frozen-group tests as much as to w_p and K7. Under an extension in which x_k is defined for U(1), the U(1) coupling does not run at one loop, so a first entry into the window after K steps with K -> infinity is not available to U(1) either (ARGUED: it depends on the extension, which nobody has stated). **Found again:** row 982 says this in its fact test T1b (`library/gap-hcphys-max.md` L86): "At weak coupling the coupling does not run, so first passage never occurs and the family 'first-passage data' is empty." So a single comparison model does not bind a hypothesis that carries the clause, whichever model it is. What binds such a hypothesis is a model in which the clause can hold: one that contains the account's trajectory as a factor, that is the product device of Lemma PT.

**(d5) The product device works with w_p as the factor (a consequence of Lemma PT and Proposition V; found by this check; not found in the searched scope: lines of `library/gap-*.md` with "product" and one of w_p, K7, first-order, decoupled, "no seed").** Let M_j be the product of the account's Wilson SU(2) at (a_j, beta_j) with w_p at its transition coupling beta_t, held fixed in j (group SU(2) x SU(2)). A hypothesis that reads first-passage data of the Wilson factor is true at M_j exactly when it is true for the account's trajectory. By Lemma PT (d) and Proposition V (corrected to the threshold 1/1650 through Theorem SH (i), `gap-crux-fp-check.md` L92), M_j has no seed at any size for any j, so (W) fails along M_j (Theorem ZD-c). So the w_p weight, used as a decoupled factor, binds kind-(c) hypotheses that read only the Wilson factor, with the same necessary condition as Corollary PT1: read the whole state space. Inputs: (TM-gen) for w_p (unchecked, row 717); van Enter-Shlosman Theorem 2 in the reading of `gap-crux-fp.md` L354 (stated for SU(n), sketched only for U(1) in d = 3); Lemma PT (tests (a), (b)). Compared with the U(1) factor of test (c), it avoids (BRIDGE): Proposition V works on periodic tori directly (through Lemma REG). Mark: PROVED GIVEN those inputs, by the lines above; unchecked.

**The other clauses of Proposition KF, read once.**

- KF (a) HOLDS, with one precision: (W) on the constant sequence gives, through the proof of Theorem ZD-c, S(L_1/(2 a_j); (L_1/a_j)^3; beta_t) <= 1/1650 for large j, a seed at the threshold of Theorem SH. Proposition V as first written excludes only 1/5041; the check of row 716 adds the line through Theorem SH (i) (`gap-crux-fp-check.md` L92). With that line, (a) holds.
- KF (b) HOLDS (the valid form of a test, on a class that contains M').
- KF (d) HOLDS as logic only in the form "H must be false at M'". Its gloss "it must contain a number that separates the weight from w_p" is the reading of `gap-crux-fp.md` L363, not logic: a qualitative property such as "log w is linear in x" (true for p = 1 only) also fails at every w_p with p >= 2. The checked file marks KF "PROVED, a statement of logic"; the gloss should carry the mark of L363 (a reading).

**Verdict (d): HOLDS AFTER CORRECTION.** Line: checked file L732-733 (KF (c)) and L737-738 (its proof). Corrections: (1) state the clause as "the cutoffs K_j tend to infinity and each (K_j, beta_j) is a first-passage datum at one fixed g, for a stated running coupling of the weight"; (2) replace the reason "enter a window at arbitrarily small g" by (d2); (3) add that under the literal reading the clause is false for every non-Wilson model, so the same reasoning exempts kind-(c) hypotheses from the single-model U(1), photon and frozen-group tests too (d4); (4) the w_p weight still binds kind-(c) hypotheses through the product device (d5).

State: step 5 done. Next: step 6, test (e).

## Step 6. Test (e): does Corollary KF1 change any conclusion of row 988 other than the wording of (c) and N2?

**Sources.** Row 988's RESULT line (`FINISH.md` L1067, read in this step); `library/gap-unit-max.md` L231-246 (Route 3) and L357 (N2), read in step 2.

**Row 988's conclusions, one by one, against KF1** (KF1 as written, and as corrected in test (d)):

| Conclusion of row 988 | Changed by KF1? |
|---|---|
| (U1), (U2) not proved; no counterexample | no |
| Seven blind approaches land on existing lane material, except the anchor | no |
| Route 1 fails: no seed below the massless floor (Lemma FLOOR, side times gap above 17.04) | no: a class-wide threshold, binding every blind trigger (6d row 26) |
| Route 2 fails: the beta_t path needs three-dimensional mixing and (NOCRIT) | no |
| Route 3 fails at (b): "no soft exclusion of the gapless branch of Corollary Z4 (K7)" | no. The RESULT line already says "soft". The statement refuted at (b), "light levels on all cubes force the unit action back into the window", has no ultraviolet clause in its hypothesis, so it is of kind (d), and KF (d) leaves its refutation as it was. (Its grade is a separate matter: K7 is a belief, and w_p does not replace it here; see step 7, 6d row 28.) |
| Route 3 (a): the two ends alone give no contradiction | no; it agrees with KF |
| Route 3 (c): "the branch can only be excluded by an input that tells the Wilson trajectory from the endpoint family beyond first passage. None is in the account or in the lane." | **wording, and the second sentence.** For a hypothesis that carries the account's first-passage clause, the account's own data already tell the trajectory from the endpoint family (the endpoint family has no first-passage data: test (d2)). So (c)'s condition is met by data that are in the account, and "None is in the account" is false as worded; the condition constrains nothing for that kind. What is missing for that kind is a selective step (6b of the checked file), which (c) does not name. |
| N2 (L357): "A row on (U1)/(U2) has value only if it brings an input that tells the Wilson trajectory from K7 beyond first passage" | wording, in the same way: read with first-passage data as the input, it admits every such row; the first two sentences of N2 ("do not queue another direction-author row that starts from the object of (U1)/(U2)"; the soft group-blind route is exhausted) are not changed |
| PROVED items: Lemma FLOOR, Identity G, Lemma ORD, the Schwarz form of Route Z | no |
| OPEN list, ending "the one input every route lacks, the exclusion of a gapless scale-invariant branch beyond first passage" | no |
| "Result of the route: ... every exact tool in the lane ... is blind to the difference between the two branches" | no |

**Answer to (e): no.** KF1 changes no conclusion of row 988 other than Route 3 (c) (its wording, and its sentence "None is in the account or in the lane", which is false for the first-passage kind) and the last sentence of N2. Its own sentence "the row's own conclusion (the route FAILS at its step (b)) is not changed" (L743-744) HOLDS.

**But KF1's second sentence needs correction** (from test (d), (d4)-(d5)). KF1 says: "For kind (c) the necessary conditions are those of the theorem-grade tests of 6c: fail for U(1), for the free photon, and for products with a massless factor (Corollary PT1)." Three kinds of hypothesis have to be told apart, by which models can meet the ultraviolet clause:

1. **No ultraviolet clause** (KF (d)). Every no-seed model binds: the constant w_p sequence, K7 (belief), U(1), the free photon, frozen groups (for T_per).
2. **A clause that only reads the bare couplings** (for example "beta_j tends to infinity"). The constant w_p sequence fails it, so w_p does not bind. U(1) does: the Villain U(1) sequence with beta_j -> infinity meets the clause and has no seed at any beta >= 2^14 (test (c), given its inputs), so (W) fails along it. For this kind, KF1's asymmetry (U(1) binds, w_p does not) is right.
3. **The account's first-passage clause** (cutoffs K_j -> infinity with (K_j, beta_j) first-passage data at one fixed g). Under the literal reading no single non-Wilson model meets it, U(1) and the free photon included (d4); under an extension the U(1) coupling does not run at one loop, so U(1) cannot meet it either (ARGUED; row 982 T1b, `gap-hcphys-max.md` L86, says the same). So for this kind U(1) and the free photon, as single models, give no constraint, by the same reasoning as KF (c). What binds this kind is the product device with **any** factor that has no seed: Villain U(1) at beta >= 2^14 (test (c)), w_p at beta_t (d5), frozen groups for T_per. They all impose the same condition: read the whole state space. The forms D2 and SHEET bind too, because they are statements about a form of hypothesis, not models.

Corrected KF1, proposed wording: "Route 3 (c) holds for hypotheses with no ultraviolet clause. For hypotheses that carry the account's first-passage clause, no single comparison model binds, U(1) and the free photon included; they are bound by the product device with any factor that has no seed (U(1) Villain at beta >= 2^14, w_p at beta_t, frozen groups for T_per), which forces them to read the whole state space, and by Theorem D2 and Lemma SHEET. For hypotheses that read only bare couplings, U(1) binds and the constant w_p sequence does not."

This bears on work item W2 of the checked file (the proposed lead rule lists "compact U(1), the free photon, a product with a massless factor, Theorem D2 and Lemma SHEET" as the tests of (K-flow)): for the first-passage kind, U(1) and the free photon should be replaced by "products with any no-seed factor".

State: step 6 done. Next: step 7, items (iii), (iv), (v).

## Step 7. Items (iii), (iv), (v)

Sources read in this step: the RESULT lines of rows 976, 982, 984, 995, 996, 884 (`FINISH.md`); `library/gap-hcphys-max.md` L86-89 (fact tests T1b-T4 of row 982) and L264-272 (its notes N1-N5); `library/gap-flux-exercise.md` L143 ((G_ev)) and L167 (C6); `library/gap-mid-max.md` L209-215 (5.2); `library/gap-ladder-max.md` L148-151; `library/gap-crux-exercise2-max.md` L413 (6a row 18); `library/gap-form-exercise.md` L143-145; `library/gap-mid-check.md` L64; `library/gap-crux-exercise2-check-astra.md` L1-2, L227-259, L350-353.

### (iii) The rows of the 6c table (checked file L540, L542-544)

**"Product with a massless factor" (L540): HOLDS AFTER CORRECTION.**
- "device of row 708": right (`gap-mid-max.md` L226-229, Wilson SU(2) x Ising); "the product algebra is checked (row 709)": right (`gap-mid-check.md` L64). Lemma PT carries it to two gauge factors with the gauge projection (test (a)).
- "T_fix, T_per, T_W (PROVED given the U(1) theorem)": the "U(1) theorem" is not a published theorem in the form needed (test (c)). With a Villain U(1) factor at a fixed beta >= 2^14 it is PROVED GIVEN row 786 Section 1.3 (checked row 794), Lemma COV, Theorem S, Corollary S3', (TM) and the trace formula for Villain U(1); with the Wilson cosine it is PROVED GIVEN (BRIDGE), open.
- "THM given the U(1) theorem and a strong-coupling seed (I27, I28)": the strong-coupling seed is not needed for "the product has no seed"; it serves only L5's picture in which the SU(2) factor has a seed. Mark as in the previous bullet.
- "ARGUED only: ... 'a decrease of D or S under doubling persists'": correctly marked ARGUED (L5 says the two factors were not constructed).
- "Binds from: as the U(1) test": better than that. The U(1) factor can be held at one fixed coupling (beta >= 2^14, Villain) while the other factor runs, so the product binds at every coupling of the other factor, on a trajectory too. And by test (d5) the factor can be any model with no seed (w_p at beta_t, given (TM-gen) and van Enter-Shlosman), so the row is "product with a factor that has no seed", the massless case being one instance.

**"w_p at its transition coupling (Proposition V)" (L543): HOLDS AFTER CORRECTION.**
- "THM, published (van Enter and Shlosman), cited; Proposition V proved in the lane given it": the check of row 716 marks Proposition V "PROVED GIVEN" van Enter-Shlosman Theorem 2 in a reading (stated for SU(n), proof sketched only for U(1) in d = 3) and (TM-gen) (unchecked, row 717), with the threshold corrected to 1/1650 through Theorem SH (i) (`gap-crux-fp-check.md` L92-94, L173, L182). "THM, published" overstates the SU(2), d = 4 case: the printed proof is not for it (`gap-crux-fp.md` L354).
- "What a tool must use: a number ..., or first-passage data": "a number" is the reading of `gap-crux-fp.md` L363, not logic (test (d), KF (d)); "or first-passage data" is right, and so is any ultraviolet clause that a constant sequence cannot meet (test (e), kind 2).
- "It does not test T_W-tools that read first-passage data (C3)": right for the constant sequence as a model; wrong for the weight as a test resource, because as a decoupled factor beside the account's trajectory it binds such tools (test (d5)).
- A limit of the row, not stated in it: Proposition V gives "no seed at any size" at beta_t. By Theorem ZD (D) that is "D unbounded, or branch G". It does not place w_p at beta_t in branch G. So w_p tests statements whose conclusion is the seed; it does not test statements about branch G ("light levels on all cubes ...") unless D is shown bounded at beta_t, which nobody has done. This matters for 6d row 28 below.

**"K7 line" (L544): HOLDS.** BELIEF (numerics), as marked; row 995's correction (coexistence supported only for beta_A about 1.3 to 1.5; the 1981 end point is not a bulk end point, Gavai 1996) is quoted correctly. "as w_p ... the belief-grade form of the w_p test": right for statements whose conclusion is the seed; the same two remarks as for w_p apply (first-passage tools: not bound as a single model, bound as a factor).

**"Frozen Q_8, 2T" (L542, corrected in 8.5): HOLDS.** Against check 884 (`gap-crux-exercise2-check-astra.md` L227-259, L352): the frozen limiting transfer operator has at least two centre-even flat states at every box, so the even sum is at least one (L259); the fixed-beta question for every box is "not settled" (L352). T_ev here is (G_ev) of row 731 (`gap-flux-exercise.md` L143), which includes "S_ev(n_i; L_i^3) -> 0", so it fails in the frozen limit as the row says. Two precisions: (1) the check also proves a finite-coupling form, box by box: S_ev(t; B) >= 1/2 once beta >= (1/d_G) log(16 E (g - 1) t) ((FG2), L250-254), with no machine step; it is not a statement at one fixed coupling for every box; (2) "for T_ev: the non-abelian flat states" names the obstruction, not a property of SU(2) that a tool could use; that is all the check supports.

### (iv) 6d rows 24, 28, 30, 33 and the last two rows (checked file L577, L581, L583, L585-587)

**Row 24 (L577): HOLDS AFTER CORRECTION.** T3 is ARGUED in row 982 (its RESULT line: "ARGUED: the port fed into Theorem BR is short by beta_K/beta_0 ... (fact test T3 fails)") and row 984 lists it as not checked ("Still OPEN: ... T3 and the roughness exponent (ARGUED, not checked here)"). Both right. Correction: "A lead rule rests on it" should be "rests in part on it". Row 982's N2 (`gap-hcphys-max.md` L266) gives two reasons: "it is short by beta_K/beta_0 (T3) and has no input at the unit (T2)". T2 is the w_p fact test at L87 ("The port alone FAILS it, as it must"). It is a one-scale argument, so it is of kind (d) in the sense of Proposition KF and is not touched by KF (c). So if T3 fell, N2's claim about a cutoff-uniform rate would lose its support, and its claim that the port alone supplies no input at the unit would stand.

**Row 28 (L581): HOLDS AFTER CORRECTION.**
- "(c) does not follow: first-passage data already tell the trajectory from K7": HOLDS (test (e)).
- "(b) is valid: K7 (better: w_p) refutes soft class-wide statements": the K7 half holds as BELIEF. **"(better: w_p)" FAILS for Route 3 (b) as written.** Route 3 (b)'s statement is "light levels on all cubes force the unit action back into the window" (`gap-unit-max.md` L238-240), made under (BDD-Delta) (L233). A model refutes it only if it has light levels on all cubes. w_p at beta_t has no seed (Proposition V), which by Theorem ZD (D) is "D unbounded, or branch G"; to place it in branch G one needs D bounded at beta_t, which is not proved. So for Route 3 (b) the only test on record is K7's end point, a belief that row 995 doubts. Row 988's third failure is therefore belief-grade, and Proposition V cannot be cited in its place without (BDD-Delta) at beta_t. (The same remark limits 6c point 3, "A row that discards on K7 should cite Proposition V": that holds for discards whose test statement ends in the seed, not for statements about branch G.)
- "The valid necessary conditions are points 1 and 2 of 6c": for hypotheses with the account's first-passage clause, point 2 must be corrected as in test (e): U(1) and the free photon, as single models, do not bind them; products with any factor that has no seed do, together with D2 and SHEET.
- "The (K-flow) kind comes back as admissible. No instance exists": HOLDS as a reading.

**Row 30 (L583): HOLDS.** 6a row 30 concerns one-plaquette separating properties; row 996's result is "every one-plaquette property I wrote blind was FOUND in rows 670-995 or has no consumer", and row 995's Turan property has "no consumer". "Valid in range: it covers (K-one) candidates only" is a fair reading: neither row searched statements along scales. (Row 996 also names three path statements ((ZF), (VIR_K), the plaquette shift) as the separating inputs a lane tool can use; these are not one-scale properties, which agrees with the row.)

**Row 33 (L585): HOLDS.** Row 976's RESULT: verdict TRANSIENT, REFUTE excluded, "Weak by construction (u_xy is a hilltop, left in one step classically, Step 3b); OPEN: escape from metastable sets of the relaxed slice". So "not tested", not "fails", is the right verdict on (ESC); the run was GUIDE in any case.

**Row "ex2 #18" (L586): HOLDS.** Exercise 2's 6a row 18 (`gap-crux-exercise2-max.md` L413): "group-blind: they confine 4D U(1) too". Ito and Seiler's Theorem 2.1, as quoted in `gap-form-exercise.md` L143: under the Migdal-Kadanoff recursion, "for D <= 4 and for G = SU(N) or G = U(N)", all non-trivial character coefficients tend to 0. The citation is through the lane's quotation; I did not read Ito-Seiler.

**Row "ex2 6c point 1" (L587): HOLDS.** Matches check 884 (RESULT line: "FAILS: ... the argument exempting Q_8 and 2T from every (ES) test"; L352: "local gappedness does not supply ES. The fixed-beta existential ES question for those groups is not settled here"), and "It holds for Z_2" matches L231 ("Z2 does not have these additional holonomies after its whole centre has been projected out"). The checker is Codex astra xhigh (row 884 RESULT), as the checked file says.

### (v) The two corrections of 8.5 (checked file L799-815)

**Correction 1 (Proposition CT is (CAS) of row 708): HOLDS, with one precision.** The quotation of (CAS) is exact (`gap-mid-max.md` L64); its verdict is at L67 ("It holds in every model of the class that has the seed after finitely many doublings ... it restates the seed in steps") and L209-215 ("So (CAS) has the same strength as the seed ... Its exact form in the coupling is (NOCRIT)"); the extensive base is `gap-ladder-max.md` L150 ("Where (TH) comes from (PROVED implication)"). Precision: (CONTR)_theta and (CAS) are the same idea, not the same statement. (CONTR)_theta is a continuum statement on the dyadic chain P with D^+ (an upper limit over the cutoffs), a base L_0 with bound B and no cap; (CAS) is a lattice statement at one coupling, over every a >= 3, with a cap M. "Found again" is right; "(CONTR)_theta is (CAS)" should read "(CONTR)_theta is the continuum dyadic form of (CAS)".
The ARGUED remark ("(CAS) gives the seed; the converse is not proved") HOLDS. My derivation: in a model with a seed, D(a) < 6.1 x 10^(-4) for all large a (Lemma Z3), so only finitely many a have 6.1 x 10^(-4) < D(a) <= M. (CAS) holds there, with some theta < 1, if and only if no such a has D(2a) >= D(a). Raising M only adds more a, and M >= D(3) is required, so a single rise at some a with D(a) <= D(3) defeats every choice of theta < 1. Class-wide the lane proves only D(2a) <= 16 D(a) (restate L43, applied in four directions). So row 708's "It holds in every model of the class that has the seed" (L67) and "same strength" (L215) are not proved. Neither the author nor I know a model that separates the two.

**Correction 2 (the finite-group narrowing struck in part): HOLDS.** It agrees with check 884 as quoted under row "ex2 6c point 1" above. Precision: the check gives also the finite-coupling, box-by-box form (FG2), which the correction does not mention, and the correction's "in the frozen limit" is the right scope.

State: step 7 done. Next: step 8, verdicts and RESULT.
