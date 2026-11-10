lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:05Z

# inset-chart-check: check of `library/inset-chart.md` (row 617)

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort high, Mac mini worker 2, at commit ff474586e. The note under check was written by Claude Fable 5.2; this reader did not write it. Not an audit. Source: YM4_1400.tex at Sussman-Alpoge commit 2bc0658f91d2 (136,637 lines, fetched to a private scratch folder, byte-identical to the copy named in the row). "Y n" = line n of that file. Credit: Sussman and Alpoge (with Claude) for YM4_1400 and the complete account; Claude Fable 5.2 for the note under check.

Status: in progress. Sections are written as each item is finished.

Repo search. `grep -n "inset-chart" FINISH.md QUEUE_DONE.md library/open-core.md`: rows 617 (the note), 619, 622 (this check), 623, 624, 626, 627, 628 and 630. Rows 619, 623, 624, 626, 627, 628, 630 read or prove inputs of the note (r1-floor, Y-PATH, the certificate, COV); none is a check of it. `library/open-core.md` has no hit. This file checks; it attacks no open lemma.

Notation is the note's: `m` top level, `j = m - 1`, `Y_m = Z''_m(X)`, `K` the exterior collar, `omega` the fixed datum, `z = (a, B)` the active part. Y writes `k` for the top level in Y 63836-63882 and `k_sharp` for the note's `k_0` (Y 63876: `M R_{k_sharp+1} L^{k_sharp+1-k} = M`; Y 63776: `a_{k_0+1} = u_k`; the two definitions agree).

## 1. Item (1): completeness of T1 to T13

**Verdict: HOLDS.** I found no retained test outside T1 to T13.

Y's own lists, read again:

- Y 62078 (end of `lem:large-field-2-2`): "On the support of the tests of a stage, the following tests equal 1: those of the preceding stage, and those of the single stored step whose fields the stage integrates (the plaquette tests of its two levels, the gauge indicators, the approximate fluctuation tests)." Preceding stage: T9. Plaquette tests of levels `m` and `j`: T4, T10. Gauge indicators: T11. Approximate fluctuation tests: T12.
- Y 63836 item (1) and Y 77744-77747: the stage imposes `chi_i^{(n+1)}` (T1 to T3), the collar gauge (a weight), `chi'_j` at `2 delta'_j` (T6), and completes the fluctuation tests of step `j+1` (T8).
- Y 64646-64665: keep "the final top density (T4), the soft gauge density (weight), the carried fluctuation factors, and the separate collar and rim factors (T8)". Remove "the preceding regularity, ordinary density, contour, and two approximate belt groups" (T9 to T12). Y 64836-64837: "The bottom-core and fixed-outgoing selectors stay on their real arguments" (T5, T4).
- Y 69536-69543: on the active strip, "the ordinary completion, collar and rim indicators on their original masks" (T8); "The free sharp collar ball" (T7); the additional inherited sharp test belongs to the incident-bond convention only (note section 7).
- Y 62013: totality (T13).

Candidates I checked and found covered:

1. "Keep also the failed-cube factors and the unexplored bond factors of the ordinary split" (Y 64631-64632). The failed factors lie in creation sets, which an eligible component misses; "only the passing queried factors occur on the eligible collar carriers. The failed factors in the frozen core keep their original signs" (Y 64642-64644). So they are in T5. On the active strip the unexplored bonds receive the completed fluctuation test (Y 77746-77747), and Y's collar list at Y 69537 names only "completion, collar and rim". A rim or cube test is a conjunction of one-bond tests: "a failed cube or rim test ... has a bond with `|a'| >= c delta_j`" (Y 72105-72119). So these are in T8. *Wording repair (optional):* T8 could name the unexplored-bond factors as replaced by the completion, with Y 77746-77747.
2. The incident-crossing query rule with `delta_j^flat` (Y 64612-64616). Y uses the other query rule ("use the query rule in which a collar bond has both ends in the explored region", Y 64605-64607). Not a retained test here.
3. The test `chi_{k,Lambda}` of (2), the last-shell test, the test on `B` and the cut-off `chi(Lambda^pr)` (Y 63836-63856) belong to the main step. They are not tests of the final stage.
4. "deep core variables whose factors can still read the moving background" (Y 69535-69536) are factors (weights), not tests; the note does not need them.

## 2. Item (2): Proposition 4.1

**Verdict: HOLDS.** Each of T1 to T5 is a function of `omega`.

- T1 to T3 read plaquette norms of `U^+`. Y holds the prospective datum fixed in the collar integration: "Fix an admitted prospective real datum and its regular critical configuration `U^+` ... The prospective datum is held fixed while the finer variables vary in the collar" (Y 64863-64867); "The prospective regularity guard depends on the fixed datum and remains outside the collar logarithm. This includes the prospective crossing tests wherever they are used" (Y 69544-69547). The note's four kinds of rows agree with Y 69603-69607 (prepared-side fine links held; links in the active block and crossing the prepared face released) and Y 64068-64069 (top rows of `U^{(N_m)}` on the test-cube box have values `V_m`). The released links are not rows of the no-inward prospective set; the strip slots `a` are level-`j` variables on `X cap Omega_m`, where the prospective set has level-`m` rows only. Gauge: the collar gauge is pinned at the coarse sites and the guard uses covariance of the critical orbit (Y 77767-77774); the orbit is "covariant under real gauges of the datum" (Y 35646-35647). With convention D, "defined" is also a property of the datum.
- T4: `chi_m(square)` is formed with the localized background `U_{m,square}(V_m)` and depends on `V_m` within `O(1)` test cubes (Y 62003). The halos of cubes based in `Omega_m^{~4} minus Omega_m` read level-`m` rows in `K`; these are the averaging targets `V_m(c)`, which are in `omega`.
- T5: Y 64022-64025 (gap at least `3 a_q`, halos less than `a_q`), Y 64836-64837.


## 3. Item (3): Lemma 4.2 and Proposition 4.3

**Verdict: HOLDS AFTER REPAIR.** The supports are one-bond balls, and Y's overlap estimate applies, after three small repairs. None changes a conclusion.

Lemma 4.2 is correct as written: `1 - I_alpha <= sum_{b in S_alpha} 1{|z_b| >= h}`; the product expands into the stated sum; indicators are idempotent; the preimage of `b` under `alpha -> b_alpha` lies in `{alpha : b in S_alpha}`, which has at most `nu` elements, so the image has at least `|A|/nu` elements. It is the displayed inequality of Y 64536-64541.

Y's hypotheses for a selector kept in the expansion (Y 64506-64512): fixed in the real integration coordinates on the whole parameter domain, fixed carrier, accepts the smaller ball. T7 is the fixed ball in `B_g` (Y 65104-65106; for the global sharp branch Y keeps `B_g` as the variable of the ball, Y 65868-65877). T8 is in the original strip coordinate: "The tests inside the integral are in their original real slots ... The domain of a hard cutoff stays in its original coordinate" (Y 69547-69551). Carriers are single bonds. Proposition 4.3 (3) is correct: with Y's norm (`<X,Y> = (1/2) Tr XY`, Y 4701-4702) a traceless Hermitian `theta` with eigenvalues `+-t` has `|theta| = t` and `norm(e^{i theta} - 1) = 2 sin(t/2) <= t`; unitary invariance gives `norm(e^{i theta} C - 1) <= delta'_j + delta'_j/8 < 2 delta'_j`. Y states the same implication (Y 65074-65075, 65868-65870). The Gaussian tail itself is Y's (Y 64542-64548), cited, as the note says.

Repairs:

- **R3-a (multiplicity).** `nu = 1` needs two merges. The three ordinary indicators at one strip slot count as one selector, their conjunction (Y 69538-69540). T6 and T7 read the same bond `b`; if both are kept as failure selectors (before the sharp split), `nu = 2`. On the passing sharp branch T6 is identically one (Y 65869-65870), and then `nu = 1`. The tail changes only by `c h^2 |A|/2` in place of `c h^2 |A|`.
- **R3-b (normalization).** Item (2) writes T8 as `abs(a_b) < rho_b` with `rho_b` a fraction of `delta_j`, and the line after Proposition 4.3 asks `g_j h <= rho_b`. These agree only if `a_b` is in field units and the ball is `abs(g_j a_b) < rho_b` (Y's angular coordinate `a' = g_j A^s_j`, Y 72106). Write T8 as `prod_b 1{abs(g_j a_b) < rho_b}`.
- **R3-c (missing hypothesis in the proof of (2)).** The identity "a hard test with threshold at most `29 delta_j/24` is the same function of the new variable as of the old one" holds under the strip bound `|H_b| <= delta_j/8` (Y 62300-62301, 64681-64682). Add it. It holds at weak coupling: the centre shift is `C_L eps_j e^{-c R_q}` (Y 63937-63939) and `delta_j/eps_j = A_1/A_0` is fixed (Y 62068).

Wording only: "No domain depends on `omega`" (after Proposition 4.3) is false for T6, whose centre `C_b(omega)` moves with the datum. It is harmless: the datum is real and fixed on the fibre, and T6 is one on the T7 ball.

## 4. Item (4): Lemma 5.1 and its uses

**Verdict: Lemma 5.1 HOLDS. Its use in Theorem 5.6 HOLDS. One sentence after Theorem 5.6 does not follow and needs repair R4.**

The lemma: two cases on `I(pi(x))`, each one line. Correct. In Theorem 5.6, (F1) is "`P Q != 0` implies `I = 1`". The incoming term contains `P` and every factor of `Q` except the new stage factors, so `P Q != 0` implies that `x` is on the entering support, where (F1-Y) gives `I = 1`. Y's derivation of the datum bound uses exactly the preceding-stage support and T4 (Y 64088-64106, 134200-134216), not the final guard. So there is no circle: (F1) uses `P`, and (F2) proves `P = 1` from `A I = 1`. The identity holds also off `K_0`: there T6 or T8 is zero, and both are in `Q`.

**R4.** The last paragraph of 5.6 says: "Since `I(pi(x)) = 1` on the entering support, the factor `I` can be dropped again after the integration; the measure does not change." This does not follow. The integrated kernel at `omega` is `I(omega) int Q dz`. At an `omega` with `I(omega) = 0`, (F1) gives `P Q = 0` on the whole fibre, but the note shows no factor of `Q` that vanishes there, so `int Q dz` may be nonzero (for example when part (ii) of `I`, the global datum, fails while `G T4 T8 = 1`; I did not decide whether the other carried factors of the term exclude this). Dropping `I` then adds mass that the original term does not have. Repair: keep `I` as a factor of kind (A) outside the collar logarithm. It is the factor that replaces `P`. It may be dropped only on a set where the outgoing `omega`-measure is already known to vanish when `I = 0`, which is the content of (F1) and has to be applied before the integration, not after. No other line of the note uses the dropped form.

Other uses: section 6 item 5 inserts `chi_E` on `{G T4 I = 1}`. That is not Lemma 5.1. It needs the stronger half of RIM-REG; see item (5).

## 5. Item (5): Lemma 5.2 against Theorem 6.2 with R-a to R-d

**Verdict: HOLDS for the first half (existence, uniqueness, radius on the whole joined set, `E` included). HOLDS AFTER REPAIR R5 for the claim in section 6 item 3 that the stronger half also holds on the same set.**

Hypotheses, first half. Theorem 6.2 needs H-GEO; `eps_int <= a_1`; `2 eps_m <= a_1` (2.1 after the constant of `rim-scale-check.md`); `C_B eps_int <= a_0`; (a) the carried top density tests on the cubes covering `X cap Omega_m`, which is the outer two cell layers by (63760) (R-c); (b) the interior bound (I3). Lemma 5.2 has H-GEO; `eps_bar <= a_1`, which contains the first two; `C_B eps_bar < a_0` follows from `C_B a_1 < a_0`, which is part of `bgc:proper-background` (Y 35633-35635); (a) is contained in T4 (bases in `Omega_m^{~4}`, Y 64096-64097); (b) is replaced by T4 plus part (i) of `I`. That replacement is sound. Part (i) asks the bound only of tested holonomies that are not tower holonomies and have no corner in a carried top density cube. Those that have such a corner are top plaquettes, bounded by T4 and (I4). Tower holonomies are one or top plaquettes of `V_m` (R1) whose four blocks lie in `X` (cells are aligned, so a block is inside or outside `X`), hence they have corners in the covered outer layers. So the three kinds exhaust the tested holonomies (Y 134207-134210), and part (i) is implied by (I3) with `C_3 = C`. Y argues the same way: "Hence the joined datum is `bar eps`-regular for `bar eps > C max_q e_q` ... The regular orbit for the localized set in force therefore exists before the prospective guard is applied" (Y 134211-134216).

R-a, R-b and R-d do not touch the first half: R-a and R-b concern the profile bound on `E`; R-d concerns Corollary 6.3. R-c concerns a citation; Lemma 5.2 cites coverage (Y 76692-76697) instead of (G1), which is enough.

Conclusion on `E`. `bgc:proper-background` bounds `R_mat`, a supremum over the whole joined set, so `R(U^+) <= C_B eps_bar` holds on `E` and the tower. With R-a this is `norm(dU^+(p) - 1) <= C_B eps_bar L^{-2 lambda(p)}` on `E`. It is a bound by `eps_bar`, which is of order `C_3 max_q R_q^2 eps_q`, not of order `eps_m`. That is all that Proposition 5.3 says the inputs read on `E` (existence, a radius below a fixed ceiling, the top rows), so the conclusion on `E` that the note uses follows.

**R5.** Section 6 item 3 adds: "The stronger half of RIM-REG (curvature at most `2 K_w eps_m L^{-2 lambda(p)}` on `E`, so `chi_E = 1`) holds on the same set." Lemma 5.2's hypotheses do not give it. Theorem 6.2's second half also needs `C_B eps_int <= a_c` (the profile, (I2)), `eps_int e^{-delta d} <= eps_m/2` with `d` the weighted distance from `E` to `X cap Omega_m^c`, and R-a, R-b. Section 8 item 5 lists neither condition. Repair: add both to the coupling ceiling (both hold at weak coupling: `d >= c M R_m`, Y 71386-71391), or restrict the sentence to that case. Nothing else in the note uses the stronger half, except the insertion of `chi_E` in section 6 item 5.
