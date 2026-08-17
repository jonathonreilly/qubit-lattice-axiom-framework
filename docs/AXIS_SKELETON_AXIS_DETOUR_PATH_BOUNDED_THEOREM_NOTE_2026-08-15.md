---
claim_id: axis_skeleton_axis_detour_path_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A shortest 0→(4,0,0) path under the named axis-skeleton hop-cost leaves the axis and sums to 8. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/axis_skeleton_axis_detour_path_2026_08_15.py
---

# A Lex-First Shortest Axis-Leaving Path To (4,0,0) Under The Axis-Skeleton Hop-Cost

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact shortest-path arithmetic on the six-neighbor cubic graph
about one seed, for the named axis-skeleton hop-cost, exhibiting a
lex-first shortest path from `0` to `(4,0,0)` that leaves the axis.
Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/axis_skeleton_axis_detour_path_2026_08_15.py`](../scripts/axis_skeleton_axis_detour_path_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Fix one seed at the origin of `Z^3` and the six nearest-neighbor steps
`B_6`. For a site `v`, write `σ_v` for the inward-neighbor set toward the
seed: one inward neighbor for each nonzero coordinate of `v`. The inward
weight is `w_v = |σ_v|`. The named axis-skeleton hop-cost on a directed
step `v → w` is

`α(v,w) = 3` if `w_v = 0` or (`w_v = w_w = 1`), else `1`.

The first clause is seed-exit. The second is the remaining axis-skeleton
hop: both endpoints have inward weight `1`. This rule is a displayed
finite member clause, not Admissibility content.

A lexicographically first shortest path from `0` to `(4,0,0)` is the
six-step site list

```text
(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (4,0,0).
```

The six hop costs along it are `3,1,1,1,1,1`. Their orbit-cost sum is
`8`. After the seed, the site `(1,-1,0)` has inward weight `2`, so the
path leaves the axis. The residual is this path type, not leftover of
the arrival number `8`.

The on-axis-only path

```text
(0,0,0) → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0)
```

has hop costs `3,3,3,3` and sums to `12`. It is displayed, not adopted,
and it is not shortest.

Do not write `α` into Admissibility. Do not attach L1. Six-neighbor
graph distance is the hop count, not the named cost.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited lex-first shortest 0→(4,0,0) path under the named axis-skeleton hop-cost leaves the axis and has orbit-cost sum 8. The on-axis-only path costs 12. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: axis_skeleton_axis_detour_path
target_blocker_text: "exhibit a lex-first shortest 0→(4,0,0) path under α that leaves the axis, with hop costs summing to 8"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "keep the named axis-skeleton hop-cost displayed; do not write it into Admissibility; do not attach L1"
conditional_surface_status: "exact on the six-neighbor graph about one seed; no admissibility or metric adoption"
hypothetical_axiom_status: "no edit; α is displayed and is not proposed as axiom content"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence names `Z^3` with
  nearest-neighbor adjacency. The live Admissibility sentence names one
  fixed nearest-neighbor admissibility rule. Both are quoted without
  rewrite. This note does not add a hop-cost to either axiom.
- **Explicit theorem-domain condition:** one seed at the origin; the six
  nearest-neighbor steps `B_6`; inward weights `w_v = |σ_v|`; the named
  rule `α`; the finite ball of six-neighbor graph radius `6` about the
  seed, which contains `(4,0,0)`.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting `α` as a physical cost, writing it
  into Admissibility, attaching L1, and identifying arrival with a
  physical time or metric remain outside the target.

## Exact Objects

Sites are integer triples. The unique seed is `s = (0,0,0)`. The six
nearest-neighbor steps are

`B_6 = {±e_1, ±e_2, ±e_3}`.

The search domain is the finite ball

`Ball_6(s) = { v in Z^3 : six-neighbor graph distance from s to v is at most 6 }`.

It has `377` sites and contains the axis target `(4,0,0)`.

For `v = (v_1,v_2,v_3)` the inward-neighbor set toward the seed is

`σ_v = { v - sgn(v_i) e_i : v_i ≠ 0 }`.

Thus `w_v = |σ_v|` equals the number of nonzero coordinates of `v`, so
`w_s = 0` and `w_{(4,0,0)} = 1`. A directed nearest-neighbor hop `v → w`
carries the ordered inward-weight pair `(w_v, w_w)` and the cost

`α(v,w) = 3` if `w_v = 0` or (`w_v = w_w = 1`), else `1`.

Arrival `t(v)` is the least sum of `α` along a `B_6` path in `Ball_6(s)`
from `s` to `v`. A path is lexicographically first among a set when its
sequence of sites is the least sequence in the dictionary order of
integer triples.

A site after the seed is said to leave the axis when its inward weight
is not `1`. These objects are supplied mathematical data for the
theorems below.

## Theorem 1 — Lex-First Shortest Path, Hop Costs, And Axis Exit

On `Ball_6(s)`, a lexicographically first shortest `s → (4,0,0)` path is

```text
P = (
  (0,0,0),
  (0,-1,0),
  (1,-1,0),
  (2,-1,0),
  (3,-1,0),
  (4,-1,0),
  (4,0,0)
).
```

The six directed hops, inward-weight pairs, and costs are

| hop | pair `(w_v,w_w)` | clause | `α` |
|---|---|---|---:|
| `(0,0,0) → (0,-1,0)` | `(0,1)` | seed-exit | `3` |
| `(0,-1,0) → (1,-1,0)` | `(1,2)` | neither | `1` |
| `(1,-1,0) → (2,-1,0)` | `(2,2)` | neither | `1` |
| `(2,-1,0) → (3,-1,0)` | `(2,2)` | neither | `1` |
| `(3,-1,0) → (4,-1,0)` | `(2,2)` | neither | `1` |
| `(4,-1,0) → (4,0,0)` | `(2,1)` | neither | `1` |

The hop-cost list is `3,1,1,1,1,1`. The orbit-cost sum is
`3+1+1+1+1+1 = 8`. Hence `t(4,0,0) ≤ 8`. The companion runner's Dijkstra
search on `Ball_6(s)` returns the same path and the same value
`t(4,0,0) = 8`, so `P` is shortest.

After the seed, `P` visits `(1,-1,0)`, whose inward weight is `2` and is
therefore not `1`. The path leaves the axis. The residual is this
leaving path type, not leftover of the arrival number.

## Theorem 2 — The On-Axis-Only Path Costs 12

The on-axis-only path that stays on the first coordinate axis is

```text
A = (
  (0,0,0),
  (1,0,0),
  (2,0,0),
  (3,0,0),
  (4,0,0)
).
```

Its four hops are seed-exit then three both-weights-`1` axis-skeleton
hops, so the hop-cost list is `3,3,3,3` and the sum is `12`. Displayed,
not adopted.

Every site of `A` after the seed has inward weight `1`. That path does
not leave the axis. Because `12 > 8`, `A` is not shortest. The cheap
detour undercuts the on-axis-only word.

## Theorem 3 — Displayed, Not Adopted

Do not write `α` into Admissibility. The live Admissibility sentences
remain the quoted nearest-neighbor distribution rule. They do not name
inward weights, seed-exit, axis-skeleton cost, or a numerical hop-cost.

Do not attach L1. Do not identify the named hop-cost with six-neighbor graph distance. The integer `8` is the orbit-cost sum along the exhibited path type, not an L1 length.

The rule and the path are displayed, not adopted. Uniqueness of `α`
among cost rules is not claimed.

## Proof-Obligation Boundary

| Obligation | Disposition |
|---|---|
| one seed and the six-neighbor stencil | supplied domain |
| inward weights and the named rule `α` | supplied display |
| lexicographically first shortest path | computed; listed in Theorem 1 |
| six hop costs and their sum | computed; orbit-cost table; sum `8` |
| some post-seed site has weight not `1` | `(1,-1,0)` has weight `2` |
| on-axis-only path cost | displayed; sum `12`; not adopted |
| `α` written into Admissibility | refused |
| L1 attached as the residual | refused |

## What This Does Not Claim

- `α` is not Admissibility content and is not a new axiom.
- The arrival number is not adopted as a physical time, rate, or metric.
- No hop-cost uniqueness theorem is claimed.
- L1 is not attached and is not the named residual.
- Sites outside `Ball_6(s)` and stencils other than `B_6` are outside
  the theorem.
- No formation process, record lock, or readout value is derived.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is
> determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

> A readout value is determined by record content alone.

> A site with no record cannot be read.

Their dependency role is limited to the repository's lattice and
admissibility vocabulary. Record supplies no hop-cost. This theorem
separately supplies the named hop-cost as displayed data. No axiom
sentence is edited.

## Runner Contract

The companion runner constructs `Ball_6(s)`, computes Dijkstra arrival
from the seed under `α`, extracts the lexicographically first shortest
path to `(4,0,0)`, and sums the six computed hop costs. It checks that
some site after the seed has inward weight not `1`. It scores the
on-axis-only path at `12`. It quotes the live Admissibility sentences,
checks that the axiom memo is not edited, and checks that the note keeps
`α` displayed and does not attach L1. Declared review inputs are this
note and the axiom memo only.
