# Claim Status Certificate

```yaml
actual_current_surface_status: proposed_promoted
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true
proposal_allowed_reason: "The PR repairs the exact normalization blocker and queues the row for audit; it does not assert effective retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

After `run_pipeline.sh`, the target row is `unaudited`, `ready=true`, and `effective_status=unaudited`; this is expected because the source hash changed and no audit verdict was applied.
