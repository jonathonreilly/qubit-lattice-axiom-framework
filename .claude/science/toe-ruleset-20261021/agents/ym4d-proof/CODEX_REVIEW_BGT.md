# PRE-STATED

Recorded 2026-10-29 01:33 UTC, before reading the target's proofs. Prior exposure: the user's summary and a heading/locating-string scan of BGT55.md; no substantive verification yet. This is an independent hostile mathematical review of the on-disk BGT55.md, not an audit-status operation. No git commands; the only permitted write is this file. Large sources will be read through searches and bounded sed ranges. Numerical checks will use integer/rational arithmetic only.

## Scope and acceptance tests

1. **Theorem GA.** Derive the quotient-space transport independently. Check annihilation of the full gauge kernel, pullback of composite-co-closed sources, well-defined induced operators, Neumann convergence, uniqueness, and every factor in the claimed bound. Attempt to break the result by a singular gauge-coordinate map, a wrong alignment, or a defect whose purported source norm is undefined. Distinguish an absolute defect estimate from a relative-Hessian estimate and explicitly revisit CODEX_REVIEW_GAPZ F7.
2. **Slice alignment and S_E.** Derive the actual congruence and its domain; test invertibility and both source identities. Check whether the level-zero spike is a proved lower bound, an upper-bound power count, or an example, keeping the class norm separate from the size of one representation.
3. **Pure gauges.** Check Hessian and gauge-map covariance with the precise tangent convention, background transformation, and source/response norms. The aligned defect must vanish identically, not approximately.
4. **KER_Z and SF_Z.** Differentiate gauge invariance at a critical point and full gauge equivariance at a possibly nonzero top value. Track the derivative-of-gradient term, chart conversion, top residual, signs, transposes, and the exact identity Dρ(z)Ξ′λ = [λ,ρ(z)].
5. **RW♯ and the reduction.** Read the actual banked flat estimates and verify all scale exponents and summations. Test whether the proposed residual weight follows uniformly in k and T. Separate proved implications from unproved all-order estimates and alignment hypotheses.
6. **OC.** Test covariance of every norm component and the selected path conventions; distinguish gauge covariance from an unjustified gauge-fixing bound.
7. **bg55_ga.** Read criteria and implementation before execution; check for writes, floating-point arithmetic, tautological expected values, and disclosed model limitations. Rerunning the author's test is reproduction, not the independent derivation. Add in-memory exact counterchecks where useful.

## Verdict rules

**CONFIRMED** means the stated claim, with explicit hypotheses and scope, survives an independent derivation or an appropriate exact certificate. **REFUTED** requires a precise contradiction or counterexample to the actual quantified claim. **NOT-VERIFIED** records a missing argument, unmatched dependency, or insufficient test without pretending to prove falsity. Every finding will give a file and locating string. The report will end with exactly what may be banked; no global constructive Yang–Mills conclusion will be inferred from a conditional algebraic lemma.

## Exact-check addendum, before the independent computations

After the source reads and the author's runner reproduction, the independent in-memory checks will test: (i) a three-dimensional aligned congruence with quotient Hessian diag(1,n), absolute defect diag(−1/2,0), and the singular threshold defect diag(−1,0); (ii) the sign of conjugation in an exact su(2) bracket basis; (iii) a flat constant rational rotation with a constant current, testing the claimed covariant cut necessity on the entire torus; (iv) the residual and cascade geometric sums at odd L=9, θ=1/2, for which every tested power is rational. Acceptance is exact matrix equality/inequality, never a floating tolerance. These finite checks illustrate the symbolic arguments below; they cannot establish uniformity by sampling.

## Scope and disposition

All filenames below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. The complete 623-line target was read in bounded ranges, including its append-only corrections. Necessary dependency statements and proofs were read in located ranges; this is not a fresh review of every upstream analytic theorem. “Banked input” below means the exact named-input implication in the cited review, not independently authenticated main/audit status. The user's prohibition on git was respected.

**CONFIRMED:** GA as finite-dimensional quotient-space perturbation theory; GA-slice; exact pure-gauge transfer; KER_Z; SF_Z's mixed-derivative identity; real unitary gauge covariance; and RW♯ as an implication of the specified flat estimates.

**NOT-VERIFIED:** general-background (R2), the S_E norm obstruction, and the asserted realization of GA's quantitative hypotheses by §6.5. **REFUTED:** literal (ALIGN-ℓ)(β) together with the claim that Λ_PL satisfies it; the exact factorization/signs printed in §6.3; and §5.1(c)'s ordinary cut condition for covariant divergence. The soft covariance formula also needs a sign correction when Ξ′ is normalized as the alignment requires. These defects do not refute GA.

Target SHA-256, unchanged between initial and subsequent reads:

`516ceddf05987c9fd35b7a9b9c60bc8e98798e1c93e184631990f504d3ef6f46`

## 1. Theorem GA — CONFIRMED; it avoids the condition-number objection in its stated pair

**Locations:** `BGT55.md`, “Theorem GA”, “No relative-Hessian series, no (FWD-0)”, and P10; `HESSREL.md`, “Every perturbative transport off the”; `CODEX_REVIEW_GAPZ.md`, “F7 — The proposed HESS-rel Neumann argument”.

Let K₁=Ran Ξ₁, K_Z=Ran Ξ_Z, Q=X/K₁, and C₁=Ann K₁. The alignment and invertibility of A imply ΥK₁=K_Z, not merely an inclusion. Independently of any estimates,

    EΥ Ξ₁ = ΥᵀH_Z Ξ_Z A − H₁ Ξ₁ = 0,
    Ξ₁ᵀ EΥ = 0,
    Ξ₁ᵀΥᵀS = AᵀΞ_ZᵀS = 0       (S∈cc_Z).

The second equality uses symmetry. Thus EΥ descends to e:Q→C₁ and Υᵀ maps the entire background annihilator to the flat annihilator. No assertion about individual source slots is needed.

Because H₁ is symmetric and ker H₁=K₁, its induced map h₁:Q→C₁ is a bijection: its image is contained in C₁ and has the same dimension. B₁ says precisely that its inverse has norm at most C_b in the **specified** source and quotient norms. Therefore

    h′ = h₁(I+h₁⁻¹e),
    ||h₁⁻¹e|| ≤ C_b δΥ < 1,
    (h′)⁻¹ = Σ_(r≥0)(−h₁⁻¹e)^r h₁⁻¹.

Consequently ker H_Z=ΥK₁=K_Z, and for H_Zx=S,

    [x]_Z ≤ t₊ t_* C_b /(1−C_b δΥ) N_Z(S).

This verifies existence, uniqueness modulo the correct gauge space, and the constant. No positivity, ambient full inverse, forward bound for H₁, or background kernel-equality assumption is hidden in this proof. It works over C with symmetric bilinear Hessians and the corresponding complex norms. That algebraic extension does not itself supply the complex-domain estimates A1–A2.

**Explicit answer concerning my earlier F7:** its literal unaligned-Hessian refutation stands. Its sufficient preconditioned Neumann criterion stands. Its use of a condition number applied to a *relative* defect estimate. GA supplies the different sufficient assumption `||e||_(Q→cc₁)≤δΥ`, and only `||h₁⁻¹|| δΥ` is needed. Once exact alignment supplies membership in cc₁, the matched inverse may indeed be the cc inverse. A general-source inverse is unnecessary here. Any reading of my earlier “full matched flat inverse” as requiring an ambient inverse even after this exact annihilator identification should be narrowed accordingly.

There is an exact nonzero-defect witness against the **universal necessity of a uniform forward bound**. On the quotient use the maximum norm and

    h₁=diag(1,n),       e=diag(−1/2,0),       n≥1.

Then `||h₁⁻¹||=1`, `||h₁||=n`, `||e||=1/2`, and `||(h₁+e)⁻¹||=2` for every n. Add a zero gauge coordinate and take

    Ξ₁=(1,0,0)ᵀ,       Υ=[[1,0,0],[1,1,0],[0,0,1]],
    Ξ_Z=ΥΞ₁,           H_Z=Υ⁻ᵀ diag(0,1/2,n) Υ⁻¹.

Transport the quotient/source norms by Υ; then t₊=t_*=1. This is an aligned, nonzero perturbation with an unbounded flat condition number and a uniform inverse bound. At defect diag(−1,0), the quotient becomes singular, exactly at C_bδ=1. This distinguishes the actual threshold from a missing-condition-number objection.

Accordingly HESSREL's universal sentence is **REFUTED**, while its conditional estimate obtained by substituting `||E||≤C f ||H₁||` is **CONFIRMED**. GA does not prove a Yang–Mills defect small merely by naming it δΥ; that is still the analytic obligation.

## 2. GA-slice — CONFIRMED; the S_E obstruction is NOT-VERIFIED

**Locations:** `BGT55.md`, “Proposition GA-slice”, “Levels l ≥ 1, W = S_E”, and “S_E must not be used as the alignment”; `BFT_B.md`, “Setting EΠ (elliptic slice)”; `CODEX_REVIEW_GSHARP.md`, “unrestricted projected-source closure”.

For Λ_WΞ₁=−I, every x has the unique decomposition x=w+Ξ₁λ with w∈W=ker Λ_W. Directly,

    Υ_W(w+Ξ₁λ)=w+Ξ_Zλ.

Thus Υ_W is invertible exactly when W∩Ran Ξ_Z={0}, equivalently when Λ_WΞ_Z is invertible. This proves the invertibility assertion omitted from the target's one-line proof. For u∈W, symmetry and H_ZΞ_Z=H₁Ξ₁=0 give

    EΥ u=(I+Λ_WᵀΞ₁ᵀ)(H_Z−H₁)u,
    Υ_Wᵀ S=(I+Λ_WᵀΞ₁ᵀ)S          (S∈cc_Z).

The restriction **u∈W** is essential to the first displayed identity. Its repetition in §6.4 must retain that restriction and the chosen chart identification.

The scale conversion in the proposed spike count is correct:

    L^(3k) L^(−3(k−l)) = L^(3l).

If a noncancelled charge of own size comparable to `L^(−3(k−l))π_l` creates a level-zero current of comparable own size, its P0 size is comparable to `L^(3l)π_l`. This is a conditional size calculation. The claimed operator obstruction does **not** follow from it:

1. The displayed charge estimate is an upper bound; a constant or co-closed j_l has no such charge. No admissible background/source or response family saturating the required charge is constructed.
2. A1 concerns the **whole** source in cc_Z. A2 concerns the **whole** Hessian defect at an actual critical background. Their Ward identities can cancel the separately counted slot divergences. Testing arbitrary independent j_l does not automatically test these inputs.
3. The output N is an infimum over slot representations. A large P0 representation is not a lower bound for N. A proof of failure needs, for example, a dual witness bounded on every allowed representation.
4. Charges at level-k roots are killed by Λ_Eᵀ, since Λ_E(x) vanishes there. The omitted root pinning also changes the displayed Green-function formula.

In fact the literal level-zero formula in §6.4, locating “Λ_E^Td^Tj_0 =”, is **REFUTED** as the transpose of the stated pinned map. Write G_X for the mean-zero Neumann inverse on Ñ_X and d_X for its internal-edge gradient. From the minimization definition,

    λ_X^E(x)=−G_X d_Xᵀx₀ + (G_X d_Xᵀx₀)(c_X)·1.

Consequently, with restriction/extension to the box understood,

    Λ_Eᵀq = −Σ_X d_X G_X[χ_X q − δ_(c_X) Σ_(z∈Ñ_X)χ_X(z)q(z)].

The target omits the pinned-root term (and has the opposite leading sign under its Λ_EΞ₁=−I convention). Each corrected bracket is neutral, as a Neumann inverse requires. The exact map annihilates q supported on level-k roots; the uncorrected expression does not incorporate this cancellation. This correction is material to a spike argument, not just notation.

**Disposition:** GA-slice is bankable. Failure of a uniform estimate for the prescribed S_E alignment is **NOT-VERIFIED**. Neither its success nor its impossibility is established by the quoted power count or by the earlier review's statement that a bound “does not follow”. The categorical instruction to abandon S_E is stronger than the supplied evidence.

## 3. Corollary GA-PG — CONFIRMED on the pure-gauge branch

**Locations:** `BGT55.md`, “Corollary GA-PG” and “E_Υ =”; `BFT_B.md`, “Lemma CONJ”; `CODEX_REVIEW_GSHARP.md`, final item 2; `CODEX_REVIEW_TOPCC.md`, final item 3.

For a real SU(N) chain gauge G, let M=M_G and A=M_G^fn. In left-trivialized coordinates, invariance of the complete functional, including transformation of the terminal datum, gives

    H_(1^G)=M⁻ᵀH₁M⁻¹=M H₁M⁻¹,
    MΞ₁=Ξ_(1^G)A.

M is orthogonal for the real Ad-invariant pairing. Therefore

    E_M=MᵀH_(1^G)M−H₁=0

exactly, with no smallness restriction on G. The covariant norm/source definitions are transported isometrically, so t₊=t_*=1. GA transfers the flat bound with the same C_b.

The precise background conclusion is at the critical representative 1^G, and hence at its root-pinned gauge orbit. If Z(V) denotes a chosen branch, equality with 1^G uses that branch's covariance/uniqueness assumption and is equality **modulo the allowed gauge**, unless that representative is selected. This does not prove uniqueness of every critical chain with pure-gauge terminal data. It also does not cover all flat torus backgrounds: flat connections with nontrivial torus holonomy need not be pure gauges.

## 4. KER_Z and SF_Z — CONFIRMED; the soft-covariance sign must be fixed

**Locations:** `BGT55.md`, “Lemma KER_Z”, “Lemma SF_Z”, and “Dρ(z)·Ξ′_zλ =”; `BGT55.md`, “(α) ‖(Ξ′_z − Ξ_1)Λ_Wx‖”; `KFACTOR_OFF55.md`, “ρ := log(V^{-1}W_0)”.

### Kernel inclusion

Let X_λ(x) be the actual infinitesimal action of g=exp(tλ) in the local chart. Differentiating `dF_x(X_λ(x))=0` in direction y gives

    Hess F_x(y,X_λ(x)) + dF_x(D_yX_λ)=0.

At a critical point the second term vanishes. In left coordinates X_λ(0)=−Ξ_Zλ with the target's `d_Zλ=Ad_Zλ(y′)−λ(y)` convention. Hence H_ZΞ_Z=0. Criticality removes the extra term; neither minimality nor positivity is used. This proves inclusion only; equality of the kernel remains GA's conclusion under its smallness hypotheses.

### Root self-current

For arbitrary level-zero λ, let λ_k=ev^(k)λ, so the datum also moves. At the base point the two actual gauge velocities are `−Ξ_Zλ` and `−d_Vλ_k`. Differentiate the joint Ward identity once in an unknown-field direction y. The unknown-field gradient vanishes; the datum velocity is independent of the unknown fields. Thus

    −〈H_Zy,Ξ_Zλ〉 − 〈F_vx y,d_Vλ_k〉=0,
    b_Z(y)=−F_vx y,
    D_Z(H_Zy)=ev^(0→k)ᵀ d_Vᵀ b_Z(y).

This is an exact independent derivation of SF_Z with the printed sign. Here D_Z must be the transpose of the **extension to all level-zero gauge functions**; its restriction to Λ₀ is zero. That distinction reconciles nonzero root charges with composite co-closedness. Only the top soft term contains the datum and hence contributes to F_vx. At the trivial chain its mixed derivative is `−κ_(k−1)r_(k−1)`, giving the stated flat formula.

The identity constructs a current, not an a-priori bound for it. Ordinary total neutrality is not automatic at a background. More precisely, every covariantly constant datum test function μ still imposes `〈q,μ〉=0`; the correct statement is the absence of a universal *ordinary* constant-test constraint.

### Exact covariance, with a consistent generator

Root-to-root contour covariance and equivariance of W₀ imply, on the chosen log branch,

    ρ(U^g)=Ad_(g(c′))ρ(U),
    Dρ(z) X_λ(z)=[λ(c′),ρ(z)].

**CONFIRMED** in this actual-generator formulation. It uses the true nonlinear map; it does not rehabilitate the false covariance assertion for the substituted Q_l^Z.

But the positive-d generator required to perturb Ξ₁ is `Ξ′_z=J(z)Ξ_Z=−X_λ(z)` as a map of λ. Consequently the consistent formula is

    Dρ(z) Ξ′_zλ = −[λ(c′),ρ(z)].

The printed positive sign is **REFUTED under this convention**. Defining Ξ′ instead to be X_λ makes the positive commutator correct, but then Ξ′₀=−Ξ₁ and (ALIGN-ℓ)(α) fails even at η=0:

    (Ξ′₀−Ξ₁)Λ_W = −2Ξ₁Λ_W ≠ 0.

Thus the two uses cannot both be correct as printed. An exact su(2) bracket check with `[e₁,e₂]=e₃`, λ=e₁ and ρ=e₂/5 gives `−e₃/5` along the positive-d generator, versus the printed `+e₃/5`. Changing this sign does not change a norm estimate, but an exact-identity claim must retain it.

## 5. Corollary RW♯ — CONFIRMED as a flat named-input implication

**Locations:** `BGT55.md`, “Corollary RW♯”; `BFT_B.md`, “Lemma TC”, “Lemma RT-cc”, “Lemma FT”, and “Theorem RHT-cc”; `COFUN_CC.md`, “Norms” and “Theorem CC-INV”; `CODEX_REVIEW_GSHARP.md`, “3.1 GF-E”; `CODEX_REVIEW_TOPCC.md`, final item 3.

Fix the printed domain d=4, odd L≥3, positive fixed κ_± and 0<α<θ<1. Let q=k−1−i≥1. The straight transpose's own-unit factor, the level-l current normalization, and conversion to level-(i+1) coarse units multiply to

    L^(−3(l−i−1)) L^(−3(k−l)) L^q = L^(−2q).

This is a sup bound for every current; no extra co-closedness of a transported slot is assumed. Applying RT-cc gives the target's estimate for r_i, with its modified currents ĵ_l.

For the stronger residual weight, all contributions can be checked separately:

    L^((1+θ)q)||s_i^c|| ≤ L^(−θ)||s||_R,
    L^((1+θ)q)L^(−2q) = L^(−(1−θ)q) ≤ 1,
    Σ_l π_l(ĵ_l) ≤ [1+2d/(1−L^(−3))] Σ_l π_l(j_l),
    Σ_l π_l(j_l) ≤ ||j₀^c||∞ + ||j||_Pc/(L^θ−1),
    L^(−2q) Σ_(r=1)^q L^((1−θ)r)
      ≤ L^(−(1+θ)q)/(1−L^(−(1−θ))).

The last line is exactly the G-slot contribution, apart from its factor 6. TOP-cc bounds `||κ_(k−1)r_(k−1)−s_(k−1)||` by C N(S). All constants are independent of k,T. The result is

    max_(0≤i≤k−2) L^((1+θ)(k−1−i))||r_i^c||∞ ≤ C N(S).

RHT-cc plus TOP-cc supplies N_res≤C N(S), and GF-E supplies the orbit field bound. At Z=1 both residual quantities are invariant along Ran Ξ₁, so the orbit seminorm of their sum with the field norm is precisely the field orbit norm plus those residual terms. For k=1 the extra maximum and sum are empty and are read as zero. The estimates hold for every permitted slot representation, hence also after taking its infimum.

This confirms RW♯ with its stated endpoint exclusions. It does not assert a stronger decay for arbitrary configurations, nor a background residual estimate without further transport.

## 6. The proposed analytic realization of GA is not yet a proved reduction

### 6.1 The power conversions are useful upper bounds, not necessity theorems

**CONFIRMED as arithmetic conditional on the own-unit estimates.** **Location:** `BGT55.md`, §6.3 table, “S1”, “S2”, “S3”. With k−l=q+1,

    S1: L^(θ(q+1)+2q) L^(−3(q+1)) · 2κCp_L²L
        = 2κCp_L² L^(θ−2) L^(−(1−θ)q),
    S2: L^(3(q+1)) · κCL L^(−(q+1)) L^(−(2+θ)q)
        = κCL³ L^(−θq),
    S3: L^(3(q+1)) L^(−(q+1)) L^(−q) L^(−2q)
        = L² L^(−q).

The final line has the response norm and the background factor a_qη restored multiplicatively. All displayed sums converge uniformly in depth when the stated inputs hold. If a hierarchical completion really carries each π_l upward at bounded cost, the advertised scalar sum is also valid:

    Σ_(q≥0)(q+1)L^(−θq) = (1−L^(−θ))^(−2).

However an upper bound proportional to k in the weaker norm is not a lower bound for the operator, and does not establish that *every* transfer must use this stronger norm. The claims locating “So the transfer must be run” and “S3 is k-uniform only with (TR-1)” are **NOT-VERIFIED as necessities**. RW♯ and TR give a sufficient scale mechanism for the displayed estimates.

### 6.2 The printed “exact BCH factorisation” is REFUTED

**Location:** `BGT55.md`, “ρ_c = Ψ̃_c·r^{full}_c”, “r^{full}_c := log V − log M̄_c”, and the following “Dρ(z)u = −Ψ̃(z)”.

This already fails to first order on commuting constant links. Choose a single commuting su(N) direction A, set the level-l μ-links to exp(tA), the other directions to identity, and the next-level field to identity. Every relevant S4′ contour has the same product, so

    M̄_c=W₀(M̄_c)=exp(LtA),       V=I,
    ρ_c=LtA,                    r_c^full=−LtA.

An analytic Ψ̃ with Ψ̃(0)=I cannot satisfy the printed equality: the derivative of its right-hand side at zero is −LA and that of its left-hand side is +LA. Equivalently, at the trivial chain the actual derivative is `Dρ(0)u=Q_lu_l−u_(l+1)=r_l(u)`, not `−r_l(u)`.

There is also a distinct map mismatch: generally M̄ is an average of unitary products, while W₀(M̄) is its SU(N) maximizer. The definition of ρ contains W₀. The elementary identity for `log(exp(−a)exp(a+h))` applies with `a=log V` and `h=log W₀(M̄)−log V`; substituting log M̄ silently drops the maximizer map. The corrected local analytic estimates can be built using that map, but the displayed exact factorization is not such a proof.

The exact SG identity itself remains **CONFIRMED**. The target's reliance on SG's literal LA-1 must use the correction in `CODEX_REVIEW_KOFF.md`, “4.2 A literal false local hypothesis”: the coefficient is `W₀⁻¹D_bM̄−Q_cb`, not `D_b(W₀⁻¹M̄)−Q_cb`. That review supplies a qualitative analytic repair, not the unchanged false formula.

### 6.3 Literal (ALIGN-ℓ)(β) and “Γ_PL satisfies (β)” are REFUTED

**Locations:** `BGT55.md`, “the level-l values ev^{(l)}Λ_W(x) are computed from x_l”, “(β) holds by construction”, and §6.5 item 6; `GSHARP55.md`, “ν_PL is computed top-down” and “through the triangular system”.

Here is a contradiction within the actual nested-root geometry, independent of any analytic estimate. Put R=ev^(0→1). For k≥2 there are level-1 sites that are not level-k roots. Literal β at levels 0 and 1 says there are linear maps B₀,B₁ such that, for every chain x with independently variable levels,

    Λ_Wx=B₀x₀,                 RΛ_Wx=B₁x₁.

Set x₁=0 and vary x₀. This forces RB₀=0, hence RΛ_W=0 on all X. But the left-inverse requirement gives

    RΛ_WΞ₁λ=−Rλ,

which is nonzero for λ supported at a level-1 root that is not a level-k root. Contradiction. If β were intended only for positive levels, the identical argument at two consecutive positive levels applies for k≥3.

The proposed Λ_PL does not evade this. Its level-i gauge values have inherited root values from λ_(i+1), which depend on coarser field levels. For an explicit mechanism, take k=2, x₀=0 and x₁=dν₁ with nonzero ν₁ vanishing at level-2 roots. The top per-level slice conditions fix λ₁=−ν₁. Hence λ₀ cannot be zero despite x₀=0, because ev^(1)λ₀=λ₁. Admissibility of Γ_PL is entirely consistent with this; strict per-level dependence is not.

A **hierarchical** condition allowing dependence on x_l,x_(l+1),… is a plausible intended repair. Under that condition the transpose of a level-l charge may use level l and coarser levels. Its coefficients and norm bounds must be established. “By construction” does not turn the inverse of a triangular gauge system into a diagonal-in-level operator, nor does locality alone prove bounded block-Neumann or funnel estimates.

This refutes the printed requirement/claimed candidate, not all possible aligned congruences. GA-PG is already a counterexample to any such broad negative conclusion.

### 6.4 Theorem R2-glob — NOT-VERIFIED as the claimed nonvacuous realization of A1–A2

**Locations:** `BGT55.md`, “Theorem R2-glob”, “(A1) from 6 (α)”, “one OPEN item, (ALIGN-ℓ), plus ARGUED expansions”, and §12 item 2.

If one separately assumes GA's two quantitative bounds, the conclusion follows by §1 of this review. But the listed conditions do not yet supply them through the displayed argument. Literal β is impossible; the exact expansion needs correction; the pinned completion is not the operator written; and the claimed estimates are not established for the full sources in the representation-infimum norm.

There is a further quotient issue to make explicit. GA-slice computes EΥu on u∈W. A bound there by `Cη|||u|||♯` yields A2 only if one controls the chosen W representative by `[u]♯`, or supplies an intrinsic quotient estimate by another argument. PL-adm proves bijectivity of a finite-dimensional gauge map, not that representative bound. The near-identity estimate in α for `(Ξ′_z−Ξ₁)Λ_W` alone does not state a bound for `Π_W=I+Ξ₁Λ_W`. Nor does it by itself compare the flat sharp norm with the covariant sharp norm after the J(z) chart change.

The concrete remaining sufficient estimates are:

    [Υx]_(Z,♯) ≤ t₊[x]_(1,♯),
    N₁(ΥᵀS) ≤ t_* N_Z(S)                     (S∈cc_Z),
    N₁((ΥᵀH_ZΥ−H₁)x) ≤ Cη[x]_(1,♯),

with an actually constructed invertible aligned Υ, all constants uniform in k,T, and `C♯ Cη<1`. A corrected hierarchical completion must prove these inequalities, not just estimate one displayed current. This review establishes neither impossibility nor target-equivalence of that remaining construction.

**Dependency freshness:** the target's statement that higher-order TR remains open has been superseded within this on-disk review set. `CODEX_REVIEW_HIGHER.md`, §6 and “Exactly what may be banked”, item 4, now confirms TR∞ and CC-CRIT∞ as qualitative named-input implications. Its checked formula is

    ||r_i^c(z)||∞ ≤ κ_-⁻¹L^(−2q)η[κ₊+(2A_s+qA_j)η]

for the actual critical point in the global 𝔐/data ball, with its corrected all-order source bookkeeping. This supplies the relevant **background's own residual** input when those hypotheses match. I read that input and its assembly; I did not rerun the HIGHER packet or independently certify its entire local analytic proof. The corrected KOFF/HIGHER results improve the inputs, but neither supplies the missing aligned source/quotient estimates. BFT-0's existence and branch hypotheses also remain explicit; this review does not establish them.

## 7. Lemma OC — CONFIRMED for real unitary chain gauges

**Locations:** `BGT55.md`, “Lemma OC (the statement is frame-free)” and the definition of N_Z; `BFT_B.md`, “Covariant local-sup norms” and “Lemma CONJ”.

The coordinate identity `F_(Z^h,V^h)(M_hx)=F_(Z,V)(x)` gives the general congruence

    H_(Z^h)=M_h⁻ᵀH_ZM_h⁻¹.

For unitary h this equals the printed conjugacy because M_h is orthogonal. On gauge functions,

    d_(Z^h) M_h^fn = M_h d_Z.

The gauge subspaces therefore correspond, as do sources by `S↦M_h⁻ᵀS`. Every transported difference or box-corner oscillation is rotated at a single common output site. Taking its Ad-invariant norm preserves its size. The true residual linearization transforms in its own output fibre, so its norm is preserved as well. Transporting each source representation, and then applying the inverse gauge transformation, proves equality of the **infimum** norms N_Z, not just an upper bound. Taking the infimum over corresponding gauge subspaces proves orbit-norm equality.

Hence (R2) is frame independent with the same constant under these gauge transformations. This is not uniformity over arbitrary choices of a gauge-fixing slice, and it does not assert norm isometry for arbitrary nonunitary complex gauge transformations. The abstract complex version of GA remains valid separately.

## 8. The direct decomposition: its skeleton survives, its asserted cut obstruction does not

**Locations:** `BGT55.md`, §5.1(a) “Exact skeleton”, §5.1(c) “requires the cut condition”, and “equivalent to the top-residual part of (R2) itself”; `COFUN_CC.md`, “Lemma FLUX” and “Gale-Hoffman”.

**CONFIRMED — the exact mixed-derivative skeleton.** Differentiate the joint Ward identity in a datum direction b at an x-critical point. With X_V the actual datum gauge velocity and the signs of §4,

    〈T_b^Z,Ξ_Zλ〉
      = 〈b,F_vv d_Vλ_k〉 − 〈F_v,D_vX_V(λ_k)[b]〉,
    T_b^Z=−F_xv b.

This is the printed 𝒟_Z formula. At the trivial chain F_v=0 and F_vv=κ_(k−1)I, giving 𝒟₁=κ_(k−1)d. It supplies no uniform right inverse for 𝒟_Zᵀ.

**REFUTED — the ordinary cut condition asserted necessary for d_Vᵀb=Δ.** The scalar untwisted graph theorem does not apply to covariant divergence. Pairing against an ordinary constant on a region leaves interior-link terms whenever that constant is not parallel for V.

An exact counterexample already exists at zero curvature. On a four-dimensional torus, take every link in direction 1 to have the same adjoint rotation

    R=[[12/13,−5/13,0],[5/13,12/13,0],[0,0,1]],

take the other link directions to be identity, and let b=e₁ on every direction-1 link and zero elsewhere. These links admit SU(2) lifts and all plaquettes are identity. The current is uniformly bounded, but at every site

    Δ=d_Vᵀb=Rᵀe₁−e₁=(−1/13,−5/13,0).

For A the whole torus, ∂A is empty and Σ_AΔ is nonzero. At T=3 the sum is `(−81/13,−405/13,0)`. Thus the claimed necessary inequality fails even though its current is explicitly given. Replacing R by the rational rotation with cosine `(1−t²)/(1+t²)` and sine `2t/(1+t²)` makes the connection arbitrarily small for nonzero rational t; the counterexample is not caused by a curvature violation.

The valid dual bound for a bounded current is of the form `|〈Δ,φ〉|≤||b||∞ Σ_links|d_Vφ|`. It becomes an ordinary boundary-capacity bound only when the interior covariant derivative of the chosen test field vanishes.

**NOT-VERIFIED — equivalence/circularity as a route-level obstruction.** SF_Z exhibits one current depending on the response; estimating that particular current from the response would be circular. It does not prove that every independently constructible bounded current must be obtained that way. Moreover, the exact decomposition equation here is `𝒟_Zᵀb=q`, whereas SF_Z gives `d_Vᵀb_Z(x)=q`. Those are different operators at a nonzero background fluctuation. Neither an equivalence to the top-residual estimate nor “it cannot be proved first” follows from their existence identities. GA's algebraic avoidance of CC-dec_Z remains valid regardless.

## 9. bg55_ga — CONFIRMED as reproduced exact finite algebra, with its disclosed limits

**Locations:** `checks/bg55_ga_criteria.md`, “Models”, “PASS criteria”, and “What this check cannot decide”; `checks/bg55_ga.py`, `build_ops`, `PZ_mul`, `HZ_mul`, `run_model`, and `if do_solve`; `BGT55.md`, “Check bg55_ga”.

I read the criteria and all 440 script lines before running:

    python3 -I -B .claude/science/toe-ruleset-20261021/agents/ym4d-proof/checks/bg55_ga.py

The script uses integers/Fractions, writes only stdout, and reproduced the stored outcomes. Before the duplicate SUMMARY block there are 29 PASS lines and 14 firing control lines; no FAIL or non-firing control appeared. M1 has dimensions 216/96, M2 540/240. M1's two alignment ranks are 216, and its two Hessian ranks are 120. The pure-gauge aligned defects vanish exactly. The nonzero tree-alignment defect counts 7504 and 26435 also reproduce; that slice is not the actual elliptic S_E.

The augmentation by PᵀP in A7 is legitimate: Ξ₁ᵀH′=0, PΞ₁=I, and Ξ₁ᵀ(ΥᵀS)=0 imply Pu=0 for a solution of `(H′+PᵀP)u=ΥᵀS`. The script also checks Pu and H_ZΥu=S directly. M1 alone runs A7/invertibility and the full curved matrix check. In M2 the left annihilation at the curved background is obtained by symmetry, not a separately formed full matrix product. These are disclosed and legitimate limitations.

The curved H_Z is explicitly `P_ZᵀH_Z^covP_Z`; its gauge degeneracy is imposed by construction. It is not the nonlinear critical-point Hessian of the project. The model is d=2 and uses the **root-to-root line map Q_ax**, not the S4′ averaged root map. Neither A7 nor its matrix inversion sums a Neumann series or establishes its norm threshold. The finite source samples lie in Ran H_Z; they do not independently establish a uniform source-space estimate. No check establishes the S_E spike claim, (ALIGN-ℓ), a critical curved Yang–Mills background, or any k,T-uniform bound.

Minor runner boundary: `rep` and `ctl` print failures but do not set a failing process exit code. A future caller must inspect the actual PASS/control output, as done here, rather than treating exit 0 as the criterion. This does not invalidate the present all-passing output.

**NOT-VERIFIED:** independent authentication of the author's historical file-creation order or timing claims. Present criteria/code/output agree; I inspected the timing files but did not infer historical provenance from their contents alone.

## 10. Independent exact checks and negative-claim scope

The symbolic arguments above are the main independent checks. A separate in-memory `python3 -I -B` process, importing only fractions, checked the three-dimensional GA/slice identities and responses at n=1,2,3,9,81; its wrong-alignment and δ=1 controls fired. It also checked the exact bracket sign, rotation orthogonality and covariant-divergence counterexample, and the rational residual/cascade sums. No separate script, cache, or log was written.

The recorded results, with Fraction values written as fractions, were:

    GA: alignment, cc pullback, slice identity and responses verified;
        C_b=1, δ=1/2, inverse bound=2 at n=1,2,3,9,81.
    Threshold control: δ=1 creates another kernel direction;
        unaligned-difference controls fire.
    Positive-d soft derivative: (0,0,−1/5);
        printed positive commutator: (0,0,1/5).
    Twisted divergence: per-site (−1/13,−5/13,0);
        T=3,d=4 total (−81/13,−405/13,0), boundary=0.
    L=9, θ=1/2, q=1..40:
        weighted G sum=(3/2)(1−3^(−q));
        cascade partial sums through q=40 are <9/4.

The general exponents and infinite-series bounds were proved symbolically above; these rational checks are not substitutes for the quantified proof.

I applied the repository's negative-claim discipline to avoid turning a bad estimate into a no-go. The following is a scoped review record, not an audit/landing packet or a claim to have exhausted five alternative proofs:

| Check | Outcome |
|---|---|
| N1, alternative mechanisms | Signed cancellation of completed slots, alternate representations in N, hierarchical gauge completion, direct background source decomposition, and more general aligned congruences remain distinct possibilities. This review does not declare them ruled out. |
| N2, independence | No count of independent necessary obstructions is asserted. A1 and A2 are sufficient quantitative hypotheses with potentially shared analytic inputs. |
| N3, hidden assumptions | Noncancelled point charges, a representation lower bound, bounded slice selection, and covariant norm comparison are exposed above. |
| N4, matching | The finite artificial Hessian tests GA algebra; it does not test the nonlinear Hessian estimate or S_E norm obstruction. The ordinary cut theorem does not match covariant divergence. |
| N5, resolution | The nested-root contradiction is exact for the literal per-level dependence; the count and tests do not exclude hierarchical dependence or other alignments. |
| N6, partial closure | GA, RW♯ and pure-gauge transfer survive independently. Repairing signs or the alignment definition requires no new physical axiom. |
| N7, strongest opposing route | Keep the signed full Ward-identity completion, construct a hierarchical Λ, and prove the three intrinsic inequalities in §6.4 above. A large isolated current does not rule this out. |
| N8, prior echo | `CODEX_REVIEW_GAPZ.md`, F7, is sharpened rather than repeated as a universal obstruction; `CODEX_REVIEW_GSHARP.md`, “unrestricted projected-source closure”, records missing evidence rather than impossibility. `CODEX_REVIEW_KOFF.md`, §6.2/§6.4, similarly distinguishes a failed separated estimate from a false full bound. |

One review pass; no source fixes, git operations, audit mutations, or additional files. The specified runner was reproduced once. Upstream global analytic proofs and the HIGHER/KOFF runners were not rerun; their exact scoped conclusions are named dependencies, not new certificates from this review.

Selected source identities used in this review:

| File | SHA-256 |
|---|---|
| `BGT55.md` | `516ceddf05987c9fd35b7a9b9c60bc8e98798e1c93e184631990f504d3ef6f46` |
| `checks/bg55_ga.py` | `902e11d5d74661039061f38c3fd28b597e38dd57edcc5754b315d1b588ff5017` |
| `checks/bg55_ga_criteria.md` | `973faf2eeed29b379836cd91597b370c5ca13bf7762ceb1563c77ffff7d30c08` |
| `checks/bg55_ga_out.txt` | `b9e2b9b238fd0deaf22c7b2aac5fc0b7e6e0d85efb1b751ef2c7577b67bb32d4` |
| `BFT_A.md` | `8074d6c5efe3648bfb28e3463a6076cf6df74c9c358a8613390044148ac6fbe0` |
| `BFT_B.md` | `b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6` |
| `COFUN_CC.md` | `2a399a7dce1de8f0a4e9b4dfb81d9f0595e8eb4d8b294e2764b1b518d98ce035` |
| `CODEX_REVIEW_GSHARP.md` | `0089399ed8af98529176046fe0b7ad10b60c3211718051a736c41b10ff8e50b5` |
| `CODEX_REVIEW_KOFF.md` | `e284b99415a1abb6f3a7ceaafb81542a6df12483cf838b4d99dd38522607247f` |
| `CODEX_REVIEW_HIGHER.md` | `9ff0e60a4a4be5a445631ac27fa3b0805eee49543f100bb0f1f544d19eb1dc6c` |

## Exactly what may be banked

1. **CONFIRMED — GA with its exact hypotheses.** Bank annihilator preservation, the quotient Neumann series, kernel equality as an output, and `t₊t_*C_b/(1−C_bδΥ)`. Only the matched flat cc inverse is needed. The universal necessity of a uniform forward/condition-number bound is **REFUTED**; the old relative-estimate warning remains correct. Locations: `BGT55.md`, “Theorem GA”; `HESSREL.md`, “Every perturbative transport”; `CODEX_REVIEW_GAPZ.md`, F7.
2. **CONFIRMED — GA-slice algebra.** Bank the stated alignment, invertibility criterion, source identity, and the defect identity **on W**. Do not bank the S_E impossibility claim or the uncorrected pinned transpose formula. Locations: `BGT55.md`, “Proposition GA-slice” and §6.4.
3. **CONFIRMED — exact pure-gauge transfer and real unitary gauge covariance.** On the flat branch and every real SU(N) gauge image, E_(M_G)=0 and the bound has the same flat constant. Norms and sources transform as in OC. Scope: pure-gauge backgrounds and the corresponding orbit norm; flat connections with nontrivial torus holonomy require a separate argument. Locations: `BGT55.md`, “Corollary GA-PG” and “Lemma OC”.
4. **CONFIRMED — KER_Z, SF_Z, and the direct decomposition skeleton.** At an actual critical background, bank kernel inclusion, the root-current identity with `b_Z=−F_vx`, and the mixed-derivative operator 𝒟_Z. These are exact identities without a new current-size estimate. Bank soft equivariance in the actual-generator form `Dρ X_λ=[λ(c′),ρ]`, or with the minus sign for the positive-d Ξ′. Locations: `BGT55.md`, §3.1, §3.2, §5.1(a), §5.3.
5. **CONFIRMED — RW♯.** At Z=1, m=0, with the named flat inputs and `0<α<θ<1`, bank the field orbit bound plus `max_i L^((1+θ)(k−1−i))||r_i^c||∞+N_res≤C N(S)`, uniformly for k≥1,T≥1, with empty terms zero. Location: `BGT55.md`, “Corollary RW♯”.
6. **CONFIRMED — the stated upper power conversions and exact finite evidence.** Bank the conversions and geometric sums in §6.1 of this review conditional on their own-unit bounds, and the reproduced bg55_ga outcomes only for its disclosed d=2 artificial/Q_ax models. The separate current HIGHER review supplies the scoped all-order critical-point residual input; it does not supply the aligned operator bounds. Locations: `BGT55.md`, §6.3 table; `checks/bg55_ga_criteria.md`; `CODEX_REVIEW_HIGHER.md`, §6 and final item 4.
7. **NOT-VERIFIED — general-background (R2), including the claimed R2-glob realization.** Literal (ALIGN-ℓ)(β), §6.3's exact factorization, and the covariant cut necessity cannot be banked unchanged. What remains is an actual alignment with uniform quotient/source/defect estimates, and the applicable existence/local-to-global hypotheses. No general curved-background clause (b), unrestricted S_E obstruction, or constructive four-dimensional Yang–Mills theorem follows from this packet. Locations: `BGT55.md`, §5.1(c), §6.3–§6.5 and §7.

