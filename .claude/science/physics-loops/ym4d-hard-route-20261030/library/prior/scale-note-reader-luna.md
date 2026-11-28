6

## Repo search

The lead’s `repo-search-2026-11-08.md` predates this scale note and reports no search result for these three targets. Its closest hits are continuation sums, regular minimiser nesting, and retained-history bookkeeping. I checked the named PR excerpts recorded in `library/scale-note-faith.md`: PR #10114 `INDUCT.md:486-504` gives a conditional contraction criterion; PR #10141 `out-mu.md:8-32,69-82,189` concerns admitted regular minimisers; and `in1.md:66-74,171-173,205-216` gives counting conventions with open payment inputs. These are related methods, not the one-window comparison, index existence, or action-cell invariant. I opened the recorded PR excerpts at their repository paths: PR #10114’s `INDUCT.md:486-504` supplies a conditional product-contraction/common-envelope criterion; PR #10141’s `out-mu.md` and `in1.md` passages concern admitted minimiser nesting and counting inputs. None closes these three targets.

The later registry hit is `R7-COUNT` (`library/open-registry.md:1008`), which owns the mathematical count and records the scale note’s Lemmas G/W/C, Example F, and Lemma K. FINISH row 657 concerns those mathematical results. This queued row is a separate reader check of the final outward wording and citations. No other registry row assigns that reader check. The prior `scale-reader-luna.md` did not exist.

I also searched the required SA indexes: the outline index’s RF5 row (chunk 19; SA 20257-20265) is a definition with adjacent rounded-scale constraints, while the CA-I index’s 4.18 R3 row (chunk 09; CA-I 53668) lists an adjacent cell ratio as assumed. The nearby index rows define frames, cells and action sequences. These are related structures, not the one-window estimate or action-sequence invariant stated in YM4_1400.tex. The outline and complete account were already present at the requested `/tmp` paths; I used the indexed excerpts and did not refetch either file.

I read the issue draft, posted note, render files, and cited YM4/EM/RT source passages. I treated the cited Sussman-Alpoge text as their manuscript, with Claude and Codex as authors of that text, as requested. The result is a text review, not a proof check or status decision.

## Findings

| # | File line | Finding | Proposed text |
|---|---:|---|---|
| 1 | `scale-note-issue.md:5`; `posted/scale-note.md:5` | The source attribution names the repository and source file but omits the required authorship credit for the manuscript: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The provenance paragraph credits models for this note, not for their manuscript. | Issue: “This concerns your manuscript, by Ethan Sussman and Levent Alpoge with Claude and Codex, in `YM4/YM4_1400.tex` at commit …” Note: “The frame, geometric rules and notation come from your manuscript, by Ethan Sussman and Levent Alpoge with Claude and Codex as authors of their text.” |
| 2 | `scale-note-issue.md:5` | The quoted fragment begins lowercase “the scale comparison”; the cited source starts with uppercase “The scale comparison” at Y 73382. This is not letter-for-letter. | “At lines 73382-73383 your text uses the comparison …” (remove quotation marks), or capitalize the quoted initial “The”. |
| 3 | `scale-note-issue.md:10,12` | The summary is accurate as a weaker summary, but does not state each named result’s full scope as requested. Corollary S also assumes a frame and only covers `h_t >= 0`; those conditions are omitted. Lemma C additionally proves (ii) the mark property and (iii) equality off active windows, while the bullet reports only (i). Example F’s `bar B >= e^14` is a sufficient subrange, not the note’s exact frame range `bar B >= e^14-e^5`; it is valid but narrower. | Corollary S: “For every frame satisfying (G), and every `t` with `h_t=t-N_t>=0`, …” Lemma C: say that it proves all three clauses (i)-(iii), then retain the action-cell consequence. If the bullet intends the exact Example F range, use `bar B >= e^14-e^5` and include the stated ranges for `underline lambda`, `c_5`, and `gamma`. |
| 4 | `posted/scale-note.md:96` | This sentence packs the dependency order, a quoted rule, the ceiling interpretation, and the conclusion that no earlier constant is restricted into one long argument. The phrase “the kind named at gamma is a ceiling” is hard to parse on first read. | “The condition (G) depends only on `r,L,c_5,bar B`, which precede `gamma` in your order (lines 72930-72931). Line 72946 allows an additional ceiling at the last constant on which it depends. Thus (G) is compatible with that order and adds no restriction on an earlier constant.” |
| 5 | `posted/scale-note.md:9-12` | The opening summary uses label (G) before the note defines it at line 84. This is understandable on a second read but makes the summary temporarily opaque. | Add “(defined in §1.4)” at its first use, e.g. “under one added ceiling (G, defined in §1.4)”. |
| 6 | `posted/scale-note.md:286` | “A condition that your text does not state” is broader than the evidence directly checked. Y 62001 says `gamma` is small, although it does not state the exact condition (G). The next sentence narrows the uncertainty but does not narrow this first claim. | “The exact ceiling (G) is not stated in the passages cited here.” |

The prose addresses the authors directly where it makes claims about their manuscript. “Your text does not state” occurs at posted note line 286: the exact condition (G) is absent, but line 62001 does say `gamma` is small. Line 287 identifies the uncertainty about whether that qualitative ceiling is intended to cover one window. Narrow line 286 as proposed in Finding 6.

## Requested tables: prose, internal material, and address

### 1. Unclear, multi-topic, or ambiguous sentences

| File line | Finding | Proposed text |
|---|---|---|
| `posted/scale-note.md:96` | The sentence combines the parameter order, the general rule, and the conclusion that (G) fits. | Split it into the three sentences in Finding 4. |

No word appears to switch technical meanings in a way that changes the result. The note distinguishes adjacent-level comparisons from the one-window comparison.

### 2. Internal material

| File line | Finding | Proposed text |
|---|---|---|
| — | No row number, registry label, lane filename, or model name outside provenance appears in the outward prose. The posted-note URL contains its public repository path. | None. |

### 3. Second-person address and manuscript claims

| File line | Finding | Proposed text |
|---|---|---|
| issue 5; note 5 | The source manuscript lacks the required authorship credit for Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. | Use the source-credit wording in Finding 1. |
| note 286 | The exact (G) condition is not stated in the cited passages, but Y 62001 does say `gamma` is small. | “The exact ceiling (G) is not stated in the passages cited here.” |

The remaining manuscript statements use second-person address where they describe the authors’ text. The mathematical exposition does not need to address the authors in every sentence.

## Citation ledger

`Y` means `/tmp/ym4_1400.tex`; line references below were opened at the cited lines, with neighbouring lines. `EM` and `RT` are the two files fetched at commit `c7fef8b21b5846e1b5806a7d4f915737b9130c27`. “Holds” means the cited passage supports the adjacent sentence; it does not mean the mathematics was independently proved here. Repeated source ranges are listed at each place they are cited.

| Our line | Citation | Result |
|---|---|---|
| issue 1 | Y 73382-73383; Y 63775-63778 | Both statements occur there. The comparison is asserted at 73382-83; the index and side inequalities are stated at 63775-78. No proof is included in either cited range, as the issue says. |
| issue 1 | Y 1475-1477 | The two-case definition and `M`-cube sentence are there. The conditional branch is quoted accurately. |
| issue 1 | Y 1110; Y 73081-73082 | Both give adjacent-level ratios. “One step” is supported. |
| issue 1 | RT 1027-1033, label `rt:eq-adjacent-cell` | The lines state the running-minimum drop condition, cite the cell condition, and give `R_j/R_{j+1} in {1,L}`. Holds. |
| issue 9 | Y 1102-1113 | The frame definition and `R` definition are present. Holds. |
| issue 10 | Y 72930-72931; Y 72946 | Order puts `r,L,c5,Bbar` before `gamma`; 72946 allows an additional condition of the named kind. Supports the claimed order fit. |
| issue 11 | Y 63775-63778 | States exactly the claimed index range and side inequalities. |
| issue 12 | Y 1475-1477 | States the two-case rule. The report correctly makes its application conditional on the reading of “those cubes.” |
| issue 14 | Y 1102-1113; Y 1121; Y 61973-61985; Y 62080; Y 62105-62128; Y 62174-62177; Y 73081-73092 | These ranges contain the frame, waiting depth, step geometry, fate/update rules, mark/window statements, and nested-label/partition statements cited in the note. They support the listed inputs as quoted or summarized. |
| issue 16 | Y 62001 | Says `gamma` is small and that adjacent size drops are nonconsecutive. It does not specify (G) or a one-window bound. The issue’s uncertainty statement is supported. |
| note 9 | Y 73382-73383 | States the comparison and its carrier consequence. Holds. |
| note 10 | Y 63775-63778 | States the index range and side inequalities. Holds. |
| note 11 | Y 1475-1477 | States the two-case rule. The application claim is explicitly conditional on the note’s reading. |
| note 19 | Y 73376-73384 | The quoted passage is present through line 73384. It says the comparison “therefore” places carriers; it supplies no derivation of the comparison in this range. Holds. |
| note 25 | Y 1110 | Gives the one-step frame inequality. Holds. |
| note 26 | Y 73081-73082 | Gives the adjacent size ratio and nonconsecutive-drop statement. Holds. |
| note 27 | Y 62001 | Gives the adjacent inequality and says `gamma` is small. Quoted fragment matches, apart from omission of surrounding context. |
| note 28 | EM 448-452 | Quoted wording matches these lines across line breaks; the passage proves the adjacent ratio conditional on its floor/step assumptions. |
| note 29 | RT 1027-1033 | Quoted wording matches these lines across line breaks; it gives an adjacent ratio under the cited cell condition. |
| note 35 | Y 1102-1113 | The frame definition, inequalities, and definition of `R` match. Holds. |
| note 43 | Y 1121; Y 73378 | Defines waiting depth and gives `h_t=t-N_t`. Holds. |
| note 45 | Y 62001; Y 650-651; Y 72936 | Supplies `r>=2`, `L>=13` odd, and the two constant identities. The citation spans for `L` and “odd” are correct. |
| note 57 | Y 1102-1110 | These are the frame conditions checked by Example F. Holds. |
| note 70 | Y 73081-73082; Y 62001 | Supports nonconsecutive size drops and the qualitative claim about `gamma`. Holds. |
| note 80 | Y 1102-1113; Y 73382-73383 | Defines the frame and states the target comparison. Holds. |
| note 90 | Y 72930-72931 | The displayed order includes the cited constants and `gamma`. Holds. |
| note 96 | Y 72946 | Contains the quoted “condition arising … fits the order” rule and the further explanation. The quote is an exact substring. |
| note 98 | Y 62001 | The quote “two consecutive drops never occur, because … gamma is small” matches the source. The inference that it does not explicitly give a one-window ceiling is accurate. |
| note 126 | Y 63775-63777; Y 63749; Y 63774; Y 63684 | Defines `k_0`, `a_i`, `u_k`, and `h=k_flat`; the quoted fragments match. |
| note 171 | Y 1121 | Defines `N_t=R_t`, as used in the proof. Holds. |
| note 173 | Y 73382-73383 | Identifies the target inequality correctly. Holds. |
| note 179 | Y 63774-63778 | The quoted sentence and all referenced bounds appear there. Holds. |
| note 181 | Y 63748-63749; Y 63684 | `a_i` is defined across these lines; `h=k_flat` is supported. The quote “set …” spans the line break and matches. |
| note 185 | Y 650 | Gives `L>=13`; oddness is not needed for the deduction `L>=4`. Holds. |
| note 192 | Y 1102-1103; Y 1109; Y 1113 | Gives the frame floor, gamma range, running minimum definition and least-power definition. Holds. |
| note 194 | Y 1110 | Gives the adjacent frame inequality. Holds. |
| note 210 | Y 63775-63778 | States the properties Lemma K claims to prove. Holds. |
| note 220 | Y 62080; Y 61973; Y 61981-61985 | Gives the same-level-cell proposition, level-cell hull convention, and formula for `Omega_t^c`. The quote from 62080 is exact. |
| note 226 | Y 62174 | The sentence about steps copying prior entries and standing marks is exact. |
| note 228 | Y 63684; Y 62105-62107; Y 62110-62115; Y 62175-62177 | Gives class definition, three fates, drop-out updates, and operation/history updates. Holds; the note distinguishes the level-`t` Lambda exception for islands. |
| note 230 | Y 62128 | Contains both the action-sequence definition and marks-wait statement. The quoted mark-window clause is exact. |
| note 232 | Y 62001; Y 73081-73084; Y 73066 | Supports nested partitions, adjacent size transitions and compatible partitions. The range 73081-84 is complete. |
| note 234 | Y 73087-73092 | Gives label nesting and `Z_j=Lambda_j^c`. Holds. |
| note 236 | Y 62121; Y 62124-62125; Y 62128; Y 73133-73140 | Gives stored regions, action/determining sequence formulas and displayed action nesting. Holds. |
| note 244 | Y 73068; Y 62195 | “Closed cells are used for collars” and the one-cell separation sentence are present. They do not define “component”; the note correctly labels (K) as its reading. |
| note 262 | Y 63684; Y 62128; Y 62080; Y 73087-73092 | Supports class-component status, step-cell geometry, and label nesting used in this proof paragraph. Holds as source premises; the connected-component consequence is the note’s (K). |
| note 268 | Y 62105; Y 62175-62177 | Supports healed updates, swallowed marks ceasing to stand, and no changes outside the class. Holds. |
| note 269 | Y 62106 | Supports island updates and the unchanged `Lambda_t`. Holds. |
| note 270 | Y 62110-62115; Y 62177; Y 62115 | Supports drop-out window formulas, unchanged outside-class entries and `Lambda_t intersect X=empty`. Holds. |
| note 276 | Y 1462; Y 1475-1477 | Gives the profile/action-sequence sentence and two-case scale definition. Holds. |
| note 278 | Y 1475-1477 | Gives the rule whose first case Corollary C applies. Holds conditionally on the stated reading. |
| note 280 | Y 1476; Y 62096 | Y 1476 says “those cubes”; Y 62096 calls level-`t` cells `M R_t`-cubes. This supports the interpretation, not a definition of the demonstrative by itself. |
| note 282 | Y 62245; Y 1476 | Y 62245 says the action regions are unions of coarse cubes; Y 1476 is the conditional branch. Holds. |
| note 287 | Y 62001 | The cited line says `gamma` is small; it does not specify that the ceiling covers a window. Holds. |
| note 288 | Y 62080 | Includes the exact parenthetical citation “(119, p. 256).” Holds. |
| note 289 | Y 1476 | “Those cubes” occurs at line 1476. Holds. |

Every quotation checked against its cited range matches letter-for-letter, except the capitalization mismatch in issue line 5 identified in Finding 2. The line 1476 “those cubes” interpretation is declared as an interpretation, not presented as a quotation establishing its meaning.

## Other requested checks

| Check | Result |
|---|---|
| Internal material | No row number, registry label, lane file reference, or model name outside provenance appears in the outward prose. The note’s public GitHub link necessarily contains the repository’s public path. |
| Second person and claims about the manuscript | The authors are addressed directly in the issue and in the note’s manuscript claims. Posted note line 286 is the only “your text does not state” sentence. It is accurate for exact (G), but should be narrowed to the cited passages as proposed above because Y 62001 does state qualitatively that `gamma` is small. |
| GitHub math rendering | In both supplied render files, all displayed math expressions occur inside `<math-renderer>` elements; the HTML contains no formula outside a math-renderer element. No math-rendering defect found. |
| Links | Issue line 5 and note line 5: commit `c7fef8b21b58`, path `YM4/YM4_1400.tex`; the fetched file exists at that commit. Issue line 7: commit `164df47e956d44b54dfed4de615705720ce22994`, path `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/scale-note.md`; `git cat-file` confirms it exists at that commit in this repository. No sign-in-only page was fetched. |
| Symbols before definition | The overview uses (G) at note lines 9-12 before its formal definition at line 84; add the cross-reference suggested in Finding 5. In the mathematical body, symbols are introduced in the frame, the quoted manuscript, or the hypotheses before use. |
| Sense of the statements | Lemma G’s threshold and proof, Example F’s counterexample and stated parameter range, Lemma W’s (S)/(W) clauses, Corollary S, Lemma K and its domain, and Lemma C/Corollary C agree with their displayed hypotheses and conclusions. Example F’s opening range is a sufficient subrange; its later “Range” paragraph gives the exact range. The issue summary omissions are in Finding 3. The scope section at note lines 284-291 agrees with the formal statements: (G) remains an added hypothesis, Example F is parameter-specific, Lemma C assumes the listed manuscript rules and reading (K), and the “those cubes” reading is acknowledged. |

## Link and source inventory

| Outward link | Commit | Path | Exists at that commit? |
|---|---|---|---|
| Issue line 5; note line 5 | `c7fef8b21b58` | `YM4/YM4_1400.tex` in `ethanwsussman/Yang--Mills-LLM-experiment` | Yes; fetched source is present. |
| Issue line 7 | `164df47e956d44b54dfed4de615705720ce22994` | `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/scale-note.md` in this repository | Yes; verified at that commit. |

No other hyperlinks occur in either text.
