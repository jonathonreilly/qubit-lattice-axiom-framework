# Claim Status Certificate

target_claim_id: `yt_ward_ratio_tadpole_cancellation_narrow_theorem_note_2026-05-17`

- actual_current_surface_status: bounded-support
- trace_class: direct_blocker_closure
- reachability_to_target: partially_closes
- conditional_surface_status: exact algebra lemma conditional on D1 and D2
- hypothetical_axiom_status: null
- admitted_observation_status: null
- proposal_allowed: false
- proposal_allowed_reason: D1 and D2 are assumptions; no retained bridge for common tadpole readout is supplied.
- audit_required_before_effective_retained: true
- bare_retained_allowed: false

## Audit Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`, the row has:

```json
{
  "audit_status": "unaudited",
  "effective_status": "unaudited",
  "claim_type": "bounded_theorem",
  "deps": [],
  "open_dependency_paths": []
}
```
