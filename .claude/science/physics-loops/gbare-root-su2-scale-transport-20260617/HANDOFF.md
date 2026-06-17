# Handoff

**PR:** https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4272

## What Changed

- Added a finite source theorem note proving that root `SU(2)` subgroups
  inside the graph-first `V_3` gauge `SU(3)` carrier use the same Pauli/2
  scale as the per-site spin double cover.
- Added a runner that checks the commutators, trace Gram, spectrum, spin
  period, permutation invariance, and failure of nontrivial positive scale
  dilation.
- Updated the stacked trace-surface bridge to cite this companion as a
  source-side candidate closure for the remaining finite scale gate.

## Claim-State Movement

This partially closes the exact blocker subclaim:

```text
per-site spin-double-cover normalization propagates to the gauge su(3)
trace surface by derivation rather than by bridge admission
```

It does not claim the parent `g_bare` theorem, does not retag any ledger row,
and does not update audit/status/publication surfaces.

## Remaining Blocker

Review/audit must decide whether the parent Wilson/Ward `g_bare` chain can
consume the graph-first `V_3` trace surface plus this finite root-`SU(2)`
scale theorem without reintroducing an admitted convention.
