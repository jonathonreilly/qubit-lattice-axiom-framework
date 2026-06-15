# Handoff

This PR repairs a conditional Koide MRU row by removing the missing physical
`SO(2)` quotient bridge from the current theorem claim.

What changed:

- The source note now says the re-audit target is only the exact unreduced
  `3 x 3` determinant-carrier obstruction.
- The reduced-carrier calculation is marked as a non-claim appendix/future
  route.
- The runner boundary checks enforce the scope lock.

Verification:

```sh
python3 scripts/frontier_koide_mru_weight_class_obstruction_theorem.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_koide_mru_weight_class_obstruction_theorem.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_mru_weight_class_obstruction_theorem.py --check-only --allow-non-main
git diff --check
```

Expected runner result: `classified_pass=37 fail=0`.
