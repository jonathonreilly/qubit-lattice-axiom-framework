# Kraus-Choi Native Reroute Handoff

## Summary

This branch updates the retained Kraus-Choi parent note and its deps-changed
hygiene companion so finite-region Kraus/Choi is no longer described as a bare
standard theorem import. The source text now routes through
`KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md`
and its proof runner, with Kraus 1971 / Choi 1975 / Nielsen-Chuang cited in
parallel.

## Scope

- No audit files are edited.
- No ledger retag or status promotion is claimed.
- Infinite-volume arbitrary channel representation remains out of scope.
- Record dynamics/CPTP identification remains a downstream lane.

## Verification

- `python3 scripts/kraus_choi_normalization_convention_check_2026_06_05.py` -> `TOTAL: PASS=16 FAIL=0`
- `python3 scripts/audit_companion_kraus_choi_representation_deps_changed_hygiene_2026_06_04.py` -> `SUMMARY: PASS=35 FAIL=0`
- `python3 scripts/audit_companion_kraus_choi_normalization_reconciled_2026_06_05.py` -> `TOTAL: 26 PASS / 0 FAIL`
- `git diff --check` -> clean
- `git diff --name-only -- docs/audit` -> empty
- targeted stale import phrase `rg` in the edited docs -> empty
