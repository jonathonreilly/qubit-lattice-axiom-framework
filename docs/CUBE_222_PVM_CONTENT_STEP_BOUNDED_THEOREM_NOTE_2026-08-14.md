---
claim_id: cube_222_pvm_content_step_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed 2×2×2 cube, one occupancy step forms unread sites with n≠0. Newly formed sites have k=|3n|^2 and lock-content traces Tr(ρP±)=(3±√k)/6: axis neighbors k=1 traces 2/3 and 1/3, face-diagonals k=2 traces (3±√2)/6, opposite corner k=3 traces (3±√3)/6. Either content still occupies the site, so later menus are unchanged. Source/tick 0→3→6→7→7. Not Born, not a unique member, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cube_222_pvm_content_step_2026_08_14.py
---

# Cube Occupancy Step With PVM Lock Content

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact occupancy update plus exact `Q(√k)` traces on a
displayed `2×2×2` cube. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/cube_222_pvm_content_step_2026_08_14.py`](../scripts/cube_222_pvm_content_step_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Same occupancy step as #6293. When a site forms, `k = |3n|^2`
and the two legal contents have traces `(3 ± √k)/6` from the
#6296 projectors. Seed `(0,0,0)`:

- step 1, axis neighbors, `k = 1`, traces `2/3` and `1/3`;
- step 2, face-diagonals, `k = 2`, traces `(3 ± √2)/6`;
- step 3, `(1,1,1)`, `k = 3`, traces `(3 ± √3)/6`.

Either content occupies the site, so later `n` does not depend
on the draw. Source/tick `0 → 3 → 6 → 7 → 7`.

This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact cube occupancy step coupled to the displayed PVM traces."
trace_class: frontier_discovery
target_claim_id: cube_222_pvm_content_step
target_blocker_text: "cube step is occupancy-only; PVM draw is line-only"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed 2x2x2 comparator"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

Those sentences do not name this coupled update.

## Theorem 1 — occupancy wave

Seed at the origin. Source/tick `0,3,6,7,7`. Empty cube is a
fixed point.

## Theorem 2 — `k` at each shell

Axis sites have `k = 1`. Face-diagonals have `k = 2`. The
opposite corner has `k = 3`.

## Theorem 3 — traces

The displayed PVM traces are `(3 ± √k)/6` at each shell.

## Theorem 4 — occupancy, not content, drives later menus

Either legal content at an axis site still occupies it, so the
face-diagonals still form.

## Theorem 5 — not a TOE

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “axis sites have `k = 2`” must fail.
2. Predicate “empty cube forms” must fail.
3. Predicate “note adopts Born” must fail.

Identity gates: `nvec(site, locks)`, `k_of(n)`, `step(locks)`.

## Honest-auditor / Boundary

Eight sites, three shells, exact `Q` traces. This note authors no
audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- Qubit remains `M_2(C)`.
