# Review History

## Local Checks

```bash
python3 -m py_compile scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py
bash docs/audit/scripts/run_pipeline.sh
PYTHONPATH=scripts python3 scripts/SIGN_PORTABILITY_INVARIANT_COMPARE.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/SIGN_PORTABILITY_INVARIANT_FAMILY_SECOND_GROWN_DERIVATION_THEOREM_NOTE_2026-05-09.md
git diff --check
```

Results:

- Sign portability cached gate certificate: `PASS=42 FAIL=0`.
- Strict audit lint: no errors; one unrelated `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` warning remains.
- Controlled vocabulary check: clean.
- Note vocabulary lint: clean.
