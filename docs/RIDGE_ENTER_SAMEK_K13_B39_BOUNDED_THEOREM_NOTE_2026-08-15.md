---
claim_id: ridge_enter_samek_k13_b39_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=13 under the named ridge-enter hop-cost on B_39(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/ridge_enter_samek_k13_b39_2026_08_15.py
---

# Same-k Reverse At k=13 Under The Named Ridge-Enter Hop-Cost On B_39(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=13 on the finite nearest-neighbor
graph `B_39(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/ridge_enter_samek_k13_b39_2026_08_15.py`](../scripts/ridge_enter_samek_k13_b39_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named ridge-enter hop-cost `κ` is

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `κ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=2` and `|σ_w|=3` and exactly
  two `|w_i|` equal `1)`, else `1`.

The finite host is

```text
B_39(0) := { v ∈ Z^3 : |v_1| + |v_2| + |v_3| ≤ 39 }.
```

It has 82239 sites. Edges are the cubic nearest-neighbor steps that remain
inside `B_39(0)`. One Dijkstra from the origin yields

```text
t(13,0,0) = 25
t(13,13,13) = 43
```

The same-k comparison at k=13 is

```text
t(13,0,0)^2 / 169 = 625/169 > 1849/507 = t(13,13,13)^2 / 507.
```

Equivalently `1875 > 1849`. The inequality holds. Displayed, not adopted.

The extra 2→3 clause is live on this host. The hop `(2,1,0) → (2,1,1)` has
`κ=3` and `ρ3=1`, and both ends lie in `B_39(0)`. The displayed k=1 body last
hop `(1,1,0) → (1,1,1)` has destination coordinates all of absolute value
`1`, so the extra clause does not fire and that hop keeps cost `1`. The
witness body enter `(13,13,0) → (13,13,1)` has only one unit destination
coordinate, so it also keeps cost `1`. Uniqueness is not claimed.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_39(0) reports t(13,0,0) and t(13,13,13) under the named ridge-enter hop-cost and scores the k=13 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: ridge_enter_samek_k13_b39
target_blocker_text: "whether same-k reverse at k=13 still holds after the ridge-enter clause is added to the ridge-slide hop-cost"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded arrival comparison"
conditional_surface_status: "exact on B_39(0) under the named hop-cost; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence supplies nearest-neighbor
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `κ` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_39(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`, and
  `κ` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `κ` into Admissibility, selecting it as
  a physical cost, or lifting the comparison off `B_39(0)` remain separate
  obligations. This note does not close them.

## Exact Objects

All runner values are integers. No float is used in the comparison.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility sentence, quoted and not rewritten:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice
> translations and proper cubic rotations.

`κ` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`κ`, using one Dijkstra on `B_39(0)`.

A witness axis walk of cost `25` is seed-exit `3` onto `(1,0,0)`, leave-axis
`1` onto `(1,1,0)`, corridor-slide `3` onto `(2,1,0)`, non-hugging face hop
`1` onto `(2,2,0)`, eleven support-preserving cost-`1` face hops to
`(13,2,0)`, corridor-slide `3` onto `(13,1,0)`, and support-drop `3` onto
`(13,0,0)`. That walk is a witness of cost `25`, not a uniqueness claim.

A witness body walk of cost `43` is the same prefix of cost `8` to
`(2,2,0)`, eleven cost-`1` face hops to `(13,2,0)`, eleven cost-`1` face
hops to `(13,13,0)`, enter-body `1` onto `(13,13,1)`, and twelve
support-preserving cost-`1` body hops to `(13,13,13)`. The enter-body hop
has only one unit destination coordinate, so the extra ridge-enter clause
does not fire. That walk is a witness of cost `43`, not a uniqueness claim.

## Theorem 1 — Arrival times at k=13

Under `κ` on `B_39(0)`,

```text
t(13,0,0) = 25
t(13,13,13) = 43
```

The runner computes both values from the single origin Dijkstra and checks
them against the explicit witness walks above.

## Theorem 2 — Same-k comparison at k=13

The displayed comparison is whether

```text
t(13,0,0)^2 / 169 > t(13,13,13)^2 / 507.
```

Substituting the computed times gives the integer statement `625/169 > 1849/507`,
or equivalently `1875 > 1849`. The inequality holds. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write κ into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `κ`, `ρ3`, `μ`, or `ν`. This note
proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=13.
- The live 2→3 clause on `B_39(0)` is not a statement about larger hosts.
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

The companion runner builds `B_39(0)`, evaluates the named hop-cost, and
runs one Dijkstra from the origin. It reports `t(13,0,0)` and `t(13,13,13)`,
checks the integer form of Theorem 2, checks that the extra 2→3 clause is
live on in-host hops and does not tax the displayed body last hop, checks
that the live Admissibility wording does not name `κ`, and records the
import boundary. Declared review inputs are this note and the axiom memo
only.
