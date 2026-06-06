# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: stable selected location remains conditional on supplied candidates, scores, selection rule, and positive margin
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch proves a supplied-selection interface; it does not derive scores, rules, or a dial setting."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Narrow Claim

Finite rational scores plus a supplied max/tie rule select exactly. A positive
winning gap gives local stability under perturbations below half the gap.

## Excluded Claims

- Record derives the scores.
- Record derives the rule.
- Record forces a generation/Koide dial.
- The branch applies or predicts an audit verdict.
