# Review History

- Local verifier: `PYTHONPATH=scripts python3 scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py` -> `PASS=41 FAIL=0`.
- `python3 -m py_compile scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py` -> pass.
- `bash docs/audit/scripts/run_pipeline.sh` -> pass; newly seeded rows=1.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> pass with existing 23 warnings and 178 notices; no errors.
- `git diff --check` -> pass.
- New audit row: `acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04`, `claim_type=bounded_theorem`, `audit_status=unaudited`, `effective_status=unaudited`, `criticality=leaf`.
- Scope review: exact algebraic support only; no AC retirement, no horn selection, no orbit-premise adoption, no K-real primitive, no registry edit, no R-eta/theta movement.
