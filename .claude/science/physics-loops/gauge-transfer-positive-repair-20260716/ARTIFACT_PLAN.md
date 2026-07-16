# Artifact Plan

## Block 01 — landed

The finite-volume gauge transfer positivity repair landed through PR 5398 at
science commit `fe6586b0985956a245ba9eb93a93912373abb55d`.

## Block 02 — active

1. Rewrite the Wilson temporal-gauge bridge around the exact `SU(N)`
   representation-ring coefficient proof.
2. Add the independent real-Gram/Schur-power positive-type proof.
3. Extend the paired runner with:
   - nonnegative Wilson exponential scalar weights;
   - exact `SU(3)` `(3 ⊕ 3bar)^tensor n` multiplicities;
   - exact dimension sums `6^n`;
   - exact order-two decomposition;
   - nonnegative truncated coefficient sums;
   - deterministic positive- and negative-coupling `SU(3)` kernel controls.
4. Refresh the runner cache and verify its SHA.
5. Run independent manual/second-implementation checks.
6. Run review-loop fan-out, apply only narrow fixes, and re-review changed
   files.
7. Run disposable pipeline/lint compatibility checks, then remove every
   generated audit/ledger/queue/effective-status output.
8. Commit, push, and open one block-02 review PR. Never merge it from this
   campaign worker.
