# Claim Status Certificate

```yaml
target_claim_id: post_record_persistent_record_production_bridge_prototype_2026-06-06
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "supplied finite bridge prototype remains exact for the supplied inputs"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The source note supplies a finite bridge form and does not derive the production law, overlap kernel, or physical dynamics."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Before

- `claim_type`: `positive_theorem`
- `claim_type_author_hint_raw`: `methodology / positive theorem`
- `claim_type_provenance`: `audited`
- `audit_status`: `audited_clean`
- `effective_status`: `retained`

## After

- `claim_type`: `bounded_theorem`
- `claim_type_author_hint_raw`: `bounded_theorem`
- `claim_type_provenance`: `author_hint`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `effective_status_reason`: `awaiting_audit`
- `queue_reason`: `unaudited`
- `ready`: `true`

The prior audit is preserved in `previous_audits`; it is not treated as a live
verdict for the changed note hash.

