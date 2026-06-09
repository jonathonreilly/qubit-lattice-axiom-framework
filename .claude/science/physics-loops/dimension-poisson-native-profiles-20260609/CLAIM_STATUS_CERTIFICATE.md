actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The branch removes one textbook-import dependency but leaves the lower-bound packet bounded to the finite runner and its analytic test-family choice."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Claim Boundary

The branch proves the runner's radial profiles under the d-dimensional radial
Poisson operator away from the source and verifies the derivative signs used by
the finite-k sign bridge. It does not assert a unique framework derivation of
the parent dimension-selection surface.

## Import Accounting

- Retired: textbook/standard Poisson Green asymptotics as the authority for
  `f_1=r`, `f_2=log(r)`, and `f_d=r^(2-d)`.
- Preserved as bounded: the finite runner chooses this analytic profile family
  as its test surface.
- Preserved as parallel references: Maradudin and standard mechanics texts.
