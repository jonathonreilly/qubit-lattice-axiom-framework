# Claim Status Certificate

## What Changed

Updated the source packet:

- `docs/GROWN_TRANSFER_BASIN_TARGETED_REPAIR_NOTE_2026-06-04.md`
- `scripts/GROWN_TRANSFER_BASIN_SWEEP.py`
- `scripts/GROWN_TRANSFER_BASIN_TARGETED.py`
- `scripts/grown_transfer_basin_live_packet.py`

Refreshed caches:

- `logs/runner-cache/GROWN_TRANSFER_BASIN_SWEEP.txt`
- `logs/runner-cache/GROWN_TRANSFER_BASIN_TARGETED.txt`
- `logs/runner-cache/grown_transfer_basin_live_packet.txt`

## Scientific Boundary

Closed source-side repair:

- The finite packet now declares `PW = 10`, matching the retained helper
  geometry actually used by `grow()`.
- The complex-action predicate now requires a strict away sign at
  `gamma = 0.5`: every seed must be away and the row mean must be
  negative.
- Both targeted and full 3x3 caches were regenerated from live compute.

Still outside scope:

- family-wide generated-geometry transfer;
- graph-ladder theorem;
- old archived note unarchive/status change;
- audit verdict or ledger retagging.

## Verification

Commands run:

```bash
PYTHONPATH=scripts python3 scripts/GROWN_TRANSFER_BASIN_TARGETED.py
PYTHONPATH=scripts python3 scripts/GROWN_TRANSFER_BASIN_SWEEP.py
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/GROWN_TRANSFER_BASIN_TARGETED.py,scripts/GROWN_TRANSFER_BASIN_SWEEP.py --force --concurrency=1 --push-mode=none
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/grown_transfer_basin_live_packet.py --force --push-mode=none
PYTHONPATH=scripts python3 scripts/grown_transfer_basin_live_packet.py
python3 -m py_compile scripts/GROWN_TRANSFER_BASIN_SWEEP.py scripts/GROWN_TRANSFER_BASIN_TARGETED.py scripts/grown_transfer_basin_live_packet.py
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/GROWN_TRANSFER_BASIN_TARGETED.py,scripts/GROWN_TRANSFER_BASIN_SWEEP.py,scripts/grown_transfer_basin_live_packet.py --check-only --push-mode=none
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Results:

- Targeted replay: `nearby rows surviving both observables: 4/4`
- Full sweep: `signed-source survivors: 9/9`, `complex-action survivors: 9/9`, `same-row survivors: 9/9`
- Each reported row has `gamma=0.5` away count `(0, 3)` and negative mean `g05`
- Live packet: `PASS=5 FAIL=0`
- Cache freshness: all relevant caches fresh
- Strict lint: OK, no errors; expected non-retained row hash-drift notice
- Diff whitespace check: OK
