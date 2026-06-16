# Handoff

Branch:
`physics-loop/dimension-upper-bound-meta-requeue-20260616`

Target:
`dimension_upper_bound_dependency_edge_repair_note_2026-06-08`

Move:
This PR makes the source row visibly canonical meta:
`Claim type: meta`, `Type: meta / dependency-edge certificate`, plus runner
guards requiring that classification. It does not change the audit ledger.

Runner movement:
`scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py` now checks
the canonical meta classification. Current cache reports
`SUMMARY: PASS=49 FAIL=0`.

Remaining blocker:
If a positive theorem is desired, create/audit a separate parent
dimension-selection theorem with direct dependencies on the lower-bound packet
and native `d <= 3` upper edge.
