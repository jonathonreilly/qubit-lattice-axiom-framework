# Goal

Refresh PR #3825 as a narrow source-side audit-unlock block.

The older branch had accumulated broad stale conflicts after main moved. This
refresh intentionally keeps only the three post-reseed conditional targets that
still need source-side repair:

- `ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11`
- `KOIDE_P1_COLLAPSES_FRAME_RESIDUALS_NOTE_2026-06-01`
- `THETA_P2_DETERMINANT_READOUT_EXHAUSTION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11`

The goal is not to audit them. The goal is to make the source artifacts precise,
cache-fresh, and reviewable so the independent review/audit lane can decide
whether any ledger movement is warranted.
