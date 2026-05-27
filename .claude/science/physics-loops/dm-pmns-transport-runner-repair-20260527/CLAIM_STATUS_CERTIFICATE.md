# Claim Status Certificate

## Target

- `claim_id`: `dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`
- `note_path`: `docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md`
- `claim_type`: `bounded_theorem`
- `criticality`: `high`
- `transitive_descendants`: `246`
- `direct_in_degree`: `7`

## Status Fields

```yaml
actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: eta_obs comparator used by existing bounded witness
proposal_allowed: false
proposal_allowed_reason: "Runner repair only; independent audit must decide bounded versus numerical-match status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Repair

The primary runner now executes without stale transitive helper imports and
prints:

```text
PASS=12  FAIL=0
```

After the deterministic audit pipeline:

```text
audit_status: unaudited
effective_status: unaudited
ready: true
```
