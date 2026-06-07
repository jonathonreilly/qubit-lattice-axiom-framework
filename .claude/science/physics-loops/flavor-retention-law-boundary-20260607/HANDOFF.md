# Handoff

## What Changed

The note now preserves the finite onsite algebra and explicitly leaves open:

- source-locality/readout selection for the physical charged-lepton surface;
- native derivation of the supplied `Q(z)` formula;
- any A2-to-source-domain retention theorem.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/flavor_retention_law_is_A2plus_2026_05_31.py
git diff --check
git diff --name-only | rg '^docs/audit/' && exit 1 || true
```

## Next Science Target

`flavor_a1prime_debt_and_data_note_2026-05-30` is the next tractable flavor
boundary candidate.
