---
claim_id: l0_formation_pvm_draw_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the displayed 3-site line, an unread site with n≠0 has k=|3n|^2 and lock-content projectors P± of H=aσx+bσy+cσz. The two legal contents have traces Tr(ρP±)=(3±√k)/6. At the seed, C has k=1 and traces 2/3 and 1/3. Both contents leave occupancy 1, so R still forms on the next step. This replaces a=1 sign(n) by the displayed PVM. Not Born, not a unique member, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/l0_formation_pvm_draw_2026_08_14.py
---

# Formation Content Is A Displayed PVM Draw

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q` traces for lock content on the displayed 3-site
line. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/l0_formation_pvm_draw_2026_08_14.py`](../scripts/l0_formation_pvm_draw_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Keep the #6290 occupancy step. Change only how a new lock chooses
content. At an unread site with `n ≠ 0` write `k = |3n|^2` and
`H = a σ_x + b σ_y + c σ_z`. The two legal contents are the
rank-1 projectors `P_± = (√k I ± H)/(2√k)`. With
`ρ = (I + H/3)/2` one has `Tr(ρ P_±) = (3 ± √k)/6`.

On the seed `(−, ·, ·)` the center has `n_x = −1/3`, `k = 1`,
traces `2/3` and `1/3`. Either content occupies the center, so
the right site still forms on step 2. Later `n` is occupancy-only.

This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Q traces replace a=1 sign(n) by the displayed PVM on the 3-site line."
trace_class: frontier_discovery
target_claim_id: l0_formation_pvm_draw
target_blocker_text: "intstep locks sign(n) with a=1; measure is disconnected"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit; cube+PVM joint update remains open"
conditional_surface_status: "exact for the displayed 3-site line comparator"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

> When present, a record locks exactly one admissible local possibility.

Those sentences do not name this draw.

## Theorem 1 — seed kernel

Seed `(−, ·, ·)`. Center has `n_x = −1/3`, `k = 1`, `H = −σ_x`.

## Theorem 2 — traces

`Tr(ρ P_+) = 2/3` and `Tr(ρ P_-) = 1/3`. Sum is `1`.

## Theorem 3 — occupancy, not content, drives the next menu

Both legal contents occupy the center. Step 2 forms the right site
in either case.

## Theorem 4 — not a TOE

Quoted Qubit, Admissibility, and Record do not name the draw.
Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “traces are `1/2, 1/2`” must fail.
2. Predicate “a `+` content at `C` blocks `R`” must fail.
3. Predicate “empty seed forms `C`” must fail.

Identity gates: `nx(site, locks)`, `pvm_probs(a,b,c)`, `step(locks)`.

## Honest-auditor / Boundary

One line, `k=1` traces, occupancy-blind recoil. This note authors no
audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Born derivation.
- Qubit remains `M_2(C)`.
