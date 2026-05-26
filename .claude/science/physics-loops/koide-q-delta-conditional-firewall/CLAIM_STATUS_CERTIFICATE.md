# Claim Status Certificate

```yaml
claim_id: koide_q_delta_linking_relation_theorem_note_2026-04-20
actual_current_surface_status: conditional-support
conditional_surface_status: "I1 and P imply delta = Q/d"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_author_hint_after_repair: bounded_theorem
audit_status_authority: independent audit lane only
effective_status_authority: pipeline-derived after audit and dependency closure
proposal_allowed: false
proposal_allowed_reason: >
  The branch does not derive I1, does not derive P, and does not provide a
  retained/audited bridge from rho_delta = 2/d^2 to selected-line CP1
  Berry holonomy in radians.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

After `bash docs/audit/scripts/run_pipeline.sh`, the row is:

```yaml
claim_type: bounded_theorem
claim_type_provenance: author_hint
audit_status: unaudited
effective_status: unaudited
runner_path: scripts/frontier_koide_q_delta_linking_relation.py
deps: []
open_dependency_paths: []
ready: true
criticality: high
load_bearing_score: 12.288
transitive_descendants: 220
```
