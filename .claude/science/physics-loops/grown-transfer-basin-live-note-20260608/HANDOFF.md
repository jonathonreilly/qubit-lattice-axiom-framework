# Handoff

## What changed

- Added `docs/GROWN_TRANSFER_BASIN_NOTE.md` as the canonical live source note.
- Added `scripts/grown_transfer_basin_live_packet.py` and its cache.

## Verification

```bash
python3 scripts/cached_runner_output.py --check-only scripts/GROWN_TRANSFER_BASIN_TARGETED.py
python3 scripts/cached_runner_output.py --check-only scripts/GROWN_TRANSFER_BASIN_SWEEP.py
python3 scripts/cached_runner_output.py --refresh scripts/grown_transfer_basin_live_packet.py
python3 scripts/cached_runner_output.py --check-only scripts/grown_transfer_basin_live_packet.py
python3 -m py_compile scripts/grown_transfer_basin_live_packet.py
git diff --name-only -- docs/audit
git diff --check
```

Expected wrapper result: `GROWN_TRANSFER_BASIN_LIVE_PACKET_ASSERTIONS=TRUE`.

