---
claim_id: two_cube_shared_normal_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "From seed (0,0,0), the occupancy kernel at the forming shared-face site (1,0,0) is n = (-1/3, 0, 0), parallel to the shared-face normal (1,0,0). The other first-wave sites have n along their own axes, not along that shared-face normal."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_shared_normal_2026_08_14.py
---

# Shared-Face Formation Has n Along The Face Normal

**Date:** 2026-08-14
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** exact direction of `n` at one shared-face site.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_shared_normal_2026_08_14.py`](../scripts/two_cube_shared_normal_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Twelve vertices, two cubes sharing the face `x=1`. Occupancy
`o : V → {0,1}` is `0` off the patch. At an unread site

```text
n_μ = (o_{+μ} − o_{-μ}) / 3.
```

Locked sites stay. An unread site forms iff `n ≠ 0`.

Seed `{(0,0,0)}`. The shared-face site `(1,0,0)` is unread. Its
six nearest neighbors give `n = (-1/3, 0, 0)`. The shared-face
normal is `(1,0,0)`. These two vectors are parallel:
`n = (-1/3) (1,0,0)`.

The other first-wave sites `(0,1,0)` and `(0,0,1)` have
`n = (0,-1/3,0)` and `n = (0,0,-1/3)`. Those are not parallel
to the shared-face normal.

This is a displayed direction of `n`, not a unique-support
statement about dual paths or tree-gauge faces.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact n at (1,0,0) is parallel to the shared-face normal."
trace_class: frontier_discovery
target_claim_id: two_cube_shared_normal
target_blocker_text: "n at the shared-face site is not shown along the face normal"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed seed and shared-face site"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name this `n` or this shared-face normal.

## Theorem 1 — geometry

Twelve vertices. Shared face `F*` is `x=1`. Its geometric
normal is `(1,0,0)`.

## Theorem 2 — kernel at the shared-face site

Seed `(0,0,0)`. At unread `(1,0,0)`,
`n = (-1/3, 0, 0)`. So `n ≠ 0` and that site forms.

## Theorem 3 — parallel to the shared-face normal

`n` is a nonzero scalar multiple of `(1,0,0)`. Cross product
with the shared-face normal vanishes.

## Theorem 4 — other first-wave axes

At `(0,1,0)`, `n = (0,-1/3,0)`. At `(0,0,1)`,
`n = (0,0,-1/3)`. Neither is parallel to `(1,0,0)`.

## Theorem 5 — display

Qubit remains `M_2(C)`. QCD is unused. The kernel and the
normal are displayed, not axiom text.

## Mutations

1. Predicate “`n` at `(1,0,0)` is orthogonal to `(1,0,0)`” must fail.
2. Predicate “`n` at `(0,1,0)` is parallel to the shared-face normal” must fail.

Identity gates: `nvec`, `parallel_to`, `shared_normal`.

## Honest-auditor / Boundary

One seed, one shared-face site, one direction. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Not a unique-support statement about dual paths or tree-gauge faces.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
