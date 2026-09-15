---
claim_id: admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_not_lattice_green_function_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the real Gaussian instance of the nearest-neighbor formation law (each site draws w times the sum of its recorded predecessors plus independent noise of variance sigma^2; gain g = 3w) in the monotone class on the half-space x_1 + x_2 + x_3 >= 0 of Z^3, conditional on the level-0 records: (T1) the centered record at x is the sum over earlier sites z of G(x,z) xi_z with G(x,z) = w^n n!/(d_1! d_2! d_3!), d = x - z, n = |d|_1, the directed-path kernel, and the covariance is sigma^2 times the overlap of two such kernels; the boundary's mean propagates by the same kernel, a probability kernel exactly when g = 1 (proved); (T2) Var(v_x) = sigma^2 sum_{n < level} g^{2n} P_n with P_n the coincidence probability of two independent directed walks after n steps; for g < 1 the variance is at most sigma^2/(1 - g^2), the level laws have a limit, a unique bounded-variance stationary law exists on Z^3 and its covariance decays exponentially; for g = 1, 1/(36 n) <= P_n <= 9 pi/(16 n), so the variance grows like the harmonic number of the level and no bounded-variance stationary law exists; for g > 1 the variance grows exponentially (proved; executed to level 200 exactly); (T3) the stationary precision's symbol at g < 1 is 1 - 2w sum cos k_j + w^2 (3 + 2 sum_{i<j} cos(k_i - k_j)), the axial-plus-face-diagonal graph of block 09; at g = 1 its expansion is K^2/9 along the level direction and |k|^4/36 in the transverse plane (parabolic); the return probability of the simple random walk on Z^3 equals C(2n,n)/4^n times P_n, so the static massless Green function exists on Z^3 while the formation law's diagonal series diverges: the record two-point function of this formation law is never the lattice Green function (proved; executed); (T4) with one transverse dimension P_n = C(2n,n)/4^n and the variance grows like the square root of the level (proved; executed); (T5) covariance of the rule under value translations forces g = 1; the second-order expansion of log prod f(s . a_i) for a zonal rule on the sphere at an aligned configuration is -kappa sum |theta - theta_i|^2 with kappa = f'(1)/(2 f(1)), whose mean is the average (g = 1) with variance f(1)/(3 f'(1)) per component, equal to 2/3 for the Born overlap (1+t)/2; block 07's real instance is the massless static Laplacian and its formation rule has g = 1/2, while the massless formation rule is the one-site conditional of no static law (proved; executed symbolically). No ordered phase, no order, no rule and no coupling is selected as physical; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms  - admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_bounded_theorem_note_2026-09-07
runner: scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py
---

# The record two-point function of a causal Gaussian formation law is a heat kernel in level time, not the lattice Green function — massless exactly when the rule is value-covariant, with logarithmic growth and no stationary law

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

The derivation campaign asks whether any propagating kernel — the Coulomb-type
`1/r` Green function the gravity lane wants, or a transverse kernel — can be a
statistic of the finished record field under a formation law, with no tick
supplied. We answer it exactly for the simplest continuous instance of our
lane's formation law: each site's value is a Gaussian whose mean is a fixed
weight times the sum of its three already-recorded neighbours. Laying records
down level by level, a fluctuation at one site spreads to later sites the way
heat spreads: the two-point function is the overlap of two directed random
walks, a heat kernel in level time. Whether the field settles down depends on
one number, the gain (three times the weight). Below one, the record field
has a stationary law with correlations that die exponentially. At exactly
one — which is what covariance forces when no value is privileged — the
record field never settles: its variance grows like the logarithm of the level
and there is no stationary law at all. Above one it blows up. In none of these
cases is the two-point function the `1/r` Green function: the static reading
of the same rule averages over all six neighbours and its return walk is free
to go back and forth, which is exactly the extra decay that makes a Green
function exist in three dimensions; the formation reading walks one way only
and loses it. The block-07 instance turns out to be the massless static
Laplacian, and its formation rule has gain one half. Under the Born overlap,
the transverse fluctuations of an aligned region are this massless law with
variance two thirds.

Exactly: `G(x,z) = w^n n!/(d_1! d_2! d_3!)` (T1); `Var(v_x) = σ² Σ_{n<t} g^{2n} P_n`
with `1/(36n) ≤ P_n ≤ 9π/(16n)` (T2); the symbol
`1 − 2wΣcos k_j + w²(3 + 2Σ_{i<j}cos(k_i − k_j))`, expansion `K²/9 + |k_⊥|⁴/36`
at `g = 1` (T3); `p_{2n}^{static} = (C(2n,n)/4^n) · P_n` (T3); `κ = f'(1)/(2f(1))`,
`σ² = 2/3` for the Born overlap (T5). Executed with exact arithmetic:
23 checks, 15 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's record-dynamics seam (#8093): whether a Laplacian or transverse kernel appears in the finished record statistics of a formation law with no tick supplied; its counterexample branch: the record-side correlators are short-ranged; the gravity node's input: a scalar record statistic whose two-point function equals the lattice Green function"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the seam is answered exactly on the Gaussian instance: the formation law's two-point function is a heat kernel in level time (parabolic), never the lattice Green function; it is massless iff the rule is value-covariant, and then log-correlated with no stationary law. Consumers: #8093's record-dynamics and assembly blocks; the gravity node (its Green-function statistic is not a formation-law two-point function of a linear rule); the campaign's queue"
conditional_surface_status: "T1–T5 proved for every w > 0 and σ² > 0 (T2b, T3 at g = 1; T2a at g < 1); executed at g = 1 and g = 1/2 to level 200 exactly, on a 5×5 transverse torus, and symbolically; conditional on the records-only reading, the monotone class and the Gaussian instance as supplied conditions"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "an explicit inverse of a unit lower-triangular operator (T1); exact series with elementary two-sided bounds (T2, T4); a trigonometric identity and an exact walk-count identity (T3); second-order Taylor coefficients computed symbolically (T5); every number an exact rational"
```

## Premises and declared objects

**Axioms used (verbatim).** From
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): "There is one
fixed nearest-neighbor admissibility rule, covariant under lattice translations
and proper cubic rotations." — "For each site, the probability distribution over
the possibilities is determined by, and varies with, the nearest-neighbor
conditions." — "Records form." — "Only records are readable."

**Readings carried, named, nothing new adopted.** The records-only reading
(block 01); the monotone class (block 05); the Gaussian instance (block 07): a real value at each site. Level time: every predecessor `x − e_i` of a site lies one level below (`x_1 + x_2 + x_3` drops by one), so under the monotone class the law is a recursion level by level — the observation block 12 (PR #8146, open; not an input here) calls level time. **The rule.** A site
`x` whose recorded predecessors are `x − e_1, x − e_2, x − e_3` draws
`v_x = w (v_{x−e_1} + v_{x−e_2} + v_{x−e_3}) + ξ_x`, `ξ_x` independent centered
Gaussians of variance `σ² > 0`, `w > 0`. The three predecessors form one orbit
of the 3-fold rotation about the corner's diagonal, so covariance under proper
cubic rotations makes the three weights equal; the gain is `g = 3w`.

**The half-space in level time.** `H = {x ∈ Z³ : ℓ(x) = x_1 + x_2 + x_3 ≥ 0}`;
the level-0 records are given (the law below is the law of levels `≥ 1`
conditional on level 0, as block 08's plane chain conditions on a plane). Every
site of level `t ≥ 1` has its three predecessors in `H`, so in every order of
the monotone class it records exactly them and the law is one (block 07, G2).
With the projection `π(x) = (x_2, x_3)` to the transverse plane: `v_t = w (I + S_1 + S_2) v_{t−1} + ξ_t` on
`Z²`, `S_1, S_2` the shifts by `(1,0)`, `(0,1)`. Write `A = w(I + S_1 + S_2)`.

**Walks.** A *directed walk* takes steps `e_1, e_2, e_3` with probability
`1/3` each; two independent directed walks *coincide* after `n` steps when
their displacements agree; `P_n` is that probability,
`P_n = Σ_{|α| = n} (n!/α!)²/9^n` over compositions `α` of `n` into three parts.
The *simple random walk* takes steps `±e_j` with probability `1/6` each;
`p_m` is its return probability after `m` steps.

## Prior art and what is new

Block 07 (on main) gave the formation precision `L†DL` of the Gaussian instance on
finite windows and showed it differs from the static precision on every window
with an edge; block 09 (PR #8139) gave the Markov graph of the six-menu law; block 12
(PR #8146) the level-time identification; both open, neither an input. Linear stochastic growth in level time is the classical
Edwards–Wilkinson equation, and its logarithmic roughness in two transverse
dimensions is classical; the bounds here use the second-moment inequality
(Chebyshev), the quadratic-mean inequality (Cauchy–Schwarz), the Fourier
representation of a return probability (Parseval), and the standard binomial
bounds — all re-proved at scope in the note or stated as elementary
identities. The lattice Green function `1/(4π r)` is the gravity lane's
supplied asymptotic (`ALPHA_BARE_FOUR_PI_FROM_Z3_PLANCHEREL_BRIDGE_BOUNDED_NOTE_2026-05-26.md`). Nothing on `main` (`af0fc1206d`;
search recorded in `ROUTE_PORTFOLIO.md`) computes a formation law's two-point
function at long distance or compares it with a static Green function.

New here: the exact directed-path kernel and its overlap form for the
formation law (T1); the gain dichotomy with explicit constants and the
non-existence of a stationary law at `g = 1` (T2); the symbol, the parabolic
expansion, and the exact identity `p_{2n} = (C(2n,n)/4^n) P_n` that separates
the static Green function from the formation two-point function in three
dimensions (T3); the two-dimensional contrast (T4); what forces `g = 1`,
including the Born-overlap linearization and the inversion "massless static
law ↔ massive formation rule at `g = 1/2`" (T5).

## Exact target and obligation graph

| obligation | status here |
|---|---|
| T1 the directed-path kernel and the overlap covariance | proved; executed on a `5×5` transverse torus against the covariance recursion (B1–B2) |
| T2 the growth laws: `g < 1` bounded with a unique stationary law and exponential decay; `g = 1` harmonic growth, no stationary law; `g > 1` exponential | proved; `P_n` executed exactly to `n = 200` against the bounds; the series at `g = 1`, `g = 1/2` (C1–C4) |
| T3 the symbol = block 09's graph; parabolic expansion; the static/formation identity; not the lattice Green function | proved; executed symbolically and on the exact partial sums (D1–D4) |
| T4 one transverse dimension: `P_n = C(2n,n)/4^n`, square-root growth | proved; executed to `n = 400` (E1) |
| T5 what forces `g = 1`; the Born linearization; block 07's instance | proved; executed symbolically (E2–E4) |
| the same statements for the sphere menu beyond second order; an ordered phase of the sphere rule; the static law's own phase structure | open; not this note |

## Theorem T1 — the directed-path kernel

**Statement.** For `x ∈ H` of level `t ≥ 1`,
`v_x = Σ_{z: ℓ(z)=0} G(x,z) v_z + Σ_{z: 1 ≤ ℓ(z) ≤ t} G(x,z) ξ_z`, where
`G(x,z) = w^n · n!/(d_1! d_2! d_3!)` if `d = x − z` has all `d_j ≥ 0`, with
`n = ℓ(x) − ℓ(z) = |d|_1`, and `G(x,z) = 0` otherwise. Hence
`E[v_x | level 0] = Σ_{ℓ(z)=0} G(x,z) v_z` and
`Cov(v_x, v_y) = σ² Σ_{1 ≤ ℓ(z) ≤ min(ℓ(x),ℓ(y))} G(x,z) G(y,z)`.
For fixed `x` and `n`, `Σ_{ℓ(z) = ℓ(x) − n} G(x,z) = g^n`; at `g = 1` the
kernel `G(x, ·)` restricted to a level is the law of the endpoint of a directed
walk of `n` steps from `x` run backward: a probability kernel, the heat kernel
of level time.

*Proof.* Iterate the recursion `v_x = w Σ_i v_{x−e_i} + ξ_x` down to level 0:
each term is a monotone path from `z` to `x` weighted by `w` per step, and the
number of monotone paths with displacement `d` is the multinomial coefficient.
The noises are independent of the level-0 records and of each other, giving the
mean and the covariance. The level sum of the multinomial coefficients is
`3^n`, so `Σ_z G(x,z) = (3w)^n = g^n`. ∎ Executed: on the `5×5` transverse torus
with six levels the covariance recursion `C_t = A C_{t−1} Aᵀ + σ² I` equals the
kernel formula (with periodic images) exactly (B1); the level sums (B2).

## Theorem T2 — the gain dichotomy

**Statement.** Let `t = ℓ(x)`. Then
`Var(v_x | level 0) = σ² Σ_{n=0}^{t−1} g^{2n} P_n`, and for two sites on the
same level at transverse displacement `d`,
`Cov(v_x, v_y) = σ² Σ_{n=0}^{t−1} g^{2n} P_n(d)`, `P_n(d)` the probability that
the difference of two independent directed walks is `d` after `n` steps.
- (a) `g < 1`: `Var(v_x) ≤ σ²/(1 − g²)`; for `|d|_∞ = m`, `Cov ≤ σ² g^{2m}/(1 − g²)`;
  for `y` downstream of `x` by `s` levels, `|Cov(v_x, v_y)| ≤ g^s · sup Var`.
  The level laws have a limit as `t → ∞` for every bounded level-0 plane, and
  there is exactly one stationary law on `Z³` (translation-invariant in level
  time and in the plane, with uniformly bounded variance): the centered Gaussian
  with covariance `σ² Σ_n g^{2n} P_n(·)`.
- (b) `g = 1`: for `n ≥ 1`, `1/(36 n) ≤ P_n ≤ 9π/(16 n)`; hence
  `σ² H_t/36 ≤ Var(v_x) ≤ σ² (1 + 9π H_{t−1}/16)` with `H_t` the harmonic
  number; the variance grows without bound, and no stationary law with
  uniformly bounded variance exists.
- (c) `g > 1`: `Var(v_x) ≥ σ² g^{2(t−1)} P_{t−1} ≥ σ² g^{2(t−1)}/(36(t−1))`.

*Proof.* The variance formula is T1 with `Σ_z G(x,z)² = w^{2n} Σ_α (n!/α!)² = g^{2n} P_n`
on the level `n` below `x`; the covariance formula likewise, the coincidence
replaced by the displacement `d` (the two backward walks from `x` and `y` meet
at `z` iff their difference equals `y − x`). (a) `Σ g^{2n} P_n ≤ Σ g^{2n}`. The
difference walk moves at most one unit per coordinate per step, so
`P_n(d) = 0` for `n < |d|_∞`. Downstream: `v_y = Σ_u G(y,u) v_u + (fresh noise)`
over `u` on `x`'s level, and `Cov(v_x, v_y) = Σ_u G(y,u) Cov(v_x, v_u)`, a sum
of weights `g^s` times terms bounded by `sup Var` (quadratic-mean inequality).
For the limit and uniqueness: after `n` further levels,
`v = (A^n v_{earlier}) + (noise of the last n levels)`, the two parts
independent; the first has variance at most `(Σ weights)² sup Var = g^{2n} sup Var`
(quadratic-mean inequality with nonnegative weights) and tends to zero, so the
covariance of any bounded-variance stationary law equals the series, and the
level laws from any bounded plane have that limit. (b) Upper bound: `P_n` is the
return probability of the difference walk, whose characteristic function on the
torus is `|φ(k)|²`, `φ(k) = (1 + e^{ik_1} + e^{ik_2})/3` (the projected steps);
so `P_n = (2π)^{−2} ∫ |φ|^{2n} dk`. Now
`|φ|² = 1 − (2/9)[(1 − cos k_1) + (1 − cos k_2) + (1 − cos(k_1 − k_2))] ≤ 1 − (4/(9π²))(k_1² + k_2²)`
on `[−π, π]²` (using `1 − cos u ≥ 2u²/π²` there), hence
`P_n ≤ (2π)^{−2} ∫_{R²} e^{−(4n/(9π²))|k|²} dk = (2π)^{−2} · 9π³/(4n) = 9π/(16 n)`.
Lower bound: the walk's position after `n` steps has mean `(n/3, n/3)` and
coordinate variances `2n/9`; by the second-moment inequality it lies within
the square of half-side `R = (8n/9)^{1/2}` around the mean with probability
at least `1/2`; that square has at most `(2R + 1)² ≤ 9n` lattice points
(`n ≥ 1`); the quadratic-mean inequality gives
`P_n = Σ_d P(X_n = d)² ≥ (1/2)²/(9n) = 1/(36 n)`. The variance bounds follow by
summing (`P_0 = 1`). Non-existence: if a stationary law had variance `≤ V`,
then decomposing over `n` earlier levels as in (a), the noise part alone has
variance `σ² Σ_{m<n} P_m ≥ σ² H_n/36`, which exceeds `V` for large `n`; the
parts are independent, contradiction. (c) Keep the last term. ∎ Executed:
`P_n` exactly for `n ≤ 200` against the rational relaxation `1/(36n) ≤ P_n ≤ 2/n`
(the note's `9π/16 < 2`) and `n P_n` (C1); the variance series at `g = 1`
against `H_t/36` and `1 + 2H_{t−1}` (C2); at `g = 1/2` against `4/3` and the
transverse decay bound (C3); the downstream bound on the torus (C4).

*Reading.* At `g = 1` the record field is log-correlated in the transverse
plane and has no equilibrium: the memory of the boundary and of every noise
spreads diffusively and never dies; the variance at level `t` is exactly
`σ²` times the expected number of coincidences of two backward directed walks,
executed as `2.040, 2.714, 3.002, 3.289` (`σ² = 1`) at `t = 10, 50, 100, 200`.

## Theorem T3 — the symbol, and why it is not the lattice Green function

**Statement.** (i) At `g < 1` the stationary law's precision is `σ^{−2}(I − A)†(I − A)`
with symbol
`|1 − wΣ_j e^{−ik_j}|² = 1 − 2wΣ_j cos k_j + w²(3 + 2Σ_{i<j} cos(k_i − k_j))`:
constant `1 + 3w²`, axial edges `−2w`, face diagonals `x ± (e_i − e_j)` with
`+2w²` — exactly the axial-plus-face-diagonal graph that block 09 (PR #8139, open; not an input here) found for the six-menu law. (ii) At `g = 1` (`w = 1/3`),
along `k = (u,u,u)` the symbol is `u² = K²/9` with `K = Σ k_j`, and on the
transverse plane `K = 0` it is `|k|⁴/36 + O(|k|⁶)`: parabolic, quadratic in the
level direction and quartic transversally. (iii) For every `n ≥ 0`,
`p_{2n} = (C(2n,n)/4^n) · P_n` and `p_{2n+1} = 0`; hence the static massless
Green function's diagonal `Σ_m p_m /6` is at most
`(1/6)(1 + Σ_{n≥1} (√3/2)(2n+1)^{−1/2} · 9π/(16n)) < ∞` (it exists on `Z³`),
while the formation law's diagonal series `σ² Σ_n P_n` diverges. The
two-point function of the formation law is not, at any gain, the lattice Green
function: at `g < 1` it decays exponentially where `1/(4π r)` does not; at
`g = 1` it does not exist as a stationary object.

*Proof.* (i) `(I − A)` has symbol `1 − wΣ e^{−ik_j}`; multiply by its
conjugate and expand `|Σ_j e^{−ik_j}|² = 3 + 2Σ_{i<j} cos(k_i − k_j)`. (ii)
Substitute and expand to fourth order (executed symbolically; the transverse
quartic is `(q_1² + q_1 q_2 + q_2²)²/9` for `k = (q_1, q_2, −q_1 − q_2)`, which
equals `|k|⁴/36`). (iii) A simple random walk returns after `2n` steps iff for
each `j` it takes `a_j` steps `+e_j` and `a_j` steps `−e_j` with `Σ a_j = n`;
the number of such walks is `Σ_a (2n)!/(a_1!² a_2!² a_3!²) = C(2n,n) Σ_a (n!/a!)²`,
and `6^{2n} = 4^n 9^n`. The bound uses T4 for the binomial and T2(b) for `P_n`.
The last sentence: at `g < 1` by T2(a); at `g = 1` by T2(b). ∎ Executed: the
symbol identity and the two expansions symbolically (D1–D2); the identity
`p_{2n} = (C(2n,n)/4^n) P_n` against a direct count of returning walks for
`n ≤ 6` (D3); the partial sums: the static series stays below `1.52` to
`n = 200` while the formation series exceeds `H_t/36` at every `t` (D4).

*Reading.* The static law's return walk goes back and forth (six directions);
the formation law's walk goes one way (three directions). The undirected walk's
freedom to retrace contributes exactly the factor `C(2n,n)/4^n ~ n^{−1/2}`,
and that factor is the difference between a summable series in three
dimensions (a Green function, `1/(4π r)`) and a logarithmically divergent one.
A causal law cannot produce the elliptic kernel; it produces the parabolic one.

## Theorem T4 — one transverse dimension

**Statement.** For the monotone class on `Z²` (two predecessors, gain
`g = 2w`), `P_n = C(2n,n)/4^n` and `1/(4n) ≤ P_n² ≤ 3/(4(2n+1))`, so at `g = 1`
`Var(v_x) ≥ σ² Σ_{n<t} (2√n)^{−1}`, growing like the square root of the level.

*Proof.* The difference of two independent directed walks on `Z²` projected
to one coordinate is a lazy walk and its coincidence probability is the
central binomial term. With `a_n = C(2n,n)/4^n = Π_{k≤n}(2k−1)/(2k)`, the
sequences `4n a_n²` and `(2n+1) a_n²` are increasing and decreasing
respectively (the ratios `(2n+1)²/(4n(n+1))` and `(2n+1)(2n+3)/(2n+2)²`), with
values `1` and `3/4` at `n = 1`. ∎ Executed to `n = 400` (E1).

## Theorem T5 — what forces `g = 1`

**Statement.** (a) If the rule is covariant under the value translations
`v ↦ v + c` (no value privileged on the line), then `g = 1`.
(b) Let `f` be a zonal overlap on the sphere, smooth at `t = 1` with `f(1) > 0`
and `f'(1) > 0`, and let `s, a_1, a_2, a_3` be unit vectors near a common pole
with exponential coordinates `θ, θ_1, θ_2, θ_3 ∈ R²`. The second-order
expansion of `log Π_i f(s·a_i)` in the coordinates is
`3 log f(1) − κ Σ_i |θ − θ_i|²`, `κ = f'(1)/(2f(1))`: as a quadratic form in `θ`
its minimizer is the average `(θ_1 + θ_2 + θ_3)/3` (gain one) and its variance
is `1/(6κ) = f(1)/(3f'(1))` per component. For the Born overlap `f(t) = (1+t)/2`:
`κ = 1/4`, variance `2/3`; for `f(t) = e^{βt}`: `κ = β/2`, variance `1/(3β)`.
(c) Block 07's real instance (`P_xx = 3`, every edge `−1/2`) is
`P = (1/2)(6I − Σ_{±j} S_j)`, the massless static Laplacian, and the formation
rule it defines has weight `1/6` per recorded neighbour: `g = 1/2` with three
predecessors. Conversely the massless formation rule `w = 1/3` is the one-site
conditional of no static law: the six-neighbour precision it would need,
`3I − Σ_{±j} S_j`, has symbol `3 − 2Σ_j cos k_j`, negative at `k = 0`.

*Proof.* (a) The mean must shift by `c`: `w Σ(a_i + c) = wΣa_i + c` forces
`3w = 1`. (b) `s·a_i = cos ∠(s, a_i)` and `∠(s,a_i)² = |θ − θ_i|² + O(4)`, so
`log f(s·a_i) = log f(1) − (f'(1)/f(1)) |θ − θ_i|²/2 + O(3)`; the quadratic form
`−κ Σ|θ − θ_i|²` is minimized at the average and its Hessian is `−6κ I`. (c)
Read off block 07's formula `mean = −(1/P_xx) Σ P_xy z_y`; the symbol of
`3I − Σ_{±j}S_j` at `k = 0` is `3 − 6`. ∎ Executed: the expansions for both `f`
symbolically (E2); block 07's instance (E3); the non-positive symbol (E4).

*Reading.* The gain is not a free knob once covariance is read on the value
space: the massless case is the covariant one. Under the Born overlap, the
transverse record fluctuations of an aligned region are the massless causal
law with `σ² = 2/3` — a statement about second-order coefficients only; whether
an aligned region exists at all is block 12's obligation and is not claimed.

## No-Go Discipline Gate

The negative sentences are: no stationary law with bounded variance at
`g = 1` (T2b), and the formation two-point function is never the lattice Green
function (T3). Both are proved for every `w, σ²`.

### N1 — Routes by which a formation two-point function could still be a Green function

| route | what it would attempt | why it fails here, or its obligation | marker |
|---|---|---|---|
| 1 a different gain | `g ≠ 1` | `g < 1` decays exponentially; `g > 1` blows up (T2) | RULED OUT AT SCOPE |
| 2 a non-monotone order | recorded sets of size two and one at the boundary | outside the class; the bulk kernel is the same directed kernel for every order in which each site records its three predecessors | narrowed |
| 3 a nonlinear rule (the sphere menu beyond second order) | non-Gaussian fluctuations | not this note; T5(b) covers the second order only; obligation named | not attempted |
| 4 a static reading | the six-neighbour conditional as a Gibbs specification | then the two-point function is the static one, `1/(4π r)` at `m = 0` — but that is the static law, not the formation law (block 01) | ATTEMPTED (T5c, the inversion) |
| 5 the zero-gain limit | `w → 0` | independent sites; no kernel at all | trivial |

### N2 — Wall-independence audit
Walls: the records-only reading, the monotone class, the Gaussian instance, positivity of `σ²`. Independent; each defines the object.

### N3 — Hidden-wall scan
Scanned for "we assume", "by construction", "as is standard", "the framework provides", "naturally", "obviously", "canonical", "registered", "background", "bridge context". Hits: none in the theorems.

### N4 — Per-citation table
| cited surface | residual it attacks | residual claimed here | match |
|---|---|---|---|
| block 07 (on main): G1, G2, the real instance | the Gaussian instance's precision | T1's setting; T5(c) | yes |
| block 12 (PR #8146, open; not an input) | level time | the automaton form, restated here | context only |
| block 09 (PR #8139, open; not an input) | the Markov graph | the remark after T3(i) | context only |
| the gravity lane's `1/(4π r)` (main) | the Green-function asymptotic | the contrast in T3(iii) (the static object; not re-derived) | reference only |

### N5 — Resolution audit
| phrase | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| "never the lattice Green function"; "no stationary law at `g = 1`" | executed: `P_n` to `n = 200`, the binomial bounds to `n = 400`, the walk identity to `n = 6` | executed: the torus covariance at every site of six levels | executed: the symbol and its two expansions | executed: the variance series at two gains to level 200; the static and formation partial sums | proved for every `w, σ²` (T2, T3); the sphere rule beyond second order is not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no gain and no boundary; none is a wall. The parabolic-versus-elliptic distinction is structural (causality), not a tuning.

### N7 — Steelman
Hostile reviewer: "Linear stochastic growth is textbook; the log roughness of a two-dimensional interface is known; you have renamed it." Reply: agreed on the objects; what is new is exact and framework-level — the formation law's two-point function as a directed-walk overlap, `g = 1` forced by covariance, the non-existence of a stationary law there, the identity `p_{2n} = (C(2n,n)/4^n) P_n` that separates the static Green function from the formation two-point function, the Born linearization, and the `g = 1/2` inversion of block 07's instance. Conceded: nothing beyond the Gaussian instance and the second-order sphere expansion is claimed.

### N8 — Cross-cycle echo
Block 08's exponential decay in the region is the finite-menu counterpart of T2(a); block 12's level automaton is the nonlinear counterpart of the automaton here. No structurally similar wall was retired.

## Falsifiers
- A level and site on the torus where the covariance recursion and the kernel formula disagree (B1), or a level sum not equal to `g^n` (B2).
- An `n ≤ 200` with `P_n` outside `[1/(36n), 2/n]` (C1); a level where the variance series leaves its bounds (C2); a variance above `4/3` at `g = 1/2` (C3).
- A symbol coefficient not matching block 09's graph, a level-direction expansion other than `K²/9`, or a transverse quartic other than `|k|⁴/36` (D1–D2); an `n ≤ 6` where the direct count of returning walks differs from `C(2n,n) Σ_a (n!/a!)²` (D3).
- An `n ≤ 400` violating the binomial bounds (E1); a second-order expansion of `log f` whose quadratic form is not `−κ Σ|θ − θ_i|²` with `κ = f'(1)/(2f(1))` (E2); block 07's real instance with a gain other than `1/2` (E3); a positive symbol for `3I − Σ S_j` at `k = 0` (E4).

## Boundaries and non-claims
This note computes the two-point function of the Gaussian instance of the formation law in the monotone class and compares it with the static Green function; it does not select an order, rule, gain or coupling as physical, does not claim an ordered phase of the sphere rule (block 12's obligation stands), and makes no statement about the static law beyond the exact identities used. No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. The lattice Green function `1/(4π r)` is named as the gravity lane's supplied asymptotic and is not re-derived; no value, constant or theorem is imported as authority.

Further: the sphere menu is treated only at second order (T5b); non-Gaussian fluctuations, the massless law's transverse correlation profile beyond the executed values, and any statement about what the gravity lane should use instead are not claimed.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 07 (on main; the Gaussian instance and its precision): proposed, unaudited; the parts used are restated. Blocks 09 and 12 (open PRs #8139, #8146) are referenced for context only and are not inputs.
- Re-proved at scope: T1–T5, including the second-moment inequality (Chebyshev), the quadratic-mean inequality (Cauchy–Schwarz), the Fourier representation of the return probability (Parseval), the binomial bounds, and the walk-count identity.
- Reference only (named, not used as authority): the Edwards–Wilkinson equation and its logarithmic roughness in `2+1` dimensions; the gravity lane's `1/(4π r)`.

## Review record
Supervisor-run block (owner directive: pull up after block 12 and find the next high-leverage science; no subagents). The control (`specs/supervisor_control_block13_causal_gaussian.py`) computed `P_n`, the variance series, the torus check, the symbol expansions, grid sums and the Taylor expansions before the contract; the lens pass is in `GOAL_block13.md`; the primary seat wrote T1–T5 and the runner; the refuting pass (`CHECKER_block13_findings.md`) recomputed the torus covariance by explicit inversion of `I − A` on the full six-level system, the coincidence probabilities from the multinomial formula instead of the walk counts, and the static return probabilities by a direct walk enumeration. Facts settled while executing: block 12's note is not on `main`, so the block is an independent PR against `main` with block 07 as its only declared parent (level time restated; blocks 09 and 12 referenced for context only); the runner checks the rational relaxation `2/n` of the note's `9π/(16n)`; a decimal string in a detail message tripped the runner's own floating-point scan and was replaced by a fraction; the yaml's quotation of the campaign's phrase contained a token the note forbids and was reworded.

## Verification

```bash
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py --exact
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py --mutation stationary_law_at_g1_claimed
```

Families: A authority and inputs; B the kernel on the torus and the level sums; C the coincidence probabilities, the variance series at two gains, the decay bounds; D the symbol, its expansions, the walk identity, the partial sums; E the binomial bounds, the Taylor expansions, block 07's instance, the non-positive symbol; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 15 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=23 FAIL=0`.
