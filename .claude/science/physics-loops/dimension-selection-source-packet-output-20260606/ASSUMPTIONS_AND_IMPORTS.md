# Assumptions And Imports

## Current Surface

- Target claim id: `dimension_selection_note`
- Existing claim boundary: finite-runner lower-bound support only. The row
  supports the stated `d = 1,2` failure and `d = 3,4,5` pass pattern for the
  runner surface; it does not prove unique spatial dimension.
- No new axiom is added.
- No audit result file is edited.

## Source-Packet Inputs

- Parent repair runner:
  `scripts/frontier_dimension_selection_lower_bound_parent_repair.py`
- Original dimension runner:
  `scripts/frontier_dimension_selection.py`
- Finite-k bridge runner:
  `scripts/frontier_dimension_selection_finite_k_centroid_sign_bridge.py`
- Parent source-packet manifest:
  `scripts/dimension_selection_parent_source_packet_manifest_2026_06_05.py`
- D3 gate:
  `scripts/frontier_d3_lower_bound_source_packet_gate_2026_06_06.py`

## Imports Retired Or Exposed

- Retired for this blocker: the missing verifier-output artifact for the
  parent source packet.
- Still open: independent audit must decide whether this exact-support packet
  clears the conditional row.
