# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: interaction_asymmetry_delta_occupation_curvature_two_body_structure_theorem_note_2026-06-06
target_blocker_text: "scope_too_broad: add and verify the symbolic effective-coupling formula with the eps+U>0 or weak-coupling hypothesis, then restate the sign law within that regime."
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: theorem_scope_repair
next_trace_action: "Independent audit should check that the sign law is now restricted to eps>0 and eps+U>0 and that the runner verifies the formula and outside-regime counterexample."
```

The branch gives the missing effective-coupling formula:

```text
K_off = t^2 * (1/eps - 1/(eps + U))
      = t^2 * U / (eps * (eps + U)).
```

The sign law is now only claimed in the no-resonance / weak-pair regime
`eps > 0`, `eps + U > 0`. The runner also verifies an `eps+U<0` example where
the old unconditional sign law fails.
