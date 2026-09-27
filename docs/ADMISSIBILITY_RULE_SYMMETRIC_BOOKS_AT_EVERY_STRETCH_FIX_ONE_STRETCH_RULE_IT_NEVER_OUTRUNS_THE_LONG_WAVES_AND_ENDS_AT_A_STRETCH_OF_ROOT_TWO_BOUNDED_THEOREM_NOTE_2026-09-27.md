---
claim_id: admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_it_never_outruns_the_long_waves_and_ends_at_a_stretch_of_root_two_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, for a uniform isotropic stretch of a per-axis walk F(k, b) with F(k, 0) = sin k and first-order term sin k cos^2 k, under the covariance principle of block 182 (pushed; each further stretch acts on the stretched walk as a relabelling, dF/db = p dF/dk), and reading symmetric books at finite stretch as block 182 T6 does (on single waves the momentum p that generates further stretch is parallel to the stretched walk's velocity; block 179 T1, pushed, re-derived): (T1) the books hold at every stretch iff p = gamma(b) F dF/dk, so u = F^2 obeys u_tau = (du/dk)^2/2, one family of walks up to reparametrisation (block 182's self-consistent flow); (T2) with the stretch l fixed by the long-wave speed dF/dk(0) = 1/l, the family is k = k0 + ((l^2 - 1)/2) sin 2k0, F = sin k0 sqrt(sin^2 k0 + l^2 cos^2 k0), and keeps the species corners; (T3) for 0 < l^2 < 2 it is a real-analytic relabelling of the free walk, and no wave is faster than 1/l per label, strictly except at the species points; (T4) no twice-differentiable member reaches l^2 = 2, where the band top becomes a cusp of order 4/3; (T5) at every l != 1 it has infinite reach, since u_kk along characteristics has a pole off the real line; (T6) the energy current on a single wave equals the momentum per unit strain at every stretch iff gamma = 1, so the strain variable is b = (1 - l^2)/2 and the long-wave metric l^2 = 1 - 2b is exactly linear in it (block 69 T4's leading form (1 + b)^2 agrees only to first order); for anisotropic diagonal stretches P parallel to v alone forces this. So covariance with symmetric books fixes the stretch rule and the strain variable; it passes the speed limit up to sqrt 2 and is not of finite reach. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
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
- **T3: it never outruns the long waves.** For `0 < ℓ² < 2` it is a real-analytic relabelling of the free walk. Every wave's speed is at most `1/ℓ` per label, per axis and in three dimensions, with equality only at the species points. The linear completion fails this beyond `ℓ = 7/6`, and the flow of the fixed two-step momentum beyond `ℓ² = 3/2`.
- **T4: it ends at `ℓ = √2`.** The band-top curvature is `−1/(2 − ℓ²)`, so no twice-differentiable member reaches `ℓ² = 2`. There the band top is a cusp, `1 − F ≈ ½(3|k − π/2|/2)^{4/3}`. Beyond it, characteristics with different slopes cross.
- **T5: it has infinite reach.** At every `ℓ ≠ 1`, `F` is not a trigonometric polynomial. Its hops decay exponentially for `0 < ℓ² < 2`.
- **T6: the books also fix the strain variable.** On a single wave the energy current is `E v_a = F_a ∂F_a`. It equals the momentum per unit strain at every stretch iff `γ ≡ 1`. Then the coupling's strain variable is `b = (1 − ℓ²)/2`, and the long-wave metric `ℓ² = 1 − 2b` is exactly linear in it; block 69 T4's leading form `(1 + b)²` agrees only to first order. For anisotropic diagonal stretches, `P ∥ v` alone already forces this.

In plain terms: suppose the walker is to keep exact, untwisted books however much the lattice is stretched, with each extra stretch just a relabelling. Then there is exactly one way the walk can respond to the stretch. That way is smooth, and it never lets a short wave outrun the long waves, which the short-range choice does beyond 7/6. But it needs hops of every length, falling off fast, and it cannot be continued smoothly past a stretch of √2. There the top of the band pinches into a point. The same books also say what the walk is coupled to: the square of the stretch, exactly.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main. Blocks 179, 181 and 182 are pushed and placed; the facts used from them are re-derived (runner B1, B3, B4, C2, D3).

- **The coupling** (block 69).
  - Uniform form, quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`".
  - Its boundary, quoted: "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
  - Its momentum, quoted: "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)".
  - At isotropic `B = b·1` each axis has `F = sin k + b sin k cos² k + O(b²)`.
- **The stretched walk.** `H = Σ_a σ_a F(k_a, b)`, the same `F` on each axis, odd in `k`. Its positive branch has `E = (Σ_a F_a²)^{1/2}` and velocity `v_a = F_a ∂F_a/E`, where `F_a = F(k_a, b)`.
- **Covariance** (block 182's principle, supplied). `∂_bF = p(k, b) ∂_kF`, with `p(k, 0) = sin k cos k`, the symbol of block 69's two-step momentum.
- **Books at finite stretch** (block 182 T6's reading, supplied). The momentum that generates further stretch, `P_j = p(k_j, b)` per axis, has a current that is symmetric on single waves. By the single-wave lemma (block 179 T1, re-derived as runner B1), a conserved density's current on a single wave is `v ⊗ P`. So the books need `P ∥ v`. This is a necessary condition. A full symmetric current on pairs of waves at finite stretch, as block 181 (pushed) built at `ℓ = 1`, is not constructed here.
- **The length.** `ℓ` is fixed by the long-wave speed, `∂_kF(0) = 1/ℓ`, as in blocks 176 and 182.
- **Admissible** means block 176's speed limit: no wave faster than `1/ℓ` per label.
- **Notation.** `s = sin k`, `c = cos k`, `s₀ = sin k₀`, `c₀ = cos k₀`, `R = (s₀² + ℓ²c₀²)^{1/2}`.

In the literature, `∂_τu = (∂_ku)²/2` is a first-order equation of the Hamilton–Jacobi type, solved along characteristics (Hopf's method); its slope obeys the inviscid equation named after Burgers. The relation `M = E − e sin E` between `M = 2k` and `E = 2k₀`, with `e = 1 − ℓ²`, is Kepler's equation, and `u_k = sin E` has its classical series in Bessel functions `J_n(ne)`. This note uses none of it as authority.

## Domain qualifications

- Uniform isotropic stretch, per axis. Anisotropic stretches are not treated.
- Books are tested on single waves only (a necessary condition).
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
- (b) Per axis, `1 − ℓ²(∂_kF)² = s₀²/R² ≥ 0`, with equality only at `s₀ = 0`.
- (c) In three dimensions, `1 − ℓ²|v|² = Σ_j F_j²(1 − ℓ²(∂F_j)²)/Σ_j F_j² ≥ 0`, with equality only at `E = 0`.
- (d) For comparison, near `k = 0` the linear completion outruns `1/ℓ` iff `ℓ > 7/6` (blocks 173, 176), and the fixed-generator flow iff `ℓ² > 3/2` (block 182 T4(a)).

*Proof.*
- (a) The extremes of `cos 2k₀`. The inverse function theorem applies because `dk/dk₀ > 0`. Then `u = sin²k₀ − τ sin² 2k₀/2` is analytic in `k`, and so is `F = s₀R`, since `R > 0`. On `|k₀| ≤ π/2`, `∂_kF = c₀/R ≥ 0` and `F(±π/2) = ±1`. Runner D2.
- (b) and (c): runner D1. In (c), each weight `F_j²` is nonnegative, and `F_j = 0` only where `s₀ = 0`.
- (d) Runner D3. For this family, `ℓ²(∂_kF)² = ℓ²/(ℓ² + tan² k₀)`. ∎

So this family passes block 176's speed limit whether it is read as a relabelling or, with the sites held physical, as a hopping law. Block 182 T5 shows the two readings differ for the linear completion.

## Theorem T4 — it ends at a stretch of √2

*Statement.*
- (a) The band-top curvature is `∂_k²F(π/2) = −1/(2 − ℓ²)`. It is unbounded as `ℓ² → 2`, so no twice-differentiable member of the family reaches `ℓ² = 2`, and none continues beyond it.
- (b) At `ℓ² = 2`, with `k₀ = π/2 + δ`, `k − π/2 = δ − ½ sin 2δ = (2/3)δ³ + O(δ⁵)` and `1 − F = δ⁴/2 + O(δ⁶)`. So `1 − F = ½(3|k − π/2|/2)^{4/3}` to leading order: a cusp of order `4/3` at the band top.
- (c) For `ℓ² > 2`, `g(δ) = δ − ((ℓ² − 1)/2) sin 2δ` has `g′(0) = 2 − ℓ² < 0` and `g(π/2) = π/2 > 0`. So there is `δ* ∈ (0, π/2)` with `g(±δ*) = 0`. The characteristics from `δ = 0, ±δ*` all reach `k = π/2`, with slopes `∂_ku = 0` and `∓ sin 2δ* ≠ 0`.

*Proof.*
- (a) `∂_kF = c₀/R` differentiated at `k₀ = π/2`, where `R = 1`, `∂_{k₀}R = 0` and `dk/dk₀ = 2 − ℓ²` (runner E1).
- Twice-differentiable solutions of `∂_τu = (∂_ku)²/2` with this initial condition are the characteristic solution while it is defined. So a twice-differentiable family on an interval of `τ` containing `τ = −1/2` would have bounded `∂_k²u` there. It does not.
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

## Theorem T6 — the books also fix the strain variable

*Statement.*
- (a) On a single wave of either branch, the energy current is `E v_a = ½ ∂_a E² = F_a ∂F_a`. So the first books identity, energy current equal to the momentum `P_a = γ F_a ∂F_a` (block 181 T1 at `ℓ = 1`, pushed), holds at every stretch iff `γ ≡ 1`.
- (b) Then `b = τ = (1 − ℓ²)/2`. The long-wave metric is `ℓ² = 1 − 2b` exactly, and `∂F/∂(ℓ²) = −½ F(∂_kF)²` at fixed `k`. Block 69 T4's leading inverse metric `(1 + b)²` agrees with `1/(1 − 2b)` to first order; the two differ by `3b²`.
- (c) For an anisotropic diagonal stretch in which each axis responds to its own `b_j`, `P ∥ v` needs `γ(b₁) = γ(b₂) = γ(b₃)` for independent `b_j`, so `γ` is a constant, `1` by block 69's first order. The strain variable is then fixed by the books alone.

*Proof.*
- (a) The single-wave lemma applied to the energy density. The rest is the equation `γ F∂F = F∂F`.
- (b) T2's `τ = (1 − ℓ²)/2`. Implicit differentiation of the closed form at fixed `k`, with `sin k₀` and `cos k₀` as symbols.
- (c) `(v ⊗ P)_{12} − (v ⊗ P)_{21} = F∂F(k₁) F∂F(k₂) (γ(b₂) − γ(b₁))/E`.
- Runner B4 checks all of these. ∎

So under the books, the walk's coupling to a uniform stretch is exactly linear in the square of the stretch: at every stretch, the momentum per unit `ℓ²` is `−½` times the stretched walk's own two-step momentum.

## What this settles and what it does not

- **Settled.**
  - Covariance with symmetric books at every stretch fixes the stretch rule uniquely (T1).
  - That rule is admissible up to `ℓ = √2`, farther than the other two named completions (T3).
  - It stops there (T4), and it is not of finite reach at any finite stretch (T5).
  - The books also fix the coupling's strain variable as `(1 − ℓ²)/2`, making the long-wave metric exactly linear in it (T6).
- **For the third column** (the coupling axis). Block 182's trilemma now has a worked cost on each side:
  - reach three with covariance: the linear completion. It twists at every `ℓ ≠ 1`, and as a hopping law it outruns the long waves beyond `7/6`.
  - covariance with symmetric books: this family. It is admissible, but has infinite reach at every `ℓ ≠ 1` and ends at `√2`.
  - reach three with symmetric books: a hopping law without covariance.
  - A closed lattice that keeps stretching uniformly, as in blocks 148 and 180, would pass `ℓ = √2` relative to the free walk. With this rule it has no smooth walk there.
- **Not settled.**
  - Anisotropic stretches.
  - A full symmetric current on pairs of waves at finite stretch.
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
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed.

## Exact target and obligation graph

Target: whether a covariant completion outside reach three is admissible at every stretch, for the completion that keeps the books. The obligations are:
- (O1) the premises (A3);
- (O2) the single-wave lemma and the books condition (B1, B2), with the failing witnesses (B3);
- (O3) the solution and its length (C1–C4);
- (O4) the speed limit and the relabelling (D1–D3);
- (O5) the end at `√2` (E1–E3);
- (O6) the reach (F1, F2);
- (O7) the strain variable (B4).

## No-Go Discipline Gate

The note's negative sentences:
- no covariant completion other than this family keeps symmetric books at every stretch;
- no twice-differentiable member of this family reaches `ℓ = √2`;
- no member at `ℓ ≠ 1` has finite reach;
- no strain variable other than `b = (1 − ℓ²)/2` keeps the energy current equal to the momentum on single waves at every stretch.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A different normalisation of the generator.* `γ(b)` only reparametrises the family, and `ℓ` is fixed by the long-wave speed, so the walk at each `ℓ` is unique. ATTEMPTED; closed.
2. *Different generators on different axes.* Isotropy of the stretch gives the same `F` and `p` on each axis, and T1's argument is per pair of axes. Anisotropic stretches are not examined.
3. *Weaker smoothness.* Past `ℓ² = 2`, solutions that are only continuous exist (kinked, of viscosity type). They are not trigonometric series with decaying hops, so they are not walks of the kind considered. Not examined further.
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
| block 181 (pushed) | the energy current equals the momentum at `ℓ = 1` | used as the reading at finite stretch (T6) |
| block 182 (pushed) | covariance, the books reading, the other two completions | re-derived (B3, C2, D3) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the books at every stretch fix the self-consistent flow and the strain variable; admissible below `√2`, infinite reach, no smooth continuation to `√2`" | executed: the lemma, the books condition, the failing witnesses, the energy current and the strain variable | executed: the characteristic solution and its second order | executed: the speed bounds, the fold-free range, the thresholds | executed: the band-top curvature, the cusp, the crossing; the pole at two stretches | proved, not executed: the pole at every `ℓ ≠ 1`; exponential decay |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The single-wave condition is only necessary. The books might fail on pairs of waves even for this family."
  - *Reply:* Granted, and stated. T1's uniqueness uses only the necessary condition, so it stands. The admissibility (T3), the end (T4) and the reach (T5) are properties of the walk, independent of the books.
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

## Boundaries and non-claims

- Uniform isotropic stretch; single-wave books; covariance supplied.
- The coupling, its completion, covariance and the reading of the books are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), quoted. Blocks 173, 176, 179 and 182 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - integration along characteristics of a first-order equation (Hopf's method);
  - the inverse function theorem and the intermediate value theorem;
  - the identity theorem for analytic functions;
  - exponential decay of Fourier coefficients of functions analytic on a strip (Paley–Wiener type);
  - Kepler's equation and its Bessel series, named only;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-27, during the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.**
  - Origin was re-fetched. Block 69 was read as landed, and blocks 179 and 182 on their branches.
  - The landed notes and the probes branch were grepped for "Kepler", "self-consistent flow" and "covariant completion". The probes' attempts on the reach-three coupling (bond-by-bond completions `f(B)`) and on the sea under a slow stretch are different objects. Block 182 introduced the flow and its second-order term; the rest is new here.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_2026_09_27.py
```

Expected: `TOTAL: PASS=24 FAIL=0`.
