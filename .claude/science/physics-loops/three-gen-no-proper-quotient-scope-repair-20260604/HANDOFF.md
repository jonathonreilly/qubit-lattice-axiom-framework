# Handoff

## Summary

This branch repairs the latest audited conditional three-generation bridge row
without adding axioms or editing the audit ledger.

The audit blocker said:

> scope_too_broad: revise the claim and B8/runner verdict text to say no
> nonzero proper invariant subspace, and replace the matrix-unit formula
> sentence with the retained Burnside formula using consistent indices.

## What Changed

- The source note now states the theorem as no nonzero proper invariant
  subspace, explicitly allowing `{0}` and `C^3`.
- The matrix-unit sentence now uses the retained-index formula
  `P_i sigma^k P_j = E_ij` with `k = i-j mod 3`.
- The runner now checks the same formula with projectors on both sides and
  replaces the old finite sample language with a complete coordinate-subspace
  reduction under the projectors and 3-cycle.
- The SHA-pinned runner cache was refreshed.

## Checks

- `PYTHONPATH=scripts python3 scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `python3 -m py_compile scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`
- `git diff --check`

## Boundaries

No audit result was added or retagged. The branch queues the repaired packet
for review and re-audit only.
