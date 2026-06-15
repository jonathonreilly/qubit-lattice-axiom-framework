# Assumptions And Imports

## Retained/native inputs

- Finite qubit carrier algebra and tensor products.
- Unitary time evolution for a finite Hermitian Hamiltonian.
- Pointer dephasing and finite-density-matrix entropy calculations used by the
  runner.

## Bounded inputs

- Quantum-Darwinism record convention: a fragment record means recoverable
  pointer information in a fragment after dephasing the system in the pointer
  basis.
- The explicit finite carrier choice `S + E_1..E_n`.
- The explicit controlled-coupling family
  `H_rec(g) = g sigma_z(S) sum_k sigma_x(E_k)`.

## Not imported

- No observed target values.
- No fitted selector.
- No literature theorem or textbook result is load-bearing.
- No dynamics/action/coupling magnitude selection.
- No audit verdict, ledger status, or effective-status update.
