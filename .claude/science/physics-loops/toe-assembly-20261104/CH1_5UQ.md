# CH1-5U-q: charged correlations and frozen stars

## 0. Status

**Pass 2; not refereed or frozen.** This item studies a supplied `L5-U` law. It adopts no law, physical axiom, reading of light, or amendment. CH1-5U-q asks for a stationary gauge- and cell-invariant state and a quasi-local odd field of charge `|q| ≥ 3` with free-Weyl large-distance correlations. The charged-correlator prescription matters.

**Proved, conditional on the stated law and cited local-algebra inputs.** Local Gauss-charge vectors are conserved (Theorem 2.1). Separated local odd fields have zero undressed two-point function at all times; the same excludes Weyl falloff for fields with sufficiently fast norm tails (Theorem 2.2). Frozen-star projectors and a class of operators inside them are conserved by the base tick (Theorem 3.1). For `3 ≤ m ≤ 7` there are exact charge-3 zero modes, for all electric angles if `m` is odd and at zero electric angle if `m` is even (Theorem 3.2). These are static defects, not Weyl particles. For even `m` there is an all-frozen invariant state, pure on the invariant algebra, at filling `m/2` (Theorem 3.3). Electrically diagonal states kill the specified local dressed correlations (Theorem 4.1). A link expectation has norm at most `1/2`, and a simple string in a suitable product state has an exponential bound (Theorem 4.2). A triple-hop operator is nonzero exactly for `3 ≤ m ≤ 7` (Theorem 5.1).

**GAP.** Norm quasi-locality alone supplies no `o(R^-3)` tail. The draft's claim that Corollary G1 decides the original CH1-5U-q as written therefore does not follow. CH1.md already requires a dressing or charge-sector prescription; calling the undressed reading the text's unique literal meaning is not justified. The draft also extends a product bound to repeated-link strings, arbitrary times, arbitrary dressings and states merely separable across links without proof; Theorem 4.2 gives the actual hypotheses. Non-product correlations need not be entanglement. The inference from the proposed L3 to the full original IR hypothesis, and conversely from IR to L3, needs a matching prescription and locality assumptions. The draft's extension to all gauge laws is not proved here.

**Open by name.** CH1-5U-q and CH1-5U-q(L3); the charged-correlator reading of IR; CH1-5U-i; AM-5; CH1-ii; CH1-5O-i; VC1-5U-odd; LW1-5U-PS7; Y2-W. No named failing step for `L5-U` follows from the attacks below. L2 is a different proposed question and is answered affirmatively, not an answer to CH1-5U-q.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1af02-1d0e-7a61-b94e-9401d7afe267`. Pass 1: `CH1_5UQ_DRAFT.md`, Claude Opus 5.5, whose own date is 2026-11-06. Pass 2: Codex, requested model `gpt-6.1-terra`; actual model, reasoning effort and session ID are not exposed to this session and cannot be verified. Checkout HEAD `193e7169ca47634e008f40deeb71aa739e8c71b0`; draft SHA-256 `ffdae83b1eb076c0d534e645ee058562da095a9d328b27ee1f8955c53014f01d`. Context: `TOE_ASSEMBLY.md` §§3.4–3.5 and CH1 target; `LW1.md`, `CH1.md`, `LIT_SMG.md`. Source-specific dependencies below are provisional draft inputs, not audit verdicts. The draft reports numerical scratch checks; their files were not independently reproduced here. No numerical check is used as proof.

## 1. Definitions inferred by the distiller

1. Sites are `Z³`, with five matter CAR modes `c_{x,k}` per site. Each link has ten rishon CAR modes, five per end, in the fixed-number register `Λ^m(C^10)`, `1 ≤ m ≤ 9`. Different links and matter commute as ordinary tensor factors; matter modes anticommute across sites. Rishons at the two ends of one link anticommute. `N_x` and `p_{ℓ,x}` count matter and end modes; `p_{ℓ,x}+p_{ℓ,y}=m`.
2. For an oriented link `(x,y)`, `U_ℓ^{jk}=r_j^y r_k^{x†}` and `h_ℓ=Σ_{jk} c_{y,j}† U_ℓ^{jk} c_{x,k}+h.c.`. The base tick is `U_0=W_E M_o M_e`, with cube generators `H_C=3^{-1/2}Σ_{ℓ⊂C}η_ℓ h_ℓ`, and `W_E=∏_ℓ exp[-iτ_E(p_{ℓ,src}-m/2)^2]`. An update of `L5-U` form adds finitely many bounded-range layers of gauge-invariant gates. Its automorphism is `α(A)=U*AU`, understood by finite gate products on local `A`.
3. `Q_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}` generates the local central `U(1)`. Gauge invariance means invariance under every local `U(5)` conjugation, not necessarily a Gauss-singlet vector. `G_U` denotes the supplied cell lifts `β_g`. Cell invariance means invariance under those lifts; stationarity means `ω∘α=ω`. `E` denotes the local-gauge averaging conditional expectation onto `𝔄^G`.
4. `S(A)` is the matter sites of a local operator and both ends of every link in its support; `M(A)` is its matter support. A charge vector `q=(q_z)` is defined by `Ad exp(iθQ_z)(A)=exp(iθq_z)A`. Its total is `Σ_z q_z`, equal to matter-number change, called `U(1)_N` charge. Fermion parity concerns matter modes.
5. A quasi-local field is a norm limit of local fields. Where a rate is needed, `ψ_R` is odd, supported in a radius-`R` ball including link ends, and `f(R)=||ψ-ψ_R||`. Spatial copies use the specified lifts; their existence for the chosen positions is assumed.
6. For stationary `ω`, its GNS unitary is `Ũ π(A)Ω=π(α(A))Ω`. Stationarity gives an isometry and surjectivity of `α` gives dense range. Its eigenvalue `e^{-iw}` defines quasi-energy `w` modulo `2π`.
7. **Proposed L1:** the undressed two-point function has a nonzero `r^-3` lower bound along arbitrarily distant pairs, at some times. This is only a necessary part of free-Weyl agreement. **Proposed L2(δ):** `ω(ψ*ψ)=1` and `ω((α(ψ)-ψ)*(α(ψ)-ψ))≤δ²`. This is distance at most `δ` from the unitary eigenvalue 1 in norm, not necessarily an eigenstate. **Proposed L3:** for a local odd `ψ`, a fixed integer time `n`, distant pairs `(x_i,y_i)`, and local dressings `D_i` with `||D_i||≤1` and `[D_i,N_z]=0` for every `z`, the bilocal `ψ_{x_i}*D_i α^n(ψ_{y_i})` is gauge invariant and its expectation has modulus at least `c|x_i-y_i|^-3` for fixed `c>0`. Full free-Weyl tensor structure is an additional requirement. These are proposals; none is adopted. Norm control prevents arbitrary rescaling; the matter-number condition excludes dressings that themselves transfer matter.
8. A state is electrically diagonal if it is invariant under every `Ad exp(iθp_{ℓ,z})`. A basis vector is flavour-locked at `x` if the occupied flavour sets of matter at `x` and of each of its six adjacent link ends agree.

The cited law and symmetry inputs are `LW1_5.md` Theorem U and Z-U, and `VC1_5_DRAFT.md` Lemmas 1.1 and C. The latter supplies finite-support gauge averaging, cell lifts and their commutation with the base tick. The results below do not promote those inputs to retained status.

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

The theorem needs neither stationarity nor cell invariance beyond the use of translates. **GAP:** a norm tail can decay arbitrarily slowly. It does not establish the asserted conclusion for all quasi-local operators. The draft's L1 test-3 judgment is conditional on the faster tail and on taking undressed correlations as the reading. A gauge-invariant dressing or charge-sector prescription is explicitly contemplated in `CH1.md`, inferred definition 8.

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
X=c_{x,1}^\dagger c_{x,2}^\dagger c_{x,3} \prod_{s=1}^6
r^{\ell_s,x\dagger}_1r^{\ell_s,x\dagger}_2r^{\ell_s,x\dagger}_3
r^{\ell_s,y_s}_3r^{\ell_s,y_s}_2r^{\ell_s,y_s}_1,\quad
\Pi=\prod_s\Pi[p_{\ell_s,x}=n_0],\quad \Psi=P_xX\Pi P_x.
\]
`Ψ` is nonzero, local and odd, with local charges `21` at `x` and `-3` at each `y_s`, hence total charge `3`. The base tick fixes it for any electric angle if `m` is odd, and for `τ_E=0` if `m` is even. In the tracial state its normalized GNS vector is a charge-3 exact zero-quasi-energy excitation. Its adjoint gives charge `-3`. Gauge transforms and cell lifts of `Ψ` are also fixed; its finite-dimensional gauge orbit span contains an irreducible multiplet of fixed odd charge-3 operators.

*Proof.* Each adjacent link factor transfers three rishons from `y_s` to `x`; the matter factor creates three at `x`. `P_x` and `Π` commute with all `Q_z`, giving the charges. Pick `S⊂{4,5}` of size `n₀`, put matter `S` and each `x`-end `S`, and choose each opposite end to contain `{1,2,3}` with size `m-n₀`. Both the input and its nonzero image under `X` are locked, so `Ψ` is nonzero. The relevant end number goes from `n₀` to `n₀+3`. For odd `m` these values are symmetric about `m/2`, so their electric phases agree; for even `m` they agree at `τ_E=0`. Theorem 3.1 applies. The local normalized trace is faithful and is preserved by local automorphisms, the tick, gauge transformations and cell lifts. Thus `τ(Ψ*Ψ)>0` and `Ũπ(Ψ)Ω=π(Ψ)Ω`. Gauge and cell covariance of the base tick gives the orbit statements; finite-dimensional compact-group complete reducibility gives a summand. □

Consequently the proposed CH1-5U-q(L2(δ)) holds for all `δ≥0`, for the listed laws. The same construction with all five flavours, `m=5`, `n₀=0`, gives charge `±5`; the same proof with one flavour gives charge `±1` for odd `m` at any electric angle, and even `m` at `τ_E=0`. Products of three separated charge-one modes also give charge three, but represent three separated operators. These examples disprove a universal spectral exclusion at charges `±3` and `±5`; they do not disprove an exclusion at every other individual charge. In particular, the draft's existential quantifier “for some |q|≥3” cannot be refuted merely by examples at `±3` and `±5`.

For `m∈{1,2,8,9}`, the end-number range has width at most two, so this locked three-unit end move is impossible. The zero modes are pinned: Theorem 2.2 kills their separated undressed correlations and Theorem 3.1 kills incident hops. A zero quasi-energy is not a propagating particle pole, residue, mass, or Weyl correlation (`LIT_SMG.md` §9).

**Theorem 3.3 (draft Corollary F2).** For even `m=2n`, `n=1,…,4`, choose a flavour set `A_x` of size `n` at each site and occupy it in the matter and all six link ends at `x`. Let `Φ` be the resulting product state and `ω_F=Φ∘E`. Then `ω_F` is stationary under the base tick, gauge invariant, cell invariant, independent of the choices `A_x`, and pure on `𝔄^G`. It has `N_x=n` and `Q_x=7n` sharply.

*Proof.* The end occupancies sum to `2n=m` on each link. Every hop kills the locked vector and electric gates act by phases, so `Φ` is stationary on local observables. Gauge averaging commutes with the base tick and cell lifts. Independent site flavour permutations map any choice of sets to any other and disappear after `E`; the lifted cell maps carry locked vectors to locked vectors, up to phases. Thus `ω_F` is cell invariant and choice independent.

For purity, fix a finite site set `S` containing the support and both ends of its links. Project onto `N_x=n` for `x∈S` and end number `n` on all incident links. The projected sector factors into site spaces `W_x=Λ^n(C^5)⊗(Λ^n(C^5))^{⊗6}` and outside ends. In each `W_x` the gauge Cartan operators `H_{x,j}=n_{x,j}+Σ_{ℓ∋x}n^{ℓ,x}_j` have joint eigenvalues 7 for `j∈A_x` and 0 otherwise. These eigenvalues force each of the seven occupied sets to be `A_x`, so the joint eigenspace is one-dimensional. By the finite-dimensional invariant-algebra purity lemma and the local-to-infinite sector lemma, `VC1_5_DRAFT.md` Lemmas 2.2–2.3, the restriction to `𝔄^G` is pure. The sharp-number statements are immediate. □

This agrees with the conditional relation `Q_x-3m=n` in `VC1_5_DRAFT.md` Theorem U2. The state is electrically diagonal and dark. The draft also invokes PS-3h5 and VC1 Corollary U3′ to infer a tick-1 record from sharp `N_x`; that downstream record claim remains conditional on those inputs, which are not checked here.

## 4. Dressed correlations

**Theorem 4.1 (draft Lemma E and Corollary E1).** A gauge-invariant electrically diagonal state is invariant under each `Ad exp(iθN_z)`. If local odd `ψ`, local `D` with `[D,N_z]=0` for all `z`, and integer `n` satisfy `M(ψ_x)∩M(α^n(ψ_y))=∅`, then
\[
\omega(\psi_x^*D\alpha^n(\psi_y))=0.
\]
Consequently no such local field meets proposed L3 in an electrically diagonal state. The tracial state, the `ω_t`, `ω_m` and full-matter partner states of `VC1_5_DRAFT.md` Theorems U1 and U3, and the state `ω_F` of Theorem 3.3 are electrically diagonal and do not meet L3.

*Proof.* `exp(iθN_z)=exp(iθQ_z)∏_{ℓ∋z}exp(-iθp_{ℓ,z})`; all factors commute and their adjoint actions preserve the state. Decompose the fields into definite local matter-number changes. Each component of `ψ_x` has an odd, hence nonzero, total matter change supported in `M(ψ_x)`. The other field has no matter change there, and `D` has none anywhere. Invariance under a site-number phase kills each term. Finite-range dynamics keeps `α^n(ψ_y)` local at each fixed `n`, so its matter support is disjoint from `M(ψ_x)` for sufficiently distant pairs. The tracial and `ω_t` register states are traces. The other named states are gauge averages of end-number eigenvector states; end numbers are gauge invariant, so their phase actions commute with `E` and preserve these states. □

The conclusion covers the listed states, not every stationary invariant state on file in an unspecified corpus. For L3 it assumes a fixed time and a local field. A quasi-local extension with variable long dressings needs its own quantitative estimate.

**Theorem 4.2 (draft Lemma W2′ and Corollary W2′.1).** For any state `λ` on one register, the matrices `u_{jk}=λ(U^{jk})` and `v_{jk}=λ(U^{jk*})` obey `||u||,||v||≤1/2`. The bound is attained at `m=5`. Let `γ` be a path of `L` distinct links from `y` to `x`, let `T_i` be the oriented transport matrix (`U` or `U†` with transposed indices), and define
\[
B_\gamma=\sum_{jk}c_{x,j}^\dagger(T_L\cdots T_1)_{jk}c_{y,k}.
\]
If the restriction of `ω` to endpoint matter and these registers is `μ⊗λ_1⊗⋯⊗λ_L`, then `|ω(B_γ)|≤5·2^{-L}`.

*Proof.* For `X²=0`, write a unit vector `a+b` with `a∈ker X`, `b⊥ker X`. Since `ran X⊂ker X`, `|⟨a+b,X(a+b)⟩|≤||X||||a||||b||≤||X||/2`. Mixed states follow by convexity. For unit `a,b∈C^5`, the matrix element `a*u b` is the expectation of `X=(Σ_j \bar a_j r_j^y)(Σ_k b_k r_k^{x†})`. It has square zero and norm at most one. The same argument applies to the adjoint matrix. At `m=5`, occupy the five orthonormal orbitals `(r_j^{y†}+Σ_k V_{kj}r_k^{x†})/√2`; the link expectation has singular values `1/2`.

For a simple path the expectation factors into the endpoint matter matrix `M_{jk}=μ(c_{x,j}†c_{y,k})` and `t_L⋯t_1`, with `t_i=λ_i(T_i)`. CAR and Cauchy–Schwarz give `||M||≤1`, so `||M||_1≤5`. Matrix Hölder and the first bound give the result. □

**GAP in the draft's generalization.** A path that repeats a link gives expectations of products in that one register, not products of one-link expectations. A product restriction on the link registers alone does not imply factorization from endpoint matter. At nonzero time `α^n(c_y)` can involve further registers, so the displayed bound does not directly apply. Nor does failure of product form imply quantum entanglement: mixtures of product states are a counterexample to that inference. The proved bound also holds for convex mixtures of states satisfying its full factorization, by linearity. It addresses this particular charge-one string, not all norm-bounded dressings, arbitrary charge, or a general perimeter law.

## 5. Triple hop and failed routes

**Theorem 5.1 (draft Lemma T).** For an oriented link `(x,y)`, let `A_ℓ=φ_{ℓ,y}*φ_{ℓ,x}` and `T_ℓ=A_ℓ³`. It is gauge invariant, moves three matter units from `x` to `y` and three rishons in the opposite direction, and is nonzero exactly when `3≤m≤7`.

*Proof.* The two endpoint `φ` operators commute, so `T_ℓ=(φ_{ℓ,y}*)³(φ_{ℓ,x})³`. Gauge invariance follows from the invariant contractions. The allowed values of `p_{ℓ,x}` are `max(0,m-5),…,min(5,m)`. Their width is at least three exactly for `3≤m≤7`; otherwise the operator, which raises `p_{ℓ,x}` by three, vanishes. In that range choose matter `{1,2,3}` at `x`, none at `y`, an `x`-end set `S⊂{4,5}` of size `max(0,m-5)`, and a `y`-end set of size `min(m,5)` containing `{1,2,3}`. The six permutations in `(φ_x)³` have the same sign after both CAR reorderings, and yield a nonzero vector. Applying `(φ_y*)³` gives nonzero mutually orthogonal terms for different three-flavour subsets of the occupied `y`-end. Thus no cancellation occurs. □

This refutes the proposed step that the finite register cannot carry a triple for every `m`. It is an algebraic hopping matrix element, not proof of a mobile isolated charge-3 particle or a long-distance phase. The draft reports a scratch check of matrix entries `36` for `m=3,…,7` and zero otherwise; it was not reproduced here.

The proposed light-cone exclusion fails at the step from finite propagation support to a charge-dependent spectral or correlation bound: the same support radius applies to each charge, and Theorem 3.2 gives a static zero mode inside it. This does not establish that every conceivable use of locality is charge blind. The proposed spectral exclusion fails at charges `±3` and `±5`, as above. The pinned-charge argument proves the undressed theorem, but gives no obstruction when a gauge-invariant dressing cancels the local charge vector.

For proposed CH1-5U-q(L3), the draft tried three routes to existence: (P1) the auxiliary c-number quasi-free tick has elementary charge `±1` modes and is not the interacting tick (`CH1_5U_DRAFT.md` Lemma Q1′ and `LW1_5.md` inferred definition 4); (P2) the charge-3 zero mode is static and its tracial state is electrically diagonal; (P3) the named invariant states are electrically diagonal and the specified product strings obey Theorem 4.2. It tried three routes to exclusion: (R1) a support cone, (R2) the finite-register capacity, and (R3) the spectral bound. The preceding results identify where each stated route stops. Failed routes do not prove the open claim or its negation.

`CH1_5U_DRAFT.md` Lemma Q1 gives `|u|≥3` for its `10_u`. If CH1-5U-i supplies a local `10_u` field satisfying exactly the L3 prescription, with all other required hypotheses, then it implies CH1-5U-q(L3); its negation would refute that correspondingly strengthened version of CH1-5U-i. **GAP:** the original IR field is quasi-local and its charged-correlator prescription is not fixed to L3. The implication as written needs those additional matches. CH1-5U-q(L3) itself is an existence question with full Weyl tensor structure in addition to the L3 lower bound.

## 6. Proposed readings and four-test results

The draft's tests ask whether an item (1) fixes a part's target, (2) remains open to further development, (3) settles downstream physics by premise, and (4) adds unnecessary structure or constants. These are author-side judgments, not mathematical verdicts. No reading is adopted.

| Proposed item | Draft's check | Distiller's qualification |
|---|---|---|
| L1, undressed | 1 pass; 2 pass; 3 fails; 4 pass | Theorem 2.2 proves the obstruction for local or fast-tail fields. General quasi-local fields and other laws need further hypotheses. CH1's charged prescription is not fixed as L1. |
| L2(δ), spectral | 1–4 pass; witness in Theorem 3.2 | A different, weaker question. A pinned defect meets it; it does not decide IR or CH1-5U-i. |
| L3, bounded, matter-number-preserving dressing | 1, 2, 4 pass; 3 conditional because a choice of dressing may exclude phases of interest | The draft calls this a working reading, but it remains proposed. Its requirements and fixed time are extra choices; sufficiency for the intended Weyl or charge-sector physics is open. |
| Frozen space `F_x` | 1–4 pass | A definition from the supplied law; Theorem 3.1 proves its properties for the base tick. |
| CH1-5U-q(L3) | 1–4 pass as an open question | Its implication from CH1-5U-i is conditional on the matching assumptions stated above. |

A free Weyl field has an equal-time two-point function with `r^-3` scale as used in the draft; this physical input is not derived here. Elitzur, Dirac, Buchholz, Fröhlich–Morchio–Strocchi, Lieb–Robinson and the SMG literature are context, not premises for the algebraic proofs. The `1/2` link-expectation bound does not by itself show that every gauge-invariant observable fails to approximate a group-valued link at larger scales. Y2-W and the needed state and scaling-limit questions remain open.
