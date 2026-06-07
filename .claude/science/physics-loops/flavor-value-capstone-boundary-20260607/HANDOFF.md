# Handoff

## What Changed

The note now preserves:

- local independence of the supplied `C3` coordinates;
- the singlet check for a supplied scalar `G=gI`;
- dispersion `Q` delta-blindness;
- readout-convention dependence.

It explicitly leaves open:

- physical carrier construction;
- physical gauge/Yukawa/CP/anomaly channel mapping;
- `eta=2/9` derivation;
- readout selection.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/flavor_four_channel_reframe_validated_2026_05_31.py
git diff --check
git diff --name-only | rg '^docs/audit/' && exit 1 || true
```

## Next Science Target

`koide_berry_monopole_bridge_reduction_note_2026-05-31` is the next plausible
finite-matrix boundary cleanup candidate.
