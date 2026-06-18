# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: bounded-support with exact-prefactor sensitivity retired
hypothetical_axiom_status: null
admitted_observation_status: empirical small `m_nu` remains load-bearing
proposal_allowed: false
proposal_allowed_reason: "The empirical small-neutrino-mass comparator and parametric thermal/cosmology scalings remain open imports."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Status Rationale

The branch removes exact-prefactor sensitivity from the I12 thermal comparator
by checking a hostile prefactor grid up to `E = 1e4`. It does not derive small
neutrino mass, the collision operator, or radiation cosmology from framework
primitives.
