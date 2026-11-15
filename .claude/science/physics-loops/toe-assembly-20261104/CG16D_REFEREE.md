lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CG16D referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort). It is pass 3, the referee, of part CG16D under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the owner freezes. This session wrote neither pass 1 (`CG16D_DRAFT.md`) nor pass 2 (`CG16D.md`). This is one check: one whole-part, line-by-line read. It reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no law, reading, specification or definition, and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. Only the owner adopts.

**Text read.** `CG16D.md` at commit `59d3886d9` (branch `claude/toe-assembly`; the last commit that touches it, equal to HEAD when read). SHA-256 `83453acb41bd4b713091b8065e6a7372513d6c95d946be99bbcbe25e908a3ffa`. Line numbers cited as "line n" or "(n)" refer to that file.

**Pass-1 source.** `CG16D_DRAFT.md`, last changed at `59af7f324`, unchanged at `59d3886d9`. SHA-256 `84705929a416f56147909a2874898fb82101bb9be210aebd431150a79fc06579`. Cited as `DRAFT:<n>`.

**References consulted.** Listed in section 0 below, with commits and line ranges.

**Owner guidance applied.** Verbatim: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws `L5-O[S_+]`, `L5-U` and the register D-reg are read plainly. No hostile reading of an axiom is used.

**Method.** Every proof step was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-CG16Dref/` (under a minute, under 1 GB, started only after `memory_pressure` showed at least 50 percent free). A check guides or refutes; it never proves. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step, with the repair where one is given). A "referee closure" is a short complete argument for a missing step, written to be Lean-formalizable.

## 0. Sources read

All files in this folder are read at `59d3886d9` (the checkout HEAD). The commit in brackets is the last commit that touches each file.

| File | Lines read | Use |
|---|---|---|
| `CG16D.md` [`59d3886d9`] | 1-123 (all) | the text refereed |
| `CG16D_DRAFT.md` [`59af7f324`] | 1-324 (all) | pass-1 source of every claim |
| `prior/CG16D.md` | 1-81 (all) | prior-work digest |
| `LW1_REFEREE.md` | 1-80 | format |
| `Y2W_DRAFT.md` | 1-30 | head format |
| `RCS1.md` [`8ca361b0c`] | 18-80 (definitions, Theorems 1-5, Lemma 5.1, Corollary 5.2), 159-170 (R2) | ported lemmas |
| `LZ1.md` [`7da1a4174`] | 24-50 (definitions, D1, band, node, "flat", Theorem 2.1 head) | definitions |
| `LW1_5.md` [`727ad9884`] | 52, 55-104 (the two laws, the cube gates), 128-202 (Q and G, U, S′, F and K, mixed registers, one-ended construction, Theorem SC, Corollary SC.1), 204, 206, 216, 262-276 (cell lifts) | laws and ported results |
| `GA1_5.md` [`913ef70a5`] | 5-13 (status), 236-272 (Lemma U, Proposition C) | NN-a compilation |
| `TOE_ASSEMBLY.md` [`913ef70a5`] | 231-235 (section 3.7, NN-a text) | NN-a conditions |
| `LW1_5O_DRAFT.md` [`c721a3507`] | grep hits at 39, 49, 64, 72, 90-127, 140, 151-165, 189, 205 | cited pass-1 lemmas K0, K5, E |
| `origin/docs/consolidate-gauge-matter-registers` [`7086189d1`], `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` | 979, 987, 1204 | the #10027 boundary and #10045 row quoted in `CG16D.md` §6 |

Not read: the audit ledger, other referee reports, `docs/MINIMAL_AXIOMS_2026-06-29.md` (unchanged and not needed).

**Working set used, by name.** PS-5 (five modes per site), PS-6r (finite link registers), PS-1c (cell covariance), the owner decision GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` section 3.7, quoted where used), and the two live laws `L5-O`, `L5-U` of `LW1_5.md` section 2. Nothing else.

**Inputs from outside the working set.** Standard mathematics, rebuilt where used: Schur's lemma; the spectral theorem for commuting finite-order unitaries; continuity of eigenvalues and Riesz projections for `C¹` Hermitian families; Newton's identities. Literature is not used.

## 1. Verdict table

**Counts.** 57 items: 52 CORRECT, 0 ERROR, 5 INCOMPLETE. No INCOMPLETE item changes the content of a theorem; each has a repair in section 2. Draft names map as follows: draft Lemma 0 = Theorem 1; Lemma 1 and Corollary 1.1 = Theorem 2; Lemma 2 = Theorem 3; Theorem A = Theorem 4; Lemma S = Theorem 5; Theorem B = Theorem 6; Example B.1 = Example 1; Proposition C = Theorem 7; Proposition D(a)-(e) = Theorem 8; Proposition D(f) = Theorem 9.

| # | Item (`CG16D.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved" list, first four sentences (7) | CORRECT | Each listed result is proved below, with the repairs of section 2. |
| 3 | §0 sentence "The flatness conclusion is directional at each node, not necessarily flatness on a neighbourhood." (7) | INCOMPLETE | True of the text as written. The hypotheses supply three axis labels on one decomposition, and referee closure N (§2.1) gives `V=1` on a `C¹` neighbourhood of every node: "flat" in the sense of `LZ1.md` §1. Replace the sentence (edit E1). |
| 4 | §0 GAP paragraph (9) | CORRECT | Three gaps. The NN-a gap is closed by referee closures C-NN and CV (§2.2, §2.3). The identification gap is R-CG1 and stays open. The N1-N8 packet is procedural (§3). |
| 5 | §0 open list (11) | CORRECT | |
| 6 | §0 provenance (13) | CORRECT | The referee read the draft at `59af7f324` (§0). |
| 7 | §1 preamble (17) | CORRECT | |
| 8 | Definition 1, GR and so(20) registers (19) | CORRECT | Matches `LW1_5O_DRAFT.md` line 49 and `LW1_5.md` line 87 ("Each link carries a finite nontrivial unitary representation R of Spin(20)"). |
| 9 | Definition 2, `z_x`, `ε`, `d_ℓ`, link-pure, `Φ_Λ` (20) | CORRECT | `ε_{ℓ,x}=ρ_{ℓ,x}(−1)` commutes with both end actions, so `Φ_Λ∈𝔄^G`. |
| 10 | Definition 3, the class `𝒰` (21) | CORRECT | |
| 11 | Definition 4, flux-sharp and `χ_sp` (22) | CORRECT | Last sentence is `LW1_5.md` line 154, S′ step 2. |
| 12 | Definition 5, D1, band, propagation, string-made (23) | CORRECT | `LZ1.md` §1 defines "flat" as "`V=1` on a neighbourhood"; see item 3. |
| 13 | Readings and four tests (25) | CORRECT | Records the draft's assessments. No objection. |
| 14 | Theorem 1 statement (29) | CORRECT | |
| 15 | Theorem 1 proof (31) | CORRECT | `RCS1.md` R2(a)'s proof uses only uniform boundedness of the net; it applies word for word. |
| 16 | Theorem 2 identity (33-36) | CORRECT | |
| 17 | Theorem 2 link-pure clause (37) | CORRECT | |
| 18 | Theorem 2 proof (39) | CORRECT | `M^{12}_x=n_{x,1}−1/2` (`LW1_5.md` line 169: "The site factors are respectively −1 and −iP_x"). |
| 19 | Theorem 3 and proof (41-43) | CORRECT | Also on file in frozen text: `LW1_5.md` line 169, "For an so(20) link the two ε's coincide." Cite it (edit E8). |
| 20 | Theorem 4 statement (45) | CORRECT | |
| 21 | Theorem 4 proof (47) | CORRECT | |
| 22 | Remark after Theorem 4 (49) | CORRECT | |
| 23 | §3 setup: `κ₀`, `u_x`, `Z_Λ=s_ΛΦ_Λ` (53) | INCOMPLETE | Two one-line reasons are missing; `DRAFT:162,166` has them (edit E3). |
| 24 | Theorem 5 statement (55) | CORRECT | |
| 25 | Theorem 5 proof: choice of `Λ₀`, bound `2δ` (57) | CORRECT | |
| 26 | Theorem 5 proof: character average, `‖(I−E_F)v‖²<2δ` (57) | CORRECT | |
| 27 | Theorem 5 proof: limits `Q_{Λ₀}` span `H` (57) | CORRECT | The `Q_{Λ₀}` increase with `Λ₀`; their limit `Q_∞` obeys `‖(I−Q_∞)v‖²≤2δ` for every `δ`. |
| 28 | Theorem 5 proof: even defects vanish; converse (57) | CORRECT | |
| 29 | Theorem 6(i) statement (61) | CORRECT | |
| 30 | Theorem 6(i) proof (67) | INCOMPLETE | Missing: `z_x` for `x∈Λ∖S` commutes with `B`. Repair in §2.5 (edit E4). The pairing is also in frozen `LW1_5.md` line 171 (F and K). |
| 31 | Theorem 6(ii) statement and proof (63, 69) | CORRECT | Closure N upgrades the conclusion to neighbourhood flatness. |
| 32 | Theorem 6(iii) statement and proof (65, 69) | CORRECT | It uses neither link-purity nor flux-sharpness. Closure N applies. |
| 33 | Line-defect remark (71) | CORRECT | With two transverse labels, closure N's argument gives `V=1` on the plane `K₀+span{e₂,e₃}` near `K₀` (§2.1). |
| 34 | Example 1 (73) | CORRECT | Restore `DRAFT:205`'s "every site in one fixed even matter vector" (edit E5). |
| 35 | `Z4` remark (75) | CORRECT | |
| 36 | Theorem 7 statement (79) | CORRECT | |
| 37 | Theorem 7 proof (81) | CORRECT | `𝒢^T_x` is the unshifted bilinear (`LW1_5.md` line 97), so `u↦Γ_x(u)` is a representation of `U(5)`. |
| 38 | Scope remark after Theorem 7 (83) | CORRECT | |
| 39 | D-reg register and `U^{ab}` (87) | CORRECT | `[L^{cd},Γ_b]=i(δ_{db}Γ_c−δ_{cb}Γ_d)` for `L^{cd}=(i/2)Γ_cΓ_d`, as `LW1_5.md` lines 130-134 need. |
| 40 | Theorem 8(i) (91) | CORRECT | |
| 41 | Theorem 8(ii) and proof (93, 99) | CORRECT | `[check]` agrees (§2.6). |
| 42 | Theorem 8(iii): Hermitian, commuting, gauge-invariant `LZ1.md` layer; `KΦ_Λ=−Φ_ΛK`; `Φ_Λ` not central (95, 99) | CORRECT | |
| 43 | Theorem 8(iii): "rotation-covariant" (95) | CORRECT | True for the lift that maps end factors by the identity map of `Q`. The composite update needs one extra site sign (§2.3). |
| 44 | Theorem 8(iv) and proof (97, 99) | CORRECT | `[check]` agrees. |
| 45 | GAP, NN-a compilation (101) | CORRECT | The gap is real in the draft. Closed by C-NN and CV (§2.2-2.3). Wording: "precisely in Theorem 2" should read "in the link-pure clause of Theorem 2" (edit E6). |
| 46 | Theorem 9: two singlets, one per matter parity (103, 105) | CORRECT | Rebuilt in §2.4. `[check]` agrees. |
| 47 | Theorem 9: the singlet span, `z_x=+1`, invariance under `h_y` and hops (103, 105) | INCOMPLETE | "closed product span" has no ambient Hilbert space. Every use is local; state it on finite regions (§2.4, edit E7). |
| 48 | Theorem 9: the columnar D1 state (103, 105) | INCOMPLETE | "a fixed eigenvector of each paired-link hop" admits parity-mixing choices: each eigenvalue has a two-dimensional eigenspace with one pair-even and one pair-odd vector (§2.4). The product construction needs even local factors. Fix: choose a pair-parity eigenvector (edit E7). |
| 49 | Theorem 9: string limit and `χ_sp=−1` (103, 105) | CORRECT | Density of local gauge-invariant elements on D-reg: §2.4. |
| 50 | Remarks and D-reg four tests (107) | CORRECT | |
| 51 | §6 prior work (111) | CORRECT | Quotes checked at `7086189d1` lines 979, 987, 1204. |
| 52 | §6 literature (113) | CORRECT | Not load-bearing. |
| 53 | §6 check record (115) | CORRECT | This referee's own `[check]` covers the same algebra (§2.6). |
| 54 | CG16D-NLP (119) | CORRECT (open) | |
| 55 | CG16D-SC (120) | CORRECT (open) | Add the remark of §2.7. |
| 56 | Unchanged open items (121) | CORRECT | |
| 57 | Downstream paragraph (123) | CORRECT | Add "and `V=1` near every node" after closure N (edit E1). |

## 2. Referee closures and notes

### 2.1 Closure N: flatness on a neighbourhood (items 3, 31-33, 57)

`RCS1.md` line 70, Lemma 5.1: "For any band and node `K₀`, `V(K₀+sn)=1` for small real `s`; hence `Σ_j n_jN_j=0`." Line 76, Theorem 5: "Every band is flat along `n` at each node and has no Clifford cone there." These are directional statements. `CG16D.md` Theorem 6(ii) applies Theorem 5 three times, with `n=e_1,e_2,e_3`, on one decomposition `H=⊕_κH_κ`. The three labels together give more.

**Lemma N (referee closure).** Let `(H,π,T,Ũ)` be a separable covariant representation with `H=⊕_{c∈C}H_c`, `ŨH_c=H_c`, `T_βH_c=H_{β·c}`, and real functions `q_1,q_2,q_3` on `C` with `q_j(β·c)=q_j(c)+β_j`. Let `(d,F,V)` be a band with node `K₀`. Let `B` be an open ball around `K₀`, of diameter less than `2π`, on which `V` is `C¹` and every eigenvalue of `V(K)` is `e^{−iθ}` with `|θ|<π/2`. Then `V(K)=1` for every `K∈B`.

*Proof.* Step 1 (boosted bands; the proofs of `RCS1.md` Theorem 5 and Lemma 5.1). Fix `j`. Put `B_t=Σ_c e^{itq_j(c)}Π_c`. It is unitary and commutes with `Ũ`, since each `Π_c` does. Since `T_β` maps `H_c` onto `H_{β·c}` and `q_j(β·c)−q_j(c)=β_j`, `B_tT_βB_t^{-1}=e^{itβ_j}T_β`. Put `(S_tψ)(K)=ψ(K−te_j)` and `G_t=B_tFS_t`. With `M_β` the multiplication by `e^{iK·β}` (`LZ1.md` §1), `M_βS_t=e^{itβ_j}S_tM_β` and `M_VS_t=S_tM_{V(·+te_j)}`. Hence `G_t` is an isometry with `T_βG_t=G_tM_β` and `ŨG_t=G_tM_{V(·+te_j)}`.

Step 2 (no variation along `e_j` anywhere in `B`). Put `h=i log V` on `B`. It is `C¹` and Hermitian, with spectrum in `(−π/2,π/2)`, and `V=e^{−ih}`. Suppose `∂_j tr(h^p)≠0` at some `K₁∈B`, for some `1≤p≤d`. By continuity it is nonzero on a ball `B₁∋K₁`. The number of distinct eigenvalues of `h` is lower semicontinuous, so it is constant on a smaller ball `B₂⊂B₁`. There the distinct eigenvalues `λ_1<…<λ_r` have constant multiplicities `m_i`, and they and their Riesz projections `P_i` are `C¹`. Since `tr(h^p)=Σ_im_iλ_i^p`, some `∂_jλ_i` is nonzero at a point of `B₂`. Choose a closed ball `B₃` and `t_*>0` with `B₃+[0,t_*]e_j⊂B₂` and `∂_jλ_i≠0` on that set. Then `t↦λ_i(K+te_j)` is strictly monotone on `[0,t_*]` for each `K∈B₃`. Let `X_t` be `G_t` restricted to `L²(B₃; ran P_i(·+te_j))`. It is a nonzero isometry with `T_βX_t=X_tM_β` and `ŨX_t=X_tM_{w_t}`, where `w_t(K)=e^{−iλ_i(K+te_j)}` is scalar. `RCS1.md` Lemma 5.1's proof gives, for such `X`, "`P(Γ)X=XM_{1_Γ(K,w(K))}` for every Borel `Γ`", with `P` the joint spectral measure of `(T_{e_1},T_{e_2},T_{e_3},Ũ)`. Take `Γ_t={(e^{iK_1},e^{iK_2},e^{iK_3},w_t(K)):K∈B₃}`, a compact set. Then `P(Γ_t)X_t=X_t`. For `t≠t′`, `Γ_t∩Γ_{t′}=∅`: equal first coordinates force the same `K` (diameter below `2π`), and then `λ_i(K+te_j)≠λ_i(K+t′e_j)`, both in `(−π/2,π/2)`. So the ranges of `X_t`, `t∈[0,t_*]`, are nonzero and pairwise orthogonal. Uncountably many such subspaces contradict separability. Hence `∂_j tr(h^p)=0` on all of `B`.

Step 3. Step 2 holds for `j=1,2,3`. So each `tr(h^p)`, `1≤p≤d`, is constant on the convex set `B` and equals `tr(h(K₀)^p)=0`. By Newton's identities the characteristic polynomial of `h(K)` is `λ^d`. A Hermitian matrix with only the eigenvalue `0` is `0`. So `h(K)=0` and `V(K)=1`. □

**Consequences.** (a) In Theorem 6(ii) and (iii), and in any covariant representation built from Example 1's sectors, every band is flat on a neighbourhood of each node in the sense of `LZ1.md` §1 ("flat if `V=1` on a neighbourhood"). So the flatness conclusion is on a neighbourhood, not only directional. (b) For the line defects of line 71 only `q_2,q_3` exist. Steps 1-2 then give `∂_2tr(h^p)=∂_3tr(h^p)=0` on `B`, so `V=1` on `(K₀+span{e_2,e_3})∩B`. Motion along the line is not excluded. (c) Credit: the mechanism is `RCS1.md` Lemma 5.1 (frozen, lines 70-74). `LZ1.md` Theorem 2.2 proves neighbourhood flatness for the finite-pattern vacuum case (`RCS1.md` line 80: "that theorem also proves neighbourhood flatness"). Lemma N extends it to every covariant representation that carries three position labels.

### 2.2 Closure C-NN: NN-a decomposition of the transfer layer (items 4, 45)

The distiller's GAP (line 101): "The site gate in Theorem 8(iii) touches six link registers. The draft gives no finite decomposition into NN-a's two-site, one-link gates." The gap is real: `DRAFT:259` claims membership in `𝒰` and `LZ1.md`'s form only.

NN-a (`TOE_ASSEMBLY.md` line 235): "A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`. ... Evenness means `[g,P_xP_y]=0` ... A nearest-neighbour layer is a locally finite product on pairwise disjoint edge triples. The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s`, for `s∈𝒢=2Z³⋊O_{c₀}`. ... Gauge invariance and cell covariance are required of the complete update only." NN-a is stated "For the named five-mode laws". D-reg is not a named law's register. Below, NN-a's words are read with `H_ℓ=Q⊗Q` and nothing else changed. Four tests of that substitution: (1) P, it states no target; (2) P, it is closed; (3) P, it decides nothing downstream; (4) P, it adds no structure. It is used only to decide the GAP and is not proposed.

`GA1_5.md` Proposition C(ii) reads: "Every member of GA1-P-5, on either law, is a composition of finitely many such layers, each invariant under `2kZ³` for some `k≥1` that depends on the member." The transfer layer is not a member of GA1-P-5, and D-reg is not either law. So C(ii) does not apply as stated. Its proof does apply, because Lemma U does not depend on the register: its proof uses only `dim H_ℓ≥2` and `𝒜_w^+≅M_{16}⊕M_{16}` (`GA1_5.md` line 234). Both hold here; `dim Q⊗Q=33²`.

**Proposition C-NN (referee closure).** Read NN-a with `H_ℓ=Q⊗Q`. For every real `θ`, the automorphism of `W_K(θ)=∏_ye^{iθh_y}` is a composition of `64L` NN-a layers, where `L` is the length of one Lemma U word for `e^{iθh_0}`. Each layer is a product of even nearest-neighbour gates on pairwise disjoint edge triples and is invariant under `4Z³`. Each gate lies in some `𝒢_{y,ℓ}=𝒜_y^+⊗B(H_ℓ)` with `ℓ∋y`.

*Proof.* (1) The six links of the star of `y` form a connected set `L′`. The set `S′` of sites shared by two of them is `{y}`. `e^{iθh_y}` is a unitary on `⊗_{ℓ∋y}H_ℓ`; it is the identity on the far-end factors and on all matter. Lemma U writes `e^{iθh_y}⊗1` as a finite word of unitaries in the algebras `𝒢_{y,ℓ}`, `ℓ∋y`. Fix one word for `y=0` and use its translate at every `y`. This is valid because `h_y` is the translate of `h_0`: the register and `K` are the same at every site.
(2) Each letter is an NN-a gate for its link `ℓ=(y,y′)`. It is a unitary in `𝒜_y^+⊗B(H_ℓ)`, so it is supported within `F_y` and `H_ℓ`. It commutes with `P_y`, being even at `y`, and with `P_{y′}`, an even element at another site; links commute with matter. So `[g,P_yP_{y′}]=0`.
(3) The word at `y` uses edge triples whose sites lie within distance 1 of `y`. If `y−y′∈4Z³∖{0}`, then `‖y−y′‖_∞≥4`, so the two words use disjoint site sets and hence disjoint edge triples. So for each class `c∈Z³/4Z³` the `k`-th letters of the words at all `y∈c` form one NN-a layer, invariant under `4Z³`. All words have length `L`.
(4) The gates `e^{iθh_y}` commute pairwise (Theorem 8(iii)). So `W_K(θ)=∏_c∏_{y∈c}e^{iθh_y}` for any order of the 64 classes, and each class product is the parallel run of its words, in `L` layers. On each local observable only finitely many gates act, so the operator identities give the identity of automorphisms (`LW1.md` E1, as in the proof of `GA1_5.md` Proposition C). The count `64L` does not depend on the volume. □

This is the scheduling of `GA1_5.md` Proposition C(ii) with `k=2`. Status: `GA1_5.md` line 11 lists Lemma U and Proposition C among "Referee closures, unrefereed". C-NN inherits that status.

**What C-NN does not give.** The letters are not gauge invariant; NN-a allows this. The complete layer fixes every local gauge generator, since each `e^{iθh_y}` is gauge invariant. Cell covariance of the complete update is closure CV (§2.3). C-NN covers the transfer layer only. Whether the matter cube gates of the base tick have an NN-a decomposition is a question about the base law; it is not checked here.

### 2.3 Closure CV: cell covariance on D-reg (items 4, 43)

Theorem 8(iii) says the transfer layer is "translation- and rotation-covariant". The draft's proof, `DRAFT:271`: "A rotation about `y` permutes the six links at `y` and maps `h_y` to itself, because the sum runs over all ordered pairs." The lift used there maps each end factor `Q^{ℓ,z}` to `Q^{gℓ,gz}` by the identity map of `Q` (`DRAFT:259`: "A rotation that reverses a link swaps its two end factors, which the register `Q⊗Q` allows"). Call it the *bare lift*. Under it `K_{ℓℓ′}↦K_{gℓ,gℓ′}`, so the transfer layer is covariant. That proves item 43 as stated.

NN-a needs the complete update to commute with every cell lift. For `L5-O[S_+]`, `LW1_5.md` line 264 proves this: "A geometric symmetry of the dressed Majorana law acts on a reversed link by exchanging the two sets of ten auxiliary Majoranas. This is an orientation-preserving transformation in 20 dimensions and lifts to Spin(20); it sends `U^{ab}` to `−U^{ba}`, while reversing the two matter Majoranas gives the other minus sign. Site parity implements LW1's sign lift."

**The missing sign on D-reg.** The bare lift sends `U^{ab}=Γ_b⊗Γ_a` to `Γ_a⊗Γ_b`, which is `+U^{ba}` on the image link. Let `g` reverse `ℓ=(x,y)`, so the image link `ℓ′` has source `y′=gy` and target `x′=gx`. With `h_ℓ=(i/2)Σ_{ab}γ_{y,a}U^{ab}_ℓγ_{x,b}` (`LW1_5.md` line 89),
\[
h_ℓ\mapsto\tfrac i2\sum_{ab}γ_{y′,a}U^{ba}_{ℓ′}γ_{x′,b}=-\tfrac i2\sum_{ab}γ_{x′,b}U^{ba}_{ℓ′}γ_{y′,a}=-h_{ℓ′},
\]
because Majoranas at different sites anticommute and links commute with matter. On `S_+` the Spin(20) swap supplies this sign; the bare lift does not.

**Lemma CV (referee closure).** Let `g∈𝒢` have linear part `R` with `Re_i=σ_ie_{π(i)}`, `σ_i=±1`. Put `J(g)={π(i):σ_i=−1}` and `s_g(x)=(−1)^{Σ_{j∈J(g)}x_j}`. Define the D-reg lift `α̂_g` as the lift of `LW1_5.md` line 264 with two changes: on a reversed link the bare swap replaces the Spin(20) swap, and the matter sign `d_g(gx)` is multiplied by `s_g(gx)`. Then the D-reg base tick at `τ_E=0`, with or without the transfer layer appended, commutes with every `α̂_g`, and `α̂_g` maps Gauss generators to Gauss generators.

*Proof.* `g` reverses exactly the links of the directions `i` with `σ_i=−1`. Their images are all the links of the directions in `J(g)`. For a link `(x,x+e_j)`, `s_g(x)s_g(x+e_j)=−1` if `j∈J(g)` and `+1` otherwise. So the extra signs give exactly one factor `−1` on the image of each reversed hop, and no factor elsewhere. Each hop then maps to its image hop with the same sign as on `S_+`, and the cube layers map as in the proof at `LW1_5.md` line 264. At `τ_E=0` there is no electric layer. The matter signs cancel in `M^{cd}_x`, and the bare lift maps `L^{cd}_{ℓ,z}` to `L^{cd}_{gℓ,gz}`; so Gauss generators go to Gauss generators. The transfer layer acts on links only. Matter signs commute with it, and the bare lift maps it to itself. □

The proof ports `LW1_5.md` line 264 (frozen) for the base tick. The only new steps are the sign computation and `s_g`. It needs `τ_E=0`: `LW1_5.md` line 92 says "A more general register and an invariant electric operator require their own covariance check." With C-NN, the transfer layer on D-reg meets NN-a's decomposition, evenness, gauge and covariance conditions, read with `H_ℓ=Q⊗Q`, provided the base tick's own gates meet NN-a. That proviso is not checked here.

### 2.4 Theorem 9: repairs (items 46-49)

**Singlets (item 46), rebuilt.** Matter at a site and an end in `H` both carry the Dirac module of `Spin(10)`; write `H=H_+⊕H_−` for its halves. The centre element `ω` has `R(ω)=−I` and `ω^2=−1` (`LW1_5.md` line 154, S′ step 2). So `ω` anticommutes with every `γ_a`, commutes with the even algebra, which acts irreducibly on each half (`LW1_5.md` line 155, step 3), so it acts on each half by a scalar; the two scalars are `ζ` and `−ζ` with `ζ^2=−1`. On a product of two equal halves `ω⊗ω` acts by `ζ^2=−1`, so there is no invariant vector. The form `β(s,t)=s^TCt` of Theorem 8(iv) is invariant and nondegenerate, since `C` is invertible and `CgC^{-1}=(g^{-1})^T`. By the same scalar argument it vanishes on equal halves, so it pairs `H_+` with `H_−` and `H_−≅H_+^*`. The halves are irreducible (`LW1_5.md` line 185: "that half-spin module is irreducible"). By Schur's lemma `H_+⊗H_−` and `H_−⊗H_+` each have one invariant line. So matter `⊗` end has exactly two invariant lines, one for each matter parity. `[check]` agrees for `Spin(6)` and `Spin(10)` (§2.6).

**Local form (item 47).** Replace "Their closed product span" by a statement on finite site sets `Y`. Let `𝒮_Y` be the span, in the space of the matter at `Y` and the `Y`-end factors of the links at `Y`, of the product vectors with exactly one `H`-end per site, singlet-coupled to that site's matter, all other ends `|0⟩`. Each `h_y`, `y∈Y`, maps `𝒮_Y` into itself; so does each hop on a link with both ends in `Y`, tensored with the far ends. On `𝒮_Y`, `z_y=+1` for `y∈Y`. The D1 state and the string states are product states whose local vectors lie in such spaces. Every use in the proof is local, so nothing else changes.

**Parity-definite eigenvector (item 48).** Fix a two-arrow link `ℓ=(x,y)`. Let `S_x`, `S_y` be the two-dimensional singlet spaces, with basis `σ_+,σ_−` by matter parity. Since `U^{ab}=Γ_b⊗Γ_a` factorizes, `h_ℓ=(i/2)A_yB_x` with `A_y=Σ_aγ_{y,a}Γ_a^{(y)}` and `B_x=Σ_bΓ_b^{(x)}γ_{x,b}`. Each is gauge invariant, Hermitian (commuting Hermitian factors) and odd at its site. So on its singlet space each is off-diagonal: `B_xσ_+=βσ_−`, `B_xσ_−=β̄σ_+`, and likewise `α` for `A_y`. Hence `h_ℓ` maps `σ_p⊗σ_q` to a multiple of `σ_{−p}⊗σ_{−q}`, and every matrix element has modulus `|α||β|/2`; the fermionic reordering contributes signs only. In the pair-even sector `span{σ_+σ_+,σ_−σ_−}` and in the pair-odd sector `span{σ_+σ_−,σ_−σ_+}`, `h_ℓ` is Hermitian and off-diagonal with entries of modulus `|α||β|/2`. So both sectors have the eigenvalues `±|α||β|/2`. `[check]`: `|β|=10` for `Spin(10)`, so these are nonzero. Each eigenvalue therefore has a two-dimensional eigenspace spanned by one pair-even and one pair-odd vector, and "a fixed eigenvector" admits parity-mixing choices. The proof's product state uses even local factor states; a vector of definite pair parity gives one, since odd operators map it into the orthogonal opposite-parity space. **Fix:** "choose an eigenvector of definite pair parity `P_xP_y`; this is possible because `h_ℓ` commutes with `P_xP_y`." With it, the state is a product of even pure states on disjoint finite blocks. It is pure, stationary, invariant under `τ_β` and under local gauge transformations, hence D1 (`LZ1.md` §1).

The tick is `LW1_5.md`'s `U₀=W_EM_oM_e` with `τ_E=0`. A direction-1 link lies in an even-tiling cube exactly when its base coordinate `x_1` is even (`LW1_5.md` line 216: "a direction-1 link belongs to the even or odd tiling according to the parity of its base coordinate `x_1`"). So every two-arrow link lies in an even cube, four per cube. On the columnar subspace every hop on a zero-arrow link vanishes. The even-cube gate `e^{−ia_eH_C}`, `H_C=3^{−1/2}Σ η_i(x)h_ℓ`, factors into the four commuting two-arrow link gates, and each odd-cube gate acts as the identity. The eigenvector of `h_ℓ` does not depend on the factor `3^{−1/2}η_1(x)a_e`, so one choice serves every two-arrow link.

**Density of local invariants (item 49).** The string proof uses a dense set of vectors `π(A)Ω` with `A` local in `𝔄^G`. `RCS1.md` definition 1 cites `VC1_5.md` Theorem 2.1 for density, stated for the two laws. On D-reg it holds by averaging. Let `A∈𝔄^G` and local `A_n→A`. Let `E_n` average `Ad` over the Haar measure of the product of the gauge groups at the finitely many sites that meet the support of `A_n`. Then `E_n(A_n)` is local and gauge invariant, and `‖E_n(A_n)−A‖=‖E_n(A_n−A)‖≤‖A_n−A‖`, because `E_n(A)=A` and `E_n` is a contraction.

### 2.5 Small repairs (items 19, 23, 30, 34, 45)

**Item 23, line 53.** The text says "Set `κ₀(x)=ω₀(z_x)∈{±1}`" and "`Z_Λ=∏_{x∈Λ}u_x=s_ΛΦ_Λ`" without reasons. Repair, from `DRAFT:162,166`: for `Λ={x}` there are no internal links, so Theorem 2 gives `Φ_{{x}}=−z_x`, and flux-sharpness gives `κ₀(x)∈{±1}`. As `z_x` is a self-adjoint unitary, `ω₀((z_x−κ₀(x))^2)=0`, so `π₀(z_x)Ω₀=κ₀(x)Ω₀` in the GNS space of `ω₀`. Hence `ω₀(∏_{x∈Λ}z_x)=∏_{x∈Λ}κ₀(x)` and `s_Λ=σ_Λ∏_{x∈Λ}κ₀(x)`. With `Φ_Λ=σ_Λ∏_{x∈Λ}z_x` this gives `s_ΛΦ_Λ=∏_{x∈Λ}κ₀(x)z_x=Z_Λ`.

**Item 30, line 67.** The proof shows that `∏_{x∈S}z_x` commutes with `B`, then says "Thus for every `Λ⊇S`, `Z_Λ` commutes with `B`". The factors `z_x`, `x∈Λ∖S`, are not treated. Repair: for `x∉S`, the site factor of `z_x` is the scalar `−1` and its end factors act on links at `x`; none of these is in the support of `B`, since every supported link has both ends in `S`. This is `LW1_5.md` Theorem SC(b): "`Ad z_x` fixes `O` for `x∉S`." So `Z_Λ=(∏_{x∈S}κ₀(x)z_x)(∏_{x∈Λ∖S}κ₀(x)z_x)` commutes with `B`. With this line the proof is complete. It is shorter than `DRAFT:199`, which uses the decomposition `B=Σ_TB_T`.

**Item 34, line 73.** "a product field state with every link in a fixed `S_+` vector" leaves the matter unspecified. A product state of the matter CAR algebra over infinitely many sites needs even local factors. Restore `DRAFT:205`: "and every site in one fixed even matter vector."

**Item 45, line 101.** "The failure of the static-flux proof occurs precisely in Theorem 2" is imprecise. Theorem 2's identity holds on D-reg; its link-pure clause does not apply. Repair: "occurs in the link-pure clause of Theorem 2: the internal product of `d_ℓ` is an operator, not a scalar."

**Item 19, line 43.** The proof cites only the pass-1 draft. The same fact is in frozen text, `LW1_5.md` line 169: "For an `so(20)` link the two `ε`'s coincide." Cite both.

### 2.6 Check record

`[check]` Script `/tmp/toe-CG16Dref/check_cg16dref.py` (outside the repo), run once on 2026-11-07 with `python3 -I`, after `memory_pressure` showed 54 percent free. It ran 8 s; peak memory footprint 893 MB; maximum resident set `1.02·10^9` bytes (0.95 GiB). Floating point, numpy. For `n=3` (`Spin(6)`, `H=C^8`) and `n=5` (`Spin(10)`, `H=C^{32}`), with Jordan-Wigner Majoranas and `M^{cd}=(i/2)γ_cγ_d`:

- singlets of matter `⊗ H` under the diagonal action: dimension 2, with matter parities `−1` and `+1` (item 46);
- `B=Σ_bγ_b⊗Γ_b` commutes with the diagonal generators (residual 0); on the singlets it is off-diagonal with both entries of modulus `2n` (6 and 10) (item 48);
- `K` on `Q⊗Q`: `max|[K,L_1+L_2]|=0`, `max|{K,ε_1}|=0`, `max|{K,ε_2}|=0` (item 41);
- `C=∏` of the real Jordan-Wigner generators satisfies `CΓ_aC^{-1}=Γ_a^T` (residual 0); the vectors `w_a` obey `(L⊗1+1⊗L)w_a=Σ_bm_{ba}w_b` with the matter coefficients `m` (residual 0); `min|w_a|>0` (item 44).

The check guides only. No verdict above rests on it.

### 2.7 A remark on the relative label (items 55, 57)

Line 123: "A merely flux-sharp nonperiodic background gives the support theorem, but does not by itself supply the covariant position label used in Theorem 6(ii)." The caution is needed. The periodicity of the background cannot simply be dropped.

**Observation (referee).** Take link-pure registers. Let `ω_per` be a flux-sharp state of `𝔄^G` whose configuration `κ_per` is cell-periodic. Let `ω₁` be a flux-sharp state whose configuration `κ₁` differs from `κ_per` exactly on a finite set `F₀` of odd size. Then the GNS representation `π_per` of `ω_per` has `χ_sp(π_per:ω₁)=−1`.

*Proof.* The `z_x` are central in `𝔄^G` and sharp in `ω_per`, so `π_per(z_x)=κ_per(x)I` on its cyclic space. Relative to `ω₁`, `Z_Λ=∏_{x∈Λ}κ₁(x)z_x` acts there as `∏_{x∈Λ}κ₁(x)κ_per(x)=(−1)^{|F₀∩Λ|}`. This is `−1` once `Λ⊇F₀`. □

Example 1 gives an instance: `ω₁=ω_x` and `ω_per=ω₀`. So "spinor class relative to `ω₁`" includes the periodic sector itself, with every band that a covariant representation of that sector may carry. Theorem 6(iii)'s words "a finite nonempty set" exclude exactly this configuration. The label measures the background's own defect as well as the sector's. For the target this does no harm. There the background is a D1 state, hence even-translation invariant, so `κ₀` is periodic and Theorem 6(ii) applies. What remains is a D1 background whose centre labels are not sharp: CG16D-SC (line 120). The observation shows only that relative class over a non-periodic background is not a position label; it says nothing about bands of `ω₀`.

## 3. The distiller's GAPs, the named questions, and the pass-1 sources

### 3.1 GAPs marked by the distiller

| GAP (line) | Real? | Verdict and repair |
|---|---|---|
| G1. NN-a compilation of the six-link transfer layer (9, 21, 101) | Real in the draft | Closed by referee closures C-NN (§2.2) and CV (§2.3), with NN-a read with `H_ℓ=Q⊗Q`. Repaired statement for line 101: "The site gate of Theorem 8(iii) touches six link registers. Lemma U of `GA1_5.md` compiles it into even nearest-neighbour gates in the algebras `𝒢_{y,ℓ}`, and the layer runs in `64L` layers invariant under `4Z³` (referee closure C-NN). With the lift of closure CV, the base tick at `τ_E=0` with this layer appended is cell covariant. NN-a for the base tick's own matter gates is not checked." C-NN inherits the unrefereed status of Lemma U and Proposition C. |
| G2. No physical identification shows that the flux label exhausts every meaning of the CG1 16, especially on `L5-U` (9) | Real | It is the owner reading R-CG1. `LW1_5.md` line 352 records it: "Open only as the owner reading R-CG1". No proof closes it. Carry by name. It is not a defect of any proof. |
| G3. The N1-N8 landing packet is not complete (9) | Procedural | Outside this proof check. No verdict. |

### 3.2 The named questions

1. **Scalar flux on `L5-O[S_+]` (Theorem 4).** CORRECT. `ε=−1` on every link end, `z_x=−1`, and `Φ_Λ=(−1)^{|∂Λ|}=1` as elements of `𝔄`, since `|∂Λ|=6|Λ|−2|L_int(Λ)|` is even. So `χ_sp=+1` for every representation relative to every state, for every update and every state. The absolute reading "eigenvalue `±i`" holds in every factor sector, the background included (`RCS1.md` Theorem 1).
2. **Static-label obstruction on link-pure registers (Theorems 5-6).** CORRECT, with the repairs of items 23 and 30. **The named step is propagation, not confinement.** Spinor-class sectors exist on a link-pure register (Example 1, made singly by a string and in pairs by a local operator). No hypothesis of Theorems 5-6 concerns string energy, deconfinement or phase. What fails is motion: over an even-translation-invariant flux-sharp background, every band in a `χ_sp=−1` covariant representation is flat. On `L5-O[S_+]` itself the failing step comes earlier: no such sector exists (Theorem 4).
3. **Flatness: directional or on a neighbourhood.** On a neighbourhood. Lemma N (§2.1) gives `V=1` on a `C¹` ball around every node, from the three position labels that Theorem 6 already has. Only for full line defects is it directional (two labels), as item 33 states.
4. **Proposition C, no analogue on `L5-U` (Theorem 7).** CORRECT. The law's gauge action factors through `U(5)`, so the pulled-back `−1∈Spin(10)` acts as `1`; every `ε` and every `Φ_Λ` is `1`; `c_x^2=1`, so relative values are `±1`. It excludes no projective charge of another symmetry and no Standard-Model-family reading, as line 83 says.
5. **Proposition D on D-reg (Theorems 8-9).** Invariant transfer: CORRECT. Odd invariant operator: CORRECT. Pure D1 singlet state: CORRECT after the parity fix of item 48. String-made defects with `χ_sp=−1`: CORRECT, with the density line of item 49. The D-reg four-test record `F,P,P,F` stands. D-reg is recorded, not proposed.
6. **The NN-a GAP.** Closed for the transfer layer by C-NN and CV, as in 3.1.

### 3.3 Check against the pass-1 sources

Every theorem of `CG16D.md` matches its draft source in content (name map in section 1). The distillation changes the draft in five places that matter. (a) Theorem 6(i)'s proof is shorter than `DRAFT:199` and drops one line (item 30). (b) Example 1 drops "even matter vector" (item 34). (c) The setup of §3 drops the reasons at `DRAFT:162,166` (item 23). (d) Theorem 9 keeps the draft's "a fixed eigenvector" (`DRAFT:269`), which needs the parity fix in both texts (item 48). (e) The distillation frames Theorems 4 and 7 "under the proposed relative flux reading" (line 123); the draft's FINISH (`DRAFT:309`) calls them counterexamples to the target outright. The distilled framing is the accurate one. The draft's claim at `DRAFT:320` that R-CG1 "does not change the answer on `L5-O`" between the two notions on file is not carried into `CG16D.md`; line 121 keeps R-CG1 open. That is also accurate.

## 4. Required edits

Each edit names the `CG16D.md` line, the change, and the argument. Imported closures carry "(referee closure, CG16D_REFEREE.md)".

| Edit | Line | Change |
|---|---|---|
| E1 | 7, 63-69, 123 | Replace "The flatness conclusion is directional at each node, not necessarily flatness on a neighbourhood." by "In the representations of Theorem 6, every band is flat on a neighbourhood of each node: `V=1` near `K₀` (Lemma N)." Insert Lemma N and its proof (§2.1) after Theorem 6. In line 123 replace "Theorem 6 blocks a nonzero leading generator" by "Theorem 6 with Lemma N gives `V=1` near every node". |
| E2 | 9, 21, 101 | Replace the NN-a GAP by the repaired statement of §3.1, G1. Insert Proposition C-NN (§2.2) and Lemma CV (§2.3) with their proofs, marked "referee closure, unrefereed", and note that C-NN inherits the status of `GA1_5.md` Lemma U and Proposition C. |
| E3 | 53 | Insert the two reasons of §2.5, item 23. |
| E4 | 67 | Insert the line of §2.5, item 30. Cite the frozen `LW1_5.md` line 171 (F and K, pairing) beside `LW1_5O_DRAFT.md` (K5). |
| E5 | 73 | After "every link in a fixed `S_+` vector" add "and every site in one fixed even matter vector". |
| E6 | 101 | "occurs precisely in Theorem 2" becomes "occurs in the link-pure clause of Theorem 2". |
| E7 | 103-105 | (a) Replace "Their closed product span" by the local form of §2.4. (b) Replace "a fixed eigenvector of each paired-link hop" by "a fixed eigenvector of definite pair parity `P_xP_y` of each paired-link hop", with the reason of §2.4. (c) Add the tiling sentence of §2.4 (`LW1_5.md` line 216) and the density line. |
| E8 | 43 | Cite `LW1_5.md` line 169, "For an `so(20)` link the two `ε`'s coincide", beside the pass-1 draft. |
| E9 | 95 | After "rotation-covariant" add "under the lift that maps end factors by the identity of `Q`; for the composite update see Lemma CV". |
| E10 | 71 | Optional. Add: "With two labels, Lemma N's argument gives `V=1` on `(K₀+span{e_2,e_3})` near the node." |
| E11 | 120 | Optional. Add the observation of §2.7 to CG16D-SC. |

No edit changes the statement of a theorem except E1, which strengthens a conclusion, and E7(b), which restricts a choice.

## 5. Open statements to carry by name

- **CG16D-NLP** (line 119). On a non-link-pure law such as D-reg: find or exclude an update in `𝒰` with a stationary D1 state, a string-made `χ_sp=−1` sector that is deconfined, and a band with a node and a nonzero leading generator. On file after this report: the D1 state and string defects (Theorem 9 with E7), the transfer layer in NN-a form with a cell-covariant composite at `τ_E=0` (C-NN, CV). Open: an update that keeps such a D1 state stationary and moves a defect with nonzero `N_j` (the transfer layer breaks matchings, line 107), any energy bound, and the NN-a form of the base tick's matter gates on D-reg (the proviso of CV). The register lies outside both live laws; its four tests are `F,P,P,F`.
- **CG16D-SC** (line 120). The meaning of relative spinor class over a background whose centre labels are neither sharp nor periodic, for example the tracial state on `S_+⊕C^{20}`. §2.7 shows that over a non-periodic flux-sharp background the relative label is not a position label. A specification is the owner's choice.
- **R-CG1** (line 121; GAP G2). Which notion of "16" CG1 needs. Owner reading.
- **RCS-P, R-CS, LW1-5-BG, GA1-P-5** (line 121). Unchanged.

No new open statement arises from this report. The closures N, C-NN and CV are proofs, not open items.

## 6. Freeze recommendation

**Freeze after edits E1-E9.** E10 and E11 are optional. The report finds no ERROR. It finds five INCOMPLETE items (3, 23, 30, 47, 48), and each has a repair above. No repair changes what a theorem asserts, except that E1 strengthens directional flatness to flatness on a neighbourhood and E7(b) restricts the choice of eigenvector in Theorem 9.

On freezing, the following enter as "referee closure, CG16D_REFEREE.md", unrefereed: Lemma N (§2.1), Proposition C-NN (§2.2), Lemma CV (§2.3), and the repairs of §§2.4-2.5. C-NN also rests on `GA1_5.md` Lemma U and Proposition C, which `GA1_5.md` line 11 lists as unrefereed referee closures. The proposed readings stay unadopted: the relative flux label `χ_sp`, NN-a read with `H_ℓ=Q⊗Q`, and the register D-reg with its lift.

## Prior work used

Paths are relative to this folder unless a branch is named.

- `RCS1.md` Lemma 5.1 and Theorem 5 (lines 70-78): ported in Theorem 6; their proof is extended in Lemma N to three labels and neighbourhood flatness.
- `RCS1.md` R2(a) (lines 159-165): the proof of Theorem 1.
- `RCS1.md` Theorem 1 (line 36): centrality of `c_z` and `κ^2=−1` on `L5-O[S_+]`, `κ^2=1` on `L5-U`; used in items 20-21 and 36-37.
- `LZ1.md` §1 (lines 34-44): the update class, D1 states, bands, nodes, and "flat if `V=1` on a neighbourhood".
- `LW1_5.md` line 169 (centre identities, `ε`'s coincide on `so(20)` links), line 171 (F and K, pairing), Theorem SC(b) (lines 187-200), S′ step 2 (line 154), line 185 (half-spin irreducibility), line 216 (tilings of direction-1 links), lines 89 and 97 (the two laws' hops and generators), line 264 (the `L5-O` cell lift; extended in Lemma CV).
- `GA1_5.md` Lemma U and Proposition C (lines 236-272): applied, by their proofs, in Proposition C-NN.
- `TOE_ASSEMBLY.md` line 235 (NN-a, owner decision GA1-P-NN).
- Consolidation branch `origin/docs/consolidate-gauge-matter-registers` at `7086189d1`, `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 979, 987, 1204 (#10027 boundary, #10045): checked as quoted in `CG16D.md` §6.

**Prior work the digest missed.** `prior/CG16D.md` does not list `GA1_5.md` Lemma U and Proposition C, which decide the NN-a GAP; `LW1_5.md` line 264, which carries the cell lift that Lemma CV modifies; or `LZ1.md` §1's neighbourhood definition of "flat", which settles what Theorem 6 should conclude. It cites `RCS1.md` only through lines 16, 64 and 219-227, not Lemma 5.1, whose proof gives Lemma N.

## FINISH

**Status.** Pass-3 referee report on `CG16D.md` at `59d3886d9`, by a Claude Opus 5.5 headless lane on the Mac mini, 2026-11-07. It adopts no law, reading, specification or definition. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Proved.**
- Verdicts: 57 items, 52 CORRECT, 0 ERROR, 5 INCOMPLETE (items 3, 23, 30, 47, 48), each with a repair.
- Lemma N (§2.1): a covariant representation with three position labels on one decomposition has every band flat on a neighbourhood of each node. So Theorem 6's conclusion is `V=1` near every node, not only directional flatness. With two labels (line defects), `V=1` on the transverse plane through the node.
- Proposition C-NN (§2.2): with NN-a read with `H_ℓ=Q⊗Q`, the D-reg transfer layer is a composition of `64L` layers of even nearest-neighbour gates on disjoint edge triples, each layer invariant under `4Z³`. It uses `GA1_5.md` Lemma U and the scheduling of Proposition C(ii), whose proof applies though its statement does not.
- Lemma CV (§2.3): on D-reg the bare end swap gives the Majorana hop a sign `−1` on reversed links. One extra cell-periodic site sign per reversed direction removes it. Then the base tick at `τ_E=0`, with or without the transfer layer, commutes with every cell lift.
- §2.4: the two singlets per site, rebuilt from the centre scalars and Schur's lemma. The paired-link hop has eigenvalues `±|α||β|/2` in both pair-parity sectors, so the D1 construction needs an eigenvector of definite pair parity. Local gauge-invariant elements are dense on D-reg.
- §2.5: the missing lines in the §3 setup and in Theorem 6(i).
- §2.7: over a flux-sharp background that is a finite odd defect of a periodic one, the periodic sector itself has `χ_sp=−1`. So relative class over a non-periodic background is not a position label.
- The named questions (§3.2): Theorem 4 (no spinor flux on `L5-O[S_+]`), Theorems 5-6 (static labels; the named step is propagation, not confinement), Theorem 7 (no analogue on `L5-U`) and Theorems 8-9 (D-reg transfer, odd invariant, D1 singlet state, string defects) are correct, with the repairs listed.

**Counterexamples.** None to any theorem of `CG16D.md`.

**Open by name.** CG16D-NLP, including the NN-a form of the base tick's matter gates on D-reg (the proviso of Lemma CV); CG16D-SC; R-CG1; RCS-P; R-CS; LW1-5-BG; GA1-P-5.

**What changes downstream.**
- `CG16D.md`: freeze after edits E1-E9 (section 4).
- CG1(e), MT1 and LZ1, under the relative flux reading: on link-pure registers over flux-sharp D1 backgrounds, every band in a spinor-class sector has `V=1` near every node, which is "flat" in the sense of `LZ1.md` §1. On `L5-O[S_+]` no such sector exists; on `L5-U` no analogue exists. R-CG1 stays open, so CG1's own reading of "16" is not decided.
- GA1-P-NN users: the argument of C-NN shows that the proof of `GA1_5.md` Proposition C(ii) applies to any link-only layer of commuting finite-support gates on finite registers of dimension at least 2, not only to members of GA1-P-5.
- D-reg remains recorded, not proposed. The route through it is CG16D-NLP.
- No frozen result changes.
