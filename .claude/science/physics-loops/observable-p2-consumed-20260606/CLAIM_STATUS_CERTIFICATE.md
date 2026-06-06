actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "Global/off-sector P2 remains out of scope; AC_phi_lambda remains separate where downstream consumers need determinant readout identification."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This PR proposes a direct blocker repair but does not run independent audit and does not claim effective retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false

checks:
  - "python3 -m py_compile scripts/frontier_hierarchy_observable_principle_from_axiom.py scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py"
  - "python3 scripts/frontier_hierarchy_observable_principle_from_axiom.py"
  - "python3 scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py"
  - "python3 scripts/precompute_audit_runners.py --runners scripts/frontier_hierarchy_observable_principle_from_axiom.py,scripts/audit_companion_observable_principle_positive_source_cone_p2_elimination_2026_06_06.py --force --allow-non-main --push-mode none"
