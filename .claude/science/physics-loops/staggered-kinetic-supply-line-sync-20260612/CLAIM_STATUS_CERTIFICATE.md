# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
conditional_surface_status: conditional-support_if_FSB-K_and_supplier_audits_pass
hypothetical_axiom_status: null
admitted_observation_status: null
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
proposal_allowed: false
proposal_allowed_reason: "The supplier chain is not fully audit-ratified and the P-FLUX selector remains conditional on FSB-K."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The PR title and body may use `bounded-support` or
`conditional-support`. They must not use bare retained or claim that the
consumer rows are already unbounded on the current surface.
