# Review History

- Ran `python3 scripts/dm_thermal_average_sommerfeld_normalization.py`.
- Ran `python3 scripts/precompute_audit_runners.py --runners
  scripts/dm_thermal_average_sommerfeld_normalization.py --allow-non-main`.
- Ran `docs/audit/scripts/run_pipeline.sh`.
- Ran `python3 docs/audit/scripts/audit_lint.py`; only the pre-existing
  Maradudin warning and existing notices remain.
- Ran `python3 scripts/vocab_lint.py --report-only
  docs/DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md
  scripts/dm_thermal_average_sommerfeld_normalization.py`.
- Ran `python3 scripts/render_controlled_vocabulary.py --check`.
- Ran `python3 -m py_compile
  scripts/dm_thermal_average_sommerfeld_normalization.py`.
- Ran `python3 scripts/precompute_audit_runners.py --runners
  scripts/dm_thermal_average_sommerfeld_normalization.py --allow-non-main
  --check-only`.
- Ran `python3 scripts/precompute_audit_runners.py --pr-diff origin/main
  --check-only`.
- Ran `git diff --check`.
