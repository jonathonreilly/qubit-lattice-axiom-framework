# Assumptions And Imports

## Allowed Inputs

- Minimal Quantum axiom: one-site qubit algebra is available.
- Minimal Record axiom: post-record object is a durable realized outcome and
  Record supplies no probability or dynamics by itself.
- Record classicalization firewall: pre-record qubit state, supplied
  instrument, realized atom, and post-record count are distinct typed objects.
- Record clock/rate normalization gate: stable dial and physical rates remain
  separate from one-step probabilities.

## Conditional Inputs

- A supplied projective instrument/readout context.
- The Born trace rule for probabilities:
  `p_r = Tr(P_r rho)`.

## Constructed Inside This Block

- Exact one-qubit density matrix.
- Exact `Z` and `X` projective instruments.
- Exact probability vectors for both instruments.
- Realized one-hot post-record atoms and integral count updates.
- Nonselective ensemble state, kept separate from realized record atoms.

## Open Imports

- Derivation of the instrument/readout context.
- Derivation of the Born trace rule or an equivalent probability-origin bridge.
- IID/typicality for frequencies.
- Physical production generator and clock/rate unit.
- Generation/Koide dial-value derivation.

## Forbidden Inputs

- Observed masses or target dial values.
- Treating the post-record atom as the probability vector.
- Treating the pre-record qubit state alone as a production kernel.
- Claiming physical rates or stable dial selection from this one-shot
  conditional gate.
