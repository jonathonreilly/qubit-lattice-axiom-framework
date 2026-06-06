# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a source-scope repair for an audited conditional row. Independent audit remains required."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Certificate Notes

The supported scoped claim is finite algebra:

- `F X F^dag = Z` and the Weyl relation hold.
- The pure-shift `H` is not Fourier-fixed at `r=1/2`.
- The enriched self-dual family `K` is fixed for all tested `g`, so `r` is free.
- The `G` family is Fourier-fixed exactly when `b=c`, with `a` free.
- Trace and traceless Hilbert-Schmidt norm are invariant under Fourier
  conjugation, but that invariance does not select a value.

No effective audit status is set by this branch.
