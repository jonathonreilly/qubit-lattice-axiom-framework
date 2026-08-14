---
claim_id: two_cube_seed_class_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Among the 12 single-site seeds on the displayed two-cube, the four A-only sites (x=0) each form 3 sites, the four shared sites (x=1) each form 4 sites, and the four B-only sites (x=2) each form 3 sites. This is a classification of one-site seeds under the displayed occupancy step, not a new patch and not a gauge clone."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_seed_class_2026_08_14.py
---

# Single-Site Seed Classes On The Two-Cube

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact formation counts for twelve single-site seeds.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_seed_class_2026_08_14.py`](../scripts/two_cube_seed_class_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Twelve vertices, two cubes sharing `x=1`. Occupancy step: locked
sites stay; unread sites form iff `n ≠ 0`. Off-patch occupancy is
`0`. The twelve single-site seeds fall into three classes by the
`x` coordinate of the seed.

A-only corners (`x=0`, four sites) each form 3 unread sites.
Shared vertices (`x=1`, four sites) each form 4 unread sites.
B-only corners (`x=2`, four sites) each form 3 unread sites.

The count is the number of on-patch nearest neighbors of the seed:
three at an A-only or B-only corner, four at a shared face vertex.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact formation counts on all twelve single-site seeds of the two-cube occupancy step."
trace_class: frontier_discovery
target_claim_id: two_cube_seed_class
target_blocker_text: "one-site seeds on the two-cube are unclassified"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed twelve single-site seeds"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name these seed classes.

## Theorem 1 — twelve single-site seeds

The displayed vertices are

```text
A-only:  (0,0,0) (0,0,1) (0,1,0) (0,1,1)
shared:  (1,0,0) (1,0,1) (1,1,0) (1,1,1)
B-only:  (2,0,0) (2,0,1) (2,1,0) (2,1,1)
```

Each vertex is one single-site seed. There are twelve.

## Theorem 2 — A-only seeds form 3

Each of the four `x=0` seeds forms exactly three unread sites.
Example: seed `(0,0,0)` forms `{(1,0,0),(0,1,0),(0,0,1)}`.

## Theorem 3 — shared seeds form 4

Each of the four `x=1` seeds forms exactly four unread sites.
Example: seed `(1,0,0)` forms `{(0,0,0),(2,0,0),(1,1,0),(1,0,1)}`.

## Theorem 4 — B-only seeds form 3

Each of the four `x=2` seeds forms exactly three unread sites.
Example: seed `(2,0,0)` forms `{(1,0,0),(2,1,0),(2,0,1)}`.

## Theorem 5 — display

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “an A-only seed forms 4” must fail.
2. Predicate “a shared seed forms 3” must fail.
3. Predicate “all twelve seeds form the same number” must fail.

Identity gates: `formed_from`, `class_counts`.

## Honest-auditor / Boundary

Twelve seeds, three classes, two integers per class. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
- Not a new occupancy patch. Not a gauge clone.
