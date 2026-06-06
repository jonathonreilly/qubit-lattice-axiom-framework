# Assumptions And Imports

## Assumed

- A two-state post-record alphabet.
- A supplied row-stochastic transition kernel `K(a,b)`.
- Parameters with `0 < a < 1`, `0 < b < 1`, so `|1-a-b| < 1`.

## Not Supplied By Record

- The kernel.
- The carrier/instrument dynamics that produces the kernel.
- A clock or physical transition rate.
- A Hamiltonian, action, coupling, Born law, or instrument.
- A rule selecting among possible kernels.
- A generation/Koide dial setting.

## Reused Landed Support

- `RECORD_EQUAL_LETTER_STABLE_LOCATION_2026-06-05`
- `RECORD_PRIOR_STABILITY_SELECTOR_2026-06-05`
- `RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05`
