# Independent hostile review of STEP55

## PRE-STATED

UTC: 2026-10-29 06:13:03 UTC. Written before deriving any review result.

Target: `STEP55.md`, one normalised RG step on a small-field chart, including a hole. This is an independent mathematical review, not an audit-ledger verdict. Author/model provenance is supplied by the assignment; this document does not independently certify runtime model metadata.

Refutation targets and decisive witnesses:

1. **I2 / BFT-coer.** Rebuild the curvature certificate, weighted energy estimate and local charge allocation. A wrong block scale, overlapping charge counted without its multiplicity, counterexample to an adjoint bound, stale stiffness, or a check that constructs its own expected answer refutes the affected assertion. Independently verify the exact constants and the finite-torus rational where feasible.
2. **I1(a).** Distinguish product-metric Hessians at a current configuration from Hessians in a displaced chart and from the joint-chain Schur complement. Rebuild the one-step pinning mass and inspect the stripe gates. A missing normaliser term, wrong power of L, non-discriminating positivity check, unsupported square-root threshold law, or an uncovered boundary/gauge direction is a refutation or an explicit gap.
3. **Normalisers.** Rebuild complex invariance and the proposed uniform zero-free estimate, including every quantifier in t and the centring function. Identify the exact denominator of a returned activity. A single-kernel theorem substituted for a mixture/integrated denominator, or zero-freeness assumed through the desired cluster expansion, does not discharge the target.
4. **I1(b).** Check whether the stated hypotheses actually imply region-, scale- and volume-uniform analytic cluster expansion, including complex sources and coupling dependence. An uncontrolled Gaussian inverse/square root, omitted smallness condition, or circular hypothesis is decisive.
5. **Geometric mismatch.** Rebuild the pointwise distance-to-action conversion with its N, theta and plaquette margins; distinguish a bad coarse plaquette from a large principal logarithm outside a fixed chart.
6. **Systemic defects.** Pin symbols to current locating strings and line numbers; recompute parameter-dependent minima and thresholds; ask of each inspected gate whether it could fail. Locate PROOF citations by string and inspect only the necessary ranges.

Constraints: no git; write only this file, incrementally; no snapshots or audit ledgers; bounded reads of the named sources and at most two additional files; exact rational/symbolic arithmetic in plain Python only, no floating-point linear algebra or long jobs. No scientific status is inferred from a source label. Review findings use CONFIRMED / NOT-VERIFIED / REFUTED; claim status uses PROVEN / ARGUED / CONDITIONAL / GAP / OPEN.

Read accounting at start: named target and the user-named `docs/ai_methodology/SCIENCE_WORKFLOW.md`; additional file 1 is `/Users/jonBridger/.codex/skills/review-loop/SKILL.md` (review procedure only, subject to the owner's narrower scope). Remaining reads will be recorded below. No derivations or check executions preceded this section.

## Findings (appended as derived)

### R1 — CONFIRMED: linear certificate and local coercivity (claim PROVEN)

Attaches to `STEP55.md:129–196`, locating strings `Lemma ST`, `Lemma CERT`, `Theorem LC`, `Theorem LC-loc`.

Independent derivation: the straight block average satisfies dQ = Q₂d by summing oriented fine plaquettes in each L-square; the axial contribution is an exact coarse gradient and disappears. Q₂ has row sum L² and column sum L⁻² in four dimensions, so its norm is at most 1. Q_str has row sum L and column sum L⁻³, so its norm is at most L⁻¹. For a co-closed coarse form s, Qᵀs = Q_strᵀs and d*Qᵀs = evᵀd*s = 0. Thus the transpose contraction iterates on d*Ξ, although it does not hold on arbitrary link fields.

Writing Ξ_i = (Q₂ᵀ)^(k−1−i)Ξ and r_i = QB_i−B_(i+1), telescoping gives

    <dB_k, Ξ> = <dB_0, Ξ_−1> − Σ_i <r_i, d*Ξ_i>.

The squared norm of the energy-dual vector is at most

    [2 + 32 Σ_(m=0)^(k−1) L^(−2m)/κ_(k−1−m)] ||Ξ||²,

because ||d*||² ≤ 16 and ||d*Ξ_i|| ≤ 4L^(−(k−1−i))||Ξ||. Weighted Cauchy–Schwarz proves the stated lower bound for every chain, hence for its infimum. At L=3 and κ_i=1, the constants are exactly 1/34, 9/338, and 1/38 for k=1, k=2, and the uniform limit. No stale minimum or stiffness substitution was needed.

For Ξ=1_S dB_k, the pairings only read their supports, so the identical inequality uses the restricted energy. The iterated Q₂ᵀ support in the plaquette plane is [0,2L^m−2]² and in its transverse coordinates [0,L^m−1]²; applying d* adds only the boundary links. This proves the no-tail, 2×2-block charge allocation for the linear tower. One certificate for the entire set S avoids a multiplicity loss; summing separate per-plaquette energy bounds would not. Extension to a punctured region requires these supports and all averaging identities to remain inside that region. This does not establish a normalised nonlinear PRICE theorem.

### R2 — CONFIRMED: the finite-torus minimum is 199017/6430226; this check can fail (claim PROVEN)

Attaches to `STEP55.md:601`, `:703`, `:740` (locating strings `exact Rayleigh quotient`, `exact minimum`, `true minimum`) and `checks/st55_1_lc.py:335–511` (`sector`, `AE_matrix`, `C2 (designed FAIL)`).

I did not rerun the large fine-lattice solve. I independently eliminated the fine gauge and Fourier modes using only exact Fractions. For each coarse sign sector χ∈{±1}⁴, let m be the number of minus signs. Longitudinal coarse data have zero energy. On transverse data, Q_root may be replaced by Q_str, since their difference is a coarse gradient. For each fine alias p, put S(p)=1+e^(ip)+e^(2ip). A plus coordinate has its only nonzero averaging alias at p=0, with (|S|²,|e^(ip)−1|²)=(9,0). A minus coordinate has three aliases with pairs (4,1),(1,4),(4,1). The transverse covariance coefficient in direction μ is

    a_μ = 3^(−12) Σ_aliases [ (Π_ν |S(p_ν)|²) |S(p_μ)|² / Σ_ν |e^(ip_ν)−1|² ].

The fine longitudinal subtraction drops out on coarse transverse vectors because S(p_μ)(e^(ip_μ)−1)=χ_μ−1. The effective-energy/curl ratio is 1/[8m(1+a_μ)]. Exact independent results:

| m | transverse sector supported on minus coordinates | sector on plus coordinates |
|---|---:|---:|
| 1 | absent | 27/238 |
| 2 | 729/11906 | 405/6794 |
| 3 | 59049/1435994 | 6561/162394 |
| 4 | 199017/6430226 | absent |

At m=4, a_μ=30841/3184272. These rational values prove the global non-flat-sector minimum, rather than merely a single-vector quotient. The check's 1/34 lower-bound gate and 1/30 negative control are separated by the actual minimum: 1/34 < 199017/6430226 < 1/30. Thus the core gate is discriminating, not an identity built from c_co. Its script alone reports one Rayleigh quotient; the independent sector comparison above supplies the asserted minimum. The improved PG-based gap, conditional on its separate PG input, is exactly 1/598500000 at κ=1,L=3.

### R3 — REFUTED: st55_3 certifies a global iff threshold or proportionality law (claims GAP)

Attaches to `STEP55.md:790–809`, locating strings `Monotone in τ for every κ_0`, `positive definite iff`, `β_c ∈ (0.118, 0.125)`, `β_c ∝ √κ_0`; and `checks/st55_3_window.py:35–65`, especially `mono = all(...)`, `def mid`, W2 and W3.

The script checks no re-entry between adjacent sampled grid values. It does not prove monotonicity of the matrix, monotonicity of its least eigenvalue, or positivity at every smaller positive τ. A continuous analytic scalar eigenvalue can agree at all sampled points and acquire extra sign changes between them: adding a multiple of Π_grid(τ−τ_i)² leaves every gate unchanged. The positive and negative controls do not test this omission. The certification of an `iff` statement is therefore refuted; whether the actual stripe has a unique first threshold remains NOT-VERIFIED by this evidence.

W2/W3 compare **midpoints of brackets**, not eigenvalue roots. The reported ratios 578/297 and 1768/3465 are exactly ratios of grid midpoints; they cannot certify proportionality. Even assuming a unique crossing in each advertised τ bracket, the supported root-ratio intervals are only 16/9 < τ_c(4)/τ_c(1) ≤ 17/8 and 16/35 < τ_c(1/4)/τ_c(1) ≤ 17/30 (with endpoint strictness depending on whether non-PD means singular or negative). A square-root law is consistent with these bounds, not proved by them. For β, the nonlinear conversion β=2 arctan τ further prevents an exact proportionality inference from τ.

The advertised decimal lower endpoint also rounds inward: alternating rational arctangent bounds give

    0.117511645 < 2 arctan(1/17) < 0.117511646,
    0.124837619 < 2 arctan(1/16) < 0.124837620.

Thus the endpoint evidence supports a zero somewhere after 2 arctan(1/17) and at or before 2 arctan(1/16), or the outward decimal enclosure (0.117511645,0.124837620), not the certified enclosure (0.118,0.125). This refutes the stated certification, not the possibility that the actual crossing exceeds 0.118. No full-space positivity follows from a stripe-subspace calculation. The chart restriction inferred from a negative vector is an upper bound on an admissible chart radius, not a sufficient small-chart theorem.

### R4 — CONFIRMED: exact action, zero-mismatch Hessian, and one-step mass (claims PROVEN)

Attaches to `STEP55.md:243–310`, locating strings `S_eff(U; V)`, `Lemma PSD`, `Proposition OSS`; inherited errors at `LARGE55.md:272` (`total soft action`), `:424–430` (`cβ² < κ`) and `LCONV55.md:412–417` (`against ≈ κu_0`).

Taking minus the logarithm of ρ(U)Π_c[e^(−tφ_c)/N_t] gives −logρ+Σ(tφ_c+logN_t). Replacing φ by ψ=φ−φ_min replaces N_t by the centred normaliser and changes nothing. Thus the omitted-normaliser action in LARGE55 is REFUTED as an exact action, and STEP55's correction is CONFIRMED.

At zero mismatch, write W_0⁻¹M=H+iθI and ρ(0)=0. The exact centred kernel exponent is Nψ=Re tr[(1−e^ρ)(H+iθI)]. The linear term vanishes because ρ is traceless anti-Hermitian. Its second variation is tr(ρ′*ρ′H); the θ contribution vanishes since tr(ρ′²) is real. If H>0, this is positive exactly when D(W_0∘M)v is nonzero. This is the Hessian of the **centred tree exponent**. The Hessian of minus log of the exact normalised kernel also contains the normaliser term and need not have that same exact kernel/nullspace.

For a constant holonomy direction, Qv=Lv on each coarse link but there are L⁴ fewer coarse links. Therefore ||Qv||²/||v||²=L⁻². The HS-normalised one-step Rayleigh quotient is κ_0/L²=κ_0/9, not κ_0. In the Euclidean SU(2) vector coordinates used in st55_2 it is 2κ_0/9. The joint following tower has squared norm ||v||²Σ_(j=0)^K L^(−2j), and only its final residual costs energy, giving κ_K L^(−2(K+1))/Σ_(j=0)^K L^(−2j). This independently establishes the distinction. The inherited missing L⁻² factor is REFUTED when an exact mass or quantitative comparison is intended; plain order notation at fixed L would hide this constant. For a quadratic deficit c_str β², the corrected comparison is c_str β²<κ_0/9: a factor 9 on the squared-angle allowance, a factor 3 on the angle allowance, not a factor 9 on the angle itself.

The product exponential coordinates at the current configuration are normal coordinates for the product bi-invariant metric. For an invariant function, restricting its Riemannian Hessian to horizontal vectors gives the quotient Hessian. Equating this with an arbitrary fixed-coordinate Hessian throughout a finite chart would require another argument; the pointwise statement is the one banked here.

### R5 — CONFIRMED for the tested stripe matrices; NOT-VERIFIED beyond their quantified scope

Attaches to `STEP55.md:391–417` (`G0`–`G3`, `Scope of the check`) and `checks/st55_2_stripe.py:96–181,240–308,326–387`.

I re-derived the Hessian assembly: for S_W=2Σ(1−scalar(U_p)), each factor's second derivative contributes 2 scalar(U_p)|v|² and each pair contributes −4 scalar(the product with the two first derivatives). For a scalar positive SU(2) contour mean M=rI, Nψ=2(|m|−m_0), so its Hessian is 2|m′_vec|²/r. Sixteen coarse sites give precisely the script's factor 16×2/r. Thus the script differentiates the stated tree action, with the same Euclidean-to-HS factor two as R4.

The horizontal restriction also has the right meaning for these subspaces. A tangent in S_(0) has divergence depending only on x_0 mod 3. Orthogonality to every root-pinned gauge tangent requires that divergence to vanish at every non-root site. Each residue class contains non-root sites, so this forces its divergence to vanish everywhere, exactly the script's co-closed condition. The same reasoning applies to S_(0,1); simply counting root-pinned gauge functions within the reduced subspace would give the wrong criterion.

I then reproduced **only** the 36-dimensional S_(0) construction and its 28-dimensional horizontal restriction at five rational τ values, using the inspected author definitions and exact Fraction elimination. This is a bounded reproduction after the analytic derivative check, not an independent implementation of the stripe matrix. Results at κ_0=1:

| τ | positive definite | positive semidefinite |
|---|---|---|
| 1/50 | yes | yes |
| 1/20 | yes | yes |
| 1/10 | no | no |
| 1/17 | yes | yes |
| 1/16 | no | no |

For τ=1/20, κ_0=1/10, the exact quadratic form on v_C is −648621277774440263051216/5459822819225833048875, so the weak-stiffness control is genuinely negative. At τ=1/10, v_C has **positive** conditional quotient 463697495862695858/16104039689207948481 while the restricted matrix is indefinite. A gate checking only v_C would miss this failure; the script's full restricted LDL gate detects it. G0/G1/G3 and the stiffness control are not tautologies. I did not rerun the 108-dimensional subspace or independently reproduce the quoted 0.191/0.062 spectral lower bounds; those numbers remain NOT-VERIFIED in this review. The finite-grid results do not repair R3's interval/iff promotion.

### R6 — CONFIRMED: fixed-width zero-freeness of a single normaliser; REFUTED: the literal SU(2) two-quaternion formula

Attaches to `STEP55.md:320–375` (`Lemma INV`, `Lemma PR`, `Lemma NZ`, `Lemma NZ-R`) and `:378–383` (`tr(V⁻¹M) + tr(M̃V) = 2v·(m + m̃)`); errata S5–S7 at `:673–678` are included.

**Single normaliser (claim PROVEN on its stated small chart, for real t>0).** Complex Haar invariance follows by differentiating ∫f(e^(iσX)V)dV: holomorphy identifies the iX derivative with i times the X derivative, whose Haar integral vanishes. Polar recentering solves P₀(e^(−Y)A−Ãe^Y)=0; on ||Y||≤2|δ|, the displayed contraction has Lipschitz bound at most 0.32 under δ₀,|δ|≤1/40, so the local holomorphic solution exists. It makes E−Ẽ scalar, removing the first-order term in log V. With E_s=(E+Ẽ)/2,

    |R(V)| ≤ [||E_s|| + C_N|ϑ|/N] s(V) = ε_E s(V).

Near I, s has a positive quadratic minimum, so Haar{s≤r} is bounded above and below by fixed multiples of r^(D/2); compactness extends the needed bound to the whole group. This yields A_N=sup_(λ>0) λ E_λ s<∞. Integrating −d(log Z)/dλ=E_λs bounds Z((1−ε)λ)/Z(λ) by (1−ε)^(−A_N), hence E_λ[λs e^(ελs)]≤A_N2^(A_N+1) for ε≤1/2. Therefore the **centred** normaliser ratio satisfies |Z−1|≤K_N ε_E≤1/2. This proves nonvanishing and a bounded analytic logarithm without assuming the desired zero-freeness. Choosing a uniform strict margin in δ₀ gives a positive fixed link width; the width does not depend on real t>0. Cauchy bounds then give an O(1) normaliser Hessian. The bound is for log Ñ_t−log N_t(I,I), not for log Ñ_t itself uniformly in t.

Consequently the rescaled exact-action Hessian differs from the tree Hessian by O(N C_Ncal/u_0)=O(g_0²) at fixed N,L. This statement does not supply a zero-free domain in an independently varied **complex coupling** t, or for an integrated returned denominator.

**SU(2) formula (claim REFUTED as printed; repair explicit).** With the ordinary quaternion convention actually used by st55_2, M↔(m₀,m_vec), M̃↔(m̃₀,m̃_vec), V↔(v₀,v_vec), direct multiplication gives

    tr(V⁻¹M)+tr(M̃V)
      = 2[v₀(m₀+m̃₀) + v_vec·(m_vec−m̃_vec)].

Thus the corrected scalar is

    ς = [(m₀+m̃₀)² + Σ_(a=1)^3(m_a−m̃_a)²]/4,

not (m+m̃)·(m+m̃)/4 in ordinary quaternion coordinates. The printed plus-sign formula can be made correct only by explicitly defining m̃ as the **dual quaternion** (m̃₀,−m̃_vec), rather than the quaternion of M̃. This is a concrete symbol/convention collision.

An exact near-identity witness is m=(9999/10001,0,0,200/10001), M̃=M⁻¹. Then the true ς=1 by Haar invariance; the printed convention gives ς=99980001/100020001. The normaliser's coefficient after removing e^(−t) is t²/8, whereas the printed formula gives (99980001/100020001)t²/8. This follows already from ∫_(S³)v_i v_j=δ_ij/4, without any Bessel-zero citation. The real-data formula using |m| is correct with the repaired convention. I do not bank the entire global Bessel zero set from a cited 'classical' label; fixed-width local zero-freeness is independently proved above and does not need it.

### R7 — CONFIRMED: the level-0 positivity mechanism; NOT-VERIFIED: unrestricted holes and a fixed-chart convexity transfer

Attaches to `STEP55.md:419–441` (`Theorem 1S-0`, `(FILL)`), `PROOF.md` locating strings `Lemma N5-coer`, `Theorem N5-sf0`, `Proposition RW-ℓ²`, `Setting N5-bg`.

The local-to-global positivity step can be rebuilt. Each enlarged local compression is K₀+Δ with K₀≥γ₀ and ||Δ||<γ₀. Its shifted inverses exist for every t≥0. With P(t)=Σ_□G_□(t)1_□ and R(t)=−Σ_□1_(Ω_□ᶜ)KG_□(t)1_□, direct multiplication gives (K+t)P=I−R. If the stated row/column walk majorant is ε_R<1, (K+t)⁻¹=P(I−R)⁻¹ exists for every t≥0. A real symmetric K therefore has no eigenvalue ≤0: a negative eigenvalue would make K+t singular at its negative. This argument is not merely 'the inverse exists at t=0'.

The overlap estimate ||P(t)||≤√μ/(γ′+t), with μ≤3⁴=81 for the stated product partition, gives ||K⁻¹||≤9/[γ′(1−ε_R)], hence λ_min≥γ′(1−ε_R)/9. The trivial gauge-fixing decomposition also has the advertised structure: solve Tλ=P_res d*A with T=P_res d*d on residual gauges, set A_P=A−dλ, use A_P⊥dλ and the block Neumann gap. Its explicit numerical constant still uses the separately supplied PG inequality; this review does not certify that earlier PG constant from its label. Positivity with some uniform trivial gap also follows from compactness of the finite block Bloch matrices after proving their nullspace is trivial: dA=0 and QA=0 leave only root-pinned gauge gradients, removed by the slice/residual fixing. This is consistent with the stated one-step mechanism.

Adding the centred-normaliser Hessian gives a positive **gauge-fixed operator** when u_0 λ_*/N>C_Ncal, by the operator norm bound in R6. At a critical point, the invariant tree Hessian annihilates gauge tangents, giving the quotient/slice comparison. At a noncritical point, N5's slice-plus-fixing operator and the quotient Hessian are different objects. A theorem for the former is not a theorem of convexity in one fixed Euclidean chart for a full conditional density. The stripe check separately tests horizontal vectors at its own current point. These scopes must remain separate.

Under actual (FILL), Rayleigh compression proves positivity on a region and its holes. But the proposed sufficient construction in `STEP55.md:435–437` only estimates new plaquettes by 32a²+4a. It establishes membership in the **same** S(ε) only if

    32a²+4a ≤ ε,
    equivalently a ≤ [sqrt(1+8ε)−1]/16.

For example a≤ε/8 and 0<ε≤1 is a simple sufficient margin. 'a small' with no relation to ε does not supply this. The coarse field and mismatch condition must also be extended consistently, keeping the prescribed collar links and their contours unchanged and choosing free coarse links as the corresponding W₀. I bank the compression implication and this repaired fill criterion, not arbitrary smooth/twisted collars. Nontrivial collar holonomy alone is not a proof of nonextendibility; a quantitative obstruction would compare its holonomy with the maximal ε-curvature of a spanning surface. The source's twisted-hole positivity gap remains OPEN.

### R8 — CONFIRMED with explicit premises: nonlinear PRICE certificate; NOT-VERIFIED: B2 as the sole remaining higher-level obligation

Attaches to `STEP55.md:198–239` (`Theorem LC-chart`), S1 at `:659–661`, and `:443–468` (`(HC_k) on the chart`, `(B2)`).

The nonlinear PRICE mechanism is a valid **CONDITIONAL** use of the linear certificate. Replace the exact fine curl and residuals by the actual plaquette logs and the arithmetic-polar mismatch. On one cone the supplied BFT link weights give an O(η²) fine-curl error; the residual-error norms are O(η²) at each level and their dual partners decay as L^(−m), so their sum is O(η²). For a set S, linearity and Σ_P|dA_k(P)|≤√|S| ||1_SdA_k|| give

    ||1_S dA_k|| ≤ c_co(k)^(−1/2) sqrt(E_nl,cone) + C_tot η² sqrt(|S|).

The coarse BCH error contributes 32η², yielding E_nl,cone≥c_co(k)|S|(ε_cl−C_natural η²)_+². The energy comparison is directly N F_tree≥(1−θ_s)E_nl,cone. This proves the asserted PRICE form **after supplying those particular local BCH/BFT bounds**, with no cone tails. The last proof line's E_nl≤N(1+θ_s)F_tree is not the literal inverse of a relative error 1−θ_s; the direct inequality just written gives the claimed (1−θ_s) conclusion without that slip.

Use S1's corrected constant C_R′=22(p_L²+3L^(4+2σ)), not the superseded 19(p_L²+2L^(4+2σ)). The coefficient 22 is conservative: the sharper contour bound |Y|≤p_La gives |X₀−QA|≤11.2p_L²a² and |X₀|≤1.23p_La; two-factor BCH then gives |r−ρ|≤17.2516p_L²a²+4|ρ|²≤22(p_L²a²+|ρ|²). S1 explicitly invokes 1+C²η²≤3/2; that extra smallness must be included when using its constant (for example Cη≤1/√2). With it, the supplied BFT residual bound squares to at most 3L^(4+2σ)L^(−2(k−j))η², as required. It does not follow just from p_Lη≤1/40 and √Nη≤1/100 when C is an otherwise unspecified BFT constant. The identification of the BFT input's ρ with this arithmetic-mean polar mismatch is **assumed** by STEP55 itself (`I assume its ρ ...`, line 215), not verified there or by this review. Thus the corrected abstract implication may be banked; its advertised upstream instance and a normalised, hole-uniform PRICE theorem may not.

For levels k≥1, the three displayed power counts are correct **if** their error operators have the asserted forms: the Wilson spin error occurs once; residual errors sum Σ_n L^(−σn); certificate errors sum Σ_n L^(−n). B2 then bounds the extension vectors with the needed weights. But the covariant replacement of Lemma CERT and its error estimates are not written or derived. In the curved setting D² is curvature, so the exact co-closed invariance used in R1 cannot simply be reused. The per-block PG transfer, finer-level invertibility for the Schur complement, and off-global-chart BFT assumptions are also explicitly additional inputs in §3.7. Therefore **NOT-VERIFIED** as a reduction to B2 alone; status **ARGUED**, with these other obligations preserved. Linear energy coercivity by itself is not a Hessian bound at a nonzero background.

### R9 — REFUTED: Theorem CX's stated hypotheses imply its full background-local conclusion (claim GAP)

Attaches to `STEP55.md:483–512`, locating strings `(H1)`, `(H2)`, `V^#(Y) depending on ... only through their restriction to Y^♯`, `Each added box raises`; and `LINEAR_PACKAGE.md:292–299` (`polymers are *-connected cube sets`). LINEAR_PACKAGE is additional read 2; only the cluster-expansion statement and its nearby qualifications were inspected.

There are two distinct missing steps.

1. **Missing parameter locality gives a counterexample to the literal implication.** H2 requires V_X to depend on **A** only in X, but allows arbitrary holomorphic dependence on (bg,V,ε̂) throughout the region. H1's decoupling statement concerns white noise W, not background dependence. Take K=I, so its exact RW square root is C(s)=I with perfect decoupling, and choose two parameter sites x,y at arbitrarily large separation. Set the sole interaction at X={x} to

       V_{ {x} }(A;z)=h z_x z_y A_x^4/p_A^4,   |z_x|,|z_y|≤1.

   All written H1–H3 bounds hold with H_V=|h|; H4 is met by taking h sufficiently small and the rates sufficiently large (choose the final decay rate above the polymer-counting entropy as well). The mixed derivative at z=0 of the log integral is exactly −h E[A_x^4]/p_A^4, independent of the separation. Any uniformly bounded expansion with each activity depending only on parameters in Y^♯ can produce this mixed derivative only from polymers whose fattening contains both x and y. The asserted exponential bound, together with the stated polymer counting/rate margin, makes their sum tend to zero with separation. This is a contradiction. The counterexample is an analytic quartic remainder, so subtracting constant/linear/quadratic terms in the definition of V_int does not remove it.

   Corrected hypotheses must require locality of **all** parameter dependence of each interaction and of the interpolated operator, or supply a separate localisation expansion with its own estimates. This is exactly relevant to inherited polymers and higher-level background maps.

2. **The interpolation-to-polymer bound is not proved.** The displayed inequality d(Z)≤d(Y)+2√d|Z−Y| is false for arbitrary added boxes. For Y a single box and one distant added box, |Z−Y|=1 while the connecting length is arbitrarily large; under LINEAR_PACKAGE's actual definition the union is disconnected and is not even a polymer. A nonzero interpolation term must be shown to have an appropriate connecting walk and charged for that walk, including any filling/fattening cost. H1's white-noise support property does not itself show the necessary vanishing for disconnected selections.

   This is not a cosmetic issue at k≥1. PROOF's RW(v) explicitly conditions finite-step walk connectivity on a finite-range K; at higher levels the effective Hessian is not finite range. For example a positive matrix I+q(|x><y|+|y><x|), with arbitrarily distant x,y and small rational q, has local compressed inverses but a nonzero one-walk derivative ∂_(s_y)C_xy at zero, whose leading term is −q/2. No selected intermediate boxes connect x and y. A weighted long-jump bound can potentially repair the argument, but neither B2 nor the stated unweighted row-sum H1 supplies it. S8's fattening instruction does not establish the omitted connectivity/cost estimate.

The standard conclusion that a suitably small, genuinely local polymer gas has an analytic exponential representation is not refuted. The claim that the displayed H1–H4 already prove this particular local, uniform RG representation **is** refuted. Theorem CX must be strengthened and re-proved before its status can be PROVEN as an implication in the advertised form.

### R10 — NOT-VERIFIED: the enlarged-box cluster instance uses stale chart/torus quantifiers

Attaches to `STEP55.md:518–525` (`(H1) at level 0`, `(H4) rates`), S8 at `:679–682`, and `PROOF.md` locating strings `ε_* := α_*/(10p_L(4R_* + 5)L)` and `Each Ω^+_□ is a box`.

N5-sf0 gets its small local gauge on boxes of diameter proportional to R_* and requires 10p_L(4R_*+5)L ε≤α_* and T≥4R_*+6. CX then enlarges R to achieve a very large s̄. Reusing the old curvature/mismatch threshold on those larger compression boxes does not follow from the AX proof: the corresponding gauge bound grows with R. One sufficient corrected application is to choose

    ε ≤ α_*/[10p_L(4R+5)L],   T ≥ 4R+6,

and the matching complex neighbourhood for this R. Alternatively derive new compression bounds from the already proved global gap, with recalculated rates and complex perturbation margin. Neither justification is supplied for the existing H1 table entry. This is a stale-quantifier issue, not an obstruction to choosing a smaller fixed chart. The new R may be k-independent, but that does not make its domain identical to the old one.

### R11 — CONFIRMED only as a conditional exponential identity; REFUTED for the full Den_Y logarithmic bound; actual returned denominator NOT-VERIFIED

Attaches to `STEP55.md:530–542` (`Proposition NZ-ret`, `whose denominator is ... of the type of Theorem CX`), S9 at `:683–685`, and `LARGE55.md:465–474` (`INCLUDING every returned activity`).

If an **independently established** convergent expansion represents the actual integral as a nonzero analytic Gaussian/main-term prefactor times exp(ΣV#), its denominator is zero-free. This conditional observation is correct. It is not circular when that expansion has independently verified hypotheses; phrasing it as 'zero-free wherever that expansion holds' does not verify the hypotheses or identify the denominator.

STEP55 has not shown that the history-dependent Den_Y of the actual return operation equals its product-white-noise, single-background integral, with identical boundary data, cut indicators, gauge Jacobian, contour deformation and reference normalisation. Its first sentence assumes that identification. In §5.1 the linear term is subtracted in defining V_int; matching the actual integral requires either a critical point of the exact S_eff or inclusion of that linear term. A critical point of the tree action alone does not provide this after adding log Ñ. Even its displayed expansion has R9–R10's unresolved hypotheses/proof steps. The corrected N5/Hessian and single-kernel results address parts of this construction but do not provide the missing identity. Excluding the ±H mixture on a single-background hypothesis is legitimate **only after showing the actual denominator has that hypothesis**. Actual returned-activity zero-freeness therefore remains **OPEN**, at level 0 as a full return construction as well as at higher levels; it has been moved to a set of obligations, not closed.

There is also an explicit normalisation error after S9. Line 534 bounds

    |log Den_Y(V_complex) − log Den_Y(V_real)| ≤ C |Y| H_V.

S9 restores the missing e^(−S_eff(bg)) and Gaussian determinant factors but supplies no bounds on their logarithmic variations. Nonvanishing of a factor does not make its variation O(H_V). Counterexample: a single Gaussian with K(z)=1+z, |z|<1/2, fixed white-noise cut and V_int=0. Then H_V=0, but Den(z)=N_χ(1+z)^(−1/2) (up to a fixed constant), so

    log Den(z)−log Den(0) = −(1/2)log(1+z) ≠ 0.

Thus the asserted bound for the **full** denominator is REFUTED. The corrected identity is

    Δ log Den_Y = −Δ S_eff(bg) − (1/2)Δ log det Õ + Δ log N_χ + ΔΣ_X V#(X),

with any other normalisation factors likewise included. The O(|Y|H_V) estimate applies to the last term, or to the explicitly reduced denominator after dividing out the other factors. It does not apply to Den_Y as defined by S9. A returned-activity analytic norm still needs cancellation or separate bounds for those factors. This is the same normalisation hazard as the omitted soft-action term, now in a new location.

### R12 — REFUTED without a sign condition; CONFIRMED after repair: geometric mismatch price

Attaches to `STEP55.md:546–568`, particularly `θ_y := 18.4y²(1 + C_N/N)` and `δ_GMI ≥ ... when ε_f′ ≤ ε_cl/2`, with S10's box and single-link corrections included.

The geometric derivation works on the stated nonwrapping box, with a further positivity condition on θ_y. An axial-gauge telescoping path crosses at most 3(2L−1) fine plaquettes, giving link-log bound a. For a contour, the small-chart geodesic bound gives |Y|≤p_La, and the elementary BCH and polar estimates give |X_c−QA(c)|≤13.2p_L²a². In particular |X_c|≤p_La+9.2(p_La)²≤1.23p_La, which is stronger than the 1.33 used in the text. Four such errors contribute at most 52.8p_L²a²; the four-link BCH error is at most 2(5.3p_La)²=56.18p_L²a². Their sum is 108.98p_L²a²≤109p_L²a². Intertwining dQ=Q₂d then gives exactly the claimed ε_f′ bound, including 32L²a².

The telescoping difference of four unitary links gives max_c||V_c−W_c||_op≥(ε_cl−ε_f′)/4. For U′=V⁻¹W, the positive matrix I−(U′+U′*)/2 and the scalar imaginary-part bound give

    ψ(V) ≥ (1−θ_y)||V−W||_HS²/(2N).

**If 0≤θ_y<1**, the norm comparison and ε_f′≤ε_cl/2 therefore imply the pointwise price (1−θ_y)ε_cl²/(128N). The factor 128 is correct. This is for a bad coarse plaquette in the specified operator-distance predicate, not an arbitrary unrelated log cutoff or a whole product of kernel factors. S10 correctly restricts the pointwise kernel bound to a mismatching link; normalisation and overlap costs of the other factors remain separate.

But p_La≤1/40 does **not** imply θ_y<1 for all N≥2. The displayed constant C_N grows cubically with N. The omitted sign hypothesis can even falsify the literal δ_GMI comparison. Exact permitted parameter values are

    N=20, L=3, p_L=11, f=1/6600, a=1/440,
    y=11/400, ε_cl=1/2, C_N=4020,
    θ_y=281083/100000, ε_f′=13741/193600 < ε_cl/2.

These give

    δ_GMI = −1249254944251923/2398781440000000000,
    (1−θ_y) ε_cl²/(128N) = −181083/1024000000,

and δ_GMI is **strictly smaller** than the alleged lower bound. The normaliser mean may still be perfectly nondegenerate: this defect concerns the chosen worst-case error coefficient and the algebraic sign in the deduction. Such a negative 'price' cannot support Peierls suppression; an inequality ψ≥a negative number is vacuous.

Correct the premise to y²<5/[92(1+C_N/N)] (strict positive price), or y²≤5/[184(1+C_N/N)] to retain 1−θ_y≥1/2. At N=20 these are respectively y²<5/18584 and y²≤5/37168. This is a further N-dependent chart condition. The SU(2) application has C_2=0 and does not suffer this particular sign failure. The polynomial prefactor still requires a strictly smaller effective exponent a_mis,eff than the raw price; STEP55 gets that expenditure right.

### R13 — CONFIRMED source distinctions; NOT-VERIFIED provenance assertions not examined

The following symbol pins prevent misleading transfers:

| symbol/object | current source and locating string | distinction required |
|---|---|---|
| κ_0 | STEP55:98, `kernel stiffness`; :299, `One-step (V fixed)` | κ_0/L² in HS units; κ_0^CE in CX is a different constant |
| κ_0^CE | LINEAR_PACKAGE:299, `16 log 12800`; STEP55, `(H4) [rates]` | polymer-counting constant; never substituted for stiffness |
| B2 (check) | st55_1_lc.py:269–288, `B2 co-closed`; STEP55:594 | tests the linear adjoint contraction |
| (B2) (hypothesis) | STEP55:459–466, `derivative of the background map` | nonlinear ℓ² derivative estimate, still OPEN; no st55_1 gate tests it |
| C_1 | STEP55:459, `curvature ≤ C_1`; :495–497, `C_1C_locH_V` | BFT amplitude and CE output constant are distinct |
| C1 (gate) | st55_1_lc.py:485–492; st55_2_stripe.py:382–385 | respectively finite-torus coercivity and weak-stiffness negative control; neither is a theorem constant |
| φ, ψ, φhat | STEP55:104–105, :249 | uncentred φ, centred ψ, and φhat=Nψ; Hessian constants must keep N |
| N_t, Ñ_t, Den_Y, reduced Den_Y | STEP55:105, :314–318, :534, S9 | four different normalisation objects; R11 shows why their bounds cannot be exchanged |
| β, τ, plaquette cut | STEP55:113, :394, :427 | β=2 arctan τ is a link angle; the stripe plaquette HS bound is 2√2β |
| m̃ | STEP55:379–381 versus st55_2_stripe.py:20–27 | quaternion coordinates versus dual quaternion coordinates; R6 repairs the sign |

No specific stale **numbered PROOF citation in STEP55** was found: its relevant PROOF references are locating strings. I matched the N5/RW/NA-alg/AX strings to the current text rather than borrowing historic line numbers. This is not a confirmation of every legacy number in LINEAR_PACKAGE or the prior reviews. The actual stale interfaces here are the finite-grid threshold, the enlarged R-domain, the uninstantiated BFT mismatch, and the denominator normalisation.

Gate disposition: st55_1's identities and norm bounds were re-derived; its coarse-energy gate is independently reconstructed in R2 and its overly strong 1/30 bound fails. st55_2's algebra and a bounded subset of matrices were checked in R5. st55_3 has discriminating point tests but cannot decide a continuum monotonicity/iff claim or exact scaling law. I did not authenticate the criteria-file timestamps/hashes, run the large legacy checks, or accept their stored PASS labels as new evidence. No snapshots or audit ledgers were opened.

## Summary table

The milestone **one normalised, history-compatible RG step on a chart with a hole remains OPEN**. STEP55 supplies useful new mathematics, but its final cluster/returned-activity promotions cannot be banked as written.

| finding | review verdict | claim status and disposition |
|---|---|---|
| R1: linear CERT, LC, LC-loc | CONFIRMED | PROVEN: c_co=1/38 and no-tail local charges on the stated linear tower |
| R2: side-2, k=1 exact minimum | CONFIRMED | PROVEN: 199017/6430226; independent Fourier-sector calculation |
| R3: stripe iff threshold and √κ law | REFUTED as certification | GAP: finite point tests do not prove either statement; corrected crossing enclosure supplied |
| R4: exact action, centred kernel Hessian, mass | CONFIRMED; inherited omissions REFUTED | PROVEN: include log Ñ; mass κ_0/L² in HS units |
| R5: stripe point certificates and controls | CONFIRMED on reproduced S_(0) cases | PROVEN at those five rational points; unexecuted larger cases/margins NOT-VERIFIED |
| R6: single-kernel zero-freeness and normaliser derivative bound | CONFIRMED | PROVEN for real t>0 on a fixed sufficiently small complex field neighbourhood |
| R6: printed SU(2) two-quaternion convention | REFUTED under ordinary coordinates | PROVEN after replacing spatial plus signs by minus signs, or explicitly using dual coordinates |
| R7: level-0 gauge-fixed positivity and hole compression | CONFIRMED as scoped | CONDITIONAL on the stated local operator bounds and actual FILL; unrestricted collars OPEN |
| R8: nonlinear local tree PRICE | CONFIRMED as strengthened implication | CONDITIONAL on the matching arithmetic-mismatch BFT input and explicit smallness; its upstream instantiation NOT-VERIFIED |
| R8: B2 alone closes higher-level positivity | NOT-VERIFIED | ARGUED: covariant certificate, PG transfer and domain/invertibility inputs remain |
| R9: CX as the displayed full local implication | REFUTED | GAP: missing parameter locality and interpolation connectivity/cost proof |
| R10: existing level-0 chart survives enlarged R unchanged | NOT-VERIFIED | GAP: use the new R-dependent domain or prove replacement compression bounds |
| R11: exponential representation implies zero-free denominator | CONFIRMED | CONDITIONAL on an independently proved expansion of that exact denominator |
| R11: full-denominator O(|Y|H_V) logarithmic variation | REFUTED | GAP: missing main-term/determinant/cut-normalisation variations |
| R11: actual normalised returned activity | NOT-VERIFIED | OPEN: exact denominator identification, uniform complex domain and analytic norm |
| R12: geometric mismatch implication | CONFIRMED after repair; unrestricted sign deduction REFUTED | CONDITIONAL on θ_y<1, the strict curvature margin, the stated box and predicate |
| R13: source/gate distinctions | CONFIRMED as scoped | B2-check is not B2-background; chronology and legacy PASS provenance NOT-VERIFIED |

## Numerical and formula corrections

| assertion being rejected | corrected statement / independent derivation |
|---|---|
| Certified β threshold bracket (0.118,0.125) from the grid | A crossing lies in (2 arctan(1/17),2 arctan(1/16)), enclosed outward by (0.117511645,0.124837620). A unique iff threshold is not established. |
| Midpoint ratios certify β_c∝√κ | 578/297 and 1768/3465 are midpoint ratios only. Even assuming one crossing, τ-root ratios are bounded only by (16/9,17/8) and (16/35,17/30); no exact law follows. |
| Inherited holonomy mass κ_0 | κ_0/L²=κ_0/9 in HS units; 2κ_0/9 in the script's Euclidean SU(2) coordinates. The squared-angle condition tightens by 9 and the angle condition by 3. |
| Ordinary-coordinate SU(2) ς=(m+m̃)²/4 | ς=[(m₀+m̃₀)²+Σ_a(m_a−m̃_a)²]/4. The rational near-identity witness gives 1, not 99980001/100020001; the t² coefficient is 1/8, not 99980001/(8·100020001). |
| Full Den log variation is zero when H_V=0 | A Gaussian with K(z)=1+z has Δlog Den=−(1/2)log(1+z). The corrected bound must include the determinant and main-term variations. |
| GMI's δ≥(1−θ)ε_cl²/(128N) follows without checking the sign | At the admissible N=20 parameters of R12, θ=281083/100000 and δ=−1249254944251923/2398781440000000000 < −181083/1024000000. Require θ<1, equivalently y²<5/[92(1+C_N/N)]; at N=20, y²<5/18584. The factor 128 itself is correct after this repair. |
| Small collar links alone verify FILL at the same ε | The stated construction needs 32a²+4a≤ε, e.g. a≤ε/8 for ε≤1, plus a compatible coarse-field extension. |
| The old ε_*(R_*) can be inserted unchanged after enlarging R | A sufficient replacement is ε≤α_*/[10p_L(4R+5)L], with T≥4R+6 and the matching complex domain. |

The already corrected source errata (19→22, its revised θ_s, S7's D factor, S8's larger rate threshold, and S12's κ=4 arctangent rounding) are not counted as newly discovered numerical refutations.

## Read and execution record

Named scientific sources inspected, by locating-string searches and bounded ranges: STEP55.md (through S13); PROOF.md (NA-alg/NA-FP, N5-bg/AX/N5-an, N5-coer, RW/N5-sf0/RW-ℓ² passages); LARGE55.md; LCONV55.md; CODEX_REVIEW_LARGE.md; CODEX_REVIEW_LCONV.md; and the three named check scripts st55_1_lc.py, st55_2_stripe.py, st55_3_window.py. The user-named SCIENCE_WORKFLOW.md was read for the operating contract. The two additional reads were the review-loop SKILL.md and LINEAR_PACKAGE.md's cluster-expansion statement/nearby qualifications. No other scientific file was opened. The criteria/output files cited by the author were not opened or treated as authenticated evidence.

Arithmetic actually executed: an independent Fraction-only Fourier alias sum for all four non-flat coarse character types; exact rational arctangent enclosures; the five-point S_(0) stripe reproduction and one weak-stiffness control; the exact N=20 GMI sign counterexample. No NumPy, BLAS, quadrature, git, long worker or auxiliary artifact was used. Only CODEX_REVIEW_STEP.md was written. Source text was not edited. This report was written incrementally, starting with its timestamped PRE-STATED section.

Completion UTC: 2026-10-29 06:50:54 UTC. Citations include locating strings; STEP55 was checked through its 812-line version ending with the st55_3 provenance amendment.

## Exactly what may be banked

1. **PROVEN:** the linear dual certificate, E_k≥c_co(k)||dB_k||², c_co=1/38 for κ=1,L=3, and the simultaneous local cone charge without tails; on punctured regions only where the full averaging/support identities stay inside the region. The exact k=1 side-2-torus minimum is **199017/6430226**.
2. **PROVEN:** the exact conditional action with its centred normaliser; the centred tree-kernel Hessian tr(ρ′*ρ′H) at zero mismatch; the one-step holonomy mass **κ_0/L²**; and the distinct vanishing joint-chain mass. The reproduced S_(0) stripe matrices are positive at τ=1/50,1/20,1/17 and indefinite at τ=1/10,1/16 for κ_0=1. These are point certificates with a crossing between 1/17 and 1/16.
3. **PROVEN:** complex Haar invariance, local complex polar recentering, fixed-field-width zero-freeness of a **single** normaliser uniformly for real t>0, and the O(1) Hessian bound for its centred background dependence. Use the corrected dual-quaternion convention for the SU(2) closed form. The corresponding exact-action perturbation is O(g_0²) after rescaling the tree Hessian.
4. **CONDITIONAL:** the level-0 gauge-fixed positivity argument on its correctly quantified small-field domain; positivity of its Dirichlet compression when actual FILL holds; and the nonlinear **tree-level** local PRICE bound with the matching arithmetic-mismatch BFT input, corrected constants and additional smallness stated in R8.
5. **CONDITIONAL:** the geometric bad-plaquette ⇒ some-link-mismatch implication and coefficient **(1−θ_y)ε_cl²/(128N)** under θ_y<1, ε_f′≤ε_cl/2, and the specified nonwrapping box/plaquette predicate. It supplies a pointwise price on the selected kernel link, with a strictly smaller effective exponent after absorbing polynomial prefactors.
6. **CONDITIONAL:** an independently established analytic exponential representation of the **actual** returned denominator, with nonzero prefactors, implies zero-freeness. Its instantiation here, the full returned-activity analytic norm, higher-level curved positivity, twisted-hole control, reference comparison and failed-return treatment remain **OPEN**. The most dangerous unverified item is the cutoff-, history- and region-uniform zero-free complex domain for the denominator that the actual returned activity divides by.
