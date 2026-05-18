# Gauge-Vacuum Plaquette First-Sector Minimal-Bulk Completion `3d+1` Reduced-Packet Complex-Givens Selector Theorem

**Date:** 2026-04-20  
**Status:** exact proposed_retained-ambient theorem on the selected minimally-positive
Wilson branch  
**Script:** `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_reduced_packet_complex_givens_selector_theorem_2026_04_20.py`

## Statement

On the canonical retained real `3d` slice selected from the minimally-positive
factorized Wilson branch, the ordered complex-Givens grammar

`G12 · G13 · G23`

contains exact solutions of the reduced projected-source packet equation for

`(E1, E2, S12, S13)`.

Among the audited exact solutions in that finite grammar, Frobenius distance to
the identity basis has a unique strict minimum. The selected dressing
reproduces the reduced projected-source packet exactly and therefore lands on
the live DM target exactly on that same selected retained slice.

## Scope

This is an exact **reduced-packet** theorem on the selected retained ambient.
It does **not** claim exact full sparse-face `9`-channel packet equality on the
same ambient.

## Authority

- Runner:
  `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_reduced_packet_complex_givens_selector_theorem_2026_04_20.py`

## Upstream authorities

The runner imports 5 helper modules; of these, two have current framework
wrapper notes:

- [DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_LAW_DERIVATION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_LAW_DERIVATION_NOTE_2026-04-16.md) — supplies the `Ne` projected-source-law inputs used to construct `TARGET` and `sparse_face_projected_data`.
- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_RHO1_LEAST_DISTORTION_SELECTOR_THEOREM_NOTE_2026-04-20.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_RHO1_LEAST_DISTORTION_SELECTOR_THEOREM_NOTE_2026-04-20.md) — supplies the `selected_line` selector used by the reduced-packet runner.

Remaining missing-dep-edge admissions (no framework wrapper exists):
- `frontier_dm_leptogenesis_dweh_even_split_transfer_layer` (transfer-layer helper)
- `frontier_dm_leptogenesis_k00_sparse_face_target_preimage_theorem` (sparse-face preimage theorem source)
- `frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19` (line-selection helper supplying `compressed_local_block_from_line`)

Each of these would need a dedicated source-note wrapper before the
remaining `compressed_local_block_from_line`, `solve_sparse_target_preimage`,
and `sparse_face_projected_data` admissions can fully close.
