---
claim_id: unequal_radius_lock_tick_stab_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among unequal-radius 3-ball unions with radii in {1,2,3}, whether lock-ticks shrink Stab at an unread weight-4 star is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_lock_tick_stab_2026_08_15.py
---

# Unequal-Radius Lock-Ticks Can Shrink Occupancy Stab (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 3-ball unions `U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3)` with
distinct centers in `[-2,2]^3`, radii `ri ∈ {1,2,3}` not all equal, and
unread sites `v` with `‖v‖_∞ ≤ 4` and `wt(σ(U,v)) = 4`. Occupied
nearest neighbors carry `t(w) = min_i ‖w − si‖_1`. Score a prefix plus
existence. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_lock_tick_stab_2026_08_15.py`](../scripts/unequal_radius_lock_tick_stab_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment ticklip: equal-radius unions force `t = r` on every occupied
neighbor of an unread site, so lock-ticks cannot shrink `Stab`. That
identity is for one common radius. The residual here is not leftover of
tickhost (equal r=2). Among unequal-radius 3-ball unions with radii in
`{1,2,3}`, do lock-ticks ever satisfy `|Stab(σ,t)| < |Stab(σ)|` at an
unread weight-4 star?

Centers are distinct sites of `Z^3` in the cube `[-2,2]^3`. Radii run
over the 24 triples in `{1,2,3}^3` that are not all equal. Lex order is
on the canonical tuple `(s1,s2,s3, r1,r2,r3, v)` with `s1 < s2 < s3` in
coordinate lex order. Empty slots have no tick. `G+` is the 24 proper
cube rotations acting on the six slots

`(+x, −x, +y, −y, +z, −z)`.

`Stab(σ) = { g in G+ : g · σ = σ }`,

`Stab(σ,t) = { g in G+ : g · σ = σ and t(g · μ) = t(μ) on occupied slots }`.

**Theorem 1.** A breaker exists. The lex-first breaker is

`(s1,s2,s3) = ((−2,−2,−2), (−2,−2,−1), (−2,−2,1))`, radii `(2, 1, 3)`,
`v = (−3,−3,−1)`,

`σ = (1, 0, 1, 0, 1, 1)`,

`t = (1, ·, 1, ·, 3, 2)`,

`|Stab(σ)| = 2`, `|Stab(σ,t)| = 1`.

On the lex-first 2000 weight-4 stars,

`N_prefix = 2000`, `N_uneq_prefix = 1413`.

**Theorem 2.** On that star, `N_tick_ok = 4`. The four July-3 pair
members with this support are all `Stab(σ,t)`-invariant because
`|Stab(σ,t)| = 1`, so `N_tick_ok = N_pair_support = 4`.

**Theorem 3.** Displayed, not adopted. Do not write radii into Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither `Stab(σ,t)` nor any lock-tick, nor any
unequal-radius 3-ball union, as the framework's fixed rule. The covariance
clause is the reason a local labeling on the orbit of `(σ, t)` must be
stabilizer-invariant. Formation site and rate remain outside the axiom
memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact search of unequal-radius 3-ball weight-4 unread stars in the declared box: a lex-first breaker exists, prefix counts N_prefix and N_uneq_prefix are exact, and N_tick_ok on that star is exact. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: unequal_radius_lock_tick_stab
target_blocker_text: "among unequal-radius 3-ball unions with radii in {1,2,3}, whether lock-ticks shrink Stab at an unread weight-4 star"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the lex-first breaker, N_prefix, N_uneq_prefix, and N_tick_ok; do not write radii into Admissibility or attach L1"
conditional_surface_status: "exact on the unequal-radius 3-ball box; breaker exists; N_prefix=2000; N_uneq_prefix=1413; N_tick_ok=4; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. A 3-ball union is

`U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3)`

with distinct `si ∈ [-2,2]^3` and `ri ∈ {1,2,3}` not all equal. The
unread site `v` satisfies `v ∉ U` and `‖v‖_∞ ≤ 4`. Occupancy `σ` is the
6-bit nearest-neighbor indicator of `U` at `v`, in the declared slot
order. Weight `wt(σ)` is the number of `1`s. Only stars with
`wt(σ) = 4` are scored.

On an occupied neighbor `w` of `v`,

`t(w) = min{ ‖w − s1‖_1, ‖w − s2‖_1, ‖w − s3‖_1 }`.

Empty slots have no tick. Local data are `(σ, t)`. `G+` acts by permuting
slots. The two stabilizers are as named above.

A star is the tuple `(s1,s2,s3, r1,r2,r3, v)` with `s1 < s2 < s3` in
coordinate lex order. That order enumerates each unordered triple of
centers once, with radii attached in that center order.

`N_prefix` is the number of weight-4 stars in the declared lex prefix of
length 2000. `N_uneq_prefix` is how many of those satisfy
`|Stab(σ,t)| < |Stab(σ)|`. Existence is the question whether any
weight-4 star in the box is a breaker. The search stops at the first
breaker after the prefix is complete.

`N_tick_ok` is the number of July-3 pair members with support `σ` that
are invariant under `Stab(σ,t)`.

The lex-first weight-4 star (not a breaker) is

`(s1,s2,s3) = ((−2,−2,−2), (−2,−2,−1), (−2,−2,0))`, radii `(2, 1, 2)`,
`v = (−3,−3,−1)`, with `σ = (1, 0, 1, 0, 1, 1)` and
`t = (1, ·, 1, ·, 2, 2)`. Occupied ticks are unequal, but the occupancy
swapper preserves them, so `|Stab(σ,t)| = |Stab(σ)| = 2`.

## Theorem 1 — a breaker exists

The runner enumerates centers in lex order with `s1 < s2 < s3`, then the
24 unequal radius triples, then unread sites `v` with `‖v‖_∞ ≤ 4`. It
retains those with `wt(σ) = 4`. The lex-first breaker is the 33rd such
star:

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
`v = (−3,−3,−1)`.

Direct distances:

`‖v − s1‖_1 = 3 > 2`, `‖v − s2‖_1 = 2 > 1`, `‖v − s3‖_1 = 4 > 3`,

so `v ∉ U`. Occupied neighbors and ticks:

- `+x = (−2,−3,−1)` has `t = 1`,
- `+y = (−3,−2,−1)` has `t = 1`,
- `+z = (−3,−3,0)` has `t = 3`,
- `−z = (−3,−3,−2)` has `t = 2`.

Hence `σ = (1, 0, 1, 0, 1, 1)` and `t = (1, ·, 1, ·, 3, 2)`.

The occupancy stabilizer is `{id, s}` with

`s : (x, y, z) ↦ (y, x, −z)`,

which swaps `+x ↔ +y` and `+z ↔ −z`. That map preserves `σ` and sends
`t(+z) = 3` to `t(−z) = 2`, so it does not preserve `t`. Therefore

`|Stab(σ)| = 2`, `|Stab(σ,t)| = 1`.

On the lex-first 2000 weight-4 stars the same comparison is exact, so

`N_prefix = 2000`, `N_uneq_prefix = 1413`.

Equal-radius unions force a constant occupied tick and cannot break
`Stab`. The present family excludes those triples. This is not leftover
of tickhost (equal r=2). Scoring a prefix plus existence. Do not attach
L1.

## Theorem 2 — `N_tick_ok` on the breaker

July-3 pair members are the 6-slot 3-letter colorings whose `G+` orbit
is sent to a different orbit by spatial inversion. Restricting to
support `σ` gives four members

`(1, 0, 2, 0, 1, 2)`, `(1, 0, 2, 0, 2, 1)`,
`(2, 0, 1, 0, 1, 2)`, `(2, 0, 1, 0, 2, 1)`,

so `N_pair_support = 4`. Because `|Stab(σ,t)| = 1`, every such member is
invariant under `Stab(σ,t)`. Hence

`N_tick_ok = 4`.

If no breaker had existed, unequal radii in this box would not break
occupancy `Stab`. A breaker exists, so that negative statement is false
on this family.

## Theorem 3 — displayed, not adopted

The lex-first breaker, the two stabilizer orders, `N_prefix = 2000`,
`N_uneq_prefix = 1413`, and `N_tick_ok = 4` are displayed member data.
They are not the framework's fixed Admissibility rule. This note does
not write radii into Admissibility. Do not write radii into
Admissibility. Do not attach L1. Occupancy-only formation is not
attached. Qubit remains `M_2(C)`. No approved primitive is added. No
axiom edit.

## Honest-auditor / Boundary

- **What is proved.** In this unequal-radius 3-ball box a lex-first
  breaker exists, with the displayed `(centers, radii, v, σ, t,
  |Stab(σ)|, |Stab(σ,t)|)`. `N_prefix = 2000` and `N_uneq_prefix = 1413`
  on the lex-first 2000 weight-4 stars. On the breaker, `N_tick_ok = 4`.
- **What is displayed only.** The radii, the ticks, and the two
  stabilizers are one rival table. They are not adopted.
- **What is not claimed.** No attachment of radii or ticks to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no leftover of
  tickhost (equal r=2); no compiler no-go.
- **Mutation controls.** A rebuilt lex-first breaker other than the
  displayed star fails. A prefix other than `N_prefix = 2000` or
  `N_uneq_prefix = 1413` fails. A rebuilt `N_tick_ok ≠ 4` fails. A note
  that writes radii into Admissibility, attaches L1, or authors an audit
  verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds every unequal-radius 3-ball union in the
center box through the lex-first breaker and the 2000-star prefix, the
lock-ticks on occupied slots, the 24 proper cube rotations, `Stab(σ)`
and `Stab(σ,t)`, `N_prefix`, `N_uneq_prefix`, `N_tick_ok` on the
breaker, the current premise boundary, and the mutation controls. It
writes no cache and authors no audit verdict.
