# Summary

Repairs `momentum_charge_commute_theorem_note_2026-05-02` after audit
found that the old note overclaimed a full framework physical momentum
operator from the lattice Noether row.

The repaired theorem narrows to the retained finite tensor-product
translation bridge:

- `[T_a,Q_total]=0`;
- finite-block spectral generators `K_mu = f(T_{e_mu})` commute with
  `Q_total`;
- axial `K_mu` commute pairwise on the finite block;
- common finite-block labels exist on this narrowed surface.

# Files

- `docs/MOMENTUM_CHARGE_COMMUTE_THEOREM_NOTE_2026-05-02.md`
- `scripts/momentum_charge_commute_check.py`
- `outputs/momentum_charge_commute_check_2026-05-25.txt`
- `.claude/science/physics-loops/momentum-charge-tensor-generator-repair/`

# Verification

```bash
python3 -m py_compile scripts/momentum_charge_commute_check.py
python3 scripts/momentum_charge_commute_check.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/MOMENTUM_CHARGE_COMMUTE_THEOREM_NOTE_2026-05-02.md scripts/momentum_charge_commute_check.py .claude/science/physics-loops/momentum-charge-tensor-generator-repair
git diff --check
```

# Status Boundary

This is `proposed_retained` only as an author proposal. Independent audit
must ratify the row before the repository treats it as effective retained.

# Audit Queue Result

After `bash docs/audit/scripts/run_pipeline.sh`,
`momentum_charge_commute_theorem_note_2026-05-02` is `unaudited`, ready,
medium criticality, queue rank 1, and depends only on
`tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`.
No audit verdict is applied by this branch.
