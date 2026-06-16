# Handoff

## What Changed

The archived unified-basin freeze packet now says that it is historical
diagnostic material only. The old frozen claim is retracted in the body, and
the note records that a future repair needs either one unified runner over the
shared neighborhood or a split into separate retained/failed components.

## What This Does Not Do

- It does not audit the row.
- It does not add a unified runner.
- It does not promote the signed-source salvage metadata.
- It does not propose retained status.

## Verification

```bash
python3 scripts/unified_basin_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/unified_basin_archive_firewall_2026_06_16.py
git diff --check
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only
python3 scripts/vocab_lint.py --report-only --report-path /tmp/unified-basin-vocab-report.json archive_unlanded/unified-basin-signed-source-salvage-2026-04-30/UNIFIED_BASIN_FREEZE_NOTE.md
```

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4108
