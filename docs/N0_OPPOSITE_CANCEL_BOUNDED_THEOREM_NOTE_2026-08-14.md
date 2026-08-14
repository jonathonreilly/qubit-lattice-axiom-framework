---
claim_id: n0_opposite_cancel_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On a displayed 3-site line with both ends locked, the unread center has n_x=0 and the occupancy step is the identity: opposite neighbors cancel. Of 64 six-neighbor occupancy cells, exactly 8 have k=0. Formation is a difference, not an OR of occupied neighbors. Not Newton, not axiom text."
upstream_dependencies:
  - minimal_axioms
runner: scripts/n0_opposite_cancel_2026_08_14.py
---

# `n = 0` Never Forms

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact `Q` cancellation on a 3-site line and a 64-cell
census. Not axiom text.
**Audit-status authority:** independent audit lane only. This note authors no audit verdict and predicts none.
**Primary runner:**
[`scripts/n0_opposite_cancel_2026_08_14.py`](../scripts/n0_opposite_cancel_2026_08_14.py)
**Parents:** [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Sites `L, C, R` on a line. `n_x = (o_right − o_left)/3`. Locked
sites stay. An unread site forms iff `n_x ≠ 0`.

If both ends are locked, `C` has `n_x = 0` and the step is the
identity. Occupied neighbors that sit opposite cancel. Among the
64 six-bit occupancy cells, exactly 8 have `k = 0`.

Formation is a difference, not an OR of occupied neighbors.

This is still a comparator, not a TOE.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact n=0 cancellation on a 3-site line and the 8 zero cells."
trace_class: frontier_discovery
target_claim_id: n0_opposite_cancel
target_blocker_text: "any occupied neighbor forms"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit"
conditional_surface_status: "exact for the displayed 3-site line and 64-cell census"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Those sentences do not name opposite cancellation.

## Theorem 1 — both ends locked

`(+, ·, +)` and `(−, ·, −)` have `n_x(C) = 0`. The step does not
form `C`.

## Theorem 2 — eight zero cells

Of 64 six-bit cells, exactly 8 have `k = 0`.

## Theorem 3 — empty and one-end still behave

Empty line is a fixed point. One locked end still forms the
center.

## Theorem 4 — not a TOE

Qubit remains `M_2(C)`. QCD is unused.

## Mutations

1. Predicate “both ends form the center” must fail.
2. Predicate “zero-cell count is 0” must fail.
3. Predicate “empty line forms the center” must fail.

Identity gates: `nx(site, locks)`, `step(locks)`, `zero_count()`.

## Honest-auditor / Boundary

Three sites and a 64-cell census, exact `Q`. This note authors no
audit verdict.

## What This Does Not Claim

- No unique member. No axiom text. No Newton.
- Qubit remains `M_2(C)`.
