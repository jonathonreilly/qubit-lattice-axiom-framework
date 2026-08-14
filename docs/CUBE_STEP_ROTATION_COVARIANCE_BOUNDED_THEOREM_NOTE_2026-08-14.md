---
claim_id: cube_step_rotation_covariance_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed 2×2×2 cube, the occupancy step commutes with the 90° rotation (x,y,z)↦(1−y,x,z) about the cube center: R(step(s))=step(R(s)) on all 256 occupancy configurations. A seed at (0,0,0) rotates to a seed at another corner and the formation pattern rotates with it. Empty cube is fixed. Covariance of the update, not of n. Not a TOE, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_step_rotation_covariance_2026_08_14.py
---

# Cube Step Commutes With A 90° Rotation

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact covariance of the `{0,1}^3` occupancy update
under one proper-cube generator. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_step_rotation_covariance_2026_08_14.py`](../scripts/cube_step_rotation_covariance_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Same 2×2×2 occupancy step as the cube6nn comparator: locked
sites stay; unread sites form iff `n≠0`; off-cube occupancy is
`0`. A 90° rotation about `z` through the cube center acts by

```text
(x, y, z) ↦ (1 − y, x, z)
```

on `{0,1}^3`. For every one of the 256 occupancy configurations,
`R(step(s))=step(R(s))`.

A seed at `(0,0,0)` rotates to a seed at another corner; the
formation pattern rotates with it. The empty cube is fixed.

This is covariance of the *update*, not of `n`. Not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact R(step(s))=step(R(s)) on all 256 cube occupancies."
trace_class: frontier_discovery
target_claim_id: cube_step_rotation_covariance
target_blocker_text: "the cube step picks an origin"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed 2x2x2 cube and one 90° generator"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name this covariance.

## Theorem 1 — rotation of the cube

`(x,y,z)↦(1−y,x,z)` is a permutation of `{0,1}^3` of order 4.

## Theorem 2 — all 256 configs

`R(step(s))=step(R(s))` on every occupancy configuration.

## Theorem 3 — seed rotates

Seed `(0,0,0)` maps to `(1,0,0)`. The step-1 trio rotates with it.

## Theorem 4 — empty cube

The empty cube is a fixed point of both `R` and `step`.

## Theorem 5 — not a TOE

Quoted Record and Admissibility do not name the covariance.
Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “some config fails `R∘step=step∘R`” must fail.
2. Predicate “seed stays at `(0,0,0)` under `R`” must fail.
3. Predicate “note adopts the cube step” must fail.

Identity gates: `rotate`, `n_at`, `step`.

## Honest-auditor / Boundary

256 configurations, one generator, exact `Q`. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- Qubit remains `M_2(C)`.
