# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
proposal_allowed: false
proposal_allowed_reason: "This branch is an auditable runner packet for an unaudited no-go synthesis; independent audit must ratify any retained_no_go status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: reviewer_owned_not_run
```

The branch does not use `retained` or `promoted` as an author-side status.
It supplies replayable evidence for a no-go row and leaves the verdict to the
review/audit lane.
