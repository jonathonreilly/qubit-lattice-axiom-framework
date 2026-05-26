# Review History

- Ran `docs/audit/scripts/run_pipeline.sh`.
- Ran `python3 docs/audit/scripts/audit_lint.py`; only the pre-existing
  Maradudin warning and existing notices remain.
- Ran `python3 scripts/vocab_lint.py --report-only
  docs/MESOSCOPIC_SURROGATE_LOCALIZATION_SWEEP_NOTE.md`.
- Ran `python3 scripts/render_controlled_vocabulary.py --check`.
- Ran `python3 -m py_compile
  scripts/mesoscopic_surrogate_localization_family_sweep.py`.
- Ran `python3 scripts/precompute_audit_runners.py --runners
  scripts/mesoscopic_surrogate_localization_family_sweep.py --allow-non-main
  --check-only`.
- Ran `git diff --check`.
