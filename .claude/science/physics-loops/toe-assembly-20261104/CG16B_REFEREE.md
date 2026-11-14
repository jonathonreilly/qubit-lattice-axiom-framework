lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CG16-B referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 (referee) of part CG16-B under PR #10138's method. Claude drafted (`CG16B_DRAFT.md`, pass 1). Codex gpt-6.1-terra distilled (`CG16B.md`, pass 2). This session wrote neither. This is one check: one line-by-line read of `CG16B.md`. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status, adopts no law, reading or definition, and changes no axiom or working-set entry. Referee closures are written out in full; they are not themselves refereed. Nothing here is a verdict on the physics.

**Source revisions read.** Local checkout, branch `claude/toe-assembly`, commit `59d3886d9530bac9ae11dabf4b1ef034f3a6059a`. Branch `origin/docs/consolidate-gauge-matter-registers` at `7086189d10`, read with `git show` after `git fetch -q`, for four quoted lines only. Files and lines read are listed under "References consulted" below.

**Working-set entries used, by name.** PS-5 (five modes per site); PS-6 (frames are local) and PS-6r (finite link registers), through the class 𝓛; PS-1c (cell covariance), only in item 22 and §3.1; the owner reading GA1-P-NN = NN-a (`TOE_ASSEMBLY.md` §3.7), in §3.1; the owner's named working candidate R-CS^str with `χ_tot` over parity-sharp backgrounds (`TOE_ASSEMBLY.md` §3.6, not adopted), in §3.2-3.3.

**Method.** Every proof in `CG16B.md` was re-derived by hand. A `[check]` is a small scratch computation in `/tmp/toe-CG16Bref/` (under a minute, a few MB). It guides only and proves nothing. Verdicts: CORRECT; ERROR (a false or wrongly cited line, quoted, with a fix or a counterexample); INCOMPLETE (a named missing step). A "referee closure" is a short complete argument for a missing step, written out here. Owner guidance applied, verbatim: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms and working-set entries are read plainly. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged and was not edited. Nothing is adopted here.

**Text read.** `CG16B.md` as of commit `59d3886d9530bac9ae11dabf4b1ef034f3a6059a` (branch head `claude/toe-assembly`; the last commit touching it). SHA-256 of the file read: `bdccbc2e9d64c25c84af63e203df95855b7d7c64e2883ad3c5ae3017a1081f27`. 149 lines. Line numbers below refer to that file. The pass-1 draft `CG16B_DRAFT.md` (last changed at `d7d458a2a028`) has SHA-256 `3f46ee993ee3bfafb6ad64efa0c71d7081e7cf1fa7693380a119d17bfbb1ae9c`, equal to the hash `CG16B.md` line 13 records `[check: shasum]`.

**References consulted** (this folder at `59d3886d9`, unless a branch is named; read by line).
- `prior/CG16B.md`, all 86 lines (SHA-256 `c200625e3a2f96b5…`, equal to the prefix the draft records).
- `CG16B_DRAFT.md`, all 323 lines.
- `TOE_ASSEMBLY.md` (last changed `36d5dd136`; SHA-256 prefix `6fda41c203ac95b5`, equal to the draft's): lines 231-236 (section 3.7, NN-a, verbatim), with the section list at lines 71-239.
- `GA1_5.md` (last changed `913ef70a5`; SHA-256 prefix `2ba3527fbb3819f7`; the draft read an earlier version with prefix `c53418ca516e84a2`): lines 7, 11, 13, 52, 228-270 (Amendment 1, GAP (2), class GA1-P-5, Lemma U, Proposition C with proofs).
- `LW1_5.md` (last changed `727ad9884`; SHA-256 prefix `bdd5159f8585030b`, equal to the draft's): lines 1-60 (status, definitions, the two laws), 100-210 (C, M, S′, alternative A, section 5 with F, K, the one-ended construction, Theorem SC, Σ, the reducible-register repair), 266-280 (B1-U).
- `LW1_5X.md` (last changed `271c868a4`; SHA-256 prefix `328b0ec22b4b64d4`): lines 1-12 (status, open names). Not read by the draft.
- `LZ1.md` (last changed `7da1a4174`; SHA-256 prefix `ecd65ab7c6854ecf`, equal to the draft's): lines 30-66 (section 1 definitions, Theorems 2.1-2.2, Corollary 2.3).
- `RCS1.md` (last changed `8ca361b0c`; SHA-256 prefix `0b2addf9efb30ce3`, equal to the draft's): lines 8-18, 24-66, 82-128, 159-187, 207, 219.
- `MT1.md` (last changed `727ad9884`; SHA-256 prefix `c7be0ddbb9766747`, equal to the draft's): lines 89-97.
- `LW1.md` (last changed `4b65c608f`; SHA-256 prefix `78280bd620800eac`): lines 186-205 (Lemma A1, Lemma A1a, dressed factorization), 401-404 (Theorem E1).
- `TOE_ASSEMBLY.md`, further: lines 201-211 (section 3.4) and 221-229 (section 3.6).
- `LW1_REFEREE.md` lines 1-80 and `Y2W_DRAFT.md` lines 1-20, for format only.

---

## 1. Verdict table

Item numbers are used in sections 2-6. "Line" is the line of `CG16B.md`.

| # | Item (line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status summary (5) | CORRECT | "orthogonal to all nontrivial centre-pattern vectors" is true and is stronger than the displayed `H_phys⊥𝒮` of Theorem 4.1(a): every `U_x` fixes `H_phys`, so `H_phys⊂H(1)⊥H_nt`. See §2.3. |
| 2 | GAP: NN compilation (7) | CORRECT (gap real) | The draft's "NN-b, hence NN-a" (draft line 173) is unsupported: cube gates are not nearest-neighbour gates. Referee closure in §3.1: under NN-a both witnesses compile; GA1-5 Proposition C does not apply as stated, but its parallel-run step does. Replace the sentence "The witnesses establish existence in 𝓛, not existence of a nontrivial NN-a law" (edit E1). |
| 3 | GAP: charged-sector identification (9) | CORRECT (gap real) | Stronger: the extension is false for string limits over a background sharp in every `z_x`. Referee closure (negative) and repaired statement in §3.2. |
| 4 | §0 Open by name (11) | INCOMPLETE | Omits LW1-5-X-B_m and LW1-5-X-O, which bound the "outside the exceptional angles" scope of Corollary 2.3 (`LW1_5X.md` line 9). Omits the two referee findings of §3 (edits E2, E3). |
| 5 | §0 provenance (13) | CORRECT | Draft hash matches `[check: shasum]`. Context list omits `MT1.md`, `GA1_5.md`, which the text cites (cosmetic). |
| 6 | Definition 1 (17) | CORRECT | Matches `LW1_5.md` §1. |
| 7 | Definition 2 (18) | CORRECT | `ω=e^{iπΣ_j M^{2j-1,2j}}=e^{iπ(N-5/2)}=-iP`, using `n_j-1/2=M^{2j-1,2j}` (`LW1_5.md` §1). |
| 8 | Definition 3, class 𝓛 (19-21) | CORRECT | The scope sentences are accurate. |
| 9 | Definition 4, classes and purity (22) | CORRECT | Agrees with `LW1_5.md` inferred definition 7. |
| 10 | Definition 5, D1 and `H_phys` (23) | CORRECT | `LZ1.md` §1 with `c_z` replaced by `z_x`; the replacement is the definition the draft uses (draft §3.5). |
| 11 | Definition 6, bands (24) | CORRECT | Agrees with `LZ1.md` §1, except that `LZ1.md` asks `V` continuous on `T³`; add "continuous" (cosmetic). |
| 12 | Definition 7, target (T) (25) | CORRECT | See §2.3 on what (T) contains. |
| 13 | Definition 8, diagonal identification (26) | CORRECT | |
| 14 | Definition 9, charged sectors (27) | CORRECT | |
| 15 | Theorem 2.1 (31-33) | CORRECT | Re-derived: `γ_1γ_2=e^{-iπM^{12}}∈G`; the commutator is `γ_1γ_3γ_1γ_3=-1`; `λ` is a homomorphism into abelian `U(1)`, so continuity is not needed. |
| 16 | Theorem 2.2 (35-37) | CORRECT | (c) ports step 5 of `LW1_5.md`'s S′ proof; "cannot be all of it" holds because `dR=0` would make `R` trivial on connected `G`, against `R(-1)=-I` (the draft says this; the distillation compresses it). |
| 17 | Corollary 2.3 (39-41) | CORRECT | Can be strengthened: for `L5-U[1]`, `L5-U[9]` the gate-wise bound holds at every window angle (`LW1_5X.md` line 7); edit E4. |
| 18 | Carrier remark (43) | CORRECT | `E_{αi}E_{βj}=0` since `⟨i|β⟩=0`; the anticommutator is re-derived. |
| 19 | Theorem 2.4 (45-47) | CORRECT | |
| 20 | MT1 comparison (49) | CORRECT | See §2.1. |
| 21 | Theorem 3.1, membership and link-purity (53-65) | CORRECT | Both registers re-derived; `ρ_{ℓ,x}(-1)ρ_{ℓ,y}(-1)` is `-1` (A) and `(-1)^m` (rishon). |
| 22 | Theorem 3.1, cell covariance of the rishon tick (53, 65) | CORRECT | The B1-U transfer holds; see §2.2. |
| 23 | GAP (NN compilation) and symmetry remark (67) | CORRECT (gap real) | Closed under NN-a by §3.1. The `U(16)` remarks are accurate. |
| 24 | Theorem 4.1(a) (73) | CORRECT | Holds for every law in 𝓛, with or without (F); it uses no dynamics. See §2.3. |
| 25 | Theorem 4.1(b) (75) | CORRECT | The Haar average fixes `A∈𝔄^G` and is a contraction, so `‖E_n(A_n)-A‖≤‖A_n-A‖`. |
| 26 | Theorem 4.1(c) (77) | CORRECT | For `x∉Λ`, the link factors of `z_x` act on links outside the support of `A`, because a supported link puts both ends in `Λ`; the distillation states only the site half of this (cosmetic). |
| 27 | "target (T) has no instance in 𝓛; (a) alone" (79) | CORRECT | `H_phys∩𝒮={0}` and a band image is nonzero. The exclusion is definitional; see §2.3. |
| 28 | Proof of 4.1 (81-85) | CORRECT | `ŨU_xŨ^*=U_x` because both fix `Ω` and implement `Ad α(z_x)=Ad z_x`. |
| 29 | Credit paragraph (87) | CORRECT | `RCS1.md` line 8 credits Theorem 4's evenness to `MT1.md`, as stated. |
| 30 | Theorem 4.2, Example O (89-91) | CORRECT | Re-derived: `Y∈𝔄^G`, odd, nonzero; `τ(Y^*Y)>0` by faithfulness of the trace. The draft's stronger remark (the trace is D1 for every update in 𝓛 on these registers that commutes with even translations) is also true. |
| 31 | Theorem 5.1, SC′ (95-97) | CORRECT | The one changed step of `LW1_5.md` SC(b) ("site factor of `z_x` is a scalar") is correctly replaced by "even"; SC(a) is replaced by Theorem 2.1, which needs no gate-wise invariance. |
| 32 | Paragraph after SC′ (99) | CORRECT | Re-derived: the hop flips `P_x` and `p_{ℓ,x}` together, so `-P_x(-1)^{p_{ℓ,x}}` is fixed; likewise at `y`. |
| 33 | NN-a and PS-6 paragraph (101) | CORRECT | `α(𝒢)=𝒢` gives `α(e^{it𝒢})=e^{it𝒢}=Z_x(e^{itM^{ab}})`, and these generate `Γ_x(G)`. |
| 34 | Theorem 6.1: centrality, conservation, Gauss identity (105-110) | CORRECT | Centrality and conservation need neither (F) nor link-purity. |
| 35 | Theorem 6.1: equality for finitely localized factor sectors (111, 113) | CORRECT | Port of `RCS1.md` Theorem 3 checked: for `z∉Λ̂`, `z_z∈𝔄^G_{Λ^c}`; for `Λ'⊇Λ̂`, `F_{∂Λ'}∈𝔄^G_{Λ^c}`; dividing the two Gauss identities leaves `χ`. |
| 36 | Theorem 6.1: translation clause (111) | INCOMPLETE | `π∘τ_β` needs `τ_β` to act on `𝔄^G`: add the hypothesis of Definition 5, `τ_β(z_x)=z_{x+2β}` with translation-covariant registers (edit E5). |
| 37 | Theorem 6.1: Corollary 9 clause (111, 113) | CORRECT | `RCS1.md` lines 125-127: the proof uses Theorem 5 and the transverse grouping only. |
| 38 | Theorem 6.2, finite strings (115-118) | CORRECT | Re-derived site by site, including the two end-parity signs at each interior site. |
| 39 | GAP: limits (120) | CORRECT (gap real) | Referee closure (negative) in §3.2: over any D1 background sharp in every `z_x`, string limits keep the background centre value at every site. |
| 40 | Theorem 6.3 (122-124) | CORRECT | `Ad(S_+(ω)⊕1)` multiplies `Hom(H_-,H_+)` by `-i` and the reverse block by `+i`. |
| 41 | Route paragraph (126) | CORRECT | |
| 42 | §7 preamble (130) | CORRECT | |
| 43 | §7 rows 𝓛, (F) as hypothesis, classes, diagonal identification (134-136, 138) | CORRECT | |
| 44 | §7 row target (T) (137) | CORRECT | Test 1 reads "states a part's target" literally; (T) is the lane's question, stated in order to be refuted, so nothing is smuggled. Say so (cosmetic). |
| 45 | §7 rows (F) as law data, rishon witness, alternative A (139-141) | CORRECT | "NN compilation is open" in the rishon row is superseded by §3.1. |
| 46 | §7 row R-16^str (142) | INCOMPLETE | The reading's text is not stated. The draft's text returns relative class `+1` on every string limit over a background sharp in every `z_x` (§3.2), so test 2 fails for that wording. Repair and tests in §3.3 (edit E3). |
| 47 | §7 row PS-6-all (143) | CORRECT | |
| 48 | Paragraph after the table (145) | CORRECT | |
| 49 | §8 review boundary (149) | CORRECT | |

**Counts.** 49 items: 46 CORRECT (three of them distiller GAPs judged real), 0 ERROR, 3 INCOMPLETE. No ERROR or INCOMPLETE item changes a proved theorem. Two referee closures change the status text: one positive (§3.1), one negative (§3.2).

`[check]` `/tmp/toe-CG16Bref/check.py` (output `out.txt`, under 2 s, 32×32 matrices): `P=(-i)^5γ_1⋯γ_10`, `n_j-1/2=M^{2j-1,2j}`, `ω=-iP`, the commutator `-1`, `γ_1γ_2=e^{-iπM^{12}}`, tracelessness of the 45 generators on `H_+` (so `det S_+(g)=1`), and the `E` anticommutator all hold. This guides only.

---

## 2. Notes on checked items

### 2.1 Sections 2-3 (items 15-23)

Theorem 2.1 needs no continuity of `λ`: any homomorphism into the abelian group `U(1)` kills commutators. Theorem 2.2(c) needs `R` continuous. The distillation states this; `R(g)_{bc}=32^{-1}tr(γ_b Ad u(g)(γ_c))` supplies it. Line 49 quotes `MT1.md` correctly. `MT1.md` line 89: "Their Fock lifts satisfy `Γ_F(u_1)Γ_F(u_2)=(-1)^NΓ_F(u_2)Γ_F(u_1)`". `MT1.md` line 95: "matter parity `θ` equals conjugation by the product of local centre elements over `Λ`, on `L_cube`, U, and O[S_+]". Neither line says anything about an (F) embedding, as line 49 says.

### 2.2 Cell covariance of the rishon tick (item 22)

`LW1_5.md` B1-U (line 268) reads: "Send `c_{x,j}↦d_g(gx)c_{gx,j}`. On each link send every rishon mode at its `z`-end to the same flavour at the `gz`-end of the image link." Each step transfers. (i) `E_{x,αi}` is odd, so it is a sum of odd monomials in the `c_{x,j}`, `c^†_{x,j}`; the signed relabelling sends it to `d_g(gx)E_{gx,αi}`. (ii) The rishon map permutes the 32 modes of a link and keeps their number, so it restricts to the sector of total number `m`. (iii) On a reversed image `(x',y')=(gy,gx)`, the first summand `E_y r^y_α r^{x†}_β E^†_x` maps to `E_{x'}r^{x'}_α r^{y'†}_β E^†_{y'}`. This is the adjoint of the first summand of `h_{(x',y')}`. No extra sign appears, because rishons commute with matter. (iv) Each summand picks up `d_g(gx)d_g(gy)`, as in B1-U, so the LW1 A2 sign identity carries `H_C` to `H_{gC}`. There is no electric layer to check.

### 2.3 The centre-pattern obstruction and its named step (items 1, 24-28)

**Decision: correct, and the named step is correct.** The named step is Theorem 4.1(a): each `z_x` implements the local gauge transformation `Γ_x(-1)`, so it fixes `𝔄^G`, and so `U_x` fixes `H_phys`.

Three facts about its scope.
1. (a) holds for every law in 𝓛. It uses neither (F), nor link-purity, nor the update. It needs only Definition 5.
2. (a) gives more than `H_phys⊥𝒮`. Every `U_x` fixes `H_phys`, so `H_phys⊂H(1)`, the trivial-pattern subspace. By (c), `H(1)⊥H_nt⊇𝒮`. Line 5 states this stronger form; Theorem 4.1(a) should state it too (edit E6).
3. The exclusion of (T) is definitional. (T) asks for nonzero vectors in `H_phys`, which every `U_x` fixes, that also lie in the closed span `𝒮` of vectors negated by some `U_x`. Fixed and negated vectors of one unitary are orthogonal, so no law could supply them. Line 149 says this correctly: the negative statement is "the explicit incompatibility in Theorem 4.1(a)".

The statements with content are (b), (c) and SC′. (b) is where (F) and link-purity enter: with both, `𝔄^G` and `H_phys` are matter-even. (c) says that every band made of vectors that carry a local centre flip is flat on a neighbourhood of each node. Under (F) with link-purity, every odd vector carries one. So in the field representation of any D1 state of such a law, no odd band moves. This is the dynamical obstruction. It is `LZ1.md` Theorems 2.1-2.2 with `c_z` replaced by `z_x`. The port is complete: the proof uses only `U_x^2=1`, commuting `U_x`, `ŨU_xŨ^*=U_x`, `T_βU_xT_β^{-1}=U_{x+2β}`, and separability.

The status line should name (c) and SC′ as the content and (a) as the definitional exclusion of (T) (edit E6).

### 2.4 Example O (item 30)

**Decision: correct.** Re-derived. The two end actions act on different summands of `H_ℓ`, so they commute. `Y=Σ_β|β_x⟩⟨0_x|⊗E^†_{x,βi}` is invariant under `Γ_x(g)`: `|β_x⟩⟨0_x|↦Σ_{β'}S_{β'β}|β'_x⟩⟨0_x|` and `E^†_{x,βi}↦Σ_{β'}\bar S_{β'β}E^†_{x,β'i}`. `Γ_y` acts trivially on it. `Y` is odd and nonzero. The quasi-local algebra is a UHF algebra, so its trace `τ` is the unique tracial state. Then `τ∘β=τ` for every automorphism `β`, so `τ` is D1 for every update in 𝓛 on these registers that commutes with even translations. The trace is faithful, so `π(Y)Ω≠0`.

Example O also shows that link-purity is needed in the last clause of Theorem 4.1(c). `π(Y)Ω` is physical, hence in `H(1)` by (a), and it is odd. So `H_odd⊄H_nt` there. Add this one sentence (edit E6).

---

## 3. The distiller's GAPs, the witnesses and the candidate reading

### 3.1 GAP: NN compilation (items 2, 23) — real; closed under NN-a

**Is the gap real?** Yes. NN-a reads (`TOE_ASSEMBLY.md` line 235): "A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`. ... A nearest-neighbour layer is a locally finite product on pairwise disjoint edge triples. The update has a fixed finite number of such layers, independent of volume. ... Gauge invariance and cell covariance are required of the complete update only." A witness cube gate `e^{-iaH_C}` acts on eight sites and twelve links. It is not a nearest-neighbour gate. The draft's "its gates are each gauge invariant (NN-b, hence NN-a)" (draft line 173) therefore does not show NN-a, and the draft's §6.1 says the compilation "is not re-run". The distiller is right.

**Does `GA1_5.md` Proposition C apply?** Not as stated. Its Lemma U compiles "every unitary `G` on `⊗_{ℓ∈L′}H_ℓ`, the operator `G⊗1` (identity on all matter and all other links)" (`GA1_5.md` line 236). Its part (ii) covers members of GA1-P-5, whose gates are each "a link-only gauge-invariant unitary" (`GA1_5.md` line 52). The witness gates act on matter by odd operators (`E_{x,βi}`; `O_{x,i}` for A), so neither hypothesis holds. One step of Proposition C does transfer: its parallel run of `W^{cube}` ("distinct cubes of one tiling have disjoint sites and links", `GA1_5.md` line 268).

**What applies.** `LW1.md` "Dressed factorization" (statement line 196, proof lines 198-205) compiles exactly this kind of gate: a cube generator that is a sum of twelve edge terms. Its proof is ported below with credit; nothing in it uses the one-mode site.

**Lemma NN-W (referee closure).** Let the law be the rishon witness of Theorem 3.1, or alternative A restricted to S′, with `H_C=3^{-1/2}Σ_{ℓ⊂C}η_i(x)h_ℓ` (`h_ℓ=h^{full}_ℓ` for A).
(a) Each cube gate `e^{-iaH_C}` is an exact finite product of unitaries `e^{-ith_ℓ}`, `t∈ℝ`, `ℓ⊂C`. Each factor is even, commutes with every `Z_x(g)`, and acts within one edge triple `F_x,F_y,H_ℓ`.
(b) The base tick is a composition of finitely many layers, independent of volume, each a product of gates on pairwise disjoint edge triples. The complete update fixes every local gauge generator.
(c) With the cell covariance of item 22 (rishon) and of `LW1_5.md` §4 (A: "the cube construction is cell covariant"), both witnesses meet NN-a read with their own registers. The compiled factors are gauge invariant one by one, so NN-b also holds.

*Proof.* (a) Each `h_ℓ` is a sum of terms (odd at `y`)(odd at `x`)(link operator), plus the adjoint. Rishon bilinears `r^y_αr^{x†}_β` keep total rishon number, so they act on the fixed-number register `H_ℓ`; for A the link factor is `|i,x⟩⟨j,y|`. A product of two odd site elements commutes with `P_xP_y`. So `h_ℓ` is an even element of the edge-triple algebra. It commutes with every `Z_x(g)` by Theorem 3.1 (`LW1_5.md` §4 for A). Put `X_ℓ=-i3^{-1/2}η_i(x)h_ℓ`, so `-iH_C=Σ_{ℓ⊂C}X_ℓ`. Work in the unitary group of the finite-dimensional space of one cube. Let `𝔤` be the real Lie algebra generated by the twelve `X_ℓ`. Let `𝖫` be the connected analytic subgroup with Lie algebra `𝔤` (analytic subgroup theorem). Let `𝖧` be the group of finite words in the `exp(tX_ℓ)`. Then `𝖧⊆𝖫`. Rebuilt from `LW1.md` lines 198-205: let `𝔳` be the span of all `Ad_hX_ℓ`, `h∈𝖧`. It is `Ad_{exp(tX_ℓ)}`-invariant; differentiating at `t=0` gives `[X_ℓ,𝔳]⊆𝔳`, so `𝔳⊇𝔤`. Also `𝔤` is invariant under `Ad_{exp(tX_ℓ)}=exp(t ad X_ℓ)`, so `𝔳⊆𝔤`. Choose a basis `Y_k=Ad_{h_k}X_{ℓ_k}` of `𝔤`. The map `(t_k)↦∏_kh_k exp(t_kX_{ℓ_k})h_k^{-1}` is smooth into `𝖫`, lands in `𝖧`, and has derivative `(t_k)↦Σ_kt_kY_k` at zero, an isomorphism onto `𝔤`. The inverse function theorem on `𝖫` puts a neighbourhood of the identity of `𝖫` inside `𝖧`. So `𝖧` is an open subgroup of the connected group `𝖫`, and `𝖧=𝖫`. Since `-iaH_C∈𝔤`, `e^{-iaH_C}∈𝖧`: an exact finite word, not a Trotter limit. Each letter `exp(tX_ℓ)` is `e^{-it'h_ℓ}` with `t'` real.
(b) "The even translations preserve the tilings and the parity-dependent signs" (`LZ1.md` §1), so `H_{C+2β}=τ_β(H_C)`. Fix one word for one cube of each tiling and translate it. Cubes of one tiling have disjoint sites and links, so the `k`-th letters of all translated words lie on pairwise disjoint edge triples and form one layer. Even gates on disjoint supports commute, and a locally finite product of them is an automorphism (`LW1.md` E1). The depth is the sum of the two word lengths. Every letter commutes with every `e^{it𝒢_x}`, so the complete update fixes `e^{it𝒢_x}` for all `t`; differentiating at `t=0` in the finite-dimensional local algebra, it fixes `𝒢_x`.
(c) follows from (a), (b) and the cited covariance. □

**Reading note.** NN-a is stated "For the named five-mode laws". Applying it to a witness puts the witness register in place of "the chosen link register". This is the plain reading; the witnesses stay unadopted.

**Repaired GAP text (lines 7 and 67).** "NN compilation (referee closure, `CG16B_REFEREE.md` §3.1). The cube generator of each witness is a sum of twelve even, gauge-invariant edge terms. By the proof of `LW1.md`'s dressed factorization, each cube gate is an exact finite word in even, gauge-invariant edge-triple gates, and the base tick has finite nearest-neighbour depth. So, under NN-a read with the witness registers, both witnesses are NN-a laws with nonzero angles; they also meet NN-b. `GA1_5.md` Proposition C does not apply as stated: its Lemma U compiles link-only unitaries. This gives no propagation."

### 3.2 GAP: limits (items 3, 39) — real; the extension is false; repaired statement

**Is the gap real?** Yes. The draft proves the equality only "For factor sectors localized in a finite set relative to a factor sector" (draft line 254). It then reads it for all strings: "the 16 can be read ... as the relative spinor class of a `χ_tot`-odd sector" (draft line 261), and "a `χ_tot`-odd straight-string sector, which under (F) is a spinor sector" (draft line 313). Nothing proves the step from finitely localized sectors to string limits.

**Finding.** The step is false over every background that is sharp in each `z_x`. The free end of a string leaves every finite region. In the limit, no site carries the flipped centre value; the flip sits in the boundary flux. `RCS1.md` §5 already notes the mechanism for the live laws (line 91): "If `ω` is sharp in `c_z`, every sufficiently long string state has the same sharp value." `RCS1.md` R3 (line 185) shows that translation-covariant factor sectors have an empty or infinite configuration difference. The following makes the consequence exact on an (F)-law.

**Proposition L (referee closure).** Take a law in 𝓛 with (F), every link link-pure, even-translation covariant. Let `ω` be a D1 state with `ω(z_y)=κ₀(y)∈{±1}` for every site `y`. (This holds when the representation of `𝔄^G` on `H_phys` is a factor, because `z_y` is central in `𝔄^G`.) Fix `x` and an axis. Let `B_{r,b}∈𝔄` commute with `z_y` for every `y≠y_{2r}`, as the strings of Theorem 6.2 do. Put `ω_r(A)=Σ_bω(B^*_{r,b}AB_{r,b})/Σ_bω(B^*_{r,b}B_{r,b})` on `𝔄^G`. Let `ω_∞` be a weak-* limit point along lengths with positive denominators, with GNS triple `(H_∞,π_∞,Ω_∞)`.
- (i) `π_∞(z_y)=κ₀(y)1` for every `y`: the centre configuration of the limit equals the background's at every site.
- (ii) If `ω(P_Λ)=ε_Λ∈{±1}` for every finite `Λ`, and each `B_{r,b}` is matter-odd with its matter at `x`, then `ε_Λπ_∞(P_Λ)→-1` strongly along the net of finite `Λ`, that is, `χ_tot(π_∞:ω)=-1` (`RCS1.md` R2).
- (iii) Under (ii), put `φ_Λ=ω(F_{∂Λ})`. Then `φ_Λ∈{±1}` and `φ_Λπ_∞(F_{∂Λ})=ε_Λπ_∞(P_Λ)` for every finite `Λ`. So the boundary label `φ_Λπ_∞(F_{∂Λ})` tends strongly to `χ_tot=-1`.
- (iv) Under (ii), if `π_∞` and the representation `π₀` of `𝔄^G` on `H_phys` are factors, `π_∞` is not localized in any finite set relative to `π₀`.

*Proof.* (i) For fixed `y` and large `r`, `y≠y_{2r}`, so `B^*z_yB=B^*Bz_y`. Since `z_y^2=1` and `ω(z_y)=κ₀(y)`, `ω((z_y-κ₀(y))^2)=0`. Cauchy-Schwarz gives `|ω(Y(z_y-κ₀(y)))|^2≤ω(YY^*)ω((z_y-κ₀(y))^2)=0` for every `Y`. So `ω_r(z_y)=κ₀(y)` for large `r`, and `ω_∞(z_y)=κ₀(y)`. Then `‖(π_∞(z_y)-κ₀(y))Ω_∞‖^2=0`. As `z_y` is central in `𝔄^G` (Theorem 6.1), `π_∞(z_y)π_∞(A)Ω_∞=κ₀(y)π_∞(A)Ω_∞`; cyclicity gives the claim.
(ii) `P_Λ∈𝔄^G`, since `u(g)` commutes with `P`. For `x∈Λ`, `P_ΛB=-BP_Λ`; the step of (i) gives `ω_r(P_Λ)=-ε_Λ`, hence `π_∞(P_Λ)Ω_∞=-ε_ΛΩ_∞`. A local `A∈𝔄^G` with matter in `Λ` is even (Theorem 4.1(b)), so `P_ΛAP_Λ=A` and `ε_Λπ_∞(P_Λ)π_∞(A)Ω_∞=-π_∞(A)Ω_∞`. Such `Λ` form a tail of the net. Local elements are dense in `𝔄^G` (Theorem 4.1(b)) and the net is bounded by one.
(iii) Theorem 6.1 gives `∏_{z∈Λ}z_z=ε^{|Λ|}s_ΛP_ΛF_{∂Λ}`, with commuting gauge-invariant factors and `s_Λ=±1`. Apply `ω` and the step of (i): `∏_Λκ₀=ε^{|Λ|}s_Λε_Λω(F_{∂Λ})`, so `φ_Λ=ε^{|Λ|}s_Λε_Λ∏_Λκ₀∈{±1}`. Apply `π_∞` and (i): `∏_Λκ₀·1=ε^{|Λ|}s_Λπ_∞(P_Λ)π_∞(F_{∂Λ})`. Multiply by `π_∞(P_Λ)`, using `P_Λ^2=1`: `π_∞(F_{∂Λ})=φ_Λε_Λπ_∞(P_Λ)`. Multiply by `φ_Λ`; (ii) gives the limit.
(iv) Suppose `π_∞` is localized in finite `Λ` via `V`. Theorem 6.1's port of `RCS1.md` Theorem 3 gives `π_∞(P_{Λ'})=χV^{-1}π₀(P_{Λ'})V` for finite `Λ'⊇Λ̂`, with `χ=∏_{Λ̂}κ_∞/κ₀=+1` by (i). On `H_phys`, `ε_{Λ'}π₀(P_{Λ'})→1` strongly: `π₀(P_{Λ'})Ω=ε_{Λ'}Ω`, `P_{Λ'}A=AP_{Λ'}` for even `A` with matter in `Λ'`, and `H_phys⊂H_even` (`RCS1.md` R2(b), rebuilt in these two steps). So `ε_{Λ'}π_∞(P_{Λ'})→+1`, against (ii). □

**Example S (referee closure; the sectors exist).** Take the rishon witness at any angles, `m=16`. Let `Φ` be the product vector with matter `|i_0⟩∈H_-` at every site, and on every link all 16 rishons at its source end and none at its target end.
- Every summand of `h_ℓ` ends in `E^†_{x,βi}` or `E^†_{y,αi}`, and `E^†=|i⟩⟨β|` kills `H_-`. So `H_CΦ=0`, every cube gate fixes `Φ`, and `ω_Φ` is stationary.
- `ω_Φ` is translation invariant and locally gauge invariant: `S_+(g)⊕1` fixes `H_-`; a full end changes by `det S_+(g)=1`, because `tr(Π_+M^{ab})=(i/4)tr(γ_aγ_b(1+P))=0` (`γ_aγ_b` and `γ_aγ_bP` are non-scalar Clifford monomials); an empty end is fixed. So it is D1.
- `P_y=-1` everywhere, so `ε_Λ=(-1)^{|Λ|}`. `z_y=-P_y∏_{ℓ∋y}(-1)^{p_{ℓ,y}}=+1` sharply (three full ends, three empty).
- For the strings of Theorem 6.2 along `+e_1`, each term of `B_{r,b}Φ` empties a full source end and fills an empty target end, and `E_{x,ai_0}|i_0⟩=|a⟩`. Distinct index sequences give orthogonal unit vectors, so `Σ_b‖B_{r,b}Φ‖^2=16^{2r+1}>0`. Limit points exist by weak-* compactness.

By Proposition L, every limit point is a `χ_tot`-odd string sector with centre value `+1` at every site and boundary label `-1`. So the draft's "a `χ_tot`-odd straight-string sector, which under (F) is a spinor sector" is false if "spinor sector" means `RCS1.md` Theorem 3's relative class `-1`.

**Repaired statement (for lines 9 and 120, and for the reading in §3.3).** "Under (F) with link-purity, over a parity-sharp D1 background sharp in every `z_x`, every straight-string limit keeps the background centre value at every site; a `χ_tot`-odd one is not finitely localized, and the class of the local `-1∈Spin(10)` sits in its boundary label: `φ_Λπ(F_{∂Λ})→χ_tot=-1` (referee closure, `CG16B_REFEREE.md` §3.2, Proposition L). Such sectors exist in the rishon witness at every angle (Example S). On `L5-O[S_+]` every end is end-pure for `-1∈Spin(10)` (`LW1_5.md` Σ), so each `F_{∂Λ}` built from these ends is a scalar and the same boundary label is `+1` for every sector. Whether these sectors carry a band is RCS-P on an (F)-law."

### 3.3 The candidate reading R-16^str (items 46, 48)

**Is it stated correctly?** No. Line 142 paraphrases it ("inspect the internal `-1` class of `χ_tot`-odd string sectors"). An owner decision needs the text. The draft's text (draft line 285) is: "Under the working candidate R-CS^str with `χ_tot` (`TOE_ASSEMBLY.md` section 3.6), CG1(e)'s 'the spinor 16 rather than the vector 10' is read as: the `χ_tot`-odd string sectors have relative class `-1` under the local `-1∈Spin(10)`, that is, the free end of their strings carries a spinor-class representation (Proposition C)."

**Is it four-tested correctly?** Not for that text. By Proposition L(i) and (iv), a `χ_tot`-odd string limit over a background sharp in every `z_x` is not finitely localized, and its centre value equals the background's at every site. So "relative class" (`RCS1.md` Theorem 3's `χ`) is undefined on the sectors the reading names, or, read through the configuration, it is `+1` on every law. "The free end" exists only for finite strings. A later part would have to supply the definition, so test 2 fails for this text (the distillation gives C). Tests 1, 3, 4 pass as the distillation says.

**Repaired candidate, for the owner (not adopted).** R-16^str′: "Under the working candidate R-CS^str with `χ_tot` over parity-sharp backgrounds (`TOE_ASSEMBLY.md` §3.6), for a background also sharp in every local centre implementer, CG1(e)'s 'spinor rather than vector' is read on the `χ_tot`-odd string sectors `π` as the boundary label of the local `-1∈Spin(10)`: the strong limit of `φ_Λπ(F_{∂Λ})`, where `F_{∂Λ}=∏_{ℓ∈∂Λ}ρ_{ℓ,in(ℓ)}(-1)` and `φ_Λ` is its background value. Spinor class means the limit is `-1`."

What it returns. On an (F)-law with link-purity, the limit exists and equals `χ_tot=-1` (Proposition L(iii)): spinor. On `L5-O[S_+]` each end factor is a scalar (`LW1_5.md` Σ), so the label is `+1`: not spinor. On `L5-U` there is no local `Spin(10)`, and the reading does not apply.

Four tests of R-16^str′:
1. P. It says where the class is read, not its value; the value differs between laws.
2. C. It inherits R-CS^str's open quantifiers over limit points and axis (`RCS1.md` line 207). Its own terms are closed.
3. P. It decides neither existence nor motion of any sector (RCS-P stays open). The value "spinor" on an (F)-law follows from (F), a law choice, by Proposition L(iii); it is not a premise of the reading.
4. P. It uses `P_Λ`, `F_{∂Λ}`, `z_x` and the background, all already present. The sharpness condition is what its own definition of `φ_Λ` needs.

It reads only the centre class. Spinor class is not an irreducible 16 (Definition 4); the name "R-16" overstates this, and the text should say "spinor class".

### 3.4 Scope of Corollary 2.3 (items 4, 17)

`LW1_5X.md` line 7 (frozen): "For `m=1,9`, the even gate gives the bound at every point of the parameter window." There the bound is `U(5)`, which lies in the Bogoliubov group. So, by Theorem 2.2(c), no (F) embedding is compatible with the even cube gate of `L5-U[1]` or `L5-U[9]` at any window angle. For `2≤m≤8` the remaining points are LW1-5-X-B_m. For `L5-O[S_+]` they are LW1-5-X-O. The whole-tick question stays LW1-5-T. Line 11's "outside the exceptional angles" is right but too broad; edit E4 sharpens it.

---

## 4. Required edits to `CG16B.md`

Required before freezing:
- **E1 (lines 7, 11, 67, 140).** Replace the NN-compilation GAP by the repaired text at the end of §3.1, marked "(referee closure, CG16B_REFEREE.md)". In line 11 drop "NN compilation" from the added named gaps. In the rishon row of §7 replace "NN compilation is open" by "NN compilation: referee closure, §3.1 of `CG16B_REFEREE.md`".
- **E2 (lines 9, 11, 120).** Replace "GAP: charged-sector identification" and "GAP: limits" by the repaired statement at the end of §3.2. Add Proposition L and Example S as referee closures. In line 11 drop "the charged-sector identification" from the added named gaps.
- **E3 (lines 142, 145).** Quote R-16^str's text (draft line 285). Mark its test 2 as F, with the reason of §3.3. Add R-16^str′ with tests P, C, P, P, as a candidate for the owner, not adopted, worded with "spinor class".
- **E4 (lines 11, 39).** After Corollary 2.3 add: "For `L5-U[1]` and `L5-U[9]` the gate-wise statement holds at every window angle, by `LW1_5X.md` (frozen)." Add LW1-5-X-B_m and LW1-5-X-O to Open by name.
- **E5 (line 111).** Before the translation clause of Theorem 6.1 add "If the law is even-translation covariant as in Definition 5 and".

Recommended (cosmetic):
- **E6.** Line 73: state `H_phys⊂H(1)`, hence `H_phys⊥H_nt⊇𝒮`. Lines 5 and 79: say that the exclusion of (T) is definitional, and that (b), (c) and SC′ carry the content (§2.3). Line 85: add that links at `x∉Λ` are outside the support of `A`. After line 91: Example O also shows link-purity is needed for `H_odd⊂H_nt` (§2.4). Line 24: "`V` continuous". Line 13: add `MT1.md`, `GA1_5.md`, `LW1_5X.md` to the context list. Line 137: note that (T) is the lane's question, so test 1 marks no smuggle.
- **E7.** Add a short "Prior work used" pointer: the draft's §1 list, plus the items this report adds (§7 below).

## 5. Open statements to carry by name

- **RCS-P** (inherited, `RCS1.md` §8), also posed on an (F)-law. Under R-16^str′ every `χ_tot`-odd string sector of an (F)-law with link-purity is spinor class (Proposition L(iii)). Whether one carries a band with a node and a nonzero leading generator is open; `RCS1.md` Corollary 9 constrains any example (Theorem 6.1).
- **LW1-5-T** (inherited): whole-tick frame symmetries; bounds Corollary 2.3.
- **LW1-5-X-B_m**, `2≤m≤8`, and **LW1-5-X-O** (inherited, `LW1_5X.md`): the exceptional points left in Corollary 2.3.
- **R-CG1**, **R-CS**, **MT1-S[R-CS^str] in the VC1 vacuum** (owner and inherited); **CG1-i, CG1-ii, MT1-ii, MT1-S, VC1** (inherited).
- **R-16^str′** (owner question): the repaired candidate of §3.3. Not adopted.

Not carried: the NN-compilation GAP (closed, §3.1) and the charged-sector identification GAP (replaced by Proposition L and Example S, §3.2).

## 6. Freeze recommendation

**Freeze after edits E1-E5.** E6 and E7 are cosmetic and recommended. No proved theorem of `CG16B.md` changes its content. Two status statements change. The NN qualification of the witnesses is removed: both witnesses are NN-a laws (and NN-b laws) under the plain reading. The extension of the parity/centre equality to string limits is refuted in Theorem 3's sense and replaced by the boundary-label statement. The referee closures enter as "(referee closure, CG16B_REFEREE.md)", unrefereed, in the usual way.

---

## 7. Prior work used

Each item is used to check a port or to build a referee closure. Paths are in this folder unless a branch is named.

- **`prior/CG16B.md`** (the digest). Checked against `CG16B.md` lines 13, 43, 126. Its quotations of #10027, #10038, #10045 agree with branch `origin/docs/consolidate-gauge-matter-registers` (`7086189d10`), `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 27, 827 (#10023 part B: "one band h(k) x 1_16, a supplied spinor-index field"), 1202, 1204, read here with `git show`.
- **`LW1_5.md`**: S′ and its proof, step 5 (`so(10)` simple, lines 149-160), used for item 16; M and the independence lines (120-124), item 17; alternative A (161-165), items 21 and §3.1; F and K, Theorem SC, Σ (171-204), items 31 and §3.2-3.3; B1-U (266-275), item 22.
- **`LZ1.md`**: §1 (lines 30-44, including line 36 on even translations), Theorems 2.1-2.2 (lines 50-64); items 10-11, 26-28 and §3.1(b).
- **`RCS1.md`**: Theorems 1-4 (lines 34-66), §5 strings and the sharp-value remark (lines 82-91), Theorem 8 and Corollary 9 (lines 97-127), R2 (lines 159-181), R3 (lines 183-187). Proposition L extends the line-91 remark and R2(b)-(c) to (F)-laws.
- **`MT1.md`** Theorems 5-6 (lines 89-97); item 20.
- **`TOE_ASSEMBLY.md`** §3.6 (line 225: R-CS^str "is a named working candidate ... It is not adopted"), §3.7 (line 235: NN-a); items 2, 46 and §3.1.

**Prior work the digest missed.**
- **`LW1.md` "Dressed factorization"** (statement line 196, proof lines 198-205): each dressed cube gate is an exact finite word in even, gauge-invariant edge-triple gates. Its proof closes the NN-compilation GAP for both witnesses (§3.1). Neither the draft nor the distillation used it.
- **`GA1_5.md` Lemma U and Proposition C** (lines 236, 264-270): the compilation the distiller pointed to. It does not apply to the witnesses as stated (§3.1); its parallel-run step does.
- **`LW1_5X.md`** line 7 (frozen): the `U(5)` bound at every window angle for `m=1,9`. It sharpens Corollary 2.3 (§3.4).
- **`RCS1.md`** line 91 and R3 (line 185): strings keep sharp background centre values; covariant factor sectors have empty or infinite configuration differences. These are the live-law forms of Proposition L(i) and (iv).

---

## FINISH

**Proved here** (pass-3 referee closures; written out in full above; not themselves refereed).
1. *Verdicts.* 49 items of `CG16B.md`: 46 CORRECT, 0 ERROR, 3 INCOMPLETE (items 4, 36, 46). Every theorem of `CG16B.md` was re-derived; none changes content.
2. *Centre-pattern obstruction (Theorem 4.1).* Correct, with the named step correct. In every law in 𝓛, `H_phys` lies in the trivial-pattern subspace, so it is orthogonal to every nontrivial centre pattern. The exclusion of (T) is definitional; the content is the matter-evenness under (F) with link-purity, the flatness of every band in `H_nt`, and SC′ (§2.3).
3. *Example O.* Correct. It also shows that link-purity is needed for `H_odd⊂H_nt` (§2.4).
4. *Lemma NN-W.* Both witnesses (alternative A restricted to S′, and the `U(16)`-rishon law) are NN-a laws under NN-a read with their own registers. Each cube gate is an exact finite word in even, gauge-invariant edge-triple gates (port of `LW1.md` dressed factorization), so NN-b holds as well. `GA1_5.md` Proposition C does not apply as stated (§3.1).
5. *Proposition L.* Under (F) with link-purity, over a D1 background sharp in every `z_x`, every straight-string limit keeps the background centre value at every site. If the background is parity-sharp and the string matter-odd, the limit has `χ_tot=-1`, its boundary label `φ_Λπ(F_{∂Λ})` tends to `-1`, and, for factor representations, it is not finitely localized (§3.2).
6. *Example S.* In the rishon witness at every angle (`m=16`), a parity-sharp, `z`-sharp, locally gauge-invariant D1 product state has string limits of positive norm; Proposition L applies to them (§3.2).
7. *Corollary 2.3, sharpened.* For `L5-U[1]` and `L5-U[9]`, no (F) embedding is compatible with the even cube gate at any window angle (from `LW1_5X.md`, §3.4).

**Counterexamples.**
- Example S refutes the draft's extension "a `χ_tot`-odd straight-string sector, which under (F) is a spinor sector" (draft line 313), read with `RCS1.md` Theorem 3's relative class. The distiller's GAP on limits is real, and the extension is false in that sense.
- The draft's text of R-16^str fails test 2 (§3.3): its "relative class" is undefined on the string limits it names.

**Open by name.** RCS-P (inherited; also on an (F)-law); LW1-5-T; LW1-5-X-B_m (`2≤m≤8`); LW1-5-X-O; R-CG1; R-CS; MT1-S[R-CS^str] in the VC1 vacuum; CG1-i; CG1-ii; MT1-ii; MT1-S; VC1. Owner question: R-16^str′ (§3.3), a candidate, not adopted.

**What changes downstream.**
- *`CG16B.md`.* Freeze after edits E1-E5 (§4). The NN qualification of the witnesses is removed. The charged-sector paragraph is replaced by Proposition L and Example S.
- *CG1(e), R-CG1.* On an (F)-law the spinor class of an odd string sector is not a site label. It is the boundary label of the local `-1∈Spin(10)`. A lane that reads "spinor rather than vector" in string limits must read it there (R-16^str′). On `L5-O[S_+]` that label is trivial.
- *RCS-P on an (F)-law.* Unchanged in difficulty. Its candidate sectors exist (Example S), are spinor class in the boundary sense, and are not finitely localized. `RCS1.md` Corollary 9 constrains any band.
- *Owner, law choice.* Unchanged: keeping (F) still needs a third five-mode law, and (F) as law data still fails tests 1 and 3 (line 139). The witnesses now meet NN-a, so admissibility under NN-a is not an obstacle.
- No law, reading, axiom or working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
