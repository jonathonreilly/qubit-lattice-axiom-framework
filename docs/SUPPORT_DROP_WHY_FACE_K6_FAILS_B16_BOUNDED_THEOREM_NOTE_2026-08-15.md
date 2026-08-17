---
claim_id: support_drop_why_face_k6_fails_b16_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Lex-first shortest paths to (12,0,0) and (6,6,0) under the named support-drop hop-cost on B_16(0) are named. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/support_drop_why_face_k6_fails_b16_2026_08_15.py
---

# Lex-First Paths And Last Hops For The k=6 Face Reverse On B_16(0)

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** one named nearest-neighbor hop-cost on the ℓ¹ ball `B_16(0)`,
restricted to naming a lex-first shortest walk from `0` to `(12,0,0)`, a
lex-first shortest walk from `0` to `(6,6,0)`, the last hops of those
walks, and the displayed k=6 comparison
`t(12,0,0)^2 / 144 > t(6,6,0)^2 / 72`.
**Audit-status authority:** independent audit lane only. This note authors
no audit verdict and predicts none.
**Primary runner:**
[`scripts/support_drop_why_face_k6_fails_b16_2026_08_15.py`](../scripts/support_drop_why_face_k6_fails_b16_2026_08_15.py)
**Cache:** none. `cache_write: false`.

## Result Up Front

Write `|σ_v|` for the number of nonzero coordinates of `v ∈ Z^3`. On a
directed nearest-neighbor hop `v → w` still inside `B_16(0)`, the displayed
rule `ν` is

`ν(v→w) = 3` if `|σ_v|=0` or `(|σ_v|=|σ_w|=1)` or `|σ_w| < |σ_v|`,
else `1`.

The first clause is seed-exit. The second is both weights `1`. The third is
support drop. Those three clauses are the whole rule. Uniqueness is not
claimed.

One origin Dijkstra on `B_16(0)` (6017 sites) gives `t(12,0,0) = 18` and
`t(6,6,0) = 14`. Among all walks of those costs, the lexicographically
first sequences of sites are

`(0,0,0) → (0,-1,0) → (1,-1,0) → (2,-1,0) → (3,-1,0) → (4,-1,0) → (5,-1,0) → (6,-1,0) → (7,-1,0) → (8,-1,0) → (9,-1,0) → (10,-1,0) → (11,-1,0) → (12,-1,0) → (12,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3` and running
costs `3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18` summing to `18`,
and

`(0,0,0) → (0,1,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (1,6,0) → (2,6,0) → (3,6,0) → (4,6,0) → (5,6,0) → (6,6,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1` and running costs
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14` summing to `14`.

The last hops that make `t = 18` versus `t = 14` are the support-drop
`(12,-1,0) → (12,0,0)` of cost `3`, versus the support-preserving face
step `(5,6,0) → (6,6,0)` of cost `1`. After the hop onto `(12,-1,0)` the
axis walk has already spent `15`; that one cost-`3` hop raises the
arrival to `18`. The site `(12,-1,0)` has ℓ¹ norm `13` and therefore lies
in `B_16(0)`, so the walk can stay on the line `y = -1` through `x = 12`
and drop support only once. The face walk never drops support and never
travels on a coordinate axis after seed-exit, so its last hop stays
cost `1` and the arrival stays `14`.

The displayed k=6 comparison is

`t(12,0,0)^2 / 144 = 324/144 = 9/4` versus
`t(6,6,0)^2 / 72 = 196/72 = 49/18`,

equivalently `72 · 324 = 23328 < 28224 = 144 · 196`. Then
`9/4 = 40.5/18 < 49/18`, so

`t(12,0,0)^2 / 144 > t(6,6,0)^2 / 72`

fails. Face reverse therefore fails at `k = 6` on `B_16(0)`, because
`t(12,0,0)` is `18`. That no bit is displayed, not adopted. The two
walks and their last hops are not leftover of the no bit.

The in-ball neighbors of `(12,0,0)` are `(11,0,0)`, `(13,0,0)`,
`(12,-1,0)`, `(12,1,0)`, `(12,0,-1)`, and `(12,0,1)`. Each incoming hop
from those six sites has cost `3` under `ν`. The in-ball neighbors of
`(6,6,0)` are `(5,6,0)`, `(7,6,0)`, `(6,5,0)`, `(6,7,0)`, `(6,6,-1)`,
and `(6,6,1)`. Incoming hops from the four face-plane sites have
cost `1`; incoming hops from `(6,6,-1)` and `(6,6,1)` are support drops
of cost `3`.

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

Let `B_16(0) = { v ∈ Z^3 : |v|_1 ≤ 16 }`. Directed edges are the six
nearest-neighbor steps whose both ends lie in the ball. For `v ∈ B_16(0)`,
`t(v)` is the least sum of `ν` along a directed path from `0` to `v` in
that graph.

A walk is lex-first among shortest walks to a named site when its sequence
of sites is the least tuple of integer triples, compared coordinatewise,
among all walks of cost `t` at that site.

Face reverse at integer scale `k = 6` means the displayed comparison
`t(12,0,0)^2 / 144 > t(6,6,0)^2 / 72`. The pair is not leftover of the
no bit: naming the two lex-first walks and the last hops is a separate
finite exhibit.

## Theorem 1 — Arrivals And Lex-First Shortest Walks

On `B_16(0)` the computed arrivals are `t(12,0,0) = 18` and
`t(6,6,0) = 14`. The lex-first walk of cost `18` to `(12,0,0)` is the
fifteen-site walk recorded above. The fourteen hop-costs are seed-exit
`3`, twelve support-preserving or support-increasing cost-`1` steps along
the line `y = -1` from `(0,-1,0)` to `(12,-1,0)`, and a final support-drop
`3` from `(12,-1,0)` onto `(12,0,0)`. The running costs after each hop are
`3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18`.

The lex-first walk of cost `14` to `(6,6,0)` is the thirteen-site walk
recorded above. The twelve hop-costs are seed-exit `3` onto `(0,1,0)` and
then eleven support-preserving or support-increasing cost-`1` steps that
stay off the axes, ending at `(6,6,0)`. The running costs after each hop
are `3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14`.

The same axis cost is realized by later walks, for example

`(0,0,0) → (1,0,0) → (1,1,0) → (2,1,0) → (3,1,0) → (4,1,0) → (5,1,0) → (6,1,0) → (7,1,0) → (8,1,0) → (9,1,0) → (10,1,0) → (11,1,0) → (12,1,0) → (12,0,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3`. That walk is
also shortest, but `(0,-1,0)` precedes `(1,0,0)`, so it is not lex-first.
The same face cost is realized by

`(0,0,0) → (1,0,0) → (1,1,0) → (1,2,0) → (1,3,0) → (1,4,0) → (1,5,0) → (1,6,0) → (2,6,0) → (3,6,0) → (4,6,0) → (5,6,0) → (6,6,0)`

with hop-costs `3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1`. That walk is also
shortest, but `(0,1,0)` precedes `(1,0,0)`, so it is not lex-first.

This names two paths. It is not leftover of the no bit.

## Theorem 2 — Displayed k=6 Reverse Fails

Whether

`t(12,0,0)^2 / 144 > t(6,6,0)^2 / 72`

holds is a displayed comparison, not an adopted law. Substituting the
Dijkstra arrivals gives `324/144 = 9/4` and `196/72 = 49/18`. Then
`9/4 = 40.5/18 < 49/18`, so the inequality fails. The integer form is
`72 · 324 = 23328 < 28224 = 144 · 196`.

The last hops named in Theorem 1 are what make the two arrivals `18` and
`14`. They are not a restatement of this no bit.

## Theorem 3 — Displayed, Not Adopted

The rule `ν` is a displayed scoring device on `B_16(0)`. Do not write `ν`
into Admissibility. Do not attach L1. The exhibited walks are shortest
paths under that displayed rule. Uniqueness is not claimed among hop-costs,
and the walks are not offered as a replacement for unit-cost first arrival.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exhibited lex-first shortest walks to (12,0,0) and (6,6,0) on the finite ball B_16(0) under one named hop-cost, together with a displayed k=6 comparison that fails. The rule is displayed, not adopted."
trace_class: frontier_discovery
artifact_role: theorem
conditional_surface_status: "exact on B_16(0) for the displayed rule ν; no Admissibility edit; not attached to L1"
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
- Any statement off `B_16(0)`.
- Any reuse of the k=6 no bit as a substitute for exhibiting the walks.

## claim_scope

Lex-first shortest paths to (12,0,0) and (6,6,0) under the named support-drop hop-cost on B_16(0) are named. Displayed, not adopted.
