## Summary

Adds a source-side partial bridge for the audited-failed `three_family_card_note` row.

This PR does not restore the archived 9/9 card. It packages the current live runner-backed evidence for the specific missing Family 3 distance-alpha slot: `alpha=-1.150`, `R^2=0.971`, `5/5 toward`, with exact zero/neutral controls and sign/tail gates passing.

## Artifacts

- `docs/THREE_FAMILY_CARD_MISSING_DISTANCE_LIVE_BRIDGE_NOTE_2026-06-18.md`
- `scripts/three_family_card_missing_distance_live_bridge_2026_06_18.py`
- `logs/runner-cache/three_family_card_missing_distance_live_bridge_2026_06_18.txt`
- pointer in `docs/DISTANCE_LAW_PRESERVING_THIRD_FAMILY_NOTE.md`
- pointer in `archive_unlanded/family-card-incomplete-artifacts-2026-04-30/THREE_FAMILY_CARD_NOTE.md`
- branch-local handoff pack under `.claude/science/physics-loops/three-family-card-missing-distance-20260618/`

## Boundary

This PR does not edit audit ledgers, queues, publication matrices, lane registries, active review queues, or repo-wide status boards. It does not claim all-nine-property recomputation, three-family equality, geometry independence, a holdout-family check, or retained status for the card.

## Verification

- `python3 scripts/family_card_archive_firewall_2026_06_16.py` -> `PASS: family-card archive firewall holds`
- `python3 scripts/three_family_card_missing_distance_live_bridge_2026_06_18.py` -> `SUMMARY: THREE FAMILY CARD MISSING DISTANCE LIVE BRIDGE PASS=51 FAIL=0`
- `python3 -m py_compile scripts/three_family_card_missing_distance_live_bridge_2026_06_18.py`
