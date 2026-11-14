# CG1-16-B. Spin(10) beyond site bilinears

## 0. Status

**FINISH: FROZEN 2026-11-07 after pass 3 (CG16B_REFEREE.md); the referee's edits E1-E7 are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `LW1_5.md` by one amendment together with the other CG1-16 probes (CG16D, CG16S, CG16K). The lead (Claude Opus 5.5, laptop) checked that each of E1-E7 is in the text and the replaced GAP text is gone; that is a text check, not a second referee. 

In the explicitly defined class 𝓛 below, an exact local Spin(10) action with its `−1` acting as site fermion parity exists. In a D1 representation, its local centre pattern is conserved. The exclusion of target (T) by Theorem 4.1(a) is definitional. Theorem 4.1(b), (c) and SC′ carry the content: with (F) and link-pure registers the physical subspace is matter-even, bands in the nontrivial-pattern subspace are flat near a node, and centre patterns are conserved. These are conditional statements about the definitions below; they do not exclude charged-sector particles or prove the CG1 target.

**NN compilation (referee closure, CG16B_REFEREE.md).** The cube generator of each witness is a sum of twelve even, gauge-invariant edge terms. By the proof of `LW1.md`'s dressed factorization, each cube gate is an exact finite word in even, gauge-invariant edge-triple gates, and the base tick has finite nearest-neighbour depth. So, under NN-a read with the witness registers, both witnesses are NN-a laws with nonzero angles; they also meet NN-b. `GA1_5.md` Proposition C does not apply as stated: its Lemma U compiles link-only unitaries. This gives no propagation.

**Charged-sector limits (referee closure, CG16B_REFEREE.md).** Under (F) with link-purity, over a parity-sharp D1 background sharp in every `z_x`, every straight-string limit keeps the background centre value at every site; a `χ_tot`-odd one is not finitely localized, and the class of the local `-1∈Spin(10)` sits in its boundary label: `φ_Λπ(F_{∂Λ})→χ_tot=-1` (referee closure, `CG16B_REFEREE.md` §3.2, Proposition L). Such sectors exist in the rishon witness at every angle (Example S). On `L5-O[S_+]` every end is end-pure for `-1∈Spin(10)` (`LW1_5.md` Σ), so each `F_{∂Λ}` built from these ends is a scalar and the same boundary label is `+1` for every sector. Whether these sectors carry a band is RCS-P on an (F)-law.

**Open by name.** RCS-P (inherited, including on an (F)-law); LW1-5-T; LW1-5-X-B_m (`2≤m≤8`); LW1-5-X-O; R-CG1; R-CS; MT1-S[R-CS^str] in the VC1 vacuum; CG1-i; CG1-ii; MT1-ii; MT1-S; VC1; R-16^str′ (owner question, candidate not adopted). No law, reading or axiom is adopted.

**Provenance.** Pass 1: Claude Opus 5.5, maximum effort, `CG16B_DRAFT.md`, SHA-256 `3f46ee993ee3bfafb6ad64efa0c71d7081e7cf1fa7693380a119d17bfbb1ae9c`. Pass 2: Codex `gpt-6.1-terra`, effort and session id: see run log. Context: `prior/CG16B.md`, `TOE_ASSEMBLY.md` §§3.4–3.6, `LW1_5.md`, `RCS1.md`, `LZ1.md`, `LW1.md`, `MT1.md`, `GA1_5.md`, `LW1_5X.md`. The pass-3 referee closures are not themselves refereed; no numerical proof is claimed. The draft's literature searches and their access limits are recorded in `CG16B_DRAFT.md` §2; this pass does not independently verify them. The digest records prior results, not an independent audit. Editing session: Codex gpt-6.1-terra, effort high, codex-cli 0.165.0; session id not visible.

**Prior work used.** The draft’s §1 lists S′ and its non-Bogoliubov proof, alternative A, SC and SC.1, the one-ended construction, F and K, the reducible-register repair, #10027, #10038, #10045, #10023, R-CS^str and `RCS1.md`, `MT1.md` Theorems 5–6 and C8, `LZ1.md` Theorems 2.1–2.2, `LW1_5.md` M, M.1 and B1-U, and NN-a. Further pointers from `CG16B_REFEREE.md` §7: `LW1.md` dressed factorization; `GA1_5.md` Lemma U and Proposition C (only its parallel-run step applies here); `LW1_5X.md` for the all-angle bound; and `RCS1.md` line 91 and R3 for the sharp-background and configuration-difference precursors.

## 1. Definitions inferred by the distiller

1. Sites are `Z³`, each with five CAR modes, ten Majoranas `γ_a`, and parity `P=(-i)^5γ_1⋯γ_10`. The site Hilbert space is `H=H_+⊕H_-`, each summand of dimension 16. The site algebra is `End(H)`, graded by `Ad P`; distinct sites use the graded tensor product. Link factors commute with matter. `θ` is global matter parity on the quasi-local algebra.
2. Let `G=Spin(10)` be the group generated on `H` by `exp(i t M^{ab})`, `M^{ab}=iγ_aγ_b/2`. Its centre is `{±1,±ω}`, where `ω²=−1` and `ω=−iP` in this representation. The standard half-spin representation on `H_+` is `S_+` (`LW1_5.md` §4). A site representation is a continuous `u:G→U(H)` commuting with `P`, so `u=ρ_+⊕ρ_-`. Its frame action is `Ad u`. Define S′ by `u=S_+⊕1`; define **(F)** by `Ad u(−1)=Ad P`. The bilinear representation is `u(g)=g`.
3. A law belongs to **𝓛** when each nearest-neighbour link `ℓ=(x,y)` has a finite Hilbert space with commuting continuous unitary endpoint representations `ρ_{ℓ,x},ρ_{ℓ,y}` of `G`; the same site representation `u` is used at each site; and the local gauge action `Γ_x(g)` is conjugation by
   `Z_x(g)=u_x(g) ⊗ ∏_{ℓ∋x}ρ_{ℓ,x}(g)`.
   Its update `α` is a finite-depth local even automorphism as in `LW1.md` E1 and commutes with every `Γ_x(g)`. This class does not itself require NN-a's nearest-neighbour decomposition or cell covariance. End actions that entangle different links lie outside this definition. Site-dependent `u_x` can be treated by the same local arguments, with (F) imposed at each site.
4. Put `z_x=Z_x(−1)`. An operator is spinor class at `x` if `Ad z_x(A)=−A`, tensor class if it is fixed. A link is **link-pure** if `ρ_{ℓ,x}(−1)ρ_{ℓ,y}(−1)` is scalar; it is **end-pure** at `x` if `ρ_{ℓ,x}(−1)` is scalar. These definitions concern the central element `−1`; spinor class alone does not specify an irreducible 16.
5. For an even-translation covariant law with `τ_β(z_x)=z_{x+2β}`, a D1 state is stationary, invariant under `τ_β` and invariant under every `Ad z_x`. Its GNS triple is `(H_ω,π,Ω)`; the corresponding implementers fixing `Ω` are `Ũ,T_β,U_x`. Let `𝔄^G` be the fixed algebra of all local gauge actions and `H_phys=closure π(𝔄^G)Ω`. A vector is spinor class at `x` if `U_xv=−v`. Let `𝒮` be the closed span of all such vectors. When `ω` is parity-invariant, `H_odd` and `H_even` denote the parity eigenspaces.
6. A band `(d,F,V)`, node and leading generators `N_j=∂_j(i log V)(K₀)` mean `LZ1.md` §1: `F` is an isometry from `L²(T³;C^d)`, intertwines translations and tick with multiplication by `e^{iK·β}` and `V(K)`, and `V(K₀)=1` with `V` continuous on `T³` and continuously differentiable nearby. Propagation means some `N_j≠0`.
7. The draft's precise **target (T)** asks for an (F)-law in 𝓛, a D1 state, and a band whose image lies in `H_phys∩H_odd∩𝒮`, with a node and some nonzero `N_j`. This is one formalization of the brief, not a definition of every possible physical or charged-sector reading.
8. The **diagonal identification** means `∏_{x∈Λ}Ad z_x(A)=θ(A)` for each local `A` and every finite `Λ` containing its matter sites and both ends of its supported links. It formalizes equality of the internal central action and the lattice spin-lift parity action on local operators; it does not construct a spacetime spin structure or a quotient group action.
9. For charged sectors use the factor representations, finite localization, relative class `χ`, background parity-sharpness, `χ_tot`, straight-string states and covariant band definitions of `RCS1.md` §§1, 3, 5 and R2. These are distinct from field-algebra vectors. R-CS^str is a working candidate, not adopted.

## 2. Site representations and conserved centre

**Theorem 2.1 (implementers).** `−1` is a commutator in `G`. For every law in 𝓛, the `z_x` are commuting self-adjoint unitaries and `α(z_x)=z_x`.

*Proof.* With `a=γ_1γ_2`, `b=γ_2γ_3`, both lie in `G` and `aba^{-1}b^{-1}=−1`. The `z_x` are involutions; distinct ones commute because site factors are even and endpoint actions commute. Covariance of `α` with `Γ_x(g)` makes `Z_x(g)^{-1}α(Z_x(g))` central in the quasi-local algebra. It is local, hence scalar. These scalars form a character of `G`, so they send the commutator `−1` to 1. □

**Theorem 2.2 (embedding E).** (a) (F) holds exactly when `u(−1)=εP`, `ε=±1`. (b) Under (F), every odd site operator is negated by `Ad u(−1)`, every even one fixed. (c) No such action is Bogoliubov. (d) S′ satisfies (F) with `ε=−1`; the bilinear action has `u(−1)=−1` and fails (F). (e) The two odd blocks transform as `ρ_+⊗ρ_-*` and `ρ_-⊗ρ_+*`; for S′ the first contains 16 copies of `S_+`.

*Proof.* (a) Equal inner automorphisms on `M_32` have implementers differing by a scalar; their squares make it `±1`. (b) follows from the grading. For (c), suppose a continuous induced `R:G→O(10)` acts on the Majoranas. Then `R(−1)=−I`. The kernel of `dR` is an ideal of simple `so(10)` and cannot be all of it; hence it is zero. The discrete normal kernel of `R` is central. It contains neither `−1` nor `±ω`, whose square is `−1`, and so is trivial. The 45-dimensional connected image is all of `SO(10)`, contradicting the centre orders four and two. For (d), `S_+(−1)=−1` and the other S′ block is trivial; the bilinear lift of `−1` is scalar `−1`. Finally `X∈Hom(H_-,H_+)` transforms as `ρ_+Xρ_-^{-1}`. □

**Corollary 2.3.** No (F) embedding is compatible gate by gate with an L5-O or L5-U cube generator, or with a cube gate outside the exceptional set of `LW1_5.md` M. The whole-tick question is LW1-5-T. For `L5-U[1]` and `L5-U[9]` the gate-wise statement holds at every window angle, by `LW1_5X.md` (frozen).

*Proof.* Both specified hops have faithful one-mode inflow. `LW1_5.md` M proves that their compatible frames are Bogoliubov, including gates outside the exceptional set. Apply Theorem 2.2(c). □

The S′ construction and its non-Bogoliubov proof were already proved in `LW1_5.md` §4, as recorded in `prior/CG16B.md`. To see what is supplied, put `E_{αi}=|α⟩⟨i|` from `H_-` to `H_+`. Then `E_{αi}E_{βj}=0` and `{E_{αi},E_{βj}†}=δ_{ij}|α⟩⟨β|+δ_{αβ}|j⟩⟨i|`. Thus these 16-component operator families are not CAR modes. They do not by themselves supply the free CAR band of #10023 part B (`prior/CG16B.md`).

**Theorem 2.4 (diagonal D).** The diagonal identification holds exactly when (F) holds and every link is link-pure. Every continuous homomorphism from `G` to a finite group is trivial.

*Proof.* Test the identity on a single site to obtain (F), and on one link with both endpoints included to obtain scalar endpoint product. Conversely, in the product over `Λ`, interior link factors are scalars, boundary factors act outside the support, and site factors give `θ`. The last assertion follows because the continuous image of a connected group in a finite discrete group is a point. □

`MT1.md` Theorem 5 identifies the lattice lift's half-turn commutator with matter parity; its Theorem 6 proves an analogous parity identity for the live laws. This does not identify the live-law local `ω` with the internal `−1` of an (F) embedding.

## 3. Finite-register witnesses

**Theorem 3.1 (W).** The full-frame alternative A of `LW1_5.md` §4, restricted to S′, is a law in 𝓛 with link-pure registers. So is the following rishon cube construction; its cube gates are separately gauge invariant and its base tick is cell covariant.

On each link take 16 fermionic rishon modes at each end, commuting with matter, restricted to total number `m`, `1≤m≤31`. Let the endpoint representation be the second quantization of `S_+`. Define
\[
 h_{xy}=\sum_i\left(\sum_\alpha E_{y,\alpha i}r^y_\alpha\right)
 \left(\sum_\beta r^{x\dagger}_\beta E^\dagger_{x,\beta i}\right)+\mathrm{h.c.},\qquad
 H_C=3^{-1/2}\sum_{(x,y)\subset C}\eta_i(x)h_{xy}.
\]
Use the two cube tilings and sign lifts of `LW1_5.md` §2, and no electric layer.

*Proof.* For A, the odd-operator representation `π` has `π(−1)=−1`; on `C^512_x⊕C^512_y` the two end actions are `\bar π⊕1` and `1⊕\bar π`, so their centre product is `−1`. Gauge and cell covariance are proved in `LW1_5.md` §4.

For the rishon construction, `E_{·i}` transforms as `S_+`, while `E†` transforms conjugately. The contractions `Σ r^{x†}_β E†_{x,βi}` and `Σ E_{y,αi}r^y_α` are invariant by unitarity of `S_+`. The hop preserves total rishon number and has two odd matter factors, so it is even and defines finite-support gates. The centre endpoint product is `(−1)^m`. Under a cell lift, the signed site relabelling sends `E_{x,αi}` to `d_g(gx)E_{gx,αi}`; rishon modes are permuted, and a reversed link exchanges the displayed term and its adjoint. The sign identity and tiling preservation of `LW1_5.md` B1-U therefore carry `H_C` to `H_{gC}`. The cube layers define a finite-depth local automorphism. □

**Lemma NN-W (referee closure, CG16B_REFEREE.md).** Let the law be the rishon witness of Theorem 3.1, or alternative A restricted to S′, with `H_C=3^{-1/2}Σ_{ℓ⊂C}η_i(x)h_ℓ` (`h_ℓ=h^{full}_ℓ` for A).
(a) Each cube gate `e^{-iaH_C}` is an exact finite product of unitaries `e^{-ith_ℓ}`, `t∈ℝ`, `ℓ⊂C`. Each factor is even, commutes with every `Z_x(g)`, and acts within one edge triple `F_x,F_y,H_ℓ`.
(b) The base tick is a composition of finitely many layers, independent of volume, each a product of gates on pairwise disjoint edge triples. The complete update fixes every local gauge generator.
(c) With the cell covariance of Theorem 3.1 (rishon) and of `LW1_5.md` §4 (A: "the cube construction is cell covariant"), both witnesses meet NN-a read with their own registers. The compiled factors are gauge invariant one by one, so NN-b also holds.

*Proof.* (a) Each `h_ℓ` is a sum of terms (odd at `y`)(odd at `x`)(link operator), plus the adjoint. Rishon bilinears `r^y_αr^{x†}_β` keep total rishon number, so they act on the fixed-number register `H_ℓ`; for A the link factor is `|i,x⟩⟨j,y|`. A product of two odd site elements commutes with `P_xP_y`. So `h_ℓ` is an even element of the edge-triple algebra. It commutes with every `Z_x(g)` by Theorem 3.1 (`LW1_5.md` §4 for A). Put `X_ℓ=-i3^{-1/2}η_i(x)h_ℓ`, so `-iH_C=Σ_{ℓ⊂C}X_ℓ`. Work in the unitary group of the finite-dimensional space of one cube. Let `𝔤` be the real Lie algebra generated by the twelve `X_ℓ`. Let `𝖫` be the connected analytic subgroup with Lie algebra `𝔤` (analytic subgroup theorem). Let `𝖧` be the group of finite words in the `exp(tX_ℓ)`. Then `𝖧⊆𝖫`. Rebuilt from `LW1.md` lines 198-205: let `𝔳` be the span of all `Ad_hX_ℓ`, `h∈𝖧`. It is `Ad_{exp(tX_ℓ)}`-invariant; differentiating at `t=0` gives `[X_ℓ,𝔳]⊆𝔳`, so `𝔳⊇𝔤`. Also `𝔤` is invariant under `Ad_{exp(tX_ℓ)}=exp(t ad X_ℓ)`, so `𝔳⊆𝔤`. Choose a basis `Y_k=Ad_{h_k}X_{ℓ_k}` of `𝔤`. The map `(t_k)↦∏_kh_k exp(t_kX_{ℓ_k})h_k^{-1}` is smooth into `𝖫`, lands in `𝖧`, and has derivative `(t_k)↦Σ_kt_kY_k` at zero, an isomorphism onto `𝔤`. The inverse function theorem on `𝖫` puts a neighbourhood of the identity of `𝖫` inside `𝖧`. So `𝖧` is an open subgroup of the connected group `𝖫`, and `𝖧=𝖫`. Since `-iaH_C∈𝔤`, `e^{-iaH_C}∈𝖧`: an exact finite word, not a Trotter limit. Each letter `exp(tX_ℓ)` is `e^{-it'h_ℓ}` with `t'` real.
(b) "The even translations preserve the tilings and the parity-dependent signs" (`LZ1.md` §1), so `H_{C+2β}=τ_β(H_C)`. Fix one word for one cube of each tiling and translate it. Cubes of one tiling have disjoint sites and links, so the `k`-th letters of all translated words lie on pairwise disjoint edge triples and form one layer. Even gates on disjoint supports commute, and a locally finite product of them is an automorphism (`LW1.md` E1). The depth is the sum of the two word lengths. Every letter commutes with every `e^{it𝒢_x}`, so the complete update fixes `e^{it𝒢_x}` for all `t`; differentiating at `t=0` in the finite-dimensional local algebra, it fixes `𝒢_x`.
(c) follows from (a), (b) and the cited covariance. □

**NN compilation (referee closure, CG16B_REFEREE.md).** The cube generator of each witness is a sum of twelve even, gauge-invariant edge terms. By the proof of `LW1.md`'s dressed factorization, each cube gate is an exact finite word in even, gauge-invariant edge-triple gates, and the base tick has finite nearest-neighbour depth. So, under NN-a read with the witness registers, both witnesses are NN-a laws with nonzero angles; they also meet NN-b. `GA1_5.md` Proposition C does not apply as stated: its Lemma U compiles link-only unitaries. This gives no propagation. The rishon hop also has local `U(16)` on `H_+` and global `U(16)` on the `H_-` index; the latter is not shown to be local. Whether PS-6 requires every such global internal symmetry to be local is a reading question, not settled here. NN-a is read with the witness register in place of the chosen link register; the witnesses stay unadopted.

## 4. Physical vectors, patterns and the target

**Theorem 4.1 (N).** Let a law in 𝓛 be even-translation covariant as in Definition 5, and let `ω` be D1.

(a) Every vector in `H_phys` is fixed by every `U_x`; hence `H_phys⊂H(1)` and `H_phys⊥H_nt⊇𝒮`, where `H(1)` is the trivial-pattern subspace and `H_nt` is defined in (c).

(b) If (F) and link-purity hold, every element of `𝔄^G` is matter-even, `ω` is parity-invariant, and `H_phys⊂H_even`.

(c) `H_ω` is the orthogonal sum of joint eigenspaces for finite-support sign patterns of the `U_x`. The tick preserves each pattern and translations shift it. The sum `H_nt` of nontrivial patterns contains `𝒮`. Every band with image in `H_nt` is identically 1 on a connected `C¹` neighbourhood of a node. Under (F) and link-purity, `H_odd⊂H_nt`.

Thus target (T) has no instance in 𝓛. Part (a) alone proves that definitional exclusion; (b), (c) and SC′ carry the content described above.

*Proof.* (a) For `A∈𝔄^G`, `Γ_x(−1)(A)=A`, so `U_xπ(A)Ω=π(A)Ω`. The `−1` eigenspace is orthogonal to the fixed subspace; take closed spans.

(b) Local invariant elements are dense in `𝔄^G`: approximate by a local element and average over the finite product of compact site groups acting on its matter and link endpoints. The average is local and fixed, and does not increase the approximation error. Theorem 2.4 makes the product of the centre actions parity on a sufficiently large finite support. A local invariant element is therefore even; density extends this to `𝔄^G`. The D1 state is invariant under the same finite products, so it is parity-invariant, and fixed elements create even vectors.

(c) For local `A`, let `Λ` contain its matter sites and link ends. Character averaging over the commuting involutions `Ad z_x`, `x∈Λ`, decomposes `A` into joint eigenoperators; outside `Λ` they act trivially because site factors are even and their link factors lie outside the support of `A`. Applying them to `Ω` and using cyclicity yields the finite-pattern decomposition. Theorem 2.1 makes the tick preserve the patterns; translations shift them. Every nonempty finite subset of `Z³` has trivial translation stabilizer. As in `LZ1.md` Theorem 2.1, choose one representative per orbit and Fourier transform to get `H_nt≅L²(T³;K)`, `T_β=M_β`, `Ũ=1⊗W` for a unitary `W` on separable `K`. The band intertwiner is a measurable fibre isometry, so eigenvalues of `V(K)` lie almost everywhere in the countable point spectrum of `W`. The `C¹` power traces are constant on a connected neighbourhood; Newton identities and `V(K₀)=1` give `V=1` there, as in `LZ1.md` Theorem 2.2. With (F) and link-purity, the product of the character signs of an odd local component is `−1`; density puts the odd subspace in `H_nt`. □

The pattern and flatness proofs extend the already proved `LZ1.md` Theorems 2.1–2.2. The evenness conclusion extends `RCS1.md` Theorem 4, itself credited there to `MT1.md`. These results do not exclude bands in other representations of `𝔄^G`.

**Theorem 4.2 (O; link-purity is needed).** There is an (F)-law in 𝓛 with a D1 state and a nonzero odd physical vector.

*Proof.* Use S′ and on each link set `H_ℓ=(C|0_x⟩⊕V_x)⊕(C|0_y⟩⊕V_y)`, with each `V≅S_+`; the `x` group acts only on `V_x`, the `y` group only on `V_y`. Put `Y=Σ_β |β_x⟩⟨0_x| E†_{x,βi}`. The fundamental and conjugate factors contract to a gauge invariant, nonzero odd operator. The endpoint centre product is `+1` on the two vacuum lines and `−1` on `V_x⊕V_y`, so the link is not link-pure. Choose the identity update and the unique tracial state; it is translation and gauge invariant, stationary and faithful. Then `π(Y)Ω` is nonzero, odd and physical. By Theorem 4.1(a) it is tensor class at every site. □

Example O also shows that link-purity is needed for `H_odd⊂H_nt`: `π(Y)Ω` is odd and lies in `H(1)`.

## 5. The static-centre theorem

**Theorem 5.1 (SC′).** Theorem SC(a)–(e) of `LW1_5.md` §5 holds for every law in 𝓛 with the present `z_x`. In particular, a local operator has a finite decomposition into centre-pattern eigenoperators; a component of pattern `T` flips exactly those centre eigenvalues, and the resulting difference remains on `T` at every tick in the sharp-state experiment of SC(e).

*Proof.* Theorem 2.1 supplies the commuting conserved involutions. For an operator supported on matter sites and links with both ends in `S`, the site factor of `z_x` for `x∉S` is even and hence commutes with the operator; its link factors are disjoint. The character projections and projection-intertwining identity in `LW1_5.md` SC(b,c) apply. Conservation gives SC(d); the sharp-state conclusion SC(e) follows from that identity and Cauchy–Schwarz, exactly as in the cited proof. □

Under (F), an odd undressed site operator flips the local centre sign. The theorem pins that sign, not a matter occupation. In the rishon hop, an allowed nonzero matrix element changes `P_x,P_y` and both endpoint rishon parities simultaneously; the products `−P_x(−1)^{p_x}` and `−P_y(−1)^{p_y}` stay fixed. This is an operator-level transfer, not a demonstrated propagating physical band. Under the bilinear embedding the site factor of `z_x` is scalar, so matter operators alone are tensor class (`LW1_5.md` F and K). SC′ does not cover entangled register changes outside 𝓛, or a charged-sector band in a different representation.

NN-a implies the covariance assumption of 𝓛 when the update fixes each local gauge generator: it then commutes with their exponentials and the generated local group. Theorem 2.1 does not require each intermediate gate to be gauge invariant. PS-6 motivates local frame changes but does not itself prove that every possible register implementation has the product form in Definition 3.

## 6. Charged sectors and other centre labels

**Theorem 6.1 (C, qualified).** Assume (F) and link-purity. Each `z_x` is central in `𝔄^G`, fixed by `α`, and for finite `Λ`
\[
 \prod_{x\inΛ}z_x=\varepsilon^{|Λ|}s_Λ P_Λ F_{\partial Λ},\quad
 s_Λ=\prod_{\ell\subset Λ}\rho_{\ell,x}(-1)\rho_{\ell,y}(-1),\quad
 F_{\partial Λ}=\prod_{\ell\in\partial Λ}\rho_{\ell,\mathrm{in}}(-1).
\]
For finitely localized factor sectors relative to a factor background, the relative centre class `χ` of `RCS1.md` Theorem 3 equals its relative parity. If the law is even-translation covariant as in Definition 5 and the registers are translation-covariant, and if the background configuration is cell-periodic and `χ=−1`, no nonzero cell translation is implemented in that sector. The conditional transverse-flatness conclusion of `RCS1.md` Corollary 9 applies to covariantly chosen ray sectors when its disjointness and tick-equivalence hypotheses hold.

*Proof.* Centrality of `−1` and commuting opposite endpoint actions make each `z_x` gauge invariant; its adjoint action is itself a local gauge transformation, so it is central in the fixed algebra. Theorem 2.1 gives conservation. Multiplying site and link factors gives the displayed identity; each boundary factor is gauge invariant. For the relative parity identity, use the localization intertwiner on the boundary flux and divide the two factor-representation identities. The remaining scalar ratio is exactly `χ`. A nonempty finite configuration difference cannot be invariant under a nonzero translation; different central scalar values make the representations disjoint, as in `RCS1.md` Theorem 3. Corollary 9 is an abstract conditional representation argument and applies under its own hypotheses. □

**Theorem 6.2 (finite strings).** In the rishon witness, for a straight path `y_0=x,…,y_{2r}`, set `T_i=(r^{ℓ_i,y_{i-1}}_a r^{ℓ_i,y_i†}_b)_{ab}` and
`B_{r,b}=Σ_a E_{x,ai₀}(T_1⋯T_{2r})_{ab}`. It is matter-odd, invariant under gauge transformations except at the free end, and is spinor class there and tensor class at every other site.

*Proof.* At the initial and interior sites, fundamental and conjugate indices are contracted; unitarity cancels each local transformation. At the far end the uncontracted creator transforms in `S_+`, and its `−1` action supplies the minus sign. There is one odd matter factor. □

**Charged-sector limits (referee closure, CG16B_REFEREE.md).** Under (F) with link-purity, over a parity-sharp D1 background sharp in every `z_x`, every straight-string limit keeps the background centre value at every site; a `χ_tot`-odd one is not finitely localized, and the class of the local `-1∈Spin(10)` sits in its boundary label: `φ_Λπ(F_{∂Λ})→χ_tot=-1` (referee closure, `CG16B_REFEREE.md` §3.2, Proposition L). Such sectors exist in the rishon witness at every angle (Example S). On `L5-O[S_+]` every end is end-pure for `-1∈Spin(10)` (`LW1_5.md` Σ), so each `F_{∂Λ}` built from these ends is a scalar and the same boundary label is `+1` for every sector. Whether these sectors carry a band is RCS-P on an (F)-law.

**Proposition L (referee closure, CG16B_REFEREE.md).** Take a law in 𝓛 with (F), every link link-pure, even-translation covariant. Let `ω` be a D1 state with `ω(z_y)=κ₀(y)∈{±1}` for every site `y`. (This holds when the representation of `𝔄^G` on `H_phys` is a factor, because `z_y` is central in `𝔄^G`.) Fix `x` and an axis. Let `B_{r,b}∈𝔄` commute with `z_y` for every `y≠y_{2r}`, as the strings of Theorem 6.2 do. Put `ω_r(A)=Σ_bω(B^*_{r,b}AB_{r,b})/Σ_bω(B^*_{r,b}B_{r,b})` on `𝔄^G`. Let `ω_∞` be a weak-* limit point along lengths with positive denominators, with GNS triple `(H_∞,π_∞,Ω_∞)`.
- (i) `π_∞(z_y)=κ₀(y)1` for every `y`: the centre configuration of the limit equals the background's at every site.
- (ii) If `ω(P_Λ)=ε_Λ∈{±1}` for every finite `Λ`, and each `B_{r,b}` is matter-odd with its matter at `x`, then `ε_Λπ_∞(P_Λ)→-1` strongly along the net of finite `Λ`, that is, `χ_tot(π_∞:ω)=-1` (`RCS1.md` R2).
- (iii) Under (ii), put `φ_Λ=ω(F_{∂Λ})`. Then `φ_Λ∈{±1}` and `φ_Λπ_∞(F_{∂Λ})=ε_Λπ_∞(P_Λ)` for every finite `Λ`. So the boundary label `φ_Λπ_∞(F_{∂Λ})` tends strongly to `χ_tot=-1`.
- (iv) Under (ii), if `π_∞` and the representation `π₀` of `𝔄^G` on `H_phys` are factors, `π_∞` is not localized in any finite set relative to `π₀`.

*Proof.* (i) For fixed `y` and large `r`, `y≠y_{2r}`, so `B^*z_yB=B^*Bz_y`. Since `z_y^2=1` and `ω(z_y)=κ₀(y)`, `ω((z_y-κ₀(y))^2)=0`. Cauchy-Schwarz gives `|ω(Y(z_y-κ₀(y)))|^2≤ω(YY^*)ω((z_y-κ₀(y))^2)=0` for every `Y`. So `ω_r(z_y)=κ₀(y)` for large `r`, and `ω_∞(z_y)=κ₀(y)`. Then `‖(π_∞(z_y)-κ₀(y))Ω_∞‖^2=0`. As `z_y` is central in `𝔄^G` (Theorem 6.1), `π_∞(z_y)π_∞(A)Ω_∞=κ₀(y)π_∞(A)Ω_∞`; cyclicity gives the claim.
(ii) `P_Λ∈𝔄^G`, since `u(g)` commutes with `P`. For `x∈Λ`, `P_ΛB=-BP_Λ`; the step of (i) gives `ω_r(P_Λ)=-ε_Λ`, hence `π_∞(P_Λ)Ω_∞=-ε_ΛΩ_∞`. A local `A∈𝔄^G` with matter in `Λ` is even (Theorem 4.1(b)), so `P_ΛAP_Λ=A` and `ε_Λπ_∞(P_Λ)π_∞(A)Ω_∞=-π_∞(A)Ω_∞`. Such `Λ` form a tail of the net. Local elements are dense in `𝔄^G` (Theorem 4.1(b)) and the net is bounded by one.
(iii) Theorem 6.1 gives `∏_{z∈Λ}z_z=ε^{|Λ|}s_ΛP_ΛF_{∂Λ}`, with commuting gauge-invariant factors and `s_Λ=±1`. Apply `ω` and the step of (i): `∏_Λκ₀=ε^{|Λ|}s_Λε_Λω(F_{∂Λ})`, so `φ_Λ=ε^{|Λ|}s_Λε_Λ∏_Λκ₀∈{±1}`. Apply `π_∞` and (i): `∏_Λκ₀·1=ε^{|Λ|}s_Λπ_∞(P_Λ)π_∞(F_{∂Λ})`. Multiply by `π_∞(P_Λ)`, using `P_Λ^2=1`: `π_∞(F_{∂Λ})=φ_Λε_Λπ_∞(P_Λ)`. Multiply by `φ_Λ`; (ii) gives the limit.
(iv) Suppose `π_∞` is localized in finite `Λ` via `V`. Theorem 6.1's port of `RCS1.md` Theorem 3 gives `π_∞(P_{Λ'})=χV^{-1}π₀(P_{Λ'})V` for finite `Λ'⊇Λ̂`, with `χ=∏_{Λ̂}κ_∞/κ₀=+1` by (i). On `H_phys`, `ε_{Λ'}π₀(P_{Λ'})→1` strongly: `π₀(P_{Λ'})Ω=ε_{Λ'}Ω`, `P_{Λ'}A=AP_{Λ'}` for even `A` with matter in `Λ'`, and `H_phys⊂H_even` (`RCS1.md` R2(b), rebuilt in these two steps). So `ε_{Λ'}π_∞(P_{Λ'})→+1`, against (ii). □

**Example S (referee closure, CG16B_REFEREE.md).** Take the rishon witness at any angles, `m=16`. Let `Φ` be the product vector with matter `|i_0⟩∈H_-` at every site, and on every link all 16 rishons at its source end and none at its target end.
- Every summand of `h_ℓ` ends in `E^†_{x,βi}` or `E^†_{y,αi}`, and `E^†=|i⟩⟨β|` kills `H_-`. So `H_CΦ=0`, every cube gate fixes `Φ`, and `ω_Φ` is stationary.
- `ω_Φ` is translation invariant and locally gauge invariant: `S_+(g)⊕1` fixes `H_-`; a full end changes by `det S_+(g)=1`, because `tr(Π_+M^{ab})=(i/4)tr(γ_aγ_b(1+P))=0` (`γ_aγ_b` and `γ_aγ_bP` are non-scalar Clifford monomials); an empty end is fixed. So it is D1.
- `P_y=-1` everywhere, so `ε_Λ=(-1)^{|Λ|}`. `z_y=-P_y∏_{ℓ∋y}(-1)^{p_{ℓ,y}}=+1` sharply (three full ends, three empty).
- For the strings of Theorem 6.2 along `+e_1`, each term of `B_{r,b}Φ` empties a full source end and fills an empty target end, and `E_{x,ai_0}|i_0⟩=|a⟩`. Distinct index sequences give orthogonal unit vectors, so `Σ_b‖B_{r,b}Φ‖^2=16^{2r+1}>0`. Limit points exist by weak-* compactness.

By Proposition L, every limit point is a `χ_tot`-odd string sector with centre value `+1` at every site and boundary label `-1`. So the draft's "a `χ_tot`-odd straight-string sector, which under (F) is a spinor sector" is false if "spinor sector" means `RCS1.md` Theorem 3's relative class `-1`.

On L5-O with uniform `S_+` ends, the lift of internal `−1` gives scalar `z_x=−1` (`LW1_5.md` Σ), so this `−1` label is trivial; the live-law odd label uses a different central element (`RCS1.md`).

**Theorem 6.3 (route comparison).** Under (F), the site factor of `z_x` is `εP_x`. Under S′, `ω` acts by `−i` on `Hom(H_-,H_+)` and by `+i` on the reverse block.

*Proof.* The first statement is Theorem 2.2(a). On `H_+`, `ω=−iP=−i`; on the trivial S′ block it is 1. Conjugation gives the stated phases. □

The site-count route #10038 and the literal-centre/spinon route #10045 have different hypotheses and are recorded in `prior/CG16B.md`; neither is closed by this comparison. The #10027 fixed-site bilinear centre theorem is already in the repository as cited by that digest. S′ drops its bilinear hypothesis. It supplies a spinor operator index but does not establish a physical family, chirality, charge identification, a mirror gap or a propagating sector.

## 7. Proposed readings and four tests

The four tests ask whether an item (1) fixes a target, (2) is closed rather than open-ended, (3) settles a downstream physics question by premise, and (4) adds unneeded structure. P, C and F below are pass-1 judgments, except for the referee’s revisions to R-16^str and the new R-16^str′ tests; they are not independently established axioms. None is adopted.

| Item | 1 | 2 | 3 | 4 | Qualification |
|---|---|---|---|---|---|
| 𝓛 | P | P | P | P | Explicit product end actions and finite-depth updates; it does not exhaust PS-6 or enforce NN-a. |
| (F) as a studied hypothesis | P | P | P | P | The condition is supplied by the brief, not derived. |
| Centre classes, link/end purity, vector class | P | P | P | P | Definitions 4–5; a centre class does not alone mean a 16. |
| Target (T) | P | P | P | P | Field-GNS formalization only; it excludes charged-sector interpretations. It states the lane’s question, so test 1 marks no smuggled premise. |
| Diagonal identification | P | P | P | P | Equality of actions on local operators; not a constructed spin-structure quotient. |
| (F) as law data | F | P | F | C | Selects the odd operator class; an independent reason for the choice is not supplied. |
| Rishon witness as a law | F | P | F | C | Inherits (F); 16 rishon modes per end and extra symmetries are supplied. NN compilation: referee closure, §3.1 of `CG16B_REFEREE.md`. |
| Alternative A | P | P | C | F | Full-frame law is an unadopted alternative in `LW1_5.md`; its large group is extra structure. |
| **R-16^str, candidate** | P | F | P | P | “Under the working candidate R-CS^str with `χ_tot` (`TOE_ASSEMBLY.md` section 3.6), CG1(e)'s 'the spinor 16 rather than the vector 10' is read as: the `χ_tot`-odd string sectors have relative class `-1` under the local `-1∈Spin(10)`, that is, the free end of their strings carries a spinor-class representation (Proposition C).” Relative class is undefined for these non-finitely localized limits, or is `+1` if read through the centre configuration; the free end exists only for finite strings. |
| **R-16^str′, owner candidate (not adopted)** | P | C | P | P | “Under the working candidate R-CS^str with `χ_tot` over parity-sharp backgrounds (`TOE_ASSEMBLY.md` §3.6), for a background also sharp in every local centre implementer, CG1(e)'s 'spinor rather than vector' is read on the `χ_tot`-odd string sectors `π` as the boundary label of the local `-1∈Spin(10)`: the strong limit of `φ_Λπ(F_{∂Λ})`, where `F_{∂Λ}=∏_{ℓ∈∂Λ}ρ_{ℓ,in(ℓ)}(-1)` and `φ_Λ` is its background value. Spinor class means the limit is `-1`.” Test 2 inherits R-CS^str’s open quantifiers over limit points and axis; its own terms are closed. |
| PS-6-all, not proposed | P | P | C | P | Would require every internal symmetry of the update to be local; this bears on family symmetries and is not settled here. |

R-16^str′ specifies where the class is read; it does not establish an irreducible 16 or a band. On an (F)-law with link-purity the boundary label is `−1` by Proposition L(iii); on `L5-O[S_+]` it is `+1`, and on `L5-U` the reading does not apply. It decides neither existence nor motion; test 1 locates the class without fixing its value, test 3 follows from the law rather than a premise of the reading, and test 4 uses existing structures with the sharpness needed for `φ_Λ`.

## 8. Review boundary

The negative statement proved here is the explicit incompatibility in Theorem 4.1(a), not a no-go for every Spin(10) law or every physical charge prescription. The draft also records potential routes outside this domain: charged representations, site-count change, deconfined spinons, non-product register changes, and loss of exact local symmetry. Their availability or failure is not established here. The N1–N8 no-go packet and its landing evidence have not been completed in this distillation; no packet PASS or audit status is claimed. The imported referee closures have not themselves been refereed.
