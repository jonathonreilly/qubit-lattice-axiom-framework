# Assumptions And Imports

## Load-Bearing Inputs

- SU(3) dimension arithmetic: `F_adj = (N_c^2 - 1) / N_c^2 = 8/9`.
- Formal one-parameter readout family:
  `K_EW(kappa_EW) = 1 / (F_adj + kappa_EW (1 - F_adj))`.

## Not Load-Bearing

- `kappa_EW = 0`
- `K_EW = 9/8`
- observed `g_1`, `g_2`, `sin^2(theta_W)`, or alpha comparisons
- the old MC sweep runner

Those remain diagnostic context only.

## Removed Dependency Edges

The repaired source uses plain-text context references rather than markdown
authority edges for the old Fierz and matching-rule notes. The target row now
has `deps: []` after pipeline regeneration.
