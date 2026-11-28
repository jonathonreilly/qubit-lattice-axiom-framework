3 findings

Provenance: Codex (gpt-6-luna, high), checkout `212781e0c`; outward-text reader check, not an audit.

## Repo search

The lead's `library/prior/repo-search-2026-11-08.md` names `CORE-GAPS` as the underlying geometry result and records that the outward note was written, with reader checks assigned to FINISH rows 659 and 660. The open registry likewise places ownership of the proof with `CORE-GAPS`; this task is the separate reader check of the outward draft, assigned to row 659. I found no repository result covering this reader check. The SA index has no exact `prop:large-field-2-3` entry. Its nearby `history:light-wait` rows and the obligations entry at 18550–18574 concern the older outline's quiet-chain estimate, not this proposition; they do not certify the note. I read those neighboring rows and the cited outline passage. The issue and note cite lines in `YM4_1400.tex`; those source lines were checked below.

## Findings

| Outward line | Finding | Proposed text |
|---|---|---|
| Issue 7 | “It uses only” omits the proof's explicit assumptions: rules (S1)–(S15), statements (H1)–(H6), and readings (R1)–(R2). These appear in the note's Theorem 6 at lines 307–308; in particular, R2 is a reading needed for the `(0,1)` pair, even though that pair is outside the displayed claim. | “The proof assumes your rules (S1)–(S15), statements (H1)–(H6), readings (R1)–(R2), and the following numerical conditions: $`L\ge3`$ odd, each $`\check R_i\ge1`$ a power of $`L`$, and your torus floor (line 61911).” |
| Note 5 | “All rules, symbols and statements used below are yours” over-attributes the note's auxiliary notation, readings, lemmas, and theorem to you. The following source citation is narrower than that sentence. | “The rules and source statements used below are from your text; the auxiliary notation and results are introduced here.” |
| Note 3 | The provenance sentence credits the proof's authors and checkers. That is a credit statement, contrary to the requested wording check. | “This is a proposed proof and research note, not an audit.” |

## Source-line checks

| Outward line(s) | Source lines checked | Result / proposed text |
|---|---|---|
| Issue 5 | Y 62080–62101, 62082–62087, 62089–62094 | Supported. Proposition label, display, equality indices, and following creation text match the summary. The proposition ends at 62101; the next paragraph begins at 62103, so “No proof follows” is supported. No change. |
| Issue 7 | Y 61983–61990, 61911 | Supported for the two-cell padding and torus-floor references. See the missing assumptions finding above. No other source correction. |
| Issue 9 | Y 645–648, 63684–63690, 63750–63763, 63760–63766, 63775–63809, 62128, 62115, 62171 | The source lines state the quoted layer convention, quiet/prepared boxes and index, “Marks wait,” and the drop-out rule. No change. |
| Issue 11 | Y 1586, 61973, 62105 | These lines support the described live-region wording and fate-rule/initial-entry reading. The note marks R1 and R2 as readings rather than statements made in those exact words. No change. |
| Issue 13 | Note 240, 313; Y 62082–62087; BA 1613–1615 | The note's nesting assertion gives $`\Lambda_j\subset\Omega_j`$ (note 240; also the chain in note 313). Since $`Z_j=\Lambda_j^c`$ (note 137), the displayed gap implies the stated gap for $`\Omega_j^c`$. BA imposes, rather than proves, the strict condition $`\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})>\rho_{\rm gap}h_j`$, with $`\rho_{\rm gap}\ge4L`$. The issue accurately describes this as a hypothesis of the same form; it does not assert equality of the two constants. No change. |
| Note 9–11 | Y 62080, 62082–62094, 62103–62128 | The quoted proposition and fate/mark lines hold the summaries. No change. |
| Note 31–35 | Y 61973, 1586, 645–648 | The initial sequence, live region, and hull/layer conventions are present. No change. |
| Note 37–51 | Y 61980, 61983–61990, 62096, 643–644, 63749, 63774, 71099–71100 | Boxing, step formulas, level cells, cube partitions, and the stated consequence match. No change. |
| Note 53–55 | Y 62001, 62195, 63882, 63684, 63750–63752 | The cited scale/depth/enlargement statements match. No change. |
| Note 57–75 | Y 62103–62128, 62161–62171, 62174–62180 | Fates, stopping vectors, the top-entry rule, and the copy/overwrite summary match the cited passages. No change. |
| Note 79–81 | Y 1640, 61911, 63692, 650 | Torus definition/floor, no-wrap sentence, and lower bound on odd $`L`$ match. No change. |
| Note 87–115 | Y 63684–63692, 63750–63767, 63770–63771, 63775–63809, 62128, 62115, 62171, 62121 | The cited quiet/prepared-box formulas, size cap, mark rule, and drop-out rule support the descriptions. No source-line correction. |
| Note 117–129 | Y 63714–63741, 62105–62107, 61973, 61900–66000 | These ranges support the stated scope of the prior nesting use and the two readings. No change. |
| Note 203, 231 | Y 63819–63824 | The cited separations are stated there. No change. |
| Note 255, 257, 286–303 | Y 62080, 62107–62115, 62128, 62121, 62140–62142, 62174–62180 | These passages support the drop-out, stopping, and label-update references. No change. |
| Note 307–328 | Y 61911, 63684–63692, 63714–63766 | The note's hypothesis/source references and ordering discussion point to the stated passages. No line-number correction. |
| Note 340, 346–350 | Y 62089–62094, 62001, 83084, 1102–1103, 61911, 63692, 650–652 | The active-index/gap description and cited scale, frame, torus, and constant references are present. No line-number correction. |
| Note 354–358 | — | These are statements about the scope of this note, not citations to Y. No source-line check applies. |

## Wording, render, symbols, and links

| Outward line(s) | Check | Result / proposed text |
|---|---|---|
| Issue 1–15; Note 1–358 | Second person, internal terms, and symbol order | Aside from the provenance and blanket attribution flagged above, the outward prose addresses you as “you/your” where it refers to your manuscript. I found no row number, registry name, lane filename, `CORE`, or model name outside the provenance line. The note's symbols are first introduced in quoted source statements or defined before use in its proof. No other change. |
| Issue 5, 7; Note 5 | Links | Issue 5 and note 5 link to commit `c7fef8b21b58`, path `YM4/YM4_1400.tex`; it exists at the SA repository's current `main` head (`c7fef8b21b5846e1b5806a7d4f915737b9130c27`, HTTP 200). Issue 7 links to commit `d78df8cc9c9159634bb2766e44133cfa76f5927c`, path `.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-core.md`; it exists at that cited commit and at this checkout's HEAD, but not at this repository's current `main` head (`bf92a1d763030836ed55631d5d7a7ef3b288f284`, HTTP 404). The pinned link resolves; no link-text change proposed. |
| Issue.html, Note.html | GitHub render | Both present. The issue has 21 `math-renderer` elements and the note has 953; no formula was outside a math-renderer element or inside a code block. No raw `\( \)` or `\[ \]` delimiters found outside rendered math. Display formulas are outside list items; no table math/bar issue. No change. |
