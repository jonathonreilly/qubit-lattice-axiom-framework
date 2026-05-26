# Review History

## Local Checks

```bash
python3 -m py_compile scripts/gate_b_farfield_harness.py
bash docs/audit/scripts/run_pipeline.sh
PYTHONPATH=scripts python3 scripts/gate_b_farfield_harness.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/GATE_B_FARFIELD_NOTE.md
git diff --check
```

Results:

- Gate B certificate: `PASS=28 FAIL=0`.
- Strict audit lint: no errors; one unrelated `lattice_greens_function_maradudin_textbook_import_note_2026-05-18` warning remains.
- Controlled vocabulary check: clean.
- Note vocabulary lint: clean.
