# Assumptions And Imports

## Assumed

- A finite record alphabet `O`.
- A fixed finite horizon `n`.
- A realized post-record word `w* in O^n`.
- A supplied normalized finite null law `P` on `O^n`.
- A supplied ordered statistic `T` and tail direction.
- A supplied threshold if the p-value is converted into an audit flag.

## Not Imported From Record

- The null law.
- Markov, stationarity, independence, exchangeability, or ergodicity.
- The statistic, threshold, or model-selection rule.
- A clock/rate map from event index to physical time.
- Born probabilities, an instrument, Hamiltonian, action, or coupling.
- A generation/Koide dial setting.

## Reused Landed Support

- `RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05`: exact finite
  post-record words and counts.
- `RECORD_DYNAMICS_LAYER_RECONCILIATION_2026-06-05`: post-record information
  dynamics consumes realized atoms and does not produce probability laws.
- `RECORD_HISTORY_COUNT_AUDIT_UNLOCK_SCAN_2026-06-05`: bounded/conditional
  audit lanes can cite finite history/count support but cannot change verdicts
  from that support alone.
