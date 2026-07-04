# Claim Status Certificate

actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This block is a current-surface no-go against primitive retirement by axiom absorption, not a retained/proposed-retained claim."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Dependency Classes

- Minimal axioms: approved axiom node.
- Approved primitive notes: approved primitive nodes, read only.
- Tier-A registry: read-only boundary.

## Forbidden Claims

- A primitive is retired.
- A primitive registry is edited.
- A Tier-A admission is retired.
- The Tier-A count changes.
