# Assumptions And Imports

## Parent Inputs

- The parent runner `scripts/frontier_quark_cp_carrier_completion.py` supplies
  the fitted completion surface and comparator constants.
- The comparator targets remain imported atlas/observation targets in the
  parent row.
- The fitted `xi_u` and `xi_d` are numerical optimizer outputs, not derived
  framework primitives.

## New Block Inputs

- Exact ratio checks use the current parent fitted solution and Schur-base
  coefficients.
- The capped scan uses
  `xi_s = rho_s c13_s(base) exp(i phi_s)` with `0 <= rho_s <= R`.
- The capped scan lets `m_u/m_c` and `m_c/m_t` vary within `1%` of the parent
  comparators.
- The capped scan is deterministic finite optimizer evidence, not a proof of
  the global supremum over all possible small-carrier surfaces.

## Imports Not Retired

- Derivation of `xi_u`, `xi_d`.
- Derivation of comparator/readout targets.
- Framework-native normalization of the non-perturbative carrier.
- Full first-principles quark mass/CKM closure.

