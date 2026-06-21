# Artifact Plan

## Included

- Refresh `logs/runner-cache/frontier_frozen_stars_rigorous.txt` from an empty `ok` stdout body
  to the full generated runner transcript.
- Include deterministic pipeline outputs from `docs/audit/scripts/run_pipeline.sh` so strict
  audit lint is clean on this branch.
- Refresh `docs/audit/data/audit_packet_script_deps.json` and
  `logs/runner-cache/audit_packet_script_deps.txt`.
- Add this branch-local physics-loop packet.
- Open one PR from `physics-loop/audit-unblock-block127-20260620` to `main`.

## Excluded

- No hand edits to audit ledgers, queues, publication matrices, lane registries, active review
  queues, or repo-wide status boards.
- No audit verdict application.
- No source theorem rewrite.
- No direct push to `main`.

## Verification Plan

- Check the refreshed runner cache with `scripts/precompute_audit_runners.py --check-only`.
- Run the audit packet dependency helper.
- Run strict audit lint.
- Run `git diff --check`.

All planned checks passed after pipeline regeneration.
