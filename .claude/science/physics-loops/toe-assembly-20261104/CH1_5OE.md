# CH1-5O-E: invariant comparisons and frozen orbits

**FINISH: FROZEN 2026-11-06 after pass 3 (CH1_5OE_REFEREE.md); the referee's edits are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment.

**Status.** The stabilizer and representation result (Theorem 2), the finite-graph frozen-orbit construction, the subgroup dimension bound and singular frozen link marginal (Corollary 4.1), the polynomial projector identities and the stated Gaussian formulas are proved below under their stated hypotheses. The state-extension result is conditional on the cited conditional expectation and exactness results. **GAP:** inclusion of the frozen measures in a named comparison class, and the universal exclusion claimed for R-Esym, are not established by a coupling label alone. **GAP:** the proposed R-E′ has classes that are not pinned; the Gaussian calculation does not establish their separation. **Open:** CH1-5O-E; CH1-5O-E′; the R-A residual; inherited, unchanged: CH1-5O-i, CH1-5U-i, AM, AM-5, CH1-i, CH1-ii, CG1-i, CG1-ii, CG1K-loc, CG1K-H, LW1-5-BG, LW1-5-X, GA1-P-5, Y2-W[`L5-O`], VC1, the formulation of IR and AM (`CH1.md` Definition 8), and the requests T0-start[G] for `Spin(10)` and for the factors of a candidate group. Pass 3 done (CH1_5OE_REFEREE.md); edits applied; ready to freeze. This is not an amendment or an adopted reading. Both laws remain live.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af1d-e133-77b2-95ad-be04cbc4ec86`. Distilled from `CH1_5OE_DRAFT.md`, pass 1 by Claude Opus 5.5; pass 2 model: gpt-6.1-terra; effort and session ID: not visible. Checkout HEAD at read: `481fcd124d2716b82d60634a95149f70e9836e84`. Draft SHA-256: `2c2ff5dfaf0c3868610a55eda2189e177df358259f05a19e77bbab07a090ac3d`. Frozen `CH1_5O.md` SHA-256: `053f1ecf4da057b46eaf70b0c0cb4ac9c6629898a125f6bc959016bb1ccd95e3`. The two source files, not the moving branch name, identify the arguments examined. The pass-1 numerical checks are reported as such; they were not independently rerun.

**Editing provenance.** Codex gpt-6.1-terra, effort high, codex-cli 0.165.0, session `01a1af45-ed49-7750-9660-d7c29d53d7a6`. Source before editing: SHA-256 `5a5c94d11637ac93fbf26ced1c286e277ee6f8a2acd5711de4ede2fce2b7383c`.

The imported referee closures R1–R6 are unrefereed.

Standard mathematics cited, not rebuilt: existence and invariance of Haar measure; the Peter-Weyl theorem; the descending chain condition for closed subgroups of a compact Lie group (sketched in Theorem 2); measure zero of `C^1` images of lower-dimensional manifolds. Literature context, credited from memory and never load-bearing: Fröhlich, Morchio and Strocchi, and 't Hooft (gauge-invariant composites; the orbit construction of Theorem 3); Fradkin and Shenker, and Osterwalder and Seiler (complementarity); the `Spin(10)` decomposition `10 ⊗ 16 = 16̄ ⊕ 144`.

## 1. Definitions inferred by the distiller

1. `G = Spin(10)`. `H` is the image of a Case I embedding with charges `(a,b)` on `C^3 ⊕ C^2`. The CH1-5O-E choice has even `a` and coprime `a,b`, hence `b ≠ 0`. A closed `K` is a candidate if `H ⊆ K ⊊ G`. The Lie-algebra inner product is `⟨X,Y⟩ = −tr_10(XY)/2`.
2. `A` is the quasi-local algebra of a fixed `L5-O` update `α`; `A^G` is the subalgebra fixed by all local gauge transformations. `E:A→A^G` is the gauge average. Cell lifts are `β_s`. A stationary state obeys `ω∘α=ω`; cell symmetry means `ω∘β_s=ω`. We use the cited hypotheses that `E` is a conditional expectation, commutes with `α,β_s`, and fixes every gauge-invariant state. These are inputs, not proved from the axioms here.
3. On a finite oriented graph `(S,L)`, the gauge action of `K^S` on `K^L` is `(k·u)_{xy}=k_xu_{xy}k_y^{-1}`. A `K`-gauge measure is a gauge-invariant probability measure. A `G` gauge-Higgs measure on `G^L × W^S` is invariant under `(U,φ)↦(g·U,σ(g)φ)`. It is frozen at `v∈W` when `φ_x∈Gv` and `σ(U_{xy})φ_y=φ_x` on every link.
4. A normalized Wilson loop is `w_{ρ,C}(U)=tr ρ(U_C)/dim ρ`, for a finite-dimensional `G` representation `ρ`. Its standard identification on a subgroup uses the same trace formula restricted to that subgroup. Products in the comparison have length at most two, including adjoints.
5. The frozen specification CH1-5O-E fixes in advance `D=(r,Λ_r,ι,ι′,C(K),C(G),g_*,δ)` and an inclusion `j` with `ι=ι′∘j`; `Λ_r` includes vector plaquettes. Clause (a) asks for a `C(K)` measure matching the listed products within `δ`; (b) no `C(G)` measure matches the same list under `ι′` within `δ`. `C(K)` is a gauge-Higgs class with coupling at most `g_*`. Normalizations, nonvacuity, maps and classes are open specifications. A finite comparison does not by itself establish uniqueness, full CG1K-H, or chirality.
6. **Proposed readings, none adopted.** R-Esym allows gauge-Higgs models on both sides, with gauge coupling at most `g_*`, Higgs couplings unbounded, and contents otherwise unpinned. R-Esym-F is the class that contains the frozen orbit extensions of the models being compared by definition. R-Easym allows such models only on the `K` side. R-E′ proposes pure-gauge T0-start small-field classes for both sides, standard loop identifications, simple-factor couplings and an abelian clause. The intended T0-start class requires a Haar density and further conditions, including reflection positivity. Its non-simple extension, normalization, existence and precise admissibility remain to be pinned. R-E′ takes the zero Higgs representation on both sides. By Definition 3 these measures are gauge-Higgs measures. So R-E′ instantiates the frozen specification if a gauge-Higgs comparison class may have `W = 0`; the frozen text does not say, and the owner may specify.
7. A covariant matrix `Φ∈M_d(B)` over a unital `*`-algebra with action `κ` satisfies `κ_g(Φ)=R(g)^T Φ R(g)` for a real orthogonal representation `R`. Its entries need not commute. For distinct complex `λ_j`, put `q(t)=∏_j(t−λ_j)` and `P_j(t)=∏_{i≠j}(t−λ_i)/(λ_j−λ_i)`.

## 2. Exact gauge invariance and invariant data

**Theorem 1 (conditional state extension).** Under Definition 2, restriction bijects stationary, gauge-invariant states of `A` with stationary states of `A^G`; the inverse is `φ↦φ∘E`. The same holds with cell symmetry. If the hypotheses of `CH1_5O.md` Theorems 1, 2, 3, 5, 6 and 7 (draft Lemma G, Theorem E, Corollary IR, Theorem L, Corollaries L.2 and L.4) hold for these states, adjoining their conclusions does not change this state set. For `O∈A^G`, its GNS vector `π(O)Ω` is fixed by the implemented global gauge group and has only the trivial `H` type.

*Proof.* `E` fixes `A^G`, and a gauge-invariant state equals its composition with `E`. Thus restriction and extension are inverse. Commutation of `E` with `α` and `β_s` preserves stationarity and cell symmetry in both directions. The cited exactness conclusions hold for every state satisfying their hypotheses. Finally `U(g)π(O)Ω=π(κ_g O)Ω=π(O)Ω`. □

The theorem does **not** prove that exactness can never imply a restriction on invariant correlations: a property could hold for every stationary state of `A^G`. It does show that merely appending the cited exactness conclusions to those hypotheses adds no restriction, and that the fixed-frame representation of `π(O)Ω` alone does not supply a same-scale exotic. CH1-5O-E comparisons use invariant data; R-E′ uses only loops. The definition of a colour-exotic type in `CH1_5O.md` Definition 4 also includes the gluon octet, so its appearance alone is not a fermion obstruction.

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

**Corollary 3.1 (conditional symmetric-class obstruction; R1).** (referee closure, CH1_5OE_REFEREE.md) Fix the data `D` of Definition 5 and a candidate `K`. Let `μ` be a probability measure on `K^L × W_1^S`, invariant under `k·(u, η) = (k·u, (σ_1(k_x)η_x)_x)`. Here `(W_1, σ_1)` is a finite-dimensional unitary `K` representation, and `W_1 = 0` is allowed. Take `(W, σ, v)` with `Stab(v) = K` (Theorem 2(i)). Take a `K`-equivariant isometry `J: W_1 → W_2` into a finite-dimensional unitary `G` representation `(W_2, σ_2)` (Theorem 2(ii)). Let `ν` be the law of `(g·u, (σ(g_x)v)_x, (σ_2(g_x)Jη_x)_x)` under `μ ⊗ m^{⊗S}`, and put `j_v(u, η) = (u, v̄, (Jη_x)_x)`. Assume:

- (C1) `ν ∈ 𝒞(G)`;
- (C2) for every `O ∈ Λ_r`, `ι′(O)` is a Borel function on `G^L × W^S × W_2^S`, invariant under the `G` gauge action; every listed product `ι′(O_1)ι′(O_2)` is `ν`-integrable; and `ι′(O)∘j_v = ι(O)` holds `μ`-almost everywhere.

If `μ` meets the bounds of (a), then `ν` meets them under `ι′`, so (b) fails. For lists of loops with the standard identification, (C2) holds for every `v`.

*Proof.* `ν` is gauge invariant: `h·(g·u, σ(g)v̄, σ_2(g)Jη) = ((hg)·u, σ(hg)v̄, σ_2(hg)Jη)`, and `m^{⊗S}` is invariant under `g ↦ hg`. The sampled point equals `g·j_v(u, η)`. Let `F` be a listed product `ι′(O_1)ι′(O_2)`, or a single `ι′(O_1)`. `F` and `|F|` are gauge invariant, so `F(g·j_v(u, η)) = F(j_v(u, η))`. Tonelli on `|F|` and then Fubini give
`E_νF = ∫∫F(g·j_v(u, η)) dm^{⊗S}(g) dμ(u, η) = ∫F(j_v(u, η)) dμ(u, η) = E_μ(ι(O_1)ι(O_2))`,
using (C2) on each factor. Hence `|ω(O) − E_ν(ι′O)| = |ω(O) − E_μ(ιO)| ≤ δ` for every listed product. By (C1), `ν` is a measure of `𝒞(G)` that meets the bounds, so (b) fails. For loops, `ι′(O) = w_{ρ,C}` depends only on the links, and `j_v` keeps the links `u`, so `ι′(O)∘j_v = w_{ρ,C}|_{K^L} = ι(O)`. ∎

This includes R-Esym only when its definition actually guarantees that closure. R-Esym-F guarantees (C1) by definition; (C2) must also hold.

**GAP in pass 1.** The inference “unbounded Higgs couplings, therefore `ν∈C(G)` at coupling ≤ `g_*`” does not follow without an action, a definition of coupling, and an admissibility/closure proof. Nor does an arbitrarily chosen extension of an observable satisfy a separately fixed `ι′`; the fixed inclusion condition must be checked. Thus the unconditional assertion that *every* pinned R-Esym instance is false is not proved. R-Esym-F has the corollary's obstruction by premise when the compatibility condition (C2) also holds.

**R2 (no frozen extension has a density; refutes the draft's step in GAP A).** Let `λ` be a σ-finite Borel measure on the Higgs space `Y`, for example Lebesgue measure on `W ⊕ W_2`, or an invariant measure on a fixed-length orbit. Let `𝒞_ac(G)` be any class of gauge-Higgs measures on `G^L × Y^S`, each with a density with respect to `m^{⊗L} ⊗ λ^{⊗S}`. Every Gibbs measure `Z^{−1}e^{−A} d(m^{⊗L} ⊗ λ^{⊗S})` with `0 < Z < ∞` is of this kind, at every finite value of every coupling in the action `A`. Let `K` be a candidate, and let the graph satisfy `12|L| > 45|S|`. Then no measure `ν` built as in R1 lies in `𝒞_ac(G)`.

(referee closure, CH1_5OE_REFEREE.md)

*Proof.* Suppose `ν` has a density `f`. By Tonelli its link marginal has the density `∫f dλ^{⊗S}` with respect to `m^{⊗L}`, so it gives measure zero to every `m^{⊗L}`-null set. The link marginal of `ν` is the law of `g·u`. It is concentrated on the image of `K^L × G^S` under `(u, g) ↦ g·u`. That image is compact, hence Borel, and it is `m^{⊗L}`-null by Corollary 4.1, since `|L| dim K + 45|S| ≤ 33|L| + 45|S| < 45|L|`. So the marginal gives a null set measure one, a contradiction. ∎

`𝒞_ac(G)` is a hypothesis of R2, not a proposed class, so it needs no four-test check.

**R6 (one plaquette coefficient on all factors, at quadratic order; supports GAP A).** Let `ρ_1, …, ρ_k` be finite-dimensional unitary `G` representations and `β_1, …, β_k` real. Put `s(U) = Σ_iβ_i(1 − Re w_{ρ_i}(U))`. Then `s(exp X) = c⟨X, X⟩ + O(|X|^4)`, with `c = Σ_iβ_ic_{ρ_i}/(2d_{ρ_i})`. For a fixed-length Higgs hopping term, `|σ(exp X)v − v|^2 = |dσ(X)v|^2 + O(|X|^3)`, and `dσ(X)v = 0` for `X ∈ 𝔨 = Lie(Stab v)`.

(referee closure, CH1_5OE_REFEREE.md)

*Proof.* `tr ρ(exp X) = Σ_{n≥0}tr(dρ(X)^n)/n!`. The `n = 1` term vanishes, since `so(10)` is perfect (section 5). `dρ(X)^3` is anti-Hermitian, so its trace is imaginary and drops out of the real part. `tr dρ(X)^2 = −c_ρ⟨X, X⟩` by Theorem 7. Hence `1 − Re w_ρ(exp X) = c_ρ⟨X, X⟩/(2d_ρ) + O(|X|^4)`. For the hopping term, `σ(exp X)v − v = dσ(X)v + O(|X|^2)`. If `X ∈ 𝔨`, then `σ(exp tX)v = v` for all `t`, so `dσ(X)v = 0`. ∎

Consequence. In unitary gauge the frozen set is `K^L × {v̄}`. There every hopping term vanishes, since `σ(u_ℓ)v = v`, and `s(u_p)` has the quadratic form `c⟨X_p, X_p⟩` on `𝔨`. So the restriction of an action made of such plaquette and hopping terms to the frozen set has one coefficient on every simple or abelian factor of `𝔨`. In the stipulated Gaussian model it gives one variance on `𝔨`, so `N_eff = dim K`. A witness `μ` with different couplings on different factors has a different action on `K^L`. Writing its frozen extension as an action of this kind needs further terms, for example Higgs-dependent plaquette terms. A pinned R-Esym class must say whether their coefficients are gauge couplings bounded by `g_*`. R6 is exact for quadratic forms; it proves nothing about measures outside the model.

**Corollary 3.2 (conditional one-sided ambiguity).** If `K″⊆K` is closed and `C(K)` contains the frozen `K` extensions of a `K″`-gauge model, its invariant loop expectations can match that model even when `K″` does not contain `H`.

*Proof.* Apply Theorem 3 with `(G,K)` replaced by `(K,K″)` and use the restricted standard loop maps. □

This includes the trivial `K″`. It does not show that every possible `C(K)` admits the extension, or that (a) holds without an actual matching state and tolerance.

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

**R5 (exact projectors on finite registers; supports items 35, 50 and 53).** Let `𝒦` be finite dimensional, `𝔅 ⊆ B(𝒦)` a unital `*`-subalgebra, and `Φ ∈ M_d(𝔅)` with `Φ^* = −Φ`. Let `λ_1, …, λ_m` be the distinct eigenvalues of `Φ` as an operator on `C^d ⊗ 𝒦`. They are imaginary; `q(Φ) = 0` for `q(t) = Π_j(t − λ_j)`; and the `P_j(Φ)` of Theorem 5 are the spectral projections of `Φ`.

(referee closure, CH1_5OE_REFEREE.md)

*Proof.* The map `Φ ↦ Σ_{ab}E_{ab} ⊗ Φ_{ab}` from `M_d(𝔅)` to `B(C^d ⊗ 𝒦)` is an injective `*`-homomorphism. So the image of `Φ` is anti-Hermitian, hence normal with imaginary eigenvalues, and it is unitarily diagonalizable (spectral theorem, cited). `q(Φ)` vanishes on every eigenspace, so it is `0`; by injectivity `q(Φ) = 0` in `M_d(𝔅)`. On the `λ_k`-eigenspace, `P_j(Φ)` acts as `P_j(λ_k) = δ_{jk}`. ∎

So at finite size the hypothesis `q(Φ) = 0` always holds for some `q`. What a finite composite controls is its spectrum. That is the stopping point of B4 as distilled.

**Theorem 6 (one-site matter adjoint).** For ten Hermitian Majoranas `{γ_a,γ_b}=2δ_ab` on `C^32`, let `M_aa=0`, `M_ab=(i/2)γ_aγ_b` for `a≠b`. Then
\[
 M^2=4iM-\tfrac94 I,\quad P_{9i/2}=\tfrac1{10}(γ_aγ_b)_{ab}=ΓΓ^*/10,\quad P_{-i/2}=I-P_{9i/2},\quad Γψ=\sum_a e_a⊗γ_aψ.
\]
The ranks are 32 and 288; both ranges are invariant under the diagonal action.

*Proof.* On a diagonal entry of `M²` the nine terms sum to `−9/4`; off diagonal the eight terms sum to `−2γ_aγ_b=4iM_ab`. The roots are `9i/2` and `−i/2`. Since `Γ*Γ=10I`, `ΓΓ*/10` is a rank-32 projection. The complementary rank is 320−32. Covariance and Theorem 5 give invariance. □

The 32-dimensional channel is the range of `Γ`; the 288-dimensional channel is the kernel of Clifford multiplication `Γ^*: e_a ⊗ ψ ↦ γ_aψ`. The draft's labels `16̄⊕144` and conjugates are representation-theory context credited from memory, not proved here. The pass-1 scratch check reports zero residual and eigenvalue multiplicities 32 and 288; this is not an independent check.

**GAP in pass 1.** The assertion that a classical Case I orbit always has four distinct eigenvalues `±ia,±ib` and ranks 3,3,2,2 needs `a,b≠0` and `a≠±b`. For example `(a,b)=(0,1)` is coprime with even `a`; the zero eigenspace has rank 6, not two separate rank-3 eigenspaces. Even with distinct roots, one-site spectral channels do not by themselves establish the dynamical large-block stabilizer channels. A small polynomial residual in a state alone also does not prove a mass gap or an effective group.

**R3 (eigenvalues of `ψ(Y)`; repairs GAP C).** Let `(a, b)` be coprime with `a` even. Then `b` is odd, so `b ≠ 0` and `a ≠ ±b`. On `C^{10}` the operator `ψ(Y)` has the eigenvalues `ia` and `−ia` (multiplicity 3 each) and `ib` and `−ib` (multiplicity 2 each). These are four distinct values if and only if `a ≠ 0`. If `a = 0`, then `b = ±1`, and the eigenvalues are `0` (multiplicity 6) and `±i` (multiplicity 2 each).

(referee closure, CH1_5OE_REFEREE.md)

*Proof.* If `b` were even, 2 would divide `gcd(a, b) = 1`. An even `a` differs from `±b` when `b` is odd. Write `C^{10} = V ⊕ V̄`, the `±i` eigenspaces of the complex structure, with `V = C^3 ⊕ C^2`. On `V`, `ψ(Y) = ia·1_3 ⊕ ib·1_2`. On `V̄` it is the complex conjugate, `−ia·1_3 ⊕ −ib·1_2`. Now `ia = −ia` only if `a = 0`; `ib ≠ −ib` since `b ≠ 0`; and `±ia ≠ ±ib` since `a ≠ ±b`. If `a = 0`, then `|b| = gcd(0, b) = 1`. ∎ [check]: for `(0, 1)` the imaginary parts `−1, 0, 1` occur 2, 6 and 2 times; for `(−2, 3)`, `(2, 3)`, `(2, 1)`, `(4, 1)` and `(2, 5)` there are four values, two of them occurring 3 times and two occurring 2 times.

## 5. Gaussian small-field calculation

Fix a closed `K ⊆ G` (a candidate, or `G` itself), an orthonormal basis `T_A` of its `n`-dimensional Lie algebra, positive numbers `σ_A²`, and a positive semidefinite path matrix `D`. Let centered jointly Gaussian `X_C^A` have covariance `δ_AB σ_A²D(C,C′)`. Set `X_C=Σ_A X_C^AT_A` and, for a `G` representation `ρ` of dimension `d_ρ`, define the **second-order loop variable** `w_{ρ,C}=1+tr(dρ(X_C)^2)/(2d_ρ)`. This model is a stipulated Gaussian truncation, not a proved approximation to a T0-start measure.

**Theorem 7 (Gaussian count).** Put `S_1=Σ_Aσ_A²`, `S_2=Σ_Aσ_A⁴` and `N_eff=S_1²/S_2`. For `c_ρ≥0` defined by `tr(dρ(X)dρ(Y))=−c_ρ⟨X,Y⟩` on `so(10)`,
\[
 E w_{ρ,C}-1=-\frac{c_ρ}{2d_ρ}D(C,C)S_1,\qquad
 \operatorname{Cov}(w_{ρ,C},w_{ρ',C'})=\frac{c_ρc_{ρ'}}{2d_ρd_{ρ'}}D(C,C')^2S_2.
\]
When the denominator is nonzero, the covariance divided by the product of the two mean shifts is `2r²/N_eff`, where `r=D(C,C′)/sqrt(D(C,C)D(C′,C′))`. `N_eff≤n`, with equality iff all variances agree. For an `Ad(G)`-invariant covariance on `G`, `N_eff=45`. For a candidate `K`, `N_eff≤33`. Matching the means with the full-group model by `σ′²=S_1/45` multiplies its covariance by `N_eff/45` relative to the subgroup model.

*Proof.* The invariant trace form is a nonpositive scalar multiple of `⟨,⟩` by simplicity of `so(10)`; `c_10=2`. Expanding the square gives the mean. Wick's fourth-moment identity gives `Cov((X_C^A)^2,(X_C′^B)^2)=2δ_AB σ_A⁴D(C,C′)^2`, giving the covariance. Cauchy–Schwarz gives `S_1²≤nS_2`, with the stated equality condition. Invariance and simplicity force the full-group covariance to be scalar. Theorem 4 supplies the bound for `K`. Substitution of `σ′²=S_1/45` proves the last statement. □

For the vector representation the linear trace vanishes, as it does for every representation of the perfect algebra `so(10)`. The calculation concerns the defined quadratic variables. It does not prove equality of exact Wilson-loop means, nor separation of general T0-start classes. Nonlinear terms, differing propagators, zero covariance, the chosen list, and comparison errors matter. The draft reports a floating-point Gram check (`c_10=2`, `c_45=16`) and a 400,000-sample check, `0.1930` versus `0.1926`, for its selected variances; these are pass-1 reports, not reruns or proofs. The order-`g^4` signal is conditional on variances scaling as `g²` and on nonzero `D(C,C′)`. No quantitative bound on `δ` for the actual classes follows without remainder and normalization bounds.

**R4 (the self-correlation ratio does not depend on the propagator; repairs GAP B(iii) inside the model).** In the model of `CH1_5OE.md` section 5, let `ρ` be nontrivial and `D(C, C) > 0`. Then `Var(w_{ρ,C})/(E w_{ρ,C} − 1)^2 = 2/N_eff`. The ratio does not depend on `D`, on `ρ`, or on a common rescaling of the `σ_A^2`. It equals `2/45 ≈ 0.044` for every `Ad(G)`-invariant model on `G`. It is at least `2/33 ≈ 0.061` for every model on a candidate `K`.

(referee closure, CH1_5OE_REFEREE.md)

*Proof.* Theorem 7 with `C′ = C` gives `r = 1`. The quotient `S_1^2/S_2` is unchanged by `σ_A^2 ↦ tσ_A^2`. Theorem 7 gives `N_eff = 45` for an `Ad(G)`-invariant covariance, and `N_eff ≤ dim K ≤ 33` for a candidate. ∎

So inside the model, a `G`-model and a candidate model with the same means differ in the variance of each single loop, whatever propagators they use. The "differing propagators" mentioned above matter only for pairs with `r < 1`. Both `E(W^*W)` and `E(W)` are compared data when `W ∈ Λ_r`. The model stays stipulated; R4 says nothing about T0-start classes.

## 6. Proposed readings and attacks

The four tests are: (1) fixes a target, (2) open-ended, (3) settles downstream physics by premise, (4) adds unneeded structure or constants. These are assessments, not owner decisions.

| Reading | Pass-1 check | Distiller's check |
|---|---|---|
| R-Esym / R-Esym-F | 1 pass; 2, 3, 4 fail; reject (R-Esym) | Test 3 fails for R-Esym-F by Corollary 3.1 when (C2) holds. Unbounded couplings alone do not prove closure for R-Esym. Tests 2 and 4 depend on how the class is fixed and justified. |
| R-Easym | 1, 2, 4 fail; 3 conditional; reject | Corollary 3.2 gives the proposed ambiguity when closure and maps hold. It does not prove that every pinned one-sided class fails. |
| R-E′ | All four pass once data are pinned; proposed | Unresolved. Pinning is not yet done; whether pure gauge is admissible in frozen CH1-5O-E turns on the `W = 0` reading. Singularity excludes the particular frozen marginal, while the Gaussian model alone does not establish separation of the full classes. Necessity of removing Higgs fields and tests 1, 3, 4 remain judgments requiring a specified class. |

**CH1-5O-E′ (proposed, open).** For fixed `r`, `Λ_r`, standard maps, nonempty precisely defined pure-gauge small-field classes and `δ`, ask for an `L5-O` update and a stationary, cell-symmetric gauge-invariant state, Case I `H` with even `a`, and candidate `K`, such that (a′) some `K`-class measure meets the bounds of (a), and (b′) no `G`-class measure meets those bounds. This is an existence version. Even a proof would not identify the state supplied by VC1. T0-start[G] is a request, not a result. A product prescription for non-simple groups, disconnected components and abelian factors needs its own definition and checks.

Pass-1 attacks, with corrected stopping points:

- **B1**, transfer fixed-frame exotic types through relational channels: Theorem 1 fixes the type of an invariant channel vector; Theorem 5 preserves exact projectors when `q(Φ)=0`. No stated bridge transfers the fixed-frame field obstruction to the requested invariant correlators. This does not prove that all such correlators are unconstrained.
- **B2**, use frozen complementarity to defeat (b): succeeds for an orbit-closed symmetric class with compatible maps. For R-E′, the exhibited frozen marginal is singular on large windows, so it is not itself a Haar-density member. Whether another admissible measure matches is open.
- **B3**, one-point Gaussian blindness: the comparison also includes products. Theorem 7 distinguishes the two stipulated Gaussian models through connected products when the correlation and resolution are nonzero. It does not settle general (b′).
- **B4**, construct an effective subgroup from a one-site FMS composite: Theorem 6 supplies exact diagonal-action channels of ranks 32 and 288, not a proof of the desired dynamical stabilizer channels. Gauge averaging makes a nontrivial covariant one-point function vanish. A large-block orbit, coset mass and weak subgroup sector remain to be demonstrated. This example does not exclude all finite composites.

The earlier attacks **A1–A4** remain as in frozen `CH1_5O.md`: A1 lacks a bridge from the effective group to the GNS global action; A2's allowed centre-containing stabilizers do not produce a state; A3's exact finite-register obstruction does not exclude approximate coarse-grained fields; A4's lift stabilizer is not an invariant diagnostic and its comparison exclusion is conditional. None establishes a named failure of either law.

## 7. Open obligations and routes

**CH1-5O-E** remains the frozen open specification in Definition 5. A witness needs both bounds for the same pinned data. A disproof at fixed data must cover its stated update and state quantifiers. **CH1-5O-E′** is the proposed pure-gauge variant above. A possible route uses a block covariant composite near a specified orbit, a coset mass, a weak subgroup sector and controlled comparison errors. It needs the relevant plaquette and weak-coupling constructions and comparison classes; these are route dependencies, not proven necessary conditions for all formulations. A small quantum-link model and the Gaussian ratio are proposed guides, not proofs.

The following names remain open: **CH1-5O-i**, **CH1-5U-i**, **AM**, **AM-5**, **CH1-i**, **CH1-ii**, **CG1-i**, **CG1-ii**, **CG1K-loc**, **CG1K-H**, **LW1-5-BG**, **LW1-5-X**, **GA1-P-5**, **Y2-W[`L5-O`]**, **VC1**, the formulation of **IR** and **AM** (`CH1.md` Definition 8), and **T0-start[G]** for `Spin(10)` and the relevant subgroup factors. The **R-A residual** in frozen `CH1_5O.md` also remains open under that reading. The inherited open items are not closed by a finite correlation match. No amendment to frozen CH1 is made here.
