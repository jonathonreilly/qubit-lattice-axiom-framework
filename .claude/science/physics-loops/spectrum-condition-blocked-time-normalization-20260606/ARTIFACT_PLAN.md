# Artifact Plan

- Patch the spectrum-condition note to define `a_blk := 2 a_tau` for
  `T := T_hat^2`.
- Patch the runner to construct `T = exp(-a_blk H_lat)` and reconstruct
  `H = -log(T/M_T)/a_blk`.
- Refresh only `logs/runner-cache/axiom_first_spectrum_condition_check.txt`.
- Run syntax and diff hygiene checks.
- Open a review PR against `main`.
