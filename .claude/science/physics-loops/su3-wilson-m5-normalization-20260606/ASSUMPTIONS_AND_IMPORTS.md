# Assumptions And Imports

## Native Inputs

- SU(N) Wilson plaquette deficit normalization:
  `W = 1 - (1/N) Re Tr U_p`.
- One-loop coefficient formula:
  `W = c_1 / beta + O(beta^-2)`, `c_1 = (N^2 - 1) / 4`.
- For SU(3), `c_1 = 2`, hence `<P>_WC(beta=6) = 1 - 2/6 = 0.666667`.
- Existing M1, M2, and M4 computations remain unchanged.

## Comparator-Only Imports

- `<P>_MC(beta=6) = 0.5934`.
- `epsilon_witness = 3.03e-4`.

These are not used to derive the four closed-form estimates. They only grade
the gap-to-comparator table.

## Literature Context

Di Renzo and Scorzato, arXiv:hep-lat/0011067, is used as a normalization
cross-check for the standard SU(3) plaquette-deficit convention and the
reported first coefficient. The branch does not use the paper as a hidden
proof input; the runner computes the coefficient from the displayed formula.
