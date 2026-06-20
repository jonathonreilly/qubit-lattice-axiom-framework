# Claim Status Certificate

```yaml
target_claim_id: post_record_source_measure_trace_normalization_prototype_2026-06-06
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "supplied finite source-measure trace/RN prototype remains exact for supplied finite inputs"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The source note supplies finite measure/RN semantics and does not derive a physical measure, Born law, selector, or dial."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Before

- `claim_type`: `positive_theorem`
- `claim_type_author_hint_raw`: `methodology / positive theorem`
- `claim_type_provenance`: `audited`
- `audit_status`: `audited_clean`
- `effective_status`: `retained`
- source/trace row-count text: `15 + 6 = 21`

## After

- `claim_type`: `bounded_theorem`
- `claim_type_author_hint_raw`: `bounded_theorem`
- `claim_type_provenance`: `author_hint`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `effective_status_reason`: `awaiting_audit`
- `queue_reason`: `unaudited`
- `ready`: `true`
- source/trace row-count text: `16 + 10 = 26`

The prior audits are preserved in `previous_audits`; they are not treated as
live verdicts for the changed note and runner hashes.

