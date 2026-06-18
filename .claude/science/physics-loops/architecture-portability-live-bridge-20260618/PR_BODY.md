## Summary

Adds a source-side live re-audit bridge for the audited-failed `work_history.repo.review_feedback.architecture_portability_audit_2026-04-11` row.

The archived work-history packet remains failed historical evidence. This PR points the repair target at the current live bounded sweep note, primary runner/cache, and archive firewall, with explicit boundaries around source-mass scaling, attraction sign, measured Born `I_3`, and excluded stronger claims.

## Artifacts

- `docs/ARCHITECTURE_PORTABILITY_LIVE_REAUDIT_BRIDGE_NOTE_2026-06-18.md`
- `scripts/architecture_portability_live_reaudit_bridge_2026_06_18.py`
- `logs/runner-cache/architecture_portability_live_reaudit_bridge_2026_06_18.txt`
- pointer in `docs/ARCHITECTURE_PORTABILITY_SWEEP_NOTE.md`
- pointer in `archive_unlanded/work-history-unverifiable-portability-2026-04-30/ARCHITECTURE_PORTABILITY_AUDIT_2026-04-11.md`
- branch-local handoff pack under `.claude/science/physics-loops/architecture-portability-live-bridge-20260618/`

## Boundary

This PR does not edit audit ledgers, queues, publication matrices, lane registries, active review queues, or repo-wide status boards. It does not restore the archived packet as evidence and does not claim full Newton closure, both-masses closure, cross-architecture distance-law closure, random-geometric 3D distance-law closure, or Wilson Born measurement.

## Verification

- `python3 scripts/frontier_architecture_portability_sweep.py` -> `OVERALL: PASS -- bounded source-mass portability companion established`
- `python3 scripts/archive_architecture_portability_firewall_2026_06_16.py` -> `PASS: architecture portability archived-audit evidence firewall holds`
- `python3 scripts/architecture_portability_live_reaudit_bridge_2026_06_18.py` -> `SUMMARY: ARCHITECTURE PORTABILITY LIVE REAUDIT BRIDGE PASS=51 FAIL=0`
- `python3 -m py_compile scripts/architecture_portability_live_reaudit_bridge_2026_06_18.py`
- `git diff --check`
