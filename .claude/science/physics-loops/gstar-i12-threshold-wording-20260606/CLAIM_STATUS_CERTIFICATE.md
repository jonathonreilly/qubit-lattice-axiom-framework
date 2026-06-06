# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: empirical-small-neutrino-mass-load-bearing
proposal_allowed: false
proposal_allowed_reason: "The source blocker is repaired, but small m_nu remains an admitted empirical observation and independent audit remains required."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Certificate Notes

This block is not a retained-status proposal. It is a bounded-support source
repair for a conditional audit row.

The repaired claim is narrower:

- Given the admitted empirical small neutrino mass, the light-Dirac branch has
  `y_nu << y_thr` and right-handed neutrinos do not thermalize.
- The heavy-Majorana branch does not include light right-handed neutrino degrees
  of freedom at the census epoch.
- The only threshold route to `g_* = 112` is `y_nu >= y_thr`; at the most
  lenient threshold this implies `m_nu >= 2 keV`, and the O(1) steelman implies
  about 174 GeV.

Independent audit is required before any effective status change.
