# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "provide the complete unelided primary/helper runner source in the restricted audit packet"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: tooling
next_trace_action: "After landing, re-audit rows whose blocker cited source elision or truncated helper/source packets."
```

Affected live examples checked on this branch:

- `gravitational_wave_probe_note`
- `meson_gauge_invariant_os_transfer_representation_bounded_note_2026-05-30`
- `staggered_backreaction_live_green_packet_note_2026-05-29`
