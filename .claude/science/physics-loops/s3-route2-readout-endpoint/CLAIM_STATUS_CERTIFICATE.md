# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "this block prunes the W2-only endpoint route; W1 remains open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Status

Block30 is an exact negative boundary for conflating W1 and W2. It does not
change repo-wide authority status and does not close the S3/Route-2 endpoint.

## Dependency Classes

- W1: algebraic source-domain bridge from `su3_R_conn_8_9` to
  `route2_center_TE_minus_8_9`.
- W2: physical connected-trace selector `kappa_EW=0`.
- Endpoint algebra: exact once W1 supplies `c_TE=-8/9`.

## Review Disposition

No audit verdict was applied in this branch. The branch carries a
self-contained runner and output for the later reviewer pass.
