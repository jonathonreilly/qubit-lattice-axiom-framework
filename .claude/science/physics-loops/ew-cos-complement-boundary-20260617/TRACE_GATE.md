# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: ew_lattice_cos_sq_theta_w_complement_bridge_theorem_note_2026-04-26
target_blocker_text: "Runner/cache reports nonzero exit and failure markers because unaudited/meta/decorated dependency statuses and stale YT_EW literal checks are treated as hard failures."
source_of_blocker_text: audit_queue_scan
reachability_to_target: partially_closes
artifact_role: demotion
next_trace_action: "Reviewer should extract the bounded-support repair, then independent audit can evaluate the row without stale retained overclaim or false hard runner failure."
```

If true, this PR does not make the claim retained. It makes the audit input
honest and runnable: exact arithmetic is preserved, open dependencies are
visible, and the cache reports `status: ok`.
