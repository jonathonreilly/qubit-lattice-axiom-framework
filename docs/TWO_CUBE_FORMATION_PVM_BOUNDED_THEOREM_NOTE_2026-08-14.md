---
claim_id: two_cube_formation_pvm_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "The three sites that form from seed (0,0,0) each have k=|3n|^2=1. The displayed PVM traces are 2/3 and 1/3."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_formation_pvm_2026_08_14.py
---

# First-Wave PVM Traces On The Two-Cube

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `k=1` traces at three forming sites.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_formation_pvm_2026_08_14.py`](../scripts/two_cube_formation_pvm_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Seed `(0,0,0)`. The three forming sites each have one unbalanced
axis, `k=1`. Traces `(3±1)/6 = 2/3, 1/3`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact k=1 traces at the three first-wave sites."
trace_class: frontier_discovery
target_claim_id: two_cube_formation_pvm
target_blocker_text: "measure disconnected from the two-cube step"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the three first-wave sites"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name these traces.

## Theorem 1 — three formers, `k=1`

`(1,0,0)`, `(0,1,0)`, `(0,0,1)` each have `k=1`.

## Theorem 2 — traces

`2/3` and `1/3`.

## Theorem 3 — display

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “a first-wave site has `k=2`” must fail.
2. Predicate “traces are `1/2, 1/2`” must fail.

Identity gates: `nvec`, `k_of`, `traces_k1`.

## Honest-auditor / Boundary

Three sites, `k=1`. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
