# Assumptions And Imports

## Load-Bearing Local Inputs

- Parent open-system reset channel interface.
- Finite-dimensional linear algebra: matrix exponentials are invertible with
  inverse `exp(-tL)`.
- Reset superoperator `R(A) = |0><0| Tr(A)`.

## Not Imported As Closure

- No Lindblad derivation from a physical bath.
- No thermodynamic cost law.
- No finite-time physical rate or clock normalization.
- No low-record boundary derivation.
- No generation/Koide selector or fixed dial location.

## Import Disposition

The block closes only the finite-time bounded-generator shortcut. It leaves
asymptotic, discrete, singular-limit, non-Markovian, and open-boundary routes
available.
