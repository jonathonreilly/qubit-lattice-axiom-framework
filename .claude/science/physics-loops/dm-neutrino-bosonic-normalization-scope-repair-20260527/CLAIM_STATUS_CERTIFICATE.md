actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch narrows an audited conditional row to exact finite-block bounded support; it does not certify retained-grade physical normalization."
audit_required_before_effective_retained: true
bare_retained_allowed: false

# Certificate

The branch-local claim is the exact finite-block ratio
`sqrt(Tr(Y^dagger Y) / Tr(Gamma_1^dagger Gamma_1)) = 1/sqrt(2)` where
`Gamma_1 = Y + Y^dagger` is the real-symmetric Hermitian completion.

The branch explicitly does not claim that the non-Hermitian raw bridge `Y`
lies in the X1 real-symmetric source domain, and it does not claim the
physical readout `y_nu/g_weak = 1/sqrt(2)`.
