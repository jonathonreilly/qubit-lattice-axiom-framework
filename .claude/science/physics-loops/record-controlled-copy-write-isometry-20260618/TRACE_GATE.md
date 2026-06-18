# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: record_formation_to_kraus_isometry_bridge_2026-06-06
target_blocker_text: "missing_bridge_theorem: derive the ideal pointer-label record-write isometry from the finite controlled-copy/fresh-fragment dynamics, or narrow the ledger scope to the already-supplied projective write premise."
source_of_blocker_text: audit_ledger
reachability_to_target: closes_source_side_blocker
artifact_role: theorem_and_runner_certificate
next_trace_action: "Reviewer should inspect the source-side theorem and runner, then independent audit can decide whether the audited_conditional row moves."
```

## Why The Trace Is Direct

The conditional audit says the target row closes within the finite projective write model, but does not derive the blank-record/ideal-write premise from the controlled-copy/fresh-fragment dynamics.

This branch proves that in the explicit controlled-copy model:

```text
U_cc(pi/4)(|psi>|0>) = P_0|psi>|eta_0> + P_1|psi>|eta_1>,
<eta_0|eta_1> = 0.
```

After fixed record-basis calibration, this is exactly the projective `W` used by the target bridge.

## Boundary

The trace reaches only the explicit finite controlled-copy/fresh-fragment model. It does not derive arbitrary persistent dynamics, the quantum-Darwinism bridge, physical couplings, Born probabilities, or downstream selectors.
