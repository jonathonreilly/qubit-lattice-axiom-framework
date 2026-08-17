---
claim_id: named_hopcost_body_diagonal_path_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A shortest 0→(2,2,2) path under the named equal-weight hop-cost is exhibited and sums to 14. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/named_hopcost_body_diagonal_path_2026_08_15.py
---

# A Shortest Body-Diagonal Path Under The Named Hop-Cost Sums To 14

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact shortest-path arithmetic on the six-neighbor cubic graph
about one seed, for the named equal-weight hop-cost. The rule and the
arrival number are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/named_hopcost_body_diagonal_path_2026_08_15.py`](../scripts/named_hopcost_body_diagonal_path_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Fix one seed at the origin of `Z^3` and the six nearest-neighbor steps
`B_6`. For a site `v`, write `σ_v` for the inward-neighbor set toward the
seed: one inward neighbor for each nonzero coordinate of `v`. The inward
weight is `w_v = |σ_v|`. The named hop-cost on a directed step `v → w` is

`ρ(v,w) = 3` if `w_v = w_w` or `w_v = 0`, else `1`.

The first clause is equal inward weight. The second is seed-exit. This
rule is a displayed finite member clause, not Admissibility content.

A lexicographically first shortest path from `0` to the body-diagonal site
`(2,2,2)` is the six-step site list

```text
(0,0,0) → (0,0,1) → (0,0,2) → (0,1,2) → (0,2,2) → (1,2,2) → (2,2,2).
```

The six hop costs along it are `3,3,1,3,1,3`. Their orbit-cost sum is
`14`. Every shortest path uses the same hop-cost multiset
`{1,1,3,3,3,3}` and therefore contains at least one cost-`3` equal-weight
or seed-exit hop. The path type is the residual: `14` is this orbit-cost
sum, not a leftover of the arrival number.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited shortest 0→(2,2,2) path under the named hop-cost has orbit-cost sum 14, and every shortest path shares that hop-cost multiset. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: named_hopcost_body_diagonal_path
target_blocker_text: "exhibit a shortest 0→(2,2,2) path and the orbit-cost sum that forces arrival 14 under the named hop-cost"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "keep the named hop-cost displayed; do not write it into Admissibility; the residual is the path type, not an adopted arrival law"
conditional_surface_status: "exact on the six-neighbor graph about one seed; no admissibility or metric adoption"
hypothetical_axiom_status: "no edit; ρ is displayed and is not proposed as axiom content"
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
  rule `ρ`; the finite ball of six-neighbor graph radius `6` about the
  seed, which contains `(2,2,2)`.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting `ρ` as a physical cost, writing it
  into Admissibility, and identifying arrival with a physical time or
  metric remain outside the target.

## Exact Objects

Sites are integer triples. The unique seed is `s = (0,0,0)`. The six
nearest-neighbor steps are

`B_6 = {±e_1, ±e_2, ±e_3}`.

The search domain is the finite ball

`Ball_6(s) = { v in Z^3 : six-neighbor graph distance from s to v is at most 6 }`.

It has `377` sites and contains the body-diagonal target `(2,2,2)`.

For `v = (v_1,v_2,v_3)` the inward-neighbor set toward the seed is

`σ_v = { v - sgn(v_i) e_i : v_i ≠ 0 }`.

Thus `w_v = |σ_v|` equals the number of nonzero coordinates of `v`, so
`w_s = 0` and `w_{(2,2,2)} = 3`. A directed nearest-neighbor hop `v → w`
carries the ordered inward-weight pair `(w_v, w_w)` and the cost

`ρ(v,w) = 3` if `w_v = w_w` or `w_v = 0`, else `1`.

Arrival `t(v)` is the least sum of `ρ` along a `B_6` path in `Ball_6(s)`
from `s` to `v`. A path is lexicographically first among a set when its
sequence of sites is the least sequence in the dictionary order of
integer triples.

These objects are supplied mathematical data for the theorems below.

## Theorem 1 — A Lexicographically First Shortest Path Sums To 14

On `Ball_6(s)`, a lexicographically first shortest `s → (2,2,2)` path is

```text
P = (
  (0,0,0),
  (0,0,1),
  (0,0,2),
  (0,1,2),
  (0,2,2),
  (1,2,2),
  (2,2,2)
).
```

The six directed hops, inward-weight pairs, and costs are

| hop | pair `(w_v,w_w)` | clause | `ρ` |
|---|---|---|---:|
| `(0,0,0) → (0,0,1)` | `(0,1)` | seed-exit | `3` |
| `(0,0,1) → (0,0,2)` | `(1,1)` | equal inward weight | `3` |
| `(0,0,2) → (0,1,2)` | `(1,2)` | neither | `1` |
| `(0,1,2) → (0,2,2)` | `(2,2)` | equal inward weight | `3` |
| `(0,2,2) → (1,2,2)` | `(2,3)` | neither | `1` |
| `(1,2,2) → (2,2,2)` | `(3,3)` | equal inward weight | `3` |

The orbit-cost sum is `3+3+1+3+1+3 = 14`. Hence `t(2,2,2) ≤ 14`. The
companion runner's Dijkstra search on `Ball_6(s)` returns the same path
and the same value `t(2,2,2) = 14`, so `P` is shortest.

## Theorem 2 — Every Shortest Path Has The Same Hop-Cost Multiset

Every shortest `s → (2,2,2)` path in `Ball_6(s)` has exactly six hops and
hop-cost multiset `{1,1,3,3,3,3}`. In particular at least one hop is a
cost-`3` equal-weight or seed-exit hop.

The six-neighbor graph distance from `s` to `(2,2,2)` is `6`, so every
path has at least six hops. The `90` words with two steps `+e_1`, two
steps `+e_2`, and two steps `+e_3` are exactly the monotone six-hop
paths. Along any such word the inward weight rises `0 → 1 → 2 → 3`
exactly once each and stays put on the other three hops:

- the unique seed-exit `0 → 1` has cost `3`;
- the unique rise `1 → 2` has cost `1`;
- the unique rise `2 → 3` has cost `1`;
- each of the three equal-weight stays (`1 → 1`, `2 → 2`, or `3 → 3`)
  has cost `3`.

The orbit-cost sum is therefore `3+1+1+9 = 14` on every monotone word.
The runner enumerates all shortest paths by predecessor search on the
Dijkstra tree of `Ball_6(s)` and finds exactly these `90` words, each
with hop-cost multiset `{1,1,3,3,3,3}`. No cheaper detour exists in the
ball. The cost-`3` hops on `P` are the seed-exit and the three
equal-weight stays; the same clauses appear on every shortest path.

The residual is this common path type. The integer `14` is the
orbit-cost sum forced by one seed-exit, two rising hops, and three
equal-weight stays. It is not a leftover of the arrival number.

## Theorem 3 — Displayed, Not Adopted

Do not write `ρ` into Admissibility. The live Admissibility sentences
remain the quoted nearest-neighbor distribution rule. They do not name
inward weights, seed-exit, or a numerical hop-cost.

Do not identify the named hop-cost with six-neighbor graph distance, and
do not treat that graph distance as the residual. The arrival number
`t(2,2,2) = 14` is the orbit-cost sum along the exhibited path type.

The rule and the path are displayed, not adopted. Uniqueness of `ρ`
among cost rules is not claimed.

## Proof-Obligation Boundary

| Obligation | Disposition |
|---|---|
| one seed and the six-neighbor stencil | supplied domain |
| inward weights and the named rule `ρ` | supplied display |
| lexicographically first shortest path | computed; listed in Theorem 1 |
| six hop costs sum to `14` | computed; orbit-cost table |
| common hop-cost multiset on every shortest path | proved for monotone words; enumerated on `Ball_6(s)` |
| at least one cost-`3` equal-weight or seed-exit hop | contained in the common multiset |
| `ρ` written into Admissibility | refused |
| graph-distance cost adopted as the residual | refused |

## What This Does Not Claim

- `ρ` is not Admissibility content and is not a new axiom.
- The arrival number is not adopted as a physical time, rate, or metric.
- No hop-cost uniqueness theorem is claimed.
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

Their dependency role is limited to the repository's lattice and
admissibility vocabulary. This theorem separately supplies the named
hop-cost as displayed data. No axiom sentence is edited.

## Runner Contract

The companion runner constructs `Ball_6(s)`, computes Dijkstra arrival
from the seed under `ρ`, extracts the lexicographically first shortest
path to `(2,2,2)`, and sums the six computed hop costs. It enumerates
every shortest path and checks the common hop-cost multiset. It quotes
the live Admissibility sentences, checks that the axiom memo is not
edited, and checks that the note keeps `ρ` displayed. Declared review
inputs are this note and the axiom memo only.
