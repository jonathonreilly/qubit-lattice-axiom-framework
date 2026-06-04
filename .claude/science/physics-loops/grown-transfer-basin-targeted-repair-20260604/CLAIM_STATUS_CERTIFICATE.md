actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch repairs the runner/cache support surface but does not run or record an independent audit verdict."
audit_required_before_effective_retained: true
bare_retained_allowed: false

No new axiom is introduced. The branch-local result is a finite bounded runner
packet: corrected predicates, current SHA-pinned caches, and a live note with
explicit audit boundaries.

