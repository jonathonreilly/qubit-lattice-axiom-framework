---
claim_id: c2d4_interior_cost2_samek_k18_b54_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=18 under the named c2d4-plus-interior hop-cost on B_54(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_interior_cost2_samek_k18_b54_2026_08_15.py
---

# Same-k Reverse At k=18 Under The Named C2d4-Plus-Interior Hop-Cost On B_54(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=18 on the finite nearest-neighbor
graph `B_54(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_interior_cost2_samek_k18_b54_2026_08_15.py`](../scripts/c2d4_interior_cost2_samek_k18_b54_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named c2d4-plus-interior hop-cost `i2` is
the first display of `i2` at k=18, the last parent same-k hold scale before
the shared wall. The parent clauses `ν`, `μ`, `ρ3`, and `c2d4` are those of
the ridge-slide and cost-2 max≥4 out-face same-k scoring on this ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`;
- `i2(v→w) = 3` if `ρ3` would be `3`, else `2` if `c2d4` would be `2` or
  (`|σ_v|=|σ_w|=3` and `min_i |w_i| ≥ 2`), else `1`.

So `i2` equals `3` if `ρ3` would be `3`. Otherwise it prices at `2` the
parent max≥4 out-face hops already priced at `2` by `c2d4`, and also the
interior body hops: support stays `3` and every absolute destination
coordinate is at least `2`. It fires on `(2,2,1) → (2,2,2)` at cost `2`.
It does not fire on the body last hop `(1,1,0) → (1,1,1)`, which is not a
`3→3` hop, nor on `(2,2,2) → (1,2,2)`, whose destination has a unit
coordinate. That last hop remains priced at `1`. The parent `c2d4` prices
`(2,2,1) → (2,2,2)` at `1`. Uniqueness is not claimed.

The finite host is scored independently: one origin Dijkstra is run on this
ball. The ball is not leftover of a larger-ball table.

```text
B_54(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 54 }.
```

It has 215929 sites (215928 nonzero). Edges are the cubic nearest-neighbor
steps that remain inside `B_54(0)`. One Dijkstra from the origin yields

```text
t(18,0,0) = 34
t(18,18,18) = 75
```

The same-k comparison at k=18 is

```text
t(18,0,0)^2 / 324 = 1156/324  versus  5625/972 = t(18,18,18)^2 / 972.
```

Equivalently whether `3468 > 5625`. The inequality does not hold. Same-k
reverse at k=18 under `i2` is no. Displayed, not adopted.

The extra interior clause is live on this host. The hop `(2,2,1) → (2,2,2)`
has `|σ_v|=|σ_w|=3` and destination min absolute coordinate `2`, so `ρ3 = 1`
and `c2d4 = 1` while `i2 = 2`. Both sites lie in `B_54(0)`. The displayed
body last hop `(1,1,0) → (1,1,1)` keeps cost `1`. The skipped hop
`(3,2,0) → (4,2,0)` has `i2=1`. The same Dijkstra gives `t(3,2,0) = 9`
and `t(4,2,0) = 10`, matching that skipped extra hop of cost `1`. The same
Dijkstra also gives `t(2,2,2) = 11`, matching the interior extra hop of
cost `2` after the ridge-slide hop off `(1,1,1)`. The max≥4 out-face hop
`(4,2,0) → (5,2,0)` has `c2d4=2` and therefore `i2=2`; both ends lie in
`B_54(0)`. Independently, `t(5,2,0) = 12`.

A cheapest body walk stays on the dest-min-abs=`1` surface until
`(18,18,1)` and only then pays the interior extra. Independently,
`t(18,18,1) = 41`. The remaining seventeen hops to `(18,18,18)` each cost
`2`, matching `t(18,18,18) = 75`.

The site `(18,18,18)` has coordinate-sum `54`, so it is absent from
`B_51(0)`. The new axis site is `t(54,0,0) = 75`. The shared axis site
`t(51,0,0) = 67` is an `i2` score on this ball. The `B_54(0)` table is
therefore not leftover of the `B_51(0)` times. The body site `(19,19,19)`
has coordinate-sum `57` and is absent from `B_54(0)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_54(0) reports t(18,0,0) and t(18,18,18) under the named c2d4-plus-interior hop-cost and scores the k=18 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: c2d4_interior_cost2_samek_k18_b54
target_blocker_text: "whether same-k reverse at k=18 still holds after interior 3-to-3 hops with dest min abs at least 2 are priced at 2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_54(0) under the named hop-cost; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `i2` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_54(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`,
  `c2d4`, and `i2` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `i2` into Admissibility, selecting it as
  a physical cost, or lifting the comparison off `B_54(0)` remain separate
  obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

`i2` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`i2`, using one Dijkstra on `B_54(0)`.

An explicit axis path of cost `34` is seed-exit `(0,0,0) → (1,0,0)` of
cost `3`, leave-axis `(1,0,0) → (1,1,0)` of cost `1`, enter-body
`(1,1,0) → (1,1,1)` of cost `1`, ridge-slide `(1,1,1) → (1,2,1)` of cost
`3`, seventeen support-preserving cost-`1` hops to `(18,2,1)`,
support-drop `(18,2,1) → (18,2,0)` of cost `3`, corridor-slide
`(18,2,0) → (18,1,0)` of cost `3`, and support-drop `(18,1,0) → (18,0,0)`
of cost `3`, summing to `34`. Every path has first hop cost `3`. That walk
is a witness of cost `34`, not a uniqueness claim.

An explicit body path of cost `75` is seed-exit `(0,0,0) → (1,0,0)` of
cost `3`, leave-axis `(1,0,0) → (1,1,0)` of cost `1`, corridor-slide
`(1,1,0) → (1,2,0)` of cost `3`, non-hugging face hop `(1,2,0) → (2,2,0)`
of cost `1`, enter-body `(2,2,0) → (2,2,1)` of cost `1`, sixteen
support-preserving cost-`1` hops to `(18,2,1)`, sixteen cost-`1` hops to
`(18,18,1)`, and seventeen interior extra hops of cost `2` to
`(18,18,18)`, summing to `75`. That walk is a witness of cost `75`, not a
uniqueness claim.

On the interior hop `(2,2,1) → (2,2,2)` one has `|σ_v|=|σ_w|=3` and dest min
absolute coordinate `2`, so `ρ3 = 1` and `c2d4 = 1` while `i2 = 2`; both
sites lie in `B_54(0)`. On the reverse hop `(2,2,2) → (1,2,2)` the extra
clause is idle because the dest min absolute coordinate is `1`; `i2` costs
`1`. On the max≥4 out hop `(4,2,0) → (5,2,0)` one has `|σ_v|=|σ_w|=2`, dest
max `5` greater than source max `4`, and source max already `4`, so `ρ3 = 1`
while `c2d4 = 2` and `i2 = 2`; both ends lie in `B_54(0)`. On the in-ball hop
`(4,1,0) → (5,1,0)` the `c2d4` extra clause fires, but the destination least
nonzero absolute coordinate is `1`, so `ρ3`, `c2d4`, and `i2` all cost `3`.
On the max≥3 out hop `(3,2,0) → (4,2,0)` the `c2d4` extra clause is idle
because the source max is `3`; `ρ3`, `c2d4`, and `i2` all cost `1`. On the
unit-out hop `(1,1,0) → (2,1,0)` corridor-slide already prices that hop at
`3`. On the body hop `(1,0,0) → (1,1,0)` both `ρ3` and `i2` cost `1`.

## Theorem 1 — Arrival times at k=18

Under `i2` on `B_54(0)`,

```text
t(18,0,0) = 34
t(18,18,18) = 75
```

The runner computes both values from the single origin Dijkstra and checks
them against the explicit paths above. These values are Dijkstra outputs,
not fitted scalars. Both sites lie in `B_54(0)`. The site `(18,18,18)` has
coordinate-sum `54`, so it is absent from `B_51(0)`. The pair is computed
on `B_54(0)`, not copied from a smaller-ball table.

## Theorem 2 — Same-k comparison at k=18

The displayed comparison is whether

```text
t(18,0,0)^2 / 324 > t(18,18,18)^2 / 972.
```

Substituting the computed times gives the integer statement `1156/324`
versus `5625/972`, or equivalently `3468 > 5625`. The inequality does not
hold. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write i2 into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `i2`, `c2d4`, `ρ3`, `μ`, or `ν`. This
note proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=18.
- The live interior `3→3` clause on `B_54(0)` is not a statement about larger
  hosts.
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

The companion runner builds `B_54(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(18,0,0)` and `t(18,18,18)`,
checks the integer form of Theorem 2, checks that the interior extra
clause prices `(2,2,1) → (2,2,2)` at `2` on this host, skips
`(2,2,2) → (1,2,2)` as a new tax, and fires `(4,2,0) → (5,2,0)` at cost `2`
with both ends inside the ball, checks that the live Admissibility wording
does not name `i2`, and records the import boundary. Declared review inputs
are this note and the axiom memo only.
