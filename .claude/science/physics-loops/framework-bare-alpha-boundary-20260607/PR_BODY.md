## Summary

- Narrows the archived bare `alpha_3 / alpha_em` packet to a conditional
  bookkeeping lemma over explicit supplied inputs.
- Removes the failed retained EW-normalization authority check and replaces it
  with source-boundary checks that forbid retained-lane, minimal-stack,
  low-energy, RGE, or projection claims.
- Preserves the exact arithmetic `2d + 3`, `d=3 -> 9`, `sin^2(theta_W)=4/9`,
  and the formal SU(5) contrast `5/72`.
- Refreshes the runner cache.

## Verification

- `python3 scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_framework_bare_alpha_3_alpha_em_dimension_fixed_ratio.py`
- `git diff --check`
- `git diff -- docs/audit`
