8

## Repo search

The lead's `prior/repo-search-2026-11-08.md` predates this note. It found related continuation estimates and history bookkeeping, not these three complete results. I read the digest and fetched the relevant PR sources. PR 10114, `INDUCT.md:486-504`, gives a conditional contraction/common-lag criterion. PR 10141, `research/ym4d/library/out-mu.md:8-32,69-82,189`, concerns admitted regular minimisers. Its `in1.md:66-74,171-173,205-216` supplies bookkeeping conventions and names remaining payment and sum inputs. None supplies the rounded-scale window comparison, the preparation-index existence argument, or the action-cell invariant. These are method neighbours, not duplicate proofs. The PR heads resolved to `f76f6c649cff7dffbab664d8976e680e8f287fe9` and `fb99b4dddc7254e6124ac124887d58eeb3a77802`.

`prior/scale-reader-sol.md` is absent. Registry R7-COUNT records the underlying proof work; this task is its separately assigned final reader check. I did not reopen that work. I read the 18 corrections in `scale-note-faith.md` and assessed the edited files, not their superseded wording. The incomplete quotation ranges and missing Example F parameters corrected there are not findings here.

Provenance: Codex, gpt-6.1-sol, high; checkout `345ab3ffacfa0611e219a0251587abb294d4f45e`, 2026-11-10. Research reader report, not an audit or proof check; no status is granted. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the imported frame, geometry and manuscript passages. Balaban remains their cited geometric source.

Only this report is a repository output. I used the supplied GitHub renders. No post, source edit, commit or push was made. File retrieval, HTML inspection and Git-blob comparison are bookkeeping, not mathematical discharge.

## Reading convention and source identity

I = `library/scale-note-issue.md`; N = `library/posted/scale-note.md`. All I/N numbers below are current file lines. “Keep” in a proposed-text column means no replacement is needed.

Y = `/tmp/ym4_1400.tex`, 136,637 lines. Its Git blob is `72610b9f832e00a78097f5abaa5cec418c56ddae`. GitHub's contents API returns that same blob for `YM4/YM4_1400.tex` at `c7fef8b21b5846e1b5806a7d4f915737b9130c27`. Thus the supplied earlier-commit download is the file the drafts cite. EM and RT were fetched at that full commit into the requested `/tmp/ym4_em.tex` and `/tmp/ym4_rt.tex`.

I fetched the requested outline and CA-I once. Before using outline passages, I read the index README and the frame/action rows and neighbours in chunks 05 and 16, with the matching obligations. Bounded source reads were SA 6017-6035, 6095-6116 and 17433-17449. They provide the frame and action definitions and identify the waiting-window obligations. They are background here, not a fresh novelty or proof check. No CA-I claim is needed to decide the outward wording. The newer Y passages, EM 448-455 and RT 1027-1036 were read directly.

## 1. Wording

These eight numbered findings are distinct corrections; later tables refer back to them. F5 is a literal-quotation defect. F7 and F8 concern readability, not the mathematics.

| ID | Our line | Finding | Proposed text |
|---|---|---|---|
| F1 | N 286, first sentence | The final scope section still makes an unrestricted absence claim. N 98 correctly limits the search result. This is a remaining occurrence, not a request to undo the earlier correction. | `In the passages found by our search, we found no explicit condition (G) or proof of the one-window comparison.` |
| F2 | N 244, first two sentences | “Your text does not define” makes another manuscript-wide claim. The two quoted lines concern collars and separation; neither establishes this absence. | `For this note we use reading (K): a component of a union of closed cells of one level is a connected component of that set.` |
| F3 | N 287, last sentence | An intention to cover one window would not identify the authors' unstated ceiling with this particular sufficient condition. | `If it is, (G) is one sufficient ceiling that makes this comparison explicit.` |
| F4 | I 5, sentence beginning “Lines 1475-1477” | “Not a union of cells” loses the source's distinction between the larger cells and the fallback M-cubes. Y says “those cubes,” not arbitrary cells. | <code>Lines 1475-1477 set $`\mathsf s_j=M`$ when $`\Lambda_j`$ is not a union of "those cubes".</code> |
| F5 | I 5, quoted phrase | Y 73382 starts “The scale comparison.” The draft quotes “the scale comparison.” The capital differs letter for letter. | <code>At lines 73382-73383 your text uses "The scale comparison $`\check R_{h_t}\le L\check R_t`$" between levels that are $`\mathsf N_t=\check R_t`$ apart.</code> |
| F6 | I 10; N 9-11 | The opening summaries omit restrictions that the statements retain. Corollary S requires a nonnegative window start. Lemma K also requires that domain. The note's Part 3 roadmap omits its readings, although I 12 now gives them. Make these roadmaps conditional explicitly. | I 10: <code>Corollary S: assume your frame and the added ceiling (G). Your comparison holds for every $`t`$ with $`h_t=t-\check R_t\ge0`$. The ceiling depends only on $`r,L,c_5,\bar B`$, so it fits your order of constants (lines 72930-72931, 72946).</code> N 9: `Part 1 treats your comparison at lines 73382-73383. Your frame definition alone does not give it (Example F). Under the frame and (G), it holds whenever the waiting window starts at a nonnegative level (Corollary S).` N 10: `Part 2 proves the existence, range and side inequalities of your preparation index at lines 63775-63778. Lemma K assumes the frame, (G), L at least 4, and a nonnegative window start.` N 11: `Part 3 proves the action-cell invariant from the quoted rules and reading (K) (Lemma C). Corollary C applies the first case of lines 1475-1477 when “those cubes” means the cells of that level.` |
| F7 | N 220, first quotation | The excerpt retains “Both statements” after quoting only one statement. Its other antecedent is the source's preceding nesting/gap assertion, omitted here. | <code>At line 62080 you state: "Every large-field region and every creation set is a union of cells of its own level." You state there that this holds for regions produced by steps.</code> Then retain the construction discussion. |
| F8 | N 13 and 291, first sentence | “Computation” normally includes the hand calculations displayed throughout the note. The intended exclusion is a computer calculation. | `No step relies on a computer calculation.` |

No other sentence needs a change merely for containing several formulas or a list of hypotheses. The long source quotations should retain the authors' wording.

## 2. Internal material

| Our line | Check | Proposed text |
|---|---|---|
| I 1-17; N 1-291 outside N 3 | No visible queue row, registry name, internal proof filename or model name was found. G, F, K, W, C and the R-* labels are defined within the outward note. | Keep, subject to the wording findings. |
| I 18; N 3 | Model names occur in provenance, as allowed. | Keep. |
| I 7, hyperlink destination | The URL contains the lane path and `scale-note.md`; the visible text is “This note.” This is the deliberately linked artifact, not an unexplained internal prerequisite. Its exact destination is checked below. | Keep. |

## 3. Address and manuscript claims

| Our line | Result | Proposed text |
|---|---|---|
| I 3-16; N 5-290 | The authors are addressed as “you/your/yours.” “We/ours” denotes the contributors. Source filenames, labels and the repository identifier do not address them in the third person. | Keep. |
| I 5; N 21, 181 | “No proof ... at those lines” is a local claim. The opened lines state/use the comparison or select the index; they contain no derivation. | Keep. |
| N 98 | The absence claim is limited to passages found by the search. | Keep. |
| N 244 | Manuscript-wide claim about “component”; the citations do not establish it. | F2. |
| N 286 | The sentence “(G) is a condition that your text does not state” is broader than the supported search report. | F1. |
| N 287 | The unknown intended ceiling cannot be identified with (G) merely from its intended purpose. | F3. |
| N 210 | The colon enumerates the index, range and two inequalities. Read with §2.1, it does not claim to prove the next prepared-box construction, which begins at Y 63778. | Keep. |

## 4. Every numerical citation

There are 20 numerical citation occurrences in I and 77 in N. Repeated references are separate rows. The named RT anchor adds two nonnumerical references, recorded too. Every cited source range below was opened. “Supports” concerns the source content; it does not certify the note's proof.

Quoted visible prose was compared after joining source line wraps and removing TeX emphasis/display wrappers. Math delimiters, `FitMath`, spacing and equivalent braces are transcribed for GitHub. These are not byte-identical quotations of TeX source. The RT `cref` is transcribed as a code label. Apart from F5, the quoted words match under these declared formatting conversions.

### Issue draft

| Our line | Citation | What the opened lines contain / result | Proposed text |
|---|---|---|---|
| I 1 | Y 73382-73383 | The named scale comparison and its inequality. Correct title locator. | Keep. |
| I 1 | Y 63775-63778 | Last equality index, range and both side inequalities. Correct title locator. | Keep. |
| I 5 | Y 73382-73383 | “The scale comparison” and the displayed inequality. Mathematical content agrees; quoted capital differs. | F5. |
| I 5 | Y 63775-63777 | Selection of the last index and `h<k_0<=k-2`; no proof there. | Keep. |
| I 5 | Y 1475-1477 | First case for a union of “those cubes”; fallback M otherwise. Supports the two-case rule, not the unqualified word “cells.” | F4. |
| I 5 | Y 1110 | `check R_j <= L check R_{j+1}`. One step. | Keep. |
| I 5 | Y 73081-73082 | Adjacent ratio in `{1,L^{-1}}`; nonconsecutive size drops. One step, plus spacing of drops. | Keep. |
| I 5 | RT `rt:eq-adjacent-cell` | Label at RT 1032; ratio at 1033; argument at 1027-1031. Correct anchor. | Keep. |
| I 9 | Y 1102-1113 | Frame floor, gamma range, drift, minimum, adjacent ratio and rounding definition. The cited definition is the one Example F addresses. | Keep. |
| I 10 | Y 72930-72931 | `r,L,c_5,bar B` precede gamma. Supports the constants order. | Keep citation; F6 clarifies the corollary domain. |
| I 10 | Y 72946 | Another ceiling of the same kind preserves the order; includes its supremum formulation. | Keep citation; F6. |
| I 11 | Y 63775-63778 | The index, its stated range, and both side inequalities. The bullet now states the frame, (G), `L>=4` and `h>=0`. | Keep. |
| I 12 | Y 1475-1477 | Two-case profile rule. The corrected bullet explicitly supplies both readings for its first-case conclusion. | Keep. |
| I 14 | Y 1102-1113 | The frame definition is present. | Keep. |
| I 14 | Y 1121 | Waiting depth equals the rounded scale. | Keep. |
| I 14 | Y 61973-61985 | Step tests, cell hull/layer convention and the formula for `Omega_t^c`. Supports this part of the stated rule list. | Keep. |
| I 14 | Y 62080 | Cell-union assertion for step-produced regions; distinguishes prepared sequences. | Keep. |
| I 14 | Y 62105-62128 | Three fates, stored regions, partial remake formulas, action sequence and waiting marks. | Keep. |
| I 14 | Y 62174-62177 | Step copying, operation overwriting and no changes outside the class. | Keep. |
| I 14 | Y 73081-73092 | Physical cell partition relation and nested-label relations. | Keep. |
| I 16 | Y 62001 | The quoted phrase “gamma is small” is present. Whether its ceiling covers a whole window is not specified there. | Keep. |

### Note

| Our line | Citation | What the opened lines contain / result | Proposed text |
|---|---|---|---|
| N 9 | Y 73382-73383 | Exact comparison being treated; its use, not a proof. | Keep citation; F6. |
| N 10 | Y 63775-63778 | Exact index target, range and side inequalities. | Keep citation; F6. |
| N 11 | Y 1475-1477 | Exact two-case rule; application requires the note's readings. | Keep citation; F6. |
| N 19 | Y 73376-73384 | The entire quoted carrier/shell/comparison passage is within this corrected range. Visible prose and formulas agree. | Keep. |
| N 25 | Y 1110 | Adjacent frame inequality exactly as displayed. | Keep. |
| N 26 | Y 73081-73082 | Quoted size sequence and nonconsecutive drops. Words agree. | Keep. |
| N 27 | Y 62001 | Quoted adjacent inequality and nonconsecutive-drop explanation using x and small gamma. Words agree. | Keep. |
| N 28 | EM 448-452 | Quoted minimum-drop bound, logarithmic ratio and rounding argument. Words agree. This proves an adjacent ratio above its stated floor. | Keep. |
| N 29 | RT 1027-1033 | Quoted drop bound, cell condition and adjacent ratio. Words agree after the disclosed `cref` transcription. | Keep. |
| N 29 | RT `rt:eq-adjacent-cell` | Label at 1032 and display at 1033. | Keep. |
| N 35-41 | Y 1102-1113 | Frame introduction, all three displayed clauses and rounding definition. Quoted words and inequalities agree. | Keep. |
| N 43 | Y 1121 | Exact waiting-depth quotation. | Keep. |
| N 43 | Y 73378 | Defines `h_t=t-N_t`. | Keep. |
| N 45 | Y 62001 | States `r>=2`. | Keep. |
| N 45 | Y 650-651 | States `L>=13` and “odd.” Both are inside this corrected range. | Keep. |
| N 45 | Y 72936 | The two identities for lambda and c_5 are present; the note separately assumes their signs. | Keep. |
| N 57 | Y 1102-1110 | All frame conditions being checked are here. Their validity for F is the note's calculation, not a result supplied by this citation. | Keep. |
| N 70 | Y 73081-73082 | Adjacent ratio and nonconsecutive-drop assertion. The example's separated drops address that assertion. | Keep. |
| N 70 | Y 62001 | Contains the same nonconsecutive-drop claim. The sentence's antecedent is that claim, not every assertion in the long source line. | Keep. |
| N 80 | Y 1102-1113 | Defines the frame class for the counterexample claim. | Keep. |
| N 80 | Y 73382-73383 | Contains the comparison the example violates. | Keep. |
| N 90 | Y 72930-72931 | The displayed constants order, including its quoted tail. | Keep. |
| N 96 | Y 72946 | Exact quoted criterion for a condition fitting the order; also expressly permits another ceiling. | Keep. |
| N 98 | Y 62001 | Exact quoted nonconsecutive-drop explanation ending “gamma is small.” Does not identify the intended window ceiling. | Keep. |
| N 126 | Y 63775-63777 | Exact quoted last-index and range fragment. | Keep. |
| N 126 | Y 63749 | Defines `a_i=M check R_i L^i`. No quotation of “set” is attributed to this single line. | Keep. |
| N 126 | Y 63774 | Defines `u_i=ML^i`, hence u_k by substitution. | Keep. |
| N 126 | Y 63684 | Defines `k_flat=k-N_k`, with source restriction at least 1. The note's h is a renaming; its algebraic lemma allows h=0 too. | Keep. |
| N 171 | Y 1121 | `N_t=check R_t` by the source's indexed definition. | Keep. |
| N 173 | Y 73382-73383 | Exact inequality identified as the corollary's target. | Keep. |
| N 179 | Y 63774-63778 | Entire quoted u-definition, last index, range and side inequalities. Words and formulas agree. The quotation stops before the next construction sentence. | Keep. |
| N 181 | Y 63748-63749 | “set” and the full quoted cell-side definition are both within this corrected range. | Keep. |
| N 181 | Y 63684 | Source depth definition; same h renaming as N 126. No index-existence argument is given there. | Keep. |
| N 185 | Y 650 | `L>=13`, exactly the fact cited here. The note does not attribute “odd” to this line alone. | Keep. |
| N 192 | Y 1102-1103 | Frame entries are at least the stated floor, and `0<gamma<e^{-1/2}`. | Keep. |
| N 192 | Y 1109 | Rounded scale is R of the running minimum. Read jointly with the next citation. | Keep. |
| N 192 | Y 1113 | R is the least L-power above the logarithmic power. Read jointly with 1109. | Keep. |
| N 194 | Y 1110 | The adjacent bound used in Step 3. | Keep. |
| N 210 | Y 63775-63778 | Contains each of the explicitly enumerated index conclusions. Its next, unfinished construction sentence is outside that enumeration. | Keep. |
| N 220 | Y 62080 | Both quoted sentences are exact. “Both statements” has an antecedent in the source omitted from this excerpt. | F7. |
| N 220 | Y 61973 | Exact hull/layer quotation. | Keep. |
| N 220-224 | Y 61981-61985 | Contains the complete `Omega_t^c,H_t` formulas, including the t=1 case. Beginning on a blank line is harmless. | Keep. |
| N 226 | Y 62174 | Exact step-copying quotation. | Keep. |
| N 228 | Y 63684 | Exact class-component quotation. | Keep. |
| N 228 | Y 62105 | Exact healed replacement and “X leaves the label” fragment. | Keep. |
| N 228 | Y 62106 | Exact island replacement fragment, with Lambda_t unchanged. | Keep. |
| N 228 | Y 62107 | Exact parenthetical failure condition and retained-X fragment. | Keep. |
| N 228 | Y 62110-62115 | Both region formulas; Lambda and S retain the `l<t` qualification; unchanged entries and empty Lambda_t intersection. The paraphrase preserves that restriction. | Keep. |
| N 228 | Y 62175-62177 | Complete operation-overwrite and outside-class quotation. | Keep. |
| N 230 | Y 62128 | Exact waiting-mark, nesting, disjoint-window and active-mark quotation. | Keep. |
| N 232 | Y 62001 | Exact nested-partitions sentence. | Keep. |
| N 232 | Y 73081-73084 | Entire quoted size-drop and coarsening/unchanged-partition sentences fit the corrected range. | Keep. |
| N 232 | Y 73066 | Exact compatibility sentence. | Keep. |
| N 234 | Y 73087-73092 | The three nested-label relations are present. The complement-nesting conclusion is a deduction, not a quotation. | Keep. |
| N 236 | Y 62121 | Exact stored-region quotation, including the analogous Lambda and S entries. | Keep. |
| N 236-240 | Y 62124-62125 | Both partial-remake formulas and their interval endpoints agree. | Keep. |
| N 242 | Y 62128 | Exact nu=0 action-sequence quotation after removing emphasis. | Keep. |
| N 242 | Y 73133-73140 | Full action-chain display and `Z_s^a=Z_s`. The intervening blank/display lines are harmless. | Keep. |
| N 244 | Y 73068 | Exact clause “Closed cells are used for collars.” This clause does not establish absence of a component definition elsewhere. | Keep quotation; F2. |
| N 244 | Y 62195 | Exact non-touching/separation fragment. It too does not establish that absence. | Keep quotation; F2. |
| N 262 | Y 63684 | Acting X is a component of Z_t after renaming k as t. | Keep. |
| N 268 | Y 62105 | Healed unions at all levels up to t. | Keep. |
| N 268 | Y 62175-62176 | Overwriting and swallowed marks; this range ends “ceases to.” The sentence finishes at 62177, separately cited in the same paragraph. Read those citations together. | Keep; optionally extend this range to 62177 for a self-contained reference. |
| N 268 | Y 62177 | Completes “stand” and states no entries change outside the class. The quoted locality clause agrees. | Keep. |
| N 269 | Y 62106 | Island replacement at lower levels and Omega_t; Lambda_t stays unchanged. | Keep. |
| N 270 | Y 62110-62115 | Exact drop-out changes and unchanged entries. The note addresses the terminal Lambda qualification explicitly. | Keep. |
| N 270 | Y 62177 | Outside-class locality. | Keep. |
| N 270 | Y 62115 | Empty Lambda_t intersection. | Keep. |
| N 276 | Y 1462 | Exact profile/action-sequence quotation. | Keep. |
| N 276 | Y 1475-1477 | Complete, exact two-case profile quotation. | Keep. |
| N 278 | Y 1475-1477 | Correct target rule. Applying its first case remains conditional on the stated readings. | Keep. |
| N 280 | Y 1476 | The words “those cubes” occur here. Corrected location. | Keep. |
| N 280 | Y 62096 | Exact `M check R_t`-cubes-of-level-t fragment. | Keep. |
| N 282 | Y 62245 | Both quoted fragments occur here: a region for pi_l and action regions made of coarse cubes. | Keep. |
| N 282 | Y 1476 | Contains fallback value `s_j=M`; “otherwise” follows at 1477. This sentence uses the value, not a purported full quotation of the case condition. | Keep. |
| N 287 | Y 62001 | Exact “gamma is small” phrase; its intention is left open by the note. | Keep citation; F3 repairs the following inference. |
| N 288 | Y 62080 | Literal `(119, p. 256)` is present. This report does not check the cited Balaban page. | Keep. |
| N 289 | Y 1476 | Literal “those cubes” is present. Corrected location. | Keep. |

Other quoted fragments are accounted for as follows. N 21's “puts every carrier inside” occurs across Y 73383-73384, already opened for N 19. I 12 and N 280/289 quote the same “those cubes” at Y 1476. I 16 and N 287 quote the small-gamma phrase at Y 62001. “Line n,” “component,” and the variable word “those” in explanatory prose are metalinguistic uses, not additional attributed manuscript sentences. There is no further unverified source quotation.

## 5. GitHub math and structure

I read both HTML files through their parsed text and element structure, comparing the text with the final Markdown. This is inspection of the supplied API render, not a browser or live-post check.

| Our file / lines | HTML result | Proposed text |
|---|---|---|
| I 1-18; `/tmp/scale-note-render/issue.html` | All 23 source formulas are inside 23 `math-renderer` elements. No formula is raw outside them or in code. Payloads agree after delimiter, whitespace and HTML-entity decoding. | Keep math syntax. |
| N 1-291; `/tmp/scale-note-render/note.html` | All 605 source formulas are inside 605 `math-renderer` elements. No raw formula or math-containing code block was found. Payloads agree under the same normalization. | Keep math syntax. |
| I 1-18 | Seven paragraphs; one four-item list; title label remains a bold paragraph, as in the source. Two links. | Keep. |
| N 1-291 | One h1, four h2, twelve h3; eight lists with 36 items; 83 paragraphs. No table in either source or render. Source list and heading structure is preserved. | Keep. |

The HTML encodes some less-than signs with another entity layer inside the renderer. Entity decoding recovers the source formulas. Their presence inside the required renderer is verified; actual client-side MathJax execution was not tested.

## 6. Every hyperlink

There are three hyperlink occurrences. Short commit `c7fef8b21b58` resolves through GitHub's public API to `c7fef8b21b5846e1b5806a7d4f915737b9130c27`. No sign-in page was fetched.

| Our line | Repository, commit and exact path | Existence / destination | Proposed text |
|---|---|---|---|
| I 5 | `ethanwsussman/Yang--Mills-LLM-experiment`; `c7fef8b21b5846e1b5806a7d4f915737b9130c27`; `YM4/YM4_1400.tex` | Public contents API confirms this path and the matching Y blob. HTML href equals Markdown href. No line fragment is supplied. | Keep. |
| I 7 | `jonathonreilly/qubit-lattice-axiom-framework`; `164df47e956d44b54dfed4de615705720ce22994`; `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/scale-note.md` | `git show` finds the exact path at that commit. Its bytes equal the current N. HTML href equals Markdown href. | Keep. |
| N 5 | `ethanwsussman/Yang--Mills-LLM-experiment`; `c7fef8b21b5846e1b5806a7d4f915737b9130c27`; `YM4/YM4_1400.tex` | Same verified public path and blob as I 5. HTML href agrees. | Keep. |

| Our line | Other path references, without hyperlinks | Result | Proposed text |
|---|---|---|---|
| I 5; N 5, 29 | `YM4/RT/YM4_RT.tex`, same external commit | Successful pinned raw fetch; named adjacent-cell label is present. | Keep. |
| N 5, 28 | `YM4/EM/YM4_EM.tex`, same external commit | Successful pinned raw fetch; cited proof is present. | Keep. |

The two manuscript paths belong to their repository; the note path belongs to this repository. None silently changes repositories or commits.

## 7. First use of symbols

| Our line | First use before definition or quotation | Proposed text |
|---|---|---|
| N 1, 9-10 | The title and roadmap use k_0, check R, h_t, L, gamma, h and k before the source quotations/definitions at N 19, 35-45 and 126. These are the authors' notation, but the roadmap has forward dependencies. | Use F6's prose roadmaps. In the title, `your preparation index` can replace the displayed k_0. This is a reader aid, not another mathematical finding. |
| N 19 onwards | M, xi, N_t and the carrier regions first occur in an attributed quotation. R, theta, lambda, c_5, bar B and r occur in the frame quotation. m_j, y_0, gamma_0 and e_i are defined on introduction. The action/mark symbols first occur in quoted rules or explicitly transcribed source displays. | Keep. |
| N 26, 232 | R without a check is quoted source notation; Y 73075 identifies it with check R. That identification lies before the quoted range, rather than being defined in the note. | Optional reader aid after N 26: <code>Here your $`R_j`$ means $`\check R_j`$ (line 73075).</code> |

## 8. Summary and scope, read for sense

This compares statements, not proofs. General constants are N 45's `r>=2`, odd `L>=13`, and nonnegative lambda, c_5 and bar B, except where a statement explicitly changes a bound. In particular, W's proof uses `L>=6`, already implied by the standing `L>=13`. K expressly singles out the weaker `L>=4` threshold.

| Our line / result | Comparison with the note | Proposed text |
|---|---|---|
| I 9 / Example F | Matches N 51-75, including r=2, L=13, lambda in [0,12], nonnegative c_5, the full gamma interval, and the sufficient bar B bound e^14. N 78 also gives the sharper e^14-e^5 threshold and explicitly says the round bound lies inside it. The issue does not falsely claim sharpness. | Keep. |
| I 10 / Corollary S and Lemma G | N 84-105 supplies (G) and its explicit positive ceiling from the four earlier constants. N 165 also requires a frame and h_t>=0; I 10 should state those. There is no separate issue bullet claiming the explicit gamma_0 formula. | F6. |
| I 11 / Lemma K | Matches N 185-188: frame, (G), L>=4, h>=0; existence, range, and both side inequalities. The edit has already fixed the missing hypotheses. | Keep. |
| I 12 / Lemma C and Corollary C | Matches N 250-254(i) and N 278. I 14 supplies the rules, and I 12 now expressly supplies (K) and the cube reading. The note additionally states the standing-mark and inactive-window invariants; the issue does not claim to list every conclusion. | Keep. |
| Lemma W / issue coverage | N 130 gives (S), the comparison throughout the window; N 131 gives (W), the preparation-index split. The issue advertises Corollary S, not an unconditional W or a counterexample to W. N 212 expressly says F breaks S, not W. | Keep. |
| N 9-11 / roadmap | The named results agree, but the opening roadmap should preserve their window domain and reading assumptions. | F6. |
| N 286 / scope | Full F parameter range is now present. It correctly declines to infer failure of a bar-B-independent ceiling from this single example. Its first sentence still overstates the absence result. | Keep the range and limitation; F1 for the first sentence. |
| N 287 / scope | Correctly leaves the intended small-gamma ceiling unresolved; the final identification with (G) is too strong. | F3. |
| N 288-290 / scope | Correctly retains the geometric rules and both readings as premises and limits the claimed application to the quoted passages. | Keep. |
| N 291 / scope | Mathematical hand-checkability is consistent with the displayed argument; “computation” is the wrong word for the excluded computer step. This reader pass does not certify formalizability. | F8. |

The report's findings concern the final text. It neither withdraws the existing proof checks nor supplies a new one. Only the requested report is left uncommitted in this detached checkout.
