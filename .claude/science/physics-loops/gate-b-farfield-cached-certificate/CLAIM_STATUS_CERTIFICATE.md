# Claim Status Certificate

```yaml
claim_id: gate_b_farfield_note
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_author_hint_after_repair: bounded_theorem
audit_status_authority: independent audit lane only
effective_status_authority: pipeline-derived after audit and dependency closure
proposal_allowed: false
proposal_allowed_reason: >
  The block certifies only a bounded cached numerical harness result. It does
  not prove the physical Gate B bridge and does not satisfy retained-proposal
  requirements.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
runner_path: scripts/gate_b_farfield_harness.py
deps: []
open_dependency_paths: []
ready: true
criticality: critical
transitive_descendants: 122
load_bearing_score: 14.443
```

The branch proposes re-audit of the bounded certificate. It does not assert a
retained or promoted status.
