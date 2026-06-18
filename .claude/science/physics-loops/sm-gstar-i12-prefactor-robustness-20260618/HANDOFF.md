# Handoff

Branch: `codex/sm-gstar-i12-prefactor-robustness-20260618`

This branch hardens the `SM_GSTAR_I12` empirical thermal comparator bridge by
making the order-of-magnitude prefactor margin executable.

## What Moved

- Added a 2026-06-18 prefactor-robustness section to
  `docs/SM_GSTAR_I12_EMPIRICAL_THERMAL_COMPARATOR_BRIDGE_BOUNDED_NOTE_2026-06-15.md`.
- Extended `scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py`
  to check a 45-case grid over `m_nu`, `T`, and relative prefactor enhancement
  `E = c_Gamma/c_H`.
- Refreshed cache to `TOTAL: PASS=40 FAIL=0`.

## Boundary

This is bounded support. It proves exact rate/Hubble prefactors are not
decisive inside `E <= 1e4`; it does not derive small neutrino mass, the
Boltzmann collision operator, or radiation-era cosmology from framework
primitives.

## Verification

```bash
python3 scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py
python3 scripts/cached_runner_output.py --refresh scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py
python3 scripts/cached_runner_output.py --check-only scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py
python3 -m py_compile scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py
```

No audit loop, ledger retagging, publication-status edit, active review queue
edit, or main landing was performed.
