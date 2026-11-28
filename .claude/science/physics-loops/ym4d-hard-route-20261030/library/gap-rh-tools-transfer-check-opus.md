lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-25T04:26Z

# Row 1487: cross-model check of row 1481 (RH tools transfer) and twin comparison with row 1482

Started 2026-11-24T16:26Z (date -u) on Mac mini worker 2, at commit e2f16e6ce, branch claude/ym4d-hard-route. Checker: Claude Opus 5.5, high effort. Row 1481 author: Claude Fable 5.2 high. Row 1482 author: gpt-6.2-astra max. A different model from row 1481's author, but this check reads the same files, so it is a cross-model check of reasoning, not an independent derivation; where I re-derive a statement by a different argument I say so.

Credit: Levent Alpoge (with Claude) for the RH proof; Michael Rubinstein for the explainer (with Claude, Codex, Gemini); Sussman-Alpoge (with Claude and Codex) for the complete account and the Lean continuum limit.

## Plan

1. Lemma PRG and its consequence in row 1481: reordering step, real analyticity of log Z^z, log Z_+, P_K on the real axis of a finite torus, the recalled theorem of item (ii), open case (iii).
2. Each 'on file' match, by reading the cited lines: T2 vs Theorem ZB, Theorem V, Theorem SC, Proposition B (rows 677-683); T6 (a) vs Proposition PER (row 1303); T5 vs Lemma TW and Theorem K2 (row 1468); T8 (ii) vs rows 1461 and 1465. Exact or likeness.
3. The reversed direction in T6 (a).
4. Then row 1482's output: every tool or candidate it names that row 1481 lacks; test each (transfer, first failing line or on-file match, filter t1-t6).
5. Verdict: HOLDS / HOLDS AFTER CORRECTION / FAILS; closure of the direction (with or without trigger R7) or a surviving candidate.

## Repo search (rule 0a)

`grep -i -E "pringsheim|vivanti"` on `library/open-core.md`, `FINISH.md` and `library/*.md` at e2f16e6ce: the only hit is row 1481's own file. So Lemma PRG is not on file elsewhere, as row 1481 says. Other greps are given at the step that uses them. Memory: `memory_pressure` reports 37 percent free at 16:30Z, which is below the 50 percent rule, so no numeric job is started. None is needed, because every step below is a hand check.

## Step 1. Lemma PRG and its consequence (done 16:27Z by date -u)

Source checked: `library/gap-rh-tools-transfer-fable.md` lines 128-142. The definitions it uses are in `library/gap-k2-tool-design-fable.md` lines 99-124: Z^z(v) is the Wilson partition function on the torus n^3 x v with temporal twist z, and the twist multiplies some links by -1.

**1.1 Lemma PRG (lines 130-132). Verdict: CORRECT, with one step written too briefly.** Re-derived here.

- Reduction to c_k >= 0 for all k: correct. Subtracting a polynomial changes neither R nor analyticity at R.
- "So the Taylor series of h at R/2 has radius rho > R/2." This is true, but the file skips the step that proves it. Repair (proved here): let Omega = {abs(beta) < R} union N, where N is an open disc about R on which h has its extension. N intersected with the disc of radius R is an intersection of two convex sets, so it is connected. The extension therefore agrees with the series on all of that intersection, and h is a single analytic function on Omega. The closed disc abs(beta - R/2) <= R/2 is compact and lies in Omega: it meets abs(beta) = R only at beta = R, and R is in N. So some epsilon-neighbourhood of it lies in Omega too, and Cauchy's theorem gives rho >= R/2 + epsilon.
- The coefficients at R/2 are h^(j)(R/2)/j! = sum_{k>=j} binom(k,j) c_k (R/2)^(k-j). This is termwise differentiation inside the disc of convergence, and each coefficient is >= 0: correct.
- Reordering: for R < x < R/2 + rho, the double series sum_j sum_k binom(k,j) c_k (R/2)^(k-j) (x - R/2)^j has non-negative terms and a finite iterated sum. By Tonelli's theorem for series it can be summed over k first. That gives sum_k c_k x^k < infinity with x > R, which contradicts the radius: correct.
- The second claim (applied to -h) and the "infinitely often" form are the contrapositive: correct.
- This is the Vivanti-Pringsheim theorem, as the file says. With the compactness line added, the proof is complete.

**1.2 Item (i) (line 136). Verdict: CORRECT; the identification step is left implicit.** If h is real-analytic on an open real set containing [0, infinity), its Taylor series at 0 has radius R > 0. If R were finite, the series and h would agree on (0, R) by the identity theorem on the interval. The local complex extension of h at the point R would then agree with the series on the connected set N intersected with {abs(beta) < R}, so the hypothesis of PRG holds. Hence coefficients that are eventually of one sign force R = infinity. "h is entire" means the series defines an entire function that equals h on [0, infinity): correct.

Real analyticity of the three quantities. Z^z(v; beta) is the integral, over a compact field space with Haar measure on one period, of exp(beta S_z), where S_z (a sum of plaquette terms, with signs flipped by the twist) is bounded and continuous. So Z^z is entire in beta and strictly positive for every real beta, negative beta included. The same holds for Z_+ = (1/8) sum_z Z^z. So log Z^z, log Z_+ and P_K = Z_+(2u)/Z_+(u)^2 are real-analytic on all of R, not just on [0, infinity): **CONFIRMED.**

**1.3 Item (ii) (line 138). Verdict: CORRECT given the recalled theorem. Two wording repairs.**

- Order: abs(Z(beta)) <= Z(0) exp(abs(beta) max abs(S)). So Z is of exponential type, and its order is at most 1. Correct.
- Recalled theorem. Hadamard's factorisation says an entire function of finite order rho with no zeros is e^g with g a polynomial of degree at most rho. This is standard and stated correctly. A second route, recalled and not rebuilt: if Z has no zeros, then g = log Z is entire, Re g(beta) <= C abs(beta) + const, and the Borel-Carathéodory inequality forces g to be a polynomial of degree at most 1. The row does not consume this lemma on the T0 chain, because it is a closed-door remark. So by the GOAL rule it needs no rebuild in `library/` unless the chain later uses it.
- Repair (wording). "Z(0) = 1" holds only when Haar measure is normalised and the action is tr U/2, with no constant subtracted. In general Z(0) = c > 0, and then Z = c e^(b beta). The conclusion (log Z)'' = 0 is unchanged.
- Variance: (log Z)''(beta) is the variance of S_z under the tilted law, and that law is equivalent to Haar measure. S_z is continuous and not constant, so the variance is strictly positive. For Z_+, the tilted law is the mixture (1/8) sum_z of the laws of S_z, which is not a point mass. Correct.
- Repair (one missing line). "Z has a zero, so log Z is not entire" needs this sentence: if the real-analytic function log Z continued to an entire function g, then e^g would be entire and equal to Z on R, hence equal to Z everywhere, so Z would have no zero. With that line, (i) gives sign changes infinitely often for log Z^z and log Z_+. **CONFIRMED.**

**1.4 Item (iii) (line 140). Verdict: the statement of the open case is CORRECT; it is still open here; and it does not bear on the verdict.** P_K is meromorphic as a ratio of entire functions. It is entire exactly when every zero of Z_+(u; .) of order m is a zero of Z_+(2u; .) of order at least 2m: correct. I did not decide this either. An attempt through indicator diagrams fails. Z_+(u)^2 and Z_+(2u) have the same conjugate indicator interval [2 m_u, 2 M_u], because the extremes of the action are extensive (m_u and M_u are the minimum and maximum of the action on the u-torus). So growth does not exclude an entire quotient. **Why it does not matter (proved here):** suppose the coefficients of P_K were eventually of one sign. By (i), P_K would then be entire. An entire P_K is a statement about complex couplings. It gives no lower bound P_K >= 457/625 at a real beta_K, and it gives no zero-free disc for Z_+, which is the input that Theorem ZB lacks. Transfer statement 2 needed that zero-free disc, and (ii) has already closed it for log Z_+. So (iii) can be left open without changing Outcome (B).

**1.5 Item (iv) (line 142). Verdict: the first sentence is CORRECT (the Pringsheim direction); the closing sentence OVERREACHES.** "Eventual positivity with a finite radius needs a singularity at the real point R": correct, by PRG. "So where the hypothesis can hold with a finite radius, the model is one that the filter must reject" assumes that 4D SU(2) Wilson has no real singularity of the infinite-volume free energy at positive beta. That absence of a bulk transition is believed but not proved. Repair: mark the closing sentence GUESSED (it rests on the unproved absence of a bulk transition in 4D SU(2)), not "recalled". The outcome does not use it.

**Step 1 result.** Lemma PRG HOLDS AFTER CORRECTION: add the compactness line for rho > R/2. Item (i) holds. Item (ii) holds given Hadamard's theorem (recalled, standard), after two wording repairs: Z(0) = c > 0 in general, and the missing line "Z has a zero, so log Z is not entire". Item (iii) is correctly stated as open and is irrelevant to the outcome. Item (iv) holds in its first sentence; its last sentence is GUESSED, not recalled.

## Step 2. The 'on file' matches, by reading the cited lines

### 2.1 T2 (row 1481 line 148) against Theorem ZB, Theorem SC, Theorem V, Proposition B (written 16:28Z by date -u)

Lines read: `library/gap-skeleton-max-b.md` 448-478 (Theorem ZB with its proof, Corollary 5', the crux (ZF_B)); `library/gap-skeleton-final.md` 100-115 (nodes Z0-Z11); FINISH row 683 RESULT (Theorem SC); FINISH row 677 RESULT and `library/gap-zf-box-x.md` 155, 186-207 (Theorem A, Proposition B, status block); `library/gap-zf-box-s.md` 16, 125, 171-188 (Theorem V); FINISH rows 1004 and 1402 (Lemma LYP; the Lee-Yang class).

The claims and what the cited lines say:

| Row 1481 says | Cited lines say | Match |
|---|---|---|
| g_q = log Z(k,B) - (1/q) log Z(qk,B) "vanishes at beta = 0 to order 4k" | Row 683 part (1): cumulants of order below 4k on time length qk are q times those on length k, so "the difference vanishes to order 4k at beta = 0"; Theorem SC: abs(g_q) <= (abs(B) k/100)(12800 abs(beta))^(4k) on abs(beta) < 1/12800 | **exact** |
| "it is bounded by C_0 abs(B) k on a zero-free domain D" | Theorem ZB proof: on the boundary of {d > 1/k} in D the bound is M_k = 24 k abs(B)(r_0 + X)(1 + 4Hk/theta), from positivity on the real axis and Borel-Carathéodory; C_0 abs(B) k exp(-kappa_0 k) is the bound on the strong-coupling circle only | **wording error, harmless.** Repair: "bounded by M_k, linear in abs(B) and polynomial in k, on D, and by C_0 abs(B) k exp(-kappa_0 k) on the strong-coupling circle". The two-constants step (Theorem LP) uses both, and the k-th root makes the polynomial factor in k irrelevant. |
| "the two-constants theorem then gives m_B >= kappa_0 omega_D(beta), uniformly in the box" | Theorem ZB statement and proof (lines 460-463) | **exact** |
| Theorem V needs dominance instead of zero-freeness | `gap-zf-box-s.md` 125 item (2), 178, 188: Theorem V gives the same bound from (DOM_B) on D', with no (TUBE) and no limit in k; checked by row 696 (`gap-skeleton-final.md` Z4) | **exact** |
| no zero-free neighbourhood of a real coupling above about 0.102 is proved (`gap-zf-box-x.md` line 201) | line 201, the status block: "Any zero-free neighbourhood of a real coupling above x_D (about 0.102 ...)" listed as open | **exact** (and Theorem A gives the tube abs(Re beta) <= 1/10, abs(Im beta) <= 10^-7) |
| Proposition B: a zero-free radius that shrinks with the gap cannot cross a region | line 195: under (H_p) the continuation ends at x_0 + c kappa_1^p/(2 Lambda p); line 207: "no hypothesis in which the zero-free radius shrinks with the gap can cross a region" | **exact** |
| Class C4 of row 1402 (zero-freeness in the couplings), closed as not selective in half-plane form (rows 1004 Lemma LYP, 1190, 1196) | Row 1402 lists "Lee-Yang zero-freeness" among its nine classes of crossing; row 1004 RESULT has Lemma LYP: the Lee-Yang crux (LY) of route B9 is false for one plaquette at every beta > 0, for Z_2, U(1) and SU(2), with Lemma LYP2 for every finite lattice at small beta. I did not find the label "C4" itself in row 1402's text (grep of the row for "C4" returns no class label), and I did not open rows 1190 and 1196 | **match in substance; the label C4 is not verified** |

What is exact and what is only a likeness. The transfer statement as row 1481 writes it (function-field form) **is** Theorem ZB with Theorem SC, after the M_k repair. That is an exact match, so this transfer adds nothing. The further sentence "the lane already ran Stepanov's method, with the strong-coupling point as the one prime" is a **likeness only**. In the RH tool the second inequality comes from the product formula: a non-zero algebraic integer has norm at least 1, and that lower bound is free. In Theorem ZB it comes from a maximum-modulus or two-constants bound, and that needs an upper bound M_k on a domain, which is the zero-free hypothesis (ZF_B). So the analogy maps "product formula" to "harmonic measure on a zero-free domain", and the zero-free domain is exactly what is missing. The likeness supports the verdict (the transfer stops at the known wall, Z6), and the verdict does not rest on it.

Verdict for T2's "on file" claim: **HOLDS AFTER CORRECTION**. Replace "C_0 abs(B) k on a zero-free domain" by M_k (repair above), and mark "C4" as a label not found, citing the Lee-Yang class of row 1402 and Lemma LYP of row 1004 instead. The arithmetic half ("no object", explainer lines 581-588) is checked in Step 2.5 below, against the source.


### 2.2 T6 (a) (row 1481 line 176) against Proposition PER of row 1303 (written 16:29Z by date -u)

Lines read: `library/gap-positivity-fable.md` 41-79 (the dictionary, readings R1 and R2) and 354-397 (Proposition PER, its proof, the reading, table 4.2).

- "P_K = Tr(A^2)/(Tr A)^2 with A = P_0 T^u": **exact**, re-derived here. P_0 is a projector that commutes with T, so (P_0 T^u)^2 = P_0 T^(2u). Hence Tr A^2 = Z_+(2u) and Tr A = Z_+(u).
- "is one over the effective rank": **exact.** (Tr A)^2/Tr A^2 is the participation ratio of the spectrum of A.
- "On file (Proposition PER of row 1303)": **exact, and closer than row 1481 says.** PER defines delta_u = (p_u^2 - p_(2u))/p_(2u). With p_k the neutral periods Z_+(k) (PER is stated for any positive trace-class T with a simple top eigenvalue, and the dictionary at line 63 of row 1303 makes p_k the neutral partition function), this gives **P_K = 1/(1 + delta_u)** identically. So the seed P_K >= 457/625 is the same as delta_u <= 168/457. PER (a) brackets s by delta_u, and PER (d) says that no inequality following from positivity of the spectral measure gives an upper bound on delta_u. These are the same facts as Fact PUR and the "wrong direction" of row 1481. Repair (wording only, adds a citation): row 1481 should state the identity P_K = 1/(1 + delta_u), so that the match with PER is visibly exact rather than a likeness.
- "the rank-one test of rows 1373, 1461": not opened by me; not needed for the verdict.

Verdict: **HOLDS** (match exact).

## Step 3. The reversed direction in T6 (a) (written 16:29Z by date -u)

Source lines read: explainer `zeta-paper_v2.tex` 1915-1930 (the rank bound and the Lemma with hypothesis (D:104)).

The tool, as read. Cauchy-Schwarz on the non-zero eigenvalues of Q >= 0 gives rank Q >= (tr Q)^2/tr(Q^2) (line 1916). The Lemma assumes **tr(Q^2) <= (1 + eta)(tr Q)^2/D** (display D:104, line 1924) and concludes that the codimension of the span of the images is at most (2 eta + 4 alpha + 4 sqrt e) D (D:105). So: an **upper** bound on the normalised second moment (purity at most (1 + eta)/D) gives a nearly **full** rank.

The crux, re-derived here by a different route from row 1481 (eigenvalues, not traces). With A = P_0 T^u >= 0 and eigenvalue ratios r_i in [0, 1]:

- The only lower bound on purity that positivity gives in general is P(A) >= 1/rank A, which is the same Cauchy-Schwarz read backwards. A has infinite rank (its kernel is strictly positive), so this bound is 0.
- The sharp form is P_K = (1 + sum r_i^(2u))/(1 + s)^2 >= 1/(1 + s)^2. So P_K >= 457/625 follows from s <= 25/sqrt(457) - 1 = 0.1695. In the other direction, Fact PUR gives s <= 4/21 = 0.190 from P_K >= 457/625. Either way, a lower bound on purity is an upper bound on s, which is the seed.
- The upper bound P(A) <= 1, that is Tr A^2 <= (Tr A)^2, is the "trivial inequality the other way": it bounds purity from above, and the crux needs a bound from below. **Confirmed.**

Could the RH lemma be used in its contrapositive? It gives: purity above (1 + eta)/D implies that the images miss a fixed fraction of H. In the crux that would read "the neutral states reached by A miss most of the space". That is a statement about rank, and A has full rank in the neutral sector, so the contrapositive yields nothing. **No reversed use exists.**

What the RH proof does to get its upper bound: an exact second-moment identity from a relative trace formula. For the twisted family, the Lemma T3 model (line 7130 onward) has "sum over chi of B_chi^dagger B_chi = abs(A) m" plus coincidences N° >= 0, and the coincidences enter with a + sign. So that identity, too, only produces upper bounds on the second moment. The direction of T6 (a) is therefore reversed at its source, not just at the Lemma.

Verdict on Step 3: **HOLDS.** First failing line: row 1481 cites line 1923; the hypothesis display is D:104 at line 1924 (an off-by-one, harmless).


### 2.3 T5 (row 1481 line 168) against Lemma TW and Theorem K2 (row 1468) (written 16:30Z by date -u)

Lines read: `library/gap-k2-tool-design-fable.md` 126-210 (Q2, Lemma TW with its proof and Remarks (i)-(iii), Theorem K2 and what it does not give) and 401-420 (obstructions, (O-d)); FINISH row 1469 RESULT (the check: "Lemma TW holds (sixteen masses carried); the release's adapted contours and base sets admit the hand port of Remark (ii)").

- "Every probability kernel carries the sixteen masses, whatever its strength, contours and base choices": **an overstatement; corrected here.** Fubini makes any probability kernel preserve total mass. A kernel carries the **twisted** masses Z^z only if it is compatible with the twist, K(C_z W, C'_z V) = K(W, V), so that it maps densities on F^z(n, v) to densities on F^z(n/2, v/2). Lemma TW proves this for Q2 at every strength kappa, but only for corner bases with the slab of C_z on a block boundary (Remark (i)). For the release's kernel it holds when contours stay in the two cells of their bond and the slab is placed on a cell boundary (Remark (ii), SKETCHED in row 1468; ported by check 1469). Repair: "every probability kernel compatible with the centre twist (Lemma TW for Q2 at every strength; Remark (ii) with check 1469 for the release's kernel) carries the sixteen masses". With that wording the match is **exact**.
- Group-blind, so not a mechanism by (t6): **exact.** (O-d) (line 414) says "Lemma TW and Lemma LD-1 hold for every group and every dimension", and the filter table line 322 says (t6) Villain U(1) is not separated by them.
- Row 1438 (check 1440), "an invertible slice factor leaves the neutral spectrum unchanged": not opened by me; the verdict does not need it.
- The identification with the RH tool (the seesaw: the final period does not depend on the twists of the intermediate lifts) is a **likeness.** In the RH proof the freedom is used. One chooses, prime by prime, the twist that makes the lattice integral there, and the gain is the integrality that the choice buys. In the crux the freedom buys nothing: no choice of kernel changes a mass, and no property (integrality, sign) is selected by the choice. Row 1481 says the same thing in other words ("not a mechanism").

Verdict: **HOLDS AFTER CORRECTION** (the twist-compatibility repair). The "no object" half (explainer line 1904) is confirmed in 2.5.

### 2.4 T8 (ii) (row 1481 line 192) against rows 1461 and 1465 (written 16:30Z by date -u)

Lines read: FINISH row 1461 RESULT and row 1465 RESULT.

- Row 1461 proves (L1): **every** infinite set E of least-root depths gives, after a subsequence, a calibrated continuum limit. It reduces the gap to the averaged inequality (4), or its exact form (6), over a compact interval I of calibration levels, and leaves (4)/(6) open. Row 1465 Step 7 says (6) "adds nothing a proof could use unless a proof naturally gives level-averaged purity bounds (none on file)". Row 1481's quote is **exact.**
- Row 1481's transfer statement, "the seed holds for most members of an auxiliary family, by a second moment", is **a likeness of row 1461, not identical to it.** Row 1461 averages over calibration levels and uses no second moment. The RH mechanism is a mean square: the average over q of abs(S)^2 is small because the off-diagonal terms cancel ("as q varies, the symbols (n/q), n <= Z, behave like independent signs", explainer line 2405, read and confirmed). An analogue in the crux would need an orthogonality between levels, cutoffs or twists. No such relation is on file, and I see none: 1 - P_K is non-negative at every level, so there is nothing to cancel, and averaging a non-negative quantity gives no gain over its supremum on a positive-measure set. So the method fails at the line row 1481 names, and that failure is confirmed. The verdict "empty frame" HOLDS, and its first failing line is right.

Verdict: **HOLDS** (the match to rows 1461 and 1465 is exact on the consumer side; the identification with the mean square is a likeness, and it fails at line 2405 as stated).

### 2.5 The 'no object' and first-failing lines, against the explainer (written 16:30Z by date -u)

Read at `~/ym4d-papers/alpoge-rh/zeta-paper_v2.tex`:

| Row 1481 cites | Source | Verdict |
|---|---|---|
| 581-588 (T2, product formula) | lines 581-588: "If such a number beta is a nonzero algebraic integer divisible by p^e ... the average of log abs(sigma(beta))^2 ... is at least 2e log p. This is the product formula." | exact |
| 428 (T3, height two) | the quoted sentence is at lines 430-431 ("multiplication by p on the formal group looks like X -> X^(p^2) modulo p") | off by two lines; harmless |
| 1030 (T7) | line 1030: "The terms x/m and m are balanced when m is about sqrt x" | exact |
| 1904 (T5) | line 1904: "the relevant finite group consists of first Galois cohomology classes over E with values in Q_l/Z_l(-a)" | exact |
| 1923 (T6 (a)) | the hypothesis display D:104 is at line 1924 | off by one; harmless |
| 2405 (T8 (ii)) | line 2405: "the symbols (n/q), n <= Z, behave like independent signs" | exact |
| 7134 (T6 (b)) | line 7134: "the family of twists must be large compared with the number of representations" | exact |
| 780 (T9) | line 780: "asserted for x >= x_0(eps)" | exact |
| 1085, 1102 (T10) | lines 1085-1087 (steps 4, 6, "an earlier form of our first step") and 1102 (step 3, "A step largely absent from the final proof") | exact |

**T7 (row 1481 line 186), one refinement (not a defect in the verdict).** Row 1481 says the step count "is fixed by the drift". In Theorem K2, however, N is a free integer (l = 512 * 2^N * v_E), and check 1469 lists "use of drift in step counts" among its repairs. The estimate (x_0 - 2.3)/0.2575 is a GUIDE (one-loop drift). A sharper first failing reason: in the RH proof the errors made once at the ends are **divided by B, which grows with m** (the m-fold multiplicity of the divisibility, explainer lines 1028-1030 and row 1481 2.6). The chain of Theorem K2 has no quantity that is divided by the number of steps. Its only multiplicity is in the time direction, s(mu) <= s(u)^m (PER (c)), and that multiplicity needs the seed s(u) < 1 first. So T7 fails whether or not N is free. Repair: replace "the number of steps is not free" by "no end error is divided by the number of steps; the only multiplicity, PER (c), presupposes the seed".


## Step 4. Twin comparison: what row 1482 names that row 1481 lacks (written 16:32Z by date -u)

Read only after Steps 1-3 were on disk: `library/gap-rh-tools-transfer-astra62.md` (152 lines, in full). Explainer lines re-read for the new items: 1116-1131 (the Dirichlet extension), 1502-1522 ((M) and its amortisation), 12347-12371 (Theorem Le18 and its proof).

Both twins reach **Outcome (B)**. Each item of row 1482 that row 1481 lacks is tested below in the same way: the transfer stated, then its first failing line or on-file match, then the filter.

**N1. The local arithmetic test (Le18 against the Wilson one-bond normalizer). New relative to row 1481, which said only "no object". HOLDS (re-derived here by a second route); scope repaired.**
- Re-derivation. F(t) = integral over SU(2) of exp(t tr(U)/2) dU = (2/pi) integral_0^pi exp(t cos theta) sin^2 theta d theta = 2 I_1(t)/t. From I_1(t) = sum (t/2)^(2n+1)/(n!(n+1)!), the Taylor coefficient of t^(2n) is 1/(4^n n!(n+1)!), so F^(2n)(0) = (2n)!/(4^n n!(n+1)!) = C_n/4^n. This is the Bessel route; row 1482 also gave the Haar-moment route, and the two agree.
- Valuations, checked. p = 3: F^(4)(0) = C_2/16 = 1/8, so v_3 = 0, while Le18 needs at least floor(12/8) = 1. F^(6)(0) = 5/64, so v_3 = 0, against floor(18/8) = 2. At n = p^j, Lucas gives binom(2p^j, p^j) = binom(2,1) = 2 mod p, and n + 1 = 1 mod p, so v_p(F^(2p^j)(0)) = 0. The exceptional case (p^2 - 1) | 2p^j is impossible, because gcd(p, p^2 - 1) = 1 and p^2 - 1 >= 8.
- Le18 (lines 12347-12350) is stated for f in Z_(p)[[t]] composed with sl. So the test proves: **F(z) is not f(sl(z)) with f p-integral, for any inert p.** That is a correct contrapositive of Le18.
- With the vacuum factor: W^(k)(0) = E(X - 1)^k, and W^(3)(0) = 0 - 3/4 + 0 - 1 = -7/4. Checked. Also (X - 1)^(p^j) = X^(p^j) - 1 mod p with p-integral moments, which gives -1 mod p. Checked.
- Scope repair (proved here). The test is tied to the coordinate. Row 1482 notes that unit rescalings keep the counterexample. A non-unit rescaling z = p w multiplies the n-th derivative by p^n, and that makes the Le18 inequality hold trivially. By the product formula the archimedean size then grows by exactly the same factor. For a non-zero rational number, the sum over p of v_p(x) log p equals log abs(x) exactly. So **no coordinate on Q produces a net gain for a rational coefficient**. The RH engine needs an upper bound on the size that is proved independently (analytic growth) and that beats the divisibility. The Wilson one-bond coefficients C_n/4^n are known in closed form, so there is no inequality left to win. N1 therefore confirms row 1481's T3 ("no object") at the one place where an object can be written down. It opens no route.
- Filter: t1 fails to separate. For U(1) the moments binom(2n,n)/4^n are also units at n = p^j (checked by Lucas). t2 (5D) is the same one-bond law. So N1 is not selective, and it is a refutation, not a candidate.

**N2. The trace-direction counterexamples. HOLDS (checked by hand); a concrete form of row 1481's T6 (a) and of Proposition PER (d).**
- Q = I_2: tr Q^2 = 2 = (tr Q)^2/D at D = 2, so eta = 0, and the purity is 1/2 < 457/625.
- Q = diag(1, 1 - h): D tr Q^2/(tr Q)^2 - 1 = [2(1 + (1-h)^2) - (2-h)^2]/(2-h)^2 = h^2/(2-h)^2, as row 1482 says. The purity (1 + (1-h)^2)/(2-h)^2 tends to 1/2.
- So the RH estimate is compatible with purity 1/2. That is T6 (a) of row 1481 with an explicit witness. On file: PER (d) of row 1303.

**N3. The explicit-formula transfer with det(I - zA), and the tensor example. HOLDS; on file.** The identity -z D'(z)/D(z) = sum over j >= 1 of z^j Tr A^j is the dictionary of row 1303 line 63 (zeta_T(z) = 1/det(1 - zT)). The example tensors with an independent two-state factor diag(1, r). That multiplies every Z^z(v) by (1 + r^v), keeps every twist ratio, and multiplies P_K by (1 + r^(2u))/(1 + r^u)^2, which tends to 1/2. This is PER (d) of row 1303 ("add a direct summand"), done as a tensor factor so that the twist ratios are kept. It shows that no explicit formula in the twist ratios alone can give the seed. On file; adds a witness.

**N4. The Dirichlet extension: a combination with positive coefficients (explainer D:37, lines 1116-1131). Lacking in row 1481. Tested here; NO TRANSFER (on file, free in the crux).**
- Tool, as read: G^psi = G + (1/(3o+1)) sum over j of Re G_(psi_j). Every prime-power coefficient lies between 3o/(3o+1) and 4o/(3o+1), so it is positive, and Landau's lemma applies to the combination.
- Transfer statement: "a combination sum over z of c_z Z^z(v), with c_z chosen so that sum over z of c_z chi_e(z) > 0 for every flux sector e, is a positive sum over sectors of Tr(P_e T^v), so a one-sided criterion applies to it".
- On-file match: the decomposition of Tr(C_z T^v) into the centre characters of the flux sectors (row 1468 3.1, `gap-flux-exercise.md` 3.0-3.1), and Fact PUR / T1. In the crux every sector trace is already a positive sum by reflection positivity, so the tool repairs a sign problem that the crux does not have. This is the same verdict as T1.
- Filter: the identity holds for every group with a centre and in every dimension. It fails (t6), (t1) and (t2) as a mechanism.

**N5. The multiscale gain (explainer lines 1502-1522, 10532-10558). Agrees with Step 2.5 of this check.** Row 1482: "the m maps must earn a quantified divisibility gain on a common endpoint ... Under repeated Q2 the equality of partition functions telescopes exactly and earns zero change of the masses." This is the refinement of T7 written in 2.5 above (no end error is divided by the number of steps), reached by a different model. The two readings agree. Both rest on Lemma TW and Theorem K2.

**N6. The uniformity clause H12 (lines 10817-10845).** Row 1482: a calculation at one K lacks a tail for infinitely many cutoffs. **Correct, and an addition to row 1481's T9.** The RH proof supplies its data at every scale of the windows through an assumed hypothesis (H12), with existential thresholds. In the crux, Theorem K2's (BASE-K2) is "for infinitely many K", so even a finite certificate of the order-one step would need to be uniform in K (in the volume l b^K). This is the same requirement as "error control uniform in volume". No tool.

**N7. Repository hits that are not RH tools.** These are `MASS_GAP_LOCAL_BLOCK_ASTRA.md` lines 131-139 and 466-486 on PR #10114 (a rank-one local block bound for one spatial loop, which needs a spatially summable half-slab covariance (31)) and a Chowla-Selberg period in a docs dispatch. Neither is a tool of the RH proof, and row 1482 tested neither as a transfer. I did not open them; they are outside this row's direction. If the lead wants them, the first is a candidate for its own row on the neutral side (purity is a rank-one statement).

**Items in row 1482 that row 1481 already had, with the same verdict:** Stepanov/product formula/Bost slope (T2), inert heights and Hasse derivatives (T3), CM fields and theta lifts (T3, T5), Fock bounds and period formulas with the order-one remainder against per-site errors growing like n^3 u (T4, wall (W2)), the seesaw and gluing (T5), Galois cohomology (T5, second half), the relative trace formula (T6), Estimate B, Behrend sets and thinning (T8), the Lean certification (T9), the announcement-only routes (T10).

**Disagreements between the twins: none on any verdict.** Two differences of emphasis. Row 1481 states T3 as "no object", while row 1482 builds the one natural object and refutes it (N1). With the scope repair above, these are the same verdict. Row 1482 also notes that the Gaussian readout coefficient 2^(d-4) is the only dimension-reading element, and that Proposition GA of row 1468 already holds it.

## Step 5. Verdict (written 16:32Z by date -u)

| Item of row 1481 | Verdict | Repair |
|---|---|---|
| Lemma PRG | HOLDS AFTER CORRECTION | add the compactness line for rho > R/2 (1.1) |
| Consequence (i) | HOLDS | (the identification of the series with h near R, written in 1.2) |
| Consequence (ii) | HOLDS given Hadamard (recalled, standard; not on the T0 chain) | Z(0) = c > 0 in general; add "Z has a zero, so log Z is not entire" (1.3) |
| Consequence (iii) | correctly OPEN; irrelevant to Outcome (B) (1.4) | none |
| Consequence (iv) | first sentence HOLDS; last sentence GUESSED, not recalled | relabel (1.5) |
| T2 match (ZB, SC, V, Prop. B) | HOLDS AFTER CORRECTION; exact match; "Stepanov with one prime" a likeness | M_k on D, not C_0 abs(B) k; label "C4" not found, cite the Lee-Yang class of row 1402 and Lemma LYP of row 1004 (2.1) |
| T6 (a) match (PER) | HOLDS; exact (P_K = 1/(1 + delta_u)) | state the identity (2.2) |
| T6 (a) reversed direction | HOLDS; the contrapositive also gives nothing | line 1923 should read 1924 (Step 3) |
| T5 match (TW, K2) | HOLDS AFTER CORRECTION; exact for twist-compatible kernels; the seesaw is a likeness | "every probability kernel compatible with the centre twist" (2.3) |
| T8 (ii) match (1461, 1465) | HOLDS; exact on the consumer side; the mean square a likeness that fails at line 2405 | none (2.4) |
| T7 | HOLDS in verdict | sharper reason: no end error is divided by the step count; the only multiplicity, PER (c), presupposes the seed (2.5) |
| Cited explainer lines | all confirmed; 428 should be 430-431, 1923 should be 1924 | (2.5) |

**Row 1481 overall: HOLDS AFTER CORRECTION.** The repairs are those in the table. None changes a verdict of row 1481, and none touches Outcome (B).

**Twin outcome: both twins end in no transfer.** No candidate of row 1482 survives. N1-N3 are refutations or witnesses for closed rows. N4 is free in the crux and not selective. N5 and N6 agree with this check's refinement of T7 and T9. **The direction "tools of the Alpoge-Claude RH proof for the crux" is closed on the record, with trigger (R7) kept as a reopen trigger, low prior and GUESSED as row 1481 says.** One condition for (R7), proved in N1: an integral structure on rational numbers known in closed form yields nothing, because the product formula is an identity for them. So (R7) should read: "a statement that places the sixteen masses, or an upper-bound function for s, at couplings on the calibrated trajectory in a number field with a stated integral structure, **together with an upper bound on their archimedean size that is proved independently of the integral structure**". The coverage limit of row 1481 (29 percent of the explainer read in full) is owned by row 1486 (luna bulk read). Row 1482 reports reading ranges over all of lines 1-13700, so the coverage of the pair is wider than that of row 1481 alone. I did not verify row 1482's coverage claim line by line.

Provenance and independence. This check is by Claude Opus 5.5 high, which is not the model of row 1481 (Claude Fable 5.2) or of row 1482 (gpt-6.2-astra). Re-derived by a different route here: the compactness step of PRG, the identity P_K = 1/(1 + delta_u), the eigenvalue form of the reversed direction, the Bessel route to F^(2n)(0), the Lucas valuations, and the product-formula scope argument of N1. Everything else is a read against the cited lines. No numeric run was made (free memory 37 percent at 16:30Z, below the 50 percent rule; no run was needed). No Lean, no code, no commit.

Credits. Levent Alpoge (with Claude): the proof of the Riemann hypothesis. Michael Rubinstein (with Claude, Codex and Gemini): the explainer and every line quoted. Ethan Sussman and Levent Alpoge (with Claude and Codex): the complete account, the Lean continuum limit and the kernel behind Q2. The authors and checkers of the lane rows cited (669-696, 1004, 1303, 1402, 1461, 1465, 1468, 1469, 1481, 1482) are as FINISH records them. Vivanti and Pringsheim, Hadamard, Borel and Carathéodory, Lucas, Legendre: classical results named above.

RESULT: Row 1487 (Claude Opus 5.5 high, Mac mini worker 2, cross-model check, hand reading and re-derivation, no numerics): row 1481 HOLDS AFTER CORRECTION. Lemma PRG is correct once the compactness step for rho > R/2 is added; consequence (ii) needs Z(0) = c > 0 and the line "Z has a zero, so log Z is not entire"; (iii) is correctly open and irrelevant to Outcome (B); the last sentence of (iv) is GUESSED. The on-file matches are exact for T2 (Theorems ZB and SC; Theorem V; Proposition B; repair M_k for C_0 abs(B) k; the label C4 is not found), T6 (a) (P_K = 1/(1 + delta_u) with Proposition PER), T5 (Lemma TW and Theorem K2, after the twist-compatibility repair) and T8 (ii) (rows 1461 and 1465), and only likenesses where row 1481 names them as the RH principles. The reversed direction of T6 (a) holds, and the contrapositive gives nothing; T7 gets a sharper reason. Both twins end in Outcome (B): none of row 1482's additions survives (the Le18 test refutes the one natural integral model, and an integral structure on closed-form rationals gains nothing by the product formula; the trace and tensor witnesses are PER (d); the Dirichlet positive-coefficient combination is free in the crux and not selective). The direction "tools of the RH proof for the crux" is closed on the record, with reopen trigger (R7) sharpened to require an archimedean size bound proved independently of the integral structure. Open, as before: the seed, (PUR-io), the order-one step and the mass gap; explainer coverage is owned by row 1486.
