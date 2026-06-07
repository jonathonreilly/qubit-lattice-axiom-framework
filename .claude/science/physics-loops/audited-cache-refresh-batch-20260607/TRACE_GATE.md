# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "audited runner cache headers were stale for 18 rows not covered by open PRs"
source_of_blocker_text: audit_runner_cache_scan
reachability_to_target: closes
artifact_role: tooling
next_trace_action: "review and extract the cache refresh; auditor can then read fresh cache outputs for these audited rows"
```

This closes cache freshness blockers only. It does not modify scientific
claims, dependency status, or audit verdicts.
