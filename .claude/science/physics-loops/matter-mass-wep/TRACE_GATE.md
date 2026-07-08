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

## block03 — composite motion (executed)

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "no note on center-of-mass motion, comoving frames, Galilean invariance, or common acceleration of a bound pair exists"
source_of_blocker_text: user_goal  # motion sweep 2026-07-08; owner's original two-masses question
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "block04 consumes C1 (rest-energy sources cannot give exact finite-spacing composite WEP) as the comparator leg of the reduction/no-go"
```

## block04 — WEP source-side reduction (executed)

```yaml
trace_class: direct_blocker_closure
target_claim_id: ep_record_stiffness_weak_field_interface_2026_06_16
target_blocker_text: "identifying the gravitational source coefficient with the same m as the inertial rest gap | still supplied shared-coupling template data"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "owner fork-interpretation answer selects: scaling-window reading -> T4 is the closure shape; exact reading -> write-up-then-stop protocol with the diagnosis already recorded in NO_GO_DISCIPLINE_CHECKLIST.md"
```

## block05 — mass-energy equivalence static-comparator no-go (executed)

```yaml
trace_class: direct_blocker_closure
target_claim_id: wep_source_reduction_window_residual_2026_07_08
target_blocker_text: "derive mass-energy equivalence for composites in the scaling window"
source_of_blocker_text: handoff  # block04 reduction, owner direction A
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "future campaign: composite mass-energy equivalence on the gauged/interacting transfer surface (the record-preservation-forced covariant-hopping class)"
```
