# PRE-STATED

UTC: 2026-10-28 23:45:02 UTC. These criteria were recorded before reading the target proof or its mathematical dependencies. Prior exposure consists only of the user's description and ranking of the claims.

This is an independent hostile mathematical review of `COFUN_CC.md`, in the order TOP-cc; DEC/FLUX; H-FREE; CC-FUN(b); clause (b) assembly/CC-CRIT. No git commands are authorized. Only this report may be written. Source provenance will be local paths, locating strings, line ranges and content hashes, not an asserted git revision. All executed arithmetic checks must use exact integers/rationals; finite checks do not prove uniform theorems.

Refutation criteria, declared in advance:

1. TOP-cc: an admissible cc source/response violating the stated inequality; a required COF(c) or W0 hypothesis absent for the top response; an unavoidable factor depending on k or T; or a dependency cycle that consumes the top-residual bound being proved. A failed proof establishes NOT-VERIFIED unless the claim itself has a matching counterexample or logical contradiction.
2. DEC/FLUX: a source satisfying the declared hypotheses whose decomposition fails an identity, support/gauge condition or stipulated norm bound; a nonzero forbidden top slot; or a current entry requiring data outside its claimed single face.
3. H-FREE: two allowed contracting operators producing different data maps; a boundary/sign/normalization error; or an advertised negative control that cannot distinguish a deliberately broken identity. A finite successful rerun alone does not establish the universal claim.
4. CC-FUN(b): a missing BL-4/BL-C hypothesis, scale-dependent Hölder constant, illegitimate summation over fine offsets, or use of COF(d) outside its domain. The alleged limitation of LINEAR_PACKAGE must be checked against the actual quantified theorem.
5. Assembly: a claimed implication requiring an unstated premise, treating an open bridge as established, or depending on a refuted input. Lemma TR's separate review is a dependency, not evidence to manufacture here.

Verdicts will be CONFIRMED (within explicitly stated premises/scope), NOT-VERIFIED (an identified gap or insufficient evidence), or REFUTED (a matched counterexample or contradiction), each with a file and locating string. The report will end with exactly what may be banked.

## Disposition

**CONFIRMED as implications of the stated lane-A analytic inputs: TOP-cc, CC-FUN(c), and CC-INV in the source norms, at the trivial background and weight zero.** The replacement of the plaquette test response by the top-link test response is legitimate. Its normalization changes the two powers of n in exactly the required way. The argument does not consume the unknown response's top residual.

**CONFIRMED:** FLUX, DEC, H-FREE for the datum map, and the BL-4 + BL-C route to CC-FUN(b). **REFUTED:** the adjacent assertion that axial-order dependence of source responses is confined to sources with nonzero root charges. An exact four-dimensional (CC-0) counterexample is below. This does not refute H-FREE or the estimates proved with a consistent choice of Q.

**NOT-VERIFIED:** promotion to the full nonlinear critical-point conclusion using only the proved quadratic row bounds. The separate TR review now exists and leaves precisely that qualification. TOP-cc removes the linear top-response obligation; it does not prove the missing estimates for the full nonlinear source.

Paths below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` unless otherwise stated. A CONFIRMED implication retains its named analytic premises; this review does not reprove the entire LINEAR_PACKAGE or certify constructive Yang–Mills closure.

| Claim and locating string | Verdict | Scope |
|---|---|---|
| `COFUN_CC.md:365`, `Lemma TOP-cc` | **CONFIRMED** | Source-only top bound, as an implication; uniform in k, T, and admissible gauge fixing |
| `COFUN_CC.md:327`, `(c) with Lemma TOP-cc` | **CONFIRMED** | Source-only sup and pointwise Hölder bound, with the stated inputs |
| `COFUN_CC.md:414`, `Theorem CC-INV` | **CONFIRMED** | Full invariant norm in the class norms, at Z = 1 and weight zero |
| `COFUN_CC.md:241`, `Lemma DEC` | **CONFIRMED** | Exact decomposition, including removal of the terminal residual slot |
| `COFUN_CC.md:165`, `Lemma FLUX` | **CONFIRMED** | Exact face current and the stated capacity/locality bound |
| `COFUN_CC.md:266`, `Lemma H-FREE` | **CONFIRMED** | Datum minimum, invariant outputs, and quotient norm are independent of the two axial choices |
| `COFUN_CC.md:281`, `collision bites exactly` | **REFUTED** | The restriction to source responses with root charges is false even for D(S) = 0 |
| `COFUN_CC.md:325`, `(b)`; `4.1 What the cited statements actually give` | **CONFIRMED** | BL-4 + BL-C for data; repaired COF(d) for the remainder |
| `COFUN_CC.md:295`, `LINEAR_PACKAGE Theorem 4.2 / 4.2′` | **CONFIRMED** | Those per-offset kernel bounds alone supply no fine-offset Hölder modulus |
| `COFUN_CC.md:430`, `6.2 What this is, and is not` | **CONFIRMED** as a scope separation | Field components, background transfer, and the general weighted estimate remain additional obligations |
| `COFUN_CC.md:450`, `𝒬_{H,m} ARGUED` | **REFUTED** as the current input-status account | Later QH_m and W0_m supersede this old status; general weighted COF is still not established here |
| `COFUN_CC.md:651`, `Corollary CC-CRIT` | **CONFIRMED** conditionally; **NOT-VERIFIED** as full nonlinear closure | Requires bounds for the actual complete source, not only its quadratic part |

## 1. TOP-cc: the high-leverage step survives

Sources: `COFUN_CC.md`, `Lemma TOP-cc`, especially `The same with N_Σ`; `BFT_B.md`, `35.5 Theorem COF`, steps (c)–(d), `35.3 Lemma DF-cc`, `35.4 Proposition COF-size`, and `29.2 Lemma FT`; `BFT_A.md`, `28.2 Lemma TOPD`, `28.5 Theorem W0`, step 3, `13.8 Lemma TS`, `13.9 Proposition W`, and `13.13 Corollary FP`.

### Admissibility and the dual identity

DEC gives S = S′ + T_b, with D(S′) = 0 and s′_(k−1) = 0. Consequently each of S′^G, S′^s, S′^j has pointwise zero composite divergence. It is S′^j, not an arbitrarily split original source, to which the strict-current regrouping applies.

For a top link β, let Y^β be the zero-datum response to the top residual source δ_β. Lemma TS identifies its unknown components with those of the source-free minimizer y^β having datum δ_β/κ_(k−1). They differ in their last residual:

    r_i(Y^β) = r_i(y^β)                      (i ≤ k−2),
    r_(k−1)(Y^β) = r_(k−1)(y^β) + δ_β/κ_(k−1).

This distinction is essential. The top residual of Y^β need not be co-closed; the data residual r_(k−1)(y^β) is. The target proof uses the latter in the transport estimate and uses only i ≤ k−2 in the residual pairing. It does not make the invalid substitution at the terminal level.

TOPD is symmetry of the Hessian tested on two actual critical points. Its proof in `BFT_A.md`, `Criticality:` under §28.2, does not use individual co-closedness of j_l. Thus

    r_(k−1)(x(S′^j))(β) = Σ_l <j′_l,Y^β_l>.

There is no n² in this identity. The n² in COF(c) belongs to the different observable f_0 = n²dx_0. Telescoping the chain gives, for this same Y^β,

    Σ_l <j′_l,Y_l>
      = <C(j′),Y_0>
        − Σ_(m=0)^(k−2) <Σ_(l>m)(Q^(m+1→l))^T j′_l,r_m(Y)>.

This is an algebraic identity for any chain. It does not require Y to be a plaquette-source response. What must be supplied afresh are its quotient ℓ¹ bound and lower-residual ℓ¹ bounds. W0 step 3 and the datum estimates supply both.

### The level-zero pairing and the corrected funnel

Use the explicit correction in `COFUN_CC.md`, `11.3 The terminal-slot and ĵ_0 corrections`:

    ĵ′_0 = j′_0 + h_0^T ψ′_0.

Using the uncorrected `BFT_B.md` convention `ĵ_0 := j_0` would invalidate the regrouping. The target's appended correction must travel with every reuse of the proof.

Since d*C(j′) = D(S′^j) = 0, pairing C(j′) with Y_0 permits adding any fine gradient to Y_0. W0 step 3, via the source-free datum and FP, gives

    𝒩(Y^β) ≤ C_N n³,
    C_N = 4 exp(20m′)(1083G_D(m′)+40) S(m′)/κ_−,

for a fixed admissible positive internal decay rate m′. The problem being estimated still has weight zero. Hence

    |<C(j′),Y_0>| ≤ n^(−3) π_0(C(j′)) C_N n³
                  = C_N π_0(C(j′)).

The two scale factors cancel exactly. The datum δ_β/κ_(k−1) is admissible for Proposition W without a co-closedness condition on the datum. FP supplies a representative for the quotient norm; it is not a field estimate for the unknown response x(S).

For clarity, the summed-current version follows directly from FT(ii), without any optimization in θ:

    Σ_l π_l(ĵ′_l)
      ≤ [1 + 2d/(1−L^(−3))] Σ_l π_l(j′_l).

It bounds both π_0(C(j′)) and max_l π_l(ĵ′_l). At d = 4, L = 3 its factor is exactly 121/13. This includes the l = 0 funnel term.

### The residual pairing and all scale factors

For the source-free datum response, testing gradient variations gives d*r_(k−1)(y^β) = 0. The unsourced Euler–Lagrange equations and root covariance then give

    κ_m r_m(y^β)
      = κ_(k−1) (Q_str^(m+1→k))^T r_(k−1)(y^β).

A one-step straight transpose has ℓ¹ norm at most L. Proposition W and periodization give

    ||r_(k−1)(y^β)||_1 ≤ 4G_D(m′) S(m′)/κ_−,
    ||r_m(Y^β)||_1 ≤ A L^(k−1−m)       (m ≤ k−2),
    A = 4 κ̂ G_D(m′) S(m′)/κ_−.

These are bounds on the known test response. They contain no r_(k−1)(x(S′^j)). DF-cc(iii) replaces each upper-current push-down by straight push-downs of ĵ′. With a = l−1−m, the factor in one pairing is exactly

    L^(−3a) L^(−3(k−l)) L^(k−l+a)
      = L^(−2a) L^(−2(k−l)).

Thus the double sum is uniformly finite. The target's bound A(1−L^(−2))^(−2) max_l π_l(ĵ′_l) is valid. At L = 3 its geometric factor is 81/64. In fact, retaining k−l ≥ 1 gives the smaller factor 9/64; that improvement is unnecessary. No positive power of n, k, or T is hidden in this step.

### Other slots, edge cases, and circularity

W0 bounds the level-zero G slot; GU bounds positive-level G slots after summing `(t+1)^2 L^(−(θ−α)t)`; BL-5(a) bounds residual slots. All contain the terminal residual in their invariant output norm. They apply to the separated strict pieces. The datum contribution is at most `(G_D+1)||b||∞/κ_−`. DEC bounds its source and current norms. This proves TOP-cc for N(S), and directly for N_Σ(S).

For k = 1 the residual double sum and positive-level source sums are empty; DEC makes the sole remaining plain current co-closed. Nothing divides by k−1. For T = 1 or 2 the small-torus lift in W0/FP is available. One can also obtain a uniform quotient-norm bound by lifting the periodically repeated datum to side 3T, summing its 3⁴ translates, using the translation-covariant representative, and descending: the number of source translates cancels the number of fundamental domains in the ℓ¹ norm. Even a cruder fixed small-T constant would suffice. Uniformity is at fixed admissible κ_±, α, θ and fixed internal decay rate; it does not claim uniformity as α approaches θ or a decay rate approaches zero.

The dependency order is acyclic:

    algebraic DEC/DF-cc/FT/COF-size
      + data estimates BL-4/W/FP + Hessian symmetry TOPD
      + restricted-source W0/GU/BL-5
      ⇒ TOP-cc ⇒ CC-FUN(c) ⇒ CC-INV.

COF(d), the step that consumes the unknown top residual, is not used to prove TOP-cc. **CONFIRMED.**

## 2. DEC and FLUX: terminal-slot repair and locality are exact

Sources: `COFUN_CC.md`, `Lemma FLUX`, `Lemma DEC`, and `X1's norm cost`; `BFT_A.md`, `13.8 Lemma TS`; `BFT_B.md`, `35.2 Lemma SPLIT` and `29.2 Lemma FT`.

**FLUX — CONFIRMED.** For a block of side s = L^(k−l), summing d*j cancels every interior link. The surviving signed boundary terms are exactly the incoming lower faces minus the outgoing upper faces. Each oriented upper face contains s³ links, so

    d*Φ_l j_l = blocksum_l(d*j_l),
    ||Φ_l j_l||∞ ≤ L^(3(k−l)) ||j_l||own,∞ = π_l(j_l).

The current b = Σ_l Φ_l j_l + s_(k−1) therefore satisfies

    d*b = q(S),
    ||b||∞ ≤ Σ_l π_l(j_l) + ||s_(k−1)||∞.

The divergence-form slots vanish pointwise under d*. An interior residual slot cancels between its two adjacent chain levels. Only the terminal slot contributes `ev^(0→k)T d*s_(k−1)`. This is why the terminal term in the capacity cannot be omitted.

Each Φ_l entry reads one specified face, at that level. An entry of b reads the corresponding nested faces across levels and one terminal-source entry; it does not inspect an entire cut or solve a global flow problem. On periodic tori, “upper face” is read in a fundamental block lift, retaining seam links. At T = 1 these can be loop links; their incoming and outgoing divergences cancel. The face-count bound remains valid. A local weight costs only a bounded coarse-distance factor, although that fact alone proves no weighted inverse theorem.

**DEC — CONFIRMED.** Put b_j = Σ_l Φ_l j_l. Subtract Q_(k−1)^T b_j from j_(k−1) and set s′_(k−1) = 0. For x_k = 0,

    L_S(x) − L_S′(x)
      = <b_j+s_(k−1),Q_(k−1)x_(k−1)>
      = <b,r_(k−1)(x)>.

Using d*Q^T = ev^T d*, the composite divergence of S′ is D(S) minus `ev^(0→k)T d*b`, hence zero pointwise. Since S′ has no terminal residual slot, D(S′^G) = D(S′^s) = D(S′^j) = 0. This is exactly the case needed by SPLIT; no false assertion about the original terminal slot is retained.

The transpose estimate is

    π_(k−1)(Q^T b_j) ≤ A_L ||b_j||∞,
    A_L = 1 + 2d L³ w.

The full four-dimensional local-kernel enumeration performed in this review gives w = 10/81 for the order average, hence A_L = 83/3. The fixed-order kernel has maximum 1/3. The operator-independent fallback w ≤ 1 gives A_L ≤ 217. Consequently `|j′|_Σ ≤ (1+A_L)|j|_Σ`, and the stated Pc bound follows by the single factor L^θ at the terminal plain slot. At k = 1 the subtraction belongs to P0; the displayed bound for N(S′) is still valid because L^θ ≥ 1. Lemma TS then supplies the response identity and the explicit terminal shift b/κ_(k−1).

The same Q must be used in the chain and the subtraction. The author's C2 control detects violating that condition.

## 3. H-FREE is correct; its source-response exclusivity sentence is false

### Datum map: CONFIRMED

Sources: `COFUN_CC.md`, `Lemma H-FREE` and `Precision to Lemma H-FREE's proof`; `BFT_A.md`, `7.1 Setting LIN`; `LINEAR_PACKAGE.md`, `1.2` and `Lemma 2.5`.

For the two lane operators, g_i = h′_i−h_i annihilates every gradient, because either axial integral of dλ is λ(y)−λ(c_X). Choose λ_0 at the final roots as in the target and recurse

    λ_(i+1) = ev λ_i − g_i(x_i).

Writing x′_i = x_i+dλ_i gives

    d x′_i = d x_i,
    Q′_i x′_i − x′_(i+1) = Q_i x_i − x_(i+1).

The prescribed final-root values make dλ_k = 0, so the last identity uses the same fixed datum. Because g_i(dλ_i) = 0, a fixed linear choice of the λ_0 extension gives the inverse by subtracting these gradients. The source-free energies are conjugate, their minima agree, all dx_i and residuals agree at corresponding minimizers, and the quotient norm 𝒩 is unchanged. For the more general hypothesis that g_i(dλ) is merely constant, the appended reverse-map argument avoids relying on the stronger inverse formula. The statement follows from equality of attainable invariant outputs and uniqueness of those outputs at minimizers.

The test B4 checks this for three data in a two-dimensional model. It is supporting evidence, not the proof in four dimensions; the conjugacy above is the proof.

### Source-order dependence without root charges: REFUTED scope sentence

Location: `COFUN_CC.md:281`, `So the collision bites exactly on statements about source responses with root charges`.

Here is a four-dimensional counterexample to that exclusivity assertion, using only the defined operators and rational coefficients. Take L = 3, k = 2, T = 1, and any admissible κ_0 > 0. Write Q for the order average and Q′ for the fixed order (0,1,2,3). On the level-1 torus of side 3 let φ be the delta function at X = (0,0,0,0). Choose

    x_0 = 0,    x_1 = dφ,    x_2 = 0,
    G = s = 0,
    j_0 = −κ_0 Q_0^T dφ,    j_1 = κ_0 dφ.

The level-2 torus has one site, so root covariance gives Q_1dφ = d(ev φ) = 0. Thus r_0(x) = −dφ and r_1(x) = 0. Direct differentiation of the quadratic energy gives H_Q x = (j_0,j_1). Moreover,

    D(S) = −κ_0 ev^T d*dφ + κ_0 ev^T d*dφ = 0.

This source is strictly (CC-0), has no terminal residual slot, and belongs to every stated source class at this finite k.

If the Q′ response had the same invariant outputs, its level-zero Hessian value would have to be Q′_0^T(κ_0 r_0), whereas the prescribed source is Q_0^T(κ_0 r_0). Put g = h′−h. Since Q′^T−Q^T = −g^T d*, their difference is

    (Q′_0^T−Q_0^T) κ_0(−dφ) = κ_0 g_0^T d*dφ.

Select the level-zero link from (1,1,1,1) to (2,1,1,1) inside block X = 0. Its fixed-order h coefficient is 1/3. Its averaged coefficient is

    (1/4)(1/3 + 1/9 + 1/27 + 1/81) = 10/81.

The link belongs to just this block and `(d*dφ)(0) = 8`. Therefore the Hessian discrepancy on this link is exactly

    κ_0 · 8 · (1/3−10/81) = 136κ_0/81 ≠ 0.

No Q′ critical point with the same invariant outputs can solve the prescribed source equation. This is an exact four-dimensional counterexample; it does not rely on a floating-point solve or on extending a two-dimensional example by an unjustified tensor argument.

A separate exact two-dimensional solve also discriminated the issue: k = 2, T = 1, κ_0 = 1, κ_1 = 2; j_0 is the unit path from (1,1) to (4,1), and j_1 is minus the level-1 link at (0,0) in direction 0. D = 0 exactly. Both 100-variable reduced solves satisfied every full Euler–Lagrange equation. At the plaquette based at (0,0), dx_0 was −1/18 for the average and −1/9 for fixed order 01, a difference of 1/18. This is an additional finite check, separate from the four-dimensional proof above.

The correct replacement for the exclusivity sentence is: **the datum map is unchanged; source maps can depend on axial order even on (CC-0). The estimates in §§4–6 can nevertheless be proved for either operator, with its own consistent source decomposition and operator constants.**

## 4. CC-FUN(b): the Hölder route is sound

Sources: `COFUN_CC.md`, `4.1 What the cited statements actually give` and `Theorem CC-FUN`; `BFT_A.md`, `Proposition BL-4`, `Lemma BL-C`, and `28.7 Theorem GU`; `BFT_B.md`, `35.5 Theorem COF`, step (d); `LINEAR_PACKAGE.md`, `Theorem 4.2` and `Theorem 4.2'`.

**CONFIRMED.** The datum b/κ_(k−1) has a uniform sup bound from FLUX. BL-4 is stated for every datum, with no datum Hölder hypothesis, and controls the invariant norm for every α in (0,1). BL-C then converts its Campanato bound to the pointwise seminorm required by CO-fun. Use the corrected BL-4 constant: `REVIEW_BFT_A_S2.md`, `LES box convention (fix B7, constant only)`, replaces a box-comparison factor 4 by at most 25 under the radius convention. This changes a fixed constant, not any quantifier or exponent.

For the strict remainder, COF(d) uses the j-only response with

    J_0 = C(j′) − (Q_str^(0→k))^T κ_(k−1) r_(k−1)(x(S′^j)).

Its strict source and absence of residual slots imply d*r_(k−1)(x(S′^j)) = 0. The bound on J_0 is a sup bound; LES-div/LE/BL-C do not require its individual plain pieces to be co-closed. The top residual here belongs initially to S′^j. The G and s response bounds convert it to that of S′, and DEC/BL-4 convert the latter to that of S, at source-norm cost. `COFUN_CC.md`, `step (d)'s top residual is that of the j-only problem`, explicitly supplies this otherwise easy-to-miss step.

Accordingly CC-FUN(b) follows without TOP-cc; substituting the independently checked TOP-cc proves CC-FUN(c). The window remains fixed `0 < α < θ < 1`: the positive-level GU sum requires α < θ, and the residual source estimate requires α ≤ θ.

**CONFIRMED limitation of LP 4.2/4.2′ as standalone input.** Those statements bound the kernel separately for each fine offset u, uniformly in u. They give no estimate for K_u−K_v at nearby offsets. Summing over input coarse sites supplies a uniform output sup, but no small factor for separation 1/n. As a logical test of the information content, kernels `K_u(X)=ε_u 1[X=0]` with adjacent ε_u = 1 and −1 obey a uniform bound and have constant analytic coarse symbols, while their adjacent-output difference is 2. Their Hölder quotient grows as n^α. These are not asserted to be Yang–Mills kernels; they show why the stated per-offset estimates alone do not imply the missing regularity. The actual data map has the additional elliptic structure used by BL-4.

## 5. Assembly: what closes and what stays conditional

### CC-INV in source norms: CONFIRMED

Sources: `COFUN_CC.md`, `6.1 The assembled statement`; `BFT_B.md`, `31.2 (NC-Γ)_cc`, `29.1 Lemma RT-cc`, and `29.2 Lemma FT`; `BFT_A.md`, `28.5 Theorem W0`, step 5.

I checked the lower-residual and upper-curvature sums independently, rather than inferring them from the old status label of INV-cc. To distinguish the weight parameter from a level difference, put t = k−1−i. RT-cc and straight-transpose contraction give

    L^t ||r_i^c||∞ ≤ κ_−^(−1) [
      L^(−θ(t+1)) ||s||_R
      + L^(−t)(κ_+||r_(k−1)||∞ + ||s_(k−1)||∞ + C|j|_Σ)
      + 6L^(−t) Σ_(l>i) L^(k−l) ||G_l^c||∞ ].

The last term is bounded by

    6 L^(−θt) ||G||_Y / (1−L^(−(1−θ))),

using θ < 1. The target corrects the overly simple old description that all non-s residual pieces decay as L^(−t): the G contribution has L^(−θt). The plain-current term uses the summed FT bound, so the same estimate holds for N_Σ. TOP-cc makes the whole right-hand side source-only.

For j ≥ 1, the curvature identity `f_j = 𝒜^(0→j)f_0 − R_j` and the inverse bound on each averaged dr_i give

    [R_j]_α ≤ 4 Σ_(i<j) L^(α(k−j)) L^(k−1−i) ||r_i^c||∞.

Since k−1−i ≥ k−j, the slowest relevant decay sums as

    Σ_(i<j) L^(α(k−j)) L^(−θ(k−1−i))
      ≤ L^((α−θ)(k−j))/(1−L^(−θ))
      ≤ 1/(1−L^(−θ)).

The sup sum is easier. The probability average carries the already-controlled f_0 seminorm to every upper level. This establishes the full stated invariant norm, uniformly in k and T. Gauge independence is only for these invariant outputs and follows from the kernel/critical-point statement of FG. No estimate for the gauge-variant field components is inferred.

The residual-Hölder estimate RHT-cc can also consume TOP-cc: its plain sums are bounded by |j|_Σ and its G sum by `Σ_(u≥1)L^(−(θ−α)u)`. Thus the old occurrence of the unknown top residual is removed there as well, under RHT-cc's stated hypotheses. This is still a source-norm conclusion, not automatically an η² bound for nonlinear rows.

### The three additional parts of BFT-5(b)

Sources: `COFUN_CC.md`, `(R1)`, `(R2)`, `(R3)` in §6.2; `BFT_B.md`, `32.1`, clause `(b)`, and `32.2 Proposition BFT5-red`.

1. **Field components — NOT-VERIFIED.** CC-INV controls dx and residuals. The inequality `||x||inv ≤ 2||x||𝔐^∇` cannot be reversed to obtain (G♯_0-field). Uniformity over gauges for invariant outputs says nothing comparable about the fields themselves.
2. **Curved background, including CC-dec_Z — NOT-VERIFIED.** The flat face cancellation, exact root covariance, d*d* = 0, and the kernel characterization are substantive inputs. Replacing d by a covariant differential introduces curvature defects. The target correctly names the missing bounded decomposition plus priced-defect estimate. Neither FLUX nor DEC proves it at Z(V_k). R♯_ω and the perturbation/patching premises remain additional inputs.
3. **The general weighted COF/TOP-cc/CC-INV assembly — NOT-VERIFIED here.** FLUX and the datum estimates have the needed locality features, but no complete weighted general-source proof is supplied by this packet. This does not refute a weighted extension.

There is a specific stale-status error in item 3. `COFUN_CC.md`, `its level-0 pairing needs YH_m: 𝒬_{H,m} ARGUED`, cites the old §28.13 heading. The same `BFT_A.md` has later `33.11 Lemma QH_m` and `33.12 Theorem W0_m`, with the appropriate Lipschitz-weighted source norm and an explicit weighted top-residual proof. `REVIEW_BFT_A_S7.md`, `m > 0: Lemma LES-dd ... Theorem W0_m: CONFIRMED`, confirms their stated range. The plain-current weighted quotient bound was already in §28.13. The current remaining input description should retain the positive-level weighted sup obligations DX_m/DB_m and the full COF assembly; it should not list the corrected level-zero QH_m or W0_m step as still unwritten. **REFUTED as an account of the available input status; not a proof of weighted COF.**

### CC-CRIT and the separate TR review

Sources: `COFUN_CC.md`, `11.5 Lemma TR`, `only their sup enters`, and `Corollary CC-CRIT`; `KFACTOR_O55.md`, `Slots of S*`, `A-priori sizes`, and `(TR-4)`; `CODEX_REVIEW_TR.md`, `Disposition`, `The unproved source hypothesis is material`, and `Exactly what may be banked`; `BFT_A.md`, `31.0 Definitions`, locating `the rows ... are its second-order part`.

**CONFIRMED conditional implication.** If the actual composite-co-closed source has the complete bounds needed by CC-INV, the η² conclusion follows. TOP-cc supplies the formerly missing top bound. Positive-level completion rows need only their weighted sups: GU explicitly states `no Hölder norm of G_l used`. Thus it is legitimate to use the weaker norm

    Ñ_Σ(S) = ||G_0^c||∞ + [G_0^c]_α
             + Σ_l π_l(j_l)
             + max_(1≤l<k) L^(θ(k−l))||G_l^c||∞ + ||s||_R.

The empty maximum at k = 1 is zero. The same proofs bound the outputs by Ñ_Σ. This is the precise way to bypass a positive-level W_l Campanato estimate; one should not claim the original, stronger G_Y norm was itself bounded merely by changing its name.

**NOT-VERIFIED full nonlinear application.** The TR review changed from its pre-stated placeholder to a completed report during this review. Its checked disposition is that transport and summation are valid conditionally, but the cited slot bounds have been established only for the quadratic source while exact criticality uses the full remainder 𝔑^0. This distinction is visible independently in `BFT_A.md:2764`, defining 𝔑^0 and describing the cited rows as its second-order part, and `KFACTOR_O55.md`, which writes `(+ higher order)` in the slots while invoking quadratic constants.

If `S_full = S_2 + ΔS`, the relevant linear equation at the nonlinear critical point uses S_full. Neither composite co-closedness nor the needed norm bound for S_full follows by silently discarding ΔS. Even a separate bound of order η³ per level would not by itself give a k-uniform level sum at fixed η. One must price the complete residual, plain, and divergence-form slots in Ñ_Σ (or supply an equivalent sufficient estimate). TOP-cc is not such a nonlinear source estimate.

Accordingly, the dependency statement “TR plus TOP-cc implies CC-CRIT” is correct when TR includes bounds for the full source actually used. The assertion that the existing quadratic lemmas alone have discharged that premise is not verified. The source's completion construction on small tori must use its stated cover/periodization convention; the later `BFT_A.md`, `[RBA7-fix] P7-2`, explicitly extends NC/WR(b) to every T ≥ 1, so this review does not invent a new small-torus obstruction.

## 6. Exact checks and source provenance

Only this report was written. No git command, audit worker, source edit, bytecode file, or auxiliary log file was created. Large source contents were read through locating searches and sed ranges. The focused local review used the review-loop evidence rules; the user's no-git and single-output scope controls over its ordinary integration workflow. No main-branch status is asserted.

### cc55 reproduction and controls

I inspected all 545 lines of `checks/cc55_checks.py` in ranges before execution. All scientific values use integers and `Fraction`. To honor the stricter exact-arithmetic request, the in-memory execution also removed floating timing and replaced the incidental random half-probability branch by its exact MT bit construction:

    rng.random() < 0.5
      → Fraction(((rng.getrandbits(32)>>5)<<26)
                 + (rng.getrandbits(32)>>6), 1<<53) < Fraction(1,2).

The bit consumption preserves that random branch's original sequence. The source file was not changed. An AST check verified that no floating literal remained in the executed adaptation. No NumPy or floating linear solver was used.

The run used the script's original cases and seeds: A at (k,T,seed) = (2,3,5501), (3,2,5502), and B at (1,3,5503). The actual final result was:

    VERDICT cc55: ALL PASS (all controls fired) [33 items]

The 33 items comprise A1–A9 and C1–C5 at each of the two A cases, then B1–B4 and C6. All were observed, not inferred from the exit code. The script does not turn a failed verdict into a nonzero process exit, so stdout/RESULTS must be inspected.

| Check | Observed result |
|---|---|
| A1–A9, both multi-level cases | PASS |
| B1–B4, exact 90-unknown solves | PASS |
| C1: omit Φ_0 | FIRES |
| C2: wrong Q in DEC subtraction | FIRES |
| C3: wrong terminal κ in datum shift | FIRES |
| C4: wrong κ in Hessian/root-charge identity | FIRES |
| C5: omit terminal source from capacity | FIRES |
| C6: energies and gauge-fixed minimizers differ for the axial choices | FIRES |
| B5, informational root-charged source contrast | `dx_0 differ = True` |

The reproduced nonzero flux examples include exactly `(max|q|,max|b|,c)=(11,10,75)` and `(3,12,249)`. The data-map equality is therefore not an all-zero-source artifact.

An additional in-memory mutation consistently doubled Q^01 and its transpose. B1–B3 still passed, while the intended data comparison returned **`B4: FAIL`**. An explicit assertion checked this failure. Thus the B4 equality gate can reject an operator outside H-FREE's hypotheses. C6 alone is a non-vacuity control; this extra mutation checks the equality gate itself.

Independent exact work in this review also included the four-dimensional 24-order path-kernel enumeration, the rational Hessian-discrepancy witness `136κ_0/81`, and the separate 100-unknown two-level (CC-0) source solve described above. The geometric constants were checked exactly: `A_L=83/3`, `C_sum=121/13`, and `(1−3^(−2))^(−2)=81/64`; finite double sums for k = 1 through 12 were below 9/64. Uniformity comes from the written infinite geometric-series bound, not these finite cases. cc55 itself is a two-dimensional algebra/model check and does not test the analytic uniform TOP-cc theorem.

### Local content identities

The target, both BFT files, LINEAR_PACKAGE, and cc55 had the same hashes at initial recording and the 2026-10-28 23:54:38 UTC check. The TR review was still developing initially; the completed version used for the dependency disposition has the hash below. All seven listed identities were checked again unchanged at 2026-10-29 00:00:37 UTC. These are local SHA-256 content identities, not git revisions.

| File | SHA-256 |
|---|---|
| `COFUN_CC.md` | `2a399a7dce1de8f0a4e9b4dfb81d9f0595e8eb4d8b294e2764b1b518d98ce035` |
| `BFT_A.md` | `8074d6c5efe3648bfb28e3463a6076cf6df74c9c358a8613390044148ac6fbe0` |
| `BFT_B.md` | `b6ddf451a4dfe2028a9f23fe7fe696ce11f1c17e497709ac3761da3e7a1172c6` |
| `LINEAR_PACKAGE.md` | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |
| `checks/cc55_checks.py` | `979d1356ef6de7b73745f796fced93407cd1972f81a59cb8ee35d17b417f3dd4` |
| `CODEX_REVIEW_TR.md` | `4899db7f4badeaaea98fd586948d3cffc094710883dab3910f8c49d80502ff37` |
| `KFACTOR_O55.md` | `24ff96d127a4298805377fd450d1905729064f8599385e2b41e508f206ce6881` |

## Exactly what may be banked

1. **CONFIRMED — algebraic repair.** Bank FLUX and DEC with the terminal residual slot removed, the same Q used throughout, and `ĵ_0 = j_0+h_0^Tψ_0` in the strict-current regrouping. The flux capacity is `Σ_lπ_l(j_l)+||s_(k−1)||∞`, and each level contribution reads one face.

2. **CONFIRMED — datum independence.** Bank H-FREE for the order-averaged and fixed-order datum problems: equal minimum, all curvature and residual outputs, and 𝒩. Do not bank axial-order independence of general (CC-0) source responses; the four-dimensional witness above refutes that stronger reading.

3. **CONFIRMED — source-only linear estimates, as implications.** At Z = 1 and weight zero, for fixed `0<α<θ<1`, fixed admissible κ_±, every k ≥ 1 and T ≥ 1, and every Setting LIN^cc source with B_k = 0, bank TOP-cc, CC-FUN(a)–(c), and CC-INV with their named lane-A/package inputs and corrected constants. In particular,

       ||f_0(S)||∞ + [f_0(S)]^∞_α
         + κ_+||r_(k−1)(S)||∞ + ||x(S)||inv ≤ C N(S),

   uniformly in k, T, and admissible gauge fixing. The bound also holds with N_Σ, and with the explicitly defined weaker Ñ_Σ above. No unknown response norm remains on the right.

4. **CONFIRMED — conditional critical-point consequence.** If the complete actual critical-point source is composite-co-closed and satisfies `Ñ_Σ(S_full)≤C_*η²`, bank the corresponding source-only η² bound for its linear response, including the whole invariant curvature tower and top residual. TR's conditional transport/aggregation result can supply part of that premise. Its currently unproved higher-order source estimates must remain explicit; full nonlinear CC-CRIT is **NOT-VERIFIED** from the present proved inputs alone.

5. **NOT-VERIFIED — the remaining BFT-5(b) scope.** Field-component bounds, background transfer including CC-dec_Z, and the general weighted COF/CC-INV assembly remain open here. Update the weighted input list to acknowledge the existing QH_m and W0_m results. Nothing in this review establishes the full background-dependent clause (b), off-critical contraction, or the constructive four-dimensional Yang–Mills conclusion.
