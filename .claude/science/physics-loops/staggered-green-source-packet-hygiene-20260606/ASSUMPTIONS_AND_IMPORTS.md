# Assumptions And Imports

## Current Surface

- Target claim id:
  `staggered_backreaction_live_green_packet_note_2026-05-29`
- Existing claim boundary: finite bounded graph-Green packet only.
- No continuum backreaction theorem, physical gravity closure, or calibrated
  holdout closure is added.
- No new axiom is added.
- No audit result file is edited.

## Inputs Used By This Repair

- Packet checker:
  `scripts/staggered_backreaction_live_green_packet_check.py`
- Source-packet manifest:
  `scripts/staggered_backreaction_live_green_source_packet_manifest_2026_06_04.py`
- Green closure source:
  `scripts/frontier_staggered_backreaction_green_closure.py`
- Prototype helper source:
  `scripts/frontier_staggered_backreaction_prototype.py`

## Imports Retired Or Exposed

- Retired for this blocker: ambiguity in the visible source-packet source
  coverage labels.
- Still open: independent audit must decide whether the current source-packet
  exposure clears the row.
