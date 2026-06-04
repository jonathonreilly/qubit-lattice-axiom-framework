actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch repairs the executable R4 runner issue but does not close R1-R3 authority coverage."
audit_required_before_effective_retained: true
bare_retained_allowed: false

dependency_classes:
  new_axioms: none
  new_observational_admissions: none
  fitted_selectors: none
  literature_imports: none
  framework_native_computation: "C3 central-projector and invariant-metric-family algebra"

checks:
  runner_scorecard: "PASS=4 FAIL=0"
  cache_fresh: true
  py_compile: true
  diff_check: true
