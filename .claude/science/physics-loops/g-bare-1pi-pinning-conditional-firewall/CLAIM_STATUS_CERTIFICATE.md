# Claim Status Certificate

```yaml
claim_id: g_bare_two_ward_same_1pi_pinning_theorem_note_2026-04-19
actual_current_surface_status: bounded-support / conditional-support
conditional_surface_status: off-surface g_bare = 1 under H_unit-residue exhaustion
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_author_hint_after_repair: bounded_theorem
audit_status_authority: independent audit lane only
effective_status_authority: pipeline-derived after audit and dependency closure
proposal_allowed: false
proposal_allowed_reason: >
  The branch does not derive the complete same-projected 1PI H_unit-residue
  exhaustion theorem. It only makes the existing conditional premise explicit
  and blocks downstream unconditional use.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Pipeline result

After `bash docs/audit/scripts/run_pipeline.sh`, the row is:

```yaml
claim_type: bounded_theorem
claim_type_provenance: author_hint
audit_status: unaudited
effective_status: unaudited
runner_path: null
deps:
  - g_bare_two_ward_rep_b_independence_theorem_note_2026-04-19
  - yt_ward_identity_derivation_theorem
open_dependency_paths: []
ready: true
criticality: critical
load_bearing_score: 13.83
transitive_descendants: 909
```

## Audit boundary

This branch queues the row for independent audit. It does not assert that the
row should land as retained, retained bounded, or audited clean.
