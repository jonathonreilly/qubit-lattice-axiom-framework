# Handoff

## Result

Verified branch-local no-go/exact-boundary result:

```text
finite post-record counts
  => empirical statistics of realized atoms
  != predictive probability law
  != Born rule
  != rate/dial selector.
```

Fresh cache: `SUMMARY: PASS=56 FAIL=0`.

## Intended Safe Use

Use this as a firewall when a downstream row tries to cite post-record
history/count support for probabilities, Born weights, rates, stochastic
kernels, typicality, or dial selection.

Safe positive use:

```text
finite realized counts + supplied statistical model
  => empirical model audit or parameter estimation under named assumptions.
```

## Do Not Use For

- deriving the Born rule;
- selecting a pre-record state or instrument;
- deriving production rates or a clock;
- selecting a generation/Koide dial value;
- applying an audit verdict.

## PR

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2820

Post-push verification:

- state: OPEN
- base: main
- head: physics-loop/post-record-count-probability-firewall-20260606
- mergeable: MERGEABLE
- mergeStateStatus: CLEAN
- checks: no status check rollup
