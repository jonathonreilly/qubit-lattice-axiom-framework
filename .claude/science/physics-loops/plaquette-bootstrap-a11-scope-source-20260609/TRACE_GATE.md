# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: plaquette_bootstrap_framework_integration_note_2026-05-03
target_blocker_text: "scope_too_broad: narrow BB1 to Wilson-loop observables proven to lie in A11's A_+^(2) surface and include the mixed-cumulant authority, or remove the beta=6 estimate from the audited theorem scope."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem_scope_repair
next_trace_action: "Review the A11 A_+^(2) narrowing and mixed-cumulant source linkage, then re-audit the same row without treating the beta=6 diagnostic as theorem scope."
```

This PR targets the exact named blocker by doing both repairs:

- BB1 is now restricted to Wilson-loop observables already proven to lie in A11's retained-bounded 2-step `A_+^(2)` surface.
- The mixed-cumulant onset theorem is linked as retained source authority.
- The beta=6 arithmetic is demoted to formal diagnostic/comparator, not a bound or closure.
