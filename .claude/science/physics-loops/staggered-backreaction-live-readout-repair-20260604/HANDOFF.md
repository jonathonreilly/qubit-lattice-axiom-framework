# Handoff

## What Changed

- Replaced the source note's stale raw two-body residual with the stable
  certified readout `two-body max <1e-12`.
- Updated the runner SAFE READ to print the same bound whenever the computed
  max residual is below the assertion threshold.
- Refreshed the cache.

## Why It Matters

The raw residual is roundoff-level and can move between fresh runs while the
mathematical assertion remains unchanged. The branch makes the displayed live
readout track the load-bearing certified threshold instead of one accidental
floating-point realization.

## Verification

- `PYTHONPATH=scripts python3 scripts/staggered_backreaction_live_capture_packet_check.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/staggered_backreaction_live_capture_packet_check.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/staggered_backreaction_live_capture_packet_check.py`
- `python3 -m py_compile scripts/staggered_backreaction_live_capture_packet_check.py`
- `git diff --check`

## Remaining Blockers

- No continuum backreaction closure.
- No revival of the archived stale table.

## Next Action

Open the review PR, then continue the conditional repair loop.
