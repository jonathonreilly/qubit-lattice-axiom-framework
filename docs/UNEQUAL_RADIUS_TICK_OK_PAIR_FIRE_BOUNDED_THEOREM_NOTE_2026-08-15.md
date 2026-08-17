---
claim_id: unequal_radius_tick_ok_pair_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the lex-first unequal-radius 3-ball breaker at v=(-3,-3,-1), how many tick-invariant July-3 pair members fire is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_tick_ok_pair_fire_2026_08_15.py
---

# Unequal-Radius Tick-Ok July-3 Pair Fire (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the locked unequal-radius union
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` and the unread
six-neighbor star at `v = (−3,−3,−1)`. Rebuild the July-3 pair members
whose support equals the occupancy of this star and that are invariant
under `Stab(σ,t)`, then count how many fire at `v`. Score `U` and the
star at `v` only. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_tick_ok_pair_fire_2026_08_15.py`](../scripts/unequal_radius_tick_ok_pair_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqrad is a census: it names the lex-first unequal-radius
breaker and reports `N_tick_ok = 4`. Investment tickfire is the equal r
lock-tick fire census on a different host. The residual here is not
leftover of uneqrad (census) and not leftover of tickfire (equal r). It
is the *run* of every tick-invariant pair member at unread `v`: how many
form exactly `v` (`N_new = 1`) with `U` persisting.

Treat `U` as already locked. The site `v = (−3,−3,−1)` is unread.
Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy mask

`σ = (1, 0, 1, 0, 1, 1)`.

Occupied nearest neighbors receive the lock tick

`t(w) = min_i ‖w − si‖_1`.

Empty slots have no tick. Local data is `(σ, t)`. `G+` is the 24
proper cube rotations acting on slots.

`Stab(σ,t) = { g ∈ G+ : g · σ = σ and t(g · μ) = t(μ) on occupied slots }`.

The July-3 unique `k = 3` chiral pair is reconstructed as the two
proper-cubic orbits of handed fully-mixed 6-tuples. It has 48 members.
Support of a 6-tuple is the slots with a nonzero letter.

`S` is the set of pair members `c` with `support(c) = σ` and
`g · c = c` for every `g ∈ Stab(σ,t)`. Rebuild gives

`|S| = 4`

and the lex-first member is `(+,0,−,0,+,−)`. Because `|Stab(σ,t)| = 1`,
every same-support pair member is tick-invariant, so `N_tick_ok = 4`.
Each of those four members lies in the pair, the center is unread, and
the displayed step forms exactly `v` with `U` persisting. Therefore

`N_fire = 4`.

Displayed, not adopted. Do not write a firing c into Admissibility. Do
not write a firing c or the radii into Admissibility. Do not write
radii into Admissibility. Do not attach L1. Occupancy-only formation
(the `n ≠ 0` gate) is not attached. Qubit remains `M_2(C)`. No axiom
edit.

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

Admissibility names neither a firing 6-tuple, the radii `(2, 1, 3)`,
nor the July-3 pair as the framework's fixed rule. Record permanence is
used only to keep the locks on `U`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact ℓ¹ geometry on one unread six-neighbor star, reconstruction of the July-3 k=3 pair, and an exact Stab(σ,t)-invariance fire census. Displayed census only."
trace_class: frontier_discovery
target_claim_id: unequal_radius_tick_ok_pair_fire
target_blocker_text: "on the lex-first unequal-radius 3-ball breaker at v=(-3,-3,-1), how many tick-invariant July-3 pair members fire"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of |S| and N_fire; do not write a firing c or the radii into Admissibility or attach L1"
conditional_surface_status: "exact on U=B_2((-2,-2,-2))∪B_1((-2,-2,-1))∪B_3((-2,-2,1)) at unread v=(-3,-3,-1); |S|=4 and N_fire=4; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `s1 = (−2,−2,−2)`, `s2 = (−2,−2,−1)`, and `s3 = (−2,−2,1)`. The
closed ℓ¹ ball of radius `r` is

`B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`.

The locked set is the already-given unequal-radius union

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`.

The three balls have 25, 7, and 63 sites. Pairwise overlaps are 7, 7,
and 7, and the triple overlap has 7 sites, so `|U| = 81`. The unread
site is

`v = (−3,−3,−1)`.

Then `‖v − s1‖_1 = 3 > 2`, `‖v − s2‖_1 = 2 > 1`, and
`‖v − s3‖_1 = 4 > 3`, so `v ∉ U`.

The six nearest neighbors, in the declared order, are

| slot | neighbor | in `U` | lock tick |
|---|---|---|---|
| `+x` | `(−2,−3,−1)` | yes | `1` |
| `−x` | `(−4,−3,−1)` | no | none |
| `+y` | `(−3,−2,−1)` | yes | `1` |
| `−y` | `(−3,−4,−1)` | no | none |
| `+z` | `(−3,−3,0)` | yes | `3` |
| `−z` | `(−3,−3,−2)` | yes | `2` |

Occupancy mask at `v`:

`σ = (1, 0, 1, 0, 1, 1)`.

On the four occupied slots the lock-tick list is

`t = (1, ·, 1, ·, 3, 2)`,

so `t(+x) = t(+y) = 1`, `t(+z) = 3`, and `t(−z) = 2`. Empty slots have
no tick. Letters are `{0, +, −}` with `0` empty. Encode `0 ↦ 0`,
`+ ↦ 1`, `− ↦ 2`. The July-3 `k = 3` pair is the unique pair of
proper-cube orbits of 3-letter 6-tuples that are not proper-equivalent
to their inversion images. That set has 48 members. A displayed pair
step at an unread site forms that site if and only if the encoded
6-tuple lies in the pair; existing locks are not removed.

`G+` is the 24 determinant-`+1` signed permutation matrices of the
three axes, acting on the six axis directions. Spatial inversion
`P = −I` exchanges `+μ` with `−μ`. Support of a coloring is the
0-1 mask of nonzero letters. Occupancy stabilizer `Stab(σ)` is
`{ g ∈ G+ : g · σ = σ }`. Lock-tick stabilizer `Stab(σ,t)` further
requires `t(g · μ) = t(μ)` on occupied slots. `S` is the subset of
the 48-member pair whose support equals `σ` and that are pointwise
fixed by every element of `Stab(σ,t)`. Those are the tick-invariant
pair members on this star. `N_tick_ok = |S|`. `N_fire` is the number
of `c ∈ S` for which the displayed step forms exactly `v`
(`N_new = 1`) while every site of `U` remains locked.

Only `U` and the star at `v` are scored.

## Theorem 1 — Rebuild `S`

`G+` has order 24. Occupancy `Stab(σ)` has order 2. A generating
list is the identity and the proper rotation

`s : (x, y, z) ↦ (y, x, −z)`,

which swaps `+x ↔ +y` and `+z ↔ −z`. That map preserves `σ` and sends
`t(+z) = 3` to `t(−z) = 2`, so it does not preserve `t`. Therefore

`|Stab(σ)| = 2`, `|Stab(σ,t)| = 1`.

Four pair members have support equal to `σ`:

`(+,0,−,0,+,−)`,
`(+,0,−,0,−,+)`,
`(−,0,+,0,+,−)`,
`(−,0,+,0,−,+)`.

Because `|Stab(σ,t)| = 1`, every such member is pointwise fixed by
the lock-tick stabilizer. Rebuilding `S` by direct enumeration of the
48-member pair against the one-element lock-tick stabilizer gives

`|S| = 4`.

The lex-first member is `(+,0,−,0,+,−)`. Hence `N_tick_ok = 4`.

This is not leftover of uneqrad (census): uneqrad reports the breaker
and `N_tick_ok`, not the fire count of those members. It is not
leftover of tickfire (equal r): tickfire is the equal-radius lock-tick
fire census on a different host.

## Theorem 2 — Fire count

Each `c ∈ S` is a July-3 pair member. The center `v` is unread. The
displayed pair step therefore forms exactly `v` (`N_new = 1`) and
does not remove any lock of `U`. All four members fire, so

`N_fire = 4`.

## Theorem 3 — Displayed, not adopted

The set `S` and the count `N_fire` are displayed member data. They
are not the framework's fixed Admissibility rule. This note does not
write a firing c into Admissibility. Do not write a firing c into
Admissibility. Do not write a firing c or the radii into
Admissibility. Do not write radii into Admissibility. Do not attach
L1. Occupancy-only formation (the `n ≠ 0` gate) is not attached.
Qubit remains `M_2(C)`. No approved primitive is added. No axiom
edit.

## Honest-auditor / Boundary

- **What is proved.** On this unread star `|Stab(σ)| = 2`,
  `|Stab(σ,t)| = 1`, four July-3 pair members share the occupancy
  support, all four are tick-invariant, `|S| = 4`, `N_tick_ok = 4`,
  and `N_fire = 4`.
- **What is displayed only.** The pair, the radii, the lock-tick
  stabilizer, and the fire count are one rival table. They are not
  adopted.
- **What is not claimed.** No attachment of a firing 6-tuple to
  Admissibility; no writing of radii or ticks into Admissibility; no
  attachment of occupancy-only formation; no axiom edit; no
  formation rate; no lattice-wide dynamics; no leftover of uneqrad
  (census); no leftover of tickfire (equal r).
- **Mutation controls.** A rebuilt `|S|` other than 4 fails. A
  rebuilt `N_fire ≠ 4` fails. A note that writes a firing c or the
  radii into Admissibility, attaches L1, or authors an audit verdict
  fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, occupancy `σ`,
lock ticks `t`, `G+`, `Stab(σ)`, `Stab(σ,t)`, the 48-member July-3
pair, `S`, `N_fire`, the current premise boundary, and the mutation
controls. It writes no cache and authors no audit verdict.
