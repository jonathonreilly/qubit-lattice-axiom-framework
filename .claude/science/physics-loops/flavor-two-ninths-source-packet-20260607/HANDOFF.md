# Handoff

This PR partially repairs two paired flavor conditional rows:

- `flavor_generation_space_bridge_reduces_to_open_gate_2026-05-31`
- `flavor_asymmetry_identification_principled_not_forced_2026-05-31`

What changed:

- Both notes now expose the audited lepton `delta = 2/9` open-gate note,
  runner, and cache as raw restricted-packet paths.
- Both runners verify the lepton row is audited-clean only as an open gate,
  that the lepton cache is SHA-fresh, and that no phase/coefficient/scale
  derivation is promoted.
- Caches are fresh:
  - generation-space `PASS=15 FAIL=0`
  - asymmetry `PASS=9 FAIL=0`

Remaining blocker:

The physical charged-lepton generation-space/readout theorem is still missing.
This block does not close that science gate.
