# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - flavor_native_action_predicts_q1_2026-06-02
  - flavor_record_readout_form_not_weight_2026-06-02
  - flavor_hw_clifford_does_not_constrain_r_2026-06-02
  - flavor_zdet_fermionic_statistics_admission_2026-06-04
target_blocker_text: "The rows leave action, Record, HW/Fourier, and determinant-statistics gates looking independent."
source_of_blocker_text: source_notes
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Reviewer/auditor can re-audit these rows as route-local bounded support around the already explicit occupancy/slot-degree atom."
```

The block does not solve the atom. It removes duplicated open-gate provenance
around it.
