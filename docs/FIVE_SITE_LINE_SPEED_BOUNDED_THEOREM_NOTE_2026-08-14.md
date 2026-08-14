---
claim_id: five_site_line_speed_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On a displayed 5-site line the occupancy step has speed 1: a seed lock at site 0 makes site i form at step i and not earlier. After t steps, sites 0..t are locked and t+1..4 are unread. Source/tick go 0,1,2,3,4,4. The empty line is a fixed point. This is a light-cone bound on composition, not Newton, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/five_site_line_speed_2026_08_14.py
---

# Five-Site Line, Speed One

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock snapshots on five sites. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/five_site_line_speed_2026_08_14.py`](../scripts/five_site_line_speed_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Sites `0,1,2,3,4` on a line. `n_x = (o_right − o_left)/3`. Locked
sites stay. An unread site forms iff `n_x ≠ 0`.

Seed lock at site `0`. Site `i` first has `n_x ≠ 0` when site
`i−1` is occupied, so it forms at step `i` and not earlier.
After `t` steps the locked set is `{0,…,t}`. Step 5 is the
identity. Source/tick: `0 → 1 → 2 → 3 → 4 → 4`.

This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact speed-1 formation wave on a displayed 5-site line."
trace_class: frontier_discovery
target_claim_id: five_site_line_speed
target_blocker_text: "composition is only two ticks / three sites"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed 5-site line"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name this wave.

## Theorem 1 — cone

For each `t = 0,…,4`, after `t` steps sites `0..t` are locked
and sites `t+1..4` are unread.

## Theorem 2 — site 3 is unread until step 3

At `t = 1`, site 3 has `n_x = 0`. At `t = 2` it is still unread
but `n_x ≠ 0`. At `t = 3` it is locked.

## Theorem 3 — permanence and empty

Step 5 does not form. The empty line is a fixed point.

## Theorem 4 — not a TOE

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “site 3 forms at step 2” must fail.
2. Predicate “step 5 increments source” must fail.
3. Predicate “empty line forms site 0” must fail.

Identity gates: `nx(site, locks)`, `step(locks)`, `locked_prefix(locks)`.

## Honest-auditor / Boundary

Five sites, six snapshots, exact `Q`. Not Newton. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No continuum light cone.
- Qubit remains `M_2(C)`.
