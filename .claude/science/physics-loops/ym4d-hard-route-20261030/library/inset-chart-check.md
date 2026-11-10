lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T15:05Z

# inset-chart-check: check of `library/inset-chart.md` (row 617)

Provenance: Claude Opus 5.5 (claude-opus-5-5), effort high, Mac mini worker 2, at commit ff474586e. The note under check was written by Claude Fable 5.2; this reader did not write it. Not an audit. Source: YM4_1400.tex at Sussman-Alpoge commit 2bc0658f91d2 (136,637 lines, fetched to a private scratch folder, byte-identical to the copy named in the row). "Y n" = line n of that file. Credit: Sussman and Alpoge (with Claude) for YM4_1400 and the complete account; Claude Fable 5.2 for the note under check.

Status: finished 2026-11-10. Verdicts in section 12.

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

1. "Keep also the failed-cube factors and the unexplored bond factors of the ordinary split" (Y 64631-64632). The failed factors lie in creation sets, which an eligible component misses; "only the passing queried factors occur on the eligible collar carriers. The failed factors in the frozen core keep their original signs" (Y 64642-64644). So they are in T5. On the active strip the unexplored bonds receive the completed fluctuation test (Y 77746-77747), and Y's collar list at Y 69537 names only "completion, collar and rim". A rim or cube test is a conjunction of one-bond tests: "a failed cube or rim test ... has a bond with `|a'| >= c delta_j`" (Y 72106-72120). So these are in T8. *Wording repair (optional):* T8 could name the unexplored-bond factors as replaced by the completion, with Y 77746-77747.
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
- **R3-c (missing hypothesis in the proof of (2)).** The identity "a hard test with threshold at most `29 delta_j/24` is the same function of the new variable as of the old one" holds under the strip bound `|H_b| <= delta_j/8` (Y 62301-62302, 64681-64682). Add it. It holds at weak coupling: the centre shift is `C_L eps_j e^{-c R_q}` (Y 63937-63939) and `delta_j/eps_j = A_1/A_0` is fixed (Y 62068).

Wording only: "No domain depends on `omega`" (after Proposition 4.3) is false for T6, whose centre `C_b(omega)` moves with the datum. It is harmless: the datum is real and fixed on the fibre, and T6 is one on the T7 ball.

## 4. Item (4): Lemma 5.1 and its uses

**Verdict: Lemma 5.1 HOLDS. Its use in Theorem 5.6 HOLDS. One sentence after Theorem 5.6 does not follow and needs repair R4.**

The lemma: two cases on `I(pi(x))`, each one line. Correct. In Theorem 5.6, (F1) is "`P Q != 0` implies `I = 1`". The incoming term contains `P` and every factor of `Q` except the new stage factors, so `P Q != 0` implies that `x` is on the entering support, where (F1-Y) gives `I = 1`. Y's derivation of the datum bound uses exactly the preceding-stage support and T4 (Y 64088-64106, 134200-134216), not the final guard. So there is no circle: (F1) uses `P`, and (F2) proves `P = 1` from `A I = 1`. The identity holds also off `K_0`: there T6 or T8 is zero, and both are in `Q`.

**R4.** The last paragraph of 5.6 says: "Since `I(pi(x)) = 1` on the entering support, the factor `I` can be dropped again after the integration; the measure does not change." This does not follow. The integrated kernel at `omega` is `I(omega) int Q dz`. At an `omega` with `I(omega) = 0`, (F1) gives `P Q = 0` on the whole fibre, but the note shows no factor of `Q` that vanishes there, so `int Q dz` may be nonzero (for example when part (ii) of `I`, the global datum, fails while `G T4 T8 = 1`; I did not decide whether the other carried factors of the term exclude this). Dropping `I` then adds mass that the original term does not have. Repair: keep `I` as a factor of kind (A) outside the collar logarithm. It is the factor that replaces `P`. It may be dropped only on a set where the outgoing `omega`-measure is already known to vanish when `I = 0`, which is the content of (F1) and has to be applied before the integration, not after. No other line of the note uses the dropped form.

Other uses: section 6 item 5 inserts `chi_E` on `{G T4 I = 1}`. That is not Lemma 5.1. It needs the stronger half of RIM-REG; see item (5).

## 5. Item (5): Lemma 5.2 against Theorem 6.2 with R-a to R-d

**Verdict: HOLDS for the first half (existence, uniqueness, radius on the whole joined set, `E` included). HOLDS AFTER REPAIR R5 for the claim in section 6 item 3 that the stronger half also holds on the same set.**

Hypotheses, first half. Theorem 6.2 needs H-GEO; `eps_int <= a_1`; `2 eps_m <= a_1` (2.1 after the constant of `rim-scale-check.md`); `C_B eps_int <= a_0`; (a) the carried top density tests on the cubes covering `X cap Omega_m`, which is the outer two cell layers by (63760) (R-c); (b) the interior bound (I3). Lemma 5.2 has H-GEO; `eps_bar <= a_1`, which contains the first two; `C_B eps_bar < a_0` follows from `C_B a_1 < a_0`, which is part of `bgc:proper-background` (Y 35636-35637); (a) is contained in T4 (bases in `Omega_m^{~4}`, Y 64096-64097); (b) is replaced by T4 plus part (i) of `I`. That replacement is sound. Part (i) asks the bound only of tested holonomies that are not tower holonomies and have no corner in a carried top density cube. Those that have such a corner are top plaquettes, bounded by T4 and (I4). Tower holonomies are one or top plaquettes of `V_m` (R1) whose four blocks lie in `X` (cells are aligned, so a block is inside or outside `X`), hence they have corners in the covered outer layers. So the three kinds exhaust the tested holonomies (Y 134207-134210), and part (i) is implied by (I3) with `C_3 = C`. Y argues the same way: "Hence the joined datum is `bar eps`-regular for `bar eps > C max_q e_q` ... The regular orbit for the localized set in force therefore exists before the prospective guard is applied" (Y 134211-134216).

R-a, R-b and R-d do not touch the first half: R-a and R-b concern the profile bound on `E`; R-d concerns Corollary 6.3. R-c concerns a citation; Lemma 5.2 cites coverage (Y 76692-76697) instead of (G1), which is enough.

Conclusion on `E`. `bgc:proper-background` bounds `R_mat`, a supremum over the whole joined set, so `R(U^+) <= C_B eps_bar` holds on `E` and the tower. With R-a this is `norm(dU^+(p) - 1) <= C_B eps_bar L^{-2 lambda(p)}` on `E`. It is a bound by `eps_bar`, which is of order `C_3 max_q R_q^2 eps_q`, not of order `eps_m`. That is all that Proposition 5.3 says the inputs read on `E` (existence, a radius below a fixed ceiling, the top rows), so the conclusion on `E` that the note uses follows.

**R5.** Section 6 item 3 adds: "The stronger half of RIM-REG (curvature at most `2 K_w eps_m L^{-2 lambda(p)}` on `E`, so `chi_E = 1`) holds on the same set." Lemma 5.2's hypotheses do not give it. Theorem 6.2's second half also needs `C_B eps_int <= a_c` (the profile, (I2)), `eps_int e^{-delta d} <= eps_m/2` with `d` the weighted distance from `E` to `X cap Omega_m^c`, and R-a, R-b. Section 8 item 5 lists neither condition. Repair: add both to the coupling ceiling (both hold at weak coupling: `d >= c M R_m`, Y 71386-71391), or restrict the sentence to that case. Nothing else in the note uses the stronger half, except the insertion of `chi_E` in section 6 item 5.

## 6. Item (6): the table of 5.4 and Theorem 5.4

**Verdict: HOLDS.** Each threshold agrees with Y, and the five cases are all the reads of the preceding guard. The lead checked the arithmetic; I also redid (a), (e) and (c) and agree.

Indices. The preceding guard is the guard after `N_m - 1` stages; Y's stage index is then `k_flat + N_m - 1 = m - 1 = j`, and the final guard has index `m` (Y 63864, 63876).

| Case | Y, preceding | Y, final | Agrees |
|---|---|---|---|
| (a) shell `i < j` | `(1 - beta_s(1 - 2^{-(j-i+1)})) eps_i L^{-2i}` times `L_flat^{2(i - k_0 - 1)_+}` (Y 63876; the factor "depends on the shell only, not on the stage") | same with `m` in place of `j`; "smaller by `beta_s 2^{-(j-i+2)}`" (Y 64236-64238) | yes |
| (b) new shell `Y_m minus Z''_j` | deep exterior at stage `j`, `e = j - k_0 - 1`, `c_l = 1`: `(1 - beta_s/2) F_j eps_j L^{-2j}` (Y 63876) | shell `j` at index `m`: `1 - beta_s(1 - 2^{-2}) = 1 - 3 beta_s/4`; "the factor is unchanged and the coefficient decreases from `1 - beta_s/2` to `1 - 3 beta_s/4`" (Y 64252-64255) | yes |
| (c) outside `Y_m`, deep exterior or `Omega_l minus Omega_{l+1}`, `k_0 < l <= j` | `(1 - beta_s/2) c_l L_flat^{2e} eps_j L^{-2j}`, `e = (j - l - 1)_+`, deep exterior `e = j - k_0 - 1`, `c_l = 1` at a non-final stage (Y 63876) | same at scale `m`: `e` rises by one except at `l = j`, where `e = 0` both times and `c_j = 3` "adjacent to `Omega_k` at the last stage"; ratio at most `(eps_m/eps_j) max{L_flat^2, 3}/L^2` (Y 64255-64261) | yes |
| (d) astride `dY_m` | read by the deep exterior clause (Y 64270-64280) | `kappa_x` at `(1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j - k_0 - 1)}` (Y 64309-64313) | yes |
| (e) carried crossing of `dZ''_{s+1}` | coefficient of shell `s`, first `1 - 3 beta_s/4`, dropping by `beta_s 2^{-(j-s+2)}` per transition (Y 64437-64444) | `c(s, m)`; the note's `c(s, J)` gives `c(s, s+1) = 1 - 3 beta_s/4` and the stated drops | yes |

The `k_0` of the note is Y's `k_sharp` (Y 63876 and Y 63776 define the same index). The final stage is compressed (`k_0 <= m - 2`, Y 63777), so `e = 0 for j <= k_sharp` never applies.

All reads. A clause of the stage-`j` guard is a shell clause (containment in one shell `i <= j - 1`), the deep exterior clause (containment in `Omega_{k_0+1}^c` outside the shells), an exterior clause (containment in one layer `Omega_l minus Omega_{l+1}`, `l <= j`), or a carried crossing (Y 63876, 64226-64228, 64277-64279, 64437-64463). A plaquette that straddles two layers or two shells is read by no containment clause; Y treats such plaquettes only through the Hölder translation in (Y-DENS) (Y 64753-64767) and the crossing tests. A deep exterior plaquette of stage `j` lies wholly in `Y_m minus Z''_j` (b), wholly outside `Y_m` (c), or astride `dY_m` (d); "the clearance from `Omega_{k_0+1}` puts it inside the old deep exterior region" (Y 64275-64277). The layer reads with `l <= k_0` are inside `Omega_{k_0+1}^c` and are deep exterior reads. So (a) to (e) are all the reads. Each lies in `X cap Omega_m^c = H_m^{[8 a_m]} = X^{[-2 a_m]}` (63760), hence in `X_in = X^{[-a_m]}`, and each final clause in the last column is a clause of `chi_in`, `kappa_x` or T3.

One citation precision: the note cites (E1) to Y 65010-65014. Y derives that display "on the old level-`j` plaquette carriers at the new prepared face" (Y 64991-64993). For the reads of case (c) in the collar `K`, the bound is the same estimate at `D = 0` with local scale `xi_j` (Y 65000-65004: `C_L delta'_j e^{-aD/2}` with weights `xi_s, xi_s^2`), and Y uses it there: "On admitted real data the collar response fits these reserves, by its weighted bound on the old shells and the small ratio `delta'_j/eps_j` in the exterior" (Y 64265-64267). Cite both.

## 7. Item (7): Proposition 5.3, independent reading of Y 63884-65404

**Verdict: HOLDS.** I read Y 63884-65404 in full, and Y 13283-13396 for (Y-JOIN). I found no use of a rim threshold on `E`.

The passages that read on or near `E`, and what each reads:

1. (Y-BELT), Y 64046-64086. The test-cube reads stay at distance at least `c M R_m` from `dX` (Y 64057-64059). On the box the top rows of `U^{(N_m)}_{m,X}` are `V_m`, and the comparison "reads the ordinary coarse density test and the retained rows. It does not require the discarded sharp bound at the artificial bare rim of `X`" (Y 64083-64086). Reads (2) only.
2. The annulus comparison of `S^-` with the ordinary centre, Y 64108-64137. Its outer band is `X` inset by a quarter of a level-`m` cell, which lies in `E`. It uses that both backgrounds have "the same regions and the same determining rows, including the top data used on its two boundary bands" (Y 64120-64123), and the joined comparison, whose hypotheses are datum bounds (Y 13284-13293). Reads (1) for `U^-` (its existence from (Y-PATH)) and (2). The note's evidence list does not name this passage; it should, and it does not change the result.
3. (Y-PATH), Y 64860-65017. It uses "the fixed small regularity ceiling of the background theorem" for `U^+` (Y 64868-64869) and "the old curvature and current scales are no larger, so `U^+` is regular also in the old units" (Y 64878-64879). Reads (1). Its estimates are at `K` and the prepared face (Y 64894-64908, 64991-64996).
4. (Y-JOIN) at the final stage, Y 65019-65067. The joining collar is at `dX`; the read set is at weighted distance at least `c M R_m` from it (Y 65054-65056). The hypothesis is a datum bound (Y 13284). Reads (2) and the regularity of the global datum (part (ii) of `I`).
5. The global annulus for the inherited strip, Y 65378-65404. It compares two global backgrounds that "read the same rows and data throughout this annulus" (Y 65396-65398). Reads data only.
6. Y 64590-64593: "For the remaining inset-positive evaluations use the real collar path at fixed prospective datum. The seam estimate concerns the prepared interface inside `X`. The face-lift calculation at `dX` supplies its own restriction." This is Y's own statement of Proposition 5.3: at `dX` the restriction comes from the face lift of `V_m`, which is (2). The note should cite it.
7. Every guard clause used lies in `X cap Omega_m^c` (Y 64229-64232) or is `kappa_x` or T3 (Y 64306-64315, 64437-64463). The Hölder translation for `kappa_x` stays in the inset (Y 64338-64345). (Y-DENS) halos lie "in the top inset of `X`" (Y 64707-64708). (Y-CONT) blocks "lie entirely in the collar" (Y 64794).

The only text in the range that names a threshold at the bare rim is Y 63876 ("There the test therefore demands `|dV_k - 1| < C eps_k eta_k^2` of the block field itself, while the carried tests provide only `2 eps_k`"), which states why the literal rim clause fails; it is not a use of that clause.

## 8. Item (8): the decision of section 6

**Verdict: HOLDS.** The rim clauses read `U^+`, which is a function of `omega` (item (2)), so `r(omega)` and `chi_E(omega)` are of kind (A). The hypotheses of the first half of RIM-REG used by Lemma 5.2 are T4, a function of `V_m`, and part (i) of `I`, a finite set of inequalities on datum holonomies in `omega`. Neither contains `r`, `G` or `z`. The derivation of `I` on the entering support uses the preceding-stage support and T4 (Y 64088-64106, 134200-134216); `r` is a factor of the final guard and is not in the incoming term. Y's sentence on preceding guards (Y 64580-64585) concerns a guard on the active collar; the final guard is never the preceding guard of a later collar integration of this operation, since "the artificial bare rim occurs only in the final guard" (Y 64232) and the final stage is the last stage. The main step, where the final guard is the preceding guard of the central integration, is outside this decision; the note says so (section 6 item 6, section 9 item 8). The example of Y 72340-72428 does have the earlier stage tests passing "while the last stage test fails" (Y 72420-72423), so the sector `chi_in (1 - r)` is not empty, as the note says. The second sentence of section 6 item 3 needs R5.

## 9. Item (9): section 7, moving domains

**Verdict: HOLDS.** With the direct graded rule, the global sharp ball and the inset guard: the passing-branch cutoffs are T7, the fixed ball in `B_g` (Y 65104-65106; "For the global sharp branch keep `B_g` as the variable of the fixed sharp ball on the free nonpivots. Its real local approximate test on those bonds is then identically one", Y 65868-65870), and T8, fixed balls in the original strip coordinates (Y 69547-69551, 65402-65404). The comparison with the free shift source uses "the source value zero with its integration variable identified with `B_g`" (Y 65871-65874). The inherited crossings stay "in the ordinary strip integral with their completed tests" (Y 65880-65882), so the incident-bond read with its open checks (Y 65212-65216, 65342-65345) does not occur. The kind-(A) factors are real functions of the real datum, which is not an analytic parameter (Y 69553-69564: "evaluated on the real data selected by the external guard"). The note's two variants (local sharp ball in the global chart; incident-bond convention) are correctly described and correctly set aside. One limit: the failed sharp branch `1 - T7` uses its own strip map with a cutoff and transported tests (Y 65129-65152, 65891-65895); the note's claim is for the passing branch only, and it is stated that way.

## 10. Item (10): order of constants (section 8)

**Verdict: HOLDS AFTER REPAIR R10.** I found no cycle. Two orderings and one condition are missing.

- **R10-a (`L_flat^2 < L`).** Section 8 step 1 takes `2 <= L_flat < L/2`. Y 65481 uses `L_flat^2 < L` (for `psi_l <= C (log theta_l)^r` on the remade shells, which feeds the `C e_l` datum bound and so (F1-Y) and `C_3`). `L_flat < L/2` does not give it: `L = 13`, `L_flat = 6` has `36 > 13`. Repair: require `2 <= L_flat` and `L_flat^2 < L` in step 1 (for example `L = 13`, `L_flat in {2, 3}`). This implies `L_flat < L/2` for `L >= 4`, so (L3) still holds. Y itself states only `2 <= L_flat < L/2` at Y 63876, so the extra condition is also missing from Y's statement of the choice; it is satisfiable.
- **R10-b (`M_2` and `delta_0`).** Step 1 lists `M_2` and step 2 lists `delta_0`. Y requires `L^2 M_2 <= M` and `c delta_0 M_2 >= 1`, with `delta_0` "fixed together with `L`" (Y 62001; also Y 17399). Move `delta_0` into step 1 before `M_2`, and add `M >= L^2 M_2` to step 3. Not a cycle.
- **R10-c.** If `a_0, a_1, C_B` or `C_3` depend on `M` through the gap floors, they come after step 3. Nothing in step 3 depends on them, so this reorder is free.

What `R_1 >= 42 L` (R-f) changes. It is a geometric floor in step 1 and depends on no later choice. It raises the floors `M_1 >= R_1 frakM` (Y 651-652, 35850) and `M >= L^4 M_1` (H-GEO), so step 3 comes later and the constants of step 2 that depend on `R_1` are fixed after it, which the order already allows. It enters the coupling ceiling through the tower fit `M R_m >= C(L, R_1) frakM` (`rim-scale-check.md`, R-f), which holds at weak coupling. Nothing in INSET-CHART uses an upper bound on `R_1`.

Consistency with the conditions of `library/prior/r1-floor.md`:

- Y 71861, `2 M_1 L^t + L^{t-1} < w = M_2 R_t L^t`, that is `M_2 R_t > 2 M_1 + 1/L`. Consistent: `M_1`, `M_2` come before the coupling ceiling, and `R_t >= (log min_i x_i)^r` is large below it (Y 62001). Add it to step 5.
- Y 84261, `C M_1 xi_{n*} < w_{l(Omega_0)}`. Consistent in the same way when `n* <= l(Omega_0)` (then it reads `C M_1 < M R_l`); I did not decide `n* <= l(Omega_0)` from the text at Y 84252-84266.
- Y 97436, `10 M_1 < M R_j`. Holds from step 3: `M >= L^4 M_1 >= 13^4 M_1` and `R_j >= 1`.
- Y 4400 against Y 17399. Y 4400 lets `c_1, B_1` depend on `L, frakM, R_1`; Y 17399 says the ceiling on `alpha_0, alpha_1, gamma_0` comes with `L` and does not depend on `M_1, R_1 M_1`. Section 8 puts every coupling condition in step 5, after all geometric choices, so it is consistent with the weaker reading (dependence on `R_1` allowed) and needs nothing from Y 17399's independence claim. The tension between Y 4400 and Y 17399 is Y's, not the note's.

## 11. The six inputs: proved or stated in Y

- (Y-PATH), Y 64860-65017: proved in prose. The pivot branch is a displayed inequality (Y 64944-64948); the path and the response bound (E1) are argued from the regular implicit inverse and the Landau response bounds of Y's background chapter, which are cited, not reproved there. (E2) and (E3) are stated in one or two sentences each from the decaying form (Y 64239-64250, 64451-64455, 65000-65004).
- (Y-JOIN), Y 13283-13396: proved, with the norm bound derived by integrating the derivative (Y 13384-13394).
- (Y-DENS), Y 64699-64789: proved in prose; the Hölder bounds and the response transfer are cited (`mb:local-regularity-conclusion`, `mb:holder-reduction`, Y 64757-64760, 64772-64774).
- (Y-CONT), Y 64791-64810: stated with a one-paragraph reason; "the mean contour map on the full block has a bounded derivative" is asserted there.
- (Y-BELT), Y 64027-64211: proved in prose from cited comparisons; the three centre bounds are displayed (Y 64078-64081, 64134-64137, 64200-64203) and the step `S^-` to `S` is argued (Y 64139-64168).
- (Y-MEAN), Y 64929-64953 and 64802-64807: the pivot branch is proved (Y 64941-64958); that every block mean of the collar is on its regular branch on the approximate ball is stated.

## 12. Summary for the lead

| Item | Verdict | First open input |
|---|---|---|
| (1) T1 to T13 complete | HOLDS | none in the list; optional wording on unexplored-bond factors |
| (2) Proposition 4.1 | HOLDS | none |
| (3) Lemma 4.2, Proposition 4.3 | HOLDS AFTER REPAIR (R3-a `nu`, R3-b normalization of T8, R3-c `|H_b| <= delta_j/8`) | Y's Gaussian tail on the stage chart (Y 64542-64548), cited |
| (4) Lemma 5.1 and uses | HOLDS; sentence after Theorem 5.6 needs R4 (keep `I`) | (F1-Y) |
| (5) Lemma 5.2 vs Theorem 6.2 | HOLDS (first half, conclusion on `E` as used); stronger half on the same set needs R5 | H-GEO; (F1-Y) part (i) = (I3) |
| (6) Table 5.4, Theorem 5.4 | HOLDS | (Y-PATH) estimates (E1) to (E3) |
| (7) Proposition 5.3 | HOLDS (second reading, by a model that did not write the note) | none |
| (8) Section 6 decision | HOLDS | main step (section 9 item 8), not in scope |
| (9) Section 7 | HOLDS | none for the direct graded rule |
| (10) Section 8 | HOLDS AFTER REPAIR (R10-a `L_flat^2 < L`; R10-b `delta_0` before `M_2`, `M >= L^2 M_2`) | Y 84261 fit, `n* <= l(Omega_0)` not decided |

First failing line: section 8 step 1, "`L_flat` with `2 <= L_flat < L/2`", which does not give `L_flat^2 < L` used at Y 65481. The repair is a stronger choice of `L_flat`, with no other change. No defect found breaks Theorem 5.6.

What this check does not show. Theorem 5.6 is still an implication from H-GEO, (F1-Y) and the six inputs of Y, none rebuilt here. I did not decide convention D (note section 9 item 4), the main step, or the earlier transitions. Provenance: one reading by Claude Opus 5.5 (high); no numeric job was run; every step is by reading and by hand.
