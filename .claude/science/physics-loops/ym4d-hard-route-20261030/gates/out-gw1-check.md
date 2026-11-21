# out-gw1-check: faithfulness of library/out-gw1.md and library/out-gw1-issue.md

Provenance: Claude Opus 5.5 (claude-opus-5-5). One reading by one model. Not an audit; grants no status. No computation. Sources were only read; this file is the only write.

**Checked texts.** `library/out-gw1.md` (1144 lines) and `library/out-gw1-issue.md` (17 lines). Codex prepared both.

**Sources.**
- `library/gw1.md` (1040 lines), with repairs R1–R3 of `gates/gw1-check.md` present (R1 at gw1 100–103, R2 at 819–824, R3 at 1031–1038).
- `library/prior/gw1.md` §§3–6 (target §6 (b)–(d); consumer tables §3).
- Posted notes: `library/out-pi.md` (Theorem PI, §2.2–2.3, items (a)–(e)) and `library/out-gw.md` (scope, inputs, (P4), (P5), (P7), (P11)–(P15)). The local out-gw.md equals the linked version at `9a3ad2072`.
- Linked files exist at the linked commits: out-pi.md at `94df5579a`, out-gw.md at `9a3ad2072`, flat-port.md and b98p5.md at `18d805bed`, b99.md and b99-w.md at `7be3220f3`. All are on `origin/claude/ym4d-hard-route`.
- The account at `31a47c543775`. Ranges read: CA-I 12737–12763, 13144–13198, 13577–13640, 13679–13683, 13715–13801, 13840–13929, 13930–13985, 14508–14514, 15262–15340, 15342–15414 (by search), 112589–112606, 166588–166601; CA-III 111515–111546; outline 10300–10312, 11701, 11705–11716, 32953.

No Balaban page was read. The note says so (out-gw1 25–26).

## Result

The mathematics of out-gw1 §§1–8 is the mathematics of gw1.md, line for line. Every display (1)–(46), every table, the theorem, the switch paragraph, the lift paragraph and the constant order match. R1, R2 and R3 are present. No step is false.

Ten items need a fix. Two change what the note says about the account or about scope: F1 (what (J8) does) and F2 ("no use needs a Laplacian bound"). The others are citation precision, one omitted constant condition in the issue, and provenance.

## Per-section table

Line numbers: out-gw1.md first, then gw1.md.

| out-gw1.md | Source | Verdict |
|---|---|---|
| Opening, 3–12 | CA-I 13944–13955, 13957–13977 | FIX F1 (lines 7–8: (J8) is not "built on q_0"). The (J7) quotation is exact (CA-I 13954–13955). |
| Opening, 14–20 | gw1 113–130, 1010–1024 | FIX F2 (lines 17–18). The rest matches. |
| Opening, 22–30 | gw1 5–18; CA-I 1, SA | PASS. "Pages not read" matches gw1 17–18. Provenance: see F10. |
| §1, 34–50 (NEW, inline (S1-loc), (S2), (S2+)) | out-pi 102–141, 329; out-gw 11–17 | PASS. Checked against PI: the gauge bound L²a_0 with weights m, m², the twist bound a_1, the η-scale bound on the extra read of Ω_0^+, the real gauges still required at a proper outer boundary. |
| §1, 52–66 (NEW, constants, torus floor, odd L) | out-gw 19–24; out-pi 62, 239, 273 | PASS. r̂=(2L+2)M_t and side ≥ max{2r̂+2, t_FM_F}ℓ_k match PI 239 and 273. |
| §1, 68–96 | gw1 34–60; CA-I 13719–13739, 13586–13589 | PASS. (1)–(2) match. The added sentences (Θ_J uses H^J; G_0=Δ_a^{-1}, q_0) match CA-I 13722–13739 and 13586–13589. |
| Theorem, 98–168 | gw1 62–130 | PASS. R1 present (136–141). "c_K ≥ 32" (165) is from gw1-check §7.2 and CA-I 14512. |
| §2 input 1, 175–182 | gw1 136–139; out-pi 273–325; CA-I 13144–13171, 13624–13627, 13974–13977, 15272 | FIX F3 (location of the q_0 assertion). The rest matches. |
| §2 input 2, 183–190 | gw1 140–146 | FIX F4 ((P4) and §4 are used but not listed). |
| §2 input 3, 191–200 | out-gw 32 | PASS. Same sections and same Balaban citations as the posted GW note. |
| §2 input 4, 201–218 | out-gw input 3 (after its F3) and verdict 1; CA-I 13175–13196 | PASS. Accurate: analytic form of Prop. 5, printed without proof (CMP 98 §E, p. 43). |
| §2 remark inputs, 220–227 | gw1 147–156; b99-w 262–285 | PASS. b99-w Lemma 3.3 uses CMP 99b (3.120), (3.126), (3.128), (3.129); B99 B15 uses (3.130), (3.138). The range "(3.128)–(3.138)" is a source range, not a claim per equation. "Not premises of the theorem" is correct. |
| §2 account, 229–237 | gw1 157–171; CA-I 15276–15304, 15381 | PASS. CMP 116 (1.6), (1.7), (1.11) all occur in the account at these places. |
| §2 bibliography, 239–246 | CA-III 111519–111544 | PASS. Titles, volumes and pages match. |
| §2 norms, 248–285 | gw1 173–210 | PASS (verbatim). |
| §3.1, 298–357 | gw1 223–282 | PASS. The added citation CMP 99b (3.87)–(3.108) (310–311) matches the posted GW note's §4 citation. |
| §3.2, 359–414 | gw1 284–338 | FIX F5 (379–380, averaging attribution). Displays (10)–(13) match. |
| §3.3, 416–502 | gw1 340–425 | PASS. Added citation (455–456): the account's J1 proof cites CMP 99b (3.42)–(3.47) and (3.49) (CA-I 13843–13866). |
| §3.4, 504–604 | gw1 427–527 | PASS (verbatim; "the requested first step" became "the insertion bound"). |
| §4, 606–695 | gw1 529–615; CA-I 13876–13897 | PASS. Added lines 608–609 match CA-I 13876–13897 and the outline 11701 route. |
| §5, 697–834 | gw1 617–749 | FIX F6 (699–700, "Balaban gives its form"). The added citation at 793–794 (CMP 96 (2.59)–(2.61), GW (P4)–(P5)) matches out-gw 304–315. |
| §6, 836–916 | gw1 751–824; CA-I 13912–13920, 13755–13758 | PASS. R2 is present as a labelled remark outside the theorem (907–916). It drops "B99 B15 constructs those real operators" but keeps "does not … replace the separate true-current proof"; that is faithful. |
| §7.1, 920–951 | gw1 828–855; CA-I 13957–13977 | PASS. Added lines 922–924 match J8 ("as is done for (3.130)"). |
| §7.2, 953–1020 | gw1 857–920; CA-I 15278–15314, 15381 | PASS. "new" was removed (1008, 1018). |
| §7.3, 1022–1059 | gw1 922–959 | PASS. "M3" was replaced by a plain description (1058–1059). |
| §8, 1061–1109 | gw1 961–1006; CA-I 15409–15412 | PASS. The added sentence 1063–1064 matches CA-I 15412 ("do not involve κ_1"). |
| §9 table, 1111–1126 | gw1 1026–1038 (R3) | PASS (verdict 4). |
| §9 limits, 1128–1144 | gw1 1010–1024; prior §6 (a); outline 10307, 11714–11715 | FIX F2 (1128–1131). The rest PASS. "Termwise lattice covariance" (1142) is wider than gw1's "all-torus covariance of a different assignment". It is a wider non-claim, so it is safe. |
| Issue | the note; CA-I as above | FIX F1, F2, F7, F8, F9, F10 (issue texts below). The identity-convention, scope and Laplacian-exclusion sentences otherwise match the note. |

**Internal names, novelty, credit.** No gate, lane, FINISH, frozen, lead, round, registry, M3, U-code, B99-W, LAYER-THM or GW1 name occurs in either text. The only file paths are the six plain links to notes. "PI" and "GW" are the names of the posted theorems (issues #13, #14). "The existence target" / "the existence proof" is not your account's term: the account calls it Theorem 0 (CA-I 397). F2 uses that name. No novelty word occurs. No sentence credits the addressees for their own work. One phrase, "your (J7) port" (issue, line 5), can read as if the port were theirs (F9).

## Explicit verdict 1: the gap, (J7), (J8), and the claimed supply

**FIX (F1). The (J7) part is accurate. The (J8) part is not. The supply is stated correctly.**

- (J7), CA-I 13944–13955. The proof writes Π^TΘ_JΠA = f′ − D_Uφ′, f′ = Θ_JΠA, φ′ = RG′D^*_Uf′, and ends: "the arguments of (J1)--(J4) apply verbatim to G_1^J, (QG_1^JQ^*)^{-1} and H_1^J" (13954–13955). The note (5–7) and the issue quote this exactly. The statement (J7) itself is at 13783–13784; the §9 table cites it there. Correct.
- (J8), CA-I 13957–13977. It does three things. (i) It builds the walks of G_0, G′, R, P, (Q′G′²Q′^*)^{-1} from Balaban's local propagators at complex configurations (CMP 99b Cor. 3.5, Thms 3.7, 3.9, 3.10). (ii) It replaces each operator in the current series by its walks, as for CMP 99b (3.130). (iii) It takes the expansion of q_0 from Remark `4.5:rem-covariance-inverse-walks`, "stated in [CMP 99b] without proof", and gets q_J and (QG_1^JQ^*)^{-1} by concatenating the walks of the Neumann series of (J3) and its (J7) analogue.
- So "(J8) builds the expansions on q_0" (note 7–8; issue line 5) is wrong for G_1^J, whose words are G_0 walks joined by insertions. It is only partly right for (QG_1^JQ^*)^{-1}: those concatenations start and end with q_0 words, but q_0's own expansion is the unproved remark. The gap the note fills is: (J7)'s "verbatim" sentence is not a written termwise estimate for the extra insertion Π^TΘ_JΠ (prior §6 (d)); and (J8)'s expansions rest on an inverse-walk remark printed without proof. PI supplies that remark on its class (input 1). The replacement text is F1.
- Supply. Theorem items 1–4 match prior §6 (b) and the J2–J4 members that (J7) transfers (gw1-check, question 1). The issue's "What it supplies" paragraph lists exactly these: termwise first-order and differentiated-source bounds with a fixed Hölder gap, coarse density and physical transpose bounds, analytic words, common-footprint restriction, zero-switch separation. It is restricted to the PI class with GW's constants (issue, "Scope and inputs"; note 64–66). Not overstated. The only omission is the condition c_K ≥ 32 on the lift bound (F7). The two identities at one (item 3) are not named in the issue; that is a harmless understatement.

## Explicit verdict 2: inputs listed before the proof

**PASS, with precision fixes F3, F4, F8.**

- §2 (172–227) is before the proof (§3 starts at 287). It lists and links: Theorem PI (issue #13, `94df5579a`), GW (issue #14, `9a3ad2072`), the flat estimates carried by GW (flat-port.md, `18d805bed`), and the supplied-frame averaging input (b98p5.md, `18d805bed`). All links resolve.
- Input 4 states the averaging input accurately: the analytic form of CMP 98 Prop. 5, (156)–(157), for the literal map (42)–(43), printed without proof at CMP 98 §E, p. 43, as the account's Remark at CA-I 13175–13196 records. It states the frame bound and how GW supplies it.
- The identity convention I_f = Σ_τ h_{τ,f}² I_f for Π is stated before the proof (136–141), marked as a choice that the account does not fix, and equal to the account's operator at one. It is used at (14). Correct.
- The B99 true-current results are linked (220–227) and marked as not premises of the theorem. Correct.
- The account's own definitions are listed (229–237) with correct ranges.
- F3: input 1 places the q_0 assertion "after Balaban's CMP 99b Theorem 3.9". The cited lines (13624–13627, 13974–13977) do not say that. The Remark (13144–13171) and the list (166593–166594) place it in "the sentence preceding (3.132)". (CA-I 15272 does say "after Theorem 3.9", but the list at 166595–166596 uses that phrase for a different input.)
- F4: the proof uses GW §4 (reversed words, 322) and GW (P4) (794), not in the list at 184.
- F8: the issue cites the averaging input as "CMP 98 Proposition 5, (156)–(157)" without saying it is the analytic form printed without proof. This repeats the fault of the earlier GW issue (out-gw-check F3).

## Explicit verdict 3: scope and limits

**FIX (F2).**

- Layer map and current: "does not assign the general layer map or switched current" (19), and §9 (1133–1137). PASS.
- B99 identification: only in the labelled remark (907–916), "cited; outside the theorem"; issue: "a cited remark only". PASS.
- Uses not checked one by one: "does not check every use in the existence proof" (20); "There is no full check of the uses in the existence proof" (1139); issue "no full check of the uses". PASS in substance; F2 gives plainer words.
- Laplacian: "No Laplacian bound for G_1^J or G_π^J is supplied" (17–18), "is proved or used" (1128). PASS. But the next sentence, "No use in the existence target needs one" (18, 1129; issue), is a positive claim about every use. The sources do not support it:
  - prior §6 (a) says only that no such theorem "was found on the T0 path", and its verification limit says it is "not a line-by-line independent check" and makes no claim "to have read … every downstream theorem".
  - gw1 §9 (1011–1012) says the port proves "neither a Laplacian estimate for G_1^J nor the general nonlinear layer's stronger graph assertion". The note drops the second half. Your account does ask for a graph norm of the layer datum in places, e.g. ‖ℍ_1−ℍ_2‖^Δ_p at CA-I 112595 (prior §3.2, U16, U19, U21).
  - The sentence also contradicts the note's own limit (20, 1139).
- The outline cite (1130–1131) is correct: outline 10307 excepts the bound on Δ_U G_(1); 11714–11715 do not assert the "covariant Laplacian member excluded in [Theorem 3.12]{B85c}", and B85c is CMP 99b (outline 32953).

## Explicit verdict 4: account-lines table (out-gw1 1117–1126)

**PASS.** Each range was read.

| Row | Range on the page | Result |
|---|---|---|
| 1 | 13759–13774: (J2) 13759–13766, (J3) 13767, (J4) 13768–13774. 13783–13784: statement (J7) | Correct (R3 applied) |
| 2 | 13847–13874: J1 proof from the G_0θ split to "ε is never sent to zero" and the weighted norms. 13944–13955: J7 proof | Correct |
| 3 | 13876–13897: J2 proof (series, ∇^* first iterate, telescoped inverse) | Correct (R3 row added) |
| 4 | 13899–13920: J3 13899–13911, J4 13912–13920. 13954–13955: "apply verbatim to …" | Correct |
| 5 | 13957–13977: J8 proof (13978 is \end{proof}) | Correct |
| 6 | 15278–15314: primitive list, expansion, tag rule with the CMP 116 quote, composites (15306–15308), A_0^J form (15311–15314) | Correct |
| 7 | 15322–15324: K10 item 1 (B_0e^{16κ_1}; composites B_0e^{c_Kκ_1}). 14512: "an integer c_K independent of all parameters" | Correct |
| 8 | 15333–15337: K10 items 3–4 (separation; equality at s≡1) | Correct |

Other cited ranges, also read and correct: CA-I 12739–12761, 13579–13637, 13583–13590, 13681–13977, 13719–13739, 13755–13758, 13175–13196, 15266–15340, 15409–15412; CA-III 111519–111544; outline 10307, 11714–11715. One content fault in a correct range: F3.

## FIX items with replacement text

**F1 (note 7–8; issue line 5). What (J8) does.**
Note: replace "Your (J8) builds their expansions on \(q_0\) ([CA-I 13957–13977](…))." by:

> Your (J8) expands these operators into concatenated walks of Balaban's local propagators, joined by the current insertions ([CA-I 13957–13977](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L13957-L13977)). It takes the walks of \(q_0\) from your `4.5:rem-covariance-inverse-walks`, which is printed without proof, and builds the coarse inverses by concatenation from them.

Issue: replace "(J8), 13957–13977, builds the expansions on \(q_0\)." by:

> (J8), 13957–13977, expands them into concatenated walks, and takes the walks of \(q_0\) from a remark printed without proof.

**F2 (note 17–18 and 1128–1131; issue "Not covered"). The Laplacian sentence.**
Note 17–18: replace "No use in the existence target needs one." by:

> We found no use in your proof of Theorem 0 that needs one, but we did not check the uses one by one.

Note 1128–1131: replace the paragraph by:

> No Laplacian (graph) bound for \(G_1^J\) or \(G_\pi^J\) is proved or used. This note also does not prove the graph norm that your account asks of the general nonlinear layer, for example \(\|\mathbb H_1-\mathbb H_2\|^\Delta_p\) at [CA-I 112595](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L112595). We found no use in your proof of Theorem 0 that needs a Laplacian bound for \(G_1^J\) or \(G_\pi^J\); the uses were not checked one by one. Your outline 10307 and 11714–11715 expressly exclude this member, following Balaban, CMP 99b Theorem 3.12.

Note 20 and 1139 (optional, same meaning, plainer): "does not check every use in the existence proof" → "does not check the uses in your proof of Theorem 0 one by one"; "There is no full check of the uses in the existence proof." → "The individual uses in your proof of Theorem 0 were not checked one by one."

Issue: replace "No Laplacian bound for \(G_1^J\) or \(G_\pi^J\); no use in the existence target needs one." by:

> No Laplacian bound for \(G_1^J\) or \(G_\pi^J\), and no graph norm for the general layer. We found no use in your proof of Theorem 0 that needs the first, but the uses were not checked one by one.

and replace "and no full check of the uses in the existence proof" by "and no check of the individual uses in your proof of Theorem 0".

**F3 (note 181–182). Where the q_0 assertion is printed.**
Replace "Your CA-I 13624–13627 and 13974–13977 cite the inverse-walk assertion after Balaban's CMP 99b Theorem 3.9 as printed without proof." by:

> Your CA-I 13624–13627 and 13974–13977 cite it as printed without proof. Your Remark, CA-I 13164–13171, places it in CMP 99b §3, in the sentence before (3.132), and quotes that sentence.

**F4 (note 184). GW parts used.**
Replace "(P5), (P7), (P11)–(P15), §§5–7, and its constant-order table" by "(P4), (P5), (P7), (P11)–(P15), §§4–7, and its constant-order table". Reason: §3.1 line 322 uses GW §4's reversed-word estimate; §5 line 794 uses (P4).

**F5 (note 379–380). Averaging attribution in §3.2.**
Replace "The one-leg density estimate of GW §7 uses the supplied-frame averaging input, following Balaban, CMP 98 Proposition 5, (156)–(157)." by:

> The one-leg density estimate of GW §7 uses input 4 of §2, the analytic form of Balaban's CMP 98 Proposition 5.

Reason: (156)–(157) are first-derivative bounds at real backgrounds; (11) needs the analytic extension (out-gw-check, verdict 2).

**F6 (note 699–700). "Balaban gives its form".**
Replace "Balaban gives its form in CMP 99b (3.132)." by:

> Your (J3) calls it the analogue of Balaban's CMP 99b (3.132). Balaban states (3.132) for \((QGQ^*)^{-1}\) and his own-current \((QG_1Q^*)^{-1}\) without proof; your CA-I 13164–13171 quotes the sentence.

**F7 (issue, tags paragraph). The condition on c_K.**
Replace "Your composite lift retains both tags and has bound \(Ce^{32\kappa_1}\)." by:

> Your composite lift retains both tags and has bound \(Ce^{32\kappa_1}\). This fits your \(Ce^{c_{\mathbb K}\kappa_1}\) when your parameter-free integer \(c_{\mathbb K}\) (CA-I 14512) is at least 32.

**F8 (issue, inputs paragraph). Averaging input.**
Replace "The latter use Balaban's CMP 95–96 propagator method and CMP 98 Proposition 5, (156)–(157)." by:

> The flat estimates rebuild Balaban's CMP 95–96 propagator method. The averaging estimates are the analytic form of his CMP 98 Proposition 5, (156)–(157), which he states without proof (your CA-I 13175–13196). The note links a written proof of each.

**F9 (issue line 5). Ownership of the port.**
Replace "writes out your (J7) port for" by "writes out your (J7) reduction for".

**F10 (note 28; issue provenance). Provenance.** Add these only after F1–F9 are applied.
Note 28: replace by:

> Codex (gpt-6-astra) wrote the proof. Claude (Opus 5.5) checked it line by line, and its repairs are applied. Codex prepared this note from the proof, and Claude checked the note line by line against it.

Issue: after "Claude (Opus 5.5) checked the proof line by line, and its repairs are applied." add "Claude also checked the note line by line against the proof."
The model name gpt-6-astra is from gates/gw1-check.md line 3.

## First failing step

First failing step: none. No proof step fails, and every display, hypothesis and constant matches gw1.md as repaired. The first faithfulness failure is the opening sentence on (J8), out-gw1 7–8 (F1).

## Overall verdict

**FIX.** The note is faithful to gw1.md and its repairs R1–R3 in every mathematical statement, hypothesis, constant and step. The NEW text (inline PI conditions, constants and torus floor, added Balaban and account citations, the §8 κ_1 sentence) is correct against the posted PI and GW notes and the account. It needs F1–F10 before posting. The material ones are F1 (what (J8) says) and F2 (the positive claim that no use needs a Laplacian bound, which the sources do not support and which drops gw1's layer graph-norm limit). F3–F8 are citation precision and one omitted condition. F9 and F10 are wording and provenance.

Checked line by line by Claude (Opus 5.5).
