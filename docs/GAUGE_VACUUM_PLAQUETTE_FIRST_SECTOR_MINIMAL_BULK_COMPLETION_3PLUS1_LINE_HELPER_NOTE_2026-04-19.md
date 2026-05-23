# Gauge-Vacuum Plaquette First-Sector Minimal-Bulk Completion `3+1` Line Helper

**Date:** 2026-04-19 (wrapper note added 2026-05-17)
**Claim type:** bounded_theorem
**Status:** bounded — shared helper layer for the retained `3d+1 -> 3d`
complement-line reduction on the least-positive-bulk selected Wilson
branch.
**Status authority:** independent audit lane only. This wrapper note is
audit-lane infrastructure for the corresponding helper module.
**Primary runner / module:** `scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py`

**Audit-dispatch parent candidate:** This row is a runner-module wrapper
for helper code in
`scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_3plus1_line_helper_2026_04_19.py`.
If a future independent audit evaluates whether it is a
non-chain-closing wrapper/decorative handle, the helper module is the
candidate source object. This is source-side routing context only; it
does not assert an `audit_status` or `effective_status`.

## Purpose

This wrapper note documents the shared helper layer used by several
gauge-vacuum-plaquette completion theorems so that downstream notes can
register it as a one-hop dependency in the citation graph. Multiple
`audited_conditional` rows in the gauge-vacuum-plaquette
3+1-reduced-packet family named this helper as a missing dependency edge.

## What this module provides

- `ORIGINAL_RETAINED_WEIGHTS` — the original `((0,0), (1,0), (0,1),
  (1,1))` four-corner weights on the retained block.
- `ORDERED_LINE_BASIS` — the canonical `(1, 0, 2, 3)` reordering used to
  expose the boundary-first complement-line basis.
- `BOUNDARY_FIRST_WEIGHTS` — the reordered four-corner weights for the
  boundary-first complement-line frame.
- `compressed_local_block_from_line(...)` — the local block-compression
  routine that builds the reduced packet from a chosen complement line.
- `normalize_line(line)` and `line_from_positive_angles(theta, phi, psi)` —
  utility helpers for parameterizing positive-hemisphere unit lines.
- `projection_frobenius_distance(line, slot)` — the projector-distance
  helper consumed by the `rho1` least-distortion selector theorem.

## Imports

The helper itself depends on:
- `frontier_dm_leptogenesis_ne_projected_source_law_derivation.hermitian_linear_responses`
- `frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_packet_theorem_2026_04_19.selected_transfer_and_packet`
- `frontier_gauge_vacuum_plaquette_spatial_environment_character_measure.build_recurrence_matrix`
- `frontier_perron_frobenius_step2_nilpotent_chain_source_response_calculus_2026_04_19.live_from_response_pack`

## Boundary

This wrapper note records the bounded-theorem character of the
helper-layer module. It does not claim:
- a framework-level derivation of the complement-line frame;
- uniqueness of `BOUNDARY_FIRST_WEIGHTS` among admissible reorderings;
- closure of any downstream gauge-vacuum-plaquette theorem.

Its only function is to provide a citeable one-hop authority for
`compressed_local_block_from_line`, `BOUNDARY_FIRST_WEIGHTS`, line
normalization / parameterization helpers, and projection-distance helpers
so downstream notes can register them cleanly. The `selected_line`
selector itself is supplied by the separate `rho1` least-distortion
selector theorem note.
