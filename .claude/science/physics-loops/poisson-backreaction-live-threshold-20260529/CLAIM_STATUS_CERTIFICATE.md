# Claim Status Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The packet is queued for independent audit, not ratified."
audit_required_before_effective_retained: true
bare_retained_allowed: false
review_loop_disposition: external_reviewer_pending
```

## Dependency Classes

- New dependencies: none.
- Open dependency paths in generated row: none.

## Verification

- `python3 -m py_compile scripts/backreaction_poisson_live_threshold_check.py`
- `python3 scripts/backreaction_poisson_live_threshold_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

Pipeline state: `poisson_backreaction_live_threshold_packet_note_2026-05-29` is `unaudited`, `ready=true`, rank 907.
