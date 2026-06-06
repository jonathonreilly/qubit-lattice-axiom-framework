# Handoff

## Result

Verified branch-local no-go/allowed-class interface:

```text
gauge-invariant-local allowed class
  != selected nonzero Hamiltonian/action/couplings/truncation.
```

Fresh cache: `SUMMARY: PASS=48 FAIL=0`.

## Intended Safe Use

Use this as a firewall when a downstream row treats gauge-invariant-local
allowed-class membership as selection of a nonzero Hamiltonian, action shape,
couplings, or truncation.

Safe positive use:

```text
supplied candidate dynamics
  => allowed-class membership check.
```

## Do Not Use For

- deriving nonzero dynamics;
- selecting couplings, masses, beta values, or finite-beta action shape;
- selecting lowest-order truncation;
- deriving probabilities, rates, or a clock;
- selecting a generation/Koide dial value;
- applying an audit verdict.

## PR

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2822

Post-push verification:

- state: OPEN
- base: main
- head: physics-loop/dynamics-nontriviality-selection-firewall-20260606
- mergeable: MERGEABLE
- mergeStateStatus: CLEAN
- checks: no status check rollup
