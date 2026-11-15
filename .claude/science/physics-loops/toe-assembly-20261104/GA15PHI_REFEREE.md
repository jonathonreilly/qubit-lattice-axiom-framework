lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GA1-5-Φ referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 (the referee) under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the owner freezes. This session wrote neither pass 1 (`GA15PHI_DRAFT.md`) nor pass 2 (`GA15PHI.md`). This is one check: one whole-part, line-by-line read of `GA15PHI.md`. No review of this review was commissioned.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. Owner guidance, applied as written: "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms and readings are read plainly.

**Sources read, with commits.** Checkout branch `claude/toe-assembly` at `15bc39079`. Text refereed: `GA15PHI.md`, last changed `618c2b93b`, SHA-256 `043e40c006d5cfb03fecaf99c2ad24d90a5edde9c78e4a58c7dc298a60a0c8c7`, lines 1-147 (all). Line numbers below refer to that file. Pass-1 source: `GA15PHI_DRAFT.md`, last changed `5143421f0`, SHA-256 `43fcd65a60dceb5c56a746a8a9388ee4e9205575a94478682351aee77ccd7c44` (equal to the hash `GA15PHI.md` line 13 records), lines 1-322 (all). Digest: `prior/GA15PHI.md` lines 1-83 (all). Cited sources, by line: `GA1_5.md` (last changed `2d48e6bdc3`) lines 7, 42-61 (§1), 65 (Theorem 2.1), 75 (Theorem 2.2), 83 (Theorem 3.1, first sentence), 148-188 (Theorems 6.1-6.4, §7 item GA1-5-Φ), 228-270 (Lemma U, Proposition C), 276-278 (Lemma S1′), 318-337 (Proposition S-odd), 383-385 (§3.9 identification); `TOE_ASSEMBLY.md` lines 231-238 (section 3.7, NN-a); `LZ1.md` line 40 (D1 state); `LW1_REFEREE.md` lines 1-80 (format only); `Y2W_DRAFT.md` lines 1-30 (format only). The six context hash prefixes of `GA15PHI.md` line 13 were recomputed and all agree. No other branch was read; nothing on `origin/main` is used as a proof step.

**Working-set entries used.** PS-5 and PS-6r only through the law `L5-U[m]` as `GA15PHI.md` §1 item 1 restates it; PS-1 only through the owner's NN-a text (`TOE_ASSEMBLY.md` line 233). The proposed class GA1-P-5, the proposed reading R-Φ and the D1, band, node and propagation definitions of `GA1_5.md` §1 are used as stated and are not adopted. Results used, by name: `GA1_5.md` Theorems 2.1, 2.2, 6.1, 6.2, 6.3, 6.4, Lemma U, Proposition C, Lemma S1′, Proposition S-odd and the §3.9 identification.

**Counts.** 54 items: 52 CORRECT, 1 ERROR, 1 INCOMPLETE. Neither the ERROR nor the INCOMPLETE item changes a theorem of `GA15PHI.md`. One referee closure (§4, closure R1) goes further: it completes the route that `GA15PHI.md` line 135 calls attack A3, and gives GA1-5-Φ for `m=1` and `m=9`. R1 is new and unchecked; §6 says how to carry it.

**Method.** Every proof step was re-derived by hand. Verdicts: CORRECT; ERROR (a false line, quoted, with the fix); INCOMPLETE (a named missing step, with what is missing). A "referee closure" is a short complete argument for a missing step. No computer-assisted proof is used. A `[check]` would be a tiny scratch computation in `/tmp/toe-ga15phiref/`; it guides and never proves.

---

## 1. Verdict table

| # | Item (`GA15PHI.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status paragraph (5) | CORRECT | Scope, conditions and "not a photon" all match the proofs below. |
| 2 | §0 "Proved here" list (7) | CORRECT | Each listed result is proved in §§2-8. |
| 3 | §0 GAP on draft Lemma 4.4 Step 2 (9) | ERROR | The draft does not infer `θ_{++}=θ_{--}` from equal squares; its step is valid as written. Fix in §3, note G1. |
| 4 | §0 GAP on draft Lemma 6.1 support (9) | CORRECT | Gap real; counterexample in §3, note G2. |
| 5 | §0 GAP on draft A3 (9) | CORRECT | Gap real. More is true: the A3 route succeeds (closure R1, §4). |
| 6 | §0 "Open by name" (11) | CORRECT | Correct for pass 2. If R1 survives its check, GA1-5-Φ[`m=1,9`] leaves the list (§6). |
| 7 | §0 provenance (13) | CORRECT | Draft hash and all six context prefixes recomputed; all agree. |
| 8 | §1 item 1, law and class (19) | CORRECT | Matches `GA1_5.md` line 50 and `TOE_ASSEMBLY.md` line 233. |
| 9 | §1 item 2, geometry (20) | CORRECT | Checked on `{0,1}³`: `r` keeps and `h` reverses the hexagon. |
| 10 | §1 item 3, spaces, `σ*`, `σ→` (21) | CORRECT | |
| 11 | §1 item 4, D1, band, R-Φ, four-test report (22) | CORRECT | Matches `GA1_5.md` lines 57-61 and `LZ1.md` line 40. |
| 12 | §1 item 5, end permutations, swaps (23) | CORRECT | The sign `(−1)^p` per transposition twists `T` by a character; `q` and `L` are unaffected. |
| 13 | Theorem 1, statement (27-32) | CORRECT | |
| 14 | Theorem 1, proof (34) | CORRECT | |
| 15 | Theorem 2, statement (36) | CORRECT | |
| 16 | Theorem 2, proof of `q` (38) | CORRECT | |
| 17 | Theorem 2, proof of `μ₁, L`, `q⊥L` (40) | CORRECT | "Every ordering" also follows from reordering a tensor product. |
| 18 | Remark on the pass-1 check (42) | CORRECT | Not used. |
| 19 | §3 choices and state (46) | CORRECT | |
| 20 | Theorem 3, statement (48) | CORRECT | |
| 21 | Theorem 3, proof (50) | CORRECT | Orthogonality for `b≠b′` uses the product form of `ω`; say so (edit E4). |
| 22 | Remark after Theorem 3 (52) | CORRECT | |
| 23 | §4 definition of `E_P, X_P` (56) | CORRECT | Both are two-dimensional. |
| 24 | Theorem 4, statement (58) | CORRECT | |
| 25 | Theorem 4 proof, eigenvalues (60) | CORRECT | The cube-root argument is valid. It is a second proof, not a repair (item 3). |
| 26 | Theorem 4 proof, target and `J_P` (62) | CORRECT | |
| 27 | Theorem 4 proof, four diagonals and `g_C` (64-68) | CORRECT | `g_C=exp(−i(π/2)(J+J^*))`. |
| 28 | §5 definitions of `G, W′_B, ω′, A′` (72-76) | CORRECT | |
| 29 | Theorem 5, statement (78-82) | CORRECT | |
| 30 | Theorem 5 proof, class and NN-a (84) | CORRECT | Every hypothesis of `GA1_5.md` line 50 checked (§2.1). |
| 31 | Theorem 5 proof, D1 and stationarity (84) | CORRECT | |
| 32 | Theorem 5 proof, `Φ` and fibre (86) | CORRECT | `V(K)=e^{−iK·1}` under `F(e^{iK·b})=u′_b`. |
| 33 | Theorem 5 proof, R-Φ (88-93) | CORRECT | |
| 34 | Theorem 6, statement (97) | CORRECT | The gate of the proof moves into `σ→+hex_P` only; "±" means one chosen sign. |
| 35 | Theorem 6 proof, corners and stabilizer (99) | CORRECT | |
| 36 | Theorem 6 proof, corner data and lines (101) | CORRECT | "Each corner" means each hexagon corner (edit E6). |
| 37 | Theorem 6 proof, state and neutral band (103) | CORRECT | |
| 38 | Theorem 6 proof, gate (105) | CORRECT | |
| 39 | Theorem 7, statement (109-113) | CORRECT | "D1 state" means a D1 state of `U_B=W_BW_EM_oM_e` (edit E7). |
| 40 | Theorem 7, proof (115) | CORRECT | |
| 41 | Corollary 7.1 (117-119) | CORRECT | |
| 42 | Paragraph on what the mode is not (121) | CORRECT | |
| 43 | Theorem 8, `AP_R=P_RAP_R` and proof (125, 127) | CORRECT | |
| 44 | Theorem 8, `H_phys=closure π(𝒩)Ω` (125, 127) | CORRECT | |
| 45 | Theorem 8, sector preservation (125, 127) | INCOMPLETE | The gate-level step does not give the state-level claim; gates crossing `∂R` are not covered. Closure in §3, note G2′. |
| 46 | Remark on the support condition (129) | CORRECT | Explicit counterexample in §3, note G2. |
| 47 | Attack A1 (133) | CORRECT | Matches `GA1_5.md` line 180. |
| 48 | Attack A2 (134) | CORRECT | |
| 49 | Attack A3 and its GAP (135) | CORRECT | The draft's failing step is false; see closure R1. |
| 50 | GA1-5-O, open (137) | CORRECT | |
| 51 | Electric half, open (139) | CORRECT | Context only; nothing there is load-bearing. |
| 52 | §9 prior work (143) | CORRECT | Matches `GA1_5.md` lines 75, 158, 182, 188. |
| 53 | §9 literature (145) | CORRECT | Correctly marked as not load-bearing. |
| 54 | §9 downstream scope (147) | CORRECT | `V(K)≠1` off a null set gives image `⊥ker(Ũ−1)`. |

## 2. The questions the lane brief asks, decided

### 2.1 Are `G` and `W′_B=GW^{swap}W_EG^*W_E^{-1}` in GA1-P-5, and admissible under NN-a?

**Yes, given the imported Proposition C.** `GA1_5.md` line 50 defines the class: "Each `W_s=∏_{X∈ℱ_s}g_X` has finite link supports; `ℱ_s` is cell-group invariant and locally finite, each `g_X` is a link-only gauge-invariant unitary, gates in the sublayer commute pairwise, and each cell lift carries `g_X` to `g_{gX}`." Each clause holds for `G`.

- *Family.* `ℱ` is the even tiling. `𝒢` maps even cubes to even cubes (`GA1_5.md` Lemma S1′(a): "`𝒢` preserves each tiling"). Each link lies in at most one even cube, so `ℱ` is locally finite.
- *Gates.* `g_C` acts on `H_C`, the twelve links of `C`. It commutes with `G_C`; by Theorem 1 it then commutes with every local gauge transformation. It is unitary (Theorem 4; `g_C=exp(−i(π/2)(J+J^*))` with `(J+J^*)²=Π`).
- *Commutation.* Distinct even cubes have disjoint link sets (`GA1_5.md` Theorem 2.1), so the gates commute.
- *Covariance.* Put `g_{sC₀}=α_s(g_{C₀})` for `s∈𝒢`. This is well defined: the stabilizer of `C₀` is `O` (Theorem 2.1 there), and `Ad L_R(g_{C₀})=g_{C₀}` for `R∈O` (Theorem 4). Hence `α_s(g_C)=g_{sC}` for all `s,C`.

`G^*` is the sublayer of the `g_C^*`. `W_E^{±1}` is the sublayer of single-link gates `e^{∓iτ_E(p_{ℓ,x}−m/2)²}`. Since `p_{ℓ,x}+p_{ℓ,y}=m`, `(p_{ℓ,x}−m/2)²=(p_{ℓ,y}−m/2)²`; so the gate does not depend on the stored orientation, and a lift that reverses a link carries it to the gate of the image link. `S_o,S_e` are in the class for every `1≤m≤9` (`GA1_5.md` Theorem 6.3, Lemma S1′; Proposition C(i) states the swap for "every `1≤m≤9`"). So `W′_B` is a product of six sublayers and lies in GA1-P-5.

NN-a (`TOE_ASSEMBLY.md` line 233): "The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s` ... Gauge invariance and cell covariance are required of the complete update only." `GA1_5.md` Proposition C(ii): "Every member of GA1-P-5, on either law, is a composition of finitely many such layers, each invariant under `2kZ³`". Its layers use gates in `𝒢_{w,ℓ}=𝒜_w^+⊗B(H_ℓ)`; these are even and lie in one edge triple, so they are NN-a gates. Its proof needs a connected finite link set around each gate support; the twelve links of a cube and a single link are connected. The complete update `U′_B=W′_BW_EM_oM_e` is gauge invariant and cell covariant, because each factor is. So `W′_B` is admissible under NN-a. Two conditions remain explicit: GA1-P-5 is a proposed class ("GA1-P-5 itself stays a proposed candidate, not adopted", `GA1_5.md` line 7), and Proposition C is a referee closure that `GA1_5.md` line 9 labels unrefereed. `GA15PHI.md` states both (lines 5, 7, 22).

### 2.2 Is the band in the physical sector of the stated D1 state, with a node at `K=0` and a nonzero leading generator?

**Yes.** Steps, each re-derived.

1. *D1.* `ω′=ω∘Ad G^*`. `G` is link-only, gauge invariant and `2Z³`-invariant, so `ω′` keeps empty matter, local gauge invariance (hence centre invariance) and even-translation invariance. On empty matter the tick acts as `𝕍′=G𝕍G^*`, `𝕍=W^{swap}W_E` (`GA1_5.md` Theorem 6.1, proof: "`U_B P₀=𝕍P₀` and `P₀ U_B=𝕍P₀`"). Then `ω′(𝕍′^*A𝕍′)=ω(𝕍^*(G^*AG)𝕍)=ω(G^*AG)=ω′(A)`.
2. *Physical vectors.* `A′_{2b}=g_CA_{2b}g_C^*`, with `C` the even cube at `2b`. `A_{2b}` acts on the three `C`-links at `2b` only, so the other gates of `G` commute with it. `A′_{2b}` is local and gauge invariant, so `u′_b=π′(A′_{2b})Ω′∈H′_phys`.
3. *Motion.* `Φ:π(B)Ω↦π′(GBG^*)Ω′` is isometric: `ω′(GB^*G^*GB′G^*)=ω(B^*B′)`. `Ũ′Φπ(B)Ω=π′(G𝕍^*B𝕍G^*)Ω′=ΦŨπ(B)Ω` by Theorem 6.1 for both layers. Theorem 3 gives `Ũu_b=u_{b−1}`, hence `Ũ′u′_b=u′_{b−1}`.
4. *Fibre.* With `F(e^{iK·b})=u′_b`: `T_βF=Fe^{iK·β}` and `Ũ′F=Fe^{−iK·1}`. So `V(K)=e^{−iK·1}`, `V(0)=1`, and near `0`, `h=i log V=K·1`. Every `N_j=∂_jh(0)=1≠0`.

`GA1_5.md` Theorem 6.2 ("If every gate of `W_B` is supported on the links of a single tiling cube ...") does not apply: `W′_B` contains the swap, whose gates act on two stars.

### 2.3 Is the image orthogonal to `closure π(𝒩)Ω′`?

**Yes.** Fix `b`, `C` and `P={2b,2b+1}`. On a finite region containing `C` and the stars of its corners, `ω` has density `ρ=ρ_rest⊗¼(P_{E_P}+P_{X_P})`. Reason: each star density is a product of `P_{q_z}/2` or `P_{L_z}` on the even multiplicity, the full odd multiplicity, and a `λ`-isotypic projection that acts on representation factors only. The even multiplicities of the eight corners give `q_{w₁}⊗q_{w₂}⊗(⊗L_w)=E_P⊕X_P`. `g_C=1⊗x` on `V_{μ⃗_P}⊗M^C_{μ⃗_P}`, so `ρ′=ρ′_rest⊗¼(P_{E_P}+P_{Y_P})` with `Y_P=xX_P`. `E_P` lies in the range of `Q⁰` (sector `σ*` on `C`), `Y_P` in that of `Q¹` (sectors `σ*±hex_P`). So `ρ′=Q⁰ρ′Q⁰+Q¹ρ′Q¹`. `A_{2b}` flips `Z_{2b}`, so it exchanges `E_P` and `X_P`; then `A′_{2b}` exchanges `E_P` and `Y_P`, and `A′Q^κρ′=Q^{1−κ}A′Q^κρ′`. Any local `N∈𝒩` commutes with `Q⁰,Q¹`. Then
\[
\omega'(N^*A')=\sum_\kappa \operatorname{tr}(N^*Q^{1-\kappa}A'Q^\kappa\rho')=\sum_\kappa\operatorname{tr}(Q^\kappa Q^{1-\kappa}N^*A'Q^\kappa\rho')=0,
\]
using `Q^κρ′=Q^κρ′Q^κ`, cyclicity and `[N,Q^{1−κ}]=0`. Each `u′_b` is thus orthogonal to `π′(𝒩)Ω′`, hence to its closure; the image is the closed span of the `u′_b`. Under the proposed R-Φ the band is flux-carrying.

### 2.4 Odd `m=3,5,7` (Theorem 6)

Re-derived. Three points carry the proof.

- *Sectors.* On `C`, the corner charges in `σ→` are `3p_+`, `2p_++p_-`, `p_++2p_-`, `3p_-`. They are distinct because `p_+=p_-+1`. A hexagon move keeps every corner charge. So the eight sources `Rσ→` and eight targets `R(σ→+hex_P)`, `R∈O/C₃`, are sixteen distinct sectors.
- *Labels.* The label choice `b_+/b_-=ρ^{-1}` is needed. With it, `X_P` has the distinct eigenvalues `κa_-b_-ρ^{±1}`. With the other choice `X_P` has one double eigenvalue `κa_+b_-`; the target `q^+⊗q^-⊗φ` then has `κ′a_+b_-` twice, so an equivariant isometry needs `κ=κ′`, which Theorem 1 does not give. No `h` relates the two diagonal corners in `σ→`, so the choice is free.
- *Matching.* Both `κa_-b_-ρ` and `κ′a_-b_-` are eigenvalues of `L^M_r` on `M^C_{μ⃗}`, hence cube roots of one scalar (Theorem 1). So `κ/κ′` is a cube root of one, and both `X_P` eigenvalues occur in `κ′a_-b_-{1,ρ,ρ^{-1}}`.

### 2.5 Conjugation and the frame dependence of R-Φ (Theorem 7, Corollary 7.1)

Re-derived. `Φ` has dense range because `B=G(G^*BG)G^*`. It maps `H_phys` onto `H′_phys` because `A` is gauge invariant if and only if `GAG^*` is. Corollary 7.1 is exact: `u_b=π(A_{2b})Ω` with `A_{2b}∈𝒩`, and `Φu_b=u′_b` is orthogonal to `closure π′(𝒩)Ω′`. So R-Φ is a property of a band in one end-number frame. It is not invariant under the unitary equivalences of Theorem 7.

## 3. The GAPs the distiller marked

### G1. The cube-root step in Theorem 4: not a real gap in the draft

`GA15PHI.md` line 9: "Draft Lemma 4.4, Step 2 infers `θ++=θ--` from equality of their squares; that inference alone is invalid." The draft does not make that inference. `GA15PHI_DRAFT.md` line 177: "Apply both sides to `v_{s's}`: `θ_{ss'}θ_{s's}=c` for all `s,s'`. With `s=s'` and `s≠s'` this gives `a_+b_+=a_-b_-`, so `b_+/b_-=ρ^{-1}`." With the product form `θ_{ss'}=κa_sb_{s'}` (same line), the case `s=s'=+` gives `κ²a_+²b_+²=c` and the case `s≠s'` gives `κ²a_+a_-b_+b_-=c`. Dividing gives `a_+b_+=a_-b_-`. The step is valid as written. The distiller's own argument is also valid: `x=θ_{++}/θ_{--}` has `x²=1` and `x³=1` (Theorem 1 with `r³=1`), so `x=x³/x²=1`. Verdict: item 3 is an ERROR of attribution. The fix is edit E1 (§5). Theorem 4 itself is CORRECT.

### G2. The support condition in Theorem 8: a real gap, with a counterexample

Draft line 279: "let `P` be the projection onto `σ^→` on the links of a finite region. Every local link-only gauge-invariant operator `A` satisfies `AP=PAP`." As stated this is false. Counterexample. Take `m=1`, the plaquette `p` at `0` in the 1-2 plane with links `ℓ₁=(0,e₁)`, `ℓ₂=(e₁,e₁+e₂)`, `ℓ₃=(e₂,e₁+e₂)`, `ℓ₄=(0,e₂)`, the region `R={ℓ₁}`, and `A=B_p=W(∂p)+W(∂p)^†`. `A` is link-only and gauge invariant (`GA1_5.md` Theorem 3.1). Let `ψ` carry one colour-1 rishon on each of the four links: at the tails of `ℓ₁,ℓ₂` and at the heads of `ℓ₃,ℓ₄`. Then `P_Rψ=ψ`. One of `W(∂p)`, `W(∂p)^†` moves each rishon one step around the circuit `0→e₁→e₁+e₂→e₂→0`; at each shared site the colour contraction forces the colour index to 1, so it maps `ψ` to `±` the basis vector with the four rishons at the heads of `ℓ₁,ℓ₂` and the tails of `ℓ₃,ℓ₄`. The other one kills `ψ`: it needs a rishon at the head of `ℓ₁`. So `Aψ≠0` and `P_RAψ=0`. Hence `AP_R≠P_RAP_R`. The distilled Theorem 8 adds "`R` contains the support of `A`", and its proof is then complete: with `f=−δ≥0` divergence free and finite, `∑_ℓf_ℓ=∑_ℓf_ℓ(s(\mathrm{head})−s(\mathrm{tail}))=−∑_zs(z)(\operatorname{div}f)(z)=0` for `s(z)=z₁+z₂+z₃`, so `f=0`. (This one-line potential argument can replace the path argument; both are valid.)

### G2′. Sector preservation in Theorem 8: incomplete, closed here

`GA15PHI.md` line 125: "A finite product of GA1-P-5 sublayers preserves such a sector-carried state." Proof, line 127: "Apply the same argument to each local unitary gate and its adjoint to get sector preservation." The gate-level fact holds only for regions that contain the gate. A gate that crosses `∂R` need not commute with `P_R` (G2). The state-level step is missing. Referee closure:

*Claim.* Let `m∈{1,9}`, let `ω` be carried by `σ→`, and let `W_s=∏_{X∈ℱ_s}g_X` be a GA1-P-5 sublayer. Then `ω∘Ad W_s^*` is carried by `σ→`. By induction the same holds for a finite product of sublayers.

*Proof.* Fix a finite `R`. Let `R₁=R∪⋃\{X:X∩R≠∅\}`; it is finite by local finiteness. Let `G_R=∏_{X∩R≠∅}g_X`; the other gates commute with `P_R`, so `W_s^*P_RW_s=G_R^*P_RG_R`. Each `g_X` in `G_R` has support in `R₁`. Theorem 8 applied to `g_X` and `g_X^*` gives `g_XP_{R₁}=P_{R₁}g_XP_{R₁}` and `P_{R₁}g_X=(g_X^*P_{R₁})^*=P_{R₁}g_XP_{R₁}`, so `g_X` commutes with `P_{R₁}`. Since `P_{R₁}≤P_R`, `P_{R₁}G_R^*P_RG_RP_{R₁}=G_R^*P_{R₁}P_RP_{R₁}G_R=P_{R₁}`. A projection `Q` with `P_{R₁}QP_{R₁}=P_{R₁}` satisfies `Q≥P_{R₁}`. So `ω(W_s^*P_RW_s)≥ω(P_{R₁})=1`. □

With this closure, item 45 becomes CORRECT. The consequence `GA15PHI.md` draws (no conjugate of a `σ→`-carried state has an R-Φ band) then follows from the first two claims of Theorem 8.

### G3. Attack A3 at `m=1,9`: a real gap, and the draft's failing step is false

Draft line 286: "So the target space of Lemma 4.4, Step 3, equals the half-turn image of the source space, and the gate cannot fix one and exchange the other. The failing step is orthogonality of target and source." `GA15PHI.md` line 135 rightly refuses to call this a theorem. The sentence does not prove what it says. Rotation invariance forces only this: a gate that fixes `E_P` also fixes `L_hE_P`, and a gate that sends `X_P` into the reversed sector `hσ` sends `L_hX_P` back into `σ`. Unitarity and `D₃` invariance allow such an exchange. Lemma 4.4's formula `J_P=(F+Ad L_h F)/√2` fails here, because its two ranges are no longer orthogonal to the sources. A different formula, `J_P=F+F^*` with `F:X_P→L_hX_P`, works when an `r`-equivariant `F` with `Ad L_h(F)=F^*` exists. §4 shows it exists. Verdict on the lane question: the draft's A3 obstruction is an attempt, not a theorem; and it is false as an obstruction.

## 4. Referee closure R1: GA1-5-Φ at `m=1` and `m=9`

New, written by this referee, not yet checked by anyone. It uses only results checked above: Theorems 1, 2 and 7, the R-Φ argument of Theorem 5 (§2.3), and the imports of §2.1. It credits the draft's attack A3 for the sector.

**Theorem R1.** Let `m∈{1,9}`. For all allowed `ε,μ,τ_E` there are a member `W′_B=GW^{swap}W_EG^*W_E^{-1}` of GA1-P-5, admissible under NN-a, and a locally gauge-invariant empty-matter D1 state `ω′` of `U′_B=W′_BW_EM_oM_e`, with a band `(1,F,e^{−iK·1})` in `H′_phys` whose image is orthogonal to `closure π′(𝒩)Ω′`. It has a node at `K=0` and every `N_j=1`. On the support of `ω′`, `A′_{2b}` exchanges the sector `σ_A` of its even cube with the reversed sector `hσ_A`.

*Proof for `m=1`.*

*Step 0 (no signs).* A link register is `C^{10}`: one rishon, at one end, with one of five colours. A lift sends "every rishon mode at its `z`-end to the same flavour at the `gz`-end of the image link" (`LW1_5.md` line 261, quoted at draft line 116). It maps one-rishon basis vectors to one-rishon basis vectors and permutes link factors, which are ordinary tensor factors. So on a cube `C` the lift of `R∈O` is the permutation unitary `L_R` of these basis vectors, and `R↦L_R` is a representation: `L_r³=1`, `L_h²=1`, `L_rL_h=L_hL_r^{-1}`. The same holds for the swap identifications `ι`.

*Step 1 (the sector `σ_A`).* Each cube `D` of either tiling has one body diagonal `P_D` joining its corners of classes `000` and `111` (in `2b+1+\{0,1\}³` the corner `2b+1+c` has class `1−c`). In `σ_A`, every link of `D` at a corner of `P_D` has its rishon at that corner. Each link of `hex_{P_D}` has its rishon at its forward end for one orientation of the hexagon. Choose the orientation on one even and one odd cube; extend by `2Z³`. On `\{0,1\}³` the point reflection `x↦1−x` maps the cycle `100→110→010→011→001→101→100` to `011→001→101→100→110→010→011`, the same cyclic order. So reflection through the centre `c_D` preserves `σ_A` on `D`. Reflection through any cube centre `c` equals translation by `2(c−c_D)∈2Z³` after reflection through `c_D`, since cube centres lie in `c₀+Z³`. So `σ_A` is invariant under `2Z³` and under every reflection through a cube centre. Every swap pair is therefore matched. Every end number is `0` or `1`, so `W_E` is the scalar `e^{−iτ_E/4}` on `σ_A`.

*Step 2 (one cube).* Fix the even cube `C` at `2b`, `P=P_C=\{w₁,w₂\}`, `w₁=2b`, `w₂=2b+1`. In local coordinates let `r:(x,y,z)↦(z,x,y)` and `h:(x,y,z)↦(1−y,1−x,1−z)`. `r` fixes `w₁,w₂` and keeps the hexagon orientation; `h` exchanges `w₁,w₂` and reverses it. In `σ_A`, `w₁` and `w₂` have three occupied `C`-ends, so `E_{w_i}=(C⁵)^{⊗3}`. Each hexagon corner has one occupied `C`-end, the hexagon link arriving there; so `E_w=V` with a one-dimensional multiplicity. `hσ_A` agrees with `σ_A` at `w₁,w₂` and occupies the other hexagon end at each hexagon corner. A rotation that fixes `σ_A` on `C` fixes `\{w₁,w₂\}`, the only corners with three occupied `C`-ends, and keeps the orientation; so the stabilizer is `⟨r⟩`. The orbit `Oσ_A` has eight distinct members, labelled by a diagonal and an orientation.

Take `μ₀,q` from Theorem 2 with `p=1`; for `p=1`, `T` differs from the plain permutation action by `sgn`, so `q` is invariant under both. `r` cycles the ends at `w₁`. Let `e_±(w₁)` be its eigenvectors on `q_{w₁}`, with eigenvalues `a_±`, and `ρ=a_+/a_-∈\{ω,ω²\}`. Put `e_±(w₂)=L^M_he_±(w₁)`. By `L_rL_h=L_hL_r^{-1}`, `r` has eigenvalue `a_±^{-1}` on `e_±(w₂)`. Let `ℓ∈M[σ_A]` and `ℓ′∈M[hσ_A]` be the products, over hexagon corners, of the canonical generators `k↦|\text{colour }k\text{ at the occupied end}⟩`. `L_r` sends each canonical generator to the one at the image corner. So `L^M_rℓ=ℓ`, `L^M_rℓ′=ℓ′` and `L^M_hℓ=ℓ′`. Put `v_{ss′}=e_s(w₁)⊗e_{s′}(w₂)⊗ℓ` and `v′_{ss′}=e_s(w₁)⊗e_{s′}(w₂)⊗ℓ′`. Then
\[
L^M_rv_{ss'}=a_sa_{s'}^{-1}v_{ss'},\quad L^M_rv'_{ss'}=a_sa_{s'}^{-1}v'_{ss'},\quad L^M_hv_{ss'}=v'_{s's},\quad L^M_hv'_{ss'}=v_{s's}.
\]
Let `E_P=span\{v_{++},v_{--}\}`, `X_P=span\{v_{+-},v_{-+}\}`, `X′_P=L^M_hX_P=span\{v′_{+-},v′_{-+}\}`. The `r` eigenvalue is `ρ` on `v_{+-}` and `v′_{+-}`, and `ρ^{-1}` on `v_{-+}` and `v′_{-+}`.

*Step 3 (the gate).* Define `f:X_P→X′_P` by `fv_{+-}=v′_{+-}`, `fv_{-+}=v′_{-+}`. (i) `fL^M_r=L^M_rf`, by equal eigenvalues. (ii) `L^M_hfL^M_h=f^*`: `L^M_hfL^M_hv′_{+-}=L^M_hfv_{-+}=L^M_hv′_{-+}=v_{+-}=f^*v′_{+-}`, and likewise on `v′_{-+}`. Put `F=1_{V_{μ⃗}}⊗f`, extended by `0`, and `J_P=F+F^*`. `J_P` is self-adjoint, and `J_P²` projects onto `V⊗(X_P⊕X′_P)`. `J_P` commutes with `G_C` (Theorem 1), with `L_r` by (i) and with `L_h` by (ii); `r,h` generate `D₃`. Transport `J_P` to the other diagonals by `O`; this is well defined. The four operators act in the eight distinct sectors of Step 2, so their supports are orthogonal, and `V⊗E_P` is orthogonal to all of them. Let `J` be their sum, `Π=J²`, and `g_C=1−Π−iJ=exp(−i(π/2)J)`. `g_C` is unitary, commutes with `G_C`, is `O`-invariant, fixes `V⊗E_P`, and maps `V⊗X_P` onto `V⊗X′_P⊂H_C[hσ_A]`. Transport `g_C` to all even cubes by `𝒢`; let `G` be the product. §2.1 applies word for word: `W′_B∈`GA1-P-5, admissible under NN-a.

*Step 4 (the neutral band on `σ_A`).* Let `Γ` be generated by `2Z³` and the reflections through cube centres; `Γ=2Z³⋊\{1,P_{c₀}\}`. `Γ` acts freely on sites (its reflections fix only half-integer points), with the four orbits `\{\text{class }c,\text{ class }1−c\}`. Choose star data at `0,e₁,e₂,e₃` and transport them by `Γ`. At `0`: `q` on the even triple, type `μ₀`; on the odd triple (also three occupied ends: `0` lies on `P_D` of its odd cube `D`) a type `μ₁′` with its full multiplicity; a star type `λ₀` in `V_{μ₀}⊗V_{μ₁′}`. At `e_i`: each triple has one occupied end, the star is `V⊗V`; choose `λ∈\{S²V,Λ²V\}`. Let `ω` be empty matter times the product of normalized projections onto these `K_z`, on `σ_A`. As in `GA1_5.md` Theorem 6.3, `ω` is locally gauge invariant and `2Z³`-invariant. Each swap gate uses `ι` induced by a reflection in `Γ`, so `ι(K_v)=K_{a(v)}` and the gate preserves `ω`. `W_E` is a scalar and the matter gates fix empty matter. So `ω` is a D1 state of `W^{swap}W_EM_oM_e`. At `w₂` the state's subspace `ι(q_{w₁})` equals `L^M_hq_{w₁}`: the two maps differ by a permutation of the ends at `w₂`, which preserves `q`. Let `e_±` at `0` be as in Step 2, `X₀=|e_+⟩⟨e_-|+|e_-⟩⟨e_+|` on `q₀`, `A₀=1⊗X₀` on type `μ₀` of the even triple in `σ_A` and zero elsewhere, and `A_{2b}` its translate. The `u_b=π(A_{2b})Ω` are orthonormal (product state, `tr X₀=0`, `tr X₀²=2`). The odd and then even identifications compose to the translation lift by `−2·1` (reflections through `2b−c₀` and `2b−3c₀`, `GA1_5.md` §3.9); by Step 0 they agree exactly. Each swap gate commutes with the support projection of `ω`. So `𝕍^*A_{2b}𝕍Q=A_{2b−2·1}Q`, and `GA1_5.md` Theorem 6.1 gives `Ũu_b=u_{b−1}`.

*Step 5 (conjugation and R-Φ).* On `C` the even-multiplicity density of `ω` is `¼P_{E_P⊕X_P}`. Put `ω′=ω∘Ad G^*` and `A′_{2b}=GA_{2b}G^*`. Theorem 7 gives a D1 state of `U′_B` and the band `(1,F,e^{−iK·1})` in `H′_phys`, node `0`, every `N_j=1`. §2.3 applies with `Q⁰` the projection onto `σ_A` on `C`, `Q¹` onto `hσ_A` on `C`, and `Y_P=X′_P`. So `ω′(N^*A′_{2b})=0` for every local `N∈𝒩`. □

*Proof for `m=9`.* Replace rishons by holes. A link of `L5-U[9]` holds one hole. Order its ten modes `x`-end first. A colour-preserving bijection `π` onto the image link keeps the end order (`π(j)=j`) or swaps it (`π(j)=j±5`). It maps `|\text{hole at }j⟩` to `\operatorname{sgn}(π)(−1)^{j−π(j)}|\text{hole at }π(j)⟩`, and this sign does not depend on `j`. So each lift is a constant sign times the permutation of hole states; conjugation ignores the constant, and Step 0 holds for hole permutations. Put end number `5−k` where `σ_A` has `k`. `P_C` corners have three ends at `4`; hexagon corners have two at `5` and one at `4`. Take `q` from Theorem 2 with `p=4`. `(p−9/2)²=1/4` on every link. Steps 1-5 run unchanged. □

**Why A1 and A2 do not block R1.** `σ_A` is not uniform, so A1's obstruction (no uniform `m/2`) does not apply. `σ_A` is not `σ→`, and its hexagon links can move, so Theorem 8 does not apply. Theorem 8 is a property of `σ→`, not of odd `m`.

## 5. Required edits to `GA15PHI.md`

None of E1-E7 changes a theorem. E8 depends on the owner's choice in §6.

- **E1 (item 3; lines 9 and 60).** Line 9: replace "Draft Lemma 4.4, Step 2 infers `θ++=θ--` from equality of their squares; that inference alone is invalid. The cube-root condition closes it in Theorem 4 below." with "Draft Lemma 4.4, Step 2 is valid: the cases `s=s′` and `s≠s′` of `θ_{ss′}θ_{s′s}=c`, with `θ_{ss′}=κa_sb_{s′}`, give `a_+b_+=a_-b_-`. Theorem 4 adds a second argument by the cube root." Line 60: replace "**GAP in the draft's inference:** equality of squares alone permits a minus sign. Here Theorem 1 also gives" with "The case `s≠s′` gives `θ_{++}²=c=θ_{+-}θ_{-+}`, hence `a_+b_+=a_-b_-`. Alternatively, Theorem 1 gives".
- **E2 (item 45; lines 125, 127).** Replace the last sentence of Theorem 8 with "Conjugation by a finite product of GA1-P-5 sublayers maps a state carried by `σ→` to a state carried by `σ→`." Replace its proof sentence with the proof of G2′ (§3), credited "referee closure, `GA15PHI_REFEREE.md` §3".
- **E3 (item 46; line 129).** Add the explicit counterexample of G2: `m=1`, `R=\{ℓ₁\}`, `A=B_p`.
- **E4 (item 21; line 50).** After "proving orthonormality" add: "for `b≠b′` the product form of `ω` gives `ω(A_{2b}^*A_{2b′})=\overline{ω(A_{2b})}ω(A_{2b′})=0`."
- **E5 (item 34; lines 97, 105).** The gate of Theorem 6 maps `X_P` into `σ→+hex_P` for one chosen orientation. Write "`σ→+hex_P`" for "`σ→±hex_P`".
- **E6 (item 36; line 101).** Replace "Each corner has no nontrivial stabilizer within the sector's `𝒢` stabilizer" with "Each hexagon corner has trivial stabilizer in `2Z³⋊⟨r⟩`, the stabilizer of `σ→` in `𝒢`".
- **E7 (item 39; line 109).** Replace "let `ω` be an empty-matter D1 state" with "let `ω` be an empty-matter D1 state of `U_B=W_BW_EM_oM_e`".
- **E8 (items 5, 6, 49; lines 9, 11, 131-135).** Either form, as §6 decides. (a) Add Theorem R1 with its proof, credited "referee closure, `GA15PHI_REFEREE.md` §4, completing draft attack A3; unrefereed"; change line 5 to "for every `1≤m≤9`, with `m=1,9` by an unrefereed referee closure"; delete GA1-5-Φ[`m=1,9`] from line 11; at line 135 replace the A3 paragraph by "A3 succeeds with the gate `J_P=F+F^*` of Theorem R1; its draft failing step is false." (b) Keep GA1-5-Φ[`m=1,9`] open and add at line 135: "The draft's failing step is false. A referee closure (`GA15PHI_REFEREE.md` §4) completes the route and awaits a check."

## 6. Open statements to carry, and the freeze recommendation

**Open statements, by name.**

- **R1-check.** One check of closure R1 (§4). Until it is checked, GA1-5-Φ[`m=1,9`] stays open with R1 as its candidate proof. The points a checker should press: the sign-free lift of Step 0 (and the `j`-independent sign at `m=9`); the identities `L^M_hv_{ss′}=v′_{s′s}` and (ii) of Step 3; the claim that `Oσ_A` has eight distinct members on `C`; and the `Γ`-transport of Step 4.
- **GA1-5-O.** A propagating band on `L5-O[S_+]`. Theorem 7 needs a neutral band to conjugate; none is known there (`GA1_5.md` §7).
- **Electric half of GA1(a)(4).** No energy functional is compared. The band supplies none.
- **Flux content up to conjugation.** Corollary 7.1 shows that R-Φ is not invariant under the unitary equivalences `Φ` of Theorem 7. A frame-independent notion, or a physical rule that fixes the frame, is an owner question if wanted. Nothing is proposed here; any proposal would need the four-test check.

These do not block a freeze; none is an error of `GA15PHI.md`.

**What was checked against the owner reading.** NN-a was read plainly, as `TOE_ASSEMBLY.md` line 233 states it. The only use of it is Proposition C(ii) plus the covariance of the complete update (§2.1). No hostile reading of any axiom was used, and none is needed.

**Freeze recommendation.** Freeze `GA15PHI.md` after E1-E7. Its main line is correct: for `m=2,…,8`, under the proposed class GA1-P-5, the owner's NN-a and the imported `GA1_5.md` closures (Proposition C, Lemma S1′, Proposition S-odd, §3.9, labelled unrefereed there), there is an admissible layer and an empty-matter D1 state with a propagating band in `H_phys`, node at `K=0`, every `N_j=1`, whose image is orthogonal to `closure π(𝒩)Ω`. For E8 the referee recommends form (a), on the precedent of `GA1_5.md` line 9, which carries referee closures labelled "unrefereed" into a frozen file. Form (b) is the cautious alternative. The choice is the owner's. Under either form, the frozen text should keep Corollary 7.1 and line 121 prominent: the band meets R-Φ, yet it is a conjugated neutral mode, so R-Φ alone does not identify a gauge boson.

## 7. Prior work used

Ported with credit, not re-derived beyond the checks named in §2. All in this folder at `15bc39079`.

- `GA1_5.md` Theorem 2.1 (link-cube incidence, cube stabilizer `O`, site stabilizer `C₃`): used in §2.1 and R1 Steps 2-3.
- `GA1_5.md` Theorem 2.2 (disjoint covariant supports keep parity-split charges): used only to confirm `GA15PHI.md` §9.
- `GA1_5.md` Theorem 6.1 (empty-matter reduction and spanning): used in §2.2, G2′ context and R1 Steps 4-5.
- `GA1_5.md` Theorem 6.2 (cube-supported layers are flat at nodes): used to confirm it does not apply (§2.2).
- `GA1_5.md` Theorem 6.3, Lemma S1′, Proposition S-odd and the §3.9 identification (swap gates, covariance, band motion): used in §2.1, §2.4 and R1 Step 4. These are referee closures of `GA1_5_REFEREE.md`, labelled unrefereed in `GA1_5.md` line 9.
- `GA1_5.md` Lemma U and Proposition C (NN-a compilation): used in §2.1 and R1 Step 3; same status.
- `GA1_5.md` Theorem 6.4 and §7 (GA1-5-Φ attacks 1-3): used to confirm `GA15PHI.md` §9.
- `GA15PHI_DRAFT.md` (Claude Opus 5.5, pass 1): its attack A3 supplies the sector `σ_A` of R1; its Lemma 4.4 Step 2 is the valid step of G1.
- `GA15PHI.md` (Codex `gpt-6.1-terra`, pass 2): Theorems 1, 2, 4, 7, 8 and the R-Φ argument of Theorem 5, as checked in §§1-3, are the inputs of R1 and G2′.
- `TOE_ASSEMBLY.md` section 3.7 (owner decision NN-a, 2026-11-06): used as stated.
- `prior/GA15PHI.md`: read in full. It reports no completed GA1-5-Φ result. Its "missed inputs" (finite-square join, Floquet energy fork, growing-spin mechanism, ice stiffness) bear on the electric half and on photon identification, not on any step checked here.

**Prior work the digest missed.** None found in the files read. This referee ran no repository-wide search.

---

## FINISH

**Proved here (pass 3; re-derived by hand; no computer-assisted step; no `[check]` was run).**
- The main line of `GA15PHI.md` is correct: Theorems 1-7, Corollary 7.1 and the first two claims of Theorem 8 (§1, §2). Under the proposed GA1-P-5, the owner's NN-a and the imported `GA1_5.md` closures, GA1-5-Φ holds for `m=2,…,8`. `G` and `W′_B` are in the class and admissible under NN-a (§2.1). The band lies in `H′_phys` of the stated D1 state, with a node at `K=0` and every `N_j=1` (§2.2). Its image is orthogonal to `closure π′(𝒩)Ω′` (§2.3).
- G1: draft Lemma 4.4, Step 2 is valid as written; the distiller's GAP misreads it (§3).
- G2′: conjugation by finitely many GA1-P-5 sublayers keeps a state carried by `σ→` carried by `σ→` (§3).
- Closure R1: GA1-5-Φ holds at `m=1` and `m=9` on the sector `σ_A` of draft attack A3, with the gate `J_P=F+F^*` (§4). New and unchecked.

**Counterexamples.**
- To draft Lemma 6.1 as stated (any finite region): `m=1`, `R=\{ℓ₁\}`, `A=B_p` gives `AP_R≠P_RAP_R` (§3, G2).
- To the failing step of draft attack A3 ("the gate cannot fix one and exchange the other"): the gate `g_C` of R1, Step 3, fixes `V⊗E_P` and exchanges `V⊗X_P` with `V⊗L_hX_P`.

**Open by name.** R1-check; GA1-5-O; the electric half of GA1(a)(4); flux content up to conjugation (an owner question, if wanted). See §6.

**What changes downstream.**
- GA1-5: the open item GA1-5-Φ can be recorded as answered for `m=2,…,8` at freeze, and for `m=1,9` as E8 decides. The answer does not identify a gauge boson.
- R-Φ: it is a property of a band in one end-number frame (Corollary 7.1). Any later use of R-Φ as a photon criterion inherits this.
- LZ1: one more one-way propagating physical band with every `N_j=1`, with image orthogonal to `ker(Ũ−1)`. It says nothing about a common Clifford cone.
- EW1, VC1, GA2/Y2-W, ZM1_OBS: nothing changes. The state is a chosen stationary state, not the VC1 vacuum.
- No axiom, law, reading, class, vacuum or working-set entry is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
