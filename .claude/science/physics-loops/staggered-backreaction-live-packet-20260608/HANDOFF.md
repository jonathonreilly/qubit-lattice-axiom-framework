# Handoff

## What changed

- Added six live staggered-backreaction replacement notes for stale archived
  rows.
- Added `scripts/staggered_backreaction_live_packet.py`, which asserts the
  current cached facts used by those notes.

## Verification

```bash
python3 scripts/cached_runner_output.py --refresh scripts/staggered_backreaction_live_packet.py
python3 scripts/cached_runner_output.py --check-only scripts/staggered_backreaction_live_packet.py
python3 -m py_compile scripts/staggered_backreaction_live_packet.py
git diff --name-only -- docs/audit
git diff --check
```

Expected wrapper result: `STAGGERED_BACKREACTION_LIVE_PACKET_ASSERTIONS=TRUE`.

## Boundary

No full self-gravity closure is claimed. The residual is still universal
source-to-field scale plus endogenous self-refresh.

