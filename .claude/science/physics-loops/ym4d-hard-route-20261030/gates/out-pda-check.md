# out-pda-check: faithfulness of library/out-pda.md and library/out-pda-issue.md

Provenance: Claude Opus 5.5 (claude-opus-5-5). One reading by one model. Not an audit; grants no status. No computation. Read-only use of sources; this file is the only write.

**Checked texts.** `library/out-pda.md` (284 lines, SHA-256 `113dc218…7395d7`) and `library/out-pda-issue.md` (15 lines). Codex prepared both.

**Sources.**
- `library/pda.md` (247 lines, SHA-256 `0216341b…f210e10`). It is byte-equal to the freeze commit `4321201aa` on `origin/claude/ym4d-hard-route`. Its freeze annotation is lines 239–247.
- `gates/pda-gate.md`: first failing step none; proved as stated, as one operation step; inherited inputs (a)–(d).
- The account at `31a47c543775`. Local CA-I SHA-256 `4cb5cb5e…6e93`, equal to pda.md line 9.

Account ranges read for this check: CA-I 4220–4228, 45555–45640, 48774–48800, 51690–51730, 53755–53763, 53770–53800, 53816–53838, 91666–91676, 92005–92022; CA-III 9888–9900, 28115–28140; the five by-name lines CA-II 145579, CA-III 21303, 53328, 111073, 111311. I searched CA-I, CA-II and CA-III for every occurrence of `Z''_{k-1}`, `Z''_{k-N_0+1}` and `Z''_{k-N_0+2}`. CMP 122a was not read.

## Result

The mathematics of out-pda.md is that of pda.md. Every hypothesis, display, constant and proof step has a checked counterpart. No step is new. No step is false. Five items need a fix. One is the wording of the endpoint defect (F1). One is a citation range (F3). One is an attribution (F2). Two concern scope and provenance (F4, F5).

## Per-section table

Line numbers: out-pda.md first, then pda.md (or pda-gate.md as "gate").

| out-pda.md | Checked counterpart | Verdict |
|---|---|---|
| Opening, 1–5 | pda 3, 12–17, 235; freeze 241–243 | PASS. "Old (A1) implies prepared (A1), one operation, every stopped prefix" is the freeze scope. |
| Old-label premise, 7–10 | pda 55; gate (1) item 4; CA-I 4224–4226 | FIX F2 ("Your representation" is Balaban's CMP 119 (2.18), which the account cites). The rest matches gate (1). |
| Endpoint correction, 12–22 | pda 34–43; freeze 243; gate (2), (c) | FIX F1 (wording; verdict 1 below). (E), the 48781–48783, 53774–53782 and 92012–92016 citations, and "coincide only when N_0 = 2" are right (N_0 ≥ 2 at CA-I 53773). "Adoption … requires the s-endpoint reading" is gate input (c). |
| Limits, 24–28 | pda 18, 202; freeze 245; gate verdict items 1–4 | FIX F3 (range 45622–45634 is too wide). FIX F4 (two freeze-scope items are missing; verdict 2 below). |
| Retained geometry, 30–35 | pda 53–69; gate "Inherited inputs" | FIX F4 (the account reads these inputs from Balaban; it does not prove them). The T8 sentence matches gate (3). |
| Data, 39–56, display (1) | pda 34, 82–90 (S); gate (3) item 1 | PASS. "1 ≤ h" is gate (3) item 1 (CA-I 45848). "Every increasing ratio a nonnegative power of L" follows from R_i/R_{i+1} ≤ L with R powers of L. |
| Conventions, 58–62 | pda 43, 71, 98 | PASS |
| Old label and old (A1), 64–79, (2) | pda 12–17, 55; gate (1) | PASS. The four clauses match CA-I 45582–45588. |
| Retained inputs, 81–103, (3), (4) | pda 56–67 (items 2–4, T8, T10); gate (3) items 3–4 | PASS. Side LMR_{i+1} at level-i scale equals σ_{i+1}. The open neighbourhood in (4) is the version pda 67 allows. |
| (G) not used, 105–106 | pda 69 | PASS |
| Choice (C), (5), 108–126 | pda 39–51; gate (2) | PASS. The bound Σ_{r=s+1}^{k} m_r < ML/(L−1) < 2M is gate (2) item 3. |
| Replacement rules, 128–130 | pda 71 | PASS |
| Claim, 132–135 | pda 92, 235; freeze 241–243 | PASS |
| Grid and component boundary, 139–168, (6) | pda §1, 96–114; gate (3) items 5–6 | PASS. Z_i ⊂ Z_{k−1} for i < k gives the extension of (3), as in pda 108. |
| Upper interpolation, 170–210, (7), (8) | pda §2, 116–148 (U1–U3); gate (3) items 7–9 | PASS. a_i ≤ 7M < 10σ_k holds by the finite sum and σ_k ≥ LM. |
| Lower members and junctions, 212–236, (9), (10) | pda §3, 150–167 (L1, L2); gate (3) items 10–11 | PASS. pda's citation 53793–53796 for Z_h ∩ X ⊂ D_{h+1} is dropped; this is harmless. |
| Global gluing, 238–266, (11), (12) | pda §4, 169–196 (G, G1, G2); gate (3) items 12–13 | PASS. m_{i+1} = Lm_i ≥ m_i in case 2. The stronger-gap remark matches pda 194. |
| Stopped prefixes, 268–276 | pda §5, 198–202; gate (3) item 14 | PASS. pda's third range 48841–48863 is dropped; this is harmless. |
| Provenance, 278–284 | pda 3, 229; freeze 241; gate header | PASS as written. FIX F5 adds this check after F1–F4. |
| Issue text, 1–15 | the note | FIX F1, F4, F5 (issue versions below). The title, scope, "Not covered" and status sentences match the note. `@LINK@` is a placeholder for the posting step. |

**New steps.** None. Each step of out-pda.md is a step of pda.md, sometimes in shorter words.

**Internal names and credit.** No gate, lane, FINISH, frozen, registry, row, port, P4, PDA, T8, T10, GEOH, DOM or ST1 name occurs in either text. No file path occurs. No novelty word occurs. No sentence credits the addressees for their own work. The account's words are addressed as "your" throughout. F2 corrects one "your" that belongs to Balaban.

## Explicit verdict 1: the endpoint defect

**Real. Stated slightly too broadly in one word. Errata class A.**

What the account says.
- CA-I 51712: "The two top members $Z''_k$ and $Z''_{k-1}$ are defined in \cite[(1.10)]{B-CMP122a}."
- CA-I 51713: "These are completed to a sequence $Z''_k,Z''_{k-1},\dots,Z''_{k-N_0+1}$".
- CA-I 51718–51721: the five-layer formula starts at $j=k-N_0$.
- CA-I 45600: "$Z''_k$ and $Z''_{k-N_0+1}$ are defined in \cite[(1.10)]{B-CMP122a}". 45609 quotes the completion as "$Z''_k, Z''_{k-1},\dots,Z''_{k-N_0+2}, Z''_{k-N_0+1}$".
- CA-I 92015 quotes (1.10): "$Z''_{k-N_0+1}=(Z'_{k-N_0})^{\sim}=(\Omega^{\sim7}_{k-N_0+1})^c\cap Z$".
- The account's own restatements agree with 45600, not with 51712: CA-III 9890–9896 ($Z''_k$ and $Z''_{k_0+1}$, "These two sets are completed …"), CA-III 28121 (the same display), and CA-I 53774–53782 ($I_M=\{k_0+1,\dots,k\}$, top member $Z''_k$).
- No other line of CA-I, CA-II or CA-III names $Z''_{k-1}$ as defined in (1.10). The other occurrences of $Z''_{k-1}$ (CA-I 51715, 64301, 91672; CA-II 13242; CA-III 9898, 9902, 9923) use it as a member of the completed sequence.

So the defect is real. With 51712 as written, the bottom member $Z''_{k-N_0+1}$ gets no formula in 51707–51728, and the sequence of 51713 would have three members fixed in advance. The two readings agree only when $N_0=2$; the account allows $N_0\ge2$ (CA-I 53773).

Narrower statement. 51712 does not use the word "endpoint". It says that the two members defined in (1.10) are $Z''_k$ and $Z''_{k-1}$. The note's "names $Z''_{k-1}$ as the second prescribed endpoint" (line 13) is the meaning of 51712 only once 51712 is read together with 51713. The exact statement is: 51712 names $Z''_k$ and $Z''_{k-1}$ as the two members defined in (1.10), where 45600, 45609 and 92015 name $Z''_k$ and $Z''_{k-N_0+1}$. F1 puts this in the note.

Class. **A.** It is one index in a summary bullet, plus the word "top", which no longer fits. No statement of the account changes, and no proof in the account uses 51712 as a formula: 51712 gives no formula. The account's arguments that need the bottom member read it from 92015 and CA-III 9890–9891, 28121. Errata text:

> CA-I 51712: replace "The two top members $Z''_k$ and $Z''_{k-1}$ are defined in" by "The two end members $Z''_k$ and $Z''_{k-N_0+1}$ are defined in".

Side remark, not a fix. CA-III 28123–28132 carries two readings of the (1.10) display, (A) $(Z'_{k_0})^{\sim1}$ and (B) $W_a\setminus(\Omega_{k_0+1})^{\sim7}$, which the display asserts are equal. The note and pda.md use (B). The note is faithful to pda.md here.

## Explicit verdict 2: claims beyond pda.md's checked scope

**No claim goes beyond the checked scope. Two scope items of the freeze annotation are missing (F4).**

- Every claim of the note is in pda.md and in the freeze scope (freeze 243): geometric (A1) for the prepared nest with rule (C), every componentwise stopped prefix, given old (A1), as one operation step. The preserved stronger gap (note 261–262) is pda 194 and pda 235. "No new constant or coupling ceiling" (note 135) is pda 92. "At least one layer is forced" (note 124–126) is gate (2).
- The Limits paragraph (24–28) keeps out (A2), the produced-nest induction, the old-label premise and the supply conditions, as freeze 245 does.
- Missing item 1: freeze 245 lists "the inputs read from Balaban rather than proved (53816–53831, 48164–48168, 92012, 92015)". The note calls these "account inputs" (line 32) but does not say that the account itself takes them from Balaban without proof. A reader could take them as proved in the account.
- Missing item 2: freeze 245 says that CA-II 145579 and CA-III 21303, 53328, 111073, 111311 cite the same pages for other content, not covered. The note and issue cite "CMP 122a, pp. 178–179" without this limit.

Neither omission makes a false claim. F4 adds both, so the note states the full checked scope.

## FIX items with replacement text

**F1 (note lines 13–14; issue line 9). Endpoint wording.** Note: replace lines 13–14 ("Your [CA-I 51712](…) names \(Z''_{k-1}\) as the second prescribed endpoint. The construction below instead uses \(Z''_s\), as named at [CA-I 45600](…).") by:

> Your [CA-I 51712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L51712) says that the two members defined in Balaban's (1.10) are \(Z''_k\) and \(Z''_{k-1}\). Your [CA-I 45600](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45600) and the quotation at [CA-I 92015](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92015) name \(Z''_k\) and \(Z''_s\). The construction below uses \(Z''_s\) as the second endpoint. A one-index fix at 51712 would read: "The two end members \(Z''_k\) and \(Z''_{k-N_0+1}\) are defined in (1.10)."

Issue: replace "[CA-I 51712](…) names $Z''_{k-1}$ as the second endpoint." by "[CA-I 51712](…) says that the two members defined in Balaban's (1.10) are $Z''_k$ and $Z''_{k-1}$." Keep the rest of the paragraph.

Reason: 51712 says "two top members … defined in (1.10)", not "endpoint" (verdict 1).

**F2 (note line 8). Attribution of the representation.** Replace "Your representation sums over admissible sequences; the later produced-nest assertion concerns the whole history." by:

> Balaban's representation, CMP 119, (2.18), as your account cites it, sums over admissible sequences. Your later assertion about the produced nests concerns the whole history.

Reason: CA-I 4224 reads "The representation \cite[(2.18)]{B-CMP119} of $\rho_k$ is a sum over admissible sequences". It is Balaban's, not the account's.

**F3 (note line 26). Citation range.** Replace "Your text keeps (A2) separate at [CA-I 45589–45591 and 45622–45634](…#L45589-L45634)." by:

> Your text keeps (A2) separate at [CA-I 45589–45591 and 45622–45624](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L45589-L45624).

Reason: 45626–45634 states that the produced-nest lemma supplies (A1) and (A2) together, with the stronger margin. It does not keep (A2) separate. pda 18 and gate (1) cite 45622–45624.

**F4 (note lines 24–35; issue lines 7 and 11). Full checked scope.** Note: after line 32 ("These are account inputs, not conclusions of this note. They are stated precisely below.") insert:

> Your account reads the cell and alignment inputs from Balaban's text and does not prove them ([CA-I 53816–53831](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L53816-L53831), [48164–48168](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L48164-L48168), [92012](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92012)). The same holds for the endpoint quotation at [92015](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L92015). This note does not prove them either.

After line 27 (the supply-conditions sentence) insert:

> Your account also cites CMP 122a, pp. 178–179, for other content at CA-II 145579 and CA-III 21303, 53328, 111073 and 111311, for example constant conditions and a point count. This note does not cover those uses.

Issue, line 7: after "and ten-layer margin." insert "Your account reads these from Balaban's text; the note does not prove them." Issue, line 11: append "Other content cited from CMP 122a, pp. 178–179, at CA-II 145579 and CA-III 21303, 53328, 111073, 111311."

Reason: freeze 245 and gate "Inherited inputs" (a)–(c), verdict item 3, and gate (4) item 4 (verdict 2).

**F5 (note lines 280–282; issue line 13). Provenance, after F1–F4.** Note: replace "Codex wrote this outward version. The recorded Claude check concerns the working proof, not this outward version." by:

> Codex wrote this outward version. Claude (Opus 5.5) checked it line by line against the checked proof.

Issue: replace "Codex wrote this outward version. … The recorded check concerns the working proof." by "Codex wrote this outward version, and Claude (Opus 5.5) checked it line by line against the proof." Keep the CMP 122a sentence. Apply F5 only after F1–F4 are applied.

Optional, not a fix: the note may link the checked proof, `library/pda.md` at `4321201aa` on `origin/claude/ym4d-hard-route`. The note is complete without it. pda.md uses internal names (P4, GEOH, DOM, ST1, port), so the link is an owner choice.

## First failing step

First failing step: none. No step is false, unproved or new. F1–F5 concern wording, one citation range, one attribution, scope sentences and provenance.

## Overall verdict

**FIX.** out-pda.md is faithful to pda.md and pda-gate.md in every statement, hypothesis, constant and proof step. The endpoint defect is real and errata class A. The note claims nothing beyond the checked scope. It needs F1–F5 before posting. The material ones are F1 (the defect as 51712 actually states it) and F4 (the account's Balaban-read inputs and the other pp. 178–179 uses stay outside the proof). F2, F3 and F5 are attribution, citation and provenance.

Checked line by line by Claude (Opus 5.5).
