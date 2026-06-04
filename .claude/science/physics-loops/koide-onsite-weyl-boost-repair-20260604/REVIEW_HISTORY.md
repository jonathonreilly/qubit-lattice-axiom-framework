# Review History

Local checks:

- `PYTHONPATH=scripts python3 scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `if rg -n "D\\s*=\\s*iH|D=iH|CPT_EXACT_REAL_ANTI|CPT|13/13" docs/KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01.md scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py logs/runner-cache/frontier_koide_onsite_weyl_boost_from_bivectors.txt -S; then exit 1; else exit 0; fi`
- `python3 -m py_compile scripts/frontier_koide_onsite_weyl_boost_from_bivectors.py`
- `git diff --check`

All passed locally.
