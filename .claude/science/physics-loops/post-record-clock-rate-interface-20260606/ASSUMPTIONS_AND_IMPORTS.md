# Assumptions And Imports

## Load-Bearing Inputs

- Existing finite post-record history/count theorems.
- Existing dynamics-layer reconciliation note.
- Finite ordered-clock arithmetic for supplied clock maps.

## Non-Inputs

- No clock/time metric is supplied by Record.
- No stochastic process, transition kernel, Hamiltonian, or transfer operator
  is supplied.
- No probability/Born bridge is supplied for stochastic rates.
- No generation/Koide dial selector is supplied.

## Status Impact

The counts-alone clock/rate route is pruned. Conditional rate calculation
remains exact after a clock map is explicitly supplied.

