# out-lrb-check: faithfulness of library/out-lrb.md and library/out-lrb-issue.md

Provenance: Claude Opus 5.5 (claude-opus-5-5). One reading by one model. Not an audit; grants no status. No computation. Read-only use of sources; this file is the only write.

**Checked texts.** `library/out-lrb.md` (1140 lines, SHA-256 `3b47c1b6…f2ee2e4`) and `library/out-lrb-issue.md` (20 lines). Codex prepared both.

**Sources.**
- `library/lrb.md` (862 lines, SHA-256 `23b7d710…2552969d`). The body is the 847-line text that the gate checked. Lines 849–862 are the change log with the eight one-sentence clarifications that answer gate findings 1–8.
- `gates/lrb-gate.md`: first failing step none; findings 1–8, all repairable.
- The account at `31a47c543775`: CA-I, CA-II and the outline `YM4_sketch_500.tex` in `/Users/jonreilly/ym4d-lead/sa/`.

Account ranges read for this check: CA-I 1490–1497, 4860–4885, 5125–5135, 5154–5194, 5948–5956, 6095–6154, 6380–6388, 6959–6984, 7303–7315, 7845–7846, 7990–8108, 8108–8395, 8555–8600, 8634–8640, 8646–8706, 8733–8740, 8761–8837 (search), 9200–9353 (search), and single lines 4636, 7474, 7491, 7530, 7540, 8653–8654, 8678–8681, 9665–9668, 9762–9767, 9774–9777. CA-II 3528–3570, 3596–3626, 3706–3724. Outline 14155–14218, 14251–14270. No Balaban page image was read: no step of the note rests on a page that this check could test against an image. CMP 116 is not in the local folder (gate, "Quotations").

## Result

The mathematics of out-lrb.md is that of lrb.md. Every clause, hypothesis, constant and exponent matches. The gate's findings 1–8 are present in the note text, not only in a change log. The note adds four kinds of text that lrb.md does not have: a short proof of the Schur-norm facts, a transcription of (k1)–(k3) and of the floors, an explicit constant in (23), and a re-proof of the vertex identity. I checked each one. All are correct. No step is false.

Six items need a fix. Two are about a source: the dμ₀ convention is attributed to the account and to Balaban's (2.8) more firmly than the sources allow (F2), and the vertex paragraph restates the authors' own printed proof as ours (F3). The others are a missing abbreviation (F1), one wrong reason (F4), provenance (F5) and the issue text (F6).

## Per-section table

Line numbers: out-lrb.md first, then lrb.md.

| out-lrb.md | Source | Verdict |
|---|---|---|
| Opening, 3–24 | lrb 5–48, Result 833–845, change log 2; CA-I 8110, 8316–8347, 8564–8575, 4875–4907, 5120–5216; outline 13904–14089, 14159–14218, 14251–14270 | FIX F1 ("SA" is not defined). The "Proof outstanding" quotation is right (CA-I 8110, 8373). The qualification of "verbatim" (CA-I 8316) and of (4b) (8340–8347) is gate finding 2, applied. The outline citations match: 14161–14165 is \(C=(\chi\mathsf A(s)\chi)^{-1}\); 14258–14260 calls gap and closeness "obligations". CA-I 4882 cites CMP 99b for the walk setting. |
| Setting, 26–64 | lrb 67–83, 104–107; CA-I 8132–8169, 7845–7846, 4623–4642 | PASS. \(Y\) with \(\mathbb B(H)\subseteq Y\subseteq\mathbb B(T)\), and \(Y=\mathbb B(T)\) in \(\mathcal S_0\), is CA-I 7845–7846. \(Z\) "any … admitted" in \(\mathcal S_0\) is CA-I 8137. The display of \(K(\sigma;\mathsf u)\) is CA-I 8156–8157. |
| (a), 66–102 | lrb 69–74, 92–102; CA-I 8111–8116, 5519–5578, 6095–6154, 6959–6984 | PASS. The (k1)–(k3) display is NEW as a transcription. I checked it against CA-I 6105–6133: every symbol and constant agrees. "Sup-diameter at most 4ℓ" is the side bound of \(q^\sharp\) under (k2) (CA-I 6138). |
| (b), (c), 104–117 | CA-I 8117–8130, 1492–1496 | PASS. \(e^{243\kappa_1}\le e^{\theta M/64}\) is restated as \(243\kappa_1\le\theta M/64\), which is equivalent. |
| (d), 119–143 | CA-I 7995–8036, 8055, 8075–8082 | PASS. NEW transcription. \(\beta=1/4\) "only \(\beta\ge0\) used" is CA-I 7995–7996. \(\mathsf r_s\), \(\eta_{\rm sym}\), \(\mathsf r^*\) and the three floors are CA-I 8024–8036. The radius-floor consequence: \(\rho-\varsigma\ge(1+\beta)\cdot3/\varepsilon_0^{P'}\), so \(\varsigma/(\rho-\varsigma)\le\varepsilon_0^{P'}/3\). |
| CMP 116 setting, 145–179 | lrb 525–546, 662–682; change log 1, 8; gate finding 1; CA-I 7303–7314, 8737; CA-II 3528–3537, 3600–3624 | FIX F2 (dμ₀ source). The potential inputs and the normalised density \(H_C=\operatorname{sym}C^{-1}\) match lrb. |
| Clauses proved, 181–276 | CA-I 8188–8371; lrb 125–363, 833–845; change log 3, 4 | PASS. (1), (2σ), (2U), (2s), (2Γ) restate the printed clauses with the same constants. (3) is the stronger \(\tfrac12\gamma_*\) of lrb 360, and names (a), (c) (gate finding 4). (4a)–(4c) are stated as lrb proves them, with the written replacements (gate finding 2). |
| Replacements, 278–359 | lrb 430–524, 548–651, 712–729 | PASS. (21), (22), (24), (25) and (34) are lrb (21), (22), (24), (25), (34) with their hypotheses (38). NEW: the explicit constant \(3(Q+1)^2D_0\hat\varepsilon\) in (23). Check: with \(D_0\hat\varepsilon\le1\), \(|C|_a,|\Gamma|_a\le Q+1\), and the three terms cost \((Q+1)^2\), \(Q(Q+1)\), \(Q^2\) times \(D_0\hat\varepsilon\). The display of (34) writes the density of \(d\mu_C\) out; for real \(B\), \(B^{\mathsf T}C^{-1}B=B^{\mathsf T}H_CB\). "What this proof does not do" matches lrb 819–827. |
| Proof §1, 363–430 | lrb §3, 67–124; gate finding 8 | PASS. "There are no parameter cubes inside int H" is finding 8, applied. NEW: the proof of Schur multiplicativity and of \(\|K\|\le|K|_0\le|K|_a\), where lrb cites CA-I 4908–4983. Check: the triangle inequality \(e^{a|b-z|}\le e^{a|b-y|}e^{a|y-z|}\) gives the row bound; the Schur test gives the norm bound, and \(\sqrt{xy}\le\max\{x,y\}\). |
| Proof §2, 432–500 | lrb §4, 125–192; gate finding 8 | FIX F4 (reason at line 436). The rest matches lrb line for line. |
| Proof §3, 502–530 | lrb §5, 194–222 | PASS. Identical except the cross-reference "proof §2" for "§4". |
| Proof §4, 532–639 | lrb §6, 224–332 | PASS. Identical except "your Combes–Thomas comparison" for "the source's inverse comparison" (gate: CA-I 8411–8471 line for line). |
| Proof §5, 641–670 | lrb §7, 334–362; change log 3, 4 | PASS. Line 649 adds the reason for \(t\le1/4\) (finding 3). Its source is CA-I 5950–5954 (form coercivity \(\ge\gamma_*\)) and 6385–6387 (\(\gamma_*\le\mathsf B\)). Line 669 names (a), (c) (finding 4). |
| Proof §6, 672–827 | lrb §8, 364–524 | PASS. Identical; the displays of (21)–(25) are repeated without tags, and the tags are those of the Replacements section. |
| Proof §7, 828–1034 | lrb §9, 525–729; change log 1; CA-II 3528–3567, 3600–3624, 3706–3722 | FIX F2 (line 859). NEW, lines 986–989: the meaning of \(D\), \(\chi_{Y_0}\), \(\chi^c_{P_{\rm fail}}\), \(T\). Check: CA-II 3540 writes the cutoff as \(\prod_b\chi(\lvert B(b)\rvert<T)\), and \(P\) is a set of bonds, so each failed factor forces \(\lvert B(b)\rvert\ge T\) and every cutoff factor has modulus at most one. (37) then follows. (36) is CA-II 3716–3719 with \(c_V\ge O(1)\). Line 1013 names (21)–(25) and (34) as the explicit form (finding 2). |
| Proof §8, 1036–1113 | lrb §10, 730–798; change log 5; CA-I 5154–5194 | FIX F3 (lines 1099–1106). Lines 1088–1091 add the \(t(Y)\), \(\tau(Y)\) integrals (finding 5); (36) is a bound on the τ-circles (CA-II 3712–3719), so it is uniform there. |
| Uses, 1115–1132 | lrb §11, 800–822; change log 6, 7; CA-I 8776–8817, 9217–9220, 9245–9246, 9350–9351, 9665–9668, 9762–9777 | PASS. The CA-III 111058 sentence is removed (finding 6). The (R9) sentence is finding 7; the replacement pair at CA-I 9220 is \(\max\{\mathsf B,4S(2/\gamma_*),4S(2/\gamma_*)^{1/2}\}\), and \(4S(2/\gamma_*)=8S/\gamma_*\), so the note's pair is the same. "Word for word" is CA-I 8779, 8817. CMP 116 Lemma 3 and the CMP 119 §3 analogue are CA-I 9245–9246. |
| Who wrote and checked, 1134–1140 | lrb 1–3, 849–850; gate | FIX F5 |
| Issue text | the note | FIX F6. The four replacement bullets, the "Not covered" paragraph and the scope sentence match the note. |

Internal names and credit. No gate, lane, FINISH, frozen, lead, round, registry, U-code or working-file path occurs in either text. The hypothesis codes that occur, (a)–(d), (k1)–(k3), (W′), (R9), (f1), (f4), are the account's own. "Obligations" (note 24) is the outline's own word (outline 14259). Residues: the undefined "SA" (F1) and the placeholder `@LINK@` in the issue (F6). No novelty word occurs. No sentence credits the addressees for their own work. One paragraph does the reverse: it restates their printed proof as part of ours (F3).

## Explicit verdict 1: the gap it claims to close

**The gap is as stated: the proposition is printed without a complete proof. The issue text should say more narrowly which parts are missing (F6).**

- CA-I 8110 heads the proposition "Proof outstanding", and CA-I 8373 repeats "Proof outstanding." A Route follows (8376–8389).
- The account then prints continued proofs. CA-I 8391–8562 proves (1), (2s) and (2Γ); the gate found that lrb §6 reproduces it line for line. CA-I 8564–8759 proves (3) and (4) from (2σ), (2U) and six inputs listed at CA-I 8566–8575.
- What is not printed: a proof of (2σ) and (2U) (8578 calls them "the preceding parts", but 8391–8562 contains neither); the kernel and product lemmas, which 8633–8645 only reduce to (2σ) and (2U); and the perturbation lemma (i)–(iv), the positivity lemma and the lemma for CMP 116 (2.16)–(2.17). The gate searched CA-I, CA-II, CA-III and the outline and found no text of these three lemmas (gate finding 2). The walk count is hypothesis (c). The restriction theorem is printed and proved (CA-I 33276).
- The note states this correctly at lines 15–17 and 278–359. The issue says only "marked 'Proof outstanding'" and "completes clauses (1)–(4)". A reader could take this to mean that the account has no proof of (1), (2s), (2Γ). F6 gives the narrower text.

## Explicit verdict 2: inputs the account does not itself prove

**PASS.** Every such input is listed before the proof.

| Input | Where listed | Who wrote and checked |
|---|---|---|
| Hypothesis (a): local half of (W′), cell-resolvent, local coercivity, symmetric-part lemma through Cor. `4.4:cor-polymer-base-form` | Setting (a), 66–92; "The full unprinted symmetry premise remains an input" (92) | The authors' hypotheses. Retained, not proved; not checked by us. |
| (b), (c), (d) | 104–143 | The authors' hypotheses, retained. |
| CMP 116 (1.42), (1.43), (1.36) and the bound (36) | 145–149, 179; issue "Not covered" | Balaban's, as read in CA-II 3528–3537, 3706–3722. Not checked against CMP 116 (note 14; issue). |
| dμ₀ as the unit Gaussian | 166–170 | A convention we fix. The source attribution needs F2. |
| Fixed cutoffs, later ceilings on α₄, γ₂ | 147, 175–177 | Balaban's, retained. |
| Replacements for the unprinted lemmas: (21)–(25), (34) | 278–359, before the proof | Written by Codex and checked line by line by Claude (lrb-gate). Provenance is at 1134–1140; F5 completes it. |

The account results the note uses with their printed proofs are Cor. `4.4:cor-localised-covariance`, Cor. `4.4:cor-polymer-base-form`, Lemma `4.4:lem-local-coercivity`, the interpolation lemma (CA-I 5154–5194) and Theorem `4.8:thm-restriction-units`. They are the authors' work, cited as such, and need no entry. The normalisation argument at outline 14023–14034 is the authors' too, and the gate checked it.

## Explicit verdict 3: scope

**PASS.** The note claims what lrb.md and lrb-gate.md support, and no more.

- lrb Result and the gate verdict: the proposition holds under (a)–(d) and the CMP 116 (2.14) setting, for the assigned families, with three readings. (4a)–(4b) hold through the written estimates (21)–(25) and (34). dμ₀ is the unit Gaussian. The CMP 116 inputs are taken as the account reads them. (4c) holds on a neighbourhood of the closed σ-polydisc at local hereditary representatives, without a global extension.
- The note: the opening (8–10), "Clauses proved" (4a)–(4c), "What this proof does not do" (355–359), the Uses table ("not a claim about every transitive use", 1132) and the issue's "Not covered" paragraph state the same three readings and the same limits. Clause (3) is stated with \(\tfrac12\gamma_*\), which lrb 358–360 proves.
- Nothing in either text claims the upstream premises, the full account or T0.

## FIX items with replacement text

**F1 (note line 13).** "SA" is used at lines 21, 22, 24, 844 but never defined. Replace "CA-I and CA-II denote Parts I and II of your complete account." by:

> CA-I and CA-II denote Parts I and II of your complete account. SA denotes your outline `YM4_sketch_500.tex`.

**F2 (note lines 166–170 and 858–859): the dμ₀ convention.** The account does not state the covariance of dμ₀. CA-I 7311 says only "the measure of \(X\)" of CMP 116 (2.8), and CA-II 3622 says only that it is restricted to \(Z\). CMP 116 is not available to check (2.8). So "of Balaban's (2.8)" (166, 858) and "as read in your account" (859) state more than the sources show. Line 859 also conflicts with line 170. Account support exists only in an indirect form: the convergence test at CA-I 8737 ("converges … if and only if the coefficient of ½‖ZX‖² is less than one") uses the unit normalisation.

Line 166: replace "Use the unit auxiliary Gaussian of Balaban's (2.8):" by "Use the normalized unit auxiliary Gaussian:".

Line 170: replace "We retain this convention explicitly; your displayed integral alone does not define its covariance." by:

> We retain this convention explicitly. Your account calls \(d\mu_0\) the measure of \(X\) in Balaban's CMP 116 (2.8) ([CA-I 7311](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L7311)) and does not state its covariance. Your convergence test at [CA-I 8737](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8737) uses this normalization. We did not check it against CMP 116. If \(d\mu_0\) has instead a bounded covariance \(\Sigma\) fixed before \(M\), replace \(D_X\) by \(\Sigma^{1/2}D_X\Sigma^{1/2}\) in proof §7 and \(v\) by \(\|\Sigma\|v\); only early constants change.

Lines 858–859: replace "Take \(d\mu_0(X)=(2\pi)^{-n/2}e^{-|X|^2/2}dX\), the normalized unit Gaussian of Balaban’s CMP 116 (2.8). We retain this convention as read in your account." by:

> Take \(d\mu_0(X)=(2\pi)^{-n/2}e^{-|X|^2/2}dX\), the normalized unit Gaussian retained in the Setting.

Check of the Σ sentence: \(\int N(0,\Sigma)(dX)\,e^{\frac12X^{\mathsf T}D_XX}=\det(I-\Sigma^{1/2}D_X\Sigma^{1/2})^{-1/2}\) when \(\|\Sigma\|v<1\). The rank stays at most \(3m\). So (32) holds with \(\|\Sigma\|v\) in place of \(v\), and (38) needs one extra early factor \(\|\Sigma\|\). This is the repair the gate proposed (finding 1).

**F3 (note lines 1099–1106): the vertex identity.** Lines 1099–1105 are NEW relative to lrb, which cites CA-I 5154–5194. I checked them: they are correct. They are also the authors' printed proof of their interpolation lemma, step for step (CA-I 5158–5186: \(|\omega|=\overline O\), "an open set meets the closure of \(O\) exactly when it meets \(O\)", the two implications). Written without attribution, they present the authors' proof as part of ours. Replace lines 1099–1106, from "At a vertex, a walk multiplier is one" to "gives \(K(1_{\sigma'};\mathsf u)=K^{W(\sigma')}(\mathsf u)\).", by:

> At a vertex, your interpolation lemma, proved at [CA-I 5154–5194](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L5154-L5194) from the footprint convention, gives \(K(1_{\sigma'};\mathsf u)=K^{W(\sigma')}(\mathsf u)\), with \(Z\) as the ambient set.

**F4 (note lines 435–436): one wrong reason.** "Then \(x\notin\operatorname{int}H\), by the prescribed meeting convention." The meeting convention gives the point \(x\in\operatorname{int}\Delta\cap|\varpi|\). It is the position of the cube that gives \(x\notin\operatorname{int}H\): parameter cubes lie in \(Z\setminus\operatorname{int}H\) (CA-I 8141). Replace lines 435–436 by:

> By the meeting convention there is a parameter cube \(\Delta\) and a point \(x\in\operatorname{int}\Delta\cap|\varpi|\). Since \(\Delta\subset Z\setminus\operatorname{int}H\), we have \(x\notin\operatorname{int}H\).

**F5 (note lines 1136–1138; issue line 18): provenance.** Apply only after F1–F4 and F6. "First failing step" is a check-report phrase.

Note: replace lines 1136–1138 by:

> Codex wrote the proof. Claude checked it line by line and found no failing step; its clarifications are applied here. Codex wrote this outward version. Claude (Opus 5.5) then checked this version line by line against the proof, and its fixes are applied.

Issue: replace "Codex wrote the proof. Claude checked it line by line; first failing step: none. Codex wrote this outward version and incorporated the checker's clarifications. The Claude check concerns the underlying proof." by:

> Codex wrote the proof. Claude checked it line by line and found no failing step. Codex wrote this outward version, with the checker's clarifications. Claude (Opus 5.5) then checked this version line by line against the proof.

**F6 (issue lines 5 and the link).**

(i) The link target `@LINK@` is a placeholder. Replace it by the commit-pinned link to `out-lrb.md` before posting.

(ii) The gap (verdict 1). Replace "[This note](@LINK@) completes clauses (1)–(4) in an explicit form, under (a)–(d) and Balaban's CMP 116 (2.14) setting." by:

> Your continuation at [CA-I 8391–8759](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L8391-L8759) already proves (1), (2s) and (2Γ). It derives (3) and (4) from (2σ), (2U) and the inputs listed at CA-I 8566–8575. It does not print proofs of (2σ) and (2U), or the perturbation lemma (i)–(iv), the positivity lemma and the lemma for CMP 116 (2.16)–(2.17). [This note](@LINK@) proves (2σ), (2U) and the product estimates, and replaces those three lemmas by written estimates. With your continuation, this completes clauses (1)–(4) in explicit form, under (a)–(d) and Balaban's CMP 116 (2.14) setting.

## Optional, not fixes

- Proof §§6–7 repeat (21)–(25) and (34) without tags and cite them by number. The Replacements section (280) says where the tags are. A reader may still look for a tag in §6. Adding "(as in the Replacements section)" after the first untagged display at line 766 would help.
- Issue, "(34)" bullet: "cost proportional to the local dimension" may read "cost proportional to the local dimension \(m\)".

## First failing step

First failing step: none. No mathematical step is false. The NEW steps (Schur facts, §1; constant in (23); cutoff facts, §7; vertex identity, §8) are correct. F3 and F4 concern attribution and one stated reason, not truth.

## Overall verdict

**FIX.** The note is faithful to lrb.md and to the gate's eight findings in every statement, hypothesis, constant and step. It needs F1–F6 before posting. The material ones are F2 (the dμ₀ convention is credited to the account and to (2.8) beyond what the sources show), F3 (the authors' printed proof is restated as ours) and F6 (the issue does not say which parts the account already proves, and the link is a placeholder). F1, F4 and F5 are a name, a reason and provenance.

Checked line by line by Claude (Opus 5.5).
