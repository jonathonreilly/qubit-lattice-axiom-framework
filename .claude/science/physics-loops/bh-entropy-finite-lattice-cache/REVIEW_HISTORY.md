# Review History

## Local Checks

```bash
python3 -m py_compile scripts/frontier_bh_entropy_derived.py
bash docs/audit/scripts/run_pipeline.sh
PYTHONPATH=scripts python3 scripts/frontier_bh_entropy_derived.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/BH_ENTROPY_DERIVED_NOTE.md
git diff --check
```

Results:

- BH entropy finite-lattice cache certificate: `PASS=44 FAIL=0`.
- Strict audit lint: no errors; one unrelated `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` warning remains.
- Controlled vocabulary check: clean.
- Note vocabulary lint: clean.
