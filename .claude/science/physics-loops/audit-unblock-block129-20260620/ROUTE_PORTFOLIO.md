# Route Portfolio

| route | status | reason |
|---|---|---|
| Extend runtime-breakage guard to include `missing_runner_file` inventory rows | selected | Distinct from block126/127/128; proves stale path blockers resolve to fresh cache evidence without editing verdicts. |
| Refresh full-ledger stale runner caches | skipped | Covered by PR #4498 for the earlier batch; re-scan first if reopening this route. |
| Repair null runner accounting in packet dependency map | skipped | Covered by PR #4497. |
| Refresh empty long-run cache transcripts | skipped | Covered by PR #4496 and PR #4497. |
| Re-run audit or apply retained hash decisions | rejected | User explicitly asked for unblocker PRs only, not audits. |
