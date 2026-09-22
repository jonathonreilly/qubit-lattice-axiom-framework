---
claim_id: admissibility_rule_directed_gaussian_propagator_overlap_covariance_gain_bounds_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For a supplied real linear Gaussian recursion on the directed half-space of Z^3 with w>0, gain g=3w, independent centered innovations of variance sigma^2 and fixed level-0 records: exact directed multinomial propagator and accumulated-overlap covariance; finite-level variance series with subcritical geometric upper bounds, critical harmonic bounds and supercritical last-term lower bound; constructed subcritical stationary innovation solution; precision symbol, critical directional expansions and exact directed/undirected return-walk identity. One-transverse-dimensional binomial bounds. Additional value-translation covariance is equivalent to gain one within this family. The sphere log-density Taylor polynomial defines an auxiliary flat Gaussian, not the actual sphere fluctuation law. Broad nonexistence, all-causal Green-function exclusion and exhaustive stationary-law classification are deferred."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_hermitian_gaussian_instance_formation_precision_ldl_bounded_theorem_note_2026-09-07
runner: scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py
---

# Directed Gaussian propagation: overlap covariance, gain bounds and walk identities

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (supplied mathematical model; unaudited)

## Result up front

For the explicitly supplied linear recursion, each innovation propagates by a
weighted directed-walk kernel. The record covariance is the sum of overlaps
of those propagators over all earlier innovation levels; it is not a single
heat kernel. Exact counting gives geometric variance bounds for gain below
one, harmonic bounds at gain one, and a last-term exponential lower bound for
gain above one. The note also constructs the subcritical stationary innovation
solution and computes its precision symbol. These are properties of this
supplied Gaussian model, not consequences of lattice covariance alone.

The exact walk-count identity relates the critical overlap series to the
simple random walk return series. Separately, a sphere log-density Taylor
polynomial defines an auxiliary Gaussian on a flat tangent plane. Its Born
coefficient gives variance `2/3` only for that auxiliary Gaussian. For the
actual sphere density with three aligned Born factors, `E[s_z]=3/5` and
`E[s_x²]=4/15`.

The actual linked parent uses a finite two-dimensional complex Gaussian with
real edge entry `+1/2`, giving conditional coefficient `−1/6`. The
sign-reversed three-dimensional real fixture below is a separate supplied
comparison, not the parent's instance. No physical rule, gain or order is
selected.

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
next_trace_action: "Use the explicit propagator, overlap covariance, gain bounds and walk-count identities within the supplied model. Broader negative and stationary-law classification claims remain deferred."
conditional_surface_status: "Finite-level identities for w>0 and sigma^2>0; constructed subcritical innovation solution for g<1; formal critical symbol at g=1; tangent-plane Gaussian explicitly auxiliary. No exhaustive stationary-law or all-causal exclusion claim."
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
(block 01); the monotone class (block 05); an independently supplied real Gaussian recursion. The actual
[Hermitian Gaussian predecessor](ADMISSIBILITY_RULE_HERMITIAN_GAUSSIAN_INSTANCE_FORMATION_PRECISION_LDL_BOUNDED_THEOREM_NOTE_2026-09-07.md)
provides the finite conditional/triangular-factor algebra; its declared fixture
is finite, two-dimensional and complex-valued, including its real-entry
precision. It does not supply the present three-dimensional real model. Level time: every predecessor `x − e_i` of a site lies one level below (`x_1 + x_2 + x_3` drops by one), so under the monotone class the law is a recursion level by level — the observation block 12 (PR #8146, open; not an input here) calls level time. **The rule.** A site
`x` whose recorded predecessors are `x − e_1, x − e_2, x − e_3` draws
`v_x = w (v_{x−e_1} + v_{x−e_2} + v_{x−e_3}) + ξ_x`, `ξ_x` independent centered
Gaussians of variance `σ² > 0`, `w > 0`. The three predecessors form one orbit
of the 3-fold rotation about the corner's diagonal, so equal weights respect that stabilizer. Equal weights, the real value menu
and independent Gaussian innovations are supplied here; lattice covariance
alone does not select them or value-translation covariance. The gain is `g = 3w`.

**The half-space in level time.** `H = {x ∈ Z³ : ℓ(x) = x_1 + x_2 + x_3 ≥ 0}`;
the level-0 records are given (the law below is the law of levels `≥ 1`
conditional on level 0, as block 08's plane chain conditions on a plane). Every
site of level `t ≥ 1` has its three predecessors in `H`, so in every order of
the monotone class it records exactly them and the product of these specified independent-innovation conditionals is the
same under every such order. This follows directly from the identical predecessor sets.
With the projection `π(x) = (x_2, x_3)` to the transverse plane: `v_t = w (I + S_1 + S_2) v_{t−1} + ξ_t` on
`Z²`, `S_1, S_2` the shifts by `(1,0)`, `(0,1)`. Write `A = w(I + S_1 + S_2)`.

**Walks.** A *directed walk* takes steps `e_1, e_2, e_3` with probability
`1/3` each; two independent directed walks *coincide* after `n` steps when
their displacements agree; `P_n` is that probability,
`P_n = Σ_{|α| = n} (n!/α!)²/9^n` over compositions `α` of `n` into three parts.
The *simple random walk* takes steps `±e_j` with probability `1/6` each;
`p_m` is its return probability after `m` steps.

## Prior art and what is new

The linked Hermitian Gaussian predecessor proves finite conditional-product
factorization. Here the supplied real directed recursion is expanded into
multinomial propagators and overlap covariances. Elementary second-moment and
quadratic-mean inequalities (Chebyshev and Cauchy–Schwarz), Fourier inversion
for a finitely supported lattice walk, Gaussian integration and binomial
identities give the bounds below. Linear stochastic growth is also studied
under the Edwards–Wilkinson model; that name supplies neither a numerical
value nor a physical identification here. No gravity asymptotic is used.

## Exact target and obligation graph

| result | retained scope |
|---|---|
| T1 propagator and covariance | exact finite-level innovation expansion |
| T2 gain bounds | finite levels; subcritical infinite-past construction |
| T3 symbol and walk identity | subcritical precision; formal critical symbol; exact return counts |
| T4 one transverse dimension | central binomial identity and finite-level bounds |
| T5 value shifts and tangent expansion | additional value symmetry within this family; auxiliary Gaussian and actual aligned-sphere moments distinguished |
| all stationary laws, all causal kernels, nonlinear sphere dynamics | deferred; no exhaustive exclusion certificate |

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
  the centered infinite-past innovation series constructs a spatially and
  temporally stationary Gaussian law whose equal-level covariance is
  `σ² Σ_n g^{2n} P_n(·)`. This construction is adapted: innovations are
  independent of the past. No classification of other stationary laws is asserted.
- (b) `g = 1`: for `n ≥ 1`, `1/(36 n) ≤ P_n ≤ 9π/(16 n)`; hence
  `σ² H_t/36 ≤ Var(v_x) ≤ σ² (1 + 9π H_{t−1}/16)` with `H_t` the harmonic
  number; these finite-level variances grow without bound.
- (c) `g > 1`, `t ≥ 2`: `Var(v_x) ≥ σ² g^{2(t−1)} P_{t−1} ≥ σ² g^{2(t−1)}/(36(t−1))`.

*Proof.* The variance formula is T1 with `Σ_z G(x,z)² = w^{2n} Σ_α (n!/α!)² = g^{2n} P_n`
on the level `n` below `x`; the covariance formula likewise, the coincidence
replaced by the displacement `d` (the two backward walks from `x` and `y` meet
at `z` iff their difference equals `y − x`). (a) `Σ g^{2n} P_n ≤ Σ g^{2n}`. The
difference walk moves at most one unit per coordinate per step, so
`P_n(d) = 0` for `n < |d|_∞`. Downstream: `v_y = Σ_u G(y,u) v_u + (fresh noise)`
over `u` on `x`'s level, and `Cov(v_x, v_y) = Σ_u G(y,u) Cov(v_x, v_u)`, a sum
of weights `g^s` times terms bounded by `sup Var` (quadratic-mean inequality).
For the construction, the infinite-past innovation terms are independent
centered Gaussian variables with total variance bounded by the geometric
series. The mean-square norm of their tails tends to zero on each finite set of
sites; consistency gives a Gaussian field. Translation of the iid innovation
array commutes with the recursion, so this constructed law is stationary in
space and level time. For a bounded deterministic initial plane,
`|A^n v_0| ≤ g^n sup|v_0|`, and the finite-level Gaussian covariances approach
the same sums. (b) Upper bound: `P_n` is the
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
summing (`P_0 = 1`). (c) Keep the last term. ∎ Executed:
`P_n` exactly for `n ≤ 200` against the rational relaxation `1/(36n) ≤ P_n ≤ 2/n`
(the note's `9π/16 < 2`) and `n P_n` (C1); the variance series at `g = 1`
against `H_t/36` and `1 + 2H_{t−1}` (C2); at `g = 1/2` against `4/3` and the
transverse decay bound (C3); the downstream bound on the torus (C4).

*Reading.* At `g=1`, the finite-level variance is `σ²` times the accumulated
coincidence probability of two directed walks. The displayed harmonic bounds
quantify its level growth; they do not establish a complete transverse
correlation profile or classify all stationary probability laws.

## Theorem T3 — the precision symbol and return-walk identity

**Statement.** (i) At `g < 1` the constructed stationary innovation law's precision is
`σ^{−2}L†L`, where on the full space-time lattice `L=I−wΣ_j S_j`
with symbol
`|1 − wΣ_j e^{−ik_j}|² = 1 − 2wΣ_j cos k_j + w²(3 + 2Σ_{i<j} cos(k_i − k_j))`:
constant `1 + 3w²`, axial cosine coefficients `−2w`, diagonal cosine
coefficients `+2w²`. The corresponding individual precision entries are
`−w` on each axial neighbor and `w²` on each face-diagonal neighbor, all
multiplied by `σ^{−2}` — exactly the axial-plus-face-diagonal graph that block 09 (PR #8139, open; not an input here) found for the six-menu law. (ii) At `g = 1` (`w = 1/3`),
along `k = (u,u,u)` the symbol is `2−2cos u = u² + O(u⁴)` with `K = Σ k_j = 3u`, so the quadratic term is `K²/9`, and on the
transverse plane `K = 0` it is `|k|⁴/36 + O(|k|⁶)`: parabolic, quadratic in the
level direction and quartic transversally. (iii) For every `n ≥ 0`,
`p_{2n} = (C(2n,n)/4^n) · P_n` and `p_{2n+1} = 0`; hence the static massless
Green function's diagonal `Σ_m p_m /6` is at most
`(1/6)(1 + Σ_{n≥1} (√3/2)(2n+1)^{−1/2} · 9π/(16n)) < ∞` (it exists on `Z³`),
while the formation law's diagonal series `σ² Σ_n P_n` diverges. These are summability statements for the two displayed series. No universal
claim about all causal laws or all static specifications is made.

*Proof.* (i) The full-lattice innovation operator `L` has symbol `1 − wΣ e^{−ik_j}`; multiply by its
conjugate and expand `|Σ_j e^{−ik_j}|² = 3 + 2Σ_{i<j} cos(k_i − k_j)`. (ii)
Substitute and expand to fourth order (executed symbolically; the transverse
quartic is `(q_1² + q_1 q_2 + q_2²)²/9` for `k = (q_1, q_2, −q_1 − q_2)`, which
equals `|k|⁴/36`). (iii) A simple random walk returns after `2n` steps iff for
each `j` it takes `a_j` steps `+e_j` and `a_j` steps `−e_j` with `Σ a_j = n`;
the number of such walks is `Σ_a (2n)!/(a_1!² a_2!² a_3!²) = C(2n,n) Σ_a (n!/a!)²`,
and `6^{2n} = 4^n 9^n`. The bound uses T4 for the binomial and T2(b) for `P_n`.
The series bounds are exactly those just proved. ∎ Executed: the
symbol identity and the two expansions symbolically (D1–D2); the identity
`p_{2n} = (C(2n,n)/4^n) P_n` against a direct count of returning walks for
`n ≤ 6` (D3); the partial sums: the static series stays below `1.52` to
`n = 200` while the formation series exceeds `H_t/36` at every `t` (D4).

*Reading.* The undirected return count contains the additional central
binomial factor. Together with the proved bounds, this gives a summable
undirected series and harmonic growth of the directed overlap partial sums.
This identity concerns the specified walks, not an exclusion of other kernels.

## Theorem T4 — one transverse dimension

**Statement.** For the monotone class on `Z²` (two predecessors, gain
`g = 2w`), `P_n = C(2n,n)/4^n` and, for `n≥1`, `1/(4n) ≤ P_n² ≤ 3/(4(2n+1))`, so at `g = 1`
`Var(v_x) ≥ σ² [1 + Σ_{n=1}^{t−1} (2√n)^{−1}]`, growing like the square root of the level.

*Proof.* The difference of two independent directed walks on `Z²` projected
to one coordinate is a lazy walk and its coincidence probability is the
central binomial term. With `a_n = C(2n,n)/4^n = Π_{k≤n}(2k−1)/(2k)`, the
sequences `4n a_n²` and `(2n+1) a_n²` are increasing and decreasing
respectively (the ratios `(2n+1)²/(4n(n+1))` and `(2n+1)(2n+3)/(2n+2)²`), with
values `1` and `3/4` at `n = 1`. ∎ Executed to `n = 400` (E1).

## Theorem T5 — additional value symmetry and the auxiliary tangent Gaussian

**(a) Value translations.** Within this supplied linear Gaussian family,
covariance under `v ↦ v+c` is equivalent to `g=1`: the mean shifts by
`3wc`, and the fixed centered noise law translates correctly exactly when
`3w=1`. This is an additional symmetry of value space, not lattice covariance.
The subcritical stable-gain range ends at `g=1`. The formal symbol has a zero
at the origin there, but zeros alone do not characterize this gain: for every
`g>1`, take `k=(0,u,−u)` with `cos u=(3/g−1)/2` to obtain
`1−(g/3)(1+2cos u)=0` as well. No massless-iff-value-covariant statement follows.

**(b) Log-density curvature.** For a smooth positive zonal overlap with
`f(1)>0`, `f'(1)>0`, let `θ,θ_i∈R²` be exponential coordinates near a common
pole. Then
`log Π_i f(s·a_i) = 3 log f(1) − κ Σ_i |θ−θ_i|² + O(3)`,
`κ=f'(1)/(2f(1))`.
The displayed quadratic log-density is maximized at the average
`θ̄=(θ_1+θ_2+θ_3)/3`, with Hessian `−6κ I`.
If, as an auxiliary construction, this quadratic expression is exponentiated
and normalized over the flat plane with Lebesgue measure, its covariance is
`(6κ)^{-1} I`. For Born overlap `f(t)=(1+t)/2`, this is `κ=1/4` and auxiliary
variance `2/3`; for `f(t)=exp(βt)`, it is `κ=β/2` and variance `1/(3β)`.

*Proof.* `s·a_i=1−|θ−θ_i|²/2+O(3)` gives the Taylor coefficient by substitution.
Completing the square gives `Σ_i|θ−θ_i|²=3|θ−θ̄|²+constant`; the negative
quadratic has its maximum at `θ̄`, and a flat Gaussian density
`exp(−3κ|θ−θ̄|²)` has the stated covariance. ∎

This is not the sphere law's fluctuation variance. The sphere area element in
these coordinates has Jacobian `sin|θ|/|θ|`; no concentration limit has been
supplied that justifies discarding it or the Taylor remainder. For three
exactly aligned Born factors at the north pole, the actual sphere density is
proportional to `(1+s_z)^3`. With `u=s_z`, its normalization integral is
`∫_{−1}^1(1+u)^3 du=4`, giving
`E[s_z]=[∫u(1+u)^3du]/4=3/5` and, by azimuthal symmetry,
`E[s_x²]=[∫(1−u²)(1+u)^3du]/8=4/15`.

**(c) Parent sign and a separate fixture.** The linked Hermitian Gaussian note
uses `P_xx=3` and real edge entry `P_xy=+1/2` on finite two-dimensional
windows with complex records. Its literal conditional coefficient is
`−P_xy/P_xx=−1/6`. Summing three such coefficients gives `−1/2` as an arithmetic
comparison; the parent itself does not supply a three-predecessor real model.
Its two-predecessor monotone rectangle sum is `−1/3`.
A separate supplied three-dimensional real precision with entries `3` and
`−1/2` has symbol `(1/2)(6−2Σcos k_j)` and conditional coefficient `+1/6`,
so its three-predecessor gain is `+1/2`. The changed sign, dimension and record
carrier are explicit changes of fixture.

**(d) A precision evaluation.** The candidate nearest-neighbor precision
`3I−Σ_{±j}S_j` has symbol `3−2Σ_j cos k_j`, equal to `−3` at zero. This exact
symbol evaluation concerns that candidate only, not a classification of all
static laws compatible with any chosen formation rule.

## No-Go Discipline Gate — broader certificate deferred

### N1 — Routes
The original route list contains unattempted and out-of-domain alternatives;
it does not establish five completed target attacks. The all-causal kernel
exclusion and exhaustive stationary-law conclusions are deferred.

### N2 — Walls
The real menu, directed order, equal positive weights, independent Gaussian
innovations and prescribed initial plane are supplied model conditions.

### N3 — Hidden premises
Value translations are additional to lattice covariance. The flat tangent
Gaussian is auxiliary; the sphere law is not identified with it.

### N4 — Source scope
Only the linked finite Hermitian Gaussian conditional algebra is used from the
parent. Its literal positive edge sign and complex carrier are retained.

### N5 — Resolution
The exact formulas, finite checks and quantitative series bounds above retain
their stated domains. They do not certify an exhaustive negative claim.

### N6 — Partial result
The propagator, overlap covariance, gain bounds, symbol and walk identities are
retained; alternative nonlinear rules and stationary constructions remain open.

### N7 — Steelman
Finite variance growth and one nonpositive candidate precision do not exclude
every probability law or every possible static construction. This is conceded.

### N8 — Recovery
All 22 original path versions, including full original proofs, two supervisor
programs and their outputs, are preserved in the
[history manifest](work_history/review_loop/pr8147/original-manifest.json).
The original branch must remain a recovery handle for unlanded conclusions.
This deferred certificate is not a passing negative-claim gate.

## Falsifiers

- A discrepancy between the finite torus covariance recursion and accumulated
  propagator overlap, or a level sum different from `g^n`.
- A directed coincidence probability outside the stated bounds for `n≥1`, or
  a finite-level variance outside its corresponding gain bound.
- A mismatch in the symbol identity, its directional Taylor coefficients,
  the return-walk count or the binomial bounds.
- A wrong log-density Hessian, aligned-sphere moment, literal parent sign or
  separately supplied precision evaluation.

## Boundaries and non-claims

This note computes the directed propagator and accumulated overlap covariance of a supplied real Gaussian recursion; no physical order, rule, gain or sphere fluctuation law is selected.
No plane, bridge, Born-weight or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
The tangent Gaussian is auxiliary; broader negative certification is deferred.

## Imports

- The current axiom memo supplies the quoted framework context, not the model's
  additional real Gaussian or value-translation assumptions.
- The linked Hermitian Gaussian predecessor supplies the finite conditional
  mean formula and triangular product algebra. Its finite complex fixture is
  not identified with the present infinite real one.
- Elementary mathematical inputs: Gaussian integration; the second-moment
  inequality (Chebyshev), quadratic-mean inequality (Cauchy–Schwarz), Fourier
  inversion for finite-step lattice walks, and mean-square completion of sums
  of independent centered Gaussian variables with summable variances. The
  finite-dimensional Gaussian limits are consistent on a countable product;
  the standard extension theorem supplies the constructed infinite field.
- The exact multinomial counts, binomial bounds, symbol identities and Taylor
  coefficients are proved above and checked by the primary at the declared
  finite ranges. Historical mutation labels denote finite sensitivity checks,
  including some forced booleans or threshold changes; they are not proofs of
  stationary-law or kernel classification.

## Historical review record
Supervisor-run block (owner directive: pull up after block 12 and find the next high-leverage science; no subagents). The control (`specs/supervisor_control_block13_causal_gaussian.py`) computed `P_n`, the variance series, the torus check, the symbol expansions, grid sums and the Taylor expansions before the contract; the lens pass is in `GOAL_block13.md`; the primary seat wrote T1–T5 and the runner; the refuting pass (`CHECKER_block13_findings.md`) recomputed the torus covariance by explicit inversion of `I − A` on the full six-level system, the coincidence probabilities from the multinomial formula instead of the walk counts, and the static return probabilities by a direct walk enumeration. Facts settled while executing: block 12's note is not on `main`, so the block is an independent PR against `main` with block 07 as its only declared parent (level time restated; blocks 09 and 12 referenced for context only); the runner checks the rational relaxation `2/n` of the note's `9π/(16n)`; a decimal string in a detail message tripped the runner's own floating-point scan and was replaced by a fraction; the yaml's quotation of the campaign's phrase contained a token the note forbids and was reworded.

## Verification

```bash
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py --exact
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py --mutation stationary_law_at_g1_claimed
```

Families: A authority and inputs; B the kernel on the torus and the level sums; C the coincidence probabilities, the variance series at two gains, the decay bounds; D the symbol, its expansions, the walk identity, the partial sums; E the binomial bounds, the Taylor expansions, literal parent sign and the separately supplied precision symbols; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. The original census reported each of the 15 mutations failing in one family; it is historical evidence, not a new execution. Expected final line: `TOTAL: PASS=23 FAIL=0`.
