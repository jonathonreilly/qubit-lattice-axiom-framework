# Artifact Plan

1. Rewrite
   `docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`
   with the exact positive-type, gauge-projector, transfer-trace, spatial
   insertion, repeated-source, and source-algebra intertwiner proofs.
2. Replace the paired runner with discriminating checks of:
   - low-order exact `SU(3)` tensor-power multiplicities;
   - sampled `SU(3)` Wilson Gram positivity and a negative-coupling control;
   - exhaustive nonabelian finite-group gauge projection and `M Q M`
     positivity;
   - exact finite-group transfer trace and spatial insertion;
   - symmetric repeated-source sandwich;
   - plaquette-holonomy pullback isometry;
   - pointwise-positive symmetric non-PSD counterexample.
3. Refresh the runner cache.
4. Run independent manual/second-implementation math checks.
5. Run review-loop reviewer fan-out, fix or demote, and re-review only changed
   files.
6. Run disposable pipeline/lint compatibility validation, then restore all
   generated audit surfaces from `origin/main`.
7. Commit, push, and open one block-01 review PR. Do not merge.
