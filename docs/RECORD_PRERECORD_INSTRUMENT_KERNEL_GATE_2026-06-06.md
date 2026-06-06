# Record Pre-Record Instrument Kernel Gate

Date: 2026-06-06

Status: conditional-support

actual_current_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact under supplied projective instrument and Born trace rule"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The block requires a supplied instrument and Born trace rule; it does not derive either premise from Record or Quantum alone."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Summary

This block makes the pre-record side of dynamics explicit:

```text
qubit state + supplied instrument + Born trace rule
  -> probabilities over possible future record atoms
realized outcome
  -> one-hot post-record atom/count update
```

The runner proves the finite one-qubit algebra under the stated conditional
premises. A pre-record density matrix plus a supplied projective instrument
gives a probability vector over possible record atoms. Once an outcome is
written, the post-record object is a realized atom or count increment, not the
probability vector.

## Runner

Runner:

```text
scripts/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_record_prerecord_instrument_kernel_gate_2026_06_06.txt
```

Scorecard:

```text
PASS=26 FAIL=0
```

## Exact Conditional Content

The runner uses the pure one-qubit state

```text
rho = [[2/3, sqrt(2)/3],
       [sqrt(2)/3, 1/3]]
```

and two supplied projective instruments.

For the `Z` instrument, the Born trace rule gives:

```text
p_Z = (Tr(P_0 rho), Tr(P_1 rho)) = (2/3, 1/3).
```

For the `X` instrument on the same state, the probabilities differ:

```text
p_X = (1/2 + sqrt(2)/3, 1/2 - sqrt(2)/3).
```

Therefore the instrument/readout context is load-bearing for the production
kernel. The qubit state alone is not the record-production kernel.

## Post-Record Split

If outcome `0` is realized, the written post-record atom is:

```text
e_0 = (1, 0).
```

If outcome `1` is realized, the written atom is:

```text
e_1 = (0, 1).
```

For a current count `(4,2)`, the realized updates are integral:

```text
(4,2) -> (5,2)
(4,2) -> (4,3)
```

The ensemble expectation is instead:

```text
E[c'] = (4,2) + (2/3,1/3) = (14/3, 7/3).
```

That expectation is useful, but it is not either realized post-record update.

## What This Unlocks

This gives the dynamics stack a typed input port:

```text
pre-record carrier state
  + supplied instrument/Born bridge
  -> production probabilities over possible record atoms
  -> realized atom after registration
  -> post-record information dynamics
```

It connects the user's implication directly: the qubit is the pre-record
probability carrier only after a probability-origin bridge and instrument are
supplied. The post-record site carries realized information.

This also composes with the clock/rate gate from PR #2809. A supplied
instrument can produce one-step probabilities; a supplied generator can then
stabilize a dial location; physical rates still need clock/rate normalization.

## Boundaries

This block does not:

- derive the measurement instrument;
- derive the Born trace rule;
- derive IID frequencies or typicality from one-shot probabilities;
- derive a physical Markov generator;
- derive a physical clock or rate unit;
- select a generation/Koide dial value;
- update repo-wide authority surfaces.

The current surface status is conditional-support because the instrument and
Born trace rule are load-bearing premises.
