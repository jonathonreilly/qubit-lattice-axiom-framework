# Handoff

## What Changed

- `scripts/GROWN_TRANSFER_BASIN_SWEEP.py` now declares a 3600-second audit
  timeout, exposes shared row predicates, and reports same-row survivors.
- `scripts/GROWN_TRANSFER_BASIN_TARGETED.py` now imports those predicates and
  no longer uses the stale `abs(action_gamma0) < 1e-12` criterion.
- `logs/runner-cache/GROWN_TRANSFER_BASIN_SWEEP.txt` is fresh and reports
  `same-row survivors: 9/9`.
- `logs/runner-cache/GROWN_TRANSFER_BASIN_TARGETED.txt` is fresh and reports
  `nearby rows surviving both observables: 4/4`.
- `docs/GROWN_TRANSFER_BASIN_TARGETED_REPAIR_NOTE_2026-06-04.md` packages the
  result as bounded support for re-audit.

## Verification

```bash
python3 -m py_compile scripts/GROWN_TRANSFER_BASIN_SWEEP.py scripts/GROWN_TRANSFER_BASIN_TARGETED.py scripts/GROWN_TRANSFER_BASIN_DIAG.py
python3 scripts/precompute_audit_runners.py --runners scripts/GROWN_TRANSFER_BASIN_TARGETED.py,scripts/GROWN_TRANSFER_BASIN_SWEEP.py --force --push-mode=none --allow-non-main --concurrency 2
```

## Audit Boundary

This PR does not edit `docs/audit/**` and does not claim an effective audit
status. It only queues a repaired live packet for review.

