# Assumptions And Imports

## Allowed Inputs

- The ten existing post-record stack notes, runners, and SHA-pinned runner caches.
- Read-only hash check of `docs/audit/data/audit_ledger.json`.

## Retired Import

- The target runner no longer relies only on hard-coded `False` booleans for the firewall. It scans the stack packet for forbidden `=TRUE` flags and checks that the audit ledger hash is unchanged.
- The runner now verifies every stack layer has a source note, runner source, and fresh cache.

## Still Open

- Independent audit is required before any ledger status movement.
- Source notes are packet authorities and not audit verdicts.
