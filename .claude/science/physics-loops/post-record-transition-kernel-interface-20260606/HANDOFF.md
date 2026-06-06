# Handoff

## Result

Verified branch-local exact-support result:

```text
post-record append/count algebra
  + supplied finite transition kernel
  => finite-history probabilities and expected count dynamics.
```

Fresh cache: `SUMMARY: PASS=39 FAIL=0`.

## Intended Safe Use

Use this when a downstream row supplies a finite transition kernel and needs
the exact record-history probabilities or expected count updates implied by
that kernel.

## Do Not Use For

- deriving the transition kernel;
- deriving Markov property or stationarity;
- deriving a clock, rate, Born law, instrument, Hamiltonian, action, coupling,
  or dial;
- applying an audit verdict.

## PR

Pending.
