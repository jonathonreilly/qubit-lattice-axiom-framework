# Handoff

## Summary

This branch repairs the onsite Weyl-boost audited conditional blocker without
adding axioms or editing audit-ledger data.

## What Changed

- The source note now states `H=iD`, equivalently `D=-iH`.
- The non-load-bearing CPT packet is removed from the restricted source and
  authority surface.
- The runner now checks `D^dagger=-D` and `H^dagger=H` directly.
- The cache is refreshed and reports `15/15` checks.

## Checks

- `PYTHONPATH=scripts python3 scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `if rg -n "D\\s*=\\s*iH|D=iH|CPT_EXACT_REAL_ANTI|CPT|13/13" docs/KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01.md scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py logs/runner-cache/frontier_koide_onsite_weyl_boost_from_bivectors.txt -S; then exit 1; else exit 0; fi`
- `python3 -m py_compile scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `git diff --check`

## Boundaries

This does not repair the global CPT packet. It removes that packet as
non-load-bearing for this onsite result, which is sufficient for the blocker as
written.
