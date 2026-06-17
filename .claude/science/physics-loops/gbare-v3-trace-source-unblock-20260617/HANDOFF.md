# Handoff

## What Changed

- Updated `docs/STAGGERED_GBARE_TRACE_SURFACE_BRIDGE_NOTE_2026-06-06.md` to
  separate the structural graph-first `V_3` gauge trace surface from physical
  SM-color naming and species-label bijections.
- Updated the paired runner to verify that source split and the finite trace
  algebra:
  - `V_3` Gell-Mann trace gives `N_F = 1/2`;
  - full matter trace `V_3 x C^2` doubles the trace;
  - all six corner-label permutations preserve the trace;
  - physical-color naming and species-label bijection are not required for
    this trace-normalization bridge.
- Refreshed the runner cache.

## Checks

```bash
python3 scripts/frontier_staggered_gbare_trace_surface_bridge_2026_06_06.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_staggered_gbare_trace_surface_bridge_2026_06_06.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_staggered_gbare_trace_surface_bridge_2026_06_06.py
python3 -m py_compile scripts/frontier_staggered_gbare_trace_surface_bridge_2026_06_06.py
git diff --check
```

## Remaining Blocker

This does not prove the per-site-to-gauge `SU(2)` scale-transport bridge. The
remaining hard science is to derive that scale transport from the framework,
or keep `N_F = 1/2` explicitly admitted.
