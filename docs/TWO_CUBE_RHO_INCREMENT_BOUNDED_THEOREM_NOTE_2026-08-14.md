---
claim_id: two_cube_rho_increment_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the two-cube occupancy step, Δρ(A) equals the number of new locks in A and Δρ(B) equals the number of new locks in B. Shared new locks count in both. Seed (0,0,0) gives Δρ(A)=3, Δρ(B)=1."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_rho_increment_2026_08_14.py
---

# Cube Source Increments By Formations In That Cube

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact increment identity on one occupancy step.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_rho_increment_2026_08_14.py`](../scripts/two_cube_rho_increment_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

`ρ(C)` is the occupancy count on cube `C`. After one occupancy
step from seed `{(0,0,0)}`, three sites form: two A-only and one
shared. `Δρ(A)=3`, `Δρ(B)=1`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Δρ = new locks in that cube."
trace_class: frontier_discovery
target_claim_id: two_cube_rho_increment
target_blocker_text: "source does not read records"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed seed step"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name `Δρ`.

## Theorem 1 — identity

`Δρ(A) = |new locks ∩ A|`, `Δρ(B) = |new locks ∩ B|`.

## Theorem 2 — seed numbers

Seed step: new locks `{(1,0,0),(0,1,0),(0,0,1)}`. Shared one.
`Δρ(A)=3`, `Δρ(B)=1`.

## Theorem 3 — display

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “`Δρ(B)=0` on the seed step” must fail.
2. Predicate “empty step changes `ρ`” must fail.

Identity gates: `occ_step`, `rho`, `new_in`.

## Honest-auditor / Boundary

One step, two cubes. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
