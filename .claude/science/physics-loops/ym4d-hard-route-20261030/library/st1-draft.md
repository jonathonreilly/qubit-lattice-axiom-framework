# ST1, pass 1: intrinsic stage domains and stage admission (D4)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, pass 1 (long draft) of submanuscript ST1 of `library/ym4-assembly.md`, written at the lead's direction under `library/process-review-2026-11-04.md` §4. Research text. It is not an audit, it grants no status, and it is not yet checked by the other model. A later pass (Codex) distils it; a fresh session then reads it line by line.

Credit. The architecture of Sections 4 and 8-15 is a port of the history-step argument of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text) in `YM3/YM3_I.tex` at commit `31a47c543775` ("Y3" below). The four-dimensional stage structure, the radius coefficient (R22), the thresholds and the R operation are from their outline `YM4_sketch_500.tex` ("SA") and complete account `theorem_0_complete_account_raw_I.tex` ("CA-I") at the same commit. The renormalisation-group method, the background field, the stage theorem (CMP 122 (1989) 175-202, (1.24), (1.60)-(1.70)) and the R operation are Tadeusz Balaban's. Jonathan Dimock's expositions ("The renormalization group according to Balaban" I-III, arXiv 1108.1335, 1212.5562, 1304.0705) are the readable model of how background changes are re-expanded. Our library notes named below are by Codex and Claude; each credits its own sources.

Line numbers. "Y3 L" is a line of `scratchpad/sa/YM3_I.tex` (89,144 lines, fetched once at the pin above). "SA L" is a line of `scratchpad/sa/ym4.tex`. "CA-I L" is a line of `scratchpad/sa/ca_I.tex`. Library notes are cited as `note.md:line` or `note.md (eq)`. I read every line range I cite, except where I say that I take a line from a library note.

Status words used inside the text.

- **[proved here]**: the argument is written in full in this file, by hand, with every inequality shown.
- **[port]**: proved here by following the cited Y3 proof; the four-dimensional changes are stated at the place where they enter.
- **[import X]**: a named statement used as an input; its own status (checked, proved, sketched, open) is given in Section 7.
- **[design]**: a definition or a choice of constants that is ours. It is not a claim and needs no proof, but it may change a consumer; Section 4.8 lists every consumer change.
- **[outstanding]**: not proved. There is exactly one: Lemma OS of Section 18.

---

## 0. Summary

**What this file proves.** Under the imports of Section 7 and the design of Section 4, every stage of every history maps the stage domain into the previous one with half the coefficient margin left, every carried term (regular term, boundary term, kept form, formed exponent, drop-out term) re-expanded through a stage is admitted to its own domain with an interpolation disc of radius ϱ_X > 1 and an explicit localised bound, and the composition over all stages gives (D4) with the full quantifiers. This is Theorem ST1* of Section 17. The proof is a four-dimensional port of the Y3 history step: Y3 Propositions II-90-39, II-90-62 (real admission), I-95-61, I-95-81 (towers in the ambient layer scale), II-93-26, II-93-38 (the regional shift and its identification), II-88-43, II-88-50 (the substitution margin) and II-104-17 (re-expansion of an earlier term).

**Three design changes carry the proof.** They are stated in Section 4 and justified in Section 3.

1. *The stage map is a substitution.* A carried term f, formed at level j as a function of a triple P = (U, A′, 𝐉) and of stored coordinates 𝔮, is carried through a stage as f(ρP ∔ λ ρ𝔥(s; P, 𝒜); 𝔮). Here 𝔥 is the regional shift, the decoupled response of the background to the stage fluctuation 𝒜, ∔ is logarithmic substitution of the complex potential and additive substitution of the independent current, and the stored coordinates and the real factor U are not changed. This is Y3's prescription (Y3 L56330-56340). The identity with the actual old read is needed, and is proved, only on the physical locus (real fields, s = 1, λ = 1, physical current), where the measure identity is evaluated (Theorem D). No identity at complex parameter values is needed by any consumer. This removes `shift-map.md`'s Lemma M (Section 3.2).
2. *Inherited towers are meets with the ambient sequence, read in the ambient layer scale at settled elements.* This is Y3 (II-86-16) at Y3 L53314 and Y3 (L3) at Y3 L53371-53388. It removes the reversed scale loss of `layered-a3.md` (3) (Section 3.3).
3. *The coefficient table spends a gap at every level at every stage.* We use SA (R22) (SA L6124-6135), whose phase term gives every read, marked or not, the gap θ_sβ_s 2^{−(t−m)}/(2𝖭_t) at a preparatory stage and (1 − θ_s)β_s 2^{−(t−m)} at a main step. The shift has a profile that fits half of that gap (Theorem E). This closes ⟦ST-phase⟧ (Section 3.4), under the growth condition (N-growth) on the waiting depth 𝖭_t (Section 16), which is a consumer requirement on LF1.

**What is outstanding.** One lemma, Lemma OS (Section 18): the background theorem, its profile bound and the weighted decoupled response on the stage determining sequences of the R operation at the stages whose collars overlap (stage levels above k_♯ in SA L17624). These sequences are not separated, and every background statement we import (BG1(2), PR1(2)) is proved on separated sequences only. Section 18 gives three distinct attacks and the exact reason each fails. Everything else in ST1 is proved here as an implication from the imports of Section 7.

**Status of the ST1 entries of the assembly** (`ym4-assembly.md` L224-234), after this file:

| Entry | Here |
|---|---|
| (1) Nesting | [proved here], Lemma 4.6. |
| (2) Allowance | [proved here], Lemma 5.6 (both gap formulas). |
| (3) ⟦ST-cov⟧ | Theorems A and B [port] on separated sequences; `layered-a3.md`'s Lemma RC is not needed (Section 9.1); reduced to Lemma OS on overlapping outer shells. |
| (4) ⟦ST-map⟧ | Theorems C, D, E [port]; the matched reconstruction is Theorem D; `shift-map.md`'s Lemmas M and R are replaced (Sections 11, 14.2). |
| (5) ⟦ST-phase⟧ | Theorem E(ii) [port], under (N-growth). |
| (6) ⟦ST-wit⟧ | Section 14 [proved here]: witnesses unchanged; returns by pinned levelling; stored slots fixed. |
| (7) ⟦ST-drop⟧ | Section 15 [proved here]: drop-out terms are carried terms on their determining sequence; telescoping keeps the old term's mass exactly. |
| Conclusion (D4) | Theorem ST1* [proved here] from Theorems A-F, modulo Lemma OS. |

---

## 1. What ST1 must deliver

### 1.1 The statement in the assembly

`ym4-assembly.md` L224-234 states Theorem ST1: nesting, allowance, coverage ⟦ST-cov⟧, the stage map ⟦ST-map⟧, no-new-mark reads ⟦ST-phase⟧, witnesses and stored slots ⟦ST-wit⟧, drop-outs ⟦ST-drop⟧, and the conclusion that "every carried composition (lifted and stage cores, stored arguments, healing gauges, logarithm charts) lies in its activity domain with room", which is (D4). L236 adds that NL1 and LF1 must construct their activities on the new domains; ST1 supplies only the domains and the admission.

### 1.2 What the consumers read

The four consumers named in the brief, and what each reads from ST1. The list is `intrinsic-dom.md:297-305`, which I checked against the cited SA lines.

- **B4** (SA L4006-4012): the step is holomorphic on the "product box" with a majorant independent of the number of labels. It reads: every carried term, after every stage, is holomorphic in the complex variables on a domain that contains the product box, with a bound by its own formation bound times a factor depending only on its own size.
- **(LOC)** (SA L5813-5826, (R10)-(R11)): every interpolated argument stays in the core for |ν| < ϱ_F, ϱ_F > 1, with separate inner and removed radii; Boolean corners obey the bracket bound (SA L5849-5861). It reads: an interpolation disc of radius > 1 in which the carried composition stays admitted.
- **(R-cov)** (`kept-cov.md` (4), (8), (13), with `gates/kept-cov-check.md` Defects 1-2): kept forms, elimination factors and recorded returns are covariant as pair functions. It reads: native real-gauge covariance of the domains and of the stage map, and admission of the returned reads.
- **Majorants** (SA L18108-18128): "both suprema" over the admitted pair domain sit inside the stored-field integral. It reads: the supremum of each carried term over the domain is bounded by its formation bound (no growth along the stages beyond a summable product).

Section 17 checks each one against Theorems E and F.

### 1.3 What "(D4)" means here

**(D4)** [design, restating `loc-4.md` §5 and `ym4-assembly.md` L39]: for every history, every level t, every stage n of the operation at level t, every carried term f and every value of the earlier parameters, fluctuations, returns and switches, the argument at which f is evaluated in the presentation after the stage lies in the domain on which f was formed, with an interpolation disc of radius > 1, and the same holds for every composition of stages.

---

## 2. Source findings

I read the following ranges. Quotations are short; the content is summarised.

**SA, the four-dimensional outline.**

- SA L5696-5727: the core definition through the chart Φ_{M_e(U)}(i^{−1}Log[M_e(𝐔)M_e(U)^{−1}]) in a "chosen continuation domain". This is the (R5) chart that stopped the earlier lanes (`stage-thm.md` Result).
- SA L6124-6135, (R22): c_σ(x|m) = 1 − β_s(1 − 2^{−(t−m)}) + ϖ_φ 𝗀_t(m) − β_R Σ_{l∈Re_σ(x)} 2^{−|m−l|}, with 𝗀_t(m) = θ_sβ_s 2^{−(t−m)} for m < t and β_s for m = t. SA L6137-6148: the lift L_♭^{2e_σ(x)}, "except for the real-potential gauge bounds", and "The data must ensure c ≤ c_σ ≤ 1 + β_s".
- SA L6150-6153: "The claims that restriction or a stage substitution maps one such space into another are analytic inclusion hypotheses." The outline does not prove them.
- SA L6155-6173: stored fluctuation variables are real bond forms, Borel in near variables, analytic in far variables and switches |μ_b| < λ_l^{st}.
- SA L6080-6118: the operation at level t integrates stored fields in 𝖭_t stages; a drop-out fails after n ≤ 𝖭_t stages and keeps them; (R21) defines the determining sequence (ν = n, "governs backgrounds") and the action sequence (ν = 0, "governs the sums and the coupling profiles"); phase weight 1 − n/(2𝖭_t) after n stages (L6116-6118).
- SA L17257: ε_k = g_k p₀(g_k), fluctuation threshold δ_k = (A₁/A₀)ε_k, "differ by a small fixed ratio".
- SA L17624 (one long paragraph): the stage tests; "The ratio δ′_j/ε_j=(A₁/A₀)(log x_j)^{−(𝔭₀−𝔭₁)} dominates the fixed constants"; "On the outermost shells, where the collars of the stages overlap, this requirement is relaxed by a factor L_♭^2 for each overlap", 2 ≤ L_♭ < L/2; k_♯ defined by MŘ_{k_♯+1}L^{k_♯+1−k} = M; "The collars of the stages with j ≤ k_♯ are disjoint, and the collars of the later stages overlap"; the lift on shell i is L_♭^{2(i−k_♯−1)_+}, growing "until it reaches Ř_k^c"; "In passing from the scale j+1 to the scale j one gains L^{−2} and pays L_♭^2"; and the running bound "ε_j/ε_i ≤ C(1+(j−i)^{1/2}), the bound valid for every pair of levels (2e)".
- SA L19410: "the waiting depth Ř_j = 𝖭_j" is made with the running minimum of the frame. So 𝖭_t depends on the coupling.
- SA L9913: "It is here that the argument needs the boundary to run within one layer." (taken from `layered-a3.md:12-14`; I did not reread L9913.)

**CA-I, the complete account.** I take these from the library notes, which quote them: CA-I L54287 ("Express U^{(n)}_k through the new background U^{(n+1)}_k and the fluctuation (A_j,B_j) on the collar R_n", quoted in `shift-map.md:13-14`); CA-I L54986-54994 (Theorem 4.18 assumes "the stage theorem", `ym4-assembly.md` L240); CA-I L49495-49546 (Remark 4.14 places background inclusion "outside the implication").

**Y3, the three-dimensional manuscript.** This is the template. I read these ranges in full.

- Y3 L52979-53248, Proposition II-90-39 (L53024): a real critical configuration with r_U(𝔢) < Cε_{λ(𝔢)} has plain triples in the cores 𝒰_j°(X; b₀, b₁, c₀) for b₀, c₀ ≥ C_mb Cε_j; restriction (II-90-49); half cores under (II-90-13). Its proof: running inequality (II-90-41), cube gauges, subordinate towers are real gauge transforms of restrictions.
- Y3 L53250-53601: the structures σ = (s, φ), the table (II-2-9) at L53266, the domain Definition II-86-20 at L53330 with clauses (L1)-(L4), the tower addresses (II-86-16) at L53314 as meets Ω_l^◇ ∩ Ω_l^𝔯(Z), "separated and subordinate"; Proposition II-90-62 (L53427): plain triples of the actual background lie in the half-radius domains of every structure; Corollary II-99-39 (L53529): the real point of a step lies in the intermediate domain times the fluctuation box.
- Y3 L53603-53920, Proposition II-93-26 (L53737): the regional shift 𝔥 = (𝐇, j)(s; 𝐩(P); B′_Y) exists, is holomorphic on fixed-real-factor fibres, hereditary and covariant, and obeys the weighted bound (II-93-35) at L53752.
- Y3 L54441-54626, Lemma II-93-23 (L54449) and Proposition II-93-38 (L54530): at real critical data, s = 1, the shifted field E = e^{iη𝐀}U₊ is a gauge transform of the critical field of the shorter datum, with J^{(k)}(E) = L^{−3}J^{(k+1)}(U₊) + 𝐊.
- Y3 L55448-55930, Proposition I-95-61 (L55600) and Corollary I-95-81 (L55869): towers on a subordinate sequence, read in the ambient layer scale at settled elements, exist and are holomorphic on 𝒬^T(a_T), with size bound (ambient-tower-size) and Lipschitz bound (I-95-62) with decay rate δ_T = δ/4.
- Y3 L55931-56283, Proposition II-88-43 (L56023) and Corollary II-88-50 (L56230): the substitution margin.
- Y3 L56285-56500, Proposition II-104-17 (L56432): re-expansion of an earlier term with amplitude λ, |λ| < ϱ_X, the bound (II-104-18) and the telescoping identity (II-104-20).

**Our library.** The Result sections of all fifteen notes in the brief, and the bodies of `intrinsic-dom.md`, `stage-resp.md`, `shift-map.md`, `layered-a3.md`, and of the newer round `scratchpad/codex/chain_out/shift-map.md` (1,099 lines; its §9 and §13, Lemma M and its six attacks). In short: `intrinsic-dom.md` builds the datum tube (5)-(6) and the seven-entry domain (8) and proves nesting and the numerical inclusion (12) from (11); `stage-resp.md` proves the first-exit and return-budget implications (5)-(8); `shift-map.md` proves the restriction identity (3) and the datum forcing bound (7) on the old system, then stops at Lemma M; `layered-a3.md` proves that lifts do not absorb the reversed loss ((3): L^{2v}/L_♭^{2v} > 4^v), that profile decay pays fixed losses ((5)), and direct target-datum admission with tube room δ/8 ((9)); `d4-stage.md`, `d4-incr.md`, `d4-chart.md`, `collar-block.md`, `dropout-bt.md` are corrections within the (R5) route; `wf-c.md` Lemma C is the single-layer collar comparison; `a3-close.md`, `a3-derivative.md` are the real-critical A3 chain; `kept-cov.md`, `r-inv.md` are the covariance and naturality consumers.

---

## 3. Diagnosis: why the lanes stopped, and what changes

### 3.1 The (R5) chart

Ten lanes required the returned datum to lie in every old (R5) continuation ball (`stage-thm.md` Result). `intrinsic-dom.md` removed the old centre by gluing canonical branches into the tube 𝒯_e ((5)-(6)). We keep that tube. It is used in Theorem B to give tube distance.

### 3.2 Lemma M asks for an identity that no consumer needs

`shift-map.md` (chain_out round, §13) states Lemma M: for every complex input P ∈ D₁^int, every allowed (A_j, B_j) and every earlier parameter and switch, "the actual stage substitution has the fixed-read normal form". Its attacks fail at "identifying, for each earlier read, its actual interior/exterior projections and node return after the prepared collar changes the determining member", and, earlier, at the observation (its §4) that "SA 5800-5803 gives background recovery only 'At s = 1 and real background data'. That locus does not determine a holomorphic function of the independent variables", with the example c(s − 1)ℓ(Δ).

The example is correct. Its consequence is the opposite of a gap. Off the physical locus there is no "actual stage substitution" to be matched: the actual measure is an integral over real fields at s = 1 with the physical current, and the decoupling parameters s, the amplitude λ and the independent current are bookkeeping variables introduced by the expansion. So we are free to *define* the carried composition off the physical locus, and we define it by the response formula (design change 1). Any two holomorphic extensions that agree on the physical locus give the same integral; we only need ours to have the domain and the bounds. Y3 does exactly this: the earlier term is Φ_Y[f](s, λ; P, 𝒜, 𝔮) = f(ρ_X^{t→j}P ∔_𝒮 λρ_X^{k→j}𝔥_Y(s; P, 𝒜); 𝔮_X) (Y3 L56330-56334), and the only identification is Proposition II-93-38, at real critical data and s = 𝟏 (Y3 L54530-54545). The telescoping identity (II-104-20) is the statement that the re-expansion sums back to the composition at s = 𝟏, λ = 1.

So the question "is the kept form evaluated at the new background a Schur complement of the old one" (`shift-map.md` chain_out §13, second attack; SA L17550-17558) does not arise in admission. The kept form of an earlier step is a carried term. Its re-expansion is its composition with the substitution. Whether it stays positive is a question for NL1 and LF1 (Y3 L51336 "Positivity of the kept part"), not for ST1.

Two things must still be proved, and are: the composition is admitted (Theorems E, F), and on the physical locus it equals the actual old read (Theorem D, with the gauge handled by pinned levelling, Section 14).

### 3.3 The reversed scale loss comes from reading a tower in its own scale

`layered-a3.md` §3 (L136-140): "At the same point, a target tower can assign scale ξ_q where the ambient nest assigns ξ_{h_q}. Equation (4) then gives only C L^{2(q−h_q)} P_σ(x) in target curvature units." Its (3) shows lifts cannot absorb this. Both are correct for the domain of `intrinsic-dom.md` (8), whose second and fourth entries read the tower in its own units (L^{s−p}η_p^{−2}|∂T_e − 1|).

Y3 never meets this loss, for two reasons. First, its towers are meets: the tower sequence at address (σ″, i, Z) is (Ω_l^◇ ∩ Ω_l^𝔯(Z))_{l≤q}, "separated and subordinate" (Y3 L53314-53321). A subordinate tower never assigns a coarser layer than the ambient. Second, the tower clause (L3) is read in the ambient scale ℓ = min{m_{σ″}(x), i} (Y3 L53375-53386), and Proposition I-95-61 measures tower curvature by G = L^{2n}(∂U^{tw} − I) with n = λ^♭(x_e) the ambient layer, only at settled elements (Y3 L55603-55613). We adopt both (design change 2). The consumers read the tower only through the activities, which NL1 and LF1 rebuild on the new domains in any case (`ym4-assembly.md` L236).

### 3.4 The no-new-mark reads have a gap

`stage-resp.md` (6) and its example: at m = l < k = t, (R22) gives 𝗀_k(l) = θ_sβ_s 2^{−(k−l)}, so "Cu_l < β_R/2 gives no bound below 𝗀_k(l)/(4N)". The example shows only that the new-mark smallness is the wrong hypothesis. The right one is a shift profile proportional to 2^{−(t−m)}, with amplitude below θ_sβ_s/(8𝖭_t). The shift has such a profile because its source sits at the top layer and its kernel decays across every intervening layer (Theorem C, Lemma 6.2). Its amplitude is the stage ratio δ′_j/ε_j, which tends to zero as a power of log x (SA L17624). Theorem E(ii) does the arithmetic.

### 3.5 What Y3 does not have

Y3 has no R operation: `grep -c` finds no "drop-out" and no L_♭ in Y3_I.tex. The four-dimensional additions are the preparatory stages inside the R operation, the drop-outs, the lifts and the growing waiting depth 𝖭_t. Sections 12, 15 and 18 treat them. The place where four dimensions change the argument in an essential way is the overlap of the stage collars on the outermost shells (SA L17624). That is Lemma OS.

---

## 4. The design

### 4.1 Histories, layers and structures

[design, following SA L6080-6118 and Y3 L53255-53274] Fix a finite cutoff, a compatible torus, a history h and its label 𝒮 = (Ω_j, Λ_j, S_j)_{j≤k} with marks. Lengths at level j are in units η_j = L^{−j} (relative to the finest lattice of the run). For a separated decreasing sequence Ω_0 ⊃ Ω_1 ⊃ ⋯ ⊃ Ω_s, the layer of a site x is m(x) = max{l ≤ s : x ∈ Ω_l}, and its local scale is ξ(x) = L^{m(x)}η_0 in units of the finest lattice.

A *structure* is σ = (𝒮, ν; t, φ) as in SA L6114-6118: a label, the drop-out stage counts ν, a level t and a phase φ ∈ {in, 1, …, 𝖭_t, out}, with phase weight ϖ = 1 at input, 1 − n/(2𝖭_t) after n stages, and 0 at output. At level zero only the output structure occurs. Structures are ordered as in SA L6119-6121: σ′ ≼ σ if σ′ counts no more completed stages and has lower level, or the same level with larger phase weight.

The *determining sequence* of σ is the one with ν = n in (R21) (SA L6097-6106). It governs backgrounds and towers. The *action sequence* (ν = 0) governs sums and couplings and is not used in this file.

**Separation.** [import GEO] A sequence is *separated with gap ρ* if dist_∞(Ω_{l+1}, Ω_l^c) ≥ ρ ξ_l for every l (SA L17401 gives LM in level-l units). The meet of two separated sequences is separated (Lemma 6.1). Every determining sequence of a main step and of the preparatory stages at stage levels j ≤ k_♯ is separated with gap ρ = R₁M (Y3 L53617-53628 states the analogous requirement; SA L17624 states that these collars are disjoint). At stage levels j > k_♯ the collars overlap (SA L17624), and separation is not available. This is the boundary of what is proved here (Section 18).

### 4.2 The radius coefficient and the table

[design] For a structure σ of level t and a radius index 0 ≤ m ≤ t, use SA (R22) (SA L6124-6135):

  c_σ(x|m) = 1 − β_s(1 − 2^{−(t−m)}) + ϖ_φ 𝗀_t(m) − β_R Σ_{l∈Re_σ(x)} 2^{−|m−l|},  𝗀_t(m) = θ_sβ_s 2^{−(t−m)} (m < t), β_s (m = t),

with 0 < β_s ≤ 1/4, 0 < θ_s < 1, β_R = c_Rβ_s, and c_R ≤ (1 − θ_s)/16 [design: this smallness is our choice; it makes Lemma 4.2 below hold]. The radius table assigns r_ι(σ; m), ι = 0 (curvature, current) and ι = 1 (potential), and the lift λ_σ(x) = L_♭^{2e_σ(x)} (SA L6141-6145). The pointwise radius at a site of radius index m is

  R_σ^{p,ι}(x) = c_σ(x|m) λ_σ(x) r_ι(σ; m) L^{−pm},  p ∈ {1, 2, 3},

as in Y3 L53275-53282 with the lift added. The real-potential gauge bounds use λ_σ r_ι without c_σ (SA L6144).

**Lemma 4.2 (range of c).** [proved here] Each label point x lies in at most 3 drop-outs at any level (this is the disjointness of waiting windows, SA L6111-6113: "Their waiting windows are required to be disjoint at a point"; I use the count 3 as an [import GEO] bound, any fixed bound works with c_R scaled). Then 1 − β_s − 9β_R ≤ c_σ(x|m) ≤ 1 + β_s, and with c_R ≤ (1 − θ_s)/16 we get c_σ ≥ 1 − 2β_s ≥ 1/2.

*Proof.* The first two terms lie in [1 − β_s, 1]. At m = t they equal 1 and the phase term is ϖβ_s ≤ β_s, so the sum is ≤ 1 + β_s. For m < t the sum of the first three terms is ≤ 1 − β_s + β_s 2^{−(t−m)}(1 + θ_s) ≤ 1 − β_s + β_s(1 + θ_s)/2 ≤ 1, since t − m ≥ 1 and θ_s < 1. The mark term: for each drop-out containing x, Re contains at most 𝖭 consecutive levels, and Σ_{l∈Z} 2^{−|m−l|} = 3. So it is at most 3·3β_R = 9β_R ≤ 9(1 − θ_s)β_s/16 < β_s. Hence c ≥ 1 − 2β_s ≥ 1/2. □

### 4.3 Triples and substitution

[design, Y3 L53330-53335 and L56062-56073] A *triple at level j on a region X* is P = (U, A′, 𝐉): U a real (SU(2)-valued) configuration on Bd(X), A′ a complex Lie-algebra-valued bond form, 𝐉 a complex bond form (the independent current), with complex field 𝐔 = e^{iη_jA′}U. A *shift* is a pair 𝔥 = (𝐀, 𝐊) of complex bond forms. The *substitution* is

  P ∔ 𝔥 = (U, A″, 𝐉 + 𝐊),  A″ = (iη_j)^{−1} log(e^{iη_j𝐀} e^{iη_jA′}),

defined where the logarithm series converges (Lemma 5.1). The real factor U is not changed. On a set of bonds 𝒮, ∔_𝒮 substitutes on 𝒮 and leaves other bond components unchanged (Y3 L56337-56340).

### 4.4 Meet towers and settled elements

[design, Y3 L53308-53328, L55448-55485] For σ′ ≼ σ, a *tower address* in a region Y is (σ″, i, Z) with σ″ ≼ σ′, 1 ≤ i ≤ level(σ″), Z a localisation region of level i − 1 contained in Y and meeting the current small-field region. Its tower sequence at depth q ≤ i, under either erosion rule 𝔯 ∈ {𝔯₁, 𝔯₂}, is the meet

  Ω′_l = Ω_l^{σ} ∩ Ω_l^𝔯(Z),  0 ≤ l ≤ q,

where Ω^σ is the determining sequence of the *current* structure σ. Its determining set is 𝐁′, its tower configuration is U_q^𝔯 = T_{𝐁′}(M_{𝐁′}(𝐔)), the intrinsic map of `intrinsic-dom.md` (6) at the actual average of 𝐔. An inner plaquette or full bond e of Z is *settled* when λ′(x_e) = min{λ^♭(x_e), q}, with λ^♭ the ambient layer and λ′ the tower layer (Y3 L55473-55476).

This is the change from `intrinsic-dom.md` §4: there the tower of a record was the record's own tower; here it is the meet with the current determining sequence. The record keeps its geometric data (levels, regions, both erosion rules, truncations and preceding structures, `stage-thm.md:58-63`), so the meet is determined.

### 4.5 The graded intrinsic domain

**Definition 4.5 (the domain Ũ_{σ′|σ}(Y)).** [design; Y3 Definition II-86-20 at L53330, with SA's lift and four-dimensional entries] Let σ′ ≼ σ, Y a region of level s′ − 1, and P = (U, A′, 𝐉) a triple at level s′ on Y. P ∈ Ũ_{σ′|σ}(Y) if:

- **(L1) seven pointwise entries, part one: five on the triple.** On Bd_𝒮(Y) (bonds of Y inside the current small-field region, Y3 L53295-53302), at every stencil there contained,
  |∂U − 1|, |∂𝐔 − 1| < R_σ^{2,0},  η_{s′}^{3}|𝐉| < R_σ^{3,0},  η_{s′}|A′| < R_σ^{1,1},  η_{s′}^2|∇_U A′| < R_σ^{2,1}.
- **(L2) real gauge witnesses.** For every σ″ ≼ σ′, 0 ≤ l ≤ level(σ″) and cube q ⊂ Y ∩ Ω_l of side ≤ 𝗈LM in level-l units, U has a real gauge U^v = e^{iη_lA} on its inner bonds with |A|, |∇^{η_l}A| < 𝗈LMB^{cg} λ_σ r_0(σ″; l) (no c_σ). The four cube families of CA-I L48527-48565 (table in `stage-thm.md:122-127`) are instances: each of their cubes is such a q, with the radius index and lift of that table.
- **(L3) seven pointwise entries, part two: two on the towers.** At every tower address, both rules and 1 ≤ q ≤ p ≤ i, the tower U_q^𝔯 and its current exist, and on Z^{≀p}, with ℓ = min{m_{σ″}(x), i} at the base point,
  |∂U_q^𝔯 − 1| < L^{i−p} c_σ(ℓ) λ_σ r_0(σ″|σ; ℓ) L^{−2ℓ},
  η_q^3|J_q^𝔯| < L^{i−p} c_σ(ℓ) λ_σ r_0(σ″|σ; ℓ) L^{−2ℓ−min(q,ℓ)},
  imposed only at settled elements whose stencils lie in Bd°(Z_𝒮); and the same with 𝐔 replaced by U. Here r(σ″|σ; l) is the ambient convention of Y3 (II-86-8): r(σ; s) at a common top layer, r(σ″; l) otherwise.
- **(L4) cores.** At every core address (σ″, i, X′) (X′ ⊂ Y ∩ Λ_i of level i − 1), the restriction ρ_{X′}^{s′→i}P lies in the small-field core 𝒰_i°(X′; c_σ(i)r_0(σ″|σ; i), c_σ(i)r_1(σ″|σ; i)) of NL1 [import CORE].

Write Ũ_σ = Ũ_{σ|σ}. The superscript 1/2 halves every table entry and the witness constant, with c_σ unchanged (Y3 L53389-53392).

The *seven entries* of `intrinsic-dom.md` (8) are the five of (L1) and the two of (L3). The witnesses (9) of `intrinsic-dom.md` are (L2). The tube condition of intrinsic-dom (5) is not imposed: Theorem B proves it on the domain.

**Lemma 4.6 (nesting; ST1(1)).** [proved here] If σ_1, σ_2 have the same label, marks and level, and c_{σ_1}(x|m) ≤ c_{σ_2}(x|m) for all x, m, then Ũ_{σ′|σ_1}(Y) ⊂ Ũ_{σ′|σ_2}(Y) for the same field, provided the tower addresses of σ_1 contain those of σ_2.

*Proof.* (L1), (L3), (L4) are strict upper bounds whose right sides are increasing in c and (for (L4)) the cores are increasing in their radii; (L2) does not involve c; the set of addresses of σ_2 is contained in that of σ_1, so every clause required for σ_2 is required for σ_1 with a smaller or equal right side. □

### 4.6 Carried terms

[design, Y3 L56290-56305] A *carried term* formed at level j is one of: a regular term f on a fixed core 𝒰_j°(X; b₀, b₁) with X ⊂ Λ_j; a boundary term or formed exponent on a layered output space Ũ_{(j,out)}(X) with its stored coordinates 𝔮 of levels < j; a kept form or elimination factor (a pair function, `kept-cov.md` (4), (8)); a drop-out term on the determining sequence of its drop-out (Section 15). Every carried term is required [design] to be:

- holomorphic on each fixed-real-factor fibre of its domain, bounded there by its formation bound b_f;
- Borel in the real factor and in the near stored variables, analytic in the far stored variables and switches (SA L6160-6173);
- invariant under real gauges acting jointly on the triple and the stored coordinates (native covariance, `intrinsic-dom.md` §3 and `kept-cov.md`);
- *tied*: for real triples it depends on P only through its pair (𝐔, 𝐉) (Y3 L56461-56463 "has the tie for real triples").

All four are properties that NL1, LF1 must give their activities; they are what Y3 Proposition II-104-17 assumes (Y3 L56443-56446).

### 4.7 The stage map

[design, Y3 L56324-56340] Let a stage (main step at level t = k + 1, or preparatory stage n → n + 1 of the operation at level t) integrate the fluctuation 𝒜 on its source bonds. For a carried term f formed at level j on X, and a localisation region Y ⊃ X^↑, the carried composition is

  Φ_Y[f](s, λ; P, 𝒜, 𝔮) = f(ρ_X^{t→j}P ∔_𝒮 λρ_X^{k→j}𝔥_Y(s; P, 𝒜); 𝔮_X)  (plain),

and the pinned variant replaces λ𝔥_Y by its pinned levelling (λ𝔥_Y)^δ[P] (Section 14). Here P is the triple of the current intermediate structure, 𝔥_Y is the regional shift of Section 10, s is the decoupling parameter in the polydisc 𝔻(Y), λ is the amplitude, and 𝔮_X is the restriction of the stored coordinates, unchanged. The term after the stage is the evaluation at s = 𝟏, λ = 1, written as a telescoping sum of localised increments (Theorem F).

This defines S_n(P; ζ) of `ym4-assembly.md` L229 off the physical locus: ζ = (s, λ, 𝒜, 𝔮, switches), and S_n(P; ζ) = ρP ∔ λρ𝔥(s; P, 𝒜). On the physical locus it is the actual old read (Theorem D).

### 4.8 Consumer changes

[design] Each change below is a change of definition. None is a claim that the old definition fails.

1. **Towers.** Inherited towers are meets with the current determining sequence, read in the ambient layer scale at settled elements (4.4, (L3)). Consumer: the activities of NL1, LF1 compute their tower backgrounds on the meet. This is the same tower wherever the record's sequence is already subordinate (the meet then equals it).
2. **Stage map.** The carried composition off the physical locus is the substitution of 4.7. Consumer: SA L17564 "both written in the new variables" is satisfied by definition; (LOC) reads the amplitude λ as its interpolation parameter ν.
3. **Real factor.** Substitution does not change the real factor U. Consumer: the "one real splitting for all records" of `intrinsic-dom.md` L222 is automatic.
4. **Stored coordinates.** Fixed through stages (Y3 L56305 "All stored coordinates remain fixed"). Consumer: stored-slot admission reduces to formation (Section 14.3).
5. **Waiting depth.** (N-growth) of Section 16 caps the growth of 𝖭_t = Ř_t. Consumer: LF1's choice of Ř (SA L19410).
6. **The tube clause.** Not part of the domain; proved on it (Theorem B).

---

## 5. Elementary lemmas

All norms on 2×2 complex matrices are operator norms; Lie-algebra elements are complex traceless 2×2 matrices. Every proof in this section is by hand and uses only power series.

**Lemma 5.1 (logarithm of a product).** [proved here; Y3 L56066-56080 with weaker constants] Let ℓ(X, Z) = log(e^X e^Z) − X − Z for complex 2×2 matrices.
(a) If |X| + |Z| ≤ 1/2, ℓ is defined by the logarithm series and |ℓ(X, Z)| ≤ 3.
(b) If |X| + |Z| ≤ 1/4, then |ℓ(X, Z)| ≤ 12(|X| + |Z|)².
(c) If |X| ≤ 1/8 and |Z| ≤ 1/16, then |ℓ(X, Z)| ≤ 4|X|.
(d) If |X|, |X′| ≤ 1/16 and |Z|, |Z′| ≤ 1/16, then |ℓ(X, Z) − ℓ(X, Z′)| ≤ 96|X||Z − Z′| and |ℓ(X, Z) − ℓ(X′, Z)| ≤ 12|X − X′|.
(e) Ad(g)ℓ(X, Z) = ℓ(Ad(g)X, Ad(g)Z) for every invertible g.

*Proof.* (a) W = e^Xe^Z − 1 = Σ_{a+b≥1}X^aZ^b/(a!b!) has |W| ≤ e^{|X|+|Z|} − 1 ≤ e^{1/2} − 1 < 0.65. The series log(1 + W) = Σ_{r≥1}(−1)^{r+1}W^r/r converges and |log(1 + W)| ≤ |W|/(1 − |W|) < 1.86. Hence |ℓ| ≤ 1.86 + 1/2 < 3. The function ℓ is holomorphic in the entries of (X, Z) on the open set |X| + |Z| < 1/2 + ε for small ε > 0, since it is a convergent composition of power series there.
(b) Expanding, e^Xe^Z = 1 + X + Z + O(2) and log(1 + W) = W + O(W²), so ℓ has no constant and no linear term. Put u = |X| + |Z| > 0 and F(z) = ℓ(zX/(2u), zZ/(2u)) for |z| < 1 + ε′. The arguments have norm sum |z|/2 ≤ 1/2 + ε′/2, so by (a) (with ε chosen accordingly) F is holomorphic and |F| ≤ 3 on the closed unit disc, and F(0) = F′(0) = 0. The second-order Schwarz lemma (apply Lemma 5.3(a) to F(z)/z) gives |F(z)| ≤ 3|z|². At z = 2u ≤ 1/2 this is |ℓ(X, Z)| ≤ 12u².
(c) Put X̂ = X/|X| (X ≠ 0; X = 0 is trivial since ℓ(0, Z) = 0) and H(z) = ℓ(zX̂, Z) on |z| ≤ 1/8. There |zX̂| + |Z| ≤ 3/16 ≤ 1/4, so |H| ≤ 12(3/16)² < 1/2 by (b), and H(0) = 0. Lemma 5.3(a) gives |ℓ(X, Z)| = |H(|X|)| ≤ (1/2)|X|/(1/8) = 4|X|.
(d) At points (Y, W) with |Y| ≤ 1/8 and |W| ≤ 1/16, the ball of radius 1/16 about W in the Z variable stays in |Y| + |Z| ≤ 1/4, where |ℓ| ≤ 12/16 < 1 by (b). Cauchy's estimate (Lemma 5.3(b), one complex direction at a time, along the segment from Z′ to Z) gives |D_Zℓ(Y, ·)| ≤ sup|ℓ|/radius ≤ (3/4)/(1/16) = 12 there (sup|ℓ| ≤ 12·(1/4)² = 3/4). So H(z) = ℓ(zX̂, Z) − ℓ(zX̂, Z′) obeys |H| ≤ 12|Z − Z′| on |z| ≤ 1/8 and H(0) = 0; Lemma 5.3(a) gives |H(|X|)| ≤ 12|Z − Z′||X|/(1/8) = 96|X||Z − Z′|. The bound in X is the same Cauchy estimate in the X variable: |D_Xℓ| ≤ 12 on |X| ≤ 1/16, |Z| ≤ 1/16, integrated along the segment from X′ to X.
(e) Ad(g)e^X = e^{Ad(g)X} and Ad(g)log(1 + W) = log(1 + Ad(g)W) term by term. □

**Lemma 5.2 (substitution increments).** [proved here; Y3 (II-88-29), (II-88-30) at L56073-56095, with weaker constants] Let η be the bond length of the triple, and assume at every bond used that η|𝐀|, η|A′| ≤ 1/16. Put D = A″ − A′, with A″ = (iη)^{−1}log(e^{iη𝐀}e^{iηA′}). Use the real covariant difference (∇_U X)(b) = U(e)X(b⁺)U(e)^{−1} − X(b), b = ⟨x, x + ηe_ν⟩, e = ⟨x, x + ηe_μ⟩, b⁺ = b + ηe_μ.
(a) η|D(b)| ≤ 5η|𝐀(b)|.
(b) η²|∇_U D|(b) ≤ 13η²|∇_U𝐀|(b) + 96η|𝐀(b)|·η²|∇_UA′|(b).
(c) For a plaquette p with corners and bonds in the domain, |∂(e^{iη𝐀}𝐔)(p) − 1| ≤ |∂𝐔(p) − 1| + C₅[η²|∇_U𝐀|_p + η|𝐀|_p(η|𝐀|_p + η|A′|_p + |∂𝐔(p) − 1|)], with C₅ an absolute constant, where |·|_p is the maximum over the four bonds of p.

*Proof.* (a) iηD = iη𝐀 + ℓ(iη𝐀, iηA′), and |ℓ(iη𝐀, iηA′)| ≤ 4η|𝐀| by Lemma 5.1(c).
(b) By Lemma 5.1(e) with g = U(e) (unitary), Ad(U(e))ℓ(iη𝐀(b⁺), iηA′(b⁺)) = ℓ(X₁, Z₁) with X₁ = iηAd(U(e))𝐀(b⁺), Z₁ = iηAd(U(e))A′(b⁺); put X₀ = iη𝐀(b), Z₀ = iηA′(b). Then iη∇_UD(b) = iη∇_U𝐀(b) + [ℓ(X₁, Z₁) − ℓ(X₀, Z₁)] + [ℓ(X₀, Z₁) − ℓ(X₀, Z₀)]. By Lemma 5.1(d) the first bracket is ≤ 12|X₁ − X₀| = 12η|∇_U𝐀(b)| and the second is ≤ 96|X₀||Z₁ − Z₀| = 96η|𝐀(b)|·η|∇_UA′(b)|. Multiply by η.
(c) Write the plaquette p = (b₁, b₂, b₃, b₄) with orientations ε_i = ±1, and let h = ∂𝐔(p) be the holonomy of 𝐔 from the base point. Moving each factor e^{iη𝐀(b_i)^{ε_i}} to the end by the partial holonomies of 𝐔 (which are products of at most three factors 𝐔(b) = e^{iηA′(b)}U(b), each of norm ≤ e^{1/16}, so their conditions numbers are ≤ e^{6/16} < 2) gives ∂(e^{iη𝐀}𝐔)(p) = h·e^{Y₁}e^{Y₂}e^{Y₃}e^{Y₄} with |Y_i| ≤ 2η|𝐀|_p. Three applications of Lemma 5.1(b) give e^{Y₁}⋯e^{Y₄} = e^{Y₁+⋯+Y₄+R} with |R| ≤ 3·12(8η|𝐀|_p)², valid when 8η|𝐀|_p ≤ 1/4, i.e. η|𝐀|_p ≤ 1/32 (shrink the hypothesis by a factor 2 if needed; this only changes C₅). The sum Y₁ + ⋯ + Y₄ is iη times the lattice covariant curl of 𝐀 around p, transported by 𝐔: replacing the partial holonomies of 𝐔 by those of U changes each Y_i by at most (e^{2·3η|A′|_p} − 1)|Y_i| ≤ 12η|A′|_p|Y_i|, and the U-transported curl equals η(∇_U𝐀_ν − ∇_U𝐀_μ) up to the transport around the full plaquette, which differs from the identity by |∂U(p) − 1| ≤ |h − 1| + |∂𝐔(p) − ∂U(p)|; the latter is ≤ 8η|A′|_p by the same telescoping. Hence |Y₁ + ⋯ + Y₄| ≤ 2η²|∇_U𝐀|_p + Cη|𝐀|_p(η|A′|_p + |h − 1|). Finally |h e^{Y} − 1| ≤ |h − 1| + |h||e^Y − 1| ≤ |h − 1| + 2·2|Y| for |Y| ≤ 1/2. Collect. □

These bounds are used only through this consequence: *in the domain, the potential, its difference and the curvature change under substitution by at most a fixed constant C₅′ times the corresponding normalised norms of the shift.* Y3 obtains the constants 1, 3/2, 3/2 and 2.03 (Y3 L56100-56116); our constants are larger and absolute, and Section 16 absorbs them into the amplitude ceiling.

**Lemma 5.3 (Schwarz and Cauchy).** [proved here] (a) If F is holomorphic on |z| < R, |F| ≤ M and F(0) = 0, then |F(z)| ≤ M|z|/R. (b) If F is holomorphic on a polydisc of radii R_1, …, R_n about a real point and bounded by M, then |∂^α F| ≤ M α! R^{−α} at the centre. (c) For a function of several variables bounded by M on the polydisc and vanishing whenever a variable in 𝒦 vanishes, the Boolean bracket over the unit cube is bounded by M(R − 1)^{−|𝒦|} times 2 (`intrinsic-dom.md` (13)).

*Proof.* (a) F(z)/z is holomorphic; on |z| = r < R it is bounded by M/r; the maximum principle and r → R give the claim. (b) Cauchy's integral formula on the product of circles. (c) is `intrinsic-dom.md` L307-319, which I reread: Schwarz in ν gives 2M_f/ϱ_F; Cauchy circles of radius < R_s − 1 at each point of the real unit cube give the factor (R_s − 1)^{−|𝒦|}. □

**Lemma 5.4 (real and imaginary parts).** [proved here; Y3 (I-95-60) at L55802] If F is holomorphic and bounded by M₀ on a ball of radius r about 0 in a complex Banach space with a real structure, then for ‖z‖ ≤ r/2,
  |F(z)| ≤ 3|F(0)| + |F(Re z)| + |F(Im z)| + 6M₀‖z‖²/r².

*Proof.* Write F(w) = F(0) + DF(0)w + R(w). For ‖w‖ ≤ r/2, Cauchy's estimate on the complex line through w gives |R(w)| ≤ 2M₀‖w‖²/r² (second-order Schwarz on the disc of radius r in that line, rescaled). Then DF(0)z = DF(0)Re z + i DF(0)Im z, and DF(0)Re z = F(Re z) − F(0) − R(Re z), similarly for Im z. Collect: |F(z)| ≤ |F(0)| + |F(Re z) − F(0)| + |F(Im z) − F(0)| + |R(Re z)| + |R(Im z)| + |R(z)| ≤ 3|F(0)| + |F(Re z)| + |F(Im z)| + 6M₀‖z‖²/r², using ‖Re z‖, ‖Im z‖ ≤ ‖z‖ (the real structure is assumed to have this property, true for the sup norms used). □

**Lemma 5.5 (the elementary sum).** [proved here] For integers q ≥ 0, q + 1 ≤ 4^q; hence √(1+q) e^{−Dq} ≤ 2^{−q} for D ≥ log 4, and Σ_{q∈Z} 2^{−|q|} = 3.

*Proof.* q = 0 is equality; q + 2 ≤ 4(q + 1) gives the step. Then √(1+q) ≤ 2^q and e^{−Dq} ≤ 4^{−q}. The sum is 1 + 2Σ_{q≥1}2^{−q} = 3. □

**Lemma 5.6 (the gaps; ST1(2)).** [proved here; Y3 (II-88-21), (II-88-22) at L55977-56003, with SA (R22)] Fix x and m ≤ t.

(i) *Main step.* Between the output structure of level t − 1 and the input structure of level t, with the same marks,
  c_{(t−1,out)}(x|m) − c_{(t,in)}(x|m) = (1 − θ_s)β_s 2^{−(t−m)}  (m ≤ t − 1).
(ii) *Preparatory stage.* Between consecutive phases n, n + 1 at level t, with new marks E_n,
  c_{(t,n)}(x|m) − c_{(t,n+1)}(x|m) = θ_sβ_s 2^{−(t−m)}/(2𝖭_t) + β_R Σ_{l∈E_n} 2^{−|m−l|}  (m < t),
and β_s/(2𝖭_t) + β_R Σ_{l∈E_n}2^{−|m−l|} at m = t.
(iii) *Sum.* Over the 𝖭_t stages of one operation the gaps (ii) at fixed m sum to at most 𝗀_t(m)/2 + 3β_R per drop-out containing x. This is `intrinsic-dom.md` (10), proved there; I reprove it: the phase part sums to 𝖭_t·𝗀_t(m)/(2𝖭_t) = 𝗀_t(m)/2, and the mark part to β_R Σ_l 2^{−|m−l|} ≤ 3β_R since each level is marked once per drop-out.

*Proof.* (i) c_{(t−1,out)}(m) = 1 − β_s + β_s 2^{−(t−1−m)} = 1 − β_s + 2β_s2^{−(t−m)}; c_{(t,in)}(m) = 1 − β_s + β_s 2^{−(t−m)} + θ_sβ_s2^{−(t−m)}. Subtract. (ii) Only ϖ changes, by 1/(2𝖭_t), and the mark set gains E_n. □

So every read, marked or not, receives at every stage a positive gap. The smallest is the phase-only gap θ_sβ_s 2^{−(t−m)}/(2𝖭_t) of a preparatory stage.

**Lemma 5.7 (the profile).** [proved here; Y3 (II-88-12) at L55953 and (history-profile-decay) at L56009] For a stage at level t, let d_min(m) = θ_sβ_s2^{−(t−m)}/(2𝖭_t) for a preparatory stage and (1 − θ_s)β_s2^{−(t−m)} for a main step, and put w(m) = ½d_min(m)r_0(m). Assume [import RUN] in the form r_0(n + ν) ≤ C_run(1 + ν^{1/2})r_0(n) and r_0(n) ≤ C_run r_0(n + ν) for n, ν ≥ 0. Then for n, ν ≥ 0 and p ≥ 1:
(a) w(n − 1) ≤ (C_run/2)w(n);
(b) w(n + ν)L^{−p(n+ν)} ≤ w(n)L^{−pn} whenever L ≥ 4C_run;
(c) e^{−ω(ν−1)}w(n + ν) ≤ 4C_run w(n) for ν ≥ 1, whenever ω ≥ log 4.

*Proof.* w(n + ν)/w(n) = 2^ν r_0(n + ν)/r_0(n) ≤ 2^νC_run(1 + √ν) ≤ C_run 4^ν, using 1 + √ν ≤ 2^ν (Lemma 5.5). (a) w(n − 1)/w(n) = r_0(n − 1)/(2r_0(n)) ≤ C_run/2. (b) The ratio is ≤ C_run4^νL^{−pν} ≤ C_run(4/L)^ν ≤ 1 for ν ≥ 1 and L ≥ 4C_run (if C_run ≥ 1), and = 1 for ν = 0. (c) e^{−ω(ν−1)}C_run4^ν = 4C_run(4e^{−ω})^{ν−1} ≤ 4C_run. □

**Four-dimensional change.** Y3 uses the three-dimensional running ε_i ≤ κ_run L^{(i−j)/2}ε_j (Y3 L52990-52993) and (Q5.2) L^{−ν}2^νr(n+ν) ≤ r(n) (Y3 L55942). In four dimensions the radii vary by at most C_run(1 + ν^{1/2}) over ν levels (SA L17624), which is weaker growth, so every Y3 inequality of this kind holds with room once L ≥ 4C_run².

---

## 6. Geometry

**Lemma 6.1 (meets).** [proved here; Y3 L53317-53319] If (Ω_l) and (Ω′_l) are decreasing and separated with gaps ρ, ρ′ (dist_∞(Ω_{l+1}, Ω_l^c) ≥ ρξ_l), then (Ω_l ∩ Ω′_l) is decreasing and separated with gap min(ρ, ρ′), and it is subordinate to both (memberwise contained).

*Proof.* (Ω_l ∩ Ω′_l)^c = Ω_l^c ∪ Ω′_l^c. A point of Ω_{l+1} ∩ Ω′_{l+1} has distance ≥ ρξ_l from Ω_l^c and ≥ ρ′ξ_l from Ω′_l^c, hence ≥ min(ρ, ρ′)ξ_l from the union. Decrease and containment are immediate. □

**Lemma 6.2 (crossing layers).** [proved here; Y3 (ambient-tower-geometry) at L55632 and its proof L55642-55660; `layered-a3.md:105-111`] On a separated sequence with gap ρ, let d be the weighted path distance with density ξ(x)^{−1}. Then |m(x) − m(z)| ≤ 1 + d(x, z)/ρ. Equivalently, if m(z) = m(x) + ν, ν ≥ 1, then d(x, z) ≥ ρ(ν − 1).

*Proof.* A connected path from layer m(x) to layer m(x) + ν crosses, for each m(x) < q < m(x) + ν, the strip Ω_q ∖ Ω_{q+1}° of Euclidean width ≥ ρξ_q (separation), where the density is ξ_q^{−1}; each strip contributes ≥ ρ, and the crossings have disjoint interiors. There are ν − 1 such strips. □

**Lemma 6.3 (scale ratio).** [proved here; Y3 L55636-55640] For a subordinate sequence with layer λ′ ≤ λ^♭ and ς(x) = ξ^♭(x)/ξ′(x) ≥ 1, if both are separated with gap ρ then ς(x)/ς(z) ≤ L^{2 + 2d′(x,z)/ρ}, where d′ is the tower weighted distance, and d′ ≥ d^♭.

*Proof.* d′ ≥ d^♭ because the tower density ξ′^{−1} ≥ ξ^{♭−1} pointwise (λ′ ≤ λ^♭), and on shared faces a perturbation into the deeper cube changes length by an arbitrarily small amount (Y3 L55642-55650). By Lemma 6.2 applied to each sequence, |λ^♭(x) − λ^♭(z)| ≤ 1 + d^♭/ρ ≤ 1 + d′/ρ and |λ′(x) − λ′(z)| ≤ 1 + d′/ρ. So log_L(ς(x)/ς(z)) = (λ^♭(x) − λ^♭(z)) − (λ′(x) − λ′(z)) ≤ 2 + 2d′/ρ. □

**Lemma 6.4 (settlement and distance to the end of a tower).** [proved here; Y3 L55822-55825] At a settled element with ς > 1, the tower has ended at its top p, and a bond b with d′(x, x_b) = D outside the distance-l neighbourhood obeys ς ≤ 1 + D.

*Proof.* Settled means λ′ = min{λ^♭, p}; ς > 1 means λ′ < λ^♭, so λ′ = p. A point outside the l-neighbourhood is at Euclidean distance > l = ξ^♭(x), and the tower density near x is ≥ ξ_p^{−1}; so D > l/ξ_p = ς. □

**Lemma 6.5 (the stage sequences are ordered).** [proved here from the sources] At a preparatory stage n → n + 1 of the operation at level t, with j = t − 𝖭_t + n, the old determining sequence Ω^− and the new Ω^+ satisfy Ω_q^− ⊂ Ω_q^+ for all q, with equality unless q = j + 1; the changed rows have an endpoint in R_n = Z_{j+1} ∖ Z″_{j+1}. Hence layers do not decrease: m^−(x) ≤ m^+(x).

*Proof.* This is `shift-map.md` §1 (its (1) and L24-41), which reads SA L17415, L17436, CA-I L53812-53814 and SA L5616-5617; I checked the logic: the stage integrates R_n and replaces only the member of level j + 1 by a larger region. Layers are maxima of indices of containing members; enlarging a member can only raise them. □

So an old (pre-stage) structure's tower is subordinate to the new determining sequence: no reversed loss arises from a stage. A drop-out keeps its stages (SA L6088), so its determining sequence is the ν = n sequence (R21), again of this form.

---

## 7. Imports

Each import is stated in the form used, with its source and status. "Separated" means separated with gap ρ = R₁M above the geometric floors of Section 16.

**[import GEO]** (LF1(2), C2). The determining sequences of histories are separated; meets with localisation regions are separated (Lemma 6.1); the preparatory stage sequences at stage levels j ≤ k_♯ are separated; at most 3 drop-outs meet at a point; tori are large compared with the cubes; the stage geometry of Lemma 6.5. Status: GEO1-GEO6, EXT, W3 [C] under three supplied rules (`ym4-assembly.md` L306); rest of C2 [O]. *Not* available: separation at stage levels j > k_♯ (SA L17624; Lemma OS).

**[import BG]** (BG1(2), (4)). On a separated sequence with determining set 𝐁, every real datum V in the admitted class ℛ_𝐁 (tested holonomies below the threshold ε̄) has a unique regular critical orbit; its axial representative Φ_V is real at real data and holomorphic on ‖B‖_∞ < r_B; restriction identity: for memberwise nested separated sequences and real ε₁-regular V, U_{𝐁′}(M_{𝐁′}(U_𝐁(V)|_{Ω′_0})) = U_𝐁(V)|_{Ω′_0} modulo residual gauges (SA L9776-9780, as quoted in `shift-map.md:62-68`); the intrinsic tube 𝒯_𝐁 of radius δ ≤ min{1/40, r_B/40} and T_𝐁 holomorphic on it (`intrinsic-dom.md` (5)-(6)). Status: (2) [C] as an implication on separated sequences (`gates/a1-balaban-gate.md`); (4) [P].

**[import AV]** (averaging). For a real U with tower-scale curvature < a on the carriers, M_𝐁(U) is c^♮a-regular, c^♮ = 2L² (Y3 L55673-55690 in three dimensions; four-dimensional statement: SA L9667's converse "within 2ε inside a layer and within CL²ε across a seam", as quoted in `layered-a3.md:167`); and the complex average of e^{iηw}U is e^{iβ}M(U) with |β_q(c)| ≤ 2ξ_q sup_{𝒫(q,c)}|w| (`wf-c.md:43`, as quoted in `layered-a3.md:172-173`). Status: `a3-close.md:87` uses it as checked; [C] in the A3 chain.

**[import PROF]** (PR1(3)). At a real critical regular background on a separated sequence, η^{−2}l(x)²|∂U − 1| and l(x)³|J(U)| ≤ C_P P_σ(x), P_σ(x) = max_τ e^{−δ_prof d_σ(x,τ)}|∂𝐕(τ) − 1| (SA L9681; `a3-profile.md:625-660`). Status: [C] in the real-critical A3 chain.

**[import DR]** (decoupled response; PR1(2) for a fixed system). On a fixed separated determining system with an admitted pair (natural local class at radius a_D) and a source B′ on its rows with ‖B′‖ < cB^{−4}, the decoupled response (𝐇, j)(s; pair; B′) exists, is jointly holomorphic in s ∈ 𝔻, the pair (on fixed-real-factor fibres) and B′, with ‖𝐇‖ ≤ 2B‖B′‖ and ‖D_{B′}𝐇[β]‖_{X,w} ≤ 2B‖β‖_{Y,w} for exponential weights w = e^{θd} (`dec-field.md` Proposition 5.1, L247-280, under [PW], [NL]); the current increment j obeys the analogous bound with the current scaling. Status: Proposition 5.1 [P] as an implication; [PW] in `pw-bridge.md` with retained premises; [NL] in `nl-r9.md` under [RED]; NL1(2) [C] as an implication end to end (`ym4-assembly.md` L288).

**[import CRIT]** (the response at criticality). If the pair is (U₀, J°(U₀)) with U₀ real critical on the system and s = 𝟏, then e^{iη𝐇}U₀ is critical with datum (e^{iB′}M(U₀))^v, v the site factors, and J(e^{iη𝐇}U₀) = J(U₀) + j at complete stencils; Q(𝐇) = B′ on the determining rows. Sources: SA L5800-5803 ("At s = 1 and real background data", quoted in `shift-map.md:176`), SA L10446-10458 (quoted in `shift-map.md` chain_out L983); Y3 Proposition I-88-127 in three dimensions (cited at Y3 L54515, L54575). Status: [SS] in SA; I have not found it rebuilt in our library. *This is a gap in the imports, not in ST1; see Section 18.4.*

**[import CORE]** (the small-field cores and outer-core substitution). The cores 𝒰_j°(X; b₀, b₁) of NL1 and the outer-core substitution lemma (Y3 Proposition II-16-69, used at Y3 L56214-56224): substitution of a shift of norm below τb₀/[C_os K^♯(1 + 𝖼_♮)] maps 𝒰_j°(X; (1 − τ)b₀, (1 − τ)b₁) into 𝒰_j°(X; b₀, b₁). Status: four-dimensional analogue is NL1(2)-(4) (`wf-c.md` Theorem A, `loc-4.md` §§3-7 [C]); the substitution lemma itself in four dimensions [O] as a separate statement; it is the core clause of the substitution margin and I treat it as part of NL1's core package.

**[import FL]** (the fluctuation box). On the support of a history, the stage fluctuation 𝒜 satisfies |𝒜| < δ_k (main step) or δ′_j (preparatory stage) on its source bonds, and on the complex contour used by NL1's Gaussian step it stays below C_𝒜δ_k, resp. C_𝒜δ′_j (Y3 Corollary II-99-39 at L53529 and L51982 "The contour estimate" in three dimensions; SA L17257, L17624 for the four-dimensional thresholds). Status: the real part is the definition of the tests; the complex contour bound is NL1's (B4 Gaussian step).

**[import RUN]** The four-dimensional running of thresholds and radii: ε_j = g_jp₀(g_j), δ_k = (A₁/A₀)ε_k, δ′_j/ε_j = (A₁/A₀)(log x_j)^{−(𝔭₀−𝔭₁)}, ε_j/ε_i ≤ C_run(1 + |j − i|^{1/2}) (SA L17257, L17624). The radius table is r_ι(σ; m) = α_ι ε_m with fixed α_0 ≤ α_1 [design].

---

## 8. Theorem A: the actual real background lies in every earlier domain (ST-cov at real points)

**Theorem A.** [port of Y3 Propositions II-90-39 (L53024) and II-90-62 (L53427), Corollary II-99-39 (L53529)] Fix a history and a structure σ of level t whose determining sequence is separated. Let U be a real configuration, critical over its own determining averages, with regularity radius r_U(𝔢) < Cε_{λ(𝔢)} at each regularity element (λ(𝔢) its highest layer index). Assume the radius floor

  (FLOOR) C_mb C ≤ ½(1 − 2β_s)α_0 and C_mb C ε_n ≤ a_♭/2 (so that C_mb Cε_l ≤ ½(1 − 2β_s)r_0(τ; l) for the table r_0(τ; l) = α_0ε_l),

with C_mb = C_mb(L, 𝗈, 𝔐, M, B^{cg}) the constant of Y3 (II-90-7) recomputed with the four-dimensional gauge constants. Then for every σ′ ≼ σ and every region Y, the plain triple 𝐏_{Y|𝒮}(U) = (U|_{Bd(Y)}, 0, 𝐉), with 𝐉 = J(U) at complete stars and 0 at incomplete ones, lies in the half-radius domain Ũ^{1/2}_{σ′|σ}(Y).

*Proof.* (L1). Let x be a plaquette base point of radius index l = m_σ(x). A regularity element with a corner in Ω_l has highest layer λ ≥ l, and the four-dimensional running [import RUN] gives L^{−2(λ−l)}ε_λ ≤ C_run(1 + (λ − l)^{1/2})L^{−2(λ−l)}ε_l ≤ C_run ε_l (in place of Y3 (II-90-41), whose three-dimensional form has the factor κ_run L^{−3(λ−l)/2}; the four-dimensional loss is only polynomial in λ − l and is beaten by L^{−2(λ−l)}). So |∂U(p) − 1| < C_runCε_lL^{−2l}·η_0² in finest units, and similarly η^3|J(U)| < C_runCε_lL^{−3l}. With (FLOOR) and c_σ ≥ 1 − 2β_s (Lemma 4.2), C_runCε_l ≤ C_mbCε_l ≤ ½c_σ(l)r_0(σ; l). The lift λ_σ ≥ 1 only enlarges the right side. A′ = 0 gives the two potential entries. At an incomplete star 𝐉 = 0.

(L2). For a cube q ⊂ Ω_l of side s ≤ 𝗈LM in level-l units, the curvature on its enlargement (which lies in layer ≥ l − 1 by separation) is below w L²η_l² with w = C_runCε_{l−1}; the matrix-divergence bound |D_U^T∂U| < 2L³wη_l² (Y3 L53106-53112, which uses only the definition of the current and Lη_i ≤ 1, valid in any dimension) and the regular cube gauge [import CORE: the four-dimensional regular gauge on cubes, `ur-gauge.md`, which is the analogue of Y3 I-28-75] give U^v = e^{iη_lA} with |A|, |∇A| < 4L³B_*(s + 2)C_runCε_{l−1} ≤ 𝗈LMB^{cg}C_mbCε_l·(C_run²) on q. Absorb C_run² into C_mb. With (FLOOR) this is below half of 𝗈LMB^{cg}λ_σr_0(σ″; l).

(L3). At a tower address the meet sequence is separated and subordinate (Lemma 6.1). Restriction of U to Z_𝒮 has a datum V′ = M_{𝐁′}(U′) with tested holonomies ≤ 2L²e, e = C_runCε_{n′}: the local four-corner averaging induction (Y3 L53171-53184; [import AV] in four dimensions) bounds each averaged holonomy at level q by 2(L²e)L^{2(q−l)} ≤ 2L^{−2}c₂^{SO} < ω_M. So V′ ∈ ℛ_{𝐁′}, and by the restriction identity of [import BG] the restricted configuration is a real gauge transform of the canonical tower: U_q^𝔯 = (U|_{Z})^{g}. Real gauge invariance of curvature and current then gives, at settled elements with ℓ = min{m_{σ″}(x), i}, |∂U_q^𝔯 − 1| < C_runCε_ℓL^{−2ℓ} and η_q^3|J_q^𝔯| < C_runCε_ℓL^{−3ℓ} ≤ C_runCε_ℓL^{−2ℓ−min(q,ℓ)}. With L^{i−p} ≥ 1 and (FLOOR) these are within half the radii of (L3). The analytic averages used in T_𝐁′ agree with the real ones at U (Y3 L53186-53212: at each intermediate level the averaged curvature is below ω_M, so the one-step analytic mean is defined and equals the real mean), so the complex tower at 𝐔 = U is this real tower; the logarithmic perturbation is zero, inside the tube (intrinsic-dom (5)) with distance δ.

(L4). For a core address X′ ⊂ Λ_i all current stars are complete, and ρ^{s′→i}_{X′}𝐏 = 𝐏^{(i)}_{X′}; Y3 Proposition II-90-39's core membership (II-90-48) with b₀, c₀ ≥ C_mbCε_i applies, its proof using exactly the bounds above; (FLOOR) gives half radii. □

**Corollary A′ (the real point of a step).** [port of Y3 Corollary II-99-39] On the support of a history step (main step or preparatory stage), with V the selected bare field and U the completed collared background, the real point 𝔲_Y = (𝐏_{Y|𝒮⁺}(U), 𝒜|_{𝔛°⟨Y⟩}, 𝔮|_Y) lies in Ũ^{1/2}_{(t,mid)}(Y) × 𝖡𝗑(Y; 1/2) × (stored tiers). *Proof.* The passed tests give tested holonomies < 2ε_j ([import FL], real part), so [import BG] gives the background with layer bounds, and Theorem A applies; the fluctuation box is the passed fluctuation test; stored variables are in their tiers by their own formation; restriction deletes coordinates. □

**Where four dimensions enter.** Only through [import RUN] (polynomial, not L^{ν/2}, growth) and the four-dimensional gauge and averaging constants. The proof needs separation of the determining sequence of σ. At preparatory stages above k_♯ this fails (Section 18).

---

## 9. Theorem B: towers on the complex domain, in the ambient scale, with tube room (ST-cov at complex points)

**Theorem B.** [port of Y3 Proposition I-95-61 (L55600) and Corollary I-95-81 (L55869)] Fix an ambient separated sequence Ω^♭ (the determining sequence of σ) and a subordinate separated meet sequence Ω′ of depth p ≤ i. Let ε_U(e) = η^{−2}l(x_e)²|∂U(e) − 1| and 𝗇_b(w) = max{l(x_b)|w(b)|, l(x_b)²|∇_Uw|(b)} with l the ambient scale, and let 𝒬^T(a) be the set of (U, w) with ε_U, 𝗇(w) < a. There are a_T, K_a, K_T, δ_T = δ/4 > 0, independent of depth, volume and number of layers, such that on 𝒬^T(a_T):

(i) the tower U^tw(U, w) = T_{𝐁′}(M_{𝐁′}(e^{iηw}U)) exists, is holomorphic in w for fixed U, and its datum lies in the intrinsic tube 𝒯_{𝐁′} with dist_∞(M_{𝐁′}(e^{iηw}U), 𝒯^c_{𝐁′}) ≥ η_* := δ/8;
(ii) at settled elements, G(U, w; e) = L^{2n}(∂U^tw(e) − I) (plaquettes) or L^{2n+n′}η³J(U^tw)(e) (full bonds), n = λ^♭(x_e), obeys |G| ≤ K_a{E_U^{δ_T}(x_e) + E_w^{δ_T}(x_e)} ≤ 1 and |G(U, w₁; e) − G(U, w₀; e)| ≤ K_T E_{w₁−w₀}^{δ_T}(x_e), with E^δ the exponentially weighted maxima of Y3 L55488-55492;
(iii) at real w the tower is the real axial representative of its actual averaged datum, and the construction is covariant under real gauges and conjugation.

*Proof.* (i) Existence and tube room. By [import AV] the real datum V₀ = M_{𝐁′}(U) is c^♮a_T-regular, c^♮ = 2L²: each tested plaquette of order q averages bare plaquettes in Ω′_{q−1} whose curvature in tower units is ≤ L²ς^{−2}ε_U < a_T^{(ia)} (ς ≥ 1, subordinate). With c^♮a_T ≤ ε_T ≤ ε̄/2, V₀ ∈ ℛ_{𝐁′} with margin. The complex average of e^{iηw}U is e^{iβ}V₀ with |β_q(c)| ≤ 2ξ_q sup_{𝒫(q,c)}|w| ≤ 2L ς(x_b)^{−1}l(x_b)|w(b)| (Y3 (ambient-row-geometry), ξ_q ≤ Lξ′(x_b); [import AV]), so ‖β‖_∞ ≤ 2La_T. With 2La_T ≤ δ/2, `layered-a3.md` (8)-(9) give D = e^{iβ}V₀ in the small patch about V₀ and dist_∞(D, 𝒯^c) ≥ δ/8. I checked (9): ‖D′V₀^{−1} − 1‖ < δ/8 + δ/(2 − δ) < 3δ/4 and ‖Log(D′V₀^{−1})‖ < (3δ/4)/(1 − 3δ/4) < δ, using unitarity of V₀ and δ ≤ 1/40. So T_{𝐁′}(D) is defined (`intrinsic-dom.md` (6)) and holomorphic in w, as a composition of the holomorphic average and T_{𝐁′}.

(ii) Real profile. At w = 0, the profile estimate [import PROF] on the tower sequence and Lemma 6.3 give ς(x_e)²𝖾_{U₀}(e) ≤ C_R max_f e^{−δd′(x_e,x_f)/2}ε_U(f) (Y3 (I-95-45)): the square of the scale ratio costs ≤ L⁴e^{4(log L)d′/ρ}, and δρ ≥ 64 log L leaves decay δ/2. Complex part. The response of T_{𝐁′} to the datum, [import DR] for the fixed tower system, gives the Landau-difference bound N_b(𝓗(B₁) − 𝓗(B₀)) ≤ min{B^♯ sup|B₁ − B₀|, B₅e^{δd′(x,y_b)}Σ(B₁ − B₀; x)} (Y3 (ambient-Landau-difference)); the pillar gauge factor has |h − I| < 1/4 and condition number < 3/2 on |𝓗| < ρ_f (Y3 L55712-55727: the ascent factors along a pillar of level q have total exponent ≤ (κ₆ + 3)τ, by the two geometric sums Σ_{m<q}L^{m−q} ≤ 1/(L − 1)); the local curvature and current maps have Lipschitz constant 600 on N_loc < 1/300 by Lemma 5.1-type expansions (Y3 L55735-55748). Combining: |𝓕(B₁) − 𝓕(B₀)| ≤ [C_X + C_h|𝓕(B₀)|]Σ(B₁ − B₀; x_e) (Y3 (I-95-55)). Near/far split. Split w = χw + (1 − χ)w with χ a cutoff at distance l (Y3 L55790-55800). For the near part apply Lemma 5.4 with M₀ = 3ς²/2, r = r_w, z = χw: the factor ς² cancels against ‖χw‖′² ≤ (Lς^{−1}𝗇(χw))², giving |F(χw)| ≤ 7C_RE_U + (6C_R + 5L²/r_w)C_χ𝗇^{nr}(w) (Y3 (I-95-67)). For the far part, Lemma 6.4 gives ς ≤ 1 + D, and Lemma 6.3 gives ς/ς(x_b) ≤ L²e^{δD/32}; using (1 + D)e^{−δD/4} ≤ 4/δ the far change is bounded by [C_X + C_h|F|]C_far max_b e^{−δ_Td′(x,x_b)}l(x_b)|u(b)| (Y3 (I-95-68)). Adding and choosing ā, a_T as in Y3 (I-95-57) gives the size bound. The Lipschitz bound follows by splitting w₁ − w₀ = χv + (1 − χ)v and applying the one-variable Schwarz lemma (Lemma 5.3(a)) on the disc |z| ≤ 1 + E/n_v (Y3 L55850-55864). (iii) Uniqueness of the axial representative at real data and holomorphy. □

**Corollary B′ (localised towers).** [port of Y3 Corollary I-95-81] For the meet Ω′_q = Ω^♭_q ⊓ X_{[q]}, q ≤ p, both erosion rules, and an element e within 2ξ_p of X^{≀p}, the element is settled and G_{p,X}(U, A′₁; e) − G_{p,X}(U, A′₀; e) ≤ e^{3δ_T}K_T max_b e^{−δ_Td_{𝐁^♭}(y_e,y_b)} max{l_i|A′₁ − A′₀|(b), l_i²|∇_U(A′₁ − A′₀)|(b)}. *Proof.* Erosion to level q is ≤ 3M₁ξ_q under either rule (Y3 L55913-55917: 2ρΣ_{r<q}ξ_r ≤ M₁ξ_q and 2M₁Σ_{r≤q}ξ_r ≤ 3M₁ξ_q, geometric sums), while dist(X^{≀p}, X^c) ≥ 2Mξ_{p−1} and (2M/L − 2) > 3M₁ when M ≥ L⁴M₁; so ambient and localised memberships agree within 2ξ_p of X^{≀p}, which is settlement. Apply (ii); passing to the deeper ambient sequence only decreases the weighted distance; moving to pillar tops costs e^{3δ_T}. □

This is what replaces ⟦BG-lay⟧ = ⟦ST-cov⟧ on separated sequences: every tower that a domain clause reads exists, has tube room η_* = δ/8, and has the ambient-scale bounds, uniformly, on 𝒬^T(a_T); and Definition 4.5's (L1) puts the triple in 𝒬^T(a_T) once (1 + β_s)λ_σr_ι ≤ a_T [design, Section 16].

### 9.1 Lemma RC and the nonflat datum with identity next average

`layered-a3.md` (final round, §20) stops at Lemma RC, its (51): for every inherited record e, the real curvature in the record's *own* tower scale ξ_e, η^{−2}ξ_e(p′)²|∂U_{n,t}(p′) − 1|, is below ε_adm/(2C₀L²) on the carriers of e. Its §18 builds, by the exact commuting formula (45), a real nonflat field in one block whose next average is the identity, with small amplitude z; with the lower determining rows retained, its (47) then forces large curvature in the coarse target scale, while the coarse datum is flat. The note says this is not yet a counterexample on an actual stage source, because the embedding into a complete history and inherited roster is not verified.

**Decision for ST1.** [proved here] *Whether or not such a datum occurs on an actual stage source, it cannot violate the domain of Definition 4.5, and Lemma RC is not needed in our design.* The reasons, each from definitions already made:

1. *We never read a record in its own scale.* Clause (L3) reads every tower at ℓ = min{m_{σ″}(x), i}, and its tower is the meet with the current determining sequence (Section 4.4). By Lemma 6.1 the meet is subordinate to the current sequence, so its layer at x is at most m_σ(x), the current ambient layer. Lemma RC's quantity, curvature in a scale ξ_e that may exceed the ambient scale, appears nowhere in (L1)-(L4).
2. *Retained lower rows lower the ambient layer.* The layer of x in a determining sequence is the largest l with x ∈ Ω_l. If determining rows of level q are present near x (the "retained lower rows" of the mixed problem, CA-I L9844-9845, L9957-9962 as quoted in `layered-a3.md` §15), then x ∉ Ω_{q+1} of that sequence, so its layer there is ≤ q. In the meet, the layer is the minimum of the two. So the (47) configuration, whose curvature sits on level-q rows, is read at scale ≤ ξ_q, where its curvature is O(z) in those units, not O(L^{2(m−q)}z).
3. *The real factor in the tested region is critical.* In Definition 4.5 the real factor on Bd_𝒮(Y) is the completed background (Corollary A′; Y3 L53556-53564), critical over its own determining averages. For a critical field on a separated sequence [import PROF] bounds its ambient-scale curvature by the profile of its averaged datum. The (45) field is a bare field; if it were the real factor, criticality would fail unless its retained rows carry its curvature, which is case 2.
4. *Tube room needs no target-scale bound.* Theorem B(i) obtains the real datum's regularity from curvature in tower units, L²ς^{−2}ε_U with ς ≥ 1, i.e. from the ambient-scale bound, and the complex datum from [import AV]. `layered-a3.md` (48)-(50) gives a second route to the same tube room δ/8 from an admitted raw datum and a small return; either suffices.

So the datum is harmless here, and the design need not change the averaging or the stage domains for it. What the datum does show, and we keep: a coarse average can erase fine curvature, so no proof may infer target-scale regularity from a flat coarse datum. Theorem A never does: its (L3) step uses the ambient-scale bounds of the critical background and the restriction identity of [import BG], whose hypothesis (tested holonomies of the restricted datum ≤ 2L²e) is checked from those same ambient-scale bounds.

One caveat, honestly stated: point 3 uses separation of the current sequence (for [import PROF]). On the overlapping outer shells this is Lemma OS again.


---

## 10. Theorem C: the regional shift

**Definition 10.1.** [design, Y3 (II-92-29) at L53728] At a stage with source bonds 𝔛 (the nonpivot fluctuation bonds touching the stage's new region: Ω_{k+1} at a main step, R_n at a preparatory stage), let 𝒜 be the fluctuation on 𝔛, completed at the pivots by the pivot formula (the free-coordinate chart of SA L8289-8296, `shift-map.md` (32)), and extended by zero to the other rows of the old determining set 𝐁 (the sequence before the stage, Lemma 6.5). Call this B′_Y. For a triple P at the stage level with pair 𝐩(P), the regional shift is 𝔥_Y(s; P, 𝒜) = (𝐀, 𝐊) = (𝐇, j)(s; 𝐩(P); B′_Y)|_{Bd(Y)}, the decoupled response of [import DR] on the old system, restricted to Y and extended by zero off the inner bonds.

**Theorem C.** [port of Y3 Proposition II-93-26 (L53737)] On 𝔻(Y) × dom_𝔥(Y), where dom_𝔥 requires sup|𝒜| < ε_𝔥, the pair in the natural local class at radius a_m, and source-cube restrictions in the simple domain at radius a_𝔥 (Y3 L53681-53698), the shift is defined, depends on P only through its pair, is holomorphic on fixed-real-factor fibres, Borel overall, hereditary under restriction, covariant under unitary gauges and conjugation, vanishes at s = 0 or 𝒜 = 0 and on wall components without a source cube, and obeys at every bond or stencil based at x of layer n

  ξ_n|𝐀|, ξ_n²|∇^{η}_𝐔𝐀|, ξ_n³|𝐊| ≤ 𝖼_𝔥 sup_{b∈𝔛} e^{−μ_𝔥 d_𝐁(x, b_−)}|𝒜(b)|,  𝖼_𝔥 = Ce^{Cκ̄}, μ_𝔥 = δ₀/8.  (C1)

*Proof.* Pivot completion: |β_c| ≤ 2C_P max_{𝔛⁺∩𝖯_c}|𝒜| (Y3 (II-93-28)), so sup|B′_Y| ≤ 2C_P sup|𝒜| ≤ 2C_Pε_𝔥 admits the source to [import DR] (reserve (history-shift-reserves), Y3 L53661-53676, all of which are term-by-term consequences of the choice of C ≥ C_min, Y3 (II-92-23)). Holomorphy: at fixed U the domain conditions are finitely many strict continuous inequalities, and the pivot formula followed by [import DR] is holomorphic. Borel: the witness conditions are compact images under strict-bound exhaustion (Y3 L53818-53826). Bound (C1): [import DR]'s weighted bound with w = e^{μd} at the pillar top y(x), d(x, y(x)) ≤ 3/2, and pivot rows within weighted distance 2L − 1 of a nonpivot bond attaining the pivot maximum, give (C1) with 𝖼_𝔥 ≥ 2C_Pe^{L/4}C_be^{C_bκ̄} (Y3 L53837-53858). Support and vanishing: the component response depends only on its own pair and source (Y3 L53866-53873). □

**Four-dimensional change.** None in the proof; the inputs are four-dimensional ([import DR], the four-dimensional pivot chart SA L8289-8296). The old system 𝐁 must be separated for [import DR]: at a preparatory stage with j ≤ k_♯ it is (Section 4.1); above k_♯ see Section 18.

---

## 11. Theorem D: identification on the physical locus (replaces Lemma M)

**Lemma D.1 (currents at incomplete stencils).** [port of Y3 Lemma II-93-23 (L54449)] Two admissible pairs with the same field and currents differing by δ supported on bonds not touching the stage region have the same response 𝐇, and current increments differing by f_𝐇^{−1}δ − δ; at a real critical first pair and a datum supported on 𝔛₀ the increments are equal. *Proof.* On the bare rows Γ₀⁺ (no endpoint in the stage region) the averaging is linear, 𝒬(A) = ξA, so the nonlinear averaging remainder and its derivatives vanish, the site field v = 𝖵A vanishes there, and every quadratic form term containing δ is zero; hence G, S, H, G₁, H₁, 𝔊 are unchanged; the only explicit current term in 𝖶(A′) changes by −𝖢′^T_𝓛Ψ_𝓛ζ + 𝖢″[A′]^Tζ = 0 with ζ = H^Tδ; both contractions have the same iterates. The current formula gives the difference. At criticality 𝒬(𝐇) = B′, which vanishes on Γ₀⁺, so 𝐇 = 0 there and f_𝐇 = 1 on supp δ (Y3 L54468-54527, read line by line; the algebra uses only the block structure of the response equations, which is the same in four dimensions). □

**Theorem D (identification).** [port of Y3 Proposition II-93-38 (L54530)] Let U₊ be in the regular critical orbit of its datum for the new sequence (after the stage), axial on the source pillars, P₊ its plain triple, and (P₊, 𝒜) ∈ dom_𝔥 real. Put (𝐀, 𝐊) = 𝔥(𝟏; P₊, 𝒜) and E = e^{iη𝐀}U₊. Let 𝖽 be the old (pre-stage) determining datum equal to e^{iB′}M_𝐁(U₊) on 𝔛₀ and to M_𝐁(U₊) elsewhere. If the regular critical orbit of (𝐁, 𝖽) exists, then E is a gauge transform of an element of it, J(E) = (current scaling)J(U₊) + 𝐊 at complete stencils, 𝐀 = 0 on bonds not touching the stage region, and 𝐊 = 0 at incomplete stencils.

*Proof.* (1) The old datum is finer on the changed rows (Lemma 6.5: Γ_j^+ ⊂ Γ_j^−, Γ_{j+1}^− ⊂ Γ_{j+1}^+, and the level-(j+1) averages are averages of level-j averages), so fixing 𝖽 imposes every constraint of the new datum. Hence U₊, critical for the new constraints with its own data, is critical for (𝐁, M_𝐁(U₊)) with zero multipliers on the added constraints. (2) Its reduced current equals the full current at complete stencils; at an incomplete stencil at most three plaquettes remain, each with curvature < a_m, so |J°(U₊)| < 3a_mξ₀^{−3} and (U₊, J°(U₊)) is in the natural class at radius 3a_m ≤ a_D. Lemma D.1 identifies its response with (𝐀, 𝐊). (3) The row source vanishes off interior rows, so the twisted datum of the response is B′ itself. [import CRIT] makes E critical with datum (e^{iB′}M_𝐁(U₊))^v; with g = v^{−1} at nodes and 1 elsewhere, E^g is critical with datum 𝖽, and the current identity of [import CRIT] gives the current. (4) Regularity, checked directly: with β_* = sup|B′| and ρ = 5b_De^{8κ̄}β_*, the response bounds give ξ_n|𝐀|, ξ_n²|∇𝐀| ≤ ρ and ξ_n³|𝐊| ≤ 10C_jb_D³e^{24κ̄}β_*; separation gives n ≥ j − 1 for the largest level touched; the plaquette variation estimate (Lemma 5.2(c)) bounds the new curvature by (3a_m + 2(1 + ρ_*)ρ)η²ξ_n^{−2}; the last reserve puts curvature and current inside ε_v. So E^g is in the regular critical orbit, and by uniqueness of the orbit [import BG] it is the old background up to gauge. □

**Why this is enough, and why Lemma M is not needed.** [proved here] Let f be a carried term formed on the old sequence. The actual measure, on the support of the history, evaluates f at the plain triple of the old background U_old, at real fields, s = 𝟏, with the physical current. By Theorem D, U_old = E^g up to the residual gauge, with pair (E, J(E)) = (e^{iη𝐀}U₊, J(U₊)-scaled + 𝐊). The substituted triple P₊ ∔ 𝔥 = (U₊, 𝐀, 𝐉₊ + 𝐊) has exactly this pair (A′ = 0 for a plain triple, so A″ = 𝐀). Since f is tied (depends on real triples only through the pair) and gauge invariant jointly with its stored coordinates (Section 4.6), and the gauge g is removed by the pinned levelling (Section 14.2), f(P_old; 𝔮) = Φ[f](𝟏, 1; P₊, 𝒜, 𝔮). So the composition of 4.7 agrees with the actual read at every point of the integration domain. The integral of the presentation is therefore unchanged by replacing the actual read with the composition, whatever happens off the physical locus. The composition is one holomorphic extension; others exist (the c(s − 1)ℓ(Δ) example of `shift-map.md` §4 and the c{J − J(U)} example of its §18 show this), but no consumer needs uniqueness: B4 and (LOC) need holomorphy and bounds of the function actually carried, and the carried function is, by design, the composition.

**What remains of Lemma M and of Lemma R.** Lemma M (chain_out §13) asks for the "fixed-read normal form" of "the actual stage substitution" at every complex parameter. In our design the actual stage substitution off the locus *is* the composition, so the normal form holds by definition, with (19), (23), (26) replaced by the single response formula of Definition 10.1. Lemma R (`shift-map.md` final round, §18, its (67)) asks for a bound on the velocity of "the actual returned pair" of each earlier read τ along a stage path, "expressed in its recorded frame", with covariant return differences. Our design has no such velocity: an earlier term is evaluated at the *current* triple restricted to its region (which Theorem A and Theorem E place in every earlier structure's domain directly, since Ũ_{σ|σ} carries the clauses of every σ″ ≼ σ), plus one shift, not at a transported earlier argument; there is no reference datum κ_t⁰ that moves. The return is the pinned levelling of the shift (Section 14.2), whose covariant first differences are bounded by the shift's own local size by construction. This is a fourth attack on Lemma R (after the gauge cocycle, local balls with contraction, and one physical restriction problem); Section 14.2 records why it succeeds where (67b) shows the pointwise shortcut fails.

---

## 12. Theorem E: the substitution margin (ST-map inclusion and ST-phase)

Fix a stage at level t with source region at the top layer, gap function d(m) of Lemma 5.6 and profile w(m) = ½d_min(m)r_0(m) of Lemma 5.7. For a shift 𝔥 = (𝐀, 𝐊) on a level-j region X and a positive profile v, put (Y3 (II-88-15), with the real transport of Lemma 5.2)

  ‖𝔥‖_{v} = max_{b∈Bd_𝒮(X)} max{L^{n(b)}η_j|𝐀(b)|, L^{2n(b)}η_j²|∇_U𝐀|(b), L^{3n(b)}η_j³|𝐊(b)|}/v(b),  v(b) = w(n(b_−)),

n(b) the current layer of b_−.

**Theorem E.** [port of Y3 Proposition II-88-43 (L56023) and Corollary II-88-50 (L56230)] Assume the separated case, the hypotheses of Theorem B and Corollary B′, (1 + β_s)λ_σr_ι ≤ â ≤ min{a_T, 1/(64L²)}, M ≥ L⁴M₁, δ_Tρ ≥ log 4 + 16 log L, and [import CORE]. Let σ′ ≼ σ* ≼ (previous structure), σ^m the structure after the stage, P ∈ Ũ_{σ′|σ^m}(X), and r = ‖𝔥‖_v ≤ r_* with

  r_* = [4C₅′ · e^{6δ_T}K_T · 4C_run · C_os K^♯(1 + 𝖼_♮)L³]^{−1}.

Then the substitution is defined on Bd_𝒮(X), and if defined on Bd(X), P ∔ 𝔥 ∈ Ũ_{σ′|σ*}(X).

(i) This holds for a main step with d_min = (1 − θ_s)β_s2^{−(t−m)}, and (ii) for a preparatory stage with d_min = θ_sβ_s2^{−(t−m)}/(2𝖭_t), in particular for reads with no new mark.

*Proof.* *Gap.* For n ≤ level(σ*), Lemma 5.6 gives [c_{σ*}(n) − c_{σ^m}(n)]λr_ι(n) ≥ d_min(n)r_0(n) = 2w(n) (lifts ≥ 1). At a point whose current layer exceeds level(σ*), n = t* + ν, the smaller-scale right side is ≤ (5/4)C_run(1 + √ν)2^{−ν}L^{−(p−1)ν}r_ι(t*)L^{−pt*} and the other ≥ r_ι(t*)L^{−pt*}, so the difference is ≥ (3/8)r_ι(t*)L^{−pt*} ≥ 2w(t*)L^{−pt*} for L ≥ 8C_run (as in Y3 L55989-56000, with the four-dimensional running). *Logarithm.* With â ≤ 1/(64L²) and r ≤ 1, η|𝐀| ≤ â/16 ≤ 1/16 on Bd_𝒮(X), so Lemmas 5.1-5.2 apply. *(L1).* By Lemma 5.2 and Lemma 5.7(b) (which transfers the profile bound at index n_k to every truncated index n_i ≤ n_k), the potential, difference, current and curvature increments are ≤ C₅′rw(n) in the local units of each clause; C₅′r ≤ 1/4 < 2. The gap absorbs them. Real curvature is unchanged because U is. *(L2).* Unchanged: U is unchanged. *(L3).* At a tower address the meet determining set is the localisation of Corollary B′. The pairs (U, A′), (U, A″), (U, 0) lie in 𝒬^T(a_T) by (L1) and the increments. Corollary B′ bounds the tower change by e^{3δ_T}K_T max_b e^{−δ_Td(y_f,y_b)}·C₅′rw(n_i(b)). If n_i(b) > n̄ = n_i(x_f), Lemma 6.2 gives d ≥ ρ(n_i(b) − n̄ − 1) − 3; Lemma 5.7(c) with ω = δ_Tρ gives e^{−δ_Td}w(n_i(b)) ≤ e^{3δ_T}4C_run w(n̄); if n_i(b) ≤ n̄, Lemma 5.7(a)-(b) gives w(n_i(b)) ≤ C_run w(n̄) ≤ 4C_run w(n̄), since w(n − ν)/w(n) = 2^{−ν}r_0(n − ν)/r_0(n) ≤ C_run by [import RUN]. So the tower increment is ≤ e^{6δ_T}K_T4C_runC₅′r w(n̄) ≤ w(n̄)/4 < 2w(n̄) by the choice of r_*. Real towers are unchanged. Existence of the complex tower at P ∔ 𝔥 is Theorem B(i). *(L4).* With τ = 1 − c_{σ^m}(i)/c_{σ*}(i), τb₀ ≥ 2w(i); an incident bond of X′ ⊂ Λ_i may start in layer i − 1, where Lemma 5.7(a) costs C_run/2 and restriction costs L, L², L³ for potential, difference, current; the choice of r_* puts these strictly inside [import CORE]'s radius 8w(i)/[5C_osK^♯(1 + 𝖼_♮)]. Restriction commutes with substitution because η_iL^{−(j−i)} = η_j. □

**Corollary E′ (the actual shift fits).** [proved here] On the support of a step, the regional shift of Theorem C, restricted to X, has ‖λ𝔥‖_v ≤ r_* for |λ| ≤ ϱ_X (Theorem F) provided the amplitude condition

  (AMP) 32 C_run 𝖼_𝔥 C_𝒜 (δ_src/ε_t) ≤ r_* d_*α_0,  d_* = (1 − θ_s)β_s (main step), θ_sβ_s/(2𝖭_t) (stage),

holds with μ_𝔥ρ ≥ log 4, where δ_src = δ_k (main step) or δ′_j (stage).

*Proof.* By (C1) and [import FL], at a bond based at x of layer n, the normalised shift is ≤ 𝖼_𝔥C_𝒜δ_src e^{−μ_𝔥d(x,𝔛)}. The source 𝔛 lies in layer ≥ t − 1, so d(x, 𝔛) ≥ ρ(t − n − 2)_+ by Lemma 6.2. Divide by w(n) = ½d_*2^{−(t−n)}α_0ε_n and use ε_n ≥ ε_t/(C_run(1 + √(t − n))) [import RUN]: the ratio is ≤ 2𝖼_𝔥C_𝒜(δ_src/ε_t)C_run(1 + √ν)2^ν e^{−μρ(ν−2)_+}/(d_*α_0) with ν = t − n. By Lemma 5.5, (1 + √ν)2^ν ≤ 4^ν, and 4^νe^{−μρ(ν−2)_+} ≤ 16(4e^{−μρ})^{(ν−2)_+} ≤ 16. So the ratio is ≤ 32C_run𝖼_𝔥C_𝒜(δ_src/ε_t)/(d_*α_0) ≤ r_* under (AMP). □

**Consequence for ST-phase.** At a preparatory stage δ′_j/ε_t ≤ C_run(1 + √𝖭_t)(A₁/A₀)(log x_j)^{−(𝔭₀−𝔭₁)} (SA L17624 and [import RUN], with |t − j| ≤ 𝖭_t and x_j ≥ x_t). So (AMP) holds for every read, with or without a new mark, if

  (N-growth) 𝖭_t^{3/2}(log x_t)^{−(𝔭₀−𝔭₁)} ≤ r_*θ_sβ_sα_0/(128C_run²𝖼_𝔥C_𝒜(A₁/A₀)),

which holds for all g_t ≤ γ, γ small, whenever 𝖭_t ≤ (log x_t)^{(𝔭₀−𝔭₁)/2}. This is a requirement on LF1's waiting depth Ř_t = 𝖭_t (SA L19410) [design]. At a main step (AMP) is a ceiling on A₁/A₀ alone, chosen after κ̄ (through 𝖼_𝔥) as in the order of Section 16.

The counterexample of `intrinsic-dom.md` (S(z) = z + 2d) is not contradicted: here the "map" is substitution of a shift whose size is proved to be below the margin.

---

## 13. Theorem F: re-expansion of a carried term (B4, LOC, majorants)

**Theorem F.** [port of Y3 Proposition II-104-17 (L56432)] Let f be a carried term formed at level j on X, bounded by b_f on its domain, tied and gauge invariant (Section 4.6). Let 𝖽_t(X) = M^{−1}d_𝐁(X, Ω_t) (distance to the stage's new region) and 𝖺 = δ_src/ε_t. Put ϱ_X = [H 𝖺 e^{−δ_sb𝖽_t(X)}]^{−1} with H = 32C_run𝖼_𝔥C_𝒜/(r_*d_*α_0)·e^{C_sbκ̄}·C_Σ and 0 < δ_sb ≤ μ_𝔥M/4. Then:

(i) for every P ∈ Ũ_{(t,mid)}(Y), sup|𝒜| < C_𝒜δ_src, s ∈ 𝔻(Y) and |λ| < ϱ_X, the substituted triple lies in the domain of f;
(ii) if ϱ_X > 1, the localised increment 𝕍[f](Y; 𝔲) = [Y ∖ X^↑ | X^↑]^*Φ_Y[f](·, 1; 𝔲) is analytic, and |𝕍[f](Y; 𝔲)| ≤ 2b_fϱ_X^{−1}e^{−(κ̄−1)#(Y∖X^↑)};
(iii) Σ_{Y⊃X^↑}𝕍[f](Y; 𝔲|_Y) = Φ_{T}[f](𝟏, 1; 𝔲) − f(ρ_X^{t→j}P; 𝔮_X).

*Proof.* (i) The shift is linear in λ. On Bd(X) the shift is the restriction of the regional shift, and its normalised size at layer n is bounded as in Corollary E′ but with the extra factor e^{−μ_𝔥 d(x,𝔛)} retained at the base points of X: since every base point of X is at weighted distance ≥ M𝖽_t(X) from 𝔛, write μ_𝔥d = (μ_𝔥/2)d + (μ_𝔥/2)d: the first half gives e^{−(μ_𝔥M/2)𝖽_t(X)} ≤ e^{−2δ_sb𝖽_t(X)} ≤ e^{−δ_sb𝖽_t(X)} (as δ_sb ≤ μ_𝔥M/4), and the second half gives the summation of Corollary E′ with rate μ_𝔥/2, which needs μ_𝔥ρ ≥ 2 log 4 (added to Section 16). Hence ‖λ𝔥‖_v ≤ |λ|ϱ_X^{−1}r_*, which is < r_* for |λ| < ϱ_X; Theorem E applies (with restriction from the mid-level space to the earlier output space preserving (L1)-(L4), as in Y3 L56245-56252). Off Bd_𝒮(X) the shift is zero and the ordinary substitution agrees with ∔_𝒮 on triples with η|A′| < log 2 (Y3 L56470-56478). (ii) λ ↦ Φ_Y[f](s, λ) − Φ_Y[f](s, 0) is holomorphic on |λ| < ϱ_X, bounded by 2b_f, and Φ_Y[f](s, 0) = f(ρP; 𝔮) is independent of s; Schwarz (Lemma 5.3(a)) gives |Φ(s, 1) − Φ(s, 0)| ≤ 2b_f/ϱ_X. The starred bracket subtracts the value at zero parameters, and the shift vanishes when the cubes of Y ∖ X^↑ carrying the source have s_c = 0 (Theorem C); Cauchy circles of radius e^{κ̄} − 1 ≥ e^{κ̄−1} in each decoupling variable of Y ∖ X^↑ (Lemma 5.3(c)) give the factor e^{−(κ̄−1)#(Y∖X^↑)}. (iii) The bracket is an inclusion-exclusion over subsets of cubes; summing over Y ⊃ X^↑ telescopes to the value at s = 𝟏 minus the value at s = 0 (Y3's bracket identity of II-18-108, a finite Möbius inversion), and at s = 0 the composition is f(ρP; 𝔮). □

**Consumer check.**

- *B4.* The new term is f(ρP; 𝔮) (unchanged, same majorant) plus Σ_Y 𝕍[f](Y), each holomorphic on the product box (part (i) covers every point of the box) with a bound independent of the number of labels, decaying in #(Y ∖ X^↑) at rate κ̄ − 1 and in the distance to the stage region. The polymer sum is NL1's (B1).
- *(LOC).* The amplitude λ is the interpolation parameter: the composition stays admitted for |λ| < ϱ_X, and ϱ_X > 1 whenever H𝖺 < 1. This is (AMP) strengthened by the fixed factor e^{C_sbκ̄}C_Σ: at a main step still a ceiling on A₁/A₀ chosen after κ̄; at a stage still implied by (N-growth) for γ small, since 𝖺 = δ′_j/ε_t tends to zero as a power of log x_t. The inner and removed radii are the two radii of (L1) at kinds ι = 0, 1. The Boolean corner bound is Lemma 5.3(c).
- *Majorants.* The supremum of the re-expanded term over Ũ_{(t,mid)} is ≤ b_f + Σ_Y|𝕍| with the bound of (ii); the stored-field integral is unchanged because stored coordinates are fixed.
- *(R-cov).* The shift is covariant under unitary gauges (Theorem C), substitution commutes with real gauges, and the domains are invariant (Definition 4.5 is gauge invariant clause by clause). So covariance of f passes to Φ_Y[f] and 𝕍[f]. Defect 1 of `gates/kept-cov-check.md` (kept forms carried as A^rel pair functions) is respected: kept forms are carried terms (Section 4.6), which are pair functions.

---

## 14. Witnesses, returns and stored slots (ST-wit)

### 14.1 Witnesses

[proved here] Substitution does not change the real factor U (Definition 4.3). The witnesses (L2) are statements about U alone. So every witness that holds before a stage holds after it, on the same cubes, with the same bounds; no new witness and no restriction argument is needed. When a cube family changes because the label changes (a new structure has new cubes), Theorem A supplies the witness at the actual real background (its (L2) part).

### 14.2 Returns: pinned levelling, and a fourth attack on Lemma R

[import LEV: Y3 Proposition II-85-34 at L54729-54787; statement read in full, proof (L54788-55124) not reread here] For a triple in the regular class 𝔗_k(Y; c_rt) of Y3 (eq:levelling-regular-triple) and an admitted shift 𝔥, there is a site gauge u = u^δ_Y[P; 𝐀], equal to 1 off the endpoints of Bd(Y), with u(y)v^♯_q(y) = 1 at levelled tops (it removes the accumulated endpoint factors of the response), |u^{±1}(x) − 1| ≤ C_mε_y(𝐀) on each pillar, cn(u) ≤ 3/2, preserving every stored transport at pinnable tops, and a levelled shift 𝔥^δ with e^{iξ𝐀^δ(b)}𝐔(b) = u(b_−)e^{iξ𝐀(b)}𝐔(b)u(b_+)^{−1}, current transformed by Ad u(b_−), and the local bound |𝔥^δ|_{𝐔,Y}(b) ≤ C_m‖𝔥‖^+_{y(b)}, where the local size includes ξ²|∇^𝐔𝐀^δ| (Y3 (II-79-5), (pinned-local-bound)). The construction is local, Borel, covariant, and holomorphic on fixed-real-factor fibres. Its prescribed values on a pillar come from the centred relative recursion with initial perturbation ξ𝐀, and are extended to turning cells B^{q−1}(a) by "smooth turns on smaller cells" (Y3 L54630-54633). Four-dimensional status: the construction uses pillars, tops and cells of the block lattice and is dimension-free except for counting constants; it has not been rewritten for four dimensions.

With [import LEV], Theorem E and Theorem F hold for the pinned composition with r replaced by C_m r (Y3 uses the pinned case for boundary terms and formed exponents, L56301-56303).

**The fourth attack on Lemma R.** `shift-map.md` §18 attacks (67) by the gauge cocycle, by native local balls with scale contraction, and by one physical restriction problem, and its (67b) shows that a pointwise-small complex return r_t(x) = e^{tεs(x)T} with alternating s gives potential velocity 2ε/η and first difference 4ε/η², so pointwise return bounds do not control (L1). The fourth attack is to change which return is used: the return is not a prescribed node gauge transported along an earlier path, but the levelling gauge u of the shift itself. Its differences are controlled by construction: u is built from the accumulated factors v^♯_q[𝐔; 𝐀] of the shift on each pillar, which by (C1) are within C_mε_y(𝐀) of 1 with ε_y(𝐀) ≤ L‖𝔥‖ in the local scale of the top, and is interpolated across turning cells of order o(a) by smooth turns, so its first differences are O(‖𝔥‖/ξ_{o(a)}), not O(‖𝔥‖/η). The levelled shift's own local size, including the covariant difference, is ≤ C_m‖𝔥‖^+ (pinned-local-bound), and the profile is preserved up to e^{C_mδ} (pinned-profile-bound). So the quantity that (67) must bound, the returned pair's velocity in the old ambient norm with its covariant difference, is in our design the levelled shift 𝔥^δ, bounded by C_m times the shift, and the shift is bounded by (C1). The example (67b) is not of this form: its gauge is not the levelling of any shift. What (67) additionally asks, the velocity of earlier references κ_t⁰ along a path, has no counterpart (Section 11). This attack succeeds as an implication from [import DR] and [import LEV]; it does not prove (67) for the outline's prescribed returns, which we no longer use.

### 14.3 Stored slots

[proved here] Stored coordinates are not changed by any stage (Definition 4.7). Hence: near slots stay real (no complex conjugation acts on them, so the non-Hermitian example of `stage-resp.md` §5 does not arise); their Borel dependence and the two switch zero identities (SA L6169-6170) are those of formation; far slots keep their analytic radius λ^{st} times their real range, which is formation data. The only requirement is that the carried term be invariant under real gauges acting jointly on triple and stored coordinates (Section 4.6), which is SA L6158 ("They transform by Ad u(b_−)") for real u. The complex levelling gauge u of 14.2 acts on the pair only; at real data u is unitary (it is built from real averages), so on the physical locus it acts on stored slots, if at all, by a unitary Ad, preserving Hermiticity. Off the physical locus the stored slots are not transformed: this is a definition of the composition, consistent with Section 11.

---

## 15. Drop-outs (ST-drop)

[proved here, from Lemma 6.5, (R21) and Theorems E, F] A drop-out C at level t fails after n(C) ≤ 𝖭_t stages and keeps them (SA L6088). Its terms are carried terms whose domain is the graded domain of the structure with ν(C) = n(C) in (R21), i.e. on the determining sequence, which "governs backgrounds" (SA L6106). Three facts close ST-drop in the separated case.

1. *No layer decreases.* By Lemma 6.5 every kept stage enlarges one member; the remade regions C ∖ Z″_l(C) contain Ω_l° ∩ C. So the drop-out's earlier structures are subordinate to its determining sequence, and the meet towers of its earlier terms are subordinate. No reversed loss arises.
2. *Later stages act by composition.* A later step or stage elsewhere carries a drop-out term by Theorem F with 𝖽_t(X) the distance from the term to the later stage region. The real factor, witnesses and stored stages of C are not changed (Sections 14.1, 14.3). The marks of C enter c_σ through −β_RΣ_{l∈Re}2^{−|m−l|}, which is part of the table and only makes the gaps of later stages larger when new marks appear (Lemma 5.6(ii)).
3. *Mass unchanged.* By Theorem F(iii), after each later stage the old term appears unchanged, f(ρP; 𝔮), and the change is a sum of new localised increments, each with its own small factor 2b_fϱ_X^{−1}e^{−(κ̄−1)#}. So the mass of the original drop-out term is carried exactly; the increments are new polymers whose sum is LF1's and NL1's bookkeeping, as for every other carried term. This is route (c) of `d4-route.md` in the form "carried with unchanged mass".

`dropout-bt.md`'s first open input asked for admission of "the actual collar read into each formation-stage hereditary domain ... including their old (R5) continuations". In our design there are no (R5) continuations, and the collar read is the composition, admitted by Theorem F(i). Its concern that SA L17564 ("both written in the new variables") forbids independent saved arguments is met: the drop-out's saved stages are stored coordinates, and its reads are written in the new variables by the composition.

The drop-out's stages are preparatory stages of the R operation. Above k_♯ their sequences are not separated. This is Lemma OS again.

---

## 16. Constants and their order

All constants below are inserted into the master order of `ym4-assembly.md` §3; none is chosen against a later one.

| Constant | Condition | Chosen after |
|---|---|---|
| L | L ≥ 8C_run, L ≥ 5 (L_♭ < L/2) | the flat package |
| c_R | β_R = c_Rβ_s, c_R ≤ (1 − θ_s)/16 (Lemma 4.2) | β_s, θ_s |
| δ, η_* | δ ≤ min{1/40, r_B/40}, η_* = δ/8 | r_B (`intrinsic-dom.md` (5)) |
| a_T, K_a, K_T, δ_T | Y3 (I-95-39)-(I-95-57) with four-dimensional analytic constants; δ_T = δ_prof/4 | L, 𝔐, BG/PR constants |
| ρ = R₁𝔐, M | δ_Tρ ≥ log 4 + 16 log L, μ_𝔥ρ ≥ 2 log 4, δρ ≥ 64 log L; M ≥ L⁴M₁, M ≥ 88𝗋_w𝔐 | δ_T, μ_𝔥 |
| 𝖼_𝔥, ε_𝔥, a_𝔥 | Y3 (II-92-25) | κ̄ |
| C_mb, (FLOOR) | C_mbC ≤ ½(1 − 2β_s)α₀; C_mbCε ≤ a_♭/2 | M, gauge constants |
| α₀ ≤ α₁ | (1 + β_s)L_♭^{2e}α_ιε_m ≤ â ≤ min{a_T, (64L²)^{−1}}; with e ≤ log_LŘ this is a ceiling on γ under (N-growth) | a_T |
| r_* | Theorem E | K_T, C_os, K^♯ |
| A₁/A₀ | (AMP) at a main step: 32C_run𝖼_𝔥C_𝒜(A₁/A₀) ≤ r_*(1 − θ_s)β_sα₀ | κ̄, r_*, α₀ |
| 𝖭_t = Ř_t | (N-growth): 𝖭_t ≤ (log x_t)^{(𝔭₀−𝔭₁)/2} | 𝔭₀, 𝔭₁ (first in the order) |
| γ | (N-growth) inequality at x_t ≥ γ^{−2}; lifts times ε small | all of the above |

In (FLOOR), C is the regularity constant of the tests (the backgrounds have r_U < Cε).

The order is consistent with the master order: (A₁, A₀) come after κ̄ and after the analytic constants, as in SA L19469-19470; 𝔭₀, 𝔭₁ are in the first group; γ is last. The only new cross-submanuscript constraint is (N-growth) on LF1.

---

## 17. Theorem ST1* and (D4)

**Theorem ST1*.** Fix L and the constants of Section 16, a finite admissible history whose determining sequences are separated at every structure (this includes every main step and every preparatory stage at stage levels ≤ k_♯), and assume the imports of Section 7. Then:

1. (Nesting) Lemma 4.6.
2. (Allowance) Lemma 5.6.
3. (Coverage) every triple of Ũ_σ has, at every tower address of every σ″ ≼ σ, its complex tower with datum at tube distance ≥ η_* = δ/8 and the ambient-scale bounds (Theorem B); the actual real background lies in Ũ^{1/2}_σ (Theorem A).
4. (Stage map) for every stage, the carried composition maps Ũ_{(t,mid)}(Y) × (fluctuation box) × 𝔻(Y) × {|λ| < ϱ_X} into the domain of every earlier carried term, with half the coefficient margin left (Theorems C, E, F), and equals the actual old read on the physical locus (Theorem D).
5. (No new mark) included in 4, under (N-growth) (Theorem E(ii)).
6. (Witnesses, returns, stored slots) Section 14, with [import LEV].
7. (Drop-outs) Section 15.

Consequently (D4) holds: by induction on the stages in the order ≼, every carried composition lies in its activity domain with an interpolation disc of radius ϱ_X > 1.

*Proof of the induction.* Order all stages of the history. Suppose that after stage n every carried term formed so far is a function on the domain of its formation, evaluated at ρP ∔ (accumulated shifts) with P in the current domain. At stage n + 1 the current real point lies in Ũ^{1/2}_{(t,mid)} by Corollary A′. Each carried term, already a function on Ũ_{(t',·)} of its own, is re-expanded by Theorem F with the new shift; Theorem E puts the argument in the earlier domain with half the stage's gap left, for every earlier structure at once (the clauses of all σ″ ≼ σ are part of Ũ_σ). The gaps used at distinct stages are distinct terms of the table, so no gap is spent twice; Lemma 4.2 keeps c ≥ 1/2. New terms formed at stage n + 1 are functions on Ũ_{(t,out)}, and the next stage treats them in the same way. The quantifiers: Theorems B, C, E, F hold uniformly in P, 𝒜, s, λ, the stored coordinates and switches, with constants independent of the history length, mesh and volume. □

What ST1* does not show: the construction of the activities on the new domains (NL1, LF1), their polymer sums, the mass bound LF-mass, positivity of kept forms, and the imports CRIT, LEV, CORE in four dimensions.

---

## 18. The outstanding lemma

### 18.1 Statement

**Lemma OS (overlapping outer shells).** [outstanding] Let the operation at level t have its 𝖭_t preparatory stages, and let j > k_♯ be a stage level with MŘ_{k_♯+1}L^{k_♯+1−k} = M (SA L17624). For the determining sequence of every structure at such a stage (whose collars overlap those of earlier stages), the conclusions of [import BG] (existence and uniqueness of the regular critical orbit for admitted data, holomorphic continuation on a radius r_B, restriction identity), [import PROF] (the profile bound) and [import DR] (the weighted decoupled response with exponential weights in the weighted path distance) hold, with constants independent of 𝖭_t, of the number of overlapping shells, of depth and of volume, and with a per-shell decay e^{−ω} in the weighted distance between shells that satisfies ω ≥ log 4 + 3 log L.

With Lemma OS, Theorems A-F hold at these stages with the same proofs, and Theorem ST1* holds without the separation restriction.

### 18.2 Three attacks

**Attack 1: separation-based decay (Lemma 6.2).** Every decay statement in Theorems A-F comes from Lemma 6.2: a path crossing from layer n to layer n + ν crosses ν − 1 strips of width ≥ ρξ, each of weighted length ≥ ρ. *Exact failure:* SA L17624 states that "the collars of the later stages overlap" for j > k_♯. Where collars of consecutive stages overlap there is no strip of width ρξ between the corresponding layers, so the lower bound d ≥ ρ(ν − 1) has no proof, and the per-layer factor e^{−μρ} in Corollary E′ and Theorem B(ii) is not available across those shells. The number of such shells is k − k_♯ − 1 = log_LŘ_k, which grows with 𝖭.

**Attack 2: count the overlapping shells and pay without decay.** Across the at most log_LŘ overlapping shells, give up decay and pay the count. For the *shift* this works numerically: Corollary E′ then loses at most a factor 4^{log_LŘ} = Ř^{log 4/log L} ≤ Ř^{1/2} (L ≥ 16), and (N-growth) with Ř = 𝖭 ≤ (log x)^{(𝔭₀−𝔭₁)/2} absorbs a polynomial in 𝖭 against (log x)^{−(𝔭₀−𝔭₁)} if the exponent is reduced (𝖭 ≤ (log x)^{(𝔭₀−𝔭₁)/3}). *Exact failure:* the payment applies to the size of the shift, not to the existence of the objects. [import BG] and [import DR] themselves are proved only on separated sequences: their right-inverse bounds for the constraint derivative rest on row and column counts "bounded at fixed L, independently of the number of layers" (SA L9987-9997, quoted in `shift-map.md:118`), which are counts per separated layer. On an overlapping shell up to log_LŘ row levels meet within distance < ρξ of one site, and I have no bound on the pivot right inverse, or on the multiplier contraction of SA L9832-9911, that is uniform in that number. Paying the count requires those bounds first.

**Attack 3: lifts (Balaban CMP 122, (1.24); SA L17624).** On shell i the test is relaxed by L_♭^{2(i−k_♯−1)_+}, and "In passing from the scale j+1 to the scale j one gains L^{−2} and pays L_♭^2. Hence the bound of each stage implies the bound of the preceding stage." *Exact failure:* this argument proves that the real curvature tests of successive stages imply one another, i.e. it supplies the *hypothesis* of [import BG] (small real curvature) on the outer shells. It does not supply the *conclusion* (existence, uniqueness, holomorphic radius, response decay) on a non-separated sequence, which is what Lemma OS asks. And where a lift is used to compare a coarser reading with a finer control, `layered-a3.md` (3) shows L^{2v}/L_♭^{2v} > 4^v, so lifts cannot be traded for decay.

### 18.3 What would close it, and a design alternative

Two routes remain open; neither is attempted to closure here.

- *A background theorem on sequences with bounded overlap.* Prove A1/A3 on sequences where at most N_ov row levels meet in any ρξ-neighbourhood, with constants polynomial in N_ov; then Attack 2 closes with (N-growth) strengthened to absorb that polynomial. SA L9789 states a layered conclusion "under wider gaps and small local profiles" (as quoted in `layered-a3.md:16`), which is the separated case only.
- *Redesign of the last stages.* Choose the stage geometry so that collars never overlap, for example by letting the collar widths of the last log_LŘ stages shrink with the stage so that consecutive collars keep a ρξ gap. This is an LF1 design question: it changes the R operation's geometry and its waiting and rarity bookkeeping (LF1(2), LF1(3)), which I have not examined.

### 18.4 Imports that are not yet rebuilt in four dimensions

These are not ST1 statements, but ST1* depends on them, and a referee should know: [import CRIT] (the response at criticality, SA L5800-5803, L10446-10458; [SS]); [import LEV] (pinned levelling, Y3 Proposition II-85-34, three-dimensional proof, dimension-free construction); the outer-core substitution lemma inside [import CORE] (Y3 Proposition II-16-69). Each is used exactly as stated in Section 7.

---

## 19. Status table

| Item | Status in this file |
|---|---|
| Lemmas 4.2, 4.6, 5.1-5.7, 6.1-6.5 | [proved here] |
| Theorem A, Corollary A′ (real admission) | [port], separated case |
| Theorem B, Corollary B′ (towers, tube room η_* = δ/8) | [port], separated case |
| Theorem C (regional shift) | [port], separated case, from [import DR] |
| Lemma D.1, Theorem D (identification on the physical locus) | [port], from [import CRIT], [import BG] |
| Section 11 (Lemma M not needed; Lemma R's object replaced) | [proved here] |
| Section 9.1 (Lemma RC not needed; the identity-average datum is harmless) | [proved here], separated case |
| Theorem E, Corollary E′ (substitution margin, ST-map, ST-phase) | [port] + [proved here] under (AMP), (N-growth) |
| Theorem F (re-expansion, LOC, B4, majorants) | [port] |
| Section 14 (witnesses, returns, stored slots) | [proved here], returns via [import LEV] |
| Section 15 (drop-outs) | [proved here], separated case |
| Theorem ST1*, (D4) | [proved here] from the above, separated case |
| Lemma OS (overlapping outer shells) | [outstanding]; three attacks in 18.2 |

No step rests on a computation. No counterexample to any stage, domain or inclusion is claimed. This text is not yet checked by the other model.
