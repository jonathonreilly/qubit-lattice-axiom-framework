# MT1. Fermions, statistics and spin

## 0. Status

**Pass 2; not refereed or frozen. MT1 is open.** The statements below are conditional on the named laws and imported results. They do not establish a vacuum, a particle spectrum, or a physical identification of the emergent rotations.

**Proved in the stated algebraic setting.** The resolved hopping identity has sign −1. The finite-register laws have a local cluster presentation for the centre-even algebra. The free cell has a six-generator Clifford algebra. Its perpendicular face half-turn lifts anticommute. At the massless free node the leading generator has one isotropic Clifford cone. Under the proposed definition ER its internal rotation has spin 1/2. The cell rotations factor into spin and taste; each chirality is irreducible under the cell group. A symmetry-allowed linear perturbation splits the cone. The free node has 20 Weyl fields on each five-mode law, with the representations stated in Theorem 11.

**GAP.** The draft's closure of MT1-i does not follow from the cluster construction: it uses link-end modes, does not produce the specified BKSF embedding, and does not construct local excitations of the VC1 vacuum. R-X tests an operator identity, not the existence or exchange of physical particles. MT1-S alone gives spin 1/2 under ER, but does not identify ER with the physical long-distance rotation group. The draft's chirality label requires conjugation into the velocity basis; see Theorem 5. The quoted numerical checks and the interacting use of the free symmetry action remain unverified here.

**Open by name.** MT1-i; MT1-ii as a physical family claim; MT1-S; VC1; ZM1-i; LZ1-i; CH1-5U-i; CH1-5O-i; CH1-5O-E; LW1-5-T; GA1-P-5; the owner reading R-CG1 of the 16. The original MT1(a) requires a common law and VC1 vacuum. Neither is supplied by free-node counting. The named failed attacks and their limits are in §6.2.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af61-ef01-7f10-8b02-8ec5ec1c3569`. Pass 1: `MT1_DRAFT.md`, Claude Opus 5.5, max effort. Pass 2: Codex, model `gpt-6.1-terra`; reasoning effort and session ID not visible. Checkout HEAD `028f2093b4ec8a3747204757b680d67df970dc56`. SHA-256: draft `b7330e9ec79e8a1496a44a7ddde29ce2664536bd48238dba364b2bd676bdfc9d`; assembly `8027d9d44eb5fcaf02393e06dbd75f1f1adc9d9a6e2e8a5f46c279d5e63afcc0`; LW1 `78280bd620800eac671ddf6047d42e94c2ecf919d2f938909cc5595b168c09b9`; LW1_5 `7afb7ee2a52d91cd1cab23008c53373d710d0ce66252e1e5169ba8ca6009b20e`; CH1 `633e4aa4eed86d1e89e25a6d85dda4cca1bbb0ea9eb029a33568494bfa09b395`; CH1_5U `2254f04e4532651774ebf83c3bd744050a53519f667569d066592fe61ecd07cd`. Imported results carry their own hypotheses and status. The draft reports checks in `/tmp/toe-mt1/check/`; that directory is unavailable in this session. Its checks are not independent evidence here. Its literature search and citations are in its introduction; this distillation does not assert an independent literature check.

## 1. Definitions inferred by the distiller

**Setting.** PS-5 supplies five CAR modes per site. PS-6r supplies finite link registers. Both `L5-O[S_+]` and `L5-U[m]`, `1 ≤ m ≤ 9`, remain live under LW1-5-RQ. Use the definitions and centre actions in `LW1_5.md`. A free tick replaces link operators by c-numbers; it is auxiliary, not the interacting tick or vacuum. `L5-U` has free walk `V ⊗ 1_5`; `L5-O` has `(WVW*) ⊗ 1_5`, `W_x=i^{x_1+x_2+x_3}`. The latter shifts the cell node by `(π,π,π)` and changes the residue basis by a fixed unitary.

**Cell and lift.** Write `x=2b+r`, `r∈{0,1}³`, `η_j(r)=(-1)^{r_1+⋯+r_{j-1}}`, and `|K,r⟩=Σ_b e^{iK·b}|2b+r⟩`. Define

\[
 A_j=\sum_{r_j=0}\eta_j(r)(|r+e_j\rangle\langle r|+|r\rangle\langle r+e_j|),\quad
 Z_j|r\rangle=(-1)^{r_j}|r\rangle,\quad \Gamma_j=iZ_jA_j.
\]

`O` is the proper cubic rotation group about `(1/2,1/2,1/2)`. Write `Qe_j=s_j e_{π(j)}`. A lift is a site-permuting unitary with site phases, or site `U(5)` matrices in the flavour case, which commutes with both free half-step generators. A sign lift is denoted `ρ(Q)`. On finite Fock space `Γ_F(u)=⊕_n ∧^n u`, with `Γ_F(-1)=(-1)^N`; at infinite volume use its CAR automorphism. `θ` denotes matter parity, with links fixed.

**Proposed reading R-X.** Exchange sign means the sign in Levin–Wen's three-hop identity, applied to colour-resolved terms with the same central mode. Test results proposed in pass 1: discriminating, closed, downstream-neutral, and no added structure. The identity does discriminate bosonic from fermionic canonical hops, but this check does not establish particle exchange or an admissible physical excitation. R-X remains proposed.

**Spinor class.** For a projective cubic action, use the sign of the commutator of perpendicular face half-turn lifts: anticommuting is spinor class, commuting is linear class. The scalar commutator is ±1 because each half-turn has scalar square. The sign is phase independent. This label is proposed; its pass-1 four tests were reported as passing. It does not by itself identify continuum spin.

**Proposed ER.** For `h_1(q)=Σ_j q_j N_j`, Hermitian `N_j`, suppose `{N_i,N_j}=2v²δ_ij` for `v>0`. On Schwartz functions set `x_j=i∂/∂q_j`, `K_j=(x_jh_1+h_1x_j)/2`, and `J_k=(i/2v²)Σ_ij ε_kij[K_i,K_j]`. ER calls the group generated by `J` the emergent rotation group, and calls its internal irreducible summands spin `s` when their Casimir is `s(s+1)`. Outside the Clifford condition ER defines no group. Pass 1 reports all four tests as passing. The formula is closed and gives a checkable result; its identification with the physical long-distance rotation group is an additional open bridge, not a consequence of the formula.

**Proposed family readings.** M1 counts at least 16 two-component free Weyl fields per cell, converting right-handed fields to left-handed conjugates. M2 asks the free node to contain the `Spin(10)` 16 or `U(5)` family `10⊕5bar` (optionally a singlet). M3 asks for a fermion-odd one-site operator space carrying a family in CH1's inferred definition 7. Pass 1 reports all four tests as passing for each. They are distinct, unadopted readings; M1 alone does not test representations, chirality selection, or a vacuum.

## 2. Lifts and exchange algebra

**Theorem 1 (lifts).** Each `Q∈O` has a cell-periodic sign lift. It is unique up to a constant phase. A lift with five flavours has the form `ρ(Q)⊗w`, `w∈U(5)`. Its fibre matrix `ρ̂(Q)` obeys `ρ̂(Q)R_T(K)ρ̂(Q)*=R_T(QK)`.

*Proof.* LW1 A2 supplies a sign lift. Comparing a signed edge and its image fixes the product of its endpoint signs. Two lifts differ by a diagonal matrix constant on each nearest-neighbour edge, hence constant on the connected lattice; the matrix-valued case gives one constant unitary. Edge-sign ratios are periodic under `2b` translations. The product of those ratios along two consecutive edges in one direction is 1, since the sign of such an edge is independent of its coordinate in that direction, as is the sign on its rotated image. Thus the lift is cell-periodic. The fibre formula follows from `g_Q(2b+r)=2Qb+g_Q(r)`. □

**Theorem 2 (resolved hopping identity).** Let `j,k,l` be distinct neighbours of `i`. Link operators `X` on their three distinct links commute with each other and with matter. For U define `t_il=c†_{i,e}X_il c_{l,b}`, `t_ki=c†_{k,c}X_ki c_{i,e}`, `t_ij=c†_{i,e}X_ij c_{j,f}`. For O use the analogous `(i/2)γ X γ` terms with the same central Majorana label. Then
\[
 t_{il}t_{ki}t_{ij}=-t_{ij}t_{ki}t_{il}.
\]
The identity holds on every state and for every choice of the link operators.

*Proof.* The link factors agree. For U, use `c_i c†_i=1-n_i`, `c†_i n_i=0`, and commute the even `n_i` past the other sites. The two matter factors differ by reversal of three mutually anticommuting operators at `j,k,l`, giving `(-1)^3`. For O use `γ_i²=1` and the same reversal. □

**GAP (draft §2.1).** A Majorana bilinear need not move a conserved particle, and arbitrary resolved components need not preserve the physical sector separately. The identity is exactly the claimed algebraic result, but the inference that *every excitation moved by the laws* has a physical exchange statistic needs a particle and exchange construction. The draft's nonzero U example is a reported numerical check, not reproduced here.

**Theorem 3 (finite cluster presentation).** On a finite box or even torus, group the five matter modes at each site with five auxiliary link-end modes for each incident link: 35 complex modes per site. For U use its rishons and impose `p_{ℓ,x}+p_{ℓ,y}=m`. For O embed `S_+` in the Fock space of ten complex link modes and impose link chirality `+1`. The law's Hilbert space is unitarily equivalent to the constrained subspace of the ordinary tensor product of the cluster Fock spaces. Site values, end numbers, end chiralities and Gauss generators are cluster-local; each hop is a sum of products of operators at its two endpoint clusters. The centre element at a site is its cluster parity up to a scalar. Centre-even local operators are local on the clusters they touch, provided they are operators of the constrained law algebra.

*Proof.* First apply Klein strings in an order of species to turn the matter CAR and the mutually commuting link species into one graded CAR algebra. The law's hopping terms contain an even number of modes in each original species, so their strings cancel. In the graded algebra each U term groups as `(c†_y r_y)(r†_x c_x)` and each O term as `i(γ_yη_y)(η_xγ_x)`; each factor is cluster-even. The Gauss generators and the stated local values are cluster-even functions of cluster modes. Order all modes cluster by cluster and apply Jordan–Wigner: cluster-even products have no intercluster strings. The number or chirality constraints pick precisely the original link register. The U centre multiplies all matter and incident rishon modes at the site by −1. For O, the centre is the site parity times the product of end parities, up to a scalar, by the centre identities in LW1_5. Thus centre-even local monomials have even degree at each cluster and map locally. Electric gates are local at one end, and gauge-invariant plaquette operators are covered if they preserve the link constraints. □

**GAP (draft Corollary 2.3).** This presentation uses 30 link-end modes in addition to the five site modes. It gives a local encoding of the centre-even algebra, not a local representation of individual odd matter operators. D1 changes PS-5's site content; it does not by itself prove the BKSF-and-role-pattern input in MT1(e), or remove the VC1 requirement. Thus MT1-i remains open under the literal target. The same construction applies to `L_cube` at `S=1/2` through the stated one-mode U equivalence; it is not claimed for other registers. The structural comparison in pass 1 credits Bravyi–Kitaev, Zohar–Cirac, and Brower–Chandrasekharan–Wiese; these citations are not used as proofs.

## 3. Clifford cell and lattice rotations

**Theorem 4 (cell algebra).** The six matrices `A_j, Γ_j` are Hermitian involutions and anticommute pairwise. Their 64 ordered monomials form an orthogonal basis of `M_8(C)`. With the convention above,
\[
 R_e(K)=\frac{\sum_j A_j}{\sqrt3},\qquad
 R_o(K)=\frac1{\sqrt3}\sum_j(\cos K_j A_j-\sin K_j\Gamma_j).
\]
Moreover `ρ̂(Q)A_jρ̂(Q)*=A_{π(j)}` and `ρ̂(Q)Γ_jρ̂(Q)*=s_jΓ_{π(j)}`.

*Proof.* Each `A_j` is a signed matching. Different matchings anticommute because each face has flux −1. `Z_j` anticommutes with `A_j` and commutes with the other matchings, giving the six Clifford relations. Every nonidentity Clifford monomial anticommutes with some generator, so has zero trace. Distinct monomials are orthogonal and the 64 span `M_8(C)`. The odd edge across the cell boundary contributes `e^{-iK_j}` from the upper to the lower residue; this gives the displayed fibre. Differentiate its covariance from Theorem 1 once and twice in `K_j` to obtain the two rotation rules. □

**Theorem 5 (half-turns and parity).** For perpendicular face half-turns `h_1,h_2`, their one-body lifts anticommute. For five flavours this remains true for lifts forming a projective action with scalar squares. Their Fock lifts satisfy `Γ_F(u_1)Γ_F(u_2)=(-1)^NΓ_F(u_2)Γ_F(u_1)`. For the specific dressed lifts of LW1, LW1_5 A2-5/B1-5 and B1-U, the corresponding automorphisms obey `α_1α_2=θ α_2α_1`.

*Proof.* Theorem 4 and irreducibility force `ρ̂(h_1)=λ_1Γ_2Γ_3`, `ρ̂(h_2)=λ_2Γ_3Γ_1`. They anticommute. For flavour twists `w_1,w_2`, a scalar commutator `λ` for the full lifts gives `det(-λ I_5)=1`; scalar squares give `λ²=1`, hence `λ=-1`. Second quantization is a homomorphism and sends `-1` to parity. For the cited dressed lifts, the commutator has this matter action; the geometric permutations of link ends commute as automorphisms. □

The draft also gives perpendicular edge-axis anticommutation: its two Clifford representatives differ by exchanging two anticommuting vectors through five factors. For sign lifts, a face quarter-turn has fourth power −1. A number-phase redefinition can change that fourth power, but not the perpendicular-half-turn commutator.

**Theorem 6 (centre and matter parity).** For a local operator supported on matter sites and links whose endpoints lie in a finite set `Λ`, matter parity `θ` equals conjugation by the product of local centre elements over `Λ`, on `L_cube`, U, and O[S_+]. Gauge-invariant local operators are `θ`-even. On a finite torus the product of all centres equals `(-1)^N` times a fixed register scalar: respectively `1`, `(-1)^{m #links}`, and `(-1)^{#links}`.

*Proof.* The site factors implement matter parity. The two endpoint actions on each complete link multiply to the identity on the link algebra: their product is 1 for `L_cube`, `(-1)^m` for U, and −1 on `S_+` for O. A gauge-invariant local operator is fixed by every centre. The finite-torus identity follows by multiplying the same factors. □

The spinor label applies to odd matter sectors with the stated lifts. Gauge-invariant local observables are even; a physical charged state and its boundary dressing still need specification.

## 4. Free node and emergent spin

**Theorem 7 (free node).** At `μ=0`, near `K=0`, `V(K)=exp(-ih(K))` with
\[
 h(K)=v\sum_jK_jG_j+O(|K|^2),\quad v=\sin\varepsilon/\sqrt3,\quad
 G_j=U\Gamma_jU^*,\quad U=e^{i\varepsilon R_e/2}.
\]
The `G_j` are Clifford generators, so the leading eigenvalues are `±v|K|`, each fourfold. The only `V=I` node is `K=0`. At `μ>0`, `V(0)=e^{iμR_e}` and `R_e` anticommutes with every `Γ_j`.

*Proof.* `R_o(0)=R_e=R` and `R_o(K)-R=-ΣK_jΓ_j/√3+O(K²)`. Duhamel's formula and `{R,Γ_j}=0` give `i dV(0)=vΣK_j e^{iεR}Γ_j=vΣK_jUΓ_jU*`. The analytic logarithm near the identity gives the expansion. The Clifford square gives the spectrum and equal multiplicities. LW1 B10 gives `1-cos w=sin²ε(1-χ(K))`, whose equality case is `K=0`. The massive identity follows directly from the two half-steps. □

**Correction (draft §§3.4, 4.2).** Set `χ=-iΓ_1Γ_2Γ_3`. It generally does **not** commute with `G_j`: `χ` anticommutes with `R_e`, so `UχU*` differs from `χ` for generic `ε`. The Weyl chirality of the leading generator is `χ_G=-iG_1G_2G_3=UχU*`. The draft's counting is correct after this conjugation. The `χ` eigenspaces used below are rotation-invariant and are carried to the corresponding `χ_G` eigenspaces by `U`.

**Theorem 8 (spin times taste).** Put `S_k=-(i/4)Σ_ab ε_kab Γ_aΓ_b` and `S^A_k=-(i/4)Σ_ab ε_kab A_aA_b`. Each triple is spin 1/2, the triples commute, and `S` commutes with `R_e`. On each four-dimensional `χ=±1` space, they act on `C²_spin⊗C²_taste`. For each cell rotation, `ρ̂(Q)=S(Q̃)T(Q)`, where `Q̃∈SU(2)` lifts `Q`, `T` commutes with every `Γ_j`, and `T A_j T*=A_{π(j)}`. Face half-turns have scalar `T`. A three-cycle has taste rotation by `±2π/3` about `(1,1,1)`; a transposition has taste rotation by `π` about `(e_j-e_k)/√2`, up to chirality-dependent phases. Taste is irreducible on each chirality, and so is the full four-dimensional projective cell representation.

*Proof.* Clifford relations give both `su(2)` commutators, Casimir `3/4`, and mutual commutation. The chirality `χ` commutes with the `Γ` and both bivector triples and anticommutes with each `A`; its eigenspaces have dimension four. Decompose each under spin; its two-dimensional multiplicity carries the taste spin 1/2 by the commuting Casimir. The spin lift and `ρ̂(Q)` have the same action on the `Γ` matrices, so their quotient fixes them and permutes the `A` matrices. For a 3-cycle the induced taste adjoint is the stated 3-fold rotation. For a transposition it is the stated half-turn; multiplication by `χ` implements the missing overall sign on the `A`'s and becomes a scalar within each chirality. The two noncommuting taste rotations have no common invariant line. The face half-turns generate the spin matrix algebra, so any operator commuting with all cell rotations is scalar on spin and then scalar on taste. □

The per-chirality character moduli on identity, 3-fold, face half-turn, quarter-turn, edge half-turn classes are `4,1,0,0,0`; they agree in modulus with restricted spin 3/2. This does not identify the physical continuum spin. The pass-1 comparisons credit Golterman and Catterall–Pradhan–Samlodia for spin–taste factorizations.

**Theorem 9 (ER boost algebra and free spin).** Under ER, put `L_k=Σ_ab ε_kab x_aq_b` and `S^N_k=-(i/4v²)Σ_ab ε_kab N_aN_b`. Then
\[
 [K_i,K_j]=-iv²\sum_k ε_{ijk}(L_k+S^N_k),\qquad J_k=L_k+S^N_k,
\]
`[J_k,h_1]=0`, and every internal irreducible summand has spin 1/2. The free massless node of all three laws satisfies ER. Its internal generator is `S`, with five flavours where applicable. At `μ>0`, the rest eigenspaces of `R_e` each carry spin 1/2 with multiplicity two per flavour.

*Proof.* Let `D_i=[x_i,h_1]=iN_i`. Since `K_i=x_i h_1-D_i/2`, expansion gives `-[x_i{D_j,h_1}-x_j{D_i,h_1}]/2+[D_i,D_j]/4`. Insert `{D_j,h_1}=2iv²q_j` and the Clifford relations. The bivectors obey `su(2)` with Casimir `3/4`; orbital and spin commutators with `h_1` cancel. For the free walk use Theorem 7 and the fact that `U` commutes with `S`. For nonzero mass, `R_e` commutes with `S` and its two eigenspaces have equal dimension. □

**Corollary 9.1.** At the free node, the spin factors of the cell rotations are restrictions of ER's internal SU(2) action. The conjugated taste factors `UT(Q)U*` commute with every `G_j`. A lattice rotation is a phase times a pure spin rotation exactly for the identity and the three face half-turns. The taste action on one chirality has no continuous homomorphism `SU(2)→U(2)` extending it up to phases.

*Proof.* The first two assertions follow from Theorems 8–9. A pure spin rotation fixes all `A_j`; Theorem 4 forces `π=id`, giving exactly the four diagonal proper rotations. For the last assertion, a face half-turn has scalar taste. All trace-zero elements of SU(2) are conjugate, and every SU(2) element is a product of two trace-zero elements. An extension with one scalar trace-zero image is therefore trivial, contrary to the irreducible non-scalar taste action. □

A different diagonal combination of spin with an internal taste SU(2) can assign other spins. ER selects the boost-generated choice, which commutes with the internal commutant. This is a mathematical choice; physical uniqueness remains open.

## 5. A symmetry-allowed cone splitting

**Theorem 10 (counterexample to symmetry forcing one cone).** Let `Z^G_j=UZ_jU*` and `h_u(K)=vΣ_jK_j(G_j+uZ^G_j)`. It transforms covariantly under the proper cell rotations and inversion, and obeys the free walk's antiunitary condition `D_r overline{h_u(-K)} D_r=-h_u(K)`, `D_r=Z_1Z_2Z_3`. For all sufficiently small nonzero `u`, it is not one isotropic Clifford cone. It is the leading term of a finite-range cell-periodic operator.

*Proof.* Inversion has sign lift `±A_1A_2A_3`: it fixes all `A` and negates all `Γ`. From `Z_j=-iΓ_jA_j`, Theorem 4 gives the vector transformation of `Z`; inversion negates it. `D_r` fixes `Z` and sends `overline{Γ_j}` to `Γ_j`; it also fixes `U` under antiunitary conjugation. Thus both triples have the stated covariance. Conjugate by `U*`. Along `e_3`, `(Γ_3+uZ_3)²=1+u²`. Along `(1,1,1)/√3`, the squared velocity is `1+(2u/3)Y+O(u²)`, where `Y=iΣ_{i<j}Γ_iΓ_j(A_i-A_j)`. Its six Clifford monomials are distinct and orthogonal, so `Y` is nonzero, Hermitian and traceless. It has eigenvalues of both signs, hence some diagonal speed changes at first order while the axial speed does not. Finally `Σ_j Z_j(T_{-2e_j}-T_{2e_j})/(2i)` has fibre `Σ_j sin K_j Z_j`; conjugation by the cell-local `U` preserves finite range. □

At `μ=0`, `σ=V_e^{-1}τ` is a free symmetry, where `τ` is LW1 A2's signed diagonal translation: `τVτ^{-1}=V_eV_o`, so `σVσ^{-1}=V`. The same argument gives `σ=M_e^{-1}τ` for the dressed base tick when `τ_E=0`; no plaquette layer is asserted. Pass 1 reports that its finite-matrix check finds `σ` forbids the displayed perturbation and leaves only the free velocity direction when combined with the listed symmetries. **GAP:** those scripts are unavailable, and no proof of this classification is supplied here. In particular the counterexample only excludes forcing by the symmetries explicitly listed in Theorem 10; it does not exclude protection by additional exact symmetries. The draft's numerical dimensions `8,4,3,1`, sample speeds, and `σ=-χ` basis identification are reported checks, not independently verified results.

## 6. Family content and open obligations

**Theorem 11 (free family count).** At the massless free node each five-mode law has 20 two-component Weyl fields per cell: ten of each chirality. As left-handed fields, U has `2(5⊕5bar)` under its global U(5), and O has two vector `10`s under global SO(10). These contain neither the SU(5) `10` nor a Spin(10) `16`. `L_cube` has four Weyl fields.

*Proof.* The eight residue dimensions split into spin dimension two, two `χ_G` chiralities, and two tastes. Five flavours multiply the number of Weyl fields by five. U's flavours are `5`; conjugating the opposite chirality yields `5bar`. O's ten Majorana components form the real SO(10) vector, so each taste yields one vector after the same conversion. The representations named in the conclusion are not summands of these elementary representations. □

### 6.1 Readings, not an adoption

M1 passes on both five-mode free walks: 20 ≥ 16; it fails on the four-field `L_cube`. M2 fails for both by Theorem 11. M3 imports CH1 Corollary U-T″: U has the one-site perturbatively anomaly-free line-family operator content exactly for `2≤m≤8`, and not for `m=1,9`; this does not establish absence of all global anomalies, light chiral dynamics, or a mirror gap. CH1 Amendment 1 describes the family through the appropriate covering of U(5). On O, LW1_5 Theorem SC excludes moving spinor-class charge in its stated centre-class sense, while CH1 Amendment 2 excludes an exact Standard Model multiplet in its stated tensor-class operator comparison. CH1 Amendment 4 limits the latter result: it gives no named failing step on gauge-invariant comparison data. Thus neither this operator result nor M2 eliminates O as a long-distance law. The owner reading R-CG1 remains open. MT1-ii is resolved only within these proposed, restricted readings, not as a physical family claim.

### 6.2 MT1-S and three attacks

**MT1-S (open).** On either five-mode law, in the VC1 vacuum, the light fermion-odd excitations have a node whose leading generator satisfies ER's Clifford one-cone condition. Theorem 9 makes this sufficient for spin 1/2 **under ER**. An additional identification of ER with the physical rotation group remains necessary for MT1(a)(2). Composite fermions require the condition for their own leading generator.

- **A1, symmetry:** fails at the claim that the listed cell rotations, inversion and free antiunitary symmetry force one cone; Theorem 10 supplies a counterexample. Further symmetries and their action on an interacting node remain open; see LW1-5-T.
- **A2, continuity:** fails at the claimed small parameter because the free link replacement is auxiliary. Even an arbitrarily small perturbation need not preserve the Clifford condition, by Theorem 10.
- **A3, renormalization:** fails at a controlled flow for these gauged Floquet laws; ZM1-i is open. The draft cites Anber–Donoghue on velocity convergence, but that does not establish this matrix-valued taste-and-direction flow or LZ1's bounds.

These are failures of the named routes, not a no-go theorem. No counterexample to MT1-S is supplied. MT1-S is related to, but is not the whole of, LZ1-i: the latter also needs a common speed across species. VC1, CH1-5U-i, CH1-5O-i, CH1-5O-E, and GA1-P-5 retain their independent obligations. Neither the hop identity, the free-node count, nor the proposed readings prove a vacuum excitation, a chiral family, or a physical long-distance spin assignment.
