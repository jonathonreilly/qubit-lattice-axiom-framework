# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "four audited runner rows had missing SHA-pinned cache files"
source_of_blocker_text: audit_runner_cache_scan
reachability_to_target: closes
artifact_role: tooling
next_trace_action: "review and extract the cache files so the audit runner has fresh output for these rows"
```

This is an audit-cache unblock only.
