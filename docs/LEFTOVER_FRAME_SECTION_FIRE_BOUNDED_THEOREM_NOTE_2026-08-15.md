---
claim_id: leftover_frame_section_fire_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the lex-first unequal-radius breaker, whether the leftover-frame-positive pair section fires is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/leftover_frame_section_fire_2026_08_15.py
---

# Leftover-Frame-Positive Section Fire On The Uneqrad Breaker (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the locked unequal-radius union
`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))` and the unread
six-neighbor star at `v = (−3,−3,−1)`. Rebuild the leftover-frame-positive
pair section `f(σ,b)` on this star and report whether that one member
fires. Score the uneqrad star only. Stars are not displayed for each of
the 12 masks, so `N_fire` among those 12 masks is not scored. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/leftover_frame_section_fire_2026_08_15.py`](../scripts/leftover_frame_section_fire_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment bitsec: leftover-frame-positive. Section `f` has
`N_commute=576`. New residual: on the uneqrad lex-first breaker, does
`f(σ,b)` fire (`N_new=1`, `U` persists)? Also report `N_fire` among the
12 masks if a star is displayed for each; else score the uneqrad star
only. Not leftover of 10→uneqrun (those 4 were not this `f`). Do not
attach L1.

`U`, `v`, `σ`, `t` are the uneqrad lex-first breaker. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

Occupancy mask

`σ = (1, 0, 1, 0, 1, 1)`.

Occupied nearest neighbors receive the lock tick

`t(w) = min_i ‖w − si‖_1`.

Empty slots have no tick. Local data is `(σ, t)`. The unique full axis
is `z`. The age bit is

`b = [t(−z) < t(+z)]`.

On this star `t(−z) = 2` and `t(+z) = 3`, so `b = 1`. Completions of
`(σ,b)` are the two July-3 pair members that write opposite letters on
the full axis according to `b`. The leftover-frame-positive section
picks the completion whose ordered triple of directions (leftover `+`,
leftover `−`, full-axis `+` letter) has determinant `+1`.

**Theorem 1.** Rebuild `f(σ,b)`. The 6-tuple is

`f(σ,b) = (+, 0, −, 0, +, −)`.

It is a July-3 pair member.

**Theorem 2.** That member forms exactly `v` (`N_new = 1`) and `U`
persists.

**Theorem 3.** Displayed, not adopted. Do not write `f` into
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

it does not supply the formation site, probability,
or rate.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

When present, a record locks exactly one admissible local possibility.

A site never carries more than one record; records are permanent.

A readout value is determined by record content alone.

A site with no record cannot be read.

Admissibility names neither the leftover-frame-positive section nor any
unequal-radius 3-ball union as the framework's fixed rule. Record
permanence is used only to keep the locks on `U`. Formation site and
rate remain outside the axiom memo. Qubit remains `M_2(C)`. No axiom
edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact rebuild of leftover-frame-positive f(σ,b) on one unread six-neighbor star and an exact fire report (N_new=1, U persists). Displayed report only."
trace_class: frontier_discovery
target_claim_id: leftover_frame_section_fire
target_blocker_text: "on the uneqrad lex-first breaker, whether leftover-frame-positive f(σ,b) fires"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of f(σ,b) and the fire report; do not write f into Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad lex-first breaker; f(σ,b)=(+, 0, −, 0, +, −); N_new=1 and U persists; displayed, not adopted"
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
no tick. The unique full axis is `z`. The age bit is
`b = [t(−z) < t(+z)]`, hence `b = 1`. Letters are `{0, +, −}` with `0`
empty. Encode `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`. The July-3 `k = 3` pair is
the unique pair of proper-cube orbits of 3-letter 6-tuples that are not
proper-equivalent to their inversion images. That set has 48 members.

Completions`(σ,b)` are the pair members that match occupancy `σ` and
write `c(+z)=+`, `c(−z)=−` when `b = 1`. There are two such members:
the leftover occupied slots `+x` and `+y` receive opposite letters, in
two ways. The leftover-frame sign of a completion is the determinant of
the ordered triple of directions (leftover `+`, leftover `−`, full-axis
`+` letter). The section `f` takes the unique completion of sign `+1`.
A displayed pair step at an unread site forms that site if and only if
the encoded 6-tuple lies in the pair; existing locks are not removed.

Score the uneqrad star only. Stars are not displayed for each of the 12
perpendicular weight-4 masks.

## Theorem 1 — Rebuild `f(σ,b)`

The unique full axis of `σ` is `z`. The bit `b = 1` writes `+` on `+z`
and `−` on `−z`. The two completions are

`(+, 0, −, 0, +, −)` and `(−, 0, +, 0, +, −)`.

The first has leftover `+` on `+x`, leftover `−` on `+y`, and full-axis
`+` on `+z`. That ordered triple of directions has determinant `+1`.
The second has leftover `+` on `+y` and leftover `−` on `+x`, so
determinant `−1`. Therefore

`f(σ,b) = (+, 0, −, 0, +, −)`.

This 6-tuple lies in the 48-member July-3 pair. It is a July-3 pair
member. Section `f` is the leftover-frame-positive completion, the
same section that scores `N_commute=576` on the 12 masks. This residual
is not leftover of 10→uneqrun (those 4 were not this `f`): uneqrun
counts all four same-support pair members, not the leftover-frame-
positive section.

## Theorem 2 — `N_new = 1` and `U` persists

The rebuilt `f(σ,b)` is a July-3 pair member. The center `v` is unread.
The displayed pair step therefore forms exactly `v` (`N_new = 1`) and
does not remove any lock of `U`. So `U` persists. Stars are not
displayed for each of the 12 masks, so this note does not report
`N_fire` among those 12 masks.

## Theorem 3 — Displayed, not adopted

The 6-tuple `f(σ,b)` and the fire report are displayed member data.
They are not the framework's fixed Admissibility rule. This note does
not write `f` into Admissibility. Do not write f into Admissibility.
Do not write radii into Admissibility. Do not attach L1.
Occupancy-only formation (the `n ≠ 0` gate) is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker,
  `b = [t(−z) < t(+z)] = 1`, the leftover-frame-positive section
  rebuilds as `f(σ,b) = (+, 0, −, 0, +, −)`, that 6-tuple is a July-3
  pair member, `N_new = 1`, and `U` persists.
- **What is displayed only.** The section `f` and the fire report are
  one rival table. They are not adopted.
- **What is not claimed.** No attachment of `f` to Admissibility; no
  writing of radii or ticks into Admissibility; no attachment of
  occupancy-only formation; no axiom edit; no formation rate; no
  leftover of 10→uneqrun (those 4 were not this `f`); no compiler
  no-go; no `N_fire` census of the 12 masks.
- **Mutation controls.** A rebuilt `f(σ,b)` other than
  `(+, 0, −, 0, +, −)` fails. A rebuilt leftover-frame sign other than
  `+1` fails. A rebuilt `N_new ≠ 1` with `U` not persisting, or a
  rebuilt `N_new` other than 0 or 1, fails. A note that writes `f`
  into Admissibility, attaches L1, or authors an audit verdict fails.

This note authors no audit verdict.

## Primary Runner

The primary runner rebuilds `U`, the star at `v`, occupancy `σ`,
lock ticks `t`, the age bit `b = [t(−z) < t(+z)]`, the 48-member
July-3 pair, the leftover-frame-positive section `f(σ,b)`, the fire
report (`N_new`, `U` persists), the current premise boundary, and the
mutation controls. It scores the uneqrad star only. It writes no cache
and authors no audit verdict.
