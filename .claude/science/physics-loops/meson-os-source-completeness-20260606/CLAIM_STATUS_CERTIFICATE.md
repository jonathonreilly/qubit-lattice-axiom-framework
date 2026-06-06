# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is an artifact-completeness repair for an audited conditional row; independent audit owns any row movement."
audit_required_before_effective_status_change: true
bare_retained_allowed: false
```

## Boundary

The PR may say it proposes a source-completeness repair. It must not claim that
the row has already moved in the audit ledger.
