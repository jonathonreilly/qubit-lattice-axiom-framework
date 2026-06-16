# Handoff

## What Changed

The archived h=0.125 failure-diagnosis packet now states that it is historical
failed diagnostic material. The old root-cause/SNR/P_det sections are marked
historical and retracted, and the README points readers to the current
executable h=0.125 audit lane.

## What This Does Not Do

- It does not audit the row.
- It does not add a repair runner for the old negative table.
- It does not alter the current h=0.125 executable positive/bounded lane.
- It does not propose retained status.

## Verification

```bash
python3 scripts/h0125_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/h0125_archive_firewall_2026_06_16.py
git diff --check
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only
python3 scripts/vocab_lint.py --report-only --report-path /tmp/h0125-vocab-report.json archive_unlanded/h0125-unverifiable-numerical-diagnostics-2026-04-30/README.md archive_unlanded/h0125-unverifiable-numerical-diagnostics-2026-04-30/H0125_FAILURE_DERIVATION.md
```

PR: TBD
