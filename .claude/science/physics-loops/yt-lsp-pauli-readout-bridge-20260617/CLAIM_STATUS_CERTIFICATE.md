actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: >
  The PR repairs the exact source-readout carrier edge only. It does not close
  source/action physical authority, O_H, LSZ, response rows, matching/running,
  m_t, or y_t.
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: reviewer_owned_not_run

# Dependency Classes

- Minimal axioms: framework premise authority.
- LSP canonical `K_r=P_r`: retained-bounded in current ledger, checked by runner.
- Y_T source-action support packet: retained-bounded in current ledger, checked
  by runner.

No observed values, fitted selectors, literature values, or new axioms are
load-bearing.
