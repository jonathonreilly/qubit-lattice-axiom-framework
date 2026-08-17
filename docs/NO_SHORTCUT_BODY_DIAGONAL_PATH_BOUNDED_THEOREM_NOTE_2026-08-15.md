---
claim_id: no_shortcut_body_diagonal_path_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "A shortest 0→(2,2,2) path under the named support-drop hop-cost is exhibited. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/no_shortcut_body_diagonal_path_2026_08_15.py
---

# A Lex-First Shortest Body-Diagonal Path Under The Support-Drop Hop-Cost

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact shortest-path arithmetic on the six-neighbor cubic graph
about one seed, for the named support-drop hop-cost. The rule, the path,
and the hop-cost multiset are displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/no_shortcut_body_diagonal_path_2026_08_15.py`](../scripts/no_shortcut_body_diagonal_path_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Fix one seed at the origin of `Z^3` and the six nearest-neighbor steps
`B_6`. For a site `v`, write `σ_v` for the inward-neighbor set toward the
seed: one inward neighbor for each nonzero coordinate of `v`. The inward
weight is `w_v = |σ_v|`. The named support-drop hop-cost on a directed
step `v → w` is

`ν(v,w) = 3` if `|σ_v| = 0` or (`|σ_v| = |σ_w| = 1`) or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is the remaining axis-skeleton
hop: both endpoints have inward weight `1`. The third clause is support
drop: the destination has strictly smaller inward-neighbor set than the
source. This rule is a displayed finite member clause, not Admissibility
content. It is a different rule from the axis-skeleton hop-cost, which
cannot price support drop: a hop with `|σ_w| < |σ_v|` that is not
seed-exit and is not both-weights-`1` costs `1` under that rule and
costs `3` here.

A lexicographically first shortest path from `0` to the body-diagonal site
`(2,2,2)` is the six-step site list

```text
(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,2,2) → (1,2,2) → (2,2,2).
```

The six hop costs along it are `3,1,1,1,1,1`. Their orbit-cost sum is
`8`. Every shortest path uses the same hop-cost multiset `{1,1,1,1,1,3}`.
The path type is the residual under this rule: the unique expensive hop
is the seed-exit, every shortest path leaves the axis after that exit,
and no shortest path uses a support-drop hop.

Do not attach L1. Six-neighbor graph distance is the hop count, not the
named cost.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "An exhibited shortest 0→(2,2,2) path under the named support-drop hop-cost has orbit-cost sum 8, and every shortest path shares hop-cost multiset {1,1,1,1,1,3}. The rule is displayed, not adopted."
trace_class: frontier_discovery
target_claim_id: no_shortcut_body_diagonal_path
target_blocker_text: "exhibit the lex-first shortest 0→(2,2,2) path, the hop-cost list, and the common hop-cost multiset under the named support-drop hop-cost"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "keep the named support-drop hop-cost displayed; do not write it into Admissibility; do not attach L1"
conditional_surface_status: "exact on the six-neighbor graph about one seed; no admissibility or metric adoption"
hypothetical_axiom_status: "no edit; ν is displayed and is not proposed as axiom content"
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
  rule `ν`; the finite ball of six-neighbor graph radius `6` about the
  seed, which contains `(2,2,2)`.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selecting `ν` as a physical cost, writing it
  into Admissibility, attaching L1, and identifying arrival with a
  physical time or metric remain outside the target.

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

`ν(v,w) = 3` if `|σ_v| = 0` or (`|σ_v| = |σ_w| = 1`) or `|σ_w| < |σ_v|`,
else `1`.

Arrival `t(v)` is the least sum of `ν` along a `B_6` path in `Ball_6(s)`
from `s` to `v`. A path is lexicographically first among a set when its
sequence of sites is the least sequence in the dictionary order of
integer triples.

These objects are supplied mathematical data for the theorems below.

## Theorem 1 — Lex-First Shortest Path, Hop Costs, And Sum

On `Ball_6(s)`, a lexicographically first shortest `s → (2,2,2)` path is

```text
P = (
  (0,0,0),
  (0,0,1),
  (0,1,1),
  (0,1,2),
  (0,2,2),
  (1,2,2),
  (2,2,2)
).
```

The six directed hops, inward-weight pairs, and costs are

| hop | pair `(w_v,w_w)` | clause | `ν` |
|---|---|---|---:|
| `(0,0,0) → (0,0,1)` | `(0,1)` | seed-exit | `3` |
| `(0,0,1) → (0,1,1)` | `(1,2)` | neither | `1` |
| `(0,1,1) → (0,1,2)` | `(2,2)` | neither | `1` |
| `(0,1,2) → (0,2,2)` | `(2,2)` | neither | `1` |
| `(0,2,2) → (1,2,2)` | `(2,3)` | neither | `1` |
| `(1,2,2) → (2,2,2)` | `(3,3)` | neither | `1` |

The hop-cost list is `3,1,1,1,1,1`. The orbit-cost sum is
`3+1+1+1+1+1 = 8`. Hence `t(2,2,2) ≤ 8`. The companion runner's Dijkstra
search on `Ball_6(s)` returns the same path and the same value
`t(2,2,2) = 8`, so `P` is shortest.

The second hop leaves the axis. The axis-extension hop
`(0,0,1) → (0,0,2)` would be a both-weights-`1` step of cost `3` and is
not used on `P`. No hop on `P` is a support drop.

## Theorem 2 — Every Shortest Path Has The Same Hop-Cost Multiset

Every shortest `s → (2,2,2)` path in `Ball_6(s)` has exactly six hops and
hop-cost multiset `{1,1,1,1,1,3}`. Displayed, not adopted.

The six-neighbor graph distance from `s` to `(2,2,2)` is `6`, so every
path has at least six hops. The seed-exit hop is present on every path
out of `s` and has cost `3`. Any extra both-weights-`1` hop also has
cost `3`. Any support-drop hop also has cost `3`. A six-hop path that
stays on the first axis for a second step therefore sums to `10`. A path
with seven or more hops sums to at least `3+6 = 9`. A six-hop path
cannot contain a support-drop hop: the only six-hop words from `s` to
`(2,2,2)` are the `90` monotone words with two steps `+e_1`, two steps
`+e_2`, and two steps `+e_3`, and along those words coordinates never
return to zero, so inward weight never drops.

The only way to reach orbit-cost `8` is a six-hop path whose unique
cost-`3` hop is the seed-exit. Among the `90` monotone words, the first
two hops use the same axis on exactly `18` words, and those `18` each
carry one both-weights-`1` hop. The remaining `72` words leave the axis
immediately after seed-exit. Along any such word the costs are one
seed-exit `3` and five ordinary `1`s, so the hop-cost multiset is
`{1,1,1,1,1,3}` and the orbit-cost sum is `8`.

The runner enumerates all shortest paths by predecessor search on the
Dijkstra tree of `Ball_6(s)` and finds exactly these `72` words, each
with hop-cost multiset `{1,1,1,1,1,3}`. No cheaper detour exists in the
ball. A concrete support-drop word such as

```text
(0,0,0) → (0,0,1) → (0,1,1) → (0,1,0) → (0,2,0) → (0,2,1) → (0,2,2) → (1,2,2) → (2,2,2)
```

uses the drop `(0,1,1) → (0,1,0)` of cost `3` and sums to `14`; it is
not shortest. Under the axis-skeleton rule that same drop hop would
cost `1`. The third clause is therefore live as a different rule even
though no shortest `s → (2,2,2)` path uses it.

This common multiset is displayed. It is not adopted as a physical
arrival law, and it is not a leftover of the axis-skeleton path type.

## Theorem 3 — Displayed, Not Adopted

Do not write `ν` into Admissibility. The live Admissibility sentences
remain the quoted nearest-neighbor distribution rule. They do not name
inward weights, seed-exit, support drop, or a numerical hop-cost.

Do not attach L1. Do not identify the named hop-cost with six-neighbor graph distance. The integer `8` is the orbit-cost sum along the exhibited path type, not an L1 length.

The rule and the path are displayed, not adopted. Uniqueness of `ν`
among cost rules is not claimed.

## Proof-Obligation Boundary

| Obligation | Disposition |
|---|---|
| one seed and the six-neighbor stencil | supplied domain |
| inward weights and the named rule `ν` | supplied display |
| lexicographically first shortest path | computed; listed in Theorem 1 |
| six hop costs and their sum | computed; orbit-cost table; sum `8` |
| common hop-cost multiset on every shortest path | proved for monotone words; enumerated on `Ball_6(s)` |
| `ν` written into Admissibility | refused |
| L1 attached as the residual | refused |

## What This Does Not Claim

- `ν` is not Admissibility content and is not a new axiom.
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

Their dependency role is limited to the repository's lattice and
admissibility vocabulary. This theorem separately supplies the named
hop-cost as displayed data. No axiom sentence is edited.

## Runner Contract

The companion runner constructs `Ball_6(s)`, computes Dijkstra arrival
from the seed under `ν`, extracts the lexicographically first shortest
path to `(2,2,2)`, and sums the six computed hop costs. It enumerates
every shortest path and checks the common hop-cost multiset. It quotes
the live Admissibility sentences, checks that the axiom memo is not
edited, and checks that the note keeps `ν` displayed and does not attach
L1. Declared review inputs are this note and the axiom memo only.
