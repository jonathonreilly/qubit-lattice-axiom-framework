---
claim_id: equal_radius_lock_tick_lipschitz_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "For equal-radius ℓ¹ ball unions, whether lock-ticks can shrink Stab at an unread site is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/equal_radius_lock_tick_lipschitz_2026_08_15.py
---

# Equal-Radius Lock-Ticks Do Not Shrink Occupancy Stab (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** finite unions `U = ∪_i B_r(s_i)` of equal-radius ℓ¹ balls, one
radius `r ≥ 1`, finite nonempty seed list. Lock tick
`t(x) = min_i ‖x − s_i‖_1`. Score the identity only: unread `v ∉ U` and
occupied nearest neighbors `w ∈ U`. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/equal_radius_lock_tick_lipschitz_2026_08_15.py`](../scripts/equal_radius_lock_tick_lipschitz_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment tickhost scored one `r = 2` box: unread `v` has `t(v) ≥ 3` and
every occupied neighbor has `t = 2`, by 1-Lipschitz of ℓ¹. That is one box.
The residual here is not leftover of tickhost (one box). The same identity
holds for every union of equal-radius ℓ¹ balls, any `r ≥ 1`. Lock-ticks
then never shrink `Stab` at a formation site of such a `U`.

`B_r(s) = { x ∈ Z^3 : ‖x − s‖_1 ≤ r }`. For a finite nonempty list of
seeds `s_i` and one common radius `r ≥ 1`,

`U = ∪_i B_r(s_i)`, `t(x) = min_i ‖x − s_i‖_1`.

Empty slots have no tick. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy `σ` is the 0-1 mask of nearest neighbors of an unread site `v`
that lie in `U`. Local data are `(σ, t)`. `G+` is the 24 proper cube
rotations acting on the six slots.

`Stab(σ) = { g in G+ : g · σ = σ }`,

`Stab(σ,t) = { g in G+ : g · σ = σ and t(g · μ) = t(μ) on occupied slots }`.

`N_stab_ok` counts July-3 `k = 3` pair members with support `σ` that are
invariant under `Stab(σ)`. `N_tick_ok` counts those invariant under
`Stab(σ,t)`.

**Theorem 1.** `t` is 1-Lipschitz. `v ∉ U` implies `t(v) ≥ r+1`.
`w ∈ U` implies `t(w) ≤ r`. Hence `t(w) = r` on every occupied neighbor.

**Theorem 2.** `Stab(σ,t) = Stab(σ)` at every unread star of an
equal-radius union. `N_tick_ok = N_stab_ok`, which is `0` on every
weight-4 mask (maskstab).

**Theorem 3.** Displayed, not adopted. Do not write the identity into
Admissibility. Do not attach L1. Do not add a 4th ball. Qubit remains
`M_2(C)`. No axiom edit.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither `Stab(σ,t)` nor the equal-radius lock-tick
identity as the framework's fixed rule. The covariance clause is the reason
a local labeling on the orbit of `(σ, t)` must be stabilizer-invariant.
Formation site and rate remain outside the axiom memo. Qubit remains
`M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact 1-Lipschitz identity for t on any finite equal-radius ℓ¹ union: occupied unread neighbors carry t=r, so Stab(σ,t)=Stab(σ) and N_tick_ok=N_stab_ok. On every weight-4 mask, N_stab_ok=0. Displayed identity only."
trace_class: frontier_discovery
target_claim_id: equal_radius_lock_tick_lipschitz
target_blocker_text: "the same identity for every union of equal-radius ℓ¹ balls, any r≥1; then lock-ticks never shrink Stab at a formation site of such a U"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the 1-Lipschitz identity, t(w)=r on occupied unread neighbors, Stab(σ,t)=Stab(σ), and N_tick_ok=N_stab_ok=0 on weight-4 masks; do not write the identity into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on every finite equal-radius union, any r≥1; Stab never shrinks; N_tick_ok=0 on every weight-4 unread star; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }` for an integer `r ≥ 1`. A
scored union is any finite nonempty seed list with one common radius:

`U = ∪_i B_r(s_i)`, `t(x) = min_i ‖x − s_i‖_1`.

Membership is the sublevel set `U = { x : t(x) ≤ r }`. An unread site is
any `v ∉ U`. Occupancy `σ` is the six-bit nearest-neighbor indicator of
`U` at `v`, in the declared slot order. Weight `wt(σ)` is the number of
`1`s. On an occupied neighbor `w` of `v`,

`t(w) = min_i ‖w − s_i‖_1`.

Empty slots have no tick. Letters of the July-3 `k = 3` pair are
`{0, +, −}` with `0` empty. The pair is the unique pair of proper-cubic
orbits of handed fully-mixed 6-tuples. It has 48 members. Support of a
coloring is the 0-1 mask of nonzero letters.

`G+` is the 24 determinant-`+1` signed permutation matrices of the three
axes, acting on the six axis directions. The two stabilizers and the two
counts `N_stab_ok`, `N_tick_ok` are as named above.

The identity is scored for every finite equal-radius union. It is not a
census of one `r = 2` three-ball box. No 4th ball is added as a new
scored family.

## Theorem 1 — `t` is 1-Lipschitz; occupied unread ticks equal `r`

ℓ¹ distance on `Z^3` is a metric, so for every seed

`‖x − s_i‖_1 ≤ ‖x − y‖_1 + ‖y − s_i‖_1`.

The right-hand side at a seed attaining `t(y)` is `‖x − y‖_1 + t(y)`,
and the left-hand side is at least `t(x)`. Therefore

`t(x) ≤ t(y) + ‖x − y‖_1`.

The symmetric bound holds with `x` and `y` swapped, so

`|t(x) − t(y)| ≤ ‖x − y‖_1`.

That is the 1-Lipschitz identity.

If `v ∉ U` then `t(v) > r`. Distances are integers, so `t(v) ≥ r+1`.
If `w ∈ U` then `t(w) ≤ r`. If `w` is a nearest neighbor of `v` then
`‖w − v‖_1 = 1`, and 1-Lipschitz gives

`t(w) ≥ t(v) − 1 ≥ r`.

Combined with `t(w) ≤ r`,

`t(w) = r`

on every occupied neighbor of every unread site of every equal-radius
union. The common value is the shared radius. This is not leftover of
tickhost (one box), where the same bound was `t(w) = 2` for `r = 2`.

## Theorem 2 — lock-ticks do not shrink `Stab`

On an unread star the occupied tick tuple is the constant-`r` function
of `σ`. Empty slots have no tick. Any `g` that preserves `σ` maps
occupied slots to occupied slots and therefore preserves the constant
tick tuple. Hence

`Stab(σ,t) = Stab(σ)`

at every unread star of an equal-radius union, of every weight. In
particular `|Stab(σ,t)| < |Stab(σ)|` never holds, so lock-ticks never
shrink occupancy `Stab` at a formation site of such a `U`.

The invariance group used by `N_tick_ok` is therefore the same as the
group used by `N_stab_ok`:

`N_tick_ok = N_stab_ok`.

The July-3 pair has 48 members. Among the 15 occupancy masks of weight
4, every mask has `N_stab_ok = 0` (maskstab). Therefore every weight-4
unread star of an equal-radius union has

`N_tick_ok = 0`.

No NN-determined pair member that is invariant under the occupancy
stabilizer, nor under the lock-tick stabilizer, exists on any 4-occupied
unread star of an equal-radius union.

## Theorem 3 — displayed, not adopted

The 1-Lipschitz identity, the constant-`r` occupied ticks, the equality
`Stab(σ,t) = Stab(σ)`, and the counts `N_tick_ok = N_stab_ok = 0` on
weight-4 masks are displayed member data. They are not the framework's
fixed Admissibility rule. This note does not write the identity into
Admissibility. Do not write the identity into Admissibility. Do not
attach L1. Do not add a 4th ball. Occupancy-only formation is not
attached. Qubit remains `M_2(C)`. No approved primitive is added. No
axiom edit.

## Honest-auditor / Boundary

- **What is proved.** For every finite equal-radius ℓ¹ union and every
  `r ≥ 1`, `t` is 1-Lipschitz, every occupied unread neighbor has
  `t(w) = r`, and `Stab(σ,t) = Stab(σ)`. Then
  `N_tick_ok = N_stab_ok`. On every weight-4 mask, that common count is
  `0`.
- **What is displayed only.** The identity and the two stabilizer
  counts are one rival table. They are not adopted.
- **What is not claimed.** No writing of the identity into
  Admissibility; no attachment of L1; no attachment of occupancy-only
  formation; no axiom edit; no formation rate; no lattice-wide
  dynamics; no fourth equal-radius ball; no leftover of tickhost (one
  box); no compiler no-go.
- **Mutation controls.** A rebuilt pair of sites with
  `|t(x) − t(y)| > ‖x − y‖_1` fails. An occupied unread neighbor with
  tick other than `r` fails. A weight-4 mask with `N_stab_ok ≠ 0`
  fails. A note that writes the identity into Admissibility, attaches
  L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `t` on finite equal-radius unions, the
1-Lipschitz identity, the unread floor `t(v) ≥ r+1`, the occupied
identity `t(w) = r`, the 24 proper cube rotations, `Stab(σ)` and
`Stab(σ,t)` on unread stars, the 48-member July-3 pair, `N_stab_ok` on
the 15 weight-4 masks, `N_tick_ok = N_stab_ok`, the current premise
boundary, and the mutation controls. It writes no cache and authors no
audit verdict.
