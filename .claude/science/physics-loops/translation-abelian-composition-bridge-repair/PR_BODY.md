# Summary

Repairs `translation_abelian_composition_theorem_note_2026-05-02` after
audit found that the old proof imported full one-site physical
translation symmetry from the lattice Noether row.

The repaired note narrows to the retained finite tensor-product
translation bridge:

- `T_a T_b = T_{a+b}`;
- `[T_a,T_b] = 0`;
- `T_0 = I`;
- `T_a^dag = T_{-a}`;
- finite quotient faithfulness on the periodic block.

# Files

- `docs/TRANSLATION_ABELIAN_COMPOSITION_THEOREM_NOTE_2026-05-02.md`
- `scripts/translation_abelian_composition_check.py`
- `outputs/translation_abelian_composition_check_2026-05-25.txt`
- `.claude/science/physics-loops/translation-abelian-composition-bridge-repair/`

# Verification

```bash
python3 -m py_compile scripts/translation_abelian_composition_check.py
python3 scripts/translation_abelian_composition_check.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/TRANSLATION_ABELIAN_COMPOSITION_THEOREM_NOTE_2026-05-02.md scripts/translation_abelian_composition_check.py .claude/science/physics-loops/translation-abelian-composition-bridge-repair
git diff --check
```

# Status Boundary

This is `proposed_retained` only as an author proposal. Independent audit
must ratify the row before the repository treats it as effective retained.

# Audit Queue Result

After `bash docs/audit/scripts/run_pipeline.sh`,
`translation_abelian_composition_theorem_note_2026-05-02` is
`unaudited`, ready, medium criticality, queue rank 1, and depends only on
`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`.
No audit verdict is applied by this branch.
