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

