# Assumptions And Imports

## Inputs Used

- The retained single-plaquette recurrence and retained `d_5 = 1/472392`.
- The paired coefficient source packet:
  `scripts/frontier_beta6_d11_coefficient_2026_06_04.py`.
- Its cache:
  `logs/runner-cache/frontier_beta6_d11_coefficient_2026_06_04.txt`.

## Boundaries

- The harness imports the coefficient packet; it does not audit-retain it.
- The Monte Carlo plaquette value remains comparator-only.
- The beta=6 closure route remains open.
