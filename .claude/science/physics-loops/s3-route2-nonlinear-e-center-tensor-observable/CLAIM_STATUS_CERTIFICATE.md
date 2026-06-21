actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "A channel-selecting nonlinear observable could reopen the route."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Same-scalar nonlinear carrier dressings force q_E/q_T=1 and cannot derive the target covariance 9/4."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: pass

# Certificate

Block75 is not a retained-status proposal. It is a current-bank no-go for
same-scalar nonlinear dressings of the current rank-1 Route-2 carrier.

Verification:

- New runner: `TOTAL: PASS=53, FAIL=0`.
- Focused checks: bilinear carrier, rank-1 factorization, Schur covariance
  no-go, exact readout map, parent S3/time verifier, constructed support
  candidate, and support center-excess law all pass.

No audit verdict is applied. Independent audit remains required before any
repo-wide status change.
