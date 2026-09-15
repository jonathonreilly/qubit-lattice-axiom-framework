---
claim_id: admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_carries_the_lattice_green_function_infrared_and_bogoliubov_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the static law of the exponential zonal rule on the pure-state sphere under the unsoldered reading — the torus law proportional to prod_{<xy>} exp(beta s_x . s_y) with the uniform surface measure — with the transform s^(k) = N^{-1/2} sum_x e^{ikx} s_x, the Laplacian symbol E(k) = sum_i 2(1 - cos k_i) and the long-range-order parameter M_N^2 = N^{-2} <|sum_x s_x|^2>: (G1) the Legendre coefficients of exp(beta t) are positive, so the law is reflection positive for reflections through planes bisecting bonds, with arbitrary single-site factors (proved; executed symbolically for l <= 4); (G2) Gaussian domination with gradient twists holds, Z(phi) <= Z(0), and yields the infrared bound <|s^e(k)|^2> <= 1/(beta E(k)) for every component and every k != 0 (proved; the twist and plane-wave identities executed exactly on a 4^3 torus); (G3) the sum rule gives M_N^2 >= 1 - (3/beta) N^{-1} sum_{k != 0} 1/E(k), whose limit is 1 - 3 G(0)/beta with G(0) <= sqrt(3) pi/8, so long-range order holds for beta > 3 sqrt(3) pi/8 (below 21/10) (proved; executed); (G4) the classical Bogoliubov inequality at zero field, with the rotation generator and integration by parts on the sphere, gives <|s^1(k)|^2> >= (2 M_N^2/3)^2 / [(beta E)^{1/2} + (beta E + 4 M_N^2/(3N))^{1/2}]^2 for k != 0 (proved; the generator, integration-by-parts and second-derivative identities executed symbolically); (G5) hence for beta > 3 sqrt(3) pi/8 and every fixed k != 0 the transverse structure factor is sandwiched between (M^2/3)^2/(beta E(k)) and 1/(beta E(k)): the ordered unsoldered static law carries the lattice Green function's symbol in its transverse channel, which the formation law (parabolic) and the soldered six-axis law (discrete order) do not (proved). Three standard mathematical imports named at definition level; no coupling, reading or rule is selected as physical; exact symbolic arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
runner: scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py
---

# The unsoldered static law's ordered phase carries the lattice Green function in its transverse channel: an infrared bound above, a zero-field Bogoliubov bound below, and long-range order for `β > 3√3π/8`

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

Where can the repository's Coulomb-type kernel come from, inside the axioms'
readings? Block 13 showed a record-by-record law spreads correlations like
heat, never like `1/r`; block 17 showed the six-axis static law either forgets
at short range or orders with a discrete symmetry, which has no massless
channel. That leaves one candidate: the static law read with a *continuous*
possibility symmetry — records on the sphere, the rule covariant under all
internal rotations, the overlap `e^{β s·s'}`. This note shows that candidate
delivers. Its torus law is reflection positive through bond planes because
the Legendre coefficients of `e^{βt}` are positive; reflection positivity
gives Gaussian domination, and Gaussian domination bounds every component's
structure factor above by `1/(βE(k))`, the lattice Laplacian's inverse symbol.
Summing over modes forces long-range order once `β` exceeds an explicit
constant. And a classical Bogoliubov argument, run at zero field against the
long-range-order parameter itself, bounds the transverse structure factor
*below* by a multiple of the same `1/(βE(k))`. So in the ordered phase the
transverse record correlator is the lattice Green function up to constants:
the massless channel that a broken continuous symmetry must have. The
formation law cannot produce it and the six-axis static law cannot either;
this reading can.

Exactly: `a_ℓ(β) > 0` (G1); `⟨|ŝ^e(k)|²⟩ ≤ 1/(βE(k))` (G2);
`M² ≥ 1 − 3G(0)/β`, `G(0) ≤ √3π/8` (G3);
`⟨|ŝ^1(k)|²⟩ ≥ (2M_N²/3)²/[(βE)^{1/2} + (βE + 4M_N²/(3N))^{1/2}]²` (G4);
`(M²/3)²/(βE(k)) ≤ lim inf ⟨|ŝ^1(k)|²⟩ ≤ 1/(βE(k))` for `β > 3√3π/8` (G5).
Executed with exact symbolic arithmetic: 17 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's gravity node (#8093): 'the covariant scalar record statistic whose two-point function on the formation law is the lattice Green function'; blocks 13 and 17 (PRs #8147, #8151) show neither the formation law nor the soldered six-axis static law can supply it; the campaign's soldering fork (the landed possibility-covariance note)"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the Green-function channel is located: the transverse structure factor of the ordered unsoldered static law is sandwiched between multiples of 1/E(k); the gravity node's input exists under the unsoldered static reading with the exponential overlap, and under neither the formation reading nor the soldered discrete menu. Open: the exact normalization (the constant in front of 1/(4 pi r)); the Born overlap (not positive-definite beyond l = 1). Consumers: #8093's assembly (gravity node; the soldering fork's physical stake); the campaign's queue"
conditional_surface_status: "G1–G5 proved for every beta > 0 (G3–G5 for beta > 3 sqrt(3) pi/8) on tori of even side and their limits; the algebraic skeleton executed exactly (Legendre positivity to l = 4, the 4^3 torus identities, the generator and integration-by-parts identities, the bounds); conditional on the sphere as the possibility domain, the unsoldered reading and the exponential overlap as supplied conditions; three standard mathematical imports named at definition level"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "a positivity of Legendre coefficients (G1); an iterated reflection-positivity inequality and a second-order expansion (G2); a unitary transform's sum rule and an elementary integral bound (G3); integration by parts on the sphere with the quadratic-form inequality (G4); the combination (G5); every executed identity exact"
```

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
the static reading of the rule (block 01 on `main`); the product rule with the
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

## Prior art and what is new

The infrared bound and its consequence, long-range order for the classical
three-component model in three dimensions, are Fröhlich–Simon–Spencer
(1976), with the reflection-positivity route of Fröhlich–Israel–Lieb–Simon
and Biskup's lecture notes; the classical Bogoliubov inequality is Mermin's
(1967) and underlies the Mermin–Wagner theorem; on `main` the Coleman–
Mermin–Wagner notes use the Bogoliubov inequality for quantum Hamiltonians
on two-dimensional sublattices, and Gaussian domination appears in the
gauge and clock lanes for link variables. None of it is used as authority.
Nothing on `main` (search recorded in `ROUTE_PORTFOLIO.md`) treats the
sphere-valued static record law or exhibits the Green-function channel.

New here: the re-proof at scope for this rule; the zero-field Bogoliubov
bound written against the long-range-order parameter `M_N²` (no spontaneous
magnetization limit and no convexity argument); the explicit constants; and
the placement of the gravity node's kernel among the readings.

## Exact target and obligation graph

| obligation | status here |
|---|---|
| G1 Legendre positivity; bond-plane reflection positivity | proved; executed symbolically for `ℓ ≤ 4` (B1) |
| G2 Gaussian domination with gradient twists; the infrared bound | proved; the twist identity, the plane-wave Laplacian and gradient sums, and the second-order expansion executed exactly (B2–B3) |
| G3 the sum rule; `G(0) ≤ √3π/8`; long-range order for `β > 3√3π/8` | proved; executed (C1–C2) |
| G4 the classical Bogoliubov bound at zero field | proved; the generator identities, integration by parts, the second-derivative identity and the quadratic executed symbolically (D1–D3) |
| G5 the two-sided channel; the contrast | proved (from G2–G4) |
| the exact normalization; the Born overlap; the band below `3√3π/8` | open; not this note |

## Theorem G1 — Legendre positivity and reflection positivity through bond planes

**Statement.** For `β > 0` and every `ℓ ≥ 0`,
`a_ℓ(β) = (2ℓ+1)/2 · ∫_{−1}^{1} e^{βt} P_ℓ(t) dt = (2ℓ+1)/2 · β^ℓ/(2^ℓ ℓ!) ∫_{−1}^{1} (1 − t²)^ℓ e^{βt} dt > 0`.
Consequently `e^{β s·s'} = Σ_ℓ a_ℓ(β) (4π/(2ℓ+1)) Σ_m Y_ℓm(s) Ȳ_ℓm(s')` is a
positive-definite kernel on `S²`, and for the reflection `θ` through a plane
bisecting the bonds in one direction (the torus has even side, so the plane
and its antipode split `T_L` into two halves `H^±` with no shared site), and
any function `F` of the spins in `H^+` and any single-site factors
`Π_x g_x(s_x)` with `g_x ≥ 0` reflection-symmetric,
`E_L^{g}[F · F∘θ] ≥ 0`.

*Proof.* Rodrigues' formula `P_ℓ = (1/(2^ℓ ℓ!)) d^ℓ/dt^ℓ (t² − 1)^ℓ` and `ℓ`
integrations by parts (the boundary terms vanish because `(t² − 1)^ℓ` has a
zero of order `ℓ` at `±1`) turn `∫ e^{βt} P_ℓ` into
`(β^ℓ/(2^ℓ ℓ!)) ∫ (1 − t²)^ℓ e^{βt} dt`, whose integrand is positive on `(−1, 1)`.
The weight factorizes as `W^+(s_{H^+}) W^−(s_{H^-}) Π_{c} e^{β s_x·s_{θx}}` over
the crossing bonds `c = (x, θx)`, with `W^− = W^+∘θ`; expanding each crossing
factor in the kernel series and collecting the sums over `(ℓ_c, m_c)`,
`Z E[F F∘θ] = Σ_{(ℓ_c, m_c)} Π_c a_{ℓ_c}(4π/(2ℓ_c+1)) · |∫ F W^+ Π_c Y_{ℓ_c m_c}(s_x) Π_{x∈H^+} g_x dσ|² ≥ 0`
(the `H^-` integral is the complex conjugate of the `H^+` integral by the
change of variables `s ↦ θs`). ∎ Executed: the Rodrigues form of `a_ℓ` against
direct integration for `ℓ ≤ 4`, symbolically in `β` (B1).

## Theorem G2 — Gaussian domination and the infrared bound

**Statement.** For any real `φ: T_L → R` and any unit vector `e`,
`Z(φ) := ∫ Π_{⟨xy⟩} e^{−(β/2)|s_x − s_y − (φ_x − φ_y)e|²} Π_x dσ(s_x) ≤ Z(0)`.
Consequently, for every component `e` and every `k ≠ 0`,
`⟨|ŝ^e(k)|²⟩ ≤ 1/(βE(k))`, and the same holds for the law with any additional
reflection-symmetric single-site factors.

*Proof.* *Domination.* Put `s̃_x = s_x − φ_x e`; then
`|s_x − s_y − (φ_x − φ_y)e| = |s̃_x − s̃_y|`, so `Z(φ)` is the untwisted
interaction integrated against the shifted site measures `dσ(s̃_x + φ_x e)`.
For a bond-plane reflection `θ`, G1 (the crossing weights are the untwisted
positive-definite kernel `e^{−(β/2)|s̃_x − s̃_{θx}|²} = e^{−β} e^{β s̃_x·s̃_{θx}}`
between the halves, and the site measures are single-site factors) gives
the quadratic-form inequality `Z(φ) ≤ Z(φ^{+})^{1/2} Z(φ^{−})^{1/2}` where `φ^{+}`
equals `φ` on `H^+` and `φ∘θ` on `H^-`, and `φ^{−}` the reverse. Iterating over
all bond planes in the three directions (each step at most doubles the
number of "reflected" sites and the product of the two factors' exponents
telescopes) bounds `Z(φ)` by a geometric mean of `Z` at fields constant along
every direction, i.e. constant fields, and `Z(constant) = Z(0)` since a common
shift of all spins leaves the differences unchanged. *The bound.* Take
`φ = λ ψ`, `ψ_x = cos(k·x)`, and expand `Z(λψ)/Z(0) = ⟨exp(βλ X − (βλ²/2) Σ_b (ψ_x − ψ_y)²)⟩`
with `X = Σ_{⟨xy⟩} (ψ_x − ψ_y)(s_x − s_y)·e`. The law is invariant under
`s ↦ −s`, so `⟨X⟩ = 0`, and `Z(λψ) ≤ Z(0)` for all small `λ` forces the
second-order coefficient to be nonpositive: `β²⟨X²⟩ ≤ β Σ_b (ψ_x − ψ_y)²`.
Now `X = Σ_x s_x^e Σ_{y∼x} (ψ_x − ψ_y) = E(k) Σ_x s_x^e ψ_x` because the plane
wave is an eigenfunction of the lattice Laplacian, and
`Σ_b (ψ_x − ψ_y)² = Σ_x ψ_x Σ_{y∼x}(ψ_x − ψ_y) = E(k) Σ_x ψ_x² = E(k) N/2` for
`k ≠ 0` with `2k ≠ 0` (and `E(k) N` when `2k = 0`, which only strengthens what
follows). Hence `⟨(Σ_x s_x^e cos(k·x))²⟩ ≤ N/(2βE(k))`, likewise with the sine,
and adding, `⟨|Σ_x s_x^e e^{ik·x}|²⟩ ≤ N/(βE(k))`, i.e. `⟨|ŝ^e(k)|²⟩ ≤ 1/(βE(k))`.
Single-site factors enter the site measures only. ∎ Executed: the twist
identity symbolically; the eigenfunction identity and the gradient sum on
the `4³` torus at two wavevectors (B2); the second-order expansion (B3).

## Theorem G3 — the sum rule and long-range order

**Statement.** `M_N² ≥ 1 − (3/β) N^{−1} Σ_{k≠0} 1/E(k)`, and
`N^{−1} Σ_{k≠0} 1/E(k) → G(0) := ∫_{[−π,π]³} d³k/((2π)³ E(k)) ≤ √3π/8`. Hence
`M² := lim inf_L M_N² ≥ 1 − 3G(0)/β > 0` whenever `β > 3√3π/8`, in particular
for `β ≥ 21/10`.

*Proof.* By unitarity `Σ_k Σ_e ⟨|ŝ^e(k)|²⟩ = Σ_x ⟨|s_x|²⟩ = N`, so
`N M_N² = Σ_e ⟨|ŝ^e(0)|²⟩ ≥ N − Σ_{k≠0} 3/(βE(k))` by G2. The Riemann sums
tend to the integral (the integrand is bounded away from `k = 0` and
`1/E(k) ≤ π²/(4|k|²)` near it, integrable in three dimensions). For the bound:
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

## Theorem G5 — the transverse channel is the lattice Green function up to constants

**Statement.** For `β > 3√3π/8` and every fixed `k ≠ 0`,
`(M²/3)²/(βE(k)) ≤ lim inf_L ⟨|ŝ^1(k)|²⟩ ≤ lim sup_L ⟨|ŝ^1(k)|²⟩ ≤ 1/(βE(k))`,
with `M² ≥ 1 − 3G(0)/β > 0`. The same holds for `ŝ^2(k)` by symmetry.

*Proof.* The upper bound is G2. In G4 let `N → ∞` at fixed `k` (the
wavevector lies in the torus lattice for all `L` in a subsequence, or use a
sequence of wavevectors tending to `k` with the continuity of `E`): the
correction `4M_N²/(3N)` vanishes and the bound tends to `(M²/3)²/(βE(k))`
along the subsequence realizing `lim inf M_N²`. ∎

*Reading.* Above the threshold the record field has a preferred direction,
and its components across that direction fluctuate with a structure factor
pinned between two multiples of `1/E(k)`, the symbol of the lattice
Laplacian's inverse — the kernel whose large-distance form is the gravity
lane's `1/(4π r)`. That channel is a consequence of a broken *continuous*
symmetry: the soldered six-axis law (block 17) orders with a discrete
symmetry and the rotation generator that drives G4 does not exist there; the
formation law (block 13) is causal and its kernel is parabolic. The
unsoldered static reading with the exponential overlap is the one reading
among those examined in this lane under which the gravity node's kernel is a
record statistic.

## No-Go Discipline Gate

This note's content is positive (the channel exists); the negative sentences
it relies on — no such channel from the formation law or the soldered
six-axis law — belong to blocks 13 and 17 and are not re-proved here. The
gate is answered for the positive claim's hidden assumptions.

### N1 — Routes by which the sandwich could fail

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a coupling below the threshold | `β ≤ 3√3π/8` | not claimed either way (the true threshold is lower; not decided here) | open |
| 2 an overlap without Legendre positivity | the Born overlap `(1+t)/2` has `a_ℓ = 0` for `ℓ ≥ 2` (nonnegative, degenerate) | G1 holds; G2's twist argument uses the Gaussian form of the exponential overlap and is not claimed for it | narrowed |
| 3 the transverse direction | `e_1` is transverse to `e_3` only on average | G4 uses the symmetry of the components, not a chosen direction; the bound is for `ŝ^1` and `ŝ^2` alike | RULED OUT AT SCOPE |
| 4 wavevectors not on the torus lattice | `k` fixed as `L` varies | a subsequence or continuity of `E(k)` (G5) | RULED OUT AT SCOPE |

### N2 — Wall-independence audit
Walls: the sphere as the domain, the unsoldered reading, the static reading, the exponential overlap, the torus of even side. Independent; each defines the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: none in the theorems.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| the possibility-covariance note (main) | the two readings; the sphere domain | the unsoldered reading as supplied | yes |
| block 01 (main) | the static reading | the object | yes |
| PRs #8147, #8151 (open; not inputs) | the formation law's kernel; the six-axis order | the contrast in G5's reading | context only |
| the three standard imports | mathematics | named at definition level | declared |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "the transverse channel is the lattice Green function up to constants" | executed: `a_ℓ` for `ℓ ≤ 4`; the generator identities; the single-bond second derivative; the quadratic | executed: the torus Laplacian identity at every site of the `4³` torus | executed: two wavevectors' gradient sums | executed: the integration-by-parts identity for three polynomials on the sphere | proved for every `β > 3√3π/8` (G5); the band below not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no coupling or overlap; none is a wall.

### N7 — Steelman
Hostile reviewer: "This is the 1976 theorem plus the classical inequality of 1967; the framework adds nothing." Reply: the framework question is *which reading* of the axioms yields the gravity node's kernel as a record statistic, and the answer needed the pair of negatives (blocks 13, 17) and this positive with its constants; the zero-field Bogoliubov form against `M_N²` is a small technical economy. Conceded: the constants are not sharp and the normalization is not fixed.

### N8 — Cross-cycle echo
Block 13's linearization (the massless causal Gaussian instance under the Born overlap) and this note's massless transverse channel are the same physics seen in the two readings; block 17's six-axis order is the discrete counterpart with no such channel.

## Falsifiers
- An `ℓ ≤ 4` at which the Rodrigues form of `a_ℓ(β)` differs from the direct integral (B1).
- A site of the `4³` torus where the plane wave is not a Laplacian eigenfunction with eigenvalue `E(k)`, or a gradient sum differing from `E(k) Σ ψ²` (B2); a second-order coefficient not equal to `β² X² − β Σ(ψ_x − ψ_y)²` (B3).
- A sample point violating `1 − cos u ≥ 2u²/π²`, a Green-function bound other than `√3π/8`, or a threshold at or above `21/10` (C1–C2).
- A generator identity or single-bond second-derivative identity that fails, or a polynomial for which the sphere integral of `L F` is nonzero (D1–D2); a quadratic root other than the displayed form or a limit other than `M²/(3(βE)^{1/2})` (D3).

## Boundaries and non-claims
This note proves, for the unsoldered static law with the exponential overlap, the infrared bound, long-range order above an explicit coupling, and a two-sided Green-function sandwich for the transverse structure factor; it does not fix the normalization of the kernel, does not treat couplings below `3√3π/8`, does not treat the Born overlap, does not select a reading, rule or coupling as physical, and adopts no clause. No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- The possibility-covariance note and block 01 (both on `main`): the readings and the object; proposed, unaudited. PRs #8147 and #8151 (open) referenced for context only.
- Re-proved at scope: G1 (Rodrigues and the sum-of-squares expansion), G2 (Gaussian domination and the expansion), G3 (the sum rule and the integral bound), G4 (integration by parts, the quadratic-form inequality, the second derivative), G5.
- Named standard imports at definition level (never as authority for physics): the Legendre expansion of a smooth function and the addition theorem for spherical harmonics; the unitarity of the discrete torus transform; the integration-by-parts identity for the divergence-free rotation field on the sphere.
- Reference only (named, not used): Fröhlich–Simon–Spencer (1976); Fröhlich–Israel–Lieb–Simon (1978); Mermin (1967); Biskup's lecture notes.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane and take it; no subagents). The control (`specs/supervisor_control_block19_sphere_static.py`) checked the Legendre forms, the torus identities, the generator and integration-by-parts identities, the bound and the quadratic before the contract, and caught the sign convention of the generator (`L s^3 = −s^1`, `L s^1 = s^3`), which enters only through an absolute value; the lens pass is in `GOAL_block19.md`; the primary seat wrote G1–G5 and the runner; the refuting pass (`CHECKER_block19_findings.md`) recomputed the Legendre coefficients by the generating-function route, the gradient sum by a direct bond enumeration on a `6×4×4` torus, the second-derivative identity by a second choice of generator axis, and the integral bound by a second inequality. Facts settled while executing: the runner's name scan treats Legendre, Rodrigues and Bogoliubov as names of standard objects (like Gaussian, Laplacian or Green function) and restricts authors' names to Prior art, Imports and the Premises' file citation; the gradient sum on the torus equals `E(k) N/2` when `2k ≠ 0` and `E(k) N` when `2k = 0` (the note's proof covers both); the control caught the generator's sign convention before the primary.

## Verification

```bash
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unsoldered_sphere_static_law_ordered_phase_transverse_channel_green_function_2026_09_15.py --mutation infrared_bound_direction_reversed
```

Families: A authority and inputs; B Legendre positivity, the torus identities and the second-order expansion; C the Green-function bound and the threshold; D the generator identities, integration by parts, the second derivative and the quadratic; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=17 FAIL=0`.
