# Handoff

This branch repairs the Choi normalization conflict in the Kraus-Choi
finite-region note. The note now uses the unnormalized
`|Omega> = sum_i |i>|i>` convention throughout, explains the normalized
alternative and its required factor `d`, and removes the stray `sqrt(d)` factor
from the unnormalized Kraus unvectorization statement.

## Verification

- `python3 scripts/kraus_choi_normalization_convention_check_2026_06_05.py`
- `python3 -m py_compile scripts/kraus_choi_normalization_convention_check_2026_06_05.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/kraus_choi_normalization_convention_check_2026_06_05.py --force --push-mode=none --allow-non-main --concurrency 1`

## Reviewer Notes

- No `docs/audit/**` files should be present in this PR.
- No new axiom is introduced.
- The branch does not claim an infinite-volume channel theorem.
- The branch does not re-prove Kraus/Choi; it repairs and checks the source convention.

## PR

Pending.
