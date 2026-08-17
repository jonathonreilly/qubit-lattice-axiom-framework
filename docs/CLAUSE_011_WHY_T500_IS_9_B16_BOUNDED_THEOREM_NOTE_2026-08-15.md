---
claim_id: clause_011_why_t500_is_9_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A lex-first shortest path to (5,0,0) under the named (0,1,1) hop-cost on B_16(0) is named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/clause_011_why_t500_is_9_b16_2026_08_15.py
---

# Named (0,1,1) Lex-First Path To (5,0,0) On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one lex-first shortest path from the origin to `(5,0,0)` under
one named hop-cost on the finite 16-hop neighborhood of the origin in
the cubic nearest-neighbor graph. The rule and the path are displayed,
not adopted.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/clause_011_why_t500_is_9_b16_2026_08_15.py`](../scripts/clause_011_why_t500_is_9_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Let `B_16(0)` be the set of sites of `Z^3` whose nearest-neighbor graph
distance from the origin is at most 16. That set has 6017 sites and is
used only as a finite domain bound. It is not a hop-cost.

Hops are the six nearest-neighbor steps that remain inside `B_16(0)`.
Write `|σ_v|` for the support of a site (the number of nonzero
coordinates). The named clause-toggle `(0,1,1)` assigns

```text
cost(v→w) = 3  if |σ_v|=|σ_w|=1 or |σ_w|<|σ_v|,
          = 1  otherwise.
```

Seed-exit therefore costs 1. Axis 1-skeleton hops and support-drop hops
cost 3. Every other admitted hop costs 1. The rule is not written into
Admissibility: do not write (0,1,1) into Admissibility. Do not attach L1.
Uniqueness is not required.

One Dijkstra from the origin yields `t(5,0,0)=9`. Among all
origin-to-`(5,0,0)` walks of that cost, the lex-first shortest path
(each successor the coordinate-lexicographic least site that remains
on the shortest-path DAG) is the hop sequence

```text
(0,0,0) --1--> (0,-1,0) --1--> (1,-1,0) --1--> (2,-1,0) --1--> (3,-1,0) --1--> (4,-1,0) --1--> (5,-1,0) --3--> (5,0,0)
```

with running cost `0,1,2,3,4,5,6,9`. The axis 1-skeleton walk
`(0,0,0)→(1,0,0)→…→(5,0,0)` would cost `1+3+3+3+3=13`. The named path
is cheaper because the first hop is a cost-1 seed-exit off the target
ray and the next five hops stay at support 2, where the axis-1 clause
does not fire. Displayed, not adopted.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations.

The axiom set supplies the cubic nearest-neighbor graph. It does not
supply a hop-cost, a preferred clause-toggle, or a preferred arrival
path. This note therefore treats `(0,1,1)` as a separately named finite
scoring rule. The note does not write `(0,1,1)` into Admissibility and
does not enlarge the axiom set.

Record is not used. No readout, formation site, or scalar collection
functional enters the arrival time or the hop sequence.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The arrival t(5,0,0)=9 and one lex-first shortest hop sequence are exact outputs of one Dijkstra on the named finite graph; the hop-cost is a disclosed scoring rule, not an axiom."
trace_class: compute
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) under the named (0,1,1) hop-cost for the lex-first path to (5,0,0); displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

`B_16(0)` is the closed 16-hop neighborhood of the origin. Every hop
used below is a nearest-neighbor step whose endpoints both lie in that
set. The site `(5,0,0)` has nearest-neighbor graph distance 5, so it
lies in the ball. One Dijkstra computes the named arrival time `t(v)`
from the origin to each site.

The axis 1-skeleton is the set of sites with support at most 1. A path
leaves that skeleton when it occupies a site of support 2 or 3. Lex
order on sites is the ordinary coordinate order on `Z^3`. The lex-first
shortest path is the unique walk obtained by starting at the origin and,
at each site, taking the least successor that remains on some
origin-to-`(5,0,0)` walk of cost `t(5,0,0)`. Other shortest paths may
exist. Uniqueness is not required.

## Theorem 1

On `B_16(0)` under the named `(0,1,1)` hop-cost, one Dijkstra gives

`t(5,0,0)=9`.

A lex-first shortest path is the hop sequence

```text
(0,0,0) --1--> (0,-1,0) --1--> (1,-1,0) --1--> (2,-1,0) --1--> (3,-1,0) --1--> (4,-1,0) --1--> (5,-1,0) --3--> (5,0,0)
```

with running cost `0,1,2,3,4,5,6,9`. The seven hop costs are
`1,1,1,1,1,1,3`. The first six hops are seed-exit or support-nondecreasing
support-2 steps and therefore cost 1. The last hop is a support drop
from `(5,-1,0)` to `(5,0,0)` and therefore costs 3.

The same Dijkstra assigns axis arrivals `t(1,0,0)=1`, `t(2,0,0)=4`,
`t(3,0,0)=7`, and `t(4,0,0)=8`. Those four values are background from
the same run; the residual named here is the path to `(5,0,0)`, not a
restatement of the arrival table.

## Theorem 2

The first-hop cost is 1. That hop is the seed-exit
`(0,0,0)→(0,-1,0)`. The path leaves the axis 1-skeleton: the origin
and `(0,-1,0)` have support 1, and the first off-axis site is
`(1,-1,0)`. The remaining interior sites
`(2,-1,0)`, `(3,-1,0)`, `(4,-1,0)`, `(5,-1,0)` also have support 2.
The terminal site `(5,0,0)` returns to the axis 1-skeleton by a
cost-3 support drop.

The cheap seed-exit is therefore present on this lex-first witness:
the walk spends six cost-1 hops before the only expensive hop. That
is why the arrival is 9 rather than the axis-skeleton sum 13. The
observation is displayed, not adopted. It does not select the rule
as framework content and does not claim that every shortest path
begins with the same seed-exit.

## Theorem 3

The note does not write `(0,1,1)` into Admissibility. Do not attach L1.
Uniqueness is not required. The current axiom memo is not edited.

## What This Does Not Claim

- It does not adopt the `(0,1,1)` hop-cost as framework content.
- It does not claim that the named path is the only shortest path.
- It does not claim that every shortest path uses the same seed-exit.
- It does not identify `t` with nearest-neighbor hop count on the axis.
- It does not attach the displayed scores as an L1 hop-cost.
- It does not supply a physical clock, a continuum metric, or a Record
  readout of the arrival time.

## Reproducibility

```text
python3 scripts/clause_011_why_t500_is_9_b16_2026_08_15.py
```

The runner prints `t(5,0,0)`, the lex-first hop sequence, the running
cost, the first-hop cost, whether the path leaves the axis 1-skeleton,
and `TOTAL: PASS=<n> FAIL=<n>`.
