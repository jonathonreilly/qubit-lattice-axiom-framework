# AG1 at level k: the weighted live-age tail, uniformly in the volume — round 2, long draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, written for the lead as the round-2 long draft of AG1. It replaces `library/ag1-draft.md` (round 1). Research text. It is not an audit, it grants no status, and no other model has read it. No step rests on a computation. Every argument is a finite sum, a union bound, a conditional expectation of independent uniform variables, a geometric series, a counting argument on cubes, a comparison of distances, or an application of a named input; each is meant to be Lean-formalisable.

Credit. The architecture is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the large-field histories, the region rules, the three fates, lineages, the volume mark, the price of survival, the chessboard for the law of the histories, the two-run agreement inside a tile and its two hypotheses (SA (2a)–(2b), Theorem 4.13, Proposition 4.14, Lemma 4.15). Their complete account (CA-I/II/III) supplies the healed-island size bound, the global stability quotient and the precise statement of the open problem (Proposition 8.12). Tadeusz Balaban's papers (CMP 119 (1988) 243; 122 (1989) 175 and 355; CMP 102 (1985) 277) are the source of the large-field regions, the region rules, the localised backgrounds and the healing; Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. Our `library/a3-derivative.md` (Codex §§1–6, Claude §§10–12) and `library/a3-close.md` (Claude) supply the localised background comparison used below, with their gates. Round 1 is `library/ag1-draft.md` (Claude).

Line references: **SA L** = `scratchpad/sa/ym4.tex`; **CA-II L** = `scratchpad/sa/ca_II.tex`; **CA-III L** = `scratchpad/sa/ca_III.tex`; **Y3 L** = `scratchpad/sa/YM3_I.tex`; **R1 L** = `library/ag1-draft.md`; **TP1 L** = `library/tp1-draft.md`; **IN1 L** = `library/in1-draft.md`. I read every cited range myself in this session, in bounded ranges. Quotations are kept short.

Status words, used inline: **[proved]** = proved here by hand from the stated inputs; **[input: NAME, owner]** = a statement another submanuscript must supply, stated exactly; **[outstanding]** = AG1's own statement, not proved; **[not provable as stated]** = a statement shown here to fail at the level of the rules or to lie beyond the available inputs, with the exact reason.

Notation clash. Round 1 called the threshold spread κ. SA's order of constants also has a κ (SA L19469; IN1 Part A). In this draft the threshold spread is **κ_T**, and κ always means SA's κ.

---

## 0. Summary

**Target.** Lemma AG-k₁ of TP1 (TP1 L483–487) in the weaker form (0.1*) that TP1 tolerates (Lemma 1.3):

  Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C e^{−ϖ_k},  ϖ_k ≥ c₀(log x_k)²,   (0.1*)

uniformly in the volume, the cutoff and the position.

**Task 1: (QL), two-run stability.**

1. *Round 1's first unchecked step is proved, and it was not the obstacle* (§6.6, Proposition 6.9) [proved]. A stored fluctuation value of level l is compared, between the two runs, by the background comparison at its own step, with decay e^{−δ·dist/ℓ_l} in level-l units. A level-i test reads it at a point that lies, by the nesting of the inner regions, at distance at least D_iℓ_i from the region where the step-l data differ. In level-l units this is D_iL^{i−l}. So the influence of the old value on the new test is at most C·e^{−δD_iL^{i−l}}. Under SA's read structure the propagation constant is 1 (no growth at all). If every level multiplied influence by a fixed factor Λ, the bound would be (2Λ)^{i−l}e^{−δD_iL^{i−l}}, still summable, since D_i(L − 1) ≥ δ^{−1}log(4Λ). Round 1 compared the old value with its own margin D_l, not with the distance at which it is read; that was the error.

2. *Round 1's (QL) is not provable from the rules and inputs as stated* [not provable as stated]. Two operations break it. Both are covered by SA's own second hypothesis, "no long cluster" (SA L23328), which round 1 dropped (R1 L422).
 - The **round recursion** of the collar and rim tests (SA L17321–17325, L17354–17360) grows a large-field region along any chain of bonds that fail the collar or rim test when examined. A chain entering the tile from outside makes the region of a core cell depend on the exterior, with no tested value near any threshold (Lemma 6.4).
 - The **background comparison** (SA Theorem 6(c), L9783–9789) needs a comparison region whose collar lies in a single layer of the sequence. A component of Ω_i^c that crosses the boundary of the agreement region cannot be excluded or included without crossing layers, so near it no decay is available (Lemma 6.3).
 
 Redesigns of the rounds were tried (§10.2, attacks T1, T2, T4), and they fail for an exact reason. The collar mean bound needs the boundary data to be smaller than the inner thresholds by a fixed factor. SA gets that factor from the greedy growth. A local rule gets it only if the conditional-mean operator contracts sup norms by 2/5 at the boundary, and no source gives that.

3. *The corrected statement (QL′) is proved* (Theorem 6.7) [proved, from (RS), (BGL), (R3)]. It restores SA's two hypotheses, stated on one run only (the local run): no window at a background-reading decision site, and no long cluster LC_i. LC_i is a crossing w-cluster of Ω_i^c, or of Z_i^{[0]} together with the *potential* collar and rim failures. The proof goes move by move through a step: plaquette and approximate fluctuation tests, Ω_i, gauge draws, the true background, the third test, the rounds, boxing, the class and stages of 𝐑, reference and frame draws, the three fates, and stored fields.

**Task 2: threshold robustness** (§5). [proved, as an implication, given the room conditions listed.] Every consumer of a threshold in LF1, NL1 and IN1 Part C reads the test either on its *fail side* or on its *pass side*.
 - On the fail side, a smooth test is bounded by the sharp indicator at the lower endpoint θ. All certificates, gains, the reserve, the drop-out majorant, Dep and (LT) keep their constants.
 - On the pass side, it is bounded by the sharp indicator at (1 + κ_T)θ. Every pass-side use has a fixed or polylogarithmic room factor, and κ_T = 1/4 fits inside each (Theorem 5.4, a list of 20 consumers).
 - The measure identity needs seven additions (MI-1)–(MI-7) (Lemma 5.2). The main ones: potential sites with their own uniforms, a single reading of each site, and smooth partitions of unity in place of idempotent indicators. With them the auxiliary uniforms integrate out exactly to the smooth-test kernels.

**Task 3** (§7, §8). Theorem F″ gives (0.1*) with ϖ_k = δ𝗇MŘ_k/512. Its inputs: (K)+(MI), (COV), (SM), (QL′), and the moment bound (MB+T), which is (MB) plus one new clause (TT). LC_i is paid by live cells through (MB), and, for its trigger part, by (TT). §8 writes AG-k₁* in TP1's form. TP1's Lemmas 6.5 and 6.6 then close with (6.3) replaced by (6.3*).

**First remaining Outstanding statement** (§10.1). It is **(TT), trigger tails**: a long chain of potential collar or rim failures, crossing the margin of a tile in the local run, must be paid in the true run. Every cell of such a chain lies near a live cell (paid by (MB)) or is a *deep trigger*: a small-field bond, two cells away from every large-field cell, at which the fluctuation exceeds the collar threshold. (TT) is the exponential-moment bound e^{−c_T p₀(g_i)²} per deep trigger, jointly with (MB). SA asserts it: "The price of such a cell is borne by the conditional law of the fluctuation field in its box" (SA L23328). It is a tail bound, not the density bound at which round 1's F3 stopped. Five attacks fail or stop, for the exact reasons in §10.2:
 - T1, single-pass tests: they need the conditional-mean operator to contract sup norms by 2/5 at the boundary, which no source gives. For the scalar Laplacian the constant is 1.
 - T2, triggers recorded as decisions or creations: deep triggers still need a tail, and near-boundary cuts break the mean bound.
 - T3, the bare Wilson stability quotient with the chessboard: its volume factor counts bare sites, L^{4k}(MŘ_k)⁴𝗇⁴ per tile.
 - T4, monotone sandwich runs: the rounds and boxing are not monotone, and no tile function can certify that the true run examined a chain.
 - T5, the conditional law in a box: it needs a lower bound on the probability that the inner tests pass in the box, uniformly in the outside field, and the constrained fluctuation Hessian has no maximum principle to give one.
 Lemma 10.1 reduces (TT) to a per-history bound (10.1) on one step's integral.

**Inputs owned by other submanuscripts** (§10): (K) [LF1(1)]; (COV) [LF1]; (RS) [LF1(2)]; (BGL) [BG1/PR1; checked conditional]; (R0)–(R3) [LF1(2)]; (LT) [LF1(3)]; (TT) [NL1 with LF1, new]; LG1(3) [C].

**Line count**: at the end of the file.

---

## 1. Statement

### 1.1 Objects (SA (2a), as read)

Fix the datum, a compatible torus and the run. Levels are j = 0, 1, …, K. The level-j lattice T^{(j)} has spacing ℓ_j := L^j a_K. A *level-j cell* is a cube of MŘ_j sites of T^{(j)} to a side, so its side is c_j := MŘ_jℓ_j (SA L17479: "a cell contains (MŘ_j)⁴" sites). Here Ř_j is "the smallest power of L that is not less than (log min_{i≤j} x_i)^r, with r ≥ 2" (SA L17334). Ř_j is non-increasing in j and Ř_j ≤ LŘ_{j+1} (SA L17334). The weight of a level-j cell is r_j := M⁴Ř_j⁵ (SA L17479); it is non-increasing in j. Partitions of all levels are nested, "because it is a power of L" (SA L17334).

A history h of level k carries, for each j ≤ k, the small-field regions Ω_j, Λ_j, the large-field region Z_j = Λ_j^c and the live region 𝒵_j ⊂ Z_j, "Z_k(h) with the components healed at step k removed" (SA L17477). Components are maximal connected unions of cells (cells adjacent when their closures meet). The three fates of a component in the class of 𝐑 are healed, island and drop-out (SA L17415–17431).

*Lineage regions* (SA L17479). For a component X of Z_k, live at level k or healed at step k, 𝖹_k(X) := X and, going down, 𝖹_j(X) := the union of all components live at level j contained in 𝖹_{j+1}(X). The lineage age of a component C live at level k is age_k(C) := k − j₀, j₀ the least level with 𝖹_{j₀}(C) ≠ ∅ (SA L17494, item (2)).

*Survival event* (SA L17477). For a level-n cell 𝔷 and n ≤ k' ≤ k, E^{(n)}_𝔷(k') := {𝔷 ⊂ 𝒵_i for every n ≤ i ≤ k'}; lv_k(𝔠) := E^{(k)}_𝔠(k).

*The age event of TP1.* 𝔏_k^{≥a}(c) := {some component C live at level k with C ∩ c ≠ ∅ has age_k(C) ≥ a}. TP1 L481 reads the age as "created at level ≤ k − a and never healed since"; SA orders the ages, label age ≤ lineage age ≤ seed age (SA L17494). Bounding the lineage-age event bounds what TP1 reads.

**Lemma 1.1 (anchor)** [proved; SA L23336 "Anchor"]. If C is live at level k and age_k(C) ≥ a, then there is a level-(k − a) cell 𝔷 ⊂ C with E^{(k−a)}_𝔷(k).

*Proof.* 𝖹_j(C) ⊂ 𝖹_{j+1}(C) for j < k, and 𝖹_k(C) = C. Since j₀ ≤ k − a and 𝖹_{j₀}(C) ≠ ∅, 𝖹_{k−a}(C) ⊇ 𝖹_{j₀}(C) ≠ ∅. It is a nonempty union of components live at level k − a, hence of level-(k − a) cells; let 𝔷 be one. For k − a ≤ i ≤ k, 𝔷 ⊂ 𝖹_i(C), a union of components live at level i, so 𝔷 ⊂ 𝒵_i; and 𝔷 ⊂ 𝖹_k(C) = C. ∎

### 1.2 The statements

**(0.1)** is TP1's (10.1) (TP1 L483–485): the same series bounded by C(log x_k)^C e^{−cp₀(g_k)}.

**(0.1*)** For a rate ϖ_k ≥ c₀(log x_k)², with C, c₀ independent of the volume, the cutoff, the position and the level, Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C e^{−ϖ_k}.

**Theorem AG (our form).** (0.1*) holds at every level k with x_k ≥ X_F, with ϖ_k = δ𝗇MŘ_k/512, as an implication from (K)+(MI), (COV), (SM), (RS), (BGL), (R0)–(R3), (LT), (TT) and LG1(3) (Theorem 7.4 with Theorem 6.7 and Lemma E.4). Status: [proved] as that implication; (TT) [outstanding, new input; §10.1].

### 1.3 The weaker rate suffices for TP1

**Lemma 1.3** [proved]. If (0.1*) holds at k = k₁, then TP1 Lemmas 6.5 and 6.6 hold as stated, and TP1(1)–(5) hold with (0.1*) in place of (0.1).

*Proof.* Written out in §8 (Proposition 8.2). In brief: TP1 reads (10.1) only through (6.3) (TP1 L377), and (6.3) is used only through (log x)^{C'}𝔄 → 0 and (log x)^{C'}𝔄^{1/2} → 0 for fixed C'. With 𝔄 ≤ C(log x)^{C}e^{−c₀(log(x/2))²} both hold. ∎

The rate p₀ of (0.1) is not reached: the chessboard charges per tile, and the charge per tile is polylogarithmic of degree r in log x_k (Remark 7.3).

---

## 2. What the sources say, and the diagnostic facts

### 2.1 Sussman–Alpoge, (2a)–(2b) and (4d)

- *Tests and regions of step t* (SA L17317–17334). Outside a margin of Y = 𝒵_{t−1}, the plaquette test χ_t(□) on V_t; its failures make P_t. The approximate fluctuation test χ'_{t−1}(□) = 𝟏{|V_{t−1}(𝓜^{t−1}U_{t,□}(V_t))^{−1} − 𝟏| < 2δ_{t−1}} at the bonds of □^{~2}; its failures make Q_t. "These sets determine Ω_t, the region on which U_t(𝐕) and 𝒜_k exist." The label's sequence "starts at Ω₀ = Ω₁^~ … and not at T_ℓ". Then the third test χ^{(t−1)}(□); its failures make R_t. With hulls and layers in level-t cells and the boxing map bx, Ω_t^c = Q_t'^{~2} ∪ P_t'^{~4} ∪ Ŷ^{~8}, Z^{[0]} = bx((Ω_t^c)^{~2} ∪ R_t'^~), Z^{[n+1]} = bx(Z^{[n]} ∪ (cells of the failures of round n)^~). The creation set 𝒲^∧_t is "the union of the hulls of every failure of the step: P_t', Q_t', R_t', the cells of the collar bonds that fail, and the rim cells that fail". With no creation, Φ_t(Y) = bx(Ŷ^{~10}).
- *Collar and rim* (SA L17348–17367). The stored part of 𝒜_{t−1} shifts the mean of the conditional Gaussian on Λ_t, 𝐦 = −C^{(k)}(Λ_t)Δ^{(k)}𝒜_k|_{Ω_t∖Λ_t}. "A recursion therefore keeps enlarging the region until, along its boundary, 𝒜_k satisfies two sharper tests": |𝒜_k| < δ_k/(4Θ₁) on the collar (stored bonds within ϖ_T of Λ_t, level-k units) and |𝒜_k| < θ_cδ_k on the rim (cells of Z_t touching Λ_t). "Every round examines bonds and cubes that no earlier round examined." The bound is |𝐦| ≤ C(Θ₁^{−1} + θ_ce^{−cϖ_T} + e^{−cMŘ_t})δ_k < ½θ_cδ_k when θ_cΘ₁ ≥ C, ϖ_T ≥ C and γ is small. It keeps the mean "well below the least threshold among the inner tests; that threshold is θ_cδ_k on bonds that cross ∂Λ_t, and δ_k further in".
- *What is local* (SA L17336–17344). "The tests χ_t and χ'_k are built from localised backgrounds. They depend on V_t, V_k only within O(1) test cubes." The third, collar and rim tests "depend on 𝒜_k = (1/i)log(V_k(V^bg_k)^{−1}), which is formed with the true averaged background on Ω_t." "Inside 𝐑, the tests are built from backgrounds localised in the component."
- *Ladder and room* (SA L17369–17396). Lemma 2.2: new tests imply old ones on supports. The factor 2 between χ^{(k)} and χ'_k "gives exactly the room needed".
- *Locality in the history* (SA L17449). "One cell exceeds the largest range of a bond test, of a pivot bond and of a collar (in the case of the collar, this is the floor M ≥ ϖ_T of (2e))"; "boxing depends on a single component only"; the class of 𝐑 "depends on the past … within the window (t_♭, t]".
- *Moves* (SA L17499–17514). A step is "a finite sequence of moves on states σ = (h, ξ) … given by positive kernels Π^{(o)} … such that Σ_oΠ^{(o)}(σ,·) has total mass one". Each move is a test, a map, a draw (gauge fixings, hypercubic frames, reference laws), or a deletion. The identities τ_h[ν₀] = ∫ν₀(dU)𝖪_h(U,·) and Σ_h𝖪_h(U,𝒱_k) = 1 hold (SA L17502–17503). *Passengers*: "the operation 𝐑 uses variables only in the components of its class" (SA L17508).
- *The class and the operation 𝐑* (SA L17575–17610). X is in the class if, for k_♭ ≤ i ≤ k, "X ∩ Z_i is a single component of Z_i and is small, that is, contained in a cube of O(1) level-i cells", and X is quiet and in quarantine. Stages integrate stored variables after "tests at the sharper threshold δ'_j … formed with backgrounds localised in X". The tree gauge, the test on B and the last-shell test follow, and then the reference law 𝔰_X, built with "the background localised in X" U_{k,X} and the cut-off χ(Λ^pr). "If one of the tests of (1)–(3) fails in a component, that component drops out."
- *Theorem 4.13, Proposition 4.14, Lemma 4.15* (SA L23258–23340), as in round 1 (R1 L81–83).
- *The localised comparison* (SA Theorem 6(c), L9783–9789). Let W be a μ-collared region: "Each part is a union of cubes of side μξ_{j_a} … the O(1) outermost layers of cubes of A_a, which form its collar, lie within the single layer j_a of the sequence", and part boundaries are separated. Then U|_W = (e^{iηf}U°_W)^w with ξ_y|f| ≤ C_με₁e^{−δ_W d_𝐁(y,W^c)}. "Two backgrounds whose sequences and whose data coincide on W differ there to this extent." The metric is d_𝐁(x,x') = inf_Γ[Σ_{j≥1}ξ_j^{−1}length(Γ ∩ (Ω_j∖Ω_{j+1})) + η^{−1}length(Γ∖Ω₁)] (SA L9602).

### 2.2 SA's two-run statement, read exactly

SA L23328: "Consider two runs with identical tile data. Assume that in the first run, up to some level J' ≤ k, two things hold in the tile. First, no tested scaled fluctuation value lies in a narrow window around its threshold … Second, no long cluster of cells of a level j ≤ J' that lie in Ω_j^c or carry a tested bond at which a lower threshold is passed by the scaled fluctuation field of the step (a trigger) appears. Then, at the end of step J', the two runs coincide in the inner layers of the tile." The windows are paid "under the conditional law of a tested fluctuation value". Triggers are paid thus: "Take a cell that has no large-field cell within two cells of it and at one of whose bonds a lower threshold is passed by the scaled fluctuation field of the step. The price of such a cell is borne by the conditional law of the fluctuation field in its box." On stored fluctuation fields: "The common data do not include the stored fluctuation fields … they are built from the averaged background, which is not local. Among the later moves, a single test of 𝐑 depends on them, and on those bonds that test is passed in every run."

So SA states two hypotheses, on one run only. Round 1 kept the first (in the uniform form, F2) and dropped the second (R1 L422: "SA's second hypothesis, no long cluster (SA L23328), is not used"). §6 shows that the second hypothesis is needed, for two separate reasons (Lemmas 6.3 and 6.4), and that its trigger part needs a tail bound of its own (§10.1).

### 2.3 The complete account and three dimensions

As round 1 (R1 L85–99): Proposition 8.12 is "Proof outstanding" (CA-II L127294–127316) and in CA-III's list (L111189–111192). The healed part is local: healed islands have "at most 100 cells to a side" (CA-II L113209–113210). The global quotient is ν̃(𝒮) ≤ exp(𝖡N⁴ − inf_𝒮Θ) (CA-II L126262–126357). In 3D the creation union bound converges; in 4D it diverges (TP1 Lemma 3.9).

### 2.4 Three diagnostic facts (round 1, kept)

**Lemma 2.1 (one cell against a global quotient)** [proved]. If ν̃(𝒮) ≤ exp(β𝒱 − inf_𝒮Θ) for all events 𝒮 and inf_{𝒮_𝔠}Θ = μ, then ν̃(𝒮_𝔠) ≤ e^{β𝒱−μ}, which is < 1 only if μ > β𝒱. *Proof.* Substitution. ∎

**Lemma 2.2 (a first moment gives a density only)** [proved]. If Θ ≥ 0, Ee^Θ ≤ e^{β𝒱} and Σ_𝔠𝟏_{E_𝔠} ≤ Θ/μ over 𝒩_c cells, then 𝒩_c^{−1}Σ_𝔠ν̃(E_𝔠) ≤ β𝒱/(μ𝒩_c). With μ = μ₀(a + 1) the bound decays like 1/a, and Σ_aL^{8a}(bound) diverges. *Proof.* Jensen: EΘ ≤ log Ee^Θ ≤ β𝒱; sum and take expectations. ∎

**Lemma 2.3 (TP1's (H) is not implied by the rules)** [proved from SA L23265, L17325]. A component Y live at level i − 1 that contains a creation of step i − 1 has a live successor at level i, whatever the level-i tests do. *Proof.* SA L23265: "𝐑 touches a component only if no creation has occurred in it during the last 𝖭_k steps." The successor contains Ŷ because Ω_i^c ⊇ Ŷ^{~8} and Z_i ⊇ Z^{[0]} ⊇ (Ω_i^c)^{~2} for every outcome (SA L17325). ∎

So TP1's Lemma 10.1 cannot be applied as stated. The replacement is the volume inequality of §4 together with the chessboard of §7.

---

## 3. The model and the inputs

### 3.1 The kernel representation

**(K)** [input: LF1(1); SA L17499–17514, L23328; `ref-73.md` §2]. There is a finite index set 𝒯 of *potential decision sites* τ, fixed before the run, each with a level j(τ), a location (a site of some T^{(i)}, never on a bond-bisecting plane) and a position in the order of moves of step j(τ). Let ω = (u_τ)_{τ∈𝒯} be i.i.d. uniform on [0,1] with law λ, independent of the bare field U ~ μ_{K,ℓ,β}. The history of level k is a measurable function h = H_k(U, ω), and ν̃ is the image of μ ⊗ λ. Step j reads only the u_τ with j(τ) ≤ j, in the order of moves. Write ℱ_j := σ(U, u_τ : j(τ) ≤ j). A location carries at most N_τ sites per level (N_τ is a constant of the construction). The draws of SA's moves (gauge fixings, frames, reference laws) are measurable transforms of their own uniforms. The additions that smooth tests need are (MI-1)–(MI-7) of §5.2.

### 3.2 Covariance

**(COV)** [input: owner LF1; SA L23298 (iii); CA-III L111428 lists "translation covariance of the label histories" as stated with proof incomplete]. For θ a translation by a multiple of the side of a level-k cell, or a reflection in a bond-bisecting plane on a level-k cell boundary, H_k(θU, θω) = θH_k(U, ω), θ acting on ω by moving locations. Such reflections preserve every block lattice and every cell partition up to level k (R1 L139).

### 3.3 The moment bound

**(MB)** [input: owner LF1; derived in Lemma E.4 from (LT) and (R0)–(R2)]. There is C_D, and for every dial c_a ≥ 1 a threshold X₁(c_a), such that for x_k ≥ X₁ the following holds. Let 𝔷₁, …, 𝔷_m be cells of levels n_i ≤ k and k_i ∈ [n_i, k], such that for every level j the level-j ancestors of those 𝔷_i with n_i ≤ j ≤ k_i are pairwise distinct. Then

  ν̃(∩_{i≤m} E^{(n_i)}_{𝔷_i}(k_i)) ≤ exp( B_k|𝕋^{(k)}| + C_Dm − 2c_a Σ_i Σ_{j=n_i}^{k_i} r_j ),   (3.1)

with |𝕋^{(k)}| the number of sites of T^{(k)} and B_k ≤ C_B(1 + log x_k).

This is round 1's (3.1) with the charge Σ_j r_j in place of r_k(k_i − n_i + 1), and with distinctness asked only among the cells designated at each level. Both changes are what Lemma E.4(b) actually uses. Since r_j ≥ r_k for j ≤ k, round 1's form follows. *Which run*: the run stopped at level k; runs over one bare datum give level-k events the same mass (CA-II L126214–126220; SA L23298), so this is TP1's law P^{(k)}.

### 3.4 Tiles

Fix 𝗇, a power of L, with 𝗇 ≥ 16 and 𝗇 ≥ 16m₀C_L (m₀ of (6.2), C_L of Lemma 6.1). A *tiling* of level k is a partition of the torus into cubes of 𝗇⁴ level-k cells whose faces lie in bond-bisecting planes on level-k cell boundaries (SA L23315), translated by a multiple of the cell side. It exists when there are at least 2𝗇 level-k cells per axis, and then the number of tiles per axis is even. 𝒩 is the number of tiles and V_T := 𝗇⁴(MŘ_k)⁴ the number of sites of T^{(k)} per tile, so |𝕋^{(k)}| = 𝒩V_T. The *core* of a tile is the concentric cube of side (3/4)𝗇 cells; a cell of level ≤ k is *deep* if the level-k cell containing it lies in the core. *Tile data* of β: the bare links of the closed tile and the u_τ located in β. θ_γ maps the reference tile to tile γ (a composition of face reflections).

### 3.5 The chessboard estimate with auxiliary variables (round 1, kept)

**Lemma 3.1** [proved from LG1(3)]. Let f_γ (γ a tile) be bounded nonnegative measurable functions of the tile data of γ, and ‖f‖_ch := (E_{μ⊗λ}Π_γθ_γf)^{1/𝒩} for f a function of the reference tile data. Then E_{μ⊗λ}Π_γf_γ ≤ Π_γ‖θ_γ^{−1}f_γ‖_ch.

*Proof.* (i) The families ω_γ := (u_τ)_{τ located in γ} are independent for distinct γ and independent of U. By Fubini, E_{μ⊗λ}Π_γf_γ = E_μΠ_γf̄_γ(U), f̄_γ := ∫f_γ dλ(ω_γ), a bounded nonnegative function of the links of the closed tile γ; λ is invariant under relabelling by θ_γ, so (θ_γf)‾ = θ_γf̄, and the same holds for the norms. (ii) Replace f̄_γ by f̄_γ + ε. (iii) LG1(3) (assembly L153, [C]; SA (AM6) L2898–2905) gives E_μΠ_γ(f̄_γ + ε) ≤ Π_γ(E_μΠ_{γ'}θ_{γ'}θ_γ^{−1}(f̄_γ + ε))^{1/𝒩}. (iv) Let ε ↓ 0: both sides are polynomials in ε with nonnegative coefficients. ∎

**Lemma 3.2 (dilution)** [proved]. If f ∈ [0,1], Π_γθ_γf ≤ 𝟏_𝔼 and ν̃(𝔼) ≤ η^𝒩exp(B_k|𝕋^{(k)}| + 𝒩(C' − μ)), then ‖f‖_ch ≤ η·exp(B_kV_T + C' − μ). *Proof.* The 𝒩-th root, with |𝕋^{(k)}| = 𝒩V_T. ∎

**Lemma 3.3 (small tori)** [proved]. If no tiling exists, |𝕋^{(k)}| < 16V_T, and every bound of §7 holds with B_kV_T replaced by 16B_kV_T, by applying (3.1) directly to the event, with no chessboard and no locality. ∎

### 3.6 The trigger clause

Let θ_col := 1/(4Θ₁) (the collar fraction, SA L17356). For a level i ≥ 1, a bond b of level i − 1 and its level-i cell 𝔡(b), let 𝔡(b)^{+2} be 𝔡(b) with two layers of level-i cells. Define the *deep trigger* event

  Trig_i(b) := {b ∈ Λ_i^{pre}, no cell of Z_i^{pre} meets 𝔡(b)^{+2}, and |𝒜_{i−1}(b)| > θ_colδ_{i−1}},

where Z_i^{pre} is the large-field region of step i after the rounds and before 𝐑, and Λ_i^{pre} its complement in Ω_i.

**(TT)** [outstanding; new input, owners NL1 (small-field tails) and LF1 ((LT)); SA L23328 asserts it]. There are c_T > 0 and C_T such that the following holds. Let the designations be as in (MB). Let 𝔅 be a finite set of bonds, each of a level i(b) − 1, whose cells 𝔡(b) are distinct and whose neighbourhoods 𝔡(b)^{+2} are pairwise disjoint among bonds of equal level. Suppose each 𝔡(b)^{+2} is disjoint from the level-i(b) and level-(i(b) − 1) ancestors of the designated cells. Then

  ν̃(∩_iE^{(n_i)}_{𝔷_i}(k_i) ∩ ∩_{b∈𝔅}Trig_{i(b)}(b)) ≤ exp( B_k|𝕋^{(k)}| + C_Dm + C_T|𝔅| − 2c_aΣ_iΣ_{j=n_i}^{k_i}r_j − c_TΣ_{b∈𝔅}p₀(g_{i(b)})² ).   (3.2)

(MB) is the case 𝔅 = ∅. (MB+T) denotes (3.1) and (3.2) together. Why (TT) is plausible and what it needs: §10.1.

---

## 4. Attack E (round 1, kept): the healing rule gives "volumes are paid by events", and (MB)

TP1's (H) asked for a fresh event at every level of survival (not implied by the rules, Lemma 2.3). The healing rule gives something weaker and true: a lineage may survive without events, but only for O(Ř + log size) levels per event, and the free evolution shrinks it meanwhile. Summed with the weights r_j, this is SA's inequality "volumes are paid by events" (SA L23267–23274). I prove it here from three rule properties, prove the first of them for SA's free evolution, and derive (MB) from it and the lineage-trace bound (LT).

### 4.1 The rule properties

Fix a component X (live at level k, or healed at a step ≤ k) and its lineage. Its *nodes* are the pairs (j, C), C a component of 𝖹_j(X) live at level j. For a node (j, C): pred(j, C) := the nodes at level j − 1 contained in C (SA L23274); Act_{j−1} := the components live at level j − 1 on which 𝐑 of level j − 1 has acted although they stay live (SA L23274); the creations (j, W) are the components of the step-j creation set lying in C, with tree length d'_j(W) in level-j cells (SA L17479); and

  e(j, C) := (|pred(j, C)| − 1)^+ + |pred(j, C) ∩ Act_{j−1}| + Σ_{W⊂C} (d'_j(W) + 1)   (SA L23274).

A node is an *event node* if e(j, C) ≥ 1 and *free* otherwise. Put v(j, C) := r_j|C|_j.

**(R0)** [input: LF1(2), region rules; SA L17479, L23274]. Each node below the top level of the lineage is in pred of exactly one node (its successor). If pred(j, C) = ∅, then C contains a creation of step j.

**(R1)** [input: LF1(2), the per-component reading of SA L17334; numerical part proved in Lemma E.2]. There are A and λ ≤ 1/6 such that for every node,

  v(j, C) ≤ λ Σ_{P∈pred(j,C)} v(P) + A r_j (|pred(j, C)| + Σ_W (d'_j(W) + 1)).   (4.1)

**(R2)** [input: LF1(2), the healing time; SA L23274: a component that "has stayed small over Ř_j + 1 levels without any event … belongs to the class of 𝐑"; SA L23265: 𝐑 acts only after 𝖭_k creation-free steps; CA's age lemma, CA-II L126270–126282, eq. 8.12:eq-volume-ranges-d, stated with proof incomplete, CA-III L111431]. There is C_N such that every maximal chain of free nodes (j_s, C_0), (j_s + 1, C_1), … whose first node has predecessor P has length ℓ ≤ C_N(Ř_{j_s} + log(2 + |P|_{j_s−1})).

*Why (R2) is the chain form of the age lemma.* CA's per-seed allowance is 𝔞(Z) ≤ 2 log_L(d'(Z) + 1) + 2R_{j(Z)} + n₁ + C_S + 4: a log of the size plus a multiple of the radius, the same shape as (R2). A free node has exactly one predecessor, no creation and a predecessor not acted on by 𝐑 (e = 0 and (R0)); along a free chain the component evolves freely, and the chain ends when 𝐑 acts (the next node is then an event node, its predecessor being in Act, or the component is healed and has no successor in the lineage).

### 4.2 Proofs

**Lemma E.1 (hull count)** [proved]. Let fine cells be the unit cubes of ℤ⁴ and coarse cells the aligned cubes of ρ⁴ fine cells, ρ ≥ 1. Let Y be a connected set (closures-meet adjacency) of n fine cells, and Ŷ the set of coarse cells meeting Y. Then |Ŷ| ≤ 81(1 + 2n/ρ).

*Proof.* Choose a maximal subset S' ⊂ Ŷ of coarse cells with pairwise disjoint closures. Every coarse cell of Ŷ has closure meeting that of some cell of S', and a coarse cell has 3⁴ = 81 coarse cells (itself included) with closures meeting its own; so |Ŷ| ≤ 81|S'|. If |S'| = 1 we are done. Otherwise pick y_Q ∈ Y ∩ Q for each Q ∈ S'. Two fine cells in coarse cells with disjoint closures are at sup-distance ≥ ρ + 1. Let t := ⌊ρ/2⌋ and B_Q the fine cells at sup-distance ≤ t from y_Q; these sets are pairwise disjoint, since 2t < ρ + 1. Y is connected and contains a cell at distance > t from y_Q (any y_{Q'}, Q' ≠ Q), so a path in Y from y_Q to it, whose consecutive cells are at sup-distance ≤ 1, contains a cell at each distance 0, 1, …, t from y_Q; hence |Y ∩ B_Q| ≥ t + 1 ≥ ρ/2. Summing, n ≥ |S'|ρ/2, so |Ŷ| ≤ 81·2n/ρ. ∎

**Lemma E.2 ((R1) for SA's free evolution)** [proved from the reading below]. *Reading of SA L17317–17334, per component.* Each node (j, C) satisfies C ⊂ bx(∪_{P∈pred(j,C)} P̂^{~10} ∪ ∪_{W⊂C} W^{~c_W}), where hulls and layers are taken in level-j cells, c_W is the O(1) of SA L17334, and the boxing map bx replaces each component contained in a cube of b₁ cells by its bounding box (SA L17317). Then (4.1) holds with λ = 162·21⁴/L and A := 81·21⁴ + (2c_W + 1)⁴ + b₁⁴; in particular λ ≤ 1/6 for L ≥ L₁ := 972·21⁴.

*Proof.* Let ρ_j be the ratio of the side of a level-j cell to that of a level-(j − 1) cell. The side of a level-j cell is MŘ_jL^ja_K, and Ř_{j−1} ∈ {Ř_j, LŘ_j} (SA L17334: Ř non-increasing, Ř_{j−1} ≤ LŘ_j). So ρ_j = L (a *normal* step, r_j = r_{j−1}) or ρ_j = 1 (a *drop* step, r_j = L^{−5}r_{j−1}). By Lemma E.1 with ρ = ρ_j, |P̂| ≤ 81(1 + 2|P|/ρ_j). A 10-layer enlargement multiplies the number of cells by at most 21⁴ (each cell's 10-neighbourhood has 21⁴ cells), and W^{~c_W} has at most (2c_W + 1)⁴|W| ≤ (2c_W + 1)⁴(d'_j(W) + 1) cells (a connected set of |W| cells has a spanning tree with |W| − 1 edges, so d'_j(W) ≥ |W| − 1). Boxing replaces a component of diameter ≤ b₁ by a box of at most b₁⁴ cells, so |bx(B)| ≤ |B| + b₁⁴·#components(B), and the union has at most |pred| + #W components. Hence

  |C|_j ≤ (162·21⁴/ρ_j) Σ_P |P|_{j−1} + (81·21⁴ + b₁⁴)|pred| + ((2c_W + 1)⁴ + b₁⁴) Σ_W (d'_j(W) + 1).

Multiply by r_j. At a normal step r_j/ρ_j = r_{j−1}/L. At a drop step r_j/ρ_j = r_{j−1}L^{−5} ≤ r_{j−1}/L. Either way the first term is ≤ (162·21⁴/L) Σ_P v(P). ∎

*Remark.* The drop steps are why the weighted form matters: at a drop the cells do not coarsen, the count grows by up to 21⁴, but the weight falls by L⁵.

**Lemma E.3 (volumes are paid by events)** [proved from (R0)–(R2)]. With c_G := (60/47)(4A + C₁), C₁ := (6A/5)C_N(1 + log(2 + 12AC_N)),

  Σ_{(j,C)} r_j|C|_j ≤ c_G Σ_{(j,C)} r_j(Ř_j + 1) e(j, C),   (4.2)

both sums over the nodes of the lineage. This is SA's inequality (SA L23267–23274, "Volumes are paid by events"), with Ř_j + 1 in place of Ř_j.

*Proof.* Let V be the left side (a finite sum), 𝔈 the event nodes. A free node has e = 0, so (|pred| − 1)^+ = 0 and no creation; by (R0), pred ≠ ∅; so it has exactly one predecessor. Group the free nodes into maximal chains of consecutive free nodes. The predecessor P of the first node of a chain is not free (else the chain would extend), so P ∈ 𝔈; and by (R0) each node is the predecessor of at most one node, so at most one chain starts above each event node.

*A chain.* Let the chain have nodes ν_0, …, ν_{ℓ−1} at levels j_s, …, j_s + ℓ − 1, with predecessor P at level j_P = j_s − 1. By (4.1) with |pred| = 1 and no creation, and r non-increasing, v(ν_t) ≤ λv(ν_{t−1}) + A r_{j_s} (ν_{−1} := P), so v(ν_t) ≤ λ^{t+1}v(P) + A r_{j_s}/(1 − λ). Summing, with λ ≤ 1/6,

  Σ_t v(ν_t) ≤ (λ/(1 − λ))v(P) + (6/5)A r_{j_s} ℓ ≤ v(P)/5 + (6/5)AC_N r_{j_s}(Ř_{j_s} + log(2 + |P|)),

by (R2). For y ≥ 0 and 0 < ε < ½, log(2 + y) ≤ εy + log(2 + 1/ε) (the difference εy + log(2 + 1/ε) − log(2 + y) is ≥ 0 at y = 0, decreases until y = 1/ε − 2 and is 1 − 2ε > 0 there, then increases). Take ε = 1/(12AC_N); since r_{j_s}|P| ≤ r_{j_P}|P| = v(P), the term (6/5)AC_N r_{j_s}ε|P| is ≤ v(P)/10. With r_{j_s} ≤ r_{j_P}, Ř_{j_s} ≤ Ř_{j_P}:

  Σ_{chain} v ≤ (3/10)v(P) + C₁ r_{j_P}(Ř_{j_P} + 1).

*Event nodes.* For P ∈ 𝔈, e(P) ≥ 1, |pred(P)| ≤ (|pred(P)| − 1)^+ + 1 ≤ 2e(P), and Σ_W(d' + 1) ≤ e(P); so (4.1) gives v(P) ≤ λ Σ_{pred(P)} v + 3A r_{j_P}e(P). Since each node is in at most one pred, Σ_{P∈𝔈} Σ_{pred(P)} v ≤ V, and

  Σ_𝔈 v ≤ λV + 3A Σ_𝔈 r e.

*Sum.* V = Σ_𝔈 v + Σ_chains Σ v ≤ (13/10)Σ_𝔈 v + C₁ Σ_𝔈 r(Ř + 1) ≤ (13/10)λV + (39/10)A Σ_𝔈 r e + C₁ Σ_𝔈 r(Ř + 1)e, using e ≥ 1 on 𝔈. Since (13/10)λ ≤ 13/60, V ≤ (60/47)(4A + C₁) Σ_𝔈 r(Ř + 1)e, and free nodes contribute 0 to the right side of (4.2). ∎

**(LT)** [input: LF1(3) in lineage-trace form, owner LF1, ⟦LF-mass⟧]. For a lineage 𝔩 define its event cost

  EC(𝔩) := Σ_{creations (j,W)∈𝔩} p₀(g_j)(d'_j(W) + 1) + Σ_{(j,C)∈𝔩} p₀(g_{j−1}) |pred(j, C) ∩ Act_{j−1}|.

For a finite set 𝒟 of cells of levels ≤ k, let 𝔐_𝒟(h) be the set of lineages of the components live at level k together with the lineages of components healed at a step ≤ k whose lineage regions contain a cell of 𝒟. Then

  E_ν̃ exp(¼ Σ_{𝔩∈𝔐_𝒟} EC(𝔩)) ≤ exp(B_k|𝕋^{(k)}| + C_D|𝒟|).   (4.3)

*Sources.* SA's masses by lineage traces: e^{−E_(k)} Σ_h 𝗍(h) ≤ e^{C|𝕋^{(k)}|} Π_𝔩 wt(𝔩), wt(𝔩) = exp[C_chg Vol_k − Dep_k − Σ_{(j,W)} 2p₀(g_j) − Σ_j |Act_j|p₀(g_j)] (SA L23280–23286), the rooted sum of wt over traces (SA L23286–23292), and the floor, which gives the exponent B_k per site (CA-II L126262–126268). These cover the lineages live at level k. For a designated cell whose lineage heals at a step ≤ k, SA asserts that "the lineage of that component pays for the cell" (SA L23328), and CA proves an annealed bound on a healed island containing a given cell, K_H w(𝒮) e^{−(3/2)p₀(g_k)} (CA-II L113200–113235, eq. 8.9:eq-healed-old-region-9 at L113228), from the inputs of its large-field block bound. (4.3) is these statements in one exponential moment. I have not checked that SA's rooted sum leaves the fraction ¼ of EC; the dial 𝗐 of SA L23292 is the device for it.

**Lemma E.4 ((MB) from (LT))** [proved from (LT), (R0)–(R2)]. Let X₁(c_a) be such that 4c_ac_G r_i(Ř_i + 1) ≤ ¼p₀(g_i) whenever x_i ≥ X₁ (possible since r_iŘ_i = M⁴Ř_i⁶ has degree 6r < 𝔭₀ in log x_i; SA L23286 states r_jŘ_j ≪ p₀(g_j)). If x_k ≥ X₁, then (MB) holds.

*Proof.* (a) *Volume against cost.* For a lineage 𝔩 put Vol(𝔩) := Σ_{(j,C)∈𝔩} r_j|C|_j. By (4.2), Vol(𝔩) ≤ c_G Σ r_j(Ř_j + 1)e(j, C). Split e. *Merges:* the nodes form a tree (each node has at most one successor, (R0)); assign to each node with |pred| = p ≥ 2 the leftmost leaves of the subtrees of its 2nd, …, p-th predecessors (any fixed order). Each leaf is assigned at most once (the node where its leftmost path joins as a non-first child), and leaves lie below the node they are assigned to; since r_j(Ř_j + 1) is non-increasing in j, Σ r_j(Ř_j + 1)(|pred| − 1)^+ ≤ Σ_{leaves (i,C')} r_i(Ř_i + 1). A leaf has pred = ∅, so contains a creation by (R0): the leaf sum is ≤ Σ_{(i,W)} r_i(Ř_i + 1)(d'_i(W) + 1). *Act:* r_j(Ř_j + 1)|pred ∩ Act_{j−1}| ≤ r_{j−1}(Ř_{j−1} + 1)|pred ∩ Act_{j−1}|. *Creations:* as they stand. So

  Σ r(Ř + 1)e ≤ 2 Σ_{(j,W)} r_j(Ř_j + 1)(d'_j(W) + 1) + Σ_{(j,C)} r_{j−1}(Ř_{j−1} + 1)|pred ∩ Act_{j−1}|.

All levels in a lineage are ≤ k, so x_i ≥ x_k ≥ X₁, and the choice of X₁ gives 2c_a Vol(𝔩) ≤ ¼EC(𝔩).

(b) *The event.* Let 𝒟 = {𝔷₁, …, 𝔷_m} be as in (MB), and suppose ∩_i E^{(n_i)}_{𝔷_i}(k_i). Fix i and n_i ≤ j ≤ k_i. Since partitions are nested, 𝔷_i lies in exactly one level-j cell, and 𝔷_i ⊂ 𝒵_j forces that cell into 𝒵_j (𝒵_j is a union of level-j cells). That cell lies in a component live at level j. Following successors, this component lies in the lineage of a component live at level k or healed at a step ≤ k; that lineage contains 𝔷_i, so it is in 𝔐_𝒟, and its node at level j contains the cell. By hypothesis the level-j cells so obtained are pairwise distinct for the i with n_i ≤ j ≤ k_i. Each is counted once in Σ_{𝔩}Vol(𝔩) at level j, with weight r_j. So Σ_{𝔩∈𝔐_𝒟} Vol(𝔩) ≥ Σ_i Σ_{j=n_i}^{k_i} r_j.

(c) *Markov.* With S := Σ_iΣ_{j=n_i}^{k_i}r_j: ν̃(∩_i E_i) ≤ e^{−2c_aS} E exp(2c_a Σ_{𝔐_𝒟} Vol) ≤ e^{−2c_aS} E exp(¼Σ_{𝔐_𝒟} EC) ≤ (3.1). ∎

*Remark (TT).* The same Markov step gives (3.2) once (4.3) is strengthened. The strengthening adds c_T p₀(g_{i(b)})² for every b ∈ 𝔅 on Trig_{i(b)}(b) to the exponent on the left, with C_T|𝔅| added on the right. That strengthening is (TT) (§10.1). Lemma E.4 itself does not use it.

### 4.3 Where Attack E stops

Attack E proves (4.2) from (R0)–(R2) and (MB) from (LT). It does not prove: (LT), which is LF1(3) (⟦LF-mass⟧, already open in the assembly) in lineage-trace form; the per-component reading of SA L17334 used in Lemma E.2; and (R2), which is the chain form of CA's age lemma and SA's "class of 𝐑" sentence. A proof of (R2) from the rules needs the definition of the class of 𝐑 and the count of drop steps: in ℓ consecutive levels there are at most 2 + r log_L(1 + log(1 + B_♯ℓ)) drops (Ř_{j}/Ř_{j+ℓ} ≤ L(1 + log(1 + B_♯ℓ))^r by IN1(3)), each multiplying the size by at most 162·21⁴ + A, so (R2) holds up to a factor of order log log ℓ if the class of 𝐑 contains every component that has had at most A/(1 − λ) + 1 cells for Ř_j + 1 creation-free levels. That factor would change c_G by a log log factor, harmless against p₀. I record (R2) as an input; it belongs to LF1(2).

**(R3)** [input: LF1(2); SA L17575; CA-II L113209–113210]. The class of 𝐑 at level t contains only components X with X ∩ Z_i contained in a cube of C_R level-i cells for t_♭ ≤ i ≤ t ("small, that is, contained in a cube of O(1) level-i cells", SA L17575). Hence 𝐑 never acts on a component of Z_t^{pre} whose diameter exceeds C_R cells. CA records the bound "at most 100 cells to a side" for healed components; C_R is that O(1). Creation cells of step t are live at level t (SA L23265: "𝒲^∧_k ⊂ 𝒵_k").

---

## 5. Smooth tests and threshold robustness (Task 2)

### 5.1 The construction (SM)

Fix **κ_T := 1/4**. Let ζ(t) := 1 for t ≤ 1, ζ(t) := 1 − (t − 1)/κ_T for 1 ≤ t ≤ 1 + κ_T, ζ(t) := 0 for t ≥ 1 + κ_T, and ζ(∞) := 0. ζ is non-increasing and Lipschitz with constant 1/κ_T = 4.

Every test of SA's construction is "the indicator function of the set where all objects occurring in it are defined and where its inequalities hold" (SA L17346). Write a test τ as a finite family of inequalities q_ι < θ_ι, q_ι ≥ 0. Put q_τ := max_ι q_ι/θ_ι, with q_τ := ∞ where some object read by τ is undefined, and θ_τ := 1 after this normalisation.

**(SM)** [design, owner LF1]. Each test τ (every test of SA (2a)–(2d), including the plaquette, approximate fluctuation, third, collar and rim tests, the tests of the stages of 𝐑, the test on B, the last-shell test and the test χ_{k,Λ}) is replaced by the two-outcome kernel

  pass with weight p_τ := ζ(q_τ/θ_τ),  fail with weight 1 − p_τ,

decided in the kernel representation by its own uniform: τ passes iff u_τ < p_τ. Cut-offs that are factors of a draw's density are not tests and are unchanged. Examples are χ(Λ^pr) inside 𝔰_X (SA L17604) and the smooth strip cut-off ϑ_co (SA L17526), the latter apart from item 17 of §5.4.

*Random thresholds.* For u ∈ [0,1) and t ∈ [0,∞], u < ζ(t) ⟺ t < 1 + κ_T(1 − u). Indeed: for t ≤ 1 both sides hold (u < 1); for t ≥ 1 + κ_T both fail; for 1 ≤ t ≤ 1 + κ_T, u < 1 − (t − 1)/κ_T ⟺ t < 1 + κ_T(1 − u). So τ is the sharp test 𝟏{q_τ < θ_τs_τ} with the threshold factor s_τ := 1 + κ_T(1 − u_τ), uniform on [1, 1 + κ_T] and independent of everything read before τ. [proved]

### 5.2 What the measure identity needs

The auxiliary uniforms must integrate out to exactly the kernels that the smooth tests define. Seven additions to (K) make this so.

- **(MI-1) Potential sites.** The set 𝒯 of potential test sites is fixed before the run, as a function of the lattices and the cell partitions only. Each site has its own uniform. The draws (gauge fixings, frames, reference laws) use further uniforms, disjoint from those of the tests.
- **(MI-2) One reading.** Along every run, every potential site is decided at most once. In SA's rounds this is "Every round examines bonds and cubes that no earlier round examined" (SA L17360). A test that SA "carries" to later steps (for example, the step-t test cube that "serves also as a test cube of the density of level t, carrying the same background and the same threshold", SA L17396) is the *same* site with the *same* uniform. It is never re-decided.
- **(MI-3) Order.** Which site comes next, and its tested value, are measurable functions of U and of the uniforms already read.
- **(MI-4) Image law.** For every history h of level k and every U, λ{ω : H_k(U, ω) = h} = Π_{τ passed in h} p_τ(U) · Π_{τ failed in h}(1 − p_τ(U)) · (draw factors). The products run over the sites visited along h and are evaluated along h. This is SA's history kernel 𝖪_h (SA L17499–17503) with tests as two-outcome kernels.
- **(MI-5) Partition of unity.** Σ_h 𝖪_h(U, 𝒱_k) = 1 for every U (SA L17503). The proof uses only p + (1 − p) = 1 at each test and mass one at each draw. It never uses idempotence 𝟏² = 𝟏 or 𝟏(1 − 𝟏) = 0.
- **(MI-6) Covariance of labels.** The labelling of potential sites commutes with the maps θ of (COV), so λ is invariant under relabelling (used in Lemma 3.1).
- **(MI-7) Sources and positivity.** The sourced densities use the same kernels with ν₀ = ρ^w₀dU (SA L17508). For real inputs every weight is nonnegative, since 0 ≤ p ≤ 1.

**Lemma 5.2** [proved from (MI-1)–(MI-3)]. (MI-4) and (MI-5) hold. For every site τ, P(τ passes | U, the uniforms read before τ) = p_τ on the event that τ is visited.

*Proof.* Induction over the finite sequence of moves. Suppose the run has reached site τ, with data 𝒢 = (U, uniforms read so far). By (MI-1) and (MI-2), u_τ has not been read and is independent of 𝒢. By (MI-3), p_τ is 𝒢-measurable. So P(u_τ < p_τ | 𝒢) = p_τ. Multiply along the history: the probability of the outcome string of h, given U, is the product of the conditional probabilities. That gives (MI-4), with the draws contributing their own conditional laws. Summing over the outcomes of the last move gives p + (1 − p) = 1 at a test and total mass one at a draw; induct backwards to get (MI-5). ∎

*What does not survive.* An argument that uses χ² = χ, or that a single test is decided twice with the same answer, has no smooth analogue. The places where SA reuses a test are carried tests (MI-2) and the frame sum, where a_r + b_r = 𝗆 holds for every frame (SA L17585). Both survive: the first is the same site, and the second is p + (1 − p) = 1 inside one gauge-fixed measure. I found no use of idempotence in SA L17317–17610.

### 5.3 The sandwich

**Lemma 5.3** [proved]. For q ∈ [0, ∞] and θ > 0:

  𝟏{q < θ} ≤ ζ(q/θ) ≤ 𝟏{q < (1 + κ_T)θ},  𝟏{q ≥ (1 + κ_T)θ} ≤ 1 − ζ(q/θ) ≤ 𝟏{q > θ}.

*Proof.* ζ = 1 on [0, 1], ζ ∈ [0, 1], and ζ = 0 on [1 + κ_T, ∞]. The second chain is 1 minus the first. ∎

*Consequence.* On the support of a smooth-test term (MI-4), every passed test has q_τ < (1 + κ_T)θ_τ and every failed test has q_τ > θ_τ. A bound proved for the sharp construction that reads tests only through
 (F) failed ⇒ q ≥ θ, and
 (P) passed ⇒ q < θ (as a smallness bound on the support),
holds for (SM) once each (P)-use is re-proved with (1 + κ_T)θ; (F)-uses need no change. In SA's construction identities of the form "the old test equals 1 on the support of the new tests" are a third kind:
 (I) passed new tests ⇒ q_old < θ_old.
They need the implication with the new thresholds multiplied by 1 + κ_T and the old threshold at its lower end, since ζ_old = 1 exactly when q_old ≤ θ_old.

### 5.4 The consumers

**Theorem 5.4 (threshold robustness)** [proved, as an implication from the cited consumers' own proofs and the room conditions (5.1)–(5.6)]. Every bound of LF1, NL1 and IN1 Part C that reads a test threshold holds for (SM) with κ_T = 1/4. The consumers are listed below, each with its type (F), (P) or (I), the argument, and the room it needs. "Same constants" means that the proof is unchanged.

1. **(F) C3 certificates**, IN1 Lemma C.3(i)–(iv) (IN1 L482–492), from (I-11)(a)–(d). Each is a contrapositive: failure, including non-existence, forces a lower bound on a bare action share, a stored Gaussian exponent or an action outside the floor. A failed smooth test has q > θ, which is failure of the sharp test at θ. Same constants. Example (i): failure gives some f_{V_t}(p') ≥ c_linε_t by (I-11)(a) in contrapositive form, read at the lower threshold.
2. **(F) Creation gain and Dep.** 𝗀_t = c_Gp₀(g_t)² (IN1 Cor. C.7) comes from item 1. SA's Dep constant obeys c ≤ c'min{Θ₁^{−2}, θ_c²} (SA L17492), fixed by "the fractions of the fluctuation threshold, namely those at which a step evaluates its tests". These are the lower endpoints. Same constants.
3. **(F) The reserve.** IN1 Cor. C.7 and Theorem C.8 Step 4 use 𝗉_t = p₀(g_t) and the gains of item 1, through the count (C.4), which reads no threshold. Same constants.
4. **(F) Mass bound.** IN1 Theorem C.8. The envelope (C.8) takes its gains on the support of χ_ω from item 1 and then drops χ_ω ≤ 1 (IN1 L564: "the indicator χ_ω is dropped after the gains are taken, which only enlarges it"). For (SM), χ_ω is the product of the p's and (1 − p)'s, still in [0, 1], and its support lies in the fail-side and pass-side sets of Lemma 5.3. The pass-side bounds enter only through (I-8) and (I-12) (items 12, 13). Same constants, given those items.
5. **(F, P) Drop-out majorant.** IN1 Theorem C.9. The evaluation fibre "at which each test listed by ω except the one whose failure made X a drop-out takes its recorded value" (IN1 L604) is redefined for (SM): passed means q < (1 + κ_T)θ and failed means q > θ. The proof uses item 1 at every evaluation (F) and the one-sided bounds (I-11)(c), (e) on the fibre. Those two bounds hold on the regular domain, and items 12 and 14 show that the enlarged fibre lies in it. The drop-out's own failing test is not used. Same constants.
6. **(F) (LT) and (MB).** The event cost EC counts creations and Act (fail side). Same constants.
7. **(F) Small-field tails in NL1.** The term C_Ee^{−cp₀(g_k)²} in (I-5) (IN1 L74–78) bounds the Gaussian mass of 1 − χ beyond the inner thresholds. Since 1 − ζ ≤ 𝟏{q > θ}, it is read at the lower threshold. Same constants.
8. **(P) Transport of smallness** (SA L17346): |∂V_k − 𝟏| < 2ε_k ⇒ |∂V_t − 𝟏| < CL²ε_k ⇒ U_{t,□}(V_t) exists. With (SM) the hypothesis is |∂V_k − 𝟏| < 2(1 + κ_T)ε_k. The conclusion needs 2CL²(1 + κ_T)ε_k ≤ ε̄ (A1's datum radius). Room: ε_k → 0. This is a ceiling on γ, chosen last. (5.1)
9. **(I) Lemma 2.2(a)** (SA L17369–17380): the old tests χ_k(□) equal 1 on the support of the new ones. The bound becomes |∂U_{k,□} − 𝟏| ≤ (1 + κ_T)[(1 + c)ε_tη_t² + C(δ_k + e^{−cδ₀M₂Ř_k}ε_k)η_k²] ≤ (5/4)(CL^{−2} + CA₁/A₀ + Ce^{−Ř_k})ε_kη_k². It must be < ε_kη_k², the old lower threshold. Room: (5/4)(CL^{−2} + CA₁/A₀ + Ce^{−Ř_k}) < 1. This is a floor on L (after κ_T), a ceiling on A₁/A₀ (SA's own condition, with 5/4 added) and a ceiling on γ. (5.2)
10. **(I) Lemma 2.2(b)** (SA L17390–17396): χ^{(k)} passed ⇒ χ'_k = 1. A passed smooth χ^{(k)} gives |𝒜_k| < (1 + κ_T)δ_k. Then |V_k(𝓜^kU_{t,□})^{−1} − 𝟏| ≤ |e^{i𝒜_k} − 𝟏| + |V^bg_k(𝓜^kU_{t,□})^{−1} − 𝟏| ≤ (1 + κ_T)δ_k(1 + δ_k) + C(A₀/A₁)e^{−cŘ_k}δ_k. This must be < 2δ_k, the old lower threshold. Room: the factor 2 against 1 + κ_T = 5/4, so 2/(1 + κ_T) = 8/5. It holds once δ_k + (4/5)C(A₀/A₁)e^{−cŘ_k} ≤ 1/2, a ceiling on γ. (5.3)
11. **(P) Collar and rim mean** (SA L17360–17364). Passed collar, rim and other tests give |𝒜_k| < (1 + κ_T) times δ_k/(4Θ₁), θ_cδ_k and Cδ_k. Hence |𝐦| ≤ (5/4)C(Θ₁^{−1} + θ_ce^{−cϖ_T} + e^{−cMŘ_t})δ_k. It must stay < ½θ_cδ_k, where θ_cδ_k is the inner tests' *lower* threshold: their fail side (item 7) is what the mean must stay below. Room: θ_cΘ₁ ≥ 5C, ϖ_T ≥ C', and a ceiling on γ. These are SA's conditions with C replaced by (5/4)C. Θ₁ and ϖ_T are chosen after M₂ and before M (SA L19469; assembly §3), after κ_T. (5.4)
12. **(P) Support bounds** (I-12) and IN1 Lemma C.10. On supports, |∂U_k − 1| < C_supŘ_j²ε_jη_j² and |J(U_k)| < C_supŘ_j²ε_j become (5/4)C_sup times the same. Lemma C.10's ratio (5/4)C_supL²(log θ_j)^{2r+𝔭₀−q}A₀/C₀ < 1 holds after a ceiling on γ, since q > 𝔭₀ + 2r (IN1 L614–618). Room: a negative power of log θ_j. (5.5)
13. **(P) The fixed set contains every later argument**, IN1 Lemma C.11, and the prepared structure (I-8) on U^c_i(X^~, α_{0,i}, α_{1,i}). These follow from item 12 exactly as in IN1 L622–624.
14. **(P) Kept forms and Jacobians**, (I-11)(c), (e). Coercivity ⟨a, Δa⟩ ≥ κ_pos‖a‖² and the chart Jacobians hold on the regular domain of radii α_{ι,j} = C_ιθ_j^{−1/2}(log θ_j)^q. Item 12 places the (5/4)-enlarged supports in it. Same constants.
15. **(P) NL1 step** (I-5): the analyticity of the step on its product box and the error bound ‖E^{(k+1)}‖ ≤ E_𝖭 + C_E(|1 − τ_k| + δ_k + …). Fields on passed supports lie in the box by item 12. The δ_k term becomes (5/4)C_Eδ_k. C_E is fixed before E₀ (IN1 L78: "C_E depends neither on E₀ nor on N_⋆"), so replacing it by (5/4)C_E keeps the order.
16. **(P) ST1 admission** (assembly ST1(3), ⟦open: ST-cov⟧). Every lifted stage field on the supports lies in its domain with margin η_*. For (SM) the supports are the (5/4)-enlarged ones. This is a requirement on ST1: prove its admission for the thresholds (1 + κ_T)θ. The room is again item 12's polylogarithmic margin, but ST1 is open, so this item is recorded, not proved.
17. **(I) The strip cut-off** (SA L17526). ϑ_co is "0 up to slightly above δ_j and 1 from slightly below 2δ_j onwards". Two properties are used. A test with threshold ≤ δ_j is the same function of the new and old variables, which needs ϑ_co = 0 on its support. A test at 2δ_j has factor 1 wherever ϑ_co < 1, which needs q < 2δ_j there. For (SM) the first support is |log W'| < (1 + κ_T)δ_j. So ϑ_co must vanish up to slightly above (5/4)δ_j and equal 1 from slightly below 2δ_j. Room: 5/4 < 2. This is a re-choice of the cut-off function before L; its Jacobian bound is unchanged in form. (5.6)
18. **(P, F) Tests inside 𝐑**: the stage tests at δ'_j, the test on B (|B| < δ'_k/g_k), the last-shell test (|∂U_{k_♭,□}((𝟏,V_{k_♭})) − 𝟏| < ½ε_{k_♭}η²) and χ_{k,Λ} (SA L17585–17604). Failures are marks paid by (I-11)(d) (F, same constants). Passes feed Proposition 2.8 (LF1(4)), whose remainder ≤ Cg_k^{1/2} has polylogarithmic room (P, as item 12). The last-shell test's ½ against the ladder of SA L17396 has room 1/(2(1 + κ_T)) = 2/5 > 0.
19. **(—) Cut-offs inside draws.** χ(Λ^pr) in 𝔰_X and φ_X (SA L17604–17607) are density factors of a draw, not tests. Unchanged.
20. **(P) TP1's inputs** (TP-live), (TP-cx) (TP1 L111–135). These are LF1 and SC1 bounds on supports, so they fall under items 12–15.

*Proof of Theorem 5.4.* Each item states which implication of the sharp proof is used and shows that the (SM) version holds, by Lemma 5.3 and the stated room. The remaining logic of each consumer is unchanged, because (MI-4) has the same product structure as SA's history kernel with indicators replaced by [0,1]-valued factors, and none of the cited proofs uses idempotence (§5.2). ∎

*Is the list complete?* I listed every place in SA L17317–17610 and IN1 Part C where a threshold appears, and the NL1 and ST1 clauses that IN1 imports ((I-1)–(I-14)). A threshold read elsewhere in SA (Sections 2c–2e, which I read only through IN1's port) would be one more item of type (F) or (P). The principle of §5.3 settles any such item once its type and room are known.

### 5.5 Constants of §5

κ_T = 1/4 is absolute and is fixed first, before L. It is independent of M and κ̄. The room conditions (5.1)–(5.6) are floors on L (5.2), floors on Θ₁ and ϖ_T (5.4), a ceiling on A₁/A₀ (5.2), the choice of ϑ_co (5.6) and ceilings on γ (5.1)–(5.5). Each sits where SA's own condition sits, with a numerical factor ≤ 5/4 (or the room 8/5 of (5.3), 2/5 of item 18) added. None involves M except as SA's existing floors, and none reverses an existing order.

---

## 6. Two-run stability (Task 1)

Throughout, two configurations (U¹, ω¹) and (U², ω²) coincide on the tile data of a tile β. The construction is SA's with (SM). Run 1 is the *reference run*: in §7 it is the local run of β. Every hypothesis is placed on run 1 only, as in SA L23328. Distances are sup-norm distances in physical units. For a set A and r ≥ 0, A^{−r} := {x ∈ A : dist(x, A^c) ≥ r} and A^{+r} := {x : dist(x, A) ≤ r}.

### 6.1 The read structure

Call a quantity computed by the run **exactly local of radius r at x** (class (E)) if, as a function of (U, ω), it depends only on the bare links within distance r of x, the uniforms located there, and the decisions, regions and other (E)-quantities within distance r of x. Call it **background-reading** (class (B)) if it is a function of (E)-quantities near x and of the true averaged background of one step, at points near x.

**(RS)** [input: LF1(2) (C2, "tests, backgrounds and retained terms depend on a stated enlargement of the determining regions", assembly LF1(2)); SA L17336, L17341, L17344, L17508, L17518–17526, L17585–17607, L23328].

- **(RS-a) The (E) moves.** The following read only (E)-quantities, of radius ≤ r_T := 2 level-t cells around their location:
 - the plaquette tests χ_t(□) and approximate fluctuation tests χ'_{t−1}(□), "built from localised backgrounds … only within O(1) test cubes" (SA L17336);
 - the gauge draws 𝔊_t (block-local Faddeev–Popov factors, SA L17317, L17346);
 - the pivot values, "the value that solves, for the pivot bond, the averaging constraint … of the single coarse bond c" (SA L17341);
 - the localised strip background V^loc_t (SA L17518);
 - inside 𝐑: the stage tests "formed with backgrounds localised in X"; the tree gauge; the test on B relative to "the averages of the minimiser U₀" of the box; the last-shell test; the frame draw r ∈ W₄; and the reference draw 𝔰_X, built with "the background localised in X" U_{k,X} (SA L17585–17607);
 - the geometric maps (hulls, layers, boxing, rounds, the class rule of 𝐑, the three fates). These read decisions and regions only.
 A test cube "lies well inside a cell of its own level" (SA L17334), the collar has width ϖ_T ≤ M level-(t−1) units (SA L17449: the floor M ≥ ϖ_T), and a cell has LMŘ_t such units. So r_T = 2 covers every read set of a test.
- **(RS-b) The (B) quantities.** These are the true background U_t(𝐕) on Ω_t, its average V^bg_{t−1} on the bonds with an end point in Ω_t (SA L9783), the fluctuation 𝒜_{t−1} = (1/i)log(V_{t−1}(V^bg_{t−1})^{−1}) on those bonds, and the strip variable W' (SA L17523). They are read by the third test χ^{(t−1)}, the collar and rim tests of step t, and, at later levels, by tests of 𝐑 ("a single test of 𝐑 depends on them", SA L23328). Each reads them as tested quantities, through a functional F with |F(a) − F(a')| ≤ Λ sup_y|a(y) − a'(y)| over a read set of diameter ≤ (C_R + 1) cells of the reading level. For a sup-norm test, Λ = 1. I allow Λ ≤ 𝔎_t (6.5), the number of bonds in the read set.
- **(RS-c) Nothing else reads (B).** No map, no draw density, no geometric rule and no class rule reads a (B)-quantity. In the U-picture a stored block field V_{t−1} is the (E)-quantity 𝓜^{t−1}U, or a reference draw in a healed region. A formula that reconstructs it from a stored A' through the background of the same step returns that (E)-quantity.
- **(RS-d) Charts.** A (B)-tested value is defined where |V_{t−1}(V^bg_{t−1})^{−1} − 𝟏| ≤ ½. Elsewhere the test fails (totality, SA L17346). All (B)-thresholds are ≤ 2δ_{t−1} ≤ 1/16, so ζ(q/θ) = 0 on a neighbourhood of the chart boundary.

*Status of (RS).* (RS-a) is a list of what SA's text says about each move. (RS-b) and (RS-c) are SA's sentence at L23328 together with the absence, in SA L17317–17610, of any other move reading V^bg. (RS) is a property of LF1's final definitions. I have checked it only against SA's description, so it is an input. The operation whose detail I could not check is 𝐑's stage maps ("integrated out as in a small-field step", SA L17585). If one of them fed a (B)-quantity into an (E)-quantity, Proposition 6.9 would still apply with its factor Λ.

### 6.2 The background comparison

**(BGL)** [input: BG1/PR1; SA Theorem 6(c), L9783–9789; proved conditionally in `a3-derivative.md` Lemma 10.1 (gate `gates/a3-derivative-gate.md` §10: "ADVANCE with the repairs/admission check below") with the auxiliary cut-meet of `a3-close.md` §3 Lemma J (gate `gates/a3-close-meet-gate.md` §B: "ADVANCE for the explicitly defined meet"); premises P81 (A1, conditional on F0), P82° and SA 9786's geometry, as listed in `a3-close.md` §3 "Consequences" 1]. There are δ ∈ (0, 1) and C_bg, fixed with L, ρ, μ and the A1/A3 constants, independent of M, κ̄, depth, volume and position, such that the following holds.

Let two separated sequences (Ω^a_q)_{q≤t}, a = 1, 2, with real ε̂-regular data (ε̂ ≤ 𝖺(L, ρ, μ)), be given. Let W̃ be a union of cubes of side μℓ_t with:
 - (i) Ω¹_q ∩ W̃ = Ω²_q ∩ W̃ for every q, with the same data on every row with an end point in W̃ and the same frozen bare links in W̃ ∖ Ω₀;
 - (ii) the O(1) outermost layers of μ-cubes of W̃ (its collar) lie in Ω¹_t = Ω²_t there.
Then at every bond b of level t − 1 in W̃ ∩ Ω_t,

  |V^{bg,1}_{t−1}(b) − V^{bg,2}_{t−1}(b)| ≤ C_bg ε̂ e^{−δ·dist(b, W̃^c)/ℓ_t}.   (6.1)

*Derivation from the cited results.*
1. Apply Lemma 10.1 of `a3-derivative.md` to each run with W := W̃ ∩ Ω₀ and the auxiliary cut-meet U°_W of `a3-close.md` §3, a single part with its collar in the top layer t. U°_W is defined from the sequence and data on W̃ only, so it is the same for both runs. This gives U^a|_W = (e^{iηf_a}U°_W)^{w_a} with ξ_y|f_a| ≤ C_με̂e^{−θd_𝐁(y,W^c)}, θ = δ₀/8 (`a3-derivative.md` (41)).
2. d_𝐁(y, y') ≥ dist(y, y')/ℓ_t, because in level-t units every local scale ξ_j ≤ 1 and η ≤ 1 (SA L9602).
3. V^bg_{t−1} is the level-(t − 1) average in block axial gauge, which does not depend on the representative of the orbit (SA L9783). Its difference between e^{iηf}U° and U° at b is ≤ C_L sup|ξf| over the double block of b, by the functional derivative of the averaging map (BG1(1); `a1-balaban.md` §3.5, CMP 98 Propositions 4–5 rebuilt).
4. The triangle inequality gives (6.1) with δ := θ and C_bg := 2C_LC_μe^{θ}.

*Reading added here.* Lemma 10.1 is stated for a μ-collared W. I use W = W̃ ∩ Ω₀, whose boundary contains pieces of ∂Ω₀ around holes inside W̃. There the joined sequence coincides with the given one: a part with collar in layer 0 has a trivial tower and lift, so there is no mismatch. SA places the mismatch "on the collar bonds" (SA L9789). This reading is needed for any use of 6(c) on a region containing old holes, SA's Lemma 4.15 included. It is flagged for BG1.

**Lemma 6.2 (tested values)** [proved from (BGL)]. With the hypotheses of (BGL), at a bond b where both values are in the chart, |𝒜¹_{t−1}(b) − 𝒜²_{t−1}(b)| ≤ 4C_bgε̂e^{−δ·dist(b,W̃^c)/ℓ_t}. For a (B)-test τ with functional F of constant Λ and threshold θ_τ ≥ θ_min δ_{t−1}, θ_min := min{θ_col, θ_c, c_R, 1}, whose read set lies at distance ≥ d from W̃^c:

  |p¹_τ − p²_τ| ≤ 4ΛC_q e^{−δd/ℓ_t},  C_q := 4C_bgC_L'(A₀/A₁)/θ_min,   (6.2)

where ε̂ ≤ C_L'ε_{t−1} on the supports, and c_R δ_{l−1} is the least threshold of 𝐑's (B)-test for a stored level-l value.

*Proof.* On SU(2), on {|g − 𝟏| ≤ ½}, |(1/i)log g − (1/i)log h| ≤ 2|g − h|: the logarithm is analytic there with derivative bounded by 2. With the same V_{t−1} in both runs, |V(V^{bg,1})^{−1} − V(V^{bg,2})^{−1}| = |V^{bg,1} − V^{bg,2}| by unitary invariance. If one value lies outside the chart, the difference bound and RS-d put both q's ≥ (1 + κ_T)θ, so both p's vanish. Otherwise ζ is 4-Lipschitz and |q¹ − q²| ≤ Λ·4C_bgε̂e^{−δd/ℓ_t}. Divide by θ_τ and use ε̂/δ_{t−1} ≤ C_L'ε_{t−1}/δ_{t−1} = C_L'A₀/A₁. ∎

### 6.3 Why round 1's (QL) is not provable

**Lemma 6.3 (crossing holes and the available comparison)** [proved]. Let A be the agreement region of step t, and let C be a connected component of Ω_t^c that meets both A^c and a point y ∈ Ω_t ∩ A. Let W̃ ⊂ A satisfy (BGL)(i)–(ii) with its collar in layer t. Then dist(y, W̃^c) ≤ dist(y, C) + O(μℓ_t). So (6.1) gives no decay at y beyond e^{−δ·dist(y,C)/ℓ_t}.

*Proof.* Since W̃ ⊂ A and C meets A^c, C ⊄ W̃. If C met W̃, then, C being connected, C would meet ∂W̃, which lies within O(μℓ_t) of W̃'s collar. The collar lies in Ω_t, and C ⊂ Ω_t^c: a contradiction up to the collar width. So C lies outside W̃ up to that width, and dist(y, W̃^c) ≤ dist(y, C) + O(μℓ_t). ∎

*What it means.* SA's 6(c) allows several parts with collars in different layers. A part with collar in a lower layer j < t has its whole collar in Ω_j ∖ Ω_{j+1} ⊂ Ω_t^c. To exclude the part of C outside A while keeping the part near y, a part boundary would have to cut across C inside one layer. Near the outer boundary of C, C lies in layer t − 1 (the gaps of SA L17401). Such a cut must close up outside C, in Ω_t, so its collar would cross from layer t − 1 to layer t, which 6(c) forbids. I found no construction of such a cut, and SA gives none. So near a crossing hole the available comparison gives nothing. This is an obstruction to the *proof*, not a counterexample: physically the influence of the exterior still has to pass through Ω₀ and should decay. It is exactly SA's "long cluster of cells … that lie in Ω_j^c" (SA L23328).

**Lemma 6.4 (SA's rounds are not tile-local)** [proved from the rules, SA L17321–17325, L17354–17360]. Let 𝔡₁, …, 𝔡_N be level-t cells along a straight line, consecutive ones adjacent, 𝔡₁ outside the tile β and 𝔡_N in its core, all in Ω_t ∖ (Ω_t^c)^{~3}, with no third-test failure within two cells. In each 𝔡_s let b_s be a stored-eligible bond. Suppose that in both runs (1 + κ_T)θ_cδ_{t−1} ≤ |𝒜_{t−1}(b_s)| < δ_{t−1} for all s, and that the rim-test uniforms are arbitrary. Suppose run 1 has a cell 𝔡₀ of Z^{[0]}, outside β, adjacent to 𝔡₁ and containing a stored bond b₀ with the same bound on |𝒜(b₀)| (for example 𝔡₀ lies in the margin of a plaquette failure outside β). Suppose run 2 has no cell of Z^{[0]} within three cells of the chain. Then 𝔡_N ⊂ Z_t in run 1, while in run 2 no round examines the chain and 𝔡_N ⊄ Z_t unless something else puts it there.

*Proof.* Since |𝒜(b_s)| < δ_{t−1}, the third test passes surely at the cubes containing b_s (ζ = 1 below the lower threshold), and the cells 𝔡_s are not in (Ω_t^c)^{~2}, so they are not in Z^{[0]}.
 - *Run 1.* 𝔡₀ is a cell of Z^{[0]} touching Λ (through 𝔡₁), so it is a rim cell. Its rim test fails surely, since |𝒜(b₀)| ≥ (1 + κ_T)θ_cδ_{t−1} makes ζ = 0, and round 0 adds 𝔡₀^~ ∋ 𝔡₁. Then 𝔡₁ is a cell of Z touching Λ through 𝔡₂; it was not examined before ("Every round examines bonds and cubes that no earlier round examined"), and it fails, so 𝔡₁^~ ∋ 𝔡₂ is added. Inductively, round s adds 𝔡_{s+1}.
 - *Run 2.* No cell 𝔡_s ever touches Z. So no 𝔡_s is a rim cell, and no b_s is a stored bond, let alone a collar bond. They are never examined and stay in Λ_t. ∎

So the deep live region depends on the exterior through a chain whose tested values are all far from their thresholds. No window hypothesis can exclude this. The chain consists of *triggers*: bonds that would fail if examined. This is the trigger part of SA's long-cluster hypothesis. To turn Lemma 6.4 into a counterexample to round 1's (QL), one needs a configuration with these tested values. I do not construct one. Nothing in the rules excludes it, so round 1's (QL) cannot be proved from the rules.

### 6.4 Inner regions, long clusters and windows

**Constants.**
- r_T = 2.
- b₁ is SA's boxing size (a component "contained in a cube of O(1) cells", SA L17317).
- r_bx := b₁⁴(b₁ + 1) (Lemma 6.5).
- w := b₁ + 3.
- C_R from (R3).
- R := 14 + b₁ and e₀ := 7(4R + 11)⁴(2w + 1) + 1 (used in §7.2).
- m₁ := 16 + 4w + r_T + e₀, m₂ := r_bx + 6w + b₁ + 4 + e₀, m₃ := r_bx + C_R + 4, m₀ := m₁ + m₂ + m₃.

All are absolute numbers given SA's geometric constants: fixed with L, before κ, independent of M and κ̄.

**Rates and widths.** Let b' := 13 and

  ϖ_k := δ𝗇MŘ_k/512,  𝔎_i := N_τ𝗇⁴(MŘ_k)⁴L^{4(k−i)}·(C_R + 1)⁴(MŘ_i)⁴L^{8(Ř_i+2)},   (6.3)
  ε_i := e^{−ϖ_k}(2L^{b'})^{−(k−i)}/(2𝔎_i),  D_i := (2/δ)[ϖ_k + (k − i)log(2L^{b'}) + log(16C_q𝔎_i²/κ_T)].   (6.4)

𝔎_i bounds both the number of potential (B)-test sites of level i in a tile and the constant Λ of any (B)-test of level i. The first count: third, collar and rim sites at level-(i − 1) bonds, and 𝐑's (B)-sites at bonds of levels ≥ i − 𝖭_i − 1 with 𝖭_i = Ř_i (SA L17585, stages j = k_♭, …, k − 1). The second: the bonds of all levels in a component of ≤ C_R cells per side.

**Inner regions of β.** Put A₁ := β^{−c₁}. For i = 1, …, k define

  A_i^{(1)} := A_i^{−12c_i},  J_i := A_i^{−(m₁c_i + D_iℓ_i)},  J_i^♮ := J_i^{−(r_bx+2)c_i},  J_i' := J_i^{−(m₂c_i + D_iℓ_i)},  A_{i+1} := J_i'^{−m₃c_i}.   (6.5)

The margin consumed at level i is μ_i := m₀c_i + 2D_iℓ_i.

**Lemma 6.1 (margins)** [proved]. Let C_L := Σ_{s≥0}L^{1−s}(1 + log(1 + B_♯s))^r, with B_♯ the frame constant of IN1(3). Suppose 𝗇 ≥ 16(m₀ + 1)C_L, M ≥ 4096(C_L + 4)log L/(δ𝗇), and x_k ≥ X_F (a floor on x_k). Then c₁ + Σ_{i=1}^k μ_i ≤ (7𝗇/64)c_k < (𝗇/8)c_k, so A_{k+1} contains the core of β.

*Proof.* In units of c_k = MŘ_kℓ_k, c_i/c_k = (Ř_i/Ř_k)L^{i−k}. As in round 1 (R1 L359), Ř_{k−s}/Ř_k ≤ L(1 + log(1 + B_♯s))^r. So c₁ + Σ_i m₀c_i ≤ (m₀ + 1)C_Lc_k ≤ (𝗇/16)c_k. Next, Σ_i 2D_iℓ_i/c_k = Σ_{s≥0} 2D_{k−s}L^{−s}/(MŘ_k), and Σ_sL^{−s} ≤ 2. Split D_{k−s}:
 - the ϖ_k term gives ≤ (4/δ)·2ϖ_k/(MŘ_k) = 𝗇/64;
 - inside log 𝔎_{k−s}, the term 8(Ř_{k−s} + 2)log L gives ≤ (64 log L/δ)Σ_s(Ř_{k−s} + 2)L^{−s}/(MŘ_k) ≤ (64 log L/δ)(C_L + 4)/M ≤ 𝗇/64, by the floor on M;
 - the remaining terms, s·log(2L^{b'}), 4s log L, log(16C_qN_τ𝗇⁴(C_R+1)⁴/κ_T), 8log(MŘ_k), 8log(MŘ_{k−s}) with log(MŘ_{k−s}) ≤ log(MŘ_k) + log L + r log(1 + log(1 + B_♯s)), contribute O(log(MŘ_k))/(MŘ_k) after the s-sum, which is ≤ 𝗇/64 for x_k ≥ X_F.
The total is ≤ 𝗇/16 + 3𝗇/64 = 7𝗇/64. ∎

*The floor on M* is a lower bound only, fixed after L, δ, 𝗇. It meets the IN1 constraint ("M only as a lower bound").

**Long clusters (run 1).** Two cells are *w-adjacent* if their sup-distance is ≤ 2wc_i; *w-components* are the components of this relation.
- S^Ω_i := A_i^{(1)} ∖ (A_i^{(1)})^{−3wc_i}. 𝒦^Ω_i is the set of w-components of the level-i cells of Ω_i^c ∩ A_i^{(1)} that meet S^Ω_i. LC^Ω_i := {some K ∈ 𝒦^Ω_i meets J_i^{+((D_i/2)ℓ_i + (w + r_T + 1)c_i)}}.
- 𝒫_i is the set of level-i cells containing a *potential* collar or rim site of step i, located in J_i^♮, whose decision would be "fail". This is computed with the site's own uniform and run 1's tested value, whether or not the site is examined in run 1.
- S^Z_i := J_i^♮ ∖ (J_i^♮)^{−3wc_i}. 𝒦^Z_i is the set of w-components of the level-i cells of (Z_i^{[0]} ∪ 𝒫_i) ∩ J_i^♮ that meet S^Z_i. LC^Z_i := {some K ∈ 𝒦^Z_i meets J_i'^{+(b₁+2)c_i}}.
- LC_i := LC^Ω_i ∪ LC^Z_i.

**The comparison region of step i (run 1, and hence run 2).** W̃_i is the union of the μℓ_i-cubes contained in (A_i^{(1)})^{−2wc_i} ∖ ∪_{K∈𝒦^Ω_i}K^{+wc_i}.

**Windows (run 1).** A *(B)-site* of level i is a potential site of χ^{(i−1)}, of a collar or rim test of step i, or of a (B)-test of 𝐑 at level i. Put Win_i := ∪_{τ (B)-site of level i located in J_i} {|u_τ − p¹_τ| ≤ ε_i}, and G_{<i} := ∩_{l<i}(Win_l ∪ LC_l)^c.

**Lemma 6.5 (boxing is local)** [proved]. For sets S of level-i cells, bx(S) ∩ Q depends only on S ∩ Q^{+r_bx c_i}.

*Proof.* Let B(S) := S ∪ ∪{box(K) : K a small component of S}, small meaning contained in a cube of b₁ cells to a side, and box(K) the bounding box. Then bx(S) = B^n(S) for n large (SA L17317, "repeats this until nothing changes"; B(S) ⊇ S and the torus is finite).
 - *One round has radius b₁ + 1.* x ∈ B(S) ∖ S iff x ∈ box(K) for a small component K of S. Then K lies in a b₁-cube containing x, and that K is a component of S is decided by S on K and its one-cell neighbourhood, all within (b₁ + 1)c_i of x. If S = S' on Q^{+(b₁+1)c_i}, the small components of S and S' meeting the b₁-cubes around points of Q coincide. So B(S) ∩ Q = B(S') ∩ Q.
 - *At most b₁⁴ rounds change anything.* Let K be a small component of B^{m−1}(S) that is not a box, with m − 1 ≥ 1. If K were a component of B^{m−2}(S), it would have been small there, box(K) ⊂ B^{m−1}(S) would be connected and meet K, so box(K) ⊂ K and K would be a box. Hence K is not a component of B^{m−2}(S). If K ⊂ B^{m−2}(S), K would be a connected subset maximal in a larger set, hence a component: a contradiction. So K contains a point of box(K') ∖ B^{m−2}(S) for a small component K' of B^{m−2}(S), and K' is not a box. By connectedness K ⊇ box(K') ⊋ K'. Iterating gives small non-box components K₀ ⊊ K₁ ⊊ … ⊊ K_{m−1} with |K_{m−1}| ≤ b₁⁴. So m − 1 ≤ b₁⁴ − 1, and B^m(S) = B^{m−1}(S) for m > b₁⁴.
Hence bx(S) = B^{b₁⁴}(S), and the radius is b₁⁴(b₁ + 1)c_i = r_bxc_i. ∎

**Lemma 6.6 (rounds are local off long clusters)** [proved]. At a step i, suppose:
 - (i) Z_i^{[0]} coincides in the two runs on J_i^♮;
 - (ii) every potential collar or rim site located in J_i^♮ has the same would-be decision in the two runs;
 - (iii) LC^Z_i fails in run 1.
Then the region Z_i^{pre} after the rounds coincides in the two runs on J_i'.

*Proof.*
 - *Confinement.* Call a cell a *seed* if it lies in Z^{[0]} or within one cell of 𝒫. A failure of round n is an examined site whose decision is "fail", so its cell is in 𝒫 (by (ii), the same set in both runs inside J_i^♮), and the cells it adds, (failure cells)^~, are seeds. *Claim:* every small component of every Z^{[n]} contains a seed. Its cells are in Z^{[0]}, or were added as (failure cells)^~, or were added in the box of a small component K' of an earlier Z^{[m]}. Components only merge, so the component contains box(K') ⊇ K', and K' contains a seed by induction. A box lies in the b₁-cube of its component, so every boxed cell is within b₁ cells of a seed. Hence every cell of Z^{pre} lies within (b₁ + 1) cells of Z^{[0]} ∪ 𝒫.
 - *Separation.* Distinct w-components are at sup-distance > 2wc_i. Their (b₁ + 1)-neighbourhoods G(K) are therefore > (2w − 2b₁ − 2)c_i = 4c_i apart. Cells in different G(K) are never adjacent, never in one component, and never in one b₁-box.
 - *Independence.* Let K be a w-component of (Z^{[0]} ∪ 𝒫) ∩ J_i^♮ that does not meet S^Z_i. Then K ⊂ (J_i^♮)^{−3wc_i} and G(K)^{+2c_i} ⊂ J_i^♮. A round's action on G(K)^{+c_i} depends only on the region within one cell of it: collar bonds are within ϖ_T < c_i of Λ, rim cells touch Λ, and boxing acts per component. By confinement and separation, no cell of any Z^{[n]} lies in G(K)^{+2c_i} ∖ G(K). Such a cell would need a seed within b₁ + 1 cells of it, hence within (b₁ + 3)c_i of K. Other w-components are farther than 2wc_i ≥ (2b₁ + 6)c_i, and seeds outside J_i^♮ are farther than (3w − b₁ − 3)c_i ≥ (2b₁ + 6)c_i. So the evolution inside G(K) reads only Z^{[0]} and the decisions inside G(K)^{+c_i}, which are equal in the two runs by (i)–(ii). By induction on the round, Z^{1,[n]} ∩ G(K)^{+c_i} = Z^{2,[n]} ∩ G(K)^{+c_i} for all n.
 - *Conclusion.* By (iii), the w-components meeting S^Z_i, and cells outside J_i^♮, have neighbourhoods disjoint from J_i'^{+c_i}. The latter are at distance ≥ (m₂ − r_bx − 2)c_i + D_iℓ_i − (b₁ + 1)c_i > c_i. So Z^{pre} ∩ J_i' is the union over interior K of Z^{pre} ∩ G(K) ∩ J_i', the same in both runs. ∎

### 6.5 The theorem

For l < i, (B)-quantities stored at step l at y are compared through W̃_l. On G_{<i}, LC^Ω_l fails for every l < i, and (6.5) gives:

  W̃_l^c ∩ J_l^{+(D_l/2)ℓ_l} = ∅, hence dist(y, W̃_l^c) ≥ dist(y, J_l^c) + (D_l/2)ℓ_l for y ∈ J_l.   (6.6)

*Proof of (6.6).* Let y' ∈ J_l^{+(r_T c_l)}. Its distance to the complement of (A_l^{(1)})^{−2wc_l} is ≥ (m₁ − 12 − 2w − r_T)c_l + D_lℓ_l ≥ D_lℓ_l + 2c_l. For K ∈ 𝒦^Ω_l, on (LC^Ω_l)^c, dist(y', K^{+wc_l}) > (D_l/2)ℓ_l + c_l. Rounding to μ-cubes costs ≤ μℓ_l ≤ c_l. So no point of W̃_l^c lies within (D_l/2)ℓ_l of J_l. For y ∈ J_l and z ∉ J_l^{+r}, sup-norm balls give dist(y, z) ≥ dist(y, J_l^c) + r. ∎

**Theorem 6.7 (QL′, two-run stability)** [proved from (RS), (BGL), (R3), Lemmas 6.2, 6.5, 6.6]. Let x_k ≥ X_F. For 1 ≤ i ≤ k + 1, on G_{<i}, the following statement 𝔄(i) holds.
 - (a) For every l < i, the sets Ω_l, Λ_l, S_l, Z_l, 𝒵_l (as modified by healing up to step i − 1), the marks, nests and creation sets, intersected with A_i, coincide in the two runs.
 - (b) Every decision of a level l < i located in A_i, and every (E)-quantity of a level l < i located in A_i, coincides.
 - (c) Every (B)-quantity Q stored at a step l < i satisfies, at y ∈ A_i, |Q¹(y) − Q²(y)| ≤ 4C_bgε̂_l e^{−δ·dist(y, W̃_l^c)/ℓ_l}.

Moreover, on G_{<i} ∩ (Win_i ∪ LC_i)^c (1 ≤ i ≤ k), every (B)-site τ of level i located in J_i has |p¹_τ − p²_τ| ≤ ε_i/2 + ε_i/4 and the same decision in both runs, and 𝔄(i + 1) holds.

*Proof.* 𝔄(1): A₁ = β^{−c₁} and there are no levels below 1 except the bare links and level-0 data, which coincide on β. Assume 𝔄(i) on G_{<i} and work on G_{<i} ∩ (Win_i ∪ LC_i)^c. Go through the moves of step i in order.

*M1. Plaquette and approximate fluctuation tests.* For a cube □ located in A_i^{−r_Tc_i}, the tested value is an (E)-quantity of radius r_Tc_i (RS-a), whose inputs coincide by 𝔄(i)(b). So q¹_τ = q²_τ and p¹_τ = p²_τ, the same uniform is used, and the decision coincides. No window is needed. So P_i and Q_i coincide on A_i^{−r_Tc_i}, and so do the gauge draws.

*M2. Ω_i.* Ω_i^c = Q_i'^{~2} ∪ P_i'^{~4} ∪ Ŷ^{~8}, with Y = 𝒵_{i−1} coinciding on A_i by 𝔄(i)(a). The hull and coarsening move a set by ≤ 1 cell and the layers by ≤ 8. So Ω_i coincides on A_i^{−12c_i} = A_i^{(1)}, and with it the separated sequence of step i (earlier members by 𝔄(i)(a)).

*M3. The comparison region.* 𝒦^Ω_i is defined from Ω_i^c ∩ A_i^{(1)}, so it is the same in both runs, and so is W̃_i. Check (BGL)(i)–(ii):
 - (i) holds because W̃_i ⊂ A_i^{(1)} and Ω_q ∩ W̃_i coincide for q ≤ i (M2 and 𝔄(i)(a)). The data on rows meeting W̃_i are (E)-quantities of levels < i located in A_i, or level-i averages of them, of radius ≤ c_i.
 - (ii): a point within O(μ)ℓ_i ≤ c_i of ∂W̃_i lies within c_i of the boundary of (A_i^{(1)})^{−2wc_i} ∖ ∪K^{+wc_i}. It is at distance ≥ (w − 1)c_i from every cell of Ω_i^c in A_i^{(1)}: crossing cells are removed with margin wc_i; non-crossing w-components lie in (A_i^{(1)})^{−3wc_i} and are > 2wc_i from crossing ones. Cells of Ω_i^c outside A_i^{(1)} are at distance ≥ (2w − 1)c_i. So the collar lies in Ω_i.

*M4. Backgrounds.* By (BGL), (6.1) holds for the true backgrounds of step i on W̃_i.

*M5. Third, collar and rim tests.* Let τ be a (B)-site of level i located in J_i. Its read set lies in J_i^{+r_Tc_i}. By (6.6) with l = i (valid since LC^Ω_i fails), it is at distance ≥ (D_i/2)ℓ_i from W̃_i^c. Lemma 6.2 with Λ ≤ 𝔎_i gives |p¹_τ − p²_τ| ≤ 4𝔎_iC_qe^{−δD_i/2}. By (6.4), e^{−δD_i/2} = e^{−ϖ_k}(2L^{b'})^{−(k−i)}κ_T/(16C_q𝔎_i²), so the bound is ≤ κ_Te^{−ϖ_k}(2L^{b'})^{−(k−i)}/(4𝔎_i) ≤ ε_i/2. On Win_i^c, |u_τ − p¹_τ| > ε_i, so u_τ lies on the same side of p²_τ as of p¹_τ: the decisions coincide. This covers the potential collar and rim sites, examined or not, so the would-be decisions coincide on J_i^♮ ⊂ J_i. The third-test failures R_i coincide on J_i.

*M6. Z^{[0]} and the rounds.* Z_i^{[0]} = bx((Ω_i^c)^{~2} ∪ R_i'^~). Its inputs coincide on J_i^{−2c_i} (R_i' adds a hull and ~ a layer), so by Lemma 6.5 Z^{[0]} coincides on J_i^{−(r_bx+2)c_i} = J_i^♮. Lemma 6.6 applies, since LC^Z_i fails, and gives Z_i^{pre} on J_i'. The creation set (hulls of P', Q', R' and of the failed collar and rim sites) coincides on J_i'.

*M7. The class of 𝐑.* Let X be a component of Z_i^{pre}, in either run, meeting A_{i+1}^{+c_i}. If X is in the class of that run, then by (R3) its diameter is ≤ C_Rc_i. With m₃ ≥ C_R + 4, X together with its one-cell neighbourhood lies in J_i', so X is a component of Z_i^{pre} in the other run as well. The class conditions read X ∩ Z_l for l ∈ [i_♭, i], the absence of creations and joinings in X, and the quarantine (SA L17575). All of these lie inside X at levels ≤ i, and they coincide by 𝔄(i)(a) and M6, since X ⊂ J_i' ⊂ A_l for l ≤ i. So the class components meeting A_{i+1}^{+c_i} coincide. A component not in the class of one run is not in the class of the other.

*M8. The operation 𝐑 on a class component X ⊂ J_i'.* Go through its moves.
 - Every (E)-move of 𝐑 (RS-a) reads data in X^~ that coincide, and uses the same uniforms, so it has the same outcome. This includes the stage tests, the tree gauge, the test on B, the last-shell test, the frame and reference draws, and χ_{k,Λ}.
 - A (B)-test of 𝐑 is a (B)-site of level i located in X ⊂ J_i. It reads stored values of levels l ∈ (i − 𝖭_i − 1, i] at bonds y ∈ X. For l < i: y ∈ J_i' ⊂ J_l with dist(y, J_l^c) ≥ D_iℓ_i, so (6.6) and 𝔄(i)(c) give |ΔQ(y)| ≤ 4C_bgε̂_le^{−δ(D_iL^{i−l} + D_l/2)}. For l = i, (6.6) and M4 give the same with exponent ≥ δ(D_i + D_i/2). By Lemma 6.2, |p¹ − p²| ≤ 4𝔎_iC_q Σ_{s≥0}e^{−δD_iL^s}. Since δD_i ≥ 2 log 2 and L ≥ 3, this is ≤ 8𝔎_iC_qe^{−δD_i} ≤ ε_i/4. On Win_i^c the decisions coincide.
 - The fate (healed, island, drop-out) is a function of these decisions. So it coincides, and so do the replacements of Ω_l, Λ_l, S_l on X (SA L17417–17431) and the drop-out sequences Ω^𝛎 (SA L17433–17440).

*M9. Conclusion.* 𝒵_i is Z_i^{pre} with the healed components removed, and these coincide on J_i' by M6–M8. The regions, marks and nests of levels ≤ i coincide on A_{i+1} = J_i'^{−m₃c_i}. The (E)-quantities of level i located in A_{i+1} have inputs within r_Tc_i, which coincide, and that gives (b). The (B)-quantities stored at step i (𝒜_{i−1} on Ω_i ∩ Λ_i^c, W' on the strip) satisfy (c) by M4 and Lemma 6.2. This is 𝔄(i + 1). ∎

**Corollary 6.8** [proved]. On G_{<j+1} the live regions 𝒵_l, l ≤ j, coincide in the two runs on A_{j+1} ⊇ A_{k+1} ⊇ core. Hence, for a deep cell 𝔷 and n ≤ j ≤ k, 𝟏{E^{(n)}_𝔷(j) in run 1} = 𝟏{E^{(n)}_𝔷(j) in run 2} on G_{<j+1}. ∎

### 6.6 The cross-level propagation of stored-field influence

Round 1's first unchecked step was: "an old stored fluctuation field's influence on a new test must grow by at most a fixed geometric rate in the level difference" (R1 L447). Under (RS) the influence does not grow (M8). The general form is as follows.

**Proposition 6.9 (geometric growth is absorbed)** [proved]. Suppose that, contrary to (RS-c), a (B)-quantity stored at step l could feed later quantities through a chain of maps. Each map, at a level m, has Lipschitz constant ≤ Λ in the sup norm on a read set within ρ ≤ m₃ cells of level m. Each such quantity is finally read by a (B)-test at level i located in J_i. Then the total difference of that test's pass weight between the runs is at most

  4𝔎_iC_q Σ_{l≤i} (2Λ)^{i−l} e^{−δD_iL^{i−l}} ≤ 8𝔎_iC_q e^{−δD_i}  provided δD_i(L − 1) ≥ log(4Λ).   (6.7)

*Proof.* A chain from level l to level i passes through a subset of the levels between, so there are at most 2^{i−l} chains, and each multiplies by at most Λ^{i−l}. The displacement along a chain is ≤ Σ_{m=l}^{i} ρc_m ≤ m₃Σ_mc_m, which the margins m₃c_m absorb. So the original value is read at a point y with dist(y, J_l^c) ≥ D_iℓ_i. By (6.6) and 𝔄(i)(c) its difference is ≤ 4C_bgε̂_le^{−δD_iL^{i−l}}. Lemma 6.2 gives the factor 4𝔎_iC_q. Finally L^s ≥ 1 + (L − 1)s gives e^{−δD_iL^s} ≤ e^{−δD_i}(e^{−δD_i(L−1)})^s ≤ e^{−δD_i}(4Λ)^{−s}, and the sum over s ≥ 0 of (2Λ)^s(4Λ)^{−s} is 2. ∎

Since D_i ≥ (2/δ)ϖ_k → ∞, the condition holds for every fixed Λ once x_k is large. The mechanism is the depth structure: a value of level l is compared in level-l units, but it is read at a distance of at least D_i *level-i* units, which is D_iL^{i−l} level-l units.

### 6.7 What changed relative to round 1's §7

- Round 1's (QL1) asked for |q_τ − q'_τ| ≤ C_qθ_τe^{−δD_j}. What the windows need is the bound on the pass weights p_τ (Lemma 6.2). The difference matters at chart boundaries and for max-type tests.
- Round 1 compared stored values at their own margin D_l. The right distance is the reading distance D_iL^{i−l} (Proposition 6.9).
- Round 1's inner regions compared level-j tests on J_j while the level-(j − 1) data agreed only on J_j. The margins (6.5) now separate the data-agreement region A_i from the decision region J_i by the decay length D_iℓ_i.
- SA's second hypothesis is restored, as LC_i, in the form needed by Lemmas 6.3 and 6.4. Its Ω^c-part and its Z^{[0]}-part are paid by live cells; its trigger part needs (TT) (§7, §10.1).
- Windows are needed only at (B)-sites. (E)-tests agree exactly.

---

## 7. The rarity bound: Theorem F″

### 7.1 The local run and the fresh windows

For a tile β let U^β be U on the bonds of the closed tile and 𝟙 elsewhere, and ω^β be ω at the locations in β and ½ elsewhere. The *local run* H^β := H_k(U^β, ω^β) is the construction applied to a modified configuration, so it is a function of the tile data of β. By (COV), and because the frozen exterior (𝟙, ½) is invariant, θ_γ maps the local run of the reference tile to that of tile γ. In this section run 1 is H^β and run 2 is the true run. Win_{β,i}, LC^Ω_{β,i}, LC^Z_{β,i} and G_{β,<i} are the events of §6.4 for the local run of β; they are functions of the tile data of β.

**Lemma 7.1 (windows are fresh)** [proved from (K), (MI-1)–(MI-3)]. For every tile β and level i, P(Win_{β,i} | ℱ_{i−1}) ≤ η_i := e^{−ϖ_k}(2L^{b'})^{−(k−i)}. Given ℱ_{i−1}, the events Win_{β,i} for distinct tiles are independent.

*Proof.* Let τ be a potential (B)-site of level i located in β, examined in the local run or not. Its local-run pass weight p¹_τ is a function of U^β and of the uniforms of β other than u_τ. For a collar or rim site, p¹_τ is computed from 𝒜 after the background of step i, which reads no collar or rim uniform. For a (B)-test of 𝐑 it reads stored values fixed earlier. Since u_τ is uniform and independent of those variables (MI-1), P(|u_τ − p¹_τ| ≤ ε_i | U, the other uniforms) ≤ 2ε_i. There are at most 𝔎_i such sites in β ((6.3)), so a union bound and the tower property give P(Win_{β,i} | ℱ_{i−1}) ≤ 2ε_i𝔎_i = η_i. Win_{β,i} is a function of ℱ_{i−1}-measurable data and of the level-i uniforms located in β. These families are independent for distinct β and independent of ℱ_{i−1}. ∎

### 7.2 Paying for long clusters

R and e₀ are the constants of §6.4. A K in LC^Ω_{β,i} has sup-extent ≥ (D_i/2)ℓ_i + (m₁ − 13 − 4w − r_T)c_i = (D_i/2)ℓ_i + (3 + e₀)c_i. A K in LC^Z_{β,i} has sup-extent ≥ D_iℓ_i + (m₂ − r_bx − 4 − 3w − b₁)c_i = D_iℓ_i + (3w + e₀)c_i. The distances are as in M3 and in the proof of Lemma 6.6. Both are ≥ E_i := (D_i/2)ℓ_i + e₀c_i.

Call a level-i cell *near-live* in the true run if it lies within R cells of a cell of 𝒵_i or of a level-i cell meeting 𝒵_{i−1}. Call it a *trigger cell* if it contains a bond b with Trig_i(b) (§3.6).

**Lemma 7.2 (what a long cluster is in the true run)** [proved from Theorem 6.7 M1–M6, (R3), SA L17325, L23265].
 - (a) On G_{β,<i} ∩ LC^Ω_{β,i}, the true run has a w-connected set of near-live level-i cells in β of extent ≥ E_i.
 - (b) On G_{β,<i} ∩ LC^Z_{β,i} ∩ (Win_{β,i} ∪ LC^Ω_{β,i})^c, the true run has a w-connected set of level-i cells in β of extent ≥ E_i, each of which is near-live or a trigger cell.

*Proof.* (a) By M1–M2, Ω_i is the same in both runs on A_i^{(1)}, so K is a w-connected set of cells of the true Ω_i^c. Each cell of Ω_i^c = Q'^{~2} ∪ P'^{~4} ∪ Ŷ^{~8} lies within 9 cells of a cell of P' ∪ Q', whose cells are creations of step i and hence live at level i (SA L17325, L23265), or of a cell meeting Y = 𝒵_{i−1}.

(b) By M5–M6, Z_i^{[0]} and the would-be decisions are the same in both runs on J_i^♮. A cell of Z^{[0]} lies within 2 + 9 + b₁ cells of a live cell: R' cells are creations, and boxing adds ≤ b₁. A cell containing a would-be failure contains a bond b with |𝒜^{true}(b)| > θ_colδ_{i−1}: the lower collar threshold, the smaller of the two lower thresholds. Either 𝔡(b)^{+2} meets a cell of the true Z_i^{pre}, or it does not. In the first case: rounds-added cells are creations (failed collar and rim cells are in 𝒲^∧) or lie within b₁ + 1 cells of creations, so the cell is within 2 + 12 + b₁ = R cells of a live cell. In the second case b ∉ Z_i^{pre} and b ∈ Ω_i, so b ∈ Λ_i^{pre} and Trig_i(b) holds. ∎

**Lemma 7.3 (cluster payment)** [proved from (MB+T)]. Let i ≤ k and n ≤ k. For each tile γ of a tiling let 𝔷_γ := θ_γ𝔷 be the copies of a deep level-n cell. Let 𝒮_{γ,i} be the true-run event of Lemma 7.2(b) in tile γ (which contains that of (a)), and let 𝔄 := ∩_γE^{(n)}_{𝔷_γ}(i − 1), the sure event if i ≤ n. Suppose (F1) and (F4) of Theorem 7.4 hold. Then

  ν̃(𝔄 ∩ ∩_γ𝒮_{γ,i}) ≤ [e^{−c_ar_k(i−n)^+}e^{−2ϖ_k}(2L^{b'})^{−2(k−i)}]^𝒩.

*Proof.* Fix γ.
 1. *A path.* Take two cells of the set at sup-distance ≥ E_i − c_i and a w-path between them inside the set, made simple. Consecutive cells of a w-path are within (2w + 1)c_i of each other, so the path has at least N₀ := ⌈(E_i − c_i)/((2w + 1)c_i)⌉ ≥ 7(4R + 11)⁴ distinct cells. Keep its first N₀ cells P_γ.
 2. *A separated subset.* Choose greedily cells of P_γ pairwise at sup-distance ≥ (2R + 5)c_i. Each choice excludes at most (4R + 11)⁴ path cells, so N'' ≥ N₀/(4R + 11)⁴ ≥ 7 cells are chosen. Drop the chosen cells within (R + 3)c_i of 𝔷_γ; by separation this drops at most one.
 3. *Designations.* For each remaining chosen cell, designate either a live cell within R (of level i, or a level-(i − 1) cell of 𝒵_{i−1} inside a level-i cell), or a bond b with Trig_i(b) in it. Separation makes the designated live cells distinct at each level. It makes the 𝔡(b)^{+2} pairwise disjoint and disjoint from the other designations and from the ancestors of 𝔷_γ at levels i and i − 1.
 4. *Union bound.* The event 𝔄 ∩ ∩_γ𝒮_{γ,i} is contained in the union, over the choices of (P_γ, designations)_γ, of the (MB+T) events. Each such event designates 𝔷_γ (survival from n to i − 1) and N_γ ≥ N''_γ − 1 ≥ (6/7)N''_γ further cells or triggers per tile.
 5. *Cost per designation.* By (3.2), each designation costs at least ϰ_i := min{2c_ar_i − C_D, c_Tp₀(g_i)² − C_T}, using r_{i−1} ≥ r_i.
 6. *Entropy per tile.* At most 𝗇⁴L^{4(k−i)} starting cells (the level-i cells of a tile; Ř_k ≤ Ř_i). At most (4w + 1)^{4N₀} continuations. At most D_des := 4(2R + 1)⁴L⁴(MŘ_i)⁴ options per designation. Since N₀ ≤ (4R + 11)⁴N''_γ, the exponent per tile is at most N''_γ[(4R + 11)⁴·4 log(4w + 1) + log D_des − (6/7)ϰ_i] ≤ −N''_γϰ_i/3, by (F4)(ii).
 7. *Assembly.* Together with e^{B_k|𝕋^{(k)}|}e^{C_D𝒩}e^{−2c_a𝒩Σ_{j=n}^{i−1}r_j} from (3.2), the per-tile factor is ≤ 𝗇⁴L^{4(k−i)}·e^{B_kV_T + C_D − 2c_aΣ_{j=n}^{i−1}r_j}·e^{−N''_γϰ_i/3}.
 8. *Case i ≤ n.* The sum over j is empty. Use B_kV_T + C_D ≤ c_ar_k (F1) and N''_γϰ_i/6 ≥ ϰ_i ≥ c_ar_k ((F4)(i), N'' ≥ 6) to absorb e^{B_kV_T + C_D}. The remaining e^{−N''_γϰ_i/6} is ≤ e^{−δD_i}, since N''_γ ≥ N₀/(4R + 11)⁴ ≥ D_i/(2(2w + 1)(4R + 11)⁴MŘ_i) and (F4)(iii).
 9. *Case i > n.* Use (F1) and Σ_{j=n}^{i−1}r_j ≥ r_k(i − n) to get e^{−c_ar_k(i−n)}, and the whole e^{−N''_γϰ_i/3} ≤ e^{−δD_i}.
 10. *Conclusion.* By (6.4), e^{−δD_i} = e^{−2ϖ_k}(2L^{b'})^{−2(k−i)}(κ_T/(16C_q𝔎_i²))². Since 𝔎_i ≥ 𝗇⁴L^{4(k−i)}, 𝗇⁴L^{4(k−i)}e^{−δD_i} ≤ e^{−2ϖ_k}(2L^{b'})^{−2(k−i)}. ∎

### 7.3 The theorem

**Theorem 7.4 (Theorem F″)** [proved from (K)+(MI), (COV), (SM), Theorem 6.7 (hence (RS), (BGL), (R3)), Lemmas 7.1–7.3 (hence (MB+T)), LG1(3)]. Let x_k ≥ X_F, where X_F is such that Lemma 6.1 holds and:
 - (F1) B_kV_T + C_D ≤ c_ar_k;
 - (F2) c_ar_k ≥ ϖ_k + log(4L^{b'});
 - (F3) 160𝗇⁴(10e^{−ϖ_k})^{1/512} ≤ ½;
 - (F4) for every i ≤ k: (i) ϰ_i ≥ c_ar_k; (ii) ϰ_i/3 ≥ (4R + 11)⁴·4 log(4w + 1) + log(4(2R + 1)⁴L⁴(MŘ_i)⁴); (iii) ϰ_i ≥ 12δ(2w + 1)(4R + 11)⁴MŘ_i.

Then for every n ≤ k and level-n cell 𝔷, ν̃(E^{(n)}_𝔷(k)) ≤ 10e^{−ϖ_k}(2L^{b'})^{−(k−n)}, and

  Σ_{a≥0} L^{8a} sup_c ν̃(𝔏_k^{≥a}(c)) ≤ C_F𝗇⁸e^{−ϖ_k},  ϖ_k = δ𝗇MŘ_k/512 ≥ (δ𝗇M/512)(log x_k)²,   (7.1)

with C_F absolute.

*X_F exists.* ϖ_k/(c_ar_k) = δ𝗇/(512c_aM³Ř_k⁴) → 0. B_kV_T/(c_ar_k) ≤ C_B(1 + log x_k)𝗇⁴/(c_aŘ_k) → 0. ϖ_k → ∞. For (F4) use r_i ≥ r_k, Ř_i ≥ Ř_k and p₀(g_i)² ≥ ½p₀(g_k)² for i ≤ k (frame bound, IN1 (F): x_i ≥ x_k − c₅). Then c_ap₀(g_k)²/(M⁴Ř_k⁵) → ∞ (𝔭₀ > 6r gives 2𝔭₀ > 5r). (iii)'s first alternative needs M³ ≥ 12δ(2w + 1)(4R + 11)⁴/c_a, a floor on M. The logarithmic terms are o(ϰ_i).

*Proof.*

**Step 1 (domination).** Choose a tiling in which 𝔷 is deep, and let β be its tile. Define the tile functions:

  f_∅ := 𝟏{G_{β,<k+1}}𝟏{E^{(n)}_𝔷(k) in H^β},
  f^W_i := 𝟏{G_{β,<i} ∩ Win_{β,i}}𝟏{E^{(n)}_𝔷(i − 1) in H^β},
  f^Ω_i := 𝟏{G_{β,<i} ∩ LC^Ω_{β,i}}𝟏{E^{(n)}_𝔷(i − 1) in H^β},
  f^Z_i := 𝟏{G_{β,<i} ∩ LC^Z_{β,i} ∖ (Win_{β,i} ∪ LC^Ω_{β,i})}𝟏{E^{(n)}_𝔷(i − 1) in H^β}  (1 ≤ i ≤ k),

with E^{(n)}_𝔷(i − 1) the sure event when i ≤ n. The events G_{β,<k+1} and G_{β,<i} ∩ (Win_{β,i} ∪ LC_{β,i}) (1 ≤ i ≤ k) cover the sample space: the first level with a bad event, or none. On G_{β,<k+1}, Corollary 6.8 identifies the true survival of 𝔷 with that of H^β. At the first bad level i it does so up to level i − 1. Hence

  𝟏{E^{(n)}_𝔷(k)} ≤ f_∅ + Σ_{i=1}^k (f^W_i + f^Ω_i + f^Z_i).   (7.2)

**Step 2 (norms).** Copies θ_γ𝔷 lie in distinct tiles, so their ancestors are distinct at every level.
 - (a) Π_γθ_γf_∅ ≤ 𝟏{∩_γE^{(n)}_{θ_γ𝔷}(k) in the true run} (Corollary 6.8 in each tile). By (3.1) and Lemma 3.2, ‖f_∅‖_ch ≤ e^{B_kV_T + C_D − 2c_aΣ_{j=n}^k r_j} ≤ e^{−c_ar_k(k−n+1)} ≤ ½e^{−ϖ_k}(2L^{b'})^{−(k−n)}, by (F1), (F2).
 - (b) For i ≤ n, Π_γθ_γf^W_i ≤ Π_γ𝟏_{Win_{γ,i}}, and by Lemma 7.1, E Π_γ𝟏_{Win_{γ,i}} = E Π_γP(Win_{γ,i} | ℱ_{i−1}) ≤ η_i^𝒩, so ‖f^W_i‖_ch ≤ η_i. For i > n, Π_γθ_γf^W_i ≤ 𝟏_𝔄Π_γ𝟏_{Win_{γ,i}} with 𝔄 := ∩_γ{E^{(n)}_{θ_γ𝔷}(i − 1) true} ∈ ℱ_{i−1}. Then E ≤ η_i^𝒩ν̃(𝔄) ≤ η_i^𝒩exp(B_k|𝕋^{(k)}| + 𝒩(C_D − 2c_aΣ_{j=n}^{i−1}r_j)), so ‖f^W_i‖_ch ≤ η_ie^{−c_ar_k(i−n)} by (F1).
 - (c) By Lemma 7.2, Π_γθ_γf^Ω_i and Π_γθ_γf^Z_i are ≤ 𝟏{𝔄 ∩ ∩_γ𝒮_{γ,i}}. By Lemma 7.3 and the 𝒩-th root, ‖f^Ω_i‖_ch, ‖f^Z_i‖_ch ≤ e^{−c_ar_k(i−n)^+}e^{−2ϖ_k}(2L^{b'})^{−2(k−i)} ≤ e^{−c_ar_k(i−n)^+}η_i.

**Step 3 (one cell).** By (7.2) and Lemma 3.1 (other tiles ≡ 1),

  ν̃(E^{(n)}_𝔷(k)) ≤ ½e^{−ϖ_k}(2L^{b'})^{−(k−n)} + 3Σ_{i≤n}η_i + 3Σ_{n<i≤k}η_ie^{−c_ar_k(i−n)} ≤ e^{−ϖ_k}(2L^{b'})^{−(k−n)}[½ + 3Σ_{s≥0}(2L^{b'})^{−s} + 3Σ_{s≥1}(2L^{b'}e^{−c_ar_k})^s] ≤ 10e^{−ϖ_k}(2L^{b'})^{−(k−n)},

using η_i = e^{−ϖ_k}(2L^{b'})^{−(k−n)}(2L^{b'})^{i−n} and 2L^{b'}e^{−c_ar_k} ≤ ½ (F2).

**Step 4 (joint events).** Let 𝔷 be deep in β₀, and let level-k cells 𝔠₁, …, 𝔠_m be deep in distinct tiles β₁, …, β_m ≠ β₀ of one tiling. Apply (7.2) in each of the m + 1 tiles (for lv_k(𝔠_s), n = k) and multiply. Expand the product, apply Lemma 3.1 to each term, and re-sum:

  ν̃(E^{(n)}_𝔷(k) ∩ ∩_{s≤m}lv_k(𝔠_s)) ≤ 10e^{−ϖ_k}(2L^{b'})^{−(k−n)}(10e^{−ϖ_k})^m.   (7.3)

**Step 5 (anchors).** Fix a reference tiling τ₀, whose tiles are called *boxes*. On 𝔏_k^{≥a}(c), Lemma 1.1 gives a live component C ∋ c and a level-(k − a) cell 𝔷 ⊂ C with E^{(k−a)}_𝔷(k), so ν̃(𝔏_k^{≥a}(c)) ≤ Σ_𝔷ν̃(E^{(k−a)}_𝔷(k) ∩ {𝔷 ∼ c}), where 𝔷 ∼ c means 𝔷 and c lie in the same live component. A level-k cell contains at most L^{4a} level-(k − a) cells (the side of a level-j cell is MŘ_jℓ_j ≥ MŘ_kℓ_j). So a box contains ≤ 𝗇⁴L^{4a} candidates, and the boxes at box-distance i from the box of c number ≤ (2i + 1)⁴.
 - *Near anchors* (i < 512): Step 3 gives ≤ 1025⁴𝗇⁴L^{4a}·10e^{−ϖ_k}(2L^{b'})^{−a}.
 - *Far anchors* (i ≥ 512). C is connected, so it meets a chain B₀, …, B_{i'} of distinct, consecutively adjacent boxes from the box of c to that of 𝔷, with i' ≥ i, each containing a cell 𝔠_s ⊂ C live at level k. Take the 2⁴ tilings τ_ε whose faces are displaced by ε_μ⌊𝗇/4⌋ cells from a corner of the level-k cell of 𝔷 (SA L23336). Every level-k cell is deep in one of them, and 𝔷 is deep in all sixteen (R1 L213, unchanged). By pigeonhole one τ_ε has ≥ (i' + 1)/16 of the 𝔠_s deep. A τ_ε-tile meets ≤ 2⁴ boxes, so these cells lie in ≥ (i' + 1)/256 distinct tiles, and m ≥ i'/512 of them are other than the tile of 𝔷. Union over: ε (16 choices), the box path (≤ 80^{i'}), the cells (≤ 𝗇^{4(i'+1)}) and the subset kept (≤ 2^{i'+1}). With (7.3) and (F3):

  ν̃(E^{(k−a)}_𝔷(k) ∩ {𝔷 ∼ c}) ≤ 16·10e^{−ϖ_k}(2L^{b'})^{−a}Σ_{i'≥i}2𝗇⁴(160𝗇⁴(10e^{−ϖ_k})^{1/512})^{i'} ≤ 640𝗇⁴e^{−ϖ_k}(2L^{b'})^{−a}2^{−i}.

Summing over the ≤ (2i + 1)⁴𝗇⁴L^{4a} anchors at distance i and over i ≥ 512 gives ≤ C𝗇⁸L^{4a}e^{−ϖ_k}(2L^{b'})^{−a}.

**Step 6 (the age series).** With b' = 13, ν̃(𝔏_k^{≥a}(c)) ≤ C𝗇⁸L^{4a}e^{−ϖ_k}(2L^{13})^{−a} uniformly in c. So Σ_aL^{8a}ν̃(𝔏_k^{≥a}(c)) ≤ C𝗇⁸e^{−ϖ_k}Σ_a(L^{12}/(2L^{13}))^a ≤ 2C𝗇⁸e^{−ϖ_k}. Small tori: Lemma 3.3, with (3.1) applied directly. ∎

**Remark 7.5 (the rate).** ϖ_k has degree r in log x_k, while p₀ has degree 𝔭₀ > 6r. The rate is set by the margin budget: each level's decoupling length D_i must fit, summed over levels, into one eighth of the tile (Lemma 6.1). It is not set by the survival charge c_ar_k, which is far larger. A rate e^{−cp₀} would need either a different locality mechanism or the first-moment route of SA Theorem 4.13 (R1 Remark 4.6). Lemma 1.3 makes it unnecessary for TP1.

**Remark 7.6 (what Theorem F″ does not use).** No fresh event per level, no (H), no constrained-versus-free comparison at fixed coarse data, no conditional *density* of a fluctuation value, no prolongation of the run and no depth floor. The measure inputs are the unconditional exponential moments (3.1) and (3.2).

---

## 8. AG-k₁ in the form TP1 needs, and TP1's Lemmas 6.5 and 6.6 (Task 3)

### 8.1 The statement

**Lemma AG-k₁*** [proved as an implication: Theorem 7.4 with its inputs; (TT) outstanding]. Let the construction be SA's with (SM) and κ_T = 1/4. There are C_AG and c₀ > 0, and a ceiling γ_AG on g, such that the following holds for g ≤ min{γ_W, γ_AG}, every first-passage datum, every compatible torus, every level k with x_k ≥ g^{−2} and every cell c of level k:

  Σ_{a≥0} L^{8a} P^{(k)}(𝔏_k^{≥a}(c)) ≤ C_AG e^{−ϖ_k},  ϖ_k = δ𝗇MŘ_k/512 ≥ c₀(log x_k)²,   (8.1)

with c₀ := δ𝗇M/512 and C_AG := C_F𝗇⁸. Here P^{(k)} is TP1's unsourced positive law at level k, the law ν̃ of the run stopped at level k (§3.3, "Which run").

*Proof.* γ_AG is chosen so that g^{−2} ≥ X_F; then x_k ≥ g^{−2} gives x_k ≥ X_F, and Theorem 7.4 gives (7.1), which is (8.1). Ř_k ≥ (log x_k)^r with r ≥ 2 gives ϖ_k ≥ c₀(log x_k)². ∎

*Relation to TP1's (10.1).* (8.1) has the rate e^{−c₀(log x_k)²} in place of C(log x_k)^Ce^{−cp₀(g_k)}. TP1 reads (10.1) only through (6.3), so only the rate's behaviour against powers of log x matters (Proposition 8.2).

*Relation to the assembly's AG1* (assembly L351). Step 3 of Theorem 7.4 gives the survival bound ν̃(E^{(n)}_𝔷(k)) ≤ 10e^{−ϖ_k}(2L^{13})^{−(k−n)}. This is a summable r(k − n) with every moment L^{bm}, b ≤ 12, uniformly in volume and position. The assembly's further clause, that "witness selection, reflection replication and pattern counting preserve the insertion and source weights", is not proved here. TP1 does not read it (TP1 L489–491; R1 Remark 4.5).

*The construction TP1 reads.* TP1's inputs (TP-pres), (TP-live), (TP-cx), (TP-far) (TP1 L97–135) are statements about the sourced construction at level k₁. With (SM) they are statements about the smooth-test construction. Theorem 5.4 item 20 places them among the pass-side consumers. TP1 must read them for that construction, which changes no constant beyond the factor 5/4 in pass-side bounds.

### 8.2 The consequences

**Lemma 8.1** [proved]. For fixed C' ≥ 0 and c > 0, (log x)^{C'}e^{−c(log(x/2))²} → 0 as x → ∞.

*Proof.* Put y := log x. For y ≥ 2 log 2, log(x/2) = y − log 2 ≥ y/2. So the expression is ≤ exp(C' log y − cy²/4) → 0. ∎

**Proposition 8.2 (TP1 with AG-k₁*)** [proved from AG-k₁* at k = k₁ and TP1's own proofs]. Replace TP1's (6.3) (TP1 L377) by

  𝔄 ≤ C(MŘ_{k₁})⁴ Σ_{a≥0} L^{8a} sup_c P(𝔏_{k₁}^{≥a}(c)) ≤ C C_AG M⁴L⁴(log(2x))^{4r} e^{−c₀(log(x/2))²} =: 𝔄*(x).   (6.3*)

Then TP1's Lemma 6.5 (E_PΦ₁₂ = Γ₁₂ + o(x^{−2})), Lemma 6.6 (|Cov_P(Φ₁, Φ₂)| = o(x^{−2})) and Proposition RL hold as stated.

*Proof.*
 1. *(6.3*).* The first inequality is TP1's own counting (TP1 L373–377: "O(1)·(CMŘ_{k₁})⁴ cells of level k₁ meet the neighbourhood"). Its inputs are TP1's: E[L^{8a(y)}𝟙_Λ] ≤ Σ_c Σ_{a'≥0}L^{8a'}P(a(y) ≥ a' and a live component of age ≥ a' meets c), since L^{8a} ≤ Σ_{a'≤a}L^{8a'}. The second uses (8.1) with ϖ_{k₁} ≥ c₀(log x_{k₁})². Also x_{k₁} ≥ x/2, which TP1 uses in the proof of Lemma 6.5 (TP1 L381: "p₀(g_{k₁}) = (log x_{k₁})^{𝔭₀} ≥ (log(x/2))^{𝔭₀}"), and Ř_{k₁} ≤ L(log x_{k₁})^r with x_{k₁} ≤ 2x.
 2. *Lemma 6.5.* TP1's proof (TP1 L381) splits E_PΦ₁₂ over Λ and Λ^c. The Λ-part is bounded by Cx^{−2}(log x)^C(𝔄 + P(Λ))‖f‖‖h‖ ≤ 2Cx^{−2}(log x)^C𝔄‖f‖‖h‖, with P(Λ) ≤ 𝔄 unchanged, and |Γ₁₂|P(Λ) ≤ Cx^{−2}𝔄‖f‖‖h‖. The only use of the rate is "(log x)^{2C}e^{−cp₀(g_{k₁})} → 0". Replace it by (log x)^{2C}𝔄*(x) → 0, which is Lemma 8.1 with C' = 2C + 4r (constants M⁴L⁴ absorbed).
 3. *Lemma 6.6.* TP1's proof (TP1 L389–391) gives |Cov_P(Φ₁, Φ₂)| ≤ Cx^{−2}[(log x)^Cx^{−4} + e^{−cd̂} + (log x)^C𝔄^{1/2}]²‖f‖‖h‖. The only use of the rate is (log x)^C𝔄^{1/2} → 0. Here 𝔄*(x)^{1/2} ≤ C'(log 2x)^{2r}e^{−(c₀/2)(log(x/2))²}, so Lemma 8.1 with c = c₀/2 gives it.
 4. *Proposition RL* (TP1 L393–399). Its error list ends with "e^{−cp₀(g_{k₁})}·(log x)^C". This becomes (log x)^C𝔄*(x) → 0 (Lemma 8.1). So ε_RL(d) → 0 as before. The threshold d₀ now also depends on γ_AG, through g ≤ γ_AG. ∎

So TP1(1)–(5) hold with AG-k₁* in place of (10.1), with all other TP-inputs unchanged (given item 20 of Theorem 5.4).

---

## 9. Constants and their order

The IN1 constraint: constants fixed before κ, independent of M and κ̄, and M only as a lower bound. AG1's constants feed no choice of IN1. They enter only TP1, and through (SM) the room conditions (5.1)–(5.6).

| Constant | Defined | Fixed | Depends on | M, κ̄ |
|---|---|---|---|---|
| κ_T = 1/4 | §5.1 | first, before L | none | independent |
| ζ | §5.1 | with κ_T | κ_T | independent |
| room (5.1)–(5.6) | §5.4 | at SA's own positions | κ_T and SA's constants | SA's existing floors only |
| δ = δ₀/8 | (BGL) | with L (δ₀ "fixed together with L", SA L17334) | L | independent |
| C_bg | (BGL) | with L, ρ, μ (A1/A3 constants, `c4-order.md` rows ≤ 7) | L, ρ, μ | independent |
| r_T, b₁, r_bx, w, R, e₀, m₁, m₂, m₃, m₀, C_R, N_τ | §6.4, §7.2, (R3), (K) | with L | SA's geometric O(1)s | independent |
| C_L | Lemma 6.1 | with L | L, r, B_♯ | independent |
| 𝗇 | §3.4 | after m₀, C_L, before κ | m₀, C_L | independent |
| b' = 13 | §6.4 | absolute | — | independent |
| C_q | (6.2) | after A₀/A₁, Θ₁, θ_c, c_R | C_bg, A₀/A₁, θ_min | depends on A₀/A₁ (chosen after M) |
| ϖ_k | (6.3) | derived | δ, 𝗇, M, Ř_k | linear in M; M only improves the rate |
| floors on M | Lemma 6.1; (F4)(iii) via c_a ≥ 1 | after L, δ, 𝗇, w, R | L, δ, 𝗇, C_L, w, R | lower bounds only |
| c_a | (MB) | SA's position, (ϱ, c_a) after γ | — | — |
| c_T, C_T | (TT) | input constants | presumably θ_col²(A₁/A₀)² | enter only (F4) |
| X_F, γ_AG | Theorem 7.4, §8.1 | last: ceilings on g | everything | — |

*The one constant that is not independent of M.* C_q contains A₀/A₁, which SA chooses after M (SA L19469: (A₁, A₀, …) after M). C_q enters only D_i, through log C_q. D_i enters only the margins, and the margins enter only the floor x_k ≥ X_F of Lemma 6.1, which is a ceiling on g, the last choice. No constant chosen before g reads C_q, so no cycle arises. The constraint holds in the sense that matters: every constant that a choice before κ reads is fixed before κ and independent of M and κ̄.

---

## 10. Status, the first remaining Outstanding statement, and the attacks

### 10.1 The first remaining Outstanding statement: (TT)

AG1's deterministic content, (QL′), is proved as an implication (Theorem 6.7). AG1's measure content is Theorem 7.4, proved as an implication. The one input on its path that no other submanuscript yet states is (TT), the trigger clause (3.2) of §3.6.

**(TT), restated.** Deep triggers cost e^{−c_Tp₀(g_i)²} each, jointly with the moment bound (MB). A *deep trigger* at level i is a bond b of level i − 1 with: b in the small-field region Λ_i^{pre} of step i; no large-field cell of step i (before 𝐑) within two cells of b's cell; and |𝒜_{i−1}(b)| > θ_colδ_{i−1}, with θ_col = 1/(4Θ₁) the collar fraction.

**Why AG1 needs it.** LC^Z_i is the trigger part of SA's long-cluster hypothesis (Lemma 6.4, Lemma 7.2(b)). It must be paid in the true run. The cells of a crossing cluster that are not near a live cell are deep triggers. They are bonds of the true run's small-field region where the fluctuation that step i integrates exceeds the collar threshold. Nothing in the history records them, so (MB) does not see them.

**Why it should hold.** At a deep bond the conditional mean of the integrated fluctuation is ≤ Cδ_{i−1}e^{−cMŘ_i}: the kernel of 𝐦 decays exponentially (SA L17360), and b is two cells from every stored bond. Its scaled size θ_col(A₁/A₀)p₀(g_{i−1}) is far above the Gaussian scale 1. A Gaussian with these parameters has tail e^{−c(θ_col(A₁/A₀))²p₀²}. SA asserts the payment: "The price of such a cell is borne by the conditional law of the fluctuation field in its box" (SA L23328).

**Lemma 10.1 (reduction)** [proved]. Suppose the per-history form (TT-hist) holds: for every history h of level k and every 𝔅 satisfying the geometric conditions of (TT) in h (they are h-measurable),

  t(h; ∩_{b∈𝔅}Trig(b)) ≤ Π_{b∈𝔅}(C_Te^{−c_Tp₀(g_{i(b)})²}) · t(h),   (10.1)

where t(h; T) := Z·μ⊗λ({H_k = h} ∩ T). Then (TT) holds.

*Proof.* The survival events of (3.2) are unions of histories. So ν̃(∩E ∩ ∩Trig) = Z^{−1}Σ_{h∈∩E}t(h; ∩Trig) ≤ Π(C_Te^{−c_Tp₀²})·ν̃(∩E). Then apply (3.1), which holds by Lemma E.4. ∎

(TT-hist) would follow from a bound on one step: the step-i conditional integral of the fluctuation on Λ_i, with the indicators 𝟏{|A(b)| > θ_colδ} inserted at deep bonds, should be at most (C_Te^{−c_Tp₀²})^{|𝔅|} times the integral without them, for every value of the retained variables. Positivity of the later kernels then carries the bound to t(h). That one-step bound is not proved here (attack T5 below).

### 10.2 The attacks on the trigger obstruction, and why each fails

- **T1 — single-pass tests (make the rounds local by redesign).** *Idea.* Test every bond of Ω_t once, at the collar and rim thresholds, before forming Λ_t. Put every failure, with two layers, into Z_t. The rounds then disappear and Z_t is a local function of local decisions (Lemma 6.5). *Exact reason it fails.* Every bond of the final Λ_t has then passed the collar test, so the Λ-integral is cut at δ_k/(4Θ₁) everywhere. The stored boundary data have the same bound (1 + κ_T)δ_k/(4Θ₁). Let C_K be the norm, from sup to sup, of A' ↦ 𝐦 = −C^{(k)}(Λ_t)Δ^{(k)}A' at bonds next to ∂Λ_t. NL1's small-field tail term (item 7 of §5.4) needs |𝐦| ≤ ½ of the inner cut, that is C_K(1 + κ_T) ≤ ½. Nothing gives C_K ≤ 2/5. For the scalar lattice Laplacian with Dirichlet data, constant boundary data extend to the same constant, so the analogous constant is 1. For the constrained fluctuation Hessian it is a fixed constant of order one that no source bounds. SA's design never needs C_K to be small: the boundary data are smaller than the inner cut by the factor 4Θ₁θ_c ≥ 4C (SA L17364), and C absorbs C_K. Only a greedy enlargement produces boundary data that small, and the greedy enlargement is the rounds.
- **T2 — record triggers as decisions, or make deep triggers creations.** *Idea.* Give every bond a recorded trigger test at θ_col. Chains of recorded failures then agree in both runs, and they are history events that (MB) might pay. Or make deep trigger failures creations, so that C3's stored-Gaussian certificate pays them. *Exact reason it fails.* A recorded test with pass weight ζ(|A|/θ_col) cuts the Λ-integral at θ_col on its pass branch. Near any hole, including the holes the deep creations make, the mean is again of the order of the boundary data θ_colδ (T1's failure). If instead triggers are recorded only far from large-field cells, "far" depends on the final region, which depends on the rounds: circular. A deep trigger that stays in Λ still has to be paid by the integrated fluctuation's tail, which is (TT) again.
- **T3 — the bare Wilson stability quotient with the chessboard.** *Idea.* A trigger forces a local action excess ≥ cθ_col²δ² relative to the background, a certificate like IN1 Lemma C.3(ii). So ∫𝟏_𝒮e^{−βA} ≤ e^{−(β/2)inf_𝒮A}Z(β/2), and the chessboard divides the Haar normalisation among the tiles. *Exact reason it fails.* Z(β/2)/Z(β) ≤ e^{C|T_bare|(1+log β)} counts *bare* sites. Per tile that is 𝗇⁴(MŘ_k)⁴L^{4k} sites at coupling β, which no level-i cost can beat. Only the RG quotient (MB), with B_k per *level-k* site, has a usable volume factor. It sees only what the history records.
- **T4 — monotone sandwich of local runs.** *Idea.* Run the local construction with a maximal exterior (everything outside J_i large-field) and with a minimal one. If the rules were monotone, the true region would lie between them, and a crossing chain of the maximal run would be a recorded chain of the true run. *Exact reason it fails.* (i) The rounds are not monotone. A larger region examines different collar bonds. A failure that the greedy rule adds with its layer ^~ need not lie in a larger admissible region, so the greedy result is not the least admissible enlargement (§6.5, discussion before Lemma 6.6). Boxing is not monotone either, since a component can grow past the box size. (ii) Even with monotonicity, a tile function cannot certify that the *true* run examined a chain. That is the whole difficulty: the true run's growth into the tile is a true-run event, not a tile event, and the chessboard (Lemma 3.1) needs tile functions.
- **T5 — the conditional law in a box (SA's sentence, made precise).** *Idea.* Prove (10.1) one step at a time. Fix a deep bond b and condition on the integrated field outside a box B' of half-cell radius around b. Inside B' the density is Gaussian: coercive by A2 (PR1(1), [C]). It is perturbed by terms whose oscillation over B' is ≤ C|B'|, using the class bounds (ii) of IN1 D.1 (SA L17267–17270). It is cut by the inner tests. The tail of A(b) is then ≤ 4e^{2C|B'|}e^{−c(θ_colA₁p₀/A₀)²}, and |B'| ≈ (MŘ_iL)⁴ ≪ p₀². *Exact reason it stops.* The *denominator* needs a lower bound: the conditional probability that the inner tests in B' pass, given the outside, must be ≥ e^{−C|B'|} for *every* outside configuration on the support. Near ∂B' the conditional mean is the Dirichlet extension of outside values that are only known to be < δ. The fluctuation Hessian is a constrained vector operator with no maximum principle, so that extension can exceed the cut, and the denominator can then be e^{−cp₀²}. The ratio is then not small. Two routes around this remain unproved. The unconditional version needs the step's generating function E[e^{sA(b)}] at |s| ≈ θ_col(A₁/A₀)p₀ in scaled units, far outside SC1's source ball. A version averaged over outside configurations needs the step's conditional measure to be close to its Gaussian at fixed coarse data, which is the small-field part of what `rarity-fresh-x.md` called (SEP). The small-field part is milder than the marked sector at which (SEP) failed, but no source states it. So T5 reduces (TT) to a precise small-field statement on NL1's side, and stops there.

**Where they meet.** Every attack meets the same fact. Locality of SA's step fails only along chains of moderately large small-field fluctuations, and paying for such chains needs a tail bound for the integrated fluctuation that the history does not record. That bound is (TT). It is a tail statement, not a density statement: round 1's F3 needed a bounded conditional density at a window, and nothing here does.

### 10.3 Status of every statement

| Statement | Where | Status |
|---|---|---|
| Lemma 1.1 (anchor) | §1.1 | [proved] |
| Lemma 1.3 (rate e^{−c(log x)²} suffices) | §1.3, §8 | [proved] |
| Lemmas 2.1–2.3 | §2.4 | [proved] |
| (K), (COV) | §3.1–3.2 | [input: LF1] |
| (MB) (per-level charge) | §3.3 | [proved from (LT), (R0)–(R2)] (Lemma E.4) |
| (TT) | §3.6, §10.1 | **[outstanding]**; reduced to (10.1) by Lemma 10.1 |
| Lemmas 3.1–3.3 (chessboard, dilution, small tori) | §3.5 | [proved] (3.1 from LG1(3)) |
| Lemmas E.1–E.4 | §4 | [proved] from (R0)–(R2), (LT) |
| (R0)–(R3), (LT) | §4 | [input: LF1(2), LF1(3)] |
| (SM), random thresholds | §5.1 | design; equivalence [proved] |
| (MI-1)–(MI-7), Lemma 5.2 | §5.2 | [proved] from (MI-1)–(MI-3) |
| Lemma 5.3 (sandwich) | §5.3 | [proved] |
| Theorem 5.4 (threshold robustness, 20 consumers) | §5.4 | [proved] as an implication; item 16 (ST1) recorded as a requirement on ST1 |
| (RS) read structure | §6.1 | [input: LF1(2)]; checked against SA L17317–17610, L23328 only |
| (BGL) two-run background comparison | §6.2 | [input: BG1/PR1, checked conditional]; derivation [proved]; reading W = W̃ ∩ Ω₀ flagged |
| Lemma 6.2 (tested values, pass weights) | §6.2 | [proved] |
| Lemma 6.3 (crossing holes) | §6.3 | [proved]; obstruction to the proof, not a counterexample |
| Lemma 6.4 (rounds not tile-local) | §6.3 | [proved] from the rules; round 1's (QL) [not provable as stated] |
| Lemma 6.1 (margins) | §6.4 | [proved] |
| Lemma 6.5 (boxing local) | §6.4 | [proved] |
| Lemma 6.6 (rounds local off LC^Z) | §6.4 | [proved] |
| Theorem 6.7 (QL′) | §6.5 | [proved] from (RS), (BGL), (R3) |
| Corollary 6.8 | §6.5 | [proved] |
| Proposition 6.9 (geometric growth absorbed) | §6.6 | [proved] |
| Lemmas 7.1–7.3 | §7 | [proved] (7.3 from (MB+T)) |
| Theorem 7.4 (F″) = (0.1*) | §7.3 | [proved] from (K)+(MI), (COV), (SM), (RS), (BGL), (R0)–(R3), (LT), (TT), LG1(3) |
| AG-k₁*, Proposition 8.2 | §8 | [proved] as an implication |
| (0.1) with rate p₀ | §1.2 | not proved; not needed by TP1 |

### 10.4 What changed relative to round 1

- Round 1's first unchecked step is proved (Proposition 6.9). The cross-level influence of a stored field is e^{−δD_iL^{i−l}}, and any per-level geometric growth is absorbed.
- Round 1's (QL) is not provable as stated (Lemmas 6.3, 6.4). It is replaced by (QL′), which restores SA's long-cluster hypothesis (Theorem 6.7).
- Round 1's Theorem F becomes Theorem F″. It adds the long-cluster terms f^Ω, f^Z (Lemmas 7.2, 7.3), windows only at (B)-sites, factor-2 decay lengths, a rate ϖ_k = δ𝗇MŘ_k/512 in place of /128, and per-level charges in (MB).
- The threshold design is checked against its consumers (Theorem 5.4). The measure identity gets (MI-1)–(MI-7).
- The open core moves from a deterministic statement, (QL), to a measure statement of tail type, (TT), on NL1's side.
- Round 1's Theorem D (exact locality) and its F1, F3 are superseded. F1's reason still explains why tests cannot be made exactly local in the bare field (R1 L337–339). F3's reason still explains why windows must sit on uniforms (R1 L426–428).

*RAM and method.* No computation was run. Every source read was a bounded range, cited above.

End of round 2. Line count: see the final line.


This file has 795 lines.
