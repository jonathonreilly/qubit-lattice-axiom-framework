# CH1-5U-q: charged correlations and frozen stars

## 0. Status

**FINISH: FROZEN 2026-11-06 after pass 3 (CH1_5UQ_REFEREE.md); the referee's edits are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment.

This item studies a supplied `L5-U` law. It adopts no law, physical axiom, reading of light, or amendment. CH1-5U-q[𝒫] asks for a stationary gauge- and cell-invariant state and a quasi-local odd field of charge `|q| ≥ 3` with free-Weyl large-distance correlations. The charged-correlator prescription matters.

**Proved, conditional on the stated law and cited local-algebra inputs.** Local Gauss-charge vectors are conserved (Theorem 2.1). Separated local odd fields have zero undressed two-point function at all times; the same excludes Weyl falloff for fields with sufficiently fast norm tails (Theorem 2.2). Frozen-star projectors and a class of operators inside them are conserved by the base tick (Theorem 3.1). For `3 ≤ m ≤ 7` there are exact charge-3 zero modes, for all electric angles if `m` is odd and at zero electric angle if `m` is even (Theorem 3.2). These are static defects, not Weyl particles. For even `m` there is an all-frozen invariant state, pure on the invariant algebra, at filling `m/2` (Theorem 3.3). Electrically diagonal states kill the specified local dressed correlations (Theorem 4.1). A link expectation has norm at most `1/2`, and a simple string in a suitable product state has an exponential bound (Theorem 4.2). A triple-hop operator is nonzero exactly for `3 ≤ m ≤ 7` (Theorem 5.1).

**GAP.** Norm quasi-locality alone supplies no `o(R^-3)` tail. The draft's claim that Corollary G1 decides the original CH1-5U-q as written therefore does not follow. CH1.md already requires a dressing or charge-sector prescription; calling the undressed reading the text's unique literal meaning is not justified. The draft also extends a product bound to repeated-link strings, arbitrary times, arbitrary dressings and states merely separable across links without proof; Theorem 4.2 gives the actual hypotheses. Non-product correlations need not be entanglement. The inference from the proposed L3 to the full original IR hypothesis, and conversely from IR to L3, needs a matching prescription and locality assumptions. The draft's extension to all gauge laws is not proved. RC7 covers laws with the stated local parity-unitary hypotheses, including `L5-U`, `L_cube`, and `L5-O` under its register hypothesis (referee closure, CH1_5UQ_REFEREE.md).

**Open by name.** CH1-5U-q[𝒫], in particular CH1-5U-q[`L3^q`] and its local form CH1-5U-q(L3); the charged-correlator prescription of IR (an owner question); CH1-5U-i; AM-5; CH1-ii; CH1-5O-E and the residual case of reading R-A; VC1-5U-odd; LW1-5U-PS7; Y2-W. No named failing step for `L5-U` follows from the attacks below. L2 is a different proposed question and is answered affirmatively, not an answer to CH1-5U-q.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af02-1d0e-7a61-b94e-9401d7afe267`. Pass 1: `CH1_5UQ_DRAFT.md`, Claude Opus 5.5, whose own date is 2026-11-06. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model, reasoning effort and session ID are not exposed to this session and cannot be verified. Checkout HEAD `193e7169ca47634e008f40deeb71aa739e8c71b0`; draft SHA-256 `ffdae83b1eb076c0d534e645ee058562da095a9d328b27ee1f8955c53014f01d`. Context: `TOE_ASSEMBLY.md` §§3.4–3.5 and CH1 target; `LW1.md`, `CH1.md`, `LIT_SMG.md`. Source-specific dependencies below are provisional draft inputs, not audit verdicts. The draft reports numerical scratch checks; their files were not independently reproduced here. No numerical check is used as proof.

**Editing session provenance.** Codex gpt-6.1-terra, effort high, codex-cli 0.165.0, session `01a1af2a-f8ce-7801-b045-aa622a0cccf4` (model and effort as supplied for this session). Referee closures RC1–RC8 have not been independently checked by another session.

## 1. Definitions inferred by the distiller

1. Sites are `Z³`, with five matter CAR modes `c_{x,k}` per site. Each link has ten rishon CAR modes, five per end, in the fixed-number register `Λ^m(C^10)`, `1 ≤ m ≤ 9`. Different links and matter commute as ordinary tensor factors; matter modes anticommute across sites. Rishons at the two ends of one link anticommute. `N_x` and `p_{ℓ,x}` count matter and end modes; `p_{ℓ,x}+p_{ℓ,y}=m`.
2. For an oriented link `(x,y)`, `U_ℓ^{jk}=r_j^y r_k^{x†}` and `h_ℓ=Σ_{jk} c_{y,j}† U_ℓ^{jk} c_{x,k}+h.c.`. The base tick is `U_0=W_E M_o M_e`, with cube generators `H_C=3^{-1/2}Σ_{ℓ⊂C}η_ℓ h_ℓ`, and `W_E=∏_ℓ exp[-iτ_E(p_{ℓ,src}-m/2)^2]`. An update of `L5-U` form adds finitely many bounded-range layers of gauge-invariant gates. Its automorphism is `α(A)=U*AU`, understood by finite gate products on local `A`.
3. `Q_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}` generates the local central `U(1)`. Gauge invariance means invariance under every local `U(5)` conjugation, not necessarily a Gauss-singlet vector. `G_U` denotes the supplied cell lifts `β_g`. Cell invariance means invariance under those lifts; stationarity means `ω∘α=ω`. `E` denotes the local-gauge averaging conditional expectation onto `𝔄^G`.
4. `S(A)` is the matter sites of a local operator and both ends of every link in its support; `M(A)` is its matter support. A charge vector `q=(q_z)` is defined by `Ad exp(iθQ_z)(A)=exp(iθq_z)A`. Its total is `Σ_z q_z`, equal to matter-number change, called `U(1)_N` charge. Fermion parity concerns matter modes.
5. A quasi-local field is a norm limit of local fields. Where a rate is needed, `ψ_R` is odd, supported in a radius-`R` ball including link ends, and `f(R)=||ψ-ψ_R||`. Spatial copies use the specified lifts; their existence for the chosen positions follows from site transitivity (`LW1_5.md` B1-U).
6. For stationary `ω`, its GNS unitary is `Ũ π(A)Ω=π(α(A))Ω`. Stationarity gives an isometry and surjectivity of `α` gives dense range. Its eigenvalue `e^{-iw}` defines quasi-energy `w` modulo `2π`.
7. **Proposed L1:** the undressed two-point function has a nonzero `r^-3` lower bound along arbitrarily distant pairs, at some times. This is the empty prescription, CH1-5U-q[∅], and only a necessary part of free-Weyl agreement. **Proposed L2(δ):** `ω(ψ*ψ)=1` and `ω((α(ψ)-ψ)*(α(ψ)-ψ))≤δ²`. Equivalently, `‖(Ũ − 1)π(ψ)Ω‖ ≤ δ`; this is not necessarily an eigenstate. **Proposed L3:** for a local odd `ψ`, a fixed integer time `n`, pairs `(x_i,y_i)` with `|x_i − y_i| → ∞`, and local dressings `D_i` with `||D_i||≤1` and `[D_i,N_z]=0` for every `z`, the bilocal `ψ_{x_i}*D_i α^n(ψ_{y_i})` is gauge invariant and its expectation has modulus at least `c|x_i-y_i|^-3` for fixed `c>0`. Full free-Weyl tensor structure is an additional requirement. These are proposals; none is adopted. Norm control prevents arbitrary rescaling; the matter-number condition excludes dressings that themselves transfer matter.
8. A state is electrically diagonal if it is invariant under every `Ad exp(iθp_{ℓ,z})`. A basis vector is flavour-locked at `x` if the occupied flavour sets of matter at `x` and of each of its six adjacent link ends agree.

The cited law and symmetry inputs are `LW1_5.md` Theorem U, Z-U and B1-U, and `VC1_5.md` Theorems 2.1 and 2.2. These supply finite-support gauge averaging and cell lifts; B1-U supplies their commutation with the base tick. The results below do not promote those inputs to retained status.

## 2. Static local charges

**Theorem 2.1 (draft Lemma 1.2).** The `Q_z` commute and have integer spectra. Every local operator has a finite decomposition into charge-vector components supported in `S(A)`. If it is odd, every component has odd total charge. It also decomposes into definite changes of all local matter and end numbers, with total matter change equal to total charge. Every `L5-U`-form update preserves each charge vector.

*Proof.* Number operators on different matter or rishon modes commute, including the two ends of a link. Fourier projection under the finite torus generated by the relevant `Q_z` gives a finite decomposition. A charge outside `S(A)` acts trivially. Refining by the commuting matter and end numbers gives the second decomposition. On each link the two end-number changes sum to zero, hence `ΣδQ_z=ΣδN_z`. Matter parity is `(-1)^{ΣδN_z}`. Each gate commutes with `Q_z`, so `α` commutes with its conjugation, including for negative times. □

**Theorem 2.2 (draft Lemma G and Corollary G1).** For a gauge-invariant state, local `A,B` and any integer `n`,
\[
\omega(B^*\alpha^n(A))=\sum_q\omega(B_q^*\alpha^n(A_q)).
\]
If `S(A)` and `S(B)` are disjoint and all components of `A` have nonzero total charge, this expectation is zero. For an odd quasi-local `ψ` as in Definition 5 and `|x-y|>2R`,
\[
|\omega(\psi_y^*\alpha^n(\psi_x))|\le (2\|\psi\|+f(R))f(R).
\]
If `f(R)=o(R^-3)`, the correlator is `o(|x-y|^-3)`, uniformly in `n`. Thus L1 fails for these fields at every charge.

*Proof.* Gauge invariance kills a component of nonzero local charge. Theorem 2.1 makes `B_{q'}*α^n(A_q)` have charge `q-q'`, proving the sum. Disjoint support forces a matching vector to vanish, contrary to the hypothesis. For the norm limit, subtract the local correlator, which is zero, and apply `||α^n||=1`, `||ψ_R||≤||ψ||+f(R)`. Choose `R` proportional to `|x-y|` and strictly less than half of it. □

The theorem needs neither stationarity nor cell invariance beyond the use of translates. **GAP:** a norm tail can decay arbitrarily slowly. It does not establish the asserted conclusion for all quasi-local operators. The draft's L1 test-3 judgment is conditional on the faster tail and on taking undressed correlations as the reading. `CH1.md`, inferred definition 8, states: “Charged correlators require a gauge-covariant dressing or a charge-sector prescription.” RC1 shows the `o(R^-3)` hypothesis is sharp: at `O(R^-3)` the L1 lower bound can arise from self-overlap without dynamics; full free-Weyl agreement remains undecided (referee closure, CH1_5UQ_REFEREE.md).

## 3. Frozen stars and spectral modes

For `ℓ∋x` define the auxiliary operator `φ_{ℓ,x}=Σ_k r_k^{ℓ,x†}c_{x,k}` on the full matter-rishon Fock space. It changes the register number, but the products below preserve it. Define
\[
K_x=\sum_{\ell\ni x}(\phi_{\ell,x}^*\phi_{\ell,x}+\phi_{\ell,x}\phi_{\ell,x}^*),\quad
F_x=\ker K_x,\quad P_x=\Pi_{F_x}.
\]

**Theorem 3.1 (draft Lemma F1 and Theorem Z0).** `K_x` and `P_x` are local, even, gauge invariant, commute with `N_x` and every adjacent end number, and `F_x` is the common kernel of all `φ_{ℓ,x}` and `φ_{ℓ,x}*`. Every flavour-locked basis vector lies in `F_x`. For `ℓ=(x,y)`,
\[
h_\ell=\phi_{\ell,y}^*\phi_{\ell,x}+\phi_{\ell,x}^*\phi_{\ell,y},\quad
[\phi_{\ell,x},\phi_{\ell,y}]=[\phi_{\ell,x},\phi_{\ell,y}^*]=0,
\]
and `h_ℓP_x=P_xh_ℓ=0`. The base tick conserves `P_x`. It also conserves any `Y=P_xYP_x` supported on the matter at `x` and its six registers, if `Y` commutes with their electric gates. These conclusions hold for every allowed `m` and all base-tick constants, with no added plaquette gates.

*Proof.* Each summand of `K_x` is positive and preserves both end numbers and matter number. The gauge actions on `r†` and `c` contract to the invariant `φ`; spectral calculus gives the claims for `P_x`. A sum of squared norms identifies its kernel. Two exchanges, one of matter modes and one of rishon modes, establish the commutators, and expansion gives `h_ℓ`. Each term then kills `F_x`. In a locked vector each term of `φ` or `φ*` is blocked by occupancy.

Split each cube generator into its links incident on `x` and the rest. The first part kills `P_x` on both sides; the second is even and disjoint from the star. Thus each cube gate commutes with `P_x` and, on its range, acts as the gate with incident hops removed. Electric gates commute with `P_x`. The remaining cube gates and electric gates away from the star commute with `Y`; the adjacent electric gates commute by hypothesis. Hence the entire tick commutes with `Y`. □

**Theorem 3.2 (draft Theorem Z and Corollary Z1).** For `m=3,…,7`, set `n₀=(m-3)/2` for odd `m`, and `n₀=max(0,m-5)` for even `m`. Let the six neighbours of `x` be `y_s` and their links `ℓ_s`. Put
\[
X=c_{x,1}^\dagger c_{x,2}^\dagger c_{x,3}^\dagger \prod_{s=1}^6
r^{\ell_s,x\dagger}_1r^{\ell_s,x\dagger}_2r^{\ell_s,x\dagger}_3
r^{\ell_s,y_s}_3r^{\ell_s,y_s}_2r^{\ell_s,y_s}_1,\quad
\Pi=\prod_s\Pi[p_{\ell_s,x}=n_0],\quad \Psi=P_xX\Pi P_x.
\]
`Ψ` is nonzero, local and odd, with local charges `21` at `x` and `-3` at each `y_s`, hence total charge `3`. The base tick fixes it for any electric angle if `m` is odd, and for `τ_E=0` if `m` is even. In the tracial state its normalized GNS vector is a charge-3 exact zero-quasi-energy excitation. Its adjoint gives charge `-3`. Gauge transforms and cell lifts of `Ψ` are also fixed; its finite-dimensional gauge orbit span contains an irreducible multiplet of fixed odd charge-3 operators.

*Proof.* Each adjacent link factor transfers three rishons from `y_s` to `x`; the matter factor creates three at `x`. `P_x` and `Π` commute with all `Q_z`, giving the charges. Pick `S⊂{4,5}` of size `n₀`, put matter `S` and each `x`-end `S`, and choose each opposite end to contain `{1,2,3}` with size `m-n₀`. Both the input and its nonzero image under `X` are locked, so `Ψ` is nonzero. The relevant end number goes from `n₀` to `n₀+3`. For odd `m` these values are symmetric about `m/2`, so their electric phases agree; for even `m` they agree at `τ_E=0`. If `x` is the target, the electric factor is a function of `m − p_{ℓ,x}`, and `(m − p − m/2)^2 = (p − m/2)^2`. Theorem 3.1 applies. The local normalized trace is faithful and is preserved by local automorphisms, the tick, gauge transformations and cell lifts. Thus `τ(Ψ*Ψ)>0` and `Ũπ(Ψ)Ω=π(Ψ)Ω`. Gauge and cell covariance of the base tick (`LW1_5.md` B1-U) gives the orbit statements; finite-dimensional compact-group complete reducibility gives a summand. □

Consequently the proposed CH1-5U-q(L2(δ)) holds for all `δ≥0`, for the listed laws. The same construction with all five flavours, `m=5`, `n₀=0`, gives charge `±5`; the same proof with one flavour gives charge `±1` for odd `m` at any electric angle, and even `m` at `τ_E=0`. Products of three separated charge-one modes also give charge three, but represent three separated operators. These single-star examples disprove a universal spectral exclusion at charges `±3` and `±5`; by themselves they do not disprove an exclusion at every other individual charge. RC6 shows that the draft’s existential spectral schema is vacuous at even `q`; restricted to odd `q`, products of separated charge-one modes provide witnesses at every odd charge and every `m` under the specified electric angles (referee closure, CH1_5UQ_REFEREE.md). These products represent separated objects.

For `m∈{1,2,8,9}`, the end-number range has width at most two, so this locked three-unit end move is impossible. The zero modes are pinned: Theorem 2.2 kills their separated undressed correlations and Theorem 3.1 gives `h_ℓP_x=P_xh_ℓ=0` for incident hops. As `LIT_SMG.md` §9 warns, “Existence of an operator with the right charge does not establish a particle pole, residue or mass.”

**Theorem 3.3 (draft Corollary F2).** For even `m=2n`, `n=1,…,4`, choose a flavour set `A_x` of size `n` at each site and occupy it in the matter and all six link ends at `x`. Let `Φ` be the resulting product state and `ω_F=Φ∘E`. Then `ω_F` is stationary under the base tick, gauge invariant, cell invariant, independent of the choices `A_x`, and pure on `𝔄^G`. It has `N_x=n` and `Q_x=7n` sharply.

*Proof.* The end occupancies sum to `2n=m` on each link. Every hop kills the locked vector and electric gates act by phases, so `Φ` is stationary on local observables. Gauge averaging commutes with the base tick and cell lifts. Independent site flavour permutations map any choice of sets to any other and disappear after `E`; the lifted cell maps carry locked vectors to locked vectors, up to phases. Thus `ω_F` is cell invariant and choice independent.

For purity, fix a finite site set `S` containing the support and both ends of its links. Project onto `N_x=n` for `x∈S` and end number `n` on all incident links. The projected sector factors into site spaces `W_x=Λ^n(C^5)⊗(Λ^n(C^5))^{⊗6}` and outside ends. In each `W_x` the gauge Cartan operators `H_{x,j}=n_{x,j}+Σ_{ℓ∋x}n^{ℓ,x}_j` have joint eigenvalues 7 for `j∈A_x` and 0 otherwise. These eigenvalues force each of the seven occupied sets to be `A_x`, so the joint eigenspace is one-dimensional. By the finite-dimensional invariant-algebra purity lemma and the local-to-infinite sector lemma, `VC1_5.md` Theorem 3.1(b)–(c), the restriction to `𝔄^G` is pure. The sharp-number statements are immediate. □

This agrees with the conditional relation `Q_x-3m=n` in `VC1_5.md` Theorem 5.3. The state is electrically diagonal; every hop annihilates the underlying product vector and the electric layer acts on it by a phase. The draft also invokes PS-3h5 and `VC1_5.md` Corollary 5.6 to infer a tick-1 record from sharp `N_x`; that downstream record claim remains conditional on those inputs, which are not checked here.

## 4. Dressed correlations

**Theorem 4.1 (draft Lemma E and Corollary E1).** A gauge-invariant electrically diagonal state is invariant under each `Ad exp(iθN_z)`. If local odd `ψ`, local `D` with `[D,N_z]=0` for all `z`, and integer `n` satisfy `M(ψ_x)∩M(α^n(ψ_y))=∅`, then
\[
\omega(\psi_x^*D\alpha^n(\psi_y))=0.
\]
Consequently no such local field meets proposed L3 in an electrically diagonal state. The tracial state, the `ω_t`, `ω_m` and full-matter partner states of `VC1_5.md` Theorems 5.2 and 5.5, and the state `ω_F` of Theorem 3.3 are electrically diagonal and do not meet L3.

*Proof.* `exp(iθN_z)=exp(iθQ_z)∏_{ℓ∋z}exp(-iθp_{ℓ,z})`; all factors commute and their adjoint actions preserve the state. Decompose the fields into definite local matter-number changes. Each component of `ψ_x` has an odd, hence nonzero, total matter change supported in `M(ψ_x)`. The other field has no matter change there, and `D` has none anywhere. Invariance under a site-number phase kills each term. Finite-range dynamics keeps `α^n(ψ_y)` local at each fixed `n`, so its matter support is disjoint from `M(ψ_x)` for sufficiently distant pairs. The tracial and `ω_t` register states are traces. The other named states are gauge averages of end-number eigenvector states; end numbers are gauge invariant, so their phase actions commute with `E` and preserve these states. □

The conclusion covers the listed states, not every stationary invariant state on file in an unspecified corpus. For L3 it assumes a fixed time and a local field. RC2 extends the conclusion to number-diagonal states, including the odd-`m` ice limits of `VC1_5.md` R4; in gauge-invariant states the required coherence is of a site number or equivalently a star end number. RC3 supplies the quasi-local estimate for `o(R^-3)` tails and norm-bounded local dressings at fixed time (referee closure, CH1_5UQ_REFEREE.md).

**Theorem 4.2 (draft Lemma W2′ and Corollary W2′.1).** For any state `λ` on one register, the matrices `u_{jk}=λ(U^{jk})` and `v_{jk}=λ(U^{jk*})` obey `||u||,||v||≤1/2`. The bound is attained at `m=5`. Let `γ` be a path of `L` distinct links from `y` to `x`, let `T_i` be the oriented transport matrix (`U` or `U†` with transposed indices), and define
\[
B_\gamma=\sum_{jk}c_{x,j}^\dagger(T_L\cdots T_1)_{jk}c_{y,k}.
\]
If the restriction of `ω` to endpoint matter and these registers is `μ⊗λ_1⊗⋯⊗λ_L`, then `|ω(B_γ)|≤5·2^{-L}`.

*Proof.* For `X²=0`, write a unit vector `a+b` with `a∈ker X`, `b⊥ker X`. Since `ran X⊂ker X`, `|⟨a+b,X(a+b)⟩|≤||X||||a||||b||≤||X||/2`. Mixed states follow by convexity. For unit `a,b∈C^5`, the matrix element `a*u b` is the expectation of `X=(Σ_j \bar a_j r_j^y)(Σ_k b_k r_k^{x†})`. It has square zero and norm at most one. The same argument applies to the adjoint matrix. At `m=5`, occupy the five orthonormal orbitals `(r_j^{y†}+Σ_k V_{kj}r_k^{x†})/√2`; the link expectation has singular values `1/2`.

For a path with `L` distinct links the expectation factors into the endpoint matter matrix `M_{jk}=μ(c_{x,j}†c_{y,k})` and `t_L⋯t_1`, with `t_i=λ_i(T_i)`. CAR and Cauchy–Schwarz give `||M||≤1`, so `||M||_1≤5`. Matrix Hölder and the first bound give the result. □

**GAP in the draft's generalization.** A path that repeats a link gives expectations of products in that one register, not products of one-link expectations. A product restriction on the link registers alone does not imply factorization from endpoint matter. At nonzero time `α^n(c_y)` can involve further registers, so the displayed bound does not directly apply. Nor does failure of product form imply quantum entanglement: mixtures of product states are a counterexample to that inference. RC4 gives a one-link counterexample with `ω(B_γ)=9/2 > 5/2` despite product form over the link registers. RC5 extends the bound to the closed convex hull of full products and shows that exceeding it forces entanglement across endpoint matter and the registers, not necessarily within the link sector (referee closure, CH1_5UQ_REFEREE.md). It addresses this particular charge-one string, not all norm-bounded dressings, arbitrary charge, or a general perimeter law.

## 5. Triple hop and failed routes

**Theorem 5.1 (draft Lemma T).** For an oriented link `(x,y)`, let `A_ℓ=φ_{ℓ,y}*φ_{ℓ,x}` and `T_ℓ=A_ℓ³`. It is gauge invariant, moves three matter units from `x` to `y` and three rishons in the opposite direction, and is nonzero exactly when `3≤m≤7`.

*Proof.* The two endpoint `φ` operators commute, so `T_ℓ=(φ_{ℓ,y}*)³(φ_{ℓ,x})³`. Gauge invariance follows from the invariant contractions. The allowed values of `p_{ℓ,x}` are `max(0,m-5),…,min(5,m)`. Their width is at least three exactly for `3≤m≤7`; otherwise the operator, which raises `p_{ℓ,x}` by three, vanishes. In that range choose matter `{1,2,3}` at `x`, none at `y`, an `x`-end set `S⊂{4,5}` of size `max(0,m-5)`, and a `y`-end set of size `min(m,5)` containing `{1,2,3}`. The six permutations in `(φ_x)³` have the same sign after both CAR reorderings, and yield a nonzero vector. Applying `(φ_y*)³` gives nonzero mutually orthogonal terms for different three-flavour subsets of the occupied `y`-end. Thus no cancellation occurs. □

This refutes, for `3 ≤ m ≤ 7`, the proposed step that one link cannot carry a triple. It is an algebraic hopping matrix element, not proof of a mobile isolated charge-3 particle or a long-distance phase. The draft reports a scratch check of matrix entries `36` for `m=3,…,7` and zero otherwise; it was not reproduced here.

The proposed light-cone exclusion fails at the step from finite propagation support to a charge-dependent spectral or correlation bound: the same support radius applies to each charge, and Theorem 3.2 gives a static zero mode inside it. This does not establish that every conceivable use of locality is charge blind. The proposed spectral exclusion fails at charges `±3` and `±5`, as above. The pinned-charge argument proves the undressed theorem, but gives no obstruction when a gauge-invariant dressing cancels the local charge vector.

For proposed CH1-5U-q(L3), the draft tried three routes to existence: (P1) the auxiliary c-number quasi-free tick has elementary charge `±1` modes and is not the interacting tick (`CH1_5U.md` Theorem 2.2, GAP Q1′ and R2; `LW1_5.md` inferred definition 4); (P2) the charge-3 zero mode is static and its tracial state is electrically diagonal; (P3) the states named in RC2, including the odd-`m` ice limits, are number-diagonal, and the specified fully factorized strings obey Theorem 4.2 and RC5 (referee closure, CH1_5UQ_REFEREE.md). It tried three routes to exclusion: (R1) a support cone, (R2) the finite-register capacity, and (R3) the spectral bound. The preceding results identify where each stated route stops. Failed routes do not prove the open claim or its negation.

`CH1_5U.md` Theorem 2.2 gives `|u|≥3` for its `10_u`. If CH1-5U-i supplies a local `10_u` field satisfying exactly the L3 prescription, with all other required hypotheses, then it implies CH1-5U-q(L3); its negation would refute that correspondingly strengthened version of CH1-5U-i. **GAP:** the original IR field is quasi-local and its charged-correlator prescription is not fixed to L3. The implication as written needs those additional matches. CH1-5U-q(L3) itself is an existence question with full Weyl tensor structure in addition to the L3 lower bound. With the quasi-local prescription `L3^q`, RC8 gives CH1-5U-i[`L3^q`] ⇒ CH1-5U-q[`L3^q`] and CH1-5U-q(L3) ⇒ CH1-5U-q[`L3^q`]; CH1-5U-q[𝒫] remains open (referee closure, CH1_5UQ_REFEREE.md).

## 6. Proposed readings and four-test results

The draft's tests ask whether an item (1) fixes a part's target, (2) is “open-ended, so a part can add to it”, (3) settles downstream physics by premise, and (4) adds unnecessary structure or constants. These are author-side judgments, not mathematical verdicts. No reading is adopted.

| Proposed item | Draft's check | Distiller's qualification |
|---|---|---|
| L1, undressed | 1 pass; 2 pass; 3 fails; 4 pass | Theorem 2.2 proves the obstruction for local or fast-tail fields. RC1 shows an `O(R^-3)` tail can meet the lower bound by self-overlap without dynamics; full Weyl agreement remains open. RC7 gives the stated extension to other laws under its parity-unitary hypotheses. L1 is the empty prescription CH1-5U-q[∅] (referee closure, CH1_5UQ_REFEREE.md). |
| L2(δ), spectral | 1–4 pass; witness in Theorem 3.2 | A different, weaker question. A pinned defect meets it; it does not decide IR or CH1-5U-i. |
| L3, bounded, matter-number-preserving dressing | 1, 2, 4 pass; 3 conditional because a choice of dressing may exclude phases of interest | The draft calls this a working reading, but it remains proposed. Its requirements and fixed time are extra choices; sufficiency for the intended Weyl or charge-sector physics is open. The referee rates test 4 conditional: full gauge invariance of the bilocal is stronger than Theorem 2.2 forces (`CH1_5UQ_REFEREE.md` §4). |
| Frozen space `F_x` | 1–4 pass | A definition from the supplied law; Theorem 3.1 proves its properties for the base tick. |
| CH1-5U-q[𝒫], including CH1-5U-q[`L3^q`] and CH1-5U-q(L3) | 1–4 pass for CH1-5U-q(L3) as an open question | RC8 gives the matched quasi-local implication; the local form needs the stated locality match (referee closure, CH1_5UQ_REFEREE.md). |

A free Weyl field has an equal-time two-point function with `r^-3` scale as used in the draft; this physical input is not derived here. Elitzur, Dirac, Buchholz, Fröhlich–Morchio–Strocchi, Lieb–Robinson and the SMG literature are context, not premises for the algebraic proofs. The `1/2` link-expectation bound does not by itself show that every gauge-invariant observable fails to approximate a group-valued link at larger scales. Y2-W and the needed state and scaling-limit questions remain open.

## 7. Referee closures

The following arguments are imported from the referee report; no other session has checked them. References to draft line numbers in these closures identify the referee’s sources.

### 7.1 RC1: the tail hypothesis of Theorem 2.2 is sharp (referee closure, CH1_5UQ_REFEREE.md)

**RC1.** Take any `m`, any update of `L5-U` form, and `q ∈ {1, 3}`. Let `B = c^†_{0,1}⋯c^†_{0,q}` at the base site `0`. For `v ∈ 2Z^3` let `B_v = β_{t_v}(B)`, with `t_v` the translation by `v`; by the lift formula (`VC1_5.md` Theorem 2.2) `B_v = ±c^†_{v,1}⋯c^†_{v,q}`. Put
\[
\psi=B_0+\sum_{k\ge1}2^{-3k}B_{2^ke_1}.
\]
(a) `ψ` is quasi-local and fermion odd. Each partial sum has definite total `U(1)_N` charge `q`. With `ψ_R` the partial sum over `2^k ≤ R`, `ψ_R` is odd, lies in the ball of radius `R`, and `f(R) ≤ (8/7)R^{−3}`.
(b) For `x ∈ 2Z^3`, `K ≥ 1` and `y = x + 2^Ke_1`, the translates `ψ_x = β_{t_x}(ψ)`, `ψ_y = β_{t_y}(ψ)` obey
\[
|\tau(\psi_y^*\psi_x)|\ \ge\ \tfrac{63}{64}\,2^{-q}\,|x-y|^{-3}.
\]
So `ψ` meets the lower-bound clause of proposed L1 (definition 7) at time `0`, at charge 3 and at charge 1. The hypothesis `f(R) = o(R^{−3})` of Theorem 2.2 cannot be weakened to `f(R) = O(R^{−3})`.

*Proof.* (a) `‖B_v‖ = 1` and `Σ_k 2^{−3k} < ∞`, so the series converges in norm. Each term is odd and has total charge `q`. Let `2^{k_0}` be the least power of two above `R`. The tail has norm at most `Σ_{k≥k_0}2^{−3k} = (8/7)2^{−3k_0} < (8/7)R^{−3}`.
(b) Lifts compose up to site sign automorphisms (`VC1_5.md` Theorem 2.2), so `β_{t_x}(B_v) = ±B_{x+v}`. Hence `ψ_x = Σ_u a_x(u)B_u` with `|a_x(x)| = 1`, `|a_x(x + 2^ke_1)| = 2^{−3k}` for `k ≥ 1`, and `a_x(u) = 0` otherwise. For `u ≠ w`, `τ(B_u^*B_w) = 0`: the unitary `(−1)^{N_u}` is even and acts on the matter at `u` only, so it conjugates `B_u^*` to `−B_u^*` and fixes `B_w`, and `τ` is invariant under inner automorphisms. For `u = w`, `τ(B_u^*B_u) = τ(∏_{i≤q}(1 − n_{u,i})) = 2^{−q}`. The double series converges absolutely, so `τ(ψ_y^*ψ_x) = 2^{−q}Σ_u\overline{a_y(u)}a_x(u)`. Both coefficients are nonzero at exactly two sites. At `u = y` the moduli are `1` and `2^{−3K}`. At `u = y + 2^Ke_1 = x + 2^{K+1}e_1` they are `2^{−3K}` and `2^{−3K−3}`. No other site qualifies: `2^K + 2^k` is a power of two only for `k = K`, and `x` is not of the form `y + 2^ke_1`. So `|τ(ψ_y^*ψ_x)| ≥ 2^{−q}2^{−3K}(1 − 2^{−3K−3}) ≥ (63/64)2^{−q}|x − y|^{−3}`. ∎

The correlation is the overlap of the field's own tail with its translate. No dynamics enters. So the lower-bound clause of L1 does not detect propagation once tails are `O(R^{−3})`. Whether such a field can match the full free-Weyl correlation is not examined.

### 7.2 RC2: Theorem 4.1 needs only number-diagonality (referee closure, CH1_5UQ_REFEREE.md)

Call a state `ω` *number-diagonal* if `ω∘Ad e^{iθN_z} = ω` for every site `z` and every real `θ`. (Four tests: a property of states defined from the law's own operators; it fixes no target, is closed, settles nothing by premise and adds nothing; it is used here as a hypothesis, not proposed as a reading.)

**RC2.** (a) The conclusion of Theorem 4.1 holds for every number-diagonal `ω`, gauge invariant or not: if `ψ` is local and odd, `D` local with `[D, N_z] = 0` for every `z`, and `M(ψ_x) ∩ M(α^n(ψ_y)) = ∅`, then `ω(ψ_x^*Dα^n(ψ_y)) = 0`.
(b) `ω` is number-diagonal in each of these cases: (i) `ω` is gauge invariant and invariant under each `Ad e^{iθP_z}`, with `P_z = Σ_{ℓ∋z}p_{ℓ,z}`; gauge-invariant electrically diagonal states are a special case; (ii) every `N_z` is sharp in `ω`; (iii) on each finite region `ω` has a density that commutes with every `N_z`.
(c) So no local odd field meets proposed L3 in `τ`, in the states `ω_t` (`VC1_5.md` Theorem 5.2), in the two witnesses of `VC1_5.md` Theorem 5.5, in `ω_F` of Theorem 3.3, or in the odd-`m` ice limits `ω∘E` of `VC1_5.md` R4. R4(d) reads: "`Q_x = 3m` and `N_x = 0` on every `|c⟩`; both are gauge invariant, so both are sharp in `ω∘E`." The ice vectors are superpositions of different end-number assignments. Neither R4 nor `CH1_5UQ.md` shows these limits electrically diagonal, so Theorem 4.1 as stated does not reach them; (b)(ii) does.
(d) For a gauge-invariant `ω`, number-diagonality at `z` is equivalent to invariance under `Ad e^{iθP_z}`. So the coherence that L3 needs (local field, fixed `n`) is coherence of some site number `N_z`, equivalently of some star end number `P_z`. Coherence of single end numbers `p_{ℓ,z}` does not suffice while `ω` stays invariant under every `Ad e^{iθP_z}`.

*Proof.* (a) The proof of Theorem 4.1, after its first sentence, uses only invariance under each `Ad e^{iθN_z}`. (b)(i) `e^{iθN_z} = e^{iθQ_z}e^{−iθP_z}`, a product of commuting unitaries. `Q_z` generates the centre of `U(5)_z`, so gauge invariance gives invariance under `Ad e^{iθQ_z}`. Electric diagonality gives invariance under each `Ad e^{−iθp_{ℓ,z}}`, hence under `Ad e^{−iθP_z}`. (ii) In the GNS triple `(H, π, Ω)`, `ω((N_z − n_z)^2) = 0` gives `π(N_z)Ω = n_zΩ`. So `π(e^{−iθN_z})Ω = e^{−iθn_z}Ω`, and `ω(e^{iθN_z}Ae^{−iθN_z}) = ⟨π(e^{−iθN_z})Ω, π(A)π(e^{−iθN_z})Ω⟩ = ω(A)`. (iii) On a finite region `F` containing `z` and the support of `A`, `ω(A) = tr(ρ_FA)`, and `[ρ_F, N_z] = 0` gives `tr(ρ_Fe^{iθN_z}Ae^{−iθN_z}) = tr(ρ_FA)`. (c) `τ` and `ω_t` with finite `t` fall under (iii): their densities on `F` are proportional to `1` and to `e^{−tN_F} ⊗ 1` (`VC1_5_DRAFT.md`, proof of Theorem U1). In `ω_{±∞}` every `N_x` is sharp at `0` or `5`, so (ii) applies. In the witnesses of Theorem 5.5, in `ω_F` and in the R4 limits, `N_x` is gauge invariant and sharp in the underlying product or ice vector, and `E` fixes it; so (ii) applies again. (d) This is (b)(i) read in both directions, using only invariance under `Ad e^{iθQ_z}`. ∎

### 7.3 RC3: quasi-local fields with fast tails (referee closure, CH1_5UQ_REFEREE.md)

**RC3.** Let `ω` be number-diagonal. Let `ψ` be quasi-local and odd as in definition 5, `D` local with `‖D‖ ≤ 1` and `[D, N_z] = 0` for every `z`, and `n` fixed. Let `r_n` be such that `M(α^n(A))` lies within distance `r_n` of `S(A)` for every local `A` (finite range of the gates, definition 2). If `|x − y| > 2R + r_n`, then
\[
|\omega(\psi_x^*D\,\alpha^n(\psi_y))|\le(2\|\psi\|+f(R))\,f(R).
\]
So if `f(R) = o(R^{−3})`, every such dressed correlation is `o(|x − y|^{−3})` at fixed `n`, and `ψ` does not meet L3 extended to quasi-local fields (`L3^q`, RC8).

*Proof.* `M(ψ_{x,R})` lies in the ball of radius `R` about `x`, and `M(α^n(ψ_{y,R}))` within distance `R + r_n` of `y`, so they are disjoint. RC2(a) gives `ω(ψ_{x,R}^*Dα^n(ψ_{y,R})) = 0`. Lifts and `α^n` are isometric, so the difference of the two bilocals has norm at most `f(R)‖D‖‖ψ‖ + (‖ψ‖ + f(R))‖D‖f(R)`. Take `R = ⌊(|x − y| − r_n)/3⌋`. ∎

### 7.4 RC4: the matter factorization in Theorem 4.2 cannot be dropped (referee closure, CH1_5UQ_REFEREE.md)

**RC4.** Let `m = 5`, `ℓ = (x, y)` with `x` the source, and `γ` the one-link path from `x` to `y`. Then `B_γ = Σ_{jk}c^†_{y,j}U_ℓ^{jk}c_{x,k}`. There is a state `ω` with `ω(B_γ) = 9/2 > 5·2^{−1}`. Its restriction to the registers of `γ`, one register, is trivially a product over the links of `γ`. So the draft's "a charge-1 field dressed by strings is never light in the sense L3 in a state that is a product over the links of the strings, whatever the matter state" (draft line 193) is false as an implication from link factorization to the bound `5·2^{−L}`.

*Proof.* Put `a_k = r^{ℓ,x†}_kc_{x,k}` and `b_j = c^†_{y,j}r^{ℓ,y}_j`. Then `B_γ = (Σ_jb_j)(Σ_ka_k)`. Each `a_k`, `b_j` is a product of one rishon and one matter operator. Rishons commute with matter, and distinct modes anticommute within each system. So the two-exchange computation of Theorem 3.1 shows that the `a_k`, the `b_j` and their adjoints commute pairwise, except `a_k` with `a_k^*` and `b_j` with `b_j^*`. Also `a_k^2 = b_j^2 = 0`. Let `v_0` be the basis vector with matter at `x` full, matter at `y` empty, `x`-end empty and `y`-end full; its register lies in `Λ^5`. For `K, J ⊆ {1, …, 5}` put `e(K, J) = ∏_{k∈K}a_k∏_{j∈J}b_jv_0`, in any order. `a_k` moves flavour `k` from the matter at `x` to the `x`-end, and `b_j` moves flavour `j` from the `y`-end to the matter at `y`. So `e(K, J)` is `±` a basis vector, distinct pairs give orthogonal vectors, and `e(K, J)` lies in `Λ^5` exactly when `|K| = |J|`. Moreover `a_ke(K, J) = e(K ∪ {k}, J)` for `k ∉ K`, and `0` for `k ∈ K`; likewise for `b_j`. Put `s_a = C(5,a)^{−1}Σ_{|K|=|J|=a}e(K, J)`, a unit vector. Each pair `(K′, J′)` with `|K′| = |J′| = a + 1` arises `(a + 1)^2` times in `B_γs_a`. So
\[
B_\gamma s_a=\binom5a^{-1}(a+1)^2\binom5{a+1}s_{a+1}=(a+1)(5-a)\,s_{a+1},
\]
which is `9s_3` for `a = 2` and `8s_4` for `a = 3`. For `w = (s_2 + s_3)/√2`, `⟨w, B_γw⟩ = (1/2)⟨s_2 + s_3, 9s_3 + 8s_4⟩ = 9/2`. Both `s_2` and `s_3` have five matter fermions at `x, y`, so `w` has definite parity there. Let `ω` be the product of the vector state of `w` with any even state of the other sites and links. ∎

`[check]` (3) agrees: `⟨s_{a+1}, B_γs_a⟩ = 5, 8, 9, 8, 5` and `⟨w, B_γw⟩ = 4.5`. The largest eigenvalue of the `6 × 6` matrix with these off-diagonal entries is `14.16`, so states with `Re ω(B_γ) ≈ 7.08` exist; the proof uses only `9/2`. Theorem 4.2 itself is untouched: `w` is entangled between the matter and the register.

### 7.5 RC5: the exact form of "entangled" (referee closure, CH1_5UQ_REFEREE.md)

**RC5.** Let `γ` have `L` distinct links. If the restriction of `ω` to the endpoint matter and the registers of `γ` lies in the closed convex hull of the product states `μ ⊗ λ_1 ⊗ ⋯ ⊗ λ_L`, then `|ω(B_γ)| ≤ 5·2^{−L}`. Hence `|ω(B_γ)| > 5·2^{−L}` forces that restriction to be entangled across the `L + 1` factors (endpoint matter; `ℓ_1`; …; `ℓ_L`).

*Proof.* `ρ ↦ ρ(B_γ)` is affine and continuous on the states of this finite-dimensional algebra. Theorem 4.2 bounds its modulus by `5·2^{−L}` on the products, hence on their convex combinations, hence on the closure. Registers commute with matter, so these are ordinary tensor products. ∎

This is the exact content of the draft's "entangled" (draft line 193) for the string bilocal at `n = 0`. It does not place the entanglement inside the link sector: in RC4 it sits between the matter and a single register.

### 7.6 RC6: spectral witnesses at every odd charge (referee closure, CH1_5UQ_REFEREE.md)

**RC6.** (a) A fermion-odd quasi-local `ψ` of definite total charge `q` has odd `q`. So for even `q` there is no such `ψ`, and the draft's schema "for some `|q| ≥ 3` and some `δ_q > 0`, no stationary, gauge-invariant, cell-symmetric state of an `L5-U` law has a local fermion-odd `ψ` of charge `q` with ..." (draft line 161) holds vacuously at `q = 4`. No example can refute it as written. Restrict it to odd `q`.
(b) Let `q` be odd, `m ∈ {1, …, 9}`, and `τ_E` arbitrary if `m` is odd, `τ_E = 0` if `m` is even. Let `x_1, …, x_{|q|}` be distinct, pairwise non-adjacent sites, and `Ψ^{(1)}_{x_i}` the one-flavour zero mode in the consequences of Theorem 3.2 at `x_i` (adjoint if `q < 0`): `Ψ^{(1)} = P_xX^{(1)}Π^{(1)}P_x` with `X^{(1)} = c^†_{x,1}∏_sr^{ℓ_s,x†}_1r^{ℓ_s,y_s}_1`, `Π^{(1)} = ∏_sΠ[p_{ℓ_s,x} = n_0]`, `n_0 = (m − 1)/2` for odd `m` and `n_0 = max(0, m − 5)` for even `m`. Then `Θ = Ψ^{(1)}_{x_1}⋯Ψ^{(1)}_{x_{|q|}}` is local, fermion odd, of total charge `q`, `α(Θ) = Θ` for the base tick, and `τ(Θ^*Θ) > 0`. So CH1-5U-q(L2(δ)) holds for every `δ ≥ 0` at every odd `q` with `|q| ≥ 3` and every `m`.

*Proof.* (a) By Theorem 2.1 and Z-U, every component of a local odd operator with definite charge vector has odd total charge. If `ψ_R → ψ` with `ψ_R` local, project `ψ_R` onto its odd part and its total-charge-`q` part. Both projections are averages over automorphism groups (global matter parity, and the global `U(1)_N` action, which on a local `A` is `Ad ∏_{z∈S(A)}e^{iθQ_z}`). So they are contractions, keep local elements local, fix `ψ`, and do not increase `‖ψ − ψ_R‖`. The projected `ψ_R` is local, odd and of total charge `q`, so it vanishes for even `q`. So `q` is odd unless `ψ = 0`. (b) The one-flavour mode is Theorem 3.2's construction with one flavour. Its locked input has matter `S ⊆ {2, …, 5}` with `|S| = n_0`, `x`-ends `S`, and `y_s`-ends of size `m − n_0` containing flavour 1. The sizes fit: `n_0 ≤ 4`, `1 ≤ m − n_0 ≤ 5`, `n_0 + 1 ≤ 5`. The image is locked with end number `n_0 + 1`. For odd `m`, `n_0` and `n_0 + 1` are symmetric about `m/2`, so the electric phases agree for every `τ_E`. The conservation clause of Theorem 3.1 gives `α(Ψ^{(1)}) = Ψ^{(1)}`, and its charge is `7` at `x` and `−1` at each `y_s`, total `1`. Distinct non-adjacent sites have disjoint stars: they share no matter and no register. `α` is an automorphism, so it fixes `Θ`. A product of an odd number of odd operators is odd, and charge vectors add. Take a basis vector that is the locked input at every `x_i`. Each factor acts only on its own star, so `Θ` maps it to `±` a basis vector. So `Θ ≠ 0`, and `τ` is faithful. ∎

As the consequences of Theorem 3.2 say, such products are several separated objects. L2 does not see that.

### 7.7 RC7: the pinned charge on other gauge laws (referee closure, CH1_5UQ_REFEREE.md)

**RC7.** Suppose a law and a state `ω` have local unitaries `V_z`, one per site, such that: each `V_z` is even and acts only on the matter at `z` and the registers (or `z`-ends) of the links at `z`; the `V_z` commute pairwise; every gate commutes with every `V_z`; `ω∘Ad V_z = ω`; and for every local `A`, `Ad(∏_{z∈S(A)}V_z)` acts on `A` as fermion parity. Then for local `A` fermion odd and local `B` with `S(A) ∩ S(B) = ∅`, `ω(B^*α^n(A)) = 0` for every `n`. The quasi-local estimate of Theorem 2.2 follows with the same proof.

*Proof.* Put `V = ∏_{z∈S(A)}V_z`. Every gate commutes with `V`, so `Ad V` commutes with `α^n`. `Ad V(A) = −A`. A link in the support of `B` at a site `z ∈ S(A)` would put `z` in `S(B)`; so the factors of `V` act on modes outside the support of `B`, and they are even, so `Ad V(B^*) = B^*`. Hence `ω(B^*α^n(A)) = ω(Ad V(B^*α^n(A))) = −ω(B^*α^n(A))`. ∎

*Instances.* (1) `L5-U`, `V_z = e^{iπQ_z}`, a gauge unitary (the central `−1` of `U(5)_z`). On a component with charge vector `q`, `Ad ∏_{z∈S(A)}e^{iπQ_z}` multiplies by `(−1)^{Σq_z}`, which is its matter parity by Z-U: "its matter parity is \((-1)^{\sum q_x}\)". Gates commute with `Q_z` (`LW1_5.md` Theorem U). (2) `L_cube`, `V_z = e^{iπ𝒢_z}`. `LW1.md` Theorem B4: "Every dressed edge term, dressed cube gate and electric gate commutes with every \(\mathcal G_x\)." `VC1_5.md` Corollary 5.4's proof: "three outgoing and three incoming links make its spectrum integer even for half-integral spin". `CH1.md` Lemma S1: "For a local homogeneous operator of total charge \(Q\), its matter parity is \((-1)^Q\)." (3) `L5-O`, `V_z` the lift of `−1_{10}` at `z`, under `LW1_5.md` line 201: "If, in addition, the lift of \(-I_{20}\) acts as a scalar on every link register inside \(\Lambda\), then \(-1_{10}\) at every site of \(\Lambda\) acts as fermion parity on operators supported with all their links in \(\Lambda\)"; the same line says this "holds for every irreducible register". Take `Λ = S(A)`.

*Scope.* This proves the draft's sentence at line 107 for these three laws, for local fields and for `o(R^{−3})` tails. RC1 transfers to `L_cube` at charge 1 with the same proof, so there too the tail hypothesis is sharp. A law whose fermion parity is not such a product is not covered.

### 7.8 RC8: the implication from CH1-5U-i, with a quasi-local prescription (referee closure, CH1_5UQ_REFEREE.md)

Let `L3^q` be proposed L3 with a quasi-local odd field (definition 5), pairs obeying `|x_i − y_i| → ∞`, and the full free-Weyl tensor structure required, as in CH1-5U-q(L3). Let CH1-5U-q[`L3^q`] be the statement of `CH1_5U.md` R4 with `𝒫 = L3^q`.

**RC8.** (a) CH1-5U-i[`L3^q`] ⇒ CH1-5U-q[`L3^q`]. (b) CH1-5U-q(L3) ⇒ CH1-5U-q[`L3^q`]. (c) So a proof of ¬CH1-5U-q[`L3^q`] refutes CH1-5U-i[`L3^q`] with no further matching; a proof of ¬CH1-5U-q(L3) refutes only the version of CH1-5U-i with local IR fields. (d) In a number-diagonal state, no quasi-local odd field with `f(R) = o(R^{−3})` meets `L3^q` (RC3).

*Proof.* (a) `CH1_5U.md` R4: "For every `𝒫`, CH1-5U-i[`𝒫`] implies CH1-5U-q[`𝒫`]." Its proof uses only that the IR fields of the `10_u` are quasi-local, odd and of charge `u` with `|u| ≥ 3` (`CH1_5U.md` Theorem 2.2), and that their correlations obey `𝒫`. (b) A local field is quasi-local with `f = 0` for large `R`. (c) From (a) and (b). (d) RC3. ∎

*Four tests for `L3^q`* (this report proposes it as the prescription that matches R4; it adopts nothing). (1) Pass: it is a correlator prescription, not a part's target. (2) Pass: one fixed class of fields and dressings. (3) Conditional, as for L3: norm-bounded local dressings may rate charged fields in a phase with a massless gauge field as not light. (4) Conditional, as for L3 (referee report §4): full gauge invariance of the bilocal is more than Theorem 2.2 forces. Relative to L3 it removes one restriction (locality of `ψ`), the one R4 needs.
