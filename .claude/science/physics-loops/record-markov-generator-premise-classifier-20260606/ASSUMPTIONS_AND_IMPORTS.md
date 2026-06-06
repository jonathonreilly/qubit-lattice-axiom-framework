# Assumptions And Imports

## Stacked Inputs

- PR #2800 supplies the Markov-generator embeddability boundary.
- The runner reuses the exact lazy, swap, and reset kernels from that boundary.

## Mathematical Inputs

- Column-stochastic transition matrices.
- Finite continuous-time Markov generators with nonnegative off-diagonal
  entries and zero column sums.
- `det(exp(Q t)) = exp(t tr(Q)) > 0` for finite real matrices at finite time.

## Forbidden Imports

- No kernel is derived from record atoms alone.
- No Born/IID bridge is derived from a stochastic kernel.
- No physical clock or rate unit is derived.
- No Koide/generation dial setting is selected or fixed.

## Open Imports

- Deriving actual production kernels.
- Deriving pre-record probability/Born interfaces.
- Deriving physical clock/rate normalization.

