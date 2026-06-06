# Claim Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: physical stochastic dynamics remains conditional on a supplied kernel
hypothetical_axiom_status: null
admitted_observation_status: null
dependency_classes:
  - finite post-record history/count algebra
  - supplied initial law
  - supplied finite transition kernel
open_imports:
  - derivation of kernel
  - Markov/stationarity assumptions
  - clock/rate bridge
  - Born/instrument bridge
proposal_allowed: false
proposal_allowed_reason: "This is a conditional supplied-kernel interface, not a derivation of the kernel or a status promotion proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Plain-Language Status

Exact-support for finite-history probability/count consequences after a
transition kernel is supplied. No support for deriving the kernel from Record
alone.

