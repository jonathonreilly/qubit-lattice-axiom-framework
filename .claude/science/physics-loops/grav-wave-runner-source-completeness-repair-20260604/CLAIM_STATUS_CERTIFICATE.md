actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch repairs a runner artifact issue for an audited conditional row; independent audit/review must decide any effective status movement."
audit_required_before_effective_retained: true
bare_retained_allowed: false

dependency_classes:
  new_axioms: none
  new_observational_admissions: none
  fitted_selectors: none
  literature_imports: none
  framework_native_computation: "finite toy-lattice runner source-completeness witness and bounded sensitivity checks"

checks:
  runner_status: "exit_code=0"
  source_witness: "Test B/Test C PASS"
  cache_fresh: true
  py_compile: true
  diff_check: true
