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

The runner imports 5 helper modules; all now have one-hop wrapper or
source authorities registered for audit-graph purposes:

- [DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_LAW_DERIVATION_NOTE_2026-04-16.md](DM_LEPTOGENESIS_NE_PROJECTED_SOURCE_LAW_DERIVATION_NOTE_2026-04-16.md) — supplies the `Ne` projected-source-law inputs used to construct `TARGET` and `sparse_face_projected_data`.
- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_HELPER_NOTE_2026-04-19.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_HELPER_NOTE_2026-04-19.md) — line-helper interface only, supplying `compressed_local_block_from_line`, `BOUNDARY_FIRST_WEIGHTS`, and the line normalization / projection utilities without deriving the complement-line frame or selector.
- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_RHO1_LEAST_DISTORTION_SELECTOR_THEOREM_NOTE_2026-04-20.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_MINIMAL_BULK_COMPLETION_3PLUS1_LINE_RHO1_LEAST_DISTORTION_SELECTOR_THEOREM_NOTE_2026-04-20.md) — `rho1`-anchored least-distortion selector theorem supplying `selected_line`.
- [DM_LEPTOGENESIS_DWEH_EVEN_SPLIT_TRANSFER_LAYER_NOTE_2026-04-19.md](DM_LEPTOGENESIS_DWEH_EVEN_SPLIT_TRANSFER_LAYER_NOTE_2026-04-19.md) — `dW_e^H` even-split transfer-layer theorem supplying `TARGET` + `(S12, S13)` even-column split.
- [DM_LEPTOGENESIS_K00_SPARSE_FACE_TARGET_PREIMAGE_THEOREM_NOTE_2026-04-15.md](DM_LEPTOGENESIS_K00_SPARSE_FACE_TARGET_PREIMAGE_THEOREM_NOTE_2026-04-15.md) — `K00`-sparse-face target-preimage theorem supplying the sparse-face preimage construction.

This dependency repair records source authority only. It does not
promote the theorem status; independent audit still decides whether the
previous missing-dep-edge admissions are fully resolved after re-audit.
