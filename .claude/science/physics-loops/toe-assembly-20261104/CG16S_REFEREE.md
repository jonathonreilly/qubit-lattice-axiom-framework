lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CG16S referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane (model id `claude-opus-5-5`, max effort) on the Mac mini, as pass 3 (the referee) under PR #10138's method. The lane brief's file template says "pass 1"; this lane is the referee. This session wrote neither pass 1 (`CG16S_DRAFT.md`) nor pass 2 (`CG16S.md`). This is one check: one whole-part, line-by-line read. It reviews no other review.

**Text read.** `CG16S.md` as of commit `c82ee8663` (the last commit that touches it; branch head `c82ee8663` when read). SHA-256 of the file read: `c23ce4472f7b98f8cc3383c01382c80f96747927f82b09badc690c24ff042977`. Line numbers below refer to that file. It was read line by line, in full (138 lines).

**References consulted, with commits.** This checkout, branch `claude/toe-assembly` at `c82ee8663`: `CG16S_DRAFT.md` lines 1-370 (all; SHA-256 `c817ba9008cf1f12...`, equal to the hash `CG16S.md` line 13 records); `prior/CG16S.md` lines 1-81 (all; hash equal to line 13's); `TOE_ASSEMBLY.md` lines 231-245 (sections 3.7 and 3.8: NN-a and ZM1-I1[a]); `LZ1.md` lines 1-70 (status, section 1, Theorems 2.1-2.3); `RCS1.md` lines 60-66 (Theorem 4 and its proof); `TM1.md` lines 20-62 (Definitions 1-8, Lemma R2, Theorems 1-5); `ZM1.md` lines 53, 71 (Definition Z, (G1)), found by grep; `LW1_5.md` lines 52, 171, 200-212 (end-pure and link-pure, F and K, SC.1, Σ, the reducible-register closure, S1-S4), found by grep. The context hashes on `CG16S.md` line 13 for `TOE_ASSEMBLY.md`, `LW1_5.md`, `RCS1.md`, `TM1.md`, `LZ1.md`, `ZM1.md` and `LW1.md` equal the current files `[check: shasum]`. Branch `origin/claude/toe-site-count-matter-20261021` at `5adea19dc2` (read with `git fetch -q` and `git show` only): the #10038 note, lines 62-84 (A2-A7/C0). No other review was read.

**Method.** Every proof in `CG16S.md` was re-derived by hand. Each cited pass-1 step was compared with `CG16S_DRAFT.md`. Verdicts: CORRECT; ERROR (a false or misleading line, quoted, with a fix); INCOMPLETE (a named missing step). A "referee closure" (RC) is a complete argument for a missing step, written here for the lead to check. One `[check]` was run: `/tmp/toe-CG16Sref/check_rcw.py` (numpy, 0.22 s, 33 MB peak), started after `memory_pressure` reported 54 percent free. It tests the operator identity used in RC-W on random 24-dimensional matrices. It guides and proves nothing.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". NN-a, ZM1-I1[a], PS-5 and the Record axiom are read plainly. Where SC-odd changes PS-5, this is recorded as a change, not attacked.

**Working-set entries used.** GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` line 235); ZM1-I1[a] (line 243), only for its "singleton embedding sets"; PS-5, only as `CG16S.md` quotes it. Proposed and unadopted, read as conditional hypotheses: SC-min, SC-odd, PS-3g, PS-3h5, R-loc, L-point, L-site. Results used: `LZ1.md` section 1 and Theorems 2.1-2.2; `RCS1.md` Theorem 4; `TM1.md` Definitions 3-6 and Theorems 1-4; `ZM1.md` Definition Z and (G1); `LW1_5.md` line 52 and S1-S4.

**Counts.** 53 items: 44 CORRECT, 3 ERROR, 6 INCOMPLETE. The eight distiller definitions count as eight items. No ERROR changes the content of a theorem. Item 34 changes the wording of a hypothesis of Theorem 7. Four referee closures (RC-W, RC-Z, RC-T, RC-C) are in §3.

---

## 1. Verdict table

| # | Item (CG16S line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | |
| 2 | §0 "Proved below" (7) | INCOMPLETE | The list omits Theorem 4 (with its link counterexample), Theorem 8, Theorem 9 and Theorem 11. Add them (edit E1). |
| 3 | §0 GAPs paragraph (9) | ERROR | Line 9: "The coarse-centre argument needs link-purity, omitted from its statement". The draft's proof uses link-purity at one step. The result does not need it (RC-Z, §3). As a claim about what Theorem 12 needs, the sentence is false. The other sentences describe real gaps; RC-W repairs the winding gap. |
| 4 | §0 "Open by name" (11) | INCOMPLETE | It omits the gap of line 58 (a fully covariant SC-min law with motion; named CML in §6). "The free-walk winding question under NN-a" is closed by RC-W if the lead accepts RC-W. |
| 5 | §0 provenance (13) | CORRECT | All recorded hashes equal the current files `[check: shasum]`. |
| 6 | Def. 1, registers (19) | CORRECT | Matches draft Definition 3.1. |
| 7 | Def. 2, SC-min and SC-odd (20) | CORRECT | Matches NN-a: "Gauge invariance and cell covariance are required of the complete update only" (`TOE_ASSEMBLY.md` 235). NN-a's grading `P_x=(-1)^{N_x}` becomes Def. 1's `P` on `V`; that substitution is part of the proposal. |
| 8 | Def. 3, end-pure and link-pure (21) | ERROR | The word "link-pure" already has another meaning. `LW1_5.md` line 52: "it is link-pure when the product of its two end actions is scalar", meaning the end actions of `−1` only. Line 21 adds the `ω` condition. One word now has two meanings. Fix: rename line 21's condition (say "ω-pure") and state that it is LW1_5 link-purity plus the hypothesis of `LW1_5.md` line 208, "the lift of `−I_20` acts as a scalar" (edit E2). |
| 9 | Def. 4, D1 states and bands (22) | CORRECT | Matches `LZ1.md` §1. |
| 10 | Def. 5, settings G, F and condition E (23) | CORRECT | |
| 11 | Def. 6, `Δn`, `θ`, classes (24) | INCOMPLETE | "its centre eigenvalue" names no centre element. The draft (Corollary 3.3) uses the eigenvalue of `Ad ω_x^{mat}` at a point `x`. Say so (edit E3). |
| 12 | Def. 7, R-site, R-point, L-point, L-site (25) | CORRECT | |
| 13 | Def. 8, TM1 and ZM1 inputs (26) | CORRECT | ZM1-I1[a] does retain "singleton embedding sets" (`TOE_ASSEMBLY.md` 243). |
| 14 | Theorem 1 and proof (30-32) | CORRECT | |
| 15 | Scope remark after Theorem 1 (34) | CORRECT | |
| 16 | Theorem 2, statement (36-40) | CORRECT | Re-derived: on `V⁻`, `ω_x=|∅⟩⟨∅|+io_x` and `P_x=(−1)^{o_x}`. |
| 17 | Theorem 2, proof (42) | CORRECT | It uses `M^{2j−1,2j}=n_j−1/2`. The opposite sign convention would swap which half-spin space has `ω=−i`. No claim depends on that choice. |
| 18 | Paragraph on #10038 and #10027 (44) | CORRECT | #10038 A2-A4 checked at `5adea19dc2`, lines 62-71. A3: "A defect is spinor class iff dn is odd, whatever its content parity dF." |
| 19 | Theorem 3, statement (46-54) | CORRECT | |
| 20 | Theorem 3, proof (56) | CORRECT | Re-derived. The graded product gives one uniform sign per `σ`, so isometry and orthogonality hold. On each pair `{v,T^σv}`, `h` acts as `σ_x`, so `exp(−iπh/2)` maps `v` to `−iT^σv`. Link-purity in both senses holds: the `y` end carries the contragredient factors. `S_+` is end-pure by `LW1_5.md` S1-S4 ("`S_+` into paired half-spin factors"). |
| 21 | Remark and GAP on motion (58) | CORRECT | The gap is real (§2, G1). The second sentence is right. Draft Proposition 3.4's proof step "Each gate commutes with `𝒢_x^{12}`" assumes gatewise invariance. Theorem 3 already repairs this by using the complete update. |
| 22 | Theorem 4, statement (60) | CORRECT | |
| 23 | Theorem 4, proof (62) | CORRECT | |
| 24 | Paragraph on #10038 A7/C0 and U(5) (64) | INCOMPLETE | #10038 A7/C0 is stated under the odd rule (line 80: "so under the odd rule it needs dn = 0 mod 4") and for operators of either parity. Theorem 4's matter-only clause is the even-operator case on `V`. Line 60's counterexample has even content under SC-min, so it does not meet A7 in its own setting. RC-C (§3) gives the SC-odd counterexample (edit E4). The U(5) remark is correct. Under L5-U's frame, `Λ⁰` is trivial, because `c_z=exp(iπQ_z)` with `Q_z=N_z+…` (`LZ1.md` §1). |
| 25 | Four-test paragraph (66) | CORRECT (as a report) | It reports the draft's ratings and adopts none. §4 gives the referee's assessment: test 4 is misapplied twice (edit E5). |
| 26 | Removed-site comparison (68) | CORRECT | It reports the draft's reads and is not re-read here. It makes no novelty claim beyond those reads. |
| 27 | Theorem 5, statement (72) | CORRECT | Decision on flatness: §4.1. |
| 28 | Theorem 5, proof, first paragraph (74) | CORRECT | For `z∉Λ`, `Ad ω_z` fixes `A`, because every link of `A` has both ends in `Λ`. So `A_κΩ∈H(κ)` with `κ` trivial off `Λ`. |
| 29 | Theorem 5, proof, second paragraph (76) | INCOMPLETE | "Its odd sector" needs a parity implementer `U_θ`. In LZ1 it exists because the product of the centre actions is `θ`. In case (a) the product is `i^{Δn}`, and under SC-odd `θ=(−1)^{Δn}`. So `θ=(∏_{z∈Λ}Ad ω_z)²` on operators localized in `Λ`. A D1 state is therefore `θ`-invariant, and `U_θ=(∏κ_z)²` on `H(κ)`. Add this line (edit E6). The rest was re-derived: decomposition into `Δn`-homogeneous parts commutes with `Ad ω_z`, because `N_s(Λ)` commutes with `ω_z`; orbit representatives give `1⊗W`; the countable-range argument of `LZ1.md` Theorem 2.2 applies verbatim. |
| 30 | Scope remark and GAP (78) | CORRECT | The gap is real (§2, G2). |
| 31 | Theorem 6, statement (80-84) | CORRECT | |
| 32 | Theorem 6, proof (86) | CORRECT | Re-derived: `Σ_s|s⟩⟨∅|_x⊗⟨s|` is the invariant pairing of `S_+` with its dual. `−1` has end factors `(−1)(−1)`. `ω` has end factors `(−i)(+i)`. |
| 33 | Paragraph after Theorem 6 (88) | CORRECT | `RCS1.md` Theorem 4's proof reads "the product is matter parity by LZ1 §1", so its scope is LZ1's laws. Line 88 says "do not extend unchanged", which is exact. Norm closure: evenness is a closed condition, and local invariant elements are dense in `𝔄^G`. |
| 34 | §4 setup paragraph (92) | ERROR | "`N_{ij}=∂_i b_j(K₀)`" together with "`|∇a·n|<|Nn|`" and "`\widehat{Nn}`" (line 98). The derivative of `b` along `n` is `N^T n`, not `Nn`, so the tilt condition as written is a different condition. Fix: set `N_{ij}=∂_j b_i(K₀)`, or write `N^T n` throughout. `χ=sign det N` is unchanged. Draft Definition 4.3 has the same slip (edit E7). |
| 35 | Theorem 7, statement (94) | CORRECT | |
| 36 | Theorem 7, proof, first paragraph (96) | CORRECT | Re-derived: `d tr θ³=−tr θ⁴=0`; `∂_tγ_t=dα_t` gives `ω₃|_C=dβ`; the shell integrals form a Cauchy family. |
| 37 | Theorem 7, proof, Weyl point (98-102) | CORRECT | With item 34's fix. Re-derived: `g^{-1}=1+(λ̄−1)P`; `PA=(1−λ̄)PdP`; `PdPP=0`; `tr(PdPdP)=(i/2)dA`; `∫₀¹|1−e^{2πit}|²2πi dt=4πi`; `c₁=−1` for the identity map of `S²`. `b(K₀+εn)/ε→N^Tn` in `C^∞(S²)` gives the `C¹` limit. The identity `∫_{S²}σ^*β=∫_{[0,1]×S²}(Φ∘(id×σ))^*ω₃` holds because `γ_t` pulls back to zero on `S²` for degree reasons. |
| 38 | Check and literature paragraph (104) | CORRECT | The sign in `Σχ=−W₃` does not matter for any use in the file: every use has `W₃=0`. |
| 39 | Theorem 8, statement (106) | CORRECT | |
| 40 | Theorem 8, proof (108) | CORRECT | With `α(A)=U^*AU`, the one-site implementer is the normalized `U` or its adjoint, depending on convention. That changes `W₃` and every `χ` by one common sign only. |
| 41 | Theorem 9, statement (110) | CORRECT | Conditional on its added hypothesis. RC-W (§3) removes the hypothesis. |
| 42 | Theorem 9, proof (112) | CORRECT | Schur step: by Burnside, `ρ_σ` spans `End(S_σ)`, so the commutant of `1⊗ρ_σ` on `ℓ²(Z³)⊗S_σ` is `B(ℓ²)⊗1`. |
| 43 | GAP in draft Theorem H (114) | CORRECT | The gap is real (§2, G3). It is closed by RC-W. After RC-W, the sentence "Theorems H and 4.5 under NN-a alone and the claimed universal mirror conclusion remain open" is out of date (edit E8). The remarks on condition E and #10038 stand. |
| 44 | Theorem 10, statement (118) | CORRECT | |
| 45 | Theorem 10, proof (120) | CORRECT | `TM1.md` Definition 3: "a finite-spectrum self-adjoint even site observable `a_x`, with `β_g(a_x)=a_{gx}`". The proofs of TM1 Theorems 1-5 use only Definitions 3-6, stationarity, the lifts and the geometry of the tilings. |
| 46 | Theorem 11, statement (122) | INCOMPLETE | "More generally the later marginal is the distribution of `R_x`" holds only when the record forms with probability 1. Otherwise the marginal is a mixture. In TM1's setting formation is never random: TM1 Theorem 1 says "formation at a fixed site and tick has probability zero or one". Cite that and the sentence becomes exact (edit E9). |
| 47 | Theorem 11, proof (124) | CORRECT | |
| 48 | GAP on recorded values (126) | CORRECT | The gap is real (§2, G4). The example is valid. TM1 says the same after its Theorem 1: "Content can nevertheless be random." The Cauchy-Schwarz step was re-derived. |
| 49 | Theorem 12, statement (128) | CORRECT | Its link-purity hypothesis is superfluous (RC-Z). |
| 50 | Theorem 12, proof (130) | CORRECT | `ZM1.md` line 53: "a unital injective graded *-homomorphism". `spec Φ(a)⊆spec a` follows because `Φ` maps inverses to inverses. |
| 51 | GAP and scope paragraph (132) | CORRECT | Its first sentence is true of the draft. The omission it reports is harmless (RC-Z), so the GAP label should go (edit E10). The rest is correct: −1 acts as `+1` on both the trivial and the vector representation while `ω` acts as `1` and `−1`; the singleton scope matches `TOE_ASSEMBLY.md` 243; the scope of Theorem 3 is stated correctly; the Lemma ER citation matches `TOE_ASSEMBLY.md` 245. |
| 52 | §6, prior evidence (136) | CORRECT | |
| 53 | Literature paragraph (138) | CORRECT | The draft's §1 table names "Lemma W (section 4.6)", "Proposition 4.6.1" and "Lemma U (section 4.6)". Its §4 ends at 4.5 (draft lines 281-293). |

## 2. The distiller's GAPs: real or not, with repairs

**G1. One moving gate is not a covariant moving law (line 58; line 9).** Real. The draft's §3.5 ends: "SC-min with Proposition 3.5's register is, as far as the search found, the repository's first site-count rule in LW1 form with gauge-invariant motion." The draft never builds such a rule. Theorem 3 builds one gate. *Repaired statement:* "Theorem 3 gives an even, gauge-invariant gate on `R` that moves a site. Whether a finite-depth NN-a law on `R`, covariant under the whole cell group, moves sites is open (CML, §6)." One route, not worked here: `TM1.md` Definition 1 says "`G=2Z^3 ⋊ O_{c_0}` preserves both tilings". So a product `M_oM_e` of cube unitaries, each gauge invariant and covariant under its cube's stabilizer, would be cell covariant and gauge invariant, as in LW1's base tick. Two steps are missing: cell-group lifts on `R` that are compatible with reversing a link, and a decomposition of the cube unitary into NN-a gates. The second sentence of line 58 is correct, and Theorem 3 already uses only the complete update.

**G2. Flat bands are not tick-fixed (line 78; line 9).** Real. The draft's §5.2 reads: "In a D1 state the centre pattern of a defect is tick-fixed (Theorem 4.2(ii)). It belongs to the static class that owner decision LZ1-SC separates". `Ũ` preserves each `H(κ)`, but on `H_nt` it acts as `1⊗W`, and `W` need not be 1. *Repaired statement:* "In Theorem 5's settings each centre pattern is tick-invariant. The tick-fixed part of `H_nt` is `L²(T³;ker(W−1))`, and only it lies in LZ1-SC's static class. A band with a node is identically 1 on a connected neighbourhood of the node. Over that neighbourhood its image is tick-fixed."

**G3. The winding proof assumes periodic layers (line 114; line 9).** Real. Draft Theorem H's proof reads: "Choose `A_g` on one gate per cell-group orbit and transport it by the lifts". This presupposes that each layer is a periodic family. NN-a requires covariance of the complete update only (`TOE_ASSEMBLY.md` 235). The intermediate unitaries `V(t)` then need not commute with translations and need not have a Bloch matrix. *Closed by RC-W (§3.1).* `W₃[V]=0` for every translation-covariant unitary on `ℓ²(Z³)⊗C^n` that is a finite product of block-diagonal unitaries with uniformly bounded blocks. No layer needs to be covariant. *Repaired statement:* Theorem 9 holds without its added first sentence. So do draft Theorems H and 4.5 in setting F under condition E.

**G4. A record's value need not be deterministic (line 126; line 9).** Real. Draft Proposition 5.3 assumes "`x` records the value `v`" and concludes `ω′∘α^n(Π_x(v))=1`. That is valid only when the recorded value is almost surely `v`. Draft Corollary 5.3.1 then concludes: "every point outside a bounded neighbourhood of `supp O` has sharp, constant occupation from tick 1 on." The word "sharp" is refuted by line 126's own example with `O=1`. Take the identity tick and `ω=½⊗_x|∅⟩⟨∅|+½⊗_x(o_x/16)` under SC-odd. This state is stationary and cell-symmetric, every `D_xy` has expectation 0, so every site records at tick 1 (TM1 Theorem 4). Yet `ω(o_x)=½`. *Repaired corollary (RC-T, §3.3):* the points outside a bounded set `B` record at tick 1 in `ω′`, and under L-point their realized values are constant from tick 1 on, almost surely and at all such points at once. Sharpness and a bounded defect relative to a background need further input, as line 126 says.

**G5a. "The coarse-centre argument needs link-purity" (line 9; line 132).** Not real as a need. The draft's proof does use link-purity ("links inside the block contribute a scalar by link-purity"). The conclusion holds without it (RC-Z, §3.2). *Repaired statement:* delete the link hypothesis from Theorem 12.

**G5b. Scalar `ω` end factors do not follow from end-purity (line 132).** Real, and the counterexample is valid. The draft's Proposition 5.4 ends: "So the coarse law cannot be of class SC-odd with end-pure coarse links." That is false. On the trivial-plus-vector register, `−1` acts as `+1` on both summands, so the register is end-pure, while `ω` acts as `1` and `−1`. A coarse SC-odd point with one such link end already has the centre spectrum `{1,i}·{1,−1}=μ₄`. *Repaired statement:* "Under (G1) with `|S_u|≥3`, the incident coarse end factors of `ω` at `u` are not all scalar." This is a condition on the coarse links, not an obstruction.

## 3. Referee closures

### 3.1 RC-W: finite-depth walks wind trivially without covariant layers

**Setting.** `H=ℓ²(Z³)⊗C^n`, where `β∈Z³` labels cells. For the one-site walk, `n=8·dim F`. `B_a` multiplies by `β_a`. For a bounded `Y` of finite propagation, put `δ_a Y=[B_a,Y]`, the operator with entries `(β_a−γ_a)Y(β,γ)`. Then `δ_a` is a derivation and `δ_aδ_b=δ_bδ_a`. Let `1_L` be the projection onto a cube `Λ_L` of `L³` cells.

**Lemma RC-W.** Let `V` be unitary on `H`, commuting with the cell translations, and equal to `L_m⋯L_1`. Each `L_k` is block-diagonal for some partition into blocks, each lying in at most `D` adjacent cells. No `L_k` need commute with translations. Then `W₃[V]=0`.

*Proof.* (1) *Two trace facts.* For finite-propagation `Y`, `Tr(1_Lδ_aY)=0`: since `B_a` commutes with `1_L`, `1_L(δ_aY)1_L=[1_LB_a1_L,1_LY1_L]`, a commutator of finite matrices. For `X,Y` of propagation at most `R`, `Tr(1_L[X,Y])=Tr([1_L,X]Y)` by cyclicity with the finite-rank `1_L`. `[1_L,X]` vanishes except between cells within `R` of the boundary of `Λ_L`, so its rank is at most `C_{R,n}L²`. Hence `|Tr(1_L[X,Y])|≤2C_{R,n}L²‖X‖‖Y‖`.

(2) *A path.* In each block choose a Hermitian logarithm with spectrum in `(−π,π]`: `L_k=e^{iA_k}`, `‖A_k‖≤π`. Put `V(t)=e^{itA_m}⋯e^{itA_1}`, so `V(0)=1` and `V(1)=V`. Put `θ_a=V^*δ_aV`, `η=V^*V'` and `Ω=ε_{abc}θ_aθ_bθ_c`, summed. Every `V(t)` has propagation at most `mD`. On each block, `‖[B_a−c,e^{itA_{k}}]‖≤D` for a suitable constant `c`. So `θ_a`, `η` and `δ_aη` are bounded uniformly in `t`, with propagation at most `2mD`.

(3) *Variation identity.* `(V^*)'=−ηV^*` gives `θ_a'=δ_aη+[θ_a,η]`. Also `δ_a(V^*)=−V^*(δ_aV)V^*` gives `δ_aθ_b−δ_bθ_a=−[θ_a,θ_b]`. Antisymmetrizing, `ε_{abc}(δ_cθ_a)θ_b=−Ω` and `ε_{abc}θ_a(δ_cθ_b)=Ω`, so `ε_{abc}δ_c(θ_aθ_b)=0`. Substitute `θ'`. Collect the `[θ,η]` terms into `[Ω,η]`. Move each `δη` factor to the right by commutators and relabel cyclically. This gives the exact identity
\[
Ω'=[Ω,η]+ε_{abc}\big([δ_aη,θ_bθ_c]+[θ_aδ_bη,θ_c]\big)+3ε_{abc}δ_c(θ_aθ_bη).
\]
`[check]` `check_rcw.py`: on random 24-dimensional matrices with diagonal commuting `B_a` and `V(t)=e^{itA}e^{itB}`, the two sides agree to `3·10^{-7}` (finite differences), against entries of size 34.

(4) *Box traces.* Put `f_L(t)=L^{-3}Tr(1_LΩ(V(t)))`. This is a finite sum of smooth matrix entries. By (1) and (3), `|f_L'(t)|≤C/L`, with `C` independent of `t` and `L`. Since `f_L(0)=0`, `|f_L(1)|≤C/L`.

(5) *The periodic end point.* `V` commutes with translations, and translations shift `B_a` by constants. So `Ω(V)` commutes with translations, and `f_L(1)=τ(Ω(V))` for every `L`, where `τ(Y)=Tr(1_{cell 0}Y)`. Letting `L→∞` gives `τ(Ω(V))=0`.

(6) *Bloch form.* Fourier transform in `β` takes `V` to the trigonometric polynomial `V(K)` and `δ_a` to `±i∂_{K_a}`. It also gives `τ(Y)=(2π)^{-3}∫_{T³}tr Y(K)d³K`. Hence `τ(Ω(V))=(±i)³(2π)^{-3}·24π²·W₃[V]`. The factor is nonzero, so `W₃[V]=0`. □

**Use.** The one-site walk of Theorem 8 is a product of layers `⊕_g u_g`, with blocks `E₁(supp g)` in at most two adjacent cells. Each `u_g` preserves content parity, and under gatewise symmetry it preserves the isotypic multiplicity spaces. So Lemma RC-W applies to `V`, to each `V_σ` and, when gates commute with `G`, to each `V_ρ`. Theorem 9 therefore holds with its first sentence deleted. The proof uses finite matrices, Fourier series of trigonometric polynomials and one-variable calculus, so it is Lean-formalizable. It follows the standard argument that the odd Chern character varies by exact terms. The trace per unit volume replaces the integral, as in the noncommutative index theory of Bellissard and of Prodan and Schulz-Baldes. This is credited from memory and is not load-bearing.

### 3.2 RC-Z: Theorem 12 needs no link hypothesis

**Statement.** Under SC-odd with Spin(10), let a unital *-homomorphism `Φ` satisfy (G1) for `S_u`, with `|S_u|≥3`. Fine link registers are finite, with commuting endpoint actions. Then `cμ₄⊆spec ω_u^{(1)}` for some `c∈U(1)`.

*Proof.* `Φ(ω_u^{(1)})=∏_{x∈S_u}ω_x`, as on line 130. This product is `M⊗Λ`, where `M=∏_xω_x^{mat}=i^{N_s(S_u)}` acts on the matter of `S_u` (Theorem 2). `Λ` is the product of all end factors of `ω` at points of `S_u`, on the finite tensor product of the link registers incident to `S_u`. These factors commute, since they sit on distinct links or are commuting end actions of one link. `Λ` is unitary in finite dimension, so it has an eigenvalue `c`. `N_s(S_u)` takes the values `0,1,2,3`, so `spec(M⊗Λ)⊇cμ₄`. Finally `spec Φ(a)⊆spec a`. □ The proof uses neither internal nor boundary link-purity. For the singleton sets of ZM1-I1[a] the same argument gives only `c{1,i}`, which every coarse SC-odd point has.

### 3.3 RC-T: the corrected record corollary

**Statement.** Let `ω` be stationary, symmetric as in TM1 Theorem 4, and in case (E), with a tick of finite range `r`. Let `O` be local with `ω(O^*O)>0`, and put `ω′=ω(O^*·O)/ω(O^*O)`. Let `B` be the set of points within `r+1` of `supp O`. Then: (i) every `x∉B` lies in `F_1(ω′)`, so `t_x=1`; (ii) every history measure with the Born marginals of `ω′∘α^n` that obeys L-point has `ξ_{2n}(x)=ξ_2(x)` for all `n≥1` and all `x∉B`, almost surely; (iii) the law of `ξ_2(x)` is the Born law of `ω′∘α` at `x`, which need not be a point mass.

*Proof.* (i) Case (E) and stationarity give a pair `y,z` with `ω(α(D))=0` for `D=D_xy+D_xz`. `D` is a sum of two projections, so `0≤D` and `α(D)²≤2α(D)`. For `x∉B`, `α(D)` is even and has support disjoint from `O`, so it commutes with `O`. Then `|ω(O^*Oα(D))|²≤ω((O^*O)²)·2ω(α(D))=0`. (ii) L-point at each point, and a countable intersection of sure events. (iii) Born marginals; G4's example with `O=1`. □

### 3.4 RC-C: the mod-4 counterexample under the odd rule

#10038 A7/C0 (line 80 at `5adea19dc2`) reads: "A Spin(10)-equivariant map from Ns to Ns + dn sites must preserve z, so under the odd rule it needs dn = 0 mod 4". Under SC-odd, let a link `ℓ=(x,y)` carry `R=Cr₀⊕S_−`, with `Spin(10)_x` acting on `S_−` and the `y` end trivial. Put `B=Σ_{t∈B_−}(|t⟩⟨∅|)_x⊗|r₀⟩⟨t|`. Then `B≠0` is local, gauge invariant, fermion odd, and has `Δn=+1`. *Proof.* The sum over `t` pairs `S_−` with its dual. The `y` end acts trivially. The matter factor creates odd content from the even `|∅⟩`. As a check, the global centre gives the factor `i` on matter and `−i` on the link. □ So the mod-4 rule fails with links even under the odd rule. `R` is not link-pure, so `B` is consistent with line 88. It also shows that line 88 needs link-purity and not only SC-odd: without link-purity, gauge-invariant odd local operators exist even under SC-odd.

## 4. Decisions on the points the lane brief names

### 4.1 Flatness of odd defect bands with gauge links in D1 states

**Decision: Theorem 5 is correct as stated, in both cases.** Item 29 asks for one missing line (`U_θ`). Two of its hypotheses are needed for the proof as written. Theorem 6 is an odd gauge-invariant local operator under SC-min, so case (a) needs SC-odd. RC-C is one under SC-odd on a register that is not link-pure, so case (a) also needs link-purity. Neither example shows a propagating odd band. Each shows only that the pattern argument fails. Flatness outside (a) and (b) is not decided here (FLAT-ext, §6). The result covers every D1 state, not only VC1. It concerns finite-fibre bands under the proposed reading R-loc, as line 78 says.

### 4.2 The free-reading mirror-pairing theorem

**Decision: correct, and stronger than the distillation states.** Theorem 7 (the Floquet Nielsen-Ninomiya index formula) is correct after the notation fix of item 34. Theorem 8 is correct. Theorem 9 is correct as a conditional theorem. **The distiller's GAP is real.** The draft's homotopy needs periodic layers, and NN-a requires "Gauge invariance and cell covariance ... of the complete update only". **RC-W repairs the gap.** `W₃=0` for every translation-covariant finite product of block-diagonal unitaries with bounded blocks. So, in setting F under condition E, draft Theorems H and 4.5 hold under NN-a. Fix a content parity `σ` and a quasienergy at which the node set of `W_σ` is finite and consists of Weyl points. Then the net chirality there is zero. In particular, no quasienergy has a single Weyl node of `W_σ` as its whole node set. The theorem leaves three things open: gates that violate E, defects over a filled or entangled background, and node sets that are infinite or not all Weyl. Setting F has no links. It is the auxiliary reading, not the class itself.

### 4.3 The two counterexamples

**Decision: both stand.** (1) Theorem 6 is valid. It refutes the extension of `RCS1.md` Theorem 4 and of LZ1's parity identity to SC-min. It does not refute RCS1 Theorem 4 on its own laws, and line 88 says exactly this. (2) Theorem 4's link example is valid against the even-operator mod-4 rule once links are allowed. #10038 A7/C0 states its rule under the odd rule. RC-C gives the matching counterexample there: a gauge-invariant odd operator with `Δn=1` under SC-odd.

### 4.4 TM1: the record conflict and the GAP on recorded values

**Decision: the GAP is real, and the conflict survives in corrected form.** Permanence fixes the realized value sample by sample. It does not make the value deterministic. TM1 itself says "Content can nevertheless be random." The draft's "sharp, constant occupation" is false: take G4's example with `O=1`. RC-T is the corrected corollary. In a case-(E) background, every L-point history of `ω′` changes occupation only inside a bounded set `B` after tick 1. This needs no sharpness. Turning it into "a defect relative to the background stays bounded" needs a coupling or sharp background values, as line 126 says. Theorem 11 needs the citation of TM1 Theorem 1 (item 46). The L-site paragraph is correct, and it no longer claims that site names are necessary.

### 4.5 ZM1: link-purity in the coarse-centre argument

**Decision: link-purity is not needed.** RC-Z proves Theorem 12 without any link hypothesis. The distiller's second correction is real: end-purity for `−1` does not make the `ω` end factors scalar (trivial plus vector). So the draft's "cannot be of class SC-odd with end-pure coarse links" is false. The correct consequence is a condition on the coarse links. The result does not touch the singleton embedding of ZM1-I1[a].

### 4.6 Are SC-min and SC-odd four-tested correctly?

The tests: a text fails if it (1) states or fixes a part's target, (2) is open-ended so that a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need.

| Rule | Draft | Referee | Reason for any change |
|---|---|---|---|
| SC-min | P P P C | P P P P | Test 4 asks about excess. SC-min adds one even line per point, and its reason, a change of site count, needs exactly that. A frame that fixes `|∅⟩` is the smallest choice. The draft's C cites Theorem 3: motion needs end-mixed registers. That is a fact about which registers realize the reason, not structure added beyond need. Test 2 passes relative to PS-6r: the register class is as open as PS-6r, and that openness belongs to GA1-P-5. |
| SC-odd | F P F C | F P F P | Tests 1 and 3 fail, as the draft says. Its quoted reason (#10038 A5) is that defect spinors become fermions, which fixes CG1(e)'s spinor-rather-than-vector clause for fermions by rule. Theorem 2 on `V⁻` then settles every fermion's centre class by premise. Test 4: removing `S_+` is not added structure. The draft's reason under test 4, "against PS-5's `M_32(C)`", is real but belongs elsewhere. SC-odd changes PS-5 at every present site, under either reading (`End(S_−)=M_16(C)` under R-site, `M_17(C)` per point under R-point). Record this as a premise change for the owner, not as a test-4 result. |

The overall outcome is the draft's: SC-min passes, and SC-odd fails tests 1 and 3. These are referee proposals. The owner decides.

## 5. Required edits to `CG16S.md`

- **E1** (line 7). Add to "Proved below": Theorem 4 with its link counterexample, Theorem 8, Theorem 9 and Theorem 11.
- **E2** (line 21; uses at 9, 72, 76, 84, 86, 88, 128, 132). Rename line 21's condition, for example "ω-pure". State that it is `LW1_5.md` link-purity (line 52) together with the scalar lift of `−I_20` (line 208). One word, one meaning.
- **E3** (line 24). Define spinor and tensor class by the eigenvalue of `Ad ω_x^{mat}` at a point `x`, as in draft Corollary 3.3.
- **E4** (line 64). Say that #10038 A7/C0 is stated under the odd rule. Add RC-C (§3.4) as the counterexample in that setting.
- **E5** (line 66). After the draft's ratings, add the referee's: SC-min P P P P and SC-odd F P F P, with §4.6's reasons. Record separately that SC-odd changes PS-5. Adopt neither.
- **E6** (line 76). Add: under SC-odd, `θ=(∏_{z∈Λ}Ad ω_z)²` on operators localized in `Λ`. So a D1 state is `θ`-invariant, and `U_θ=(∏κ_z)²` on `H(κ)`.
- **E7** (lines 92, 98). Use `N_{ij}=∂_j b_i(K₀)`, or write `N^T n` wherever `Nn` appears.
- **E8** (lines 9, 11, 110, 112, 114). Insert RC-W with its proof. Delete Theorem 9's first sentence. Replace "Theorems H and 4.5 under NN-a alone and the claimed universal mirror conclusion remain open" with §4.2's statement and scope. Remove "the free-walk winding question under NN-a" from the open list.
- **E9** (line 122). Cite TM1 Theorem 1, "formation at a fixed site and tick has probability zero or one". Then "the later marginal is the distribution of `R_x`" holds whenever the record forms.
- **E10** (lines 9, 128, 132). Replace "needs link-purity" with RC-Z. State Theorem 12 without a link hypothesis. Keep the trivial-plus-vector counterexample and the corrected consequence of G5b.
- **E11** (line 126). Add RC-T as the corrected form of draft Corollary 5.3.1. Note that `O=1` in the example refutes "sharp".
- **E12** (line 11). Replace the open list with §6's.

## 6. Open statements to carry, by name

Inherited and unchanged: CG1-i; CG1-ii; MT1-i; MT1-ii; MT1-S[R-CS^str]; R-CS^str; VC1, including whether its vacuum is a D1 state; LZ1-i and R-SC; TM1-i and the point-register form of PS-3h5; ZM1-I1[a]; GA1-P-5. For the owner: adoption of SC-min or SC-odd; R-site or R-point; L-point or L-site; the PS-5 change that SC-odd makes. Open within this item:
- **CML.** Is there a finite-depth NN-a law on Theorem 3's register, covariant under the whole cell group and gauge invariant, that moves sites? (G1; one route in §2.)
- **SING-P.** Does Theorem 6's gauge-invariant odd singlet propagate under some SC-min law?
- **FLAT-ext.** Are odd bands flat under SC-min, or under SC-odd with registers that are not ω-pure? The pattern argument fails there (Theorem 6, RC-C).
- **F-ext.** The free-reading pairing without condition E, or over a filled or entangled background.

No item here stops at a three-attack lemma. Each is open because no attack was run in this pass.

## 7. Freeze recommendation

**Freeze after edits E1-E12.** No theorem of `CG16S.md` is false in content. The three ERRORs are a term used with two meanings, one transposed matrix in a hypothesis, and one false claim that a hypothesis is needed. The six INCOMPLETEs are one-line additions. RC-W strengthens the free-reading result, from conditional on periodic layers to unconditional under NN-a with condition E. RC-Z removes a hypothesis. RC-T and RC-C sharpen two scope statements. The four closures come from this one check and should be read as such: the lead should verify RC-W step (3) and step (6) before freezing. No independent second review was run.

## Prior work used

| Prior result | Path | How used |
|---|---|---|
| The CG16S digest | `prior/CG16S.md` (this folder), lines 1-81 | Read first and in full. It set the scope of the source check. |
| Local centre patterns, D1 states, flat nodes (Theorems 2.1-2.2), FROZEN | `LZ1.md` §1 and §2 | Checked Theorem 5 against them, including the countable-range argument. |
| "Every `A∈𝔄^G` is matter-even" (Theorem 4), FROZEN | `RCS1.md` line 64 | Scope of the counterexample of Theorem 6 (§4.3). |
| Definitions 1-8; Theorem 1 ("formation ... has probability zero or one"; "Content can nevertheless be random"); Theorem 4 (case E), FROZEN | `TM1.md` lines 20-62 | Items 45-48, G4, RC-T. |
| Definition Z ("a unital injective graded *-homomorphism") and (G1) | `ZM1.md` lines 53, 71 | Items 49-51, RC-Z. |
| End-pure and link-pure (line 52); the scalar lift of `−I_20` (line 208); Σ and S1-S4 (lines 204-212), FROZEN | `LW1_5.md` | Item 8 (term clash), item 20 (`S_+` is end-pure). |
| NN-a and ZM1-I1[a], owner decisions | `TOE_ASSEMBLY.md` lines 235, 243 | G3 is real; singleton scope. |
| #10038 A2-A4 and A7/C0 | `origin/claude/toe-site-count-matter-20261021:docs/A_SITE_COUNT_CHANGE_BY_ONE_CARRIES_THE_SPIN10_SPINOR_SO_UNDER_THE_ODD_SITE_RULE_EVERY_FERMION_IS_A_MOBILE_SITE_DEFECT_WHILE_ITS_CONES_STAY_VECTOR_LIKE_BOUNDED_THEOREM_NOTE_2026-10-22.md`, lines 62-84, at `5adea19dc2` | Items 18 and 24, RC-C. |

**Prior work the digest missed.** (1) `TOE_ASSEMBLY.md` §3.7, line 235 (NN-a). Its last sentence makes G3 a real gap. (2) `LW1_5.md` lines 52 and 208, which define "link-pure" and its strengthening (E2). (3) `TM1.md` Theorem 1 and the remark after it, which already say that record content can be random (G4). (4) #10038 A7/C0 is stated "under the odd rule" (line 80 at `5adea19dc2`); the digest quotes only the consolidation. The draft had already added `LZ1.md` Theorems 2.1-2.2.

**Credits, not load-bearing.** RC-W follows the standard fact that the odd Chern character varies by exact terms. Replacing the integral by a trace per unit volume follows the noncommutative index theory of J. Bellissard and of E. Prodan and H. Schulz-Baldes. The one-dimensional analogue is the walk index of Gross, Nesme, Vogts and Werner (arXiv:0910.3675, as listed in the draft). These are credited from memory and were not re-read.

## FINISH

**Proved here (referee closures; one check, for the lead to verify).**
- RC-W. A unitary on `ℓ²(Z³)⊗C^n` that commutes with the cell translations and is a finite product of block-diagonal unitaries with bounded blocks has `W₃=0`. No layer needs to be covariant. So Theorem 9 holds without its added hypothesis, and so do draft Theorems H and 4.5, in setting F under NN-a and condition E.
- RC-Z. Theorem 12 holds with no link hypothesis.
- RC-T. In a case-(E) background, every L-point history of a local excitation changes occupation only inside a bounded set after tick 1. Sharpness is not claimed.
- Verdicts: Theorems 1-12 are correct in content. Theorem 7 needs the `N^T` fix (E7), Theorem 11 a citation (E9), and Theorem 5 a one-line addition (E6).

**Counterexamples.**
- RC-C. Under SC-odd, a link register `Cr₀⊕S_−` carries a gauge-invariant, fermion-odd, local operator with `Δn=1`. This refutes #10038 A7/C0's mod-4 rule once links are allowed, under the odd rule itself. It also shows that "invariant local operators are even" needs link-purity as well as SC-odd.
- Confirmed: Theorem 6 (an odd invariant singlet under SC-min); Theorem 4's link example; G4's random-content example (refutes "sharp"); G5b's trivial-plus-vector register (refutes "cannot be SC-odd with end-pure coarse links").

**Open by name.** CML; SING-P; FLAT-ext; F-ext. Inherited: CG1-i, CG1-ii, MT1-i, MT1-ii, MT1-S[R-CS^str], R-CS^str, VC1, LZ1-i, R-SC, TM1-i, PS-3h5 in point-register form, ZM1-I1[a], GA1-P-5. For the owner: SC-min or SC-odd, R-site or R-point, L-point or L-site, and the PS-5 change under SC-odd.

**What changes downstream.**
- CG1(e), route 1. In the free reading, the pairing of light 16 nodes no longer depends on periodic layers. It holds for every NN-a law of setting F under condition E. In the class itself, odd bands in D1 states are flat under Theorem 5's hypotheses (a) and (b).
- RCS1 and LZ1. For site-count laws, the parity identity needs both SC-odd and ω-purity (Theorem 6, RC-C).
- ZM1. The coarse-centre result constrains the coarse links at a coarse point. It neither obstructs end-pure coarse links nor needs fine link-purity.
- TM1. Under L-point, a case-(E) background confines all later occupation changes of a local excitation to a bounded set, history by history. A bounded defect relative to the background still needs a coupling.
- Four tests (referee proposal). SC-min passes all four. SC-odd fails tests 1 and 3 and changes PS-5.
- Freeze `CG16S.md` after E1-E12.
