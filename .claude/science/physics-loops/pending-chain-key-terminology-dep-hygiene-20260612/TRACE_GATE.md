# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "chain_waiting_on:key_terminology"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: tooling
next_trace_action: "Reviewer can land the source hygiene change and let the audit/ledger pipeline recompute effective dependencies."
```

If the pipeline recomputes graph dependencies from source, these rows should no
longer have a `key_terminology` graph edge. Any remaining bounds then come from
their scientific dependencies, not a glossary link.
