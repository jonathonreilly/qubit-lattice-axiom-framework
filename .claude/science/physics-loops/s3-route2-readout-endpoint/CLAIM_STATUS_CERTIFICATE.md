# Claim Status Certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "this block prunes a bypass route; it does not certify selected P_R"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Status

Block28 is an exact negative boundary for the scalar-bypass route. It does not
change repo-wide authority status and does not close the S3/Route-2 endpoint.

## Dependency Classes

- rho_E-free support: native projector/support grammars,
  scalar-comparison bridge, STRC/RPSR reduced amplitude.
- endpoint-readout-sensitive support: tensor endpoint slope/denominator
  routes and Route-2 endpoint ratio-chain routes.
- selected-map route: still conditional on a supplied `P_R`.

## Review Disposition

No audit verdict was applied in this branch. The branch carries self-contained
runners and outputs for the later reviewer pass.
