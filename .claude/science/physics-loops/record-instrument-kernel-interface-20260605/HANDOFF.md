# Handoff

## Result

Bounded-support / exact conditional interface block ready for review.

## Main Finding

Given a supplied finite instrument and trace/effect pairing, probabilities form
a normalized kernel over possible record atoms. A realized outcome feeds the
post-record layer as a one-hot atom/history/count update. The expected count is
an ensemble object and is not generally a realized record.

## Boundaries

- Does not derive the instrument, Born/reference bridge, local observability,
  production, rates, time, or measurement Hamiltonian.
- Does not identify a nonselective density matrix with a record atom.
- Does not select a generation/Koide dial setting.

## Next Exact Action

Open PR against `main`, then patch this loop pack with the PR URL.
