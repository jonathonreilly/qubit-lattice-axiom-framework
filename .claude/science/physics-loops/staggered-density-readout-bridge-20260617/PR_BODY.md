## Summary

This PR adds a narrow finite-CAR bridge for the local density/readout blocker in
the lattice-Noether onsite/internal row. It proves
`rho_x = chibar_x chi_x -> a_x^dag a_x` as the local number projection and
normalized onsite U(1) generator, then updates the Noether note to cite that
bridge directly.

The broader staggered/Kawamoto-Smit realization gate remains out of scope. The
Noether packet keeps the KS coefficient matrix as an explicit finite exhibit
rather than a load-bearing broad gate dependency.

## Checks

- `python3 scripts/staggered_dirac_local_density_readout_bridge_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/staggered_dirac_local_density_readout_bridge_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/staggered_dirac_local_density_readout_bridge_2026_06_17.py`
- `python3 -m py_compile scripts/staggered_dirac_local_density_readout_bridge_2026_06_17.py`
- `git diff --check`

## Scope Guard

- No audit-loop run.
- No audit result, audit ledger, publication, or front-door edits.
- No review-loop run; reviewer owns extraction and landing.
