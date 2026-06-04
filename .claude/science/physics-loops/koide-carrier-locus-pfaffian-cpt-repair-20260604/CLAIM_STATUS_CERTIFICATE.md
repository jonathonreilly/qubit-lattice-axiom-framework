actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch repairs a named audited conditional blocker; independent audit/review must decide any effective status movement."
audit_required_before_effective_retained: true
bare_retained_allowed: false

dependency_classes:
  new_axioms: none
  new_observational_admissions: none
  fitted_selectors: none
  literature_imports: none
  framework_native_computation: "2x2 real antisymmetric Pfaffian sign algebra and existing finite carrier-locus checks"

checks:
  cpt_runner: "PASS=35 FAIL=0"
  carrier_locus_runner: "13/13 checks passed"
  caches_fresh: true
  py_compile: true
  diff_check: true
