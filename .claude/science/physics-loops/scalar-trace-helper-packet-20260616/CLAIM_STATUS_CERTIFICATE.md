actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: "The no-go remains scoped to the imported scalar-functional/probe-family surface unless audit accepts the helper packet as sufficient."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The branch repairs source/cache evidence for helper imports but does not independently derive the helper constructions from framework axioms."
audit_required_before_effective_retained: true
bare_retained_allowed: false

Checked evidence:

- primary runner uses static imports for the three helper modules;
- helper packet runner reports `SUMMARY: PASS=33 FAIL=0 TOTAL=33`;
- primary no-go runner cache reports `PASS=6 FAIL=0 TOTAL=6`;
- each helper cache is present, SHA-fresh, exits with status `ok`, and has
  passing output.
