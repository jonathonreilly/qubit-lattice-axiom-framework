# OS, pass 1: the stage sequences of the R operation above k_♯ (Lemma OS of ST1)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, pass 1 (long draft) of the one open lemma of submanuscript ST1, `library/st1-draft.md` §18. Research text. It is not an audit, it grants no status, and no other model has checked it. A later pass distils it; a fresh session then reads it line by line.

Credit. The R operation, its stages, nests, collars, lifts and thresholds are Tadeusz Balaban's (CMP 122 (1989) 175-202 and 355-392, cited through the texts below). The four-dimensional outline `YM4_sketch_500.tex` ("SA") and the complete account `theorem_0_complete_account_raw_I.tex` ("CA-I") are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, commit `31a47c543775`. The three-dimensional manuscript `YM3_I.tex` ("Y3") at the same commit is theirs as well. Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable model of Balaban's background re-expansion. Library notes cited below are by Codex and Claude; each credits its own sources.

Line numbers. "SA L" is a line of `scratchpad/sa/ym4.tex`; "CA-I L" of `scratchpad/sa/ca_I.tex`; "Y3 L" of `scratchpad/sa/YM3_I.tex`. Library notes are cited as `note.md:line`. I read every range I cite in this session, unless I say I take it from a note.

Status words, as in ST1: **[proved here]**, **[port]**, **[import X]**, **[design]**, **[outstanding]**.

---

## 0. Summary

**Result.** Lemma OS, as stated in `st1-draft.md` §18.1, has a false premise. The premise is that the determining sequences of the stage structures at stage levels j > k_♯ are not separated. They are separated. What overlaps at those levels is the family of *collars* R_n = Z_{j+1} ∖ Z''_{j+1}, the regions whose stored variables successive stages integrate. A collar is an integration region. It is not a member of any determining sequence. After every stage, the determining sequence in force is a decreasing sequence whose consecutive members are separated by at least one M-cube of the later level, that is, by LM in the units of the earlier level (Lemma 2.3). This is the separation that SA L17398-17404 states for every stage sequence and every nest, and that CA-I L53780-53782 records from Balaban ("separated by one layer").

Consequently (Theorem 3.1), parts (i)-(iii) of Lemma OS hold at every stage, at every stage level, with the constants of the separated-sequence theorems BG1(2), PR1(2), PR1(1) taken at the *gap floor* ρ_0 = R₁M₁ and cube size 𝔐 = M₁ of SA L9593-9599, under one design condition on the localisation side M:

  (M-sep) M₁ divides M (both are powers of L, with aligned partitions), and LM ≥ R₁M₁.

The constants are independent of 𝖭_t, of the number of overlapping collars, of the number of shells, of depth and of volume. **They are also independent of M and of κ̄**, as the coordinator requires for IN1 (Section 5): M enters only through the lower bound (M-sep), never through a constant, and κ̄ does not enter at all. The per-shell decay is ω = μ ρ_0 for the relevant rate μ (profile rate δ_prof, or response weight θ_DR), and ω ≥ log 4 + 3 log L is a choice of the gap number R₁ after μ (Lemma 3.4).

**Route (a), redesign.** Not needed. I also show (Proposition 6.1) that a redesign that makes *all* collars disjoint is impossible inside the R operation as SA defines it: disjointness of the last two collars forces the prepared box Λ^pr to contain a whole level-(k − 1) cell, of side MŘ_{k−1}/L in level-k units, whereas SA's Proposition 2.4 needs a box of side O(M) so that C(M) is fixed before γ (SA L17612, L17656). So the overlap is forced by the purpose of the stages.

**Route (b), bounded overlap.** It works in the strongest form: the result needs no bound on the overlap number K of the collars at all, because the overlap of collars does not enter any determining sequence (Theorem 3.1). For the record, K ≤ N_0 + 2 with N_0 = k − k_0 the number of stages whose collars overlap (CA-I L65658-65660, L42907-42916).

**Two defects found in ST1's separated-case proofs, with repairs.** Reading the stage geometry closely shows two places where `st1-draft.md` does not yet apply as written, at overlapping *and* at disjoint collars. Neither is Lemma OS, but route (a) asks me to prove that the separated results of ST1 apply, so I treat both.

- **D1 (the phase gap at early stages).** Corollary E′ of ST1 says "The source 𝔛 lies in layer ≥ t − 1". At the preparatory stage n of the operation at level t, the source lies in layer j_n = t − 𝖭_t + n. The gap of (R22) at index j_n is θ_sβ_s 2^{−(t−j_n)}/(2𝖭_t), while the shift at the source has relative size of order δ′_{j_n}/ε_{j_n} with no decay. For t − j_n large the shift does not fit (Section 7.1). Repair [design + proved here]: a stage-graded term in the radius coefficient (Definition 7.2). With it, Lemma 7.3 keeps c_σ ≥ 1/2 and Corollary 7.5 replaces Corollary E′, under the condition (AMP-st), which (N-growth) implies.
- **D2 (the radius index on integrated collars).** After the stage at level j, the integrated collar R_n lies in layer j + 1 of the new sequence, but the stage tests bound the real background there only "in the scale j of the stage" (SA L17624), with the lift L_♭^{2e}. This is a factor of order L² L_♭^{2e} above the layer-(j + 1) scale. ST1's Definition 4.5 uses the layer as radius index, and its Theorem A assumes regularity at the highest layer index. Repair [design + proved here]: on integrated collars the radius index is the stage level, and the lift exponent is the one of SA L17624 (Definition 7.6); Theorem 7.7 then proves Theorem A's (L1) on the support of the stage tests.

**What is outstanding after this file.** No new lemma. Lemma OS is replaced by (M-sep), by the order requirement of Lemma 3.4 (R₁ after the rates), and by the two design repairs D1, D2, all proved here as implications from the same imports that ST1 uses. Two import statements must be read in their final form to confirm that their separation hypotheses are floors (Section 3.3, items (F-3) and (F-4)). This is a check of the import texts, not a new proof.

**First outstanding statement.** None at the level of Lemma OS. The nearest open item is the import floor check (F-3)-(F-4) of Section 3.3: that PR1(1) (the fibre precision bounds (I-1) of IN1 at layered pairs, PR-lay) and [import DR]'s premises [PW], [NL] are stated for every separated sequence whose gap is at least a fixed floor, with constants not depending on the gap above it. A1 and A3 are checked here to have that form (Lemma 3.2).

---

## 1. The statement under study and what the brief asks

`st1-draft.md:571` states Lemma OS: for "the determining sequence of every structure at such a stage (whose collars overlap those of earlier stages)", the conclusions of [import BG], [import PROF] and [import DR] hold "with constants independent of 𝖭_t, of the number of overlapping shells, of depth and of volume, and with a per-shell decay e^{−ω} ... ω ≥ log 4 + 3 log L". `st1-draft.md:143` gives the premise: "At stage levels j > k_♯ the collars overlap (SA L17624), and separation is not available." The three attacks of `st1-draft.md:577-581` all start from this premise. Attack 1 says that "there is no strip of width ρξ between the corresponding layers"; Attack 2 that "up to log_LŘ row levels meet within distance < ρξ of one site".

The brief adds the coordinator's requirement: any background or response theorem used at layered stage pairs must have constants fixed before κ̄, that is, independent of M and κ̄ (IN1 Theorems A.5-A.7, `in1-draft.md:217-316`). IN1 needs at the stage pairs only (I-1)(b)-(d): a uniform gap, entrywise exponential decay, and the pair-perturbation bound (`in1-draft.md:57-62`).

---

## 2. The geometry of the R operation, from the sources

### 2.1 Source findings

**SA L17575-17583 (the class).** A component X of Z_k is in the class when, for k_♭ ≤ i ≤ k, X ∩ Z_i is "a single component of Z_i and is small"; it is quiet and in quarantine. In it Ω_i^c ∩ X = H_i^{[8]} and Z_i ∩ X = H_i^{[10]} for k_♭ < i ≤ k, where H_i is the hull in level-i cells of X ∩ Z_{i−1}. SA L17459: "the cells of level t are MŘ_t-cubes".

**SA L17585 (the stages).** "for j = k_♭, …, k − 1, one value after another, the stored variables of the outer shell of Z_{j+1} ∩ X are integrated out as in a small-field step." What remains is a box Λ^pr of side at most CM, "In it the levels k_♭, …, k are stacked in thin shells". The core C_{k_♭} = X ∩ Z_{k_♭} has side at most CMŘ_{k_♭}L^{−𝖭_k} in level-k units.

**SA L17398-17407 (Proposition 2.3).** The label regions are nested "with gaps of at least cMŘ_j in level-j units". For the stage sequences, prepared sequences and drop-out nests: "In these sequences and nests the boxes are only unions of M-cubes, and the only lower bound on the gaps is one M-cube of the later level", displayed as dist_∞(Z_j, Ω_{j+1}) ≥ LM in level-j units (L17401). L17407: "Consequently the estimates of (1b), (1c) must hold with a separation of only one M-cube."

**SA L17415-17440.** The nest Z''_l(X), t_♭ < l ≤ t, "consists of increasing boxes in Ω_l^c ∩ X". After n stages of a drop-out, Ω_l ∩ X = Λ_l ∩ X = X ∖ Z''_l(X) for t_♭ < l ≤ t_♭ + n (L17422-17424). The ν-sequences (L17436-17437, and (R21) at SA L6100-6105) take X ∖ Z''_l for t_♭ < l ≤ t_♭ + ν and the old Ω_l° above. L17440: "each Ω^ν is the label of an actual history, the one in which the operations stop after ν stages."

**SA L17624 (the overlap).** "On the outermost shells, where the collars of the stages overlap, this requirement is relaxed by a factor L_♭² for each overlap"; k_♯ is defined by MŘ_{k_♯+1}L^{k_♯+1−k} = M; "The collars of the stages with j ≤ k_♯ are disjoint, and the collars of the later stages overlap." "In the region not covered by the shells, the bound is expressed in the scale j of the stage and equals (1 − ½β_s)c_l L_♭^{2e}ε_jη_j²", with e = (j − l − 1)_+ on Ω_l ∖ Ω_{l+1}, k_♯ < l ≤ j, and e = j − k_♯ − 1 between the shells and Ω_{k_♯+1}; e = 0 for j ≤ k_♯.

**CA-I L53737-53830 (Definition 4.18, prepared sequence and collars).** This is the account's transcription of Balaban's construction. The integer N_0 is "the smallest positive integer N_0 such, that L^{−N_0+1}MR_{k−N_0+1} = M" (L53771-53772), with k_0 = k − N_0, so a_{k_0+1} = M, a_i ≤ M for i ≤ k_0 + 1 and a_i ≥ M for i ≥ k_0 + 1 (L53773-53777), where a_i = MR_iu_i is the side of a level-i cell in level-k units and u_i = L^{−(k−i)}. Write I_M = {k_0 + 1, …, k}. The prepared sequence (L53779-53787):
  - for i ∈ I_M, Z''_i is a union of level-i M-cubes; the members are nested, and "Z''_i and Z''_{i−1} are 'separated by one layer' of level-i M-cubes"; the last member is Z''_k = (Ω^{∼5}_{k_0+1})^c ∩ Z;
  - for h < i ≤ k_0, Z''_i = (Ω_i^{∼5})^c ∩ Z;
  - for i ≤ h, Z''_i = Z_i.
The collar of stage n + 1 (j = h + n) is R_n := Z_{j+1} ∖ Z''_{j+1} (L53806-53810). "After the integration of stage n + 1, the member of level j + 1 in force inside Z is Z''_{j+1}, the members of the levels i > j + 1 are still Z_i, and those of the levels i ≤ j are Z''_i" (L53812-53814). The margins of the T operations: Z_t ⊃ (Z_{t−1})^{+10a_t} and Ω_t^c ⊃ (Z_{t−1})^{+5La_t} (L53816-53830).

So SA's k_♯ is CA-I's k_0, SA's 𝖭_k = Ř_k is CA-I's N (the number of stages), and CA-I's N_0 = k − k_0 is the number of top levels.

**CA-I L65655-65661.** "Bałaban's construction counts the stages whose collars overlap, of which there are at most N_0".

**SA L9593-9599 (the separated class of the background theory).** Regions Ω_0 ⊃ ⋯ ⊃ Ω_k, each a union of cubes of side 𝔐ξ_j, are separated when dist_∞(Ω_j^c, Ω_{j+1}) > ρξ_j. "Both the cube size 𝔐 and the gap ρ = R₁𝔐 are large powers of L"; "The cube size is the quantity M₁"; "The cube size 𝔐 and the side M of the localisation cubes, which is fixed at a later stage, are different quantities".

**Y3.** Y3 has no R operation. Its structures are only (s, mid) and (s, out) (Y3 L53259-53263), and `grep -c -i 'drop-out\|dropout'` on Y3_I.tex returns 0. So there is no three-dimensional treatment of later-stage collars to port. What does port is Y3's handling of every stage sequence as a separated sequence on which the background theorem is applied (Y3 L53314-53321, meets "separated and subordinate"), and this file does exactly that.

### 2.2 Overlap of collars

Fix a class component Z (= X) at step k, with prepared sequence and collars as in CA-I Definition 4.18. All sets are intersected with Z.

**Lemma 2.1 (when collars overlap).** [proved here] For consecutive stages, R_n ∩ R_{n+1} = Z_{j+1} ∖ Z''_{j+2}, with j = h + n. Hence R_n ∩ R_{n+1} = ∅ if and only if Z_{j+1} ⊂ Z''_{j+2}.

*Proof.* R_n = Z_{j+1} ∖ Z''_{j+1} and R_{n+1} = Z_{j+2} ∖ Z''_{j+2}. Since Z_{j+1} ⊂ Z_{j+2} (the T operations enlarge the large-field regions, CA-I L53816-53818) and Z''_{j+1} ⊂ Z''_{j+2} (nesting, CA-I L53796-53799), R_n ∩ R_{n+1} = Z_{j+1} ∩ (Z''_{j+1})^c ∩ (Z''_{j+2})^c = Z_{j+1} ∖ Z''_{j+2}. □

**Lemma 2.2 (the last collars overlap).** [proved here] Suppose Z_{k−1} contains a level-(k − 1) cell (it does: Z_{k−1} is a nonempty union of level-(k − 1) cells, CA-I L53815-53816). If Λ = Λ^pr has side ≤ C_ΛM in level-k units and a_{k−1} > C_ΛM, then R_{N−2} ∩ R_{N−1} ≠ ∅.

*Proof.* The last two stages have j + 1 = k − 1 and j + 2 = k. By Lemma 2.1 they are disjoint iff Z_{k−1} ⊂ Z''_k. Since Z''_k ⊂ Λ (CA-I L53796), disjointness would give a level-(k − 1) cell, of side a_{k−1}, inside Λ, of side ≤ C_ΛM. □

Since a_{k−1} = MR_{k−1}u_{k−1} = MR_{k−1}/L and R_{k−1} grows with the inverse coupling (CA-I L42911-42913), a_{k−1} > C_ΛM as soon as R_{k−1} > C_ΛL. So the overlap is real, and it grows: the top N_0 stages have collars that overlap (CA-I L65658).

### 2.3 Separation of every stage sequence

**Lemma 2.3 (stage sequences are separated).** [proved here, from the construction as recorded in CA-I Definition 4.18 and SA Proposition 2.3] Let 0 ≤ n ≤ N, and let S^{(n)} be the sequence in force after n stages: members Z''_i for i ≤ h + n, Z_i for i > h + n (inside Z), and the label outside Z. For a level i let Ω_i^{(n)} be the corresponding small-field member, Ω_i^{(n)} ∩ Z = Z ∖ Z''_i for i ≤ h + n (SA L17422-17424) and Ω_i^{(n)} ∩ Z = Ω_i ∩ Z otherwise. Then for every i,

  dist_∞(Ω_{i+1}^{(n)}, (Ω_i^{(n)})^c) ≥ LM u_i  (level-k units; one level-(i + 1) M-cube),

and every member is a union of level-i M-cubes (within Z) and of level-i cells (outside Z).

*Proof.* Distances are in level-k units; u_i = L^{i−k}; a level-(i + 1) M-cube has side Mu_{i+1} = LMu_i. Because Ω_i^{(n)} ⊃ Λ_i^{(n)}, the complement (Ω_i^{(n)})^c lies in the large-field member of level i in force. There are five cases.

(a) Both i, i + 1 ≤ h + n and i + 1 ∈ I_M. Then (Ω_i^{(n)})^c ∩ Z = Z''_i and Ω_{i+1}^{(n)} ∩ Z = Z ∖ Z''_{i+1}. By CA-I L53780-53782, Z''_{i+1} and Z''_i are separated by one layer of level-(i + 1) M-cubes, so a point outside Z''_{i+1} has distance ≥ LMu_i from Z''_i.

(b) Both i, i + 1 ≤ h + n and h < i + 1 ≤ k_0. Then Z''_{i+1} = (Ω_{i+1}^{∼5})^c and Z''_i ⊂ Z_i (for i ≤ h, Z''_i = Z_i; for h < i, Z''_i = (Ω_i^{∼5})^c ⊂ Ω_i^c ⊂ Z_i). A point y ∉ Z''_{i+1} lies in Ω_{i+1}^{∼5}, so within five layers of Ω_{i+1}. Each layer of Balaban's enlargement at level i + 1 has width at most a_{i+1} [reading: I take "layers" in S^{∼ℓ} as layers of level-(i + 1) cells, CA-I L53742-53743; if they are layers of M-cubes the bound only improves]. Since Ω_{i+1}^c ⊃ (Z_i)^{+5La_{i+1}} (CA-I L53825-53829), dist(Ω_{i+1}, Z_i) ≥ 5La_{i+1}, hence dist(y, Z_i) ≥ 5La_{i+1} − 5a_{i+1} = 5(L − 1)a_{i+1}. As a_{i+1} = MR_{i+1}u_{i+1} ≥ Mu_{i+1} = LMu_i (R_{i+1} ≥ 1), dist(y, Z''_i) ≥ 5(L − 1)LMu_i ≥ LMu_i.

(c) i = h + n, i + 1 = h + n + 1 > h + n (the first unprepared level). Then (Ω_i^{(n)})^c ∩ Z = Z''_i and Ω_{i+1}^{(n)} = Ω_{i+1}. Since Z''_i ⊂ Z_i (as in (b), and for i ∈ I_M because Z''_i ⊂ Z''_k ⊂ Λ ⊂ Ω^c_{k_0+1} ⊂ Z_{k_0+1}, CA-I L53804, together with the obvious Z''_i ⊂ Ω_i^c ⊂ Z_i of SA L17415), dist(Ω_{i+1}, Z''_i) ≥ dist(Ω_{i+1}, Z_i) ≥ 5La_{i+1} ≥ LMu_i.

(d) Both i, i + 1 > h + n. The members are those of the label, and dist(Ω_{i+1}, Z_i) ≥ 5La_{i+1} ≥ LMu_i as in (c). (SA Proposition 2.3, L17398, gives the larger gap cMŘ_i in level-i units for these members.)

(e) Outside Z the sequence is the label's, separated as in (d); across ∂Z the members are those of the label, because Z is a component of Z_k and Z_k ∩ Z = Z (CA-I L53751-53752), so every member of level ≤ k is unchanged near ∂Z except inside Z.

Cube structure: for i ∈ I_M, Z''_i is a union of level-i M-cubes (CA-I L53780). For h < i ≤ k_0, Z''_i = (Ω_i^{∼5})^c is a union of level-i cells when Ω_i is, and a cell (side a_i = MR_iu_i, R_i integer) is a union of level-i M-cubes. For i ≤ h, Z''_i = Z_i is a union of cells. □

**Corollary 2.4 (all structures).** [proved here] Every sequence that ST1 reads at the operation is separated in the same sense: (i) the determining sequence after n stages (Lemma 2.3); (ii) every ν-sequence of (R21), ν ≤ n (it is S^{(ν)} on the levels ≤ t_♭ + n, by SA L17440, "the label of an actual history"); (iii) every meet of these with a tower sequence Ω^𝔯(Z′) of a localisation region, by Lemma 6.1 of ST1, provided the tower is separated with a gap above the same floor; (iv) the old/new pair at a stage, which is memberwise ordered, Ω^− ⊂ Ω^+ (ST1 Lemma 6.5; here directly: only the member of level j + 1 changes, from Ω_{j+1} to Z ∖ Z''_{j+1} ⊃ Ω_{j+1}).

*Proof.* (i)-(ii) as stated. (iii): the meet of two separated sequences with gaps ρ, ρ′ is separated with gap min(ρ, ρ′) (ST1 Lemma 6.1, whose proof is three lines and which I reread at `st1-draft.md:301-303`), and it is a union of cubes of the common refinement. (iv): Z''_{j+1} ⊂ Ω_{j+1}^c ∩ Z (SA L17415 "increasing boxes in Ω_l^c ∩ X"), so Z ∖ Z''_{j+1} ⊃ Ω_{j+1} ∩ Z. □

**What this says about the three attacks of ST1 §18.2.** Attack 1's "no strip of width ρξ between the corresponding layers" refers to two *collars*, R_n and R_{n+1}, which are not layers of one sequence. Within any one sequence S^{(n)}, every layer is a strip of width ≥ LMu_i (Lemma 2.3). Attack 2's observation that many row levels meet within distance ρξ_i of a site is correct, but it holds for every separated sequence whose gaps are near the floor: the layers below i have widths ρξ_{i−1}, ρξ_{i−2}, …, which sum to less than ρξ_i. It is exactly the situation the mixed-scale summation lemma of `a1-balaban.md` §3.7 handles: "There are at most 3 + 2R/ρ possible scales" within weighted distance R (`a1-balaban.md:533`). So the counts per separated layer that SA L9987-9997 uses are available. Attack 3 is correct as stated (lifts do not create decay) and is not needed.

---

## 3. Theorem OS: the conclusions (i)-(iii) at every stage

### 3.1 Statement

Write 𝒮_sep(ρ_0, M₁) for the class of sequences of SA L9593: each member a union of aligned cubes of side M₁ξ_j, with dist_∞(Ω_j^c, Ω_{j+1}) > ρ_0ξ_j. Let the background theorems be stated as in ST1 §7:

- [import BG] (BG1(2)): on every sequence of 𝒮_sep(ρ_0, M₁) with ρ_0 ≥ ρ_BG, regular critical orbit, holomorphic axial representative on ‖B‖_∞ < r_B, restriction identity for memberwise nested sequences, tube 𝒯_𝐁 of radius δ;
- [import PROF] (PR1(3)): the profile bound (30) of `a3-profile.md`, rate δ_prof, constant C_P;
- [import DR] (PR1(2) for a fixed system): `dec-field.md` Proposition 5.1 with weights e^{θ d_𝐁}, 0 ≤ θ ≤ θ_DR;
- PR1(1): the fibre precision bounds (I-1)(b)-(d) of IN1, gap a, decay H e^{−μ₀d}, perturbation η(P)e^{−μ₀d}.

**Theorem 3.1 (Lemma OS, replaced).** [proved here, as an implication] Assume [import BG], [import PROF], [import DR] and PR1(1), each holding on 𝒮_sep(ρ_0, M₁) for every ρ_0 ≥ ρ_floor with constants that depend on L, M₁ and the cited-pending constants only (the floor property, Section 3.3). Assume (M-sep). Then, at every stage of every operation, at every stage level (j ≤ k_♯ and j > k_♯ alike), for the determining sequence of every structure, every ν-sequence, every meet with a separated tower, and the old/new pair of the stage:

(i) the regular critical orbit exists and is unique for admitted data, its axial representative is holomorphic on ‖B‖_∞ < r_B, and the restriction identity holds for memberwise nested pairs, in particular for the old and new sequence of the stage;
(ii) the profile bound holds: η^{−2}𝖫(p)²|∂U_p − 1|, 𝖫(b)³|J(U)(b)| ≤ C_P max_τ e^{−δ_prof d_𝐁(x,τ)}|∂𝐕(τ) − 1|;
(iii) the decoupled response exists and obeys ‖D_{B′}𝐇[β]‖_{X,w} ≤ 2B‖β‖_{Y,w} for w = e^{θd_𝐁}, θ ≤ θ_DR; and the fibre precision obeys (I-1)(b)-(d).

The constants r_B, δ, C_P, δ_prof, B, θ_DR, a, H, μ₀ are those of the separated theorems at the floor ρ_floor; they are independent of 𝖭_t, of the number of collars meeting at a point, of the number of shells, of depth, of volume, of M and of κ̄. Moreover, with ρ_0 := R₁M₁ and the gap number R₁ chosen as in Lemma 3.4, every complete layer of a stage sequence contributes at least ρ_0 to d_𝐁, so each crossed shell gives a factor e^{−ω} with ω = μρ_0 ≥ log 4 + 3 log L for μ ∈ {δ_prof, θ_DR, μ₀}.

*Proof.* By Lemma 2.3 and Corollary 2.4, every sequence named is a member of 𝒮_sep(LM, M) ⊂ 𝒮_sep(R₁M₁, M₁): the gap inclusion uses LM ≥ R₁M₁ (M-sep), and the cube inclusion uses M₁ | M with aligned partitions, so a level-j M-cube is a union of (M/M₁)⁴ aligned level-j M₁-cubes. The floor property (Section 3.3) says the imports hold on 𝒮_sep(ρ_0, M₁) for every ρ_0 ≥ ρ_floor with constants not depending on ρ_0. Apply them with ρ_0 = R₁M₁ ≥ ρ_floor. The per-shell decay: a path from layer i to layer i + ν crosses ν − 1 complete layers, each of Euclidean width ≥ LMu_{i′} ≥ ρ_0 u_{i′} in a region of density u_{i′}^{−1}, so d_𝐁 ≥ ρ_0(ν − 1) (this is ST1 Lemma 6.2 with ρ = ρ_0; its proof `st1-draft.md:307` uses only the strip widths). The factor per crossed layer is e^{−μρ_0} = e^{−ω}. Independence of M: M occurs in no constant; it occurs only in (M-sep), which is a lower bound. Independence of κ̄: κ̄ is a polymer constant of NL1, chosen after the background constants in the master order (`ym4-assembly.md` §3; SA L19469-19470 as cited in `st1-draft.md:543`), and no import of Theorem 3.1 refers to it. □

### 3.2 The order of constants

**Lemma 3.4 (choice of R₁).** [proved here] Let μ_min := min{δ_prof, θ_DR, μ₀}. If the rates are fixed before R₁ (they are functions of L and of F0's constants only), choose the gap number R₁ (a power of L) with

  R₁M₁ μ_min ≥ log 4 + 3 log L  and  R₁M₁ ≥ ρ_floor.

Then ω = μρ_0 ≥ log 4 + 3 log L for each of the three rates, and every condition of ST1 §16 that has the form "rate × ρ ≥ constant(L)" holds with ρ = ρ_0 (δ_Tρ ≥ log 4 + 16 log L with δ_T = δ_prof/4; μ_𝔥ρ ≥ 2 log 4; δρ ≥ 64 log L) if the first inequality is replaced by R₁M₁ min{δ_prof/4, μ_𝔥, δ} ≥ log 4 + 64 log L.

*Proof.* Each is a lower bound on R₁M₁ by a number that is already fixed. □

Where the rates come from, so that the order is not circular: the profile rate is δ = (log 2)/R with R = C_Lσ, and σ, C_L are fixed from L and the cited-pending constants, "not on depth" (`a3-profile.md:620-638`); the gap is chosen afterwards ("Choose ρ > C_Lσ", `a3-profile.md:318`). The summation gap of A1 is "ρ ≥ 2(8 + |p|) log L/a" with a the fixed kernel rate (`a1-balaban.md:540-541`). So R₁ after the rates is the order these notes already use. M comes after R₁M₁ (SA L9599: M "is fixed at a later stage"), and (M-sep) is one more lower bound on M. This also meets ST1's M ≥ L⁴M₁ (`st1-draft.md:532`).

The coordinator's requirement (`in1-draft.md` Theorems A.5-A.7): a, H, μ₀ of (I-1) at the stage pairs must depend "on L and the constants of `c4-order.md` rows 1-7 only". Theorem 3.1 gives exactly the constants of (I-1) on separated sequences at the floor. So stage pairs introduce no constant beyond those of the separated layered case. The pair-perturbation function H_p(M) of (I-1)(d) may depend on M (`in1-draft.md:61`); Theorem 3.1 does not change it.

### 3.3 The floor property of the imports

The proof of Theorem 3.1 needs every separation hypothesis of the imports to be a floor: if the theorem holds on 𝒮_sep(ρ_0, M₁), it holds on 𝒮_sep(ρ′, M₁) for ρ′ ≥ ρ_0 with the same constants. A sequence with larger gaps is a sequence with smaller gaps a fortiori (dist > ρ′ξ ≥ ρ_0ξ), so 𝒮_sep(ρ′, M₁) ⊂ 𝒮_sep(ρ_0, M₁) as sets. **Hence the floor property is automatic for any theorem stated "for every sequence in 𝒮_sep(ρ_0, M₁)" with constants depending on (L, M₁, ρ_0).** What must be checked is only that the import is stated that way, with a single ρ_0 and constants not depending on the particular sequence. I record the four imports:

- (F-1) A1, [import BG]. `a1-balaban.md:129-131`: "All constants in the following statements are uniform in depth, volume, and the admitted separated domains." `a1-balaban.md:1265-1268`: "S_* was bounded uniformly over every gap above its previously fixed minimum." `a1-balaban.md:2440-2446` lists the choices, "None is chosen as a function of the number of layers." **Floor: yes.**
- (F-2) A3, [import PROF]. `a3-profile.md:34-37`: constants "independent of depth, torus size, datum and shapes of the separated regions"; the only gap condition is ρ > C_Lσ (`a3-profile.md:318`). `a3-close.md:16` states its theorem for "a separated sequence (SA 9593) with gap ρ ≥ ρ′_0". **Floor: yes.**
- (F-3) DR, [import DR]. `dec-field.md` Proposition 5.1 (L247-280) uses only (5.1) in weighted norms; its weights e^{θd_𝐁} and the convergence of its iterations need the summation of A1 §3.7, which is a floor. The premises [PW] and [NL] are cited-pending (`dec-field.md:244`). **Floor: yes for Proposition 5.1 itself; [PW], [NL] must be stated on 𝒮_sep(ρ_0, M₁) for one ρ_0 — to be confirmed when they are written.**
- (F-4) PR1(1) at layered pairs (PR-lay, `in1-draft.md:62`, open). **Its final statement must take the same form.** Theorem 3.1 shows that this suffices for every stage pair.

So the conclusions (i)-(iii) of Lemma OS are reduced to the separated-sequence theorems with no new hypothesis besides (M-sep) and Lemma 3.4.

### 3.4 Bounded overlap (route (b)), stated for the record

**Corollary 3.5.** [proved here] Let K be the largest number of collars R_n of one operation that contain a common point. Theorem 3.1 holds with constants independent of K. Moreover K ≤ N_0 + 2.

*Proof.* The first sentence: K appears nowhere in the proof of Theorem 3.1. The count: for stages with j + 2 ≤ k_0, Z_{j+1} ⊂ Z''_{j+2} (by (b) of Lemma 2.3 with i + 1 = j + 2: Z''_{j+2} = (Ω_{j+2}^{∼5})^c ⊃ (Z_{j+1})^{+5(L−1)a_{j+2}}), so R_n ∩ R_{n+1} = ∅ by Lemma 2.1, and more generally R_n ∩ R_{n′} = ∅ for n < n′ with j_n + 2 ≤ k_0, since R_n ⊂ Z_{j_n+1} ⊂ Z''_{j_n+2} ⊂ Z''_{j_{n′}+1}. A point lies in at most one collar of a stage with j + 2 ≤ k_0, and possibly in the collars of the stages with j + 2 ∈ {k_0 + 1, …, k}, which number N_0. □

### 3.5 The profile bound on the overlapping collars, made explicit

Part (ii) of Theorem 3.1 is the general profile bound. The overlap shows up in the *data*: on integrated collars the stage tests bound the datum only in the stage scale with a lift (SA L17624). I check that the profile still gives each shell its own tested bound up to a fixed factor, using ω ≥ log 4 + 3 log L. This is where the per-shell rate demanded in Lemma OS is used.

**Lemma 3.6 (profile on the nest).** [proved here] After the stage at level j (> k_♯ or not), let the datum tests obey, in the normalised units of the layer of the test (v(τ) := |∂𝐕(τ) − 1| divided by the layer scale ε_iη_i² of its layer i):
  v(τ) ≤ ν_i := L_♭^{2(i−k_♯−1)_+} on the shell of level i ≤ j (SA L17624),
  v(τ) ≤ ν_coll := 3L²C_run L_♭^{2e} on the region outside the shells, with e ≤ j − k_♯ − 1,
  v(τ) ≤ 1 elsewhere (label tests).
Then at a point x of the shell of level i, the profile in units of ε_iη_i² is at most C_sh L² ν_i, with C_sh := 3C_run²e^{ω}, a constant fixed before M (ω = μ_minR₁M₁ is fixed before M).

*Proof.* P(x) = max_τ e^{−δ_prof d(x,τ)} v(τ)·(scale ratio). Normalise to layer i: a test of layer i′ has scale ratio ε_{i′}η_{i′}²/(ε_iη_i²) ≤ C_run(1 + |i′ − i|^{1/2})L^{−2(i′−i)} for i′ ≥ i, and ≤ C_runL^{2(i−i′)} for i′ < i (η_{i′} = L^{i−i′}η_i; [import RUN]). By Theorem 3.1, d(x, τ) ≥ ρ_0(|i′ − i| − 1)_+. Three cases.
  (1) i′ > i, shells: the contribution is ≤ e^{−ω(i′−i−1)} C_run(1 + √(i′ − i)) L^{−2(i′−i)} L_♭^{2(i′−i)} ν_i ≤ ν_i C_run e^{ω} (L_♭²·2e^{−ω})^{ν} with ν = i′ − i, using 1 + √ν ≤ 2^ν and L^{−2} ≤ 1. Since e^{−ω} ≤ 1/(4L³) and L_♭² < L²/4, L_♭²·2e^{−ω} < 1/(8L), and the maximum over ν ≥ 1 is ≤ ν_i C_run e^{ω}/(8L) ≤ ν_i C_run e^ω.
  (2) The region outside the shells, at layer j + 1 ≥ i + 1: as (1) with ν = j + 1 − i and ν_coll = 3L²C_runL_♭^{2e}; e ≤ j − k_♯ − 1, and L_♭^{2e} ≤ L_♭^{2(i−k_♯−1)_+}L_♭^{2(j−i)} ≤ ν_i L_♭^{2ν}. The contribution is ≤ 3L²C_run²e^{ω}ν_i(L_♭²·2e^{−ω})^{ν} ≤ 3L²C_run²e^{ω}ν_i.
  (3) i′ < i: the lower shells and the core. ν_{i′} ≤ ν_i (the lift is nondecreasing in the level), the scale ratio is ≤ C_runL^{2(i−i′)}, and the distance is ≥ ρ_0(i − i′ − 1)_+; the contribution is ≤ C_run e^{ω} ν_i (L²e^{−ω})^{i−i′} ≤ C_run e^ω ν_i (1/(4L))^{i−i′} ≤ C_run e^ω ν_i.
Taking the maximum gives P(x) ≤ 3L²C_run²e^{ω}ν_i = C_shL²ν_i. □

So, at the actual stage background, the curvature on the shell of level i is ≤ C_PC_shL²ν_iε_iη_i²: the tested bound times a constant that depends on L, ω and C_P only. The relaxation on the overlapping collars does not spread: it is damped by e^{−ω} per shell against at most L_♭² growth per shell, and ω ≥ log 4 + 3 log L is more than enough (Lemma 3.6 needs only L_♭²e^{−ω} ≤ 1/(8L) and L²e^{−ω} ≤ 1/(4L)).

---

## 4. The localised backgrounds and the restriction identity

SA L17624: "adjacent to X^c, the background localised in X is constrained bond by bond on the bare lattice." The tests of a stage are formed with backgrounds U^{(n)}_{k,X} localised in X (SA L17585). Read literally (bare constraints next to X^c while the layers inside X reach the top level), this localised problem is not separated: layer 0 would touch layer k. The library already treats localisation by erosion towers: the localised sequence is the meet of the sequence with an eroded tower of the region, whose layers descend geometrically to the bare level within a collar (`wf-c.md:36`, SA L9783-9789 as read there; `a3-close.md` Lemma J at L110-137, "discharged as an implication"; ST1 §4.4, Corollary B′). The erosion is ≤ 3M₁ξ_q per level (`st1-draft.md:383`, from Y3 L55913-55917).

**Lemma 4.1.** [proved here] The meet of S^{(n)} with an erosion tower of X with gap ≥ ρ_0 is in 𝒮_sep(ρ_0, M₁), and Theorem 3.1 applies to the localised backgrounds U^{(n)}_{k,X}, with the restriction identity relating the localised and the unlocalised background on the region where the two sequences agree.

*Proof.* Separation of the meet: ST1 Lemma 6.1. Restriction identity: [import BG], restriction clause, for memberwise nested separated sequences (the meet is memberwise contained in S^{(n)}). □

The literal bare-collar reading is the place where SA's "boundary to run within one layer" condition matters (SA L9913, quoted in `layered-a3.md:12-14`); it concerns every localisation, not the stage overlap, and Lemma 4.1 replaces it by the erosion-tower localisation that the library uses. [design: localised stage backgrounds are formed on the meet with the erosion tower of X.]

---

## 5. The coordinator's requirement, stated explicitly

**Proposition 5.1 (constants for IN1).** [proved here] At every layered stage pair of the R operation and at its real reference, the three properties IN1 needs, namely (I-1)(b) uniform gap a, (I-1)(c) entrywise decay H e^{−μ₀d}, and (I-1)(d) the pair-perturbation bound η(P)e^{−μ₀d}, hold whenever PR1(1) holds on 𝒮_sep(ρ_0, M₁), with the same a, H, μ₀. These are fixed before κ and κ̄, independent of M and of κ̄, and also independent of 𝖭_t, of the number of overlapping collars and shells, of depth and of volume.

*Proof.* Theorem 3.1(iii), last clause, and Section 3.2. The perturbation size η(P) ≤ H_p(M)(a₀ + a₁ + j₀) keeps the M-dependence that (I-1)(d) allows. □

The constants introduced in this file and their dependence:

| Constant | Depends on | Chosen before |
|---|---|---|
| ρ_floor, r_B, δ, C_P, δ_prof, B, θ_DR, a, H, μ₀ | L, M₁, F0 and the cited-pending constants | R₁ |
| R₁ (gap number) | rates above, L (Lemma 3.4) | M |
| ω = μ_min R₁M₁ | the above | M |
| C_sh = 3C_run²e^ω (Lemma 3.6) | C_run, ω | M |
| (M-sep): M₁ \| M, LM ≥ R₁M₁ | lower bound on M | — |

None depends on M or κ̄. Section 7's repairs add κ_t (depends on β_s and 𝖭, not on M or κ̄) and the condition (AMP-st), a ceiling on γ chosen last.

---

## 6. Route (a): redesign so that collars never overlap

**Proposition 6.1 (disjoint collars force a large box).** [proved here] In the R operation of SA L17585 and CA-I Definition 4.18, suppose all consecutive collars are disjoint. Then Λ^pr contains a level-(k − 1) cell, and its side is at least a_{k−1} = MR_{k−1}/L in level-k units.

*Proof.* Lemma 2.2. □

**Why this defeats route (a).** SA L17612: "the stages reduce the component from side MŘ_k to a box of side O(M). Hence C(M) is a constant fixed before γ." SA Proposition 2.4 (L17656) gives the minimiser in the box with a Hessian lower bound c(M) > 0 (Balaban: cM^{−5}) and C(M) chosen "after M and before γ". With a box of side ≥ MR_{k−1}/L the same proof gives constants C(MR_{k−1}/L), which grow with the inverse coupling. The test at the main step (2) needs C(M)ε_k ≤ a_Λ (SA L17656) and the main-step condition C(M)L^{−𝖭_k}𝖭_k^{1/2} ≤ c (SA L17627). Both become conditions with C(MŘ) in place of C(M); the first is then C(MŘ)ε ≤ a_Λ, which Balaban's M⁵ dependence would turn into a polynomial in Ř against ε, perhaps still satisfiable, but the order of constants of SA L17612 ("C(M) is a constant fixed before γ") is lost, and with it the claim that the stages reach a box on which the reference law is uniform. So a geometric redesign to disjoint collars changes the main step, not only the stages. Two alternatives that keep the box:

- *Spacing the stage levels* (integrate several levels in one stage). This keeps a box of side O(M) but changes the stage ladder (SA L17615), whose margin per stage must pay for one level of scale change. I did not pursue it, because Section 3 makes it unnecessary.
- *Shrinking the collar widths of the last stages.* The collars are R_n = Z_{j+1} ∖ Z''_{j+1}; their size is fixed by Z_{j+1}, which is a label region (made by the T steps, CA-I L53816-53818) and cannot be shrunk by the R operation. Only Z''_{j+1} is a choice, and Lemma 2.1 shows disjointness needs Z''_{j+2} ⊃ Z_{j+1}: shrinking the prepared members makes the overlap larger, not smaller.

**Conclusion for route (a).** A redesign to disjoint collars is not possible without changing the main step and Proposition 2.4. It is not needed: Theorem 3.1 holds on the overlapping collars as they are. The LF1 quantities that the brief asks to check are untouched: (N-growth) 𝖭_t ≤ (log x_t)^{(𝔭₀−𝔭₁)/2} (`st1-draft.md:461-463`), the reserve, and the drop-out rules (SA L17415-17440). Section 3 changes no region, no test, no waiting depth and no rule; (M-sep) is a lower bound on M, which SA already takes large.

---

## 7. Two defects in ST1's separated-case proofs, and their repairs

These arise at every preparatory stage, overlapping or not. They must be repaired for "the separated-sequence results of ST1 apply" to be true.

### 7.1 D1: the phase gap does not cover the shift at early stages

ST1 Corollary E′ (`st1-draft.md:457`): "The source 𝔛 lies in layer ≥ t − 1, so d(x, 𝔛) ≥ ρ(t − n − 2)_+ by Lemma 6.2." At the preparatory stage n → n + 1 of the operation at level t, the source bonds are those touching R_n = Z_{j+1} ∖ Z''_{j+1}, j = t_♭ + n = t − 𝖭_t + n. Before the stage, R_n lies in Ω_j^{(n)}, because it is outside Z''_{j+1} ⊃ Z''_j. Its part in Ω_{j+1}^c (the five-layer rim of Ω_{j+1}^c when j + 1 ≤ k_0, the large collar when j + 1 ∈ I_M) has layer j; its part in the strip Ω_{j+1} ∩ Z_{j+1} has layer j + 1, since Ω_{j+2}^c ⊃ Z_{j+1}. So the source is in layers j and j + 1, not t − 1, unless n ≥ 𝖭_t − 2.

Now take a carried term that reads a point x of layer j inside R_n, with radius index j. Boundary terms are such terms whenever their domains meet R_n: SA L17548 puts into B^{(j+1)} an O(1) amount "for each M-cube of level j+1 next to Z_{j+1}", and these domains meet the rim of Z_{j+1}. If no carried term ever read such points the defect would be empty; I do not see a rule that excludes them. ST1 Lemma 5.6(ii) gives the gap at index j as θ_sβ_s2^{−(t−j)}/(2𝖭_t) = θ_sβ_s2^{−(𝖭_t−n)}/(2𝖭_t). The shift at x has, by (C1) and [import FL], relative size up to 𝖼_𝔥C_𝒜δ′_j/(α_0ε_j), with no decay factor, since x is at distance O(1) from source bonds. The ratio shift/gap at x is therefore of order 2^{𝖭_t−n}𝖭_t(δ′_j/ε_j). For n = 0 it is 2^{𝖭_t}𝖭_t(A₁/A₀)(log x_j)^{−(𝔭₀−𝔭₁)}. With 𝖭_t = Ř_t ≈ (log x_t)^r (SA L17630) this tends to infinity. So the proof of Theorem E(ii) does not cover early stages: (AMP) fails there by a factor 2^{𝖭_t−n}. This is a failure of a proof step, not a counterexample to an inclusion; the inclusion could still hold for another reason, but none is given.

### 7.2 Repair of D1: a stage-graded term

**Definition 7.2 (stage-graded coefficient).** [design] For a level u let W(u) = {t : t − 𝖭_t ≤ u ≤ t} (the operations having a stage at level u, including its main step level) and put κ(u) := β_s/(8#W(u)). For a structure σ, let St(σ) be the set of preparatory stages (t′, n′) completed by σ (in the order ≼ of ST1 §4.1), and j(t′, n′) = t′ − 𝖭_{t′} + n′ their stage levels. Define

  c^♮_σ(x|m) := c_σ(x|m) − Σ_{(t′,n′)∈St(σ)} κ(j(t′,n′)) 2^{−|m − j(t′,n′)|},

with c_σ the coefficient of (R22) (ST1 §4.2). Use c^♮ in place of c in Definition 4.5 of ST1.

**Lemma 7.3 (range).** [proved here] Σ_{(t′,n′)} κ(j(t′,n′))2^{−|m−j(t′,n′)|} ≤ 3β_s/8 for every σ and m, over all stages of the whole history. Hence, with ST1 Lemma 4.2, 1 − β_s − 9β_R − 3β_s/8 ≤ c^♮_σ ≤ 1 + β_s, and c^♮ ≥ 1/2 when β_s ≤ 1/4 and c_R ≤ (1 − θ_s)/16.

*Proof.* Group the stages by level u: each operation t ∈ W(u) has at most one preparatory stage at level u (n′ = u − t_♭ is determined). So the stages at level u number at most #W(u), and they contribute ≤ #W(u)κ(u)2^{−|m−u|} = (β_s/8)2^{−|m−u|}. Sum over u ∈ ℤ: (β_s/8)·3 (ST1 Lemma 5.5). For the lower bound: 1 − β_s − 9β_R − 3β_s/8 ≥ 1 − (11/8)(1/4) − 9(1/16)(1/4) = 1 − 11/32 − 9/64 = 33/64 > 1/2. □

**Lemma 7.4 (the new gap).** [proved here] Between consecutive phases n, n + 1 of the operation at level t, at index m, c^♮_{(t,n)}(m) − c^♮_{(t,n+1)}(m) ≥ κ(j_n)2^{−|m−j_n|} + (the gaps of ST1 Lemma 5.6(ii)). At a main step the new term does not change, and ST1 Lemma 5.6(i) holds unchanged. Nesting (ST1 Lemma 4.6) holds for c^♮.

*Proof.* The stage (t, n) → (t, n + 1) adds exactly one element to St, with level j_n. A main step adds none. Nesting: Lemma 4.6's proof uses only monotonicity of the clauses in c. □

**Corollary 7.5 (replaces Corollary E′ at preparatory stages).** [proved here] Assume (FLOW): 0 ≤ x_{t+1} − x_t ≤ C_fl, and 𝖭_t ≤ (log x_t)^{(𝔭₀−𝔭₁)/2} (N-growth). On the support of the stage n → n + 1 at level t (stage level j = j_n), the regional shift restricted to X has ‖λ𝔥‖_v ≤ r_* for |λ| ≤ ϱ_X, with profile w(m) := ½κ(j)2^{−|m−j|}α_0ε_m, provided

  (AMP-st) 256 C_run 𝖼_𝔥 C_𝒜 #W(j) (δ′_j/ε_j) ≤ r_* β_s α_0,

and μ_𝔥ρ_0 ≥ log 4. (AMP-st) holds for all g ≤ γ with γ small.

*Proof.* At a bond based at x of layer m, (C1) and [import FL] give normalised shift ≤ 𝖼_𝔥C_𝒜δ′_j e^{−μ_𝔥d(x,𝔛)}. The source 𝔛 lies in layers j and j + 1 (Section 7.1). For m ≤ j, d(x, 𝔛) ≥ ρ_0(j − m − 1)_+; for m ≥ j + 1, d(x, 𝔛) ≥ ρ_0(m − j − 2)_+ (Theorem 3.1, ST1 Lemma 6.2). With ν = |m − j|, d ≥ ρ_0(ν − 2)_+ in both cases. [import RUN]: ε_m ≥ ε_j/(C_run(1 + √ν)). The ratio to w(m) is ≤ 2𝖼_𝔥C_𝒜C_run(δ′_j/ε_j)(1 + √ν)2^ν e^{−μ_𝔥ρ_0(ν−2)_+}/(κ(j)α_0) ≤ 32𝖼_𝔥C_𝒜C_run(δ′_j/ε_j)/(κ(j)α_0), by the computation of ST1 Corollary E′ (`st1-draft.md:457`: (1 + √ν)2^ν ≤ 4^ν and 4^νe^{−μρ(ν−2)_+} ≤ 16). With κ(j) = β_s/(8#W(j)) this is ≤ r_* under (AMP-st). For the amplitude λ the argument of ST1 Theorem F(i) applies unchanged. It remains to see that (AMP-st) holds for γ small. Every t ∈ W(j) satisfies j ≤ t ≤ j + 𝖭_t, so #W(j) ≤ 1 + max_{t∈W(j)}𝖭_t. By (FLOW), x_t ≤ x_j + C_fl𝖭_t, and 𝖭_t ≤ (log x_t)^{(𝔭₀−𝔭₁)/2} ≤ x_t^{1/2} for x_t large, so x_t ≤ x_j + C_flx_t^{1/2}, which gives x_t ≤ 2x_j for x_j ≥ 4C_fl² and hence log x_t ≤ log x_j + 1. Then #W(j)(δ′_j/ε_j) ≤ (1 + (log x_j + 1)^{(𝔭₀−𝔭₁)/2})(A₁/A₀)(log x_j)^{−(𝔭₀−𝔭₁)} → 0 as x_j → ∞, i.e. as g → 0. □

(FLOW) is the bounded flow increment, [import RUN]'s companion (SA's running couplings; one step changes x by a bounded amount). Theorem E holds with this w in place of Lemma 5.7's. [proved here] Its proof uses Lemma 5.7(a)-(c). For w(m) = ½κ(j)2^{−|m−j|}α_0ε_m: since ||n + ν − j| − |n − j|| ≤ ν and [import RUN] gives ε_{n+ν} ≤ C_run(1 + √ν)ε_n, w(n + ν)/w(n) ≤ 2^νC_run(1 + √ν) ≤ C_run4^ν, which is the bound used in the proof of Lemma 5.7(b)-(c), so (b)-(c) hold as stated. For (a), w(n − 1)/w(n) ≤ 2·ε_{n−1}/ε_n ≤ 2C_run, so (a) holds with C_run/2 replaced by 2C_run; this enlarges the factor 4C_run in r_* to 16C_run.

The main-step gap of ST1 is unchanged, and so is (AMP) at a main step, whose source is at the top layer t: there ST1 Corollary E′ is correct.

### 7.3 D2: the radius index on integrated collars

After the stage at level j, the integrated collar R_n lies in Ω_{j+1}^{(n+1)} and not in Ω_{j+2}^{(n+1)} (Lemma 2.3, case (c)), so its layer is j + 1. The stage tests bound the real background there "in the scale j of the stage", by (1 − ½β_s)c_l L_♭^{2e}ε_jη_j² (SA L17624). In layer-(j + 1) units this is (1 − ½β_s)c_l L_♭^{2e}(ε_j/ε_{j+1})L² ε_{j+1}η_{j+1}², because η_j = Lη_{j+1}. So the real background on R_n is only L²L_♭^{2e}-regular in its own layer scale. The reason is elementary: the new level-(j + 1) data on R_n are averages of the stored level-j field, which was tested only at level j, and a level-(j + 1) plaquette encloses L² level-j plaquettes.

ST1 Theorem A assumes "regularity radius r_U(𝔢) < Cε_{λ(𝔢)} at each regularity element (λ(𝔢) its highest layer index)" and its domain uses the layer as radius index (`st1-draft.md:351-357`). On R_n the hypothesis fails by L²L_♭^{2e}. SA's lift L_♭^{2e_σ(x)}, with e_σ(x) the nonnegative difference between "the original regularity layer and the layer after each stage" (SA L6141-6143), gives at a point originally of layer l now of layer j + 1 the lift L_♭^{2(j+1−l)}, while the test bound is L²L_♭^{2(j−l−1)_+} above the layer scale. For l = j (a point integrated once) this needs L_♭² ≥ L²·const, which is false (L_♭ < L/2). So the domain, read with radius index = layer, does not contain the actual background on the support. This holds at disjoint collars too (there e = 0 and the factor is L²).

### 7.4 Repair of D2: radius index of the stage

**Definition 7.6 (radius index on integrated collars).** [design, following SA L17624 "expressed in the scale j of the stage"] For a structure σ after the stage at level j, and a point x of the collar R_n of that stage that has not been integrated by a later stage, the radius index is 𝗆_σ(x) := j and the lift exponent is e_σ(x) := e of SA L17624 at that stage ((j − l − 1)_+ on the original layer l, j − k_♯ − 1 between the shells and Ω_{k_♯+1}, 0 for j ≤ k_♯). At all other points 𝗆_σ(x) is the layer. Clauses (L1)-(L4) of ST1 Definition 4.5 are read with 𝗆_σ in place of m_σ.

**Theorem 7.7 (real admission on integrated collars).** [proved here] Assume α_0 ≥ 12, and the stage tests of SA L17624 on the support. Then the actual real background satisfies the (L1) curvature entry at every point of an integrated collar with half the radius: |∂U − 1| < ½c^♮_σ(𝗆)λ_σ r_0(σ; 𝗆)L^{−2𝗆}, and the current entry likewise with the profile constant.

*Proof.* On the support of the stage tests, |∂U − 1| < (1 − ½β_s)c_lL_♭^{2e}ε_jη_j² with c_l ≤ 3, which is a tautology of the indicator. The right side of (L1) at 𝗆 = j is c^♮λ_σα_0ε_jη_j² ≥ ½·L_♭^{2e}·α_0ε_jη_j² by Lemma 7.3 and Definition 7.6. With α_0 ≥ 12, half of it is ≥ 3L_♭^{2e}ε_jη_j². For the current: Theorem 3.1(ii) bounds 𝖫(b)³|J| by C_P times the profile, and the computation of Lemma 3.6 at a collar point (case (2) with ν = 0, cases (1), (3) for the shells) bounds the profile by C_shL²·L_♭^{2e}ε_j in the stage scale. So the current entry holds when α_0 ≥ 8C_PC_shL²; this is a (FLOOR)-type condition of ST1 §16, fixed before M. □

**Consequences for the rest of ST1.** [proved here] (1) Theorem B needs (1 + β_s)λ_σr_ι ≤ â in *ambient-scale* units. At a point with 𝗆 = j and layer j + 1 this is (1 + β_s)L²L_♭^{2e}α_ιε_j ≤ â. Since e ≤ N_0 − 1 and L^{N_0−1} = R_{k_0+1} (CA-I L42913), L_♭^{2e} ≤ R_{k_0+1}^{2 log L_♭/log L} ≤ R_k², so the condition is (1 + β_s)L²R_k²α_ιε_j ≤ â, a ceiling on γ (R_k ≈ (log x)^{r} and ε_j = g_jp₀(g_j) → 0). This is the row "lifts times ε small" of `st1-draft.md:539`, with the extra L². (2) Theorem E's gap is read at 𝗆 instead of the layer. Lowering the index by one costs the factor w(𝗆 − 1)/w(𝗆) ≤ 4C_run (Lemma 5.7(a) with the bound of §7.2), absorbed by enlarging the 4C_run in r_*. (3) At the next stage (level j + 1) the collar R_n is either integrated again (overlap case) and then has 𝗆 = j + 1 and e + 1, or it lies in a shell (disjoint case, R_n ⊂ Z_{j+1} ⊂ Z''_{j+2}), where the stage tests bound it in the shell scale (SA L17624, first requirement). In the overlap case the requirement passes from scale j to scale j + 1: "one gains L^{−2} and pays L_♭²" (SA L17624), so the new radius L_♭^{2(e+1)}ε_{j+1}η_{j+1}² ≈ (L_♭²/L²)×(old) is smaller; the inclusion of the new domain in the old one holds pointwise there, and the substitution margin of Theorem E is used only for the shift, as before. In the disjoint case the shell test is stronger than the collar test by L^{−2} up to C_run; this is the order in which SA's ladder runs ("the bound of each stage implies the bound of the preceding stage").

---

## 8. Status

| Item | Status here |
|---|---|
| Lemmas 2.1, 2.2 (collars overlap; last collars must overlap) | [proved here] from CA-I Definition 4.18 |
| Lemma 2.3, Corollary 2.4 (every stage sequence separated, gap LM) | [proved here] from CA-I L53779-53830, SA L17398-17440; one reading flagged in case (b) |
| Theorem 3.1 (Lemma OS (i)-(iii) at every stage) | [proved here] as an implication from BG, PROF, DR, PR1(1) on separated sequences, under (M-sep) |
| Lemma 3.4 (order; ω ≥ log 4 + 3 log L) | [proved here] |
| Floor property | (F-1), (F-2) checked; (F-3) Proposition 5.1 checked, [PW]/[NL] to confirm; (F-4) PR-lay to be stated in floor form |
| Corollary 3.5 (no dependence on overlap K; K ≤ N_0 + 2) | [proved here] |
| Lemma 3.6 (profile on the nest, relaxed collars) | [proved here] |
| Lemma 4.1 (localised stage backgrounds) | [proved here] with the erosion-tower localisation [design] |
| Proposition 5.1 (IN1 constants independent of M, κ̄) | [proved here] |
| Proposition 6.1 (disjoint collars impossible with box O(M)) | [proved here] |
| D1, D2 (defects in ST1 Corollary E′ and Theorem A on stage collars) | found here; repaired by Definitions 7.2, 7.6 [design], Lemmas 7.3-7.4, Corollary 7.5, Theorem 7.7 [proved here] |

Consumer changes [design], for ST1 §4.8: (7) the stage-graded term of Definition 7.2 in the radius coefficient; (8) the radius index and lift of Definition 7.6 on integrated collars; (9) (M-sep) in the order of constants, after R₁M₁; (10) R₁ chosen after the rates δ_prof, θ_DR, μ₀ (Lemma 3.4); (11) localised stage backgrounds on the meet with the erosion tower (Lemma 4.1). New conditions on γ: (AMP-st) and (1 + β_s)L²R_k²α_ιε ≤ â. New import: (FLOW).

No step rests on a computation. No counterexample is claimed. The one reading I could not settle from the account alone is the width of a "layer" in Balaban's enlargement S^{∼5} (Lemma 2.3(b)); either reading gives the bound. This text is not checked by the other model.
