# Handoff

## What Changed

- Added `source_completeness_witness()` to `scripts/frontier_grav_wave_post_newtonian.py`.
- The witness verifies that Test B and Test C have executable bodies, quantitative table markers, append/return paths, and no omitted-body markers.
- Updated `docs/GRAVITATIONAL_WAVE_PROBE_NOTE.md` to name the witness.
- Refreshed `logs/runner-cache/frontier_grav_wave_post_newtonian.txt`.

## Checks

- `PYTHONPATH=scripts python3 scripts/frontier_grav_wave_post_newtonian.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_grav_wave_post_newtonian.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_grav_wave_post_newtonian.py`
- `python3 -m py_compile scripts/frontier_grav_wave_post_newtonian.py`
- `git diff --check`

## Review Target

Please inspect this as a direct repair of the restricted-packet source-completeness blocker. It does not claim a physical gravitational-wave or post-Newtonian bridge.
