# Claim Status Certificate

```yaml
claim_id: causal_field_portability_note
actual_current_surface_status: bounded-support
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_author_hint_after_repair: bounded_theorem
audit_status_authority: independent audit lane only
effective_status_authority: pipeline-derived after audit and dependency closure
proposal_allowed: false
proposal_allowed_reason: >
  The block certifies a bounded cache diagnostic only. It does not derive the
  carrier operators or a portability criterion and does not satisfy retained-
  proposal requirements.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Pipeline Result

After `bash docs/audit/scripts/run_pipeline.sh`:

```yaml
claim_type: bounded_theorem
audit_status: unaudited
effective_status: unaudited
runner_path: scripts/causal_field_portability_probe.py
deps: []
helper_runner_paths: []
open_dependency_paths: []
ready: true
criticality: high
transitive_descendants: 84
load_bearing_score: 9.909
```

The branch proposes re-audit of the bounded cache certificate. It does not
assert retained status.
