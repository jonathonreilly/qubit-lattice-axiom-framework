---
claim_id: ridge_slide_clock_not_readiness_12host_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Leftover-frame fire on the 12 perp-mask hosts with the named ridge-slide hop-cost as unused labels and as a cost-1 filter is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_slide_clock_not_readiness_12host_2026_08_15.py
---

# Ridge-Slide Hop-Cost As Clock, Not Readiness, On 12 Hosts (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 lex-first realizing 3-ball hosts of the perpendicular
weight-4 occupancy masks from bitall. On each host, leftover-frame-positive
`f` is scored with the named ridge-slide hop-cost `ρ3` as unused edge
labels versus as a cost-1 filter. Report `N_label_fire` and
`N_filt_fire`. The 12 lex-first perp-mask hosts only. Uniqueness is not
required. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_slide_clock_not_readiness_12host_2026_08_15.py`](../scripts/ridge_slide_clock_not_readiness_12host_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment: μ fires 12/12 as labels and filter. New residual: the same
12 hosts with ρ3. First display. Uniqueness not required. Do not
attach L1.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The 12 rows are the bitall / bitreal Theorem 2 hosts: for each
perpendicular weight-4 mask, the lex-first `(centers, radii, v)` whose
unread 6-NN occupancy equals that mask. On each host, `t` is the
seed-radii ℓ¹ lock tick on occupied neighbors, `b` is read from the
unique full axis, and `f` is the leftover-frame-positive July-3 pair
member of `(σ,b)`.

`f` is the leftover-frame-positive pair section. Write `|σ_x|` for the
number of nonzero coordinates of `x ∈ Z^3`. The named ridge-slide
hop-cost, ρ3 as in ridk1, is

`ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
`|w_i|` equal `1)`, else `1`,

where `μ` as in hugax is

`μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least
nonzero `|w_i|` equals `1)`, else `1`,

and `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The extra clause is a ridge 3→3 slide: both ends have support `3`, and
the destination has exactly two unit coordinates. Those clauses are the
whole rule.

**Theorem 1.** On each of the 12 lex-first realizing hosts, `f` with
`ρ3` as unused labels has `N_new = 1`. `N_label_fire = 12`.

**Theorem 2.** On those 12, `f` with fire restricted to cost-1 edges
has `N_new` on six hosts and fails on the six hosts whose unread
center has exactly two unit coordinates. `N_filt_fire = 6`. Displayed,
not adopted.

**Theorem 3.** Displayed, not adopted. Do not write ρ3 into Admissibility.
Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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

Admissibility names neither leftover-frame-positive `f` nor the named
ridge-slide hop-cost `ρ3` as the framework's fixed rule. Record permanence
is used only to keep the locks on each `U`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact 12-host leftover-frame fire with ridge-slide hop-cost rho3 as unused labels and as a cost-1 filter: N_label_fire=12 and N_filt_fire=6. Displayed counts only."
trace_class: frontier_discovery
target_claim_id: ridge_slide_clock_not_readiness_12host
target_blocker_text: "on all 12 perp-mask realizing hosts, leftover-frame fire with rho3 as unused labels and as a cost-1 filter"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of N_label_fire and N_filt_fire on the 12 lex-first hosts; do not write rho3 into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 lex-first realizing hosts; N_label_fire=12; N_filt_fire=6; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are `(+x, −x, +y, −y, +z, −z)`. Occupancy at an unread site `v`
relative to a locked set `U` is the 6-bit indicator

`σ(U, v)_i = 1` if and only if `v + e_i ∈ U`.

A weight-4 mask is perpendicular when the two emptied slots lie on two
distinct axes. The 12 perpendicular masks, in lex order, are

`(0, 1, 0, 1, 1, 1)`,
`(0, 1, 1, 0, 1, 1)`,
`(0, 1, 1, 1, 0, 1)`,
`(0, 1, 1, 1, 1, 0)`,
`(1, 0, 0, 1, 1, 1)`,
`(1, 0, 1, 0, 1, 1)`,
`(1, 0, 1, 1, 0, 1)`,
`(1, 0, 1, 1, 1, 0)`,
`(1, 1, 0, 1, 0, 1)`,
`(1, 1, 0, 1, 1, 0)`,
`(1, 1, 1, 0, 0, 1)`,
`(1, 1, 1, 0, 1, 0)`.

Write `B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`. Each host is a 3-ball
union in the uneqrad box

`U = B_{r1}(s1) ∪ B_{r2}(s2) ∪ B_{r3}(s3)`

with distinct `si` in `[−2,2]³` and `(r1,r2,r3) ∈ {1,2,3}³` not all
equal, together with an unread site `v ∉ U`, `‖v‖_∞ ≤ 4`, whose
occupancy is the named mask. The twelve hosts are the bitall / bitreal
Theorem 2 lex-first rows.

On occupied nearest neighbors the seed-radii ℓ¹ lock tick is

`t(w) = min_i ‖w − si‖_1`.

Empty slots have no tick. Local data is `(σ, t)`. The unique full axis
is the unique axis with both slots occupied. The age bit is

`b = [t(−axis) < t(+axis)]`.

Letters are `{0, +, −}` with `0` empty. Encode `0 ↦ 0`, `+ ↦ 1`,
`− ↦ 2`. Completions of `(σ,b)` are the two July-3 pair members that
match occupancy `σ` and write opposite letters on the full axis
according to `b`. The leftover-frame sign of a completion is the
determinant of the ordered triple of directions (leftover `+`, leftover
`−`, full-axis `+` letter). The section `f` takes the completion of
sign `+1`. A displayed pair step at an unread site forms that site
if and only if the encoded 6-tuple lies in the pair; existing locks are
not removed. `N_new = 1` and `U` persists exactly when that step forms
`v` and leaves every lock of `U` in place.

On a directed nearest-neighbor edge `x → y`,

`ρ3(x → y) = 3` if `μ` would be `3` or `(|σ_x|=|σ_y|=3` and exactly two
`|y_i|` equal `1)`, else `1`,

where `|σ_x|` is the number of nonzero coordinates of `x`.

Assigning `ρ3` as unused labels writes those costs on already-present
directed edges. It does not rewrite which neighbors of `v` lie in `U`,
and it does not rewrite the lock-ticks `t(w)`. Therefore `(σ,b)` and
leftover-frame-positive `f(σ,b)` are the same as in the bitall census.
`N_label_fire` is how many of the 12 hosts still have `N_new = 1` and
`U` persisting after that unused labeling.

If `ρ3` is instead used as a cost-1 filter, an occupied neighbor
participates in the pair step only when the directed edge from that
neighbor to `v` has cost `1`. The filtered occupancy is `σ_ready`.
Leftover-frame-positive `f` is then evaluated on `(σ_ready, b)` when
`σ_ready` still has a unique full axis, and is undefined otherwise.
`N_filt_fire` is how many of the 12 hosts have `N_new = 1` under that
filter.

The 12 lex-first perp-mask hosts only.

## Theorem 1 — unused labels; `N_label_fire = 12`

Each bitall Theorem 2 row rebuilds: the three ℓ¹ balls with the named
centers and radii have unread center `v`, and the 6-NN occupancy of `v`
equals the named mask. Assigning `ρ3` as unused labels does not change
the occupancy mask or the age bit, so leftover-frame-positive `f` is
the same section as in bitall. Each `f` is a July-3 pair member, each
`v` is unread, the displayed pair step forms exactly that `v`
(`N_new = 1`), and no lock of `U` is removed, so `U` persists.
Therefore

`N_label_fire = 12`.

The twelve hosts are

| `σ` | lex-first `(centers, radii, v)` |
|---|---|
| `(0, 1, 0, 1, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-1, -1, -1))` |
| `(0, 1, 1, 0, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-1, -3, -1))` |
| `(0, 1, 1, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 1, 2), (-1, -1, -1))` |
| `(0, 1, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-1, -1, -2))` |
| `(1, 0, 0, 1, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -1, -1))` |
| `(1, 0, 1, 0, 1, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, -2, 0)), (2, 1, 2), (-3, -3, -1))` |
| `(1, 0, 1, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 1, 2), (-3, -1, -1))` |
| `(1, 0, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-3, -1, -2))` |
| `(1, 1, 0, 1, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 1, 2), (-1, -1, -1))` |
| `(1, 1, 0, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -1, -2))` |
| `(1, 1, 1, 0, 0, 1)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 1, 2), (-1, -3, -1))` |
| `(1, 1, 1, 0, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -3, -2))` |

The twelve label-fire rows are

| `σ` | axis | `t` | `b` | `f(σ,b)` | `N_new` |
|---|---|---|---|---|---|
| `(0, 1, 0, 1, 1, 1)` | `z` | `(·, 1, ·, 1, 2, 2)` | `0` | `(0, −, 0, +, −, +)` | `1` |
| `(0, 1, 1, 0, 1, 1)` | `z` | `(·, 1, 1, ·, 2, 2)` | `0` | `(0, +, −, 0, −, +)` | `1` |
| `(0, 1, 1, 1, 0, 1)` | `y` | `(·, 1, 2, 1, ·, 2)` | `1` | `(0, −, +, −, 0, +)` | `1` |
| `(0, 1, 1, 1, 1, 0)` | `y` | `(·, 1, 1, 1, 2, ·)` | `0` | `(0, −, −, +, +, 0)` | `1` |
| `(1, 0, 0, 1, 1, 1)` | `z` | `(1, ·, ·, 1, 2, 2)` | `0` | `(+, 0, 0, −, −, +)` | `1` |
| `(1, 0, 1, 0, 1, 1)` | `z` | `(1, ·, 1, ·, 2, 2)` | `0` | `(−, 0, +, 0, −, +)` | `1` |
| `(1, 0, 1, 1, 0, 1)` | `y` | `(1, ·, 2, 1, ·, 2)` | `1` | `(+, 0, +, −, 0, −)` | `1` |
| `(1, 0, 1, 1, 1, 0)` | `y` | `(1, ·, 1, 1, 2, ·)` | `0` | `(+, 0, −, +, −, 0)` | `1` |
| `(1, 1, 0, 1, 0, 1)` | `x` | `(2, 1, ·, 1, ·, 2)` | `1` | `(+, −, 0, +, 0, −)` | `1` |
| `(1, 1, 0, 1, 1, 0)` | `x` | `(1, 1, ·, 1, 2, ·)` | `0` | `(−, +, 0, +, −, 0)` | `1` |
| `(1, 1, 1, 0, 0, 1)` | `x` | `(2, 1, 1, ·, ·, 2)` | `1` | `(+, −, −, 0, 0, +)` | `1` |
| `(1, 1, 1, 0, 1, 0)` | `x` | `(1, 1, 1, ·, 2, ·)` | `0` | `(−, +, −, 0, +, 0)` | `1` |

This is not leftover of the 12/12 μ label-and-filter count. μ fires
12/12 as labels and filter is the investment. The present score puts
ridk1 `ρ3` on the same 12 hosts with ρ3 in the leftover-frame
label-versus-filter split. First display.

## Theorem 2 — cost-1 filter; `N_filt_fire = 6`

If `ρ3` is instead used as a cost-1 filter, fire is restricted to
cost-1 incoming edges. On every one of the 12 hosts the unread center
has coordinate support `3`. Seed-exit, both-weights-`1`, support drop,
and the corridor-slide `2→2` clause never occur toward that center, so
every incoming `μ` is `1`. The ridge 3→3 clause is live exactly when
the destination has exactly two unit coordinates and the neighbor has
support `3`.

On the six hosts whose unread center has three unit coordinates, or
exactly one unit coordinate, the ridge clause never fires, every
incoming `ρ3` is `1`, `σ_ready = σ`, and leftover-frame-positive `f`
still fires `N_new = 1`.

On the six hosts whose unread center has exactly two unit coordinates,
every support-`3` incoming hop is priced `3`. The only remaining
cost-1 neighbor is the unique support-`2` occupied neighbor. The
filtered occupancy then has weight `1` and no unique full axis, so
`f` is undefined and `N_new = 0`.

Therefore

`N_filt_fire = 6`.

The twelve filter rows are

| `σ` | incoming `ρ3` | `σ_ready` | unique full axis of `σ_ready` | `N_new` |
|---|---|---|---|---|
| `(0, 1, 0, 1, 1, 1)` | `(1, 1, 1, 1)` | `(0, 1, 0, 1, 1, 1)` | `z` | `1` |
| `(0, 1, 1, 0, 1, 1)` | `(3, 3, 1, 3)` | `(0, 0, 0, 0, 1, 0)` | none | `0` |
| `(0, 1, 1, 1, 0, 1)` | `(1, 1, 1, 1)` | `(0, 1, 1, 1, 0, 1)` | `y` | `1` |
| `(0, 1, 1, 1, 1, 0)` | `(3, 1, 3, 3)` | `(0, 0, 1, 0, 0, 0)` | none | `0` |
| `(1, 0, 0, 1, 1, 1)` | `(3, 3, 1, 3)` | `(0, 0, 0, 0, 1, 0)` | none | `0` |
| `(1, 0, 1, 0, 1, 1)` | `(1, 1, 1, 1)` | `(1, 0, 1, 0, 1, 1)` | `z` | `1` |
| `(1, 0, 1, 1, 0, 1)` | `(3, 1, 3, 3)` | `(0, 0, 1, 0, 0, 0)` | none | `0` |
| `(1, 0, 1, 1, 1, 0)` | `(1, 1, 1, 1)` | `(1, 0, 1, 1, 1, 0)` | `y` | `1` |
| `(1, 1, 0, 1, 0, 1)` | `(1, 1, 1, 1)` | `(1, 1, 0, 1, 0, 1)` | `x` | `1` |
| `(1, 1, 0, 1, 1, 0)` | `(1, 3, 3, 3)` | `(1, 0, 0, 0, 0, 0)` | none | `0` |
| `(1, 1, 1, 0, 0, 1)` | `(1, 3, 3, 3)` | `(1, 0, 0, 0, 0, 0)` | none | `0` |
| `(1, 1, 1, 0, 1, 0)` | `(1, 1, 1, 1)` | `(1, 1, 1, 0, 1, 0)` | `x` | `1` |

The ridge-slide extra drops the support-`3` occupied slots on the six
hosts whose destination has exactly two unit coordinates. Unused labels
and the cost-1 filter therefore disagree. Displayed, not adopted.

## Theorem 3 — displayed, not adopted

The counts `N_label_fire = 12` and `N_filt_fire = 6`, the twelve
hosts, the unused-label fire rows, and the cost-1 filter rows are
displayed member data. They are not the framework's fixed
Admissibility rule. This note does not write `ρ3` into
Admissibility. Do not write ρ3 into Admissibility.
Do not attach L1. Occupancy-only formation is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.
Uniqueness not required.

## Honest-auditor / Boundary

- **What is proved.** On the 12 lex-first perp-mask realizing hosts,
  leftover-frame-positive `f` with `ρ3` as unused labels has
  `N_new = 1` on every host, so `N_label_fire = 12`. The same `f`
  with fire restricted to cost-1 edges has `N_filt_fire = 6`.
- **What is displayed only.** The named ridge-slide hop-cost, the
  unused-label versus cost-1 filter split, and both counts are one
  rival table. They are not adopted.
- **What is not claimed.** No attachment of `ρ3` to
  Admissibility; no attachment of L1; no uniqueness of the matching
  member; no leftover of the 12/12 μ label-and-filter count; no axiom
  edit; no formation rate; no compiler no-go.
- **Mutation controls.** A rebuilt `N_label_fire` other than 12
  fails. A rebuilt `N_filt_fire` other than 6 fails. A note that
  writes `ρ3` into Admissibility, attaches L1, claims
  uniqueness, or authors an audit verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| rebuild the 12 bitall lex-first hosts | closed; the twelve rows rebuild |
| score `f` with `ρ3` as unused labels | closed by Theorem 1; each `N_new = 1` |
| report `N_label_fire` | closed by Theorem 1; `N_label_fire = 12` |
| score `f` with fire restricted to cost-1 edges | closed by Theorem 2 |
| report `N_filt_fire` | closed by Theorem 2; `N_filt_fire = 6` |
| treat the μ 12/12 clock-and-filter count as this leftover-frame score | refused; not leftover of the 12/12 μ label-and-filter count |
| write `ρ3` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |
| claim uniqueness | refused; uniqueness not required |

The obligation graph is acyclic. Adoption of `ρ3` is not a proof leaf.

## What This Does Not Claim

- Do not write `ρ3` into Admissibility.
- Do not attach L1.
- Uniqueness is not required and is not claimed.
- The comparison is not leftover of the 12/12 μ label-and-filter count.
- The 12 lex-first perp-mask hosts only.
- No path-length law is attached.
- No Record readout is assigned to a site without a record.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> it does not supply the formation site, probability,
> or rate.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> A readout value is determined by record content alone.

> A site with no record cannot be read.
