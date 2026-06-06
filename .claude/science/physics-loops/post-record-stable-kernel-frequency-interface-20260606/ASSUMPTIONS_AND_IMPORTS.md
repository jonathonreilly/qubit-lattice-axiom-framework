# Assumptions And Imports

## Assumed

- A finite post-record alphabet.
- A supplied target prior and reset strength.
- A supplied initial law.
- A supplied event-step probability model.
- A finite horizon `N`.

## Not Supplied By Record

- The target prior.
- The transition kernel.
- The initial law.
- Concentration bounds or p-value rules.
- A clock/rate map, Born law, instrument, Hamiltonian, action, coupling, or
  generation/Koide dial.

## Reused Landed Support

- `RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05`
- `RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05`
- `RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05`
