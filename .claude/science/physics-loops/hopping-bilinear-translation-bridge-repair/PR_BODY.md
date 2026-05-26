## Summary

Repairs the audited-conditional hopping bilinear row by adding the retained
one-hop bridge named by the audit.

- replaces the stale lattice-Noether translation dependency with
  `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
- updates the runner to fail if that bridge is not retained-grade
- preserves the positive theorem proposal but leaves the actual status to
  independent audit

## Verification

- `python3 -m py_compile scripts/hopping_bilinear_hermiticity_check.py`
- `python3 scripts/hopping_bilinear_hermiticity_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `git diff --check`

## Audit Queue Result

- `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
  is now audit queue rank 1, ready, `audit_in_progress`, awaiting its
  required second-auditor cross-confirmation after becoming critical.
- `hopping_bilinear_hermiticity_theorem_note_2026-05-02` is now audit queue
  rank 2, ready, `unaudited`, with one-hop dependency
  `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`.

No audit verdict is applied in this PR.
