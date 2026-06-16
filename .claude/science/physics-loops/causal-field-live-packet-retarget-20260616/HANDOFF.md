# Handoff

## What changed

This branch retargets current causal-field context references from the archived
failed `CAUSAL_PROPAGATING_FIELD_NOTE.md` packet to the live finite-replay
`CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md` packet. It also
updates renderer scripts so regenerated notes do not recreate the stale link.

## What did not change

- No audit ledger or queue files were edited.
- No effective-status table was edited.
- No new axiom or physics premise was introduced.
- No physical field-speed or retarded-carrier theorem is claimed.

## Verification

Run:

```bash
python3 scripts/causal_field_live_packet_reference_firewall_2026_06_16.py
python3 -m py_compile scripts/causal_field_live_packet_reference_firewall_2026_06_16.py scripts/causal_distance_tail_probe.py scripts/causal_impact_parameter_probe.py scripts/shapiro_phase_lag_probe.py scripts/shapiro_complex_interaction.py
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only
git diff --check
```

## Reviewer notes

The intended source movement is narrow: the old archived `0.45` table becomes
historical caution only, and live downstream causal/Shapiro/diamond references
use the existing live finite-replay packet.
