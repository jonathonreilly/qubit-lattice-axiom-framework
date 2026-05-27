# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: diagnostic_interpolation_against_ETA_OBS_only
proposal_allowed: true
proposal_allowed_reason: "The branch queues a bounded interval witness for fresh audit after repairing the runner import blocker; it does not claim retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Current generated ledger state after `docs/audit/scripts/run_pipeline.sh`:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `claim_type`: `bounded_theorem`
- `ready`: `true`
- helper runner surface: `scripts/dm_leptogenesis_exact_common.py`

This is not a direct ledger retag and not an audit verdict.
