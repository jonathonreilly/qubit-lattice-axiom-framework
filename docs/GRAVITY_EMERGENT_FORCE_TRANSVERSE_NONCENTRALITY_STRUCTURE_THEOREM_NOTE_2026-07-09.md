# The Emergent Force Is Not Central: Exact Transverse Structure at O(1/r⁴) and the Three Central Orbits

**Date:** 2026-07-09
**Claim type:** theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_gravity_transverse_noncentrality_structure.py`](../scripts/frontier_gravity_transverse_noncentrality_structure.py)
**Cached output:** [`logs/runner-cache/frontier_gravity_transverse_noncentrality_structure.txt`](../logs/runner-cache/frontier_gravity_transverse_noncentrality_structure.txt)

## Claim

> **`−∇G = [1/(4π r²) + (15/(32π))·K₄(n̂)/r⁴]·n̂ − (5/(8π))·(n̂³ − S₄ n̂)/r⁴ + O(1/r⁶)`**

The second correction term is exactly tangent to the sphere, so the emergent force is
not central in a generic direction. It is asymptotically central precisely on the three
cubic orbits `⟨100⟩`, `⟨110⟩`, and `⟨111⟩`, the stationary orbits of `S₄`. Its transverse
magnitude is `(5/(8π))·√(S₆ − S₄²)/r⁴`, and relative to the Newtonian radial term it is
at most `(5/2)·q_max/r²`, where `q²_max = (827 + 73√73)/18432` and the exact minimal
polynomial is `9216·Q² − 827·Q + 8`.

## Setting and dependencies

The input expansion comes from the leading-correction theorem
[`GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07`](GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md),
which supplies `G(r) = 1/(4π r) + [5/(32π)]·K₄(n̂)/r³ + O(1/r⁵)`. This note is pure
structure downstream of that expansion: exact gradient algebra plus an independent
numeric certification of the remainder order against the exact Bessel-resolvent Green
function. No new physical identification is introduced. “Force” means `−∇` of the same
emergent potential named in that theorem.

Write `r = |x|`, `n̂ = x/r`, `S₄ = Σ_μ n̂_μ⁴`, `S₆ = Σ_μ n̂_μ⁶`,
`K₄ = S₄ − 3/5`, and `n̂³ = (n̂_x³,n̂_y³,n̂_z³)` componentwise. Define
`t(n̂) = n̂³ − S₄n̂` and `q²(n̂) = S₆ − S₄²`.

## Theorem

- **T1 — gradient and remainder.** Exact differentiation of the supplied asymptotic form gives
  `∇[1/(4πr) + (5/(32π))K₄/r³]`
  `= −[1/(4πr²) + (15/(32π))K₄/r⁴]n̂ + (5/(8π))t/r⁴`.
  Consequently the displayed force formula holds with remainder `O(1/r⁶)`. The
  `O(1/r⁵)` potential term first contributes to its gradient at `O(1/r⁶)`.

- **T2 — exact tangency and magnitude.** The identities
  `n̂·t = n̂·n̂³ − S₄ = 0` and `t_μ = n̂_μ(n̂_μ² − S₄)` hold componentwise.
  For the degree-zero homogeneous extension of `S₄`, `∇S₄ = 4t/r`, equivalently
  `t = (1/4)∇_tan S₄`. Moreover, `|t|² = S₆ − S₄² = q²(n̂)` exactly.

- **T3 — centrality classification.** `t = 0` if and only if every nonzero component
  obeys `n̂_μ² = S₄`. The unit-norm condition then makes the `k` nonzero components
  equal in magnitude, with `S₄ = 1/k` for `k = 1,2,3`. Thus the zero set is exactly
  `⟨100⟩ ∪ ⟨110⟩ ∪ ⟨111⟩`, with `S₄ = 1,1/2,1/3`, respectively.

- **T4 — stationary-orbit signatures.** These three orbits are precisely the stationary
  orbits of `S₄` on the unit sphere. Its tangent-plane Hessian has eigenvalues
  `{-4,-4}` at `⟨100⟩` (maximum), `{-2,+4}` at `⟨110⟩` (saddle), and
  `{+8/3,+8/3}` at `⟨111⟩` (minimum). The equal eigenvalues at the first and third
  orbits are forced by their `C₄` and `C₃` stabilizers.

- **T5 — all-orders centrality on the three orbits.** The asymptotic gradient field is
  equivariant under proper cubic rotations. At a fixed direction, any transverse term
  must be a fixed vector of the stabilizer's tangent-plane action. The generators act
  by rotation through `π/2` at `⟨100⟩`, `π` at `⟨110⟩`, and `2π/3` at `⟨111⟩`;
  none has tangent-plane eigenvalue `1`. Every transverse term therefore vanishes there
  at every asymptotic order. Conversely, T3 gives a nonzero `O(1/r⁴)` transverse term
  in every other direction. The field is asymptotically central precisely on ⟨100⟩ ∪ ⟨110⟩ ∪ ⟨111⟩.

- **T6 — transverse-to-radial ratio.** Dividing the leading transverse magnitude by
  `1/(4πr²)` gives
  `|transverse|/|radial| = (5/2)·q(n̂)/r² + O(1/r⁴)`.

- **T7 — extremal anisotropy.** Stationarity of `q²` on the sphere is equivalent to
  `n̂_μ(6n̂_μ⁴ − 8S₄n̂_μ² − 6S₆ + 8S₄²) = 0` for every `μ`. The bracketed factor is
  quadratic in `n̂_μ²`, so at a stationary direction the nonzero components take at most
  two distinct squared values; up to permutation and sign, every stationary direction
  therefore lies in the planar family `n̂² = (v,1−v,0)` or the family
  `n̂² = (u,u,1−2u)`. On the family
  `n̂² = (u,u,1−2u)`,
  `q²(u) = 2u³ + (1−2u)³ − [2u² + (1−2u)²]²` is maximized at
  `u* = (13−√73)/48`. The global value is
  `q²_max = (827 + 73√73)/18432 ≈ 0.0787061780`, and it obeys
  `9216·Q² − 827·Q + 8 = 0`. The planar family has maximum `q² = 1/16` at
  `n̂_x² = cos²(π/8)`, strictly below the global value. Hence the largest ratio
  coefficient is `(5/2)q_max ≈ 0.70136553`. The lattice direction `(1,1,3)` has
  `q² = 1152/14641 ≈ 0.0786832`, within `0.05%` of the global maximum.

## Why the transverse term is the tangential gradient of S₄

At this order the angular dependence enters through `S₄` alone. The derivative of
`K₄/r³` therefore separates into a radial derivative and a sphere-tangential derivative.
Projection onto the tangent plane gives the one-line identity
`∇_tan S₄/4 = (n̂³ − S₄n̂) = t`.
Thus the transverse component of `∇G` is parallel to the tangential gradient of `S₄`.
Its gradient-field lines bend along the `S₄` gradient flow on the sphere, whose fixed
points are the three orbits in T3 and whose local signatures are those in T4.

## Numeric certification (runner)

The `S1–S8` gates use exact SymPy algebra for the gradient, tangency, component factors,
magnitude, classification, tangent Hessians, constrained stationarity, extrema, exact
anchors, pair-response contrast, and stabilizer fixed-vector determinants. The runner
does not infer any coefficient from numerical data. A deterministic simplex-grid scan
over squared directions additionally certifies that no direction exceeds the
two-equal-squares family maximum, at grid resolution `1/240`.

The `N1–N5` gates evaluate the exact lattice Green function at `mp.dps = 24` using
`G(x) = ∫₀^∞ e^{−6t} Π_μ I_{x_μ}(2t) dt`. They use the six lattice sites
`(3,3,9)`, `(5,5,15)`, `(8,4,0)`, `(14,7,0)`, `(8,4,4)`, and `(12,6,6)`.
The five-point stencil
`D_ν = [−G(x+2e_ν)+8G(x+e_ν)−8G(x−e_ν)+G(x−2e_ν)]/12`
has truncation `O(∂⁵G) = O(1/r⁶)`; the three-point stencil is insufficient because its
`O(1/r⁴)` truncation is the same order as the transverse term.

For each site the runner computes `ρ_num = n̂·D`, `t_num = D−ρ_num n̂`, and the radial
and transverse predictions directly. The observed scaled transverse and radial residuals
are bounded by the gates, the three direction pairs show the required relative
`O(1/r²)` convergence, all six sites witness non-centrality, and the two largest-radius
sites reproduce the ratio in T6 within `15%`. The exact direction anchors are
`q²(1,1,3)=1152/14641`, `q²(2,1,0)=36/625`, `q²(2,1,1)=1/18`, and `q²=0` on
`⟨100⟩`, `⟨110⟩`, and `⟨111⟩`.

The `CTRL1–CTRL4` gates require rejection of a `10%`-inflated transverse coefficient,
the nontangent substitution of `S₆` for `S₄`, the wrong minimal-polynomial coefficient
`826`, and the wrong gradient coefficient `3/8`. These controls reuse the computed
quantities and add no fitted parameter.

## Conditional corollary (bounded bridge)

Conditional on the weak-field source-response bridge
[`GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11`](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md),
which converts `G` into a static pair response, two equal-source pairs at equal separation
`r` along `⟨100⟩` and `⟨111⟩` differ in response magnitude by
`(5/(32π))[K₄(⟨100⟩)−K₄(⟨111⟩)]/r³ = 5/(48π r³)` per unit coupling, since
`K₄(⟨100⟩)=2/5`, `K₄(⟨110⟩)=−1/10`, and `K₄(⟨111⟩)=−4/15`. The equilibrium
orientations of the induced torque, where the `O(1/r⁴)` transverse component vanishes,
are exactly the three orbits of T3. This corollary is conditional on the bridge; the main
theorem does not depend on it. Which response extremum is energetically preferred depends
on the bridge's coupling-sign convention and is not assigned here.

## Boundary / honest auditor read

- The theorem gives the exact asymptotic structure of the supplied expansion together
  with numerical certification of the remainder order; it does not derive new dynamics.
- The `O(1/r⁶)` remainder is certified on six sites in three directions with `r ≤ 16.6`,
  rather than proven symbolically here.
- The conditional corollary inherits the bounded status of its cited bridge.
- T5 is a symmetry theorem about the asymptotic series of an `O_h`-equivariant field,
  certified by the stabilizer fixed-vector check.
- The next natural step is the transverse structure at the next order: the `l=4,6,8`
  content of the `O(1/r⁶)` transverse term.

## Files

- Source: this theorem note.
- Executable runner: `scripts/frontier_gravity_transverse_noncentrality_structure.py`.
- Reviewer cache target: `logs/runner-cache/frontier_gravity_transverse_noncentrality_structure.txt`.
