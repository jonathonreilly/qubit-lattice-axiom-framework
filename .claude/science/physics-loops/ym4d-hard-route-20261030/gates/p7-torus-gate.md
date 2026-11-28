# P7 torus-independence port: line-by-line check

First failing step: L1076–1077 (activities item 3: the prepared/stage factors from [Z''_i∩Y_b]_i are said to differ from one only in Y_b^♯). Local and removable; no conclusion of the theorem changes.

Object checked: `library/port/p7-torus.md` (1329 lines), a port of A14, `4.38:thm-torus-independence`, CA-I:58187–58411, with its proof route CA-I:58413–60808.
Source: `scratchpad/sa/ca_I.tex`, read in bounded excerpts only. CA-II and CA-III were searched only for the CMP 109 (5.10) supplier.
Method: one honest reading, section by section. The port was read against each source passage it cites. This is not a hostile reading.

## 1. Statement (port L20–254)

- I extracted the port's `latex` block and ran `diff` against CA-I:58187–58411. They are **byte-identical** (225 lines each).
- Standing. CA-I:58413–58414 says the proof is "given in the remainder of this section". The heading is unqualified. "Proved implication with named hypotheses" is correct.
- The final sentence of the statement gives (H_{j+1})(a), (b) and (c⁺) only. Clause (d) is not given. The port's Result table (L1281) and F16 (L1223–1226) say the same.

## 2. Inputs table (L257–303)

- Each of the theorem's assumptions (1)–(7) and (H_j) appears as a named row: H1–H7, H6a–c, Hnum, Hwalk, Hsum, Hextract, Hmin, Hnorm, Hfamily, Hlevel. I spot-checked the cited line ranges (58193, 58196, 58201, 58210, 58219–58272, 58622–58637, 58878, 58985, 59000–59005, 59101–59108, 59196–59203, 60756–60765). Each one points at the passage the table names.
- Credited standings. I checked the closing check-log line of P1, P3, P4, P5 and ui, and the referee line of lrb, mu, oc and pda. Each matches the standing that the table credits. The older "not yet checked" sentences in those notes are superseded by their logs, as L291–292 says.
- **The CMP 109 (5.10) supplier (row Hsum, L277).** The source cites "the lemma on pointed polarisation sums" at CA-I:58985–58987, by description only. I searched CA-I, CA-II and CA-III for a lemma or label of that name and found none. (The near names `9.5:lem-pointed-sums` and `5.2:lem-pointed-irrelevance` are different statements.) Its true status is therefore: an unlocated internal citation, whose content is Balaban's printed CMP 109 (5.10). The port keeps it as a named, unproved input and does not claim to replace it. That is correct. **Repair (wording):** the row should say "cited by description; no statement located in CA-I–III; content = CMP 109 (5.10) as printed", not "the pointed-polarisation-sums lemma" as if it were locatable. Also note that the port's own decay, (P7.14) and L795–799, has rate δ′/2 = ⅛min{δ₀,κ/M}. This is weaker than the rate ½min{δ₀,κ/M} that CA-I:4130 gives for (5.10). So the retained input really is needed for "satisfies (5.10)".
- Hwalk: equality of the CMP 99b Thm 3.10/3.12 walk terms on two tori is the second hypothesis of `prf-polarisation-limit` (CA-I:58740–58746). The port maps it to P7-H2. The source theorem must supply it from its assumptions (2)–(3) in the same way, so the port adds no new gap here.

## 3. Geometry, traces, profiles (L305–512)

- Sites: S_j, S_j^♭ and s_j/2 ≥ L¹⁰MŘ_{j−1} agree with CA-I:57038–57090. Arithmetic checked.
- Non-wrapping, collar ≤ s_j/16, injectivity, isometry and deck translations agree with CA-I:57291–57371 (b),(c),(e),(g).
- Tree lengths: the folding map F agrees with `lem-tree-lengths`, CA-I:57552–57650. Correct.
- **F1** (L360): wrapping bound when d_j is an infimum. Correct; the limit is taken by compactness. The source's (f) assumes a shortest tree, so this is a genuine small fill.
- (P7.2)–(P7.4) agree with `lem-round-up-touch` (a)–(e). The parent argument for (P7.4) checked.
- Strip: m_♯ = ⌊(Ř−1)/2⌋, (s1)–(s4), and 106a_j < s_j/4 agree with CA-I:56877–56930 and 57291 (h).
- Profile (P7.5) is CA-I:56764–56774 verbatim. 3a_i/4 ≥ L^{−(j−i)} because Ř_i ≥ L. Checked.
- **F2** (L471): the case split is right (Ř odd ≥5 gives n ≤ (Ř−1)/4 ≤ (Ř−3)/2; Ř = 3 gives n = 0). But it is **not a fill**. CA-I:58010–58032 already contains this exact argument, including the Ř = 3 case. Relabel F2 as "restated", not "filled".
- (P7.6) telescoping: signs checked against `lem-profile-telescopes`.
- Growth gluing restates `lem-growth-factorise` (r1)–(r3). The separation is ≥ c_K > ϖ. Correct.

## 4. Proof of (i) (L514–642), against CA-I:58416–58730

- Route: Ψ_X from localisation and pointing, the vertex formula (P7.7), restricted walks K^{W′} (P7.8), ingredients (α)–(δ), φ_i ≡ 1 in the whole-lattice setting, and translation by MZ⁴ via MŘ_i | L^{j−i} for i ≤ k₁. This is the source's route. The operator list matches CA-I:58640–58730, items 1–3.
- P7.7: the inclusion–exclusion identity checked.
- **F3** (cluster cancellation of log Ξ(𝕋)): correct. Clusters supported away from the excluded set appear identically in both logarithms. The truncation and tail argument is sound under the absolute convergence given by Hnorm and Hlevel(d).
- **F4** (infinite-volume subtractions): correct. Bilinearity gives four terms, and all complements are kept. This agrees with CA-I:58601–58637 ("Nothing is dropped").
- **F5** (equality on the full domain): the termwise match plus the ε-tail argument is correct. The analytic extension is left in H6b, as in the source.
- Translation step: MŘ_i ≤ L^{j−i} is put into Hnum (the k₁ clock inequality plus monotonicity of L^iŘ_i, CA-I:58560–58568). This is a fair naming. The divisibility conclusion checked.

## 5. Proof of (ii)(a) (L644–800), against CA-I:58732–58988

- **F6**: an invariant linear functional on ⊕ sl_N(ℂ) under the diagonal Ad action is zero, copy by copy. Differentiating the infinitesimal gauge identity gives D²F(0)[w,(dλ,0)] = 0 (this is the first identity of CMP 109 (4.15)). The chain-rule term multiplies DF(0) = 0. All correct. It fills the source's one-line assertion.
- (P7.12) and the finite-range current bound: correct.
- **F7**: Cauchy limit of h_s from the uniform absolute tail. Correct. It needs the two-tori equality (see §2, Hwalk).
- **F8**: bidisc radii (1−ε)a/(2U), (1−ε)a/(2V). Image norm < (1−ε)a. Cauchy gives 4E₀UV/((1−ε)²a²). Let ε↓0. This reproduces the source constant 4E(a)^{−2}C_h². Correct.
- Distance inequality and δ′ = ¼min{δ₀,κ/M}: arithmetic checked (2Mδ′d ≤ κd/2). (P7.14) matches (b).
- (P7.15) wrapping bound and **F9** (changing index sets): correct; this is the source's dominated convergence.
- Euclidean clause on totals at regular minimisers: the same three ingredients as CA-I:58915–58958 (closed expression, covariance lemma with its hypotheses, orbit uniqueness via CMP 102b Thm 1). One small gap: the port says only "earlier bounds (2.29),(2.32)". The source supplies them from (H_j)(b) and the merging criterion (CA-I:58935–58936). That is covered by "its hypotheses" in the H3 row, so this is not a gap. The 𝔄 part uses f^𝔄 ∈ 𝔉_{j−1}, and the ℜ part follows by subtraction. Both as in the source.
- (P7.16) two-point sum and the shell summability: correct. The final inequality e^{−δ′(|x−z|+|y−z|)} ≤ e^{−δ′|x−y|/2}e^{−δ′|x−z|/2} checked.
- (5.10): kept as a named input. See §2 for its true status.

## 6. Proof of (ii)(b) (L802–853), against CA-I:58990–59086

- **C1 is right, and it corrects an error in the source text.** At CA-I:59018–59019 the source writes "Clause (d) of (H_j) supplies the translation invariance". (H_j)(d), CA-I:58241–58267, states convergence, analyticity, reality, G^c invariance and the polydisc bound. It states no translation or Euclidean covariance. The invariance actually used is part (d) of `prf-polarisation-limit`. That part is hypothesis (2) of this same lemma, and the source's own next paragraph relies on it ("available for Π_∞ by the previous paragraph"). So the error is a wrong clause reference. It is harmless to the mathematics because the correct supplier is already among the lemma's hypotheses. The port's repair adds no premise.
- The reduction to one coefficient is Hextract (hypothesis (3) of the lemma). The port's inputs to it match: reflections and permutations, transversality (F6), (3.63) as (P7.16), and finite second moments from (P7.14).
- **F10**: reality, additivity β_j = β_j^𝔄 + β_j^ℜ, and dependence only on the prefix (g_0,…,g_{j−1}) via β_i = x_{i−1} − x_i and Ř_i = Ř_i(prefix). All correct. Then x_j is common to all sites, and g_j, Ř_j, ε_j, δ_j, k₁(j), S_j are common given x_j > 0. This is as stated.
- Bookkeeping and profile independence: the port's version agrees with the source.

## 7. (iii): profile members, interior terms, inherited domains (L855–959), against CA-I:59088–59318

- (P7.17) and the supp h_z ⊂ W remark agree with Step 1.
- (P7.19), the T-label chain, agrees with Step 4: one of the two layers of (Ω_j^c)^{∼2} ⊂ Λ_j^c, then Ω_j ⊂ ((Z′_{j−1})^{∼5})^c, then nesting.
- **F11**: for X ⊂ Λ_j^T at an R-label, (P7.19) together with "healing enlarges Λ_i" (source fact (B)) gives (P7.18). Correct.
- **C3 is right, as a repair of an unjustified step.** Step 5 (CA-I:59279–59301) writes Λ_j(ℓ) = Λ_j^T ∪ ⋃X_a with X_a whole healed islands. It then takes a cell C of [X] and uses "C ⊂ Λ_j(ℓ)". That needs Λ_j(ℓ) to be a union of level-j cells. The source's own `lem-range-empty-trace` (CA-I:59617–59642) and `lem-coupling-profile`(b) allow Λ_j(ℓ)^c = Z_j ∪ ⋃Y_b with the Y_b, and the prepared Z″_i, unions of M-cubes that are not cell-unions. Under that generality, Step 5 is unproved. (I cannot tell from CA-I alone whether it is false.) The port's route does not need it. X ⊂ Λ_j^T uses F11. Any X that meets newly admitted cubes meets Z, and Balaban's completion (CMP 122b p.377, in H6a; the source applies it in Step 2 and at CA-I:59446–59453) replaces the **whole** member by the whole-lattice member. The source's later uses of the chain (CA-I:59421, 60540–60549) occur only in the X ⊂ Λ_j^T branch, or are made unnecessary by completion. The port is correct to state that it does not assert the general chain (c) at R-labels.
- **F12**: T-produced B and T terms come before R′ activities. There is no circularity, in agreement with the step order CA-I:60740–60770.

## 8. (iii): catalogue, range, activities (L961–1143), against CA-I:59320–60101

- Catalogue (c1)–(c5) agrees with (eq-label-remainder-c). "Do not touch" = "share no point". The seed count 4+1+1+2+1+1 = 10 agrees with CA-I:59500–59512.
- **F13**: the trace sees every relevant whole component, because the strip reach is m_♯M < a_j and K₀ is maximal. This is the source's argument at CA-I:59569–59580, stated more explicitly. The reading of "strictly contained" as Y_b ⊋ K₀ is right. Calling it "filled" overstates a little, but nothing is wrong.
- (P7.21) range = empty trace, with the cube-wise convention and "index distance 2, not 3": agrees with `lem-range-empty-trace`.
- **F14**: agrees with the (c)⇔(d) nesting at CA-I:59745–59765.
- Activity ingredients 1–7 agree with CA-I:59899–60011. (P7.4) gives reading set [Y]_j⁺¹ ⊂ X⁺¹ for every ingredient.
- **First failing step, L1076–1077.** "Its extra prepared/stage factors from [Z″_i∩Y_b]_i differ from one only in Y_b^♯." This copies the source's CA-I:59953, which uses [Z″_i∩Y_b]_i ⊂ Y_b. But that is a round-up of a union of M-cubes, and Y_b is only an M-cube union. That inclusion is exactly the kind the port's own C2 (L1112–1113, "the same parent argument applies to stage sets inside Y_b") declines to assume. `lem-coupling-profile`(f) covers sets S′ ⊂ X_a, not round-ups that may leave Y_b. So the sentence is unproved inside the port and inconsistent with C2. **It is not used for any conclusion.** Trace locality follows from `lem-coupling-profile`(e) and (P7.4) alone: the factor at x ∈ Y reads only cells within a_i/4 of x, and those lie in [Y]_i⁺¹ ⊂ [Y]_j⁺¹ ⊂ X⁺¹. The empty-trace step uses (P7.22) instead. **Repair:** replace the sentence with that radius statement, and drop the Y_b^♯ claim (or name it as part of H6a's prepared-rounding input).
- **C2 is right, and it corrects an error in the source text.** CA-I:60035–60037 says the cells of [Λ_i(ℓ)^c]_i lie in Λ_j(ℓ)^c. This holds when Λ_j(ℓ)^c is a union of level-j cells (true at T-labels). After R, Λ_j(ℓ)^c = Z_j ∪ ⋃Y_b is only an M-cube union, so the inclusion is unjustified. CA-I:60041–60042 has the same flaw for [Z″_i∩Y_b]_i ⊂ Y_b. The replacement (P7.22), [Λ_i^c]_i ⊂ [Λ_j^c]_j, is always valid by the parent argument. The conclusion survives: a level-i cell inside X⁺¹ forces its level-j parent into X⁺¹, and no cell of [Λ_j^c]_j lies there. Hence the non-island factors are ≡ 1 on X.
- (P7.23) and the covariance for t ∈ MŘ_jZ⁴: correct. The collar 2a_j + m_♯M < 3a_j lifts on S_j.

## 9. Boundary objects and the next hypothesis (L1145–1229), against CA-I:60103–60234 and 60662–60808

- The table of four objects agrees with `prf-label-boundary`: B and T^{(j−1)} with W = X, B′ = R′ off 𝒳_j and zero on it, T′_j with W = X^♯, and (X_a^♯)⁺¹ ⊂ X⁺¹ inside a polymer.
- **F15**: reaches do not accumulate because every older reading set is [X″]_i⁺¹ ⊂ [W]_j⁺¹, by (P7.4) applied once. Correct. It matches the source's "six places" list at CA-I:60499–60560.
- (P7.24): a same-label regrouping only. That is fine.
- **F16**: next (a) comes from (ii)(b) plus x_j ≥ γ⁻². Next (b) comes from the completed step with E = 0. Next (c⁺) comes from (i), (ii)(a), (iii) plus Hfamily. The (P7.25) deduction agrees with `cor-volume-families` (CA-I:60685–60716): clauses other than volume consistency come from the two propagation lemmas; volume consistency comes from the proof of (i) plus the layer-bookkeeping premise. The final order display agrees with `rem-step-order`. **Clause (d) of (H_{j+1}) is explicitly not produced.** Correct, as the theorem's last sentence requires.
- Small omission: `prf-label-boundary` hypothesis (3) also lists "the bound on the large-field part of the coupling increment β_j at level j" (that is, theorem assumption (5), P7-H5). F16 does not say where H5 enters. H5 is kept in the inputs table, so nothing is lost. A one-line pointer would make the propagation complete as written.

## 10. Result block (L1268–1329)

- The fill and correction summaries match the body, with the F2/F13 labelling caveats above. The named-hypothesis list is complete.

## Findings

1. Statement is byte-identical to CA-I:58187–58411; standing (proved implication, named hypotheses) correct.
2. First failing step L1076–1077: the claim that the prepared/stage factors from [Z″_i∩Y_b]_i differ from one only in Y_b^♯ inherits the unproved round-up inclusion of CA-I:59953 and contradicts the port's own C2. It is not used; replace it with the radius statement (lem-coupling-profile (e) plus (P7.4)).
3. C1 is right: CA-I:59018–59019 cites (H_j)(d) for translation invariance, but (H_j)(d) has no covariance clause. The supplier is `prf-polarisation-limit`(d), already hypothesis (2) of that lemma. This is a reference error in their text.
4. C2 is right: CA-I:60035–60037 (and 60041–60042) put round-ups to level-i cells inside the unrounded Λ_j(ℓ)^c (resp. Y_b). That fails to be justified once Λ_j(ℓ)^c is only an M-cube union after R. The replacement [Λ_i^c]_i ⊂ [Λ_j^c]_j is valid and keeps the conclusion. This is an error in their text.
5. C3 is right as a repair: Step 5 (CA-I:59279–59301) needs Λ_j(ℓ) to be a cell-union, which the source's own range lemma does not grant. Routing through the completion clause (already a source input) proves everything the theorem uses.
6. The CMP 109 (5.10) supplier ("lemma on pointed polarisation sums", CA-I:58985–58987) has no locatable statement in CA-I–III. The port correctly keeps it as an unproved named input, but the Hsum row should state that status. The port's own decay rate (⅛min{δ₀,κ/M}) is weaker than the printed (5.10) rate.
7. F2 is the source's own argument (CA-I:58010–58032), not a fill. F13 is largely the source's argument too. These are labelling issues only.
8. Fills F1, F3–F12 and F14–F16 are correct.
9. F16 should point to where H5 (prf-label-boundary hypothesis (3)) enters. H5 is retained.
10. The final sentence gives only (H_{j+1})(a), (b), (c⁺). Clause (d) is explicitly not produced.

## Verdict

**Faithful with repairs.** The repairs are: the L1076–1077 sentence (finding 2), the Hsum status wording (finding 6), the F2/F13 labels (finding 7), and the H5 pointer (finding 9). None changes the route or any conclusion.

Checked line by line by Claude (fresh session).
