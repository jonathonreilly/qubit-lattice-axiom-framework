# Handoff

Branch: `physics-loop/gbare-derivation-ledger-boundary-20260617`

Target: `g_bare_derivation_note`

What changed:

- Section G of `frontier_g_bare_derivation.py` now reports visible repair rows with their current audit/effective status.
- If the repair rows are not retained, the runner prints `[BOUNDARY]` and keeps the parent gate open instead of printing `[FAIL]`.
- The note documents this status-reporting behavior.
- The cache was refreshed and now has no failure markers.

Checks run:

- `python3 -m py_compile scripts/frontier_g_bare_derivation.py`
- `PYTHONPATH=scripts python3 scripts/frontier_g_bare_derivation.py`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py --refresh scripts/frontier_g_bare_derivation.py --timeout-sec 120`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/frontier_g_bare_derivation.py`
- `rg -n 'FAIL=|\[FAIL\]|FAILED:' logs/runner-cache/frontier_g_bare_derivation.txt`
- `git diff --check`

Remaining blocker:

The parent `g_bare = 1` row remains open until the two repair rows are independently retained with closed dependencies.
