---
claim_id: skew_three_seed_lock_tick_pair_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the off-axis three-ball union at unread v=(-1,1,1), how many lock-tick-invariant July-3 pair members fire is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/skew_three_seed_lock_tick_pair_fire_2026_08_15.py
---

# Lock-Tick-Invariant July-3 Pair Fire On The Off-Axis Three-Seed Star (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the locked union
`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))` and the unread six-neighbor
star at `v = (−1,1,1)`. Rebuild the July-3 pair members whose support
equals the occupancy of this star and that are invariant under
`Stab(σ, t)`, then count how many fire at `v`. Score `U` and the star
at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/skew_three_seed_lock_tick_pair_fire_2026_08_15.py`](../scripts/skew_three_seed_lock_tick_pair_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment ticklab names `N_tick_ok` pair members that are invariant
under `Stab(σ, t)` on this star. Investment orbfire counts fire among
occupancy-`Stab(σ)` members. Investment delrun executes one product
tuple. The residual here is not leftover of orbfire (occupancy Stab)
and not leftover of delrun (one product tuple). It is the *run* of
every lock-tick-invariant pair member at unread `v`: how many form
exactly `v` (`N_new = 1`) with `U` persisting.

Treat `U` as already locked. The site `v = (−1,1,1)` is unread.
Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy mask

`σ = (1, 0, 1, 1, 0, 1)`.

Occupied nearest neighbors receive the lock tick

`t(w) = min{ |w|_1, |w − (2,0,0)|_1, |w − (1,2,1)|_1 }`.

Empty slots have no tick. Local data is `(σ, t)`. `G+` is the 24
proper cube rotations acting on slots.

`Stab(σ, t) = { g ∈ G+ : g · σ = σ and t(g · μ) = t(μ) on occupied slots }`.

The July-3 unique `k = 3` chiral pair is reconstructed as the two
proper-cubic orbits of handed fully-mixed 6-tuples. It has 48 members.
Support of a 6-tuple is the slots with a nonzero letter.

`S` is the set of pair members `c` with `support(c) = σ` and
`g · c = c` for every `g ∈ Stab(σ, t)`. Rebuild gives

`|S| = 0`

and there is no lex-first member. Four pair members share this
support; none is fixed by the nontrivial lock-tick stabilizer
element. Therefore `N_tick_ok = 0` and

`N_fire = 0`.

Displayed, not adopted. Do not write a firing c into Admissibility.
Do not attach L1. Do not add a 4th ball. Occupancy-only formation
(the `n ≠ 0` gate) is not attached. Qubit remains `M_2(C)`. No
axiom edit.

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

Admissibility names neither a firing 6-tuple, a lock tick, nor the
July-3 pair as the framework's fixed rule. Record permanence is used
only to keep the locks on `U`. Formation site and rate remain outside
the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one unread six-neighbor star, reconstruction of the July-3 k=3 pair, and an exact Stab(σ,t)-invariance fire census. Displayed census only."
trace_class: frontier_discovery
target_claim_id: skew_three_seed_lock_tick_pair_fire
target_blocker_text: "on the off-axis three-ball union at unread v=(-1,1,1), how many lock-tick-invariant July-3 pair members fire"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of |S| and N_fire; do not write a firing c into Admissibility, attach L1, or add a 4th ball"
conditional_surface_status: "exact on U=B_2(0)∪B_2((2,0,0))∪B_2((1,2,1)) at unread v=(-1,1,1); |S|=0 and N_fire=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0 = (0,0,0)`, `p = (2,0,0)`, and `q = (1,2,1)`. The closed ℓ¹
ball of radius two is

`B_2(c) = { x ∈ Z^3 : |x − c|_1 ≤ 2 }`.

The locked set is the already-given union

`U = B_2(0) ∪ B_2((2,0,0)) ∪ B_2((1,2,1))`.

The three balls each have 25 sites. Pairwise overlaps are 7, 4, and 4,
and the triple overlap has 2 sites, so `|U| = 62`. The unread site is

`v = (−1,1,1)`.

Then `|v|_1 = 3`, `|v − p|_1 = 5`, and `|v − q|_1 = 3`, so `v ∉ U`.

The six nearest neighbors, in the declared order, are

| slot | neighbor | in `U` | lock tick |
|---|---|---|---|
| `+x` | `(0,1,1)` | yes | `2` |
| `−x` | `(−2,1,1)` | no | none |
| `+y` | `(−1,2,1)` | yes | `2` |
| `−y` | `(−1,0,1)` | yes | `2` |
| `+z` | `(−1,1,2)` | no | none |
| `−z` | `(−1,1,0)` | yes | `2` |

Occupancy mask at `v`:

`σ = (1, 0, 1, 1, 0, 1)`.

On the four occupied slots the lock-tick list is

`t(+x) = t(+y) = t(−y) = t(−z) = 2`.

Empty slots have no tick. Letters are `{0, +, −}` with `0` empty.
Encode `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`. The July-3 `k = 3` pair is the
unique pair of proper-cube orbits of 3-letter 6-tuples that are not
proper-equivalent to their inversion images. That set has 48 members.
A displayed pair step at an unread site forms that site if and only
if the encoded 6-tuple lies in the pair; existing locks are not
removed.

`G+` is the 24 determinant-`+1` signed permutation matrices of the
three axes, acting on the six axis directions. Spatial inversion
`P = −I` exchanges `+μ` with `−μ`. Support of a coloring is the
0-1 mask of nonzero letters. Occupancy stabilizer `Stab(σ)` is
`{ g ∈ G+ : g · σ = σ }`. Lock-tick stabilizer `Stab(σ, t)` further
requires `t(g · μ) = t(μ)` on occupied slots. `S` is the subset of
the 48-member pair whose support equals `σ` and that are pointwise
fixed by every element of `Stab(σ, t)`. Those are the lock-tick
invariant pair members on this star. `N_tick_ok = |S|`. `N_fire`
is the number of `c ∈ S` for which the displayed step forms exactly
`v` (`N_new = 1`) while every site of `U` remains locked. If
`|S| = 0` then `N_fire = 0`.

Only `U` and the star at `v` are scored.

## Theorem 1 — Rebuild `S`

`G+` has order 24. Occupancy `Stab(σ)` has order 2. A generating
list is the identity and the proper rotation

`R : (x, y, z) ↦ (−z, −y, −x)`,

which acts on slots by

`(+x, −x, +y, −y, +z, −z) ↦ (−z, +z, −y, +y, −x, +x)`.

The four occupied ticks are all `2`. The image under `R` of those
occupied slots is `{−z, −y, +y, +x}`, the same occupied set, and
each image slot also has tick `2`. Therefore `R` survives
`Stab(σ, t)`, and

`|Stab(σ, t)| = 2`.

Lock-ticks do not shrink the occupancy stabilizer on this star.

Four pair members have support equal to `σ`:

`(+ ,0, +, −, 0, −)`,
`(+ ,0, −, +, 0, −)`,
`(− ,0, +, −, 0, +)`,
`(− ,0, −, +, 0, +)`.

Every July-3 pair member bi-colors every axis. The only fully
occupied axis on this star is the `y`-axis, so each of those four
members has distinct letters on `+y` and `−y`. The nontrivial
lock-tick stabilizer element exchanges `+y` with `−y`, so it moves
every same-support pair member. Therefore none is
`Stab(σ, t)`-invariant.

Rebuilding `S` by direct enumeration of the 48-member pair against
the two-element lock-tick stabilizer gives

`|S| = 0`.

There is no lex-first member. Hence `N_tick_ok = 0`.

This is not leftover of orbfire (occupancy Stab): the present
objects are the fire count on lock-tick-invariant members, not the
occupancy-only stabilizer fire census. It is not leftover of
delrun (one product tuple): no single product 6-tuple is executed
in isolation.

## Theorem 2 — Fire count

If `|S| = 0`, then `N_fire = 0` by the empty count: no
lock-tick-invariant member is present to form `v`. The displayed
pair step is not run on a nonexistent member. `U` persists because
no lock is added or removed. The center `v` remains unread.

Because `N_tick_ok = 0`, report `N_fire = 0`.

## Theorem 3 — Displayed, not adopted

The set `S` and the count `N_fire` are displayed member data. They
are not the framework's fixed Admissibility rule. This note does not
write a firing c into Admissibility. Do not write a firing c into
Admissibility. Do not write ticks into Admissibility. Do not attach
L1. Do not add a 4th ball. Occupancy-only formation (the `n ≠ 0`
gate) is not attached. Qubit remains `M_2(C)`. No approved
primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On this unread star the four occupied lock
  ticks are all `2`, `|Stab(σ, t)| = 2`, four July-3 pair members
  share the occupancy support, none is lock-tick-invariant,
  `|S| = 0`, `N_tick_ok = 0`, and `N_fire = 0`.
- **What is displayed only.** The pair, the lock-tick stabilizer,
  and the fire count are one rival table. They are not adopted.
- **What is not claimed.** No attachment of a firing 6-tuple to
  Admissibility; no writing of ticks into Admissibility; no
  attachment of occupancy-only formation; no axiom edit; no
  formation rate; no lattice-wide dynamics; no fourth equal-radius
  ball; no re-execution of the delrun product tuple; no restatement
  of the orbfire occupancy-Stab fire census as an adopted law.
- **Mutation controls.** A rebuilt `|S|` other than the runner's
  enumeration fails. A claimed fire from an empty `S` fails. A note
  that writes a firing c into Admissibility, attaches L1, or authors
  an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, occupancy `σ`,
lock ticks `t`, `G+`, `Stab(σ, t)`, the 48-member July-3 pair, `S`,
`N_fire`, the current premise boundary, and the mutation controls.
It writes no cache and authors no audit verdict.
