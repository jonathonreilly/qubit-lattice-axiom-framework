---
claim_id: cube_222_occupancy_step_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On a displayed 2×2×2 cube with 6-NN occupancy (missing neighbor occupancy 0), one update locks every unread site with n≠0. A seed at (0,0,0) forms the three axis neighbors on step 1, the three face-diagonals on step 2, and (1,1,1) on step 3. Source/tick go 0→3→6→7→7. The empty cube is a fixed point. This is the occupancy step on Z^3 adjacency, not a 1D line extra, not Newton, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_222_occupancy_step_2026_08_14.py
---

# Occupancy Step On A Displayed `2×2×2` Cube

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock update on eight sites. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_222_occupancy_step_2026_08_14.py`](../scripts/cube_222_occupancy_step_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Sites are `{0,1}^3`. Occupancy of a neighbor outside the cube is
`0`. At an unread site `n_μ = (o_{+μ} − o_{-μ})/3`. The one
update locks every unread site with `n ≠ 0` and leaves locked
sites. Source and tick equal the number of new locks.

Seed `(0,0,0)`. Step 1 forms the three axis neighbors. Step 2
forms the three face-diagonals (`k = 2`). Step 3 forms
`(1,1,1)`. Step 4 is the identity. Source/tick:
`0 → 3 → 6 → 7 → 7`. The empty cube does not form.

This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-to-lock update on a displayed 2x2x2 cube."
trace_class: frontier_discovery
target_claim_id: cube_222_occupancy_step
target_blocker_text: "executable update only exists on a 1D line extra"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit; joint cube+PVM member remains open"
conditional_surface_status: "exact for the displayed 2x2x2 comparator"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name this cube update.

## Theorem 1 — seed

Only `(0,0,0)` locked. Source `0`. Each axis neighbor has
`n` with `k = 1`. Face-diagonals and `(1,1,1)` have `n = 0`.

## Theorem 2 — three axis sites form together

After one step the three axis neighbors are locked. Formations `3`.

## Theorem 3 — face-diagonals then the opposite corner

Step 2 forms the three face-diagonals. Step 3 forms `(1,1,1)`.
Step 4 is permanence.

## Theorem 4 — empty cube is a fixed point

No seed, no formations.

## Theorem 5 — not a TOE

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “step 1 forms `(1,1,1)`” must fail.
2. Predicate “empty cube forms the origin” must fail.
3. Predicate “step 4 increments source” must fail.

Identity gates: `occ(site, locks)`, `nvec(site, locks)`, `step(locks)`.

## Honest-auditor / Boundary

Eight sites, four snapshots, exact `Q`. Not Newton. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
