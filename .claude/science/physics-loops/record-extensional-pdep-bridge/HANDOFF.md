# Handoff

## What Changed

This PR adds a narrow source-side bridge proving that record-intrinsic scalar
readouts are extensional in the registered atom. The unordered-mass-multiset
bridge now cites that artifact instead of carrying P-dep as an explicit
supplied premise.

## What It Should Unlock

If accepted, the audited conditional blocker on
`unordered_mass_multiset_registrability_bridge_narrow_theorem_note_2026-06-11`
should be ready for re-audit because the named P-dep premise is no longer
hidden or supplied; it is routed through a source theorem.

## What Remains Open

- physical species readout context;
- R-eta magnitude/value;
- Tier-A registry/theta retirement decisions;
- occupancy dial `r`;
- any auxiliary hidden-context diagnostic a downstream physical model wants to
  use instead of a record-intrinsic scalar readout.

## Verification

```text
python3 scripts/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.py
python3 scripts/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.py
python3 -m py_compile scripts/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.py scripts/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.py
python3 - <<'PY'
from scripts.runner_cache import cache_status
for r in [
    'scripts/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.py',
    'scripts/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.py',
]:
    print(r, cache_status(r))
PY
git diff --check
```
