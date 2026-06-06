# Assumptions And Imports

## Load-Bearing Local Inputs

- Parent finite-time reset semigroup no-go.
- Parent open-system reset channel interface.
- Supplied per-step damping parameter `p`.
- Elementary residual arithmetic.

## Not Imported As Closure

- No derivation of `p`.
- No clock map from step count to physical time.
- No bath, temperature, or thermodynamic cost law.
- No exact finite-time reset endpoint.
- No generation/Koide selector or fixed dial location.

## Import Disposition

This block supplies epsilon accounting only. It does not convert step counts
into physical rates.
