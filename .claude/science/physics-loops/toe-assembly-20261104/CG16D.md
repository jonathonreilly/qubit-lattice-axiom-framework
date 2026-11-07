# CG1-16-D. A deconfined spinor-class sector

## 0. Status

**Pass 2; not refereed or frozen.** The results below are conditional on the stated laws and definitions. They adopt no reading, law, specification or axiom. A fresh referee must check the complete dependency chain. The draft's scratch checks are unavailable here and are not independent verification.

**Proved, subject to the cited inputs.** The finite-region flux identity, the scalar flux on `L5-O[S_+]`, the support lemma and the static-label obstruction on link-pure registers; a string-sector example on a reducible register; the triviality of the pulled-back `−1` action on `L5-U`; and the non-link-pure register's invariant transfer, odd invariant operator, singlet construction and string defects. These statements use the proposed flux reading below. The flatness conclusion is directional at each node, not necessarily flatness on a neighbourhood.

**GAP.** The draft does not prove that the added six-link transfer layer has the nearest-neighbour gate decomposition required by NN-a. It is admissible in the broader appended-layer class of `LZ1.md`. Also, no physical identification shows that the proposed flux label exhausts every possible meaning of the CG1 16, especially on `L5-U`. The draft's conclusion for the target is conditional on that reading. The no-go-discipline N1–N8 landing packet has not been completed; this note is a distillation for review, not a landing or audit verdict.

**Open.** CG16D-NLP, CG16D-SC, RCS-P, R-CS, R-CG1, LW1-5-BG and GA1-P-5 remain open as stated in §7. No deconfinement, particle statistics, spatial spin or physical family is established.

**Provenance.** Pass 1: Claude Opus 5.5, `CG16D_DRAFT.md`. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model, effort and session id: see run log. Source revision identifiers are those recorded in the draft; no revision was fetched or verified in this session.

## 1. Definitions inferred by the distiller

These are proposed precisifications, not adopted physics. Use the quasi-local field algebra `𝔄`, its gauge-invariant subalgebra `𝔄^G`, and translations `τ_β` by `2β`, as in `RCS1.md` §§1, 4 and `LZ1.md` §1. Sites have five modes and six incident links.

1. **GR register.** A finite link Hilbert space has commuting unitary `Spin(10)` representations at its two ends, with generators `L^{cd}_{ℓ,x}`. Link factors commute with matter. The Gauss generator is `𝒢_x^{cd}=M_x^{cd}+Σ_{ℓ∋x}L^{cd}_{ℓ,x}`. An **so(20) register** comes from a representation of `Spin(20)` restricted to its two commuting `Spin(10)` end actions, as in `LW1_5.md` §4. `L5-O[S_+]` uses the half-spin register on every link.
2. Put `z_x=exp(2πi𝒢_x^{12})`, `ε_{ℓ,x}=exp(2πiL_{ℓ,x}^{12})` and `d_ℓ=ε_{ℓ,x}ε_{ℓ,y}`. A register is **link-pure** when `d_ℓ` is scalar. For a finite site set `Λ`, let `L_int(Λ)` be its internal links and `∂Λ` its crossing links. Define the **spinor flux** `Φ_Λ=∏_{ℓ∈∂Λ}ε_{ℓ,in(ℓ)}`. Each `ε` represents central `−1∈Spin(10)` and is a commuting self-adjoint involution. The flux lies in `𝔄^G`.
3. `𝒰` consists of translation-covariant tick automorphisms of the `LW1.md` E1 form that fix each local gauge generator. The appended gauge-invariant layers of `LZ1.md` §1 satisfy these properties. NN-a also requires a finite nearest-neighbour decomposition and full cell covariance; membership in `𝒰` alone does not establish those extra requirements.
4. A state `ω₀` of `𝔄^G` is **flux-sharp** when `s_Λ=ω₀(Φ_Λ)∈{±1}` for every finite `Λ`. Define `χ_sp(π:ω₀)=s∈{±1}` when `s_Λπ(Φ_Λ)→s I` strongly along **all** finite site sets ordered by inclusion. Call `s=−1` spinor class relative to `ω₀`. This is proposed by analogy with `χ_tot` in `RCS1.md` R2; it is not an adopted identification of a physical 16. The square of the `Spin(10)` centre generator `ω` is `−1`; on a spinor irreducible representation `ω` has value `±i`.
5. A D1 state is stationary, even-translation invariant and invariant under every centre adjoint action. A band, node and leading generators `N_j=∂_j(i log V)(K₀)` are as in `LZ1.md` §1 and `RCS1.md` definition 5. Propagation in this question means some `N_j≠0`. A string-made state is a weak-* limit of states obtained by operators supported on finite strings. No definition of finite string energy is supplied here.

**Proposed readings and checks, not adoptions.** The draft's absolute reading of centre eigenvalue `±i` has tests 1–4 `P,P,F,P`: it is already true in every `L5-O[S_+]` factor sector, including the background. The relative all-finite-sets flux reading has the draft's tests `P,P,P,P`; its physical identification is still open. Requiring all finite sets excludes, for example, an infinite line of flipped labels: centred cubes alone can have odd intersections. On `L5-U`, reading the ratio of `exp(iπQ_x/2)` as `±i` has tests `F,P,F,P`; that `U(1)` element is not central in `Spin(10)`. The draft rejects this reading. These are the draft's assessments, not independent owner decisions.

## 2. Flux identities

**Theorem 1 (relative-label invariance).** Quasi-equivalent representations have the same defined `χ_sp`. A direct sum of representations with the same defined value has that value.

*Proof.* The elements `s_ΛΦ_Λ` are uniformly bounded. The direct-sum result follows by convergence on finite-support vectors. Normal isomorphisms between the generated von Neumann algebras preserve bounded strong convergence; equivalently use the amplification argument of `RCS1.md` R2(a), already proved there for the same kind of net. □

**Theorem 2 (finite-region Gauss identity).** For GR registers,
\[
\prod_{x\in Λ}z_x=(-1)^{|Λ|}\left(\prod_{ℓ\in L_{int}(Λ)}d_ℓ\right)Φ_Λ.
\]
All factors commute and square to one. If every link is link-pure, `Φ_Λ=σ_Λ∏_{x∈Λ}z_x`, where `σ_Λ=(-1)^{|Λ|}∏_{int}d_ℓ∈{±1}`. It is then central in `𝔄^G` and fixed by every tick in `𝒰`.

*Proof.* The matter contribution to `z_x` is `exp(2πi(n_{x,1}−1/2))=−1`, so `z_x=−∏_{ℓ∋x}ε_{ℓ,x}`. Multiply over `Λ`: internal links supply both end factors, crossing links one. End actions commute. The `z_x` are central in `𝔄^G` and tick-fixed because they are functions of gauge generators; scalar `d_ℓ` gives the corollary. □

**Theorem 3 (so(20) registers).** For any `Spin(20)` register, `ε_{ℓ,x}=ε_{ℓ,y}=ρ_ℓ(−1_{Spin(20)})`, so `d_ℓ=1`.

*Proof.* In the Clifford realization a `2π` rotation in either end plane equals the same kernel element `−1` of `Spin(20)→SO(20)`. Apply `ρ_ℓ`. This is already proved in `LW1_5O_DRAFT.md`, Lemma K0(iii); the draft is not a frozen authority. □

**Theorem 4 (`L5-O[S_+]`).** Every `ε_{ℓ,x}=−1`, every `z_x=−1`, and every `Φ_Λ=1`. Every state is flux-sharp and every representation has `χ_sp=+1` relative to it. In every factor representation the local centre implementer has value `±i`; ratios between two factor values are `±1`.

*Proof.* The kernel element `−1` acts as `−1` on `S_+`. Theorem 2 gives `z_x=−(−1)^6=−1`. Since `6|Λ|=2|L_int(Λ)|+|∂Λ|`, the number of crossing links is even, so `Φ_Λ=1`. The relative-label statement follows. The factor statement follows from centrality and `c_x²=z_x=−1`, as already recorded in `RCS1.md` Theorem 1 and `LW1_5.md` Σ. □

Thus the flux-defined target sector does not exist on `S_+`, irrespective of string energy or dynamics. This does not decide a different identification of the CG1 representation.

## 3. Static labels on link-pure registers

Fix a flux-sharp background `ω₀`. Set `κ₀(x)=ω₀(z_x)∈{±1}`, `u_x=κ₀(x)z_x`, and `Z_Λ=∏_{x∈Λ}u_x=s_ΛΦ_Λ`. For a configuration `κ`, let `D(κ)={x:κ(x)≠κ₀(x)}` and let `H_κ` be the joint eigenspace of all `π(z_x)` with eigenvalues `κ(x)`.

**Theorem 5 (support).** On link-pure registers, `χ_sp(π:ω₀)=−1` exactly when `H` is the orthogonal direct sum of the `H_κ` with `D(κ)` finite and odd.

*Proof.* For the forward direction suppose `π(Z_Λ)→−I` strongly. For a unit vector `v` and `δ>0`, choose finite `Λ₀` so `‖(π(Z_Λ)+I)v‖<δ` whenever `Λ⊇Λ₀`. For finite `F` disjoint from `Λ₀`, and every `F'⊆F`, the identity `Z_{F'}=Z_{Λ₀∪F'}Z_{Λ₀}` gives `‖(I−π(Z_{F'}))v‖<2δ`. Averaging over `F'` shows that `E_F=∏_{x∈F}(I+π(u_x))/2` obeys `‖(I−E_F)v‖²<2δ`. The decreasing limit over finite `F` outside `Λ₀` projects onto vectors with background labels outside `Λ₀`. As `δ→0`, these projections span `H`. Split each such subspace into the joint eigenspaces on the finite set `Λ₀`. Thus only finite differences occur. An even difference gives eventual eigenvalue `+1`, hence its subspace vanishes. Conversely, on each finite odd difference `Z_Λ` is eventually `−I`; boundedness extends convergence from finite sums to all of `H`. □

**Theorem 6 (local creation and flat bands).** Under the same hypotheses:

(i) If a state of `𝔄` extends `ω₀`, any nonzero state produced from its GNS vector by a local or quasi-local `B∈𝔄` generates an `𝔄^G` representation with `χ_sp=+1`.

(ii) If `ω₀` is also even-translation invariant, every band in any separable covariant representation with `χ_sp=−1` satisfies `V(K₀+se_j)=I` for small `s` at every node and for each axis. Hence every `N_j=0`.

(iii) The same directional conclusion holds in a separable covariant representation spanned by joint centre eigenvectors whose configurations differ on a finite nonempty set from some cell-periodic configuration.

*Proof.* (i) For local `B`, choose `S` containing its matter support and both ends of each supported link. `∏_{x∈S}z_x=σ_SΦ_S` commutes with `B`, since the boundary links do not meet its support. Thus for every `Λ⊇S`, `Z_Λ` commutes with `B` and fixes the background vector. It also commutes with `𝔄^G`, so it fixes the cyclic subspace. Norm approximation extends this to quasi-local `B`, with strong convergence on the cyclic subspace. This recovers the pairing obstruction already in `LW1_5O_DRAFT.md` (K5) and extends the local static-label result of `LW1_5.md` Theorem SC to the stated sector representation.

(ii) Theorem 5 gives an orthogonal sum over finite odd defects. The tick preserves each configuration; translations shift it by `2β`. The least point `p` of each finite defect obeys `p(β·κ)=p(κ)+2β`. Apply `RCS1.md` Theorem 5 with `q_j=p_j/2`. (iii) A cell-periodic configuration equal to `κ` outside a finite set is unique: two distinct periodic configurations differ on infinitely many translated sites. Its nonempty defect has the same translation rule. Apply the same theorem. □

A full line of defects has no `χ_sp` limit along all finite sets; its transverse position still supplies conserved labels and gives transverse directional flatness by `RCS1.md` Theorem 5. It does not establish point-particle propagation along the line.

**Example 1 (string sector).** On `L5-O[S_+⊕C²⁰]`, choose a product field state with every link in a fixed `S_+` vector. Replace links along a finite ray segment by a fixed vector of `C²⁰`. The `z` labels flip at its two endpoints. The local product of rank-one link maps produces this state. Extend the segment to a half-ray: the restricted states converge weak-* to a state with one flipped label. In its `𝔄^G` GNS representation the central `Z_Λ` is eventually `−I`, so `χ_sp=−1`. The background is flux-sharp and cell-translation invariant. Theorem 6 rules out a nonzero leading generator in a covariant representation built from this sector; it says nothing about string energy. □

For any `Z4` boundary flux `Ψ_Λ=∏_{∂Λ}ρ_{ℓ,in}(ω)`, one has `Ψ_Λ²=Φ_Λ`. Therefore a gauge-invariant toric-code or `Z4` layer cannot move the spinor-class square on link-pure registers; changes of the remaining class-2 component are not ruled out. On `S_+` its square is `1`. This does not establish the existence of any such deconfined layer.

## 4. The `L5-U` action

**Theorem 7.** Let `p:Spin(10)→SO(10)` and let `G̃=p⁻¹(U(5))`. The `L5-U` gauge action pulled back to `G̃` sends `−1` to the identity. The two lifts `±ω` of `−I₅` both act as `c_x=exp(iπQ_x)`. Their relative factor-sector values are `±1`, never `±i`.

*Proof.* `p(−1)=I`, while `p(±ω)=−I₅`. The law uses an actual `U(5)` representation on matter and rishons, hence its pullback sends `−1` to `I`. The action of `−I₅` is matter parity times the six end parities, namely `exp(iπQ_x)`. It is central in `𝔄^G` and squares to `I` by `RCS1.md` Theorem 1. □

This rules out relative spinor class for this specified pulled-back gauge action, for every `L5-U[m]`. It does not rule out a projective charge of a different symmetry or an independent SM-family reading. RCS-P's odd-sector propagation remains open.

## 5. A non-link-pure counterexample to extending Theorem 6

Let `H=C³²` be the Dirac spin module of `Spin(10)`, `Q=C|0⟩⊕H`, and put `R_ℓ=Q^{ℓ,x}⊗Q^{ℓ,y}` with independent end actions. Let `ε` act as `+1` on `|0⟩` and `−1` on `H`. The register supports a `(10,10)` tensor operator: `U^{ab}=Γ_b⊗Γ_a` on `H⊗H` and zero otherwise, as in `LW1_5O_DRAFT.md` Proposition E(ii). It is not an so(20) register by Theorem 3.

**Theorem 8 (transfer and odd invariant).** On this register:

(i) `d_ℓ=+1` on `C⊗C` and `H⊗H`, and `−1` on `C⊗H` and `H⊗C`.

(ii) For two distinct ends at `y`, the operator `K_{12}=Σ_k|h_k⟩⟨0|⊗|0⟩⟨h_k|` is gauge invariant, commutes with every `z_x`, and anticommutes with each of `ε_{1,y},ε_{2,y},d_1,d_2`. Here `(h_k)` is any orthonormal basis of `H`.

(iii) `h_y=Σ_{ℓ≠ℓ'∋y}K_{ℓℓ'}` is Hermitian. The gates `exp(iθh_y)` have finite support, commute across sites, and form a translation- and rotation-covariant gauge-invariant appended layer. If one link is internal to `Λ` and the other crosses its boundary, `K_{12}Φ_Λ=−Φ_ΛK_{12}`. Thus `Φ_Λ` is not central in `𝔄^G`.

(iv) A nonzero gauge-invariant fermion-odd local operator exists.

*Proof.* (i) Multiply the end signs. (ii) `K` is the canonical identity tensor in `H⊗H*`; simultaneous end rotations leave it invariant. It transfers `H` from one end to the other and vanishes on the other summands, giving the anticommutations. Gauge invariance gives commutation with `z_x`. (iii) `K_{12}*=K_{21}`. Different sites use distinct end factors; rotations permute the ordered pairs. The crossing flux contains exactly one of the two flipped end signs. (iv) The vector occurs in the Dirac-spinor tensor square: construct an equivariant map `B:H⊗H→C¹⁰` using `β_a(s,t)=sᵀCΓ_at`, where `CΓ_aC⁻¹=Γ_aᵀ`. Clifford covariance makes `B` equivariant and nonzero. Put `w_a=B*e_a`, `X_a=|w_a⟩⟨0,0|` on two ends, and `O_y=Σ_aγ_{y,a}X_a`. Both `γ_a` and `X_a` transform as vectors, so their contraction is invariant. Linear independence of the `γ_a` makes it nonzero; it is matter-odd. This is outside the hypotheses of the matter-even theorem in `RCS1.md` Theorem 4. □

**GAP, NN-a compilation.** The site gate in Theorem 8(iii) touches six link registers. The draft gives no finite decomposition into NN-a's two-site, one-link gates. It is an allowed `LZ1.md` appended layer and preserves the defining properties of `𝒰`; no NN-a admissibility is asserted. The failure of the static-flux proof occurs precisely in Theorem 2: the internal product of `d_ℓ` is an operator, not a scalar.

**Theorem 9 (singlets and strings on the wider register).** At every site choose exactly one incident end in `H`, all others in `|0⟩`, and couple that end and the matter spin module to a local singlet. There are two singlets, one per matter parity. Their closed product span is gauge invariant, has `z_x=+1`, and is preserved by `h_y` and by the Majorana hops using the above `U`. The end choices are arrows; `d_ℓ=−1` exactly when one end of `ℓ` has an arrow. A columnar matching, with a fixed eigenvector of each paired-link hop and electric time `τ_E=0`, gives a pure locally gauge-invariant D1 state for the base tick. A half-column shift gives a weak-* string-limit state with a single unmatched link and `χ_sp=−1` relative to that state.

*Proof.* The spin modules decompose as `16⊕16̄`; `16⊗16̄` and its reverse each have one singlet, while equal chiralities have none. One spinor end gives `z_x=−(−1)=+1`. The transfer is the identity on the moved spinor and preserves the singlet; the hop vanishes unless both ends of its link are spinors, and otherwise preserves the two local singlet spaces by gauge invariance. On a columnar matching, occupied links are pairwise disjoint. The even-cube gate factors into commuting occupied-link gates; odd-cube hops vanish. A product of their eigenvectors is pure, stationary and invariant under even translations and local gauge transformations, hence D1. A finite shifted segment has two unmatched links; its local state is obtained by a local map from the matching state. A half-infinite shift leaves one unmatched link and is the local weak-* limit. For any finite `Λ` containing it and all the support of a fixed local observable, the relative flux is `−1` on the limiting vector and commutes with that observable, since the boundary lies outside its support. This proves strong convergence to `−I` on a dense GNS domain and hence `χ_sp=−1`. □

The transfer layer also breaks matchings. Neither an update that preserves the D1 state while giving the defect a nonzero band generator nor finite string energy is proved. The proposed D-reg specification has the draft's four-test result `F,P,P,F`: it is a closed register and does not itself decide a phase, but was chosen for the target and its independent end classes lack a working-set reason. It is recorded, not proposed for adoption. The wider family row c13 in `LW1_5O_DRAFT.md` records failures 1, 2 and 4; it does not by itself prove that this particular register fails test 2.

## 6. Prior work and checks

`prior/CG16D.md` identifies prior fixed-site obstructions and their limits. The fixed-site centre theorem and the analogous static centre-gauging example are already on file in `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`, rows #10027 and #10045, as cited in the digest; the former explicitly excludes infinite-volume superselection sectors. The #10038 moving-spinor example changes the site-count premise. `LW1_5.md` Theorem SC already proves static local centre-difference patterns; `RCS1.md` Theorems 1, 2 and 5 supply centre centrality, the parity/flux analogue and the directional-band lemma. `LZ1.md` Theorems 2.1–2.2 treat the finite-pattern vacuum-GNS case. None establishes deconfinement here. The digest's `ref/` paths are historical source locations and were not available as a verified source revision in this session.

Pass 1 reports literature searches and context from Gaiotto–Kapustin–Seiberg–Willett (one-form symmetries), Naaijkens and Kitaev (string sectors), Senthil–Fisher and Essin–Hermele (fractionalization), Barata–Nill (charged states), Huse et al. (dimer phases), and Wen (lattice chiral gauge theory). No theorem above relies on those citations. The Fredenhagen–Marcu source was not fetched in pass 1; the site content of Wen's construction was not verified. See `CG16D_DRAFT.md` Literature for search terms and exact scope.

Pass 1 reports a floating-point check of the transfer and equivariant vector map for `Spin(6)` and `Spin(10)`, with residual at most `7e-16`, and a direct odd-invariant check for `Spin(6)`. Its first SVD run exceeded the stated 1 GB limit; its second used a closed-form matrix. The reported `/tmp/toe-CG16D/scripts/check_cg16d.py` and `/tmp/toe-CG16D/out.txt` are absent in this session. These checks were not reproduced and are not proof or independent review.

## 7. Open items and downstream scope

- **CG16D-NLP:** On a non-link-pure law such as D-reg, find or exclude a stationary D1 state with a string-made `χ_sp=−1` sector that is deconfined and has a node with nonzero leading generator. Theorem 9 supplies a state and string defect, not the required dynamics or energy bound.
- **CG16D-SC:** Specify relative spinor class for backgrounds with neither sharp nor periodic centre labels. For example, the tracial state on `S_+⊕C²⁰` has independent link-class weights `512/532` and `20/532`; its centre labels are not sharp. Theorem 6(iii) does not cover a generic such configuration.
- **RCS-P, R-CS, R-CG1, LW1-5-BG, GA1-P-5:** unchanged and not solved here. In particular R-CG1 asks which 16 reading CG1 needs.

Under the proposed relative flux reading, Theorem 4 blocks the target on `L5-O[S_+]`; Theorem 7 blocks the pulled-back spinor class on `L5-U`. Theorem 6 blocks a nonzero leading generator on other link-pure registers relative to a translation-invariant flux-sharp background, and on the explicitly stated finite defects of periodic backgrounds. A merely flux-sharp nonperiodic background gives the support theorem, but does not by itself supply the covariant position label used in Theorem 6(ii). These results do not settle CG1's Standard Model alternative, MT1's physical particles, RCS-P, or the other escapes: changing site count and changing the `Spin(10)` action. The draft's proposed reading and register are not adopted.
