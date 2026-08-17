---
claim_id: support_drop_why_face_k5_fails_b12_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (10,0,0) and (5,5,0) under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_face_k5_fails_b12_2026_08_15.py
---

# Lex-First Paths And Last Hops For The k=5 Face Reverse Fail On B_12(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_12(0)`,
restricted to naming a lex-first shortest walk from `0` to `(10,0,0)`, a
lex-first shortest walk from `0` to `(5,5,0)`, the last hops of those
walks, and the displayed k=5 comparison
`t(10,0,0)^2 / 100 > t(5,5,0)^2 / 50`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_face_k5_fails_b12_2026_08_15.py`](../scripts/support_drop_why_face_k5_fails_b12_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_12(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One origin Dijkstra on `B_12(0)` (2625 sites) gives `t(10,0,0) = 16` and
`t(5,5,0) = 12`. Among all walks of those costs, the lexicographically
first sequences of sites are

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (10,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3` and running
costs `3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16` summing to `16`,
and

`(0,0,0) → (0,1,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (2,5,0) → (3,5,0) → (4,5,0) → (5,5,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1` and running costs
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12` summing to `12`.

The last hops that make `t = 16` versus `t = 12` are the support-drop
`(10,-1,0) → (10,0,0)` of cost `3`, versus the support-preserving face step
`(4,5,0) → (5,5,0)` of cost `1`. After the hop onto `(10,-1,0)` the axis
walk has already spent `13`; the cost-`3` drop raises the arrival to `16`.
The face walk never drops support and never travels on a coordinate axis
after seed-exit, so its last hop stays cost `1` and the arrival stays `12`.

The displayed k=5 comparison is

`t(10,0,0)^2 / 100 = 256/100 = 64/25 < 72/25 = 144/50 = t(5,5,0)^2 / 50`,

equivalently `50 · 256 = 12800 < 14400 = 100 · 144`. Face reverse therefore
fails at `k = 5`. That fail is displayed, not adopted. The two walks and
their last hops are not leftover of fail8.

Every in-ball neighbor of `(10,0,0)` has incoming hop-cost `3`: the two
axis neighbors are both-weights-`1`, and the four off-axis neighbors are
support drops. The in-ball neighbors of `(5,5,0)` are the four face
neighbors `(4,5,0)`, `(6,5,0)`, `(5,4,0)`, `(5,6,0)` of cost `1` and the
two support-drop neighbors `(5,5,±1)` of cost `3`.

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

A walk is lex-first among shortest walks to a named site when its sequence
of sites is the least tuple of integer triples, compared coordinatewise,
among all walks of cost `t` at that site.

Face reverse at integer scale `k = 5` means the displayed comparison
`t(10,0,0)^2 / 100 > t(5,5,0)^2 / 50`. The pair is not leftover of fail8:
fail8 named the lex-first walks to `(8,0,0)` and `(4,4,0)`. Naming the
k=5 walks is a separate finite exhibit.

## Theorem 1 — Arrivals And Lex-First Shortest Walks

On `B_12(0)` the computed arrivals are `t(10,0,0) = 16` and
`t(5,5,0) = 12`. The lex-first walk of cost `16` to `(10,0,0)` is the
thirteen-site walk recorded above. The twelve hop-costs are seed-exit
`3`, ten support-preserving cost-`1` steps along the line `y = -1`
from `(0,-1,0)` to `(10,-1,0)`, and a final support-drop `3` from
`(10,-1,0)` onto `(10,0,0)`. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16`.

The lex-first walk of cost `12` to `(5,5,0)` is the eleven-site walk
recorded above. The ten hop-costs are seed-exit `3` onto `(0,1,0)` and
then nine support-preserving or support-increasing cost-`1` steps that
stay off the axes, ending at `(5,5,0)`. The running costs after each hop
are `3, 4, 5, 6, 7, 8, 9, 10, 11, 12`.

The same axis cost is realized by later walks, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (10,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3`. That walk is
also shortest, but `(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.
The same face cost is realized by

`(0,0,0) → (1,0,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (2,5,0) → (3,5,0) → (4,5,0) → (5,5,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1`. That walk is also
shortest, but `(0,1,0)` precedes `(1,0,0)`, so it is not lex-first.

This names two paths. It is not leftover of fail8.

## Theorem 2 — Displayed k=5 Reverse Fails

Whether

`t(10,0,0)^2 / 100 > t(5,5,0)^2 / 50`

holds is a displayed comparison, not an adopted law. Substituting the
Dijkstra arrivals gives `256/100 = 64/25` and `144/50 = 72/25`. Then
`64/25 < 72/25`, so the inequality fails. The integer form is
`50 · 256 = 12800 < 14400 = 100 · 144`.

The last hops named in Theorem 1 are what make the two arrivals `16` and
`12`. They are not a restatement of this fail bit, and they are not
leftover of fail8.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_12(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walks are shortest
paths under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walks are not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhibited lex-first shortest walks to (10,0,0) and (5,5,0) on the finite ball B_12(0) under one named hop-cost, together with a displayed k=5 comparison that fails. The rule is displayed, not adopted."
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
- Any reuse of the fail8 k=4 walks as a substitute for exhibiting these
  k=5 walks.

## claim_scope

Lex-first shortest paths to (10,0,0) and (5,5,0) under the named support-drop hop-cost on B_12(0) are named. Displayed, not adopted.
