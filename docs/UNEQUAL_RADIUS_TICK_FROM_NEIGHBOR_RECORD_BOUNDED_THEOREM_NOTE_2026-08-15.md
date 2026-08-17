---
claim_id: unequal_radius_tick_from_neighbor_record_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the lex-first unequal-radius breaker, whether neighbor Records valued in M_2 supply the lock-tick field is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_tick_from_neighbor_record_2026_08_15.py
---

# Neighbor Records And The Unequal-Radius Lock-Tick Field (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the uneqrad lex-first unequal-radius breaker
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` at
`v = (−3,−3,−1)`. For each occupied neighbor the displayed Record clock is
the ℓ¹-to-nearest-seed value (L1 formation-count). Whether that 6-star
content rebuilds the lock-tick field, and whether Record valued in `M_2`
supplies it, is reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_tick_from_neighbor_record_2026_08_15.py`](../scripts/unequal_radius_tick_from_neighbor_record_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqext names the lock-tick field `t` as an extra versus
occupancy. That extra is not leftover of delloc (product rule) or uneqext
(extra vs occupancy). The residual here is whether each occupied neighbor's
Record, whose only displayed clock is the L1 formation-count (equivalently
ℓ¹-to-nearest-seed), can rebuild `t` at the 6-star only, without naming
distant seeds or radii.

`U, v` are the uneqrad lex-first breaker. Occupancy `σ` is the 6-bit
nearest-neighbor indicator of `U` at `v`. On an occupied neighbor `w`,

`t(w) = min_i ‖w − s_i‖_1`.

Empty slots have no clock. Local input at `v` is the 6-tuple of
`(occupied?, clock-or-none)`.

**Theorem 1.** That 6-tuple equals `(σ,t)` on this star. It is not occupancy
alone.

**Theorem 2.** Rebuilding `t` from neighbor Records uses the seed-distance
clocks. Those clocks are not a function of the qubit state on `M_2` at `w`
(L1 Bloch is an occupancy function). So Record-as-`M_2` does not supply
`t`. Naming seed-distance as Record content is the same extra.

**Theorem 3.** Displayed, not adopted. Do not write a clock into Record or
Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

## Current Premise Boundary

The Lattice, Admissibility, Record, and Qubit sentences used here are quoted
from [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

Only records are readable. A readout value is determined by record content
alone.

A site with no record cannot be read.

Admissibility names neither lock-ticks nor seed-distance clocks as the
framework's fixed rule. Record locks one admissible local possibility in
`M_2(C)` and supplies no integer formation-count. The displayed neighbor
clocks are one rival table, not current Record content. Qubit remains
`M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "On the uneqrad lex-first star the displayed neighbor-Record 6-tuple equals (σ,t) and is not occupancy alone. The same M_2 lock on every occupied neighbor has one Bloch vector, so Record-as-M_2 does not supply t. Displayed, not adopted."
trace_class: negative_route_pruning
target_claim_id: unequal_radius_tick_from_neighbor_record
target_blocker_text: "whether neighbor Records valued in M_2 supply the lock-tick field on the lex-first unequal-radius breaker"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "independent audit of the 6-tuple identity and the M_2 non-supply on this star; do not write a clock into Record or Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad lex-first 6-star; Record-as-M_2 does not supply t; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. The host is the uneqrad
lex-first breaker

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,
radii `(2, 1, 3)`,
`v = (−3,−3,−1)`.

Slots are the six directions

`(+x, −x, +y, −y, +z, −z)`.

A neighbor `w = v + e` is occupied when `w ∈ U`. Occupancy and ticks are

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`.

So `v ∉ U` and the four occupied neighbors carry mixed clocks `{1, 1, 3, 2}`.

The displayed Record table on the star is: occupied neighbors carry a Record
whose only displayed clock is `t(w)`; empty neighbors carry no Record and
cannot be read. The local input is the 6-tuple of `(occupied?, clock-or-none)`

`ρ = ((1, 1), (0, ·), (1, 1), (0, ·), (1, 3), (1, 2))`.

The one-site possibility domain is `M_2(C)`. The displayed lock used to
test Record-as-`M_2` is the same rank-1 projector

`P = ((1, 0), (0, 0))`

on every occupied neighbor. Its Bloch vector is `(0, 0, 1)`. L1 Bloch is an
occupancy function: `1` when a Record is present and `0` when the site has
no Record. That occupancy function is `σ`, not `t`.

## Theorem 1 — the 6-tuple equals `(σ,t)` and is not occupancy alone

Direct ℓ¹ distances on the six neighbors rebuild `σ` and `t` above. The
displayed Record 6-tuple is obtained by writing `(1, t(w))` on an occupied
slot and `(0, ·)` on an empty slot. That 6-tuple equals `(σ,t)` on this
star:

`ρ = ((1, 1), (0, ·), (1, 1), (0, ·), (1, 3), (1, 2))`.

It is not occupancy alone. Occupancy is the bit string
`σ = (1, 0, 1, 0, 1, 1)`. The four occupied slots are indistinguishable
under `σ`, while their clocks are `1, 1, 3, 2`. In particular the `+z`
clock `3` and the `−z` clock `2` differ from the `+x` and `+y` clocks
`1`. The 6-tuple therefore carries the uneqext extra, not occupancy
alone.

## Theorem 2 — Record-as-`M_2` does not supply `t`

Rebuilding `t` from neighbor Records uses the seed-distance clocks. Those
clocks are not a function of the qubit state on `M_2` at `w`.

On this star every occupied neighbor may lock the same `M_2` possibility
`P`. The four occupied Bloch vectors are then identical, `(0, 0, 1)`,
while the clocks remain `1, 1, 3, 2`. L1 Bloch is an occupancy function:
it returns `1` on each occupied neighbor and `0` on each empty neighbor,
which is exactly `σ`. A function of the `M_2` lock, or of that occupancy
function, cannot send the same lock to both `1` and `3`.

So Record-as-`M_2` does not supply `t`. Naming seed-distance as Record
content is the same extra already named by uneqext versus occupancy. The
delloc product rule is a different map and is not used.

## Theorem 3 — displayed, not adopted

The 6-tuple identity and the `M_2` non-supply are displayed star data.
They are not the framework's fixed Record or Admissibility content.
Displayed, not adopted. Do not write a clock into Record or Admissibility.
Do not attach L1. Occupancy-only formation is not attached. Qubit remains
`M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first unequal-radius breaker, the
  displayed neighbor-Record 6-tuple equals `(σ,t)` and is not occupancy
  alone. The same `M_2` lock on every occupied neighbor has one Bloch
  vector, so Record-as-`M_2` does not supply `t`.
- **What is displayed only.** The seed-distance clocks, the 6-tuple, and
  the chosen projector `P` are one rival table. They are not adopted.
- **What is not claimed.** No clock written into Record or Admissibility;
  no attachment of L1; no axiom edit; no formation rate; no lattice-wide
  dynamics; no leftover of delloc (product rule) or uneqext (extra vs
  occupancy); no compiler no-go.
- **Mutation controls.** A rebuilt 6-tuple other than `(σ,t)` fails. A
  rebuilt mixed-clock witness that collapses to occupancy alone fails. A
  note that writes a clock into Record or Admissibility, attaches L1, or
  authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the uneqrad lex-first host, the occupancy,
the lock-ticks, the displayed neighbor-Record 6-tuple, the common `M_2`
lock and Bloch occupancy function, the current premise boundary, and the
mutation controls. It writes no cache and authors no audit verdict.
It scores the uneqrad star only.
