# out-m3-check: faithfulness of library/out-m3.md and library/out-m3-issue.md

Provenance: Claude Opus 5.5 (claude-opus-5-5). One reading by one model. Not an audit; grants no status. No computation. Sources were only read; this file is the only write.

**Checked texts.** `library/out-m3.md` (1285 lines) and `library/out-m3-issue.md` (17 lines). Codex prepared both.

**Sources.**
- `library/m3.md` (1148 lines), with repairs R1–R2 of `gates/m3-check.md` present (R1 at m3 467–474, R2 at m3 3 and 429–430).
- `gates/m3-check.md` (all), `gates/layer-part-ref.md` 187–274 (the defect verdict), `library/prior/m3.md` §5 (262–376), `gates/out-gw1-check.md` (form).
- `library/layer-pkg.md` 93–135 ((S5)), 655–800 ((R), (5.3)–(5.9), cutoff repair).
- Posted notes at the linked commits: out-pi.md `94df5579a`, out-gw.md `9a3ad2072` (item 3, 34–36), out-gw1.md `7198d9fa2` (section list, (5) at 155–168). All three exist (`git cat-file -e`) and are on `origin/claude/ym4d-hard-route`.
- The account at `31a47c543775`. Ranges read: CA-I 13175–13196, 13686–13726, 14393–14495, 14722–14770, 15262–15340, 15425–15456, 15669–15702, 72373–72400, 72536–72547, 72700–72730, 72825–72855, 72942–72954, 111386–111462, 111525–111528; label and symbol searches for `eq-response-chart-a`, `\mathfrak{m}_H`, `(e3)`, `(F5)` in CA-I/II/III; CA-II 13888–14105 (label search only); CA-III 111525–111544; outline 10560–10578.

Method: word diff of m3.md against out-m3.md (997 changed lines), then a full reading of every changed or added passage. Unchanged passages carry m3-check's verdicts.

## Result

The mathematics of out-m3 §§1–8 is the mathematics of m3.md as repaired. Every display (1)–(39), the mass table, the theorem, the scale table, the constant order and the consumer table match. R1 is present (out-m3 §3, 568–589) and R2 is present (input 4, 115–121). Most changes are notation (backticks to TeX), "the account's" to "your", and plain descriptions in place of internal file references.

The NEW text is correct. It is: the zero-switch test and gap statement in the opening (from the defect verdict, not from m3); the explicit inputs 6 and 8; the pairing display for j_J, k_J, m_J; two added items in the theorem; the Schwarz estimate for the remainder; and the commutator count for (33). The last two replace m3's citations of `layer-pkg.md`. I checked each one.

No step is false. Eight items need a fix. Three make the gap statement exact (F1–F3). Two make inputs exact (F4, F5). One cites an account line (F6). One stops a claim of more consumers read than were read (F7). One is provenance (F8).

## Per-section table

Line numbers: out-m3.md first, then m3.md.

| out-m3.md | Source | Verdict |
|---|---|---|
| Opening, 3–9 | CA-I 72373, 72392–72399, 72720–72728, 72831–72851, 111394–111399; m3 24–25 | PASS. The label `4.21:lem-exempted-set` is at CA-I 72373. A search of CA-I/II/III finds no definition of \(\mathfrak m_H(\sigma)\) or \(P_1(\sigma)\) at \(\sigma\ne1\). |
| Opening, 11–32 (NEW: zero-switch test) | layer-part-ref 207–237; CA-I 14396–14409, 15279–15313, 72704 | PASS with F1 (notation h, line 21). Proof check below (NEW N1). |
| Opening, 34–40 (NEW: over-wide sentence) | layer-part-ref 239–250; CA-I 14455–14493, 14759–14765, 15448–15451 | FIX F1 (35–36), F2 (37–39). |
| Opening, 42–53 | m3 16–33; check §5.1 | PASS. Definition change stated plainly (verdict 2). |
| Opening, 55–71 | CA-III 111525–111544; CA-I citation counts | PASS. Titles, volumes, years match. CMP 99 (3.116)–(3.120), (3.130)–(3.138) and CMP 109 (3.11), (3.14) are cited in the account. |
| Opening, 73–75 | m3-check header | FIX F8 (provenance). |
| Inputs 1, 82–95 | m3 424–428; out-gw1-check (PI 239, 273) | PASS. |
| Inputs 2, 96–107 | m3 431–435, 442–444; out-gw 34–36 | FIX F4 (104–106). The wider list (P4), §4 is conservative. |
| Inputs 3, 108–114 | m3 436–441; out-gw1 section list | PASS. GW1 §§3.1, 3.3, 7, 8 have the same numbers in gw1.md and out-gw1.md. |
| Inputs 4, 115–121 | m3 429–430 (R2), 4.4 | PASS. R2 present. |
| Inputs 5, 122–129 | m3 445–451, 452–454, 945–949 | PASS. |
| Inputs 6, 130–152 (NEW: explicit) | layer-pkg (R) 662–668, §5.3 739–776; CA-I 111437, 111525–111527 | FIX F5 (143–144). (R), ϑ ≤ 5/4, m_y ≤ Lℓ_□, M ≥ 2L² match layer-pkg. |
| Inputs 7, 153–158 | m3 452–456, 416–418 | PASS. |
| Inputs 8, 159–166 (NEW: K6 hypotheses) | m3 457–460; CA-I 15669–15686 | PASS. U_0=U_k(V_0), regularity, current ceiling, J=J(U_0), polydisc and radius ε̄_4 match the proposition. |
| §1.1, 168–262 | m3 37–123 | PASS. Added definitions of N_y, N_y^Δ, E_p, F_p (186–190) match layer-pkg 57–91 and the uses in (32). |
| §1.2, 264–354 | m3 125–215 | PASS (verbatim up to notation). |
| §2.1, 357–448 | m3 219–304 | PASS. The NEW pairing display (412–418) equals CA-I 13702–13710 term by term (NEW N2). |
| §2.2, 450–525 | m3 306–381 | PASS (verbatim up to notation; "(S5)" became "(29)"). |
| §2.3 Theorem, 527–566 | m3 383–418 | PASS. Added item 3 sentence = (28) (§4.3); added item 6 sentences = §5.2 (923–924, 1017–1033). "the displayed consumer interfaces listed there" is narrower than m3's "each consumer listed in the digest"; correct. |
| §3, 568–589 | m3 467–474 (R1); outline 10562–10578; CA-I 72541–72545, 72945–72952 | PASS (verdict 5). |
| §4.1–4.4, 591–882 | m3 478–770 | PASS (verbatim up to notation). §4.4 transport paragraph (862–870) keeps m3's limit in plain words. |
| §5.1, 884–919 | m3 774–810; layer-pkg 114–119 | PASS. NEW line 896 (S, C_s) matches (S5). |
| §5.2, 921–1033 | m3 812–886; layer-pkg 668–676, 692–776 | FIX F6 (948–949). NEW Schwarz estimate (939–945) and commutator count (979–1011): proof checks below (N3, N4). F5 also applies to 1002–1004. |
| §5.3, 1035–1073 | m3 888–927; CA-I 14444–14448, 15669–15702 | PASS. |
| §6.1–6.2, 1077–1177 | m3 931–1029 | PASS. Added 1111 (2δ_P ≤ λ) is m3-check's observation; correct. |
| §6.3, 1179–1215 | m3 1031–1067; m3-check §6.3 | FIX F5 (row 1193, "repaired cutoff"), F7 (1181–1184). Rows match m3 (verdict 4). |
| §7, 1217–1262 | m3 1069–1114 | PASS ("RJ" became "local-current"). |
| §8, 1264–1285 | m3 1116–1148 | PASS. Scope is not wider than m3; m3's internal closure record is removed. |
| Issue | the note; CA-I as above | FIX F3, F7, F8. Rest matches. |

**Internal names, novelty, credit.** No gate, lane, FINISH, frozen, lead, round, registry, digest, census, M3, LAYER-M, U-code, RJ, EQ, PH or "premise M" occurs in either text. m3's "Theorem M", "M module", "U27" and "frozen census" are gone. The only file paths are the three plain links to posted notes. K6, K10, F5, (e3)^+, site (T)/(L) are your account's own labels (CA-I 15669, 15265, 19684, 115403). (S1-loc), (S2), (S2+) and (P4)–(P15) are labels of the posted PI and GW notes. "New definition" and "new primitives" are technical terms (an off-one definition; union-tagged operators), not novelty claims. No sentence credits the addressees for their own work; m3's credit paragraph (m3 10–14) was removed. The issue still has the placeholder `@LINK@` (issue line 5); it must be the note's link before posting.

## NEW steps: proof checks

**N1. Zero-switch test (out-m3 11–32).** Counterpart: layer-part-ref 207–237, not m3. At site (T), K = ∅ (CA-I 72704). At s ≡ 0 every walk term of every primitive in CA-I 15279–15281 meets a cube, so it is zero. Q, a and I are not in that list, so they carry no factor; the composites formed "by the formulas" (CA-I 15306–15309) give H_0 = H^J = 0, P_0 = I, k = −aℓ^{-1}. In the G̃ form (CA-I 15311–15313) G̃^J = 0 gives the fixed point 𝒜 = 0, so A_G = 𝒜 + H_0B = 0, X_G = D^J(0) = 0, 𝓗^J = 0, Ξ = 0 (V'(0) = 0). The definition at CA-I 14406–14408 then gives 𝔍 = Q^*(q_0 − a)B̃ = −Q^*aB̃, which is −Q^Taℓ^{-1}b in the note's normalisation. Any reduced rider (18) at A' = X = 𝓗 = 0 is F(W,0) = 0. The composite coefficient of X_G in the definition is −Q^*aℓ^{-1} + 0, and Y(0) = ∅, so the locality clause (CA-I 72724–72727) asks for a zero kernel. Correct. Only notation: "h" (line 21) is not yet defined there (F1).

**N2. Pairing display (out-m3 412–418).** CA-I 13704–13709: ⟨λ, j_J(A)⟩ = ⟨A, k_J(λ)⟩ := ⟨c^{(1)}(A,λ), J⟩, ⟨λ_1, m_J(λ_2)⟩ := 2⟨c^{(2)}(λ_1,λ_2), J⟩. The note's display is the same with u for A. Correct.

**N3. Remainder difference (out-m3 939–945).** With N_y(h_i) ≤ 1/40 and D = N_y(h_1 − h_2) > 0, the disc |z| ≤ 1/(40D) keeps h_2 + z(h_1 − h_2) in N_y ≤ 1/40 + 1/40 = 1/20. Input 6 with p ≤ 1 and Θ_0+Θ_1 ≤ 2N_y ≤ 1/10 gives |F| ≤ K_J(1.1)(0.1) = 0.11K_J, so the difference from the centre is ≤ 0.22K_J. If R = 1/(40D) ≥ 1, Schwarz at z = 1 gives ≤ 0.22K_J/R = 8.8K_JD. If R < 1, then 40D > 1 and 0.22K_J < 8.8K_JD. So ≤ 9K_JD. Correct; equal to layer-pkg 668–676 and to the structure of CA-I 111450–111462.

**N4. Commutator count (out-m3 979–1011).** I recomputed. [∇_α, χ] = f_αT_α and [∇_μ^T, χ] = −g_μT_μ^{-1}, so [∇_μ^T∇_α, χ] = ∇_μ^T f_αT_α − g_μT_μ^{-1}∇_α, and ∇_μ^T f_α = f_α∇_μ^T − (∂^-_μ f_α)T_μ^{-1}. This is the display. Both identities ∇_μ^TT_μ = −∇_μ and ∇_μ^TT_ν = T_μ^{-1}∇_ν + ∇_μ^T − ∇_ν hold by expansion. With ∇_μ^T = −T_μ^{-1}∇_μ (norm ϑ on gradients), the α = μ term has gradient coefficient 1 + ϑ and the α = ν term 1 + 2ϑ + ϑ = 1 + 3ϑ; the value terms give 1 + ϑ². Summing over μ ≠ ν gives (2+4ϑ)(d−1)(m s_1 + m² s_2)N_y(B). With s_1 ≤ 5|τ|/(Mℓ_□), s_2 ≤ 42|τ|/(Mℓ_□)², m_y ≤ Lℓ_□, M ≥ 2L², L ≥ 3: 5/(2L) + 42/(4L²) ≤ 5/6 + 7/6 = 2. So c_ζ = 2(2+4ϑ)(d−1). Correct; equal to layer-pkg (5.4)–(5.6) and 769–776.

**N5. Theorem additions (out-m3 545, 555–557).** P_1(0) = m_H(0) = 0 at site (T) is (28), §4.3 (823–828). Joint holomorphy in amplitudes, (0,0,1) and J_0^♯[1] = 0 are proved at 923–924 and 1017–1033. Correct.

## Explicit verdict 1: the gap statement

**FIX (F1, F2, F3). The gap is stated narrowly and correctly. Three sentences are slightly wider or looser than the sources.**

- Assumed package: CA-I 72392–72399 is "Assume the following statements …" in `4.21:lem-exempted-set` (label at 72373). Correct.
- Consumption: CA-I 72720–72728 ("local function of (A',X,𝒴), up to the action of the decoupled operators P_1(s) and 𝔪_H(s)", with the locality clause), 72831–72851 (second entry, source-free component) and 111394–111399 (`4.25:eq-current-partner-1`, the reduced form with P_1(σ), 𝔪_H(σ)). Correct.
- Never defined at σ ≠ 1: a search of CA-I/II/III finds 𝔪_H only at 72724–72851, 94985–94994, 111399–112596 and CA-II 613, 39327–39331; all are uses. Correct.
- Own switched current: CA-I 15306–15313 forms 𝔍(s) by the formulas from the tagged primitives; at site (T), s ≡ 0, it is −Q^Taℓ^{-1}b (N1). The reduced rider gives 0 there, and the composite mass kernel is nonzero while the locality clause asks for zero. Correct in the note (26–30). The issue says "where the reduced rider and locality clause require zero". The locality clause is about the kernel, not the current value (F3).
- Over-wide sentence: CA-I 15448–15451 names three identities and restricts "the first and the last" to s ≡ 1. The middle one, `4.5:eq-response-chart-a`, is stated "At every (U,J) ∈ 𝔖" (14439). Its proof (14455–14493) uses Δ_aP_0G_0 = P_0^T, Δ_aH_0 = Q^*q_0, QP_0 = 0, QH_0B = B̃. Correct. "available only at switches one" (note 36) reads as a claim about every s ≠ 1; the sources show the proof is valid only at one, and that one identity fails at s ≡ 0 (F1).
- No proved step uses it off one: the only label uses are K3 (14732, 14759–14760), the K10 sentence (15450) and K6 (15686–15854, at s ≡ 1). K10 extends K1, K3–K5, K8 by bounds and locality only (15429–15438). K3's term list at 14759–14765 is the defining list of 14406–14408. But your text there introduces it with "The representation identity … expresses 𝔍(B) … through the terms". A reader checking 14759 needs the reason the identity is not used (F2).
- Missing definition, not a false proved step: correct, and it matches layer-part-ref 252–264.
- Nothing is overstated beyond F1–F3. The note does not say K10 is wrong at one, and does not say the account is inconsistent.

## Explicit verdict 2: the off-one definition change

**PASS.** Stated plainly and more than once: "Away from one this is a **new definition of the switched current**. It does not repair or identify (K10)'s current there" (49–50); §5.1 912–919 ("They replace K10's current away from one where that package uses (30). They do not change your earlier definition. … The agreement with your chart is restricted to switches one."); §5.2 1031–1033 ("the two switched definitions differ"); §6.3 1207–1215; §8 1281–1283. The issue: "Away from one it is a new definition, not a repair of K10's current." This matches m3 24–27, 790–801 and prior/m3.md §5.3, fourth bullet. Optional plainer wording for 916, "Your inverse proof cannot do that.": "Your proof of the representation identity uses identities proved only at one, so it does not give that."

## Explicit verdict 3: inputs listed before the proof, with working links

**PASS, with FIX F4 and F5.**

- The "Inputs" section (77–166) precedes §1. Every input of m3 §3 is there: PI (1), GW (2), GW1 (3), geometry with R2 (4), layer solution (5), local current and cutoff (6), readers and profiles (7), identification at one and K6 (8). The block-local gauge map is in 5. The averaging input is in 2.
- Each item states its content; nothing used in §§1–7 is missing. The two estimates that m3 cited from `layer-pkg.md` are now proved in the note (N3, N4), from the hypotheses of input 6.
- Links: out-pi.md at `94df5579a`, out-gw.md at `9a3ad2072`, out-gw1.md at `7198d9fa2`. `git cat-file -e <sha>:.claude/science/physics-loops/ym4d-hard-route-20261030/library/<file>` succeeds for all three, and each commit is on `origin/claude/ym4d-hard-route`. The issue uses the same three links. The account links use `blob/31a47c543775/` with the three account file names and `YM4_sketch_500.tex`, which are the local snapshot names.
- F4: input 2 says the averaging input "follows Balaban's … Proposition 5, (156)–(157), through the written proof linked in GW". (156)–(157) bound first derivatives at real backgrounds. The input used is the analytic form, which Balaban states without proof (CMP 98 §E, p. 43; CA-I 13186–13196). The posted GW note (out-gw 34) says this. This is the same fault as out-gw1-check F5/F8.
- F5: input 6 assumes |ζ''| ≤ 42. Your cutoff at CA-I 111525–111527 asks |ζ'|, |ζ''| ≤ 5. The note does not say that its bump differs from yours, and §6.3 row 1193 says "repaired cutoff" without saying what was repaired. With your plateau and support, ζ'(1/3) = ζ'(2/3) = 0, so |ζ''| ≤ 5 gives |ζ'(x)| ≤ 5 min(x − 1/3, 2/3 − x) and a total drop of at most 5/36 < 1. So no C² function meets your list. I checked this. The constant c_ζ is unchanged with 42 (N4).

## Explicit verdict 4: consumers

**FIX (F7). The table matches m3 §6.3. The note claims more reading than m3-check did.**

- Rows: out-m3 1186–1205 has the same 18 rows as m3 1039–1056, in the same order, with the same ranges and the same matching arguments. Changes are wording only: "its M module" → "the reduced current"; "K_j, c_ζ" → "K_j = 3+18d+9K_J and c_ζ" (= layer-pkg (5.3)); "U27 … frozen census" → "Outside multiple"; "is not a consequence of M" → "remains a separate layer premise". The closing paragraph (1207–1215) matches m3 1058–1067.
- Reading. m3-check §6.3 read the primary text for CA-I 72373–72438, 72714–72728, 72828–72862, 72918–72980, 94978–94996, 111391–111410, 111530–111550, 112608–112626 and CA-II 39314–39336, 39634–39650. That covers ten rows (in part for the rows 72754–72783; 72823–72860, 111391–111486, 111512–111580, 112587–112625, and 14720–14727; 14797–14800). It says it did not reread the other eight rows: 112072–112104; 112181–112194, 112708–112738; 115389–115407, CA-II 610–628, 20794–20828; 21125–21144, 21950–22080, 23160–23169; 23993–24005, 13888–14105, and the older chart rows 19637–19685; 29381–29412.
- The note says "Those passages were read for this note" (1182). The issue says "The displayed consumer interfaces are matched". Both read as if all eighteen interfaces were read in your text. The note's own limit sentence (1182–1183, 1284–1285) is correct.

## Explicit verdict 5: the SA 10578 explanation

**PASS.** out-m3 §3 (568–589) carries every element of R1:
- 10578 keeps the diagonal member −a of system (II) untagged ("carried by no proper set"), and the splitting is built around it (outline 10578, read). Note 571–573.
- That member belongs to the system the fixed point solves; the note keeps (29), its V'_s and every inverted operator's members and tags (575–576). R1: "equation (29), its V'_s and every inverted operator keep their prescribed members and tags."
- The bare mass is a coefficient of the current output, never inverted; the locality clause asks its kernel to vanish off Y(s); an untagged copy fails at site (T); so (6) tags it (576–581). R1, same.
- The account needs only a C¹ function on the cube for the interpolation, and uses holomorphy and the value at one (583–585). CA-I 72541–72545 says "the expansion holds for every continuously differentiable function on [0,1]^{σ_0}"; 72945–72952 uses holomorphy on the polydisc and f(1). This is more exact than R1's "only holomorphy".
- Added: "consistent with the operators-as-data method of Balaban, CMP 116, (1.5), as quoted in your outline 10562". Outline 10562 quotes CMP 116 p. 3, (1.5), and says "no identity enters the argument. The identities are applied earlier, where they hold." Correct, and 570–571 summarise it correctly.
- Dropped from R1: "The outline gives neither (6) nor (17)." Harmless.

## FIX items with replacement text

**F1 (note 21 and 35–36). Notation and the reach of "available only".**
Note 21: replace "The small fixed point gives \(A_G=X_G=h=\Xi=0\)." by:

> The small fixed point gives \(A_G=X_G=\mathcal H^J=\Xi=0\).

Note 35–36: replace "Its proof, [CA-I 14455–14493](…), uses inverse and constraint identities available only at switches one." by:

> Its proof, [CA-I 14455–14493](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14455-L14493), uses inverse and constraint identities that your account proves only at switches one. At zero switches one of them fails: there \(H_0=0\), so \(QH_0B=0\ne\tilde B\).

**F2 (note 37–39). Why the K3 bounds do not use the identity.**
Replace "No proved step of yours uses that identity at \(s\ne1\): the bounds extended by (K10) read the defining term list at [CA-I 14759–14765](…), and (K6) uses the identity at one." by:

> No proved step of yours uses that identity at \(s\ne1\). (K10) extends (K1), (K3)–(K5) and (K8) by bounds and locality only. The (K3) proof bounds the terms listed at [CA-I 14759–14765](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14759-L14765). Your text there introduces the list through the identity, but the list is exactly the defining one at [CA-I 14406–14408](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L14406-L14408). So these bounds hold without it. (K6) uses the identity at one only.

**F3 (issue line 7). What the locality clause requires.**
Replace "gives \(-Q^Ta\ell^{-1}b\) at zero switches at site (T), where the reduced rider and locality clause require zero." by:

> gives \(-Q^Ta\ell^{-1}b\) at zero switches at site (T). There the reduced rider gives zero, and the locality clause requires a zero mass kernel, but the composite mass is \(-Q^Ta\ell^{-1}\).

**F4 (note 104–106). The averaging input.**
Replace "This averaging input follows Balaban's *Averaging operations for lattice gauge theories*, CMP **98** (1985), Proposition 5, (156)–(157), through the written proof linked in GW." by:

> This averaging input is the analytic form of Balaban's *Averaging operations for lattice gauge theories*, CMP **98** (1985), Proposition 5, (156)–(157). Those bounds are for first derivatives at real backgrounds. Balaban states the analytic extension without proof (CMP 98 §E, p. 43), and your Remark `4.5:rem-averaging-analyticity`, [CA-I 13175–13196](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L13175-L13196), cites it as printed. GW, input 3, links a written proof.

**F5 (note 143–144 and row 1193). The cutoff bump.**
Note 143–144: after "\(|\zeta'|\le5\), \(|\zeta''|\le42\)." add:

> Your cutoff at [CA-I 111525–111527](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111525-L111527) asks \(|\zeta''|\le5\). With this plateau and support, \(\zeta'(1/3)=\zeta'(2/3)=0\), so \(|\zeta''|\le5\) allows a total drop of at most \(5/36<1\). We therefore assume the weaker bound \(|\zeta''|\le42\); the existence of such a bump is part of this input. The constant \(c_\zeta\) in (33) does not change.

Row 1193: replace "Equation (33) uses the unchanged lift and repaired cutoff." by "Equation (33) uses the unchanged lift and the cutoff of input 6."

**F6 (note 948–949). Cite the account line.**
Replace "Do not use the printed unsupported replacement of that size by \(N_y(\delta h)\)." by:

> Your proof at [CA-I 111436–111439](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L111436-L111439) writes \(N_y(\delta\mathbb H)\) in this bound. The bound on \(K_W\) applies to \(\delta A'\), so we use \(N_y(\delta A')\). The entries and the constant \(3+18d\) do not change.

**F7 (note 1181–1184; issue "Not covered"). What was read.**
Note: replace "This table matches the displayed interfaces at the cited lines. Those passages were read for this note. We have not reread every downstream consumer proof one by one." by:

> This table matches the displayed interfaces at the cited lines. Claude's check read your text for ten rows: CA-I 72392–72399, 72714–72728, 72823–72860, 72918–72979, 111391–111410, 111530–111550, 112608–112625, 94980–94995, 14720–14727, and CA-II 39312–39335 with 39622–39650. For the other eight rows, the match is to the property each use needs, as stated in the table; your text there was not reread. No downstream consumer proof was reread one by one.

Issue: replace "The displayed consumer interfaces are matched; downstream consumer proofs have not been reread one by one." by:

> The note's consumer table matches 18 interfaces. Ten were read in your text; the other eight are matched to their stated use only. No downstream consumer proof was reread one by one.

**F8 (note 73; issue line 15). Provenance and the link.** Apply after F1–F7.
Note 73: replace by:

> Codex (gpt-6-astra) wrote the proof. Claude (Opus 5.5) checked it line by line, and its repairs are applied. Codex prepared this note from the proof, and Claude checked the note line by line against it.

Issue: after "Claude (Opus 5.5) checked the proof line by line, and its repairs are applied." add "Claude also checked the note line by line against the proof." Replace `@LINK@` (issue line 5) by the note's link at the posting commit. The model name gpt-6-astra is from gates/m3-check.md line 3.

## First failing step

First failing step: none. No proof step fails. Every display, hypothesis and constant matches m3.md as repaired, and the five NEW proof steps (N1–N5) are correct. The first faithfulness fault is note 35–36 (F1).

## Overall verdict

**FIX.** out-m3.md is faithful to m3.md and its repairs R1–R2 in every mathematical statement, hypothesis, constant and step. The gap statement is narrow and correct: an assumed package consumes P_1(σ), m_H(σ) that are never defined at σ ≠ 1; the account's own switched current fails the locality clause at zero switches at site (T); 15450–15451 is too wide; no proved step uses the identity off one. The definition change is plain. The SA 10578 paragraph carries R1. Before posting, apply F1–F8. The material ones are F7 (the note and issue claim more consumer reading than was done) and F5 (the bump differs from your account's cutoff without saying so). F1–F3 sharpen the gap sentences, F4 and F6 are citation precision, F8 is provenance and the link placeholder.

Checked line by line by Claude (Opus 5.5).
