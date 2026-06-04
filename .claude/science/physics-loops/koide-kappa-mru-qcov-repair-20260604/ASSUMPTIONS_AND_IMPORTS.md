# Assumptions And Imports

## Retained-Bounded One-Hop Authority

- `KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md`
  supplies the formal reduced two-slot log-volume identity:
  `rho_plus^2 = rho_perp^2`, with
  `kappa := 2 rho_plus^2 / rho_perp^2 = 2`.

## Native Checks

- Z3 circulant Gram ratio `Tr(B_1^2)/Tr(B_0^2) = 2`.
- Master identity and basis-robustness checks.
- Q/CoV convention algebra:
  `K_std = (sum m)/(sum sqrt(m))^2 = 2/3` at `CoV = 1`;
  inverse `Q_inv = 1/2` at `CoV = 1`.

## Not Imported

- No physical charged-lepton SO(2) quotient bridge.
- No observational mass input is load-bearing.
- No new axiom.
