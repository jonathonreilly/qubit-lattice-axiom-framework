---
claim_id: admissibility_rule_sphere_static_law_zero_field_component_fourier_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Supplied uniform-sphere nearest-neighbour exponential static law on even three-dimensional tori: Legendre positivity and real reflection form; finite Gaussian domination explicitly imported with normalized nearest-neighbour interaction; component infrared and zero-field rotation-generator bounds; controlled magnetization-square liminf and two-sided Fourier bounds along every nonzero limiting momentum sequence. No selected extremal-state transverse channel, pointwise real-space decay, physical identification or universal exclusion of other models is claimed."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py
---

# Sphere static law: zero-field component Fourier bounds

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

For the supplied sphere-spin static model, a precise finite-volume Gaussian-domination import gives an upper bound on each zero-field component structure factor. The rotation-generator argument gives a lower bound in terms of the finite-volume squared total magnetization. Together with the sum rule and a controlled small-momentum limit, these give the two-sided Fourier bounds stated below.

The finite torus law is rotation invariant: all three components are equivalent, and no magnetization direction is selected. These Fourier bounds do not identify an extremal-state transverse correlator, pointwise real-space `1/r` decay, or a physical gravity observable. They do not exclude any formation or discrete-spin model.

The original shifted-spin argument omitted variable norm factors and did not prove Gaussian domination. That argument and all original controls remain byte-exact in [the recovery manifest](work_history/review_loop/pr8153/original-manifest.json). Gaussian domination is now a declared mathematical import, not a claimed new proof.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
artifact_role: theorem
next_trace_action: "Retain supplied-model zero-field component Fourier bounds; physical identification and negative classifications remain deferred."
conditional_surface_status: "Uniform sphere measure, positive exponential nearest-neighbour coupling, even periodic three-dimensional torus; Gaussian domination imported with explicit normalization."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
No negative certificate or gravity-channel identification is issued.

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "Each site has
a domain of local possibilities. The full one-site possibility domain has
algebraic presentation `M_2(C)`." — "No possibility is privileged." — "There
is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations." — "For each site, the probability
distribution over the possibilities is determined by, and varies with, the
nearest-neighbor conditions." — "Records form."

**Readings carried, named, nothing new adopted.** The pure-state sphere `S²`
as the possibility domain and the *unsoldered* reading (independent internal
rotations) from the landed possibility-covariance note
([`POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`](POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md));
the static law explicitly defined below; the product rule with the
exponential overlap `f(t) = e^{βt}`, `β > 0` supplied (the sphere counterpart
of the six-axis weights).

**The torus law.** `T_L = (Z/2L Z)³`, `N = (2L)³`, `3N` bonds;
`μ_L(ds) = Z_L^{−1} Π_{⟨xy⟩} e^{β s_x·s_y} Π_x dσ(s_x)`, `dσ` the uniform
probability measure on `S²`. For unit spins `e^{β s_x·s_y} = e^{β} e^{−(β/2)|s_x − s_y|²}`,
so `μ_L` is also the law with weight `Π e^{−(β/2)|s_x − s_y|²}`. The
transform `ŝ(k) = N^{−1/2} Σ_x e^{ik·x} s_x`, `k ∈ (π/L) Z³` modulo `2π`;
`E(k) = Σ_{i=1}^{3} 2(1 − cos k_i)`; the long-range-order parameter
`M_N² = N^{−2} ⟨|Σ_x s_x|²⟩ = N^{−1} ⟨|ŝ(0)|²⟩`. Rotation generators: for a
site `x`, `L_x F = (e_2 × s_x)·∇_{s_x} F`, so `L_x s_x^3 = −s_x^1`,
`L_x s_x^1 = s_x^3`, `L_x s_x^2 = 0`, and `L_x(s_x·s_y) = e_2·(s_x × s_y)`.

**Standard mathematical imports (definition level, never authority for
physics).** (i) A smooth function on `[−1, 1]` is the sum of its Legendre
series `Σ_ℓ a_ℓ P_ℓ(t)`, `a_ℓ = (2ℓ+1)/2 ∫ f P_ℓ`, and
`P_ℓ(s·s') = (4π/(2ℓ+1)) Σ_m Y_ℓm(s) Ȳ_ℓm(s')`. (ii) The discrete transform on
the torus is unitary: `Σ_k |ŝ^e(k)|² = Σ_x (s_x^e)²`. (iii) For a smooth
function `F` on `S²` and the divergence-free field `e_2 × s`,
`∫ (e_2 × s)·∇F dσ = 0` (executed for polynomials; cited for smooth functions).



**Gaussian-domination import.** Theorem 4.6, printed pages 40–41, of
[Marek Biskup, lecture notes on reflection positivity, Theorem 4.6](https://www.math.ucla.edu/~biskup/PDFs/papers/Prague-School.pdf)
is load-bearing mathematics. Use its nearest-neighbour interaction, an even periodic torus, the identical compact single-site probability measure `dσ` on `S²⊂R³`, and nonnegative theorem parameter `b`. With ordered nearest-neighbour weights `J_xy=1/6` (periodized with multiplicities on side two), its twisted partition function has exponent `−b Σ_{x,y}J_xy |s_x−s_y+h_x−h_y|²` and is maximal at constant `h`. Set `b=3β/2` and `h_x=−φ_x e`. The ordered sum counts each bond twice, so the exponent becomes `−(β/2)Σ_{⟨xy⟩}|s_x−s_y−(φ_x−φ_y)e|²`, exactly the object below. No arbitrary site-dependent measure or single-site-factor extension is imported.

## Prior art and what is new

The infrared method is established mathematical work of Fröhlich–Simon–Spencer and Fröhlich–Israel–Lieb–Simon. Biskup's Gaussian-domination theorem is explicitly used above. The zero-field rotation-generator inequality is in the classical Bogoliubov/Mermin tradition. The contribution retained here is the normalization and combination for the supplied model, with explicit finite-volume and momentum limits; it does not locate a physical kernel among the framework's readings.

## Exact target and obligation graph

| Object | Status and scope |
|---|---|
| Legendre coefficients and real reflection form | Complete positive-integrand and factorization proofs; coefficients through degree four checked by primary |
| Gaussian domination | Named imported theorem with the exact normalization above |
| Infrared bound | Derived below, including self-inverse momenta |
| Sum rule and magnetization-square liminf | Small-momentum lattice shell estimate supplied below |
| Zero-field lower bound | Complete finite-volume rotation-generator proof |
| Two-sided component Fourier bound | Every allowed sequence `k_L→k≠0`, using eventual liminf control |
| Transverse extremal state, real-space asymptotic, physical model selection | Not established; deferred |

## Theorem G1 — Legendre positivity and reflection positivity through bond planes

**Statement.** For `β > 0` and every `ℓ ≥ 0`,
`a_ℓ(β) = (2ℓ+1)/2 · ∫_{−1}^{1} e^{βt} P_ℓ(t) dt = (2ℓ+1)/2 · β^ℓ/(2^ℓ ℓ!) ∫_{−1}^{1} (1 − t²)^ℓ e^{βt} dt > 0`.
Consequently `e^{β s·s'} = Σ_ℓ a_ℓ(β) (4π/(2ℓ+1)) Σ_m Y_ℓm(s) Ȳ_ℓm(s')` is a
positive-definite kernel on `S²`, and for the reflection `θ` through a plane
bisecting the bonds in one direction (the torus has even side, so the plane
and its antipode split `T_L` into two halves `H^±` with no shared site), and
any real-valued square-integrable function `F` of the spins in `H^+`, `E_L[F · F∘θ] ≥ 0`.

*Proof.* Rodrigues' formula `P_ℓ = (1/(2^ℓ ℓ!)) d^ℓ/dt^ℓ (t² − 1)^ℓ` and `ℓ`
integrations by parts (the boundary terms vanish because `(t² − 1)^ℓ` has a
zero of order `ℓ` at `±1`) turn `∫ e^{βt} P_ℓ` into
`(β^ℓ/(2^ℓ ℓ!)) ∫ (1 − t²)^ℓ e^{βt} dt`, whose integrand is positive on `(−1, 1)`.
The weight factorizes as `W^+(s_{H^+}) W^−(s_{H^-}) Π_{c} e^{β s_x·s_{θx}}` over
the crossing bonds `c = (x, θx)`, with `W^− = W^+∘θ`; expanding each crossing
factor in the kernel series and collecting the sums over `(ℓ_c, m_c)`,
`Z E[F F∘θ] = Σ_{(ℓ_c, m_c)} Π_c a_{ℓ_c}(4π/(2ℓ_c+1)) · |∫ F W^+ Π_c Y_{ℓ_c m_c}(s_x) Π_{x∈H^+} dσ|² ≥ 0`
(the `H^-` integral is the complex conjugate of the `H^+` integral by the
change of variables `s ↦ θs`). ∎ Executed: the Rodrigues form of `a_ℓ` against
direct integration for `ℓ ≤ 4`, symbolically in `β` (B1).

## Theorem G2 — Gaussian domination and the infrared bound

**Imported starting bound.** For real `φ:T_L→R` and a unit vector `e`,
`Z(φ)=∫exp[−(β/2)Σ_{⟨xy⟩}|s_x−s_y−(φ_x−φ_y)e|²]Π_x dσ(s_x)≤Z(0)`
by the Gaussian-domination theorem and parameter mapping in Premises. The spins shifted by `φ_x e` are not unit vectors: the general identity contains the factors `exp[−β(|u|²+|v|²)/2]exp(βu·v)`. The false constant norm replacement is not used.

**Infrared derivation.** Put `φ=λψ` and
`X=Σ_{⟨xy⟩}(ψ_x−ψ_y)(s_x−s_y)·e`, `S_2=Σ_{⟨xy⟩}(ψ_x−ψ_y)²`.
Expansion gives `Z(λψ)/Z(0)=⟨exp(βλX−βλ²S_2/2)⟩`. Spin inversion implies `⟨X⟩=0`, so domination implies `β²⟨X²⟩≤βS_2`.
For a cosine or sine mode of momentum `k`, summation over bonds gives
`X=E(k)Σ_x s_x^e ψ_x` and `S_2=E(k)Σ_xψ_x²`.
If `2k≠0` modulo `2π`, both cosine and sine norms are `N/2`; their two variance bounds add to
`⟨|Σ_xe^{ik·x}s_x^e|²⟩≤N/(βE(k))`.
If `k≠0` but `2k=0`, the wave is real, its cosine norm is `N` and its sine vanishes. The single cosine bound is then `⟨(Σ_x s_x^e cos(k·x))²⟩≤N/(βE(k))`, giving the same normalized result directly. Thus for every nonzero allowed mode,
`⟨|ŝ^e(k)|²⟩≤1/(βE(k))`. ∎

The primary checks the algebraic shift and second-order expansion and two non-self-inverse modes on the `4³` torus. The self-inverse calculation above is written proof; original independent controls separately checked two such modes. Neither finite control executes the imported domination theorem.

## Theorem G3 — the sum rule and long-range order

**Statement.** `M_N² ≥ 1 − (3/β) N^{−1} Σ_{k≠0} 1/E(k)`, and
`N^{−1} Σ_{k≠0} 1/E(k) → G(0) := ∫_{[−π,π]³} d³k/((2π)³ E(k)) ≤ √3π/8`. Hence
`M² := lim inf_L M_N² ≥ 1 − 3G(0)/β > 0` whenever `β > 3√3π/8`, in particular
for `β ≥ 21/10`.

*Proof.* By unitarity `Σ_k Σ_e ⟨|ŝ^e(k)|²⟩ = Σ_x ⟨|s_x|²⟩ = N`, so
`N M_N² = Σ_e ⟨|ŝ^e(0)|²⟩ ≥ N − Σ_{k≠0} 3/(βE(k))` by G2. To justify the singular Riemann sum, write `h=π/L`, `k=hn` using representatives in `[-π,π)^3`. Since `E(k)≥4|k|²/π²`, the normalized contribution from `0<|k|≤δ` is at most a constant times `L^{-1} Σ_{0<|n|≤δ/h}|n|^{-2}`. The integer shell `j≤|n|<j+1` contains at most `C(j+1)²` points (cover each point by its disjoint unit cube in an annulus of fixed larger thickness), so this sum is at most `C'(δL+1)`. The contribution is therefore at most `C''δ+O(1/L)`, uniformly in `L`. Away from a small ball the integrand is continuous and ordinary Riemann sums apply; its integral inside the ball is also `O(δ)`. First take `L→∞`, then `δ→0`. For the bound:
`1 − cos u ≥ 2u²/π²` on `[−π, π]` (the function `(1 − cos u)/u²` decreases on
`(0, π]`), so `E(k) ≥ (4/π²)|k|²` and
`G(0) ≤ (π²/4)(2π)^{−3} ∫_{|k| ≤ √3π} d³k/|k|² = (π²/4)(2π)^{−3} 4π·√3π = √3π/8`.
The threshold `3√3π/8 = 2.0405…` is below `21/10`. ∎ Executed: the inequality
at sample points and the integral bound symbolically (C1); the threshold
comparison (C2).

## Theorem G4 — the classical Bogoliubov bound at zero field

**Statement.** For `k ≠ 0` and every `N`,
`⟨|ŝ^1(k)|²⟩ ≥ (2M_N²/3)² / [(βE(k))^{1/2} + (βE(k) + 4M_N²/(3N))^{1/2}]²`.

*Proof.* Let `c_x = e^{−ik·x}` and `L = Σ_x c_x L_x`, `w = Π_{⟨xy⟩} e^{β s_x·s_y}`.
*Integration by parts:* for smooth `G`, `∫ L_x G dσ(s_x) = 0` (import (iii)),
hence `⟨L G⟩ = −⟨G · L log w⟩`. *The first application:* with
`F = ŝ^1(k) m̂`, `m̂ = N^{−1} Σ_y s_y^3`:
`L ŝ^1(k) = N^{−1/2} Σ_y e^{ik·y} c_y L_y s_y^1 = N^{−1/2} Σ_y s_y^3 = N^{1/2} m̂` and
`L m̂ = N^{−1} Σ_y c_y L_y s_y^3 = −N^{−1} Σ_y e^{−ik·y} s_y^1 = −N^{−1/2} ŝ^1(k)^*`, so
`⟨L F⟩ = N^{1/2} ⟨m̂²⟩ − N^{−1/2} ⟨|ŝ^1(k)|²⟩`. By the three-fold symmetry of the
components, `⟨m̂²⟩ = M_N²/3`. *The quadratic-form inequality:*
`|⟨L F⟩|² = |⟨F · L log w⟩|² ≤ ⟨|F|²⟩ ⟨|L log w|²⟩ ≤ ⟨|ŝ^1(k)|²⟩ ⟨|L log w|²⟩`
using `|m̂| ≤ 1`. *The second application:* with `G = (L log w)^*`,
`⟨|L log w|²⟩ = −⟨L (L log w)^*⟩ = −⟨L L̄ log w⟩`, and for a single bond
`−(c_x L_x + c_y L_y)(c̄_x L_x + c̄_y L_y)(s_x·s_y) = |c_x − c_y|² (s_x^1 s_y^1 + s_x^3 s_y^3)`,
so `⟨|L log w|²⟩ = β Σ_{⟨xy⟩} |c_x − c_y|² ⟨s_x^1 s_y^1 + s_x^3 s_y^3⟩ ≤ β Σ_{⟨xy⟩} |e^{−ik·x} − e^{−ik·y}|² = β N E(k)`
(the gradient sum of the plane wave, with `|s_x^1 s_y^1 + s_x^3 s_y^3| ≤ 1`).
*Combining:* with `u = ⟨|ŝ^1(k)|²⟩^{1/2}`,
`N^{1/2} M_N²/3 − N^{−1/2} u² ≤ u (βNE(k))^{1/2}`, i.e.
`u²/N + (βE)^{1/2} u − M_N²/3 ≥ 0`, whose positive root is the displayed
bound. ∎ Executed: the generator identities, the single-bond second
derivative and integration by parts for polynomials symbolically (D1–D2);
the quadratic's root and its limit (D3).

## Theorem G5 — component bounds along momentum sequences

**Statement.** Let `β>3√3π/8`, `M²=liminf_L M_N²`, and choose any sequence of nonzero torus momenta `k_L` tending modulo `2π` to a fixed `k≠0`. For every fixed component `e`,
`(M²/3)²/(βE(k)) ≤ liminf_L ⟨|ŝ^e(k_L)|²⟩ ≤ limsup_L ⟨|ŝ^e(k_L)|²⟩ ≤ 1/(βE(k))`,
where `M²≥1−3G(0)/β>0`.

*Proof.* The upper bound follows for every `L` from the infrared bound and continuity of `E` at nonzero `k`. Fix `η` with `0<η<M²`. Eventually `M_N²≥M²−η`, while `M_N²≤1`. The finite lower bound is therefore at least
`[2(M²−η)/3]²/[sqrt(βE(k_L))+sqrt(βE(k_L)+4/(3N))]²`.
Taking the liminf and then `η↓0` gives the displayed lower bound. This uses all sufficiently large volumes, not a selected subsequence attaining the magnetization liminf. Component symmetry extends the same result to all three components. ∎

The zero-field torus measures remain rotation invariant. The result compares Fourier structure factors with the inverse Laplacian symbol at fixed nonzero limiting momentum. It supplies no preferred magnetization direction, no extremal ordered-state transverse correlation, and no pointwise real-space decay law.

## No-Go Discipline Gate

### N1 — Negative certification deferred
The original route list did not establish five independent exact-target attacks. Universal exclusions of formation and discrete-spin laws, and a unique physical candidate, are withdrawn. No negative certificate is issued.

### N2 — Conditions and imports
The uniform sphere measure, static exponential interaction and periodic torus are supplied mathematical conditions. Gaussian domination is an explicit theorem import, not a new framework axiom or an assertion of independent walls.

### N3 — Corrected boundaries
Shifted spins are not unit. Self-inverse modes need their own normalization calculation. Rotation-invariant finite-volume component bounds do not identify an extremal-state transverse observable.

### N4 — Input scope
The linked possibility-covariance parent supplies conditional representation vocabulary. It does not select a static law or coupling. The Gaussian theorem supplies only the finite domination statement under its stated hypotheses.

### N5 — Evidence resolution
The primary executes coefficients through degree four, two non-self-inverse torus modes and four sphere-polynomial integrals. The self-inverse proof, shell estimate and momentum-sequence argument are written proofs, not new primary executions. The imported theorem is not independently executed by this runner.

### N6 — Primitive boundary
No primitive supplies an overlap, coupling, state or physical interpretation.

### N7 — Other kernels
The kernel `(1+t)/2` has Legendre coefficients `1/2,1/2,0,...` and is positive semidefinite, although not strictly positive in higher degrees. This note neither denies its reflection positivity nor extends the exponential Gaussian-domination argument to it.

### N8 — Recovery
The original complete arguments and controls are preserved in the recovery manifest. Corrected formation and discrete-model scopes supply no universal exclusion used here.

## Falsifiers
- An `ℓ ≤ 4` at which the Rodrigues form of `a_ℓ(β)` differs from the direct integral (B1).
- A site of the `4³` torus where the plane wave is not a Laplacian eigenfunction with eigenvalue `E(k)`, or a gradient sum differing from `E(k) Σ ψ²` (B2); a second-order coefficient not equal to `β² X² − β Σ(ψ_x − ψ_y)²` (B3).
- A sample point violating `1 − cos u ≥ 2u²/π²`, a Green-function bound other than `√3π/8`, or a threshold at or above `21/10` (C1–C2).
- A generator identity or single-bond second-derivative identity that fails, or a polynomial for which the sphere integral of `L F` is nonzero (D1–D2); a quadratic root other than the displayed form or a limit other than `M²/(3(βE)^{1/2})` (D3).

## Boundaries and non-claims

This note gives zero-field component Fourier bounds for the supplied sphere static law using an explicit Gaussian-domination import; it establishes no selected transverse-state correlator, pointwise real-space decay or physical model classification, and adopts no clause.

No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.

The uniform sphere measure and exponential interaction are declared model inputs; all load-bearing mathematical imports are explicitly identified.

## Imports

The linked axiom memo supplies only its quoted sentences. The possibility-covariance parent supplies the conditional sphere/rotation representation, not a selected probability law. The finite static measure is explicitly defined here.

Biskup's Theorem 4.6, with the hypotheses and `b=3β/2` mapping in Premises, is a load-bearing Gaussian-domination import. It is not merely a reference. The remaining mathematical imports are the Legendre expansion of the exponential and spherical-harmonic addition formula, finite-torus transform unitarity, and integration by parts for the divergence-free sphere rotation field. The Rodrigues integral, infrared expansion, sum-rule estimates and zero-field quadratic argument are given here. Fröhlich–Simon–Spencer, Fröhlich–Israel–Lieb–Simon and Mermin identify the historical mathematical setting, not additional physical premises.

## Review record

All original proof versions, historical controls and outputs remain byte-exact in the recovery manifest. The original independent reviewer identified the shifted-norm, normalization, limit and interpretation defects. This source repair uses the named theorem import, preserves the useful finite identities and withdraws unsupported physical/negative conclusions. Same-session affected-source confirmation is pending; the author has executed no scientific primary or replacement control.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py --mutation infrared_bound_direction_reversed
```

Families: A authority and inputs; B Legendre positivity, the torus identities and the second-order expansion; C the Green-function bound and the threshold; D the generator identities, integration by parts, the second derivative and the quadratic; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=17 FAIL=0`.
