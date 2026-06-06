# Assumptions And Imports

## Current Surface

- Target claim id:
  `meson_gauge_invariant_os_transfer_representation_bounded_note_2026-05-30`
- Existing claim boundary: finite 3+1 carrier, gauge-invariant
  number-conserving meson basis, Berezin/operator transfer representation
  checked numerically to the note's existing tolerance.
- No continuum claim is added.
- No new axiom is added.
- No audit ledger row is edited.

## Inputs Used By This Repair

- Primary runner:
  `scripts/meson_gauge_invariant_os_transfer_representation_2026-05-30.py`
- Primary cache:
  `logs/runner-cache/meson_gauge_invariant_os_transfer_representation_2026-05-30.txt`
- Source-packet manifests:
  `scripts/meson_os_transfer_source_packet_manifest_2026_06_06.py`
  and
  `scripts/meson_gauge_invariant_os_transfer_source_packet_manifest_2026_06_06.py`

## Imports Retired Or Exposed

- Retired for this blocker: the need to trust stdout alone for whether the
  load-bearing Berezin/operator kernel-build functions are available for
  inspection.
- Still open: independent audit must decide whether the source-packet repair is
  sufficient for any status movement.
