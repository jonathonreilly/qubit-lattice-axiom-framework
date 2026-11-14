# out-gw-check: faithfulness of library/out-gw.md and library/out-gw-issue.md

Provenance: Claude Opus 5.5 (claude-opus-5-5). One reading by one model. Not an audit; grants no status. No computation. Read-only use of sources; this file is the only write.

**Checked texts.** `library/out-gw.md` (1195 lines) and `library/out-gw-issue.md` (19 lines). Codex prepared both.

**Sources.**
- `library/walks-gw.md` (1154 lines, SHA-256 `f96a56f1…6528e737a`). It is byte-equal to the linked version at `ba4304ff6`.
- `gates/walks-gw-check.md`: two repairs (§5 tree, §7 complex Wilson step) and one wording fix (§7 box).
- `library/b98p5.md` §§1–2.5 (SHA-256 `baa2b490…5ad132d1ec`, equal at `ba4304ff6`) and `gates/b98p5-port-check.md`.
- `library/out-pi.md` (the posted Theorem PI note), `library/layer-pkg.md` §§1.1–1.2 and 4.4, `library/flat-port.md` §§4.1 and 11 (SHA-256 `32937141…26b920cc`, equal at `ba4304ff6`), `gates/flat-port-gate.md`, `library/a3-balaban.md` §5, `library/b102.md` H6.
- The account at `31a47c543775`: CA-I SHA-256 `4cb5cb5e…10e6e93`, CA-III `7e36523b…7a352d`, outline `YM4_sketch_500.tex` `d7f77d4d…4d537d4b6f`. These equal the hashes in walks-gw.md.

Account ranges read for this check: CA-I 13144, 13170–13200, 13540–13722, 13806–13850, 13981–14010, 14132–14200, 14377–14425, 15262–15318, 15350–15412, 166588–166601; CA-III 111515–111546; outline 10240–10256. No Balaban page image was read. The note itself says that Balaban's pages were not checked for it (line 62).

## Result

The mathematics of out-gw.md §§1–8, the theorem, the constant order and the test are those of walks-gw.md. Both repairs and the wording fix of walks-gw-check.md are present. No step is false. Nine items need a fix. Most are about sources and names. Two concern proof text: the shell count (P4) lost its proof (F6), and the test section adds an existence claim without proof (F8).

## Per-section table

Line numbers: out-gw.md first, then walks-gw.md.

| out-gw.md | Source | Verdict |
|---|---|---|
| Opening, 1–7 | walks 20–34; CA-I 166595–166596 | FIX F1 (outline file not named). The CA-I quotation and the labels are right. |
| Scope, 9–26 | walks 36–105; out-pi §2.3, 326–329; CA-I 15266–15310 | PASS. (S1-loc), (S2), (S2+) match out-pi 111–141. The tag rule and "CMP 116, (1.6), after (1.7)" match CA-I 15276–15304. The identity decomposition is marked as a choice. |
| Input 1, PI, 30 | out-pi 7, 1237 | PASS |
| Input 2, flat, 32 | walks §2 (flat-port §§4.1, 8, 9.2, 11, 12) | FIX F2 (the proof of this input is not named; PI does not contain all of it) |
| Input 3, averaging, 34–52 | walks 780–789; b98p5 (3), (4), (11), §2.4 | FIX F3 (verdict 2 below). The displayed estimates match b98p5 (3) and §2.4 at d = 4. |
| Frame bound, 54–58 | walks 771–782; out-pi Lemma 5.2 | PASS (verdict 1 below) |
| Wilson, current, bibliography, 60–62 | walks 799–833; b102 H6; CA-I 13811–13846; CA-III 111519–111544 | PASS. The bibliography quotes CA-III exactly. |
| Limits, provenance, 64–66 | walks 93–105, 1062–1075 | FIX F4 ("U01–U34" is an internal code); FIX F5 (provenance incomplete) |
| Objects and norms, 68–148 | layer-pkg (1.1)–(1.5); CA-I 13540–13722, 14132–14200, 13981–14010 | PASS. Operators, c^(1), c^(2), j_J, k_J, m_J, (N) and the labels match the account. Writing Ad(W_b) for the account's R_b is the gauge-transform meaning of R_b. CMP 99b (3.116)–(3.138) and CMP 102b (129), (131) match CA-I 13544, 13638, 13688, 13756–13784. |
| Theorem, 150–219 | walks 36–105 | PASS. "(N)" replaces layer-pkg (1.5); "every domain used in your account" replaces the U-codes. |
| §1, 223–262 | walks 109–148 | PASS |
| §2, 264–403 | walks 150–293 | FIX F6 ((P4) without proof) |
| §3, 405–506 | walks 295–397 | PASS. CMP 99b (3.10) agrees with out-pi 730. |
| §4, 508–600 | walks 399–491 | FIX F7 (C_K and C_com do not match out-pi's names). CMP 99b (3.87)–(3.108) agrees with out-pi 760. |
| §5, 602–737 | walks 493–627; walks-gw-check §5 repair | PASS. The repair is present (686–727). The new tree paragraph (625–629) restates out-pi 1260–1275 (the K10 geometry) correctly; 16L(L+1)M_t+8L²+12L ≤ 24L²M_t holds for L ≥ 3, M_t ≥ 4L. CA-I 15357 and 15368–15410 say what the note says. |
| §6, 739–879 | walks 629–767 | PASS. The label `4.5:eq-free-current-operators-1` is at CA-I 13826, inside 13811–13846. CMP 99b (3.42)–(3.49), (3.116)–(3.120) are cited there (CA-I 13570–13592, 13688, 13838–13846). The note keeps the walks-gw point that the printed Hölder bounds are not used as word estimates (60). |
| §7, 881–1087 | walks 769–962; walks-gw-check §7 repair and wording fix; b102 H6 | FIX F3 (line 895 attribution). The complex-background repair is present (941–954). The wording fix is present (883–885). The inlined plaquette calculation (909–939) matches b102 H6 637–718; "(H6.1), (H6.2)" become "the cubic identity and the displayed difference identity", correctly. |
| §8, 1089–1138 | walks 964–1013 | PASS |
| Constant order, 1140–1167 | walks 1015–1042 | PASS except row 5 (F7). Row 9 sets a_0^* = a_1^* = a_* with C_S(L²+1)a_* ≤ e_L. This is one valid way to meet PI item 7. |
| Test, 1169–1194 | walks 1044–1066; layer-pkg (S5), (4.11); CA-I 15311–15314, 14377–14425 | FIX F8 (new existence sentence); FIX F9 ("(4.11)" is an internal number). The equation for z is layer-pkg (S5). At j = 0 it is CA-I 15311–15314, as stated. |
| Issue text | the note | FIX F3, F4, F5, F9 (issue versions given below). The scope, tag and bound paragraphs match the note. |

Internal names and credit. No gate, lane, FINISH, frozen, lead, round, registry or row name occurs. No file path occurs other than the two plain links (out-pi.md at `94df5579a`, walks-gw.md at `ba4304ff6`; both commits are on `origin/claude/ym4d-hard-route`). Residues: "U01–U34" (F4) and "(4.11)" (F9). No novelty word occurs. No sentence credits the addressees for their own work.

## Explicit verdict 1: "On this PI class, (S1-loc) together with the twist bounds supplies that frame after reducing the radii."

**PASS. It is proved in walks-gw.md, not a new claim.**

- walks-gw.md 771–782: the double-block carrier of a positive-height row fits in the (S1-loc) box N_τ of a tile of height j−1 or j whose cutoff support holds the base point. PI's gauge estimate gives ℓ_j‖B‖_{∞,E_c} ≤ C_{N,L}(a_0+a_1). The radii are reduced to a_* ≤ ρ/(16C_{N,L}), with ρ the radius of b98p5.md (11). Constant table row 9 (walks 1032) records the same choice.
- walks-gw-check.md §7, "Averaging": checked "Correct", with the box wording fix, which the note uses (out-gw 54, 883–885).
- I rechecked the geometry against out-pi. supp h_τ has half-width M_tℓ_τ, and every read that meets it lies within (M_t+2L)ℓ_τ ≤ 3M_tℓ_τ (out-pi 826, 1137). That is inside N_τ (half-width 7M_tℓ_τ) and inside C_τ (half-width at least 4M_tℓ_τ), where the model scale equals the actual scale. A row of level j ≥ 1 reads only bonds inside Ω_0 (out-pi 108), so (S1-loc) and (S2) apply on E_c. The proof of PI Lemma 5.2 is pointwise: B = (iη)^{-1}log(e^{iη𝔞^u}e^{iηA}), so ℓ(b)|B| ≤ C_S(L²a_0+a_1) on each bond of E_c. Each such bond has ℓ(b) ≥ s_c/L, so s_c‖B‖ ≤ L·C_S(L²a_0+a_1), up to the √N norm change. The (11) hypothesis then holds for small a_0, a_1. Smaller ceilings are allowed by PI item 7.
- "Twist bounds" means (S2) and (S2+). (S2+) is not needed on E_c, but naming it does no harm.

Optional precision, not a fix. At out-gw 54, "PI Lemma 5.2 … gives" may read "the proof of PI Lemma 5.2, applied on E_c ⊂ C_τ ∩ N_τ where the model and actual scales agree, gives". walks-gw.md has the shorter form, so the note is faithful as written.

## Explicit verdict 2: the source of the supplied-frame averaging estimates

**FIX. The note does not present this input accurately.**

- What the note says (34, 895; issue, inputs paragraph): the estimates are Balaban's CMP 98, Proposition 5, (156)–(157), "with its analytic derivative estimates", used as an implication.
- What (156)–(157) are: first-derivative bounds at a real background. (156) has the leading coefficient 1+2C'_1α_0 (b98p5.md 58–69, from the printed p. 42 as read in the port check).
- What the note uses: the bounds at a complex moving reference W, joint holomorphy in (B, A), second and third derivatives, the difference R''(A)−R''(0), and the physical transposes. This is the analytic extension. Balaban states it without proof: CMP 98 §E, p. 43, "The formulations are obvious". The account cites it as printed in Remark `4.5:rem-averaging-analyticity`, CA-I 13175–13196, and in its list at CA-I 166598–166599. The account lemmas that need it assume it explicitly (CA-I 13683–13686, 13982–13983).
- Where the proof is: walks-gw.md 780–789 uses b98p5.md §§2.1–2.4 (comb map) and §2.5 (symmetrised and plain averages). These prove b98p5 (3) and (4), and the third derivative (§2.4, 335–336), as an implication from (11) at every row, with constants (2) that depend only on N and L. Codex (gpt-6-astra) wrote them (b98p5.md 3). Claude checked them line by line (gates/b98p5-port-check.md: first failing step none; repairs R1, R2 applied, b98p5.md 447).
- The note's estimates match b98p5 at d = 4 (s_c^{1-d} = s_c^{-3}). Its constant C is larger than the leading coefficient of (156). The port check notes this, and no use in walks-gw needs a coefficient near one.

So the note credits a printed proposition for an extension that is printed without proof, and it hides the working proof that the argument actually uses. The replacement text is F3 below.

## FIX items with replacement text

**F1 (line 7).** After the first sentence, insert: "The outline means `YM4_sketch_500.tex` at the same commit."

**F2 (input 2, line 32).** Replace the last two sentences ("This is the flat method … summed remainder.") by:

> These estimates are proved in the [working note on the flat propagators](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ba4304ff6/.claude/science/physics-loops/ym4d-hard-route-20261030/library/flat-port.md): §4.1 for (P7), §§8 and 9.2 for the inverse, §11 for the absolute word bounds, and §12 for the torus room \(t_FM_F\). Codex (GPT-6) wrote it, and Claude (Opus 5.5) checked it line by line. Appendix A of the PI note prints its energy part. The free Poisson estimate (P7) and the absolute word bounds are not in the PI note. The argument rebuilds the flat method of Balaban, CMP 95, Proposition 1.1 and (1.89)–(1.90), and CMP 96, (2.95)–(2.141), Propositions 2.5–2.6. The input includes absolute individual-word bounds, not just a bound on the summed remainder.

Reason: out-pi.md 1288 says "We do not need flat pointwise or Hölder estimates". The note uses flat-port §4.1 (walks 240, 273) and §11 (walks 152–155). These are not in PI.

**F3 (input 3, line 34; §7, line 895; issue text).** At line 34, replace "Use the literal straightened averaging map of Balaban, CMP 98, Proposition 5, (156)–(157), with its analytic derivative estimates. We use the following implication." by:

> Use the literal straightened averaging map of Balaban, CMP 98, pp. 23–24, (42)–(43), as in PI. His Proposition 5, (156)–(157), bounds its first derivatives at real backgrounds. We need the analytic form at complex backgrounds, with second and third derivatives and transposes. Balaban states that extension without proof (CMP 98 §E, p. 43). Your Remark `4.5:rem-averaging-analyticity`, CA-I 13175–13196, cites it as printed. We use a written proof of it as an implication from a frame bound: the [working note on the averaging derivatives](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/ba4304ff6/.claude/science/physics-loops/ym4d-hard-route-20261030/library/b98p5.md), §§2.1–2.5. Codex (gpt-6-astra) wrote it. Claude (Opus 5.5) checked it line by line, and its two repairs are applied. It rebuilds Balaban's map and his real-background method, and moves the reference without a factor that grows with depth. Its constants depend only on N and L. Its first-derivative constant is larger than the leading coefficient \(1+2C'_1\alpha_0\) of (156); no step here needs a coefficient near one. Its §3, on the frame bound for your full class, is not used. It proves the following implication.

At line 58, replace "The averaging estimates themselves remain the stated input implication." by "The averaging estimates themselves remain the input implication of item 3, proved in the linked working note."

At line 895, replace "That input, from Balaban, CMP 98, Proposition 5, (156)–(157), gives" by "That input (item 3: the written proof of the analytic form of Balaban's CMP 98 Proposition 5) gives".

In the issue, replace "Theorem PI, the stated absolute flat estimates, and the supplied-frame averaging estimates from Balaban's CMP 98, Proposition 5, (156)–(157). The averaging estimates hold as an implication from their frame bound." by:

> Theorem PI; the absolute flat estimates, from a written reconstruction of Balaban's flat method; and the supplied-frame averaging estimates. The last are the analytic form of Balaban's CMP 98 Proposition 5, (156)–(157), which he states without proof (your CA-I 13175–13196). The note links a written proof of that form as an implication from a frame bound.

The next sentence of the issue ("On this PI class, …") stays (verdict 1).

**F4 (line 64; issue, "Not covered").** "U01–U34" are labels of our working package, not of your account (no "U01" occurs in CA-I, CA-II or CA-III). Note line 64: replace "The U01–U34 uses in the working note were not checked use by use." by "The individual uses of these bounds in your account were not checked one by one." Issue: replace "The U01–U34 uses were not checked use by use." by "The individual uses in your account were not checked one by one."

**F5 (line 66; issue provenance).** Note line 66: replace "Codex (gpt-6-astra) wrote the proof. Claude (Opus 5.5) checked it line by line; its repairs are applied. Codex prepared this outward note from that text." by:

> Codex (gpt-6-astra) wrote the proof. Claude (Opus 5.5) checked it line by line; its repairs are applied. The flat input was written by Codex (GPT-6) and the averaging input by Codex (gpt-6-astra); Claude checked each line by line. Codex prepared this outward note from the proof, and Claude checked the note line by line against it.

Issue: after "Codex prepared the outward note." add "Claude checked the note line by line against the proof." Add these sentences only after F1–F9 are applied.

**F6 (§2, lines 300–303).** walks-gw.md 186–192 proves (P4) by a pointer to a hand proof in a working note (a3-balaban.md §5, (5.1)–(5.3)). The note dropped the pointer but kept "Counting endpoints … gives (P4)". So the reader has no proof of (P4). Replace from "We give the required shell count" to "Counting endpoints separately on each permitted grid gives" by:

> Here is the shell count in PI's lattice-contour metric. It does the work of Balaban's scale summation, CMP 96, (2.59)–(2.61), which your account uses at CA-I 13420–13427. Let the gap be \(\rho\ge1\) in local units, and fix \(y\) of level \(i\). A path of cost at most \(t\) from \(y\) that reaches level \(h>i\) crosses every complete collar of levels \(i+1,\ldots,h-1\). Each crossing has Euclidean length at least \(\rho\ell_q\) at scale at most \(\ell_q\), so it costs at least \(\rho\). The crossings are disjoint. Hence every endpoint \(z\) has \(|j_z-i|\le1+t/\rho\), and the largest scale on the path is at most \(L^{1+t/\rho}m_y\). The lifted displacement is at most \(tL^{1+t/\rho}m_y\). At a fixed endpoint level, a cube of this radius holds at most \((3+2tL^{2+2t/\rho})^4\le(3+2t)^4L^{8+8t/\rho}\) grid points. There are at most \(3+2t/\rho\le5(1+t)\) levels, and \((m_z/m_y)^b\le L^{|b|(1+t/\rho)}\). Together these give

Arithmetic: 5(1+t)·(3+2t)^4 L^{8+8t/ρ}·L^{|b|(1+t/ρ)} = 5L^{8+|b|}(1+t)(3+2t)^4 exp((8+|b|)(log L)t/ρ), which is (P4). The count is a3-balaban.md 105–124. The flat-port gate rechecked it in the flat case, and walks-gw-check §2 matched (P4)–(P5) to it.

**F7 (§4, line 561; constant table row 5).** In out-pi, C_com is the flat commutator constant of the flat inverse lemma, and C_K = 3C_com is a derived constant (out-pi 232–233, 936). The note uses C_com for its own constant in (P11), and enlarges "C_K". Line 561: replace "Enlarge PI's \(B_F,c_h,C_K,C_C\) to cover these constants before applying its eight choices." by:

> Enlarge PI's \(B_F,c_h,C_C\) and PI's flat commutator constant (also written \(C_{\rm com}\) in PI) to cover \(B_Z,c_Z,C_Z\) and the constant \(C_{\rm com}\) of (P11), before applying PI's eight choices. PI's \(C_K=3C_{\rm com}\) then covers it as well.

Row 5: replace "\(C_K\ge C_{\rm com}\)" by "PI's flat \(C_{\rm com}\ge\) the \(C_{\rm com}\) of (P11) (so \(C_K\ge C_{\rm com}\))". Check: θ_Z = 3B_Zc_Z²C_com/M_t ≤ 3B_Fc_h²C_K/M_t = θ, and PI item 7 gives 2c_ZC_Ze ≤ (PI's C_com)/M_t. These are the two uses in walks-gw-check §4.

**F8 (test, line 1177).** The sentence "Since \(V'_\sigma\) starts at degree two, its local small solution exists by the derivative bound (T2), after reducing the datum ball." is not in walks-gw.md, which only differentiates the defining equations (walks 1046–1050). The claim is true at weight one. Replace it by:

> At weight one the local small solution exists. Fix \(r\le r_{\kappa_1}\) with \(C_{\kappa_1}r\le1/4\), and let \(\|j\|^\Delta_1+|b|_1\le c\,r\) with \(c\) small. Then \(N(H_0b)\le r/2\) by (T2). On the ball \(\|z\|^\Delta_1\le r/2\), every argument has \(N\le r\). Since \(GV'_\sigma(0)=0\), the third line of (T2) makes \(z\mapsto GV'_\sigma(z+H_0b)\) Lipschitz with constant \(C_{\kappa_1}r\le1/4\) on that ball, and of size at most \(r/4\). With \(\|Tj\|^\Delta_1+\|\Gamma H_0b\|^\Delta_1\le r/4\) from (T2), the right side maps the ball into itself and is a contraction. The inner equation for \(X\) is the small branch of §7.

Or delete the sentence: the test needs only the linearization of these equations, as in walks-gw.md.

**F9 (test, line 1183; issue).** "(4.11)" is the equation number of a working note, not of this note or of your account. Line 1183: replace "\tag{4.11}" by "\tag{L}". Line 1192: replace "the necessary bounds in (4.11)" by "the necessary bounds in (L)". Issue: replace "the necessary linearization test (4.11)" by "a necessary linearization test".

## First failing step

First failing step: §2, (P4), out-gw 300–308. The shell count is stated without its proof after the pointer to the working proof was removed (F6). The step is true, and no step is false.

## Overall verdict

**FIX.** The note is faithful to walks-gw.md and its repairs in every mathematical statement, constant and hypothesis. It needs F1–F9 before posting. The material ones are F3 (the averaging input is credited to a printed proposition, but its source is the linked working proof of an extension that is printed without proof), F2 (the flat input's proof is not named), F6 ((P4) needs its proof) and F8 (an unproved existence sentence). F1, F4, F5, F7 and F9 are names and provenance.

Checked line by line by Claude (Opus 5.5).
