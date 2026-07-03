actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "bounded three-row nonlabel grown basin at seed 0, drift 0.2"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch repairs the recompute artifact and table precision for re-audit; audit owns effective status movement."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Dependency Classes

- Live recompute artifact: SHA-fresh cache checked by primary verifier.
- Frozen log: regression row-gate check only.

## Open Imports

- No unbounded basin/family theorem.

## Firewalls

- No `docs/audit/**` edits.
- No local audit status update.
- No branch-local bare status promotion.
