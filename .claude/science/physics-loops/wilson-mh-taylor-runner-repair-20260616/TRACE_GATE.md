# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: wilson_m_h_tree_at_extremum_leading_order_in_r_bounded_note_2026-05-08
target_blocker_text: "tighten the perturbative-validity runner check to compare the truncated closed form with the Taylor expansion rather than only testing sqrt-argument positivity"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should re-check the bounded Wilson formula; Higgs-channel readout and Wilson coefficient normalization remain separate blockers."
```

This repair closes the runner-quality part of the blocker. It does not derive
the physical Higgs readout, `N_taste=16`, or a canonical Wilson coefficient.
