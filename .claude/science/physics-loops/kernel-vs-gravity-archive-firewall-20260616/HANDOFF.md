# Handoff

## What Changed

The archived kernel-vs-gravity note now explicitly says it is historical /
diagnostic and retired as evidence. The old result and claim-boundary headings
are retracted, and the safe boundary distinguishes local per-link attenuation
from total detector-escape suppression.

## What Did Not Change

- No audit ledger or queue files were edited.
- No effective-status table was edited.
- No complex-action theorem is claimed.
- No new physics premise was introduced.

## PR

Review PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4100

## Verification

Run:

```bash
python3 scripts/kernel_vs_gravity_archive_firewall_2026_06_16.py
python3 -m py_compile scripts/kernel_vs_gravity_archive_firewall_2026_06_16.py
git diff --check
```
