---
claim_id: support_drop_filter_fire_edge_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The leftover-frame fire edge on the uneqrad host has support-drop cost 1, so a cost-1 filter does not kill fire. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_filter_fire_edge_2026_08_15.py
---

# Support-Drop Cost Of The Leftover-Frame Fire Edge (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one host, the uneqrad lex-first breaker, plus the 12-count
check `N_filt_fire` on the 12 lex-first perp-mask hosts. On the uneqrad
host, leftover-frame fire edges of leftover-frame-positive `f` are scored
with the named support-drop hop cost `ν`. Report which of those edges
have `ν`-cost 1, and confirm that the fire slot is among them. Displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_filter_fire_edge_2026_08_15.py`](../scripts/support_drop_filter_fire_edge_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment nuclk: `N_filt_fire=12` under `ν`, versus 4 under `ρ`. New
residual: on the uneqrad lex-first host, report which leftover-frame fire
edges have `ν`-cost 1, and confirm the fire slot is among them. Not
leftover of the 12/12 count. Do not attach L1.

Host `U` is the uneqrad lex-first breaker. Direction order is

`(+x, −x, +y, −y, +z, −z)`.

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`,

unread center `v = (−3,−3,−1)`. Occupancy and lock-ticks are

`σ = (1, 0, 1, 0, 1, 1)`, `t = (1, ·, 1, ·, 3, 2)`.

The unique full axis is `z`. The age bit is `b = [t(−z) < t(+z)] = 1`.
The leftover-frame-positive section is

`f = (+, 0, −, 0, +, −)`.

Write `|σ_x|` for the number of nonzero coordinates of `x ∈ Z^3`. The
named support-drop hop cost, as in noshrt, is

`ν(x→y) = 3` if `|σ_x|=0` or `(|σ_x|=|σ_y|=1)` or `|σ_y| < |σ_x|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third
is support drop. Those three clauses are the whole rule.

A leftover-frame fire edge is a directed incoming nearest-neighbor edge
from an occupied leftover-frame neighbor of `v` to `v`. The leftover
frame on this star is the occupied pair `{+x, +y}`. The fire slot of `f`
is the leftover `+` slot, here `+x`. The directed fire edge of `f` is
that slot's incoming edge.

**Theorem 1.** The directed fire edge of `f` on `U` has `ν`-cost 1. Both
leftover-frame fire edges have `ν`-cost 1, and the fire slot is among
them.

**Theorem 2.** `N_filt_fire = 12` on the 12 lex-first perp-mask hosts
(nuclk). Displayed, not adopted.

**Theorem 3.** Displayed, not adopted. Do not write f or ν into Admissibility. Do not attach L1. Qubit remains `M_2(C)`. No axiom edit.

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
support-drop hop cost `ν` as the framework's fixed rule. Record permanence
is used only to keep the locks on `U`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact incoming support-drop costs of leftover-frame fire edges on one uneqrad host, plus the exact 12-host N_filt_fire count. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: support_drop_filter_fire_edge
target_blocker_text: "on the uneqrad lex-first host, which leftover-frame fire edges have nu-cost 1, and whether the fire slot is among them"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the uneqrad leftover-frame fire-edge nu costs and of N_filt_fire=12; do not write f or nu into Admissibility or attach L1"
conditional_surface_status: "exact on the uneqrad lex-first breaker plus the 12-count; directed fire edge has nu-cost 1; N_filt_fire=12; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `s1 = (−2,−2,−2)`, `s2 = (−2,−2,−1)`, and `s3 = (−2,−2,1)`. The
closed ℓ¹ ball of radius `r` is

`B_r(c) = { x ∈ Z^3 : ‖x − c‖_1 ≤ r }`.

The locked set is

`U = B_2((−2,−2,−2)) ∪ B_1((−2,−2,−1)) ∪ B_3((−2,−2,1))`.

The unread site is `v = (−3,−3,−1)`. Then
`‖v − s1‖_1 = 3 > 2`, `‖v − s2‖_1 = 2 > 1`, and
`‖v − s3‖_1 = 4 > 3`, so `v ∉ U`. Occupied nearest neighbors and
lock-ticks are

| slot | neighbor | in `U` | lock tick |
|---|---|---|---|
| `+x` | `(−2,−3,−1)` | yes | `1` |
| `−x` | `(−4,−3,−1)` | no | none |
| `+y` | `(−3,−2,−1)` | yes | `1` |
| `−y` | `(−3,−4,−1)` | no | none |
| `+z` | `(−3,−3,0)` | yes | `3` |
| `−z` | `(−3,−3,−2)` | yes | `2` |

so `σ = (1, 0, 1, 0, 1, 1)` and `t = (1, ·, 1, ·, 3, 2)`. The unique
full axis is `z`. The age bit is `b = [t(−z) < t(+z)] = 1`. Letters are
`{0, +, −}` with encode `0 ↦ 0`, `+ ↦ 1`, `− ↦ 2`. Completions of
`(σ,b)` write `+` on `+z` and `−` on `−z`. The leftover-frame sign of a
completion is the determinant of the ordered triple of directions
(leftover `+`, leftover `−`, full-axis `+` letter). The section `f`
takes the unique completion of sign `+1`,

`f = (+, 0, −, 0, +, −)`.

Leftover occupied slots are `+x` and `+y`. The leftover `+` letter of
`f` sits on `+x`, so the fire slot is `+x`. The leftover-frame fire
edges are the directed incoming hops

`(+x) : (−2,−3,−1) → (−3,−3,−1)`,
`(+y) : (−3,−2,−1) → (−3,−3,−1)`.

Those two code spans are
`(−2,−3,−1) → (−3,−3,−1)`
and
`(−3,−2,−1) → (−3,−3,−1)`.

The directed fire edge of `f` is the fire-slot hop
`(−2,−3,−1) → (−3,−3,−1)`.

The 12 lex-first perp-mask hosts are the bitall / bitreal Theorem 2
rows used by nuclk. On each of those hosts, leftover-frame-positive
`f` is evaluated with fire restricted to incoming cost-1 edges.
`N_filt_fire` is how many of those 12 still have `N_new = 1`.

One host plus the 12-count check.

## Theorem 1 — the directed fire edge has `ν`-cost 1

On `U`, coordinate supports of the leftover-frame sources and of `v`
are

`|σ_(−2,−3,−1)| = 3`, `|σ_(−3,−2,−1)| = 3`, `|σ_v| = 3`.

Neither hop is seed-exit, neither hop has both weights `1`, and neither
hop drops support. Therefore both leftover-frame fire edges have

`ν((−2,−3,−1) → (−3,−3,−1)) = 1`,
`ν((−3,−2,−1) → (−3,−3,−1)) = 1`.

The leftover-frame fire edges of `ν`-cost 1 are `{+x, +y}`. The fire
slot `+x` is among them. The directed fire edge of `f` is the `+x`
incoming hop, so that edge has `ν`-cost 1.

The two full-axis incoming hops likewise have `ν`-cost 1
(`(−3,−3,0)` has support `2` and `(−3,−3,−2)` has support `3`; neither
drops toward `v`). They are not leftover-frame fire edges. They are
recorded only to show that a cost-1 filter on this host drops no
occupied slot.

This is not leftover of the 12/12 count. The 12-count is a host-wise
fire tally on the bitall lex-first realizing rows. The present residual
names the leftover-frame incoming edges on the uneqrad breaker, whose
third center and radii are `((−2,−2,1), 3)`, not the bitall row for
the same mask.

## Theorem 2 — `N_filt_fire = 12` on the 12 lex-first perp-mask hosts

On each of the 12 lex-first perp-mask hosts the unread center has
coordinate support `3`, and every occupied neighbor has coordinate
support `2` or `3`. Seed-exit and both-weights-`1` never occur.
Support drop never occurs toward that center. Every incoming `ν` is
`1`, so `σ_ready = σ` and leftover-frame-positive `f` still fires
`N_new = 1`. Therefore

`N_filt_fire = 12`.

Displayed, not adopted. The 12-count is the nuclk Theorem 2 score. It
is displayed here only as the 12-count check. It does not replace
Theorem 1.

## Theorem 3 — displayed, not adopted

The leftover-frame fire-edge costs on the uneqrad host, the fire slot
`+x`, and the count `N_filt_fire = 12` are displayed member data. They
are not the framework's fixed Admissibility rule. This note does not
write `f` or `ν` into Admissibility. Do not write f or ν into Admissibility. Do not attach L1. Occupancy-only formation is not
attached. Qubit remains `M_2(C)`. No approved primitive is added. No
axiom edit.

## Honest-auditor / Boundary

- **What is proved.** On the uneqrad lex-first breaker, both leftover-
  frame fire edges have `ν`-cost 1. The directed fire edge of `f` has
  `ν`-cost 1. The fire slot `+x` is among the cost-1 leftover-frame
  fire edges. On the 12 lex-first perp-mask hosts, `N_filt_fire = 12`.
- **What is displayed only.** The named support-drop hop cost, the
  leftover-frame fire edges, and the 12-count are one rival table.
  They are not adopted.
- **What is not claimed.** No attachment of `f` or `ν` to
  Admissibility; no attachment of L1; no leftover of the 12/12 count;
  no axiom edit; no formation rate; no compiler no-go.
- **Mutation controls.** A rebuilt directed-fire-edge cost other than
  1 fails. A rebuilt leftover-frame cost-1 set that omits the fire
  slot `+x` fails. A rebuilt `N_filt_fire` other than 12 fails. A note
  that writes `f` or `ν` into Admissibility, attaches L1, treats the
  edge list as leftover of the 12/12 count, or authors an audit
  verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| rebuild the uneqrad lex-first breaker | closed; `U`, `v`, `σ`, `t`, `b`, `f` rebuild |
| name leftover-frame fire edges and the fire slot | closed; edges `{+x, +y}`, fire slot `+x` |
| score those edges with `ν` | closed by Theorem 1; both have cost 1 |
| confirm the fire slot is among the cost-1 edges | closed by Theorem 1 |
| confirm the directed fire edge has `ν`-cost 1 | closed by Theorem 1 |
| report `N_filt_fire` on the 12 lex-first hosts | closed by Theorem 2; `N_filt_fire = 12` |
| treat the edge list as leftover of the 12/12 count | refused; not leftover of the 12/12 count |
| write `f` or `ν` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |

The obligation graph is acyclic. Adoption of `f` or of `ν` is not a
proof leaf.

## What This Does Not Claim

- Do not write `f` or `ν` into Admissibility.
- Do not attach L1.
- The comparison is not leftover of the 12/12 count.
- One host plus the 12-count check.
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
