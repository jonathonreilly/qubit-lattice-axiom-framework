# Assumptions And Imports

## Allowed Framework Inputs

- Lattice+Quantum finite local algebra on the canonical finite lattice.
- Finite-range Hamiltonian interaction support with range `R_int`.
- Per-site interaction norm bound `J_*`.
- Interaction adjacency degree bound `D_int`.
- Standard operator norm submultiplicativity and Duhamel expansion.

## Retired Import

- The previous truncated Poisson-tail shortcut is no longer load-bearing.
  The branch removes the false inequality route and uses weighted finite
  paths directly.

## Remaining Open Input

- L2 static/spatial cluster decomposition remains conditional on a separate
  gap/transfer-matrix authority. LR finite-speed control alone is not used
  to prove static connected-correlator decay.
