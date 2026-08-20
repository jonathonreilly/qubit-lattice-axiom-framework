---
claim_id: c2d4_interior_cost2_samek_k7_b21_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=7 under the named c2d4-plus-interior hop-cost on B_21(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/c2d4_interior_cost2_samek_k7_b21_2026_08_15.py
---

# Same-k Reverse At k=7 Under The Named C2d4-Plus-Interior Hop-Cost On B_21(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=7 on the finite nearest-neighbor
graph `B_21(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/c2d4_interior_cost2_samek_k7_b21_2026_08_15.py`](../scripts/c2d4_interior_cost2_samek_k7_b21_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named c2d4-plus-interior hop-cost `i2` is
the first display of `i2` at `k=7`. The parent clauses `ν`, `μ`, `ρ3`, and
`c2d4` are those of the ridge-slide and cost-2 max≥4 out-face scorings:

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `c2d4(v→w) = 3` if `ρ3` would be `3`, else `2` if (`|σ_v|=|σ_w|=2` and
  `max_i |w_i| > max_i |v_i|` and `max_i |v_i| ≥ 4`), else `1`;
- `i2(v→w) = 3` if `ρ3` would be `3`, else `2` if `c2d4` would be `2` or
  (`|σ_v|=|σ_w|=3` and `min_i |w_i| ≥ 2`), else `1`.

The extra interior clause is a `3→3` hop whose destination minimum absolute
coordinate is at least `2`. It taxes body hops more than axis hops. It
fires on `(2,2,2) → (3,2,2)` at cost `2`. It does not fire on the ridge-slide
hop `(1,1,1) → (2,1,1)`, whose destination minimum absolute coordinate is
`1` and which is already priced at `3` by `ρ3`. The cost-3 interior-slide
parent `ι` prices some of those interior hops at `3` and skips height-`m`
ridges; `i2` prices the interior clause at `2` and also taxes height-`m`
ridges such as `(3,2,2) → (4,2,2)`. Uniqueness is not claimed.

The finite host is scored independently: one origin Dijkstra is run on this
ball. The ball is not leftover of a larger-ball table.

```text
B_21(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 21 }.
```

It has 13287 sites. Edges are the cubic nearest-neighbor steps that remain
inside `B_21(0)`. One Dijkstra from the origin yields

```text
t(7,0,0) = 21
t(7,7,7) = 31
```

The same-k comparison at k=7 is

```text
t(7,0,0)^2 / 49 = 441/49 > 961/147 = t(7,7,7)^2 / 147.
```

Equivalently `1323 > 961`. The inequality holds. Same-k reverse holds at k=7.
Displayed, not adopted.

Independently, the new axis site is `t(21,0,0) = 42`. The shared axis site
`t(18,0,0) = 34` is an `i2` score on this ball, not a `ρ3` leftover. The
site `(7,7,7)` has coordinate-sum `21`, so it is absent from `B_18(0)`. The
`B_21(0)` table is therefore not leftover of the `B_18(0)` times.

The pair is not leftover of `ρ3`: the same sites under `ρ3` are `19` versus
`25`. On the interior hop `(2,2,2) → (3,2,2)` one has `|σ| : 3 → 3` and
destination min abs `2`, so `ρ3 = 1` while `i2 = 2`. Therefore `ρ3`
cannot price interior body hops. On the max≥4 out-face hop `(4,2,0) → (5,2,0)` one
has `|σ| : 2 → 2`, destination max `5` greater than source max `4`, and
source max already `4`, so `ρ3 = 1` while `c2d4 = 2` and `i2 = 2`.
Therefore `ρ3` cannot price max≥4 out-face. Independently, `t(5,2,0) = 12`
and `t(3,2,2) = 12` under `i2`. The skipped hop `(3,2,0) → (4,2,0)` grows
the max absolute coordinate, but its source max is `3`, so it is not max≥4
out-face; it stays `i2 = 1`. Independently, `t(3,2,0) = 9` and
`t(4,2,0) = 10`.

The pair is not leftover of `c2d4`: that parent already prices max≥4
out-face at `2`, but it leaves interior body hops at `1`. On
`(2,2,2) → (3,2,2)` one has `c2d4 = 1` while `i2 = 2`.

The pair is not leftover of `ι`. That cost-3 interior-slide parent taxes a
`3→3` hop whose destination has `min |w_i| ≥ 2` and is not a height-`m`
ridge, and it killed reverse at `k=7`. On `(2,2,1) → (2,2,2)` and on
`(3,3,2) → (3,3,3)` one has `ι = 3` while `i2 = 2`, so `ι`
cannot price the cost-2 interior clause. On the height-`m` ridge `(3,2,2) → (4,2,2)` one has
`ι = 1` while `i2 = 2`.

A cheapest `i2` walk to `(7,0,0)` is seven axis hops of cost `3`, summing
to `21`. A cheapest `i2` walk to `(7,7,7)` uses two cost-`3` hops, thirteen
cost-`1` hops, and six interior cost-`2` hops, summing to `31`. Those walks
are witnesses, not a uniqueness claim. The displayed body last hop
`(1,1,0) → (1,1,1)` keeps cost `1`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_21(0) reports t(7,0,0) and t(7,7,7) under the named c2d4-plus-interior hop-cost and scores the k=7 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: c2d4_interior_cost2_samek_k7_b21
target_blocker_text: "whether same-k reverse at k=7 still holds after interior 3-to-3 hops are priced at 2 on top of c2d4"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_21(0) under the named hop-cost; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `i2` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_21(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`,
  `c2d4`, and `i2` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `i2` into Admissibility, selecting it as
  a physical cost, or lifting the comparison off `B_21(0)` remain separate
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
`i2`, using one Dijkstra on `B_21(0)`.

An explicit axis path is

```text
(0,0,0) → (1,0,0) → (2,0,0) → (3,0,0) → (4,0,0) → (5,0,0) → (6,0,0) → (7,0,0)
```

with costs `3+3+3+3+3+3+3=21`. An explicit body path is

```text
(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,2,2) → (0,2,3) → (0,2,4)
→ (1,2,4) → (1,2,5) → (1,2,6) → (1,2,7) → (1,3,7) → (1,4,7) → (1,5,7)
→ (1,6,7) → (1,7,7) → (2,7,7) → (3,7,7) → (4,7,7) → (5,7,7) → (6,7,7)
→ (7,7,7)
```

with costs `3+1+3+1+1+1+1+1+1+1+1+1+1+1+1+2+2+2+2+2+2=31`. Every path has
first hop cost `3`, and every hop costs at least `1`, so these paths are
optimal once Dijkstra matches them.

On the interior hop `(2,2,2) → (3,2,2)` one has `|σ_v|=|σ_w|=3` and dest
min abs `2`, so `ρ3 = 1` and `c2d4 = 1` while `i2 = 2`. Independently,
`t(2,2,2) = 11`. On the height-`m` ridge `(3,2,2) → (4,2,2)` the
destination has min abs `2` and exactly two coordinates equal to that min,
so `ι = 1` while `i2 = 2`. On `(3,3,2) → (3,3,3)` one has `ι = 3` while
`i2 = 2`. On the max≥4 out hop `(4,2,0) → (5,2,0)` one has `c2d4 = 2` and
`i2 = 2` while `ρ3 = 1`. On the max≥3 out hop `(3,2,0) → (4,2,0)` the
max≥4 extra is idle; `i2 = 1`. On the deep-out hop `(2,2,0) → (3,2,0)` the
max≥4 extra is idle; `i2 = 1`. On the unit-out hop `(1,1,0) → (2,1,0)`
corridor-slide already prices the hop at `3`. On the body hop
`(1,0,0) → (1,1,0)` one has `i2 = 1`. On `(2,1,1) → (2,1,2)` the
destination min abs is `1`, so the interior clause is idle and `i2 = 1`.

## Theorem 1 — Arrival times at k=7

Under `i2` on `B_21(0)`,

```text
t(7,0,0) = 21
t(7,7,7) = 31
```

The runner computes both values from the single origin Dijkstra and checks
them against the explicit paths above. These values are Dijkstra outputs,
not fitted scalars.

## Theorem 2 — Same-k comparison at k=7

The displayed comparison is whether

```text
t(7,0,0)^2 / 49 > t(7,7,7)^2 / 147.
```

Substituting the computed times gives the integer statement `441/49 > 961/147`,
or equivalently `1323 > 961`. The inequality holds. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write i2 into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `i2`, `c2d4`, `ρ3`, `μ`, or `ν`. This
note proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=7.
- The live interior and max≥4 out-face clauses on `B_21(0)` are not a
  statement about larger hosts.
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

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md). Lattice
supplies the six-neighbor graph and the ball. Admissibility supplies none
of the hop costs. The integers `3`, `2`, and `1`, the support-size
clauses, the least-nonzero-coordinate clause, the two-unit-height ridge
clause, the max≥4 out-face source-max clause, the interior dest-min
clause, and the arrival function `t` are separately displayed mathematical
inputs. No axiom text is edited.

## Named Rule

Let `B_21(0) = { v ∈ Z^3 : |v|_1 ≤ 21 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_21(0)`,
`t(v)` is the least sum of `i2` along a directed path from `0` to `v` in
that graph.

The comparator `ρ3` uses only the first five clauses. On
`(2,2,2) → (3,2,2)` and on `(4,2,0) → (5,2,0)` the extra `i2` predicates
hold and `ρ3` stays at `1`. The comparator `c2d4` uses the max≥4 out-face
clause but not the interior clause. On `(2,2,2) → (3,2,2)` one has
`c2d4 = 1` while `i2 = 2`. The comparator `ι` uses a cost-3 interior
non-ridge test. On `(3,3,2) → (3,3,3)` one has `ι = 3` while `i2 = 2`.
On `(3,2,2) → (4,2,2)` one has `ι = 1` while `i2 = 2`.

## Runner Contract

The companion runner builds `B_21(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(7,0,0)` and `t(7,7,7)`,
checks the integer form of Theorem 2, checks that the extra interior and
max≥4 out-face clauses fire in-ball, skips `(3,2,0) → (4,2,0)` as a new
max≥4 tax, checks that the live Admissibility wording does not name `i2`,
and records the import boundary. Declared review inputs are this note and
the axiom memo only.
