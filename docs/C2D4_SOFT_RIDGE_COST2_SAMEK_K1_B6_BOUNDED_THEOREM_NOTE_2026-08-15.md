---
claim_id: c2d4_soft_ridge_cost2_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named c2d4-plus-soft-ridge hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_soft_ridge_cost2_samek_k1_b6_2026_08_15.py
---

# Same-k Reverse At k=1 Under The Named C2d4-Plus-Soft-Ridge Hop-Cost On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=1 on the finite nearest-neighbor
graph `B_6(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_soft_ridge_cost2_samek_k1_b6_2026_08_15.py`](../scripts/c2d4_soft_ridge_cost2_samek_k1_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named c2d4-plus-soft-ridge hop-cost `s2` is
the first display of `s2`. The parent clauses `ν`, `μ`, `ρ3`, and `c2d4` are
those of the ridge-slide and cost-2 max≥4 out-face same-k scoring on this
ball:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`;
- `s2(v→w) = 3` if `μ` would be `3`, else `2` if (`|σ_v|=|σ_w|=3` and
  exactly two `|w_i|` equal `1`) or (`c2d4` would be `2`), else `1`.

So `s2` equals `3` if `μ` would be `3`. Otherwise it is `c2d4` except that
`ρ3`'s `3→3` ridge-stay — support stays `3` and exactly two destination
absolute coordinates equal `1` — costs `2` not `3`. The extra clause
cheapens body ridge-stay hops, the opposite of an interior tax on
`3→3` hops whose destination min absolute coordinate is at least `2`.
It fires on `(1,1,1) → (2,1,1)` at cost `2`. The parent `ρ3` and `c2d4`
price that hop at `3`. It does not fire on the body last hop
`(1,1,0) → (1,1,1)`, which is not a `3→3` hop, nor on `(2,2,1) → (2,2,2)`,
whose destination has no unit coordinate. Those hops remain priced at `1`.
Uniqueness is not claimed.

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

The extra ridge-stay clause is live on this host. The hop `(1,1,1) → (2,1,1)`
has `|σ_v|=|σ_w|=3` and exactly two destination absolute coordinates equal
to `1`, so `μ = 1` and `ρ3 = 3` and `c2d4 = 3` while `s2 = 2`. Both sites
lie in `B_6(0)`. The displayed body last hop `(1,1,0) → (1,1,1)` keeps cost
`1`. The skipped hop `(3,2,0) → (4,2,0)` has `s2=1`. The same Dijkstra gives
`t(3,2,0) = 9` and `t(4,2,0) = 10`, matching that skipped extra hop of cost
`1`. The same Dijkstra also gives `t(2,1,1) = 7`, matching the ridge-stay
extra hop of cost `2` off `(1,1,1)`, and `t(2,2,2) = 9`, matching the idle
interior hop of cost `1` after that ridge-stay. A `c2d4`-cheap max≥4
out-face hop still needs destination coordinate-sum at least `7`, so its
destination is not a site of this ball. The definitional example
`(4,2,0) → (5,2,0)` has `c2d4=2` and therefore `s2=2`; the source lies in
`B_6(0)` and the destination has coordinate-sum `7`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_6(0) reports t(1,0,0) and t(1,1,1) under the named c2d4-plus-soft-ridge hop-cost and scores the k=1 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: c2d4_soft_ridge_cost2_samek_k1_b6
target_blocker_text: "whether same-k reverse at k=1 still holds after rho3 3-to-3 ridge-stay hops are priced at 2"
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
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `s2` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_6(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`,
  `c2d4`, and `s2` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `s2` into Admissibility, selecting it as
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

`s2` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`s2`, using one Dijkstra on `B_6(0)`.

An explicit axis path is the single hop `(0,0,0) → (1,0,0)` of cost `3`.
An explicit body path is

```text
(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1)
```

with costs `3+1+1=5`. Every path has first hop cost `3`, and every hop costs
at least `1`, so these paths are optimal once Dijkstra matches them.

On the ridge-stay hop `(1,1,1) → (2,1,1)` one has `|σ_v|=|σ_w|=3` and
exactly two destination absolute coordinates equal to `1`, so `μ = 1` while
`ρ3 = 3` and `c2d4 = 3` and `s2 = 2`; both sites lie in `B_6(0)`. On the
interior hop `(2,2,1) → (2,2,2)` the extra clause is idle because the
destination has no unit coordinate; `s2` costs `1`. On the max≥4 out hop
`(4,2,0) → (5,2,0)` one has `|σ_v|=|σ_w|=2`, dest max `5` greater than
source max `4`, and source max already `4`, so `ρ3 = 1` while `c2d4 = 2`
and `s2 = 2`; the destination is not a site of `B_6(0)`. On the in-ball hop
`(4,1,0) → (5,1,0)` the `c2d4` extra clause fires, but the destination least
nonzero absolute coordinate is `1`, so `μ`, `ρ3`, `c2d4`, and `s2` all cost
`3`. On the max≥3 out hop `(3,2,0) → (4,2,0)` the `c2d4` extra clause is
idle because the source max is `3`; `ρ3`, `c2d4`, and `s2` all cost `1`.
On the unit-out hop `(1,1,0) → (2,1,0)` corridor-slide already prices that
hop at `3`. On the body hop `(1,0,0) → (1,1,0)` both `μ` and `s2` cost `1`.

## Theorem 1 — Arrival times at k=1

Under `s2` on `B_6(0)`,

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

Do not write s2 into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `s2`, `c2d4`, `ρ3`, `μ`, or `ν`. This
note proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=1.
- The live ridge-stay `3→3` clause on `B_6(0)` is not a statement about
  larger hosts.
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
checks the integer form of Theorem 2, checks that the ridge-stay extra
clause prices `(1,1,1) → (2,1,1)` at `2` on this host, skips
`(2,2,1) → (2,2,2)` as a new tax, and fires `(4,2,0) → (5,2,0)` at cost `2`
with destination outside the ball, checks that the live Admissibility wording
does not name `s2`, and records the import boundary. Declared review inputs
are this note and the axiom memo only.
