# Assumptions And Imports

## Allowed Current Inputs

- Finite `C^2 x C^3` matrix algebra computed in
  `scripts/frontier_koide_gamma5_factor_bridge_no_go.py`.
- Companion G2 packet:
  `docs/G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md`,
  `scripts/frontier_g2_bridge_c3_current_cannot_beat_gap_a.py`, and
  `logs/runner-cache/frontier_g2_bridge_c3_current_cannot_beat_gap_a.txt`.
- Existing Koide gamma5 packet:
  `docs/KOIDE_GAMMA5_FACTOR_BRIDGE_NO_GO_NOTE_2026-06-06.md`,
  `scripts/frontier_koide_gamma5_factor_bridge_no_go.py`, and its cache.

## Imported Or External Inputs

None added. The packet only makes an existing companion source/runner/cache
edge explicit and machine-checked.

## Forbidden Inputs

- No new axiom.
- No observational target value.
- No fitted selector.
- No branch-local promotion of status.
- No edits under `docs/audit/`.

## Remaining Open Import

The actual frontier residual remains open: a rooted carrier that entangles
spin into the generation index and satisfies the T-odd/non-commuting-with-`S`
requirement without forcing `r`.
