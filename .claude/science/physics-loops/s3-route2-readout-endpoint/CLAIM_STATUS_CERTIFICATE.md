actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "If a two-reciprocal-unit-frame-analysis-leg primitive is accepted, the granted T-side algebra gives rho_E=21/4."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The block still requires an unproved theorem selecting two independent reciprocal analysis legs and a source/readout split."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: local_pass_external_review_pending

# Claim Status Certificate

Block17 is conditional support plus a no-go boundary for the finite-frame/Riesz
route.

Allowed branch-local status language:

- `conditional-support`
- `upstream_support`
- `finite-frame/Riesz boundary`
- `two-leg primitive remains open`

Disallowed language:

- endpoint-closing language;
- unique theta-to-slice theorem;
- a claim that `rho_E=21/4` is derived;
- a claim that canonical Riesz reconstruction supplies the target;
- any bare retained/promoted status wording.

Independent audit remains required before any repo-wide status surface can use
this block. This physics-loop PR does not run or apply an audit verdict.
