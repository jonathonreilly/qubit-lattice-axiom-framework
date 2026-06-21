actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Block20 is an exact support/boundary split, not a proposed endpoint theorem."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: "not run: user instruction says not to audit; branch-local self-review only"

## Certificate Notes

Block20 proves a safe consumer boundary for existing exact support surfaces:

- time-channel factor-rigidity statements are readout-independent;
- `delta_E=0` carrier consumers are `rho_E`-blind;
- E-center consumers remain conditional on the missing readout/source rule.

The PR must not claim endpoint selection, readout primitive selection, or
promotion of the parent row.

