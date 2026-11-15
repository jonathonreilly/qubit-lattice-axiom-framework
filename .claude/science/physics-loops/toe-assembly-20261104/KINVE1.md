# KINVE1. One cell boundary

## 0. Status

**Pass 2; not refereed.** For the chain model and the proposed patches below, the construction proves a unital injective, label-preserving cell-to-block map, its gluing across two cells, and an exactly local map on the line. It includes endpoint gauge actions. It gives the multiplicities and matrix units below. The one-collar variant holds; removing the fine incident links makes the stated translation condition impossible. Tensor-product gluing across a cubic face fails by a rank count.

**GAP 1 — site-to-dimer obstruction.** Draft Proposition 4.9 permits a different map at every site, but its last paragraph uses the left and right permutations of the same site as if they were constrained by the same link. The link actually relates the right permutation at site X to the left permutation at X+1. The proof establishes the obstruction for a translation-identical family; it does not establish the stated arbitrary-family result. No counterexample to the latter is asserted.

**GAP 2 — full spatial stabilizer.** The construction proves covariance under the line reflection and its translated copies. The draft calls this the patch stabilizer, but a line patch embedded in three dimensions can have additional transverse rotations. Their lifted action on the constructed map is not checked here. Thus the full three-dimensional patch-stabilizer clause remains open; the proved statement uses the induced line reflection. The construction also does not settle the cubic patch.

**Open by name.** E1-CUBE: the two adjacent cubic cells at m=m₁=2, L=2, with incident links, all endpoint actions, dilated translations and patch-stabilizer covariance. E2 in three dimensions; K-INV-E; K-INV-O; K-ODD; D and D1; P-LOCK and ZM1-I1[INV] remain open or unchanged as in their sources. The line result does not supply the physical vacuum or correlation comparison. No law or reading is adopted.

**Provenance.** Codex pass 2, model `gpt-6.1-terra`; effort and session id: see run log. Draft SHA-256 `0e55d058d6c5a41ab9b93aa11c367ece00647cdd67a6afa1cb05f0dd856f1e44`; digest SHA-256 `6c3431662339eb18b8ef6a7efb641a79d1fa7ad5386787a346bae9ce6accc66c`. Draft scratch checks were not rerun and are not proofs. Source files are `KINVE1_DRAFT.md`, `prior/KINVE1.md`, `TOE_ASSEMBLY.md`, `ZM1_TREE.md`, `ZM1.md`, `KINV.md`, and `LW1.md`. The draft records a scratch job launched below its lane memory threshold; its outputs are not needed below.

## 1. Definitions inferred by the distiller

1. Work with the five-mode U(5) law L5-U[2] on both scales, R-form, and the invariant-only map class ZM1-INV. A line region contains specified matter factors and complete link factors along e₁. Its invariant algebra B(R) is the commutant of all gauge actions, including those at exterior link endpoints. This is a conditional mathematical setting, not a new axiom.
2. Coarse cells are `{2u,2u+1}`; fine blocks are `{4u,4u+1,4u+2,4u+3}`. R has coarse matter at 0–3 and links ℓ₋₁,…,ℓ₃. S has fine matter at 0–7 and links (−1,0),…,(7,8). Set R₀⁺=R∩(R−2) and S₀⁺=S∩(S−4). The reflection of a coarse cell is γ:X↦1−X, with fine counterpart γ̂:x↦3−x; on the two-cell patch they are X↦3−X and x↦7−x.
3. **Proposed reading (P).** A unital injective *-map B₁(R)→B₀(S) obeys φ(τ₂a)=τ₄φ(a) for all a∈B₁(R₀⁺), and intertwines the two patch reflections. P⁺ uses S enlarged by matter at −1,8 and links (−2,−1),(8,9). The draft's four tests for the line reading, P, and P⁺ respectively were P/P/P/P in each case. These are author checks, not owner adoption. P uses the full overlap domain and fine incident links. Theorem 10 tests the version without those links. The extra three-dimensional stabilizer issue is GAP 2.
4. A star has matter Fock space Λ•C⁵ and one Λ≤2C⁵ factor for each included link end. The diagonal U(5) acts by exterior powers. A complete link imposes end-number sum 2. Exterior stars have one slot and commutant C³. For an open-slot cell, include both three-slot stars and their internal link, but no exterior gauge action. Denote its invariant algebra by M; M′ is the corresponding four-star fine-block algebra. Eᵢⱼ and E′ᵢⱼ fix the left and right open-slot numbers i,j∈{0,1,2}. They are not generally central.
5. `T(a,b)=Λᵃ⊗Λ•⊗Λᵇ`, `D=Λ⁵`, `F=Λ⁵⊗Λ¹`, and `J_ab=1` if a+b=2, zero otherwise. For each U(5) irreducible ν let `C(ν)_ab=dim Hom(ν,T(a,b))`. The irreducible labels of a cell are pairs ν=(ν₀,ν₁), those of a block quadruples μ. Write `R(ν)=C(ν₀)JC(ν₁)` and `R′(μ)=C(μ₀)JC(μ₁)JC(μ₂)JC(μ₃)`; these matrices give the multiplicity-space dimensions at each open-slot label.

## 2. Region algebras and gluing

**Theorem 1 (star corner).** For a finite line region, write Sₓ for the commutant on the included slots at x, and P for the product of the link-number-sum-2 projections. Then `B(R)≅P(⊗ₓSₓ)P`. The line-region invariant algebra is the same whether the gauge actions are taken in the line model or restricted from the three-dimensional law.

*Proof.* Outside factors of a local gauge unitary commute with region operators: the matter factors are even and links are ordinary independent factors. A link Fock space is `Λ²(C⁵⊕C⁵)=⊕ₚ ΛᵖC⁵⊗Λ²⁻ᵖC⁵`. Choose contiguous Jordan–Wigner ordering of each end. Gauge generators are even and act on the corresponding star. The physical region is P times the product of star spaces. P commutes with the gauge group; extending an invariant operator by zero gives the corner of the product-group commutant, which is the tensor product of star commutants. □

**Theorem 2 (boundary pinning).** Any map satisfying P takes the shared coarse-link number projections to the shared fine-link projections by a permutation σ of {0,1,2}. Translation gives the same permutation on the left incident link; reflection gives σ(2−q)=2−σ(q), hence σ is the identity or swaps 0 and 2.

*Proof.* P forces the first cell algebra into B(S₀⁺), and its translate into B(S₀⁺+4). Their intersection contains only the shared fine link. The invariant algebra of one link is C³: its three end-number sectors are inequivalent irreducible representations of the two endpoint groups. A unital injection C³→C³ permutes its minimal projections. Translation identifies the two permutations; reflection exchanges the two ends of the link and sends q to 2−q. □

**Theorem 3 (gluing and multiplicities).** If `ψ:M→M′` is a unital *-homomorphism with `ψ(Eᵢⱼ)=E′ᵢⱼ`, its tensor product over cells, together with the identity on exterior C³ stars, restricts to a unital patch map satisfying the translation clause of P. It is injective if ψ is. A label-preserving ψ exists exactly when nonnegative integers `N_{μν}` satisfy `Σν N_{μν}R(ν)=R′(μ)` for each μ. It is injective exactly when every column is nonzero.

*Proof.* Group the star corner by cells. Every joining-link projection is `Σq [p_left=q]⊗[p_right=2−q]`. Label preservation carries it to its fine counterpart, so the tensor map restricts to the corners. Finite-dimensional tensor products preserve injectivity. On an incident-link cell algebra, exterior endpoint operators reduce to functions of the cell's open-slot numbers; the same map is used on each translated block, giving the translation relation. For the second statement, decompose `M=⊕ν End(Xν)` and `M′=⊕μ End(Yμ)`. A unital representation on Yμ is `⊕ν Xν⊗C^{N_{μν}}`. Equality of the ranks of each Eᵢⱼ is necessary and sufficient: a unitary on Yμ aligns the two orthogonal labelled decompositions. A source summand is killed exactly when its column vanishes. □

**Theorem 4 (reflection on blocks).** The line lifts γ and γ̂ are involutions, exchange Eᵢⱼ with Eⱼᵢ, and reverse the irreducible tuples. On a self-mirror full matrix block the induced automorphism is inner, implemented by a unitary whose square is scalar.

*Proof.* On the line all edge signs are η₁=1. The sign lift is constant along the line, so applying the reflection twice fixes matter and rishon generators. Geometric transport reverses the tuples and the open labels. Every full matrix algebra automorphism carries matrix units to matrix units, and the two systems are unitarily conjugate. Its square being the identity makes the square of its implementing unitary scalar. □

## 3. The cell map

**Theorem 5 (nine characters).** M has characters χᵢⱼ with `χᵢⱼ(Eₖₗ)=δᵢₖδⱼₗ` and `χᵢⱼ∘γ=χⱼᵢ`.

*Proof.* List occupation sets as `(left | matter | internal)` at star 0 and `(internal | matter | right)` at star 1, with `[5]={1,2,3,4,5}`:

| ij | star 0 | star 1 | weights at stars 0,1 |
|---|---|---|---|
| 00 | ∅ \| ∅ \| {1} | {1} \| ∅ \| ∅ | (1,0,0,0,0); same |
| 11 | {1} \| {1} \| {1} | {1} \| {1} \| {1} | (3,0,0,0,0); same |
| 22 | {1,2} \| [5] \| {1} | {1} \| [5] \| {1,2} | (3,2,1,1,1); same |
| 01 | ∅ \| ∅ \| ∅ | {1,2} \| {1} \| {1} | 0; (3,1,0,0,0) |
| 02 | ∅ \| ∅ \| ∅ | {1,2} \| [5] \| {1,2} | 0; (3,3,1,1,1) |
| 12 | {1} \| {1} \| {1} | {1} \| [5] \| {1,2} | (3,0,0,0,0); (3,2,1,1,1) |

Each displayed joint torus weight determines its occupation vector uniquely. For 00, the two internal-link particles exhaust the two site weights. For 11, three copies of flavour 1 fill all slots. For 22, flavour 1 fills all slots; the internal ends then contain only 1, and the remaining seven particles fill matter and the open end, with flavour 2 fixing the latter. For 01 and 02, the zero-weight star is empty, forcing two particles at the other internal end; the listed weight then forces the other slots. For 12, the first star is fixed as in 11 and the second as in 22. Every invariant operator preserves the resulting one-dimensional weight space and acts by a character. Reflect the three off-diagonal vectors for 10, 20, 21; the diagonal vectors are reflection symmetric. This weight-space mechanism is already proved in `GB1Z2L5.md` Theorem 2 and `ZM1INV.md` Theorem 2.1. □

**Theorem 6 (recoupling).** Set q₀=1 and q₁=q₂=2. There are equivariant isometries `aₖ:D→T(2−k,qₖ)` and `bₖ:F→T(2−qₖ,k)`, with matter degrees of aₖ equal to `3−qₖ+k` and of bₖ equal to 5,5,4. They define an isometry `V:Hcell⊗D⊗F→Hblock` by inserting aₖ and bₖ between the two original stars in the internal-link sector k. It intertwines U(5)⁴ with the original end-star actions and D,F on the two middle stars, and preserves open-slot labels. Its invariant corner is exactly `P_V M′ P_V=V(M⊗1)V*`.

*Proof.* For aₖ use the normalized adjoint of the nonzero equivariant wedge map from `Λ^{2−k}⊗Λ^{3−qₖ+k}⊗Λ^{qₖ}` to Λ⁵. For b₀,b₁ use the natural identifications with `Λ¹⊗Λ⁵` and `Λ⁵⊗Λ¹`. For b₂ use the normalized adjoint of `t:Λ⁴⊗Λ²→Λ⁵⊗Λ¹`, `t(ω⊗u∧v)=(ω∧u)⊗v−(ω∧v)⊗u`. It is nonzero and onto the irreducible F; `tt*` is scalar by Schur's lemma. The three fine link end-number pairs are `(k,2−k)`, `(qₖ,2−qₖ)`, `(k,2−k)`. Distinct k and open labels give orthogonal sectors, hence V is isometric. The group intertwining is factorwise. The corner is the commutant of U(5)⁴ on the range; D⊠F is irreducible for the middle product group, so that commutant is M⊗1. □

**Theorem 7 (explicit unital map).** Put `P_V=VV*`, `P_V^γ=γ̂(P_V)`, `P_K=1−P_V−P_V^γ`. Then
\[
ψ(x)=V(x⊗1)V^*+\hatγ\!\left(V(γ(x)⊗1)V^*\right)+\sum_{ij}χ_{ij}(x)E'_{ij}P_K
\]
is a unital injective *-homomorphism M→M′, preserves every Eᵢⱼ, and satisfies `ψγ=γ̂ψ`.

*Proof.* Equivariance puts the first corner and P_V in M′. On its range the fine star 1 has U(1) charge 5. On the reflected range it has charge 6, so the two range projections are orthogonal. Both commute with every E′ᵢⱼ because V preserves labels, as does P_K. Each of the three terms is a *-homomorphism on its own orthogonal corner; the last uses the nine characters and the mutually orthogonal E′ᵢⱼP_K. Their units sum to 1. Compression by V recovers x⊗1, proving injectivity. Applying the formula to Eₖₗ gives E′ₖₗ. Reflection exchanges the first two terms and, using χᵢⱼγ=χⱼᵢ, fixes the form of the third. □

**Theorem 8 (matrix units and symmetry).** Let νᵢⱼ be the one-dimensional source block of χᵢⱼ and define
\[
N_{\mu\nu}=[\mu=(\nu_0,D,F,\nu_1)]+[\mu=(\nu_0,F,D,\nu_1)]+\sum_{ij}[\nu=\nu_{ij}]r_{ij}(\mu),
\]
\[
r_{ij}(\mu)=R'(\mu)_{ij}-[(\mu_1,\mu_2)\in\{(D,F),(F,D)\}]R(\mu_0,\mu_3)_{ij}.
\]
These are nonnegative integers, satisfy the equations of Theorem 3 and have no zero column. Explicit matrix units are obtained by inserting the normalized multiplicity vectors of aₖ,bₖ into the two middle stars, adjoining the reflected insertion, and adding `E′ᵢⱼP_K` on the one-dimensional block νᵢⱼ.

*Proof.* In each fine isotypic multiplicity space the two recoupling ranges occupy precisely the indicated D,F and F,D blocks, each with labelled ranks R. Their orthogonal complement has rank rᵢⱼ in label ij, proving nonnegativity. It carries rᵢⱼ copies of χᵢⱼ. Thus the displayed N is the actual representation multiplicity, giving both rank identities and every column through the first term. Choose orthonormal labelled bases `x_s^ν` of each Xν and write `e^ν_st=|x_s^ν⟩⟨x_t^ν|`. The inserted and reflected isometries ι and ι′ give
\[
ψ(e^ν_{st})=f^{(ν_0,D,F,ν_1)}_{ιx_s,ιx_t}+f^{(ν_0,F,D,ν_1)}_{ι'x_s,ι'x_t}+\delta_{st}\sum_{ij}[ν=ν_{ij}]E'_{ij}P_K,
\]
where `f^μ_{v,w}=1_{Wμ}⊗|v⟩⟨w|`; the last term has s=t=1. The reflection lift unitaries themselves supply the symmetry intertwiners, and Theorem 7 proves their covariance. □

## 4. Patches, line, and failed variants

**Theorem 9 (chain patch and line).** The map of Theorem 7, glued by Theorem 3, proves P as defined above, with σ=id. It also proves P⁺. The compatible maps on all finite unions of cells extend to a unital injective, exactly local, cell-translation- and cell-reflection-covariant map of the quasi-local invariant algebras of the line.

*Proof.* Label preservation gives translation and the required joining corners; Theorem 7 gives cell reflection, and the two-cell reflection exchanges the two copies. Including S into S⁺ preserves the unit, gauge invariance and the equalities. For increasing unions of cells, the boundary number functions are carried to the same fine number functions before and after inclusion, so the maps are compatible. Injective C*-maps are isometric. Extend to the norm closure. Finite invariant density follows by support-preserving Haar averaging; it is already proved in `GB1Z2L5.md` Theorem 1, whose argument applies on the line. Locality is exact by construction. This proves line reflection, subject to GAP 2 for the full embedded spatial stabilizer. □

**Theorem 10 (incident links).** Remove (−1,0) and (7,8) from S. No unital injective patch map into the resulting algebra obeys the translation condition in P.

*Proof.* Translation forces the image of the first incident-link cell algebra into the intersection of the shortened fine patch and its translate by −4. That intersection has sites 0–3 and only their three internal links. Its translate by 4 is disjoint. The common coarse link algebra C³ must therefore map into the scalar intersection of these two disjoint fine algebras, contradicting injectivity. □

**Theorem 11 (forced labels).** Let two finite-dimensional algebras on each side carry nonzero three-projection partitions A_q,B_q and A′_s,B′_s. If unital maps θ,θ′ have nonzero images of all these projections and `Σq θ(A_q)⊗θ′(B_{2−q})=Σs A′_s⊗B′_{2−s}`, the images are the primed partitions up to a common permutation, with complementary indices on the second factor.

*Proof.* Slice the equality with vector states supported on each B′ projection. Each A′ is a sum of θ(A_q), because its coefficients lie in [0,1] and the sum is a projection. Slicing with states supported on θ′(B_q) gives the converse refinement. Two partitions into three nonzero projections that refine each other coincide up to permutation. Multiplication by one A′ factor gives the matching B′ projection. □

**Theorem 12 (site-to-dimer obstruction, corrected scope).** There is no translation-identical family of unital site-star-to-dimer maps whose tensor product sends every coarse joining-link projection to the corresponding fine joining-link projection and is injective on the line invariant algebra.

*Proof.* Theorem 11 forces left and right slot labels to be permuted by σ_L,σ_R, with `σ_L(2−q)=2−σ_R(q)`. Injectivity ensures the coarse slot projections have nonzero images. A single star character can only have equal left and right labels: the slot-swap unitary belongs to its commutant and exchanges two orthogonal unequal-label projections, which a character cannot both assign 1. The dimer characters χ₀₂ and χ₂₀ composed with the site map therefore force `c=σ_L⁻¹(0)=σ_R⁻¹(2)` and `d=σ_L⁻¹(2)=σ_R⁻¹(0)`. Compatibility gives c=1 and d=1, contradicting bijectivity. For site-dependent maps the compatibility relates different sites, so this proof does not establish the draft's wider claim; that is GAP 1. □

**Theorem 13 (cubic tensor-gluing obstruction).** For d≥2 and L≥2, no tensor product of two unital open-cell-to-open-block maps carries the entire coarse face-number constraint projection to the fine one.

*Proof.* If a tensor has a decomposition `Σ_{m=1}^r a_m⊗b_m` with both families linearly independent, every decomposition has at least r terms: dual functionals on the b_m show that all a_m belong to the span of the other decomposition's left factors. The coarse face projection is a sum of `3^{2^{d−1}}` elementary tensors. The fine face projection has a decomposition into `3^{(2L)^{d−1}}` elementary tensors with nonzero mutually orthogonal, hence linearly independent, slot-number projections on both sides. Every fine face assignment is attainable with interior links at (1,1). The latter count is larger. At d=3,L=2 the counts are 81 and 3¹⁶. This excludes only the specified tensor-gluing ansatz, not E1-CUBE or K-INV-E. □

## 5. Prior results and remaining interfaces

The recoupled corner extends the m=1 path mechanism already proved in `ZM1INV.md` Theorem 3.4; its register and global scope differ. The character term is per cell, not the single global filler excluded by `KINV.md` Theorem 5. The full-algebra charge-equivariant class J remains excluded by `KINV.md` Theorem 6; the present invariant-only map does not provide that extension. The locked-character condition is already `KINV.md` Theorem 3: the locked fine configuration lies in P_K with labels (1,1), where χ₁₁ assigns one to the balanced internal-link projection; the intercell links preserve their labels. The disjoint-support obstruction and its quantitative version are already in `ZM1INV.md` Theorems 3.5–3.6 and R6; the present exact images share block or link support. The zero-extension and global-filler failures do not rule out the present per-cell representation.

The digest identifies the free-chain even refinement in `docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` as an already proved, unaudited ungauged result, and the finite-group chain refinement in `ZM1I1A.md` RC-6 as a distinct pure-gauge analogue. Neither proves this construction. Boundary-sector preservation is already addressed in `docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`, an unaudited conditional approximation result. The Z₃ state-isometry face-total grouping in `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` is a proposed lead for E1-CUBE, not an algebra map. AF and perturbation programmes are unverified leads, not proof inputs. The draft's literature search and scratch checks establish no novelty or independent review.

For E1-CUBE, a putative translation-compatible map would need to represent the coarse face algebra C⁸¹ in the fine face algebra C^{3¹⁶}, grouping fine face labels into nonempty classes. Theorem 13 rules out only the particular tensor-corner gluing used on the line. E2 needs compatible overlapping embeddings; K-INV-E needs the three-dimensional quasi-local map. D and ZM1-I1[INV] additionally require the specified state and correlation comparison. Charged-sector consumers need a separate bridge. These are obligations, not consequences of the line construction.
