# Handoff

## Summary

This branch repairs `g_bare_derivation_note` as a bounded parent audit unlock.
The science chain is unchanged; the runner no longer fails because generated
audit ledger rows have changed state.

## Changes

- `docs/G_BARE_DERIVATION_NOTE.md`: source claim hint changed to
  `bounded_theorem`; expected runner summary updated to require zero failures.
- `scripts/frontier_g_bare_derivation.py`: Section G now checks source packet
  boundaries instead of audit/effective status fields.
- `logs/runner-cache/frontier_g_bare_derivation.txt`: refreshed.

## Verification

```bash
python3 scripts/frontier_g_bare_derivation.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_g_bare_derivation.py --check-only
```

Expected summary: `EXACT PASS=51 FAIL=0`, `BOUNDED PASS=15 FAIL=0`.

## Audit Boundary

This PR does not audit the row and does not edit `docs/audit/*`,
publication effective-status files, or `docs/repo/FRONT_DOOR_STATUS.md`.
