# Assumptions And Imports

The finite-grid diagnostic uses visible implementation inputs:

- canonical plaquette constants from `scripts/canonical_plaquette_surface.py`;
- Ward target `g_lattice / sqrt(6)`;
- two-loop SM RGE normalization;
- threshold scales and EW initial conditions in the runner.

These are not promoted to retained proof authorities by this branch. The
bounded claim is only that the coded diagnostic is stable on the declared grid
and brackets.
