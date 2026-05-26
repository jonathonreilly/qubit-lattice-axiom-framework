# Claim Status Certificate

```yaml
claim_id: bh_entropy_derived_note
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_author_hint_after_repair: bounded_theorem
audit_status_authority: independent audit lane only
effective_status_authority: pipeline-derived after audit and dependency closure
proposal_allowed: false
proposal_allowed_reason: >
  The block certifies finite cached numerical evidence only. It does not prove
  an infinite-size coefficient, a horizon carrier, or a physical entropy
  theorem.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
runner_path: scripts/frontier_bh_entropy_derived.py
deps: []
helper_runner_paths: []
open_dependency_paths: []
ready: true
criticality: high
transitive_descendants: 71
load_bearing_score: 10.17
```
