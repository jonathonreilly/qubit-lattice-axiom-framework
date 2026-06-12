# Assumptions And Imports

## Inputs Kept

- A finite `4 x 4` massive Dirac Hamiltonian matrix.
- Standard Hermitian eigensolver facts: `numpy.linalg.eigh` returns an
  orthonormal eigenbasis for a Hermitian matrix.
- Finite-dimensional spectral projector algebra.

## Imports Retired Or Exposed

- The branch does not import a covariant `2E` spinor normalization into the
  live `I_4` claim.
- If a later version uses covariant `2E` spinors, it must include the matching
  `1/(2E)` field-expansion weight before claiming the equal-time identity.

## Open Guardrails

- CAR selection is not derived from the framework.
- Spacelike microcausality is not proved.
- Partner chirality and OS/Wightman field delivery remain open.
