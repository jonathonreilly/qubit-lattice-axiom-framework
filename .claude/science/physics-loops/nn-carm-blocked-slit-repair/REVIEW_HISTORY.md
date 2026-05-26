# Review History

- Ran `python3 scripts/lattice_nn_rescaled_C_arm_derivation.py`.
- Ran `python3 scripts/precompute_audit_runners.py --runners
  scripts/lattice_nn_rescaled_C_arm_derivation.py --allow-non-main`.
- Ran `docs/audit/scripts/run_pipeline.sh`.
- Ran `python3 docs/audit/scripts/audit_lint.py`; only the pre-existing
  Maradudin warning and existing notices remain.
- Ran `python3 scripts/vocab_lint.py --report-only
  docs/NN_LATTICE_RESCALED_C_ARM_DERIVATION_NOTE_2026-05-10.md`.
- Ran `python3 scripts/render_controlled_vocabulary.py --check`.
- Ran `python3 -m py_compile scripts/lattice_nn_rescaled_C_arm_derivation.py
  scripts/lattice_nn_rescaled_continuum_identification.py`.
- Ran `python3 scripts/precompute_audit_runners.py --runners
  scripts/lattice_nn_rescaled_C_arm_derivation.py --allow-non-main --check-only`.
- Ran `python3 scripts/precompute_audit_runners.py --pr-diff origin/main
  --check-only`.
- Ran `git diff --check`.
