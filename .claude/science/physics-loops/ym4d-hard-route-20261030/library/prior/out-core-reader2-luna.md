2 findings

## Repo search

The task says the lead searched `origin/main` and open YM4D PRs #10114,
#10133, #10134 and #10141 before queuing this reader check, but it supplies no
target-specific hit lines. The local `library/prior/repo-search-2026-11-08.md`
is a retroactive search for row 531's unrelated targets; I did not treat it as
the search record for this proposition. `library/open-registry.md:1003` names
`CORE-GAPS` as the owner of the underlying geometry proof and records that
proof, its checks, the outward note and the earlier reader rows 659-660. This
is the exact mathematical work behind the drafts, but the present task is the
separate final-wording check. I read the registry entry and the final drafts.
The earlier reader reports' fixes are present; I did not repeat them. The
requested `library/prior/core-reader2-luna.md` is absent.

Provenance: Codex (gpt-6-luna, high), checkout `4f3c55a7a`; outward-text
reader check, not an audit. This report grants no scientific status.
Source authorship: Ethan Sussman and Levent Alpoge; their text is coauthored
with Claude and Codex.

## 1. Clarity and multiple meanings

| Finding | Our line | Reader problem | Proposed text |
|---|---|---|---|
| F1 | Note 129 | The notation `d` is used in the alternative to (R2) before it is defined at note 139. | Replace `$`d(\Omega_0^c,\Omega_1)\ge a_1`$` with `$`\operatorname{dist}_\infty(\Omega_0^c,\Omega_1)\ge a_1`$`. |

No other sentence was unclear, combined unrelated topics, or used one word
with two meanings in a way that could mislead these readers. The long theorem
statements enumerate quantified scope. Note 143 distinguishes the two uses
of `h` locally.

## 2. Internal material

| Finding | Our line | Reader problem | Proposed text |
|---|---|---|---|
| F2 | Issue 7, link target | The destination exposes the internal lane path `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-core.md`. The visible link text is neutral, but the URL is internal. | Replace the destination with the stable public snapshot permalink: `[This note](<public snapshot permalink>)`. No snapshot permalink is established in the checked files, so this link needs that URL before use. |

Neither file displays a row number, registry name, model name outside its
provenance line, or the word `CORE`. Manuscript tags and paths identify your
source material. The note link's destination is the sole internal item found.

## 3. Address, attribution and claims about your manuscript

The drafts address Ethan and Levent in the second person. Their source claims
stay within the cited lines. Issue 5 says no proof follows the proposition;
it does not say there is no local explanation. The eight-layer explanation
at Y 62089-62094 is separately reported. The two provenance lines are the
only places that name authors or checkers, as requested.

## 4. Every cited source line

I read the cited ranges in `/tmp/ym4_1400.tex` and `/tmp/ym4_ba.tex` at the
specified revisions. Each row names one source citation from the outward
files. “Holds” means the cited text supports the wording; it does not verify
the mathematical truth of the source statement.

### Issue citations

| Our line | Source citation | Result |
|---|---|---|
| 5 | Y 62080-62101 | Holds: the proposition ends at 62101; the next paragraph begins at 62103. “No proof follows” is local to this proposition. |
| 5 | Y 62082-62087 | Holds: all three displayed relations and the level-unit qualification appear there. |
| 7 | Y 61911 | Holds: the torus admissibility floor is stated. |
| 7 | Y 61983-61985 | Holds: for `t >= 2`, `H_t` is the eight-layer enlargement of the hull of the live region. |
| 7 | Y 61986-61990 | Holds: the initial `Z^[0]` has two layers of padding, and `Z_t` is the final boxed set. |
| 9 | Y 645-648 | Holds: layer addition/removal and hulls are defined in the named partition. |
| 9 | Y 63684-63690 | Holds: the box enlargement and quiet-component outputs are stated. |
| 9 | Y 63750-63763 | Holds: the box enlargement is in sup distance and the quiet-box formulas are given. |
| 9 | Y 63760-63766 | Holds: the displayed quiet boxes and unlabeled-region convention are present. |
| 9 | Y 63775-63809 | Holds: the change-of-scale index, weights, prepared boxes and cube-grid conclusion are stated. |
| 9 | Y 62128 | Holds: the exact words “Marks wait” occur, followed by the standing-mark condition. |
| 9 | Y 62115 | Holds: the drop-out rule leaves `Lambda_t cap X` empty. |
| 9 | Y 62170-62171 | Holds: at the top index, the drop-out keeps each indicated `q` outside `Lambda_s`. |
| 9 | Y 63692 | Holds: the text concludes that no cell, box or box neighbourhood wraps. |
| 9 | Y 63770-63771 | Holds: the small-box cutoff gives at most 100 cells along a side. |
| 11 | Y 1586 | Holds: `Z_k(h)` is called the live region after healing. |
| 11 | Y 61973 | Holds: the step's live region and the sequence's initial `Omega_0` are stated. |
| 11 | Y 61973 | Holds: the initial `Omega_0=Omega_1^~` convention is the cited basis for the alternative reading. |
| 11 | Y 62105-62106 | Holds: healing fills entries through `t`; an island fills below `t` and fills `Omega_t`. |
| 13 | BA 1612-1615 at commit `c7fef8b21b58`, `YM4/BA/YM4_BA.tex` | Holds: the text imposes the strict separation condition for `0 <= j < k` with `rho_gap >= 4L`. Lines 1605-1611 give the hierarchy/block hypotheses; the issue compares only the separation formula and explicitly leaves constants and units un-compared. |

### Note citations

| Our line | Source citation | Result |
|---|---|---|
| 9 | Y 62080-62101 | Holds: proposition location and its full span. |
| 9 | Y 62080 | Holds: opening proposition sentence quoted at note 9. |
| 11 | Y 62080 | Holds: the proposition is at this line. |
| 11 | Y 62082-62087 | Holds: the three displayed relations and unit note are present. |
| 17 | Y 62094-62098 | Holds: the local eight-layer explanation and two creation types are stated. |
| 17 | Y 62101 | Holds: the proposition ends there. |
| 22 | Y 62101 | Holds: end of the proposition. |
| 22 | Y 62103 | Holds: the next paragraph begins there. |
| 23 | Y 62080 | Holds: first occurrence of the label. |
| 23 | Y 62128 | Holds: the text says the proposition applies to the geometric label. |
| 23 | Y 63716 | Holds: the nesting is invoked there; the quoted phrase begins on line 63715, and note 23 cites both lines. |
| 31 | Y 61973 | Holds: the label sequence starts with the cited `Omega_0` rule. |
| 33 | Y 61973 | Holds: the live-region and initial-entry quotations are at this line. |
| 33 | Y 1586 | Holds: the “live region after healing” wording is exact. |
| 35 | Y 61973 | Holds: the layer and hull units are stated for step `t`. |
| 35 | Y 645-648 | Holds: the layer and hull definitions are quoted accurately. |
| 37 | Y 61980 | Holds: the boxing-map description is at this line. |
| 39-49 | Y 61983-61990 | Holds: the step formulas, two-layer padding and final `Z_t` definition. |
| 49 | Y 71099-71100 | Holds: the pre-operation region contains the two-layer enlargement. |
| 51 | Y 62096 | Holds: the level-`t` creation cells are `M Rcheck_t` cubes. |
| 51 | Y 642-644 | Holds: `pi_j` is the partition of centered half-open `M`-cubes. |
| 51 | Y 63749 | Holds: the side `a_i` of a level-`i` cell is stated. |
| 51 | Y 63774-63775 | Holds: the side `u_i` of an `M`-cube is stated. |
| 53 | Y 62001 | Holds: the power-of-`L` running-minimum definition and nesting claim. |
| 53 | Y 62195 | Holds: `N_t=Rcheck_t` is non-increasing. |
| 53 | Y 63882 | Holds: the later scale comparison with `log x_k`. |
| 55 | Y 63684 | Holds: depth, class, quarantine and box enlargement are introduced. |
| 55 | Y 63750-63752 | Holds: box enlargement by sup distance in the lift. |
| 57 | Y 62103 | Holds: `t_flat` and the prepared nest are introduced. |
| 57 | Y 62105 | Holds: the healed replacement rule. |
| 57 | Y 62106 | Holds: the island replacement and remaining top region. |
| 57 | Y 62107 | Holds: a drop-out remains in `Z_t`. |
| 57-63 | Y 62110-62115 | Holds: the drop-out formulas and unchanged-entry conclusion. |
| 65 | Y 62121 | Holds: marks persist until swallowed; the retained pre-operation regions are described. |
| 71 | Y 62128 | Holds: determining/action sequence distinction and stopping interpretation. |
| 73 | Y 62161-62168 | Holds: the reindexed-cell formula for `Omega`. |
| 73 | Y 62169-62171 | Holds: the corresponding `Lambda` rule and top-level exclusion. |
| 75 | Y 62174-62180 | Holds: step copying, operation overwrite and drop-out entries. |
| 77 | Y 63714-63715 | Holds: the before/after labels are defined. |
| 79 | Y 1640 | Holds: `T_ell` is defined as the four-torus. |
| 79 | Y 61911 | Holds: the torus admissibility floor is stated. |
| 79 | Y 63692 | Holds: the no-wrapping conclusion. |
| 81 | Y 650-651 | Holds: `L >= 13` odd. |
| 65 | Y 62124-62125 | Holds: the stopping-vector formulas are displayed. |
| 87 | Y 645-648 | Holds: the general layer/hull convention. |
| 87 | Y 63684 | Holds: box enlargement is by pushing faces outward by cells. |
| 87 | Y 63686-63690 | Holds: the quiet-component formulas. |
| 87 | Y 63760-63763 | Holds: the quiet-box equations. |
| 87 | Y 63750-63751 | Holds: the quoted sup-distance enlargement phrase begins on 63750 and continues on 63751. |
| 89 | Y 63684 | Holds: `H_i` is the hull in level-`i` cells of `X cap Z_{i-1}`. |
| 89 | Y 63756 | Holds: the displayed containment for `G_{i-1}` and `H_i`. |
| 89 | Y 63752-63753 | Holds: `G_h` is a nonempty box. |
| 89 | Y 63760-63766 | Holds: the quiet-box equations and no-label convention. |
| 95 | Y 63766-63767 | Holds: unlabeled `Omega_i,Z_i` are assigned to `S'_k`. |
| 97 | Y 63775-63777 | Holds: the final equal-scale index and its range. |
| 99-101 | Y 63783-63784 | Holds: all three `w_i` formulas. |
| 103-107 | Y 63798-63804 | Holds: the prepared-box cases and formula. |
| 109 | Y 63805-63809 | Holds: the grid-alignment and `M`-cube conclusion. |
| 111 | Y 62128 | Holds: the disjoint-window statement. |
| 113 | Y 62115 | Holds: the top `Lambda_t` entry remains empty for the drop-out. |
| 113 | Y 62171 | Holds: the drop-out keeps the indicated `q` outside `Lambda_s`. |
| 113 | Y 62121 | Holds: the mark persists until swallowed. |
| 115 | Y 63692 | Holds: no-wrapping conclusion. |
| 115 | Y 63770-63771 | Holds: the 100-cell side cap. |
| 117 | Y 63715-63716 | Holds: labels before/after the operation and the nesting invocation; the quote starts at 63715. |
| 117 | Y 63716-63720 | Holds: the decrease of `Z_i` and the unchanged/enlarged regions are described. |
| 117 | Y 63714-63741 | Holds: these lines contain the full cited part of the earlier-label argument. |
| 123 | Y 1586 | Holds: the live-region wording after healing. |
| 123 | Y 62106-62107 | Holds: island and drop-out regions remain in the stated top set. |
| 125 | Y 62105 | Holds: healed entries are replaced for `l <= t`. |
| 125 | Y 62106 | Holds: island entries are replaced for `l < t` and at `Omega_t`. |
| 125 | Y 61973 | Holds: the sequence starts at `Omega_0=Omega_1^~`. |
| 129 | Y 61973 | Holds: the sentence cited for the alternative standing rule. It states the initial rule; the note labels “at every moment” as a reading. |
| 129 | Y 61900-66000 | This is a search interval, not a claim that the whole interval was read. I searched it for `Omega_0`; the occurrences listed next are all the matches. |
| 129 | Y 61973, 62078, 62245, 63032, 63039, 63374 | Holds: these are the `Omega_0` occurrences found by the bounded search. None states a healing update for `Omega_0`. |
| 139 | Y 63750-63752 | Holds: the box enlargement and signed-distance convention are stated. |
| 157 | Y 61990 | Holds: `Z_t` is identified as the final `Z^[n]`. |
| 157 | Y 71099-71100 | Holds: the pre-operation `Z_h` contains the two-layer enlargement. |
| 198 | Y 63819-63820 | Holds: the cited separation starts at 63819; `Z''_i` is named on 63820. |
| 222 | Y 63820-63824 | Holds: the early and late prepared-box separations are stated. |
| 246 | Y 62080 | Holds: the proposition and prepared-sequence scope. |
| 246 | Y 62107-62115 | Holds: drop-out fates, stage window and top-entry result. |
| 246 | Y 62128 | Holds: determining sequence and stopping after stages. |
| 279 | Y 62140-62142 | Holds: top entries use recorded step data and are fixed under a stage-index change. |
| 294 | Y 62174-62180 | Holds: copying, overwriting, unchanged exterior entries and drop-out updates. |
| 319 | Y 63714-63766 | Holds as the source range for the earlier-label argument used to order the induction. |
| 333 | Y 62089-62094 | Holds: equality range, change-of-scale index and `w_j-w_{j+1}` gap are stated. |
| 339 | Y 650-651 | Holds: `L >= 13` odd. |
| 339 | Y 63805-63809 | Holds: oddness is used in the grid-alignment conclusion for prepared boxes. |
| 340 | Y 62001 | Holds: the running-minimum definition and power-of-`L` condition. |
| 340 | Y 62001 | Holds: the same line states nested partitions and non-increasing size. |
| 340 | Y 83084 | Holds: `g_j=x_j^{-1/2}`. |
| 340 | Y 61911 | Holds: `g_j <= gamma` is one of the coupling-flow assumptions on that line. |
| 340 | Y 1102-1103 | Holds: the frame definition states `gamma < e^{-1/2}`. |
| 340 | Y 61911 | Holds: this line also supplies the coupling ceiling referenced in the final sentence. |
| 341 | Y 61911 | Holds: the torus admissibility floor. |
| 341 | Y 63692 | Holds: the no-wrapping conclusion. |
| 343 | Y 650-652 | Holds: the cited inequalities on `R_1`, `M_1'` and `M`. |
| 349 | Y 62130-62133 | Holds: the retained-space identity and `l <= j` restriction. |

Quoted words were checked against these passages. The earlier Sol reader's
pinpoint repairs are present in the final note: note 23 cites 63715-63716;
note 51 includes 642-644 and 63774-63775; note 81 cites 650-651; note 87
includes 63750-63751; note 222 includes 63820; and note 339 cites 650-651.
No uncorrected quote mismatch was found.

## 5. GitHub rendering

I read `/tmp/out-core-render/issue.html` and `note.html`. The issue has 22
`math-renderer` elements and the note has 952. The HTML scan found no raw
math-like delimiter outside a renderer; no formula appeared in a code or
preformatted block. The formulas in both drafts are rendered. No correction.

## 6. Links

| Our line | Commit, repository and path | Existence check |
|---|---|---|
| Issue 5; Note 5 | Sussman-Alpoge commit `c7fef8b21b5846e1b5806a7d4f915737b9130c27`, `YM4/YM4_1400.tex` | Exists (HTTP 200). Its bytes match `/tmp/ym4_1400.tex` at the supplied revision. |
| Issue 7 | This repository commit `9c40b1d4bdc2371c45c083aa97becba8b0cc9334`, `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-core.md` | Exists at the linked commit (`git show`); byte-identical to the final note read here. Its path exposes the internal lane name; see F2. |
| Issue 13, unlinked source reference | Sussman-Alpoge commit `c7fef8b21b5846e1b5806a7d4f915737b9130c27`, `YM4/BA/YM4_BA.tex` | Exists (HTTP 200); lines 1605-1620 were read. It is a source reference, not a Markdown hyperlink. |

These are all the links in the two rendered files. The source-file hyperlink
is repeated once in each file; both point to the same existing path.

## 7. Symbols before definition or quotation

F1 is the only ordering issue found: note 129 uses `d` before note 139 defines
it. Other early symbols are in quoted source passages or introduced locally.
The proposed `dist_infty` replacement uses notation already displayed from
your proposition at issue 5.

The requested additions were read as mathematical remarks, not checked as a
proof. Remark 1 (note 331) follows from (N) and (G): (N) gives
`Omega_j^c subset Z_j`, and distance to `Omega_{j+1}` cannot decrease when
the first set is replaced by its subset. In Lemma 4, the cube condition on
each `D_i(X)` is supplied in Theorem 6 at note 317: (H3) and (S7) supply
`h < i <= t`, while `D_h(X)=Z'_h cap X` follows from the inherited cube
property. The alternative to (R2) at note 129 is explicitly called a reading;
under that reading, enlarging `Omega_1` and then taking its one-layer
enlargement contains the former `Omega_0` and the healed component. The issue's
BA comparison is accurate for BA 1605-1620: BA imposes the strict separation
as a hypothesis after stating the hierarchy assumptions; the formula has the
same complement-to-next-region shape, and the issue does not equate scales or
constants.

No mathematical status is changed. I wrote only this report. Concurrent
working-tree changes to `FINISH.md` and `library/open-registry.md` were visible
at final inspection and were left untouched.
