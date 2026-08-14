---
claim_id: two_cube_plus_x_ray_support_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the two-cube dual graph with nodes A, B, exterior and edges F* (A—B), F_B (B—ext), F_A (A—ext), there are exactly two simple A→ext paths. The unique path that is monotone in +x uses {F*, F_B}. That is the support of the displayed tree gauge. Not axiom text, not Newton."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_plus_x_ray_support_2026_08_14.py
---

# Plus-`x` Ray Selects `{F*, F_B}`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact path count on a three-node dual graph.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_plus_x_ray_support_2026_08_14.py`](../scripts/two_cube_plus_x_ray_support_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Dual nodes: cube `A`, cube `B`, exterior. Edges: `F*` joins `A` to
`B` at `x=1`, `F_B` joins `B` to exterior at `x=2`, `F_A` joins
`A` to exterior at `x=0`.

Simple paths from `A` to exterior: `(F*)` then `(F_B)`, or `(F_A)`
alone. The first is monotone in `+x`. The second steps to smaller
`x`. So a displayed `+x` orientation selects `{F*, F_B}` uniquely.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact uniqueness of the monotone +x A-to-exterior path."
trace_class: frontier_discovery
target_claim_id: two_cube_plus_x_ray_support
target_blocker_text: "gaugefix support {F*,F_B} is a free choice"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed two-cube dual"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Those sentences do not name this dual path.

## Theorem 1 — two paths

Exactly two simple `A → ext` paths exist.

## Theorem 2 — unique `+x` path

Only `(F*, F_B)` is monotone in `+x`.

## Theorem 3 — display

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “there is a third simple path” must fail.
2. Predicate “`F_A` is `+x`-monotone” must fail.

Identity gates: `paths()`, `monotone_plus_x(path)`, `selected()`.

## Honest-auditor / Boundary

Three nodes, three edges. This note authors no audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
