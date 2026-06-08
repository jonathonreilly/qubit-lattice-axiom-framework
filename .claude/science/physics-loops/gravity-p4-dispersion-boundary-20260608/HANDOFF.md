# Handoff

This branch repairs the gravity premise-4 source packet as bounded support.

What changed:

- T1 now uses the exact axis-lattice relation `k(phi)=arccos(1-(E-phi)/2)` before taking the small-k weak-field limit.
- The note exposes retained-bounded `self_consistency_forces_poisson` and `finite_rank_source_to_metric` dependencies.
- The Kubo comparison packet is checked as present/SHA-fresh but kept unaudited and comparison-only.
- The runner ends `TOTAL: PASS=19 FAIL=0`.

Remaining blocker:

A retained physical Fermat/eikonal bridge deriving `n=k/k0` from framework dynamics is still needed for full premise-4 closure.
