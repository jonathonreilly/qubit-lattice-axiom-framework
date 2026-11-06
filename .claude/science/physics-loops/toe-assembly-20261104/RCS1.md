# RCS1. A charged-sector prescription for the five-mode laws

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (RCS1_REFEREE.md); the referee's edits 1-10 are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. R-CS stays an owner choice; no prescription, odd label or specification here is adopted. The lead (Claude Opus 5.5, laptop) checked that the four-test table matches the referee's verdicts and that the status block lists the referee's open statements; that is a text check, not a second referee.

**Proved, conditional on the named law and source inputs.** The local centre implementers are central observables. They give the finite-region parity/flux identity (Theorems 1–2). A finite localized factor sector of odd relative parity over a cell-periodic factor background has no implemented nonzero cell translation (Theorem 3). The observable algebra is matter-even (Theorem 4). A conserved label shifted by translations forces directional flatness at a node (Theorem 5). Escaping sharp observables separate representations (Lemma 6). The proposed straight-string construction is empty in the stated locked U-law states; the alternating empty-matter example has string limits and transverse flatness (Theorems 7–8). The general conditional obstruction is Corollary 9.

**GAP: odd-sector identification.** The open-string operators are odd in the *field-algebra vacuum GNS representation*, when that representation and its parity implementer are specified. Their limit states are representations of the even algebra `𝔄^G`, which has no intrinsic odd subspace. The draft's expression `π(B_{r,b})Ω` is undefined for `π` a representation only of `𝔄^G`. An odd identification invariant under unitary equivalence and inherited by subrepresentations cannot extend LZ1’s grading in every D1 state (R1(a)). Over a parity-sharp background, `χ_tot` supplies a proposed odd label agreeing with LZ1’s grading and, for localized factor sectors relative to the factor vacuum sector, with Theorem 3 (R2). Every band in Theorem 8(d) lies in a representation odd in that sense (R2(d)). Corollary 9 and backgrounds that are not parity-sharp still need the owner’s specification; the prescription is not an adoption or a physical particle identification.

**GAP: scope and inferences.** The draft's localization theorem does not show that *every* translation-covariant odd sector retains the vacuum configuration: it assumes finite localization and its defined relative parity. R3 repairs the localization statement: for factor `π,π₀` with cell-periodic `κ₀`, if `π` is quasi-equivalent to `π∘τ_β` for a nonzero `β`, the configuration difference set is empty or infinite; if `π` is also finitely localized relative to `π₀`, it is empty and `χ=+1`. Failure of pairwise disjointness implies quasi-equivalence for factor representations, but not in general; Theorem 8 does not establish that its ray representations are factors. The suggested Dirac-cloud obstruction in A2 needs a defined representation and label decomposition: for rays along `e_j`, transverse labels supply a shift direction only when `n_j=0`, so rays along all three axes supply no common nonzero `n` through those labels alone. Neither a coherence bound nor an absent specified plaquette layer rules out deconfinement. Details appear below.

**Open by name.** **R-CS**, the owner’s choice, including which representations of `𝔄^G` count as MT1’s odd species for backgrounds that are not parity-sharp; **RCS-P**, with failed attacks A1, A2, A3 and failed kill attempt K (§8); **MT1-S[R-CS^str] in the VC1 vacuum**, with VC1. The inherited open lists of `LZ1.md` and `MT1.md` are unchanged. R-loc, R-CS^str, R-CS^FMS, R-CS^pair, R-CS^Dirac, R-CS^KR, R-CS^BR and the automorphism form are proposed readings or constructions, not adoptions (§7). Neither five-mode law is eliminated.

**Provenance.** Pass 1: Claude Opus 5.5, `RCS1_DRAFT.md`, SHA-256 `36420fe9ef5b166452ccf4d7cc43e71a38ad18bf6014f8275e02ad1c5f94707f`. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1b059-b69c-7a72-bfc3-87fe21fcce60` (from the run log). Working-tree HEAD `22dfc60d86c3872a4f341a199479622ba6f0ece1`. Context: `TOE_ASSEMBLY.md` §§3.4–3.5 and MT1 target; `LW1.md`, `LZ1.md`, `MT1.md`, `CH1_5UQ.md`, `EW1.md`, `LW1_5.md`. The draft's literature record is §0.2 of `RCS1_DRAFT.md`; it reports searches and distinguishes fetched from inaccessible papers. This pass did not independently verify that literature. Imported results retain their stated hypotheses and status. No numerical check is claimed. The draft read `EW1.md` before it was frozen; the cited sentence is unchanged. Pass 3 is the referee report, and its imported closures are unrefereed; it is not an audit.

**Editing-session provenance.** Codex gpt-6.1-terra, effort high, codex-cli 0.165.0; session `01a1b083-0724-7691-a7fb-ffb2ba2f4463`.

## 1. Definitions inferred by the distiller

1. Use `VC1_5.md` definition 1 for the quasi-local field algebra `𝔄`, and `LZ1.md` §1 for cell translations `τ_β` by `2β`, tick `α`, D1 states, centre implementers `c_z`, bands, nodes and Clifford cones. The update is the base tick or an appended gauge-invariant update in LZ1's class. Write `𝔄^G` for the local-gauge fixed algebra. Its local fixed elements are dense by `VC1_5.md` Theorem 2.1. The two laws and gauge actions are those of `LW1_5.md` §2.
2. On U, `c_z=e^{iπQ_z}`, `Q_z=N_z+Σ_{ℓ∋z}p_{ℓ,z}`; on O, `c_z=∏_{j=1}^5e^{iπ𝒢_z^{2j−1,2j}}`. Write `P_Λ=∏_{z∈Λ}(−1)^{N_z}`. For a finite site set `Λ`, let `L_int(Λ)` contain links with both ends in `Λ`, `∂Λ` those with exactly one, and `in(ℓ)` the end in `Λ`. Set `f_{ℓ,z}=(−1)^{p_{ℓ,z}}` on U and `f_{ℓ,z}=Γ^z_ℓ=i^5η^z_1⋯η^z_{10}` on O. On `S_+`, the two end chiralities agree. Put `F_{∂Λ}=∏_{ℓ∈∂Λ}f_{ℓ,in(ℓ)}`.
3. A factor representation has `π(𝔄^G)''` with scalar centre. Its configuration `κ_π(z)` is the scalar `π(c_z)`. Two representations are disjoint if no nonzero bounded operator intertwines them. Quasi-equivalence means the normal isomorphism of their generated von Neumann algebras that maps each `π(A)` to `π'(A)` exists. Equivalently, every nonzero subrepresentation of either representation contains a nonzero subrepresentation equivalent to a subrepresentation of the other. The nonzero qualification makes the draft definition explicit. For factor representations non-disjointness implies quasi-equivalence.
4. Let `𝔄_{Λ^c}` be generated by matter outside `Λ` and links with neither end in `Λ`; set `𝔄^G_{Λ^c}=𝔄_{Λ^c}∩𝔄^G`. Say `π` is localized in `Λ` relative to `π₀` if their restrictions to this algebra are unitarily equivalent via `V:H_π→H_{π₀}`. Let `Λ̂` contain sites at distance at most one from `Λ`.
5. A covariant representation `(H,π,T,Ũ)` has separable `H`, `π` a representation of `𝔄^G`, a unitary representation `T` of `Z³`, and unitary `Ũ`, such that `T_βπ(A)T_β*=π(τ_β A)`, `Ũπ(A)Ũ*=π(α A)` and `ŨT_β=T_βŨ`. Bands and nodes use LZ1's definitions with these implementers. In particular `F:L²(T³;C^d)→H` is an isometry, `T_βF=FM_β`, `ŨF=FM_V`, `V(K₀)=1`, `V` is `C¹` near `K₀`, and `N_j=∂_j(i log V)(K₀)`.
6. An operator is *carried at* `x` if every gauge automorphism at sites other than `x` fixes it. “Odd” for field-algebra elements refers to matter parity `θ`. A relative parity of localized factor representations is defined in Theorem 3; it is not automatically an intrinsic parity grading of an arbitrary representation of `𝔄^G`.
7. Definitions of the proposed straight string, dipole variant and representation family are in §5. The four-test results are judgments from pass 1, qualified in §7; they do not adopt these definitions.

## 2. Centre and Gauss identity

**Theorem 1.** On either law, every `c_z` is central in `𝔄^G`, `α(c_z)=c_z`, and `τ_β(c_z)=c_{z+2β}`. In a factor representation `π`, `π(c_z)=κ_π(z)1`, with `κ_π(z)^2=1` on U and `−1` on O. Quasi-equivalent representations have the same configuration. Composition with `α` leaves it unchanged; composition with `τ_β` shifts it to `κ_π(z+2β)`. Thus quasi-equivalence to `π∘τ_β` requires invariance under that shift.

*Proof.* The element implemented by `c_z` is central in the local gauge group; the other sites' gauge actions commute with it, including at opposite link ends. Hence `c_z` is fixed by all gauge actions. Its adjoint action is itself a local gauge action, so it commutes with each fixed observable. Gauge-invariant gates commute with it, and translations shift its site. In a factor representation its image is scalar. On U, `Q_z` is integer-valued. On O, the local lift squares to `−1` for the `S_+` register, as in `LW1_5.md` §5. A quasi-equivalence preserves scalar images, and the remaining claims follow by applying the automorphisms to `c_z`. □

**Theorem 2.** For either law and finite `Λ`,
\[
\prod_{z\inΛ}c_z=s_ΛP_ΛF_{∂Λ},\quad
s_Λ=\begin{cases}(-1)^{m|L_{int}(Λ)|}&L5\text{-U}[m],\\
(-i)^{|Λ|}(-1)^{|L_{int}(Λ)|}i^{|∂Λ|}&L5\text{-O}[S_+].\end{cases}
\]
All displayed factors are gauge invariant. Consequently `π(P_Λ)π(F_{∂Λ})=s_Λ^{-1}∏_{z∈Λ}κ_π(z)1` in a factor representation.

*Proof.* On U, `c_z=P_z∏_{ℓ∋z}(−1)^{p_{ℓ,z}}`; an internal link contributes `(−1)^m` by its fixed total rishon number. On O, `exp(iπ(iχ_{2j−1}χ_{2j}/2))=−χ_{2j−1}χ_{2j}`. The five factors give `−iP_z` for matter and `iΓ^z_ℓ` at each link end. The two end chiralities agree on `S_+` and square to one, so an internal link contributes `−1`; a boundary link contributes `iΓ`. Parity, end number parity and end chirality commute with the relevant gauge generators and with the other end's action. The factor-representation formula follows from Theorem 1. □

This is a native `Z₂` parity/flux identity; the draft compares it to Kijowski–Rudolph's finite-lattice global Gauss law. It does not impose a particular value of `κ`.

## 3. Localized sectors and even observables

**Theorem 3.** Let `π,π₀` be factor representations, with `π` localized in finite `Λ` relative to `π₀` via `V`. Then `κ_π=κ₀` outside `Λ̂`. Define
\[
χ(π:π₀)=\prod_{z\in\widehat Λ}\frac{κ_π(z)}{κ₀(z)}\in\{\pm1\}.
\]
For any finite `Λ'⊇Λ̂`, `π(P_{Λ'})=χ V^{-1}π₀(P_{Λ'})V`. If `χ=−1` and `κ₀` is cell-periodic, `π` and `π∘τ_β` are disjoint for every nonzero `β`. In particular no such translation is implemented in `π`.

*Proof.* For `z∉Λ̂`, `c_z` belongs to the exterior fixed algebra, so localization equates its scalar values. Every boundary link of `Λ'` has neither end in `Λ`, so `V` intertwines `F_{∂Λ'}`. Divide the two instances of Theorem 2; the ratio is `χ`. If `χ=−1`, the set `D` on which the configurations differ is finite and nonempty. A nonzero translation cannot preserve such a set. As `κ₀` is periodic, translating `π` moves `D`, giving different central scalar values and hence no nonzero intertwiner. □

If the restriction of a D1 field state to `𝔄^G` is a factor state with configuration `κ₀`, a field `A` of finite LZ1 centre pattern `ε` creates vectors with central values `ε_zκ₀(z)`. This explains LZ1's pattern pinning. The theorem itself does not classify nonlocalized sectors or assign them an odd parity.

**Theorem 4.** Every `A∈𝔄^G` is matter-even. If `A∈𝔄` is carried at `x`, then `Ad(c_x)(A)=θ(A)`. Thus an even `Φ` and an odd `ψ`, both carried at `x`, give an odd `Φ*ψ`, which cannot be gauge invariant.

*Proof.* For local fixed `A`, multiply `Ad(c_z)` over a finite region containing its support. Every factor fixes `A`; the product is matter parity by LZ1 §1. Local fixed elements are dense, and `θ` is norm-continuous. For carried `A`, approximate it by local elements. Products of centre actions over increasing finite regions converge on `A` to `θ(A)`; all factors except the one at `x` fix `A`. Hence the second assertion, including quasi-local `A`. □

## 4. A conserved label and node flatness

**Lemma 5.1 (boost; draft Lemma B).** Let `H` be separable, let `T` represent `Z³`, and let `Ũ` commute with `T`. Suppose `n∈Z³\{0}` and for every `0≤t<t_*` a unitary `B_t` commutes with `Ũ` and obeys `B_tT_βB_t^{-1}=e^{it n·β}T_β`. For any band and node `K₀`, `V(K₀+sn)=1` for small real `s`; hence `Σ_j n_jN_j=0`.

*Proof.* Near the node put `h=i log V`, with spectrum in `(-π/2,π/2)`. Write `(S_tψ)(K)=ψ(K−tn)` and `G_t=B_tFS_t`. Then `G_t` is an isometry intertwining translations with `M_β` and `Ũ` with multiplication by `V(K+tn)`.

Suppose some `tr(h^p)`, `1≤p≤d`, has nonzero directional derivative on an open set. On a smaller ball the number of distinct eigenvalues is maximal and constant. Riesz projections and their eigenvalues are `C¹` there, so one eigenvalue `λ` has strictly monotone variation along `n` on a small tube. Restrict each boosted band to its `λ(K+tn)` eigenspace over a fixed positive-measure ball. For bounded `X` with `T_βX=XM_β` and `ŨX=XM_w` for scalar `w`, the joint spectral measure satisfies `P(Γ)X=XM_{1_Γ(K,w(K))}` for every Borel `Γ`: first verify this for polynomials, extend to continuous functions by Stone–Weierstrass, then to Borel sets by regularity of the measures. The joint spectral measure of the commuting unitaries `(T_1,T_2,T_3,Ũ)` assigns its nonzero range to the graph of `e^{-iλ(K+tn)}`. These graphs are pairwise disjoint for distinct `t` in an interval, since the eigenvalues stay within the chosen logarithm branch and vary strictly. This produces uncountably many mutually orthogonal nonzero subspaces, contrary to separability. Therefore every `tr(h^p)` is constant along short `n`-segments. Newton identities make the characteristic polynomial constant there. At the node it is `λ^d`; Hermiticity gives `h=0` on that segment. Differentiate. □

**Theorem 5.** Suppose additionally `H=⊕_{c∈C}H_c`, `ŨH_c=H_c`, `T_βH_c=H_{β·c}`, and a real `q` satisfies `q(β·c)=q(c)+n·β` for some nonzero `n∈Z³`. Every band is flat along `n` at each node and has no Clifford cone there. Here “flat along `n` at `K₀`” means `V(K₀+sn)=1` for all small real `s`.

*Proof.* With `Π_c` the projections, `B_t=Σ_c e^{itq(c)}Π_c` commutes with `Ũ` and obeys the boost relation in Lemma 5.1. A Clifford triple with speed `v>0` would instead satisfy `(Σ n_jN_j)^2=v²|n|²1`. □

**Corollary 5.2 (draft Corollary 5.1).** In LZ1's nontrivial finite-pattern subspace, translations act freely on each pattern orbit. Taking `q_j(τ_βκ_rep)=β_j` for orbit representatives gives `N_j=0` for every `j` at every node. This recovers the node portion of LZ1 Theorem 2.2; that theorem also proves neighbourhood flatness. □

## 5. Proposed straight strings

Fix an oriented axis `e`, a locally gauge-invariant D1 state `ω`, `y_i=x+ie`, and links `ℓ_i=(y_{i−1},y_i)` for `1≤i≤2r`. Let `T_i` be the law's link transport matrix from `y_i` to `y_{i−1}`, transforming at its two ends. On U, for a positively oriented link, `(T_i)_{ab}=(U^{ba}_{ℓ_i})*=r^{ℓ_i,y_{i−1}}_a r^{ℓ_i,y_i*}_b`. Put `ψ†_{x,a}=c†_{x,a}` on U and `γ_{x,a}` on O, and define
\[
 B_{r,b}(x)=\sum_a\psi^\dagger_{x,a}(T_1\cdots T_{2r})_{ab},\quad
 \omega_r^{(x)}(A)=\frac{\sum_b\omega(B_{r,b}^*AB_{r,b})}{\sum_b\omega(B_{r,b}^*B_{r,b})},\quad A\in\mathfrak A^G,
\]
when the denominator is positive. The index is contracted at every site except the far end. The dipole variant contracts the far end with a matter annihilator (on O, a Majorana). **R-CS^str(e), proposed:** call GNS representations of weak-* limit points of these states string sectors. For each site residue modulo `2Z³`, choose one limit point and translate it covariantly. Positivity along an unbounded sequence of lengths suffices for limit points by weak-* compactness; positivity for every length is not necessary. If no such sequence exists the construction supplies no sector. The proposed MT1-S[R-CS^str(e)] asks, for some axis `e` and some covariant choice of limit points, for a Clifford node in a covariant direct sum of subrepresentations quasi-equivalent to these GNS representations, with the odd-sector identification specified as in §0.

For `z` different from the far endpoint, `B_{r,b}` commutes with `c_z`. If `ω` is sharp in `c_z`, every sufficiently long string state has the same sharp value. Thus the limiting state has the same centre values wherever the background is sharp. This alone does not prove a charge is present or localized at infinity. The construction is modeled on the pass-1 account of Fredenhagen–Marcu as described by Barata–Nill; their hypotheses and conclusions are not imported as proofs here.

**Lemma 6 (asymptotic separation; draft Lemma D).** Let `π₁,π₂` be direct sums of cyclic representations of `𝔄^G`. Let uniformly bounded self-adjoint local `X_t∈𝔄^G` have supports escaping every finite set. Suppose each cyclic vector in the first sum is eventually an eigenvector of `X_t` with value `a`, and each in the second with value `b≠a`. Then `π₁,π₂` are disjoint.

*Proof.* Local fixed observables are dense and even. For any finite sum of local observables applied to the cyclic vectors, eventual locality gives `π_i(X_t)ξ=c_iξ`, with `c_1=a`, `c_2=b`. Uniform boundedness extends this to strong convergence `π_i(X_t)→c_i1` on the whole Hilbert space. An intertwiner `S` would satisfy `aS=bS`, so `S=0`. □

**Theorem 7 (draft Proposition 6.1).** On U, let `ω=Φ∘E`, where `Φ` is a product state whose six ends at every site have the same occupied flavour set. Then the open and dipole string denominators vanish for every `x,e,r≥1`. This includes the stated locked witnesses of `VC1_5.md` Theorem 5.5 and `CH1_5UQ.md` Theorem 3.3.

*Proof.* The summed norm operator is gauge invariant, so its expectation in `Φ∘E` is the sum of `‖B_{r,b}Φ‖²`. At the first interior site, each term creates a flavour at one incident end and annihilates the same flavour at the other. The two occupied sets agree, so no term survives. The dipole has the same interior factor. □

**Theorem 8 (draft Theorem 6).** On `L5-U[2k]`, `k=1,2`, choose disjoint `k`-element flavour sets `S_e,S_o`. Let `Φ_AB` have empty matter and each link of the even, respectively odd, tiling occupied by `S_e`, respectively `S_o`, at both ends. Let `ω_AB=Φ_AB∘E`. For the base tick and every allowed `ε,μ,τ_E`:

(a) `ω_AB` is gauge invariant, cell invariant and stationary, hence D1.

(b) The open-string states for `e=e₁` have positive denominators and converge on each local observable as `r→∞`. In the limit `N_x=1`, `N_z=0` for `z≠x`; each ray link has end numbers `(k−1,k+1)` from near to far, and every other link has `(k,k)`.

(c) The tick and cell translations have commuting unitary implementers on the direct sum of the limit GNS representations. Transversely displaced rays have disjoint representations; the tick preserves each representation up to unitary equivalence.

(d) Every band in any covariant representation whose observable representation is a direct sum of subrepresentations each quasi-equivalent to one of these ray representations has `V(K₀+se₂)=V(K₀+se₃)=1` near a node. In particular `N₂=N₃=0` and no Clifford cone occurs. Every such band lies in a representation with `χ_tot(·:ω_AB)=−1` (R2(d)). The analogous result holds for the other coordinate axes. The dipole variant has zero norm in this state.

*Proof.* (a) Every hop annihilates empty matter, and the electric layer is scalar on the sharp end-number product state. Cell symmetries preserve the two tilings and carry the product state to itself up to phases. The gauge average `E` commutes with the tick and cell lifts (`VC1_5.md` Theorem 2.1).

(b) Along an axis, consecutive links alternate tilings. An index term is nonzero exactly when its near-end flavour is occupied and its far-end flavour unoccupied. At each interior site the shared flavour must lie in the next link's set, possible because `S_e` and `S_o` are disjoint. There are `k` choices for each interior index and `5−k` for the last index. Distinct sequences give orthogonal occupation vectors, so the denominator is positive and the asserted numbers are sharp. For a fixed local observable, sum over the unseen tail: different tail occupations are orthogonal and each boundary index has the same number of continuations. The normalized expectation therefore stops changing once the endpoint passes the support. This proves the limit and its local sharp values.

(c) In the state vector after a string, all matter is at `x`, and all terms have the same end numbers. The inverse electric layer therefore contributes a common phase. Under the inverse odd cube layer only the cube containing `x` acts; after that, only the eight even cubes meeting it can act. Their ordered product is a local gauge-invariant unitary `G_x*`, independent of string length and far index. Thus, with the convention `α(A)=U₀*AU₀`,
\[
\omega_\infty^{(x)}\circ α^{-1}=\omega_\infty^{(x)}\circ\operatorname{Ad}G_x.
\]
The GNS map `π_x(A)Ω_x↦π_x(α(A))π_x(G_x*)Ω_x` is an isometry by this identity and has dense range; it implements `α`. Translation covariance of the strings and of `G_x` supplies commuting translation implementers on `⊕_xH_x`.

For distinct transverse ray positions choose `X_t=(p_{ℓ_t,y_{t−1}}−k)²` on links escaping along one ray. By (b) its value is 1 in that ray's cyclic state and 0 in the other. Lemma 6 gives disjointness. The unitary above gives tick equivalence.

(d) Group summands by transverse position `c=(x₂,x₃)`. Different groups are disjoint, hence orthogonal even if their invariant subspaces were not initially chosen orthogonal. Tick covariance and the tick equivalence in (c) make each group invariant; translation covariance shifts `c` by `2(β₂,β₃)`. Intertwining projections between disjoint groups vanish. Apply Theorem 5 with `q(c)=c₂/2` and then `c₃/2`. Cell rotations carry the construction to the other axes. The far matter annihilator of the dipole kills the empty matter state. □

**Corollary 9 (draft Corollary 6.2).** For either law, suppose the proposed ray sectors exist and are chosen covariantly, sectors at distinct transverse positions are disjoint, and each is quasi-equivalent to its tick transform. Then every band in any covariant representation built from their quasi-equivalent subrepresentations is flat in both transverse directions at each node, and has no Clifford cone.

*Proof.* The disjointness and tick-equivalence hypotheses give the same transverse decomposition and invariant subspaces as in Theorem 8(d). Translation covariance shifts the labels. Apply Theorem 5 twice. □

Theorem 8 supplies a counterexample for odd sectors in the sense of `χ_tot` to the claim that existence of these sectors and implemented tick and translations alone forces a Clifford cone. No band with a node is shown to exist. In the representation constructed in Theorem 8(c), Theorem 5 with `q(x)=x_j/2` gives `N₁=N₂=N₃=0`; for other covariant representations built from these sectors the result does not rule out motion along the ray. Theorem 7 supplies a counterexample to existence of the proposed sectors in every D1 state. Theorem 4 excludes gauge-invariant odd field elements, including the proposed FMS-type composite. These conclusions do not identify the constructed representation with a physical charged particle.

## Referee closures

The following closures are unrefereed and are imported from `RCS1_REFEREE.md`; they adopt no reading or law.

### R1. Odd labels from representations of `𝔄^G` alone (referee closure, RCS1_REFEREE.md)

**R1(a) (tracial state; both laws).** Let `τ` be the tracial state of the quasi-local algebra `𝔄` of `L5-U[m]` or `L5-O[S_+]`. Let `(H,π,Ω)` be its GNS representation, `U_θ` the unitary with `U_θπ(A)Ω=π(θ(A))Ω`, `H_odd` its `−1` eigenspace and `H_phys` the closure of `π(𝔄^G)Ω`. Then there is a nonzero bounded `W:H_phys→H_odd` with `Wπ(A)=π(A)W` on `H_phys` for every `A∈𝔄^G`. So a nonzero subrepresentation of `𝔄^G` on `H_phys` is unitarily equivalent to a subrepresentation on `H_odd`.

`τ` is a locally gauge-invariant D1 state: `LZ1.md` RC2 for `L5-U` ("`τ` is stationary for every update in §1. It is invariant under every lift of the cell group and under every local gauge transformation") and `VC1_5.md` Theorem 4.1 for `L5-O[S_+]` ("`τ` satisfies (i)–(iii)").

*Proof.* `𝔄` is the norm closure of an increasing union of full matrix algebras (the proof of `LZ1.md` RC2), and `τ(AB)=τ(BA)` for all `A,B∈𝔄`. `τ∘θ=τ`, because `τ` is invariant under every automorphism (same proof), so `U_θ` exists. Define `J` on `π(𝔄)Ω` by `Jπ(A)Ω=π(A^*)Ω`. It is well defined and isometric, since `‖π(A^*)Ω‖²=τ(AA^*)=τ(A^*A)=‖π(A)Ω‖²`. It is antilinear, so it extends to an antiunitary on `H` with `J²=1`. For `B,C∈𝔄`, `Jπ(B)Jπ(C)Ω=Jπ(BC^*)Ω=π(CB^*)Ω`. Hence for `A∈𝔄`, `π(A)Jπ(B)Jπ(C)Ω=π(ACB^*)Ω=Jπ(B)Jπ(A)π(C)Ω`, and by density `Jπ(B)J` commutes with `π(𝔄)`. Take `ψ=c_{x,1}` on `L5-U` and `ψ=γ_{x,1}` on `L5-O`. Let `W` be `Jπ(ψ)J` restricted to `H_phys`. It commutes with `π(𝔄^G)`. `WΩ=Jπ(ψ)Ω=π(ψ^*)Ω`, and `‖π(ψ^*)Ω‖²=τ(ψψ^*)`, which is `1/2` on `L5-U` and `1` on `L5-O`. For `A∈𝔄^G`, `Wπ(A)Ω=π(A)WΩ=π(Aψ^*)Ω`. `A` is even by Theorem 4, so `Aψ^*` is odd and `U_θ` negates `π(Aψ^*)Ω`. So `W` maps a dense subset of `H_phys`, hence all of it, into `H_odd`, and `W≠0`. In the polar decomposition `W=V|W|` on `H_phys`, `|W|` commutes with `π(𝔄^G)` there and `V` intertwines. `V` restricted to `(\ker W)^⊥` is the unitary equivalence. ∎

*Consequence.* Suppose a rule assigns "even" or "odd" to representations of `𝔄^G`, is constant on unitary-equivalence classes, and gives every nonzero subrepresentation the label of the representation that contains it. Then in `τ` it cannot label the representation on `H_phys` even and the one on `H_odd` odd: the two equivalent subrepresentations of R1(a) would carry both labels.

*Remark, cited and not used.* Tomita–Takesaki theory gives the same intertwiner, `Jπ(ψ)J` with `J` the modular conjugation, in every D1 state whose GNS vector is separating for `π(𝔄)''`. A state that is pure on `𝔄` is not of this kind.

**R1(b) (approximants do not label the limit).** In `ω_AB` of Theorem 8, for every local `A∈𝔄^G` and every site `y` outside the support of `A`,
\[
 \frac{ω_{AB}(c_{y,1}A\,c^\dagger_{y,1})}{ω_{AB}(c_{y,1}c^\dagger_{y,1})}=ω_{AB}(A).
\]
So `ω_AB|𝔄^G` is the weak-* limit, as `y→∞`, of the restrictions of the vector states of the `θ`-odd vectors `π(c^\dagger_{y,1})Ω`.

*Proof.* `A` is even (Theorem 4) and its support avoids `y`, so `A` commutes with `c_{y,1}`. Then `c_{y,1}Ac^\dagger_{y,1}=A(1−n_{y,1})`. The gauge average `E` of `VC1_5.md` Theorem 2.1 fixes `A` and is a Haar average, so `E(A(1−n_{y,1}))=A\,E(1−n_{y,1})=A(1−N_y/5)`. `Φ_AB` is a product state, `A` and `N_y` are even with disjoint supports, and matter is empty, so `Φ_AB(A(1−N_y/5))=Φ_AB(A)`. Also `ω_AB(A)=Φ_AB(E(A))=Φ_AB(A)`. The case `A=1` gives the denominator `1`. ∎

**R1(c) (sharp configuration separates R-loc's sectors).** Let `ω` be a D1 state of either law with field GNS data `(H,π,Ω,U_θ)`, and let `π(c_z)Ω=κ₀(z)Ω` for every `z`. Then no nonzero bounded `S:H_phys→H_odd` intertwines the two representations of `𝔄^G`.

*Proof.* `c_z` is central in `𝔄^G` (Theorem 1), so `π(c_z)=κ₀(z)` on `H_phys`. Let `A∈𝔄` be local and odd. The proof of `LZ1.md` Theorem 2.1 writes `A=Σ_εA_ε` over sign patterns `ε` on a finite set, with `Ad c_z(A_ε)=ε_zA_ε`, and every nonzero `A_ε` has `∏_zε_z=−1`. Fix such an `ε` and a site `z` with `ε_z=−1`, and put `v=π(A_ε)Ω`. Then `π(c_z)v=ε_zκ₀(z)v`, so `π(c_z)^*v=\overline{ε_zκ₀(z)}\,v`. For `ξ∈H_phys`, `ε_zκ₀(z)⟨v,Sξ⟩=⟨π(c_z)^*v,Sξ⟩=⟨v,Sπ(c_z)ξ⟩=κ₀(z)⟨v,Sξ⟩`. So `⟨v,Sξ⟩=0`. These `v` span a dense subspace of `H_odd`, because `(1−U_θ)/2` maps `π(A)Ω` to `π((A−θ(A))/2)Ω`. Hence `Sξ⊥H_odd`; since `Sξ∈H_odd`, `Sξ=0`. ∎

### R2. Relative total parity in parity-sharp backgrounds (referee closure, RCS1_REFEREE.md)

**Setting.** A D1 state `ω₀` is *parity-sharp* if `ω₀(P_Λ)=ε_Λ∈{±1}` for every finite `Λ`; then `ω₀((P_Λ−ε_Λ)²)=0`, since `P_Λ` is a self-adjoint unitary. For a representation `π` of `𝔄^G` write `χ_tot(π:ω₀)=s` if `ε_Λπ(P_Λ)→s·1` strongly along the net of finite site sets ordered by inclusion, with `s∈{±1}`.

**R2(a) (invariance).** If `χ_tot(π:ω₀)=s` and `σ` is quasi-equivalent to `π` in the sense of definition 3, then `χ_tot(σ:ω₀)=s`. If every `σ_i` has `χ_tot(σ_i:ω₀)=s`, so does `⊕_iσ_i`.

*Proof.* Direct sums: every `ε_Λσ(P_Λ)` has norm at most one. Strong convergence on each summand gives it on finite sums of summand vectors. These are dense, and a uniformly bounded net that converges strongly on a dense set converges strongly everywhere. Quasi-equivalence: on a closed `π`-invariant `L⊂H_π` the restricted net still converges to `s`. If a unitary `U:K→L` carries `σ|_K` to `π|_L`, then `ε_Λσ(P_Λ)|_K=U^*(ε_Λπ(P_Λ)|_L)U→s`. By Zorn's lemma choose a maximal family `{K_j}` of mutually orthogonal nonzero closed `σ`-invariant subspaces, each unitarily equivalent to a subrepresentation of `π`. Its orthogonal complement is `σ`-invariant. If it were nonzero, definition 3 would give it a nonzero subrepresentation equivalent to a subrepresentation of `π`, against maximality. So `H_σ=⊕_jK_j`, and the direct-sum case applies. ∎

**R2(b) (agreement with LZ1's grading).** Let `(H₀,π₀,Ω₀)` be the GNS representation of `ω₀` on `𝔄` and `U_θ` as in `LZ1.md` line 27. Then `ε_Λπ₀(P_Λ)→U_θ` strongly. So `χ_tot=+1` on every `π₀(𝔄^G)`-invariant subspace of `H_even`, including the vacuum sector on `H_phys`, and `χ_tot=−1` on every such subspace of `H_odd`.

*Proof.* Sharpness gives `π₀(P_Λ)Ω₀=ε_ΛΩ₀`. Let `A∈𝔄` be local with its matter in `Λ`. `P_Λ` implements parity on the modes of `Λ` and fixes links, so `P_ΛA=θ(A)P_Λ`. Then `ε_Λπ₀(P_Λ)π₀(A)Ω₀=ε_Λπ₀(θ(A))π₀(P_Λ)Ω₀=π₀(θ(A))Ω₀=U_θπ₀(A)Ω₀`. Local vectors are dense and the net is uniformly bounded. ∎

**R2(c) (agreement with Theorem 3).** Let `π,π'` be factor representations of `𝔄^G`, with `π` localized in a finite `Λ` relative to `π'` via `V`. If `χ_tot(π':ω₀)=s'`, then `χ_tot(π:ω₀)=χ(π:π')s'`.

*Proof.* Theorem 3 gives `ε_{Λ'}π(P_{Λ'})=χ\,V^{-1}(ε_{Λ'}π'(P_{Λ'}))V` for every finite `Λ'⊇Λ̂`. These `Λ'` form a tail of the net. Conjugation by a fixed unitary preserves strong convergence. ∎

With `π'` the vacuum sector (assumed a factor representation; `s'=+1` by R2(b)), `χ_tot` is Theorem 3's `χ`.

**R2(d) (the string sectors of Theorem 8).** `ω_AB` is parity-sharp with `ε_Λ=1`. Every string sector `π_x` of Theorem 8 has `χ_tot(π_x:ω_AB)=−1`. So does every covariant representation `(H',π',T',Ũ')` of Theorem 8(d).

*Proof.* Matter is empty in `Φ_AB` and `P_Λ` is gauge invariant, so `ω_AB(P_Λ)=1` sharply. By Theorem 8(b), `N_x=1` and `N_z=0` (`z≠x`) are sharp in `ω_∞^{(x)}`. So `π_x(P_Λ)Ω_x=−Ω_x` whenever `x∈Λ`. Let `A∈𝔄^G` be local and let `Λ` contain `x` and the matter of `A`. `A` is even, so `P_ΛAP_Λ=θ(A)=A`. Then `π_x(P_Λ)π_x(A)Ω_x=π_x(A)π_x(P_Λ)Ω_x=−π_x(A)Ω_x`. Density and uniform boundedness give `χ_tot(π_x:ω_AB)=−1`. Each summand of `π'` is quasi-equivalent to some `π_x`, so R2(a) gives `χ_tot(π':ω_AB)=−1`. ∎

*Consequence.* With `χ_tot` as the odd label, Theorem 8(d) is a statement about odd bands. Under R-CS^str(e), for each axis `e`, MT1-S's asserted odd Clifford node does not exist in `ω_AB`. This holds for the base `L5-U[m]` tick, `m∈{2,4}`, at all constants.

### R3. Configurations of translation-covariant factor sectors (referee closure, RCS1_REFEREE.md)

**Statement.** Let `π,π₀` be factor representations of `𝔄^G` with `κ₀` cell-periodic, and let `π` be quasi-equivalent to `π∘τ_β` for one `β≠0`. Then `D={z:κ_π(z)≠κ₀(z)}` is empty or infinite. If `π` is also localized in a finite region relative to `π₀`, then `D=∅` and `χ(π:π₀)=+1`.

*Proof.* Theorem 1 gives `κ_π(z+2β)=κ_π(z)` for every `z`. With `κ₀` periodic, `z∈D` exactly when `z+2β∈D`. A nonempty finite subset of `Z³` is not invariant under a nonzero translation. Under localization in a finite `Λ`, Theorem 3 gives `D⊂Λ̂`, a finite set, so `D=∅` and every ratio in `χ` is `1`. ∎

### R4. The displayed strings are not multiples of unitaries (referee closure, RCS1_REFEREE.md)

**Statement.** For every `x`, axis `e`, `r≥1` and `b`, neither `B_{r,b}(x)` nor its dipole variant is a scalar multiple of a unitary; in particular neither is an isometry. So no rescaling of `Ad B_{r,b}(x)` is an automorphism of `𝔄`, and the displayed strings give no instance of the automorphism form.

*Proof.* It suffices that `B^*B` is not a scalar. On `L5-U`, `B_{r,b}=Σ_a(T_1⋯T_{2r})_{ab}c^\dagger_{x,a}`, since link operators commute with matter. It is nonzero (Theorem 8(b) gives a vector it does not annihilate, for suitable `b`; relabel flavours for the others) and it annihilates every vector with all five modes at `x` occupied. So `B^*B` has a nontrivial kernel and is not a scalar. The dipole variant also annihilates every vector with empty matter at `y_{2r}`. On `L5-O[S_+]`, each `(T_i)_{ac}` is `±iη^{\rm far}_cη^{\rm near}_a`, with one sign for all indices; it is a self-adjoint unitary. Write `B_{r,b}=Σ_sW_s` over index sequences `s=(a_0,…,a_{2r−1})`, each `W_s` a product of commuting unitaries on matter and on the ray links. Equal sequences give `W_s^*W_s=1`, so `B^*B=10^{2r}+Y`. Two sequences that differ only in `a_0`, say `a≠a'`, give `W_s^*W_{s'}=γ_{x,a}γ_{x,a'}\,η^{ℓ_1,x}_aη^{ℓ_1,x}_{a'}`, whatever the common tail. Every other pair of different sequences gives a monomial with a Majorana of `ℓ_1`'s far end or of a later link. So `Y` contains `10^{2r−1}Σ_{a≠a'}γ_{x,a}γ_{x,a'}η^{ℓ_1,x}_aη^{ℓ_1,x}_{a'}`, which is not cancelled and is nonzero on `S_+`, since even bilinears act faithfully there. Hence `B^*B` is not a scalar. The dipole variant has the same `a_0`-terms. ∎


## 6. Conditional symmetry route

Global gauge transformations fix `𝔄^G`: on local fixed elements they reduce to a finite product of local gauge transformations, and density extends the result. Thus the global `U(5)` action on this algebra is trivial. At `μ=τ_E=0`, if an appropriately defined node fibre is unitarily identified with the free `C⁸` node representation and rotations, inversion, `Θ_d` and `σ` have the forms required by `MT1.md` C4, that result conditionally gives `N_j=aG_j` for real `a`. This is not a proof that such a fibre exists, or that these symmetries act as required. For the fixed-axis family in Theorem 8, rotation sends a ray to a different axis; escaping ray-end-number observables separate those families by Lemma 6, so this family by itself does not supply the required rotation implementer.

## 7. Proposed readings and four tests

The tests ask whether the reading (1) fixes a part's target, (2) is open-ended, (3) settles downstream physics by premise, or (4) adds unnecessary structure or constants. `P` means passed; `C` means conditional; `F` means failed. These are pass-1 judgments as corrected by the referee, not proofs or adopted readings.

| Reading or construction | 1 | 2 | 3 | 4 | Check and limitation |
|---|---|---|---|---|---|
| R-loc: odd species in the vacuum's field-algebra GNS representation | P | P | P | P | LZ1 Corollary 2.3 excludes its odd Clifford node under its hypotheses. Pattern pinning is not a classification of all charged representations. |
| R-CS^str(e): straight strings and covariant limit family of §5 | P | C | C | C | Test 2 is closed once the odd identification (R2’s `χ_tot` in parity-sharp backgrounds; an owner specification elsewhere) and the quantifiers over limit points and axis are fixed. The axis and endpoint are choices and may miss other dressings. Theorems 7–8 and Corollary 9 give the stated cases. The draft's “exists exactly when the string norms are positive” is corrected in §5. |
| R-CS^FMS: gauge-invariant odd composites `Φ*ψ` or odd elements of `𝔄^G` | P | P | P | P | Empty on both laws by Theorem 4, so it supplies no candidate. |
| R-CS^pair: infer odd dispersion from even gauge-invariant pair spectra | P | F | F | F | A fixed inference rule is missing. Any rule that reads one-particle bands from pair spectra presupposes that separated pairs factorize, which is the deconfinement question. Even pair observables do not by themselves supply a one-particle odd band. |
| R-CS^Dirac: superpose string dressings over many rays | P | F | P | C | No fixed weights or representation are supplied; no general obstruction for the cloud is proved. |
| R-CS^KR: finite-box global flux sectors with external links | P | P | P | F | Adds a boundary absent from the infinite law. Theorems 2–3 give a related native identity and localization result, not a construction of the full KR prescription. |
| R-CS^BR: light-cone charge classes | C | P | C | F | Test 1 passes only with the tick’s causal cone; with the relativistic light cone it presupposes LZ1’s target. Not constructed here; applicability of its relativistic hypotheses to the lattice tick needs proof. |
| Automorphism form: limit of adjoint actions of string unitaries | — | — | — | — | The displayed contracted quantum-link strings are not scalar multiples of unitaries (R4); this does not exclude a different unitary construction. |

For the inferred covariant representation, factor/configuration, localization and flux definitions, the draft judged all four tests passed. It judged `Λ̂` and `χ` likewise. These are precise choices; the theorem statements above retain their domains and do not turn the tests into evidence for physical identification.

## 8. RCS-P and failed routes

**RCS-P (open).** Does an update in LZ1's class, a locally gauge-invariant D1 state, and an axis `e` admit a covariant representation built from R-CS^str(e) sectors with a Clifford-node band? To answer the original *odd* version requires the charge/odd identification in §0; `χ_tot` supplies one candidate over parity-sharp backgrounds. By Corollary 9, any example must have two non-disjoint sectors at distinct transverse positions, or a sector that is not quasi-equivalent to its tick transform. Non-disjointness does not in general mean equivalence.

**A1, frozen backgrounds.** Locked states give no strings (Theorem 7); `ω_AB` gives transversely flat bands (Theorem 8). The draft extends this to every empty-matter product state with sharp end numbers. For a D1 gauge average of an empty-matter product state with sharp end numbers, each nonzero string term changes each ray end number by a fixed ±1 and leaves off-ray links unchanged. The electric layer is therefore a common phase; only the odd cube containing `x` and the eight even cubes meeting it act in the inverse matter layers. The local-unitary argument of Theorem 8(c), and Lemma 6 applied to a far ray end number versus its background value, give tick equivalence and transverse disjointness whenever covariantly chosen string limits exist. Corollary 9 then gives transverse flatness. On O, empty matter is not generally preserved by the Majorana hop, so this U-law argument does not transfer.

**A2, free links and Dirac clouds.** `CH1_5UQ.md` Theorem 4.2 bounds the norm of one-link expectation matrices by `1/2` on U. `EW1.md` reports a coherence bound `κ≤1/10` on `S_±` under its stated definition and hypotheses. These obstruct the particular lattice-scale c-number-unitary approximation; they do not exclude collective deconfinement, asymptotic equivalence of strings, or a different dressing. The proposed cloud has no specified weights or sector decomposition, so the claimed application of Theorem 5 is unproved.

**A3, loop condensation.** No appropriate fluctuating-loop D1 state is constructed in the draft. A plaquette class is open law data GA1-P-5, while matter hopping may itself generate loop dynamics. Absence of a specified plaquette layer does not prove absence of loop condensation. The route remains open.

**K, kill attempt.** The proof of conserved asymptotic ray labels for empty-matter `ω_AB` uses the fact that distant cube hops annihilate the state. In matter-filled states, including the tracial example, hops can act on ray links. No general conservation theorem is supplied. The attempted universal refutation of RCS-P fails at that step.

**Downstream.** MT1-S[R-CS^str] in the VC1 vacuum remains open with VC1. CH1's charged-correlator prescription and the choice R-CS remain owner questions. The conditional free-node symmetry route in §6 does not settle either. No law, axiom or working-set entry is changed here.
