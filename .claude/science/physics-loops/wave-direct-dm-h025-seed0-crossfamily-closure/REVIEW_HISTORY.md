# Review history

## Iteration 1

Disposition: fixes required.

- split the class-B dependency reads from the class-A load-bearing
  inequalities;
- accept the full retained-grade dependency-status set rather than pinning
  `retained_bounded`;
- replace the stale trace quote with the active hard-coded-match blocker;
- classify `H`, seed, and strength as inherited coordinates, not an admission;
- align the proposed-retained note status and certificate.

All five findings were fixed. Independent raw-log arithmetic reproduced the
two negative signs, both strict orderings, and spreads `7.773%` and `6.673%`.

## Iteration 2

Disposition: pass.

- Code / runner: pass.
- Physics claim boundary: bounded.
- Imports / support: clean.
- Nature-retention disposition: bounded.
- Labeling convention: pass.
- Repo governance: pass after adopting the current
  `candidate-retained-grade` certificate field.
- Audit compatibility: pass; independent audit remains required.

## Validation

- Primary runner: pass; transcript exact match.
- Independent arithmetic: pass.
- Python compilation: pass.
- Vocabulary lint: pass with zero violations.
- Audit pipeline: pass; the changed row seeded as `bounded_theorem`, was reset
  to `unaudited`, had exactly the two retained control dependencies, and
  appeared in the ordinary audit queue.
- Static runner classification after the final numeric-check cleanup:
  dominant class `A` (`A=4`, `B=3`, `C=0`, `D=0`).
- Strict audit lint: zero errors; repo-global pre-existing warnings/notices
  remained.
- Generated audit, queue, and effective-status outputs were restored from
  `origin/main` and are not branch changes.

## Iteration 3

Disposition: pending focused review.

- Prior-art result: the bounded theorem is already landed; cycle 2 is a
  reproducibility repair, not a new derivation claim.
- Discovered defect: the primary runner crashes on current main because the
  monolithic audit-ledger cache is no longer tracked.
- Applied repair: remove mutable audit-grade reads, import both self-contained
  source runners for packet inclusion, declare all note/runner/log inputs for
  cache fingerprinting, and narrow `weak-field control` to exact configured
  ladder checks.
- Pre-review checks: primary runner, paired output equality, cache freshness,
  Python compilation, and static helper discovery pass.
