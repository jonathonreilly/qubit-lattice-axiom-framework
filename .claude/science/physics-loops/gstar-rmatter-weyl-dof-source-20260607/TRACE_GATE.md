# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: sm_gstar_r_matter_residual_reduction_bounded_note_2026-05-29
target_blocker_text: "P_Weyl_thermal_dof / R-WEYL-THERMAL carried as a bounded thermal-counting premise"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem_and_runner_certificate
next_trace_action: "Reviewer should inspect stacked dependency on the Dirac/Weyl dof PR; independent audit decides any effective status change."
```

If the upstream Dirac/Weyl dof packet is retained, this block gives the
R-MATTER row a cleaner source for the Weyl factor `2`. It does not close I12,
R-RH, R-SPIN, or the neutral-singlet convention.
