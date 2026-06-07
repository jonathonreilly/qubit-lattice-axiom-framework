# Review History

Local verification:

- `python3 scripts/signed_gravity_aps_locked_source_action_proposal.py`
  -> `SUMMARY: PASS=16 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/signed_gravity_aps_locked_source_action_proposal.py`
  -> cache refreshed
- `python3 scripts/cached_runner_output.py scripts/signed_gravity_aps_locked_source_action_proposal.py --check-only`
  -> fresh
- `git diff --check`
  -> clean
