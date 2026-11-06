# MT1. Fermions, statistics and spin

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (MT1_REFEREE.md); the referee's edits are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. MT1 is open. The statements below are conditional on the named laws and imported results. They do not establish a vacuum, a particle spectrum, or a physical identification of the emergent rotations.

**Amendment 1, 2026-11-06 (MT1-S; frozen part `LZ1.md`).** No proved result of this file changes.
- MT1-S read in the vacuum's own GNS representation (reading R-loc) is false on both five-mode laws. `LZ1.md` (Claude draft `LZ1_DRAFT.md`, Codex distillation, referee `LZ1_REFEREE.md`, frozen) proves it: the local centre elements commute with every gauge-invariant tick, so every odd band of a stationary, cell-invariant, centre-invariant state lies in the nontrivial Gauss-pattern sector, where the tick does not depend on momentum, and is flat at each node with zero leading generator (`LZ1.md` Theorems 2.1-2.2, Corollary 2.3).
- MT1-S therefore needs a charged-sector prescription, R-CS. This is the same owner question as CH1's charged-correlator prescription. Under R-CS, on `L5-U` at `μ = 0 = τ_E`, a node fibre unitarily equivalent to the free node representation has a Clifford leading generator up to a real scalar (`LZ1.md` Theorem 5.1); two copies allow unequal speeds (`LZ1.md` RC3).
- `LZ1.md` Theorem 5.2 gives an antiunitary symmetry of the dressed `L5-O[S_+]` tick for all constants.
- Open after this amendment: MT1-S[R-CS]; R-CS; MT1-i; the rest of the list below is unchanged.

**Amendment 2, 2026-11-06 (charged sectors; frozen part `RCS1.md`).** No proved result of this file changes.
- On both laws no gauge-invariant odd composite exists, and a localized odd sector admits no translation (`RCS1.md`, Claude draft `RCS1_DRAFT.md`, Codex distillation, referee `RCS1_REFEREE.md`, frozen).
- Under the Fredenhagen–Marcu straight-string prescription R-CS^str, MT1-S fails in flavour-locked states (no sectors) and in the state `ω_AB` on `L5-U[2,4]`, whose string sectors are odd by the referee's relative parity `χ_tot` (`RCS1.md` Theorem 8 with R2). This is not the VC1 vacuum.
- Eight candidate prescriptions carry four-test verdicts in `RCS1.md`; none is adopted. Open after this amendment: R-CS (owner, including the odd label outside parity-sharp backgrounds); RCS-P; MT1-S[R-CS^str] in the VC1 vacuum, with VC1.

**Amendment 3, 2026-11-06 (prior work in the repository; digest `prior/MT1.md`).** No proved result of this file changes. MT1 was drafted before the prior-work gate (SCIENCE_WORKFLOW rule 9, PR #10138). The digest (Codex `gpt-6.1-sol`, read-only) records:
- Duplicates, credited here: Theorem 5's one-body half-turns and Theorem 8's spin–taste factorization and count are PR #10129 (`docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`); Theorems 7 and 11's free node and count are `FL1_DRAFT.md` Theorem B; M3's family criterion is `CH1.md`.
- Theorems 2 and 9 and Corollary 9.1 are new in the searched files; Theorems 1, 3–6, 8, 10–11 and C4 extend earlier results.
- Contradicted: nothing; the draft's claimed MT1-i closure was corrected.
- Inputs that the open statements should use: PR #10126 (`docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`) #10029 and PR #10129 (`docs/FAMILIES_FLAVOUR_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`) #10044, for symmetry and the corrected commutant; `docs/BKSF_CUBIC_FERMION_CODES_ARE_NOT_ROTATION_INVARIANT_MINIMAL_ORBIT_FOUR_BOUNDED_THEOREM_NOTE_2026-10-17.md` and `docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`, for encoding and localization; `docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md` and `docs/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md`, for charged-sector intermediate targets; `LZ1.md` and `RCS1.md`, for the charged prescription; `CH1.md` and `LIT_SMG.md`, for family operators and the remaining dynamics.
- Open statements are unchanged.

**Proved in the stated algebraic setting.** Each cell rotation has a cell-periodic sign lift, unique up to phase (Theorem 1). Matter parity is implemented locally by the centre (Theorem 6). The resolved hopping identity has sign −1. The finite-register laws have a local cluster presentation for the centre-even algebra. The free cell has a six-generator Clifford algebra. Its perpendicular face half-turn lifts anticommute. At the massless free node the leading generator has one isotropic Clifford cone. Under the proposed definition ER its internal rotation has spin 1/2. The cell rotations factor into spin and taste; each chirality is irreducible under the cell group. The spin factors restrict the ER action, with the taste and extension properties of Corollary 9.1. A linear perturbation allowed by the cell rotations, inversion and the free antiunitary symmetry splits the cone; at `μ=0` the free symmetry `σ` forbids it. The free node has 20 Weyl fields on each five-mode law, with the representations stated in Theorem 11.

**GAP.** The draft's closure of MT1-i does not follow from the cluster construction: it uses link-end modes, does not produce the specified BKSF embedding, and does not construct local excitations of the VC1 vacuum. R-X tests an operator identity, not the existence or exchange of physical particles. MT1-S alone gives spin 1/2 under ER, but does not identify ER with the physical long-distance rotation group. The draft's chirality label requires conjugation into the velocity basis; see the correction after Theorem 7. The referee closures C1–C8 below are unrefereed; the interacting use of the free symmetry action remains open.

**Open by name.** MT1-S; MT1-i; MT1-ii as a physical family claim; VC1; ZM1-i; LZ1-i; CH1-5U-i; CH1-5O-i; CH1-5O-E; LW1-5-T; GA1-P-5; the owner reading R-CG1 of the 16. The original MT1(a) requires a common law and VC1 vacuum. Neither is supplied by free-node counting. The named failed attacks and their limits are in §6.2.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af61-ef01-7f10-8b02-8ec5ec1c3569`. Pass 1: `MT1_DRAFT.md`, Claude Opus 5.5, max effort. Checkout HEAD `028f2093b4ec8a3747204757b680d67df970dc56`. SHA-256: draft `b7330e9ec79e8a1496a44a7ddde29ce2664536bd48238dba364b2bd676bdfc9d`; assembly `8027d9d44eb5fcaf02393e06dbd75f1f1adc9d9a6e2e8a5f46c279d5e63afcc0`; LW1 `78280bd620800eac671ddf6047d42e94c2ecf919d2f938909cc5595b168c09b9`; LW1_5 `7afb7ee2a52d91cd1cab23008c53373d710d0ce66252e1e5169ba8ca6009b20e`; CH1 `633e4aa4eed86d1e89e25a6d85dda4cca1bbb0ea9eb029a33568494bfa09b395`; CH1_5U `2254f04e4532651774ebf83c3bd744050a53519f667569d066592fe61ecd07cd`. Imported results carry their own hypotheses and status. The draft reports checks in `/tmp/toe-mt1/check/`; that directory is unavailable in this session. Its checks are not independent evidence here. Its literature search and citations are in its introduction; this distillation does not assert an independent literature check.

**Editing session provenance.** Codex `gpt-6.1-terra`, effort high, codex-cli 0.165.0, session `01a1af91-1702-7ae1-9579-349779332e7f`.

## 1. Definitions inferred by the distiller

**Setting.** PS-5 supplies five CAR modes per site. PS-6r supplies finite link registers. Both `L5-O[S_+]` and `L5-U[m]`, `1 ≤ m ≤ 9`, remain live under LW1-5-RQ. Use the definitions and centre actions in `LW1_5.md`. A free tick replaces link operators by c-numbers; it is auxiliary, not the interacting tick or vacuum. `L5-U` has free walk `V ⊗ 1_5`; `L5-O` has `(WVW*) ⊗ 1_5`, `W_x=i^{x_1+x_2+x_3}`. The latter shifts the cell node by `(π,π,π)` and changes the residue basis by a fixed unitary. Statements below about `V` at cell momentum `K` hold for the L5-O free walk at `K+(π,π,π)` after conjugation by `D=diag(i^{r_1+r_2+r_3})` (`LW1_5.md` line 322). In particular the L5-O internal generator in Theorem 9 is `DSD*`.

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

*Proof.* LW1 A2 supplies a sign lift. Comparing a signed edge and its image fixes the product of its endpoint signs. Two lifts differ by a diagonal matrix constant on each nearest-neighbour edge, hence constant on the connected lattice; the matrix-valued case gives one constant unitary. The product of those ratios along two consecutive edges in one direction is 1, since the sign of such an edge is independent of its coordinate in that direction, as is the sign on its rotated image. Thus the lift is cell-periodic. Theorem 1 holds on every even torus: `g_Q(x+Lb)=g_Q(x)+LQb`, and the sign function is cell-periodic, hence `L`-periodic. So the one-body lifts anticommute on every even torus, as the `Γ_F` identity needs. The fibre formula follows from `g_Q(2b+r)=2Qb+g_Q(r)`. □

**Theorem 2 (resolved hopping identity).** Let `j,k,l` be distinct neighbours of `i`. Link operators `X` on their three distinct links commute with each other and with matter. For U define `t_il=c†_{i,e}X_il c_{l,b}`, `t_ki=c†_{k,c}X_ki c_{i,e}`, `t_ij=c†_{i,e}X_ij c_{j,f}`. For O use the analogous `(i/2)γ X γ` terms with the same central Majorana label. Then
\[
 t_{il}t_{ki}t_{ij}=-t_{ij}t_{ki}t_{il}.
\]
The identity holds on every state and for every choice of the link operators.

*Proof.* The link factors agree. For U, use `c_i c†_i=1-n_i`, `c†_i n_i=0`, and commute the even `n_i` past the other sites. The two matter factors differ by reversal of three mutually anticommuting operators at `j,k,l`, giving `(-1)^3`. For O use `γ_i²=1` and the same reversal. □

**GAP (draft §2.1).** A Majorana bilinear need not move a conserved particle, and arbitrary resolved components need not preserve the physical sector separately. The identity is exactly the claimed algebraic result, but the inference that *every excitation moved by the laws* has a physical exchange statistic needs a particle and exchange construction. For the law's own link components both sides are nonzero; see C1 (referee closure, MT1_REFEREE.md). The draft's nonzero U example is a reported numerical check, not reproduced here.

**Theorem 3 (finite cluster presentation).** On an even torus, group the five matter modes at each site with five auxiliary link-end modes for each incident link: 35 complex modes per site. For U use its rishons and impose `p_{ℓ,x}+p_{ℓ,y}=m`. For O embed `S_+` in the Fock space of ten complex link modes and impose link chirality `+1`. The law's Hilbert space is unitarily equivalent to the constrained subspace of the ordinary tensor product of the cluster Fock spaces. Site values, end numbers, end chiralities and Gauss generators are cluster-local; each hop is a sum of products of operators at its two endpoint clusters. The centre element at a site is its cluster parity up to a scalar. Centre-even local operators are local on the clusters they touch, provided they are operators of the constrained law algebra.

*Proof.* First apply Klein strings in an order of species to turn the matter CAR and the mutually commuting link species into one graded CAR algebra. The law's hopping terms contain an even number of modes in each original species, so their strings cancel. In the graded algebra each U term groups as `(c†_y r_y)(r†_x c_x)` and each O term as `i(γ_yη_y)(η_xγ_x)`; each factor is cluster-even. The Gauss generators and the stated local values are cluster-even functions of cluster modes. Order all modes cluster by cluster and apply Jordan–Wigner: cluster-even products have no intercluster strings. The number or chirality constraints pick precisely the original link register. The U centre multiplies all matter and incident rishon modes at the site by −1. For O, the centre is the site parity times the product of end parities, up to a scalar, by the centre identities in LW1_5. Every link operator is the restriction of a link-even mode polynomial, and averaging an extension of a centre-even law operator over cluster parities gives a cluster-even extension. Thus general centre-even local law operators map locally; see C2 (referee closure, MT1_REFEREE.md). Electric gates are local at one end, and gauge-invariant plaquette operators are covered if they preserve the link constraints. □

**GAP (draft Corollary 2.3).** This presentation uses 30 link-end modes in addition to the five site modes. It gives a local encoding of the centre-even algebra, not a local representation of individual odd matter operators. No local qubit encoding represents single odd operators locally on disjoint factors: such operators commute, whereas distinct single CAR modes anticommute and have nonzero product. This is no shortfall against BKSF (referee closure, MT1_REFEREE.md). D1 changes PS-5's site content; it does not by itself prove the BKSF-and-role-pattern input in MT1(e), or remove the VC1 requirement. Thus MT1-i remains open under the literal target. The same construction applies to `L_cube` at `S=1/2` through the stated one-mode U equivalence; it is not claimed for other registers. The structural comparison in pass 1 credits Bravyi–Kitaev, Zohar–Cirac, and Brower–Chandrasekharan–Wiese; these citations are not used as proofs.

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

**Theorem 6 (centre and matter parity).** For a local operator supported on matter sites and links whose endpoints lie in a finite set `Λ`, matter parity `θ` equals conjugation by the product of local centre elements over `Λ`, on `L_cube`, U, and O[S_+]. The centre elements are `e^{iπ𝒢_x}` on `L_cube`, `Γ_x(−1)` on U, and `ω_x` on O[S_+]. Gauge-invariant local operators are `θ`-even. On every even torus the product of all centres equals `(-1)^N` (referee closure, MT1_REFEREE.md).

*Proof.* The site factors implement matter parity. The two endpoint actions on each complete link multiply to a scalar, so their joint action on the link algebra is the identity: their product is 1 for `L_cube`, `(-1)^m` for U, and −1 on `S_+` for O. A gauge-invariant local operator is fixed by every centre. The finite-torus identity follows by multiplying the same factors. For O the site factors give `(−i)^V`. On every even torus `V=L³` is divisible by 8 and the number of links `3V` is even, so all three scalars equal 1 (referee closure, MT1_REFEREE.md). □

The spinor label applies to odd matter sectors with the stated lifts. Gauge-invariant local observables are even; a physical charged state and its boundary dressing still need specification. On L5-O the free walk’s lifts and the dressed lifts differ by a centre gauge transformation that is not constant in space. It acts as the identity on gauge-invariant operators, but not on fermion-odd ones (C7; referee closure, MT1_REFEREE.md).

## 4. Free node and emergent spin

**Theorem 7 (free node).** At `μ=0`, near `K=0`, `V(K)=exp(-ih(K))` with
\[
 h(K)=v\sum_jK_jG_j+O(|K|^2),\quad v=\sin\varepsilon/\sqrt3,\quad
 G_j=U\Gamma_jU^*,\quad U=e^{i\varepsilon R_e/2}.
\]
The `G_j` are Clifford generators, so the leading eigenvalues are `±v|K|`, each fourfold. The only `V=I` node is `K=0`. At `μ>0`, `V(0)=e^{iμR_e}` and `R_e` anticommutes with every `Γ_j`.

*Proof.* `R_o(0)=R_e=R` and `R_o(K)-R=-ΣK_jΓ_j/√3+O(K²)`. Duhamel's formula and `{R,Γ_j}=0` give `i dV(0)=vΣK_j e^{iεR}Γ_j=vΣK_jUΓ_jU*`. The analytic logarithm near the identity gives the expansion. The Clifford square gives the spectrum and equal multiplicities. LW1 B10 gives `1-cos w=sin²ε(1-χ(K))`, whose equality case is `K=0`. The massive identity follows directly from the two half-steps. □

**Correction (draft §§3.4, 4.2).** Set `χ=-iΓ_1Γ_2Γ_3`. It generally does **not** commute with `G_j`: `χ` anticommutes with `R_e`, so `UχU*` differs from `χ` for every `ε` in the window. The Weyl chirality of the leading generator is `χ_G=-iG_1G_2G_3=UχU*`. The draft's counting is correct after this conjugation. The `χ` eigenspaces used below are rotation-invariant and are carried to the corresponding `χ_G` eigenspaces by `U`.

**Theorem 8 (spin times taste).** Put `S_k=-(i/4)Σ_ab ε_kab Γ_aΓ_b` and `S^A_k=-(i/4)Σ_ab ε_kab A_aA_b`. Each triple is spin 1/2, the triples commute, and `S` commutes with `R_e`. On each four-dimensional `χ=±1` space, they act on `C²_spin⊗C²_taste`. For each cell rotation, `ρ̂(Q)=S(Q̃)T(Q)`, where `Q̃∈SU(2)` lifts `Q`: for `Q` the rotation by `φ` about the unit axis `n` and a lift `Q̃=±e^{−iφn·σ/2}`, put `S(Q̃)=±e^{−iφn·S}`. Here `T` commutes with every `Γ_j`, and `T A_j T*=A_{π(j)}`. Face half-turns have scalar `T`. A three-cycle has taste rotation by `±2π/3` about `(1,1,1)`; a transposition has taste rotation by `π` about `(e_j-e_k)/√2`, up to chirality-dependent phases. Taste is irreducible on each chirality, and so is the full four-dimensional projective cell representation.

*Proof.* Clifford relations give both `su(2)` commutators, Casimir `3/4`, and mutual commutation. The chirality `χ` commutes with the `Γ` and both bivector triples and anticommutes with each `A`; its eigenspaces have dimension four. Decompose each under spin; its two-dimensional multiplicity carries the taste spin 1/2 by the commuting Casimir. The spin lift and `ρ̂(Q)` have the same action on the `Γ` matrices, so their quotient fixes them and permutes the `A` matrices. For a 3-cycle the induced taste adjoint is the stated 3-fold rotation. For a transposition it is the stated half-turn; multiplication by `χ` implements the missing overall sign on the `A`'s and becomes a scalar within each chirality. The two noncommuting taste rotations have no common invariant line. The face half-turns generate the spin matrix algebra, so any operator commuting with all cell rotations is scalar on spin and then scalar on taste. □

The per-chirality character moduli on identity, 3-fold, face half-turn, quarter-turn, edge half-turn classes are `4,1,0,0,0`; they agree in modulus with restricted spin 3/2. This does not identify the physical continuum spin. The pass-1 comparisons credit Golterman and Catterall–Pradhan–Samlodia for spin–taste factorizations.

**Theorem 9 (ER boost algebra and free spin).** Under ER, put `L_k=Σ_ab ε_kab x_aq_b` and `S^N_k=-(i/4v²)Σ_ab ε_kab N_aN_b`. Then
\[
 [K_i,K_j]=-iv²\sum_k ε_{ijk}(L_k+S^N_k),\qquad J_k=L_k+S^N_k,
\]
`[J_k,h_1]=0`, and every internal irreducible summand has spin 1/2. The free massless node of all three laws satisfies ER. Its internal generator is `S`, with five flavours where applicable. At `μ>0`, the rest eigenspaces of `R_e` each carry spin 1/2 with multiplicity two per flavour.

*Proof.* Let `D_i=[x_i,h_1]=iN_i`. Since `K_i=x_i h_1-D_i/2`, expansion gives `-[x_i{D_j,h_1}-x_j{D_i,h_1}]/2+[D_i,D_j]/4`. Insert `{D_j,h_1}=2iv²q_j` and the Clifford relations. The bivectors obey `su(2)` with Casimir `3/4`; orbital and spin commutators with `h_1` cancel. For the free walk use Theorem 7 and the fact that `U` commutes with `S`. For nonzero mass, `R_e` commutes with `S` and its two eigenspaces have equal dimension. □

**Corollary 9.1.** At the free node, the spin factors of the cell rotations are restrictions of ER's internal SU(2) action. The taste factors `T(Q)=UT(Q)U*` commute with every `G_j`. A lattice rotation is a phase times a pure spin rotation exactly for the identity and the three face half-turns. The taste action on one chirality has no continuous homomorphism `SU(2)→U(2)` extending it up to phases.

*Proof.* The first two assertions follow from Theorems 8–9. A pure spin rotation fixes all `A_j`; Theorem 4 forces `π=id`, giving exactly the four diagonal proper rotations. For the last assertion, a face half-turn has scalar taste. All trace-zero elements of SU(2) are conjugate, and every SU(2) element is a product of two trace-zero elements. An extension with one scalar trace-zero image is therefore trivial, contrary to the irreducible non-scalar taste action. □

A different diagonal combination of spin with an internal taste SU(2) can assign other spins. ER selects the boost-generated choice, which commutes with the internal commutant. This is a mathematical choice; physical uniqueness remains open.

## 5. A symmetry-allowed cone splitting

**Theorem 10 (counterexample to symmetry forcing one cone).** Let `Z^G_j=UZ_jU*` and `h_u(K)=vΣ_jK_j(G_j+uZ^G_j)`. It transforms covariantly under the proper cell rotations and inversion, and obeys the free walk's antiunitary condition `D_r overline{h_u(-K)} D_r=-h_u(K)`, `D_r=Z_1Z_2Z_3`. For all sufficiently small nonzero `u`, it is not one isotropic Clifford cone. The added term is the leading term of a finite-range cell-periodic operator.

*Proof.* Inversion has sign lift `±A_1A_2A_3`: it fixes all `A` and negates all `Γ`. From `Z_j=-iΓ_jA_j`, Theorem 4 gives the vector transformation of `Z`; inversion negates it. `D_r` fixes `Z` and sends `overline{Γ_j}` to `Γ_j`; it also fixes `U` under antiunitary conjugation. Thus both triples have the stated covariance. Conjugate by `U*`. Along `e_3`, `(Γ_3+uZ_3)²=1+u²`. Along `(1,1,1)/√3`, the squared velocity is `1+(2u/3)Y+O(u²)`, where `Y=iΣ_{i<j}Γ_iΓ_j(A_i-A_j)`. Its six Clifford monomials are distinct and orthogonal, so `Y` is nonzero, Hermitian and traceless. It has eigenvalues of both signs, hence some diagonal speed changes at first order while the axial speed does not. Finally `Σ_j Z_j(T_{-2e_j}-T_{2e_j})/(2i)` has fibre `Σ_j sin K_j Z_j`; conjugation by the cell-local `U` preserves finite range. □

At `μ=0`, `σ=V_e^{-1}τ` is a free symmetry, where `τ` is LW1 A2's signed diagonal translation: `τVτ^{-1}=V_eV_o`, so `σVσ^{-1}=V`. The same argument gives `σ=M_e^{-1}τ` for the dressed base tick when `τ_E=0`; no plaquette layer is asserted. At the node `σ` is a phase times `χ_G` (C3), and the node forms of the rotations, inversion, `Θ` and `σ` allow exactly real multiples of the free velocity triple; each of the latter three conditions is needed (C4; referee closure, MT1_REFEREE.md). In particular the counterexample only excludes forcing by the symmetries explicitly listed in Theorem 10; it does not exclude protection by additional exact symmetries. The draft's numerical dimensions `8,4,3,1`, sample speeds, and `σ=-χ` basis identification are reported checks, not independently verified results.

## 6. Family content and open obligations

**Theorem 11 (free family count).** At the massless free node each five-mode law has 20 two-component Weyl fields per cell: ten of each chirality. As left-handed fields, U has `2(5⊕5bar)` under its global U(5), and O has two vector `10`s under global SO(10). These contain neither the SU(5) `10` nor a Spin(10) `16`. `L_cube` has four Weyl fields.

*Proof.* The eight residue dimensions split into spin dimension two, two `χ_G` chiralities, and two tastes. Five flavours multiply the number of Weyl fields by five. U's flavours are `5`; conjugating the opposite chirality yields `5bar`. O's ten Majorana components form the real SO(10) vector, so each taste yields one vector after the same conversion. The representations named in the conclusion are not summands of these elementary representations. □

### 6.1 Readings, not an adoption

M1 passes on both five-mode free walks: 20 ≥ 16; it fails on the four-field `L_cube`. M2 fails for both by Theorem 11. M3 imports CH1 Corollary U-T″: U has the one-site perturbatively anomaly-free line-family operator content exactly for `2≤m≤8`, and not for `m=1,9`; this does not establish absence of all global anomalies, light chiral dynamics, or a mirror gap. CH1 Amendment 1 describes the family through the appropriate covering of U(5). On L5-O[S_+], one-site operator content is tensor class (`LW1_5.md` F and K, and Corollary SC.1: "With one end-pure class on all links, every \(z_x\) is the scalar \(-1\) (Σ below), every local operator is tensor class everywhere, and (e) is vacuous."). So M3 fails there for the 16. Theorem SC adds that no spinor-class charge moves under any finite register. On O, CH1 Amendment 2 excludes an exact Standard Model multiplet in its stated tensor-class operator comparison. CH1 Amendment 4 limits the latter result: it gives no named failing step on gauge-invariant comparison data. Thus neither this operator result nor M2 eliminates O as a long-distance law. The owner reading R-CG1 remains open. MT1-ii is resolved only within these proposed, restricted readings, not as a physical family claim.

### 6.2 MT1-S and three attacks

**MT1-S (open).** On either five-mode law, in the VC1 vacuum, the light fermion-odd excitations have a node whose leading generator satisfies ER's Clifford one-cone condition. Theorem 9 makes this sufficient for spin 1/2 **under ER**. An additional identification of ER with the physical rotation group remains necessary for MT1(a)(2). Composite fermions require the condition for their own leading generator.

- **A1, symmetry:** On L5-U at `μ=0=τ_E`, rotations, inversion, `Θ` and `σ` are symmetries of the dressed tick, and their free node forms allow only the free direction (C4–C6; referee closure, MT1_REFEREE.md). The missing step is whether the light fermion-odd node of an invariant interacting state carries these four symmetries in their free node forms. `σ=M_e^{-1}τ` contains an interacting gate, so this step is not one-body. Where `σ` is absent (`τ_E≠0`), the route fails at Theorem 10. On L5-O two more steps fail: no antiunitary symmetry of the dressed tick is known, and the dressed lifts act on bare matter in the exchanged form of C7. See LW1-5-T.
- **A2, continuity:** fails at the claimed small parameter because the free link replacement is auxiliary. Even an arbitrarily small perturbation need not preserve the Clifford condition, by Theorem 10. On L5-O the free walk carries the dressed symmetry action only up to a centre gauge transformation that is not constant in space (C7; referee closure, MT1_REFEREE.md).
- **A3, renormalization:** fails at a controlled flow for these gauged Floquet laws; ZM1-i is open. The draft cites Anber–Donoghue on velocity convergence, but that does not establish this matrix-valued taste-and-direction flow or LZ1's bounds.

These are failures of the named routes, not a no-go theorem. No counterexample to MT1-S is known. The leading generator of the light fermion-odd excitations of an interacting state is not yet defined; on L5-O their gauge dressing also needs specification. MT1-S is related to, but is not the whole of, LZ1-i: the latter also needs a common speed across species. VC1, CH1-5U-i, CH1-5O-i, CH1-5O-E, and GA1-P-5 retain their independent obligations. Neither the hop identity, the free-node count, nor the proposed readings prove a vacuum excitation, a chiral family, or a physical long-distance spin assignment.


## 7. Referee closures

The following closures are reproduced from MT1_REFEREE.md and have not been independently refereed. References to MT1 line numbers refer to the pass-2 source. In C2, `J` denotes the unitary equivalence of Theorem 3, `𝔉_c` its constrained cluster space, and `F_x` and `C_x` the Fock space and modes of cluster `x`.

### C1. Theorem 2 is not vacuous (referee closure, MT1_REFEREE.md)

**Statement.** Take for each `X` the colour component of the law's own link operator in the hop term that moves matter along that link: `r^y_jr^{x†}_k` or its adjoint on `Λ^mC^{10}` for L5-U, and `U^{ab}=iη_aη_{10+b}` for L5-O. Then both sides of Theorem 2's identity are nonzero operators.

**Proof.** `LW1_5.md` line 33: "Links commute with matter and are ordinary tensor factors." So `t_{il}t_{ki}t_{ij}=(X_{il}⊗X_{ki}⊗X_{ij})⊗F`, where `F` is the matter factor found in the proof of Theorem 2 and identities act on the other factors. A tensor product of operators is nonzero when each factor is nonzero.
- *L5-U links.* Fix `1≤m≤9`. Choose a basis vector `e_S` of `Λ^mC^{10}` whose set `S` contains the `y`-end mode `j` and omits the `x`-end mode `k`; such `S` exists because `1≤m≤9`. Then `r^y_jr^{x†}_ke_S=±e_{(S∖{j})∪{k}}≠0`. The adjoint is nonzero too.
- *L5-O links.* `(iη_aη_{10+b})²=−η_aη_{10+b}η_aη_{10+b}=1`, so `U^{ab}` is invertible.
- *Matter.* For U, `F=c†_{i,e}c_{l,b}c†_{k,c}c_{j,f}` maps the occupation vector with `(l,b)` and `(j,f)` filled and `(i,e)`, `(k,c)` empty to plus or minus an occupation vector. For O, `F=γ_{i,e}γ_{l,b}γ_{k,c}γ_{j,f}` is a product of four unitaries.

So the left side is nonzero, and the right side is its negative. ∎ [check: one colour, four sites, random link matrices; the left side equals minus the right side and is nonzero.]

### C2. Theorem 3, the locality of centre-even operators (referee closure, MT1_REFEREE.md)

**Statement.** On an even torus, let `O` be an operator of the law supported on finitely many sites and links. Suppose `O` commutes with the centre element at every site. Let `T` be the set of sites that carry matter of `O` or are endpoints of its links. Then `JOJ^{-1}` is the restriction to `𝔉_c` of a finite sum of products of operators on the factors `F_x`, `x∈T`.

**Proof.** *Step 1: every link operator is the restriction of a link-even polynomial.* For L5-U, take `|A|=|B|=m` and ordered products `r†_A`, `r_B`. Then `r†_Ar_B` maps `e_B` to `±e_A` and kills every other basis vector `e_{B'}` of `Λ^mC^{10}`, because `r_B` kills `e_{B'}` unless `B⊆B'`, and `|B'|=|B|`. So every matrix unit on `Λ^mC^{10}` is the restriction of a number-conserving, hence even, monomial. For L5-O, write `d_c` for the ten link modes and `P_0=∏_c(1−d†_cd_c)` for the projector onto their vacuum. Then `|e_A⟩⟨e_B|=d†_AP_0d_B`. The chirality is `Γ=−η_1⋯η_{20}=(−1)^{p_x+p_y}`, because the product of the ten Majoranas of one end is `i(−1)^p` [check]. So `S_+` is the even sector of the total link number. For `e_A,e_B∈S_+` the monomial `d†_AP_0d_B` is even. Matter operators on finitely many modes are sums of monomials. So `O` is the restriction of an element `Õ` that is a finite sum of products of matter monomials and link-even polynomials. By the Klein-string step of Theorem 3's proof, `Õ` is represented in the graded algebra.

*Step 2: parity average.* The cluster parities `Π_x` and the link constraints are diagonal in the occupation basis, so each `Π_x` preserves `𝔉_c`. By Theorem 3 the centre element at `x` is a scalar times `Π_x`, so `JOJ^{-1}` commutes with each `Π_x` on `𝔉_c`. Put `Π_t=∏_{x∈t}Π_x` and `Õ'=2^{−|T|}Σ_{t⊆T}Π_tÕΠ_t`. On `𝔉_c` each term restricts to `Π_t(JOJ^{-1})Π_t=JOJ^{-1}`, so `Õ'` restricts to `JOJ^{-1}`. `Õ'` commutes with every `Π_x`, `x∈T`, and it contains no mode of a cluster outside `T`.

*Step 3: cluster-even monomials.* Normal-ordered monomials form a basis of the mode algebra, and conjugation by `Π_x` multiplies each by `(−1)^{(its degree in C_x)}`. So every monomial of `Õ'` is even in every cluster. The Jordan–Wigner step of Theorem 3's proof maps each such monomial to a product of operators on the factors `F_x` of the clusters it involves. ∎

### C3. The node form of `σ` (referee closure, MT1_REFEREE.md)

**Statement.** At `μ=0`, the fibre of `σ=V_e^{-1}τ` at `K=0` is `cχ_G` for a phase `c`, where `χ_G=−iG_1G_2G_3=UχU*`.

**Proof.** LW1 A2, last paragraph: "Finally translation by \(\mathbf1\) swaps the tilings, with a sign correction obtained by the same face argument. Conjugation by \(D_s\) reverses both hop operators. The resulting operation sends \(V_e\) to \(e^{ia_eR_o}\) and \(V_o\) to \(e^{-ia_oR_e}\)." So `τ=D_sD_dT_𝟙` with `τR_eτ^{-1}=−R_o` and `τR_oτ^{-1}=−R_e`. The sign gauge obeys `d(x)d(y)=η(e)η(e−𝟙)` on every edge `e={x,y}`. Two consecutive edges in one direction have equal `η` and equal shifted `η`, so `d(x+2e_k)=d(x)`. `D_s` is cell-periodic as well. `T_𝟙` maps `2b+r` to `2(b+r)+(𝟙−r)`. Hence `τ` commutes with cell translations, and its fibre is `τ̂(K)=τ_0E(K)`, with `E(K)=diag(e^{−iK·r})=exp(−iΣ_jK_j(1−Z_j)/2)` and `τ_0` a signed permutation.

Fix `j` and put `K=te_j`. `Z_j` anticommutes with `A_j` and commutes with `A_k`, `k≠j`. So `e^{itZ_j/2}A_je^{−itZ_j/2}=e^{itZ_j}A_j=cos t A_j+sin t Γ_j`, and `E(K)R_eE(K)^{-1}=3^{−1/2}(Σ_{k≠j}A_k+cos t A_j+sin t Γ_j)`. In fibres, `τR_eτ^{-1}=−R_o` reads `τ_0E(K)R_eE(K)^{-1}τ_0^{-1}=−3^{−1/2}(Σ_{k≠j}A_k+cos t A_j−sin t Γ_j)` for all `t`. The functions `1`, `cos t`, `sin t` are independent. So `τ_0A_kτ_0^{-1}=−A_k` for every `k` and `τ_0Γ_jτ_0^{-1}=Γ_j`. The unitary `χ` induces the same map. By Theorem 4 the six generators span `M_8(C)` as an algebra, so `τ_0=cχ` with `|c|=1`. Finally `σ̂(0)=e^{iεR_e}τ_0=c e^{iεR_e}χ=cUχU*`, because `χ` anticommutes with `R_e`. ∎ [check: `τ̂(0)` is proportional to `χ` and `σ̂(0)` to `χ_G` on a torus of side 4.]

**Node forms.** Near `K=0` put `h=i log V`; conjugation commutes with the analytic logarithm. Each symmetry of `V` gives a condition on the linear term `h_1(K)=Σ_jK_jN_j`, read off at first order in `K`. Rotations: `ρ̂(Q)N_jρ̂(Q)*=Σ_iQ_{ij}N_i`. Inversion: `ρ̂(I)N_jρ̂(I)*=−N_j`. `Θ`: `D_rN̄_jD_r=N_j` (Theorem 10's proof). `σ`: `σ̂(K)=σ̂(0)+O(K)` and `h=O(K)`, so `σ̂(0)N_jσ̂(0)^{-1}=N_j`, that is, `N_jχ_G=χ_GN_j`.

### C4. Proposition C: the four free symmetries force one cone at the node (referee closure, MT1_REFEREE.md)

**Statement.** Let `N_1,N_2,N_3` be Hermitian `8×8` matrices with
- (R) `ρ̂(Q)N_jρ̂(Q)*=Σ_iQ_{ij}N_i` for every `Q∈O`;
- (I) `ρ̂(I)N_jρ̂(I)*=−N_j`, with `ρ̂(I)=±A_1A_2A_3`;
- (Θ) `D_rN̄_jD_r=N_j`, with `D_r=Z_1Z_2Z_3`;
- (σ) `N_jχ_G=χ_GN_j`.

Then `N_j=aG_j` for one real `a`. For `a≠0` this is one isotropic Clifford cone with speed `|a|`. Each of (I), (Θ), (σ) is needed. Write `{j,k,l}={1,2,3}`. The triples
- `G_j+uU(iS_jA_j(A_k+A_l))U*`, which satisfies (R), (Θ), (σ) and not (I);
- `G_j+uUZ_j(A_k+A_l)U*`, which satisfies (R), (I), (σ) and not (Θ);
- `G_j+uZ^G_j` (Theorem 10), which satisfies (R), (I), (Θ) and not (σ);

have no isotropic cone for small `u≠0`.

**Proof.** `U=e^{iεR_e/2}` commutes with every `ρ̂(Q)` and with `ρ̂(I)`, since both commute with `R_e=Σ_jA_j/√3`. Also `D_rŪD_r=U`, since `D_rA_jD_r=−A_j`. So `M_j=U*N_jU` satisfies (R), (I), (Θ) and (σ′) `M_jχ=χM_j`.

Expand `M_j` in the basis `Γ^SA^R` of Theorem 4, with ordered products over subsets `S,R⊆{1,2,3}`. Conjugation by `χ` multiplies `Γ^SA^R` by `(−1)^{|R|}`. Conjugation by `ρ̂(I)` multiplies it by `(−1)^{|S|}`. Conjugation by `ρ̂(h_1)=λ_1Γ_2Γ_3` multiplies it by `(−1)^{|S∩{2,3}|}`; `h_2` and `h_3` act likewise with `{1,3}` and `{1,2}`. These maps act coefficient by coefficient. So (σ′) keeps only even `|R|`, and (I) keeps only odd `|S|`. (R) for `h_1, h_2, h_3` requires, in `M_1`, that `|S∩{2,3}|` be even and `|S∩{1,3}|`, `|S∩{1,2}|` be odd. With `|S|` odd this leaves `S={1}`. The same holds for `M_2`, `M_3` with their own index. So `M_j=Γ_jP_j` with `P_j∈span{1,A_1A_2,A_1A_3,A_2A_3}`.

Write `P_1=a+b_{12}A_1A_2+b_{13}A_1A_3+b_{23}A_2A_3`. Let `C` be the 3-fold turn with `Ce_1=e_2`, `Ce_2=e_3`, `Ce_3=e_1`. (R) for `C` gives `M_2=ρ̂(C)M_1ρ̂(C)*=Γ_2(a+b_{12}A_2A_3−b_{13}A_1A_2+b_{23}A_3A_1)`. Let `C_4` be the quarter-turn with `C_4e_1=e_2`, `C_4e_2=−e_1`, `C_4e_3=e_3`. (R) for `C_4` requires `ρ̂(C_4)M_1ρ̂(C_4)*=M_2`. The left side is `Γ_2(a−b_{12}A_1A_2+b_{13}A_2A_3−b_{23}A_3A_1)`. Comparing coefficients gives `b_{12}=b_{13}=:b` and `b_{23}=0`. So `M_j=Γ_j(a+bA_j(A_k+A_l))`.

`Γ_j` is Hermitian and `Γ_jA_jA_k` (`k≠j`) is anti-Hermitian. So `a` is real and `b` is imaginary. With `Γ_jA_j=iZ_j`, `M_j=aΓ_j+b′Z_j(A_k+A_l)` with `b′=ib` real. (Θ) sends `Z_jA_k` to `Z_j(D_rA_kD_r)=−Z_jA_k`, so `b′=0`. Hence `M_j=aΓ_j` and `N_j=aG_j`. Conversely `aG_j` satisfies all four conditions: (R), (I) and (Θ) by Theorem 10's proof, and (σ) because each `G_j` commutes with `G_1G_2G_3`.

*The witnesses.* Each witness satisfies the three conditions claimed [check: `check_witness.py`]. By hand, the parities of `|S|` and `|R|` and the action of `D_r` decide (I), (σ) and (Θ) as above. (R) holds for the second witness because it lies in the family `Γ_j(a+bA_j(A_k+A_l))`. It holds for the first because `S_j` and `Γ_j` transform alike under rotations, so the computation above applies with `Γ_j` replaced by `S_j`. For `Z^G` the failure of one cone is Theorem 10. Work in the frame of `M_j` for the other two. Without (Θ): `M_1=Γ_1+uZ_1(A_2+A_3)` gives `M_1²=1−2iu(A_1A_2+A_1A_3)+O(u²)`. Since `(A_1A_2+A_1A_3)²=−2`, the squared speeds along `e_1` are `1±2√2u+O(u²)`. Without (I): `iS_1=Γ_2Γ_3/2`, so `M_1=Γ_1+(u/2)Γ_2Γ_3A_1(A_2+A_3)`. `Γ_1` commutes with `Γ_2Γ_3A_1A_k`, so `M_1²=1+u·iχA_1(A_2+A_3)+O(u²)`. Since `(iχA_1(A_2+A_3))²=2`, the squared speeds along `e_1` are `1±√2u+O(u²)`. One isotropic cone has equal speeds in every direction. Both split at first order. ∎ [check: the real dimensions of the solution spaces are 8 (R), 4 (R, I), 3 (R, I, Θ), 1 (R, I, Θ, σ), 2 (R, I, σ), 2 (R, Θ, σ); squared-speed spreads along `e_1` at `u=0.01` are `0.0566` and `0.0283`.]

**Remark (L5-U at `μ=0=τ_E`).** The four symmetries are symmetries of the dressed L5-U tick there: rotations by `LW1_5.md` B1-U, inversion by C5, `Θ` by C6 and `σ` by `MT1.md` line 120. On matter one-body operators the first three act as the free ones, tensored with flavour. A Hermitian triple on `C^8⊗C^5` that commutes with `1⊗U(5)` has the form `N_j′⊗1_5`, because the commutant of `U(5)` on `C^5` is the scalars. So: if the leading generator of the light fermion-odd excitations of an invariant state is a Hermitian triple on `C^8⊗C^5`, invariant under `U(5)` and under these four symmetries in their free node forms, then it is `aG_j⊗1_5`. The hypothesis is not proved. In particular `σ=M_e^{-1}τ` contains the interacting gate `M_e`, so its action on an interacting node is not one-body.

### C5. Inversion is a symmetry of the dressed base ticks (referee closure, MT1_REFEREE.md)

**Statement.** Let `I(x)=𝟙−x`, the inversion through `c_0`. For `L_cube`, for L5-U with every `m`, and for L5-O[S_+], and for all `ε, μ, τ_E`, there is an automorphism of the quasi-local algebra that moves sites and links by `I`. It maps each cube gate to the gate of the image cube and fixes `W_E`. So it commutes with the tick automorphism.

**Proof.** `I` maps the even centres `c_0+2b` to `c_0−2b` and the odd centres `c_0+𝟙+2b` to `c_0+𝟙+2(−b−𝟙)`. So it preserves both tilings, maps links to links and reverses every link. Every face has sign product `−1` (LW1 A1) and `I` maps faces to faces. So LW1 A2's argument applies: "Their ratio has product one on every face. Fix its value at one site and define a site sign by multiplying the ratios along an edge path to that site." It gives signs `d` with `d(Ix)d(Iy)=η(e)η(Ie)` on every edge. The three covariance proofs treat reversed links explicitly. They use only that the map preserves both tilings, maps links to links and has such signs; none uses `det Q=1`.
- *L_cube.* LW1, gauged covariance: "If it reverses an oriented link, conjugation by the spin rotation \(e^{-i\pi S^x}\) sends \(E\) to \(-E\) and \(J\) to \(J^\dagger\)." The electric squares are preserved.
- *L5-U.* `LW1_5.md` B1-U: each rishon at the `z`-end goes to the same flavour at the `Iz`-end. On a reversed link the image of `Σ_{jk}c†_{y,j}r^y_jr^{x†}_kc_{x,k}` is the adjoint of the image link's summand after exchanging `j,k`, because link factors commute with matter. So the hop maps to `d(Ix)d(Iy)` times the image hop. The electric term is kept: "On a reversed link \(p_x\mapsto p_y=m-p_x\), and \((m-p_x-m/2)^2=(p_x-m/2)^2\)".
- *L5-O.* The exchange of the two sets of ten link Majoranas is ten transpositions, with determinant `(−1)^{10}=1`. It lifts to Spin(20) and preserves `S_+`. The hop transforms as computed in C7(a). "The end chiralities agree on \(S_+\), so the electric layer is preserved" (`LW1_5.md` A2-5).

In each case the sign identity maps `H_C` to `H_{IC}`, and both layers are kept because each tiling is. ∎

### C6. An antiunitary symmetry of the dressed L5-U and L_cube ticks at `τ_E=0` (referee closure, MT1_REFEREE.md)

**Statement.** On a finite even torus, let `𝒦` be complex conjugation in the product occupation basis. That basis is the matter Fock basis in a fixed Jordan-Wigner order, tensored with the occupation basis of each `Λ^mC^{10}` (L5-U) or the `|m⟩` basis of each spin-`S` link (L_cube). Let `D_s` send `c_{x,j}` to `(−1)^{x_1+x_2+x_3}c_{x,j}`. Then `Θ_d=D_s𝒦` satisfies `Θ_dU_0Θ_d^{-1}=U_0` for all `ε, μ` when `τ_E=0`. When `τ_E≠0` it maps `W_E` to `W_E^{-1}`.

**Proof.** In this basis `c_{x,j}`, `c†_{x,j}`, the rishon operators, `J` and `E` are real matrices. So each dressed hop `h_ℓ` is real and `𝒦h_ℓ𝒦=h_ℓ`. Its two matter factors sit at sites of opposite parity of `x_1+x_2+x_3`, so `D_sh_ℓD_s=−h_ℓ`. This is the dressed form of LW1 B10: "Each \(R_T\) is real and satisfies \(D_sR_TD_s=-R_T\)." Hence `Θ_dH_CΘ_d^{-1}=−H_C` and `Θ_de^{−iaH_C}Θ_d^{-1}=e^{(+ia)(−H_C)}=e^{−iaH_C}`. So `Θ_d` fixes `M_e` and `M_o`. At `τ_E=0`, `W_E=1`. For `τ_E≠0` the generator of `W_E` is real and fixed by `D_s`, so `W_E` goes to `W_E^{-1}`. ∎ On matter one-body operators `Θ_d` acts as LW1's `Θ=D_s𝒦`, tensored with conjugation on flavour. The argument does not apply to L5-O: its Majorana hop is not real in this basis, since `γ_{2j}=−i(c_j−c†_j)`.

### C7. The dressed L5-O lifts at the free O node (referee closure, MT1_REFEREE.md)

**Statement.**
- (a) The dressed L5-O[S_+] lift of `Q∈O` (`LW1_5.md` A2-5 and B1-5) acts on matter by `γ_{x,a}↦d(gx)γ_{gx,a}`, where `d(gx)d(gy)=η(e)η(ge)` on every edge. So it acts by the sign lift `ρ(Q)` of `V`, tensored with the identity on the ten labels.
- (b) `ρ(Q)` is a lift of the free O walk `WVW*` exactly when `Qe_j=e_{π(j)}` for every `j`: the identity and the two turns about `(1,1,1)`.
- (c) In the frame where the free O walk is `V`, the fibre of the dressed matter lift at the node is a phase times `ρ̂(Q)∏_{j:s_j=−1}Z_j`. It acts by `Γ_k↦Γ_{π(k)}` and `A_k↦s_kA_{π(k)}`. The `A`-triple rotates as a vector and the `Γ`-triple is permuted without signs.
- (d) The free O walk's own lift is `Wρ(Q)W*=c̄_Qρ(Q)D_Q`, with `|c_Q|=1` and `D_Q(x)=∏_{j:s_j=−1}(−1)^{x_j}`. On matter, `D_Q` is the action of the centre gauge transformation `∏_{x:D_Q(x)=−1}ω_x`.

**Proof.** (a) `LW1_5.md` line 257: "A geometric symmetry of the dressed Majorana law acts on a reversed link by exchanging the two sets of ten auxiliary Majoranas. ... it sends \(U^{ab}\) to \(-U^{ba}\), while reversing the two matter Majoranas gives the other minus sign. Site parity implements LW1's sign lift." In detail, let `e=(x,y)` with `y=x+e_i`, and let `g` reverse it, so the image link is `e′=(gy,gx)`. The `y`-end Majoranas `η_{e,a}` go to the source end `η_{e′,10+a}`, and the `x`-end Majoranas `η_{e,10+b}` go to the target end `η_{e′,b}`. So `U_e^{ab}=iη_{e,a}η_{e,10+b}↦iη_{e′,10+a}η_{e′,b}=−U_{e′}^{ba}`. With `γ_{z,a}↦d(gz)γ_{gz,a}`, `h_e=(i/2)Σγ_{y,a}U_e^{ab}γ_{x,b}` goes to `−(i/2)d(gx)d(gy)Σγ_{gy,a}U_{e′}^{ba}γ_{gx,b}`. `U` commutes with matter and `γ_{gy,a}γ_{gx,b}=−γ_{gx,b}γ_{gy,a}`, so this equals `d(gx)d(gy)h_{e′}`. On a link whose orientation is kept, `h_e↦d(gx)d(gy)h_{ge}` directly. So `η(e)h_e↦η(ge)h_{ge}` exactly when `d(gx)d(gy)=η(e)η(ge)`. That is Theorem 1's condition for `V`.

(b) With `W_x=i^{x_1+x_2+x_3}` and `gx=Q(x−c_0)+c_0`, `Σ_k(gx)_k−Σ_kx_k=Σ_j(s_j−1)x_j+(3−Σ_js_j)/2`. Hence `W*ρ(Q)W=c_Qρ(Q)D_Q`. So `ρ(Q)` commutes with `WR_eW*` and `WR_oW*` exactly when `ρ(Q)D_Q` is a lift of `V`. By Theorem 1 this holds exactly when `ρ(Q)D_Q` is a phase times `ρ(Q)`, that is, when `D_Q` is constant, that is, when no `s_j=−1`. A proper rotation with all `s_j=1` has even `π`. [check: exactly 3 of the 24 sign lifts commute with `WVW*`.]

(c) `D_Q` is cell-periodic, with fibre `∏_{s_j=−1}Z_j`. `Z_j` anticommutes with `Γ_j` and `A_j` and commutes with `Γ_k`, `A_k` for `k≠j`. So this fibre maps `Γ_k↦s_kΓ_k` and `A_k↦s_kA_k`. Theorem 4 then gives `Γ_k↦s_k·s_kΓ_{π(k)}=Γ_{π(k)}` and `A_k↦s_kA_{π(k)}`. [check]

(d) The computation in (b) with `W` and `W*` exchanged gives `Wρ(Q)W*=c̄_Qρ(Q)D_Q`. The site factor of `ω_x` is `−iP_x` (`LW1_5.md` line 162), and conjugation by `P_x` negates the Majoranas at `x`. ∎

**Consequence.** On L5-O the free walk's lifts and the dressed lifts differ by a centre gauge transformation that is not constant in space. It acts as the identity on gauge-invariant operators, but not on fermion-odd ones. At the free node the two actions exchange the roles of the velocity triple `Γ` and the taste triple `A`. So the rotation action on a fermion-odd excitation of L5-O depends on its gauge dressing. `MT1.md` line 79 already says that "a physical charged state and its boundary dressing still need specification". L5-U has no such difference: its free hop `c†_yc_x+h.c.` is symmetric under reversal, so the free walk and the dressed lifts of B1-U use the same sign lift `ρ(Q)`.

### C8. The product of all centres on a torus (referee closure, MT1_REFEREE.md)

**Statement.** On every even torus, the product of all local centre elements equals `(−1)^N` exactly, on `L_cube`, L5-U and L5-O[S_+].

**Proof.** The centre elements at different sites commute: two share at most one link, where they act through commuting end factors. Multiply the factors as in Theorem 6. For L5-O the `V` site factors give `(−i)^V(−1)^N`. The links give `(−1)^{#links}`, by `LW1_5.md` line 199: "Their product is \(\eta_1\cdots\eta_{20}=-\Gamma\), which is \(-1\) on \(S_+\)". For L5-U the links give `(−1)^{m·#links}`; for `L_cube` they give 1. LW1 §1: "Tori have even site side length \(L\)". So `V=L³` is divisible by 8, `(−i)^V=1`, and `#links=3V` is even. ∎
