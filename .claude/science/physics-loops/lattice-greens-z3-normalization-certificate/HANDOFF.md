# Handoff

PR: pending

This block repairs `lattice_greens_function_maradudin_textbook_import_note_2026-05-18`
with a bounded Z^3 graph-Laplacian normalization certificate.

Generated audit state after the pipeline:

```text
audit_status=unaudited
effective_status=unaudited
claim_type=bounded_theorem
ready=true
open_dependency_paths=[]
```

Verification:

- `python3 scripts/lattice_greens_z3_asymptotic_normalization_certificate.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/lattice_greens_z3_asymptotic_normalization_certificate.py --allow-non-main`
- `bash docs/audit/scripts/run_pipeline.sh`
