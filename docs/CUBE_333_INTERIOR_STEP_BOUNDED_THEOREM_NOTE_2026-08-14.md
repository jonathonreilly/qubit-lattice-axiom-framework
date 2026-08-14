---
claim_id: cube_333_interior_step_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On a displayed 3×3×3 cube the occupancy step seeded at the interior site (1,1,1) forms the 6 face-centers on step 1 (k=1), the 12 edge-centers on step 2 (k=2), and the 8 corners on step 3 (k=3). Source/tick go 0→6→18→26→26. The empty 27-site cube is a fixed point. This is the update on a patch with a full 6-NN interior, not a 2×2×2 corner cube, not Newton, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_333_interior_step_2026_08_14.py
---

# Occupancy Step On A `3×3×3` Interior

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock update on 27 sites. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_333_interior_step_2026_08_14.py`](../scripts/cube_333_interior_step_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Sites are `{0,1,2}^3`. The center `(1,1,1)` has all six neighbors
in the patch. Occupancy of a neighbor outside the cube is `0`.
`n_μ = (o_{+μ} − o_{-μ})/3`. Locked sites stay. An unread site
forms iff `n ≠ 0`.

Seed the center. Step 1 forms the six face-centers (`k = 1`).
Step 2 forms the twelve edge-centers (`k = 2`). Step 3 forms
the eight corners (`k = 3`). Step 4 is the identity.
Source/tick: `0 → 6 → 18 → 26 → 26`. The empty cube does not form.

This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact occupancy-to-lock update on a displayed 3x3x3 interior."
trace_class: frontier_discovery
target_claim_id: cube_333_interior_step
target_blocker_text: "executable cube has no interior; every site is a 2x2x2 corner"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed 3x3x3 comparator"
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

## Theorem 1 — interior seed

Only `(1,1,1)` locked. Each face-center has `k = 1`. Edge-centers
and corners have `n = 0`.

## Theorem 2 — three cubic shells

Step 1 forms 6. Step 2 forms 12. Step 3 forms 8. Step 4 is
permanence. Source/tick `0,6,18,26,26`.

## Theorem 3 — empty cube is a fixed point

No seed, no formations.

## Theorem 4 — not a TOE

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “step 1 forms a corner” must fail.
2. Predicate “empty cube forms the center” must fail.
3. Predicate “step 4 increments source” must fail.

Identity gates: `occ(site, locks)`, `nvec(site, locks)`, `step(locks)`.

## Honest-auditor / Boundary

27 sites, four snapshots, exact `Q`. Not Newton. This note
authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
