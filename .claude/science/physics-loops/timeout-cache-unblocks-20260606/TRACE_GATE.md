# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id:
  - kernel_vs_gravity_note
  - shapiro_five_family_portability_note
target_blocker_text: "runner cache status was timeout under the default 120 second budget"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "Independent audit should read or rerun the fresh SHA-pinned caches and decide the row statuses."
```

## Reachability

The blocker is executable rather than conceptual.  Both runners complete just
above the old default timeout and now declare their runtime budget in source.
The fresh caches pin the new SHAs and report `status: ok`.
