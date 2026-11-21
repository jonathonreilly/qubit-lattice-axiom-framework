# out-lsc-check: faithfulness of library/out-lsc.md and library/out-lsc-issue.md

Provenance: Claude Opus 5.5 (claude-opus-5-5). One reading by one model. Not an audit; grants no status. No computation. Read-only use of sources; this file is the only write.

**Checked texts.** `library/out-lsc.md` (819 lines) and `library/out-lsc-issue.md` (17 lines). Codex prepared both.

**Checked sources.** `library/lsc.md` (724 lines); `gates/lsc2-gate.md` (round-2 check, first failing step none); `gates/nrm-check.md` (§§1, 2, 4–6, verdict); `gates/lsc-uses-check.md` (§§2–3, result); `gates/lsc-value.md` (all, decision in §5). Form follows `gates/out-gw-check.md`.

**Account ranges read for this check** (commit `31a47c543775`). CA-I 470–490, 641–667, 920–936, 2530–2545, 156998–157132, 159140–159165, 159285–159340, 159505–159522. CA-II 2791–2966 (selected), 59643–59682, 59739–59815, 61887–61912, 63096–63120, 63364–63368, 63964–64045, 64095–64246, 109918–109930, 140878–140928. Outline 23403–23416, 23478–23540. Other ranges are accepted from lsc2-gate and nrm-check, which read them.

## Result

The mathematics of out-lsc.md is that of lsc.md after its round-2 repair. Every statement, hypothesis, constant and equation (1)–(31), (N1)–(N6) matches lsc.md. No proof step is false. The new material is (i) the opening on the defect, (ii) the list of retained inputs in §2, (iii) the one-step paragraph in §3, and (iv) the expanded counterterm in §6.1. Each has a checked counterpart or matches the account; I checked each against the account lines. Nine items need a fix. Most are names, attribution and provenance. One sentence makes a false claim about the authors' notation (F3). One sentence weakens a fair statement about their proof (F4).

## Per-section table

Line numbers: out-lsc.md first, then lsc.md.

| out-lsc.md | Source | Verdict |
|---|---|---|
| Opening, 1–23 | lsc 152–243 (N1)–(N5); nrm-check §1, §5 (18)–(21), verdict; CA-I 477–481, 924–933, 157039–157041, 159153–159160; CA-II 140916–140926; SA 23405–23415, 23515–23527 | PASS. See explicit verdict 1. |
| §1 text, 25–41 | lsc 13–25, 130–144; lsc-value §§1, 3, 5 | FIX F1 (line 40). Lines 32–39 match lsc-value §3. Line 34: SA 23504–23539 holds the Haar calculation and (OH6); lsc-value cites 23481–23539. Both are correct. |
| Lemma 43–145 | lsc 27–128 | PASS. Line 43 "§2" is the correct new section number. Line 61 is new. It matches CA-II 2875–2878: the correlation theorem's flow line holds for 0≤i<j≤K, and that K is the note's K_J. Line 100 "Wilson probability measures" is narrower than lsc's "bare measures"; both are true. Line 105 is new and true: (21) and (22) bound each exponent. Line 121 matches CA-II 63098–63118 word for word. Line 133: (24) defines C_UV and C_face; 𝔯=2 is lsc 493. Line 135 matches CA-II 63104–63109. |
| §2 Retained inputs, 147–199 | lsc 27, 150, 168, 175, 209, 211, 223, 233, 490–507, 664; lsc2-gate verdict | PASS. Every range was read. Item 1: CA-I 2533–2542 is clause (0); CA-II 2875–2884 and 2958–2966 are the flow and torus-independence. Item 2: CA-II 2791–2812 lists the admitted inputs; 2810–2812 calls the window-data proof outstanding; 2921–2935 and 2937–2959 are clauses (iii) and (iv). Item 3: CA-I 157030–157078 holds (h1)–(h11); the paraphrase of (h1)–(h3), (h7)–(h11) is accurate. Item 4: CA-I 159288–159309 and 159511–159520. Item 6: CA-II 59645–59680, items 1–9, paraphrased correctly; item 8 is "the floor for the unsourced integral". The list equals the inputs of the lsc2-gate verdict. |
| §3 (N1)–(N6), 201–262 | lsc 152–201 | PASS. Line 221 says "your vacuum theorem's proof"; lsc says "the relevant part". C_𝔯 = D_0/(L⁴−1) equals the account's C_𝔯 = c_G^♯ + K_*(E_0+1)/(L^d−1) (CA-I 159314). |
| §3 one-step paragraph, 245–253 | NEW in lsc. Counterpart: nrm-check (19). | PASS, with proof check below. |
| §3 (9)–(11), 264–292 | lsc 203–231 | PASS. Line 292 "Your proof" refers to `4.31:lem-window-characteristic`. |
| §3 upper majorant, 294–303 | lsc 233–242 | FIX F2 (line 301). Line 294: the nine hypotheses are in §2, item 6, as stated. Line 303: CA-II 59801–59806 says "Balaban proves the upper member … by bounding the moduli"; the attribution is fair. |
| §3 (12)–(13a), shift remark, 305–367 | lsc 244–306 | FIX F3 (line 316). The rest is identical to lsc. |
| §4, 369–440 | lsc 308–379 | PASS. "This reproduces your proof at II:62887–62983", "Part (a): added offset argument" and "Part (b): your printed identification argument" agree with lsc-value §3. |
| §5, 442–544 | lsc 381–481 | PASS. Lines 444–446 mark the common radius as added and drop the reserve hypotheses of 8.8; this is lsc 140. |
| §6.1, 546–649 | lsc 485–539; CA-II 63964–64258 | FIX F4 (line 550), FIX F5 (line 605). Lines 572–628 are new detail. They match CA-II 63974–63977 (definition of 𝓔''), 64000–64041 (holomorphy, conjugation, value at zero), 64095–64145 (real part, locality, simple transitivity) and 64207–64236 (face terms, Σ|I_c|=n, q≤n). |
| §6.2–6.4, 651–733 | lsc 541–623 | PASS except F3 (line 688). The headings "Your printed part (c)", "Your printed parts (d) and (e)" and "Added completion" agree with lsc-value §§3, 5. Line 688 replaces "the first-passage bound from P1" by CA-I 2533–2537; the bound is CA-I 2535. |
| §6.5, 735–770 | lsc 625–660; lsc2-gate (3) | PASS. Line 767 adds "This passage also needs C_low separately uniform; (21) supplies that bound." This is lsc2-gate (3), checked. |
| §7 scope, 772–801 | lsc 662–700; lsc-uses-check §3, result; lsc-value §2 | PASS. See explicit verdict 2. Line 792: N=2L^{m_1+b} gives N⁴=L^{4b}(2L^{m_1})⁴. |
| §7 check record, 803–819 | lsc 702–724; lsc-gate record in lsc 704–706; lsc2-gate | FIX F6 (804, 808, 810), FIX F7 (816–817). The facts are right. |
| Issue text, 1–17 | out-lsc.md | FIX F8 (paragraph 4), FIX F9 (`@LINK@`), FIX F7 (provenance). The defect paragraph, the scope sentence and "Not covered" match the note. All four account links point to the right file and lines. |

**Internal names.** No gate, lane, FINISH, frozen, lead, registry, row or internal file path occurs in either text. "LSC", "NRM", "P1", "SR1", "T0" and "(I1)–(I3)" of lsc.md are all removed. Residues: "round 1", "round-2", "round-1" and the commit `5129d8d4e` (F6). The issue's `@LINK@` is a placeholder (F9).

**Novelty and credit.** No novelty word occurs. "Added" and "additions" mark the parts, as lsc-value asks. One sentence says "It is not a second discovery here" (F1); it refers to our internal history, not the authors' work. No sentence credits the authors for their own work. The text says "your proof", "your convention", "your printed proofs".

## Proof check of the one-step paragraph (out-lsc 245–253)

For the never-large label, Ω_j = Λ_j = T. So (N2) gives E^bare_1[∅] = −E^{(0)}(T,T) = −v_0. By (N3), −v_0 = (9/2)(L⁴−1)V_1 log x_0 − r_0 ≥ [(9/2)(L⁴−1) log x_0 − D_0]V_1. This exceeds C_𝔯V_1 exactly when log x_0 > (D_0+C_𝔯)/[(9/2)(L⁴−1)]. Applied to the bare energy, (h4)(a) (CA-I 157041) gives E^bare_1 = −𝔩_1 + 𝔯_1 ≤ C_𝔯V_1, since 𝔩_1 ≥ 0 by (h3). C_𝔯 and D_0 are fixed before g_0 (CA-I 157041 "depends only on L, N and 𝔭"; CA-I 159312–159316), and x_0 = g_0^{-2} is unbounded on the admitted range 0<g_0≤g_-(g). So the substitution fails at k=1 for all small g_0. The step uses (N3), that is, the vacuum theorem's one-step inputs, and the note says so ("under the stated one-step inputs"). This is nrm-check (19). Correct.

## Explicit verdict 1: the normalization defect

**Real as stated.** I read every line cited for it.

- CA-I 477–481: Definition 1.1, ρ_0 = exp[−g_0^{-2}A(U)], "the bare density". No constant.
- CA-I 924–933: Definition 1.5, ρ_k = (RT)^k ρ_0, "where ρ_0 is the bare density of Definition 1.1". Notation 4.20 (CA-I 60940–60958) repeats this. Its E_k collects only the subtracted unit-configuration values (CA-I 61023–61029).
- CA-I 157039–157041: (h4) "The vacuum-energy theorem applies"; (a) "−E_k[𝒮_∅] = 𝔩_k − 𝔯_k", 𝔩_k ≥ 0, |𝔯_k| ≤ C_𝔯N_k. Here E_k[𝒮_∅] is the constant of the term τ_∅ of ρ_k (CA-I 157011–157018).
- CA-I 159153–159160: the vacuum theorem's E := Σ_{j<K}E^{(j)}(T,T) and E_k[𝒮] := E − Σ_{j<k}E^{(j)}(Ω_{j+1},Λ_{j+1}). Its hypothesis (h1) (CA-I 159298–159300) asks for this energy constant. Its part (a) (CA-I 159321–159327) gives 𝔈_k = Σ_{j=k}^{K−1}E^{(j)}(T,T).
- CA-II 140916–140926: Z̃_m = e^{−E_m−𝓔_m}Z_m with Z_m bare (140880–140886). It calls exp[−x_0A−E_m] "the density ρ_0 of Definition 1.5" (140922–140923). This second sentence conflicts literally with CA-I 929.
- SA 23405–23415 and 23515–23527: Z̃ = e^{−E−𝓔}Z, and the floor (OH6) is for e^{−E}Z(0).

The bare recursion starts with constant zero. (h4)(a) imports a conclusion about an energy that starts with E. So the bare identity is −E^bare_k = E_vac + 𝔩_k − 𝔯_k, as (N5) and the issue say. The one-step paragraph shows that the literal substitution fails at k=1 for small g_0. The note does not overstate the defect. It does not say that the normalized lower member or the account's conclusions fail. It says that the repair uses the account's own convention, and that the lower-bound argument stays valid there.

Optional precision, not a fix. The issue could also cite CA-II 140922–140923: the account itself calls the normalized density "the density ρ_0 of Definition 1.5", while CA-I 929 points to the bare formula. This shows the conflict inside the text without any computation.

## Explicit verdict 2: the scope of the claimed completion

**PASS. The scope is restricted to what lsc.md and its checks support.**

- Note 41, 787–789: "the Chapter 6 uses listed in §6.5 and the original torus floor of clause (iii-b)". These are the four consumers lsc2-gate checked (CA-II 63531, 63907–63920, 64272, 68364) and the finite-torus completion (29) of lsc §6.4. The issue says the same ("the checked Chapter 6 consumers and clause (iii-b)'s original floor").
- Note 791–796 and issue "Not covered": no replacement of every later use; cross-torus comparisons keep a vacuum-density difference (CA-II 141688–141725); no unit-lattice bound. This matches lsc-uses-check U6, U7, U9 and lsc-value §2.
- None of the lsc-uses-check additions (Lemma M, face-constant bound, Case B transfer repair) appears. lsc-value §2 says they are not part of the checked proof.
- Note 798–801 and issue: the representation, vacuum-energy and sourced upper hypotheses, Balaban's real-background input and the outstanding window-data statement stay as assumptions. No stability theorem, main-theorem result, factorial growth, clustering or rotation result is claimed. The issue's list of assumptions is shorter than the note's (F8).
- Note 781–785: uniformity is in m_1 at fixed m_J(g); b is not constant across bare couplings; part (d) gives no partition-function floor. This matches lsc-value §2.

## Explicit verdict 3: the account's printed proofs against the additions

**PASS, with two attribution fixes (F2, F4).**

- Note 32–39 and the issue name the printed parts: (b) CA-II 63369–63526, (c) 63568–63689, (d) 63691–63798, (e) 63800–63833, the floor calculation (CA-II 109918–109975, SA 23504–23539) and the Chapter 4 vacuum remainder. They name the additions: the offset proof for (a), the common-window constants, the normalization reconciliation, and the completion under the original floor. This is the list in lsc-value §3.
- Section headings carry the marking: §4 "Part (a): added offset argument" and "Part (b): your printed identification argument"; §5 "Your floor calculation and the added common-window constants"; §6.2, §6.3 "Your printed …"; §6.4 "Added completion …".
- Note 40, 243, 515 say that the normalization reconciliation comes from the separate Codex check, as lsc-value §3 requires ("must not be counted again").
- F2: line 301 credits "Balaban's sourced bounds". The sourced versions are retained statements of the account (CA-II 59656–59658, 59741–59745), not Balaban's.
- F4: line 550 drops lsc's sentence that the account's proof has no circle. As written, the reader may think the note repairs a circle in their proof.

## FIX items with replacement text

**F1 (line 40).** Replace "The normalization reconciliation comes from a separate Codex normalization check. It is not a second discovery here." by:

> The normalization reconciliation is taken from a separate Codex check of the normalization.

**F2 (line 301).** Replace "2. Balaban’s sourced bounds and the retained complex-weight estimate make the Wilson contribution nonpositive." by:

> 2. The retained sourced versions of Balaban's CMP 119 bounds (2.43)–(2.48) and clause (c) of your complex-weight lemma bound the Wilson part by \(-(1-\theta_W)A\le0\).

**F3 (line 316; line 688).** Line 316 says that the letter \(B_\sharp\) of I:157049 is "distinct from the first-passage constant \(B^\sharp\)". The account uses one symbol \(B_\sharp\): it is the clause-(0) slope (I:641–667), and the same symbol appears in I:157049 and in the window bound \(\log(g^{-2}+B_\sharp)\) of 4.33(i-b)(3). The note's \(B^\sharp\) is that slope. Replace the second sentence of line 316 by:

> The letter \(B_\sharp\) in (12) is the constant of I:157049. Your text writes the clause-(0) slope with the same symbol (I:641–667); this note writes that slope as \(B^\sharp\) in the first-passage formulas. No step needs the two to differ.

At line 688, replace "For part (e), your clause (0), I:2533–2537, gives" by "For part (e), your clause (0), I:2533–2537 (where \(B^\sharp\) is written \(B_\sharp\)), gives".

**F4 (lines 550–551).** Replace "There is an apparent circle if part (c) cites the *uniformity conclusion* of the per-ball theorem. Keep its proof in the following order. First retain \(t=E_+^\sharp+C_{\rm low}\) as a numerical parameter throughout the proof of 6.4. Only its final paragraph invokes the uniform last-scale conclusion." by:

> There is an apparent circle if part (c) cites the *uniformity conclusion* of the per-ball theorem. Your proof has no circle. It keeps \(t=E_+^\sharp+C_{\rm low}\) as a numerical parameter throughout the proof of 6.4. Only its final paragraph invokes the uniform last-scale conclusion.

**F5 (lines 605–606).** η is the note's L^{-K'} from §5, not the spacing ε that the account's proof uses at II:64119. Replace "For a bulk domain in \(\sigma c\), its relevant plaquettes lie within \(2\eta\) of that cell. Other copied balls lie at least \(R+2\) from its faces, and \(\eta\le1\)." by:

> For a bulk domain in \(\sigma c\), its relevant plaquettes lie within \(2\varepsilon\) of that cell, where \(\varepsilon\le1\) is the lattice spacing used in your proof at II:64117–64120. Other copied balls lie at least \(R+2\) from its faces, so at distance at least \(R+2-2\varepsilon\ge R\) from those plaquettes.

**F6 (lines 804, 808, 810).** "Round" and the commit `5129d8d4e` are internal. The commit is not linked and the reader cannot use it. Replace lines 804–813 by:

> A fresh Claude session checked the first version line by line. It rejected the identification with the bare mass.
> It accepted the offset, lattice matching, local count and subsequence arguments.
> It also accepted the per-ball deductions conditional on a valid common exponent.
> A separate Codex check identified the missing vacuum term and the repair in your existing convention.
> That check also corrected the first checker's stronger claim that no normalization could work.
>
> A fresh Claude session then checked the repaired changes line by line, keeping the accepted parts of the first version.
> Its report says: “First failing step: none.”
> It checked the normalized floor, the upper bound in the same convention, the separate constants,
> and the four consumer cancellations. It explicitly retained the common-energy identification as an assumption.
> This acceptance is conditional on the inputs in §2.

**F7 (lines 816–817; issue paragraph 6).** Apply only after F1–F9. Replace "Codex wrote this outward version against the checked working proof and read the cited source ranges. This outward wording has not received a separate independent model check." by:

> Codex wrote this outward version against the checked working proof and read the cited source ranges. Claude (Opus 5.5) checked this version line by line against the working proof and the cited account lines; its fixes are applied.

In the issue, replace "Codex wrote this outward version; it has no separate independent check." by "Codex wrote this outward version. Claude (Opus 5.5) checked it line by line against the working proof; its fixes are applied."

**F8 (issue paragraph 4, last sentence).** The note (798–799) also keeps the vacuum-energy hypotheses. The sourced majorant inputs are the account's sourced statements, not Balaban's. Replace "Balaban's real-background, representation and majorant inputs remain explicit assumptions." by:

> Balaban's real-background input, your representation and vacuum-energy hypotheses, and the eight sourced upper-bound inputs of your torus-bound proof remain explicit assumptions.

**F9 (issue paragraph 2).** "[This note](@LINK@)" is a placeholder. Replace `@LINK@` by a plain link to `library/out-lsc.md` at a pushed commit, after F1–F7 are applied.

## First failing step

First failing step: none. No proof step is false or missing. F3 corrects a false remark about the authors' notation; it is not a proof step.

## Overall verdict

**FIX.** The note is faithful to lsc.md, its round-2 check and the normalization check in every statement, hypothesis, constant and step. The defect is real as stated. The scope is restricted correctly. The parts are marked correctly, except for two attributions. Apply F1–F9 before posting. The material ones are F3 (a false claim about the authors' notation), F4 (fairness to their proof), F2 and F8 (attribution of the sourced inputs). F1, F5, F6, F7 and F9 are names, notation and provenance.

Checked line by line by Claude (Opus 5.5).
