# Handoff

## Current Status

Stacked branch:

```text
physics-loop/record-prerecord-instrument-kernel-gate-20260606
```

Intended base:

```text
physics-loop/record-clock-rate-normalization-gate-20260606
```

Parent PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2809

PR for this block: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2810

GitHub verification: open PR, base
`physics-loop/record-clock-rate-normalization-gate-20260606`, head
`physics-loop/record-prerecord-instrument-kernel-gate-20260606`, mergeable
`MERGEABLE`, merge state `UNSTABLE`.

## Result

The runner gives conditional support for the pre-record instrument interface:
a supplied one-qubit projective instrument and Born trace rule produce
probabilities over possible future record atoms, while realized post-record
updates are one-hot/count information.

## Boundaries

- Does not derive the instrument/readout context.
- Does not derive the Born trace rule.
- Does not derive IID/frequency typicality.
- Does not derive a physical generator or clock/rate unit.
- Does not select a generation/Koide dial value.
- Does not update repo-wide authority surfaces.

## Next Action

Continue the 12-hour campaign. The immediate record follow-on is an
IID/typicality firewall; the next non-record hard lane remains repo-owned
finite SU(3), Wilson beta=6 reproduction.
