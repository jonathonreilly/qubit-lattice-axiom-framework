# Handoff

## What Changed

- Repaired
  `docs/FLAVOR_SUBSTRATE_BRIDGE_FAILS_SOURCE_OPERATOR_ASYMMETRY_NOTE_2026-05-31.md`.
- Updated
  `scripts/flavor_substrate_bridge_fails_source_operator_asymmetry_2026_05_31.py`.
- Refreshed
  `logs/runner-cache/flavor_substrate_bridge_fails_source_operator_asymmetry_2026_05_31.txt`.

## Science Boundary

This PR does not derive source-domain carrier/readout authority and does not
close the substrate-necessity bridge. It keeps only the finite operator-collapse
algebra:

- `S=I` gives degenerate signed `Q=1/3`.
- Split circulant `H` gives signed `Q=2/3`.
- `Diag(H)=I` collapses the split operator to signed `Q=1/3`.
- `E_loc(I+zZ)=(1-z/3)I` is scalar for the displayed `Z`.

## Verification

- `python3 scripts/flavor_substrate_bridge_fails_source_operator_asymmetry_2026_05_31.py`
  - `SCORECARD PASS=5 FAIL=0`

## Remaining Work

The source-domain carrier/readout bridge remains open if the project wants the
broader physical substrate claim. This branch intentionally does not edit audit
ledgers, generated audit results, or repo-wide authority surfaces.
