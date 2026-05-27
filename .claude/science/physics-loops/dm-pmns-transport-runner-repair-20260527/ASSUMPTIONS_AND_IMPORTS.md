# Assumptions And Imports

## Imported Into The Bounded Witness

- `dm_leptogenesis_exact_common` exact package constants and transport profile
  helpers.
- The finite active charged-lepton block shape used by the existing witness:
  `canonical_h(x,y,delta) = Y Y^dagger`.
- The fixed `N_e` parameterized family and the interpolation criterion
  `eta/eta_obs = 1`.

## Removed/Stabilized Imports

- The primary runner no longer imports `canonical_h` from
  `frontier_dm_leptogenesis_pmns_projector_interface.py`, because that helper
  is now intentionally narrowed to raw pair-to-projector algebra.
- The primary runner no longer imports `active_packet_from_h` through the
  active-projector helper.
- The primary runner no longer imports the flavored column functional helper;
  the one-column functional is local and auditable inside this runner.

## Explicitly Not Claimed

- No retained physical selector law.
- No derivation of the off-seed source from `Cl(3)` on `Z^3`.
- No promotion of the PMNS helper rows.
- No full DM closure.
