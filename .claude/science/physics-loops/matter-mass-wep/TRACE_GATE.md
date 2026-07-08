# Trace Gate — matter-mass-wep

## block01 — mass observable

```yaml
trace_class: direct_blocker_closure
target_claim_id: ep_record_stiffness_conditional_template_2026_06_07
target_blocker_text: "A separate theorem identifying an inertial rest-gap readout for physical matter."
source_of_blocker_text: audit_ledger  # 2026-06-17 no-go "What remains open"
reachability_to_target: partially_closes  # R2 readout half; R1 narrowed to I-DYN chain, not closed
artifact_role: theorem
next_trace_action: "block02 supplies the inertial-response half of R2"
```

## block02 — inertial closure (drafted, pending execution)

```yaml
trace_class: direct_blocker_closure
target_claim_id: matter_inertial_closure_2026_04_07
target_blocker_text: "the slope is dispersion-dependent, not mass-dependent"
source_of_blocker_text: handoff  # MATTER_INERTIAL_CLOSURE_NOTE.md decisive finding
reachability_to_target: closes  # the mechanism, on the realized surface, within the stated window
artifact_role: theorem
next_trace_action: "block03 extends to composites; block04 consumes M_I for the source side"
```

## block03 / block04 — to be drafted at block start.
block04's expected trace on the negative fork: negative_route_pruning +
diagnosis note; on the positive fork: direct_blocker_closure of EP-S3b.
