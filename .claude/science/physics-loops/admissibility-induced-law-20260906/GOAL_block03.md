# Goal — block 03: the exact uniqueness region — where the rule induces exactly one static law on the cubic lattice (2026-09-06)

## Why this block

Block 02 (PR #7999) proved that an infinite-volume static law exists on `Z^3`
for the finite menu and left open whether it is unique. The owner's gate asks
what the rule induces on the infinite lattice; "an action, and one law or
several" is the honest shape of the answer. This block gives the exact
region of couplings in which the answer is "exactly one static law", by
re-proving the classical one-site contraction criterion at scope (a coupling
argument on finite windows, then the corollary on the lattice) and computing
the criterion's coefficient exactly for the covariant product rule. Outside
the region the criterion is silent: nothing is claimed about several laws.

Supervisor controls (exact; `specs/supervisor_control_block03_*`,
`specs/supervisor_control_block02_dobrushin_strip.py`): the one-neighbor
interdependence coefficient `c_1` of the covariant product rule on the
six-neighbor shell — `270/989` at `(3,1,2)` (`6c_1 = 1620/989`),
`8650000/40615109` at `(5,2,4)` (`6c_1 ≈ 1.278`), `2/13` at `(2,1,2)`
(`6c_1 = 12/13`), `2079/15566` at `(3,2,2)` (`6c_1 = 6237/7783`),
`4000000/61385721` at `(5,4,4)`, `98241110000/4544062780611` at
`(11,10,10)`; `c_1(p,q,r) = c_1(q,p,r)` on the whole grid; with the
orthogonal weight fixed at 4, `6c_1 < 1` exactly on the diamond
`{(2,4),(3,3),(3,4),(3,5),(4,2..6),(5,3..6),(6,4),(6,5)}` of `(p,q)` in
`1..12`; along the line `(t,1,1)` the crossing `6c_1 = 1` is at the second
real root of `t^7 − 2t^5 + 5t^4 − 8t^3 − t^2 − 4` (`≈ 1.60970232778585`) with
the maximizing shell pattern three `+x`, two `−x` and the flipped neighbor
`+x ↔ −x`; along `(t,t,1)` at the second real root of
`4t^7 − 8t^5 + 5t^4 − 8t^3 − t^2 − 1` (`≈ 1.47753945492135`), pattern three
`+x`, two orthogonal, flipped `+x ↔` orthogonal; along `(1,1,t)` at the
second real root of `t^7 + t^5 + 8t^4 − 5t^3 + 8t^2 − 4` (`≈ 0.676800877749306`),
same pattern. On the `3×3` planar window the finite-window comparison bound
holds with room: exact center-site total-variation sensitivity to one flipped
exterior slot `0.0090109` against the bound `1/56` at `(2,1,2)`, `0.0073929`
against `1971216/114898033` at `(3,2,2)`, `0.0016901` against
`100000000/30049760881` at `(5,4,4)` (the window's own four-neighbor
coefficients `1/8`, `1404/11431`, `10000/175641`).

## Declared objects

- Menu, rotations, orbit weights `(p, q, r)`, product rule, positivity, the
  static law of a finite window with exterior records `ω`, the specification
  and the existence of an infinite-volume static law: as in blocks 01 and 02
  (linked as upstream; definitions restated where used). Declared triples:
  the region triples `(2,1,2)`, `(3,2,2)`, `(5,4,4)`, `(11,10,10)` and the
  silent triples `(3,1,2)`, `(5,2,4)`; the constant triple as the boundary.
- A configuration `η` of the six-neighbor shell of a site `x`; the one-site
  conditional `r_x(· | η)`; for a neighbor direction `y`, the
  **interdependence coefficient**
  `C_{xy} = sup { TV(r_x(·|η), r_x(·|η')) : η, η' differ only at y }`,
  `TV = (1/2) Σ_s |·|`; for the covariant rule `C_{xy} = c_1(p,q,r)` for
  every neighbor `y` and `0` otherwise, and `α = Σ_y C_{xy} = 6 c_1`.
- A finite window `Λ` (a finite graph with declared exterior slots; the
  interior interdependence matrix `C_Λ` restricted to `Λ`); the influence
  series `D_Λ = Σ_{n≥0} C_Λ^n`, convergent when every row sum of `C_Λ` is at
  most `α_Λ < 1`; for two exterior assignments `ω, ω'` the vector
  `b_y = Σ_{z exterior, z ~ y} c_1 [ω_z ≠ ω'_z]`.
- Windows executed: the plaquette with its eight exterior slots (the
  one-step coupling inequality); the `3×3` planar window with its twelve
  exterior slots (the comparison bound by row transfer, four-neighbor
  coefficient); the `Z^3` shell (the coefficient `c_1`).

## Theorems (native proofs in the note; every finite statement executed)

**Theorem G (the coefficient, exactly).** (G1) For the covariant product
rule `C_{xy}` is the same number `c_1(p,q,r)` for all six neighbors (proper
rotations) and zero for non-neighbors (the conditional depends on the shell
only); `α = 6 c_1`. (G2) `c_1(p,q,r) = c_1(q,p,r)`: the relabeling
`s ↦ −s` of the forming site's value exchanges the parallel and antiparallel
orbits and leaves the total variation invariant. (G3) `c_1 = 0` iff
`p = q = r` (the constant rule; otherwise some one-neighbor conditional
varies). (G4, executed) the exact values at the six declared triples and at
the constant triple; the grid with `r = 4`, `p, q ∈ 1..8` (or `1..12` if it
fits) with the `6c_1 < 1` cells; the maximizing shell pattern and flipped
pair at each declared triple. (G5, executed) along each of the three lines
`(t,1,1)`, `(t,t,1)`, `(1,1,t)`: the maximizing pattern at the crossing, the
displayed rational function `6·TV(t) − 1` at that pattern (sign pattern of
the six differences fixed on the isolating interval — executed), the unique
positive root `t*` of its numerator isolated to width `10^{-20}` (Sturm), and
the exact verification at the two rational endpoints of the isolating
interval that the displayed pattern attains the supremum over all `7776 × 15`
pattern-and-pair choices and that `6c_1 − 1` changes sign across `t*`; the
threshold is stated as that root, with the sign change as the executed
content.

**Theorem H (finite-window comparison by coupling; re-proved at scope).**
Let `Λ` be a finite window with exterior assignments `ω, ω'`, and let
`μ = μ_Λ^ω`, `μ' = μ_Λ^{ω'}` be the static laws (unique with their full
conditionals, block 01 Theorem A). Suppose the row sums of `C_Λ` are at most
`α_Λ < 1`. Then there is a coupling of `μ` and `μ'` whose disagreement
probabilities `u_x = P(η_x ≠ η'_x)` satisfy `u ≤ D_Λ b` entrywise, hence for
every function `f` on `M^Λ`, `|μ(f) − μ'(f)| ≤ Σ_x δ_x(f) (D_Λ b)_x`, where
`δ_x(f)` is the oscillation of `f` in its `x` argument.
*Proof (all steps finite).* (H1, one step) Consider the random-scan
single-site update: choose `x ∈ Λ` uniformly, resample `η_x` from
`r_x(· | η, ω)`. Couple two chains (`η` with `ω`, `η'` with `ω'`) by choosing
the same `x` and using a maximal coupling of the two one-site conditionals,
which agree with probability `1 − TV`. Changing one site at a time along a
path from `(η, ω)` to `(η', ω')` and using the triangle inequality,
`TV(r_x(·|η,ω), r_x(·|η',ω')) ≤ Σ_{y∈Λ, y~x} C_{xy} [η_y ≠ η'_y] + b_x`.
Hence, writing `u_x` for the disagreement probability at `x` before the
step and `u'_x` after it, `u'_x ≤ (1 − 1/|Λ|) u_x + (1/|Λ|) ((C_Λ u)_x + b_x)`
(the site `x` is chosen with probability `1/|Λ|`, in which case the
disagreement at `x` is at most the total variation just bounded, in
expectation over the other sites' states; otherwise it is unchanged).
Executed on the plaquette with exterior records: the one-step inequality
`TV ≤ Σ C [differ] + b` for a declared family of configuration pairs and one
flipped exterior slot (exact integers), and the maximal-coupling agreement
identity `P(agree) = 1 − TV` on the same instances. (H2, the fixed point)
The map `u ↦ (1 − 1/|Λ|) u + (1/|Λ|)(C_Λ u + b)` is monotone and, from
`u^0 = 1`, its iterates decrease to the least fixed point `u* = D_Λ b`
(the Neumann series converges since `‖C_Λ‖_∞ ≤ α_Λ < 1`); executed on the
`3×3` window: `D_Λ` by exact inversion, `u*`, and the monotone iterates.
(H3, stationarity and the limit) Start both chains in their stationary laws
`μ` and `μ'` under any coupling; the coupled dynamics keeps the marginals
stationary (each chain is a Markov chain with `μ`, resp. `μ'`, invariant:
the single-site resampling preserves a law with the right full conditionals
— the static law's, by block 01 Theorem A). The disagreement vector after
`t` steps is bounded by the `t`-th iterate from `u^0 = 1`, which tends to
`u*`; the joint laws live on the finite set `M^Λ × M^Λ`, so a subsequence
converges to a coupling of `μ` and `μ'` with `u ≤ u*`. The bound on
`|μ(f) − μ'(f)|` follows by writing `f(η) − f(η')` as a telescoping sum of
single-site changes. ∎ Executed on the `3×3` window at the region triples:
the exact center-site marginals for the base exterior assignment and for one
flipped exterior slot (row transfer, integers), their total variation, and
the bound `(D_Λ b)_{center}`; the inequality holds at each triple with the
exact values above; at `(3,1,2)` the window's row sum exceeds one and the
window bound is not asserted (recorded, not used).

**Theorem I (uniqueness on the lattice in the region; corollary).** If
`α = 6 c_1 < 1` then the specification of the covariant product rule on
`Z^3` has exactly one infinite-volume static law. *Proof.* Let `μ, ν` be two
static laws (Gibbs measures for the specification; block 02 Theorem C2
gives at least one). For a local `f` with support in a box and the box `Λ_L`
of side `2L + 1` around it, the conditional identity of block 02 (C1 in the
limit) gives `μ(f) = ∫ μ_{Λ_L}^{ω}(f) μ(dω)` and likewise for `ν`, so
`|μ(f) − ν(f)| ≤ sup_{ω, ω'} |μ_{Λ_L}^ω(f) − μ_{Λ_L}^{ω'}(f)|`. By Theorem H
with `b_y ≤ 6 c_1 [y adjacent to the exterior]`, this is at most
`Σ_{x ∈ supp f} δ_x(f) Σ_{y ∈ ∂_in Λ_L} (D_Λ)_{xy} · 6c_1`. Since
`(C_Λ^n)_{xy} ≤ c_1^n N_n(x, y)` with `N_n` the number of nearest-neighbor
paths of length `n` from `x` to `y` inside `Λ`, and `Σ_y N_n(x,y) ≤ 6^n`,
`Σ_{y ∈ ∂_in Λ_L} (D_Λ)_{xy} ≤ Σ_{n ≥ L − ℓ} (6 c_1)^n = α^{L−ℓ}/(1 − α)`
(`ℓ` the radius of the support of `f`), which tends to zero as `L → ∞` when
`α < 1`. Hence `μ(f) = ν(f)` for every local `f`, and `μ = ν`. ∎ Executed:
the path-count bound's arithmetic `α^L/(1 − α)` as exact rationals for
`L = 1..12` at the region triples (a table), and the exact identity
`Σ_y N_n(x,y) = 6^n` on `Z^3` for `n ≤ 4` by enumeration.

**The region, stated.** For the covariant product rule at
`(2,1,2)`, `(3,2,2)`, `(5,4,4)`, `(11,10,10)` the rule induces exactly one
static law on `Z^3`; on the line `(t,1,1)` for every rational `t` strictly
between `1` and the isolating interval's lower endpoint of `t*`, and
likewise on the other two lines (executed at a declared list of rational
points on each line, each with its own exact `c_1`). At `(3,1,2)` and
`(5,2,4)` the criterion is silent: no statement about one law or several.

## Named readings and premises (carried; nothing new adopted)

Records-only reading (it enters only through blocks 01–02's definitions,
not this block's theorems, which concern the static laws); positivity; the
extensional reading of the variation clause restricted to the declared menu.
No formation order enters this block.

## Quantifiers / domain

Theorem G executed at the declared triples, grid and lines; G1–G3 proved.
Theorem H proved for every finite window; executed on the plaquette and the
`3×3` planar window. Theorem I proved on `Z^3` for `α < 1`; executed as
arithmetic. No statement about the silent triples beyond "silent"; no
statement about several static laws anywhere; no sharper criterion
attempted (named as leads: the two-site Dobrushin–Shlosman condition,
disagreement percolation); no formation law; no plane; no bridge, Born or
gravity statement; this block does not fire wake condition 1 of
`docs/repo/DEFERRED_DECISIONS.md` entry 1.

## Forbidden

Floating point anywhere in the runner; "non-unique", "phase transition",
"several static laws" as claims; "the physical rule"; any uniqueness claim
at the silent triples; any claim that the silent triples are outside every
criterion; "certified", "closed", "complete", "global", "the law" outside
their exact meaning; naming the criterion after its author in a claim
sentence (the author's name may appear once in the prior-art line as a
reference re-proved here).

## Value gate (supervisor, in advance)

V1: the owner's infinite-lattice gate ("one law or several") and block 02's
named next target; consumers: the parked bridge decision material (not
fired), the gravity lane's action question (the static law is unique in the
region — the object the lane's Gaussian analogy would need). V2: new — the
exact coefficient of the covariant rule, the exact region and thresholds,
the coupling re-proof of the finite-window comparison bound executed on
exact windows, the corollary on the lattice; sweep recorded in
`ROUTE_PORTFOLIO.md` (block 03). V3: the criterion is classical (referenced
and re-proved); its coefficient for this menu, the maximizing patterns and
the exact thresholds are framework computations the audit lane does not
have; the only in-repo use of the criterion (`WILSON_STAGGERED_*`,
2026-07-12) is on a different carrier and quotes the theorem as authority.
V4: non-trivial — the region is an exact algebraic object; the thresholds
are degree-7 algebraic numbers with the maximizing patterns identified.
V5: not a variant of blocks 01–02 (existence and formation) or of anything
landed.
