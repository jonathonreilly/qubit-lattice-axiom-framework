# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: charged_lepton_generation_dynamics_partition_gate
target_blocker_text: "Why should charged-lepton/generation dynamics use the two-sector singlet|doublet record partition rather than the three complex character sectors?"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Audit the partition selector, then attack the arrow/measure gate."
```

## Reachability

If this theorem is accepted, the partition half of the dynamics gate is closed
within the supplied generation readout context:

```text
C3 carrier + fixed K/CPT + Record orbit rule
  -> native central partition P0 | P1.
```

It does not close value selection because it does not choose:

- block-count versus dimension weighting;
- Born probability;
- a source/action;
- a time-arrow or dynamics map.
