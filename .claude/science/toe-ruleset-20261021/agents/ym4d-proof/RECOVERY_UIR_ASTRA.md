Continuation author runtime: gpt-6-astra; reasoning effort: max (coordinator/tool dispatch metadata; this worker's visible system identity says GPT-6 generically).

# Recovery of the interrupted UIR continuation

## PRE-STATED

This is a bounded interactive continuation, with no git operations, audit verdict, landing, or publication. Writes are restricted to this note and `checks/recovery_uir_*`. Claude's `UIR2_55.md` is preserved unchanged. The supplied baseline is `46dc04b05c5842a03ae3af64caa77628f099128f`; git freshness is deliberately not rechecked because the handoff prohibits git. Methodology is the named worktree snapshot: `AGENTS.md`, `docs/ai_methodology/SCIENCE_WORKFLOW.md`, and its physics-loop skill/references, with the handoff's narrower scope overriding campaign, git, and packet mechanics.

Before this block I read the complete 320-line `UIR2_55.md`, the historical worker brief, the repository operating map, and the physics-loop discovery, claim-status, and delivery references. A combined earlier tool read of the reviews was truncated; it is not counted as complete coverage. No new derivation or check execution is claimed before this block.

Targets and quantified domains:

1. Check the fixed-depth, finite-volume residual determinant identity and its exact quadratic expansion; distinguish off-shell and saddle identities.
2. Test the sufficiency of (IC), and the actual leading-operator matching claimed under (IRL)/(IRW), before using either to infer a bounded or zero residual coefficient. The discriminating failure is an admissible homogeneous integrand whose required limit does not exist, an omitted operator block at the same infrared degree, or a mismatch under an explicit block determinant calculation.
3. Recover the strongest rigorous version of the tree-jet statement: distinguish uniform bounds for each torus, convergence/consistency as the torus grows, and identification of the analytic critical action with the actual minimum-defined consumer.
4. Complete a concrete missing lemma if its prerequisites can be established in this bounded continuation. Otherwise give the exact defect and a constructive next lemma, without upgrading a reformulation to closure.

Pre-stated check contract: criteria are saved before each script; verdicts use exact rational/symbolic arithmetic or analytic proofs. Controls deliberately alter a hypothesis or omit a load-bearing term. Failed checks and wrong candidate formulas remain visible. A finite model checks algebra only, never the full Yang–Mills action or an infinite-volume limit. No target is treated as a physical premise.

Pre-statement saved UTC: 2026-10-29T10:48:46.408196+00:00

## 1. Fixed-volume identities and the first exact obstruction

Read coverage now includes the full `CODEX_REVIEW_UIR.md`, `CODEX_REVIEW_LANEA.md`, and `CODEX_REVIEW_B2.md`, UIR55 §§2–3, 3.5′, 5, 7 and its late errata; the relevant definitions in FLOW §§0/3, BFT_A §1.1, BFT34_55 §§1.1–1.3, and the finite-chain/germ arguments in CODEX_REVIEW_ASSEMBLY R3/R6. Large PROOF reads were bounded around NA-alg, the normalized-chain definition, Setting N5-bg and TOWER-VAR. Source statements, not their status labels, determine the claims below.

### 1.1 VS and the quadratic chain rule survive at fixed regulator

Use the same normalized φ action, a regular finite-dimensional gauge stratum, a fixed zero-mode prescription and a neighborhood where all inverses/determinant branches exist. Let `Z=F_UU+D_U D_U*`, `Y=F_UV`, `X=F_VV+D_V D_V*`. At the fine saddle, fine invariance gives `D_U*Y=0` and `F_UU D_U=0`. The Schur complement of Z is therefore `Hess T_n+D_V D_V*`. Taking the opposite Schur complement gives the stated Φ representation.

At ρ=0, `Y=−M*Π`, `X=Π+DD*`, and `Z=H_W+M*ΠM+D_U D_U*`. The elementary identity `Π X^−1 Π=Π` cancels the soft term in `Z−YX^−1Y*`. On the transverse/gauge decomposition, `det X=det_E(Π) det′(D*D)`, and `det_E Π=det_E(PCP)^−1`. This cancels the remaining group and ghost determinants. Thus **Φ(U,0)=0** wherever these finite-regulator expressions are defined. This argument does not require off-shell transversality of H_W.

Colour invariance kills the linear functional Φ_ρ(1,0). Differentiating the composition gives exactly

`D²Δ_n[v,v] = 2 Φ_Uρ[ζv,ρ_1] + Φ_ρρ[ρ_1,ρ_1]`.

At the trivial point the linear stationarity identities give `ρ_1=C H_n v`, `d*C^−1ρ_1=0`, `h_1ρ_1=0` and `Πρ_1=H_n v`. These are finite-regulator algebraic statements. They establish neither continuity of the complete pulled-back coefficient nor the size of its infrared limit. In particular I do not certify every term of LOC's proposed coefficient decomposition merely from covariance.

### 1.2 The displayed IRM matrix reintroduces the off-shell defect

UIR2_55 §1.6 asserts both that the Schur operator has **zero fine gauge rows at the saddle**, and that the top-left block of its auxiliary `J_LS` is the full off-shell `H_W+D_U D_U*`. These are different operators. The full Wilson block generally has a nonzero transverse–gauge entry fixed by the Wilson equation of motion. UIR55's exact identity is `R_UU D_U=−H_W D_U`; dropping this completion repeats the defect identified in CODEX_REVIEW_UIR R11.

An exact two-sector test makes the discrepancy visible. Put

```
W(t) = [ a  bt ]                 J_bad(t) = [ a  bt  bt ]
       [ bt c ]                            [ bt c   0 ]
                                             [ bt 0   c ],
```

with a,c>0 and b≠0. W is the off-shell fine transverse/gauge block; the additional level coupling is B=(bt,0), precisely the displayed projected external coupling. Then

`det J_bad = ac²−2cb²t²`, while `det(W⊕c)=ac²−cb²t²`.

Thus the claimed identification of these printed operators fails already at quadratic order. For a=c=b=1, `½log det J_bad−½log det(W⊕1)=−t²/2+O(t⁴)`. All matrices are positive for sufficiently small real t, so the mismatch is not a zero-mode or logarithm-branch artifact. This is a counterexample to the displayed block manipulation, **not** a model of the actual Yang–Mills residual and not a value for Ρ_n.

The corrected algebraic matching lemma is exact: for an arbitrary finite transverse block A, gauge block C, cross block B and an invertible free fine-gauge block C₀, let

```
W = [ A B ]             J_corr = [ A  0  B ]
    [ B* C ]                      [ 0 C₀  0 ]
                                  [ B* 0  C ].
```

A simultaneous row/column permutation gives `det J_corr=det C₀ det W`. Changing the sign of B is harmless by gauge-variable conjugation. This is the legitimate version of the desired cancellation. Its field-theory application requires proving that, after the fine gauge-row completion and coarse transverse elimination, the actual leading blocks are A,B,C of the Wilson operator and that the remaining terms have vanishing scaled trace integral. The gauge-row identities alone do not determine the transverse block A or establish those remainder estimates. Consequently IRM is **not proved as the printed implication of (IC)+(IRL)+(IRW)**; a corrected principal-block matching hypothesis is still needed.

## 2. A corrected infrared limit lemma

### 2.1 What (IC) does not state

UIR2_55 §1.5 uses the **total** homogeneity of a two-centre integrand to infer integrability at each centre. That inference needs separate subdegree bounds. With `λ(K)=Σ_μ4sin²(K_μ/2)`, the rational periodic example

`g(K,P)=1/[λ(K)² λ(K+P)]`

has exactly the named real singular points K=0 and K=−P, and leading total degree −6. For each fixed nonzero small P it is not integrable at K=0: there it is a positive constant times |K|^−4, whose four-dimensional radial integral is `∫dr/r`. Hence the literal algebraic/degree clauses of (IC) do not imply its claimed integrability. If “trace” is intended to impose additional cancellation or integrability, that is an extra hypothesis which must be stated and proved on the grouped trace. This is a counterexample to the degree criterion alone, not an asserted term of Φ.

There is a separate repairable error in IRD's proof: “degree ≥−5 for Φ_ρρ” does **not** imply that its remainder is continuous at P=0. A convergent example on R⁴ is

`∫ k_2/[|k|⁴ |k+t e_2|²] d⁴k = −π²/t`  (t>0).

Each finite-t singularity is integrable (orders 3 and 2), and the total degree is −5. To derive the value, use `1/(A²B)=2∫₀¹ x/[xA+(1−x)B]³ dx`, translate by `(1−x)t e_2`, and integrate the odd numerator to zero. The remaining numerator is `−(1−x)t`, while `∫d⁴q/(q²+Δ)³=π²/(2Δ)` and `Δ=x(1−x)t²`; all x factors cancel. The result diverges like t^−1. Crucially, multiplication by the two residual factors and division by Wilson's t² density supplies an additional t², so its contribution tends to zero. **Continuity was stronger than needed and false; scaled negligibility is the correct property.** This example addresses the proof's analytic inference, not the parity of the actual summed YM kernel.

The basic transverse core in §1.4 is independently correct:

`∫ k_1²/[|k|⁴ |k+t e_2|⁴] d⁴k = π²/(2t²)`.

Indeed `1/(A²B²)=6∫₀¹x(1−x)[xA+(1−x)B]^−4 dx`. The transverse numerator is unchanged by the same translation, and rotational averaging gives `∫q_1²/(q²+Δ)^4 d⁴q=π²/(12Δ)`. For completeness, the radial integral follows from `∫d⁴q f(q²)=π²∫₀∞u f(u)du` and `∫₀∞u²/(u+Δ)^4du=1/(3Δ)`; the factor 1/4 is the angular average of q₁²/q². The parameter integral yields π²/(2t²). This scalar core alone does not establish the sign, colour multiplicity, or absence of cancellation in the full residual.

### 2.2 Two-centre scaling lemma (proved here)

Let P=tω with |ω|=1, 0<t<r/4. Suppose a measurable scalar or finite matrix kernel on |K|<r is bounded by a finite sum of

`C |K|^−a |K+P|^−b`, with `0≤a,b<4`.

Put s=a+b. Its absolute integral is bounded, with a t-independent constant, by

```
C'                         if s<4,
C'(1+log(r/t))              if s=4,
C' t^(4−s)                 if s>4.
```

Proof: in |K|<2t, scale K=tz. On |z|<2 the two singularities 0 and −ω have fixed separation; the separate conditions a,b<4 make the resulting integral uniformly finite in ω. On 2t≤|K|<r, `|K+P|≥|K|/2`; radial integration reduces to `C∫₂t^r u^(3−s)du`. These two estimates give the stated cases. A finite partition covers variants centred at the other pole. For s<4 the same argument on a ball of radius δ gives a bound tending to zero uniformly as δ→0, so pointwise convergence away from the poles implies convergence of the integral by uniform integrability.

Consequences directly relevant to IRD:

* A remainder in the X coefficient with s≤3 is continuous after integration, provided its pointwise limit away from K=0 exists.
* A remainder in the quadratic-residual kernel with s≤5 obeys `t²∫R_B→0`; in the worst degree-five case it is O(t). No continuity assertion is needed.
* If h_B is jointly homogeneous of degree −6 and has a bound of this type with a+b=6, then h_B(z,ω) is integrable both at the two finite poles and at infinity. Therefore
  `t²∫_{|K|<r}h_B(K,tω)dK → ∫_{R⁴}h_B(z,ω)dz`.
  The large-z tail is O((t/r)²).

For the degree −4 part h_X one needs an additional ultraviolet statement about the *homogeneous model*: uniformly in directions,

`h_X(z,ω)=|z|^−4 H(z/|z|)+O(|z|^−5)` as |z|→∞,

where H is independent of ω. Together with separate-pole integrability this gives

`∫_{|z|<R}h_X(z,ω)dz = A log R + F(ω)+o(1)`, `A=∫_{S³}H`.

This follows by subtracting the degree −4 radial tail outside a fixed ball; the remaining tail is absolutely integrable. Suppose the **full grouped** coefficient satisfies the exact Ward identity `X(tω) ŝ(tω)=0`, and all nonhomogeneous contributions have a continuous limit. Divide the identity by t and then by log(1/t). Since `ŝ(tω)/t→iω`, it gives Aω=0 for every ω, hence A=0. Thus the spherical finite part F exists for the sum, even when individual traces have logarithms. Covariance without these analytic hypotheses is not a substitute for the argument.

If the continuous part is hypercubic covariant, its value at zero is yI in spacetime indices (within a fixed root sector); the unscaled Ward identity gives `(F(ω)+yI)ω=0`. Substitution into the exact quadratic chain rule then gives IRD's transverse-minus-longitudinal formula, with its original normalization and `ρ_1=c_n t²v+o(t²)`. This is a **corrected sufficient infrared lemma**: separate-pole bounds, the displayed large-z expansion and continuity/scaled-negligibility must replace the incomplete (IC) statement. It does not enumerate or verify the actual diagrams.

### 2.3 What a corrected IR matching calculation must supply

The remaining calculation can be finite and decisive at each n: differentiate the exact Φ of §1.1 through total order two, retain the `−½Tr(G δO G δO)` coefficient, eliminate the fine gauge-row defect before forming the model block, and list for each **grouped** trace its two local pole exponents and homogeneous symbol. Pair the ρ factors before assigning infrared degrees. Compare the resulting critical blocks to J_corr, including its transverse block, and evaluate the longitudinal Ward identity with one common regulator/cutoff. The fact that h₁ρ₁=0 removes one external map; it does not remove internal h propagators or their variations.

Once the corrected lemma applies, a particularly economical target is **boundedness of Ρ_n**, not necessarily its value zero. Exact n-independence of the scaled homogeneous combination would suffice. But (IRL)'s list of propagator limits and gauge-row vertices does not by itself prove that every critical-degree vertex or transverse block has that same n-independent limit. Neither UNIV nor IRM may currently be used as a completed proof of boundedness.

Exact check `checks/recovery_uir_01.py` completed once. The output preserves all three failed printed determinant identities. Its 19 correction/control predicates pass; stderr is empty. Those predicates check the finite algebra and degree arithmetic only. The universal claims in §2.2 are established by the estimates above, not by sampling exponents in the script.

## 3. Completing the finite-depth tree-jet transfer

### 3.1 Exact normalization and its limited scope

The actual source definitions match after a fixed normalization, rather than by a same-name identification. BFT_A §1.1 and PROOF's TOWER-VAR use

`F_BFT = Σ_p Re tr(1−U_p) + Σ_{j<n}κ_j Σ_c φ̂_c`, `φ̂=Nφ`.

FLOW §0 uses `s(U)=1−N^−1 Re tr U`. Its corrected normalized tree exponent (FLOW §3.1 erratum) is κφ. With uniform `κ_j=κ`, the **same matrix-valued configurations** therefore satisfy

`F_FLOW,φ = F_BFT/N`.

Choose HS-orthonormal generators e_a for BFT and `t_a=√N e_a` for FLOW. If b are FLOW's colour coordinates, their HS coordinates are √N b. Thus for the value germs and their kernels

`T_FLOW,φ(b) = E_BFT(√N b)/N`,
`K_q,FLOW,φ = N^(q/2−1) K_q,BFT`.

The factors at q=2,3,4 are respectively **1, √N, N**. They are independent of depth and volume for fixed colour rank N. This supplies the missing normalization map, including the coordinate convention. No large-N uniformity is asserted.

For the literal k̃ tower, only finite-order agreement is justified. Here is a direct derivation of the needed order. Near the trivial field, every S4′ contour transporter has a traceless anti-Hermitian logarithm A_i; let `M=Σ_i w_i exp A_i`, `w_i≥0`, `Σw_i=1`. The imaginary part of `tr log M` has zero constant, linear and quadratic terms: `tr A_i=0`, and the traces of `A_i²` and `(Σw_i A_i)²` are real. Hence `θ=arg det M=O(A³)`. Writing the polar decomposition M=WP, the SU(N) candidate `V=W exp(−iθ/N)` gives

`0≤d(M)≤N^−1 tr(P)[1−cos(θ/N)]=O(A⁶)`.

The SU(N) maximizer is analytic near M=1: compactness and the unique maximum at identity keep every global maximizer inside the local implicit-function chart; the Hessian there is the nondegenerate negative trace inner product. Thus d is analytic and its jets through order five vanish. The two composite energies therefore have identical jets through five at the trivial chain. Their nondegenerate stationary value jets through four agree by the explicit formulas below. This proves the needed **jet** dictionary; the false every-background equality for N≥3 remains withdrawn, in agreement with CODEX_REVIEW_FLOW55 §1.2.

### 3.2 Fixed-volume minimum germs for this same normalized chain

Fix finite n,T, odd L≥3, positive κ_j, periodic links, and the S4′ contours/winding convention of the sources. Each normalized φ term and each Wilson term is nonnegative. At top field 1, zero energy forces all fine plaquettes to be 1 and every next-level link to be exactly the S4′ transporter of that flat field. For a flat field the S4′ paths in the relevant contractible blocks have equal transport. Blocking preserves torus-cycle holonomies; top links 1 force every fine cycle holonomy to be 1. Path transport from one root consequently gives a periodic pure gauge, with its restrictions supplying all higher levels. Thus the zero set is one composite gauge orbit with top gauge fixed to 1.

The Hessian on a gauge complement is positive: zero quadratic energy requires `dx₀=0` and `x_{j+1}=Q_jx_j`, with x_n=0. A closed periodic x₀ is a gradient plus its four constant cycle components; the top condition kills the constant components, and the rest are exactly the composite gauge directions. The implicit-function theorem gives a unique analytic value germ on the complement. Compactness of the finite product of groups keeps the energy at V=1 bounded below by some δ>0 outside any chosen neighborhood of that zero orbit. For V close enough to 1 the complement remains above δ/2, whereas the analytic critical value tends to zero. Every global minimum must therefore be that germ. This re-establishes the finite-chain mechanism of CODEX_REVIEW_ASSEMBLY R6 for the now explicit normalization dictionary.

The same conclusion applies to the k̃ chain near 1: it is nonnegative, its zero set at top 1 is the same, and its Hessian is identical. The neighborhoods and δ can depend on n,T. This argument establishes all the finite-volume derivatives at 1 needed here. It does **not** establish one common neighborhood on which a recursively defined minimum equals the analytic action for every n,T; nor does it identify any different local-history action.

### 3.3 JET-∞: exact consistency by a local gauge slice and tree diagrams

**Theorem (fixed-depth jet periodization).** For the normalized local φ-chain just specified, at each fixed n≥1 the derivatives of orders q=2,3,4 of the value germ at the trivial field have translation-invariant infinite-lattice kernels `K_{n,q}^∞`. These decay exponentially at some positive rate that may depend on n. On every periodic coarse torus with side T≥3, its value-germ kernels are the exact periodizations

`K_{n,q}^T(ȳ₁,…,ȳ_q) = Σ_{z₂,…,z_q∈Z⁴} K_{n,q}^∞(y₁,y₂+Tz₂,…,y_q+Tz_q)`.

Consequently they converge at every fixed external tuple as T→∞, and their limit is unique. This is a tree-level consistency statement; it makes no assertion about a one-loop determinant's finite-volume coefficient.

**Proof, including the positivity needed for the inverse.**

1. In every L-block at every level, choose a rooted nearest-neighbor spanning tree wholly inside the block, repeated by translations. Set the links of those trees to 1. A composite gauge transformation is uniquely determined by its root values and by recursively transporting along these trees; starting with top gauge 1 gives a local analytic slice through the trivial chain. Its tangent sets precisely those tree-link components to zero. This construction is periodic and commutes with coarse translations and torus quotients. It need not coincide with BFT's S_E: gauge invariance and uniqueness of the value germ identify the two stationary **values** at each finite n,T.

2. Group all levels and offsets in one top-level cell into a finite list of components. At fixed n, the quadratic Hessian H_n on this tree slice is a finite-range block operator on Z⁴. Its Bloch symbol H_n(p) is a finite matrix of Laurent polynomials, Hermitian for real p. It is positive definite at **every** real p. To see this, suppose its quadratic form is zero. Then the fine curvature and every mismatch vanish. At Bloch momentum p≠0, the fine momenta are `(p+2πm)/L^n`, none zero; the identity `d x₀=0` makes each Fourier component a gradient, since `s∧x=0` with s≠0 implies x=sλ. At p=0 the only additional closed components are the constant harmonic ones. Blocking multiplies each constant 1-form by L at each step, so x_n=0 kills those components. The identity `Qd=d ev` carries the remaining gradients up the chain. Their top potential is zero after subtracting its harmless common constant at p=0. On each block a gradient whose tree links vanish has constant potential equal to its root value. Descending from the zero top potential makes every component vanish. Thus no nonzero slice vector has zero energy.

3. Compactness of the real Brillouin torus and the finite matrix size give `min_p λ_min(H_n(p))=γ_n>0`. The Laurent-polynomial extension is uniformly invertible in some complex strip around that torus. Its inverse therefore has an exponentially decaying infinite-lattice kernel G_n. Neither γ_n nor the strip width is claimed uniform in n. On a finite torus, the discrete Fourier multiplier is the restriction of the same symbol inverse. Fourier inversion gives exactly `G_n^T(x)=Σ_{z∈Z⁴}G_n(x+Tz)`; this series converges absolutely.

4. The original energy's tensors through order four are finite-range, common local tensors on this slice, independent of T. Write its joint variables as z=(x,B), H=F_xx at zero, and `ζv=(−H^−1F_xB v,v)`. Put `c(v₁,v₂)=F_xzz[ζv₁,ζv₂]`. Differentiating stationarity gives the polarized tree identities

   `E₂[v₁,v₂]=F₂[ζv₁,ζv₂]`,

   `E₃[v₁,v₂,v₃]=F₃[ζv₁,ζv₂,ζv₃]`,

   `E₄[v₁,v₂,v₃,v₄]=F₄[ζv₁,ζv₂,ζv₃,ζv₄]−Σ_{three pairings}⟨c(v_i,v_j),H^−1 c(v_k,v_l)⟩`.

   These follow from `x′=−H^−1F_xB` and `x″[v,w]=−H^−1c(v,w)`; the chain-rule terms combine to the three exchanges. No loop trace occurs. Each term is a finite tree made from local vertices and exponentially decaying edges. At fixed n all sums converge absolutely, with exponential decay at a possibly smaller positive rate.

5. Periodization commutes with the contractions in these **trees**. Root a diagram at the first external position. Expanding every periodized edge assigns an integer image to each traversed edge; since the graph is acyclic, these assignments lift all internal vertices uniquely once the root lift is fixed. The remaining choices are exactly the images of the other external leaves. This is a bijection between the finite-torus contraction sums and the displayed infinite-lattice periodization sums, with absolute convergence justifying rearrangement. A loop graph would retain a winding sum and would require a different argument; none occurs in the tree jets. The identity factors in ζ and coincident derivative indices are allowed local edges/labels, so they do not create a graph cycle.

6. At fixed external positions, every nonzero image in the periodization eventually leaves any fixed box. Absolute exponential summability makes their total tend to zero. This proves convergence and identifies the limit with the stationary tree-diagram construction, completing the theorem. ∎

This is the missing consistency mechanism that excludes the alternating-volume counterexample in CODEX_REVIEW_ASSEMBLY R3: here all tori are quotients of **one** local action and one fixed-depth Bloch inverse. No inference from uniform bounds alone was used. The infinite-volume object asserted here is the value's Taylor kernels obtained by stationary elimination, not an infinite total energy or a global minimum of an infinite group product.

### 3.4 Transfer of the uniform weighted bounds

Retain BFT34_55's **actual** producer hypotheses: (H1), the assembled (H2)_μ, and the required weighted source locality (H3)_μ, or a separately verified implication discharging it. No claim that those hypotheses are unconditional is made here. Include the same-link direct term in the second-derivative envelope formula, as required by CODEX_REVIEW_B2 R5. The producer then gives, in its HS coordinates,

`|K_{n,q}^T(y₁,…,y_q)| ≤ A_q exp[−μ t(y₁,…,y_q)/(q−1)]`, `q=2,3,4`,

with A_q independent of n,T. Choose one `0<m₀<μ/3`. Since diameter≤tree length, the rooted-tree summation gives the weighted row bound

`|||K_{n,q}^T|||_{m₀} ≤ A_q q^(q−2) Z_(μ/(q−1)−m₀)^(q−1)`

up to fixed link/colour multiplicities, where `Z_a=((1+e^−a)/(1−e^−a))⁴`. For q=2 there is just one edge. This is the same valid norm conversion independently checked in CODEX_REVIEW_ASSEMBLY R3.

Now fix n and a finite box of external positions around y₁. For sufficiently large T the torus distances in this box equal the infinite-lattice distances. By §3.3, every kernel entry converges. The weighted absolute sum over that finite box is therefore bounded by the same T-independent constant. Letting the box increase gives the infinite-volume bound by monotone convergence of the nonnegative partial sums. The constant was independent of n, so taking sup_n preserves it. Finally multiply by `N^(q/2−1)` from §3.1.

Thus **the normalization and JET-∞ portions of T1 are completed for the actual fixed-depth normalized φ-chain and its jets through order four**. The resulting common weighted cubic/quartic bound is conditional only on the explicitly stated uniform BFT producer package (plus the fixed source definitions), not on a further unexplained thermodynamic-limit assumption.

The allowed rate must respect CODEX_REVIEW_LANEA R4/R5: use a checked unprimed rate `μ<min(m_Y,m_*)`, choose/recompute its kernel constants and the auxiliary c accordingly, and then choose m₀<μ/3. Do not silently use the larger unverified interval m<m_*′ or the numerical 0.0384 primed rate from UIR55. The lower verified rate is sufficient because this consumer needs some positive m₀, not a preassigned value. No numerical final chart radius is certified here.

## 4. Final theorem and open-input ledger

`actual_current_surface_status: conditional-support`; `target_claim_type: bounded_theorem`; `trace_class: upstream_support`; `reachability_to_target: partially_closes`; `bare_retained_allowed: false`. These are author-side recovery classifications, not an audit verdict.

| Item | Result of this continuation | Exact limitation |
|---|---|---|
| VS / Φ(U,0)=0 / complete quadratic chain rule | PROVED at a fixed regulated finite volume from the normalized action and the stated inverses | No uniform open-background determinant neighborhood or infrared exchange |
| UIR2's printed J_LS≅J_W⊕free identity | REFUTED as the written block manipulation; exact −cb²t² determinant discrepancy | No value or nonvanishing claim for the actual Ρ_n |
| Corrected projected-block determinant lemma | PROVED for arbitrary compatible finite blocks | Its principal-symbol identification with the actual grouped Φ remains to be derived |
| IC's total-degree integrability inference | REFUTED without separate pole bounds; degree-five continuity claim also false | Corrected scaling lemma supplies sufficient bounds; actual diagram verification remains open |
| Scalar transverse core π²/(2t²) | PROVED analytically | Does not certify colour factors, complete vertices, or aggregate noncancellation |
| Source/coordinate normalization | PROVED: E_FLOW,φ(b)=E_BFT(√N b)/N and K_q scales by N^(q/2−1) | Uniform κ and the same local φ-chain; k̃ agrees only through the needed jets |
| Finite-volume minimum germ and JET-∞ | PROVED for the specified finite-depth φ-chain; exact jet periodization and unique T→∞ kernel limit | No n-uniform minimum-identification radius, infinite total-energy minimization, or finite-volume one-loop estimate |
| Common weighted tree jets of orders 3,4 | PROVED as an implication of the actual uniform BFT producer package, using a valid smaller weight | H1/H2/H3 and the corrected same-link estimate remain named prerequisites; use unprimed verified rate |
| (ρ-null), UNIV, UIR and the weaker positive-slope bracket | OPEN for the actual model | No complete grouped residual calculation or bound on its depth dependence was obtained |

**One further scope correction to the interrupted note.** UIR2 §1.7 promotes the nonzero super-marginal scalar core to a refutation of the actual continuous-coefficient route. A nonzero individual integral does not establish that the complete coefficient is discontinuous; cancellation within the relevant group has to be checked. Here the scalar core is confirmed, while the claimed complete-term enumeration and the discontinuity of the summed actual X remain unverified. In particular I do not inherit UIR2's claim that cancellation has already been proved “complete.”

**Weaker flow target.** HINT2_55 §R2.3 requires a bracket for **every increment** `B_n−B_j`, 0≤j≤n. A bound only on B_n from j=0 would not supply that contract. Under the corrected FP/TEL hypotheses and common jets, let a_n=a(J_n). Then

`B_n−B_j = β₀^std(n−j)log L + a_n−a_j − (Ρ_n−Ρ_j)`,
`|a_n−a_j|≤2C_FP`.

A sufficient weaker residual target is

`|Ρ_n−Ρ_j|≤r(n−j)log L+C_R` for all j≤n, with `0≤r<β₀^std`.

It gives HINT2's bracket with `β′=β₀^std−r>0`, `β″=β₀^std+r`, and `R′=2C_FP+C_R`. A uniform bound on Ρ_n is stronger and also suffices; a constant value for n≥1 would suffice even if that value were nonzero. This continuation proves **neither** actual residual estimate. The other nonlinear/remainder hypotheses of F-flow/F-tune remain separate.

**Review compatibility.** I agree with CODEX_REVIEW_UIR's corrected 1/2 bubble coefficient, regulated algebra, conditional FP/TEL, R11's off-shell warning and R12's volume warning. The new matrix test exposes the same off-shell issue in UIR2's replacement matching argument. I agree with CODEX_REVIEW_LANEA's smaller-rate restriction; no unchanged primed interval is claimed. I agree with CODEX_REVIEW_B2's stationary-value identity and its distinction from uniform minimum-action identification. Section 3 establishes the specifically needed finite-volume germ and Taylor-kernel consistency for the same explicit action; it does not override that review's unresolved uniform/background consumer bridge.

**Next exact scientific action:** derive the leading transverse block after the actual fine gauge-row completion in Φ, then compare it with the Wilson transverse block in J_corr. Record the residual vertices and their separate pole exponents together, before evaluating any infrared integral. This directly tests the remaining matching statement. A successful tree-jet transfer cannot substitute for this one-loop calculation.

## 5. Checks, scope discipline and provenance

The additional exact scalar control `checks/recovery_uir_02.py` completed once: **15/15 predicates pass**, including rejection of omitted periodic images and of a missing quartic exchange. It compares rational Gauss–Jordan inverses against the independently summed geometric Green kernel, and substitutes the stationary power series into the polynomial energy before comparing it to the vertex/exchange formulas. Its scope is finite scalar algebra, not the Yang–Mills gauge-slice theorem. Both scripts have empty saved stderr. Criteria, scripts, stdout and stderr are preserved separately; no historical ui2_* artifact was edited or rerun.

Negative-claim discipline: this is **partial-narrowing**, not a global no-go packet. N1's five-family submission requirement is not claimed satisfied; the actual attempted mechanisms are the residual Schur algebra, two-centre scaling, and the independent local-tree construction. N2: the unverified producer and residual conditions are not asserted pairwise independent; no inflated wall count is given. N3: every use of an inverse, normalization, gauge slice, limit and uniform estimate above has its domain stated. N4: the matching prior findings are UIR R11 (same off-shell gauge rows), ASSEMBLY R3/R6 (same jets/limit/germ distinction), and B2 R8 (the stronger uniform action bridge, expressly not discharged here). N5: the finite block counterexample has only its stated algebraic scope, while the tree consistency theorem is lattice-wide at fixed depth; the runner logs spell out their narrower resolutions. N6: no new physical axiom is required or adopted by any construction here; the primitive registry was read and is not used to supply dynamics or analytic closure. N7's strongest counter-route is exactly the missing gauge-row completion: it may restore actual infrared cancellation, so a no-go for rho-null would be unwarranted. N8: the matching historical defect is already recorded in UIR R11 and is explicitly repaired algebraically here. No claim of an exhaustive repository or literature impossibility search is made, and no N-gate PASS is asserted.

The sole written source note is this recovery file. No original source, shared summary, git state, audit ledger, PR or publication was changed by this worker. The baseline commit is coordinator-supplied, not independently queried. Current SHA-256 identities and check timestamps below bind the read source/check bytes; they do not authenticate historical run order of Claude's files. This recovery's own criteria were written in separate completed tool calls before their scripts.

```text
bc10b5cc37c8f10cb339e234a3ca3aa252fd401cfb75476334c8c94aa8f5a6f3  UIR2_55.md
4c6d80473a80714e2a5aa1e241e8835648bbe3c65a7bca38a5758faf3c5accb4  UIR55.md
74860ce5d301819ec626940ff1d6cf1a6326cb9c2639c9329a7f1083e087b952  CODEX_REVIEW_UIR.md
7b2c99e5787741af7a9e51312dea156891cea93b4738037246a8b342382f742b  CODEX_REVIEW_LANEA.md
d7baa377f386e6a6800e6056b87fdaf89b3811dd3845b958050a2176420108ed  CODEX_REVIEW_B2.md
a6a9c59121d33eb197de8c38108279660efbcb924d14f89b61b552cdc5137306  checks/recovery_uir_01_criteria.md
ae6539a9c160cf693b9f77283e9168b76ea205aef94cefa4ab2c323a08f119c3  checks/recovery_uir_01.py
b460fee76555f9b1f73d927d05fe6b16cfc413ac1b54e5c542c7347081190e4b  checks/recovery_uir_01_out.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  checks/recovery_uir_01_err.txt
1b2220fac847a70bc20e3274751bd78dcba49d09bc1ce38f275c5ecaeb555f0a  checks/recovery_uir_02_criteria.md
b14a9406e00520826d40dfa4b6ed6d34a0a3a7307af053afad4568a444568a29  checks/recovery_uir_02.py
e4a955c54e6143491c536a8080e43250e2173b3bcc1e26c5c6c7f9cad8b80778  checks/recovery_uir_02_out.txt
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  checks/recovery_uir_02_err.txt
```

Completion UTC: 2026-10-29T11:10:14.911199+00:00
