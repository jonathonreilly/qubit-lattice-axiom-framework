# Claim Status Certificate

actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
dependency_classes:
  - retained_no_go clock-rate/count boundary
  - retained_bounded Matsubara temporal count
  - retained_bounded two-step RP positivity
  - retained/staggered spatial count packet
open_imports:
  - "Per-record/UV readout selection remains open."
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
proposal_allowed: false
proposal_allowed_reason: "Audit must decide row status; branch only repairs source dependencies."
audit_required_before_effective_retained: true
bare_retained_allowed: false
