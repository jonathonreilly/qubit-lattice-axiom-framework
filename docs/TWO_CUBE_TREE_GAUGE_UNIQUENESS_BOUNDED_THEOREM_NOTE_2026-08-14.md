---
claim_id: two_cube_tree_gauge_uniqueness_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On two unit cubes with g_A=φ(F*) and g_B=−φ(F*)+φ(F_B), the source-complete fluxes supported only on {F*,F_B} are unique: φ(F*)=ρ(A), φ(F_B)=ρ(A)+ρ(B). Allowing a third face F_A (A’s x=0) produces a 1-parameter family. ρ is the occupancy count on each cube. Not axiom text, not Newton."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_cube_tree_gauge_uniqueness_2026_08_14.py
---

# Unique Tree-Gauge Flux On Two Cubes

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact linear uniqueness of a 2-face flux given `g=ρ`.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/two_cube_tree_gauge_uniqueness_2026_08_14.py`](../scripts/two_cube_tree_gauge_uniqueness_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Two cubes share `F*`. Incidence is `g_A = φ(F*)` and
`g_B = −φ(F*) + φ(F_B)`. Source `ρ` is the occupancy count on
each cube’s eight vertices. Shared vertices count in both.

If flux is allowed only on `{F*, F_B}`, then `g=ρ` has exactly
one solution: `φ(F*)=ρ(A)`, `φ(F_B)=ρ(A)+ρ(B)`.

If `A`’s outer face `F_A` may also carry flux, then
`g_A = φ(F*) + φ(F_A)` and the solution is a 1-parameter family.

On the corner seed, the unique 2-face flux is `(1,1)`. After the
three in-patch neighbors form, it is `(4,5)`.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact uniqueness of 2-face source-complete flux."
trace_class: frontier_discovery
target_claim_id: two_cube_tree_gauge_uniqueness
target_blocker_text: "recgrav gauge is one of many fluxes"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for two cubes and the displayed incidence"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Those sentences do not name this gauge.

## Theorem 1 — unique 2-face solution

`φ(F*)=ρ(A)` and `φ(F_B)=ρ(A)+ρ(B)` is the only pair with
`g=ρ` and support in `{F*, F_B}`.

## Theorem 2 — third face is not unique

With free `φ(F_A)`, `φ(F*)=ρ(A)−t`, `φ(F_A)=t`,
`φ(F_B)=ρ(B)+ρ(A)−t` solves `g=ρ` for every integer `t`.

## Theorem 3 — seed and one occupancy step

Seed occupancy `{(0,0,0)}` has unique 2-face flux `(1,1)`.
After forming `(1,0,0)`, `(0,1,0)`, `(0,0,1)`, unique 2-face
flux is `(4,5)`.

## Theorem 4 — display

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “a second 2-face solution exists on the seed” must fail.
2. Predicate “the 3-face family is a single point” must fail.
3. Predicate “note adopts Newton” must fail.

Identity gates: `rho(locks)`, `unique_two_face(rho)`, `three_face_family(rho, t)`, `occ_step(locks)`.

## Honest-auditor / Boundary

Two equations, two or three faces, exact `Z`. This note authors no
audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No inverse-square law.
- Qubit remains `M_2(C)`.
- This is still a comparator, not a TOE.
