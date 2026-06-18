# Handoff

This PR addresses the new audited conditional on the Wilson all-orders
extremum row by following the auditor's split option.

Main artifacts:
- `docs/WILSON_M_H_TREE_AT_EXTREMUM_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`
- `scripts/frontier_wilson_m_h_tree_at_extremum_algebraic_core_split_2026_06_18.py`

Claim movement:
- Splits the clean algebraic curvature-scale formula into a standalone
  diagnostic bounded-support artifact.
- Leaves physical Higgs-pole readout, channel selection, nonzero `r`, and
  external matching outside scope.

Verification:
- `PYTHONPATH=scripts python3 scripts/frontier_wilson_m_h_tree_at_extremum_algebraic_core_split_2026_06_18.py`
- `PYTHONPATH=scripts python3 scripts/frontier_wilson_m_h_tree_at_extremum_all_orders.py`
- `python3 -m py_compile scripts/frontier_wilson_m_h_tree_at_extremum_algebraic_core_split_2026_06_18.py`
- `git diff --check`

No audit loop was run, and no audit/publication/status files were edited.
