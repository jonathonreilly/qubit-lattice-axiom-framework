---
claim_id: max3_out_face_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named max≥3 out-face hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/max3_out_face_samek_k1_b6_2026_08_15.py
---

# Same-k Reverse At k=1 Under The Named Max≥3 Out-Face Hop-Cost On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=1 on the finite nearest-neighbor
graph `B_6(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/max3_out_face_samek_k1_b6_2026_08_15.py`](../scripts/max3_out_face_samek_k1_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named max≥3 out-face hop-cost `d3` is the
first display of `d3`. The parent clauses `ν`, `μ`, and `ρ3` are those of
the ridge-slide same-k scoring on this ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `d3(v→w) = 3` if `ρ3` would be `3` or (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 3`), else `1`.

The extra clause is a max≥3 out-face hop: support stays `2`, the destination
max absolute coordinate grows, and the source max is already at least `3`.
It fires on `(3,2,0) → (4,2,0)`. It does not fire on the deep-out hop
`(2,2,0) → (3,2,0)`, whose source max is `2`, nor on the unit-out-face hop
`(1,1,0) → (2,1,0)`, whose source max is `1`. That unit-out hop remains
priced at `3` by corridor-slide `μ`, which is already inside `ρ3`. The
skipped deep-out hop stays at `ρ3 = 1`, so `d3 = 1` there. The deep-out-face
rule that prices growing-max `2→2` hops already at source max `2` is not the
displayed rule. Uniqueness is not claimed.

The finite host is scored independently: one origin Dijkstra is run on this
ball. The ball is not leftover of a larger-ball table.

```text
B_6(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 6 }.
```

It has 377 sites. Edges are the cubic nearest-neighbor steps that remain
inside `B_6(0)`. One Dijkstra from the origin yields

```text
t(1,0,0) = 3
t(1,1,1) = 5
```

The same-k comparison at k=1 is

```text
t(1,0,0)^2 / 1 = 9 > 25/3 = t(1,1,1)^2 / 3.
```

Equivalently `27 > 25`. The inequality holds. Same-k reverse holds at k=1.
Displayed, not adopted.

The extra `2→2` clause is live on this host. The hop `(3,2,0) → (4,2,0)` has
`d3=3` and `ρ3=1`, and both ends lie in `B_6(0)`. Therefore `ρ3` cannot
price the max≥3 out-face hop. The displayed body last hop `(1,1,0) → (1,1,1)`
keeps cost `1`. The skipped hop `(2,2,0) → (3,2,0)` has `d3=1`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_6(0) reports t(1,0,0) and t(1,1,1) under the named max≥3 out-face hop-cost and scores the k=1 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: max3_out_face_samek_k1_b6
target_blocker_text: "whether same-k reverse at k=1 still holds after max≥3 out-face 2-to-2 hops are priced at 3"
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
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `d3` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_6(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`, and
  `d3` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `d3` into Admissibility, selecting it as
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

`d3` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`d3`, using one Dijkstra on `B_6(0)`.

An explicit axis path is the single hop `(0,0,0) → (1,0,0)` of cost `3`.
An explicit body path is

```text
(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1)
```

with costs `3+1+1=5`. Every path has first hop cost `3`, and every hop costs
at least `1`, so these paths are optimal once Dijkstra matches them.

On the max≥3 out hop `(3,2,0) → (4,2,0)` one has `|σ_v|=|σ_w|=2`, dest max
`4` greater than source max `3`, and source max already `3`, so `ρ3 = 1`
while `d3 = 3`. On the deep-out hop `(2,2,0) → (3,2,0)` the extra clause is
idle because the source max is `2`; both `ρ3` and `d3` cost `1`. On the
unit-out hop `(1,1,0) → (2,1,0)` the extra clause is idle because the source
max is `1`; corridor-slide already prices that hop at `3`. On the body hop
`(1,0,0) → (1,1,0)` both `ρ3` and `d3` cost `1`. On the interior `3→3` hop
`(2,2,2) → (3,2,2)` the destination has no unit coordinate, so both `ρ3`
and `d3` cost `1`.

## Theorem 1 — Arrival times at k=1

Under `d3` on `B_6(0)`,

```text
t(1,0,0) = 3
t(1,1,1) = 5
```

The runner computes both values from the single origin Dijkstra and checks
them against the explicit paths above. These values are Dijkstra outputs,
not fitted scalars.

## Theorem 2 — Same-k comparison at k=1

The displayed comparison is whether

```text
t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3.
```

Substituting the computed times gives the integer statement `9 > 25/3`, or
equivalently `27 > 25`. The inequality holds. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write d3 into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `d3`, `ρ3`, `μ`, or `ν`. This note
proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=1.
- The live `2→2` clause on `B_6(0)` is not a statement about larger hosts.
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
checks the integer form of Theorem 2, checks that the extra `2→2` clause is
live on in-host hops at cost `3`, skips `(2,2,0) → (3,2,0)` as a new tax,
and fires `(3,2,0) → (4,2,0)`, checks that the live Admissibility wording
does not name `d3`, and records the import boundary. Declared review inputs
are this note and the axiom memo only.
