# PRE-STATED — independent hostile review of SRCAN55

UTC: 2026-10-29 03:37:31 (clock tool; recorded before derivation).

Target: `SRCAN55.md`, with §8 E3–E9 and the earlier E1/E2 overriding the named text. The errata and locating strings have been inspected; no mathematical verdict has yet been derived. This review does not assert an unobservable model identity or independent source revision.

Refutation targets fixed in advance:

1. SA-CF/E8: reconstruct both Cauchy derivatives and total variance; a missing quantifier, invalid transfer from unconditional to conditional variance, or a counterterm-dependent conclusion refutes the stated scope.
2. SA-PC/SA-TC/SA-S: rebuild polarization and harmonic measure, checking the dimension dependence, derivative orders, decay rate, and support/counterterm assumptions. A factorial hidden in the source domain, a false harmonic-measure extremum, or an inadmissible slice refutes an all-orders claim. Inspect check criteria before code/output; distinguish a discriminating check from a tautology.
3. SA-K/K1: inspect the actual KOFF row constructions. A cancellation-dependent bound re-used for arbitrary coefficient weights, an omitted linear row, a missing Hölder factor, or a stale smallness threshold refutes the proposed implication.
4. SA-J/E1, SA-RW/E6, SA-WD, SA-F: check flux normalization, weighted inverse assumptions, finite-step and all-step domains, both flow bounds, and parameter-uniform constants. A derivative bound proved only on a smaller domain than the flow uses is a refutation.
5. SA-TI, SA-E1/E2, LOC-e/E4: reconstruct source differentiation, the coefficient 6, the scale sums, and the logical relation to flow derivatives. A scalar marginal estimate cannot silently discharge position-dependent/local fluctuation bounds.
6. OS0 scale window: distinguish a fixed-test-function continuum limit from uniform finite-cutoff control and from distributional continuity. A claim of necessity must have the matching quantifiers.
7. D1/D2 and SA-MOM: test what produces decay and which random envelopes require which moments; a hidden high moment of a path product, uncontrolled mixed norm, or unsupported locality claim refutes the reduction.

Verdicts used: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED applies only to the explicitly reconstructed statement and stated hypotheses; it never verifies an inherited premise merely by citation.

Restrictions: no git, no .git access, no audit ledgers or snapshots, no whole PROOF read; only this deliverable is written. Exact rational/symbolic Python only. Reads remain within the user-named files plus at most two explicitly recorded additional files. New findings will be appended as they are obtained.

## Findings (appended incrementally)

### 1. SA-CF and E8 — CONFIRMED, with their stated all-coarse-fields quantifier

Locators: `SRCAN55.md:391–410`, “Lemma SA-CF”; `SRCAN55.md:870–879`, “E8”; `SRCCD55.md:215–281`, “Lemma V”, with its E2 at 926. Claim status: PROVEN for the analytic inequality; CONDITIONAL incompatibility along (F_R).

For a holomorphic log moment-generating function bounded by A, the one-variable Cauchy estimates are |E X − c| ≤ A/ρ and Var X ≤ 2A/ρ², including after subtracting a deterministic linear term cz. Thus A/(ρ₁ρ₂) ≥ √(Var X₁ Var X₂)/2. This is a lower bound on the **Cauchy majorant**, not on the covariance. If the conditional bound holds for every U_K, total variance gives

    Varω X ≤ 2A/ρ² + Varν(E_K X − c) ≤ (2A + A²)/ρ².

The lower-bound mechanism behind Lemma V can be reconstructed without assuming positive plaquette correlations: select direction-1 links based on the even sublattice, condition on their complement, then condition each link on its embedded SU(2) circle coset. No plaquette contains two selected links. The circle density has parameter κ=u₀|z|/N; on an event of probability at least 1/2, 1≤|z|≤12. The two angular intervals of widths 2/√κ, respectively near 0 and between 2/√κ and 3/√κ, have probability product at least 8e^(−5)/π³ and cosine gap at least 1/κ. The weighted staple amplitude is at least (2|h(x)|−24a||∇h||∞)_+/N. Therefore

    Varω e(h) ≥ [c_v/(288u₀²)] Σ_even (2|h(x)|−24a||∇h||∞)_+²
               ≥ [c_v/(1152u₀²a⁴)] (||h||₂²−24a||∇h||∞||h||₁−O_h(a²)).

The constants N cancel, and 1152=288·16/4. The elementary bounds e<87/32 and π<22/7 give c_v/1152 > (32/87)^5(7/22)^3/144 > 3/2000000. Along (F_R), u₀=O(log(ℓ_ref/a)), so this diverges for fixed nonzero h. E8's contradiction is valid without SRC-E′.

Scope: a bound only on U_K∈𝒮_K is insufficient for this total-variance contradiction without control of its complement. A counterterm with appropriate contact support, or a bound directly on cross-support derivatives, avoids this particular contradiction. Merely calling a counterterm “local” does not make its cross derivatives zero: its range must be smaller than the separation. Here `SRCCD55.md:394` specifies range c₁a, so that holds eventually for fixed separated supports.

### 2. SA-PC, SA-TC and SA-S — CONFIRMED as conditional inequalities; the geometric-growth quantifier needs to be explicit

Locators: `SRCAN55.md:412–459`, “Polarisation”, “The harmonic measure”, “Constants grow geometrically in n”; check criteria/code/output `checks/sa55_hm*`. Claim status: PROVEN for the complex-analysis lemmas; CONDITIONAL for SA-S.

Put p=n−2. Expanding Σ_{ε∈{±1}^p}(Πε_i)T(v_ε,…,v_ε), a monomial survives only if every coordinate multiplicity is odd. Their sum is p, hence every multiplicity is exactly one. There are p! permutations and 2^p signs. This proves the normalizer 1/(2^p p!) for every p; p=0 is the empty-product case. Cauchy's p! cancels it exactly. The real slice stays inside the source cube because ||tv_ε||∞=|t|.

The map w=(1+t/r_z)/(1−t/r_z) sends the upper half-disc to the first quadrant. Its diameter has arg w=0 and its circular arc has arg w=π/2, so the bounded harmonic function with boundary values 1 and 0 is 1−2 arg(w)/π. On |t|=rr_z,

    Im(w)/Re(w)=2r sin θ/(1−r²) ≤ 2r/(1−r²),

with equality at θ=π/2. Since 0<r<1, arctan[2r/(1−r²)]=2 arctan r. Subharmonic comparison on each half-disc gives exactly ω_hm=1−4 arctan(r)/π. Zeros of g cause no problem for log|g|. A vanishing real envelope forces each slice identically zero. The two-constants step therefore transfers real second-order decay at rate ω_hm μ_R in d_max, with prefactor (rr_z)^(−p), and with the asserted 1/(n−1) loss if rewritten using an MST of the supports.

The inequality is valid for each n. **REFUTED as a consequence of the literal printed quantifiers:** uniform geometric growth across n. Hypothesis (A), at `SRCAN55.md:446–447`, says r_z and 𝒰_ℂ are uniform in a,R,U_K; it does not say uniform in n or in the support family, and (B) similarly leaves C_ℝ and μ_R's order dependence unstated. The correct all-orders version explicitly fixes r_z, 𝒰_ℂ, C_ℝ and μ_R independently of n (or supplies their permitted order dependence). Disjoint smooth sources make such a source-domain radius plausible, but do not prove those envelopes. No hidden factorial occurs in the proved inequality itself.

A bounded-random-variable counterexample to that quantifier inference is X_i=1+ξ for all i, with ξ a fair sign, assigning the variables to separated supports of diameter D_n≤Cn. Then Φ_n(z)=Σ_i z_i+log cosh(Σ_i z_i). For each n take r_z=1/(4n): |Σz_i|≤1/4, so the log is zero-free and |∂_i∂_jΦ|=|sech²(Σz_i)|<2. On the real cube the derivative is ≤1, hence (B) holds with μ_R=1 and C_ℝ=e^{D_n} (at most geometric). All constants are uniform in cutoff and any extra torus volume. But the higher cumulants are the derivatives of log cosh at zero. They cannot be bounded geometrically in n: such a bound would make their exponential generating series entire, contradicting the pole of its derivative tanh at iπ/2. The missing common radius is decisive. This refutes only the formal all-orders inference from the displayed hypotheses, not a claim that this correlated sign field is Wilson Yang–Mills.

Check receipt: criteria were read before code/output. Running `python3 -B …/checks/sa55_hm.py` produced `VERDICT: PASS`, with all three designed controls firing (the C1 control correctly does not fire at p=1). C1 evaluates independently specified symmetric forms; it can detect the missing factorial. C2 tests rational alternating-series enclosures and rejects ω(1/2)≥1/2. C3 tests independently computed complex division against the proposed formula, and its wrong-denominator control fires. None is an unsatisfiable or tautological PASS gate. The rational enclosures printed are [409665529/10⁹,409665530/10⁹], [688083478/10⁹,688083479/10⁹], and [873097930/10⁹,873097931/10⁹] for r=1/2,1/4,1/10 respectively. Finite samples are not the proof of polarization or monotonicity; the all-parameter derivations above supply that proof. The historical assertion that the criteria existed before the author wrote the script is NOT-VERIFIED by a rerun; it is not needed for the mathematical verdict.

### 3. SA-F — upper bound CONFIRMED; the propagated nonzero lower bound is REFUTED under the stated hypotheses

Locators: `SRCAN55.md:321–346`, “Lemma SA-F”; `SRCAN55.md:729`, “|δu_K|/|δu_0| ∈ [e^{−c}, e^c]”, “opposite triangle inequality”; `SRCAN55.md:761`, “both bounds”. Claim status: CONDITIONAL upper stability; GAP in the lower stability claim.

Let A=u_K−R>0, B=β₋log L>0, and q_j=2C_b/(ρu_j²). Cauchy on the inner half-disc gives |c′_j|≤q_j there. The induction yields |δu_j|≤|δu₀|exp(Σ_{i<j}q_i), and

    Σ_{j≤K}g_j⁴ ≤ Σ_{m≥0}(A+Bm)^(−2) ≤ A^(−2)+(AB)^(−1).

These bounds and the stated bootstrap are correct. A>0 is required by the displayed sum estimate and nonvacuous radius.

The opposite triangle inequality gives (1−q_j)|δu_j|, which is a useful positive lower bound **only if q_j<1**. No such hypothesis is stated. An exact counterexample works for any fixed one-loop step B₀=β₀^std log L>0: take K=1, u₀=A+B₀, u₁=A, R=0, β₋log L=β₊log L=B₀, and

    b₀(u)=−B₀−(u−u₀),    ρ=1/2,    C_b=ρu₀².

Then c₀(u)=−(u−u₀) is entire and sup_{|u−u₀|≤ρu₀}|c₀(u)|=ρu₀=C_b g₀², exactly (Flow-an). Also q₀=2. Choose any nonzero rational δu₀ sufficiently small to obey the displayed bootstrap (for example 0<δu₀<A/100). Nevertheless

    u₀+δu₀+b₀(u₀+δu₀)=A,     δu₁=0.

Thus the correct universal lower bound is **0**, not e^(−c)>0. This is an implication counterexample, not a claim about the actual Yang–Mills beta function. It can be placed at the last step of arbitrarily long unperturbed one-loop trajectories, keeping A and C_b fixed and taking the other c_j=0.

Repair: add q_*:=sup q_j<1. Then the corrected lower factor is Π_j(1−q_j), at least exp[−Σ_j q_j/(1−q_*)]. For q_*≤1/2, exp(−2Σq_j) suffices; exp[−Σq_j(1+o(1))] requires the additional small-q_* limit. The upper size claim survives. The assertion that all perturbations necessarily persist, and the “too large” conclusion in §4 when justified by that lower bound, need this extra hypothesis; one-loop flow itself does exhibit the proposed large-shift obstruction.

### 4. SA-K1 and SA-K — CONFIRMED as the specified conditional tree-level theorem

Locators: `SRCAN55.md:156–242`, “Exact decomposition”, “The one step I could not re-derive line by line”; `CODEX_REVIEW_KOFF.md:270–294` (SG), `321–416` (§4.3), `491–547` (§5.3); `PROOF.md`, “(i) Covariance. A fine gauge transformation”. Claim status: CONDITIONAL on the stated linear response/gauge package and local quadratic input; these inputs are not independently certified merely by their labels.

**The per-term question is settled affirmatively for coefficients attached to entire plaquettes/soft links.** It is essential that ε_l(c) multiplies the whole soft term, not separately chosen words inside its average. The cancellations that gain a scale occur inside that one term and survive this weighting.

Here is the row estimate rebuilt before taking sums. Write q=k−l=m+1, h=L^(−q). A soft term contains a fixed finite set of words, of bounded length and incidence depending only on N,L. Its maximizer is analytic because the X-derivative of Π(e^(−X)M) at (0,I) is −I. On a fixed smaller complex neighbourhood the coefficient

    A_{cb}=W_c^(−1) ∂M_c/∂x_b−Q_{cb}

is O_L(hη_b), as is the analogous coarse-coordinate correction; G_c−I=O_L(h²η_b²). This is the corrected coefficient, **not** ∂(W_c^(−1)M_c)/∂x_b−Q_{cb}, which would have the wrong value at zero. The SG identity at this individual c is

    δs_c=κ_l[−Re tr(Θ_c W_c^(−1)δM_c)+Re tr(Z_c Θ_c G_c)].

Its residual part is R_l^TΨ_c; the remainder consists of products of those small coefficients with Θ_c. The within-term quadratic cancellation and the cubic Taylor remainder give

    |ρ_c−r_c|≤C_L h³η_b²,   |ρ_c|≤L^(−(2+σ)m)η_b+C_Lh³η_b².

Consequently, before summing over c,

    |E_{l,c}| ≤ C_L hη_b [L^(−(2+σ)m)η_b+h³η_b²].

Multiplying by the own-to-coarse current factor L^(3q) yields C_L[L^(−σm)η_b²+L^(−q)η_b³]. The output at l+1 changes only fixed L factors. Bounded incidence then sums absolute values; no cancellation between different c is used. Multiplication by ε_l(c) therefore costs at most ||ε_l||∞. Differentiating these products gives C_L L^(−σm)η_b||δx||. Similarly, Ψ−r=(ρ−r)+O(ρ³) has normalized residual bound Cη_b² because L^((2+σ)m)h³=L^(−3)L^((σ−1)m)≤L^(−3). The linear weighted residual adds O(||ε||∞(η_b+s)); it is not quadratic and must be retained, as SA-K1 does.

For Wilson, each plaquette contributes exactly d*[ε_W∇w(F)] plus (Dq)^T[ε_W∇w(F)]. The normalized first row is a product of a C^α coefficient and a C^α curvature; the second is a bounded-incidence sum of such products with Dq=O(x). The product inequality supplies precisely ||ε_W||∞+[ε_W]^∞_α. Soft rows require only a supremum norm. Divergence-form and residual rows are co-closed off the roots even with variable coefficients: d*d*=0 and the two contributions of each R_l^Ty_l cancel for arbitrary y_l. The remaining plain rows are routed with Σ_{m≥0}(m+1)L^(−σm)=(1−L^(−σ))^(−2), and the Wilson Hölder route with Σ_{i≥1}L^(−αi)=1/(L^α−1). Both are uniform in k,T at fixed α,σ>0.

Thus a finite K_ε with the stated dependence exists; no value is fabricated. With G_cc interpreted consistently as the **complex** inverse norm, the two added budgets are exactly C₀s/2 for the image and 1/4 for the Lipschitz constant. Together with the unperturbed C₀s/2 and 1/2, this gives invariance and contraction at 3/4. Position weights preserve each term's composite gauge invariance. The root-pinned Ward identity therefore still makes the fixed point a full critical point; its injectivity constant depends on the field ball, not ε. Uniform analytic iteration proves joint holomorphy, and zero data leaves zero as a fixed point. Cauchy's n!(2/ε̂_*)^n C₀s bound is a repeated-direction derivative, so its factorial does not conflict with SA-PC.

This does not identify the composite with the source-tilted RG tower (TOWER-VAR^η), establish the inherited linear package, or bound fluctuation integrals. To remove a real symbol collision, I used ε_W for the Wilson field: the target also writes ε̂₀(c) for the level-zero soft coefficient. Their different domains distinguish them, but they are independent coefficient slots.

### 5. SA-WD — NOT-VERIFIED: its weighted contraction is missing the coefficient term

Locators: `SRCAN55.md:300–313`, “the Neumann series is the same”; additional file `BFT34_55.md:109–127`, “Lemma WD”, “(H3)_m”. Claim status: GAP in the stated implication.

The actual differentiated fixed-point equation is

    [I−𝓛_Γ^(−1)(D_x S̃−P_cc D_x∇δF_ε)] ∂_φx*
      = −𝓛_Γ^(−1)P_cc∇δF_φ.

The original WD controls only 𝓛_Γ^(−1)D_x S̃ in the weighted norm by 1/2. The newly named (H3^{ε̂})_m in SRCAN55 bounds the **right-hand source** for a localized φ; it does not bound P_cc D_x∇δF_ε on weighted variations. SA-K1(ii) bounds that derivative only at m=0. Decreasing the data threshold ε₀(m) cannot absorb a new term O(||ε||) that remains linear as s→0. This is a stale-smallness-domain error, not a loss of co-closedness.

A sufficient corrected input is

    N_{m,f}(P_cc D_x∇δF_ε v) ≤ K_{ε,m}||ε||_cf ||v||_{(σ),m,f},
    G_♯(m)K_{ε,m}||ε||_cf ≤ 1/4.

With the old weighted 1/2 budget, the resulting inverse bound is **4**, giving 4e^(c_rm)G_♯(m)S_φ(η_b+s), not an automatically inherited 2. To retain 2, allocate at most 1/4 to each term by shrinking both data and coefficient domains. More generally the prefactor is [1−q_m−G_♯(m)K_{ε,m}||ε||_cf]^(−1). Local finite range plausibly supplies K_{ε,m}, but that proof and the m-dependent coefficient threshold must be stated. I do not claim a counterexample to actual Yang–Mills background locality or that 4 is its sharp constant; the printed factor 2 is NOT-VERIFIED.

### 6. SA-RW/E6 — estimates CONFIRMED conditionally; literal holomorphy for arbitrary Δ is REFUTED

Locators: `SRCAN55.md:276–298`, “Let Δ be any operator”, “Every walk term … holomorphic”; E6 at `859–864`; `PROOF.md`, “Lemma CT♯”, “If Δ = Δ(z) depends holomorphically”; “Theorem RW”, including its internal corrections. Claim status: CONDITIONAL resolvent/walk bounds; GAP in the printed analyticity hypothesis.

Write t=||ε||∞, H₀=N₀(Ĥ_i), H_D=D_m(Ĥ_i). E6 gives tH₀≤γ_i/2 and t(H_D+H₀/2)≤γ_i/2−𝔇(m), hence γ′≥γ_i/2 and D_m(|K₀|)+D_m(|Δ|)≤γ′/2. Schur's test and conjugation by e^(m dist) then give the compressed resolvent bound 2e^(−md)/(γ′+s). Integrating s^(−1/2)/π gives 2e^(−md)/√γ′ for the principal inverse square root. The corrected R choice makes (8S′_m/γ′)coth⁴((m−m₁)/4)e^(−(m−m₁)RL/2)≤1/2. These are valid estimates, without a Hölder hypothesis. Small t must also be chosen uniformly from a uniform gap/margin if uniformity in i is claimed.

But the majorant assumption alone says nothing about parameter analyticity. On a one-dimensional space take K₀=1, Δ(ε)=conj(ε), Ĥ=1, |ε|≤1/2. Here D_m=0, E6 gives radius 1/2, every size and symmetry hypothesis holds, and (1+conj(ε))^(−1) is **not holomorphic**. The missing hypothesis is “Δ(ε) is holomorphic.” It holds for the coefficient-weighted Hessian at a fixed background, so this refutes the literal abstract formulation without destroying that application.

At a nontrivial level-zero background, one must also charge the existing background perturbation in the CT margin. `PROOF.md`, “by Lemma N5-an, ||Δ_□|| ≤ N_0(|Δ_□|) ≤ C_Δα_*”, explicitly spends that budget on C_Δα_*; the trivial-background E6 threshold cannot simply be reused at its saturated boundary. A smaller background/coefficient neighbourhood gives the usual repair. Identification at higher levels remains OPEN as the target says. Also retain RW(iv)'s correction: the weakened integrated field map need not square to the weakened covariance at general complex s.

### 7. SA-J/E1 — slice mechanism CONFIRMED; the signed formula is REFUTED in the repository's convention

Locators: `SRCAN55.md:244–274`, “Lemma SA-J”; `352–360`, “Corrected statement (exact; abelian quadratic, d = 4)”; `PROOF.md`, “ν_α(p) := e^{ip_α} - 1”, “With (dB)^_{αβ} = ν_αb̂_β - ν_βb̂_α”, and “The Euler-Lagrange equations: d*dB_0 + κ_0Q^Tr_0 = 0”. Claim status: PROVEN slice algebra after the sign correction; ARGUED/NOT-VERIFIED for the fully quantified rough-background obstruction.

With the repository's forward-difference convention,

    (dx)_{1ν}(t,y)=x_ν(t+a,y)−x_ν(t,y)−∂_νx_1(t,y).

The contribution to d*(cF) at a ν-link in slice t is c(t−a)F_{1ν}(t−a,y)−c(t)F_{1ν}(t,y). Summing the other plane terms over the periodic transverse slice kills them by telescoping, without any fine translation invariance of the block kernel. Since d*(cF)=−j, the corrected E1 identity is

    c(t) F̄_{1ν}(t)−c(t−a) F̄_{1ν}(t−a) = +j̄_ν(t),

**not −j̄_ν(t)**. The max-over-slice inequality is correct. The sign does not affect the Hölder obstruction. A direct rational check of the underlying adjoint algebra uses A=(0,1,0) on a three-site circle, F=(1,−1,0), c=(2,1,1): at t=0 the flux difference is 2, j=−d*(cF)=2, and the printed −j is −2. This check is an incidence/sign check, not a constructed multiscale critical background.

With c_+=c_−+Δc, the exact rearrangement is

    F̄_+−F̄_− = [j̄−Δc F̄_−]/c_+.

It gives a large jump when |j̄| is small compared with |Δc F̄_−|. Merely saying “small compared with cF” is insufficient when Δc→0: the comparison must include the small jump amplitude. For a full-depth rough bare coefficient Δc≈1/K, exponential decay of the residual majorant would beat 1/K **if** a nonvanishing coarse curvature slice is supplied. The file explicitly lacks that background lower bound. Thus a necessity theorem for the actual family of critical points is not yet PROVEN; the flux mechanism and the sufficiency of a Hölder coefficient class are established separately.

**REFUTED quantifier:** `SRCAN55.md:494`, “at every depth k with ℓ_k ≫ a.” The condition for a source of fixed lattice amplitude is r_src g₀² L^(kα) being too large, not merely L^k→∞. Take α=1/2, k=2m, total depth K=L^(2m), and a one-loop trajectory with u₀≈K. Then ℓ_k/a=L^(2m)→∞ but g₀²L^(kα)≈L^(−m)→0. The stated Hölder threshold is eventually satisfied. At k=K it fails for a fixed nonzero rough amplitude, as intended.

For a source z e_a(x) on one site, the stronger SA-K admissible radius is O(ε̂_* u₀ a⁴(a/ℓ_k)^α), because its coefficient jump is |z|g₀²/(2a⁴). The target's O(a⁴u₀) is the relative-sup-norm restriction alone; it must not be read as the radius already sufficient for SA-K.

### 8. SA-TI and SA-E1/E2 — identities and coefficient 6 CONFIRMED; the action-derivative sign is REFUTED

Locators: `SRCAN55.md:524–541`, “Lemma SA-TI”; `544–556`, “It is the z-derivative … conditional action”; E2 at `576–583`; `SRCAN55.md:130–135`, Φ_K=−ΔS_K. Claim status: PROVEN generating identity; CONDITIONAL tree estimate.

For O held fixed under the tilt, ∂_w log E exp(wO+Σz_iX_i)|_{w=0}=E[O exp(Σz_iX_i)]/E exp(Σz_iX_i). Commuting derivatives at zero proves the one-O cumulant formula for every m. The 46 component labels therefore require no independent O-source domain to define these derivatives. This does not establish (A_O), (B_O), their pointwise weights, or the case of several non-e insertions; it also does not allow an O depending on z to be differentiated without its own derivative terms.

For real backgrounds, every site is a corner of 24 unoriented plaquettes, and h_□(p)=Σ_corners h/2. Hence Σ_p|h_□(p)|≤12Σ_x|h(x)|. For an anti-Hermitian plaquette log X,

    1−N^(−1)Re tr(e^X) ≤ ||X||_F²/(2N) ≤ ||X||_op²/2.

Combining this with ||X_p||≤L^(−2K)(2η_b+9η_b²) and a^(−4)L^(−4K)=ℓ_ref^(−4) gives exactly **6**, or **6/N** if the supplied bound is in Frobenius norm. These are E2's corrected constants; I do not re-refute the superseded 3 or 3N.

There is still a sign error in the envelope interpretation. ε_W(z)=−g₀² z h_□, so stationarity gives

    ∂_z [u₀𝔉_K^{ε(z)}(x*(z))]_{z=0} = −E_K^tree[e(h)].

The energy image is **minus** the derivative of the conditional action, equivalently plus the derivative of its negative/log weight. The plus sign claimed at line 549 is inconsistent with the file's own Φ_K=−ΔS_K. Its absolute-value bound is unaffected. This statement concerns the composite classical value; identifying it with the complete source-tilted conditional action still requires the named tower and fluctuation inputs.

### 9. LOC-e/E4 — the a^(−4) non-implication CONFIRMED; reduction to the scalar flow derivative NOT-VERIFIED

Locators: `SRCAN55.md:558–574`, “(LOC-e)”, “The summable coefficient”; E4 at `842–852`; `SRCCD55.md:390–401`, “SRC-poly”. Claim status: PROVEN abstract non-implication; OPEN local fluctuation estimate.

There are O(|supp h|ℓ_r^(−4)) level-r roots. Cauchy on a fixed source disc costs 1/r_src per first derivative and supplies no canonical background factor. For ℓ_r=aL^r,

    Σ_{r=0}^K ℓ_r^(−4)
       = a^(−4) [1−L^(−4(K+1))]/[1−L^(−4)].

Thus a uniform activity majorant permits a^(−4) growth, not just K=O(log(1/a)). It is a possible worst-case divergence, not a lower bound for the Wilson singleton.

E4 supplies a matching abstract example. Restrict to a fixed physical region, choose a bounded nonconstant coarse local ψ, and make the fine field deterministic conditional on U_K with value (A/r_src)ψ Σ_rℓ_r^(−4). Put one linear activity on each cube meeting that region, with the region indicator included in the source sum. Its absolute value is bounded by A M⁴||ψ||∞ on the source ball; any one-cube polymer weight is absorbed into this fixed constant. The same ψ can lie within the allowed Mℓ_ref halo of every contributing cube by taking the region sufficiently small. All conditional cumulants of order ≥2 vanish, while the centered conditional mean is

    (A/r_src)(ψ−νψ)(∫h) a^(−4) [1−L^(−4(K+1))]/[1−L^(−4)].

So neither centering nor cross-support second-order control repairs the singleton. This model refutes the stated abstract implication, not Yang–Mills.

The flow derivative mechanism is sound **for a separately identified marginal local coefficient**: Cauchy gives ∂_u b_r=O(g_r⁴), because the one-loop term is constant, and the sum is finite. However (Flow-an) is a scalar, constant-coupling statement. It supplies neither the local functional derivative with respect to η(x), nor bounds on the irrelevant/nonlocal remainder, nor the coefficient extraction that identifies every U_K-dependent oscillation of 𝔦_r with that marginal derivative. Gauge invariance alone does not provide those estimates. A gauge-invariant small-field expansion with canonical scaling, a source-localization map, and summable remainder bounds are additional obligations. One can even append an independent exact one-loop scalar flow to E4's abstract model without changing its divergent singleton. Therefore the claimed “singleton is a statement about the coupling flow's derivative” is not a proved reduction from the listed hypotheses.

### 10. OS0 scale window — fixed-separated tests are covered eventually; full fixed flat tests still need a uniform extension estimate

Locators: `SRCAN55.md:515–522`, “a scale window”; E7 at `866–868`; `642–644`, “OS0 … needs every scale down to ca”. Claim status: CONFIRMED domain calculation for a fixed radius; NOT-VERIFIED full OS0; REFUTED if read as a necessary continuum obstruction from analyticity itself.

For normalized bumps varying at scale δ with [h]_α≤Cδ^(−α), a fixed r_z and the sufficient SA-K condition give δ≳(g₀²r_z/ε̂_*)^(1/α), hence the displayed logarithmic δ_a along (F_R). E7 correctly notes that a fixed power of log cannot defeat a^(−4n).

There are two different fixed-test questions:

* For any fixed collection of smooth supports with separation δ>0, eventually δ>δ_a. The window causes **no obstruction to taking a→0 on those tests**. It also does not prove that such limits exist; SA-S's bounds and the coarse/LF inputs remain needed.
* A fixed F∈^0𝒮 can approach the diagonals at arbitrarily small separations while being flat there. Convergence on every fixed separated support does **not** ensure convergence on this entire test space. Uniform continuity/equicontinuity, or another controlled extension, is needed to exchange the cutoff limit with infinitely many Whitney pieces.

The second point is not merely a finite-a technicality. In relative dimension four let a bounded positive kernel C_a(x,y), compactly supported in the centre coordinate, have height a^(−8) on δ_a/3<|x−y|<2δ_a/3 and vanish outside a slightly larger annulus. It vanishes eventually on every fixed separated compact test. Choose the single, cutoff-independent smooth flat test

    F(x,y)=χ(x,y) exp[−|x−y|^(−α/2)]

near the diagonal, with compact χ equal to one in the chosen region, and F=0 on the diagonal. Its pairing with C_a is bounded below by a constant times

    a^(−8) δ_a⁴ exp(−C δ_a^(−α/2))
      ≍ a^(−8) [log(1/a)]^(−4/α) exp(−C′ sqrt(log(1/a))) → ∞.

This respects the crude two-point bound O(a^(−8)). It is an abstract distributional counterexample to the inference from fixed-separated convergence plus that crude bound, not a Wilson/RP counterexample. Thus the uncovered window can matter even for a **fixed** flat test.

But the fixed-radius window is **not a necessary obstruction imposed by holomorphy**. Allow r_z(δ)=cδ^α (for δ≤1) and use a uniform upper bound on g₀². Then g₀²r_z(δ)[h]_α≤cg_max²C at every cutoff. Choosing c sufficiently small satisfies SA-K for all δ≥ca. Cauchy now costs δ^(−α(n−2)) in SA-TC, a power singularity with degree linear in n. For normalized local averages the additional δ^(−4) per insertion is also polynomial. If the complex/real envelopes have controlled polynomial dependence on δ and support size, this is compatible with flat-test estimates. The exact canonical SRC-κ powers are a stronger objective than this OS0 continuity argument.

Therefore the correct verdict is a missing **uniform test-function estimate**, not a proof that the continuum OS0 axiom fails, and not a theorem that only (P1), a flux norm, or a smoothed tower can repair it. A shrinking source radius is another possible route; the required envelope estimates on those discs are OPEN.

### 11. Decay input and the fixed-kernel chain — CONFIRMED distinction; the two named routes are sufficient mechanisms, not an exhaustion theorem

Locators: `SRCAN55.md:129–154`, “The kernels are NOT changed”; `585–610`, “Which locality is needed”; `883–887`, E9. Claim status: PROVEN source identity and non-implication; CONDITIONAL decay mechanisms.

Multiplying the fine Wilson density by exp(Σ_p h_η(p)s(U_p)) changes u₀ to u₀−h_η(p) and leaves every kernel factor and its normalization untouched. Retuning those kernels would define a different conditional generating function. Thus the mismatch noted in §2.1/E9 is genuine, and real-tilt CD must be proved for this exact fixed-kernel family.

An analytic bounded function Φ=z₁z₂ has ∂₁∂₂Φ=1 independently of support distance. More physically, a conditional law in which two arbitrarily distant observables are the same fair sign has covariance one even if its deterministic background map is identically zero and perfectly local. Hence background locality cannot by itself supply covariance decay.

(D1) supplies decay when an analytic source-dependent polymer expansion has quantitatively decaying activities and enough summability to beat polymer entropy; the source derivatives must attach to all supports. Bond-parameter analyticity is useful only together with a true decoupling/splitting identity, a sufficient complex radius, and bounds on the family. The finite-word coefficient perturbation does not construct that family. (D2) is the independently proved SA-TC mechanism, conditional on real-tilt CD and the complex cross-derivative envelope. These are valid alternatives. “Exactly two ways” is not an established classification of all possible decay proofs.

The stronger BFT34 scalar example cited by the target has the advertised logical separation: a degree-n grid monomial can have a diameter-decaying coefficient, while any connected polymer containing all n terminals must pay an Euler-tour lower bound on its size. Taking the grid size first and spacing second makes the required polymer exponent larger than the available diameter exponent. This is an abstract scalar analyticity/locality counterexample, not an SU(N) realization. No claim about the entire Balaban literature is independently verified here; external literature was outside the permitted read set.

### 12. SA-MOM — CONFIRMED inequality; a first moment uniform over real tilts is still required

Locators: `SRCAN55.md:618–635`, “Proposition SA-MOM”, “which Proposition C/E3 controls”; `SRCCD55.md:930–938`, E3; `CODEX_REVIEW_SRCCD.md:226–255`, “first-moment argument”. Claim status: PROVEN moment-transfer inequality; OPEN application to the source-tilted LF envelopes.

Put ω=1/(bq), p=q/(q−1), and r=tan[π(1−ω)/4]. Raising SA-TC to b gives

    |κ_n|^b ≤ (rr_z)^(−b(n−2)) 𝒰_ℂ^(b−1/q) 𝒰_ℝ^(1/q).

Hölder with exponents p,q gives exactly the printed formula. In particular b=2,q=2 requires E(𝒰_ℂ³), not E(𝒰_ℝ²). For j factors the choice ω=1/(jbq) works: two applications of Hölder bound the real part by Π_l(E𝒰_{ℝ,l})^(1/(jq)), and the complex part by Π_l[E𝒰_{ℂ,l}^{p(jb−1/q)}]^(1/(jp)). No high path moment has been hidden in this algebra.

**NOT-VERIFIED bridge:** 𝒰_ℝ here is a supremum over the real tilted cube, with the original ν_K used for averaging. Proposition C/E3 controls the indicated zero-source path envelope under its own pointwise LF/image hypotheses and Peierls law. It does not by itself establish a uniform real-tilt majorant for this new supremum, particularly for the fixed-kernel mismatch family. Even uniform bounds on E|h(z,U_K)| separately at every real z do not imply a bound on E sup_z|h(z,U_K)|. A common path majorant valid for all those tilts, with the required first-moment smallness, would make this step valid.

If 𝒰_ℂ is bounded by a fixed finite-neighbourhood LF factor as explicitly hypothesized, all its fixed moments are indeed bounded deterministically; the conditional moment problem closes given that hypothesis and the required first moment of 𝒰_ℝ. If its “neighbourhood” grows with a support's size, order, or cutoff, that growth must be counted. If it contains the same unbounded path product as 𝒰_ℝ, the high-moment problem has simply moved. No uniform all-order unconditional OS0 estimate follows without these bounds, singleton control, and explicit growth in n.

### 13. Symbols, stale domains, gates and citation integrity — CONFIRMED observations within the read scope

Locators: `SRCAN55.md:107–125` (symbol table), `137–138`, `159`, `180`, `326–332`, `446`, `859–864`; `SRCCD55.md:319` and `751–754`; `SRCAN55.md:68–70` (PROOF citations).

The review used these typed meanings before comparing bounds:

| Notation | Object and source locator | Required distinction |
|---|---|---|
| ε_W vs ε_{S,l} | SRCAN55:113, 150–153 | Wilson plaquettes vs soft level-(l+1) links; the target uses ε̂₀ for both when l=0 |
| η_b | SRCAN55:111, 160–164 | field-ball radius, not the observable source η |
| ε̂_* vs ε₀ | SRCAN55:198–202 | coefficient threshold vs data threshold; SA-WD needs a new m-dependent coefficient threshold |
| m in L^(−σm) | KOFF:347–349; SRCAN55:180–190 | depth offset k−1−l, not the exponential weight set to zero in SA-K1's setting |
| G_cc vs G_♯(m) | SRCAN55:117, 198, 307–308 | unweighted complex response norm vs weighted response norm; do not reuse the coefficient budget across them |
| R_F | SRCCD55:751–754; SRCAN55:326–332 calls it R | flow-error bound, fixed along the trajectory |
| R_tor | SRCCD55:319; SRCAN55:446 calls it R | physical torus side over which uniformity is required |
| R_walk | PROOF, “Theorem RW”, “a partition 𝒫”; SRCAN55:E6 calls it R | integer box size chosen after the perturbed covariance constants |

Thus the target's “every collision checked” table misses an R collision. In all flow formulas above, R means **R_F**, never R_tor. Reading u_K−R with the torus-side meaning would destroy its positivity as the volume grows. No numerical comparison in this report uses the collided interpretation.

The decisive stale-domain problems are explicit: (i) the flow's lower bound needs q_*<1 although C_b is now an unconstrained finite output; (ii) the weighted derivative needs a coefficient threshold involving G_♯(m), not merely a smaller data threshold; (iii) all-orders geometric growth needs a radius uniform in n; (iv) the real-tilt supremum is not the zero-source first-moment envelope.

The analytic gates themselves are feasible: SA-K reserves half the image budget and one quarter of the Lipschitz budget; E6 has a positive threshold when the stated CT margin is strictly positive; the flow upper-bound bootstrap has nonzero admissible perturbations when u_K−R_F>0. Their availability is conditional on the named finite constants. The hm checks have genuine wrong-answer controls, but do not test any of these RG hypotheses.

PROOF citations were located by strings. **The file moved nonuniformly during this review.** At the first read, CT♯/RW/RW-triv/N5-sf0/E_NA were at the target's 5560/5577/5637/5646/2539; “Decision 4 is MADE” was already at 586, not the cited 585. At the closing string check (2026-10-29 04:12:41 UTC), the map was:

| PROOF locating string | SRCAN55's cited line | Closing observed line |
|---|---:|---:|
| “Decision 4 is MADE” | 585 | 588 |
| “E_NA := S_W(U)” | 2539 | 2542 |
| “Lemma CT♯” | 5560 | 5562 |
| “Theorem RW (random-walk expansion” | 5577 | 5579 |
| “Corollary RW-triv” | 5637 | 5639 |
| “Theorem N5-sf0 (N5 at small-field backgrounds” | 5646 | 5648 |
| “Lemma TOWER-VAR” | 6666 ff. | 6669 |

TOWER-VAR's “ff.” range still contains the statement; its starting line is not the lemma heading. The exact-line locators are stale. I replaced the report's load-bearing PROOF references with strings and re-read the CT hypothesis and N5 margin at their new locations; the mathematical text used there is unchanged. The forward-difference and dB formulas were relocated to 3772 and 3810. No missing theorem was inferred from a shifted line, and no frozen-revision claim is made.

Read boundary: the user-named target, SRCCD55, CODEX_REVIEW_SRCCD, CODEX_REVIEW_KOFF, PROOF in located ranges, and `checks/sa55_hm*`; the separately supplied project entry-point methodology was read. The two additional chosen files were `docs/ai_methodology/skills/review-loop/SKILL.md` and `BFT34_55.md` (only the ranges needed for the weighted derivative and the cited decay mechanism). The user's no-git/one-output/read-budget instructions override the generic skill's broader operational workflow. No external literature, audit ledger, snapshot, source edit, or additional deliverable was used. The runner was inspected before executing and writes stdout only; `-B` prevented bytecode output.

## Summary table

“CONFIRMED” in this table preserves every named hypothesis and scope limitation in the corresponding finding.

| Finding | Review verdict | Claim status / consequence |
|---|---|---|
| 1. SA-CF and E8 | CONFIRMED | Analytic floor PROVEN; full-log uniform bound incompatible with Lemma V along (F_R), with the all-U_K quantifier |
| 2. SA-PC/SA-TC and fixed-n SA-S | CONFIRMED | PROVEN complex-analysis inequality; conditional decay rate ω_hm μ_R in d_max |
| 2. Geometric growth from the printed quantifiers | REFUTED | A common n-independent radius/envelope condition is missing; correlated-sign counterexample |
| 2. hm runner | CONFIRMED | Actual PASS and three controls; finite certificate scope only |
| 3. SA-F upper bound and Σg⁴ estimate | CONFIRMED | CONDITIONAL, requiring u_K−R_F>0 |
| 3. Positive lower propagation bound | REFUTED | Universal lower factor is 0; a positive product needs q_*<1 |
| 4. SA-K1 absolute-row structure / SA-K | CONFIRMED | CONDITIONAL tree-level theorem; weighted terms do not destroy within-term cancellation |
| 5. SA-WD at the printed domain and factor 2 | NOT-VERIFIED | GAP: weighted coefficient derivative and threshold missing; 4 is a sufficient repaired factor after a new 1/4 budget |
| 6. SA-RW/E6 size estimates | CONFIRMED | CONDITIONAL CT/walk theorem with corrected gap and box radius |
| 6. Holomorphy for arbitrary bounded Δ | REFUTED | Must assume Δ holomorphic; Δ=conj(ε) defeats the literal statement |
| 6. Same covariance threshold at a saturated nontrivial background | NOT-VERIFIED | Existing background error must share the CT budget |
| 7. E1 slice algebra / sign | REFUTED as signed; CONFIRMED after correction | +j̄ in the repository's convention, not −j̄; telescoping is valid |
| 7. Universal actual-background roughness obstruction | NOT-VERIFIED | Need a nonvanishing slice family and |j̄|≪|Δc F̄| |
| 7. “Every depth ℓ_k≫a” | REFUTED | The actual test is g₀²r_src L^(kα) against ε̂_* |
| 8. SA-TI and E2 coefficient 6 | CONFIRMED | PROVEN insertion identity; CONDITIONAL real-background energy bound, 6/N for a Frobenius bound |
| 8. Energy as plus action derivative | REFUTED | E_tree=−∂_z S_tree; plus derivative applies to log weight |
| 9. E4 / a^(−4) singleton non-implication | CONFIRMED | PROVEN abstract counterexample to SRC-poly ⇒ singleton control |
| 9. LOC-e from the scalar flow derivative | NOT-VERIFIED | OPEN source localization, local coefficient identification, and summable remainders |
| 10. Fixed-radius scale window | CONFIRMED | A domain restriction for that chosen radius; fixed separated tests eventually qualify |
| 10. Necessary analytic obstruction to continuum OS0 | REFUTED | Shrinking radii remove that domain restriction; needed envelope estimates remain OPEN |
| 10. Full flat-test continuum bound | NOT-VERIFIED | A shrinking annulus can affect one fixed flat test; a uniform extension estimate is missing |
| 11. Decay is additional to deterministic background locality | CONFIRMED | D1/D2 are conditional sufficient mechanisms; no exhaustion theorem |
| 12. SA-MOM inequality | CONFIRMED | PROVEN; only first real-envelope moments enter the Hölder calculation |
| 12. First-moment control for the real-tilt supremum | NOT-VERIFIED | Need a common tilted path envelope under the original coarse law |
| 13. Symbols and citation checks | CONFIRMED | R needs three meanings distinguished; live nonuniform PROOF drift recorded above |

The numerical/sign corrections newly established here are: the flow lower factor e^(−c)>0 becomes **0** without an extra small-derivative hypothesis; E1's **−j̄ becomes +j̄** (the exact test gives **−2→+2** on its right side); the action-envelope identity's **+E_tree becomes −E_tree**; and the closing PROOF citation corrections are **585→588, 2539→2542, 5560→5562, 5577→5579, 5637→5639, 5646→5648** (TOWER-VAR is at **6669**, within the cited “6666 ff.” range). The SA-WD coefficient **2 is NOT-VERIFIED**, not numerically disproved; the repaired 1/2+1/4 budget gives the sufficient resolvent factor **4**. The harmonic-measure decimals and E2's **6** survive.

**Single most dangerous unverified thing:** a cutoff-uniform complex cross-support derivative envelope for the actual fixed-kernel, source-tilted chain, including its large-coarse-field dependence. Tree-level contraction and the correct interpolation theorem do not furnish it. Without that input, the attractive all-orders and LF-moment reductions cannot be promoted to SRC or OS0.

Closing review: 2026-10-29 04:12:41 UTC. The target still has 899 lines and ends with its 03:35:58Z completion line. This is a review of observed local text, not a repository-status promotion.

## Exactly what may be banked

1. The bare e-source changes only the Wilson coefficient in the exact fixed-kernel chain. Retuning kernels is a different problem.
2. SA-CF and E8's scoped variance obstruction, with Lemma V's coefficient at least 3/2000000 and the corrected variance remainder. This excludes a uniformly bounded full conditional log for all coarse fields along (F_R); it does not exclude counterterm-subtracted or cross-support bounds.
3. SA-PC/SA-TC, including the exact exponent 1−4 arctan(r)/π and cancellation of the polarization factorial. SA-S follows for each n from (A),(B); geometric growth follows only with explicitly uniform-in-n radii and envelope control.
4. SA-K1's per-term coefficient weighting and SA-K's tree-level contraction, gauge/critical-point correspondence, and joint holomorphy, **conditional on the stated linear/gauge package and corrected local analytic inputs**, in the sup-plus-Wilson-Hölder coefficient class on 𝒞_glob. No source-tower identification or fluctuation statement is added.
5. E6's covariance perturbation estimates, with a uniform positive margin, a suitable walk-box size, and **holomorphic Δ** for the analytic conclusion. Nontrivial-background and weighted-background applications must budget the additional perturbations.
6. SA-F's upper propagation and summable Σg⁴ bound under (Flow-an),(F_R), with u_K−R_F>0. A positive lower propagation bound additionally needs sup_j 2C_bg_j⁴/ρ<1 and uses the corrected product/exponent.
7. The slice-averaged flux identity with **+j̄**, the mixed one-O insertion identity, and the real tree-energy bound with coefficient **6** (or **6/N** under a Frobenius-norm hypothesis), with **E_tree=−∂_zS_tree**.
8. The abstract a^(−4) singleton counterexample and the resulting need for genuine local first-order image control. Scalar flow analyticity alone is not that control.
9. SA-MOM's exact Hölder inequality, conditional on its analytic envelopes and their indicated moments. It does not establish those moments, uniformity in real tilts, or all-order unconditional growth.
10. The OS0 quantifier distinction: fixed separated tests eventually fit a fixed-radius domain; the full flat-test space needs a uniform extension estimate, and shrinking source radii provide a possible alternative domain strategy. **No full SRC theorem, OS0 result, nontrivial continuum Yang–Mills field, or mass gap is banked.**
