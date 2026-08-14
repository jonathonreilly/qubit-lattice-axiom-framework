---
claim_id: two_cube_exterior_vacuum_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube occupancy step, off-patch occupancy defaults to 0. From seed (0,0,0), the B-front site (2,0,0) has n=0 and does not form. If the virtual neighbor (3,0,0) is occupied, n_x at (2,0,0) equals (1-0)/3 ≠ 0 and the site forms. The displayed exterior vacuum is why B-only sites stay unread on step 1."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_exterior_vacuum_2026_08_14.py
---

# Exterior Vacuum Is Load-Bearing On The Two-Cube Occupancy Step

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `n` and formation on one seed step, with and without a
displayed off-patch occupancy.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_exterior_vacuum_2026_08_14.py`](../scripts/two_cube_exterior_vacuum_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Twelve vertices, two cubes sharing `x=1`. Occupancy step: locked
sites stay; unread sites form iff `n ≠ 0`. The three-axis field is

`n_i(x) = (occ(x+e_i) − occ(x−e_i))/3`.

Off-patch occupancy defaults to `0`. That default is the displayed
exterior vacuum. It is extra bookkeeping, not axiom text.

Seed `{(0,0,0)}`. The B-front site `(2,0,0)` has vacuum neighbors
on every axis, so `n=(0,0,0)` and it does not form. Every B-only
site stays unread on this step.

If the virtual neighbor `(3,0,0)` is occupied, then
`n_x(2,0,0)=(1−0)/3=1/3 ≠ 0` and `(2,0,0)` forms. The vacuum
exterior is therefore load-bearing for the unread B-only sites.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact n and formation at the B-front, with default off-patch occupancy 0 versus a displayed occupied exterior."
trace_class: frontier_discovery
target_claim_id: two_cube_exterior_vacuum
target_blocker_text: "off-patch occupancy is implicit"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed seed step and one exterior witness"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> A site with no record cannot be read.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name off-patch occupancy or this vacuum default.

## Theorem 1 — default vacuum, B-front unread

Default off-patch occupancy is `0`. On the seed, `n` at `(2,0,0)`
is `(0,0,0)`. The site does not form. All four B-only vertices
stay unread after one `occ_step`.

## Theorem 2 — occupied exterior forms the B-front

If the virtual neighbor `(3,0,0)` is occupied, then
`n_x(2,0,0)=(1−0)/3 ≠ 0`. The B-front forms. The other three
B-only sites remain unread under that one-site exterior.

## Theorem 3 — load-bearing

The displayed vacuum exterior is why B-only sites stay unread on
step 1. Occupying `(3,0,0)` is enough to form `(2,0,0)`. The
unread B-front is not a seed-distance identity independent of the
off-patch default.

## Theorem 4 — display

The exterior map is displayed extra. Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “`(2,0,0)` forms from the seed under default vacuum” must fail.
2. Predicate “occupied `(3,0,0)` leaves `n=0` at `(2,0,0)`” must fail.

Identity gates: `n_at_Bfront`, `forms_if_exterior`.
The step gate `occ_step` accepts an optional exterior map.

## Honest-auditor / Boundary

One seed, one B-front, one exterior witness. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
