---
claim_id: two_cube_unique_monotone_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed two-cube occupancy step, the formation count is 0 on the empty configuration and increases by the number of new locks. ρ(A) is monotone but is not that integer. Among {formation count, ρ(A), ρ(B), lock count}, only the formation count vanishes on empty and rises by exactly the new-lock count."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_unique_monotone_2026_08_14.py
---

# Unique Empty-Vanishing Monotone On The Two-Cube Step

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integers on two occupancy snapshots.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_unique_monotone_2026_08_14.py`](../scripts/two_cube_unique_monotone_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Twelve vertices, two cubes sharing `x=1`. Occupancy step: locked
sites stay; unread sites form iff `n ≠ 0`. Empty occupancy is a
fixed point.

The formation count `F` is 0 on empty and rises by the number of
new locks. `ρ(A)` (occupancy sum on `A`) is monotone on the seed
step but starts at 1 and rises by 3, not by `F` in the empty-based
sense. Lock count equals `F` plus the seed size.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact comparison of four occupancy integers on the two-cube step."
trace_class: frontier_discovery
target_claim_id: two_cube_unique_monotone
target_blocker_text: "clock is a disconnected table"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed two-cube step"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name this monotone.

## Theorem 1 — empty

Empty has `F=0`, `ρ(A)=ρ(B)=0`, lock count 0.

## Theorem 2 — seed step

Seed `{(0,0,0)}`. One step forms three sites. `F: 0→3`.
`ρ(A): 1→4`. `ρ(B): 0→1`. Locks: `1→4`.

## Theorem 3 — only `F` matches the empty-vanishing increment

`F` vanishes on empty and rises by the new-lock count. `ρ(A)`
does not vanish on the seed. Lock count tracks `F` plus seed size.

## Theorem 4 — display

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “`ρ(A)` vanishes on the seed” must fail.
2. Predicate “empty has a nonzero formation count” must fail.

Identity gates: `occ_step`, `formed`, `rho`, `F_of`.

## Honest-auditor / Boundary

Two snapshots, four integers. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
