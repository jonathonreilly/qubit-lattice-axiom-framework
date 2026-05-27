# Review History

No review-loop pass has been run in this block. The draft PR is for reviewer
extraction and independent audit handling.

Local checks:

- `PYTHONPATH=scripts python3 scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
- `python3 scripts/vocab_lint.py --report-only docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`
