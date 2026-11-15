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
