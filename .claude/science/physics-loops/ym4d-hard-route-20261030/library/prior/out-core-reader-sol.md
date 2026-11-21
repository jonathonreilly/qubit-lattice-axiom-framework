9

## Repo search

The lead's `prior/repo-search-2026-11-08.md` covers main and PRs 10114,
10133, 10134 and 10141. It records related geometry and preparation work,
not this later outward-text reader check. I read that digest. I fetched
current main and PR 10141 and opened the closest cited passages:

| Hit checked | Closeness |
|---|---|
| PR 10141, `research/ym4d/library/open-registry.md:224-231` | Earlier geometry, preparation and interface assignments; not a reader report on these drafts. |
| PR 10141, `research/ym4d/library/st1-r4.md:1703-1707` | Earlier collar/rim interface restrictions; not this proposition's outward wording. |
| This checkout, `library/open-registry.md:1003` | Records the proof, its checks, the outward note, and the separate readers in rows 659-660. This task is the assigned row 660 reader, not a new attack on that proof. |

PR 10141 resolved to `fb99b4dddc7254e6124ac124887d58eeb3a77802`;
main resolved to `bf92a1d763030836ed55631d5d7a7ef3b288f284`.
`library/prior/core-reader-sol.md` was absent. No prior report on this
reader target was supplied by these hits. No proof was redone.

Provenance: Codex reader, 2026-11-10, checkout
`2ac2702b793f5236be370a837399e87c7297b24d`. Research text, not an audit;
this grants no status. Mathematical correctness was not checked.

Here **I** means `library/out-core-issue.md`; **N** means
`library/posted/out-core.md`. Line numbers refer to those exact files.
The nine findings below include editorial findings; they are not nine
mathematical defects. Repeated occurrences share one finding number.

I read GOAL and the requested FINISH rules. I used the outline index's
README, obligations and chunk 16 geometry rows with their neighbours, then
read outline lines 17398-17447. Its index calls the geometry proposition
sketched. The outline and CA-I were fetched once as requested; CA-I was
not needed for this reader check. The source text is by Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text. The earlier
repository work above is reused as search history, not independent evidence.

## 1. Clarity and multiple meanings

| Finding | Our line | Reader problem | Proposed text |
|---|---|---|---|
| F1 | I11; N129 | “A second reading” follows two named readings. It can sound like another name for R2, rather than an alternative to R2. | “An alternative to (R2) is to read line 61973 as the standing rule $`\Omega_0=\Omega_1^\sim`$ at every moment. This also gives the gap for the pair $`(0,1)`$.” Retain the following explanation in N129. |
| F2 | N355 | “Only (R2) matters” can tell the reader that R1 is unnecessary. N172 expressly invokes R1. | “The note does not decide between interpretations of your wording. The step argument uses (R1). Reading (R2) affects only the pair $`(0,1)`$, which your display does not contain.” |

The long theorem statements mainly list mathematical quantifiers. I did not
classify length alone as unclear. N143 explicitly distinguishes the two uses
of $`h`$; its local explanations make them readable.

## 2. Internal material

| Finding | Our line | Occurrence | Proposed text |
|---|---|---|---|
| F8 | I7, link destination only | The URL exposes `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-core.md`, an internal lane path. The visible text “This note” is clean. This is a naming concern, not a broken link. | Keep “This note” as the link text. If the no-internal-name rule includes URL paths, replace the destination with an owner-prepared outward snapshot URL. No replacement URL is established by this check. |
| — | I1-17; N1-358 | No internal row number, registry name, lane filename or `CORE` in displayed prose. Model names occur only in I17 and N3, the provenance lines. Manuscript paths and labels belong to your sources. | Keep. |

## 3. Address, attribution and claims about your manuscript

| Finding | Our line | Reader problem | Proposed text |
|---|---|---|---|
| F3 | N5 | “All rules, symbols and statements used below are yours” gives blanket credit. It also appears to attribute the note's lemmas and conventions to you. | “The source passages cited below are in your `YM4/YM4_1400.tex` at commit `c7fef8b21b58`.” Retain the source link and the explanation of line numbering. |
| F4 | N85, N87, N354 | The section calls every hypothesis a statement taken “as stated.” N87 itself distinguishes the quoted box case from the convention adopted for every union of cells. A reader should not have to reconcile these descriptions. This is a provenance-label concern, not a verdict on H1. | At N85: “The proof assumes (H1)-(H6). Their source passages and the convention used in (H1) are specified below.” At N87: “Your quoted box formulas use this sup-norm enlargement. We assume the same convention for every union of cells of one level.” At N354 replace “They are taken from your text as stated” with “Their source passages and the convention in (H1) are listed in section 3.” |
| F5 | I9; N354 | Both summaries omit the no-wrapping hypothesis H6. N354 names H1-H6 but enumerates only the other five. I7 mentions the torus floor, but I9 should identify the no-wrapping statement that the note also assumes. | Append to the lists: “and the no-wrapping statement (line 63692; hypothesis (H6)).” |
| F6 | I13 | BA 1614 imposes a strict inequality. “With ... in the place of $`LM`$” suppresses that difference from the preceding weak inequality. It also leaves the comparison of units implicit. | “Your `YM4/BA/YM4_BA.tex` imposes the hypothesis $`\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho_{\rm gap}h_j`$, with $`\rho_{\rm gap}\ge4L`$ (`eq:layered-separation`, lines 1613-1615 at the same commit). This compares the form of the separation conditions; it does not identify their constants or units.” |
| — | Both files | References to you use “your,” not third-person “their.” Generic descriptions of regions and proofs need no second-person subject. The provenance lines are the requested exception for authorship/checker statements. | Keep the second-person usage. |

N22 makes the narrow, locally supported observation that no proof follows
the proposition. N23's three label occurrences were confirmed by a label
search. Neither sentence establishes absence of a proof elsewhere; I did
not read them as doing so.

## 4. Cited-line checks

The local Y file has 136,637 lines. Its bytes equal the public file at
`c7fef8b21b5846e1b5806a7d4f915737b9130c27`; SHA-256 is
`222ef1bd4b668f88fab33f6edd131b4308fc897eefb112ac5898b8730549f178`.
I opened the cited ranges below. “Holds” means the lines contain the
represented statement or words; it does not certify that statement's truth.

Every issue citation is covered here, including repeated citations at I11.

| Our line | Source opened | Result | Proposed text |
|---|---|---|---|
| I5 | Y62080-62101 | Holds: proposition and its closing line. | Keep. |
| I5 | Y62082-62087 | Holds: all three displayed relations and units. | Keep. |
| I5 | Y62080; Y62101-62103 | Holds: reference is attached to step regions; the next paragraph follows the proposition. | Keep the local “No proof follows” wording. |
| I5 | Y62089-62094 | Holds: active-index equality and the quoted eight-layer explanation. | Keep. |
| I7 | Y61911 | Holds: stated torus floor. | Keep. |
| I7 | Y61983-61990 | Holds: two-cell padding occurs in the initial boxing input. | Keep. |
| I9 | Y645-648 | Holds: layers, hulls and periodic versions. | Keep; clarify H1 as in F4. |
| I9 | Y63684-63690 | Holds: cell-layer box convention and quiet output. | Keep. |
| I9 | Y63750-63763 | Holds: sup-norm enlargement and the displayed quiet boxes. | Keep. |
| I9 | Y63760-63766 | Holds: quiet-box equations. | Keep. |
| I9 | Y63775-63809 | Holds: stipulated index, weights, prepared boxes and alignment statement. | Keep the “takes ... as stated” limitation. |
| I9 | Y62128 | Holds: “Marks wait.” | Keep. |
| I9 | Y62115; Y62171 | Holds: top Lambda entry stays empty/outside under reindexing. | Keep; add H6 as in F5. |
| I11, R1 | Y1586; Y61973 | Holds as support for the explicitly named reading: live region after healing and step input. | Keep the reading label. |
| I11, R2 | Y61973; Y62105; neighbouring Y62106 | Partial citation: the first two lines give the initial entry and healing; the island rule is on 62106. | **F7:** cite “lines 61973, 62105-62106.” |
| I13 | BA1613-1615; context BA1603-1617 | Holds that separation is imposed as a hypothesis; strict sign needs preserving. | Use F6. |

The following 50 note entries sample every section, including the proof
and both final sections. Some entries cover several citations on one line.

| Our line | Source opened | Result | Proposed text |
|---|---|---|---|
| N9 | Y62080 | Holds: quoted nesting and step-region sentences. | Keep. |
| N11-17 | Y62080-62094 | Holds: prepared sequences, display, units and equality qualifications. | Keep. |
| N22 | Y62101-62103 | Holds: end of proposition and next paragraph. | Keep. |
| N23 | Y62080; Y62128; Y63715-63716 | These are exactly the three label occurrences. The quotation attributed to line 63716 starts on 63715. | **F7:** introduce that quotation with “Lines 63715-63716 say”. Keep 63716 in the label-occurrence list. |
| N31 | Y61973 | Holds: initial Omega entry. | Keep. |
| N33 | Y61973; Y1586 | Holds: live-region quotations. | Keep. |
| N35 | Y61973; Y645-648 | Holds: units of layers and hull definition. | Keep. |
| N37 | Y61980 | Holds: boxing map quotation. | Keep. |
| N39-49 | Y61983-61990; Y71099-71100 | Holds: step formulas and separately quoted padding consequence. | Keep. |
| N51 | Y642-644; Y62096; Y63749; Y63774-63775 | Formulas and descriptions hold. “The partition” starts on 642. The quoted words “in bare units” extend through 63775. | **F7:** cite “lines 642-644” and “lines 63774-63775” for those quotations. |
| N53 | Y62001; Y62195; Y63882 | Holds: power of L, nesting, non-increasing scale and identification with N. | Keep. |
| N55 | Y63684; Y63750-63752 | Holds: class/depth/quarantine and both enlargement conventions. | Keep. |
| N57-63 | Y62103-62116 | Holds: three fates and window entries. | Keep. |
| N65-71 | Y62121-62128 | Holds: stored regions, stopping vectors and determining label. | Keep. |
| N73 | Y62161-62171 | Holds: reindexed Omega formula and Lambda rule. | Keep. |
| N75 | Y62174-62180 | Holds: copying, overwriting and drop-out entries. | Keep. |
| N77 | Y63714-63715 | Holds: labels before and after the operation. | Keep. |
| N79 | Y1640; Y61911; Y63692 | Holds: torus, admissibility and no-wrapping statements. | Keep. |
| N81 | Y650; neighbouring Y651 | The lower bound is on 650; “odd” is on 651. | **F7:** “Lines 650-651: ‘Take $`L\ge13`$ odd’.” |
| N87 | Y645-648; Y63684-63690; Y63750-63763 | Holds for the quoted conventions/formulas; the note itself labels the arbitrary-union usage as its extension. “Enlargement by a distance” begins on 63750, not 63751 alone. | Use F4. **F7:** cite “lines 63750-63751” for that quotation. |
| N89 | Y63684; Y63752-63756; Y63760-63766 | Holds: hull, oldest box and quiet-box equations. | Keep. |
| N95 | Y63766-63767 | Holds: unlabelled regions refer to the pre-operation label. | Keep. |
| N97 | Y63775-63777 | Holds: last index and its stated range. | Keep. |
| N99-101 | Y63783-63784 | Holds: all three weight formulas. | Keep. |
| N103-107 | Y63798-63804 | Holds: both prepared-box cases. | Keep. |
| N109 | Y63805-63809 | Holds: alignment and union-of-cubes statements. | Keep. |
| N111 | Y62128 | Holds: waiting and disjoint windows. | Keep. |
| N113 | Y62115; Y62171; Y62121 | Holds: top entry and persistence quotations. | Keep. |
| N115 | Y63692; Y63770-63771 | Holds: no wrapping and 100-cell cutoff. | Keep. |
| N117 | Y63714-63741 | Holds: nesting is invoked for the earlier labels in the described survival argument. | Keep; no correctness verdict on the joint induction. |
| N123 | Y1586; Y62106-62107 | Holds: live-after-healing wording and retained island/drop-out regions. | Keep the reading label. |
| N125 | Y62105-62106; Y61973 | Holds: quoted quantifiers and starting entry; including zero is explicitly presented as a reading. | Keep. |
| N129 | Y61973; Y62078; Y62245; Y63032; Y63039; Y63374 | The occurrence list in Y61900-66000 is exact. Those occurrences do not explicitly state an update under healing. | Use F1 and F9; keep the bounded-search wording. |
| N139 | Y63750-63752 | Holds: box enlargement by sup distance. | Keep. |
| N157 | Y61990; Y71099-71100 | Holds: final set and stated padding consequence. | Keep. |
| N203 | Y63819-63820 | Holds: quoted first prepared-box separation. | Keep. |
| N231 | Y63820-63824 | Holds: early and late separations. The quoted subject $`Z''_i(X)`$ is on 63820, before the cited range. | **F7:** cite “lines 63820-63824.” |
| N255 | Y62080; Y62107-62115; Y62128 | Holds: stage/prepared sequences, drop-out stage rule and stopped geometric labels. | Keep; the note's identification is not re-proved here. |
| N288 | Y62140-62142 | Holds: recorded data and previous-level top region. | Keep. |
| N303 | Y62174-62180 | Holds: copied and overwritten entries. | Keep. |
| N328 | Y63714-63766 | Holds as a description of the source argument's earlier-label dependencies. | Keep; no new circularity check attempted. |
| N340 | Y62089-62094 | Holds: both equality qualifications. | Keep the distinction between boxes and labels. |
| N346 | Y650-651; Y63805-63809 | Holds with the expanded L citation; oddness/alignment wording is present. | **F7:** replace “Your line 650” with “Your lines 650-651.” |
| N347 | Y62001 | Holds: running-minimum power definition. | Keep. |
| N347 | Y83084; Y61911 | Holds: coupling identity and coupling ceiling. | Keep; no derivation checked. |
| N347 | Y1102-1103 | Holds: frame's gamma bound. | Keep. |
| N348 | Y61911; Y63692 | Holds: floor and no-wrapping statement. | Keep. |
| N350 | Y650-652 | Holds: the listed background constant inequalities. | Keep; no verification of the note's constant-use inventory attempted. |
| N354 | Y63692, through H6 | H6 is present in section 3 but missing from this verbal list. | Use F5. |
| N356 | Y62080; Y62094-62098; Y62130-62133 | Holds: excluded step/cell/creation assertions and retained-space identity occur there. | Keep. |

F7 is one finding about incomplete citation ranges, with seven locations:
I11, N23, N51, N81, N87, N231 and N346. The proposed changes above only
broaden the pinpoints to include the words already quoted.

## 5. GitHub mathematics and supplied HTML

| Our line | Check and observed result | Proposed text |
|---|---|---|
| I1-17 | All 21 inline formulas are inside `math-renderer` elements in `issue.html`. No raw formula remains outside one. | Keep. |
| N1-358 | All 942 inline formulas and 11 displays are inside `math-renderer` elements in `note.html`. No formula is in a code/pre block. No display is inside a list. | Keep. |
| Both files | No `\( ... \)`, `\[ ... \]`, or bare-dollar form. No source table containing a math bar. | Keep. |
| N23, N117 | Three literal `\cref{...}` source-reference commands appear outside renderers. These are quoted TeX cross-references, not unrendered mathematical formulas. | No mathematical-rendering correction. |
| Both supplied HTML files | Formula order and contents match the Markdown after HTML entity decoding. The note has one h1, seven h2, nine h3, 44 list items and no table. | Keep. |

This checks the supplied GitHub HTML, not live browser typesetting or a
posted issue. I made no render API POST and posted nothing.

## 6. Every link

For “branch head,” the pinned checkout HEAD and current origin/main are
reported separately. Upstream manuscript paths are also checked at its
public default-branch head. No sign-in page was fetched.

| Our line | Commit and path | Existence and destination | Proposed text |
|---|---|---|---|
| I5; N5 | Sussman-Alpoge `c7fef8b21b58`, full commit `c7fef8b21b5846e1b5806a7d4f915737b9130c27`; `YM4/YM4_1400.tex` | Public file exists. Upstream main HEAD is the same commit. File matches local Y byte for byte. This external path is absent from this repository's pinned HEAD, as expected. | Keep; optionally append `#L62080-L62101` for the issue's proposition link. |
| I7 | This repository, `d78df8cc9c9159634bb2766e44133cfa76f5927c`; `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-core.md` | Exists at linked commit and pinned checkout HEAD. Both versions are byte-identical to the note read here. Path is absent from current origin/main. The link is pinned, so that absence does not make its target wrong. See F8 for the internal URL name. | Keep the verified pinned URL unless an outward snapshot URL is supplied. |

These are all Markdown/HTML hyperlinks: two in the issue, one in the note,
with the source link repeated. I13's unlinked manuscript reference
`YM4/BA/YM4_BA.tex` also exists at `c7fef8b21b58` and upstream main HEAD.
Its cited lines were read above. It is not a local repository path.

The linked note's SHA-256 is
`bb69d05a7bef5e455380365919d1e06c609e8963d5ae34857e95b9a7eac86904`.
The issue's SHA-256 is
`b3f1e9ec9463a37c9a5f9dafb0434926d217d643f7b240c7083b92b43c7d90b7`.

## 7. Symbols before definition or quotation

| Finding | Our line | Reader problem | Proposed text |
|---|---|---|---|
| F9 | N129 | The note first uses its unquoted distance symbol $`d`$ here, but defines it only at N139. | Replace $`d(\Omega_0^c,\Omega_1)\ge a_1`$ here with $`\operatorname{dist}_\infty(\Omega_0^c,\Omega_1)\ge a_1`$. The latter notation has already been quoted at N14. |
| — | N9-358 | Other symbols encountered before the notation section occur in attributed source quotations/formulas, or are locally introduced. N137 introduces the zero-index conventions before the invariant uses them. | Keep. |

I wrote only this report. I changed neither reviewed draft nor any proof,
registry or status file. No mathematical obligation was discharged.
Other concurrent checkout changes appeared during final verification;
I left them untouched. Both reviewed drafts retained the hashes above.
