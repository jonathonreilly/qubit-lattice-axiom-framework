# Handoff

## What changed

- Added `scripts/frontier_teleportation_acceptance_suite_note_sync_check.py`.
- Updated `docs/TELEPORTATION_ACCEPTANCE_SUITE_NOTE.md` to cite the sync guard.
- The guard executes the live default and strict-lane `--list-probes` surfaces,
  parses the note's strict-lane inventory table, and asserts exact equality.

## Verification

```bash
python3 scripts/cached_runner_output.py --refresh scripts/frontier_teleportation_acceptance_suite_note_sync_check.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_teleportation_acceptance_suite_note_sync_check.py
python3 -m py_compile scripts/frontier_teleportation_acceptance_suite.py scripts/frontier_teleportation_acceptance_suite_note_sync_check.py
git diff --name-only -- docs/audit
git diff --check
```

Expected sync-guard result: `PASS=6 FAIL=0`.

## Boundaries

- No audit files were edited.
- No physical teleportation closure is claimed.
- This is a meta/harness source-sync repair only.

