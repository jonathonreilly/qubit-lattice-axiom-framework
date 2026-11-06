# LZ1-i: one common speed for propagating light species

## 0. Status

**Pass 2; not refereed or frozen.** Subject to the imported results and proposed finite-band reading, Theorems 1–8 construct, for each even `m` in `L5-U[m]`, an admissible interacting update and a stationary, gauge-invariant, cell-invariant, half-filled state with two neutral propagating bands of different Clifford speeds. This refutes the unrestricted all-species assertion in that reading. It does not identify these bands as gauge bosons, fermions or gravitons, or select the VC1 vacuum.

**GAP: relative-budget comparison.** Draft Corollary C3 invokes `ZM1_OBS.md` Theorem 9′ without expressly requiring its common comparable-weight bounds on *both* fine and coarse branches. The corrected conditional statement is Theorem 10. No coarse comparison is constructed here.

**Open.** LZ1-i[O], LZ1-i[odd m], LZ1-i[cube], LZ1-i[VC1], LZ1-i[R-CS^str]; the rate and one-loop coefficient clauses of LZ1(a); ZM1-i; MT1-S[R-CS]; R-CS; GA1-P-5 as law data. See §7. No proposed specification is adopted.

**Provenance.** Pass 1: `LZ1I_DRAFT.md`, Claude Opus 5.5, max, SHA-256 `42ee0a77972ec5461c15406d34c018ee7296b4a54de1f2cd3e31f38791b2a73d`. Pass 2: Codex CLI `gpt-6.1-terra`, reasoning effort high, session `01a1b212-0ee4-71f3-9073-7ad4fb0dac06` (laptop account; from the run log). Source identities: `prior/LZ1I.md` `8a4abb6e628a6148`, `LZ1.md` `e5e18302fd535f6d`, `MT1.md` `c7be0ddbb9766747`, `GA1_5.md` `c53418ca516e84a2`, `ZM1_OBS.md` `8d1e40accea00ef0`, `LW1.md` `78280bd620800eac`, `TOE_ASSEMBLY.md` `6fda41c203ac95b5` (SHA-256 prefixes). The pass-1 scratch files in `/tmp/toe-lz1i` were unavailable in this session; their reported numerical check is not independent evidence.

## 1. Definitions inferred by the distiller

These are proposed precisifications, not adopted laws. Use the `L5-U[m]` base tick `U₀=W_E M_o M_e`, its cube generators and cell lifts as stated in `LW1_5.md` §2 and B1-U. Append finitely many locally finite, even-translation-invariant layers of commuting, finite-support, gauge-invariant gates, with finitely many gates per cell: the class of `LZ1.md` §1. Also require the proposed GA1-P-5 conditions in `GA1_5.md` §1 and implementability under NN-a (`TOE_ASSEMBLY.md` §3.6). Call such an update *admissible* here. Its base matter–link hopping gates remain present. GA1-P-5 is proposed law data, not an adopted unique law.

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

Let `R_C` be the one-flavour free cube generator of `MT1.md` §2, `R_T=Σ_{C∈T}R_C`, and `V_θ=e^{iθR_o}e^{−iθR_e}`. The two tilings are the even and odd cube tilings. For `θ∈(0,π/2)`, `MT1.md` Theorem 7 already proves its node at zero and Clifford slope `v=sin θ/√3`; `LW1.md` B10 already gives `1−cos w(K)=sin²θ(1−χ(K))`, `χ=(Σ_i cos K_i)/3`.

**Theorem 4 (covariant periodic frame).** There is a periodic diagonal unitary `Ψ` on `ℓ²(Z³)` such that `ĥ_C=Ψ*R_CΨ` obeys `π(g)ĥ_Cπ(g)⁻¹=ĥ_{gC}` for the ordinary site permutation representation `π` of `𝒢_Σ`.

*Proof.* `MT1.md` Theorem 1 gives cell-periodic monomial sign lifts `ρ(Q)` commuting with the even and odd generators. Since each generator is block diagonal on its tiling, the lift carries each cube block to the image cube block. The fourth power of the sign lift of `r` is a constant sign by uniqueness; rephase it by a fourth root of that sign. Together with even translations it is then an honest representation `ρ'` of `𝒢_Σ`. Write `ρ'(g)|x⟩=c_g(x)|gx⟩`. By the free action, define `ψ(gx_a)=c_g(x_a)` for orbit representatives `x_a=0,e₃`. The representation law gives `Ψπ(g)=ρ'(g)Ψ` for `Ψ=diag ψ`. Even translations act without phases, so `Ψ` is periodic. Conjugating cube covariance proves the assertion. □

Define `W_θ=Ψ*V_θΨ` and let `Ψ₀` be the diagonal fibre of `Ψ`. For a cube `C` in tiling `T`, let `s_e=−1`, `s_o=+1`. On `B_C=⊗_{x∈C}B` define `g_C` to fix the all-`0` vector, act by `exp(is_T θ_j ĥ_C)` on the one-`j` subspace for `j=1,2`, and act as identity on the remaining orthogonal complement. Embed it via the `ev_x` at the corners, with identity on the multiplicity and vertical factors; take zero outside the projection `Π_C^Σ` fixing the six end numbers at every corner. Call this embedded partial unitary `G_C^Σ`.

Choose coset representatives `g_k`, `k=1,…,6`, of `𝒢/𝒢_Σ`. Define `Π_C^{(k)}=α_{g_k}(Π_{g_k^{-1}C}^Σ)` and `G_C^{(k)}=α_{g_k}(G_{g_k^{-1}C}^Σ)`. Put
\[
G_C=\sum_{k=1}^6G_C^{(k)}+1-\sum_{k=1}^6Π_C^{(k)},\qquad L_T=\prod_{C∈T}G_C,\qquad U=L_oL_eU₀.
\]

**Theorem 5 (admissibility).** `G_C` is a local link-only gauge-invariant unitary; gates of each tiling commute and transform covariantly under `𝒢`. The two layers belong to GA1-P-5 and to the class of `LZ1.md` §1. Under NN-a they compile to finitely many disjoint edge-triple layers, so `U` is admissible.

*Proof.* Theorem 3 and the covariant frames show the embedding and the projections transform covariantly under the stabilizer; Theorem 4 supplies cube covariance of the one-particle matrices. Thus the coset definitions do not depend on representatives. Different `Π_C^{(k)}` are orthogonal by Theorem 3. Each partial unitary is unitary on its projection, and the last term is identity on the complement. Theorem 2 gives gauge invariance. The support is the finite set of links incident on cube corners. Distinct cubes of one tiling have disjoint corners. Their gates preserve end numbers and act on different end factors, hence commute even when a link is shared. The full cell group permutes the cosets and the cubes, giving covariance. These facts verify GA1-P-5 and the LZ1 layer conditions. For NN-a, the incident-link set is connected. `GA1_5.md` Lemma U and Proposition C, already proved there, compile each link unitary into edge-triple gates. Translate the finite word and split cube positions into eight residue classes modulo `4Z³`; compiled supports in each class are disjoint. The intermediate gates need not be gauge invariant: NN-a requires gauge invariance and covariance of the complete update. □

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

*Proof.* Cell covariance of the update and gauge actions makes each image stationary and gauge invariant. The group permutes the six images. At any site three are full and three empty. `E^x_{j0}` contains the `Σ` end-number projection, and thus annihilates the supports of the other five sector states. In the mixture, `√6 π̄(E^x_{j0})Ω̄` has exactly the inner products and evolution of `u_x^j`; apply Theorem 7. The sine maps `(0,π/2)` onto `(0,1)`, giving every positive ratio. `LZ1.md` Theorem 4.1 already proves D5 symmetries preserve directional and Clifford speeds, giving the last claim. □

The state is a six-sector mixture and does not establish VC1 or charge clustering. The created vectors lie in `π(𝒩)Ω`, since the `E^x_{j0}` are gauge invariant and conserve all end numbers. Thus the bands are not flux-carrying under proposed R-Φ. They need not be the physical species named in the intended LZ1 target.

**Theorem 9 (necessary restriction).** A universal common-Clifford-speed assertion over any class containing either constructed state and the constructed law with `θ₁≠θ₂` is false. Any true version must exclude these examples by restricting the layers, the state, or the species prescription.

*Proof.* Theorems 7–8 give two unequal speeds within either stated state. The mixture already has D1, gauge invariance, full cell invariance and half filling, and the bands meet LZ1-SC. □

**Theorem 10 (conditional zoom transfer; corrected C3).** Suppose a coarse comparison satisfies the absolute budget and all branch hypotheses of `ZM1_OBS.md` Theorem 9 for either constructed band, or its relative budget and all hypotheses of Theorem 9′, including comparable positive branch weights on both sides. Then the corresponding branch phases agree to `O(|K|^{p+1})` for `p>0`, and existing directional speeds agree. Applying this separately to both bands preserves their unequal speeds.

*Proof.* The local centered composites `E^s_{j0}` produce the orthonormal vectors of Theorem 7, so the equal-time correlation is `δ_{β0}1₈` and is summable. The two fine phases are `±w(K)`, each with nonzero projection weight, and their separation is `2v_j|K|+O(|K|²)` by B10. They satisfy the fine-side hypotheses. The stated coarse assumptions supply the remaining hypotheses; Theorems 9 or 9′ of `ZM1_OBS.md` give the matching and speed equality. □

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
- **Inherited:** the rate and one-loop coefficient clauses of LZ1(a), ZM1-i, MT1-S[R-CS], R-CS and GA1-P-5 as law data remain open. A2, the free continuation route, remains unclosed: `MT1.md` identifies the free link replacement as auxiliary. Kill attempt K in `LZ1.md` found no exactly solvable propagating sector; that was a failed search, not a no-go. This construction uses frozen matter and link multiplicities instead.

The digest `prior/LZ1I.md` also identifies prior structural dispersion, taste census, spatial power mixing, supplied matched free cones, Hall response and polarization obstacles, and gauge-register constructions. These are separate results with the assumptions and unaudited or author-side statuses stated there; none establishes a universal physical common speed. In particular the spatial power-mixing channel does not fix its coefficient (`docs/EMERGENT_LORENTZ_SPATIAL_BZ_POWER_MIXING_BOUNDARY_THEOREM_NOTE_2026-06-18.md`). ZM1-OBS transfers branch speeds only under its stated comparison hypotheses, and does not establish equality between species.

Pass 1 reported an `8³` torus floating-point check at angles 0.4 and 1.1: eigenphase errors below `3.5×10⁻¹⁵`, a sign-lift fourth power `−1`, and no nontrivial stabilizer of `0`. The script and output were unavailable for inspection in this session. The proofs above use the cited analytical results, not that check. The pass-1 literature search and its claimed limited novelty are recorded in `LZ1I_DRAFT.md` §7; they were not independently verified here.

Downstream, ST1's signature and MT1-S do not require equality of these two neutral speeds. GA2 and GR1/GR2 need whatever restricted common-speed input their claims actually use; GR2's two tensor modes need their speed tied to the assembly speed. The example does not itself establish or refute those physical modes. A zoom comparison of the form in Theorem 10 transfers the split; it does not establish that such a comparison exists, nor that the constructed state is the VC1 fine vacuum.
