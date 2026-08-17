---
claim_id: height_ridge_samek_k1_b6_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Same-k reverse at k=1 under the named height-ridge hop-cost on B_6(0) is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/height_ridge_samek_k1_b6_2026_08_15.py
---

# Same-k Reverse At k=1 Under The Named Height-Ridge Hop-Cost On B_6(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one Dijkstra arrival comparison at k=1 on the finite nearest-neighbor
graph `B_6(0)`, under a named hop-cost displayed for this note only.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/height_ridge_samek_k1_b6_2026_08_15.py`](../scripts/height_ridge_samek_k1_b6_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
nearest-neighbor hop `v → w` the named height-ridge hop-cost `ζ` is

- `ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`, else `1`;
- `μ(v→w) = 3` if `ν` would be `3` or `(|σ_v|=|σ_w|=2` and the least nonzero
  `|w_i|` equals `1)`, else `1`;
- `ρ3(v→w) = 3` if `μ` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `1)`, else `1`;
- `ζ(v→w) = 3` if `ρ3` would be `3` or `(|σ_v|=|σ_w|=3` and exactly two
  `|w_i|` equal `m`, with `m = min_j |w_j|` and `m ≥ 2)`, else `1`.

The finite host is

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

The inequality holds. Displayed, not adopted.

On this host the extra `m ≥ 2` clause is idle: no nearest-neighbor hop
inside `B_6(0)` has `|σ_v|=|σ_w|=3` and exactly two destination coordinates
equal to a minimum of at least 2. The named clause is still part of `ζ`;
the hop `(2,2,2) → (3,2,2)` has `ζ=3` and `ρ3=1`, but that destination lies
outside `B_6(0)`. Uniqueness is not claimed.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "One Dijkstra on B_6(0) reports t(1,0,0) and t(1,1,1) under the named height-ridge hop-cost and scores the k=1 same-k comparison. The hop-cost is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: height_ridge_samek_k1_b6
target_blocker_text: "whether same-k reverse at k=1 still holds after the height-ridge clause is added to the ridge-slide hop-cost"
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
  adjacency on `Z^3`. It is quoted without rewrite. The hop-cost `ζ` is not
  Lattice content.
- **Explicit theorem-domain condition:** the finite set `B_6(0)`, its
  nearest-neighbor edges, and the named directed costs `ν`, `μ`, `ρ3`, and
  `ζ` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** writing `ζ` into Admissibility, selecting it as
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

`ζ` is a separately named hop-cost on directed nearest-neighbor hops. It is
not that admissibility rule.

Write `t(v)` for the Dijkstra arrival cost from the origin to `v` under
`ζ`, using one Dijkstra on `B_6(0)`.

An explicit axis path is the single hop `(0,0,0) → (1,0,0)` of cost `3`.
An explicit body path is

```text
(0,0,0) → (1,0,0) → (1,1,0) → (1,1,1)
```

with costs `3+1+1=5`. Every path has first hop cost `3`, and every hop costs
at least `1`, so these paths are optimal once Dijkstra matches them.

## Theorem 1 — Arrival times at k=1

Under `ζ` on `B_6(0)`,

```text
t(1,0,0) = 3
t(1,1,1) = 5
```

The runner computes both values from the single origin Dijkstra and checks
them against the explicit paths above.

## Theorem 2 — Same-k comparison at k=1

The displayed comparison is whether

```text
t(1,0,0)^2 / 1 > t(1,1,1)^2 / 3.
```

Substituting the computed times gives the integer statement `9 > 25/3`, or
equivalently `27 > 25`. The inequality holds. Displayed, not adopted.

## Theorem 3 — No axiom write and no L1 attachment

Do not write ζ into Admissibility. Do not attach L1.

The live Admissibility wording names one fixed nearest-neighbor
admissibility rule and does not name `ζ`, `ρ3`, `μ`, or `ν`. This note
proposes no axiom edit. The comparison above is a score of the named
hop-cost against itself at two sites; it is not an attachment of a
coordinate-sum hop-cost.

## What This Does Not Claim

- No uniqueness claim is made for this named hop-cost at k=1.
- The idle `m ≥ 2` clause on `B_6(0)` is not a statement about larger hosts.
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
checks the integer form of Theorem 2, checks that the `m ≥ 2` clause is
idle on in-host hops, checks that the live Admissibility wording does not
name `ζ`, and records the import boundary. Declared review inputs are this
note and the axiom memo only.
