---
claim_id: mid_leave_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named mid-leave hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/mid_leave_samek_k1_b6_2026_08_15.py
---

# Same-k Reverse At k=1 Under The Named Mid-Leave Hop-Cost On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=1 on the finite nearest-neighbor
graph `B_6(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/mid_leave_samek_k1_b6_2026_08_15.py`](../scripts/mid_leave_samek_k1_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

This is the first display of the named mid-leave hop-cost `μλ`. Write
`|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named costs `ν`, `μ`, and `ρ3` are those
of the ridge-slide display, and `μλ` is `ρ3` plus one extra 1→2 clause:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `μλ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=1` and `|σ_w|=2` and
  `max_i |w_i|=1` and `max_i |v_i| ≥ 2)`, else `1`.

The finite host is

```text
B_6(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 6 }.
```

It has 377 sites. Edges are the cubic nearest-neighbor steps that remain
inside `B_6(0)`. The ball is not leftover of a larger-ball table: one
Dijkstra from the origin is run on this ball.

On a nearest-neighbor hop, a support-1 source with `max_i |v_i| ≥ 2` that
gains a second coordinate keeps that large coordinate, so the destination
cannot have `max_i |w_i|=1`. The extra clause is therefore empty on the
graph of `B_6(0)`, and `μλ` agrees with `ρ3` on every remaining edge.
The unit-cube leave `(1,0,0) → (1,1,0)` has source max `1`, so it stays
cost `1`. The dest-max-at-least-two leave `(2,0,0) → (2,1,0)` is not the
extra clause and also stays cost `1` under `μλ`.

One Dijkstra from the origin yields

```text
t(1,0,0) = 3
t(1,1,1) = 5
```

The same-k comparison at k=1 is

```text
t(1,0,0)^2 / 1 = 9 > 25/3 = t(1,1,1)^2 / 3.
```

Equivalently `27 > 25`. The inequality holds. Same-k reverse holds at
k=1. Displayed, not adopted. Independently, the axis endpoint of this
ball is `t(6,0,0) = 18`. Uniqueness is not claimed.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_6(0) reports t(1,0,0) and t(1,1,1) under the named mid-leave hop-cost and scores the k=1 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: mid_leave_samek_k1_b6
target_blocker_text: "whether same-k reverse at k=1 still holds after the mid-leave clause is added to the ridge-slide hop-cost"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_6(0) under the named hop-cost; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `μλ` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_6(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`, and
  `μλ` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `μλ` into Admissibility, selecting it as
  a physical cost, or lifting the comparison off `B_6(0)` remain separate
  obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

`μλ` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`μλ`, using one Dijkstra on `B_6(0)`.

An explicit axis path is the single hop `(0,0,0) → (1,0,0)` of cost `3`.
An explicit body path is

```text
(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1)
```

with costs `3+1+1=5`. Every path has first hop cost `3`, and every hop costs
at least `1`, so these paths are optimal once Dijkstra matches them.

## Named Rule

Let `B_6(0) = { v ∈ Z^3 : |v|_1 ≤ 6 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_6(0)`,
`t(v)` is the least sum of `μλ` along a directed path from `0` to `v` in
that graph.

The extra clause asks for a 1→2 hop whose destination has all coordinates
of absolute value at most `1` and whose source already has some coordinate
of absolute value at least `2`. No nearest-neighbor edge of `B_6(0)` meets
both conditions at once. The displayed rule is therefore a first naming of
that conjunction, not a change of any remaining nearest-neighbor price
relative to `ρ3`.

## Theorem 1 — Arrival times at k=1

Under `μλ` on `B_6(0)`,

```text
t(1,0,0) = 3
t(1,1,1) = 5
```

The runner computes both values from the single origin Dijkstra and checks
them against the explicit paths above. Every listed site lies in `B_6(0)`.
These values are Dijkstra outputs, not fitted scalars.

## Theorem 2 — Same-k comparison at k=1

The displayed comparison is whether

```text
t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3.
```

Substituting the computed times gives the integer statement `9 > 25/3`, or
equivalently `3 t(1,0,0)^2 ? t(1,1,1)^2`. That is `27 > 25`. The
inequality holds. Arrival per Euclidean length is larger at `(1,0,0)` than
at `(1,1,1)`. Same-k reverse at k=1 is yes. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write μλ into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `μλ`, `ρ3`, `μ`, or `ν`. This note
proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- Uniqueness is not claimed for this named hop-cost at k=1.
- The empty extra clause on nearest-neighbor edges of `B_6(0)` is not a
  statement about larger hosts or about non-nearest-neighbor steps.
- No physical identification of `t` as a clock, mass, or force law is made.
- No claim is made that Record locks these arrival times.
- Independent leftovers on larger balls are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

> A site with no record cannot be read.

Their dependency role is limited to the repository's site graph and the
refusal to treat a named hop-cost as axiom content.

## Runner Contract

The companion runner builds `B_6(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(1,0,0)` and `t(1,1,1)`,
checks the integer form of Theorem 2, checks that the extra mid-leave
clause fires on no nearest-neighbor edge while sparing the unit-cube 1→2,
checks that the live Admissibility wording does not name `μλ`, and records
the import boundary. Declared review inputs are this note and the axiom
memo only.
