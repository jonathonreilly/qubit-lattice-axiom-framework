# Trace Gate

```yaml
trace_class: upstream_support
target_claim_id: stable_post_record_dial_location
target_blocker_text: "The dial should be a stable setting, not a forced endpoint."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "Use the stable-location certificate while keeping physical dial selection open."
```

If true, this artifact supports dial work by authorizing stable-location wording
and forbidding forced-selection wording.
