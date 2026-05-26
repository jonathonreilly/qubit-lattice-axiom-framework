## Summary

Repairs `parity_operator_basis_dimension5_lv_no_go_theorem_note_2026-05-02` after audit held it conditional on an unproved bridge from formal SME derivative labels to actual staggered-lattice derivative representatives.

This PR narrows the row to what the packet actually proves:

- formal 4x4 Dirac-sign identities for the four listed dimension-5 templates,
- odd total spatial-index parity gives formal P-sign `-1`,
- even total spatial-index parity remains an excluded P-even consistency sector,
- the separate finite-lattice identity `epsilon H_0 epsilon = -H_0` for free staggered `H_0`.

It explicitly drops:

- a dimension-5 LV lattice-action no-go,
- any complete staggered SME operator-basis claim,
- any claim that formal `partial_mu` labels have actual lattice derivative representatives here.

## Audit Routing

- Target row: `parity_operator_basis_dimension5_lv_no_go_theorem_note_2026-05-02`
- Post-pipeline status: `unaudited`
- Queue position: 1
- Criticality: critical
- Transitive descendants: 889
- Audit verdict applied: no

## Checks

- `python3 scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 -m py_compile scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py .claude/science/physics-loops/parity-formal-signature-repair`
- `git diff --check`
