# Handoff

This branch repairs the Kubo Fam2 data dependency blocker.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2618

## What Changed

- The source note links the data-producing refinement runner, runner cache, and
  legacy artifact log.
- The primary checker now verifies the data-producing runner source markers,
  SHA-fresh cache, and exact Recorded Finite Data table values.
- The cache for the primary checker is refreshed at `PASS=57 FAIL=0`.

## Verification

```bash
python3 -m py_compile scripts/frontier_kubo_fam2_non_convergence_stretch.py scripts/kubo_fam2_refinement.py
python3 scripts/cached_runner_output.py --check-only scripts/kubo_fam2_refinement.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_kubo_fam2_non_convergence_stretch.py
```

No audit result files are changed.
