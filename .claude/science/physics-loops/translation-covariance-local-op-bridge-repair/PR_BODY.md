# Summary

Repairs `translation_covariance_local_op_theorem_note_2026-05-02` after
audit found that the old proof imported a full one-site `H_phys`
translation representation from lattice Noether.

The repaired note narrows to the retained finite tensor-product
translation bridge:

- single-site `M_2(C)` operators shift by `T_a M_x T_a^dag = M_{x+a}`;
- finite-support products shift all support labels;
- translation-invariant finite sums commute with `T_a`;
- density and hopping monomial examples are checked on the same surface.

# Files

- `docs/TRANSLATION_COVARIANCE_LOCAL_OP_THEOREM_NOTE_2026-05-02.md`
- `scripts/translation_covariance_local_op_check.py`
- `outputs/translation_covariance_local_op_check_2026-05-25.txt`
- `.claude/science/physics-loops/translation-covariance-local-op-bridge-repair/`

# Verification

```bash
python3 -m py_compile scripts/translation_covariance_local_op_check.py
python3 scripts/translation_covariance_local_op_check.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/TRANSLATION_COVARIANCE_LOCAL_OP_THEOREM_NOTE_2026-05-02.md scripts/translation_covariance_local_op_check.py .claude/science/physics-loops/translation-covariance-local-op-bridge-repair
git diff --check
```

# Status Boundary

This is `proposed_retained` only as an author proposal. Independent audit
must ratify the row before the repository treats it as effective retained.

# Audit Queue Result

After `bash docs/audit/scripts/run_pipeline.sh`,
`translation_covariance_local_op_theorem_note_2026-05-02` is `unaudited`,
ready, medium criticality, queue rank 1, and depends only on
`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`.
No audit verdict is applied by this branch.
