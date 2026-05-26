# Handoff -- DM PMNS Projector Raw-Interface Repair

## Summary

This loop repairs the DM/PMNS projector interface by taking only the raw
Hermitian-pair algebra to re-audit. Physical carrier authority, N1 column
selection, and eta diagnostics are outside this row.

## Files

- `docs/DM_LEPTOGENESIS_PMNS_PROJECTOR_INTERFACE_NOTE_2026-04-16.md`
- `scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`
- `outputs/dm_pmns_projector_raw_interface_repair_2026-05-25.txt`
- `.claude/science/physics-loops/dm-pmns-projector-raw-interface-repair/`

## Verification

- `docs/audit/scripts/run_pipeline.sh`
- `PYTHONPATH=scripts python3 scripts/frontier_dm_leptogenesis_pmns_projector_interface.py`

Runner result: `PASS=27 FAIL=0`.

## Audit state

- audit status: `unaudited`
- effective status: `unaudited`
- deps: `[]`
- helper runner paths: `[]`
- queue position: `1`
- ready: `true`

## Next action

Open the PR for review. The independent audit lane must decide retention.
