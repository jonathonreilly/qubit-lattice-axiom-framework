---
claim_id: unequal_radius_tick_rule_equivariance_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the G+ orbit of the lex-first unequal-radius breaker, whether a tick-ok pair member is cube-equivariant is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/unequal_radius_tick_rule_equivariance_2026_08_15.py
---

# Unequal-Radius Tick-Ok Pair Member on the Breaker Orbit (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the `G+` orbit of the uneqrad lex-first unequal-radius breaker
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` at
`v = (−3,−3,−1)`, with the lex-first `Stab(σ,t)`-ok July-3 pair member.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/unequal_radius_tick_rule_equivariance_2026_08_15.py`](../scripts/unequal_radius_tick_rule_equivariance_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment uneqrad names a breaker where `|Stab(σ,t)| = 1` and
`N_tick_ok = 4`. That census is one star. The residual here is not leftover
of uneqrad (one star) or deleq (different map). Rotate the three balls,
radii, and star together under `G+`. How many of the 24 proper cube
rotations send this host to a weight-4 unread star whose
`Stab(σ_g, t_g)`-ok set contains the rotated 6-tuple `g·c`?

`G+` is the 24 proper cube rotations about the origin. It acts on seeds,
radii (radii travel with their seeds), `v`, and the six slots

`(+x, −x, +y, −y, +z, −z)`.

Empty slots have no tick. Local data are `(σ, t)`. Pair members are the
July-3 6-slot 3-letter colorings whose `G+` orbit is sent to a different
orbit by spatial inversion. The `Stab(σ,t)`-ok set is the pair members
with support `σ` that are invariant under `Stab(σ,t)`.

**Theorem 1.** `N_commute = 24` and `N_commute / 24 = 24/24`. Every
`g` in `G+` sends this host to a weight-4 unread star, and that image's
`Stab(σ_g, t_g)`-ok set contains `g·c`.

**Theorem 2.** Whether N_commute = 24. N_commute = 24 holds. On this
orbit, tick-ok membership of the lex-first pair member is cube-equivariant
as a set membership. This does not write radii or ticks into
Admissibility.

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

Admissibility names neither `N_commute` nor any unequal-radius 3-ball
union, nor any lock-tick labeling, as the framework's fixed rule. The
covariance clause is the reason a local labeling on the orbit of
`(σ, t, c)` must be checked under `G+`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact G+ orbit of the uneqrad lex-first unequal-radius breaker: N_commute and the 24/24 ratio are exact. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: unequal_radius_tick_rule_equivariance
target_blocker_text: "on the G+ orbit of the lex-first unequal-radius breaker, whether a tick-ok pair member is cube-equivariant"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_commute on this orbit; do not write radii into Admissibility or attach L1"
conditional_surface_status: "exact on the 24-element G+ orbit of the displayed host; N_commute=24; displayed, not adopted"
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

Occupancy `σ` is the 6-bit nearest-neighbor indicator of `U` at `v`.
On an occupied neighbor `w` of `v`,

`t(w) = min_i ‖w − s_i‖_1`.

Direct distances give `v ∉ U`,

`σ = (1, 0, 1, 0, 1, 1)`,
`t = (1, ·, 1, ·, 3, 2)`,

`|Stab(σ)| = 2`, `|Stab(σ,t)| = 1`, and `N_tick_ok = 4`. The four
tick-ok pair members are

`(1, 0, 2, 0, 1, 2)`, `(1, 0, 2, 0, 2, 1)`,
`(2, 0, 1, 0, 1, 2)`, `(2, 0, 1, 0, 2, 1)`.

The lex-first member is

`c = (1, 0, 2, 0, 1, 2)`.

For `g` in `G+`, the image host is the three balls with seeds `g·s_i`,
the same radii traveling with those seeds, and unread site `g·v`. Slots
move by the induced permutation of the six directions. The image
occupancy and ticks are `σ_g = g·σ` and `t_g = g·t` because ℓ¹ is
preserved by proper cube rotations. The rotated 6-tuple is `g·c`.

`N_commute` is the number of `g` that send this host to a weight-4 unread
star whose `Stab(σ_g, t_g)`-ok set contains `g·c`. The 24 image hosts
remain inside the uneqrad box (centers in `[-2,2]^3`, `‖v‖_∞ ≤ 4`) and
remain breakers (`|Stab(σ_g, t_g)| = 1 < |Stab(σ_g)| = 2`). This is a
different map from deleq's claim-delta sign product.

## Theorem 1 — `N_commute / 24`

The runner rebuilds `U`, `v`, `(σ, t)`, the July-3 pair, and the
lex-first tick-ok member `c`, then applies each of the 24 proper cube
rotations to seeds, radii, `v`, and slots.

Every image is unread and has weight 4. Because `|Stab(σ_g, t_g)| = 1`,
the image tick-ok set is the four pair members with support `σ_g`. The
July-3 pair is a union of `G+` orbits, so `g·c` remains a pair member,
and `support(g·c) = g·σ = σ_g`. Hence `g·c` lies in the image tick-ok
set for every `g`. Therefore

`N_commute = 24`, `N_commute / 24 = 24/24`.

The identity is one such `g`. The occupancy swapper
`s : (x, y, z) ↦ (y, x, −z)` is another: it sends `c` to
`(2, 0, 1, 0, 2, 1)`, which is tick-ok on the image star at
`g·v = (−3,−3,1)`.

## Theorem 2 — whether `N_commute = 24`

Whether N_commute = 24. N_commute = 24 holds. On this orbit a
tick-ok pair member remains tick-ok after every proper cube rotation of
the host. The scored rule is set membership of `g·c` in the image
tick-ok set, not a unique product-of-ticks labeling and not deleq's
sign-product map. If `N_commute` had not been 24, unequal-radius ticks
would not be a cube-covariant Admissibility rule. That negative clause
is not triggered. The count is still displayed member data, not the
framework's fixed rule.

## Theorem 3 — displayed, not adopted

`N_commute = 24` and `N_commute / 24 = 24/24` are displayed orbit data.
They are not the framework's fixed Admissibility rule. This note does
not write radii into Admissibility. Do not write radii into
Admissibility. Do not attach L1. Occupancy-only formation is not
attached. Qubit remains `M_2(C)`. No approved primitive is added. No
axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the `G+` orbit of the uneqrad lex-first
  unequal-radius breaker, with lex-first tick-ok pair member
  `c = (1, 0, 2, 0, 1, 2)`, every image is a weight-4 unread star and
  `N_commute = 24`.
- **What is displayed only.** The radii, the ticks, the pair member, and
  the commute count are one rival table. They are not adopted.
- **What is not claimed.** No attachment of radii or ticks to
  Admissibility; no attachment of occupancy-only formation; no axiom
  edit; no formation rate; no lattice-wide dynamics; no leftover of
  uneqrad (one star) or deleq (different map); no compiler no-go.
- **Mutation controls.** A rebuilt `N_commute ≠ 24` fails. A rebuilt
  lex-first `c` other than `(1, 0, 2, 0, 1, 2)` fails. A note that
  writes radii into Admissibility, attaches L1, or authors an audit
  verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds the uneqrad lex-first host, the lock-ticks,
the 24 proper cube rotations, the lex-first tick-ok pair member, the
image weight-4 unread stars, `N_commute`, the current premise boundary,
and the mutation controls. It writes no cache and authors no audit
verdict.
