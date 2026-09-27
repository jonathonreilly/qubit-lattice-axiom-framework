---
claim_id: admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_it_never_outruns_the_long_waves_and_ends_at_a_stretch_of_root_two_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, for a uniform isotropic stretch of a per-axis walk F(k, b) with F(k, 0) = sin k and first-order term sin k cos^2 k, under the covariance principle of block 182 (pushed; each further stretch acts on the stretched walk as a relabelling, dF/db = p dF/dk), and reading symmetric books at finite stretch as block 182 T6 does (on single waves the momentum p that generates further stretch is parallel to the stretched walk's velocity; block 179 T1, pushed, re-derived): (T1) the books hold at every stretch iff p = gamma(b) F dF/dk, so u = F^2 obeys u_tau = (du/dk)^2/2, one family of walks up to reparametrisation (block 182's self-consistent flow); (T2) with the stretch l fixed by the long-wave speed dF/dk(0) = 1/l, the family is k = k0 + ((l^2 - 1)/2) sin 2k0, F = sin k0 sqrt(sin^2 k0 + l^2 cos^2 k0), and keeps the species corners; (T3) for 0 < l^2 < 2 it is a real-analytic relabelling of the free walk, and every wave with E != 0 is strictly slower than 1/l per label (the bound is approached, not attained, at the species points); (T4) no family continuous in l and twice differentiable in k reaches l^2 = 2, where the band top has zero slope and infinite curvature, 1 - F proportional to |k - pi/2|^(4/3); (T5) at every l != 1 it has infinite reach, since u_kk along characteristics has a pole off the real line; (T6) supplying block 181 T1's identification at every stretch (the energy current equals the momentum per unit strain) normalises the strain variable: gamma = 1, b = (1 - l^2)/2, and the long-wave metric l^2 = 1 - 2b is exactly linear in it (block 69 T4's leading form (1 + b)^2 agrees only to first order); for diagonal anisotropic stretches with each axis's generator of the form gamma(b_a) F dF/dk, P parallel to v alone forces a common constant gamma; (T7) for every walk h = sum_a F_a(k_a) X_a + mu Gamma with anticommuting involutions and real per-axis hops, block 181's objects built from divided differences give the site energy a current P^s whose current K^s is symmetric, exactly (only h^2 being a number is used), with P^s = F F' on single waves: every per-axis completion keeps its own books on pairs of waves, and this family's stretch generator equals P^s on single waves; placing the stretch generator as P^s on pairs is open; (T8) at fixed label momentum every wave's energy obeys d log E/d log l = -l^2 |v|^2 exactly, the law of a relativistic free particle with fixed momentum per label, so the content's pressure is sum E l^2 |v|^2/(3V), strictly between 0 and rho/3 per moving positive-energy wave, and block 180's first-order result is its l = 1 case. So covariance with symmetric books fixes the stretch rule and the strain variable; it passes the speed limit up to sqrt 2 and is not of finite reach. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_2026_09_27.py
---

# Symmetric books at every stretch fix one stretch rule: it never outruns the long waves, and it ends at a stretch of √2

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 69 as landed, block 182's covariance principle and block 182's reading of books at finite stretch; blocks 179, 181 and 182 are pushed and placed, and the facts used from them are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within block 69 as landed on main (the two-step coupling of the walk to a uniform strain) and asks which completion to finite stretch keeps the walker's books symmetric at every stretch; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 69 (landed) fixes the two-step coupling at first order in the strain and leaves its completion open. Block 182 (pushed) found a trilemma at finite stretch: reach three, covariance (each further stretch a relabelling) and symmetric books cannot all hold. It left open whether any covariant completion outside reach three is admissible at every stretch. This note answers that for the pair "covariance with symmetric books".

- **T1: the books fix the rule.** Among covariant stretches, the momentum that generates further stretch is parallel to the stretched walk's velocity on every single wave, at every stretch, iff the generator is `γ(b) F ∂_kF`. So `u = F²` obeys `∂_τu = (∂_ku)²/2` with `τ = ∫γ db`. That is one family of walks, block 182's self-consistent flow, up to reparametrisation. The other two named covariant completions fail the books at every `ℓ ≠ 1`.
- **T2: in closed form.** With `ℓ` fixed by the long-wave speed, `∂_kF(0) = 1/ℓ`, as in blocks 176 and 182, the family is

  `k = k₀ + ((ℓ² − 1)/2) sin 2k₀`,  `F = sin k₀ √(sin² k₀ + ℓ² cos² k₀)`.

  Its first two orders are block 69's and block 182 T4(b)'s. It keeps the species corners, with speed `±1/ℓ` at `k = 0, π`.
- **T3: it never outruns the long waves.** For `0 < ℓ² < 2` it is a real-analytic relabelling of the free walk. Every wave with `E ≠ 0` is strictly slower than `1/ℓ` per label, per axis and in three dimensions; the bound is approached at the species points, not attained. The linear completion fails this beyond `ℓ = 7/6`, and the flow of the fixed two-step momentum beyond `ℓ² = 3/2`.
- **T4: it ends at `ℓ = √2`.** The band-top curvature is `−1/(2 − ℓ²)`, so no twice-differentiable member reaches `ℓ² = 2`. There the band top keeps zero slope but its curvature is infinite, `1 − F ≈ ½(3|k − π/2|/2)^{4/3}`. Beyond it, characteristics with different slopes cross.
- **T5: it has infinite reach.** At every `ℓ ≠ 1`, `F` is not a trigonometric polynomial. Its hops decay exponentially for `0 < ℓ² < 2`.
- **T6: the books normalise the strain variable.** On a single wave the energy current is `E v_a = F_a ∂F_a`. Supplying block 181 T1's identification at every stretch, that the energy current equals the momentum per unit strain, gives `γ ≡ 1`. Then the coupling's strain variable is `b = (1 − ℓ²)/2`, and the long-wave metric `ℓ² = 1 − 2b` is exactly linear in it; block 69 T4's leading form `(1 + b)²` agrees only to first order. Since `γ` only reparametrises the family, this fixes a normalisation, not the walks.
- **T7: every per-axis walk keeps its own books on pairs of waves.** Block 181's pair-level construction (pushed), built from divided differences of the hops, works for every walk `Σ_a F_a(k_a)X_a + μΓ` whose square is a number. The per-axis hops `F_a` are any real functions. So every per-axis completion, this family included, keeps its own exact books on pairs of waves, with `P^s = F∂F` on single waves. This family's stretch generator equals `P^s` on single waves; placing it as `P^s` on pairs of waves is open.
- **T8: every wave slows as a relativistic free particle does.** With the sites held physical (fixed label momentum, as on a closed lattice), `d log E/d log ℓ = −ℓ²|v|² = −|u|²` exactly, where `u = ℓv` is the velocity measured in lengths. So a uniform stretch presses with `Σ E|u|²/(3V)`, strictly between `0` and `ρ/3` for moving positive-energy content. Block 180's first-order result is the `ℓ = 1` case.

In plain terms: suppose the walker is to keep exact, untwisted books however much the lattice is stretched, with each extra stretch just a relabelling. Then there is exactly one way the walk can respond to the stretch. That way is smooth, and it never lets a short wave outrun the long waves, which the short-range choice does beyond 7/6. But it needs hops of every length, falling off fast, and it cannot be continued smoothly past a stretch of √2. There the top of the band becomes infinitely sharply curved. The same books also say what the walk is coupled to: the square of the stretch, exactly.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main. Block 139 is used as landed. Blocks 179, 181 and 182 are pushed and placed; the facts used from them are re-derived (runner B1, B3, B4, C2, D3, I1–I3).

- **The coupling** (block 69).
  - Uniform form, quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`".
  - Its boundary, quoted: "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
  - Its momentum, quoted: "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)".
  - At isotropic `B = b·1` each axis has `F = sin k + b sin k cos² k + O(b²)`.
- **The stretched walk.** `H = Σ_a σ_a F(k_a, b)`, the same `F` on each axis, odd in `k`. Its positive branch has `E = (Σ_a F_a²)^{1/2}` and velocity `v_a = F_a ∂F_a/E`, where `F_a = F(k_a, b)`.
- **Covariance** (block 182's principle, supplied). `∂_bF = p(k, b) ∂_kF`, with `p(k, 0) = sin k cos k`, the symbol of block 69's two-step momentum.
- **Books at finite stretch** (block 182 T6's reading, supplied). The momentum that generates further stretch, `P_j = p(k_j, b)` per axis, has a current that is symmetric on single waves. By the single-wave lemma (block 179 T1, re-derived as runner B1), a conserved density's current on a single wave is `v ⊗ P`. So the books need `P ∥ v`. This is a necessary condition; T7 supplies the pair-level construction.
- **Block 181's objects** (pushed; re-derived in general as runner I1). For pair symbols with `q = k − k′` and `w_a = 1 − e^{−iq_a}`, the divided difference along axis `a` is `D_a[G] = (G(k_a) − G(k′_a))/w_a`. Block 181 uses `Â_a = ¼(e^{ik_a} + e^{−ik′_a})σ_a`, `f_a = ½(1 + e^{iq_a}) sin(k_a + k′_a)`, `P̂^s_j = ½(½f_j + h′Â_j + Â_jh)` and `K̂^s_{aj} = ½(Â_af_j + Â_jf_a)`, with `ê = ½(h + h′)`.
- **Block 139** (landed), quoted: "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`, and each wave's energy current is its two-step momentum at every `k`, massive or not." 
- **The length.** `ℓ` is fixed by the long-wave speed, `∂_kF(0) = 1/ℓ`, as in blocks 176 and 182.
- **Admissible** means block 176's speed limit: no wave faster than `1/ℓ` per label.
- **Notation.** `s = sin k`, `c = cos k`, `s₀ = sin k₀`, `c₀ = cos k₀`, `R = (s₀² + ℓ²c₀²)^{1/2}`.

In the literature, `∂_τu = (∂_ku)²/2` is a first-order equation of the Hamilton–Jacobi type, solved along characteristics (Hopf's method); its slope obeys the inviscid equation named after Burgers. The relation `M = E − e sin E` between `M = 2k` and `E = 2k₀`, with `e = 1 − ℓ²`, is Kepler's equation, and `u_k = sin E` has its classical series in Bessel functions `J_n(ne)`. This note uses none of it as authority.

## Domain qualifications

- Uniform isotropic stretch, per axis, in three dimensions (T1 needs at least two axes). Anisotropic stretches are treated only in T6(c), under its stated assumption.
- T1 uses the single-wave condition, which is necessary. T7 gives each walk's own books on pairs of waves; it does not place the stretch generator on pairs.
- `ℓ > 0`. At `ℓ → 0` the fold moves to the species points (runner D2), and that end is not treated.

## Theorem T1 — the books fix the rule

*Statement.* Under covariance, `P ∥ v` holds on every single wave at every stretch iff `p = γ(b) F ∂_kF` for a function `γ` with `γ(0) = 1`. Then `u = F²` obeys `∂_τu = (∂_ku)²/2`, with `τ = ∫₀^b γ`. So the stretched walks form one family up to reparametrisation. The fixed-generator flow (`p = s c`) has `p/(F∂_kF) = (ℓ²c² + s²)²/ℓ²`, and the linear completion's ratio depends on the axis (block 182 T6). Both fail at every `ℓ ≠ 1`.

*Proof.*
- `(v ⊗ P)_{aj} − (v ⊗ P)_{ja} = (F∂F(k_a) p(k_j) − F∂F(k_j) p(k_a))/E`.
- The momenta `k_a` and `k_j` are independent. Fix `y₀` with `F∂F(y₀) ≠ 0`. Then `p(y) = (p(y₀)/F∂F(y₀)) F∂F(y)` for every `y`, which is `γ(b)F∂_kF`. The converse is immediate (runner B2).
- At `b = 0`, `F∂_kF = s c = p(k, 0)`, so `γ(0) = 1`.
- `∂_bF = γF(∂_kF)²` and `u = F²` give `∂_bu = γ(∂_ku)²/2` (runner B2).
- The two failing ratios are runner B3. ∎

## Theorem T2 — the family in closed form

*Statement.* The solution from `u = sin² k` is, along characteristics,

`k = k₀ − τ sin 2k₀`,  `u = sin² k₀ − τ sin² 2k₀/2`,  `∂_ku = sin 2k₀`.

At fixed `k`, `F = s + τ s c² + τ² s(3 − 10s² + 7s⁴)/2 + O(τ³)`. The long-wave speed is `(1 − 2τ)^{−1/2}`, so `τ = (1 − ℓ²)/2`, and

`k = k₀ + ((ℓ² − 1)/2) sin 2k₀`,  `F = s₀R`,  `∂_kF = c₀/R`.

The shift `k₀ → k₀ + π` gives `k → k + π` and `F → −F`, so the species corners are kept, with speed `−1/ℓ` at `k = π`.

*Proof.*
- On `dk/dτ = −∂_ku`, the slope `∂_ku` is constant and `du/dτ = −(∂_ku)²/2`. Integrating gives the display.
- Runner C1 checks `∂_ku = sin 2k₀` and `∂_τu = (∂_ku)²/2` exactly.
- Runner C2 inverts to second order at fixed `k`.
- `∂_kF = ∂_ku/(2F) = c₀/(1 − 2τc₀²)^{1/2}`, and `1 − 2τc₀² = R²` at `τ = (1 − ℓ²)/2` (runner C3).
- Runner C4 checks the corners. ∎

## Theorem T3 — it never outruns the long waves

*Statement.* For `0 < ℓ² < 2`:
- (a) `dk/dk₀ = 1 + (ℓ² − 1) cos 2k₀ ≥ min(ℓ², 2 − ℓ²) > 0`. So `k₀ ↦ k` is a real-analytic diffeomorphism of the zone, and `F = sin ψ(k)` with `ψ` monotone: a relabelling of the free walk, covariant at every stretch.
- (b) Per axis, `1 − ℓ²(∂_kF)² = s₀²/R² ≥ 0`, zero only at `s₀ = 0`.
- (c) In three dimensions, `1 − ℓ²|v|² = Σ_j F_j²(1 − ℓ²(∂F_j)²)/Σ_j F_j² > 0` for every wave with `E ≠ 0`. At the species points `E = 0` and `v` is not defined; the bound is approached there, not attained.
- (d) For comparison, near `k = 0` the linear completion outruns `1/ℓ` iff `ℓ > 7/6`, re-derived here; the global statement is blocks 173 and 176's. The fixed-generator flow outruns it somewhere iff `ℓ² > 3/2`, checked globally here (block 182 T4(a)).

*Proof.*
- (a) The extremes of `cos 2k₀`. The inverse function theorem applies because `dk/dk₀ > 0`. Then `u = sin²k₀ − τ sin² 2k₀/2` is analytic in `k`, and so is `F = s₀R`, since `R > 0`. On `|k₀| ≤ π/2`, `∂_kF = c₀/R ≥ 0` and `F(±π/2) = ±1`. `ψ = arcsin F` is analytic at `F = ±1` as well: `k₀ → π − k₀` gives `k → π − k` and `F → F`, so `F` is even about `π/2`, and `∂_k²F(π/2) = −1/(2 − ℓ²) ≠ 0` (T4). Runner D2.
- (b) and (c): runner D1. In (c), each weight `F_j²` is nonnegative, and `F_j = 0` only where `s₀ = 0`.
- (d) Runner D3. For the fixed-generator flow, with `y = ℓ²` and `x = sin² k`, the excess `y³(1 − x) − (y − (y − 1)x)³` vanishes at `x = 0`, has slope `y²(2y − 3)` there and is concave on `[0, 1]`. So it stays nonpositive iff `y ≤ 3/2`. For this family, `ℓ²(∂_kF)² = ℓ²/(ℓ² + tan² k₀)`. ∎

So this family passes block 176's speed limit whether it is read as a relabelling or, with the sites held physical, as a hopping law. Block 182 T5 shows the two readings differ for the linear completion.

## Theorem T4 — it ends at a stretch of √2

*Statement.*
- (a) The band-top curvature is `∂_k²F(π/2) = −1/(2 − ℓ²)`. It is unbounded as `ℓ² → 2`, so no family continuous in `ℓ` and twice differentiable in `k` reaches `ℓ² = 2`, and none continues beyond it.
- (b) At `ℓ² = 2`, with `k₀ = π/2 + δ`, `k − π/2 = δ − ½ sin 2δ = (2/3)δ³ + O(δ⁵)` and `1 − F = δ⁴/2 + O(δ⁶)`. So `1 − F = ½(3|k − π/2|/2)^{4/3}` to leading order. The band top keeps zero slope, `∂_kF → 0`, but its curvature is infinite, `∂_k²F ∝ −|k − π/2|^{−2/3}`.
- (c) For `ℓ² > 2`, `g(δ) = δ − ((ℓ² − 1)/2) sin 2δ` has `g′(0) = 2 − ℓ² < 0` and `g(π/2) = π/2 > 0`. So there is `δ* ∈ (0, π/2)` with `g(±δ*) = 0`. The characteristics from `δ = 0, ±δ*` all reach `k = π/2`, with slopes `∂_ku = 0` and `∓ sin 2δ* ≠ 0`.

*Proof.*
- (a) `∂_kF = c₀/R` differentiated at `k₀ = π/2`, where `R = 1`, `∂_{k₀}R = 0` and `dk/dk₀ = 2 − ℓ²` (runner E1).
- Solutions of `∂_τu = (∂_ku)²/2` that are twice differentiable, with this initial condition, are the characteristic solution while it is defined: the slope is constant along characteristics, and the construction is reversible in `τ`. So a family continuous in `τ` and twice differentiable in `k`, on an interval containing `τ = −1/2`, would have `∂_k²u` continuous there, and bounded near the band top. It does not.
- (b) Series (runner E2). At `ℓ² = 2`, `u = s₀²(1 + c₀²) = 1 − c₀⁴`.
- (c) The intermediate value theorem. At `ℓ² = 3`, `g(π/4) = π/4 − 1 < 0`, so `δ* ∈ (π/4, π/2)` (runner E3). ∎

## Theorem T5 — it has infinite reach

*Statement.* At every `ℓ ≠ 1` with `0 < ℓ² < 2`, `F` is not a trigonometric polynomial: the stretched walk has hops of every length. Since `F` is analytic on the real line, the hops decay exponentially.

*Proof.*
- Along characteristics, `∂_k²u = 2 cos 2k₀/(1 + (ℓ² − 1) cos 2k₀)` (runner F1).
- Suppose `F` had finite reach. Then `u = F²` is a trigonometric polynomial, so `∂_k²u` is entire. So is `∂_k²u(k(k₀))`, since `k(k₀)` is entire.
- It equals the right-hand side on the real line, so by the identity theorem the right-hand side would be entire.
- But at `cos 2k₀ = −1/(ℓ² − 1)`, which has complex solutions `k₀`, the denominator vanishes and the numerator is `−2/(ℓ² − 1) ≠ 0`. That is a pole, a contradiction.
- Runner F2 checks two exact instances: `ℓ² = 3/2`, where `k₀ = π/2 + i arccosh(2)/2`, and `ℓ² = 1/2`, where `k₀ = i arccosh(2)/2`. At `ℓ = 1` the expression is `2 cos 2k₀`, which is entire.
- The exponential decay is the standard property of the hop amplitudes (the coefficients of the trigonometric series) of a function analytic on a strip. ∎

## Theorem T6 — the books normalise the strain variable

*Statement.*
- (a) On a single wave of either branch, the energy current is `E v_a = ½ ∂_a E² = F_a ∂F_a`. So the first books identity, energy current equal to the momentum `P_a = γ F_a ∂F_a` (block 181 T1 at `ℓ = 1`, pushed, supplied here at every stretch), holds at every stretch iff `γ ≡ 1`. Since `γ` only reparametrises the family (T1), this fixes the normalisation of the strain variable, not the walks.
- (b) Then `b = τ = (1 − ℓ²)/2`. The long-wave metric is `ℓ² = 1 − 2b` exactly, and `∂F/∂(ℓ²) = −½ F(∂_kF)²` at fixed `k`. Block 69 T4's leading inverse metric `(1 + b)²` agrees with `1/(1 − 2b)` to first order; the two differ by `3b²`.
- (c) For an anisotropic diagonal stretch in which each axis responds to its own `b_j`, with each axis's generator of the form `γ(b_j)F∂F` (assumed), `P ∥ v` needs `γ(b₁) = γ(b₂) = γ(b₃)` for independent `b_j`, so `γ` is a constant, `1` by block 69's first order. The strain variable is then fixed by the books alone.

*Proof.*
- (a) The single-wave lemma applied to the energy density. The rest is the equation `γ F∂F = F∂F`.
- (b) T2's `τ = (1 − ℓ²)/2`. Implicit differentiation of the closed form at fixed `k`, with `sin k₀` and `cos k₀` as symbols.
- (c) `(v ⊗ P)_{12} − (v ⊗ P)_{21} = F∂F(k₁) F∂F(k₂) (γ(b₂) − γ(b₁))/E`.
- Runner B4 checks all of these. ∎

So under the books, the walk's coupling to a uniform stretch is exactly linear in the square of the stretch: at every stretch, the momentum per unit `ℓ²` is `−½` times the stretched walk's own two-step momentum.

## Theorem T7 — every per-axis walk keeps its own books on pairs of waves

*Statement.* Take any walk whose plane-wave block is `h(k) = Σ_a F_a(k_a)X_a + μΓ`, where `X_a` and `Γ` are mutually anticommuting hermitian involutions and the per-axis hops `F_a` are any real functions (real hops make `P̂^s` and `K̂^s` hermitian pair symbols). Set `Â_a = (i/2) D_a[F_a] X_a`, `f_a = i D_a[F_a²]`, and build `ê`, `P̂^s` and `K̂^s` as block 181 does.
- (a) Exactly, `Σ_j w_j P̂^s_j = i(êh − h′ê)` and `Σ_a w_a K̂^s_{aj} = i(P̂^s_jh − h′P̂^s_j)`, with `K̂^s` symmetric. So `ë = ∇̄∇̄:K^s` for every state.
- (b) On single waves `P^s_j(k, k) = F_j∂F_j`, the energy current `E v_j`, and `K^s_{aj}(k, k) = ∂F_a∂F_j(F_jX_a + F_aX_j)/2`, whose expectation on a wave is `E v_a v_j`.
- (c) For the free walk, `D[sin]` and `D[sin²]` are block 181's objects. A constant offset in `h` breaks the construction, as block 139 T3 found for its own convention.
- (d) So every per-axis completion, this note's family included, keeps its own exact symmetric books on pairs of waves at every stretch. What distinguishes this family (T1, T6) is that its stretch generator equals `P^s` on single waves. For the linear completion and the fixed-generator flow the stretch generator is not `P^s` (runner B3). Placing this family's stretch generator as `P^s` on pairs of waves is not done here.

*Proof.*
- (a) `h − h′ = Σ_a w_a D_a[F_a]X_a` and `h² − h′² = Σ_a w_a D_a[F_a²]`, since `h²` is a number.
- Then `Σ_j w_jP̂^s_j = ½(½(h² − h′²) + h′(h − h′)/2 + (h − h′)h/2)·i = (i/2)(h² − h′²)`, and `i(êh − h′ê)` is the same.
- For the stress, `P̂^s_jh − h′P̂^s_j = ½[½f_j(h − h′) + (h² − h′²)Â_j]`. With `f = 2·(i/2)·D[F²]`, this is `(1/(2i)) Σ_a w_a (Â_af_j + f_aÂ_j)`. That is symmetric in `(a, j)` because the coefficients of `Â` and `f` differ by exactly the factor two chosen.
- Runner I1 checks (a) symbolically with `4 × 4` involutions, for arbitrary values of the hops on both waves of the pair, and checks that an offset breaks it.
- (b) As `k′ → k`, `D[G] → −i∂G`; with `{h, X_j} = 2F_j`, runner I2.
- (c) Runner I3.
- (d) follows from (a), (b), T1 and T6. ∎

For finite-reach hops the divided differences are trigonometric polynomials in `k` and `k′`, so the densities have finite reach. For this family's hops (T5), they have infinite reach with exponentially decaying terms.

## Theorem T8 — every wave slows as a relativistic free particle does

*Statement.* At fixed label momentum `k`, `d log E/d log ℓ = −ℓ²|v|²` for every wave of the family, with `|v|² = Σ_a F_a²(∂F_a)²/E²`. In terms of the velocity measured in lengths, `u = ℓv`, this is `−|u|²`, with `|u| ≤ 1` by T3. So the pressure of content in a volume `V = ℓ³N`, `p = −∂E/∂V`, is `Σ E|u|²/(3V)`. Each moving positive-energy wave presses strictly between `0` and `E/(3V)`. At `ℓ = 1`, `|v|² = 1 − Σ s⁴/E²`, which is block 180's first-order result.

*Proof.* T6 gives `∂F/∂(ℓ²) = −½F(∂_kF)²` at fixed `k`. So `∂E/∂(ℓ²) = Σ_a F_a ∂F_a/∂(ℓ²)/E = −½E|v|²`, and `d log E/d log ℓ = 2ℓ² ∂E/∂(ℓ²)/E` (runner B5). ∎

For a relativistic free particle, `E² = μ² + |p|²/ℓ²` with its momentum per label `p` fixed, the same law holds with `|u|` its velocity. Here it holds at every stretch for every wave of the walk.

## What this settles and what it does not

- **Settled.**
  - Covariance with symmetric books at every stretch fixes the stretch rule uniquely (T1).
  - That rule is admissible up to `ℓ = √2`, farther than the other two named completions (T3).
  - It stops there (T4), and it is not of finite reach at any finite stretch (T5).
  - The books also fix the coupling's strain variable as `(1 − ℓ²)/2`, making the long-wave metric exactly linear in it (T6).
  - Every wave slows under the stretch as a relativistic free particle does, so content presses with its kinetic pressure at every stretch (T8).
  - Every per-axis walk whose square is a number keeps its own exact books on pairs of waves (T7). So for the other completions, the "twist" of block 182 T6 is exactly that their stretch generator is not the energy current's momentum `P^s`.
- **For the third column** (the coupling axis). Block 182's trilemma now has a worked cost on each side:
  - reach three with covariance: the linear completion. It twists at every `ℓ ≠ 1`, and as a hopping law it outruns the long waves beyond `7/6`.
  - covariance with symmetric books: this family. It is admissible, but has infinite reach at every `ℓ ≠ 1` and ends at `√2`.
  - reach three with symmetric books: a hopping law without covariance.
  - A closed lattice that keeps stretching uniformly, as in blocks 148 and 180, would pass `ℓ = √2` relative to the free walk. With this rule it has no smooth walk there.
- **Not settled.**
  - Anisotropic stretches.
  - Whether the stretch generator can be placed as `P^s` on pairs of waves; T6 matches them on single waves.
  - Whether a principle should restart the rule at each stretch. This family is not self-similar: `dτ/d log ℓ = −ℓ²`, and the free walk is its preferred member.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 69 N1 as landed: the leading order does not determine a nonlinear completion; block 182 (pushed): whether any covariant completion outside reach three is admissible at every stretch"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; anisotropic stretches; a pair-symbol symmetric current at finite stretch for this family"
conditional_surface_status: "exact within block 69, under block 182's covariance principle and its single-wave reading of books at finite stretch"
hypothetical_axiom_status: "the coupling, its completion, covariance and the books at finite stretch are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling, and that the leading order does not fix a completion.
  - Blocks 173 and 176 (pushed): the linear completion's threshold `7/6`, and the speed limit.
  - Block 179 (pushed): the single-wave lemma.
  - Block 182 (pushed): the covariance principle, the trilemma, the self-consistent flow and its second-order term, and the fixed-generator flow's threshold `ℓ² = 3/2`.
- **In the literature.**
  - First-order equations of the Hamilton–Jacobi type solved along characteristics (Hopf); the inviscid equation named after Burgers.
  - Kepler's equation `M = E − e sin E`, with its series in Bessel functions `J_n(ne)`. Here `e = 1 − ℓ²`, and `|e| < 1` is exactly `0 < ℓ² < 2`.
  - The inverse function theorem; the identity theorem for analytic functions; exponential decay of Fourier coefficients for functions analytic on a strip (Paley–Wiener type).
  - None is used as authority.
- **New here.**
  - Uniqueness: the books at every stretch force the self-consistent flow (T1).
  - Its closed form in the length (T2).
  - Its speed limit at every stretch below `√2` (T3).
  - Its end at `√2` (T4), and its infinite reach (T5).
  - The strain variable (T6).
  - The law of slowing at every stretch (T8). At first order it is block 180's.
  - Block 181's pair-level books for every per-axis walk whose square is a number (T7). Block 139 had the mechanism (the square is a number) for the free walk with its staggered mass.
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: whether a covariant completion outside reach three is admissible at every stretch, for the completion that keeps the books. The obligations are:
- (O1) the premises (A3);
- (O2) the single-wave lemma and the books condition (B1, B2), with the failing witnesses (B3);
- (O3) the solution and its length (C1–C4);
- (O4) the speed limit and the relabelling (D1–D3);
- (O5) the end at `√2` (E1–E3);
- (O6) the reach (F1, F2);
- (O7) the strain variable (B4);
- (O8) the pair-level books for every per-axis walk (I1–I3);
- (O9) the law of slowing and the pressure (B5).

## No-Go Discipline Gate

The note's negative sentences:
- no covariant completion other than this family keeps symmetric books at every stretch;
- no twice-differentiable member of this family reaches `ℓ = √2`;
- no member at `ℓ ≠ 1` has finite reach;
- no strain variable other than `b = (1 − ℓ²)/2` keeps the energy current equal to the momentum on single waves at every stretch;
- with a constant offset, block 181's construction does not give the books (T7(c)).

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different normalisation of the generator.* `γ(b)` only reparametrises the family, and `ℓ` is fixed by the long-wave speed, so the walk at each `ℓ` is unique. ATTEMPTED; closed.
2. *Different generators on different axes.* Isotropy of the stretch gives the same `F` and `p` on each axis, and T1's argument is per pair of axes. Anisotropic stretches are not examined.
3. *Weaker smoothness.* Past `ℓ² = 2`, kinked solutions of viscosity type exist. They are not twice differentiable, their hops decay only algebraically, and selecting one needs an entropy-type principle that covariance does not supply. Not examined further.
4. *Books with a different momentum.* The books are read on the momentum that generates further stretch (block 182 T6). Another reading would need another coupling. Not examined.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: isotropy, covariance, the single-wave reading of the books and the long-wave length.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling's first order and momentum; no completion fixed | yes (quoted, A3) |
| block 179 (pushed) | the single-wave lemma | re-derived (B1) |
| block 180 (pushed) | the first-order slowing `1 − Σs⁴/E²` | re-derived as the `ℓ = 1` case (B5) |
| block 181 (pushed) | the energy current equals the momentum at `ℓ = 1`; the pair-level objects | used as the reading at finite stretch (T6); re-derived in general (I1–I3) |
| block 139 (landed) | the mechanism: the square is a number; an offset breaks it | quoted; checked (I1) |
| block 182 (pushed) | covariance, the books reading, the other two completions | re-derived (B3, C2, D3) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the books at every stretch fix the self-consistent flow and normalise the strain variable; every per-axis walk keeps its own books on pairs of waves; admissible below `√2`, infinite reach, no smooth continuation to `√2`" | executed: the lemma, the books condition, the failing witnesses, the energy current and the strain variable | executed: the characteristic solution and its second order | executed: the speed bounds, the fold-free range, the thresholds; the pair-level books for arbitrary hops (symbolic) | executed: the band-top curvature, the infinite curvature at `√2`, the crossing; the pole at two stretches | proved, not executed: the pole at every `ℓ ≠ 1`; exponential decay |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The single-wave condition is only necessary. The books might fail on pairs of waves even for this family."
  - *Reply:* T1's uniqueness uses only the necessary condition, so it stands. T7 gives every per-axis walk, this family included, its own books on pairs of waves. Placing the stretch generator as `P^s` on pairs remains open, as stated.
- *Objection:* "Infinite reach with exponential decay is local enough."
  - *Reply:* It may be. The note records the cost; it does not rank it.

### N8 — Cross-cycle echo
- Block 69: no completion fixed.
- Block 176: admissible iff `q ≥ −1/6` within reach three.
- Block 182: covariance within reach three forces the linear completion, and the trilemma.
- This note: covariance with the books forces one completion outside reach three, admissible up to `√2`.

## Falsifiers

- A covariant stretch family, other than a reparametrisation of this one, keeping `P ∥ v` at every stretch.
- A twice-differentiable member at `ℓ² = 2`.
- A finite-reach member at some `ℓ ≠ 1`.
- A strain variable other than `(1 − ℓ²)/2` with energy current equal to momentum at every stretch.
- A walk `Σ_a F_a X_a + μΓ` with anticommuting involutions for which T7(a) fails.

## Boundaries and non-claims

- Uniform isotropic stretch; single-wave books; covariance supplied.
- The coupling, its completion, covariance and the reading of the books are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), quoted. Blocks 173, 176, 179 and 182 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - integration along characteristics of a first-order equation (Hopf's method), and uniqueness of twice-differentiable solutions of the Cauchy problem while characteristics do not cross;
  - the inverse function theorem and the intermediate value theorem;
  - the identity theorem for analytic functions;
  - exponential decay of Fourier coefficients of functions analytic on a strip (Paley–Wiener type);
  - divided differences and Clifford algebra (anticommuting involutions);
  - Kepler's equation and its Bessel series, named only;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.**
  - Origin was re-fetched. Block 69 was read as landed, and blocks 179 and 182 on their branches.
  - The landed notes and the probes branch were grepped for "Kepler", "self-consistent flow" and "covariant completion". The probes' attempts on the reach-three coupling (bond-by-bond completions `f(B)`) and on the sea under a slow stretch are different objects. Block 182 introduced the flow and its second-order term; the rest is new here.
- **Mutation census.** One mutation per science family (A–F and I), each failing only in its own family, and two in family G.
- **Second version.** T7 was added the same evening: block 181's construction was found to use only that the walk's square is a number.
- **Third version.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. It asked for scope corrections, which are applied:
  - T7 is each walk's own books, not pair-level sufficiency for the stretch generator;
  - T6 fixes a normalisation, and its anisotropic part carries an assumption;
  - T4 needs continuity in `ℓ`;
  - the band top at `√2` is infinitely curved with zero slope, not a corner;
  - the speed bound is approached, not attained;
  - the fixed-generator threshold is checked globally;
  - the free particle is relativistic.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_2026_09_27.py
```

Expected: `TOTAL: PASS=28 FAIL=0`.
