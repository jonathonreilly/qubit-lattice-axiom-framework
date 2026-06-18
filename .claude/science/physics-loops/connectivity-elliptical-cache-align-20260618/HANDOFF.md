# Handoff

This branch repairs the source-side blocker on
`connectivity_family_v2_elliptical_duplicate_note` without editing audit
results.

The note now cites the current primary runner and SHA-pinned cache, records the
45-row inventory, retires the stale `drift = 0.02, seed = 0` targeted row, and
states the current `25/45` duplicate-boundary result.

Verification run:
- `python3 scripts/cached_runner_output.py --check-only scripts/CONNECTIVITY_FAMILY_V2_ELLIPTICAL_SWEEP.py`
- `git diff --check`

Do not land this branch directly. Reviewer extraction and independent audit
decide whether the row moves.
