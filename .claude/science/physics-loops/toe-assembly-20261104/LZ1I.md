# LZ1-i: one common speed for propagating light species

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (LZ1I_REFEREE.md); the referee's edits E1-E9 are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `LZ1.md` as its Amendment 3. It is the first item run through the prior-work gate (`prior/LZ1I.md`). The lead (Claude Opus 5.5, laptop) checked that each of E1-E9 is in the text and the replaced text is gone; that is a text check, not a second referee. Subject to the imported results and proposed finite-band reading, Theorems 1–8 construct, for each even `m` in `L5-U[m]`, an admissible interacting update and a stationary, gauge-invariant, cell-invariant, half-filled state with two neutral propagating bands of different Clifford speeds. This refutes the unrestricted all-species assertion in that reading. It does not identify these bands as gauge bosons, fermions or gravitons, or select the VC1 vacuum.

The pass-2 GAP on the relative budget is resolved. For these composites the relative and absolute budgets are equivalent, and Theorem 10′ needs no comparable-weight condition (`LZ1I_REFEREE.md` §4). Theorem 10′ also covers zooms, which fold the fine momenta.

**Open.** LZ1-i[O]; LZ1-i[odd m]; LZ1-i[cube]; LZ1-i[VC1]; LZ1-i[R-CS^str]; Inherited: the rate and one-loop coefficient clauses of LZ1(a), ZM1-i, MT1-S[R-CS], R-CS, GA1-P-5 as law data; LZ1-i[ZM1a]. See §7. No proposed specification is adopted.

**Imported referee closures, unrefereed.** RC-A, RC-B, RC-C, RC-Z and Theorem 10′ (referee closure, `LZ1I_REFEREE.md`).

**Provenance.** Pass 1: `LZ1I_DRAFT.md`, Claude Opus 5.5, max, SHA-256 `42ee0a77972ec5461c15406d34c018ee7296b4a54de1f2cd3e31f38791b2a73d`. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1b212-0ee4-71f3-9073-7ad4fb0dac06` (laptop account; from the run log). Source identities: `prior/LZ1I.md` `8a4abb6e628a6148`, `LZ1.md` `e5e18302fd535f6d`, `MT1.md` `c7be0ddbb9766747`, `GA1_5.md` `c53418ca516e84a2`, `ZM1_OBS.md` `8d1e40accea00ef0`, `LW1.md` `78280bd620800eac`, `TOE_ASSEMBLY.md` `6fda41c203ac95b5` (SHA-256 prefixes). The pass-1 scratch files in `/tmp/toe-lz1i` were unavailable in this session; their reported numerical check is not independent evidence.

**Editing-session provenance.** Codex gpt-6.1-terra, effort high, codex-cli 0.165.0.

## 1. Definitions inferred by the distiller

These are proposed precisifications, not adopted laws. Use the `L5-U[m]` base tick `U₀=W_E M_o M_e`, its cube generators and cell lifts as stated in `LW1_5.md` §2 and B1-U. Append finitely many locally finite, even-translation-invariant layers of commuting, finite-support, gauge-invariant gates, with finitely many gates per cell: the class of `LZ1.md` §1. Also require the proposed GA1-P-5 conditions in `GA1_5.md` §1 and implementability under NN-a (`TOE_ASSEMBLY.md` §3.7, line 235). Call such an update *admissible* here. Its base matter–link hopping gates remain present. GA1-P-5 is proposed law data, not an adopted unique law.

A D1 state is stationary, invariant under translations by `2Z³`, and invariant under the local centre actions. Use its GNS representation `(H,π,Ω)`, tick `Ũ`, translation implementers `T_β`, gauge-invariant physical space `H_phys`, and matter-parity spaces `H_even`, `H_odd` as in `LZ1.md` §1. A band `(d,F,V)` consists of an isometry `F:L²(T³;C^d)→H` and continuous `V:T³→U(d)` with `T_βF=F e^{iK·β}` and `ŨF=FM_V`. A node has `V(K₀)=1` and `V` is `C¹` nearby. Set `h=i log V` and `N_i=∂_i h(K₀)`. It propagates if some `N_i≠0`; it has a Clifford cone of speed `v>0` if `{N_i,N_j}=2v²δ_ij`. A proposed light species is a band with a node wholly in one parity space. Under the owner-selected LZ1-SC, the dispersion clause applies only to images in `ker(Ũ−1)^⊥`. This is the proposed R-loc band reading, not a complete physical species prescription; R-CS^str remains proposed and open.

Write `𝒢=2Z³⋊O_{c₀}`, `c₀=(1/2,1/2,1/2)`, with proper cubic rotations and the link lifts of B1-U. The end `(x,d)` is at site `x`, directed along `d∈{±e₁,±e₂,±e₃}`. A D5 symmetry is the unitary or antiunitary symmetry defined in `LZ1.md` §1. Proposed R-Φ calls a physical band flux-carrying if its image is orthogonal to `closure π(𝒩)Ω`, where `𝒩` is the local gauge-invariant end-number-conserving algebra (`GA1_5.md` §1).

## 2. Frozen sector and labels

Fix `m∈{2,4,6,8}`. Set `n_F=min(m,5)`, `n_E=m−n_F`. Define `Σ` by full matter at sites with even `x₃` (F-sites), empty matter at odd `x₃` (E-sites), `m/2` rishons at each end of every horizontal link, and `n_F,n_E` at the F- and E-ends of each vertical link. Finite-region projections onto these end numbers and matter occupations are denoted `P_R^Σ`.

**Theorem 1 (frozen matter and electric phase).** Every matter cube Hamiltonian annihilates `P_R^Σ` when `R` contains its support. On this sector each horizontal electric gate is `1`, and each vertical gate is `exp(−iτ_E(n_F−m/2)²)`.

*Proof.* In a horizontal link both matter sites are full or both are empty, so each hopping monomial vanishes. On a vertical link the E-to-F hop starts at empty matter. The F-to-E hop needs both an occupied E-end and an F-end hole. For `m≤4` the E-end is empty; for `m≥6` the F-end is full. Thus every cube hop vanishes. The electric claim follows from `n_F+n_E=m`; reversing the link changes the sign inside the square. □

Let `D_∥={±e₁,±e₂}`, `W=Λ^{m/2}C⁵`, and `B={b:D_∥→C:Σ_d b(d)=0}`, with the natural `S₄` action. Put `A_x=Hom_{S₄}(B,W^{⊗4})` and `ev_x(b⊗f)=f(b)`.

**Theorem 2 (gauge-invariant label operators).** Fixed end-number link sectors factor into their two end spaces, and hence `Σ` factors into site stars. The 3-dimensional `S₄` representation `B` is irreducible; `A_x` is nonzero; `ev_x` is an isometry with the gauge action confined to `A_x`. For `X∈End(B)`, its compression `X̂_x=ev_x(X⊗1)ev_x*`, extended by identity on vertical ends and zero outside the prescribed six end numbers, is local, link-only, gauge invariant and multiplicative in `X`. It is fixed by matter parity.

*Proof.* The fixed `(p,q)` link basis maps unitarily to `Λ^pC⁵⊗Λ^qC⁵`. End-number-preserving end operators act on their respective factors: the even bilinears generate the full matrix algebra on each exterior power and commute across ends. Local gauge transformations act on the matter and ends at their site. The four horizontal end spaces are `W^{⊗4}` and their factor permutations commute with the gauge action. For `B`, the character on the five `S₄` classes is `(3,1,−1,0,−1)` with class sizes `(1,6,3,8,6)`; its character norm is one. Schur's lemma makes `f*f'` scalar, defining the inner product on `A_x` and proving the isometry. To see `A_x≠0`, choose orthogonal `w₀,w₁∈W` and map `b` to the sum of four product vectors with `w₁` in position `d`, weighted by `b(d)`. Gauge transformations commute with permutations, so they act on `A_x` and preserve the evaluation image and complement. The compressed operators thus commute with all local gauge transformations. The isometry proves multiplicativity; their link-only support proves matter-parity invariance. □

**Theorem 3 (sector symmetries).** The stabilizer of `Σ` in `𝒢` is `𝒢_Σ=2Z³⋊⟨r⟩`, `r(x)=(1−x₂,x₁,x₃)`. It acts freely on sites, with F- and E-site orbits. Its six cosets give the three choices of vertical axis and two choices of full-plane parity. Any two of these six sectors have different prescribed end numbers at every site. Under the stabilizer, `α_g(X̂_x)=(Λ(Q_g)XΛ(Q_g)^{-1})̂_{gx}`, where `Λ` permutes the horizontal directions on `B`.

*Proof.* Preserving `Σ` requires `Qe₃=e₃`: other axes change a vertical end number to `m/2`, and `Qe₃=−e₃` exchanges full and empty planes. The remaining rotations are the four powers of `r`. Their images of `0` occupy the four horizontal residues modulo two, so no nontrivial power fixes a site modulo even translations; the same holds at `e₃`. This proves freeness and the two orbits. There are `24/4=6` cosets. Since `n_F≠m/2≠n_E` and `n_F≠n_E`, their end-number patterns differ as claimed. B1-U permutes the end modes. On fixed-number factors, fermionic reordering contributes only a scalar sign; it cancels in the adjoint action. Equivariance of `ev_x` gives the displayed transformation. □

Choose an orthonormal basis `|0⟩,|1⟩,|2⟩` of `B`. For the unique `g∈𝒢_Σ` carrying the relevant orbit representative `0` or `e₃` to `x`, set `|j⟩_x=Λ(Q_g)|j⟩` and `E^x_{jk}=(|j⟩_x⟨k|_x)̂_x`. These frames are even-translation periodic and `α_g(E^x_{jk})=E^{gx}_{jk}` for `g∈𝒢_Σ`.

## 3. Walk and admissible layers

Let `R_C` be the one-flavour free cube generator, the restriction of `R_T` to the cube `C` (`LW1.md` lines 59–65), `R_T=Σ_{C∈T}R_C`, and `V_θ=e^{iθR_o}e^{−iθR_e}`. The two tilings are the even and odd cube tilings. For `θ∈(0,π/2)`, `MT1.md` Theorem 7 already proves its node at zero and Clifford slope `v=sin θ/√3`; `LW1.md` B10 already gives `1−cos w(K)=sin²θ(1−χ(K))`, `χ=(Σ_i cos K_i)/3`.

**Theorem 4 (covariant periodic frame).** There is a periodic diagonal unitary `Ψ` on `ℓ²(Z³)` such that `ĥ_C=Ψ*R_CΨ` obeys `π(g)ĥ_Cπ(g)⁻¹=ĥ_{gC}` for the ordinary site permutation representation `π` of `𝒢_Σ`.

*Proof.* `MT1.md` Theorem 1 gives cell-periodic monomial sign lifts `ρ(Q)` commuting with the even and odd generators. Since each generator is block diagonal on its tiling, the lift carries each cube block to the image cube block. The fourth power of the sign lift of `r` is a constant sign by uniqueness; rephase it by a fourth root of that sign. Together with even translations it is then an honest representation `ρ'` of `𝒢_Σ`. Write `ρ'(g)|x⟩=c_g(x)|gx⟩`. By the free action, define `ψ(gx_a)=c_g(x_a)` for orbit representatives `x_a=0,e₃`. The representation law gives `Ψπ(g)=ρ'(g)Ψ` for `Ψ=diag ψ`. Even translations act without phases, so `Ψ` is periodic. Conjugating cube covariance proves the assertion. □

Define `W_θ=Ψ*V_θΨ` and let `Ψ₀` be the diagonal fibre of `Ψ`. For a cube `C` in tiling `T`, let `s_e=−1`, `s_o=+1`. On `B_C=⊗_{x∈C}B` define `g_C` to fix the all-`0` vector, act by `exp(is_T θ_j ĥ_C)` on the one-`j` subspace for `j=1,2`, and act as identity on the remaining orthogonal complement. The all-`0` vector and the one-`j` subspaces are taken in the frames `|j⟩_x` of §2, and `ĥ_C` acts on the corner index. Let `Π_C^Σ` fix the six end numbers at every corner. On `Ran Π_C^Σ` put `G_C^Σ=[(⊗_xev_x)(g_C⊗1)(⊗_xev_x)^*+1−(⊗_xev_x)(⊗_xev_x)^*]⊗1_vertical`, with `1` on the multiplicity factors; on its complement put `G_C^Σ=0`. Then `G_C^Σ` is unitary on `Ran Π_C^Σ`.

Choose coset representatives `g_k`, `k=1,…,6`, of `𝒢/𝒢_Σ`. Define `Π_C^{(k)}=α_{g_k}(Π_{g_k^{-1}C}^Σ)` and `G_C^{(k)}=α_{g_k}(G_{g_k^{-1}C}^Σ)`. Put
\[
G_C=\sum_{k=1}^6G_C^{(k)}+1-\sum_{k=1}^6Π_C^{(k)},\qquad L_T=\prod_{C∈T}G_C,\qquad U=L_oL_eU₀.
\]

**Theorem 5 (admissibility).** `G_C` is a local link-only gauge-invariant unitary; gates of each tiling commute and transform covariantly under `𝒢`. The two layers belong to GA1-P-5 and to the class of `LZ1.md` §1. Under NN-a they compile to finitely many disjoint edge-triple layers, so `U` is admissible.

*Proof.* Theorem 3 and the covariant frames show the embedding and the projections transform covariantly under the stabilizer; Theorem 4 supplies cube covariance of the one-particle matrices. Thus the coset definitions do not depend on representatives. This uses `α_{gh}=α_g∘α_h` on link operators: B1-U's link part is the second quantization of an end-mode bijection, second quantization is a homomorphism, and B1-U's site-sign freedom acts on matter only (referee closure RC-A, `LZ1I_REFEREE.md`). Different `Π_C^{(k)}` are orthogonal by Theorem 3. Each partial unitary is unitary on its projection, and the last term is identity on the complement. Theorem 2 gives gauge invariance. The support is the finite set of links incident on cube corners. Distinct cubes of one tiling have disjoint corners. Their gates preserve end numbers and act on different end factors, hence commute even when a link is shared. The full cell group permutes the cosets and the cubes, giving covariance. These facts verify GA1-P-5 and the LZ1 layer conditions. For NN-a, the incident-link set is connected. `GA1_5.md` Lemma U and Proposition C, already proved there, compile each link unitary into edge-triple gates. Translate the finite word and split cube positions into eight residue classes modulo `4Z³`; compiled supports in each class are disjoint. The intermediate gates need not be gauge invariant: NN-a requires gauge invariance and covariance of the complete update. □

**RC-A. Lifts compose exactly on link operators** (referee closure, `LZ1I_REFEREE.md`)

**Statement.** For `g,h∈𝒢` and every link-only local operator `X`, `α_g(α_h(X))=α_{gh}(X)`.

*Proof.* By B1-U (`LW1_5.md` line 268), `α_g` acts on the link algebra as conjugation by `Γ_g=⊗_ℓΓ(π_{g,ℓ})`. Here `π_{g,ℓ}` sends each rishon mode at the `z`-end of `ℓ` to the same flavour at the `gz`-end of `gℓ`, and `Γ(π)` is its second quantization on `Λ^mC^{10}`. The end-mode bijection of `gh` is `π_{g,hℓ}∘π_{h,ℓ}`: the `z`-end goes to the `hz`-end of `hℓ`, then to the `ghz`-end of `ghℓ`, with the flavour kept. Second quantization is functorial: `Γ(π′∘π)` and `Γ(π′)Γ(π)` both send `e_{i₁}∧⋯∧e_{i_k}` to `e_{π′π(i₁)}∧⋯∧e_{π′π(i_k)}`. So `Γ_{gh}=Γ_gΓ_h` on the link tensor product, and the conjugations compose exactly. B1-U's caveat, "The lifts may compose only up to site sign automorphisms", concerns the matter signs `d_g`. Link-only operators do not see them. □

*Use.* In Theorem 5, `α_{g_kh}(G^Σ_{h^{-1}C₁})=α_{g_k}(α_h(G^Σ_{h^{-1}C₁}))=α_{g_k}(G^Σ_{C₁})` for `h∈𝒢_Σ`, and `α_g(G^{(k)}_C)=α_{gg_k}(G^Σ_{g_k^{-1}C})` for `g∈𝒢`. The rest of the proof is as written.

## 4. State and bands

Define `ω_Σ` as the product state over site stars: matter is full at F-sites and empty at E-sites; each horizontal four-end factor has density `ev_x(|0⟩_x⟨0|_x⊗1_{A_x}/dim A_x)ev_x*`; each vertical end has normalized identity on its prescribed exterior-power space. Fixed-number link factorization makes these finite-region densities consistent.

**Theorem 6 (stationary state).** `ω_Σ` is a gauge-invariant D1 state, with matter occupation `5` on F-sites, `0` on E-sites, and cell-average `5/2`.

*Proof.* The full and empty matter lines are gauge invariant. Gauge action on horizontal labels is confined to `A_x`, where the density is normalized identity; vertical identities are invariant. Periodic frames give even-translation invariance. On the support of each finite-region density, every cube matter gate is identity by Theorem 1, each electric factor is scalar, and every appended gate fixes the all-`0` label state. For a local observable use the finite backward gate cone: its finite product sends the support projection to itself times a phase. Conjugation therefore preserves the density and the expectation. Local gauge invariance includes centre invariance. The filling follows from four F-sites and four E-sites per cell. □

**Theorem 7 (two exact bands).** For `j=1,2` define `u_x^j=π(E^x_{j0})Ω`. These vectors are orthonormal, belong to `H_phys∩H_even`, transform by `T_βu_x^j=u_{x+2β}^j`, and obey
\[
 \widetilde Uu_x^j=\sum_y(W_{θ_j}^*)_{yx}u_y^j.
\]
They define orthogonal bands `(8,F_j,V_j)` with `V_j(K)=Ψ₀*V_{θ_j}(−K)*Ψ₀`. Both band images lie in `ker(Ũ−1)^⊥`. Each has a node at zero and Clifford speed `v_j=sin θ_j/√3`.

*Proof.* Theorem 2 gives matrix-unit multiplication on the label image. Product-state expectations give `⟨u_x^j,u_y^k⟩=δ_xyδ_jk`. Gauge invariance of the operators puts the vectors in `H_phys`, and link-only support makes them even. The frame gives the translation law. On a finite support projection for `ω_Σ`, each `E^x_{j0}` creates precisely one label excitation. Matter gates remain identity there and electric gates have the same scalar as on the vacuum; each appended cube gate acts on the excitation position by its prescribed matrix. Taking the adjoint tick gives the displayed evolution. This is an equality of GNS vectors because the corresponding operator difference annihilates the support density.

For Fourier coefficients `f̂_s(b)` define `F_jf=Σ_{b,s}f̂_s(b)u^j_{2b+s}`. Orthonormality makes it an isometry; the translation law gives the band intertwining. The tick law gives the displayed fibre in this Fourier convention. By `MT1.md` Theorem 7, `V_θ(K)=exp(−ih(K))`, `h(K)=vΣ_iK_iG_i+O(|K|²)` near zero with Clifford `G_i`. Hence the band generators are `v_jΨ₀*G_iΨ₀`. The band image reduces `Ũ`. A fixed vector in it would have fibre support where `V_j(K)` has eigenvalue 1. The B10 identity makes this set only `K=0` on the torus, of measure zero. Therefore the image is orthogonal to all tick-fixed vectors. □

**Theorem 8 (cell-invariant mixture and free speed ratio).** Average the six spatial images of `ω_Σ` to obtain `ω̄`. It is a gauge-invariant D1 state, invariant under every cell lift and half filled at each site. Its GNS space has the two bands of Theorem 7. Their speed ratio ranges over `(0,∞)` as `θ₁,θ₂∈(0,π/2)` vary; for unequal speeds no D5 symmetry maps one band image onto the other.

*Proof.* Cell covariance of the update and gauge actions makes each image stationary and gauge invariant. The group permutes the six images. At any site three are full and three empty. `E^x_{j0}` contains the `Σ` end-number projection, and thus annihilates the supports of the other five sector states. The mixture bands follow from RC-B below. The sine maps `(0,π/2)` onto `(0,1)`, giving every positive ratio. The last claim follows from RC-C and Lemma M below. □

**RC-B. The two bands in the mixture `ω̄`** (referee closure, `LZ1I_REFEREE.md`)

**Statement.** Let `ω_l=ω_Σ∘α_{g_l}^{-1}` (`l=1,…,6`, `g₁=1`) and `ω̄=(1/6)Σ_lω_l`. Let `A` be local, let `V` be the finite product of the gates of `U` met by the backward cone of `A`, and let the finite region `R` contain the supports of those gates. Let `P^{(l)}_R` be the support projection of the density of `ω_l` on `R`.
- (a) `VP^{(l)}_R=c_lP^{(l)}_R` with `|c_l|=1`.
- (b) For `A=E^x_{j0}` and `l≠1`: `E^x_{j0}P^{(l)}_R=0` and `α(E^x_{j0})P^{(l)}_R=0`.
- (c) The vectors `ū^j_x=√6\,π̄(E^x_{j0})Ω̄` satisfy the orthonormality, translation law and tick law of Theorem 7. Hence Theorem 7's band construction gives, in the GNS space of `ω̄`, two bands with the fibres `V₁,V₂`, in `H̄_phys∩H̄_even∩ker(Ũ̄−1)^⊥`.

*Proof.* (a) `α_{g_l}` commutes with the tick automorphism. It maps each gate of `U` to a gate of the same layer: B1-U maps `H_C` to `H_{gC}` and the electric factor of `ℓ` to that of `gℓ` (`LW1_5.md` line 274), and Theorem 5 maps `G_C` to `G_{gC}`. So `α_{g_l}^{-1}(V)` is the ordered product of the gates met by the backward cone of `α_{g_l}^{-1}(A)`. Also `α_{g_l}^{-1}(P^{(l)}_R)` is the support projection of `ω_Σ` on `g_l^{-1}R`. Theorem 6's argument gives `α_{g_l}^{-1}(V)α_{g_l}^{-1}(P^{(l)}_R)=c_lα_{g_l}^{-1}(P^{(l)}_R)`. Apply `α_{g_l}`.
(b) `E^x_{j0}` contains the projection onto `Σ`'s numbers at the six ends at `x` (Theorem 2). `P^{(l)}_R` lies under the projection onto `Σ_l`'s numbers there. By Theorem 3 they differ at some end at `x`. So the two are spectral projections of commuting end numbers for different values, hence orthogonal, and `E^x_{j0}P^{(l)}_R=0`. Then `α(E^x_{j0})P^{(l)}_R=V^*E^x_{j0}VP^{(l)}_R=c_lV^*E^x_{j0}P^{(l)}_R=0`.
(c) For local `Z` supported in `R`, `6ω̄(Z)=Σ_lω_l(Z)`. The density of `ω_l` on `R` is supported in `Ran P^{(l)}_R`, so `ω_l(Z)=0` whenever `ZP^{(l)}_R=0`. By (b), for `l≠1` this holds for `Z=E^x_{0j}E^y_{j′0}` and for `Z=D^*D`, where `D=α(E^x_{j0})−Σ_y(W_{θ_j}^*)_{yx}E^y_{j0}`. So `⟨ū^j_x,ū^{j′}_y⟩=ω_Σ(E^x_{0j}E^y_{j′0})=δ_{jj′}δ_{xy}`, and `‖Ũ̄ū^j_x−Σ_y(W_{θ_j}^*)_{yx}ū^j_y‖²=ω_Σ(D^*D)=0` by Theorem 7. Translations: `α_{τ_β}(E^x_{j0})=E^{x+2β}_{j0}` and `ω̄` is translation invariant. `E^x_{j0}` is gauge invariant and link-only. The rest of Theorem 7's proof uses only these relations and B10. □

**RC-C. The band images lie in different D5 orbits** (referee closure, `LZ1I_REFEREE.md`)

**Lemma M (commutant of the multiplications)** (referee closure, `LZ1I_REFEREE.md`). Let `X` be bounded on `L²(T³;C^d)` with `XM_β=M_βX` for every `β∈Z³`. Then `X=M_u` for some `u∈L^∞(T³;M_d(C))`.

*Proof.* Let `X_{ab}` be the `(a,b)` component of `X`, an operator on `L²(T³)`. It commutes with multiplication by every trigonometric polynomial `q`. Put `x=X_{ab}1`. Then `X_{ab}q=qx`. For `f∈L²` take trigonometric polynomials `q_n→f` in `L²`. Then `X_{ab}q_n→X_{ab}f` in `L²`, and `q_nx→fx` in `L¹` by Cauchy–Schwarz. So `X_{ab}f=fx` almost everywhere. If `|x|>‖X‖` on a set `E` of positive measure, then `‖X_{ab}1_E‖=‖1_Ex‖>‖X‖‖1_E‖`, which is impossible. So `x∈L^∞` and `X_{ab}=M_x`. □

**Statement.** If `θ₁≠θ₂`, no D5 symmetry `S` satisfies `S(H₁)=H₂`, where `H_j` is the image of band `j` (in the GNS space of `ω_Σ` or of `ω̄`).

*Proof.* Suppose `S(H₁)=H₂`. By `LZ1.md` Theorem 4.1 (line 94), `S∘F₁`, composed with the coordinate change of its proof, is a band `(8,F′,V′)` with image `H₂`. Its fibre is `V′(K)=V₁(Q^{-1}K)` if `S` is unitary and `\overline{V₁(−Q^{-1}K)}` if `S` is antiunitary. Put `X=F₂^*F′`. Both isometries have range `H₂`, so `X` is unitary. Both satisfy `T_βF=FM_β`, so `X` commutes with every `M_β`. By Lemma M, `X=M_u`, and `u(K)` is unitary for almost every `K`. `H₂` reduces `Ũ`, so `Ũ^*F₂=F₂M_{V₂^*}` and `F₂^*Ũ=M_{V₂}F₂^*`. Hence `F₂^*ŨF′` equals both `M_uM_{V′}` and `M_{V₂}M_u`. So `V₂(K)=u(K)V′(K)u(K)^*` for almost every `K`. By continuity `V₂(K)` and `V′(K)` have the same eigenvalues for every `K`. By B10 every eigenvalue of `V_θ(K)` has real part `1−sin²θ(1−χ(K))`. Complex conjugation, `Ψ₀`, `K↦−K` and `K↦Q^{-1}K` keep this real part, since `χ` is even and invariant under signed permutations. So `sin²θ₂(1−χ(K))=sin²θ₁(1−χ(K))` for every `K`. At any `K` with `χ(K)<1` this gives `sin θ₁=sin θ₂`, so `θ₁=θ₂` on `(0,π/2)`. □

The state is a six-sector mixture and does not establish VC1 or charge clustering. The created vectors lie in `π(𝒩)Ω`, since the `E^x_{j0}` are gauge invariant and conserve all end numbers. Thus the bands are not flux-carrying under proposed R-Φ. They need not be the physical species named in the intended LZ1 target.

**Theorem 9 (necessary restriction).** A universal common-Clifford-speed assertion over any class containing either constructed state and the constructed law with `θ₁≠θ₂` is false. Any true version must exclude these examples by restricting the base law (the register parameter `m`, or the choice of `L5-U`), the appended layers, the state, or the species prescription.

*Proof.* Theorems 7–8 give two unequal speeds within either stated state. The mixture already has D1, gauge invariance, full cell invariance and half filling, and the bands meet LZ1-SC. □

**RC-Z. Theorem 9 with far branches, on a cone of directions** (referee closure, `LZ1I_REFEREE.md`)

**Setting.** As in `ZM1_OBS.md` line 90 and Theorem 9. For `i∈{0,1}`: a unitary `U_i`; unitary translations `T^{(i)}_β`, `β∈Z³`, commuting with `U_i`; vectors `v_{i,1},…,v_{i,d}` (the same `d` on both sides); `C_i(β,t)_{ab}=⟨v_{i,a},U_i^tT^{(i)}_βv_{i,b}⟩`; `c_i(θ,t)=Σ_βC_i(β,t)e^{−iθ·β}` where the sum converges absolutely; `ξ_i(f)=Σ_{a,β}f_a(β)T^{(i)}_βv_{i,a}`.

**Hypotheses.**
- (Z0) `p>0`, and `σ_i=Σ_β‖C_i(β,0)‖<∞` for `i=0,1`.
- (Z1) For every `t∈N₀` and all `f,g` with Fourier support in `B_{κ₀}`, `⟨ξ_i(f),U_i^tξ_i(g)⟩=(2π)^{-3}∫\hat f^*c_i(θ,t)\hat g\,dθ`, with `c_i(·,t)` continuous on `B_{κ₀}∖{0}`.
- (Z2) For `0<κ≤κ₀`, every `t∈N₀`, and all `f,g` with Fourier support in `B_κ`: `|⟨ξ₀(f),U₀^tξ₀(g)⟩−⟨ξ₁(f),U₁^tξ₁(g)⟩|≤C(κ^p+tκ^{p+1})‖f‖‖g‖`.
- (Z3) A closed set `Γ` of unit directions and `s₁>0` are given. For `θ=sθ̂`, `θ̂∈Γ`, `0<s<s₁`, and every `t`: `c_i(θ,t)=Σ_{k=1}^{n_i}W_{i,k}(θ)e^{−itλ_{i,k}(θ)}`, with `W_{i,k}(θ)≥0`, real continuous phases, and each `λ_{i,k}(sθ̂)` converging mod `2π` as `s→0`, uniformly in `θ̂∈Γ`. A branch is a *zero branch* if its limit is `0 mod 2π` and a *far branch* otherwise.
- (Z4) A branch `(i₀,k₀)` is *selected*: it is a zero branch, `‖W_{i₀,k₀}(θ)‖≥w>0`, and `|λ_{i₀,k₀}(θ)−λ_{i₀,k}(θ)|_{2π}≥g|θ|` for every other zero branch `k` of side `i₀`, for all `θ` in (Z3).

**Conclusion.** Put `S=max_in_iσ_i` and `K₀=8πCS/w²`. There is `s₂>0` such that, for every `θ=sθ̂` with `θ̂∈Γ` and `0<s<s₂`, some zero branch `k′` of side `1−i₀` satisfies `|λ_{1−i₀,k′}(θ)−λ_{i₀,k₀}(θ)|_{2π}≤K₀s^{p+1}`. Hence, on each ray of `Γ` along which `λ_{i₀,k₀}(sθ̂)=vs+o(s)`, some zero branch of side `1−i₀` equals `vs+o(s)` along a sequence `s→0`; if that branch has a directional derivative along the ray, it is `v`.

*Proof.* Step 1 (pointwise bound). Fix `θ₀=sθ̂` as above with `s` small. Lemma SP(4) (`ZM1_OBS.md` line 212) gives smooth normalized profiles concentrated in the `δ`-ball about `θ₀`, with unit vectors `u,u′`, whose forms tend to `⟨u,c_i(θ₀,t)u′⟩` as `δ→0`. Their Fourier support lies in `B_{s+δ}`. By (Z2), `|⟨u,(c₀−c₁)(θ₀,t)u′⟩|≤C((s+δ)^p+t(s+δ)^{p+1})`. Let `δ→0`: `‖c₀(θ₀,t)−c₁(θ₀,t)‖≤C(s^p+ts^{p+1})`.

Step 2 (weights). At `t=0`, `c_i(θ,0)=Σ_kW_{i,k}(θ)` with each `W_{i,k}≥0`. So `‖W_{i,k}(θ)‖≤‖c_i(θ,0)‖≤σ_i` and `Σ_k‖W_{i,k}(θ)‖≤S` (Lemma S0, `ZM1_OBS.md` line 276).

Step 3 (averaging). Put `λ=λ_{i₀,k₀}(θ₀)` and `γ_T(x)=T^{-1}Σ_{t=0}^{T−1}e^{itx}`. For `x≢0`, `|γ_T(x)|≤π/(T|x|_{2π})`, because `|Σ_{t<T}e^{itx}|=|\sin(Tx/2)/\sin(x/2)|` and `|\sin(x/2)|≥|x|/π` for `|x|≤π`. Put `A_i=Σ_kW_{i,k}(θ₀)γ_T(λ−λ_{i,k}(θ₀))`, the average of `e^{itλ}c_i(θ₀,t)` over `0≤t<T`. Step 1 gives `‖A₀−A₁‖≤C(s^p+Ts^{p+1})`.

Step 4 (far branches). Let `δ_F>0` be the least circular distance from `0` of the far limits on both sides. By (Z3) there is `s₃≤s₁` such that, for `s<s₃`, every zero phase lies within `δ_F/4` of `0` and every far phase at least `δ_F/2` from `0`. Then every far phase at `θ₀` lies at least `δ_F/4` from `λ`.

Step 5 (estimate). By Steps 2–4 and (Z4), `‖A_{i₀}‖≥w−S(π/(Tgs)+4π/(Tδ_F))`. Let `δ` be the circular distance from `λ` to the nearest phase of side `1−i₀` at `θ₀`. If `δ>0`, `‖A_{1−i₀}‖≤Sπ/(Tδ)`. Take `η=w/(4C)` and `T=⌈ηs^{−p−1}⌉`, so `CTs^{p+1}≤w/4+Cs^{p+1}`. Then
\[
w−S\Big(\frac{π}{Tgs}+\frac{4π}{Tδ_F}\Big)−\frac{Sπ}{Tδ}\le \frac w4+C(s^p+s^{p+1}).
\]
The terms `Sπ/(Tgs)≤(Sπ/(gη))s^p`, `4πS/(Tδ_F)≤(4πS/(ηδ_F))s^{p+1}` and `C(s^p+s^{p+1})` sum to at most `w/4` for small `s`. Then `Sπ/(Tδ)≥w/2`, so `δ≤2πS/(Tw)≤K₀s^{p+1}`. If `δ=0` the bound holds trivially.

Step 6 (the partner is a zero branch). Choose `s₂≤s₃` with the smallness of Step 5 and `K₀s₂^{p+1}<δ_F/4`. The phase of side `1−i₀` within `δ` of `λ` then lies within `δ_F/2` of `0`. So it is not far; it belongs to a zero branch `k′`.

Step 7 (rays). Fix `θ̂∈Γ` with `λ_{i₀,k₀}(sθ̂)=vs+o(s)`. Step 6 gives an index `k′(s)` for each `s<s₂`. There are finitely many indices, so one `k′` occurs along a sequence `s_n→0`. Lift the zero phases to real numbers near `0`. Then `λ_{1−i₀,k′}(s_nθ̂)=vs_n+o(s_n)`. If the directional derivative of `λ_{1−i₀,k′}` along `θ̂` exists, it is `v`. □

This is the proof of `ZM1_OBS.md` Theorem 9 (line 112) with one more leakage term (Step 4) and with the gap condition imposed only around the selected branch. Theorem 9 is the case in which every branch is a zero branch and every branch is selected.

**Theorem 10′ (zoom transfer)** (referee closure, `LZ1I_REFEREE.md`)

**Statement.** Fix `j∈{1,2}` and integers `M,L′≥1`. Take the fine data `U₀=Ũ^M`, `T^{(0)}_β=T_{L′β}` (translation by `L′` fine cells per coarse step) and the list `u^j_s`, `s∈{0,1}³`. Let a coarse system satisfy (Z0), (Z1) and (Z3) on a punctured neighbourhood of zero. Suppose the comparison meets the absolute budget (Z2), or the relative budget `C(κ^p+tκ^{p+1})N(f)N(g)`; for this fine list the two are equivalent (§4). Then there is a closed cone `Γ` of directions with nonempty interior such that, along every ray of `Γ`, the coarse system has zero branches within `K₀|θ|^{p+1}` of `+Mw_j(θ/L′)` and of `−Mw_j(θ/L′)`, where `Mw_j(θ/L′)=(Mv_j/L′)|θ|+O(|θ|³)`. Where their directional derivatives exist, they are `±(M/L′)v_j`. One may take `Γ=S²` unless `M≥3` and `θ_j` lies in a finite set `E_{M,L′}`. Applied to `j=1` and `j=2`, a coarse system that reproduces both bands carries the two coarse speeds `(M/L′)v₁` and `(M/L′)v₂`.

*Proof.* We check (Z0)–(Z4) on the fine side with `i₀=0` and the two branches `n=0` below selected. The coarse side meets (Z0), (Z1), (Z3) by assumption; the budget gives (Z2).

(a) *Summability.* `C₀(β,0)_{ss′}=⟨u^j_s,u^j_{2L′β+s′}⟩=δ_{ss′}δ_{β0}`, so `σ₀=1` and `c₀(θ,0)=1₈`.

(b) *Folding.* `F_j` maps the constant `e_s` to `u^j_s`, intertwines `T_{L′β}` with `M_{e^{iL′K·β}}` and `Ũ^{Mt}` with `M_{V_j^{Mt}}`. So `C₀(β,t)_{ss′}=(2π)^{-3}∫[V_j(K)^{Mt}]_{ss′}e^{iL′K·β}dK`. `V_j^{Mt}` is a trigonometric polynomial; write `[V_j^{Mt}]_{ss′}(K)=Σ_γa_γe^{iγ·K}`. Then `C₀(β,t)_{ss′}=a_{−L′β}`, a finite family in `β`, and `c₀(θ,t)_{ss′}=Σ_βa_{L′β}e^{iθ·β}`. Since `L′^{-3}Σ_{n∈\{0,…,L′−1\}³}e^{2πiγ·n/L′}` is `1` for `γ∈L′Z³` and `0` otherwise,
\[
c₀(θ,t)=L′^{-3}\sum_{n\in\{0,\dots,L′-1\}^3}V_j(K_n(θ))^{Mt},\qquad K_n(θ)=(θ+2πn)/L′ .
\]
This is (Z1) by `ZM1_OBS.md` Theorem 7, and it is continuous in `θ`.

(c) *Branches.* By B10, for `K∉2πZ³`, `V_j(K)` has the two eigenvalues `e^{±iw_j(K)}`, with `cos w_j=1−sin²θ_j(1−χ(K))` and `0<w_j(K)≤2θ_j<π`. Its spectral projections `P_±(K)` are continuous off `2πZ³`. For `0<|θ|<π` no `K_n(θ)` lies in `2πZ³`. So `c₀(θ,t)=Σ_{n,±}L′^{-3}P_±(K_n(θ))e^{±itMw_j(K_n(θ))}`. These are the branches `(n,±)`, with weights of norm `L′^{-3}` and phase limits `∓Mw_j(2πn/L′)`.

(d) *The selected branches.* Take `n=0`. Their weights have norm `w=L′^{-3}`. From `1−cos w_j=sin²θ_j(1−χ)` and `1−χ(K)=(2/3)Σ_isin²(K_i/2)`, `w_j(K)=v_j|K|+O(|K|³)`. So the two phases are `±(Mv_j/L′)|θ|+O(|θ|³)`. They are `2Mw_j(θ/L′)≥(Mv_j/L′)|θ|` apart for small `|θ|`.

(e) *Other zero branches.* A branch with `n≢0` is a zero branch only if `Mw_j(2πn/L′)∈2πZ`. If `M≤2` this never happens, because `0<Mw_j<2π`; then all such branches are far, and `Γ=S²` works. Let `M≥3` and `n≢0`. Then `χ(2πn/L′)<1`, and `θ_j↦w_j(2πn/L′)` is strictly increasing on `(0,π/2)`. So `Mw_j(2πn/L′)=2πk` has at most one solution for each `k∈\{1,…,⌊M/2⌋\}`. Thus `E_{M,L′}` has at most `(L′³−1)⌊M/2⌋` points. For `θ_j∈E_{M,L′}` a folded zero branch has phase `(M/L′)a_n·θ+O(|θ|²)`, `a_n=∇w_j(2πn/L′)`; `w_j` is smooth there because `0<w_j<π`. Its distance to a selected phase is `(M/L′)|θ|\,|a_n·θ̂∓v_j|+O(|θ|²)`. The directions with `a_n·θ̂=±v_j` form at most two circles or points on `S²`. Let `Γ` be the directions at angular distance at least `ε` from all of them, for a small `ε>0`. On `Γ`, by compactness, every selected branch keeps a gap of at least `c_ε|θ|` from every other zero branch for small `|θ|`.

So (Z0)–(Z4) hold, and RC-Z gives the statement. □

*Remarks.* For `M=L′=1`, Theorem 10′ gives Theorem 10's fine-to-coarse conclusion with fewer coarse hypotheses. If a coarse zero branch is also selected in the sense of (Z4), RC-Z with `i₀=1` matches it to a fine zero branch. The cone `Γ` is needed only for the finitely many angles in `E_{M,L′}`; for ZM1's first step `L=2` (so `M=2`) it is never needed. [check] at `M=L′=4`, `θ_j=π/3`, `K=(π,π/2,π/2)`: `4w_j=2π` to machine precision, so `E_{4,4}` is not empty.

## 5. Symmetry, attraction and gravity routes

**Theorem 11 (scale-dependent two-sector drag).** For continuous `a,b≥0`, if `v_F'=a(v_B−v_F)` and `v_B'=b(v_F−v_B)`, then
\[
 Δ(ℓ)=Δ(0)\exp\!\left[-\int_0^ℓ(a+b)\,ds\right],\qquad Δ=v_F−v_B.
\]
The difference tends to zero exactly when it starts at zero or the integral diverges.

*Proof.* Subtraction yields `Δ'=−(a+b)Δ`; the integrating factor gives the formula. A finite nonnegative integral leaves a positive exponential limit, and a divergent integral makes it zero. □

**Theorem 12 (marginal rate).** If `a+b=λκ₀/(1+Wκ₀ℓ)` with `λ,κ₀,W>0`, then `Δ(ℓ)=Δ(0)(1+Wκ₀ℓ)^{−λ/W}`. At `ℓ=log(1/(a_lat|k|))`, a nonzero difference is not `O((a_lat|k|)^p)` for any `p>0`.

*Proof.* Integrate the coefficient in Theorem 11. Every positive power of `1/(a_lat|k|)` grows faster than any power of its logarithm. □

**A1, symmetry.** A1.1 needs a time–space exchange symmetry and invariant Euclidean measure. These are not supplied for the live tick; D5 fixes the tick by definition. The conditional B4 result already appears in `docs/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`; the distinct two-surface conditions are in `docs/CROSS_SECTOR_FRONT_SPEED_B4_TWO_SURFACE_ALIGNMENT_BOUNDED_THEOREM_NOTE_2026-07-16.md`. The digest records those notes as unaudited. A1.2 needs all light species in one symmetry orbit. Theorem 8 supplies different orbits under the proposed band reading. This extends the free-copy witness already proved in `LZ1.md` Theorem 4.2; it does not derive a time-exchanging symmetry. The digest also identifies the #9913 analysis in `docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` on PR #10125 as author-side, not retained evidence.

**A3, RG attraction.** A3.1 needs a controlled zoom and matching to physical poles; ZM1-i remains open. A3.2 needs drag with divergent integral, not just positive drag at each finite scale. The constructed one-excitation bands are exactly decoupled in the tick; no interspecies alignment follows. The constant-positive-coefficient exchange result is already proved conditionally in `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`; Theorem 11 extends its algebra to scale-dependent coefficients. The parent `docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` is conditional support with an open gate. The disconnected neutral-sector exception and logarithmic modes already appear for the supplied model in `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md`. Theorem 12 makes the rate limitation explicit; A3.3 cannot infer the power rate in LZ1(a) from that marginal model. A3.4 also needs matching of finite cell-scale offsets; the draft reports #9913's supplied-law numerical one-loop calculation, not a proof for this law. The digest records the main notes as unaudited.

**A4, constraint closure.** The supplied-family common-cone coefficient result is already in `docs/CURVATURE_MEMBER_CLOSURE_WITH_MATTER_FORCES_ONE_COMMON_CONE_AND_THE_LORENTZIAN_SIGN_AND_HAS_AN_ORDER_A_SQUARED_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-10-18.md`. Its lapse-labelled constraint family and closure on every species are not supplied by the fixed-tick law. `docs/SOFT_SPIN2_COLLISION_INVARIANTS_COMMON_CONES_AND_LATTICE_WARD_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md` instead needs its stated pole, Ward and connected-scattering hypotheses; disconnected sectors are outside its conclusion. Both are unaudited in the digest. Neither proves the native gravity route here.

## 6. Proposed specifications and checks

The four tests are whether a proposal (1) fixes a target, (2) is open-ended, (3) settles downstream physics by premise, or (4) adds unnecessary structure or constants. The table records the draft's checks; none is adopted.

| Proposal | Test 1 | Test 2 | Test 3 | Test 4 | Effect |
|---|---|---|---|---|---|
| S-PL: only GA1-P-5's tiling-cube layer with its two angles | pass | pass | fail: it settles the magnetic-class question | pass | Excludes this construction; LZ1-i[cube] stays open. |
| S-CONN: each light species couples to the charged sector with divergent-integral drag | fail: states the desired mechanism | conditional: drag needs a controlled zoom | fail: decides neutral-sector coupling by premise | pass | Excludes the example by premise. |
| S-PHI: count only R-Φ flux-carrying and odd charged-sector bands | pass | pass | fail against the all-light-species target: removes neutral species by definition | pass | Excludes these bands. |

These are lane-specific checks. The independent R-Φ checks in `GA1_5.md` §1 are test 1 conditional, tests 2 and 3 pass, and test 4 conditional; they assess the proposed distinction itself, not its use to narrow T3.

## 7. Open items, prior work and limits

- **LZ1-i[O]:** `L5-O[S_+]`; its Majorana hop does not preserve matter number, so Theorem 1 does not transfer. GA1-5-O is open.
- **LZ1-i[odd m]:** this construction uses integer `m/2` at each horizontal end.
- **LZ1-i[cube]:** the base tick with at most the proposed tiling-cube layer.
- **LZ1-i[VC1]:** the selected interacting vacuum is not constructed. Any common-speed theorem there must use a property excluding `ω̄` beyond the properties in Theorem 8, or restrict the other premises.
- **LZ1-i[R-CS^str]:** the charged fermion prescription; the present bands are neutral.
- **LZ1-i[ZM1a]:** whether a class-(a) comparison (`ZM1_OBS.md` §5.1), chosen by the owner for ZM1-I1, keeps both speeds when applied to `ω_Σ` or `ω̄`.
- **Inherited:** the rate and one-loop coefficient clauses of LZ1(a), ZM1-i, MT1-S[R-CS], R-CS and GA1-P-5 as law data remain open. A2, the free continuation route, remains unclosed: `MT1.md` identifies the free link replacement as auxiliary. Kill attempt K in `LZ1.md` found no exactly solvable propagating sector; that was a failed search, not a no-go. This construction uses frozen matter and link multiplicities instead.

The digest `prior/LZ1I.md` also identifies prior structural dispersion, taste census, spatial power mixing, supplied matched free cones, Hall response and polarization obstacles, and gauge-register constructions. These are separate results with the assumptions and unaudited or author-side statuses stated there; none establishes a universal physical common speed. In particular the spatial power-mixing channel does not fix its coefficient (`docs/EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`). ZM1-OBS transfers branch speeds only under its stated comparison hypotheses, and does not establish equality between species.

Pass 1 reported an `8³` torus floating-point check at angles 0.4 and 1.1: eigenphase errors below `3.5×10⁻¹⁵`, a sign-lift fourth power `−1`, and no nontrivial stabilizer of `0`. The script and output were unavailable for inspection in this session. The proofs above use the cited analytical results, not that check. The pass-1 literature search and its claimed limited novelty are recorded in `LZ1I_DRAFT.md` §7; they were not independently verified here.

Downstream, ST1's signature and MT1-S do not require equality of these two neutral speeds. GA2 and GR1/GR2 need whatever restricted common-speed input their claims actually use; GR2's two tensor modes need their speed tied to the assembly speed. The example does not itself establish or refute those physical modes. A zoom comparison of the form in Theorem 10′ transfers the split; it does not establish that such a comparison exists, nor that the constructed state is the VC1 fine vacuum. The owner's ZM1-I1[a] (`TOE_ASSEMBLY.md` §3.8) is a class-(a) comparison of separated tails. Theorem 10′ concerns band-limited branch data. `ZM1_OBS.md` line 176 says class (a) 'does not by itself prove speed transfer'. So this file does not say what a class-(a) comparison does to the two speeds (LZ1-i[ZM1a]).
