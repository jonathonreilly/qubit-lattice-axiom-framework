# AG1 at level k: the weighted live-age tail, uniformly in the volume — pass 1, long draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, written for the lead as pass 1 of the core open lemma of TP1/AG1 (`library/tp1-draft.md` §10.1). Research text. It is not an audit, it grants no status, and no other model has read it. No step rests on a computation. Every argument is a finite sum, a union bound, a conditional expectation of independent uniform variables, a geometric series, a counting argument on cubes, or an application of the chessboard estimate LG1(3); each is meant to be Lean-formalisable.

Credit. The architecture used here is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the large-field histories, lineages, the volume mark, the price of survival and the chessboard for the law of the histories are theirs (SA (2a), Theorem 4.13, Proposition 4.14, Lemma 4.15). Their complete account (CA-I/II/III) supplies the healed old-region bound, the global stability quotient, the age lemma and the precise statement of the open problem (Proposition 8.12). Their three-dimensional manuscript YM3_I supplies the 3D comparison. Tadeusz Balaban's papers (CMP 119 (1988) 243; 122 (1989) 175 and 355) are the source of the large-field regions, the region rules and the healing; Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. Our own `library/tp1-draft.md` (Claude) poses the target and records Attacks A–C; `library/rarity-fresh-x.md` (Codex) records where the constrained comparison (SEP) stopped.

Line references: **SA L** = `scratchpad/sa/ym4.tex` (32,992 lines); **CA-II L** = `scratchpad/sa/ca_II.tex` (145,624 lines); **CA-III L** = `scratchpad/sa/ca_III.tex` (111,583 lines); **Y3 L** = `scratchpad/sa/YM3_I.tex` (89,144 lines); **TP1 L** = `library/tp1-draft.md`. I read every cited range myself in this session, in bounded ranges. Quotations are kept short.

Status words, used inline: **[proved]** = proved here by hand from the stated inputs; **[input: NAME, owner]** = a named statement another submanuscript must supply, stated exactly; **[outstanding]** = AG1's own statement, not proved here; **[false]** = refuted here (not used in the end: Lemma 2.3 is stated as a non-implication).

---

## 0. Summary

**Target.** Lemma AG-k₁ of TP1 L483–487: at a coarse level k, for the unsourced positive history law ν̃,

  Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C (log x_k)^C e^{−c p₀(g_k)},   (0.1)

uniformly in the volume, the cutoff and the position. This is CA's Proposition 8.12 (CA-II L127294–127316), listed under "no complete argument is known" (CA-III L111189–111192).

**What is proved here.**

1. *Diagnosis* (§2). [proved] The global stability quotient used one cell at a time cannot give (0.1) in a large volume (Lemma 2.1); a first moment gives densities, never a factor per level (Lemma 2.2, the arithmetic behind SA L23313). [proved] The healing dichotomy (H) of TP1 L497 does not follow from SA's region rules (Lemma 2.3): a component survives at least one level after its creation whatever the next tests do, so (H) fails on any positive-weight history with a quiet step after a creation. So TP1's Lemma 10.1 cannot be applied as stated, and (SR) is the wrong mechanism.
2. *A weaker rate suffices* (§1.3). [proved] TP1 reads (0.1) only through (log x)^C × (rate) → 0. The variant (0.1*) with rate e^{−ϖ_k}, ϖ_k ≥ c₀(log x_k)², closes TP1 Lemmas 6.5 and 6.6 unchanged (Lemma 1.3).
3. *Attack D — chessboard dilution of the global quotient* (§4). [proved] Theorem D: under exact tile locality (LOC), the designated moment bound (MB), covariance (COV) and LG1(3), the bound (0.1*) holds with ϖ_k = c_a r_k/2, r_k = M⁴Ř_k⁵. The mechanism: the price of survival is a volume charge per cell *per level* (SA's mark), not a fresh event per level; the global cost B(x_k) per site, which kills CA's one-cell argument in large volume, is divided among the tiles by the chessboard estimate, so it costs B(x_k)𝗇⁴(MŘ_k)⁴ per tile, which the charge c_a M⁴Ř_k⁵ beats.
4. *Attack E — the healing rule gives "volumes are paid by events"* (§5). [proved] Lemma E.1 (hull count), Lemma E.2 (the weighted volume recursion (R1) for SA's free evolution bx(Ŷ^{~10}), for L ≥ L₁), Lemma E.3 (the inequality "volumes are paid by events", SA L23267–23274, from (R0)–(R2)), Lemma E.4 ((MB) from the lineage-trace bound (LT) and E.3). This is the correct replacement of (H).
5. *Attack F — locality* (§6). F1 (make every test local in the bare field): **fails**; exact reason in §6.1. F2 (smooth decompositions of unity, decided by the auxiliary uniforms, so that a "window" is an event of an independent uniform variable and not of a field value): [proved] Theorem F gives (0.1*) with ϖ_k = δ𝗇MŘ_k/128 from (SM), (QL), (MB), (COV), LG1(3). F3 (SA's own sharp tests with witness functions): **fails** at a conditional-density bound for a tested fluctuation value under the interacting history law; exact reason in §6.3.

**First outstanding statement** (§7). The two-run stability (QL) of the construction with smooth tests: if two configurations agree on a tile, and their decisions agree at all earlier decision sites in the nested inner regions, then every tested quantity at a level-j decision site in the level-j inner region differs between the two runs by at most C_q θ_τ e^{−δD_j}, and the discrete data (decision sites, live regions, lineages) agree on the next inner region. (QL) is deterministic: no measure enters. It is AG1's own outstanding statement. SA asserts it in sketch form for its sharp tests (SA L23328, "agreement of two runs inside a tile"); CA lists translation covariance of the label histories and the age lemma as stated without complete proof (CA-III L111428, L111431).

**Inputs owned by other submanuscripts** (§3, §8): (LT) = LF1(3) in lineage-trace form with designated healed lineages (⟦LF-mass⟧, open); (SM) = a design choice for LF1's tests; (COV) = translation and reflection covariance of the history construction; (R0)–(R2) = the region rules (LF1(2)), of which (R2) is the chain form of CA's age lemma; LG1(3) [C].

**Line count** of this file: given at the end of §9.

---

## 1. Statement

### 1.1 Objects (SA (2a), as read)

Fix the datum, a compatible torus and the run. Levels are j = 0, 1, …, K. The level-j lattice T^{(j)} has spacing L^j a_K. A *level-j cell* is a cube of side MŘ_j sites of T^{(j)} (SA L17479: "a cell contains (MŘ_j)⁴" sites). Here Ř_j is "the smallest power of L that is not less than (log min_{i≤j} x_i)^r, with r ≥ 2" (SA L17334). Since x_i decreases in i up to first passage, min_{i≤j} x_i = x_j, so Ř_j is non-increasing in j, and Ř_j ≤ LŘ_{j+1} (SA L17334). The weight of a level-j cell is r_j := M⁴Ř_j⁵ (SA L17479); it is non-increasing in j.

A history h of level k carries, for each j ≤ k, the large-field region Z_j = Λ_j^c and the live region 𝒵_j ⊂ Z_j, a union of level-j cells (SA L17325, L17477). Components are maximal connected unions of cells (cells adjacent when their closures meet). At each step a live component either is healed by the operation 𝐑, or has its image contained in a component of the next level (SA L17415–17433, the three fates).

*Lineage regions* (SA L17479). For a component X of Z_k, live at level k or healed at step k, 𝖹_k(X) := X and, going down, 𝖹_j(X) := the union of all components live at level j contained in 𝖹_{j+1}(X). The *lineage* of X consists of these components (j, C) and the creations (j, W) inside the 𝖹_j(X). For a component C live at level k, its *lineage age* is age_k(C) := k − j₀, j₀ the least level with 𝖹_{j₀}(C) ≠ ∅ (SA L23300).

*Survival event* (SA L23267). For a level-n cell 𝔷 and n ≤ k' ≤ k, E^{(n)}_𝔷(k') := {𝔷 ⊂ 𝒵_i for every n ≤ i ≤ k'}. For a level-k cell 𝔠, lv_k(𝔠) := E^{(k)}_𝔠(k).

*The age event of TP1.* 𝔏_k^{≥a}(c) := {some component C live at level k with C ∩ c ≠ ∅ has age_k(C) ≥ a}. TP1 L481 defines the age as "created at level ≤ k − a and never healed since", citing SA L26103–26117; SA's Proposition 4.14 (SA L23300–23313) orders the three ages, label age ≤ lineage age ≤ seed age, and states that the expansions of (7b) need "the age read in the label", which is at most the lineage age (SA L23336, end). So bounding the lineage-age event bounds what TP1's (TP-live) reads. I use the lineage age throughout.

**Lemma 1.1 (anchor)** [proved from the definitions; SA L23336]. If C is live at level k and age_k(C) ≥ a, then there is a level-(k − a) cell 𝔷 ⊂ C such that E^{(k−a)}_𝔷(k) holds.

*Proof.* By definition 𝖹_j(C) ⊂ 𝖹_{j+1}(C) for every j < k (it is a union of sets contained in 𝖹_{j+1}(C)), and 𝖹_k(C) = C. Since j₀ ≤ k − a and 𝖹_{j₀}(C) ≠ ∅, nestedness gives 𝖹_{k−a}(C) ⊇ 𝖹_{j₀}(C) ≠ ∅. 𝖹_{k−a}(C) is a union of components live at level k − a, hence a nonempty union of level-(k − a) cells; let 𝔷 be one of them. For k − a ≤ i ≤ k, 𝔷 ⊂ 𝖹_{k−a}(C) ⊂ 𝖹_i(C), and 𝖹_i(C) is a union of components live at level i, so 𝔷 ⊂ 𝒵_i. Finally 𝔷 ⊂ 𝖹_k(C) = C. ∎

### 1.2 The statements

**(0.1)** is TP1's (10.1) (TP1 L483–485).

**(0.1*)** For a rate ϖ_k ≥ c₀(log x_k)², with C, c₀ independent of the volume, cutoff, position and level:

  Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C e^{−ϖ_k}.

**Theorem AG (our form).** (0.1*) holds at every level k with x_k ≥ X_AG, as an implication from the inputs (K), (COV), (SM), (QL), (MB) and LG1(3) (Theorem F, §6.2); (MB) follows from (LT) and (R0)–(R2) (Lemma E.4, §5). Status: [proved] as that implication; (QL) [outstanding].

### 1.3 The weaker rate suffices for TP1

**Lemma 1.3** [proved]. If (0.1*) holds at k = k₁, then TP1 Lemmas 6.5 and 6.6 hold as stated, and hence TP1(1)–(5) hold with (0.1*) in place of (0.1).

*Proof.* TP1 reads (10.1) only through (6.3) (TP1 L377): 𝔄 ≤ C(MŘ_{k₁})⁴ Σ_a L^{8a} sup_c P(…) ≤ C(log x)^C·(rate). In Lemma 6.5 (TP1 L381) the rate enters through the single requirement (log x)^{2C}·(rate) → 0, and through P(Λ) ≤ 𝔄. In Lemma 6.6 (TP1 L389) it enters through (log x)^C 𝔄^{1/2} → 0. With rate e^{−ϖ_{k₁}}, ϖ_{k₁} ≥ c₀(log x_{k₁})² and x_{k₁} ≥ x/2 (TP1 L381), we have (log x)^{C'} e^{−c₀(log(x/2))²} → 0 as x → ∞ for every fixed C', since (log x)² grows faster than C' log log x. No other line of TP1 reads the rate. ∎

So the target I prove is (0.1*). The rate p₀ of (0.1) is not reached by the arguments below (see Remark 4.6): the chessboard charges per tile, and the charge per tile is polylogarithmic of degree 5r, not of degree 𝔭₀.

---

## 2. What the sources say, and why the known routes stop

### 2.1 Sussman–Alpoge, (2a) and (4d)

- *Region rules* (SA L17317–17334). The step-t tests are a plaquette test χ_t, an approximate fluctuation test χ'_k (a sharp indicator, "𝟏{|…| < 2δ_k}", SA L17317), a third test χ^{(k)}, and collar and rim tests. The regions are Ω_t^c = Q_t'^{~2} ∪ P_t'^{~4} ∪ Ŷ^{~8}, Z^{[0]} = bx((Ω_t^c)^{~2} ∪ R_t'^{~}), then rounds; "If nothing is created, the step reduces to the free evolution Φ_t(Y) = bx(Ŷ^{~10})", and in general Z_t ⊂ Ŷ^{~10} ∪ (𝒲^∧_t)^{~O(1)} up to boxing (SA L17325–17334). Hulls and layers are taken in level-t cells (SA L17317).
- *Locality of the tests* (SA L17336–17344). χ_t and χ'_k "are built from localised backgrounds"; the third test and the collar and rim tests "depend on 𝒜_k", formed with the true averaged background, "local in the new variable 𝒜_k, but not in (V_k, V_t)" (SA L17336). Inside 𝐑, tests use backgrounds localised in the component (SA L17344).
- *Theorem 4.13* (SA L23258–23298): ν̃(lv_k(𝔠)) ≤ Ce^{−cp₀(g_k)} uniformly, by a first moment: (i) healed lineages pay the factor of 𝐑; (ii) "Volumes are paid by events": Σ_{(j,C)} r_j|C|_j ≤ c_G Σ_{(j,C)} r_jŘ_j e(j,C) — "a statement on the geometry of the regions alone" (SA L23267–23274); masses by lineage traces with weights wt(𝔩) (SA L23280–23286); r_jŘ_j ≪ p₀(g_j) (SA L23286); (iii) translation averaging; (iv) prolongation of the run. The end mark "registers only lineages of components still live at the last level" (SA L23292).
- *Proposition 4.14* (SA L23300–23313, proof L23336) and *Lemma 4.15* (SA L23315–23328). SA states that a first moment yields "only a density, and never a factor per level" for one cell (SA L23313), and therefore applies the chessboard to the law of the histories. Lemma 4.15's proof: price of survival with the dial 𝗐 = 0, for "the run stopped at level k", via Markov, ν̃(𝖤_k) ≤ exp[𝖡(x_k)|𝕋^{(k)}| − inf Θ^{(k)}]; Vol_k "charges it once for each level" (SA L23322–23328). Witnesses: a history is "determined by the bare field together with independent auxiliary variables", one uniform per kernel application, attached to a location (SA L23328); locality via "agreement of two runs inside a tile" under two hypotheses, no tested value in a narrow window and no long cluster; the windows are paid "under the conditional law of a tested fluctuation value"; triggers are paid "by the conditional law of the fluctuation field in its box" (SA L23328).
- *Anchors* (SA L23336): the 2⁴ tilings displaced by ±⌊n_□/4⌋ cells, every level-k cell deep in one of them, the pigeonhole step, the geometric mean with Theorem 4.13.

### 2.2 The complete account (CA-II Chapter 8, CA-III Chapter 13)

- *The problem as stated.* Proposition 8.12 (CA-II L127294–127316): Σ_{𝖺>𝔩} L^{8(𝖺+1)} q^{ℰ,=𝖺}_{k₀} ≤ A^ℰ_lv L^{8(𝔩+1)} q^lv_{k₀}, uniform in m, "Proof outstanding". The route paragraph (CA-II L127320–127352) gives two reductions, both ending at unproved one-cell statements.
- *The split.* Proposition 8.12:prop-old-region-moments (CA-II L125400–125520) splits q^{=a} into healed and end slices, assumes the healed old-region bound, and states that the old-age tail for the end slices "is not proved in this book" (its clause (c)).
- *The healed part is local.* Proposition 8.9 (CA-II L113036–113335) bounds the healed slices at every level with no depth floor; healed islands "have at most 100 cells to a side" (CA-II L113210, L113325).
- *The global quotient.* For any set 𝒮 of terminal internal histories, ν̃(𝒮) ≤ exp(𝖡N⁴ − inf_𝒮 Θ), 𝖡 ≤ C_𝖡(1 + log g^{−2}) (CA-II L126262–126357, eqs. 8.12:eq-volume-ranges-4, -7, -b).
- *Case V is proved* as an implication (CA-II L126359–126640): there the terminal torus has polylogarithmically many sites, and one seed's linear reserve pays 𝖡N^{†4}.
- *Case C needs a volume floor* (CA-II L126839–127028): the step (∗) reads 𝖡 at γ_* and needs 9 ln L(s − m_𝕋 + k^† − K) ≥ C_𝖡(1 + log X_*)N_C(m)⁴.
- *Why it is stuck.* CA-II L126035–126110: the age-blind end density 𝔢_{k₀} = 𝔈L^{−4(K'−k₀)} is volume-free, but its age series diverges with K; the global moment caps ages only at a_{N_T} ∝ 𝖡N_T⁴/ϱ, a volume-dependent cap.
- *The list.* CA-III L111189–111199 (list (1): Proposition 8.12, "the exit bound", the half-skin bound, the unbounded-union depth statement, the collar transfer); CA-III L111428–111432 (translation covariance of the label histories; the age lemma; rarity above a depth floor — "stated; proof incomplete").
- CA does not use SA's Lemma 4.15. A grep of `ca_II.tex` for "chessboard" finds hits only at CA-II L60906–61405 (Chapter 6.2, complex cell observables); in CA-III the hits concern the volume transfer of sources (e.g. CA-III L72830–72852).

### 2.3 Three dimensions

Y3 L791–797: "locality and the rarity of early large-field regions control the remaining history", and "the two-state comparison transfers the estimate to arbitrary admissible volumes". In 3D the creation union bound converges because x_j grows geometrically toward finer levels (TP1 Lemma 3.9(b), L214–216). In 4D it diverges (TP1 Lemma 3.9(a)). So 4D needs a price per level of *survival*, which is SA's volume mark.

### 2.4 Three diagnostic facts

**Lemma 2.1 (one cell against a global quotient)** [proved]. Let a law ν̃ satisfy ν̃(𝒮) ≤ exp(β𝒱 − inf_𝒮 Θ) for all events 𝒮, where 𝒱 is the number of sites, and let 𝒮_𝔠 be an event at one cell with inf_{𝒮_𝔠} Θ = μ. The bound gives ν̃(𝒮_𝔠) ≤ e^{β𝒱 − μ}, which is < 1 only if μ > β𝒱.

*Proof.* Substitution. ∎

So for one cell the per-cell cost μ must beat the whole volume. This is CA's depth floor (CA-II L126839–126860): μ grows like 9 ln L·(depth), so the depth must exceed C𝖡N_C⁴.

**Lemma 2.2 (a first moment gives a density only)** [proved]. Let Θ ≥ 0, E_ν̃ e^Θ ≤ e^{β𝒱}, and let E_𝔠 (𝔠 in a set of 𝒩_c cells) satisfy Σ_𝔠 𝟏_{E_𝔠} ≤ Θ/μ. Then 𝒩_c^{−1} Σ_𝔠 ν̃(E_𝔠) ≤ β𝒱/(μ𝒩_c). If μ = μ₀(a + 1) grows linearly in an age a, the bound decays only like 1/a, so Σ_a L^{8a}·(bound) diverges.

*Proof.* Jensen: E Θ ≤ log E e^Θ ≤ β𝒱. Sum the inequality and take expectations. The last sentence is arithmetic. ∎

This is the arithmetic behind SA L23313 and behind CA-II L126035 (the cap a_{N_T} ∝ 𝖡N_T⁴/ϱ). A factor per level for one cell needs an exponential moment *of a quantity extensive in the number of copies of the event*. The chessboard estimate supplies exactly that.

**Lemma 2.3 ((H) of TP1 is not a consequence of SA's rules, and fails on any positive-weight history with a quiet step after a creation)** [proved from SA L23265, L17325]. TP1's (H) (TP1 L497) asserts: if a live component at level i − 1 has a live descendant at level i, then the level-i small-field test fails on some cell of level i within C_H cells of its image. For SA's rules with 𝖭_t ≥ 1:

(a) a component Y live at level i − 1 that contains a creation of step i − 1 has a live successor at level i, *whatever the outcomes of the level-i tests*;

(b) hence (H) holds on such a history only if some level-i test fails within C_H cells of Ŷ, and (H) is false as soon as one history with a creation in Y at step i − 1 and no level-i failure within C_H cells of Ŷ has positive ν̃-weight.

*Proof.* (a) SA L23265: "𝐑 touches a component only if no creation has occurred in it during the last 𝖭_k steps." At step i a creation has occurred in Y during the last 𝖭_i ≥ 1 steps, so 𝐑 does not act on the successor of Y. The successor is nonempty and contains Ŷ: Ω_i^c ⊇ Ŷ^{~8} and Z_i ⊇ Z^{[0]} ⊇ (Ω_i^c)^{~2} (SA L17325), and these inclusions hold for every outcome of the tests. Since 𝐑 does not act, the component of Z_i containing Ŷ is live. (b) is (a) restated. ∎

*On positivity.* The history law is a positive measure (LF1(1)); CA records "every age carries positive ν̃-weight" (CA-II L126085). Whether the particular configuration of (b) has positive weight is a property of the measure that I do not prove; but nothing in the rules forces a failure, so (H) cannot be derived from the healing rule, which is what TP1's Attack B needed (TP1 L519).

*Consequence.* TP1's Lemma 10.1 (product of per-level fresh events) is correct as an implication but its hypothesis (H) does not hold. A lineage can survive without fresh events for a number of levels of the order of log_L(size) + Ř (the free evolution shrinks it; 𝐑 waits 𝖭 steps). The right statement is a *bound on the total survival volume by the events* (Lemma E.3 below), which allows event-free survival but charges it.

---

## 3. The model and the inputs

### 3.1 The kernel representation

**(K)** [input: LF1(1), owner LF1; SA L23328, `ref-73.md` §2]. There is a countable index set 𝒯 of *decision sites* τ, each with a level j(τ) ≤ K, a location (a site of T^{(j(τ))} or the centre of a test cube) and a position in the order of moves of step j(τ). Let ω = (u_τ)_{τ∈𝒯} be i.i.d. uniform on [0,1] with law λ, independent of the bare field U ~ μ_{K,ℓ,β}. The history of level k is a measurable function h = H_k(U, ω), and ν̃ is the image of μ ⊗ λ. Step j reads only the u_τ with j(τ) ≤ j, and within step j it reads them in the order of moves. Write ℱ_j := σ(U, u_τ : j(τ) ≤ j); the history up to level j is ℱ_j-measurable. Each location carries at most N_τ decision sites per level, N_τ a constant of the construction.

### 3.2 Covariance

**(COV)** [input: owner LF1; CA-III L111428 lists "translation covariance of the label histories" as stated with proof incomplete; SA L23298 (iii) asserts translation covariance by level-k cells]. Let θ be a translation by a multiple of the side of a level-k cell, or a reflection in a plane that bisects bonds and lies on the boundary of the level-k cells. Then H_k(θU, θω) = θH_k(U, ω), where θ acts on ω by moving locations.

Why these maps: a reflection in the plane x_μ = c maps the level-j block lattice onto itself iff 2c ∈ L^jℤ (in bare units, blocks centred on L^jℤ⁴, L odd). A level-k cell boundary has c ∈ L^{k'}(ℤ + ½) with k' = k + log_L(MŘ_k) ≥ j, so 2c = L^{k'}(2n + 1) ∈ L^jℤ for every j ≤ k'. So these reflections preserve all block lattices and all cell partitions up to level k (the partitions are nested because Ř is a power of L, SA L17334).

### 3.3 The moment bound with designated cells

**(MB)** [input: owner LF1/UV1; derived in Lemma E.4 from (LT)]. There is C_D, and for every dial c_a ≥ 1 a threshold X₁(c_a), such that for x_k ≥ X₁: for every m ≥ 1, all cells 𝔷₁, …, 𝔷_m of levels n_i ≤ k whose level-j ancestors are pairwise distinct for every j ≤ k, and all k_i ∈ [n_i, k],

  ν̃(∩_{i≤m} E^{(n_i)}_{𝔷_i}(k_i)) ≤ exp( B_k|𝕋^{(k)}| + C_D m − 2c_a r_k Σ_i (k_i − n_i + 1) ),   (3.1)

with |𝕋^{(k)}| the number of sites of T^{(k)} and B_k ≤ C_B(1 + log x_k).

*Which run.* (3.1) is read for the run stopped at level k. Runs over the same bare datum coincide through the last step of the shorter one and give level-k events the same mass (CA-II L126214–126220, "Consistency of runs over one bare datum"; SA L23298: continuation "leaves the law up to level k unchanged"), so this is the law P^{(k)} that TP1 reads (TP1 L481).

*Relation to the sources.* For k_i = k for all i, (3.1) with C_D = 0 is SA's price of survival (SA L23322–23328: the moment bound for the run stopped at level k, Markov, and Vol_k charging each surviving cell once per level), with r_j ≥ r_k for j ≤ k. For k_i < k the lineage of 𝔷_i may heal before k; SA asserts that then "the lineage of that component pays for the cell" (SA L23328). The bound on B_k is CA's degree bound 𝖡(g) ≤ C_𝖡(1 + log g^{−2}) (CA-II L126262–126268, eq. 8.12:eq-volume-ranges-4).

### 3.4 Tiles

Fix 𝗇, a power of L with 𝗇 ≥ 16 (fixed below, (6.10)). A *tiling* of level k is a partition of the torus into cubes of 𝗇⁴ level-k cells whose faces lie in bond-bisecting planes on level-k cell boundaries (SA L23315), translated by a multiple of the side of a level-k cell. A tiling exists when the number of level-k cells per axis, 2L^{m+K−k}/(MŘ_k), is at least 2𝗇; it is then 2𝗇L^p for an integer p ≥ 0, so the number of tiles per axis is even. 𝒩 denotes the number of tiles, V_T := 𝗇⁴(MŘ_k)⁴ the number of sites of T^{(k)} per tile, so |𝕋^{(k)}| = 𝒩V_T. The *core* of a tile is the concentric cube of side (3/4)𝗇 cells; a cell of level ≤ k is *deep* if the level-k cell containing it lies in the core. *Tile data* of a tile β: the bare links of the closed tile and the u_τ with location in β (locations are sites, never on a face, since faces bisect bonds).

The tiles of a tiling are images of one reference tile under the group generated by the reflections in the face planes; write θ_γ for the map taking the reference tile to tile γ.

### 3.5 The chessboard estimate with auxiliary variables

**Lemma 3.1** [proved from LG1(3)]. Let f_γ (γ a tile) be bounded nonnegative measurable functions, f_γ depending only on the tile data of γ. Put ‖f‖_ch := (E_{μ⊗λ} Π_γ θ_γ f)^{1/𝒩} for a function f of the reference tile data. Then

  E_{μ⊗λ} Π_γ f_γ ≤ Π_γ ‖θ_γ^{−1} f_γ‖_ch.

*Proof.* (i) *Integrating the uniforms.* The families ω_γ := (u_τ)_{τ located in γ} are independent for distinct γ and independent of U. By Fubini, E_{μ⊗λ} Π_γ f_γ = E_μ Π_γ f̄_γ(U) with f̄_γ(U) := ∫ f_γ(U, ω_γ) dλ(ω_γ), a bounded nonnegative function of the links of the closed tile γ. Since λ is invariant under the relabelling of locations by θ_γ, (θ_γ f)‾ = θ_γ f̄. The same identity holds for the dissipated products, so ‖f‖_ch = (E_μ Π_γ θ_γ f̄)^{1/𝒩}. (ii) *Positive infima.* Replace f̄_γ by f̄_γ + ε. (iii) *Chessboard.* LG1(3) (assembly L153: "The one-direction and four-direction chessboard estimates hold", status [C]; SA (AM6) at L2898–2905 for one direction) gives E_μ Π_γ (f̄_γ + ε) ≤ Π_γ (E_μ Π_{γ'} θ_{γ'}θ_γ^{−1}(f̄_γ + ε))^{1/𝒩}. (iv) Let ε ↓ 0: both sides are polynomials in ε with nonnegative coefficients, finite at ε = 0 (bounded functions on a finite torus). ∎

**Lemma 3.2 (dilution)** [proved]. Let f be a [0,1]-valued function of the reference tile data, 𝔼 an event, 0 < η ≤ 1, μ ≥ 0, and suppose Π_γ θ_γ f ≤ 𝟏_𝔼 pointwise and ν̃(𝔼) ≤ η^𝒩 exp(B_k|𝕋^{(k)}| + 𝒩(C_D − μ)). Then ‖f‖_ch ≤ η·exp(B_kV_T + C_D − μ).

*Proof.* Take the 𝒩-th root and use |𝕋^{(k)}| = 𝒩V_T. ∎

This is the whole point: the global factor e^{B_k|𝕋^{(k)}|}, fatal in Lemma 2.1, costs only e^{B_kV_T} per tile once the event is copied into every tile.

**Lemma 3.3 (small tori)** [proved]. If no tiling exists, then |𝕋^{(k)}| < 16𝗇⁴(MŘ_k)⁴ = 16V_T, and every bound below holds with B_kV_T replaced by 16B_kV_T, applying (3.1) directly to the event (no chessboard, no locality).

*Proof.* Fewer than 2𝗇 cells per axis gives fewer than (2𝗇)⁴ = 16𝗇⁴ cells. Then (3.1) with m = 1 gives exp(16B_kV_T + C_D − 2c_a r_k(k' − n + 1)) for one survival event, and the remaining steps of §4 and §6 are unchanged. ∎

---

## 4. Attack D: chessboard dilution of the global quotient, under exact locality

This attack differs from TP1's Attacks A–C (TP1 L513–521). A was a union over creations; B asked for a fresh event at each level and a per-level constrained free energy (CF); C closed regions at creation. Here no fresh event per level is used, no constrained-versus-free comparison at fixed coarse data is used, and the only measure statement is the unconditional global bound (MB). The chessboard turns the global bound into a per-tile bound.

**(LOC)** [hypothesis of this section only]. For every tiling, every tile β and every j ≤ k, the restriction to the inner region of β (the tile minus a shell of 𝗇/8 cells) of the history up to level j is a function of the tile data of β, and these functions are covariant under the θ_γ.

**Theorem D** [proved from (K), (COV), (LOC), (MB), LG1(3)]. Let 𝗇 ≥ 16 be fixed, and let x_k ≥ X_D, where X_D is such that for x_k ≥ X_D:

  (D1) B_kV_T + C_D ≤ c_a r_k,  (D2) L^{12}e^{−c_a r_k} ≤ ½,  (D3) 162𝗇⁴ e^{−c_a r_k/512} ≤ ½.

Then for every n ≤ k and level-n cell 𝔷, ν̃(E^{(n)}_𝔷(k)) ≤ e^{−c_a r_k(k−n+1)}, and

  Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C_D' 𝗇⁴ e^{−c_a r_k/2},   (4.1)

with C_D' absolute. Such X_D exists because r_k = M⁴Ř_k⁵ ≥ M⁴(log x_k)^{10} while B_kV_T ≤ C_B(1 + log x_k)𝗇⁴M⁴Ř_k⁴, so (D1) holds once c_aŘ_k ≥ 2C_B(1 + log x_k)𝗇⁴ + C_D, true for large x_k since Ř_k ≥ (log x_k)².

*Proof.* **Step 1 (one survival event).** Choose a tiling in which 𝔷 is deep (translate by a multiple of the cell side). Let β₀ be its tile. By (LOC), f := 𝟏{E^{(n)}_𝔷(k)} is a function of the tile data of β₀ (the event reads 𝒵_i on 𝔷 ⊂ core for i ≤ k). By (COV), θ_γ f = 𝟏{E^{(n)}_{θ_γ𝔷}(k)}. The copies θ_γ𝔷 lie in distinct tiles; tiles are unions of level-j cells for every j ≤ k, so their level-j ancestors are distinct. So Π_γ θ_γ f = 𝟏_𝔼 with 𝔼 = ∩_γ E^{(n)}_{θ_γ𝔷}(k), and (3.1) with m = 𝒩, k_i = k gives ν̃(𝔼) ≤ exp(B_k|𝕋^{(k)}| + 𝒩(C_D − 2c_a r_k(k − n + 1))). Lemma 3.2 with η = 1 gives ‖f‖_ch ≤ exp(B_kV_T + C_D − 2c_a r_k(k−n+1)) ≤ e^{−c_a r_k(k−n+1)} by (D1). Lemma 3.1 with f_{β₀} = f and f_γ = 1 otherwise (‖1‖_ch = 1) gives the claim.

**Step 2 (joint events).** Let 𝔷 be deep in tile β₀ and 𝔠₁, …, 𝔠_m (level k) deep in distinct tiles β₁, …, β_m ≠ β₀ of the same tiling. Then

  ν̃(E^{(n)}_𝔷(k) ∩ ∩_i lv_k(𝔠_i)) ≤ e^{−c_a r_k(k−n+1)} e^{−c_a r_k m}.   (4.2)

Indeed the indicator is Π f_{β_i}, each a tile function by (LOC); Lemma 3.1 bounds its expectation by the product of the chessboard norms, and each norm is bounded as in Step 1 (for lv_k, n = k).

**Step 3 (anchors near c).** Fix a reference tiling τ₀ whose tiles we call *boxes*. Let c be a level-k cell. By Lemma 1.1, on 𝔏_k^{≥a}(c) there is a live component C ∋ c at level k and a level-(k − a) cell 𝔷 ⊂ C with E^{(k−a)}_𝔷(k). Write 𝔷 ∼ c for "𝔷 and c lie in the same live component at level k". So

  ν̃(𝔏_k^{≥a}(c)) ≤ Σ_𝔷 ν̃(E^{(k−a)}_𝔷(k) ∩ {𝔷 ∼ c}),   (4.3)

the sum over level-(k − a) cells 𝔷. Let i(𝔷) be the box distance (sup-norm, in boxes) between the box of c and the box of 𝔷. A level-k cell contains at most L^{4a} level-(k − a) cells: the physical side of a level-j cell is MŘ_jL^j a_K ≥ MŘ_kL^j a_K. So a box contains at most 𝗇⁴L^{4a} candidates 𝔷, and the boxes at distance i number at most (2i + 1)⁴. For i(𝔷) < i₀ := 512, Step 1 gives

  Σ_{i(𝔷)<i₀} ν̃(E_𝔷) ≤ (2i₀ + 1)⁴𝗇⁴L^{4a}e^{−c_a r_k(a+1)}.

**Step 4 (far anchors).** Let i := i(𝔷) ≥ i₀ and suppose 𝔷 ∼ c. The component C is a connected union of level-k cells containing c and 𝔷. Consecutive cells of a path in C lie in equal or adjacent boxes, so the boxes met by C contain a sequence B₀ (box of c), B₁, …, B_{i'} (box of 𝔷) of distinct boxes, consecutive ones adjacent, with i' ≥ i. Choose in each B_s a cell 𝔠_s ⊂ C; it is live at level k.

Consider the 2⁴ tilings τ_ε (ε ∈ {±}⁴) whose face planes are displaced by ε_μ⌊𝗇/4⌋ cells from a corner of the level-k cell of 𝔷 (SA L23336). In one coordinate, with tile side 𝗇 and core [𝗇/8, 7𝗇/8) relative to a face, the two tilings with faces at 𝔷 − ⌊𝗇/4⌋ and 𝔷 + ⌊𝗇/4⌋ differ by a shift s := 2⌊𝗇/4⌋ ∈ [𝗇/2 − 2, 𝗇/2] cells. Their cores cover every position: a position outside the first core lies within 𝗇/8 cells of a face of the first tiling; the faces of the second tiling are at distance s or 𝗇 − s ≥ 𝗇/2 − 2 from those faces; so the position is at distance ≥ 𝗇/2 − 2 − 𝗇/8 = 3𝗇/8 − 2 ≥ 𝗇/8 (for 𝗇 ≥ 8) from every face of the second tiling, that is, in its core. And 𝔷 lies at relative positions ⌊𝗇/4⌋ and 𝗇 − ⌊𝗇/4⌋, at distance ⌊𝗇/4⌋ ≥ 𝗇/8 from the faces, so in both cores. In four coordinates, every level-k cell is deep in at least one τ_ε, and 𝔷 is deep in all sixteen.

By pigeonhole, one tiling τ_ε contains at least (i' + 1)/16 of the cells 𝔠_s as deep cells. A τ_ε-tile meets at most 2⁴ boxes (same side), and the 𝔠_s are in distinct boxes, so these cells lie in at least (i' + 1)/256 distinct τ_ε-tiles, at most one of which is the tile of 𝔷. Since i' ≥ i ≥ 512, (i' + 1)/256 − 1 ≥ i'/512. Keep one cell per tile: m ≥ i'/512 deep live cells in distinct tiles other than that of 𝔷.

So {E_𝔷 ∩ 𝔷 ∼ c} is contained in the union over: the tiling ε (16 choices); the box path B₀, …, B_{i'} from the box of c to that of 𝔷 (at most 80^{i'} paths of length i', and i' ranges over i ≤ i' — the path is determined up to its length, and we sum over i' ≥ i); the cells 𝔠_s (at most 𝗇^{4(i'+1)}); and the subset kept (at most 2^{i'+1}); of events bounded by (4.2) with m ≥ i'/512. Hence

  ν̃(E_𝔷 ∩ {𝔷 ∼ c}) ≤ 16 e^{−c_a r_k(a+1)} Σ_{i'≥i} 160𝗇⁴(160𝗇⁴e^{−c_a r_k/512})^{i'} ≤ 32·160𝗇⁴ e^{−c_a r_k(a+1)} 2^{−i}

by (D3). Summing over 𝔷 at distance i ≥ i₀ (at most (2i + 1)⁴𝗇⁴L^{4a} of them) gives at most C𝗇⁸L^{4a}e^{−c_a r_k(a+1)} with C absolute; absorb 𝗇⁴ into the constant by (D3) once more (160𝗇⁴e^{−c_a r_k/512} ≤ ½ makes 𝗇⁴ ≤ e^{c_a r_k/512}), so the far sum is at most C𝗇⁴L^{4a}e^{−c_a r_k(a + 1 − 1/512)}.

**Step 5 (the age series).** Steps 3–4 give ν̃(𝔏_k^{≥a}(c)) ≤ C𝗇⁴L^{4a}e^{−c_a r_k(a + 1/2)}, uniformly in c. Then

  Σ_a L^{8a} ν̃(𝔏_k^{≥a}(c)) ≤ C𝗇⁴e^{−c_a r_k/2} Σ_a (L^{12}e^{−c_a r_k})^a ≤ 2C𝗇⁴e^{−c_a r_k/2}

by (D2). This is (4.1). Small tori: Lemma 3.3. ∎

**Remark 4.1 (what was used).** Only: the kernel representation, covariance, exact locality, the designated moment bound with k_i = k (so only lineages live at level k, which is SA's own end-mark statement), and LG1(3). In particular: no fresh event per level; no (H); no constrained-versus-free comparison at fixed coarse data (TP1's (CF), `rarity-fresh-x.md`'s (SEP)); no prolongation of the run; no depth floor.

**Remark 4.2 (why the volume is harmless).** In CA's Case C (CA-II L126839–126860) the event at one cell is weighed against 𝖡N_C⁴. Here the event is copied into 𝒩 = |𝕋^{(k)}|/V_T tiles, so the volume cost per copy is B_kV_T, independent of the volume, and the per-copy charge 2c_a r_k(k − n + 1) is extensive in the number of copies because Vol_k charges distinct cells separately (SA L23328: "charges it once for each level").

**Remark 4.3 (the user's suggestions).** *Asymptotic freedom* (p₀(g_k) growing with k) is not used: the per-level charge c_a r_j is level-independent up to the factor Ř_j⁵ and beats L^{8a} because c_a is a free dial. What asymptotic freedom provides, through IN1(3), is only that r_jŘ_j ≪ p₀(g_j) at every level (SA L23286), which makes the charge prepaid (Lemma E.4). *Reflection positivity at fixed coarse data* with the carrying Wilson factor is replaced by reflection positivity of the bare Wilson measure, unconditional; the coarse data enter only through (MB). *Bounded ages* by redesign are not needed: ages are unbounded, but each level of survival is charged.

**Remark 4.4 (exact locality fails as stated).** SA does not claim (LOC). The third test and the collar and rim tests use the true averaged background, which is "not local" in (V_k, V_t) (SA L17336), and the stored fluctuation fields are "built from the averaged background, which is not local" (SA L23328). A sharp test 𝟏{q < θ} at a site where q = θ − 0 flips under an arbitrarily small change of q, and q depends on the bare field outside any fixed tile through the background. So (LOC) cannot be expected for SA's construction; §6 replaces it.

**Remark 4.5 (the unsourced law).** Only the unsourced law ν̃ appears. TP1 reads only it (TP1 L491). No source-weight preservation under replication, which SA D3 (SA L4167–4170) asks for, is needed.

**Remark 4.6 (the rate).** The rate c_a r_k = c_aM⁴Ř_k⁵ has degree 5r in log x_k; p₀ has degree 𝔭₀ > 6r. The chessboard bound on one cell cannot give e^{−cp₀}: a single giant live component can serve every copy with a per-tile cost only of order c_a r_k𝗇 (the volume of the component per tile), because one creation pays for many tiles. A rate e^{−cp₀} needs the first-moment argument of SA Theorem 4.13 and its geometric mean with the age decay (SA L23336), which in turn needs the volume-uniform one-cell bound that CA-II L126035–126110 shows is only a density. Lemma 1.3 makes this unnecessary for TP1.

---

## 5. Attack E: the healing rule gives "volumes are paid by events", and (MB)

TP1's (H) asked for a fresh event at every level of survival (not implied by the rules, Lemma 2.3). The healing rule gives something weaker and true: a lineage may survive without events, but only for O(Ř + log size) levels per event, and the free evolution shrinks it meanwhile. Summed with the weights r_j, this is SA's inequality "volumes are paid by events" (SA L23267–23274). I prove it here from three rule properties, prove the first of them for SA's free evolution, and derive (MB) from it and the lineage-trace bound (LT).

### 5.1 The rule properties

Fix a component X (live at level k, or healed at a step ≤ k) and its lineage. Its *nodes* are the pairs (j, C), C a component of 𝖹_j(X) live at level j. For a node (j, C): pred(j, C) := the nodes at level j − 1 contained in C (SA L23274); Act_{j−1} := the components live at level j − 1 on which 𝐑 of level j − 1 has acted although they stay live (SA L23274); the creations (j, W) are the components of the step-j creation set lying in C, with tree length d'_j(W) in level-j cells (SA L17479); and

  e(j, C) := (|pred(j, C)| − 1)^+ + |pred(j, C) ∩ Act_{j−1}| + Σ_{W⊂C} (d'_j(W) + 1)   (SA L23274).

A node is an *event node* if e(j, C) ≥ 1 and *free* otherwise. Put v(j, C) := r_j|C|_j.

**(R0)** [input: LF1(2), region rules; SA L17479, L23274]. Each node below the top level of the lineage is in pred of exactly one node (its successor). If pred(j, C) = ∅, then C contains a creation of step j.

**(R1)** [input: LF1(2), the per-component reading of SA L17334; numerical part proved in Lemma E.2]. There are A and λ ≤ 1/6 such that for every node,

  v(j, C) ≤ λ Σ_{P∈pred(j,C)} v(P) + A r_j (|pred(j, C)| + Σ_W (d'_j(W) + 1)).   (5.1)

**(R2)** [input: LF1(2), the healing time; SA L23274: a component that "has stayed small over Ř_j + 1 levels without any event … belongs to the class of 𝐑"; SA L23265: 𝐑 acts only after 𝖭_k creation-free steps; CA's age lemma, CA-II L126270–126282, eq. 8.12:eq-volume-ranges-d, stated with proof incomplete, CA-III L111431]. There is C_N such that every maximal chain of free nodes (j_s, C_0), (j_s + 1, C_1), … whose first node has predecessor P has length ℓ ≤ C_N(Ř_{j_s} + log(2 + |P|_{j_s−1})).

*Why (R2) is the chain form of the age lemma.* CA's per-seed allowance is 𝔞(Z) ≤ 2 log_L(d'(Z) + 1) + 2R_{j(Z)} + n₁ + C_S + 4: a log of the size plus a multiple of the radius, the same shape as (R2). A free node has exactly one predecessor, no creation and a predecessor not acted on by 𝐑 (e = 0 and (R0)); along a free chain the component evolves freely, and the chain ends when 𝐑 acts (the next node is then an event node, its predecessor being in Act, or the component is healed and has no successor in the lineage).

### 5.2 Proofs

**Lemma E.1 (hull count)** [proved]. Let fine cells be the unit cubes of ℤ⁴ and coarse cells the aligned cubes of ρ⁴ fine cells, ρ ≥ 1. Let Y be a connected set (closures-meet adjacency) of n fine cells, and Ŷ the set of coarse cells meeting Y. Then |Ŷ| ≤ 81(1 + 2n/ρ).

*Proof.* Choose a maximal subset S' ⊂ Ŷ of coarse cells with pairwise disjoint closures. Every coarse cell of Ŷ has closure meeting that of some cell of S', and a coarse cell has 3⁴ = 81 coarse cells (itself included) with closures meeting its own; so |Ŷ| ≤ 81|S'|. If |S'| = 1 we are done. Otherwise pick y_Q ∈ Y ∩ Q for each Q ∈ S'. Two fine cells in coarse cells with disjoint closures are at sup-distance ≥ ρ + 1. Let t := ⌊ρ/2⌋ and B_Q the fine cells at sup-distance ≤ t from y_Q; these sets are pairwise disjoint, since 2t < ρ + 1. Y is connected and contains a cell at distance > t from y_Q (any y_{Q'}, Q' ≠ Q), so a path in Y from y_Q to it, whose consecutive cells are at sup-distance ≤ 1, contains a cell at each distance 0, 1, …, t from y_Q; hence |Y ∩ B_Q| ≥ t + 1 ≥ ρ/2. Summing, n ≥ |S'|ρ/2, so |Ŷ| ≤ 81·2n/ρ. ∎

**Lemma E.2 ((R1) for SA's free evolution)** [proved from the reading below]. *Reading of SA L17317–17334, per component.* Each node (j, C) satisfies C ⊂ bx(∪_{P∈pred(j,C)} P̂^{~10} ∪ ∪_{W⊂C} W^{~c_W}), where hulls and layers are taken in level-j cells, c_W is the O(1) of SA L17334, and the boxing map bx replaces each component contained in a cube of b₁ cells by its bounding box (SA L17317). Then (5.1) holds with λ = 162·21⁴/L and A := 81·21⁴ + (2c_W + 1)⁴ + b₁⁴; in particular λ ≤ 1/6 for L ≥ L₁ := 972·21⁴.

*Proof.* Let ρ_j be the ratio of the side of a level-j cell to that of a level-(j − 1) cell. The side of a level-j cell is MŘ_jL^ja_K, and Ř_{j−1} ∈ {Ř_j, LŘ_j} (SA L17334: Ř non-increasing, Ř_{j−1} ≤ LŘ_j). So ρ_j = L (a *normal* step, r_j = r_{j−1}) or ρ_j = 1 (a *drop* step, r_j = L^{−5}r_{j−1}). By Lemma E.1 with ρ = ρ_j, |P̂| ≤ 81(1 + 2|P|/ρ_j). A 10-layer enlargement multiplies the number of cells by at most 21⁴ (each cell's 10-neighbourhood has 21⁴ cells), and W^{~c_W} has at most (2c_W + 1)⁴|W| ≤ (2c_W + 1)⁴(d'_j(W) + 1) cells (a connected set of |W| cells has a spanning tree with |W| − 1 edges, so d'_j(W) ≥ |W| − 1). Boxing replaces a component of diameter ≤ b₁ by a box of at most b₁⁴ cells, so |bx(B)| ≤ |B| + b₁⁴·#components(B), and the union has at most |pred| + #W components. Hence

  |C|_j ≤ (162·21⁴/ρ_j) Σ_P |P|_{j−1} + (81·21⁴ + b₁⁴)|pred| + ((2c_W + 1)⁴ + b₁⁴) Σ_W (d'_j(W) + 1).

Multiply by r_j. At a normal step r_j/ρ_j = r_{j−1}/L. At a drop step r_j/ρ_j = r_{j−1}L^{−5} ≤ r_{j−1}/L. Either way the first term is ≤ (162·21⁴/L) Σ_P v(P). ∎

*Remark.* The drop steps are why the weighted form matters: at a drop the cells do not coarsen, the count grows by up to 21⁴, but the weight falls by L⁵.

**Lemma E.3 (volumes are paid by events)** [proved from (R0)–(R2)]. With c_G := (60/47)(4A + C₁), C₁ := (6A/5)C_N(1 + log(2 + 12AC_N)),

  Σ_{(j,C)} r_j|C|_j ≤ c_G Σ_{(j,C)} r_j(Ř_j + 1) e(j, C),   (5.2)

both sums over the nodes of the lineage. This is SA's inequality (SA L23267–23274, "Volumes are paid by events"), with Ř_j + 1 in place of Ř_j.

*Proof.* Let V be the left side (a finite sum), 𝔈 the event nodes. A free node has e = 0, so (|pred| − 1)^+ = 0 and no creation; by (R0), pred ≠ ∅; so it has exactly one predecessor. Group the free nodes into maximal chains of consecutive free nodes. The predecessor P of the first node of a chain is not free (else the chain would extend), so P ∈ 𝔈; and by (R0) each node is the predecessor of at most one node, so at most one chain starts above each event node.

*A chain.* Let the chain have nodes ν_0, …, ν_{ℓ−1} at levels j_s, …, j_s + ℓ − 1, with predecessor P at level j_P = j_s − 1. By (5.1) with |pred| = 1 and no creation, and r non-increasing, v(ν_t) ≤ λv(ν_{t−1}) + A r_{j_s} (ν_{−1} := P), so v(ν_t) ≤ λ^{t+1}v(P) + A r_{j_s}/(1 − λ). Summing, with λ ≤ 1/6,

  Σ_t v(ν_t) ≤ (λ/(1 − λ))v(P) + (6/5)A r_{j_s} ℓ ≤ v(P)/5 + (6/5)AC_N r_{j_s}(Ř_{j_s} + log(2 + |P|)),

by (R2). For y ≥ 0 and 0 < ε < ½, log(2 + y) ≤ εy + log(2 + 1/ε) (the difference εy + log(2 + 1/ε) − log(2 + y) is ≥ 0 at y = 0, decreases until y = 1/ε − 2 and is 1 − 2ε > 0 there, then increases). Take ε = 1/(12AC_N); since r_{j_s}|P| ≤ r_{j_P}|P| = v(P), the term (6/5)AC_N r_{j_s}ε|P| is ≤ v(P)/10. With r_{j_s} ≤ r_{j_P}, Ř_{j_s} ≤ Ř_{j_P}:

  Σ_{chain} v ≤ (3/10)v(P) + C₁ r_{j_P}(Ř_{j_P} + 1).

*Event nodes.* For P ∈ 𝔈, e(P) ≥ 1, |pred(P)| ≤ (|pred(P)| − 1)^+ + 1 ≤ 2e(P), and Σ_W(d' + 1) ≤ e(P); so (5.1) gives v(P) ≤ λ Σ_{pred(P)} v + 3A r_{j_P}e(P). Since each node is in at most one pred, Σ_{P∈𝔈} Σ_{pred(P)} v ≤ V, and

  Σ_𝔈 v ≤ λV + 3A Σ_𝔈 r e.

*Sum.* V = Σ_𝔈 v + Σ_chains Σ v ≤ (13/10)Σ_𝔈 v + C₁ Σ_𝔈 r(Ř + 1) ≤ (13/10)λV + (39/10)A Σ_𝔈 r e + C₁ Σ_𝔈 r(Ř + 1)e, using e ≥ 1 on 𝔈. Since (13/10)λ ≤ 13/60, V ≤ (60/47)(4A + C₁) Σ_𝔈 r(Ř + 1)e, and free nodes contribute 0 to the right side of (5.2). ∎

**(LT)** [input: LF1(3) in lineage-trace form, owner LF1, ⟦LF-mass⟧]. For a lineage 𝔩 define its event cost

  EC(𝔩) := Σ_{creations (j,W)∈𝔩} p₀(g_j)(d'_j(W) + 1) + Σ_{(j,C)∈𝔩} p₀(g_{j−1}) |pred(j, C) ∩ Act_{j−1}|.

For a finite set 𝒟 of cells of levels ≤ k, let 𝔐_𝒟(h) be the set of lineages of the components live at level k together with the lineages of components healed at a step ≤ k whose lineage regions contain a cell of 𝒟. Then

  E_ν̃ exp(¼ Σ_{𝔩∈𝔐_𝒟} EC(𝔩)) ≤ exp(B_k|𝕋^{(k)}| + C_D|𝒟|).   (5.3)

*Sources.* SA's masses by lineage traces: e^{−E_(k)} Σ_h 𝗍(h) ≤ e^{C|𝕋^{(k)}|} Π_𝔩 wt(𝔩), wt(𝔩) = exp[C_chg Vol_k − Dep_k − Σ_{(j,W)} 2p₀(g_j) − Σ_j |Act_j|p₀(g_j)] (SA L23280–23286), the rooted sum of wt over traces (SA L23286–23292), and the floor, which gives the exponent B_k per site (CA-II L126262–126268). These cover the lineages live at level k. For a designated cell whose lineage heals at a step ≤ k, SA asserts that "the lineage of that component pays for the cell" (SA L23328), and CA proves an annealed bound on a healed island containing a given cell, K_H w(𝒮) e^{−(3/2)p₀(g_k)} (CA-II L113200–113235, eq. 8.9:eq-healed-old-region-9 at L113228), from the inputs of its large-field block bound. (5.3) is these statements in one exponential moment. I have not checked that SA's rooted sum leaves the fraction ¼ of EC; the dial 𝗐 of SA L23292 is the device for it.

**Lemma E.4 ((MB) from (LT))** [proved from (LT), (R0)–(R2)]. Let X₁(c_a) be such that 4c_ac_G r_i(Ř_i + 1) ≤ ¼p₀(g_i) whenever x_i ≥ X₁ (possible since r_iŘ_i = M⁴Ř_i⁶ has degree 6r < 𝔭₀ in log x_i; SA L23286 states r_jŘ_j ≪ p₀(g_j)). If x_k ≥ X₁, then (MB) holds.

*Proof.* (a) *Volume against cost.* For a lineage 𝔩 put Vol(𝔩) := Σ_{(j,C)∈𝔩} r_j|C|_j. By (5.2), Vol(𝔩) ≤ c_G Σ r_j(Ř_j + 1)e(j, C). Split e. *Merges:* the nodes form a tree (each node has at most one successor, (R0)); assign to each node with |pred| = p ≥ 2 the leftmost leaves of the subtrees of its 2nd, …, p-th predecessors (any fixed order). Each leaf is assigned at most once (the node where its leftmost path joins as a non-first child), and leaves lie below the node they are assigned to; since r_j(Ř_j + 1) is non-increasing in j, Σ r_j(Ř_j + 1)(|pred| − 1)^+ ≤ Σ_{leaves (i,C')} r_i(Ř_i + 1). A leaf has pred = ∅, so contains a creation by (R0): the leaf sum is ≤ Σ_{(i,W)} r_i(Ř_i + 1)(d'_i(W) + 1). *Act:* r_j(Ř_j + 1)|pred ∩ Act_{j−1}| ≤ r_{j−1}(Ř_{j−1} + 1)|pred ∩ Act_{j−1}|. *Creations:* as they stand. So

  Σ r(Ř + 1)e ≤ 2 Σ_{(j,W)} r_j(Ř_j + 1)(d'_j(W) + 1) + Σ_{(j,C)} r_{j−1}(Ř_{j−1} + 1)|pred ∩ Act_{j−1}|.

All levels in a lineage are ≤ k, so x_i ≥ x_k ≥ X₁, and the choice of X₁ gives 2c_a Vol(𝔩) ≤ ¼EC(𝔩).

(b) *The event.* Let 𝒟 = {𝔷₁, …, 𝔷_m} be as in (MB), and suppose ∩_i E^{(n_i)}_{𝔷_i}(k_i). For each i and n_i ≤ j ≤ k_i, the level-j cell containing 𝔷_i is live, hence in a component at level j; following successors, this component lies in the lineage of a component live at level k or healed at a step ≤ k, and that lineage contains 𝔷_i, so it is in 𝔐_𝒟. The level-j ancestors of distinct 𝔷_i are distinct cells. So Σ_{𝔩∈𝔐_𝒟} Vol(𝔩) ≥ Σ_i Σ_{j=n_i}^{k_i} r_j ≥ r_k Σ_i (k_i − n_i + 1).

(c) *Markov.* ν̃(∩_i E_i) ≤ e^{−2c_a r_kΣ(k_i−n_i+1)} E exp(2c_a Σ_{𝔐_𝒟} Vol) ≤ e^{−2c_a r_kΣ(k_i−n_i+1)} E exp(¼Σ_{𝔐_𝒟} EC) ≤ (3.1). ∎

### 5.3 Where Attack E stops

Attack E proves (5.2) from (R0)–(R2) and (MB) from (LT). It does not prove: (LT), which is LF1(3) (⟦LF-mass⟧, already open in the assembly) in lineage-trace form; the per-component reading of SA L17334 used in Lemma E.2; and (R2), which is the chain form of CA's age lemma and SA's "class of 𝐑" sentence. A proof of (R2) from the rules needs the definition of the class of 𝐑 and the count of drop steps: in ℓ consecutive levels there are at most 2 + r log_L(1 + log(1 + B_♯ℓ)) drops (Ř_{j}/Ř_{j+ℓ} ≤ L(1 + log(1 + B_♯ℓ))^r by IN1(3)), each multiplying the size by at most 162·21⁴ + A, so (R2) holds up to a factor of order log log ℓ if the class of 𝐑 contains every component that has had at most A/(1 − λ) + 1 cells for Ř_j + 1 creation-free levels. That factor would change c_G by a log log factor, harmless against p₀. I record (R2) as an input; it belongs to LF1(2).

---

## 6. Attack F: locality of the history events

Theorem D needs (LOC); (LOC) is not available (Remark 4.4). Three ways to supply locality.

### 6.1 F1: make every test local in the bare field — fails

*Idea.* Replace the true averaged background in the third, collar and rim tests (SA L17336) and in 𝐑's test on stored fluctuation fields (SA L23328) by backgrounds localised in the test cube, as χ_t and χ'_k already are (SA L17336). The block fields V_j are block averages of the bare field, so every test then reads the bare field in O(1) test cubes, 𝐑 reads it in its component (of at most 100 cells per side, CA-II L113210), and (LOC) holds with a margin of O(1) cells per level.

*Exact reason it fails.* The step integrates the fluctuation in the variable 𝒜_k = (1/i) log(V_k(V^bg_k)^{−1}) on Ω_t, where V^bg_k is the constrained background on Ω_t (SA L17336). SA chooses the true background for the third test so that "these tests are therefore local in the new variable 𝒜_k" (SA L17336), and the induction carries the property that "each indicator stored in 𝐓_k(Z) depends only on those field variables that are localised in Z" (SA L17344), which is what makes everything attached to Z_t factorise over its components (the four facts, SA L17336–17341). A test that is exactly local in (V_k, V_t), rewritten in (𝒜_k, V_t), depends on V^bg_k, hence on V_t over all of Ω_t; the indicator attached to one component then reads the fields of every other component, the pivot difficulty of SA L17341 at every test. To restore factorisation one would expand the test into localised differences (a telescoping sum over nested localisations, each difference bounded by ‖ζ'‖e^{−δ·dist}); but the terms of such an expansion are signed, and the positive history law (LF1(1): "for real inputs every probability weight is nonnegative") is lost. (MB) and the chessboard (Lemma 3.1 needs f ≥ 0) need that positivity. So exact locality in the bare field and exact factorisation in the RG variables cannot both hold for a non-constant test: the change of variables V_k ↦ 𝒜_k is nonlocal. This is structural, not a missing constant.

### 6.2 F2: smooth tests decided by the auxiliary uniforms — reduces locality to a deterministic stability statement

*Idea.* Make the window an event of an auxiliary uniform variable, not of a field value. Then a window has conditional probability exactly equal to its width, given everything before it, with no conditional density of any field.

**(SM)** [input: design of LF1's tests, owner LF1]. Fix κ ∈ (0, ½]. Each test τ of the construction (all of χ_t, χ'_k, χ^{(k)}, the collar and rim tests, the tests inside 𝐑, and every other decision that depends on field values) is decided by its uniform: τ is passed iff u_τ < ζ(q_τ/θ_τ), where q_τ ≥ 0 is the tested quantity, θ_τ > 0 its threshold, and ζ(t) := 1 for t ≤ 1, 1 − (t − 1)/κ for 1 ≤ t ≤ 1 + κ, 0 for t ≥ 1 + κ. Equivalently, τ is the sharp test 𝟏{q_τ < θ_τ(1 + κ(1 − u_τ))}: a sharp test with an independent random threshold in [θ_τ, (1 + κ)θ_τ]. The input asserts that all bounds of LF1, NL1, SC1, IN1 and UV1 hold, with the same constants, for every assignment of thresholds θ_τs_τ with s_τ ∈ [1, 1 + κ] chosen site by site.

*Why (SM) is a robustness statement and not a new construction.* The equivalence is the identity u < 1 − (t − 1)/κ ⟺ t < 1 + κ(1 − u) for t ∈ [1, 1 + κ], with u < 1 almost surely for t ≤ 1. So the history law under (SM) is the average, over independent thresholds, of sharp constructions. Bounds proved for the sharp construction uniformly in the thresholds pass to the average. The room needed is that of SA's Lemma 2.2, "the factor 2 between the two thresholds gives exactly the room needed" (SA L17396); a factor 1 + κ ≤ 3/2 per test leaves room 2/(1 + κ) ≥ 4/3 > 1.

**(QL)** [outstanding; stated in full in §7]. Two-run stability: (QL1) tested quantities at decision sites in the level-j inner region of a tile differ, between two runs with the same tile data and the same earlier inner decisions, by at most C_qθ_τe^{−δD_j}; (QL2) the discrete data on the next inner region then agree.

*Parameters.* Let 𝗇 ≥ 16 be a power of L with 𝗇 ≥ 16m₀C_L, C_L := Σ_{s≥0} L^{1−s}(1 + log(1 + B_♯s))^r (finite). Let b' := 13 and

  ϖ_k := δ𝗇MŘ_k/128,  ε_j := e^{−ϖ_k}(2L^{b'+4})^{−(k−j)} / (2N_τ𝗇⁴(MŘ_k)⁴),  D_j := δ^{−1} log(1/(κε_j) · C_q).   (6.1)

The *inner regions* of a tile β are J_0 := β and J_j := the points of J_{j−1} at sup-distance ≥ μ_j from the complement of J_{j−1}, with μ_j := m₀MŘ_{j−1}L^{j−1}a_K + D_jL^ja_K (m₀ level-(j − 1) cells for the discrete operations of step j − 1, plus D_j level-j lattice units for the decoupling of the level-j tests), for 1 ≤ j ≤ k + 1, D_{k+1} := 0. Level-j decisions are compared on J_j.

**Lemma F.0 (margins)** [proved]. If x_k ≥ X_F, then Σ_{j≤k+1} μ_j ≤ (𝗇/8)MŘ_kL^ka_K, so J_{k+1} contains the core of β.

*Proof.* In units of the level-k cell side MŘ_kL^ka_K, the m₀-part is Σ_{j=1}^{k+1} m₀(Ř_{j−1}/Ř_k)L^{j−1−k} = Σ_{s≥0} m₀(Ř_{k−s}/Ř_k)L^{−s}. The smallest power of L that is ≥ y ≥ 1 is ≤ Ly, so Ř_{k−s} ≤ L(log x_{k−s})^r ≤ L(log x_k + log(1 + B_♯s))^r (IN1(3): x_{k−s} ≤ x_k + B_♯s; and log(x + y) ≤ log x + log(1 + y) for x ≥ 1), while Ř_k ≥ (log x_k)^r ≥ 1; so Ř_{k−s}/Ř_k ≤ L(1 + log(1 + B_♯s))^r, and the m₀-part is ≤ m₀C_L ≤ 𝗇/16. The D-part is Σ_{s≥0} D_{k−s}L^{−s}/(MŘ_k). With D_{k−s} = δ^{−1}[ϖ_k + s log(2L^{b'+4}) + log(2N_τ𝗇⁴(MŘ_k)⁴C_q/κ)], the sum is ≤ 2δ^{−1}[ϖ_k + log(2L^{17}) + log(2N_τ𝗇⁴(MŘ_k)⁴C_q/κ)]/(MŘ_k), using Σ_s L^{−s} ≤ 2 and Σ_s sL^{−s} ≤ 1. The ϖ-part is 2δ^{−1}ϖ_k/(MŘ_k) = 𝗇/64, and the logarithms are o(MŘ_k) as x_k → ∞, so for x_k ≥ X_F the D-part is ≤ 𝗇/32. Total ≤ 𝗇/16 + 𝗇/32 < 𝗇/8. ∎

*The local run.* For a tile β let U^β be U on the bonds of the closed tile and 𝟙 elsewhere, and ω^β be ω at the locations in β and ½ elsewhere. The *local run* H^β := H_k(U^β, ω^β) is the true construction applied to a modified configuration; it is a function of the tile data of β. By (COV), and because the frozen exterior (𝟙, ½) is invariant, θ_γ maps the local run of the reference tile to the local run of tile γ. For a decision site τ of level j of the local run located in J_j, its *local window* is W_τ := {|u_τ − ζ(q^β_τ/θ_τ)| ≤ ε_j}, where q^β_τ is its tested value in the local run. Put A_{β,j} := ∪_{τ: level j, located in J_j} W_τ and G_{β,<j} := ∩_{i<j} A_{β,i}^c.

**Lemma F.1 (windows are fresh)** [proved from (K)]. For every tile β and level j, P(A_{β,j} | ℱ_{j−1}) ≤ η_j := e^{−ϖ_k}(2L^{b'})^{−(k−j)}, and the events A_{β,j}, β ranging over distinct tiles, are conditionally independent given ℱ_{j−1}.

*Proof.* The local run's level-j decision sites in β are visited in the order of moves, τ₁, τ₂, …; which potential site comes next, and its tested value q^β_{τ_s}, are functions of U and of the u_σ (σ located in β) read before τ_s. The u_τ are indexed by the fixed set 𝒯 of potential sites, so u_{τ_s} is uniform and independent of everything read before it. Hence P(W_{τ_s} | U, earlier u_σ) ≤ 2ε_j. There are at most N_τ potential sites per location and at most (𝗇MŘ_kL^{k−j})⁴ level-j sites in β (its side is 𝗇MŘ_kL^ka_K and the level-j spacing L^ja_K). The union bound and the tower property give P(A_{β,j} | ℱ_{j−1}) ≤ 2ε_jN_τ𝗇⁴(MŘ_k)⁴L^{4(k−j)} = e^{−ϖ_k}(2L^{b'+4})^{−(k−j)}L^{4(k−j)} = η_j. Given ℱ_{j−1}, A_{β,j} is a function of ℱ_{j−1}-measurable data and of the level-j uniforms located in β; these families are independent for distinct β and independent of ℱ_{j−1}. ∎

**Lemma F.2 (agreement)** [proved from (SM), (QL)]. On G_{β,<j*}, the true run H_k(U, ω) and the local run H^β have the same decision sites and the same decisions at every site of level i < j* located in J_i, and therefore (QL2) the same live regions of levels < j* on J_{j*}.

*Proof.* Induction over the decision sites in their order. Let τ, of level j < j* and located in J_j, be the next site, and suppose agreement at all earlier sites located in their regions. The two configurations coincide on the tile data of β. By (QL1), τ is a site of both runs and |q_τ − q^β_τ| ≤ C_qθ_τe^{−δD_j}. Since ζ is Lipschitz with constant 1/κ, |ζ(q_τ/θ_τ) − ζ(q^β_τ/θ_τ)| ≤ C_qe^{−δD_j}/κ = ε_j by (6.1). On W_τ^c, |u_τ − ζ(q^β_τ/θ_τ)| > ε_j, so u_τ lies on the same side of ζ(q_τ/θ_τ) as of ζ(q^β_τ/θ_τ): the decisions agree. The last clause is (QL2). ∎

**Theorem F** [proved from (K), (COV), (SM), (QL), (MB), LG1(3)]. Let x_k ≥ X_F, where X_F is such that Lemma F.0 holds and

  (F1) B_kV_T + C_D ≤ c_a r_k,  (F2) c_a r_k ≥ ϖ_k + log(4L^{b'}),  (F3) 160𝗇⁴(4e^{−ϖ_k})^{1/512} ≤ ½.

Then for every n ≤ k and level-n cell 𝔷, ν̃(E^{(n)}_𝔷(k)) ≤ 4e^{−ϖ_k}(2L^{b'})^{−(k−n)}, and

  Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C_F 𝗇⁸ e^{−ϖ_k},  ϖ_k = δ𝗇MŘ_k/128 ≥ (δ𝗇M/128)(log x_k)²,   (6.2)

with C_F absolute. This is (0.1*). X_F exists: ϖ_k/(c_a r_k) = δ𝗇/(128c_aM³Ř_k⁴) → 0, B_kV_T/(c_a r_k) ≤ C_B(1 + log x_k)𝗇⁴/(c_aŘ_k) → 0, and ϖ_k → ∞.

*Proof.* **Step 1 (domination).** Take a tiling in which 𝔷 is deep, β its tile. Define tile functions

  f_∅ := 𝟏{G_{β,<k+1}} 𝟏{E^{(n)}_𝔷(k) in H^β},  f_{j*} := 𝟏{G_{β,<j*} ∩ A_{β,j*}} 𝟏{E^{(n)}_𝔷(j* − 1) in H^β}  (1 ≤ j* ≤ k),

with E^{(n)}_𝔷(j* − 1) the sure event when j* ≤ n. The events G_{β,<k+1} and G_{β,<j*} ∩ A_{β,j*} (1 ≤ j* ≤ k) partition the sample space (first level with a local window, or none). On G_{β,<j*}, Lemma F.2 gives agreement of the live regions of levels < j* on J_{j*} ⊇ J_{k+1} ⊇ core ∋ 𝔷 (Lemma F.0). So on the true event E^{(n)}_𝔷(k): if no local window opens up to level k, f_∅ = 1; if the first one opens at j*, then E^{(n)}_𝔷(j* − 1) holds in the true run, hence in H^β, and f_{j*} = 1. Thus

  𝟏{E^{(n)}_𝔷(k)} ≤ f_∅ + Σ_{j*=1}^{k} f_{j*}.   (6.3)

**Step 2 (norms).** Write 𝔷_γ := θ_γ𝔷. Copies lie in distinct tiles, so their level-j ancestors are distinct for every j ≤ k.

(a) Π_γ θ_γ f_∅ ≤ 𝟏{∩_γ E^{(n)}_{𝔷_γ}(k) in the true run} (agreement in each tile). By (MB) with k_i = k and Lemma 3.2, ‖f_∅‖_ch ≤ e^{B_kV_T + C_D − 2c_a r_k(k−n+1)} ≤ e^{−c_a r_k(k−n+1)} ≤ ½e^{−ϖ_k}(2L^{b'})^{−(k−n)}, by (F1) and (F2).

(b) j* ≤ n: Π_γ θ_γ f_{j*} ≤ Π_γ 𝟏_{A_{γ,j*}}. By Lemma F.1, E Π_γ 𝟏_{A_{γ,j*}} = E Π_γ P(A_{γ,j*} | ℱ_{j*−1}) ≤ η_{j*}^𝒩, so ‖f_{j*}‖_ch ≤ η_{j*}.

(c) n < j* ≤ k: Π_γ θ_γ f_{j*} ≤ 𝟏_𝔄 Π_γ 𝟏_{A_{γ,j*}}, with 𝔄 := ∩_γ {E^{(n)}_{𝔷_γ}(j* − 1) in the true run} (agreement before j* in each tile). 𝔄 ∈ ℱ_{j*−1}. By Lemma F.1 and (MB) with k_i = j* − 1,

  E[𝟏_𝔄 Π_γ 𝟏_{A_{γ,j*}}] = E[𝟏_𝔄 Π_γ P(A_{γ,j*} | ℱ_{j*−1})] ≤ η_{j*}^𝒩 exp(B_k|𝕋^{(k)}| + 𝒩(C_D − 2c_a r_k(j* − n))),

so ‖f_{j*}‖_ch ≤ η_{j*}e^{B_kV_T + C_D − 2c_a r_k(j*−n)} ≤ η_{j*}e^{−c_a r_k(j*−n)} by (F1).

**Step 3 (sum).** By (6.3) and Lemma 3.1 (other tiles ≡ 1),

  ν̃(E^{(n)}_𝔷(k)) ≤ ‖f_∅‖ + Σ_{j*≤n} η_{j*} + Σ_{n<j*≤k} η_{j*}e^{−c_a r_k(j*−n)}
   ≤ e^{−ϖ_k}(2L^{b'})^{−(k−n)}[½ + Σ_{s≥0}(2L^{b'})^{−s} + Σ_{s≥1}(2L^{b'}e^{−c_a r_k})^s] ≤ 4e^{−ϖ_k}(2L^{b'})^{−(k−n)},

using η_{j*} = e^{−ϖ_k}(2L^{b'})^{−(k−n)}(2L^{b'})^{j*−n} and 2L^{b'}e^{−c_a r_k} ≤ ½ (F2).

**Step 4 (joint events).** Let 𝔷 be deep in β₀ and level-k cells 𝔠₁, …, 𝔠_m deep in distinct tiles β₁, …, β_m ≠ β₀ of one tiling. Apply (6.3) to each (for lv_k(𝔠_i), n = k) and multiply: the indicator of E^{(n)}_𝔷(k) ∩ ∩_i lv_k(𝔠_i) is at most a product over the m + 1 tiles of sums of tile functions. Expand the product, apply Lemma 3.1 to each term, and re-sum:

  ν̃(E^{(n)}_𝔷(k) ∩ ∩_i lv_k(𝔠_i)) ≤ 4e^{−ϖ_k}(2L^{b'})^{−(k−n)} (4e^{−ϖ_k})^m.   (6.4)

**Step 5 (anchors).** Repeat Steps 3–5 of Theorem D with (6.4) in place of (4.2). Near anchors (i < 512): at most 1025⁴𝗇⁴L^{4a} cells, each ≤ 4e^{−ϖ_k}(2L^{b'})^{−a}. Far anchors at box distance i ≥ 512: for a box path of length i' ≥ i there are m ≥ i'/512 deep live cells in distinct tiles other than that of 𝔷 in one of the 16 tilings, so

  ν̃(E_𝔷 ∩ {𝔷 ∼ c}) ≤ 16·4e^{−ϖ_k}(2L^{b'})^{−a} Σ_{i'≥i} 2𝗇⁴(160𝗇⁴(4e^{−ϖ_k})^{1/512})^{i'} ≤ 256𝗇⁴e^{−ϖ_k}(2L^{b'})^{−a}2^{−i}

by (F3); summing over the at most (2i + 1)⁴𝗇⁴L^{4a} anchors at distance i and over i ≥ 512 gives at most C𝗇⁸L^{4a}e^{−ϖ_k}(2L^{b'})^{−a}. So ν̃(𝔏_k^{≥a}(c)) ≤ C𝗇⁸L^{4a}e^{−ϖ_k}(2L^{13})^{−a}, uniformly in c, and

  Σ_a L^{8a}ν̃(𝔏_k^{≥a}(c)) ≤ C𝗇⁸e^{−ϖ_k} Σ_a (L^{12}/(2L^{13}))^a ≤ 2C𝗇⁸e^{−ϖ_k}.

Small tori: Lemma 3.3 (there (MB) is applied directly to the events and no locality is used). ∎

*What F2 changes relative to SA's Lemma 4.15.* SA's windows are on tested field values and are paid "under the conditional law of a tested fluctuation value" (SA L23328). Here the window is on u_τ, and Lemma F.1 is exact: no conditional law of any field enters. SA's widths decrease like (2L⁴)^{−(k−j)} l_□^{−4} (SA L23328); mine carry the extra factor e^{−ϖ_k}, which is what makes the one-cell bound small, and the margin budget of Lemma F.0 shows this costs only a fixed fraction of the tile when ϖ_k ≤ δ𝗇MŘ_k/128. SA's second hypothesis, no long cluster (SA L23328), is not used: under (SM) large-field regions inside the tile are frozen bare data common to both runs, so they do not carry the difference between the runs; whether (QL) needs it is part of §7.

### 6.3 F3: keep SA's sharp tests and pay the windows by conditional densities — fails

*Idea.* Keep 𝟏{q_τ < θ_τ}, define the window as {|q^β_τ − θ_τ| ≤ ε'_j}, and bound its probability by a conditional density of the tested value (SA L23328).

*Exact reason it fails.* In Step 2(c) one needs, for the event 𝔄 of the history up to level j* − 1, E[𝟏_𝔄 Π_γ 𝟏{window at level j* in tile γ}] ≤ η^𝒩ν̃(𝔄). With sharp tests the windows are functions of U, and so is 𝔄. Conditioning on ℱ_{j*−1} ⊇ σ(U) leaves no randomness. One must condition on less: on the history up to level j* − 1 and the coarse data, and bound the conditional probability that a level-j* tested fluctuation value lies in a window of width ε', jointly over 𝒩 tiles. That is a bounded conditional density of a fluctuation coordinate under the interacting history law at fixed coarse data, on every history including large-field ones. SA itself records that "no such convexity, symmetry or force bound is asserted for the resummed interacting conditional density" (SA L28219–28221, as quoted in TP1 L19). It is the same kind of fixed-coarse-data comparison at which `rarity-fresh-x.md` stopped ((SEP), its §3) and at which TP1's Attack B stopped ((CF), TP1 L519). SA's triggers are paid the same way, "by the conditional law of the fluctuation field in its box" (SA L23328). F2 removes exactly this step by moving the randomness of the decision into an independent uniform.

---

## 7. The first outstanding statement: (QL), two-run stability

Fix a level k, a tile side 𝗇, the parameters (6.1) and the inner regions J_j of a tile β (§6.2). The construction is the one of (SM).

**(QL) [outstanding].** There are constants δ > 0, C_q and m₀ (depending only on the constants fixed before the coupling ceiling) such that, for every compatible torus, every tile β, every choice of D_j ≥ 0 subject to Lemma F.0's budget, and every two configurations (U, ω), (U', ω') that coincide on the tile data of β:

(QL1) Let τ be a potential decision site of level j located in J_j. Suppose the two runs have the same decision sites and the same decisions at every site of level i < j located in J_i, and at every site of level j located in J_j that precedes τ. Then τ is a decision site of both runs or of neither, and if of both, |q_τ − q'_τ| ≤ C_qθ_τe^{−δD_j}.

(QL2) Suppose the two runs have the same decision sites and decisions at every site of level i ≤ j located in J_i. Then, for every i ≤ j, 𝒵_i ∩ J_{j+1} is the same in both runs, and so is, for every level-i cell in J_{j+1}, the set of levels i' ∈ [i, j] at which it is live.

*Status and sources.* (QL) is deterministic: it compares two runs pointwise and involves no measure. It is SA's "agreement of two runs inside a tile" (SA L23328) with SA's narrow-window hypothesis replaced by the explicit Lipschitz bound (QL1), for the construction of (SM). CA lists the related "translation covariance of the label histories" as stated with proof incomplete (CA-III L111428). The decay rate δ is "the rate at which two backgrounds that have the same data in a region approach each other within that region" (SA L23328); that is a BG1/PR1 property.

*What a proof must check, operation by operation (SA (2a)–(2d)).*
1. χ_t and χ'_k: built from localised backgrounds, depending on V_t, V_k "only within O(1) test cubes" (SA L17336). V_t, V_k are block averages of the bare field. (QL1) holds for them with D_j replaced by the test-cube size, provided the block averages in the inner region are determined by the tile's bare field (true: the averaging is block-internal, SA (1a)).
2. The third test χ^{(k)}, the collar and rim tests: they read 𝒜_k on Ω_t, built with the true background (SA L17336, L17348–17360). (QL1) needs: if the decisions agree on J_j, then the two backgrounds V^bg_k on Ω_t ∩ J_j differ by ≤ Ce^{−δ dist} at distance dist from the complement of J_j. Inside large-field regions the data are frozen; they are bare data of the tile, common to both runs. So the difference enters only through Ω_t across the boundary of J_j, and the decay is the propagator decay of BG1/PR1 (SA (1b)–(1c)).
3. Stored fluctuation fields: "built from the averaged background, which is not local", and read by "a single test of 𝐑" (SA L23328). Here (QL1) needs a propagation estimate across levels: a stored field of level i < j, which differs between the runs by ≤ Ce^{−δD_i}, enters a level-j tested value with a Lipschitz constant Λ_{ij}, and Σ_{i<j} Λ_{ij}Ce^{−δD_i} ≤ C_qθ_τe^{−δD_j} must hold. With D_i − D_j = δ^{−1}(j − i) log(2L^{b'+4}) from (6.1), this needs Λ_{ij} ≤ C(2L^{b'+4})^{(j−i)/2}: the influence of an old stored field on a new test may grow at most geometrically in the level difference, at a fixed rate. **This is the first sub-statement of (QL) that I cannot check from the text I read.**
4. Pivot values (SA L17341): Balaban retains only old tests whose cubes lie outside Ω_t^{~} (SA L17341), so a test of one component reads a pivot of another only within one layer; this costs O(1) cells of margin per level (part of m₀).
5. 𝐑: its tests use backgrounds "localised in the component" (SA L17344), and it acts only on components of at most 100 cells per side (CA-II L113210, L113325). A component meeting J_{j+1} on which 𝐑 acts therefore lies in J_j once m₀ ≥ 100: margin.
6. Hulls, layers, boxing and rounds (SA L17317–17334): deterministic and local with O(1) layers per level (part of m₀); boxing acts only on components inside a cube of O(1) cells.
7. Determining sets start at Ω₀ = Ω₁^~, not at the torus (SA L17317, L23265, L23328, citing Balaban CMP 119 p. 255): without this a single rough plaquette anywhere would turn off the background everywhere, and (QL) would be false. This is a property of the definition, which SA states and requires.

So (QL) reduces, item by item, to the background decay (item 2, owner BG1/PR1), the cross-level propagation of stored fields (item 3), and the margin bookkeeping (items 4–6). Item 3 is the precise first open sub-statement.

**The three attacks and where each stopped.**
- *D (chessboard dilution).* Complete as an implication (Theorem D). Stopped at exact locality (LOC), which SA's construction does not have (Remark 4.4).
- *E (healing rule ⇒ volumes paid by events ⇒ (MB)).* Complete as an implication (Lemmas E.1–E.4). Stopped at its inputs (LT) (= LF1(3), ⟦LF-mass⟧, open) and (R2) (the chain form of CA's age lemma, stated without complete proof in CA), both owned by LF1.
- *F (locality).* F1 failed: a test exactly local in the bare field is nonlocal in the RG variable 𝒜_k, and localising it produces signed terms that destroy the positive history law. F3 failed: sharp tests make the windows functions of U, so their cost needs a conditional density at fixed coarse data, which no source asserts (SA L28219–28221). F2 succeeded as an implication (Theorem F) and leaves (QL), whose first unchecked item is the cross-level propagation of stored fields.

---

## 8. Status of every statement

| Statement | Where | Status |
|---|---|---|
| Lemma 1.1 (anchor) | §1.1 | [proved] from SA's definitions |
| Lemma 1.3 (rate e^{−c(log x)²} suffices for TP1) | §1.3 | [proved] |
| Lemma 2.1 (one cell against the global quotient) | §2.4 | [proved] |
| Lemma 2.2 (first moment gives a density) | §2.4 | [proved] |
| Lemma 2.3 (TP1's (H) is not implied by SA's rules) | §2.4 | [proved]; (H) false on any positive-weight quiet history after a creation |
| Lemma 3.1 (chessboard with auxiliary uniforms) | §3.5 | [proved] from LG1(3) |
| Lemmas 3.2, 3.3 (dilution; small tori) | §3.5 | [proved] |
| Theorem D | §4 | [proved] from (K), (COV), (LOC), (MB), LG1(3) |
| (LOC) exact locality | §4 | not available for SA's construction (Remark 4.4) |
| Lemma E.1 (hull count) | §5.2 | [proved] |
| Lemma E.2 ((R1) for the free evolution, L ≥ L₁) | §5.2 | [proved] from the per-component reading of SA L17334 |
| Lemma E.3 (volumes paid by events) | §5.2 | [proved] from (R0)–(R2) |
| Lemma E.4 ((MB) from (LT)) | §5.2 | [proved] |
| (R0), (R1)-reading, (R2) | §5.1 | [input: LF1(2)]; (R2) = chain form of CA's age lemma |
| (LT) | §5.2 | [input: LF1(3), ⟦LF-mass⟧] |
| (K) | §3.1 | [input: LF1(1)] |
| (COV) | §3.2 | [input: LF1]; CA-III L111428 incomplete |
| (SM) | §6.2 | [input: design of LF1's tests; threshold robustness] |
| F1 | §6.1 | fails; exact reason given |
| Lemmas F.0, F.1, F.2 | §6.2 | [proved] (F.2 from (QL)) |
| Theorem F = (0.1*) | §6.2 | [proved] from (K), (COV), (SM), (QL), (MB), LG1(3) |
| F3 | §6.3 | fails; exact reason given |
| (QL) | §7 | **[outstanding]**; first unchecked item: cross-level propagation of stored fields |
| (0.1) with rate p₀ | §1.3 | not proved; not needed by TP1 (Lemma 1.3) |

**What AG1 now is.** (0.1*) at every level, uniformly in the volume, the cutoff and the position, for the unsourced law, as an implication from (QL) and inputs owned by LF1 ((K), (COV), (SM), (R0)–(R2), (LT)) and LG1(3) [C]. With Lemma 1.3, TP1(1)–(5) then hold with (0.1*) in place of (10.1).

**What changed relative to TP1 §10.**
- (H) is not implied by the rules (Lemma 2.3); Lemma 10.1's route is replaced by the volume mark (Lemma E.3) and the chessboard (Theorems D, F).
- (SR) and (CF) are not needed: no fresh event per level and no constrained-versus-free comparison at fixed coarse data enter. The only measure input is the unconditional exponential moment (LT)/(MB).
- The rate drops from p₀ to (log x)², which TP1 tolerates.
- The open core moves from a measure statement (rarity at fixed coarse data) to a deterministic one (QL).

---

## 9. Remarks

1. *Relation to CA's Case C.* CA's step (∗) (CA-II L126839–126990) weighs one cell against 𝖡(γ_*)N_C⁴. Theorem F weighs one tile against B_kV_T, independent of N_C. So the depth floor (8.12:eq-depth-floor-rarity-a) is not needed, and neither are the prolonged runs. Theorem F does not distinguish healed from never-healed lineages: (MB) with k_i < k covers both, through (LT)'s designated healed lineages.
2. *Relation to SA's Lemma 4.15.* The structure (tiles, price of survival with 𝗐 = 0, anchors, 2⁴ tilings) is SA's. The changes are: windows on uniforms (F2) instead of on field values; widths carrying e^{−ϖ_k}; no long-cluster hypothesis; and the healing rule written out as Lemma E.3.
3. *A reroute that avoids volume uniformity.* Y3 L796–797 proves its short-distance law and then lets "the two-state comparison" transfer it to arbitrary volumes; CA does the same with its volume-transfer theorem (CA-III L71642, L72830–72852). CA's Case V (CA-II L126359–126640) gives the age series without a depth floor on weakly coupled tori. If TP1's reference law were proved on one weakly coupled torus and transferred, AG-k₁ would be needed only there. TP1 chose an infinite-volume reference (TP1 L20, L268) and so needs volume uniformity. This reroute is not an attack on (0.1*) and I did not pursue it.
4. *Bounded ages.* Ages are not bounded: by the positivity of the law every age has positive weight (CA-II L126085). The chessboard makes their weight decay geometrically instead.
5. *RAM and method.* No computation was run. Every source read was a bounded range, cited above.

*Line count of this file:* see the closing line.

End of pass 1. This file has 511 lines.
