## Summary

Adds a source-side re-audit bridge for the audited-failed `causal_propagating_field_note` row.

The archived row remains failed historical evidence. This PR makes the current live bounded replay target explicit and machine-checks that the live packet has the executable primary runner, cache, manifest runner/cache/JSON, and stale-table guardrails needed for independent re-audit.

## Artifacts

- `docs/CAUSAL_PROPAGATING_FIELD_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md`
- `scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py`
- `logs/runner-cache/causal_propagating_field_live_reaudit_bridge_2026_06_18.txt`
- pointers in `docs/CAUSAL_PROPAGATING_FIELD_LIVE_PACKET_NOTE_2026-06-05.md`
- pointer in `archive_unlanded/causal-field-stale-runners-2026-04-30/CAUSAL_PROPAGATING_FIELD_NOTE.md`
- branch-local handoff pack under `.claude/science/physics-loops/causal-field-live-reaudit-bridge-20260618/`

## Boundary

This PR does not edit audit ledgers, queues, publication matrices, lane registries, active review queues, or repo-wide status boards. It does not restore the archived `0.63 / 0.45` table, claim geometry independence, claim a physical wave speed, or promote the row to retained status.

## Verification

- `python3 scripts/causal_propagating_field.py` -> `ASSERTIONS: PASS`
- `python3 scripts/causal_propagating_field_source_packet_manifest_2026_06_05.py` -> `SUMMARY: CAUSAL PROPAGATING FIELD SOURCE PACKET PASS=30 FAIL=0`
- `python3 scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py` -> `SUMMARY: CAUSAL FIELD LIVE REAUDIT BRIDGE PASS=39 FAIL=0`
- `python3 -m py_compile scripts/causal_propagating_field_live_reaudit_bridge_2026_06_18.py`
- `git diff --check`
- forbidden audit/status path guard passed
