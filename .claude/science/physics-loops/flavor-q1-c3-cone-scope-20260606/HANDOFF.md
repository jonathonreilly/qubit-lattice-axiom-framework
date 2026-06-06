# Handoff

## Summary

This branch repairs the Q1/PRR packet by preserving the finite C3 reference-cone
no-go and removing the unsupported repo-baseline/PRR-status conclusion.

## Files

- `docs/FLAVOR_Q1_DEFAULT_RESTS_ON_PRR_NOTE_2026-05-30.md`
- `scripts/flavor_Q1_default_rests_on_PRR_2026_05_30.py`
- `logs/runner-cache/flavor_Q1_default_rests_on_PRR_2026_05_30.txt`

## Science

The packet now says:

- Under stipulated `C3`, the invariant reference-state cone admits both
  tracial `1:2` and non-tracial `1:1` block masses.
- Full `U(3)` invariance is a stronger selector, but this packet does not
  decide whether that stronger selector belongs to baseline.
- The displayed `Q` formula is spectral in `H` and does not use `rho`.

## What Review Should Check

- The note does not promote a repo-baseline only-C3 conclusion.
- The note does not decide PRR acceptance/status.
- The runner's C5 guard correctly enforces that boundary.
- No `docs/audit/**` files are changed.

## Next Science

The hard follow-up remains a physical readout theorem deciding how the doublet
is counted; that is outside this bounded source repair.
