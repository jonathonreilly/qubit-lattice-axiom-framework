lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T08:17Z

FAITHFUL AFTER THE LISTED CORRECTIONS (12 corrections of line numbers and quotations, applied, section 5), with 7 proposed changes of text that I did not apply (section 6; P1-P3 should be decided before the post).

# out-core-faith: faithfulness check of `library/out-core.md` and `library/out-core-issue.md` (FINISH row 658)

Provenance: Claude Fable 5.2, effort medium, Mac mini worker 1, branch claude/ym4d-hard-route at 212781e0c. This is check 2 of the rule "five checks before any outward post": a comparison of texts. It is not a new check of the proof and not an audit. Claude Fable 5.2 also wrote `library/core-gaps-check.md`, so this reading is not independent of that check. No computation was run as a proof step; one script located quoted strings in the source, and I read every hit and every miss by eye.

Sources. Y = `YM4_1400.tex` of Sussman and Alpoge (with Claude and Codex as authors of their text), commit 2bc0658f91d2, fetched by URL into `/tmp/corefaith/y/` (136,637 lines; byte-identical to `/tmp/ym4_1400.tex`). I also fetched `YM4/YM4_1400.tex` at commit c7fef8b21b58, the commit that the note and the issue cite: it is byte-identical to Y (`cmp`), so the line numbers hold at the cited commit. BA = `YM4/BA/YM4_BA.tex` at c7fef8b21b58 (4,850 lines), fetched into `/tmp/corefaith/ba/`.

Repo search. `library/open-core.md` has no row for this item; FINISH rows 640, 650, 653 are named in row 658 as not duplicates. This item attacks no open lemma.

## 1. Item (a): every quotation and line number against Y

Method: each text in double quotes was searched in Y after the map from GitHub math to TeX; each display was compared by eye. "ok" means the quoted words stand on the cited lines. Line numbers of our files are those of the files before my corrections (the corrections do not move lines).

### 1.1 The note `out-core.md`

| place (note line) | cited lines | result |
|---|---|---|
| 8, commit and file | c7fef8b21b58, `YM4/YM4_1400.tex` | ok, identical to Y |
| 12, opening of the proposition | 62080-62101; quote at 62080 | ok |
| 14, second quote, with `[...]` | 62080 | ok; the elision is marked |
| 16-20, display and "(level-j units; ...)" | 62082-62087 | ok (the words are at 62086) |
| 20, two quotes on equality and on `j=k_0(t)+1` | 62089-62094 | ok (62089-62091 and 62093-62094) |
| 20, two kinds of creation; end | 62094-62098; 62101 | ok |
| 24, "(119, p. 256)", "the regions that the steps produce" | 62080 | ok |
| 25, next paragraph | 62103 | ok |
| 26, the label occurs three times | 62080, 62128, 63716 | ok (grep: exactly these three) |
| 26, quote of 62128 | 62128 | ok |
| 26, "We use the nesting ..." | 63716 | words are on 63715-63716. **Corrected (C1)** |
| 34 (S1) | 61973 | ok |
| 36 (S2) | 61973; 1586 | ok (Y prints the first five words in bold) |
| 38 (S3) | 61973; 645-648 | ok |
| 40 (S4) | 61980 | ok |
| 42-52 (S5) two displays; "The set Z_t ..." ; "The pre-operation region ..." | 61983-61987; 61990; 71099-71100 | ok |
| 54 (S6) "are M R-check_t-cubes of level t" | 62096 | ok (Y says it of the cells of the creation set) |
| 54 (S6) "The partition pi_j ..." | 643-644 | the sentence starts on 642. **Corrected (C2)** |
| 54 (S6) "a_i = ..." | 63749 | ok |
| 54 (S6) "Let u_i = ML^i ..." | 63774 | words are on 63774-63775. **Corrected (C3)** |
| 56 (S7) three quotes | 62001; 62195; 63882 | ok |
| 58 (S8) four quotes; box enlargement | 63684; 63750-63752 | ok (the quote is on 63750-63751, inside the cited range) |
| 60 (S9) five quotes | 62103, 62105, 62106, 62107 | ok |
| 62-66 (S9) display | 62110-62115 | the display drops the entry `S_l ∩ X = ∅` of line 62113 without a mark. **Corrected (C4)** |
| 68-74 (S10) quotes and display | 62121; 62124-62125; 62128 | ok |
| 76 (S11) | 62161-62168; 62169-62171 | ok |
| 78 (S12) | 62174-62180 | ok |
| 80 (S13) | 63714-63715 | ok |
| 82 (S14) three quotes | 1640; 61911; 63692 | ok; the elision is marked |
| 84 (S15) "Take L >= 13 odd" | 650 | "odd" is on 651. **Corrected (C5)** |
| 90 (H1) | 645-648; 63684; 63686-63690; 63760-63763 | ok |
| 90 (H1) "enlargement by a distance s in the sup norm" | 63751 | words are on 63750-63751. **Corrected (C6)** |
| 92-98 (H2) | 63684, 63756; 63752-63753; 63760-63766; 63766-63767 | ok |
| 100-112 (H3) | 63775-63777; 63783-63784; 63798-63803; 63805-63809 | ok |
| 114 (H4) | 62128 | ok |
| 116 (H5) three quotes | 62115, 62171, 62121 | "At l=s the" is on 62170. **Corrected (C7)** |
| 118 (H6) | 63692; 63770-63771 | ok |
| 120, remark on order | 63715-63716; 63716-63720; 63714-63741 | ok |
| 126 (R1) | 1586; 62106; 62107 | ok |
| 128 (R2) "for l <= t", "for l < t" | 62105; 62106 | ok |
| 128 (R2) "A label's sequence starts at Omega_0" | 61973 | the quote stops inside Y's formula `Omega_0 = Omega_1^~`. **Corrected (C8)** |
| 132, search for Omega_0 in 61900-66000 | 61973, 62078, 62245, 63032, 63039, 63374 | ok (my search gives the same six lines) |
| 142, `B^{[s]}` | 63750-63752 | ok |
| 206, Lemma 3 (a) | 63819-63820 | ok |
| 234, two quotes | 63821-63824 | the first quote starts on 63820. **Corrected (C9)** |
| 258 | 62080, 62107-62115, 62128 | ok |
| 291 | 62140-62142 | ok |
| 306 | 62174-62180 | ok |
| 331 | 63714-63766 | ok |
| 343, Remark | 62089-62094 | ok |
| 349 "Your line 650 takes L >= 13 odd"; oddness | 650; 63805-63809 | "odd" is on 651. **Corrected (C10)**; second citation ok |
| 350 | 62001; 83084; 61911; 1102-1103 | ok (`g_j=x_j^{-1/2}`; `g_j <= gamma`; `0<gamma<e^{-1/2}`) |
| 351 | 61911; 63692 | ok |
| 353 | 650-652 | ok |
| 359 | 62130-62133; quote of 62080 | ok |

### 1.2 The issue draft `out-core-issue.md`

| place (issue line) | cited lines | result |
|---|---|---|
| 5, proposition; display | 62080-62101; 62082-62087 | ok |
| 5, "(119, p. 256)" | inside the proposition | ok (62080) |
| 5, "a step places eight layers ..." | 62089-62094 | the words stand on 62094. See P4 for what they are the reason of |
| 7, torus floor; step rule | 61911; 61983-61990 | ok |
| 9, layer convention | 645-648, 63684-63690, 63750-63763 | ok |
| 9, quiet boxes; `k_0` and prepared boxes; "Marks wait" | 63760-63766; 63775-63809; 62128 | ok |
| 9, standing drop-out | 62115, 62171 | the sentence starts on 62170. **Corrected (C11)** |
| 11 (R1) | 1586, 61973 | ok |
| 11 (R2) "a healed component or an island" | 61973, 62105 | the island rule is line 62106. **Corrected (C12)** |
| 13, BA | `eq:layered-separation`, 1613-1615 | ok, see section 4 |

## 2. Item (b): the note against `library/core-gaps.md`

Each row is a place where the note differs from the checked proof. "Covered" means that the checked proof, as written, gives the note's form.

| # | place in the note | difference | covered? |
|---|---|---|---|
| 1 | (H1), section 3 | Says less. core-gaps 2.2 states the equality `A^{~r} = A^{[r a_t]}`. The note takes only the inclusion `A^{~r} ⊃ A^{[r a_t]}`, as a hypothesis. | Yes. I checked each use (Lemma 1, Lemma 2 three times): each needs the inclusion only. In Theorem 6 the symbols `Z_j^~` and `Lambda_j^{~-1}` are defined in the statement, as in core-gaps. |
| 2 | (H5), (H6) | Says the same in another way. They are two named hypotheses. core-gaps has them in section 7 item 2 and in the last paragraph of section 5. | Yes. |
| 3 | (S11) for (R3) | Another way. core-gaps calls the rule for `Lambda` "(R3), not a reading"; the note makes it a quoted rule. | Yes (repair R5 of the first check). |
| 4 | Lemma 0, proof | Says more: the two steps on interiors are written out. | Yes, same argument. |
| 5 | Lemma 1 | Says more: the first paragraph proves `Z_t ⊃ (Omega_t^c)^{~2}` (core-gaps: rule (b) of its table 2.1); `e^{[2a_t]}` is called "the box of 5^4 level-t cells". The label is named `S`, not `S'_t`. | Yes. The count 5^4 is not in core-gaps; it is correct (a cube of side `a_t` enlarged by `2a_t` on each side, aligned) and nothing uses the number. |
| 6 | Lemma 2 | Same steps, written out. | Yes. |
| 7 | Lemma 3, statement | Says more: `g_l` is given by formula in cases (a)-(e); core-gaps gives lower bounds. Case (c) is `7a_{k_0}+u_t` where core-gaps has `>= u_t`. The sets `O_i` of Y are used for `D_l ⊂ G_l`, where core-gaps uses the chain of the `G_i`. | Yes. I redid each case by hand from (H2), (H3): (a)-(e) hold, `L^2-3L+1 >= 0` at `L >= 3`, and `D_l ⊂ O_{k_0+1} ⊂ O_l ⊂ G_l`. |
| 8 | Lemma 3 (f), (g) | Says more. They are not in core-gaps. (g) is `library/h-geo.md` Lemma 2 (f), checked in `library/h-geo-check.md`. (f) is not in a checked file. | Not covered by core-gaps. Both are correct by my reading (`O_{i+1} = H_{i+1}^{[8a_{i+1}]} ⊃ G_i^{[8a_{i+1}]} = O_i^{[2a_i+8a_{i+1}]}`; `Z''_t^{[5u_t]} = O_{k_0+1} ⊂ O_t`, `X = O_t^{[2a_t]}`). The note says that they are not used, and nothing uses them. See P7. |
| 9 | Section 5.6 and Lemma 4 | Says more: "every entry of level i is a union of M-cubes of level i" is a named hypothesis and a conclusion; in core-gaps it is a sentence inside the proof of (G) (repair R3). | Yes, same argument. One formal point, the same in core-gaps: see P6. |
| 10 | Lemma 4, after the statement | Says more: "A component that the operation has not yet treated is stopped after 0 stages." | Yes: for `m=0` the window is empty and the rule changes nothing; core-gaps allows `0 <= m(X)`. |
| 11 | Lemma 5 (a), (c) | Another way: the hypothesis "(N) for the determining label" is in the statement of (a), and "(a) holds for h'" in (c); core-gaps has both inside the proof. The quote of 62140-62142 is added. | Yes. |
| 12 | Theorem 6 | Says more: the hypotheses (S1)-(S15), (H1)-(H6), (R1), (R2) are named; the cube property is in the conclusion; the base case and the step case give the cube property. | Yes. |
| 13 | Remark after Theorem 6 | Says less: core-gaps says that the gap "is attained" and "cannot be improved"; the note says only that Lemma 3 (d), (e) give the same values, and section 7 says the equality is not proved. | Yes (weaker). |
| 14 | Section 6 | Says less: "The theorem holds for every M >= 1" is replaced by "no inequality on M is used". | Yes. |
| 15 | Section 7, second bullet | Same words as core-gaps section 7 item 3: "Only (R2) matters". The proof uses (R1) in Lemma 2 for every pair `(t-1,t)`. | The proof is not touched. The sentence is not exact in both files: see P1. |
| 16 | Corollary 7 (the internal form) | Left out of the note. | Nothing to cover. |

No statement of the note is stronger than what `core-gaps.md` proves, apart from row 8, which is unused.

## 3. Item (c): the issue against the note and against Y

| issue sentence | against the note and Y | result |
|---|---|---|
| line 5, sentences 1-3 | note section 1; Y 62080-62087 | ok |
| line 5, "Lines 62089-62094 then say where the first inequality is an equality, with the words ..." | Y 62094: "which still gives the displayed lower bound but can be larger; the reason is that a step places eight layers around the old region, and the preparation removes most of them again". In Y the words are a reason. They follow the sentence on `j=k_0(t)+1`. They do not say where the equality holds. | words exact; the link "with the words" is loose: P4 |
| line 5, "No proof follows the proposition." | note line 25; Y 62101-62103 | ok |
| line 7, "a proposed proof of the nesting and of the display"; "every history, every moment ..., every fate and stage count ..., every stopping vector" | Theorem 6 | ok |
| line 7, "It uses only L >= 3 odd, each R-check_i >= 1 a power of L, and your torus floor" | note section 6: "these constants and conditions, and no others" | ok as a sentence on constants; a reader can take "only" as "no other hypothesis". The next two paragraphs list the hypotheses, so I propose no change |
| line 7, "Each new pair of regions gets either the two-cell padding of your step rule or a gap from your box formulas." | In the note this sentence is the end of Lemma 4 (an operation). At a step the new pair gets the eight layers of `H_t` (Lemma 2, line 61984), and the first pair gets the one layer of line 61973. | says the step case in a way that the note does not: P3 |
| line 9, list of statements taken as stated | note section 3 has (H1)-(H6). The issue lists (H1)-(H5). (H6), no wrapping (lines 63692, 63770-63771), is missing. | says less than section 3, so the issue under-states the hypotheses: P2 |
| line 11, (R1), (R2), second reading | note section 4 | ok |
| line 13, first sentence | not in the note. It follows in one line from (N) and (G) of Theorem 6; `core-gaps.md` Corollary 7 has the same line in its proof. | covered by the checked proof; see section 4 and P5 |
| line 13, second sentence | BA 1612-1616 | ok, see section 4 |
| line 15 | note section 7 | ok |
| line 17, provenance | not judged (row 658) | - |

## 4. Item (d): the two sentences on `YM4/BA/YM4_BA.tex`

I read BA 1595-1660.

- Label and lines. `\label{eq:layered-separation}` is on line 1613; the formula is on 1614-1615; the display ends on 1616. "lines 1613-1615" is right.
- Imposed, not proved. Line 1612 says "Impose the separation". The lemma at 1638-1641 takes "nested regions [...] satisfying \eqref{eq:layered-separation}". No line in 1595-1660 proves it. So "imposes ... as a hypothesis" is right.
- Form of the constant. BA 1614-1615: `dist_infty(Omega_j^c, Omega_{j+1}) > rho_gap h_j` for `0 <= j < k`, with `rho_gap >= 4L`. BA line 169 has `h_j = L^j h_0`, the level-j spacing. So `rho_gap h_j` stands where the display has `LM` in level-j units. The issue's words are right.
- Two differences that the issue does not state, and does not need: BA's inequality is strict, and BA's range starts at `j=0`. The issue says "a separation of this form" and does not say that the hypothesis of BA is met. To meet it one needs `rho_gap < LM` for `j >= 1`, and the pair `(0,1)` needs reading (R2) or the second reading.
- The step to `dist(Omega_j^c, Omega_{j+1}) >= LM`. `Lambda_j ⊂ Omega_j` gives `Omega_j^c ⊂ Lambda_j^c = Z_j`, so `dist(Omega_j^c, Omega_{j+1}) >= dist(Z_j, Omega_{j+1}) >= LM`. The step holds. `Lambda_j ⊂ Omega_j` is (N) of the note (section 5.6, note line 240), which Theorem 6 asserts (note line 310). In Y it is the first sentence of the proposition (line 62080, "The regions are nested, ... ⊃ Omega_1 ⊃ Lambda_1 ⊃ ..."), and at a step it is 61986-61990 (`Z_t ⊃ (Omega_t^c)^{~2}`).
- Verdict: the two sentences claim no more than BA 1612-1616 and Theorem 6 give. The note itself does not print the consequence (P5).

## 5. Item (e), wording, and the corrections applied

Wording. Both files address the authors in the second person; the only "their" and "they" refer to marks, nests and facts, and one "them" is inside a quote of Y. No row number, registry name, lane file name or "CORE" occurs. Model names occur only in the provenance lines. The only internal path is inside the link of the issue to the posted note. All mathematics is in `` $`...`$ `` or in ```` ```math ```` fences; no `\(`, `\[`, `$$` or bare `$`; no fence is inside a list item; there is no table. Two remarks, no change made: note line 8, "All rules, symbols and statements used below are yours", states the source and I do not read it as a credit sentence; note line 28 says "This note proves", where the title and the issue say "proposed proof".

Corrections applied (line numbers and quotations only). Before -> after.

- C1, note line 26: `Line 63716 says "We use ..." . Both lines use the proposition.` -> `Lines 63715-63716 say "We use ..." . Both passages use the proposition.`
- C2, note line 54: `Lines 643-644: "The partition` -> `Lines 642-644: "The partition`
- C3, note line 54: `Line 63774: "Let` -> `Lines 63774-63775: "Let`
- C4, note line 63 (display of (S9)): `\Lambda_l\cap X=X\setminus Z''_l(X)\ \ (\text{the same }l,\ l<t),` -> `\Lambda_l\cap X=X\setminus Z''_l(X),\quad S_l\cap X=\emptyset\ \ (\text{the same }l,\ l<t),` (Y 62112-62114)
- C5, note line 84: `Line 650: "Take` -> `Lines 650-651: "Take`
- C6, note line 90: `(line 63751)` -> `(lines 63750-63751)`
- C7, note line 116: `Lines 62115, 62171 and 62121` -> `Lines 62115, 62170-62171 and 62121`
- C8, note line 128: `"A label's sequence starts at $`\Omega_0`$"` -> `"A label's sequence starts at $`\Omega_0=\Omega_1^\sim`$"`
- C9, note line 234: `Your lines 63821-63824 state` -> `Your lines 63820-63824 state`
- C10, note line 349: `Your line 650 takes` -> `Your lines 650-651 take`
- C11, issue line 9: `(lines 62115, 62171)` -> `(lines 62115, 62170-62171)`
- C12, issue line 11: `(lines 61973, 62105)` -> `(lines 61973, 62105-62106)`

Consequence for the lead. `library/posted/out-core.md` was equal to the note without its two header lines; it now differs from the note by C1-C10. I did not edit it. The issue links the posted copy at commit d78df8cc9c; the link needs the commit that holds the new copy.

## 6. Proposed changes, not applied (statements, hypotheses, sentences on the proof)

Ranked by what each one touches.

- **P1, note section 7, second bullet (and the same words in `core-gaps.md` 7.3).** Now: "It does not decide the readings (R1) and (R2). Only (R2) matters, and only for the pair $`(0,1)`$, which your display does not contain." The proof of the display uses (R1) in Lemma 2, for every pair $`(t-1,t)`$. Proposed: "It does not decide the readings (R1) and (R2). The proof of your display uses (R1), through the inclusion $`Z_{t-1}\subset\widehat Y`$ in Lemma 2. It uses (R2) only for the pair $`(0,1)`$, which your display does not contain."
- **P2, issue line 9.** Add the sixth statement of section 3 of the note, before the full stop: "; and that no cell, box or neighbourhood of a box wraps around the torus (lines 63692, 63770-63771)".
- **P3, issue line 7, last sentence.** Proposed: "At a step, the new pair of regions gets the eight layers of your step rule (lines 61983-61985). At an operation, each new pair gets either the two-cell padding of your step rule (lines 61986-61990) or a gap from your box formulas."
- **P4, issue line 5.** Proposed: "Lines 62089-62094 then say where the first inequality is an equality, and give the reason: "a step places eight layers around the old region, and the preparation removes most of them again"."
- **P5, note, after the proof of Theorem 6.** The issue states a consequence that the note does not print. Proposed remark: "**Remark.** By (N), $`\Lambda_j\subset\Omega_j`$, so $`\Omega_j^c\subset Z_j`$. Hence (G) gives $`d(\Omega_j^c,\Omega_{j+1})\ge u_{j+1}`$ for $`0\le j<s`$." (For $`j=0`$ this is the pair $`(0,1)`$, so it reads (R2).)
- **P6, note Lemma 4, hypothesis on the nests (the same in `core-gaps.md`).** The proof uses "$`D_i`$ is a union of $`M`$-cubes of level $`i`$" and cites "proof of Lemma 3". This is not among the conclusions of Lemma 3 as displayed. Proposed: in Lemma 4 write "with the conclusions of Lemma 3, and with each $`D_i(X)`$ a union of $`M`$-cubes of level $`i`$"; in Theorem 6, operation case, fourth bullet, add "and each $`D_i`$ is a union of $`M`$-cubes of level $`i`$ by (H3)". For Theorem 6 nothing is missing, because its nests are those of (H3).
- **P7, note Lemma 3 (f), (g).** Unused, and (f) is in no checked file. Proposed: delete the two items and their two proof paragraphs, or keep them and accept that only this reading covers (f).

Also, low value: note line 24, "one reference" could read "one reference to the literature" (the proposition also has cross-references inside your text, to a section and to `eq:elab-history-prepared-boxes`).

## 7. What this check does not show

- It does not check the proof again; it compares texts. It does not check the statements (H1)-(H6) of Y.
- It does not check the render (check 3), the two readers (check 4, rows 659 and 660), or rules 0g and 0i.
- I did not search Y for a proof of the proposition under another name; the claim "No proof follows" was compared with Y 62101-62103 and with the three uses of the label only.
- The provenance lines were not judged.

RESULT: FAITHFUL AFTER THE LISTED CORRECTIONS. All quotations and line numbers of the note and the issue draft were compared with Y (identical at c7fef8b21b58): 12 wrong or short line citations and quotations were corrected in the two files (C1-C12), none touches a statement. The note says nothing stronger than `core-gaps.md` proves, except the unused Lemma 3 (f). The two sentences on YM4_BA.tex claim no more than BA 1612-1616 and Theorem 6 give. Open, for the lead: seven proposed text changes not applied (P1 "Only (R2) matters" is not exact, the proof uses (R1); P2 the issue omits hypothesis (H6); P3 the issue's sentence on padding omits the step case; P4-P7 smaller), and `library/posted/out-core.md` with the issue's commit link must be refreshed after C1-C10.
