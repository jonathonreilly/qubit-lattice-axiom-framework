# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a source-scope repair and finite runner certificate; independent audit remains required."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Certificate Notes

The supported scoped claim is:

- For finite `A_Lambda ~= M_d(C)`, self-adjoint `H` gives
  `D_H=exp(-H)/tau(exp(-H))`.
- `D_H` is positive and `tau(D_H)=1`.
- `omega_H(O)=tau(D_H O)` is positive on positive `O`.
- The normalized-trace formula equals the usual density-matrix formula.

No effective audit status is set by this branch.
