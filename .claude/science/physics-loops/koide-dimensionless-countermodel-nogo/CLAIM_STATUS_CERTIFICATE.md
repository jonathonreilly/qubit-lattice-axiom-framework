# Claim Status Certificate

```yaml
claim_id: koide_dimensionless_note_2026-04-24
actual_current_surface_status: no-go
conditional_surface_status: exact-support-if-source/readout-selection-added
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_author_hint_after_repair: no_go
audit_status_authority: independent audit lane only
effective_status_authority: pipeline-derived after audit and dependency closure
proposal_allowed: false
proposal_allowed_reason: >
  The block proves an exact no-go/countermodel boundary, not a positive
  closure proposal.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_type: no_go
audit_status: unaudited
effective_status: unaudited
runner_path: scripts/frontier_koide_dimensionless_objection_closure_review.py
deps: []
helper_runner_paths: []
open_dependency_paths: []
ready: true
criticality: high
transitive_descendants: 73
load_bearing_score: 11.709
```
