# ZM1-I1[a]: trace obstruction for the zoom

**Status.** Under the explicit coarse-algebra and locality readings below, Theorems 1–6 prove that the required singleton Gauss embedding cannot exist for `L≥2` on `L5-U[m]`, `1≤m≤9`. The separate `L5-O[S_+]` analogue has the same obstruction. These are author-side arguments, not independent audit findings. The result precedes the choice of vacuum, update, comparison class and `p`; it does not adopt a new axiom.

**GAP.** The draft's general Theorem G omits hypotheses needed for trace transfer and bounded displacement. Its swap-band inference and its application of spectral transfer also omit hypotheses. See §5–6. The exact applicability of the inferred coarse-link assignment to Definition Z is a reading question, not an established owner decision.

**Open.** G1-EQ; the owner's choice among R-G1EQ, R-ISO, R-MEAS or another reading; the named inherited items in §7. No independent referee has checked this item.

**Provenance.** Pass 2 distillation of `ZM1I1A_DRAFT.md`, pass 1 by Claude Opus 5.5. Model: `gpt-6.1-terra`; effort and session id: see run log. The draft cites source revisions `31ef08a1e` and `59d3886d9`; these were not checked with git. The pass-1 scratch enumeration was not rerun and is not proof.

## 1. Definitions inferred by the distiller

1. **Fine and coarse systems.** The fine sites form `Z³` with nearest-neighbour links. For `L5-U[m]`, matter at each site has five CAR modes; each link has algebra `End(Λ^m C¹⁰)`, `1≤m≤9`, with five rishon modes at each end. Finite matter/link regions generate the quasi-local algebra. Link factors commute with matter and each other. Put `Q_x=N_x+Σ_{ℓ∋x}p_{ℓ,x}`. The star of `x` consists of its matter factor and six link factors. Use normalized traces on finite factors and their compatible quasi-local trace `τ`.
2. **Coarse indexing.** A coarse cell `u∈Z³` contains eight sites `X=(u,r)`, `r∈{0,1}³`; `X↦2u+r` identifies the coarse graph with `Z³`. Its fine block `β_u` contains `(2L)³` fine sites. A coarse link is assigned to an endpoint cell or an adjacent cell. Uniform (Z-a) applies to each site and link factor relative to that assigned block. This makes the locality use explicit; Definition Z includes coarse links in site algebras but does not itself spell out this assignment.
3. **R-form, proposed, not adopted.** The coarse algebra of a law of `L5-U` form is the same construction on that graph, with any `m₁∈{1,…,9}`. The draft's four tests are P P P P: no target or downstream result is stipulated; the algebra is specified up to `m₁`; no extra equality `m₁=m` is imposed. This is an interpretation of the stated form, not an owner ruling. The O analogue uses `End(S_+)` on each link.
4. **Trace covariance.** `Cov_τ(A,B)=τ(AB)−τ(A)τ(B)`, without conjugation. A pair `(ω,α)` is **dark** if `ω(Xαⁿ(Y))=ω(X)ω(Y)` for every `n≥0` and disjointly supported local gauge-invariant `X,Y`. A finite-range map sends each coarse factor into a fixed-radius neighborhood of its assigned block.
5. **G1-eq, proposed.** For singleton representatives `x_X`, require `Φ∘Ad(e^{iθG_X^{(1),T}})=Ad(e^{iθG_{x_X}^T})∘Φ` for every `X,T,θ`. The remaining conditions of R-G1EQ are in §7.

The owner-selected comparison and its `p=2` envelope are in `TOE_ASSEMBLY.md` §3.8. Definition Z and (G1)–(G2) are in `ZM1.md` §§1.3–1.4. The O comparison is separate and proposed in `ZM1_OBS.md` §5.

## 2. Trace and adjacency on L5-U

**Theorem 1 (T1–T3: trace transfer and covariance).** A unital *-homomorphism `Φ:𝔄₁→𝔄` transfers the normalized trace: `τ∘Φ=τ₁`. Put `v_m=m(10−m)/36`. Then
\[
\operatorname{Cov}_τ(Q_x,Q_y)=\begin{cases}-v_m,&x\sim y,\\0,&x\ne y,\ x\not\sim y,\end{cases}\quad
\operatorname{Var}_τ(Q_x)=5/4+6v_m.
\]
In particular, neighbouring coarse charges have covariance `−v_{m₁}<0`.

*Proof.* Finite CAR algebras are full matrices: Jordan–Wigner gives a surjection onto `M_{2^k}`, and the `4^k` ordered CAR monomials span the domain. Tensor with the full link matrices. A tracial state on `M_n` vanishes on off-diagonal matrix units and has equal values `1/n` on diagonal units. Thus `τ∘Φ` agrees with `τ₁` on each finite algebra, hence by density everywhere.

Under the trace, each matter occupation is an independent fair bit and each link is a uniform `m`-subset of ten modes. If `p` counts the occupied modes in one five-mode end, indicator covariances give
\[
\operatorname{Var}(p)=5\frac m{10}(1-\frac m{10})+20(\frac{m(m-1)}{90}-\frac{m²}{100})=v_m.
\]
The other end has number `m−p`. Distinct stars share precisely their common link when adjacent and no factor otherwise. Sum independent contributions; the matter variance is `5/4`. □

**Theorem 2 (T: adjacency).** If (G1) holds at `T=1` with singleton representatives, each coarse edge `(X,Y)` maps to a fine edge `(x_X,x_Y)`, and `m(10−m)=m₁(10−m₁)`.

*Proof.* Trace transfer and (G1) equate the covariance of `Q_{x_X},Q_{x_Y}` to `−v_{m₁}`. Equal representatives have nonnegative variance; distinct non-neighbours have covariance zero. Thus they are neighbours and Theorem 1 equates the two negative covariances. □

**Theorem 3 (T5, T′, T″: locality and density).** Under the locality assignment in §1, (G1) and disjoint singleton sets, `L=1`. Thus there is no specified map for `L≥2` under R-form.

*Proof.* (Z-a) approximates `Q_{x_X}=Φ(Q_X^{(1)})`, a sum of seven terms of norm at most five, by an operator in a fixed-radius neighborhood of `β_{u(X)}`, with error at most `35Ce^{-R/ξ}` after a fixed enlargement for incident coarse links. If the fine star is disjoint from that neighborhood, choose two occupation configurations equal outside it, with empty versus full matter at `x_X` and end occupations minimal versus maximal. Their expectations of `Q_{x_X}` differ by at least 11, while their expectations of the approximation agree. For large fixed `R` this contradicts the error bound. Hence representatives lie within a uniform distance `R_*` of their blocks.

The representative map is injective by disjointness. Theorem 2 sends each of the six distinct neighbours of a coarse vertex to the six neighbours of its image. Its image is therefore closed under adjacency, and connectivity makes it all of `Z³`. The `(2LN)³` fine sites in an `N³` block cube must then come from at most `8(N+2c)³` coarse sites for a constant `c` determined by `R_*` and `L`. Divide by `8N³` and let `N→∞`: `L≤1`. □

The failing requirement is the exact generator identity (G1), together with locality and the fixed-form coarse algebra. The proof does not use (Z-b), (G2), grading, dynamics, states, the envelope or `p`. It gives the same conditional obstruction for the original ZM1-I1 and the classes in `ZM1_OBS.md` §5. Extra finite gauge-neutral coarse factors do not affect the covariance. The Z0 indexing with one site per block has an even lower coarse density.

**Theorem 4 (V: finite embedding sets).** On U, if (G1) at `T=1` holds for nonempty finite sets `S_X`, each set is a singleton, even if `m₁` differs from `m`.

*Proof.* Let `S=S_X`, `I(S)` count internal edges and `∂S` boundary edges. Internal end numbers sum to `m`, so the variance of `Σ_{x∈S}Q_x` is `5|S|/4+v_m|∂S|`. Trace transfer gives
\[
45(|S|-1)=6k₁-k|∂S|,\quad k=m(10-m),\ k₁=m₁(10-m₁)\in\{9,16,21,24,25\}.
\]
Every finite nonempty subset of `Z³` has at least six boundary edges, one from each coordinate extremum. Hence `|S|≤3`. Three sites span at most two edges, so `|∂S|≥14` and the equation would give `90≤24`. For two sites the boundary is 10 or 12, making the right side even and the left side 45. Thus `|S|=1`. □

**Theorem 5 (Z5: traceless generators suffice).** For U, (G1) on traceless `T` and disjoint singletons also implies Theorem 3.

*Proof.* Put `ζ=e^{2πi/5}` and `H=(2π/5)diag(1,1,1,1,−4)`. Then `u_x=e^{iG_x^H}=ζ^{N_x}∏_{ℓ∋x}ζ^{p_{ℓ,x}}`. Homomorphisms preserve exponentials (`ZM1_OBS.md` Theorem 1, already proved there). Let `μ=(1+ζ)^5/32` and `κ=Eζ^p`. For neighbouring coarse sites the covariance is `μ²κ^{10}(ζ^{m₁}−κ²)`. Here `μ≠0`, `|κ|<1` because at least two consecutive end numbers have positive weights, and `κ≠0`: for `m₁≤2` the contributing roots lie in an open half-plane; direct sums for `m₁=3,4,5` have negative real parts; particle-hole symmetry covers `m₁≥6`. Thus the covariance is nonzero. Disjoint non-neighbouring fine stars have zero covariance, so adjacency follows. Apply the bounded-displacement and counting proof of Theorem 3 to any nonconstant local traceless generator, for instance `G^{diag(1,-1,0,0,0)}`: configurations differing only on the remote star give a fixed nonzero expectation difference. □

## 3. The O analogue

**Theorem 6 (O1, O, O″).** For coarse and fine `L5-O[S_+]` systems, (G1) on the five Cartan generators and disjoint singleton sets forces adjacency of representatives. With §1 locality it forces `L=1`.

*Proof.* Each matter algebra is `M₃₂` and each link algebra is `End(S_+)=M₅₁₂`, so Theorem 1's trace-transfer proof applies. On five complex modes the Cartan sum is `N−5/2`. On a link the two end occupations have equal parity. For `g=exp(iπ(N−5/2)/2)`, let `χ_e,χ_o` be the unnormalized even and odd traces. Direct binomial sums give `χ_e=−4e^{-5πi/4}`, `χ_o=−4i e^{-5πi/4}`, `(χ_e−χ_o)²=−32`, and each one-factor normalized trace is `2^{-5/2}`. Thus the covariance of the two end actions on one link is `(χ_e−χ_o)²/1024=−1/32`. For neighbouring stars the other twelve factors multiply this by `(2^{-5/2})^{12}`, yielding `−2^{-35}`. Disjoint stars have zero covariance. Homomorphism and (G1) transfer the exponentials; disjoint representatives exclude coincident sites. Adjacency follows.

For bounded displacement use one Cartan generator. Its star spectrum includes `±7/2`, attained by local occupation configurations with each link in `S_+`; a far-end mode adjusts link parity. Two such configurations agree off the star, giving a fixed separation from any operator supported away from it. Theorem 3's locality and counting argument applies. □

The O analogue therefore has no data under these readings for any O vacuum or update. This is not an assertion that the owner selected the O analogue.

## 4. First tests

**Theorem 7 (Proposition 6.0: dark pairs).** Suppose `Φ` has (G1)–(G2), singleton sets and finite range, and both state/update pairs are dark. Then the class-(a) bound holds for every `p≥1`, with a constant depending on the support radius and map range.

*Proof.* `ZM1_OBS.md` Theorem 3 already proves `Φ(𝔄₁^G)⊆𝔄^G`. Beyond a fixed separation `r_*`, the two pairs of supports are disjoint, hence both truncated values vanish. For smaller `r≥1`, the difference is at most `2M(r,t)≤2r_*^p r^{-p}M(r,t)`. □

**Theorem 8 (DK: dark kinematics).** For the U base tick without plaquette layer, take an even product state `ψ` over site and link factors with empty or full matter everywhere and link densities commuting with electric factors. If `ω=ψ∘E`, then for invariant local `X,Y`, `ω(Xαⁿ(Y))=ψ(Xγⁿ(Y))`, where `γ=Ad(W_E^*)` is a product of single-link automorphisms. Thus the pair is dark.

*Proof.* `GA1_5.md` Theorem 6.1 already proves the empty-matter reduction. Invariant `X` preserves the empty-matter sector by total local charge conservation; hops vanish there, and the update restricts to `W_E`. The same holds on full matter because creation into a filled mode kills the hop. The trace computation in the finite support region gives the displayed identity. Electric evolution preserves each link factor and `ψ`; disjoint supports factorize. Gauge averaging fixes invariant products. □

This applies to the empty/full product witnesses of `VC1_5.md` Theorems 5.2 at `t=±∞` and 5.5 under their stated readings. With hypothetical finite-range maps and dark coarse pairs, their class-(a) test is automatic; Theorem 3 still excludes the specified map. Exponential locality alone does not imply automatic matching: a nonzero tail against an identically zero tail violates `ZM1_OBS.md` Lemma ER.

**Theorem 9 (R2′).** For the mixture in `VC1_5.md` Proposition R2, the invariant link projection `P=[p_{ℓ,src}=a]` has truncated correlation `1/4` with its distinct cell translates along the same direction at every tick.

*Proof.* In each of the eight product states `ψ_s`, `P` and its translate are fixed by the electric evolution and are sharp, both equal to 1 for four choices of `s` and 0 for the other four. Theorem 8 gives the evolved product value. The mixture has product expectation `1/2` and each one-point value `1/2`, so the truncated value is `1/4`. □

For a comparison channel that actually contains this observable as an image, Lemma ER in `ZM1_OBS.md` already proves equality of the asymptotic tail envelopes, including amplitude `1/4`. It does not establish that a given block map contains `P`.

## 5. General mechanism and corrections

**Theorem 10 (corrected G).** Suppose both quasi-local algebras have compatible unique normalized product traces on full finite matrix factors. Suppose the coarse endpoint gauge unitaries of one edge have nonzero covariance, while corresponding fine unitaries at distinct non-neighbouring sites have zero covariance. A unital homomorphism obeying (G1) on disjoint singletons sends that edge to a fine edge. If this holds for every edge of connected degree-six cubic graphs and locality also gives uniformly bounded representative displacement relative to the blocks, then `L=1`.

*Proof.* Transfer the trace as in Theorem 1, preserve exponentials, and compare covariances. The degree and density argument is Theorem 3. □

**GAP G.** The draft's general theorem assumes only finite link registers, compact gauge action and nonzero unshared traces. Those conditions alone do not establish a unique trace on arbitrary local algebras, the graph degree/density, or the fixed local spectral separation needed for bounded displacement. Theorem 10 states sufficient hypotheses. The draft's `L_cube` covariance `−S(S+1)/3` assumes the stated spin-electric generator and trace; its application of the general theorem also needs these missing hypotheses.

**GAP swap-band inference.** `GA1_5.md` Theorem 6.3 and Proposition S-odd already establish the named exact neutral swap band; `GA15PHI.md` records its conjugate. The draft infers an exact coarse glider from a nonzero component of an image along one glider vector. A component alone does not isolate the channel from other spectral components, and the bound is approximate. Even for a pure glider it gives an `O(t^{-2})` relative discrepancy at the moving point, not exact equality at finite `t`. The fine ticks are `Lt`; its position must be converted consistently into coarse-cell units. Exact matching requires further hypotheses and proof.

**GAP two-band inference.** `LZ1I.md` Theorems 6–8 already prove the two stated neutral bands in their stated setting. `ZM1_OBS.md` Theorems 8′–9′ give conditional branch/weight conclusions under their Fourier summability, separation and weight hypotheses. The draft does not verify those hypotheses or show the relevant bands occur in the image of the proposed map. Therefore it cannot assert unconditional reproduction of both phases. `LZ1-i[ZM1a]` remains open.

**GAP scope of R2′.** The draft says every separation; its product proof assumes distinct links. Theorem 9 states the supported result. At zero separation the projection happens also to give variance `1/4`, but this is a separate calculation and is not a class-(a) separation.

## 6. Boundaries and prior results

The obstruction uses a unital full-algebra homomorphism, finite full-matrix factors with product trace, exact generator identification, the specified coarse adjacency, disjoint representatives, and local placement. It does not rule out other zoom notions. Under G1-eq, `e^{-iθG_{x_X}}Φ(e^{iθG_X^{(1)}})` lies in the relative commutant; the image generator need not equal the fine generator. For a non-unital isometry `V`, the relevant normalized compressed trace can correlate distant factors. Measure-level maps are outside Definition Z. Infinite-dimensional group links need not admit the normalized matrix trace used here. These observations do not prove existence of a replacement.

The digest `prior/ZM1I1A.md` identifies results already proved elsewhere: exact regrouping Z0, its content cost, Z4 and the free Z1–Z2 results in `ZM1.md`; tail rigidity Lemma ER and invariant-image Theorem 3 in `ZM1_OBS.md`; the dyadic even refinement in `ref/main/docs/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md`; the conditional finite-region Peter–Weyl approximation in `ref/main/docs/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md`; and the level-matched isometry in `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`. These are not this proof and do not supply the specified fixed-form map. The digest reports the latter as author statements for review and the Peter–Weyl result as conditional and unaudited. `GA2_Y2.md` Theorem 2.1 separately proves a finite-register obstruction to an invertible covariant link; it is not this trace argument.

The pass-1 literature discussion is context, not a proof input. In particular the claimed finite-abelian equivariant refinement example relies on the stated conventions for the external refinement map and was not independently checked here. The draft marks Trezzini et al. arXiv:2511.23398 Theorem 1, the Balaban/Gawędzki–Kupiainen/Brydges–Federbush sources, and the D-theory search-only references as not verified. No literature absence claim is established.

## 7. Proposed readings and open items

The four-test verdicts below are pass-1 assessments, not adopted decisions. P means pass and C conditional; the tests address target, closure, downstream physics by premise, and added structure.

- **R-G1EQ, proposed: P P C P.** Replace (G1) by G1-eq; retain (G2), disjoint singletons, (Z-a), (Z-b), a unital injective graded map and the same-type coarse law. Gauge-conjugation arguments of `ZM1_OBS.md` Theorems 2–3 and `ZM1.md` Lemma R-GI still apply when their other hypotheses hold. Charged-sector identification needs a separate bridge. **G1-EQ (open):** does such a map exist for some `L≥2` on either five-mode law?
- **R-ISO, proposed: C C C C.** Replace the unital map with an isometric embedding into a specified subspace and intertwine Gauss generators. A rule must fix the subspace; a vacuum or low-energy choice must not assume the dynamical closure sought. The classification in `ZM1.md` GAP Attack 3 remains open.
- **R-MEAS, proposed: P C C C.** Use a Euclidean measure-level block map to compare class-(a) data. It needs a specified Euclidean form (Y1), and positive-weight use needs the relevant reflection-positivity result (ST1); it adds structure. Y1 and ZM1-G remain open.

Dropping (Z-a) removes the density contradiction; adjacency and disjointness alone give a graph bijection, not by themselves an identification of the full map or dynamics with a relabelled law. Restricting (G1) to `SU(5)` or enlarging finite embedding sets does not avoid Theorems 5 or 4 on U. Theorem 10 covers other finite registers only when its stated hypotheses hold.

Other named open items preserved from the draft: odd-`m` ice-state tails and ICE-T; finite-`t` U and O witness tails; R-CS and MT1-S charged-sector bridges; GA1-5-Φ and GA1-5-O; LZ1-i[ZM1a]; Y1, ST1, ZM1-G, H-BLOCK and GA2's observable dictionary and propagated errors. The draft does not calculate those tails. Its proposed readings are not owner decisions. No frozen source, working-set entry or axiom is changed by this file.
