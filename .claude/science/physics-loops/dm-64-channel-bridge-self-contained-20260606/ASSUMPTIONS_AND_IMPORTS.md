# Assumptions And Imports

## Current Surface

- Target claim id:
  `dm_full_closure_64_to_1_channel_weight_bridge_narrow_theorem_note_2026-06-02`
- Downstream consumer:
  `dm_full_closure_same_surface_thermal_bounding_theorem_note_2026-04-17`
- Existing gap moved: the bridge is now self-contained with respect to the
  downstream parent helper.
- No new axiom is added.
- No audit result file is edited.

## Load-Bearing Inputs

- `CL3_COLOR_AUTOMORPHISM_THEOREM.md` for the retained `3 x 3bar = 1 + 8`
  carrier split.
- `DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md` for the
  bounded Sommerfeld notation used to name `s_1` and `s_8`.
- The verifier itself proves the Gell-Mann generator normalization, singlet and
  octet projectors, exact `64:1` raw squared-coupling ratio, and exact folded
  `(8 s_1 + s_8)/9` coefficient identity.

## Remaining Parent Gaps

This repairs only the 64:1 channel-weight part of the parent blocker. Live-DM
plaquette/eta-omega constants and packet-completeness/selector premises remain
open for separate repair or audit.
