# Assumptions And Imports

## Assumed

- A finite record alphabet `O`.
- A fixed finite horizon `n`.
- A realized post-record word `w* in O^n`.
- A supplied finite candidate set `M`.
- A supplied normalized law `P_m` on `O^n` for each `m in M`.
- Optional supplied prior `pi` if posterior weights are computed.
- Optional supplied threshold, loss, or decision rule if a model is selected.

## Not Imported From Record

- The model family.
- The prior.
- The decision rule or threshold.
- The observation protocol or horizon.
- Markov, stationarity, independence, exchangeability, or ergodicity.
- Born probabilities, an instrument, Hamiltonian, action, coupling, clock, or
  rate.
- A generation/Koide dial setting.

## Reused Landed Support

- `RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05`: exact finite
  post-record words and counts.
- `RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05`: post-record information
  dynamics consumes realized atoms and does not produce probability laws.
- `RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05`: bounded/conditional
  audit lanes need explicit remaining gates and cannot change verdicts by
  history/count support alone.
