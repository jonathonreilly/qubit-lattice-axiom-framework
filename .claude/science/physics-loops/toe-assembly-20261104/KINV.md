# KINV. The zoom's kinematic lemma

## 0. Status

**Pass 2; provisional, not refereed or audited.** The statements below use the cited character and lift results as inputs. They do not select a physical vacuum or prove the TOE target.

**Proved, under the stated lift interpretation.** For odd coarse `m₁`, a unital invariant-algebra map cannot intertwine the specified end-exchanging rotation into an even-`m` U or O fine law (Theorem 2). This excludes the corresponding K-INV instances. For even `m₁`, a constant character map meets all map conditions except injectivity (Theorem 4). No injective uniformly exponentially local map can act as a character on a nonzero invariant defect projection (Theorem 5). A specified full-algebra charge-equivariant decimation cannot have `L≥2` (Theorem 6). A coarse central projection freezes a site (Theorem 7).

**GAP and repair.** In `KINV_DRAFT.md` Theorem J, Step 1 asserts that star generators at distinct fine sites commute. Their stars can share a link, so evenness and star support alone do not establish this assertion. The contradiction needs the assertion only for *nonadjacent* representatives, whose stars are disjoint. Theorem 6 makes that restriction before using commutation and retains the conclusion. The draft's claim that every defect must be handled by a local modification is stronger than Theorem 5: the theorem excludes a single character filler on a nonzero invariant projection, not every nonlocal defect mechanism. GAP-GLOBAL remains open.

**Open by name.** K-INV(m, m₁, L) with even `m,m₁`; K-INV(O; m₁, L) with even `m₁`; their existential version **K-INV-E**; **K-INV-O** with O coarse law; and K-INV with odd fine `m`, outside the original even-`m` question. Also open: **GAP-GLOBAL** (good-sector extension), ZM1-I1[INV] in non-character vacua, fine-side test non-triviality, and coarse-state symmetry under readings imposing it. Inherited: VC1 and its vacuum choice; ICE-T and ICE-U(R4); LZ1-i[ZM1a]; ZM1-G; Y1; H-BLOCK; R-CS and R-CS^str; MT1-S; ZM1(a)1 and full ZM1. The map itself excludes odd coarse `m₁` for the specified fine laws, regardless of a coarse-state symmetry requirement.

**Provenance.** Pass 1: Claude Opus 5.5, `KINV_DRAFT.md`, SHA-256 `05eae300f71c1134abb2497879520b6164e9096a4f63b42c4950902872162f91`; its reported source revisions are recorded there, not independently refreshed here. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model, effort and session id: see run log. This is a distillation with author-side checks, not independent review. `prior/KINV.md` SHA-256 `da5b488b892225e41f10043a99d4e0a079936ad227f538ac4130467a131ad7ad`; `ZM1INV.md` `e37c76dca9bc9641187913239897a8eed5aaba2714c600d02e527fb5f140a32c`; `GB1Z2L5.md` `a31db56ab72c3645cd3b79408e24f224bb7508e47bb7c8fd746e7f070e5b414f`. The draft's scratch check was not rerun and is not proof.

## 1. Definitions inferred by the distiller

1. **Laws and algebras.** `L5-U[m]` has five matter modes per site and five rishon modes at each end of a link. The total rishon number on each link is fixed to `m∈{1,…,9}`. Its local group is `U(5)`. The O law `L5-O[S₊]` uses the even ten-mode link sector and local `Spin(10)`. The fine quasi-local algebra and its gauge fixed algebra are `𝔄` and `𝔄^G`; coarse counterparts are `𝔄₁` and `𝔄₁^G`. For U coarse law write `p_{ℓ,X}` for the number at end `X`, `N_X` for the matter number, and `Q_X=N_X+∑_{ℓ∋X}p_{ℓ,X}`. On `ℓ=(X,Y)`, `p_{ℓ,X}+p_{ℓ,Y}=m₁1` and the end spectrum is `P_{m₁}={max(0,m₁−5),…,min(5,m₁)}`. End numbers and `Q_X` are invariant. Finite matter-and-link region algebras are full matrix algebras; matter factors use the CAR grading.
2. **Cells.** Coarse sites are `X=2u+r`, `u∈ℤ³`, `r∈{0,1}³`. Cell centres are `2u+(1/2,1/2,1/2)`. Cell translations are by `2b`; their fine spatial translations are by `2Lb`. Proper cubic rotations about cell centres and translations act by the coarse law's lifts `β¹`, and by the corresponding fine law's lifts `β`. The U lifts carry end numbers to their geometric images. The allowed global matter phase or parity may be composed with a fine lift. This specified action is a premise of Theorems 1–3; an arbitrary internal automorphism is not included.
3. **Map conditions.** A K-INV map `Φ:𝔄₁^G→𝔄^G` is a unital injective `*`-homomorphism; for each coarse cell translation and proper rotation there is a fine lift with `Φβ¹=βΦ`; and for each source support radius `R₀` there are constants `C_{R₀},ξ>0`, uniform over the position and the inputs of that radius, such that `dist(Φ(A),𝔄(N_R))≤C_{R₀}e^{-R/ξ}‖A‖`. `N_R` is the `R`-neighbourhood of the fine blocks corresponding to the source support. No charged-field or Gauss-generator map is required. K-INV(m, m₁, L) uses even-`m` U fine law; K-INV(O; m₁, L) uses O fine law and U coarse law; K-INV-O uses O at both scales. The zoom asks for `L≥2`.
4. **Characters and witnesses.** A character is a unital nonzero `*`-homomorphism to `ℂ`. A locked U witness for even `m=2k` has empty or full matter and the same occupied flavours `1,…,k` at both ends of every link. A locked O witness has empty or full matter and link vacuum or full link vectors as in `VC1_5.md` Theorem 4.2. Their restrictions to `𝔄^G` are characters by `ZM1INV.md` Theorem 2.1. Their invariance under the stated lifts follows from `VC1_5.md` Theorems 4.2 and 5.5 and is checked below. These are supplied mathematical witnesses, not a selected VC1 vacuum.
5. **Class J.** A unital full-algebra map `Ψ:𝔄₁→𝔄`, injective site representatives `X↦x_X` with `x_{X+2b}=x_X+2Lb`, and even finite-spectrum self-adjoint fine star operators `Q^F_x` obey, for every `X,θ`,
\[
 Ψ\operatorname{Ad}(e^{iθQ_X})=\operatorname{Ad}(e^{iθQ^F_{x_X}})Ψ. \tag{J}
\]
A K-INV map is of class J when it is the restriction of such a `Ψ`. This is an attack class, not an adopted reading.

## 2. Rotation and character obstruction

**Theorem 1 (spectra and lifts).** A character of the coarse invariant algebra takes `p_{ℓ,X}` to an integer in `P_{m₁}`. Every locked fine character is invariant under the specified cell lifts and global matter phase or parity. The proper rotation
\[
 ρ(2u+(x,y,z))=2u+(1-x,z,y)
\]
fixes the cell centre and exchanges the ends `X=2u`, `Y=2u+e₁` of its internal link; its coarse lift sends `p_{ℓ,X}` to `p_{ℓ,Y}`.

*Proof.* The spectral projections of `p` are polynomials in `p`, lie in `𝔄₁^G`, are mutually orthogonal and sum to one. A character takes each to 0 or 1, exactly one to 1. Thus its value on `p` is one of the listed integers. The lift permutes sites and link ends and changes matter modes only by phases. The U locked occupation configuration is unchanged, even when ends exchange; so is its vector state. For O, the link vacuum or full vector and the empty or full matter vectors are carried to themselves up to phases (`VC1_5.md` Theorem 4.2). Global matter phase and parity also fix these vector states. Gauge averaging fixes invariant elements, so the restricted characters are invariant. The linear part of `ρ` is `diag(-1,1,1)` followed by a swap of the last two axes; its determinant is 1 and its square is 1. It fixes the centre and swaps `X,Y`. The coarse lift transports the end-number operator accordingly. □

**Theorem 2 (P).** Let `m₁` be odd and the fine law be U with even `m` or O. For any `L≥1`, no unital `*`-homomorphism `Φ:𝔄₁^G→𝔄^G` intertwines the rotation `ρ` of Theorem 1 with one of the specified fine lifts. Injectivity and locality are not assumed.

*Proof.* Let `χ₀` be a locked fine character. Then `χ=χ₀Φ` is a coarse character and covariance plus Theorem 1 gives `χβ¹_ρ=χ`. Hence `χ(p_{ℓ,X})=χ(p_{ℓ,Y})`. Their sum is `m₁`, so each value is `m₁/2`, contrary to the integer spectrum. □

**Corollary 2.1 (P1 and P2).** K-INV(m, m₁, L) and K-INV(O; m₁, L) are false for the specified fine laws, odd `m₁` and `L≥2` (indeed the obstruction holds for `L≥1`). For a locked U or O fine witness and its base tick, the existential ZM1-I1[INV] target with a U coarse law is equivalent to existence of the corresponding K-INV map for some even `m₁∈{2,4,6,8}` and `L≥2`. With odd `m₁` there is no instance for any fine state, update or comparison class requiring these map conditions.

*Proof.* The map conditions include the rotation. `ZM1INV.md` Theorem 2.3 and R1–R2 already prove the locked-vacuum reductions, including the O-fine/U-coarse case; Theorem 2 removes the odd cases. Every target instance requires the kinematic map independently of the state and update. □

**Theorem 3 (P4).** For even `m₁`, a K-INV map and each locked fine character satisfy `χ₀(Φ([p_{ℓ,X}=m₁/2]))=1` on every coarse link.

*Proof.* Each link has an end-exchanging element in the cell group (`VC1_5.md` Theorem 2.2). Its lift is a composition of the generators in the covariance condition, so `χ₀Φ` is invariant under it. The two end values coincide and sum to `m₁`; the spectral-projection argument in Theorem 1 gives the result. □

The translation-invariant odd-register character already constructed in `ZM1INV.md` R1 is not end-reversal invariant. Theorem 2 uses rotation covariance, not an extra symmetry requirement on the chosen coarse state. If a reading changes the coarse rotation by an internal particle-hole operation at `m₁=5`, or admits fine lifts moving every locked character, this proof does not decide that reading. Theorem 2 also supplies no odd-fine-`m` result: the same end exchange precludes a reversal-invariant character there.

## 3. Three tested routes

**Theorem 4 (T: constant locked map).** For even `m₁`, let `χ₁` be a coarse locked character and define `Φ_T(a)=χ₁(a)1`. For any fine U or O law and any `L≥1`, this is a unital `*`-homomorphism, cell covariant and exactly local, but not injective.

*Proof.* A character is multiplicative and unital. Theorem 1 makes `χ₁` invariant under coarse lifts, while every fine lift fixes scalars. Scalars lie in every local algebra. The nonzero projection `1−[p_{ℓ,X}=m₁/2]` is in the kernel, since `P_{m₁}` contains another value. □

Thus attack **A, covariant characters**, fails to exclude even `m₁` without using injectivity. This does not show that every character-based argument using injectivity fails.

**Theorem 5 (NGF: no character filler).** Let `Φ` be unital, injective and uniformly exponentially local as in Definition 3. Let `0≠E=E²=E*∈𝔄^G` and let `P∈𝔄₁^G` be a local projection distinct from 0 and 1. For all sufficiently distant coarse cell translates `τ_βP`,
\[
 Φ(τ_βP)E\notin\{0,E\}.
\]
Consequently no character `χ` satisfies `Φ(a)E=χ(a)E` for every coarse invariant `a`.

*Proof.* Invariants are even under matter parity (`GB1Z2L5.md` Theorem 6, already proved in `RCS1.md` Theorem 4). Fix `δ=1/10`. Approximate `E` within `δ` by an even local `e`. Uniform locality and parity averaging approximate each `Φ(τ_βP)` within `δ` by an even `f_β` in a neighbourhood of the translated block of fixed radius. For sufficiently distant `β` the two regions are disjoint. If `Φ(τ_βP)E=cE`, `c∈{0,1}`, then
\[
 \|(f_β-c)e\|\le δ(1+δ)+δ<3δ.
\]
Even disjoint operators have tensor-product norm, so `‖(f_β-c)e‖=‖f_β-c‖‖e‖`, and `‖e‖≥1−δ`. Therefore `‖Φ(τ_βP)−c1‖<δ+3δ/(1−δ)<1`. A projection at distance less than 1 from 0 or 1 equals that scalar projection. Injectivity then gives `P=c1`, a contradiction. A character takes each translated projection to 0 or 1. □

**Corollary 5.1 (NGF1).** No K-INV map has `Φ(a)=ρ(a)+χ(a)(1−P_g)` with `P_g≠1` an invariant projection, `ρ` a `*`-homomorphism with `ρ(1)=P_g`, and `χ` a coarse character.

*Proof.* Put `E=1−P_g`. Then `ρ(a)E=0`, so `Φ(a)E=χ(a)E`, contrary to Theorem 5. □

Attack **B, good sector completed by a character**, fails at Theorem 5. `ZM1INV.md` Theorem 3.4 already constructs the `m=m₁=1` good-path sector and notes that extension by zero is nonunital. The present result excludes the stated character completion, not all extensions. Uniformity over translated inputs and separation of their blocks are essential to the proof.

**Theorem 6 (J: charge-equivariant decimation).** If (J) holds at coarse neighbours `X,Y` with distinct representatives, those representatives must be fine neighbours. Hence no class J map exists for `L≥2`, for any allowed U coarse `m₁` and either specified fine law.

*Proof.* Suppose the representatives `x,y` are not neighbours. Their stars share no factor. Their even star operators `Q^F_x,Q^F_y` therefore commute and their joint spectrum is the Cartesian product of their individual spectra. By (J), `Ψ(Q_X)` commutes with `Q^F_x`; moreover `k_X=Ψ(Q_X)−Q^F_x` commutes with `Ψ(𝔄₁)`, since `e^{iθk_X}=e^{-iθQ^F_x}e^{iθΨ(Q_X)}` implements the identity on the image. Likewise for `Y`. Applying (J) at the other site gives the cross commutators zero; hence `Ψ(Q_X), Ψ(Q_Y), k_X,k_Y` commute and have finite spectra.

Choose a finite coarse full matrix algebra `F` containing both stars. Unitality makes `Ψ|_F` injective. If `0≠π∈Ψ(F)` and `0≠κ∈Ψ(F)'`, then `πκ≠0`: matrix units reduce a nonzero coefficient of `π` to `e₁₁κ`, and `e₁₁κ=0` would imply `κ=∑_i e_{i1}e₁₁κe_{1i}=0`. Applying this to joint spectral projections shows that the fine joint spectrum is `J₁−K`, where `J₁` is the joint spectrum of `(Q_X,Q_Y)` and `K` that of `(k_X,k_Y)`.

Let `s=max(0,m₁−5)`. The individual minimum of each coarse charge is `6s`. Both minima occur separately, but not together: at the shared link an end at `s` forces the other end to `m₁−s>s`, since `m₁−2s=min(m₁,10−m₁)>0`. Thus `J₁` has no componentwise least element. The fine Cartesian product has a least point `q*−κ*`. For every `q∈J₁`, the point `q−κ*` also occurs, so `q≥q*` componentwise, a contradiction. Injective representatives exclude `x=y`; hence they are neighbours. Two coarse steps would then produce at most two fine steps, but cell covariance requires displacement `2Le_i`. Thus `L≤1`. □

Attack **C, charge-equivariant decimation**, fails at this joint-spectrum step. This extends the factorwise end-equivariant path obstruction already proved in `ZM1INV.md` Theorem 3.3. The endpoint argument in `ZM1I1A_OWNER_CHECK.md` is a related unrefereed full-algebra argument. Neither result excludes invariant-only maps without a full-algebra charge-equivariant extension.

## 4. Freezing and remaining constraints

**Theorem 7 (CF: central freezing).** Let `t=min(5,m₁)` and `Π_X=[Q_X=5+6t]`. Then `Π_X` is central in `𝔄₁^G`; `a↦Π_Xa` is a local `*`-homomorphism onto `Π_X𝔄₁^G`. On its range, matter at `X` is full and each of its six end numbers is `t`. For neighbouring sites `X,Y`, `Π_XΠ_Y=0`.

*Proof.* `Q_X` generates the central `U(1)` subgroup of the local gauge group, so invariant elements commute with it and its spectral projections. Since `Q_X` itself is invariant, `Π_X` is central. Multiplication by a central projection is a `*`-homomorphism, with support enlarged only by the star. The sum `N_X+∑p_{ℓ,X}` reaches its maximum only when each term is maximal. On a shared link, both ends cannot equal `t`, since `2t>m₁` for `1≤m₁≤9`. □

This is a coarse-side freezing tool. No compatible fine defect pattern or faithful realization is constructed. Every K-INV-E map must satisfy Theorems 3 and 5, the shared-support bound already proved in `ZM1INV.md` R6, and the exclusion of class J in Theorem 6. These conditions do not establish existence or nonexistence.

The fine character helps through covariance in Theorem 2. Character composition without covariance was already used in `ZM1INV.md` R5 and does not exclude K-INV because the coarse invariant algebra has characters, including odd `m₁` (`GB1Z2L5.md` Theorem 2). `GB1Z2L5.md` Theorem 5 already excludes global invertible `a,b` with `ab=λba`, `λ≠1`, in these algebras. This alone gives no further obstruction: the coarse algebra also has a character. The invariant algebra need not be abelian: `GB1Z2L5.md` Theorem 8 already constructs non-unital `M₂` corners. Ordered `K₀` is a possible nonlocal route; no classification or embedding test is verified here.

## 5. Existing work, readings and limits

`prior/KINV.md` records the relevant source search. In addition to the results cited above, `ZM1.md` Theorem Z0 already gives exact regrouping with larger content; `ZM1I1A.md` RC-6 gives a finite-group one-dimensional refinement analogue; `docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` records coherent even-algebra refinement in a one-dimensional free model (ledger unaudited); and `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` records a level-matched 2+1-dimensional Z₃ isometry (author statements for review). Their domains and status are those recorded in the digest. An isometry gives `a↦VaV*` with unit `VV*`, so does not itself supply a unital global K-INV map. The digest also records state- and energy-adapted refinements, finite-region Peter–Weyl approximation and H-BLOCK; none supplies this embedding. These external reference-tree files were not reopened in this pass.

The pass-1 literature record in `KINV_DRAFT.md` §2 reports abstract-level searches, including Brothier–Stottmeister on gauge refinements, Morinelli and coauthors on wavelets, and Po and coauthors on lattice homotopy. It distinguishes fetched abstracts from search-only entries. They are context, not proof inputs; no novelty claim follows from that search.

**Readings.** R-V, R-NC and R-ALL remain proposed and not adopted, with the prior pass-1 checks `P P P P`, `C P F P`, and `P F P C`, respectively (`ZM1INV.md` §5). The translation-only alternative **R-TR** is recorded, not proposed: the draft's four tests are `P P C P`; it would remove the rotation premise of Theorem 2, and the odd coarse character is translation invariant. A coarse rotation composed with particle-hole at `m₁=5` is likewise not proposed; the draft assessed its test 4 as F. These are assessments, not owner decisions or independent checks.

**Scope of negative claims.** Theorem 2 rules out all maps satisfying its exact unitality and specified rotation covariance hypotheses, not all possible zoom definitions. Theorem 5 rules out one completion mechanism, and Theorem 6 rules out class J. The older neutral matrix, end-equivariant path and representative-end attacks have the distinct scopes in `ZM1INV.md` Theorems 3.2–3.6. Their failures do not exhaust invariant-only embeddings. A steelman for the open even case is a unital, covariant, exponentially local invariant-only embedding that handles all defect configurations compatibly without a character filler or a representative-site charge map; its terminal obligation is an explicit faithful, globally compatible map with the stated locality. No N1–N8 packet or independent referee is claimed in this pass. Charged sectors still need a separate bridge; the one-step kinematic map does not supply a continuum limit, speed or controlled trajectory.
