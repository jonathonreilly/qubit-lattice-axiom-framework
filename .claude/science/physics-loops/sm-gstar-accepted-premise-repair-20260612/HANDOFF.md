# Handoff

## What Changed

PR #3787 has been narrowed to the still-current I12 `nu_R`
thermal-exclusion conditional. The prior Higgs-sector accepted-premise edit is
not carried forward because latest main already changed that lane.

The source note now records:

- P-MNU: admitted empirical small neutrino mass;
- P-THERM: accepted thermalization comparator;
- branch-independent exclusion across the retained Dirac/seesaw no-go;
- no first-principles derivation claim for small `m_nu`.

## Validation

- I12 runner: `RESULT: PASS=68 FAIL=0`
- Explicit runner cache check: one runner considered; fresh.
- `git diff --cached --check`: clean.
- Exact conflict-marker scan: clean.
- Generated audit/status/publication diff check: empty.

## Reviewer Notes

This is source-side audit-unlock work only. It does not edit ledger verdicts or
generated effective-status/audit files. Independent audit should decide whether
the explicit accepted-input boundary is sufficient for bounded support or if the
row remains conditional.
