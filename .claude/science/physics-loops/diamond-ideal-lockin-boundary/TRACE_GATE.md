# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: diamond_sensor_prediction_note, diamond_sensor_protocol_note, diamond_nv_phase_ramp_signal_budget_note, diamond_phase_ramp_bridge_card_note
target_blocker_text: "missing NV ideal-detector forward-model bridge theorem mapping a driven source trajectory to lock-in observables X, Y, phi and the spatial phase profile"
source_of_blocker_text: source_notes_and_audit_selector
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Reviewer/auditor can re-check the Diamond rows with the detector-map blocker removed; source-to-NV coupling and absolute calibration remain open."
```

If the new theorem is true, it closes the detector-map bridge only. It does not
close a physical source-to-NV coupling, an absolute amplitude budget, a lab
noise model, or any audit verdict.
