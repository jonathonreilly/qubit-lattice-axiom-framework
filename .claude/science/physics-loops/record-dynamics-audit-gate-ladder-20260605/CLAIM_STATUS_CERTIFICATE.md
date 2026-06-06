claim_id: record_dynamics_audit_gate_ladder_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "branch-local dynamics gate classifier; no audit verdict or physical rate closure"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block supplies a classifier only; produced records, physical implementation, rates, cost, and dial selection remain open per target lane."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

## Dependency Classes

- Record dynamics stack artifacts.
- Finite set/classifier logic.

## Open Imports

- Target-lane produced records.
- Physical implementation, bath/cost, and clock/rate.
- Any dial selection.

## Wording Firewall

Allowed: bounded support, branch-local classifier, gate ladder, open residuals.

Not allowed: audit verdict applied, physical rate derived, thermodynamic cost
derived, produced records derived globally, dial fixed or forced.
