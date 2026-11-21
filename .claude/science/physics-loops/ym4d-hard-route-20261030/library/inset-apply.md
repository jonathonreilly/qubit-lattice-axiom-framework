lead: anthropic/claude-opus-5-5/medium mac-mini-worker
lease_until: 2026-11-11T01:29Z

# inset-apply (FINISH row 645): repairs of `library/inset-chart-check.md` applied to `library/inset-chart.md`

Provenance: Claude Opus 5.5 (claude-opus-5-5), medium effort, Mac mini worker 2. Checkout at commit a42b9bec2, 2026-11-10. This is not an audit. The edits are text only, with no proof by computer and no numeric job. Credit: Claude Fable 5.2 wrote `library/inset-chart.md`. Claude Opus 5.5 (high) wrote the repairs in `library/inset-chart-check.md`. Sussman and Alpoge (with Claude) wrote YM4_1400.tex.

Source: YM4_1400.tex at Sussman-Alpoge commit 2bc0658f91d2, 136,637 lines, fetched by URL into a private scratch folder. "Y n" means line n of that file. Before each edit I reread the Y lines it cites: Y 62001 (`L^2 M_2 <= M`, `c delta_0 M_2 >= 1`, "`delta_0` is fixed together with `L`"), Y 62068 (`delta_k/eps_k = A_1/A_0`), Y 62301-62302 and 64681-64682 (`|H| <= delta_j/8`, hard tests at thresholds at most `29 delta_j/24` unchanged), Y 63937-63939 (shift `C_L eps_j e^{-c R_q}`), Y 65481 ("The latter bound uses `L_flat^2 < L`"), Y 65868-65870 (on the global sharp branch the approximate test is identically one), Y 72106 (`a' = g_j A^s_j`), Y 71386-71391 and Y 77947-77949. Each says what the check says it says.

Repo search: `grep -n inset-apply FINISH.md library/open-registry.md` finds only row 645 and the registry row INSET-CHART, which names this row. `library/open-core.md` has no hit. This row applies repairs and attacks no open lemma.

Scope rule: the only statements and proof steps changed are the ones a repair names. The only files touched are `library/inset-chart.md` and this log.

## Edit log

| # | Repair | Place in `library/inset-chart.md` | Status | Note |
|---|---|---|---|---|
| 1 | R3-a | Proposition 4.3, the paragraph after the items ("So Lemma 4.2 holds ...") | APPLIED | Removed the unconditional `nu = 1`. Added that `nu = 1` holds after two merges: (i) the three ordinary indicators at a slot are one selector (Y 69538-69540); (ii) T6 and T7 on the same bond give `nu = 2` before the sharp split, with tail `c h^2 abs(A)/2`, and on the passing sharp branch T6 is identically one (Y 65869-65870), so `nu = 1`. |
| 2 | R3-a | Section 4.2, last paragraph ("For the direct graded rule ...") | APPLIED | Added "on the passing sharp branch and with the merges (i), (ii) above". This sentence restates the claim R3-a repairs. |
| 3 | R3-a | Section 0, result table, row "(2) Way (B)" | APPLIED | "multiplicity 1" now carries the same two conditions. This summary restates the claim R3-a repairs. |
| 4 | R3-b | Proposition 4.3 item 2 | APPLIED | T8 is `prod_b 1{abs(g_j a_b) < rho_b}`, with `a_b` in field units and `g_j a_b` Y's angular coordinate `a'` (Y 72106). The bound on `rho_b` is unchanged. The condition after the proposition, `g_j h <= rho_b`, now agrees with item 2 as written. |
| 5 | R3-b | Section 2, the definition of `Ch(omega)`, strip clause | APPLIED | `abs(a_b) < rho_b` became `abs(g_j a_b) < rho_b`. `Ch(omega)` is built from the T8 ball, and Theorem 5.6 uses `K_0 = {z in Ch(omega)}`. Without this edit the chart and T8 would use different normalizations. The edit uses the normalization R3-b names. |
| 6 | R3-c | Proof of Proposition 4.3, step (2) | APPLIED | Added the hypothesis `abs(H_b) <= delta_j/8` (Y 62301-62302, 64681-64682) before the sentence on hard tests at thresholds at most `29 delta_j/24`. Added the reason it holds at weak coupling: shift `C_L eps_j e^{-c R_q}` (Y 63937-63939) and `delta_j/eps_j = A_1/A_0` fixed (Y 62068). |
| 7 | R4 | Section 5.6, the last sentence after the proof of Theorem 5.6 | APPLIED | Replaced "the factor `I` can be dropped again after the integration; the measure does not change". The new text: `I(omega)` is kept as a factor of kind (A) outside the collar logarithm, in place of `P`. The integrated kernel is `I(omega) int Q dz`. `I` may be dropped only where the outgoing measure is known to vanish when `I = 0`, that is, by (F1) before the integration. Theorem 5.6 and its proof are unchanged. |
| 8 | R5 | Section 6 item 3, last sentence (the stronger half of RIM-REG) | APPLIED | The sentence now holds under the extra hypotheses of the second half of `rim-scale.md` Theorem 6.2: `C_B eps_bar <= a_c`, `eps_bar e^{-delta d} <= eps_m/2`, and R-a, R-b of `rim-scale-check.md`. Reasons for weak coupling are cited: `d >= c M R_m` (Y 77947-77949) and `eps_* e^{-c delta_c M R_m} = o(eps_m)` (Y 71386-71391). I wrote the conditions with the note's `eps_bar`, which plays the role of the theorem's `eps_int` because Lemma 5.2's radius is `C_B eps_bar`. Of the two options in R5, I chose to add the conditions to the ceiling (edit 9). Section 6 item 5 (inserting `chi_E`) is covered by the same ceiling and is unchanged. |
| 9 | R5 | Section 8 item 5 (coupling ceiling) | APPLIED | Added `C_B eps_bar <= a_c` and `eps_bar e^{-delta d} <= eps_m/2`, for the stronger half. |
| 10 | R10-a | Section 8 item 1 | APPLIED | `2 <= L_flat < L/2` became `2 <= L_flat` and `L_flat^2 < L`, citing Y 65481, where Y uses it, and Y 63876, which states only `2 <= L_flat < L/2`. By hand: for `L >= 4`, `L_flat < sqrt(L) <= L/2`, so (L3) of section 5.4 still holds and Table 5.4 case (c) is unaffected. For `L = 13`, `L_flat` is 2 or 3. |
| 11 | R10-b | Section 8 items 1 and 2 | APPLIED | `delta_0` now sits in step 1, before `M_2`, with the reason `c delta_0 M_2 >= 1` and "`delta_0` fixed together with `L`" (Y 62001). It is removed from step 2, which now names only `C_mu` of (Y-JOIN). Y 62068 uses the same `delta_0` for the localized minimisers (`e^{-c delta_0 dist}`). |
| 12 | R10-b | Section 8 item 3 | APPLIED | Added `M >= L^2 M_2` (Y 62001). |

Not applied, because row 645 does not name them (the check marks them optional or as wording only):

| # | Item of the check | Status | Reason |
|---|---|---|---|
| 13 | Item (1): T8 wording on the unexplored-bond factors (Y 77746-77747) | NOT APPLIED | Optional wording, not named in row 645. |
| 14 | Item (3): "No domain depends on `omega`" is false for T6, though harmless | NOT APPLIED | Wording only, not named in row 645. The sentence stays as it was. |
| 15 | Item (6): cite Y 65000-65004 and 64265-64267 next to (E1) for case (c) in `K` | NOT APPLIED | A citation precision, not named in row 645. |
| 16 | Item (7): add Y 64108-64137 and Y 64590-64593 to the evidence for Proposition 5.3 | NOT APPLIED | A citation addition, not named in row 645. |
| 17 | R10-c: put `a_0, a_1, C_B, C_3` after step 3 if they depend on `M` | NOT APPLIED | Not named in row 645. The check calls it a free reorder. |
| 18 | Item (10): add the fit Y 71861 to step 5 | NOT APPLIED | Not named in row 645. |
| 19 | Header status line of `inset-chart.md` ("Not checked by another model") | NOT APPLIED | Not a repair. That line is for the lead to update. |

## What stays open

The edits change no conclusion. Theorem 5.6 is still an implication from H-GEO, (F1-Y) and the six inputs of Y, which are (Y-PATH), (Y-JOIN), (Y-DENS), (Y-CONT), (Y-BELT) and (Y-MEAN). None is rebuilt. Still open, as in the check: convention D, the main step (Y 63876, 71336-71405), the earlier transitions, the fit Y 84261 with `n* <= l(Omega_0)`, and the kernel comparison D2 on the rim sector. No model other than the writer has checked these edits.

Status: finished 2026-11-10.
