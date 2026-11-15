# SGAPT: S-GAP at nonzero hopping

**Status.** S-GAP at nonzero hopping, node S, is **OPEN**. The conditional block comparison, first-order finite-ring bound, local spectral resonances, free-light correlation bound, localized removal identity, window example and two-bond bound below are proved subject to the stated finite-ring inputs. They have not had the fresh-session referee. **GAPs:** the draft does not establish a volume-uniform remainder, divergence of the complete polymer link, or a flux bound for its localizers. Its claims that these routes fail in general exceed the calculations. **Open by name:** SGAPT-R, LOC, S-GAP-LL and S-GAP-CDW, plus the inherited items in §8. No reading, law, axiom or working-set entry is adopted.

**Provenance.** Pass 1: Claude Opus 5.5, max, `SGAPT_DRAFT.md`. Pass 2: Codex `gpt-6.1-terra`; effort and session id: see run log. Source SHA-256: `SGAPT_DRAFT.md` `b6eab250bcb55520c1368832fe928e74df17e1e969d55e3ea78c6d27e81c378d`; `prior/SGAPT.md` `219058fbdff320fc6ceb6749bae812a75c90a5c32ab99640c9d208c90e82b94e`; `SGAP.md` `2a3a06e7a273c9249ab4192a9625939bcb904171d19a2580f1c13b1ef9fbf89e`; `SMG15.md` `b65cf2e1b52ff83b756e355b1293e54754da89be4bfa4db3bbd0502573b6a995`; `SMG1.md` `1e5a05a66d0b11016d18264351321165979d569cd84ad213e1dc4072cb021622`; `SMG1_TREE.md` `ff2904913d409cc0d49cbf1671a24cdb53f3db91d215c7583c7127dda3d7d232`; `TOE_ASSEMBLY.md` `f443399e659c5411177e1735449c292e0465bee12f8d177193a44ead08fdd8b5`; `SGAP0.md` `aea9b1ce9c107bf3540e3f6dc17d2b22553f3ef40065d531c5947c6ef3db2fbd`. Historical revision claims in pass 1 were not refreshed. Pass 1 reports no numerical checks. This is an author-side distillation, not an independent audit.

## 1. Definitions inferred by the distiller

These fix mathematical notation; they add no physical premise.

1. Use the model of `SGAP.md` Definitions 1–4. Let `L∈4ℕ`, `L≥8`, `τ>0`, `t,ε∈ℝ`, electric coupling zero, and light number `N=L/2`. The eight mirror Majoranas at site `x` are `γ_{x,a}` and the light mode is `c_x`. Put `Λ_x=c_x†c_{x+1}+c_{x+1}†c_x`, with indices modulo `L`, and `T_{x,a}=iγ_{x,a}γ_{x+1,a}Λ_x`. The Hamiltonian is `Hε=HM+HL+εH4`, `HM=τ∑x(Wx+14)`, `HL=−t∑x hop_x`, `H4=∑x,a T_{x,a}`. Here `hop_x` includes its gauge link; `Λ_x` does not.
2. Let `S`, the eight odd characters `ρ_a`, the even-character group `Ŝ_+` and one-dimensional configuration vectors `e_χ` be as in `SMG15.md` Theorems 1–2. The atom has shifted energies `0,14τ,16τ` on `1`, the odd lines and the seven nontrivial even lines, respectively (`SMG1.md` Theorem 2.2). Set `q(ξ)=∏x ξ_x`. In either holonomy `w=±1`, the half-filled space is `𝓜_+⊗𝓕_{L/2}`, where `𝓜_+` contains configurations with `q∈Ŝ_+`. Even mirror and light operators act on their respective factors. The reduced light Hamiltonian is

   `h^(w)=−t∑_{x<L−1}Λ_x−twΛ_{L−1}`.

   The undressed `T_{x,a}` has no holonomy factor, including at the wrap bond. It sends `ξ` to `ξ^{x,a}`, obtained by multiplying both endpoint characters by `ρ_a`, with mirror amplitude of modulus one and light factor `Λ_x`. Let `E_σ` be the least energy in charge `σ` over both holonomies and `E_0=minσ E_σ`.
3. S-GAP asks for `c₀,Δ>0` such that `E_σ≥E_0+Δτ` for all allowed `L`, all `τ>0`, `|t|,|ε|≤c₀τ` and all `σ≠1`. The allowed nontrivial charges are the seven nontrivial elements of `Ŝ_+`. A uniform positive lower bound for all `E_σ−E_1` is equivalent to S-GAP: it makes the neutral sector the global minimum. This is a finite-ring target, not a GNS or tick gap.
4. For an arc `I`, write `P_I=∏_{x∈I}P_x^1`, `Q_I=1−P_I`, and `𝒩=∑x(1−P_x^1)`. An arc may be the entire ring. A local operator means the restriction of an even operator in the full matter CAR algebra on `I`; number-conserving operators preserve the fixed-number sector. Norms of local operators below may be taken on the full local Fock space, so vacuum compression is unambiguous. Holonomy-dependent operators are understood blockwise, with norms and maxima over both blocks. This convention avoids defining a full local algebra solely inside the fixed-number subspace.
5. A localizer at `y` for charge `σ` is a real function `χ_y(ξ)` supported on configurations with `ξ_y=σ`. For a normalized charged vector `Ψ=∑ξ e_ξ⊗ψ_ξ`, set

   `wχ=∑y‖χ_yΨ‖²`,

   `Φ(χ)=∑y,x,a,ξ(χ_y(ξ^{x,a})−χ_y(ξ))²‖ψ_{ξ^{x,a}}‖‖ψ_ξ‖`.

   The sum includes both orientations of every configuration move. The definition extends blockwise to a ground vector spanning holonomies by summing its block contributions.

**Proposed readings, not adopted.** `SMG15.md` proposes R15-SPEC under the owner-selected SMG1-GAP generator reading. The four tests recorded in `SGAP.md` are `C,P,P,C`: the finite-ring and canonical-sector bridge makes test 4 conditional. R-COR is proposed as a diagnostic; its recorded tests were `C,P,C,P`, but it fails test 3 as a reading of “gapped” after SMG1-GAP. The ratio `ε²/(τ|t|)` is a proposed weak-interaction diagnostic, undefined at `t=0`. The S-GAP⁰ subcase has four recorded passes; it is not a new reading. This item proposes no further reading. See `TOE_ASSEMBLY.md` §§3.4–3.6 for the owner decisions; finite rings alone do not supply the GNS or tick bridges.

## 2. Inputs already proved in the repository

`SGAP.md` Theorems 1–3 prove charge bookkeeping, `E_σ−E_1=16τ` at `ε=0`, and the charge-removal conjugation. `SGAP0.md` Theorem 9 proves S-GAP⁰ with `c₀=2·10⁻¹⁰`, `Δ=7`. `SMG15.md` Theorem 3 already proves the configuration-conserving charged bound `14τ−2δ`; its Theorem 7 already proves the atomic resolvent and formal second-order light term. `SGAP.md` Theorem 5 already proves the unlocalized removal identity; A4 remains open. `SGAP.md` A5 disproves the unrestricted strict local-window comparison. These are scoped inputs, not new results of this item. `prior/SGAPT.md` records their provenance and further prior work. Frozen author status is not an audit verdict.

## 3. Defect-relative comparison

**Theorem 1 (vacuum compression and block criterion; draft A.0 and A).** Let `V_I` be even, self-adjoint, number conserving and supported on `I`. Its vacuum compression defines an even local light operator `ℓ_I` by `P_IV_IP_I=ℓ_IP_I`, with `‖ℓ_I‖≤‖V_I‖`. If `V_I` commutes with `P_I`, put `δ_I=‖V_I−ℓ_I‖` and `d=max_x∑_{I∋x}δ_I`. Suppose a unitary `U` preserves the global charge, number and holonomy and

`UHεU*=HM+∑_I V_I+R`,

with a finite family of arcs, self-adjoint `R` and `d≤14τ`. Then for each `σ≠1`,

`E_σ−E_1≥14τ−d−2‖R‖`.

*Proof.* Expand `V_I` into products of mirror and light monomials. The mirror vacuum on `I` is a rank-one even vector. Its expectation kills odd mirror monomials, giving `ℓ_I`; compression is contractive. Uniqueness holds as an operator on the full local light Fock space. Number conservation passes to the compression.

Because `[V_I,P_I]=0` and `P_I(V_I−ℓ_I)P_I=0`, one has `V_I−ℓ_I≥−δ_I Q_I`. The commuting projectors obey `Q_I≤∑_{x∈I}(1−P_x^1)`. Thus, for `H_eff=∑Iℓ_I`,

`UHεU*≥H_eff+(14τ−d)𝒩−‖R‖`.

Let `e_eff` be the least half-filled light energy of `H_eff` over holonomies. On a charged sector `𝒩≥1`, so its lower bound is `e_eff+14τ−d−‖R‖`. On the neutral all-vacuum mirror vector tensored with a light ground vector of `H_eff`, the expectation is at most `e_eff+‖R‖`. The variational principle and the charge-preserving `U` give the result. `□`

This needs no light spectral gap. For `U=1`, `R=0`, and the configuration-conserving bonds of `SMG15.md` Theorem 3, `δ_I≤δ` and each site meets two bonds, so `d≤2δ`. The theorem recovers that already-proved charged bound, under its hypotheses.

**Theorem 2 (first-order dressing; draft B.1 and B).** For every allowed `L`, real `t` and `|ε|≤7τ/8`,

`E_σ−E_1≥14τ−16|ε|−(2L|ε|/τ)(12|t|+144|ε|)`.

If `|t|,|ε|≤c₀τ`, `c₀>0`, and `L≤(7−16c₀)/(312c₀²)`, the lower bound is at least `7τ`.

*Proof.* For a move `ξ→ξ^{b,a}` let `Δ_{b,a}(ξ)` be its atomic-energy change divided by `τ`. A single site contributes `14`, `−14`, `2`, or `−2`, so `Δ∈{0,±4,±12,±16,±28}`. Define diagonal `K_{b,a}=1/Δ` on nonzero entries and zero otherwise; define `T^0=T1_{Δ=0}` and `T^≠=T−T^0`. The move reverses `Δ`, hence `T^0,T^≠` are Hermitian contractions, `TK` is anti-Hermitian, `‖K‖≤1/4`, and `[HM,TK]=τT^≠`. Since a vacuum bond changes energy by `28τ`, `T^0` annihilates its vacuum on both sides. These operators are bond-supported and preserve charge, number and holonomy.

Set `S=(ε/τ)∑_{b,a}T_{b,a}K_{b,a}` and `k_b=−t hop_b+ε∑a T^0_{b,a}` in each holonomy. Then `[S,HM]=−εT^≠`, `‖S_b‖≤2|ε|/τ`, and `‖k_b‖≤|t|+8|ε|`. The Duhamel identity gives

`e^S Hε e^(−S)=HM+∑b k_b+R`,

`R=∫₀¹e^{uS}([S,∑b k_b]+u[S,εT^≠])e^(−uS)du`.

Even operators on disjoint bonds commute; each bond meets at most three bonds. Therefore

`‖R‖≤12L|ε|(|t|+8|ε|)/τ+48Lε²/τ=L|ε|(12|t|+144|ε|)/τ`.

The compression of `k_b` is its light hop, `δ_b≤8|ε|`, and `d≤16|ε|≤14τ`. Theorem 1 gives the first bound. The second follows from `2L|ε|(12|t|+144|ε|)/τ≤312Lc₀²τ`. `□`

The undressed choice `U=1` also gives `d≤16|ε|`, `‖R‖≤8L|ε|`, and `E_σ−E_1≥14τ−16|ε|−16L|ε|` when `16|ε|≤14τ`. Theorem 2 improves that upper estimate on the remainder. Its bound is extensive; it does not prove an extensive lower bound on `‖R‖` or rule out a different dressing. The draft's assertion that no finite-order dressing can eliminate volume dependence is **GAP**. Its `√L` argument concerns a formal leading term, not the full remainder.

## 4. Local resonances

For a proper arc of `ℓ` sites, `2≤ℓ≤L−1`, let

`G_I=τ∑_{x∈I}(W_x+14)−t∑_{b⊂I} hop_b`.

Gauge away the possible wrap-bond sign on this open arc. Put `n=⌊ℓ/2⌋`, `ε_k=−2t cos(πk/(ℓ+1))`, and `E_A=∑_{k∈A}ε_k` for `|A|=n`. Let `𝓗_+` have vacuum mirror configuration and `n` light particles on the arc, and let `𝓗_pair` have `(ρ_a,ρ_a,1,…)` and the same light number.

**Theorem 3 (draft C).** For `t≠0`, the block spectra are `{E_A}` and `{28τ+E_B}`. Every point between `E_min=min_A E_A` and `E_max=max_A E_A` is within `π|t|/(ℓ+1)` of an `E_A`, and `E_max−E_min≥|t|(ℓ−1)`. If `ℓ≥1+28τ/|t|`, the two spectra come within `π|t|/(ℓ+1)`. If the commutator map on all operators `𝓗_+→𝓗_pair` is invertible, its inverse norm is at least `(ℓ+1)/(π|t|)`. As allowed arc lengths and rings vary, exact coincidences occur at a dense set of `t` in every `[-c₀τ,c₀τ]`. At a coincidence, `[G_I,X]=Y` has no solution if `Y` has a nonzero matrix element between the coinciding eigenvectors.

*Proof.* Open-chain sine waves have one-particle energies `ε_k`; Slater determinants give the block spectra, with a `28τ` atomic shift for the pair. Order `ε_k` increasingly. Move particles one at a time from the lowest `n` levels to the highest `n`, always keeping distinct levels. Each step changes energy by at most `2π|t|/(ℓ+1)`. Thus every intermediate energy is within half that step of a sum. By spectral reflection and `cos(πu)≥1−2u` for `0≤u≤1/2`,

`E_max−E_min=4|t|∑_{k=1}^n cos(πk/(ℓ+1))≥|t|(ℓ−1)`.

If the width is at least `28τ`, approximate `28τ+E_min` by an `E_A`. A rank-one eigenoperator gives the inverse bound. For any `0<a<b`, take `ℓ` large enough that the adjacent increments divided by `|t|` are below `28τ/a−28τ/b` and the total width divided by `|t|` exceeds `28τ/a`. Some increment-path difference `g` lies in `(28τ/b,28τ/a)`; setting `t=28τ/g` gives a coincidence in `(a,b)`. Negative `t` follows by symmetry. At coincidence the relevant matrix element of `[G_I,X]` is zero. `□`

The density statement varies `L` with `ℓ`; a fixed finite ring has only finitely many arc lengths. **GAP:** coincidence alone does not show that the actual perturbation has a nonzero resonant matrix element, nor that every convergent block scheme fails. The argument establishes a spectral obstruction to a uniform inverse on the full operator space. Leaving light hopping out of `G_I` avoids this particular denominator but regenerates commutators such as `[S,HL]`.

## 5. Free-light linked correlation

Take `w=−1`, `t≠0`, `c_{x+L}=−c_x` and `Λ̃_x=c_x†c_{x+1}+c_{x+1}†c_x`. Let `Φ₀` be the unique half-filled free ground vector, `E_L` its energy, and

`C(x,s)=⟨Φ₀,Λ̃_x e^(−s(h−E_L)) Λ̃_0 Φ₀⟩−⟨Λ̃_x⟩⟨Λ̃_0⟩`, `s≥0`.

**Theorem 4 (draft D).** For every `s≥0`, `∑x C(x,s)=0` and `∑x(−1)^xC(x,s)≥0`. Moreover,

`∑x∫₀∞|C(x,s)|ds≥∫₀∞∑x(−1)^xC(x,s)ds≥log(L/4+1)/(2π|t|)`.

*Proof.* Let `K=(2π/L)(ℤ+1/2)` modulo `2π`. For `t>0`, the occupied momenta are `O={k∈K:cos k>0}`. No Fermi momentum is zero-energy. With `ε_k=−2t cos k`, Fourier expansion and the particle-hole basis give

`C(x,s)=L⁻²∑_{k∈O,q∉O}|e^{ik}+e^{−iq}|²e^{−i(k−q)x}e^{−s(ε_q−ε_k)}`.

Summing over `x` imposes `q=k`, impossible for a particle-hole pair. The staggered sum imposes `q=k−π`, giving

`∑x(−1)^xC(x,s)=L⁻¹∑_{k∈O}4 sin²k e^{−4ts cos k}`

and integral `(tL)⁻¹∑_{k∈O}sin²k/cos k`. Pair positive and negative `k`. For `u=π/2−k=2πm/L≤π/4`, with `m=1/2,3/2,…`, `cos²u/sin u≥L/(4πm)`. There are at least `L/8` such half-integers, and `∑_{i=0}^{M−1}1/(i+1/2)≥log(2M+1)`. This yields the bound. For `t<0`, shift momenta by `π`. The triangle inequality and Tonelli give the absolute bound. `□`

For short vacuum-pair insertions, `Λ̃_x²=n_x+n_{x+1}−2n_xn_{x+1}`. Wick expansion at half filling has a bilinear part `2G₁:Λ̃_x:`, where `G₁=⟨c_x†c_{x+1}⟩→1/π` for `t>0`. Its bilinear-bilinear contribution to a pair link is `4G₁²C(x,s)`; the quartic and mixed terms are not estimated here.

**GAP (draft D.2 and attack 1).** Theorem 4 proves divergence of the absolute sum of this free correlation component, not a lower bound for the absolute sum of the complete link: other Wick components may cancel it. No full polymer activity or weight bound is established. Thus one cannot infer that every Kotecký–Preiss or Dobrushin condition fails, nor that the charged polymer ratio fails for all nonzero `t,ε`. The exact zero-momentum cancellation and staggered logarithm above remain valid. The pass-1 proposed route divides by the full moving-light partition function and keeps determinant correlations before estimating them; its missing complete linked-gas estimate remains open.

## 6. Localized charge removal

**Theorem 5 (draft E).** Let `σ∈Ŝ_+\{1}` and let `Ψ` be a normalized `σ`-ground vector. For any localizers with `wχ>0`,

`E_σ−E_1≥16τ−|ε|Φ(χ)/(2wχ)`.

*Proof.* Choose `a≠b` with `σ=ρ_aρ_b` and put `Y_y=iγ_{y,a}γ_{y,b}`. By `SGAP.md` Theorem 3, `Y_yχ_yΨ` is neutral and half-filled. In the `ξ_y=σ` line the atomic part of the conjugation difference is `−16τ`; its bond part has zero compression because each such term changes `ξ_y`. Thus

`E_1‖χ_yΨ‖²≤⟨χ_yΨ,Hεχ_yΨ⟩−16τ‖χ_yΨ‖²`.

Use `χHχ=(χ²H+Hχ²+[χ,[H,χ]])/2` and the eigenvector equation. Only `εH4` contributes to the double commutator. Its `ξ',ξ` element is `−(χ(ξ')−χ(ξ))²(εH4)_{ξ'ξ}`. The light hop norm is at most one. Bound its expectation by the corresponding term of `|ε|Φ`, sum over `y`, and divide by `wχ`. `□`

The special choice `χ_y=P_y^σ` is the already-proved removal comparison in `SGAP.md` Theorem 5, rearranged. The corresponding A4 bound controls the unlocalized odd weight needed for that comparison; it remains open.

**Theorem 6 (window example; draft E.2).** Let `r≥0` and `χ_y` depend only on `[y−r,y+r]`, with value one on the content `σ` at `y` and vacuum at all other sites of that window. If these sites and `y±(r+1)` are distinct, a configuration with `ρ_a` at `y−r−1`, `σ=ρ_aρ_b` at `y`, `ρ_b` at `y+r+1`, and vacuum between them has `χ_y=1`. The three characters multiply to `1`; their atomic energy is `44τ`. Removing the central `σ` releases `16τ` and leaves energy `28τ` at the two endpoints.

*Proof.* The displayed window equals the prescribed one. Since `ρ_a²=ρ_b²=1`, the three-character product is trivial. The shifted atomic energies are `14τ,16τ,14τ`. `□`

Other sites may carry the global charge; the theorem concerns the displayed local neutral group. The distinctness condition, omitted in pass 1, is needed on a finite ring, e.g. `L≥2r+3`.

**GAP (draft attack 3).** A matching window does not establish the ground-state weight of such configurations, a lower bound on their flux, or failure of LOC. The suggested weight `L(ε/(Cτ))^{4r+4}` and associated `44τ` flux loss are formal only. The number and size of perturbative denominators and possible cancellations are not controlled. Extended-window and arc-product localizers remain proposals, not proved constructions.

## 7. Residuals, rungs and formal infrared picture

**SGAPT-R (open).** There exist `c₀,Δ>0` such that, for every allowed `L`, `τ>0`, `0<|t|≤c₀τ`, `|ε|≤c₀τ`, and `σ≠1`, the neutral-sector bottom of `Hε+B_σ` exceeds that of `Hε` by at least `Δτ`, where

`B_σ=16τ(P_0^1−P_0^σ)−2ε∑_{c∈{a,b}}(T_{−1,c}+T_{0,c})`, `σ=ρ_aρ_b`.

By `SGAP.md` Theorem 3 this is S-GAP restricted to `t≠0`. Together with the already-proved S-GAP⁰ it implies S-GAP with the smaller constants. It is a restatement, not a closure.

**LOC (open).** There exist `c₀>0`, `K<∞` such that, for every allowed `L`, `τ>0`, `|t|,|ε|≤c₀τ`, `σ≠1`, some normalized `σ`-ground vector and some localizers `0≤χ_y≤1` satisfy `wχ≥1/2` and `Φ(χ)≤K`. Theorem 5 gives `E_σ−E_1≥(16−Kc₀)τ`. Shrink `c₀` if necessary to make the coefficient positive. LOC is a sufficient mathematical condition, not an adopted reading. No minimality among sufficient conditions is proved.

**Theorem 7 (two-bond rung).** Replace `εH4` by its terms on any two bonds. For every allowed `L` and real `t,ε`, the resulting sector energies satisfy `E_σ−E_1≥16τ−32|ε|`.

*Proof.* Each bond has eight Hermitian contractions, so the perturbation norm is at most `16|ε|`. At `ε=0`, `SGAP.md` Theorem 2 gives the exact gap `16τ`. The variational principle bounds the energy shift in each sector by the perturbation norm. `□`

The other tree rung, one charged history with arbitrary free-light propagation, has a normalized time-ordered light factor of modulus at most one by the generalized trace Hölder inequality, cited in pass 1 but not rebuilt here. This bounds that factor by a mirror-only positive weight; it does not control the full charged-to-neutral ratio. Tree P5, P6 and P7 correspond respectively to `SMG15.md` Theorems 3 and 7 and `SGAP0.md` Theorem 9. Node S matches `SGAP.md` Definition 4. The tree is a sketch, not independent proof.

**Formal only.** `SMG15.md` Theorem 7 gives the exact second-order atomic resolvent identity; treating its negative as the effective light Hamiltonian gives the formal chain

`−t∑hop_x−(4ε²/(7τ))N+(4ε²/(7τ))∑n_xn_{x+1}`,

with formal XXZ anisotropy `2ε²/(7τ|t|)`. For `0<c₀≤14`, `ε=c₀τ/2`, `|t|=c₀²τ/14` lies in the square and gives anisotropy one; for larger `c₀` use any smaller positive constant in that construction. This algebra does not establish an effective chain uniformly in volume. The XXZ phase and gap claims in pass 1 are credited from memory and **NOT VERIFIED** for the required hypotheses. The proposed weaker targets **S-GAP-LL** (`ε²≤κτ|t|`) and **S-GAP-CDW** (`|t|≤κε²/τ`) are named, open and not adopted; neither establishes the whole square. Higher-order remainder growth, extensive fooled-window weight, and higher-dimensional power counting are also formal, not results.

## 8. Scope and outstanding checks

S-GAP, SGAPT-R and LOC remain open. The three attempted routes leave, respectively, a complete charged linked-gas estimate, a suitable block form with controlled defect-relative error, and a ground-state localizer with bounded flux. The resonance theorem covers only its specified arc operator and full-space inverse. The free-correlation theorem covers the stated `w=−1` free ring. The finite-ring estimates do not establish a 3+1-dimensional mirror gap, a GNS generator gap, a tick statement, or light-sector correlations.

Other inherited open items are `(G1)` inside `𝒱_p`, sharper constants, A4, R1.5-U, R1.5-D, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4. A5 and A6 have the specific counterexamples recorded in `SGAP.md`; they do not refute S-GAP.

Pass 1 reports the literature search and source-specific checks in `SGAPT_DRAFT.md` §2. It checked mainly abstracts; the Fröhlich–Pizzo theorem locator, the degenerate extension, the Benfatto–Mastropietro locator, the Yarotsky locator, the edge-transport transfer and several memory citations were not verified. No outside theorem is a load-bearing proof input above. `prior/SGAPT.md` identifies the existing static-source comparison, massive fermionic polymer bounds and volume-dependent Feshbach estimate; their hypotheses do not establish this moving-light result. Their reported ledger status is unaudited, and this pass did not refresh those sources from main. The next fresh session must referee the complete dependency chain and the GAP dispositions before any freeze.
