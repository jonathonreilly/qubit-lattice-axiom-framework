# Assumptions And Imports

No new axiom is introduced.

No selector theorem is derived here.

Open/adopted inputs:

- `I_seed = D_KL(x || x_seed) + D_KL(y || y_seed) + (1 - cos delta)` remains
  an adopted information-geometric selector objective.
- The equality `eta_{i_*} / eta_obs = 1` remains imposed.
- The transport-favored column is supplied by sister machinery; this block
  computes consequences of adopting the selector on that surface.

The runner verifies only the conditional diagnostic: given the selector
surface, the low-cost off-seed closure source is reproduced.
