# CH1-5O-E: invariant comparisons and frozen orbits

**Status.** The finite-graph frozen-orbit construction, the subgroup dimension bound, the polynomial projector identities and the stated Gaussian formulas are proved below under their stated hypotheses. The state-extension result is conditional on the cited conditional expectation and exactness results. **GAP:** inclusion of the frozen measures in a named comparison class, and the universal exclusion claimed for R-Esym, are not established by a coupling label alone. **GAP:** the proposed R-E′ changes the frozen gauge-Higgs specification and its classes are not pinned; the Gaussian calculation does not establish their separation. **Open:** CH1-5O-E, CH1-5O-E′ and the inherited items in §7. This is pass 2, not a referee verdict, an amendment, or an adopted reading. Both laws remain live.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af1d-e133-77b2-95ad-be04cbc4ec86`. Distilled from `CH1_5OE_DRAFT.md`, pass 1 by Claude Opus 5.5; pass 2 model: gpt-6.1-terra; effort and session ID: not visible. Checkout HEAD at read: `481fcd124d2716b82d60634a95149f70e9836e84`. Draft SHA-256: `2c2ff5dfaf0c3868610a55eda2189e177df358259f05a19e77bbab07a090ac3d`. Frozen `CH1_5O.md` SHA-256: `053f1ecf4da057b46eaf70b0c0cb4ac9c6629898a125f6bc959016bb1ccd95e3`. The two source files, not the moving branch name, identify the arguments examined. The pass-1 numerical checks are reported as such; they were not independently rerun.

## 1. Definitions inferred by the distiller

1. `G = Spin(10)`. `H` is the image of a Case I embedding with charges `(a,b)` on `C^3 ⊕ C^2`. The CH1-5O-E choice has even `a` and coprime `a,b`, hence `b ≠ 0`. A closed `K` is a candidate if `H ⊆ K ⊊ G`. The Lie-algebra inner product is `⟨X,Y⟩ = −tr_10(XY)/2`.
2. `A` is the quasi-local algebra of a fixed `L5-O` update `α`; `A^G` is the subalgebra fixed by all local gauge transformations. `E:A→A^G` is the gauge average. Cell lifts are `β_s`. A stationary state obeys `ω∘α=ω`; cell symmetry means `ω∘β_s=ω`. We use the cited hypotheses that `E` is a conditional expectation, commutes with `α,β_s`, and fixes every gauge-invariant state. These are inputs, not proved from the axioms here.
3. On a finite oriented graph `(S,L)`, the gauge action of `K^S` on `K^L` is `(k·u)_{xy}=k_xu_{xy}k_y^{-1}`. A `K`-gauge measure is a gauge-invariant probability measure. A `G` gauge-Higgs measure on `G^L × W^S` is invariant under `(U,φ)↦(g·U,σ(g)φ)`. It is frozen at `v∈W` when `φ_x∈Gv` and `σ(U_{xy})φ_y=φ_x` on every link.
4. A normalized Wilson loop is `w_{ρ,C}(U)=tr ρ(U_C)/dim ρ`, for a finite-dimensional `G` representation `ρ`. Its standard identification on a subgroup uses the same trace formula restricted to that subgroup. Products in the comparison have length at most two, including adjoints.
5. The frozen specification CH1-5O-E fixes in advance `D=(r,Λ_r,ι,ι′,C(K),C(G),g_*,δ)` and an inclusion `j` with `ι=ι′∘j`; `Λ_r` includes vector plaquettes. Clause (a) asks for a `C(K)` measure matching the listed products within `δ`; (b) excludes all `C(G)` measures. `C(K)` is a gauge-Higgs class. Normalizations, nonvacuity, maps and classes are open specifications. A finite comparison does not by itself establish uniqueness, full CG1K-H, or chirality.
6. **Proposed readings, none adopted.** R-Esym allows gauge-Higgs models on both sides, with no bound on Higgs couplings and explicitly includes the frozen orbit extensions of the models being compared. R-Easym allows such models only on the `K` side. R-E′ proposes pure-gauge T0-start small-field classes for both sides, standard loop identifications, simple-factor couplings and an abelian clause. The intended T0-start class requires a Haar density and further conditions, including reflection positivity. Its non-simple extension, normalization, existence and precise admissibility remain to be pinned. R-E′ removes the gauge-Higgs requirement of the frozen specification; it is a proposed change, not an already valid instantiation.
7. A covariant matrix `Φ∈M_d(B)` over a unital `*`-algebra with action `κ` satisfies `κ_g(Φ)=R(g)^T Φ R(g)` for a real orthogonal representation `R`. Its entries need not commute. For distinct complex `λ_j`, put `q(t)=∏_j(t−λ_j)` and `P_j(t)=∏_{i≠j}(t−λ_i)/(λ_j−λ_i)`.

## 2. Exact gauge invariance and invariant data

**Theorem 1 (conditional state extension).** Under Definition 2, restriction bijects stationary, gauge-invariant states of `A` with stationary states of `A^G`; the inverse is `φ↦φ∘E`. The same holds with cell symmetry. If the hypotheses of `CH1_5O.md` Lemma G, Theorem E, Theorem L and Corollaries L.2, L.4 and IR hold for these states, adjoining their conclusions does not change this state set. For `O∈A^G`, its GNS vector `π(O)Ω` is fixed by the implemented global gauge group and has only the trivial `H` type.

*Proof.* `E` fixes `A^G`, and a gauge-invariant state equals its composition with `E`. Thus restriction and extension are inverse. Commutation of `E` with `α` and `β_s` preserves stationarity and cell symmetry in both directions. The cited exactness conclusions hold for every state satisfying their hypotheses. Finally `U(g)π(O)Ω=π(κ_g O)Ω=π(O)Ω`. □

The theorem does **not** prove that exactness can never imply a restriction on invariant correlations: a property could hold for every stationary state of `A^G`. It does show that merely appending the cited exactness conclusions to those hypotheses adds no restriction, and that the fixed-frame representation of `π(O)Ω` alone does not supply a same-scale exotic. CH1-5O-E comparisons use invariant data; R-E′ uses only loops. The definition of exotic in the draft also includes the gluon octet, so its appearance alone is not a fermion obstruction.

A frozen invariant measure has the analogous vanishing of a covariant one-point function with no singlet: its expectation is an invariant vector, hence zero by group averaging. This does not identify the classical model with an `L5-O` state or establish all the quantum theorem's analogues.

## 3. Frozen complementarity

**Theorem 2 (stabilizer and representation).** For a compact Lie group `G` and closed `K`, (i) some finite-dimensional unitary `G` representation has a vector with stabilizer exactly `K`; (ii) every finite-dimensional unitary `K` representation embeds `K`-equivariantly and isometrically in the restriction of a finite-dimensional unitary `G` representation.

*Proof.* (i) For each `g∉K`, a continuous function on `G/K` separates `gK` from `K`. Approximate its pullback uniformly by matrix coefficients and average on the right over `K`. The result is `K`-fixed but not `g`-fixed, in a finite-dimensional right-translation representation. Finite intersections of these stabilizers have a minimal member: closed subgroups of a compact Lie group satisfy the descending chain condition, since dimension cannot decrease indefinitely and, at fixed identity component, the finite component group cannot decrease indefinitely. That minimal intersection is exactly `K`. Take the direct sum of its finitely many representations and vectors.

(ii) Let `V` be the `K` representation and consider continuous `f:G→V` with `f(xk)=k^{-1}f(x)`, acted on by left translation. Evaluation at the identity is `K`-equivariant and onto: average `χ(xk)kw` over `K`, with `χ` concentrated near the identity on `K`. Peter–Weyl approximation followed by the equivariance average makes the left-translation-finite functions dense. Select finitely many whose evaluations span `V`; their orbit span is a finite-dimensional `G` representation with equivariant evaluation onto `V`. Its adjoint, normalized by `(ev ev*)^{-1/2}`, is the desired isometry. □

**Theorem 3 (frozen orbit).** Let `K=Stab(v)⊆G`, let `μ` be a `K`-gauge measure on a finite graph, and draw independent Haar `g_x∈G`. Set `U_{xy}=g_xu_{xy}g_y^{-1}` and `φ_x=σ(g_x)v`. Their law `ν` is a frozen `G` gauge-Higgs measure, with link marginal `μ̃`. For any bounded invariant Borel function `F` on the relevant configuration space,
\[
 E_{\tilde μ}F=E_μ F(u),\qquad E_νF=E_μ F(u,\bar v).
\]
Every continuous `K`-gauge-invariant function on `K^L` has a unique continuous invariant extension to the frozen set, restricting to the original function at `(u, v̄)`.

*Proof.* Haar invariance under `g_x↦h_xg_x` gives gauge invariance. Since `u_{xy}v=v`, the frozen link relation holds. The expectation identities follow because `(U,φ)=g·(u,v̄)`. Every frozen configuration is gauge equivalent to `(u,v̄)` for some `u∈K^L`. The possible choices of `g` differ by `K^S`, so a `K`-invariant function defines a unique invariant extension. The map from the compact space of `(U,g)` with `g^{-1}·U∈K^L` to the frozen set is a continuous surjection onto a Hausdorff space and hence a quotient map; the extension is continuous. □

**Corollary 3.1 (conditional symmetric-class obstruction).** If every `μ∈C(K)` that can witness (a) has an orbit extension `ν∈C(G)` and the fixed maps satisfy `ι=ι′∘j` on the support, then (a) implies the failure of (b). This includes R-Esym only when its definition actually guarantees that closure.

*Proof.* The fixed identification and Theorem 3 give identical expectations of each listed product. The same error bounds hold for `ν`. For `K`-Higgs fields, Theorem 2(ii) embeds their representation into a `G` representation and the same orbit argument applies. □

**GAP in pass 1.** The inference “unbounded Higgs couplings, therefore `ν∈C(G)` at coupling ≤ `g_*`” does not follow without an action, a definition of coupling, and an admissibility/closure proof. Nor does an arbitrarily chosen extension of an observable satisfy a separately fixed `ι′`; the fixed inclusion condition must be checked. Thus the unconditional assertion that *every* pinned R-Esym instance is false is not proved. An R-Esym class defined to contain these extensions has the corollary's obstruction by premise.

**Corollary 3.2 (conditional one-sided ambiguity).** If `J⊆K` is closed and `C(K)` contains the frozen `K` extensions of a `J`-gauge model, its invariant loop expectations can match that model even when `J` does not contain `H`.

*Proof.* Apply Theorem 3 with `(G,K)` replaced by `(K,J)` and use the restricted standard loop maps. □

This includes the trivial `J`. It does not show that every possible `C(K)` admits the extension, or that (a) holds without an actual matching state and tolerance.

**Theorem 4 (dimension bound).** For a candidate `K` in Definition 1, `dim K≤33`.

*Proof.* As a real `H` representation, `so(10)=u(5)⊕p`. The off-diagonal block in `u(5)` contains a 12-dimensional real irreducible `A`, the realification of `(3,2)_{a−b}`; `p` contains a 12-dimensional real irreducible `B`, from `(3,2)_{a+b}`. They are inequivalent because `b≠0` and `3` is not `3̄`; each occurs with multiplicity one. Since `Lie K` is `H`-invariant, its intersection with each is either the whole piece or zero.

If it contains both, `su(3)⊕su(2)⊕A` generates `su(5)`: an off-diagonal bracket has a nonzero traceless block-scalar component, and the other components are already in the generated algebra. The `SU(5)` orbit of nonzero `B` spans `p`, since `p_C=10⊕10̄` is real irreducible. Simplicity of `so(10)` then gives `[p,p]=u(5)` and `Lie K=so(10)`. Connectedness of `G` gives `K=G`, contrary to properness. Thus a proper `K` misses at least one 12-dimensional piece. □

**Corollary 4.1 (singular frozen link marginal).** If a finite four-dimensional block window has `12|L|>45|S|`, the `μ̃` of Theorem 3 for a candidate `K` is singular relative to product Haar measure on `G^L`.

*Proof.* The smooth map `K^L×G^S→G^L` has domain dimension at most `33|L|+45|S|<45|L|`. Its image has Haar measure zero. □

A periodic 4D box has `|L|=4|S|`; sufficiently large cubes also meet the inequality. Hence this frozen marginal cannot be a member of a class requiring a Haar density on that window. Singularity does not rule out a different absolutely continuous measure matching a finite list within `δ`.

## 4. Relational projectors

**Theorem 5 (operator polynomial calculus).** With Definition 7, every `p(Φ)` is covariant and `p(Φ)r(Φ)=(pr)(Φ)`. The polynomials `P_j` sum to one; both `P_jP_k−δ_jkP_j` and `(t−λ_j)P_j` are divisible by `q`. Therefore `q(Φ)=0` gives mutually orthogonal idempotents in the algebraic sense, summing to one. If `Φ* = −Φ` and all `λ_j` are imaginary, they are self-adjoint projections. If `B⊆B(K)` and `κ_g=Ad V(g)`, `Φ` and its polynomial projectors commute with `R(g)⊗V(g)`; their ranges are diagonal-action subrepresentations.

*Proof.* Associativity suffices for polynomial evaluation in one algebra element. Scalar orthogonality gives `p(R^TΦR)=R^Tp(Φ)R`. Lagrange interpolation proves the identities and divisibility. Complex conjugation of coefficients and `Φ* = −Φ` give self-adjointness for imaginary roots. The covariance equation rearranges to `[Φ,R⊗V]=0`, and the same holds for its polynomials. □

For vector-covariant multiplets `ψ,ψ′`, the contraction `Σ_ab ψ_a* P_j(Φ)_ab ψ′_b` is gauge invariant by orthogonality of `R`. Noncommuting entries alone do not spoil projector identities; `q(Φ)=0` is the necessary stated hypothesis for this construction.

**Theorem 6 (one-site matter adjoint).** For ten Hermitian Majoranas `{γ_a,γ_b}=2δ_ab` on `C^32`, let `M_aa=0`, `M_ab=(i/2)γ_aγ_b` for `a≠b`. Then
\[
 M^2=4iM-\tfrac94 I,\quad P_{9i/2}=\tfrac1{10}(γ_aγ_b)_{ab}=ΓΓ^*/10,\quad P_{-i/2}=I-P_{9i/2},\quad Γψ=\sum_a e_a⊗γ_aψ.
\]
The ranks are 32 and 288; both ranges are invariant under the diagonal action.

*Proof.* On a diagonal entry of `M²` the nine terms sum to `−9/4`; off diagonal the eight terms sum to `−2γ_aγ_b=4iM_ab`. The roots are `9i/2` and `−i/2`. Since `Γ*Γ=10I`, `ΓΓ*/10` is a rank-32 projection. The complementary rank is 320−32. Covariance and Theorem 5 give invariance. □

The Clifford multiplication image is the 32-dimensional channel; the other is its kernel. The draft's labels `16̄⊕144` and conjugates are representation-theory context credited from memory, not proved here. The pass-1 scratch check reports zero residual and eigenvalue multiplicities 32 and 288; this is not an independent check.

**GAP in pass 1.** The assertion that a classical Case I orbit always has four distinct eigenvalues `±ia,±ib` and ranks 3,3,2,2 needs `a,b≠0` and `a≠±b`. For example `(a,b)=(0,1)` is coprime with even `a`; the zero eigenspace has rank 6, not two separate rank-3 eigenspaces. Even with distinct roots, one-site spectral channels do not by themselves establish the dynamical large-block stabilizer channels. A small polynomial residual in a state alone also does not prove a mass gap or an effective group.

## 5. Gaussian small-field calculation

Fix a candidate `K`, an orthonormal basis `T_A` of its `n`-dimensional Lie algebra, positive numbers `σ_A²`, and a positive semidefinite path matrix `D`. Let centered jointly Gaussian `X_C^A` have covariance `δ_AB σ_A²D(C,C′)`. Set `X_C=Σ_A X_C^AT_A` and, for a `G` representation `ρ` of dimension `d_ρ`, define the **second-order loop variable** `w_{ρ,C}=1+tr(dρ(X_C)^2)/(2d_ρ)`. This model is a stipulated Gaussian truncation, not a proved approximation to a T0-start measure.

**Theorem 7 (Gaussian count).** Put `S_1=Σ_Aσ_A²`, `S_2=Σ_Aσ_A⁴` and `N_eff=S_1²/S_2`. For `c_ρ≥0` defined by `tr(dρ(X)dρ(Y))=−c_ρ⟨X,Y⟩` on `so(10)`,
\[
 E w_{ρ,C}-1=-\frac{c_ρ}{2d_ρ}D(C,C)S_1,\qquad
 \operatorname{Cov}(w_{ρ,C},w_{ρ',C'})=\frac{c_ρc_{ρ'}}{2d_ρd_{ρ'}}D(C,C')^2S_2.
\]
When the denominator is nonzero, the covariance divided by the product of the two mean shifts is `2r²/N_eff`, where `r=D(C,C′)/sqrt(D(C,C)D(C′,C′))`. `N_eff≤n`, with equality iff all variances agree. For an `Ad(G)`-invariant covariance on `G`, `N_eff=45`. For a candidate `K`, `N_eff≤33`. Matching the means with the full-group model by `σ′²=S_1/45` multiplies its covariance by `N_eff/45` relative to the subgroup model.

*Proof.* The invariant trace form is a nonpositive scalar multiple of `⟨,⟩` by simplicity of `so(10)`; `c_10=2`. Expanding the square gives the mean. Wick's fourth-moment identity gives `Cov((X_C^A)^2,(X_C′^B)^2)=2δ_AB σ_A⁴D(C,C′)^2`, giving the covariance. Cauchy–Schwarz gives `S_1²≤nS_2`, with the stated equality condition. Invariance and simplicity force the full-group covariance to be scalar. Theorem 4 supplies the bound for `K`. Substitution of `σ′²=S_1/45` proves the last statement. □

For the vector representation the linear trace vanishes, as it does for every representation of the perfect algebra `so(10)`. The calculation concerns the defined quadratic variables. It does not prove equality of exact Wilson-loop means, nor separation of general T0-start classes. Nonlinear terms, differing propagators, zero covariance, the chosen list, and comparison errors matter. The draft reports a floating-point Gram check (`c_10=2`, `c_45=16`) and a 400,000-sample check, `0.1930` versus `0.1926`, for its selected variances; these are pass-1 reports, not reruns or proofs. The order-`g^4` signal is conditional on variances scaling as `g²` and on nonzero `D(C,C′)`. No quantitative bound on `δ` for the actual classes follows without remainder and normalization bounds.

## 6. Proposed readings and attacks

The four tests are: (1) fixes a target, (2) open-ended, (3) settles downstream physics by premise, (4) adds unneeded structure or constants. These are assessments, not owner decisions.

| Reading | Pass-1 check | Distiller's check |
|---|---|---|
| R-Esym | 1 pass; 2, 3, 4 fail; reject | Test 3 fails for the explicitly orbit-closed class by Corollary 3.1. Unbounded couplings alone do not prove closure. Tests 2 and 4 depend on how the class is fixed and justified. |
| R-Easym | 1, 2, 4 fail; 3 conditional; reject | Corollary 3.2 gives the proposed ambiguity when closure and maps hold. It does not prove that every pinned one-sided class fails. |
| R-E′ | All four pass once data are pinned; proposed | Unresolved. Pinning is not yet done; pure gauge changes frozen CH1-5O-E. Singularity excludes the particular frozen marginal, while the Gaussian model alone does not establish separation of the full classes. Necessity of removing Higgs fields and tests 1, 3, 4 remain judgments requiring a specified class. |

**CH1-5O-E′ (proposed, open).** For fixed `r`, `Λ_r`, standard maps, nonempty precisely defined pure-gauge small-field classes and `δ`, ask for an `L5-O` update and a stationary, cell-symmetric gauge-invariant state, Case I `H` with even `a`, and candidate `K`, such that some `K`-class measure satisfies (a) and no `G`-class measure satisfies (b). This is an existence version. Even a proof would not identify the state supplied by VC1. T0-start[G] is a request, not a result. A product prescription for non-simple groups, disconnected components and abelian factors needs its own definition and checks.

Pass-1 attacks, with corrected stopping points:

- **B1**, transfer fixed-frame exotic types through relational channels: Theorem 1 fixes the type of an invariant channel vector; Theorem 5 preserves exact projectors when `q(Φ)=0`. No stated bridge transfers the fixed-frame field obstruction to the requested invariant correlators. This does not prove that all such correlators are unconstrained.
- **B2**, use frozen complementarity to defeat (b): succeeds for an orbit-closed symmetric class with compatible maps. For R-E′, the exhibited frozen marginal is singular on large windows, so it is not itself a Haar-density member. Whether another admissible measure matches is open.
- **B3**, one-point Gaussian blindness: the comparison also includes products. Theorem 7 distinguishes the two stipulated Gaussian models through connected products when the correlation and resolution are nonzero. It does not settle general (b′).
- **B4**, construct an effective subgroup from a one-site FMS composite: Theorem 6 supplies exact diagonal-action channels of ranks 32 and 288, not a proof of the desired dynamical stabilizer channels. Gauge averaging makes a nontrivial covariant one-point function vanish. A large-block orbit, coset mass and weak subgroup sector remain to be demonstrated. This example does not exclude all finite composites.

The earlier attacks **A1–A4** remain as in frozen `CH1_5O.md`: A1 lacks a bridge from the effective group to the GNS global action; A2's allowed centre-containing stabilizers do not produce a state; A3's exact finite-register obstruction does not exclude approximate coarse-grained fields; A4's lift stabilizer is not an invariant diagnostic and its comparison exclusion is conditional. None establishes a named failure of either law.

## 7. Open obligations and routes

**CH1-5O-E** remains the frozen open specification in Definition 5. A witness needs both bounds for the same pinned data. A disproof at fixed data must cover its stated update and state quantifiers. **CH1-5O-E′** is the proposed pure-gauge variant above. A possible route uses a block covariant composite near a specified orbit, a coset mass, a weak subgroup sector and controlled comparison errors. It needs the relevant plaquette and weak-coupling constructions and comparison classes; these are route dependencies, not proven necessary conditions for all formulations. A small quantum-link model and the Gaussian ratio are proposed guides, not proofs.

The following names remain open: **CH1-5O-i**, **CH1-5U-i**, **AM-5**, **CH1-i**, **CH1-ii**, **CG1-i**, **CG1-ii**, **CG1K-loc**, **CG1K-H**, **LW1-5-BG**, **LW1-5-X**, **GA1-P-5**, **Y2-W[`L5-O`]**, **VC1**, and **T0-start[G]** for `Spin(10)` and the relevant subgroup factors. The **R-A residual** in frozen `CH1_5O.md` also remains open under that reading. The inherited open items are not closed by a finite correlation match. No amendment to frozen CH1 is made here.
