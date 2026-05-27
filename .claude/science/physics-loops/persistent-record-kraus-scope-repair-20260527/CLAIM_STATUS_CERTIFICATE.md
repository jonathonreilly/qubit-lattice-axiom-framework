# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is finite isometry algebra, not a retained persistent-record bridge proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Runner

`PYTHONPATH=scripts python3 scripts/persistent_record_kraus_instrument_certificate.py`

Result: certificate pass with isometry and Kraus resolution errors below
`1e-15`.
