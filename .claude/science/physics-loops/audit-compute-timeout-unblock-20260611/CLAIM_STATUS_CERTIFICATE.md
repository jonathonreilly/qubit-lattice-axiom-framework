# Claim Status Certificate

This PR is a compute unblock for two audited-conditional rows whose runner
inventory recorded timeout-class failures:

- `higgs_from_lattice_note`: replaces dense field-grid sweeps with bounded
  scalar minimization plus local curvature for the same bounded CW readout.
  The runner now completes under the 60-second cache timeout and keeps exact SM
  crossing open.
- `dm_full_closure_same_surface_thermal_bounding_theorem_note_2026-04-17`:
  replaces finite-range `mp.nsum` calls with explicit finite `mp.fsum` loops and
  reduces arbitrary precision from 80 to 60 decimal digits. The displayed
  certified endpoints and bracketing checks are unchanged at audit precision,
  and the runner now clears the 60-second cache timeout.

No retained status is asserted here. Independent audit owns all verdicts.
