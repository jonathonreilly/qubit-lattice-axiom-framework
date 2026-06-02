# Koide Anticommuting Eigenvector and Circulant Eigenvalue Readouts Are Consistent

**Date:** 2026-06-01
**Claim type:** bounded_theorem
**Claim boundary:** finite three-dimensional `C_3` readout reconciliation. This note
distinguishes eigenvector and eigenvalue Koide readouts; it does not choose which readout
is physical.
**Primary runner:**
`scripts/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.py`
with cache
`logs/runner-cache/frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.txt`.

## Result

There is no contradiction between the anticommuting/eigenvector route and the
circulant/eigenvalue route. They compute `Q=2/3` from different objects:

- In the anticommuting route, `{H,Gamma_chi}=0` and the theorem reads `sqrt(m)` from
  eigenvector components. The lightcone condition gives `Q(v)=2/3` for nonzero
  eigenvalue eigenvectors.
- In the circulant route, `[H,Gamma_chi]=0` and the theorem reads `sqrt(m)` from
  eigenvalues. At `r=|b|^2/a^2=1/2`, the eigenvalue readout gives `Q=2/3`.

Applying the eigenvalue readout to an anticommuting `H` gives `Q=infinity`, because the
odd-dimensional anticommuting spectrum is `{ -lambda, 0, +lambda }` and `sum lambda=0`.
That is a spectral fact about the wrong readout class for the anticommuting theorem, not
a contradiction with its eigenvector result.

## Computed Content

The runner checks:

- `Gamma_chi=(2/3)J-I`, `Gamma_chi^2=I`, and eigenvalues `{+1,-1,-1}`.
- A constructed Hermitian `H_anti` anticommutes with `Gamma_chi` and has spectrum
  `{ -1, 0, +1 }`.
- Nonzero eigenvectors of `H_anti` satisfy the lightcone condition and have
  eigenvector-readout `Q(v)=2/3`.
- The eigenvalue readout of that same `H_anti` is infinite because `sum lambda=0`.
- The circulant `H=aI+bC+conj(b)C^2` commutes with `Gamma_chi` and has eigenvalue-readout
  `Q=2/3` at `r=1/2`.

## Boundary

The note reconciles a readout-category confusion. It does not make anticommutation
necessary for `Q=2/3`, and it does not select eigenvectors or eigenvalues as the physical
charged-lepton readout. The remaining question is the readout-class selector.

## Load-Bearing Authorities

[KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md](KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md)
[KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md)
