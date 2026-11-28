# Check: library/out-live.md and library/out-live-issue.md

Claude (Opus 5.5), 2026-11-08. One faithfulness check of the outward note (653 lines) and the issue text (15 lines), both by Codex gpt-6-astra.
Sources: CA-I `theorem_0_complete_account_raw_I.tex` (31a47c543775), SA `YM4_sketch_500.tex` (31a47c543775), N `YM4_1400.tex` (local copy used by the proof check).
Basis: library/geoh-live-ab.md and gates/geoh-live-ab-check.md (ADVANCE). This check is not an audit.

## Verdict: FIX

The claims about their text are right, and the mathematics is the checked proof.
Four text fixes are needed before posting: the credit sentence (finding 4), the ambiguous "separate question" sentence (finding 5), internal process text in note §8 (finding 6), and the attribution of Bałaban's rules as "your" rules (finding 7).
Findings 8-9 are small wording fixes. No finding changes a bound.

## Findings

1. **"Proof outstanding" and use as hypotheses. CONFIRMED.**
   Note 5-6, 30-36; issue 5. CA-I 85575 reads: "\begin{definition}[Geometry and counting of live large-field regions. Proof outstanding]". CA-I 85598 reads: "The following statements are used in this chapter as hypotheses."
   Later uses repeat this, for example CA-I 85757 "(proof outstanding)" and CA-I 86927 "whose proof is outstanding".
   The clauses at CA-I 85602-85641 and the contour hypothesis at 85644-85648 match the note's rendered text (note 41-98) word for word.

2. **YM4_1400 does not prove the invariant. CONFIRMED; the search record is accurate.**
   My own searches of N: "proof outstanding" has no hit. `live[- ]strips?` hits exactly the 17 lines in note 617. `101` hits exactly 81387, 81388, 85138, 85173, 100889, 127775, 136629. Literal `5/2` hits exactly the 7 lines in note 620. `\tfrac52`/`\frac52` hits exactly 127519, 127536, 127542, 127762, 127768. No `7\check R` clause. "birth collar" has no literal hit; "birth-scale collar" is at 85185.
   "persist" hits are unrelated (2461-2470 is hypothesis D3 on age-resolved rarity, an assumed input; 41023 is carrier lifts). No `\label` names a live-strip, pocket or birth-collar statement.
   I read N 81370-81395, 85115-85215, 127474-127500, 127610-127662, 71095-71110, 85380-85395, 84478-84490. Each uses the strip geometry (side bound, collar, separation) or proves a conditional filing fact. None proves the persistence induction.
   N 63684 is the closed-endpoint quiet class with no joining. N 63713-63771 traces a component under "the exclusion of marks at levels h,...,k-1". N 71104-71106 says "the class rule excludes ... a second-class mark at h itself". So N's ingredients are for the stricter class, as note 631 says. Not BLOCK.

3. **Clause table and mathematics. CONFIRMED.**
   Note 100-111 and issue 7, 11 match the check table: proved (a) for i ≥ m, (b), (c), (d), (e), (h); (g) only m ≤ h; not (f), the rest of (g), (i1), (i2), the contour hypothesis.
   I diffed note §§2-6 against geoh-live-ab.md §§2-6 after normalising R to Ř and stripping links. Equations (1)-(15) are identical. The only changes are wording ("Sussman–Alpoge's" to "your") and the two citation repairs of the check (findings 5 and 6 there: note 234 cites CA-I 53783; note 247 calls N's quiet boxes the special case). No new proof step.
   New text outside the proof: note 137-145 and 646-649. CA-I 63776-63786 reads "It remains to prove clauses (e)--(i)" and takes (e) from "condition (G0)". CA-I 63909-63915 is the treated-collar subtraction. Both claims are accurate. Note 575 (N 63684 closed endpoint, no joining) is accurate. Note 572-573 (SA 17440 "Marks wait", SA 17575 "the lower end point included") is accurate.

4. **Credit sentence. FIX (rule).**
   Issue 9: "Credit belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of your text." Note 12-13: "Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of your text, for the definitions, construction rules, and arguments cited here." Both give third-person credit to the readers.
   Replace issue 9, sentences 1-4, with:
   > The scope is a finite-history geometric invariant. The inputs are your definitions, your statement of the construction rules, and your conditional collar calculations. The large-field method, the T rule and the preparation geometry are Tadeusz Bałaban's (CMP 119, §3, and CMP 122, §1, as your account cites them).

   Replace note 12-14 with:
   > The definitions, the statement of the construction rules, and the arguments cited here are yours.
   > The large-field method, the T rule and the preparation geometry are Tadeusz Bałaban's.

5. **"Matching these rules to the revised operation is a separate question." FIX (ambiguous).**
   Issue 11, last sentence; note 579 ("The match to a separately revised operation and its selectors remains a separate question."). Readers will take "the revised operation" to be their revised outline. The mismatch in GEOH-O1 is about our own selector (ti-2), not theirs. Delete both sentences.
   For the endpoint, replace issue 9, last two sentences ("Your account allows the open lower endpoint. The note distinguishes this from the outline's closed-endpoint rule."), with:
   > Your account allows an operation at the lower endpoint of the exclusion window. Your outlines exclude it (YM4_sketch_500.tex, lines 17440 and 17575; YM4_1400.tex, line 63684). Under that closed-endpoint rule the narrow case h = m does not occur, and the same bounds hold.

   Sources: SA 17440 "Marks wait: a mark of level s lying inside a class component of level t satisfies s<t_♭"; SA 17575 and N 63684 "[k_♭,k), the lower end point included". This is what geoh-live-ab-check finding 12 confirmed (it cites SA 17435; the "Marks wait" sentence is on line 17440). Note 576-577 already says this; keep it.

6. **Internal process text in note §8. FIX.**
   Note 595-601 names our index ("the full-read outline index", "the CA index entries"), our earlier lane ("The earlier prior-work comparison"), our repository ("The repository already contained the checked proof reproduced here"), our task ("This task packages that proof and repairs its citations") and our open rows ("The separate operation, code/read, and carrier-lift questions were not taken over"). Replace note 595-601 with:
   > We first read SA 6055–6115, 17317–17449 and 17575 onward, and CA-I 45985–46032 and 53765–53819. We then ran the searches below on all of N.

   Keep the link on SA 6055–6115 and the CA-I links.

7. **"Your" for Bałaban's rules. FIX (attribution).**
   Note 127 ("Your eight-layer T rule"), 223 ("This is your eight-layer T rule at CA-I 50196–50229"), 129 ("Your five-layer lower preparation"), 130 ("Your upper prepared gap"), 131 ("Your nested prepared members"). CA-I 50226-50229 says the eight-layer display "is Ba{\l}aban's definition \cite[(3.5)]{B-CMP119}, rewritten". CA-I 53776 introduces "The prepared sequence ... of \cite{B-CMP122a}". The eight-layer form is their rewriting; the rule is Bałaban's.
   Replacements:
   - Note 119: "### Construction rules used below, as your account states them"
   - Note 127, first cell: "Bałaban's T rule in your eight-layer form, followed by two further layers and monotone boxing"
   - Note 129-131, first cells: "Bałaban's five-layer lower preparation", "Bałaban's upper prepared gap", "Bałaban's nested prepared members, main box, and stage collars"
   - Note 223: "This is Bałaban's T rule in the eight-layer form your account derives at [CA-I 50196–50229](...), with the two further layers and monotone boxing at [CA-I 50342–50368](...)."

8. **Internal jargon. FIX (minor).**
   - "port": note 195 "The birth size gives a port, not a fresh research claim." → "The birth size bound is your calculation." Note 208 "This is the same-level port from" → "This is your same-level calculation at". Note 226 "we port it here" → "we use it here". Note 485 "Use the ported T-buffer argument from" → "Use your T-buffer argument at". Note 504 "The radius comparison is the port used in (3)." → "The radius comparison is the one used in (3)."
   - "CA" is not defined in the note: note 263 "CA's exclusion interval" → "Your account's exclusion interval"; note 315 "CA's class" → "Your account's class".
   - "grants no status" means nothing to the readers: issue 15 → "This is a proposed proof for your review. It is research text, not an audit." Same change at note 19. At note 114, delete "It grants no status to the account or its other hypotheses."
   - Issue 5 "the pinned revised outline, YM4_1400.tex" → "your revised outline, [YM4_1400.tex](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex) at commit 2bc0658f".

9. **Lemma lettering. FIX (minor, optional).**
   Note 141 and 646: the partial proof at CA-I 63772-63916 is the proof of Lemma 4.21 (label `4.21:lem-live-region-geometry`), whose clause (e) is strip connectedness and containment (CA-I 63784-63786). That differs from clause (e) of the 4.22 definition. Write "clauses (e)–(i) of your Lemma 4.21" at note 141 and 646.

10. **Issue 13 and the placeholder. CONFIRMED, with one reminder.**
    "Claude (Opus 5.5) checked the proof line by line, and its repairs are applied" is accurate (geoh-live-ab-check, ADVANCE, repairs 5 and 6 are in note 234 and 247). This check is a second Claude reading of the outward text, not an independent model. `@NOTE_LINK@` (issue 7) must be filled before posting.

## Who checked what

Checked line by line by Claude (Opus 5.5) against CA-I 85575-85648, 63500-63570, 63772-63800, 63905-63916, 64420-64480, 45990-46032, 50196-50230, 50342-50368, 53765-53790, 63588-63593, 132160-132177; SA 17433-17440 and 17575; N 63678-63740, 63684 and the passages in finding 2. Codex wrote the note and the issue.
