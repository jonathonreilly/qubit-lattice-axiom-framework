actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "The spectrum note remains conditional on the named staggered-only transfer-positivity sector and on SC3 nondegeneracy for a positive gap."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This PR closes a quoted normalization blocker but does not run independent audit and does not claim effective retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false

checks:
  - "python3 -m py_compile scripts/axiom_first_spectrum_condition_check.py scripts/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.py"
  - "python3 scripts/axiom_first_spectrum_condition_check.py"
  - "python3 scripts/precompute_audit_runners.py --runners scripts/axiom_first_spectrum_condition_check.py --force --allow-non-main --push-mode none"
  - "python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.py --check-only --allow-non-main --push-mode none"
