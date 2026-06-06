# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: stable target-kernel dynamics remains conditional on supplied target prior and reset strength
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch proves supplied-target stability; it does not derive the target prior or dial setting."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Narrow Claim

For any supplied finite target `pi` and supplied `alpha`, the reset kernel is
stationary at `pi`, detailed-balanced, and contracts exactly by `1-alpha`.

## Excluded Claims

- Record derives `pi`.
- Record derives `alpha`.
- Stability chooses the physical target or dial.
- The branch applies or predicts an audit verdict.
