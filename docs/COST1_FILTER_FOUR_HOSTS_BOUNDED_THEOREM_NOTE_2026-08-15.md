---
claim_id: cost1_filter_four_hosts_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "The 4 of 12 perp-mask hosts on which leftover-frame fire survives a cost-1 hop-cost filter are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cost1_filter_four_hosts_2026_08_15.py
---

# Cost-1 Filter: Four Surviving Hosts (Bounded Theorem)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** the 12 lex-first realizing 3-ball hosts of the perpendicular
weight-4 occupancy masks from bitall. On each host, leftover-frame-positive
`f` is scored with fire restricted to cost-1 incoming edges of the named
hop cost `ρ`. The 4 masks (and lex-first hosts) with `N_new = 1` are named
in bitall order, and the other 8 with `N_new = 0` are displayed. The 12
lex-first perp-mask hosts only. Uniqueness is not required. Displayed, not
adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cost1_filter_four_hosts_2026_08_15.py`](../scripts/cost1_filter_four_hosts_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

## Result Up Front

Investment clkonly: leftover-frame fire scored with hop-cost as unused
labels versus as a cost-1 readiness filter has `N_label_fire = 12` and
`N_filt_fire = 4`. New residual: exhibit the 4 lex-first perp-mask
hosts on which leftover-frame fire still has `N_new = 1` when restricted
to cost-1 edges, and the 8 on which it dies. This is not leftover of the
12/4 counts. Uniqueness not required. Do not attach L1.

Direction order is

`(+x, −x, +y, −y, +z, −z)`.

The 12 rows are the bitall / bitreal Theorem 2 hosts: for each
perpendicular weight-4 mask, the lex-first `(centers, radii, v)` whose
unread 6-NN occupancy equals that mask. On each host, `t` is the
seed-radii ℓ¹ lock tick on occupied neighbors, `b` is read from the
unique full axis, and `f` is the leftover-frame-positive July-3 pair
member of `(σ,b)`.

`f` is the leftover-frame-positive pair section. The named hop cost is

`ρ = 3` iff equal inward weight or seed-exit, else `1`.

Inward occupation at a site `x` uses the same seed-distance already
used for lock-ticks,

`d(x) = min_i ‖x − s_i‖_1`,

with a direction bit set exactly when the neighbor is strictly nearer
the nearest seed. Inward weight is the number of such bits. Seed-exit
means the source has inward weight `0`.

**Theorem 1.** The 4 masks, in bitall order, on which leftover-frame
fire still has `N_new = 1` under the cost-1 filter are

`(0, 1, 1, 1, 1, 0)`,
`(1, 0, 1, 1, 1, 0)`,
`(1, 1, 0, 1, 1, 0)`,
`(1, 1, 1, 0, 1, 0)`.

**Theorem 2.** The other 8 have `N_new = 0` under that filter.
Displayed, not adopted.

**Theorem 3.** Displayed, not adopted. Do not write `f` or `ρ` into
Admissibility. Do not write f or ρ into Admissibility.
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
hop cost `ρ` as the framework's fixed rule. Record permanence is used
only to keep the locks on each `U`. Formation site and rate remain
outside the axiom memo. Qubit remains `M_2(C)`. No axiom edit.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite exact naming of the 4 of 12 lex-first perp-mask hosts on which leftover-frame-positive f still has N_new=1 under a cost-1 hop-cost readiness filter, and of the 8 on which N_new=0. Displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: cost1_filter_four_hosts
target_blocker_text: "which 4 of the 12 lex-first perp-mask hosts keep leftover-frame fire under a cost-1 hop-cost filter, and which 8 die"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the named 4 surviving hosts and the 8 dying hosts; do not write f or rho into Admissibility or attach L1"
conditional_surface_status: "exact on the 12 lex-first realizing hosts; 4 named survivors with N_new=1; 8 displayed deaths with N_new=0; displayed, not adopted"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Slots are `(+x, −x, +y, −y, +z, −z)`. Occupancy at an unread site `v`
relative to a locked set `U` is the 6-bit indicator

`σ(U, v)_μ = 1` if and only if `v + e_μ ∈ U`.

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
`−`, full-axis `+` letter). The section `f` takes the unique completion
of sign `+1`. A displayed pair step at an unread site forms that site
if and only if the encoded 6-tuple lies in the pair; existing locks are
not removed. `N_new = 1` and `U` persists exactly when that step forms
`v` and leaves every lock of `U` in place.

Inward occupation at `x` is the 6-bit string whose direction bit is
set exactly when `d` of the neighbor is strictly less than `d(x)`. On
a directed nearest-neighbor edge `x → y`,

`ρ(x → y) = 3` if `|σ_in(x)| = |σ_in(y)|` or `|σ_in(x)| = 0`, else `1`.

If `ρ` is used as a readiness filter, an occupied neighbor participates
in the pair step only when the directed edge from that neighbor to `v`
has cost `1`. The filtered occupancy is `σ_ready`. Leftover-frame-positive
`f` is then evaluated on `(σ_ready, b)` when `σ_ready` still has a unique
full axis, and is undefined otherwise. `N_new` under the filter is `1`
exactly when that filtered section is defined, lies in the pair, and
forms the unread host site.

The 12 lex-first perp-mask hosts only.

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

## Theorem 1 — four cost-1 survivors, bitall order

On each of the 12 lex-first realizing hosts, fire is restricted to
cost-1 incoming edges. Four hosts have every incoming occupied edge of
cost `1`, so `σ_ready = σ` and leftover-frame-positive `f` still fires
`N_new = 1`. Those four masks, listed in the bitall order of the 12
perp-mask hosts, are

`(0, 1, 1, 1, 1, 0)`,
`(1, 0, 1, 1, 1, 0)`,
`(1, 1, 0, 1, 1, 0)`,
`(1, 1, 1, 0, 1, 0)`.

The four lex-first hosts are exactly those whose occupancy has `+z` occupied and `−z` empty. On those four, every incoming inward weight is
unequal to the unread center, so every incoming `ρ` is `1`.

The four filter-surviving rows are

| `σ` | lex-first `(centers, radii, v)` | incoming `ρ` | `σ_ready` | unique full axis of `σ_ready` | `f(σ,b)` | `N_new` |
|---|---|---|---|---|---|---|
| `(0, 1, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-1, -1, -2))` | `(1, 1, 1, 1)` | `(0, 1, 1, 1, 1, 0)` | `y` | `(0, −, −, +, +, 0)` | `1` |
| `(1, 0, 1, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (-2, 0, -2)), (1, 2, 1), (-3, -1, -2))` | `(1, 1, 1, 1)` | `(1, 0, 1, 1, 1, 0)` | `y` | `(+, 0, −, +, −, 0)` | `1` |
| `(1, 1, 0, 1, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -1, -2))` | `(1, 1, 1, 1)` | `(1, 1, 0, 1, 1, 0)` | `x` | `(−, +, 0, +, −, 0)` | `1` |
| `(1, 1, 1, 0, 1, 0)` | `(((-2, -2, -2), (-2, -2, -1), (0, -2, -2)), (1, 2, 1), (-1, -3, -2))` | `(1, 1, 1, 1)` | `(1, 1, 1, 0, 1, 0)` | `x` | `(−, +, −, 0, +, 0)` | `1` |

This is not leftover of the 12/4 counts: the clkonly investment reports
how many hosts survive the filter, and this note names which four
survive, in bitall order.

## Theorem 2 — the other eight die

The remaining eight hosts drop at least one occupied slot of the unique
full axis, so `σ_ready` has no unique full axis and leftover-frame-positive
`f` is not defined on the filtered star. Those eight have `N_new = 0`.
Displayed, not adopted.

The eight dying masks, in bitall order, are

`(0, 1, 0, 1, 1, 1)`,
`(0, 1, 1, 0, 1, 1)`,
`(0, 1, 1, 1, 0, 1)`,
`(1, 0, 0, 1, 1, 1)`,
`(1, 0, 1, 0, 1, 1)`,
`(1, 0, 1, 1, 0, 1)`,
`(1, 1, 0, 1, 0, 1)`,
`(1, 1, 1, 0, 0, 1)`.

The eight filter-death rows are

| `σ` | incoming `ρ` | `σ_ready` | unique full axis of `σ_ready` | `N_new` |
|---|---|---|---|---|
| `(0, 1, 0, 1, 1, 1)` | `(1, 1, 3, 3)` | `(0, 1, 0, 1, 0, 0)` | none | `0` |
| `(0, 1, 1, 0, 1, 1)` | `(1, 1, 3, 3)` | `(0, 1, 1, 0, 0, 0)` | none | `0` |
| `(0, 1, 1, 1, 0, 1)` | `(1, 3, 1, 1)` | `(0, 1, 0, 1, 0, 1)` | none | `0` |
| `(1, 0, 0, 1, 1, 1)` | `(1, 1, 3, 3)` | `(1, 0, 0, 1, 0, 0)` | none | `0` |
| `(1, 0, 1, 0, 1, 1)` | `(1, 1, 3, 3)` | `(1, 0, 1, 0, 0, 0)` | none | `0` |
| `(1, 0, 1, 1, 0, 1)` | `(1, 3, 1, 1)` | `(1, 0, 0, 1, 0, 1)` | none | `0` |
| `(1, 1, 0, 1, 0, 1)` | `(3, 1, 1, 1)` | `(0, 1, 0, 1, 0, 1)` | none | `0` |
| `(1, 1, 1, 0, 0, 1)` | `(3, 1, 1, 1)` | `(0, 1, 1, 0, 0, 1)` | none | `0` |

On each of these eight, at least one incoming edge is equal-weight
cost `3` and that slot is dropped. Displayed, not adopted.

## Theorem 3 — displayed, not adopted

The four named surviving masks and hosts, the eight dying masks, and
the filter rows are displayed member data. They are not the
framework's fixed Admissibility rule. This note does not write `f` or
`ρ` into Admissibility. Do not write f or ρ into Admissibility.
Do not attach L1. Occupancy-only formation is not attached. Qubit
remains `M_2(C)`. No approved primitive is added. No axiom edit.
Uniqueness not required.

## Honest-auditor / Boundary

- **What is proved.** On the 12 lex-first perp-mask realizing hosts,
  leftover-frame-positive `f` with fire restricted to cost-1 edges has
  `N_new = 1` on exactly the four named bitall-order masks
  `(0, 1, 1, 1, 1, 0)`, `(1, 0, 1, 1, 1, 0)`, `(1, 1, 0, 1, 1, 0)`,
  `(1, 1, 1, 0, 1, 0)`, and `N_new = 0` on the other eight.
- **What is displayed only.** The named hop cost, the cost-1 readiness
  filter, the four surviving hosts, and the eight dying hosts are one
  rival table. They are not adopted.
- **What is not claimed.** No attachment of `f` or `ρ` to
  Admissibility; no attachment of L1; no uniqueness of the matching
  member; no leftover of the 12/4 counts; no axiom edit; no formation
  rate; no compiler no-go.
- **Mutation controls.** A rebuilt survivor list other than the four
  named bitall-order masks fails. A rebuilt death list other than the
  eight named masks fails. A note that writes `f` or `ρ` into
  Admissibility, attaches L1, claims uniqueness, leftovers the 12/4
  counts, or authors an audit verdict fails.

This note authors no audit verdict.

## Proof-Obligation Graph

| Obligation | Disposition |
|---|---|
| rebuild the 12 bitall lex-first hosts | closed; the twelve rows rebuild |
| name the 4 cost-1 survivors in bitall order | closed by Theorem 1 |
| score `f` with fire restricted to cost-1 edges on those 4 | closed by Theorem 1; each `N_new = 1` |
| name the other 8 with `N_new = 0` | closed by Theorem 2 |
| treat the 12/4 counts as already naming the hosts | refused; not leftover of the 12/4 counts |
| write `f` or `ρ` into Admissibility | refused; Theorem 3 |
| attach L1 | refused; Theorem 3 |
| claim uniqueness | refused; uniqueness not required |

The obligation graph is acyclic. Adoption of `f` or of `ρ` is not a
proof leaf.

## What This Does Not Claim

- Do not write `f` or `ρ` into Admissibility.
- Do not attach L1.
- Uniqueness is not required and is not claimed.
- The comparison is not leftover of the 12/4 counts.
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
