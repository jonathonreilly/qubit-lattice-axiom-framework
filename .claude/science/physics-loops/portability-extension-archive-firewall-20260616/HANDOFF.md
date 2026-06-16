# Handoff

## What Changed

The archived portability extension README and notes now carry explicit
2026-06-16 archive-firewall language. The old retained-positive portable card
and package verdicts are demoted to historical/retracted taxonomy/worklist
status.

## What This Does Not Do

- It does not audit the rows.
- It does not recompute portability checks.
- It does not repair the sign, distance-law, three-family-card, or
  complex-action dependencies.
- It does not propose retained status.

## Verification

```bash
python3 scripts/portability_extension_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/portability_extension_archive_firewall_2026_06_16.py
git diff --check
python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only
python3 scripts/vocab_lint.py --report-only --report-path /tmp/portability-extension-vocab-report.json archive_unlanded/portability-stale-extension-wrappers-2026-04-30/README.md archive_unlanded/portability-stale-extension-wrappers-2026-04-30/PORTABLE_CARD_EXTENSION_NOTE.md archive_unlanded/portability-stale-extension-wrappers-2026-04-30/PORTABLE_PACKAGE_EXTENSION_NOTE.md
```

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4105
