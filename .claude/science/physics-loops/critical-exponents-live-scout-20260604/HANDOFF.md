# Handoff

## What Changed

- `scripts/frontier_critical_exponents.py` now labels itself as a bounded
  scout, collects the live rows, and asserts fit/degenerate acceptance
  criteria.
- `logs/runner-cache/frontier_critical_exponents.txt` is refreshed and now
  includes `ASSERTIONS: PASS`.
- `docs/CRITICAL_EXPONENTS_TOPOLOGY_LIVE_SCOUT_NOTE_2026-06-04.md` records the
  current table and narrow safe read.

## Verification

```bash
python3 -m py_compile scripts/frontier_critical_exponents.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_critical_exponents.py --force --push-mode=none --allow-non-main --concurrency 1
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_critical_exponents.py --check-only --push-mode=none --allow-non-main --concurrency 1
git diff --check
```

## Audit Boundary

This PR does not edit `docs/audit/**` and does not assign an effective audit
status. It queues a live bounded scout packet for review.

