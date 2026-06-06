actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
proposal_allowed: false
proposal_allowed_reason: "The source-action term remains open; this branch fixes only stale control numbers."
audit_required_before_effective_retained: true
bare_retained_allowed: false

Certified repair:

- Displayed `Born I3` controls now match the runner/cache value `+5.381e-43`.
- Displayed max norm drift now matches the runner/cache value `3.331e-15`.
- Runner remains `SUMMARY: PASS=11 FAIL=0` and cache is fresh.

Residual blockers:

- `S_int = - chi_eta M_phys <rho,Phi>` is still not derived from retained structure.
- No physical signed-gravity claim is made.
