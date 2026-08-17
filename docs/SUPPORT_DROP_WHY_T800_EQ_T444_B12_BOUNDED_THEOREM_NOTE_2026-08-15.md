---
claim_id: support_drop_why_t800_eq_t444_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (8,0,0) and (4,4,4) under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_t800_eq_t444_b12_2026_08_15.py
---

# Lex-First Shortest Paths To (8,0,0) And (4,4,4) On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
restricted to naming a lex-first shortest walk from `0` to `(8,0,0)`, a
lex-first shortest walk from `0` to `(4,4,4)`, the two running-cost
sequences, and the hop that equalizes the arrivals.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_t800_eq_t444_b12_2026_08_15.py`](../scripts/support_drop_why_t800_eq_t444_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not claimed.

One origin Dijkstra on `B_12(0)` (2625 sites) gives `t(8,0,0) = 14` and
`t(4,4,4) = 14`. Among all walks of those costs, the lexicographically first
sequence of sites to each target is recorded in Theorem 1. The two
running-cost sequences both terminate at `14`. The hop that equalizes the
arrivals is the last hop of the axis walk, `(8,-1,0) → (8,0,0)`, of cost
`3`.

These named walks and that hop are not leftover of the shared-shell bit.
The integer pair `t=14`, `t=14` does not name either site sequence or the
equalizing hop.

The rule is displayed, not adopted. Do not write `ν` into Admissibility.
Do not attach L1.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations.

For each site, the probability distribution over the possibilities is
determined by, and varies with, the nearest-neighbor conditions.

Lattice supplies the six-neighbor graph and the ball. Admissibility supplies
none of the hop costs. The integers `3` and `1`, the support-size clauses,
and the arrival function `t` are separately displayed mathematical inputs.
No axiom text is edited.

## Named Rule

Let `B_12(0) = { v ∈ Z^3 : |v|_1 ≤ 12 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_12(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A walk is lex-first among shortest walks to a named target when its
sequence of sites is the least tuple of integer triples, compared
coordinatewise, among all walks of cost `t` at that target.

## Theorem 1 — Lex-First Shortest Walks

On `B_12(0)` the computed arrivals are `t(8,0,0) = 14` and
`t(4,4,4) = 14`.

The lex-first walk of cost `14` to `(8,0,0)` is

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (8,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 3` summing to `14`.

The lex-first walk of cost `14` to `(4,4,4)` is

`(0,0,0) → (0,0,1) → (0,1,1) → (0,1,2) → (0,1,3) → (0,1,4) → (0,2,4) → (0,3,4) → (0,4,4) → (1,4,4) → (2,4,4) → (3,4,4) → (4,4,4)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1` summing to `14`.

The same costs are realized by later walks. The axis walk that starts
`(0,0,0) → (1,0,0) → (1,1,0)` and ends `(8,1,0) → (8,0,0)` has the same
hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 3`, but `(0,-1,0)` precedes
`(1,0,0)`. The body-diagonal walk that starts `(0,0,0) → (1,0,0)` and
climbs the first octant has hop-costs `3` then eleven `1`s, but
`(0,0,1)` precedes `(1,0,0)`.

This names two paths. Uniqueness is not claimed among hop-costs.

## Theorem 2 — Running-Cost Sequences And The Equalizing Hop

The running-cost sequence along the lex-first walk to `(8,0,0)` is

`3, 4, 5, 6, 7, 8, 9, 10, 11, 14`.

The running-cost sequence along the lex-first walk to `(4,4,4)` is

`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14`.

Both sequences equal `14` at their last entry. Displayed, not adopted.

After nine hops both running costs are `11`. The next hop on the axis
walk is `(8,-1,0) → (8,0,0)`, a support-drop of cost `3`, taking that
walk from `11` to `14`. The body-diagonal walk then uses three cost-`1`
hops, the last of them `(3,4,4) → (4,4,4)`, to the same integer `14`.
That support-drop is the hop that equalizes the arrivals.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walks are shortest
paths under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walks are not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhibited lex-first shortest walks on the finite ball B_12(0) under one named hop-cost, with running-cost sequences both equal to 14. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_12(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## What This Note Does Not Claim

- Uniqueness of `ν` among hop-costs with these arrivals or these walks.
- Any edit of Lattice, Qubit, Admissibility, or Record.
- Any attachment to L1.
- Any continuum potential, any inverse-power kernel, and any gravitational
  identification.
- Any statement off `B_12(0)`.
- Any reuse of the shared-shell bit as a substitute for exhibiting the
  walks or the equalizing hop.
