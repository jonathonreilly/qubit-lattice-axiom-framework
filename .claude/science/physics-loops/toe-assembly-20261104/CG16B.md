# CG1-16-B. Spin(10) beyond site bilinears

## 0. Status

**Pass 2; not refereed or frozen.** In the explicitly defined class 𝓛 below, an exact local Spin(10) action with its `−1` acting as site fermion parity exists. In a D1 representation, its local centre pattern is conserved. The gauge-invariant physical subspace is orthogonal to all nontrivial centre-pattern vectors. With link-pure registers it is also matter-even. A band wholly in the nontrivial-pattern subspace is flat near a node. These are conditional statements about the definitions below; they do not exclude charged-sector particles or prove the CG1 target.

**GAP: NN compilation.** The proposed rishon cube tick is a finite-depth local circuit. The draft does not prove its decomposition into the nearest-neighbour edge-triple layers required by NN-a. The same qualification applies to alternative A. The witnesses establish existence in 𝓛, not existence of a nontrivial NN-a law. The identity update is an NN-a example with the same local action, but does not establish propagation. The draft's statement that its witnesses meet NN-a conflates exact gauge invariance with the separate gate-decomposition requirement.

**GAP: charged-sector identification.** Equality of relative parity and relative centre class is proved below for the finitely localized factor sectors of `RCS1.md` Theorem 3. The draft extends this without proof to every `χ_tot`-odd straight-string limit. Such a limit need not be a finitely localized factor sector; `χ_tot` is a proposed label over parity-sharp backgrounds, not an intrinsic grading of arbitrary representations of the observable algebra. The finite string has a spinor-class free end, but that alone does not establish the representation or charge of its infinite limit.

**Open by name.** RCS-P, including its version for an (F)-law; LW1-5-T, whole-tick frame symmetries; R-CG1, the reading of a physical 16; R-CS and MT1-S[R-CS^str] in the VC1 vacuum. CG1-i, CG1-ii, MT1-ii, MT1-S and VC1 remain open. The claimed inference that an (F)-law must be outside both live laws is established only gate by gate, outside the exceptional angles; LW1-5-T remains open. NN compilation and the charged-sector identification above are additional named gaps of this item. No law, reading or axiom is adopted.

**Provenance.** Pass 1: Claude Opus 5.5, maximum effort, `CG16B_DRAFT.md`, SHA-256 `3f46ee993ee3bfafb6ad64efa0c71d7081e7cf1fa7693380a119d17bfbb1ae9c`. Pass 2: Codex `gpt-6.1-terra`, effort and session id: see run log. Context: `prior/CG16B.md`, `TOE_ASSEMBLY.md` §§3.4–3.6, `LW1_5.md`, `RCS1.md`, `LZ1.md`, `LW1.md`. No independent referee or numerical proof is claimed. The draft's literature searches and their access limits are recorded in `CG16B_DRAFT.md` §2; this pass does not independently verify them. The digest records prior results, not an independent audit.

## 1. Definitions inferred by the distiller

1. Sites are `Z³`, each with five CAR modes, ten Majoranas `γ_a`, and parity `P=(-i)^5γ_1⋯γ_10`. The site Hilbert space is `H=H_+⊕H_-`, each summand of dimension 16. The site algebra is `End(H)`, graded by `Ad P`; distinct sites use the graded tensor product. Link factors commute with matter. `θ` is global matter parity on the quasi-local algebra.
2. Let `G=Spin(10)` be the group generated on `H` by `exp(i t M^{ab})`, `M^{ab}=iγ_aγ_b/2`. Its centre is `{±1,±ω}`, where `ω²=−1` and `ω=−iP` in this representation. The standard half-spin representation on `H_+` is `S_+` (`LW1_5.md` §4). A site representation is a continuous `u:G→U(H)` commuting with `P`, so `u=ρ_+⊕ρ_-`. Its frame action is `Ad u`. Define S′ by `u=S_+⊕1`; define **(F)** by `Ad u(−1)=Ad P`. The bilinear representation is `u(g)=g`.
3. A law belongs to **𝓛** when each nearest-neighbour link `ℓ=(x,y)` has a finite Hilbert space with commuting continuous unitary endpoint representations `ρ_{ℓ,x},ρ_{ℓ,y}` of `G`; the same site representation `u` is used at each site; and the local gauge action `Γ_x(g)` is conjugation by
   `Z_x(g)=u_x(g) ⊗ ∏_{ℓ∋x}ρ_{ℓ,x}(g)`.
   Its update `α` is a finite-depth local even automorphism as in `LW1.md` E1 and commutes with every `Γ_x(g)`. This class does not itself require NN-a's nearest-neighbour decomposition or cell covariance. End actions that entangle different links lie outside this definition. Site-dependent `u_x` can be treated by the same local arguments, with (F) imposed at each site.
4. Put `z_x=Z_x(−1)`. An operator is spinor class at `x` if `Ad z_x(A)=−A`, tensor class if it is fixed. A link is **link-pure** if `ρ_{ℓ,x}(−1)ρ_{ℓ,y}(−1)` is scalar; it is **end-pure** at `x` if `ρ_{ℓ,x}(−1)` is scalar. These definitions concern the central element `−1`; spinor class alone does not specify an irreducible 16.
5. For an even-translation covariant law with `τ_β(z_x)=z_{x+2β}`, a D1 state is stationary, invariant under `τ_β` and invariant under every `Ad z_x`. Its GNS triple is `(H_ω,π,Ω)`; the corresponding implementers fixing `Ω` are `Ũ,T_β,U_x`. Let `𝔄^G` be the fixed algebra of all local gauge actions and `H_phys=closure π(𝔄^G)Ω`. A vector is spinor class at `x` if `U_xv=−v`. Let `𝒮` be the closed span of all such vectors. When `ω` is parity-invariant, `H_odd` and `H_even` denote the parity eigenspaces.
6. A band `(d,F,V)`, node and leading generators `N_j=∂_j(i log V)(K₀)` mean `LZ1.md` §1: `F` is an isometry from `L²(T³;C^d)`, intertwines translations and tick with multiplication by `e^{iK·β}` and `V(K)`, and `V(K₀)=1` with `V` continuously differentiable nearby. Propagation means some `N_j≠0`.
7. The draft's precise **target (T)** asks for an (F)-law in 𝓛, a D1 state, and a band whose image lies in `H_phys∩H_odd∩𝒮`, with a node and some nonzero `N_j`. This is one formalization of the brief, not a definition of every possible physical or charged-sector reading.
8. The **diagonal identification** means `∏_{x∈Λ}Ad z_x(A)=θ(A)` for each local `A` and every finite `Λ` containing its matter sites and both ends of its supported links. It formalizes equality of the internal central action and the lattice spin-lift parity action on local operators; it does not construct a spacetime spin structure or a quotient group action.
9. For charged sectors use the factor representations, finite localization, relative class `χ`, background parity-sharpness, `χ_tot`, straight-string states and covariant band definitions of `RCS1.md` §§1, 3, 5 and R2. These are distinct from field-algebra vectors. R-CS^str is a working candidate, not adopted.

## 2. Site representations and conserved centre

**Theorem 2.1 (implementers).** `−1` is a commutator in `G`. For every law in 𝓛, the `z_x` are commuting self-adjoint unitaries and `α(z_x)=z_x`.

*Proof.* With `a=γ_1γ_2`, `b=γ_2γ_3`, both lie in `G` and `aba^{-1}b^{-1}=−1`. The `z_x` are involutions; distinct ones commute because site factors are even and endpoint actions commute. Covariance of `α` with `Γ_x(g)` makes `Z_x(g)^{-1}α(Z_x(g))` central in the quasi-local algebra. It is local, hence scalar. These scalars form a character of `G`, so they send the commutator `−1` to 1. □

**Theorem 2.2 (embedding E).** (a) (F) holds exactly when `u(−1)=εP`, `ε=±1`. (b) Under (F), every odd site operator is negated by `Ad u(−1)`, every even one fixed. (c) No such action is Bogoliubov. (d) S′ satisfies (F) with `ε=−1`; the bilinear action has `u(−1)=−1` and fails (F). (e) The two odd blocks transform as `ρ_+⊗ρ_-*` and `ρ_-⊗ρ_+*`; for S′ the first contains 16 copies of `S_+`.

*Proof.* (a) Equal inner automorphisms on `M_32` have implementers differing by a scalar; their squares make it `±1`. (b) follows from the grading. For (c), suppose a continuous induced `R:G→O(10)` acts on the Majoranas. Then `R(−1)=−I`. The kernel of `dR` is an ideal of simple `so(10)` and cannot be all of it; hence it is zero. The discrete normal kernel of `R` is central. It contains neither `−1` nor `±ω`, whose square is `−1`, and so is trivial. The 45-dimensional connected image is all of `SO(10)`, contradicting the centre orders four and two. For (d), `S_+(−1)=−1` and the other S′ block is trivial; the bilinear lift of `−1` is scalar `−1`. Finally `X∈Hom(H_-,H_+)` transforms as `ρ_+Xρ_-^{-1}`. □

**Corollary 2.3.** No (F) embedding is compatible gate by gate with an L5-O or L5-U cube generator, or with a cube gate outside the exceptional set of `LW1_5.md` M. The whole-tick question is LW1-5-T.

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

**GAP (NN compilation).** The preceding proof does not factor cube gates into the edge-triple layers of `TOE_ASSEMBLY.md` §3.7. Gauge invariance of each cube gate is not such a factorization. A zero-angle tick is an NN-a example, but gives no nontrivial motion. The rishon hop also has local `U(16)` on `H_+` and global `U(16)` on the `H_-` index; the latter is not shown to be local. Whether PS-6 requires every such global internal symmetry to be local is a reading question, not settled here.

## 4. Physical vectors, patterns and the target

**Theorem 4.1 (N).** Let a law in 𝓛 be even-translation covariant as in Definition 5, and let `ω` be D1.

(a) Every vector in `H_phys` is fixed by every `U_x`; hence `H_phys⊥𝒮`.

(b) If (F) and link-purity hold, every element of `𝔄^G` is matter-even, `ω` is parity-invariant, and `H_phys⊂H_even`.

(c) `H_ω` is the orthogonal sum of joint eigenspaces for finite-support sign patterns of the `U_x`. The tick preserves each pattern and translations shift it. The sum `H_nt` of nontrivial patterns contains `𝒮`. Every band with image in `H_nt` is identically 1 on a connected `C¹` neighbourhood of a node. Under (F) and link-purity, `H_odd⊂H_nt`.

Thus target (T) has no instance in 𝓛. Part (a) alone proves that exclusion.

*Proof.* (a) For `A∈𝔄^G`, `Γ_x(−1)(A)=A`, so `U_xπ(A)Ω=π(A)Ω`. The `−1` eigenspace is orthogonal to the fixed subspace; take closed spans.

(b) Local invariant elements are dense in `𝔄^G`: approximate by a local element and average over the finite product of compact site groups acting on its matter and link endpoints. The average is local and fixed, and does not increase the approximation error. Theorem 2.4 makes the product of the centre actions parity on a sufficiently large finite support. A local invariant element is therefore even; density extends this to `𝔄^G`. The D1 state is invariant under the same finite products, so it is parity-invariant, and fixed elements create even vectors.

(c) For local `A`, let `Λ` contain its matter sites and link ends. Character averaging over the commuting involutions `Ad z_x`, `x∈Λ`, decomposes `A` into joint eigenoperators; outside `Λ` they act trivially because site factors are even. Applying them to `Ω` and using cyclicity yields the finite-pattern decomposition. Theorem 2.1 makes the tick preserve the patterns; translations shift them. Every nonempty finite subset of `Z³` has trivial translation stabilizer. As in `LZ1.md` Theorem 2.1, choose one representative per orbit and Fourier transform to get `H_nt≅L²(T³;K)`, `T_β=M_β`, `Ũ=1⊗W` for a unitary `W` on separable `K`. The band intertwiner is a measurable fibre isometry, so eigenvalues of `V(K)` lie almost everywhere in the countable point spectrum of `W`. The `C¹` power traces are constant on a connected neighbourhood; Newton identities and `V(K₀)=1` give `V=1` there, as in `LZ1.md` Theorem 2.2. With (F) and link-purity, the product of the character signs of an odd local component is `−1`; density puts the odd subspace in `H_nt`. □

The pattern and flatness proofs extend the already proved `LZ1.md` Theorems 2.1–2.2. The evenness conclusion extends `RCS1.md` Theorem 4, itself credited there to `MT1.md`. These results do not exclude bands in other representations of `𝔄^G`.

**Theorem 4.2 (O; link-purity is needed).** There is an (F)-law in 𝓛 with a D1 state and a nonzero odd physical vector.

*Proof.* Use S′ and on each link set `H_ℓ=(C|0_x⟩⊕V_x)⊕(C|0_y⟩⊕V_y)`, with each `V≅S_+`; the `x` group acts only on `V_x`, the `y` group only on `V_y`. Put `Y=Σ_β |β_x⟩⟨0_x| E†_{x,βi}`. The fundamental and conjugate factors contract to a gauge invariant, nonzero odd operator. The endpoint centre product is `+1` on the two vacuum lines and `−1` on `V_x⊕V_y`, so the link is not link-pure. Choose the identity update and the unique tracial state; it is translation and gauge invariant, stationary and faithful. Then `π(Y)Ω` is nonzero, odd and physical. By Theorem 4.1(a) it is tensor class at every site. □

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
For finitely localized factor sectors relative to a factor background, the relative centre class `χ` of `RCS1.md` Theorem 3 equals its relative parity. If the background configuration is cell-periodic and `χ=−1`, no nonzero cell translation is implemented in that sector. The conditional transverse-flatness conclusion of `RCS1.md` Corollary 9 applies to covariantly chosen ray sectors when its disjointness and tick-equivalence hypotheses hold.

*Proof.* Centrality of `−1` and commuting opposite endpoint actions make each `z_x` gauge invariant; its adjoint action is itself a local gauge transformation, so it is central in the fixed algebra. Theorem 2.1 gives conservation. Multiplying site and link factors gives the displayed identity; each boundary factor is gauge invariant. For the relative parity identity, use the localization intertwiner on the boundary flux and divide the two factor-representation identities. The remaining scalar ratio is exactly `χ`. A nonempty finite configuration difference cannot be invariant under a nonzero translation; different central scalar values make the representations disjoint, as in `RCS1.md` Theorem 3. Corollary 9 is an abstract conditional representation argument and applies under its own hypotheses. □

**Theorem 6.2 (finite strings).** In the rishon witness, for a straight path `y_0=x,…,y_{2r}`, set `T_i=(r^{ℓ_i,y_{i-1}}_a r^{ℓ_i,y_i†}_b)_{ab}` and
`B_{r,b}=Σ_a E_{x,ai₀}(T_1⋯T_{2r})_{ab}`. It is matter-odd, invariant under gauge transformations except at the free end, and is spinor class there and tensor class at every other site.

*Proof.* At the initial and interior sites, fundamental and conjugate indices are contracted; unitarity cancels each local transformation. At the far end the uncontracted creator transforms in `S_+`, and its `−1` action supplies the minus sign. There is one odd matter factor. □

**GAP: limits.** A finite-string transformation law does not establish existence, nonzero normalization, factorhood, localization, or a spinor multiplet in an infinite-string limit. Nor does Theorem 6.1 identify `χ_tot` with `χ` for all such limits. RCS-P remains open, including on an (F)-law. On L5-O with uniform `S_+` ends, the lift of internal `−1` gives scalar `z_x=−1` (`LW1_5.md` Σ), so this `−1` label is trivial; the live-law odd label uses a different central element (`RCS1.md`).

**Theorem 6.3 (route comparison).** Under (F), the site factor of `z_x` is `εP_x`. Under S′, `ω` acts by `−i` on `Hom(H_-,H_+)` and by `+i` on the reverse block.

*Proof.* The first statement is Theorem 2.2(a). On `H_+`, `ω=−iP=−i`; on the trivial S′ block it is 1. Conjugation gives the stated phases. □

The site-count route #10038 and the literal-centre/spinon route #10045 have different hypotheses and are recorded in `prior/CG16B.md`; neither is closed by this comparison. The #10027 fixed-site bilinear centre theorem is already in the repository as cited by that digest. S′ drops its bilinear hypothesis. It supplies a spinor operator index but does not establish a physical family, chirality, charge identification, a mirror gap or a propagating sector.

## 7. Proposed readings and four tests

The four tests ask whether an item (1) fixes a target, (2) is closed rather than open-ended, (3) settles a downstream physics question by premise, and (4) adds unneeded structure. P, C and F below are pass-1 judgments, not independently established axioms. None is adopted.

| Item | 1 | 2 | 3 | 4 | Qualification |
|---|---|---|---|---|---|
| 𝓛 | P | P | P | P | Explicit product end actions and finite-depth updates; it does not exhaust PS-6 or enforce NN-a. |
| (F) as a studied hypothesis | P | P | P | P | The condition is supplied by the brief, not derived. |
| Centre classes, link/end purity, vector class | P | P | P | P | Definitions 4–5; a centre class does not alone mean a 16. |
| Target (T) | P | P | P | P | Field-GNS formalization only; it excludes charged-sector interpretations. |
| Diagonal identification | P | P | P | P | Equality of actions on local operators; not a constructed spin-structure quotient. |
| (F) as law data | F | P | F | C | Selects the odd operator class; an independent reason for the choice is not supplied. |
| Rishon witness as a law | F | P | F | C | Inherits (F); 16 rishon modes per end and extra symmetries are supplied. NN compilation is open. |
| Alternative A | P | P | C | F | Full-frame law is an unadopted alternative in `LW1_5.md`; its large group is extra structure. |
| **R-16^str, candidate** | P | C | P | P | Proposed reading: inspect the internal `−1` class of `χ_tot`-odd string sectors under R-CS^str. The finite-localized equality is proved; identification for general limits is a GAP. It decides neither existence nor motion. |
| PS-6-all, not proposed | P | P | C | P | Would require every internal symmetry of the update to be local; this bears on family symmetries and is not settled here. |

The candidate R-16^str is a request to specify where the charge is read. It is not a proof that any string limit is a 16 or that a band exists. The original pass-1 test judgments do not resolve the charged-sector gap.

## 8. Review boundary

The negative statement proved here is the explicit incompatibility in Theorem 4.1(a), not a no-go for every Spin(10) law or every physical charge prescription. The draft also records potential routes outside this domain: charged representations, site-count change, deconfined spinons, non-product register changes, and loss of exact local symmetry. Their availability or failure is not established here. The N1–N8 no-go packet and its landing evidence have not been completed in this distillation; no packet PASS or audit status is claimed. A fresh referee must check the final text and its dependencies before freezing.
