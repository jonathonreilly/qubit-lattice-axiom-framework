# Handoff

## What Changed

The archived testable-ranking notes and README are now explicit historical /
diagnostic brainstorming records. The old current-retained ranking labels,
retained-connection labels, top-non-diamond verdict, and bottom-line current
ranking are demoted.

## What This Does Not Do

- It does not audit the rows.
- It does not regenerate a current testables map from the audit ledger.
- It does not propose retained status.

## Verification

```bash
python3 scripts/testable_ranking_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/testable_ranking_archive_firewall_2026_06_16.py
git diff --check
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only
python3 scripts/vocab_lint.py --report-only --report-path /tmp/testable-ranking-vocab-report.json archive_unlanded/testable-ranking-stale-wrappers-2026-04-30/README.md archive_unlanded/testable-ranking-stale-wrappers-2026-04-30/TESTABLE_PREDICTIONS_MAP_NOTE.md archive_unlanded/testable-ranking-stale-wrappers-2026-04-30/MOONSHOT_OTHER_TESTABLES_NOTE.md
```

PR: TBD
