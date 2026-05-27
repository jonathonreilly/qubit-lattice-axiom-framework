# Claim Status Certificate

## Current-Surface Status

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This PR queues repaired bounded-theorem rows for independent audit; it does not propose retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Rows

### KMS Majorant

- Claim id: `kms_fermionic_brydges_majorant_external_narrow_theorem_note_2026-05-11`
- Source: `docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`
- Runner: `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
- Claim type after pipeline: `bounded_theorem`
- Audit status after pipeline: `unaudited`
- Effective status after pipeline: `unaudited`
- Queue readiness: ready
- Binding repair: finite framework majorant/comparison lemma proved directly.

### Born Rule Bridge

- Claim id: `born_rule_from_gleason_busch_derivation_note_2026-05-20`
- Source: `docs/BORN_RULE_FROM_GLEASON_BUSCH_DERIVATION_NOTE_2026-05-20.md`
- Runner: `scripts/born_rule_framework_bridge_check.py`
- Claim type after pipeline: `bounded_theorem`
- Audit status after pipeline: `unaudited`
- Effective status after pipeline: `unaudited`
- Queue readiness: ready
- Binding repair: raw standard-math imports replaced by retained-grade
  framework dependencies plus a finite algebraic bridge runner.

## Status Firewall

This block does not claim `retained`, `proposed_retained`, or
`proposed_promoted`. The repaired rows are deliberately left for the auditor.
