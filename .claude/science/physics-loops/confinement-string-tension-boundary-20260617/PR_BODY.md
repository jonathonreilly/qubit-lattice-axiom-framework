## Summary

This PR repairs the source-side boundary for
`confinement_string_tension_note`. It preserves the exact graph-first SU(3)
`g_bare = 1 -> beta = 6` arithmetic and the useful finite-volume support
checks, while removing the retained/proposed-retained confinement theorem
claim.

The note now treats standard Yang-Mills confinement, Sommer-scale data, EFT
running, and phenomenological string-tension comparators as bounded imported
context.

## Checks

- `python3 scripts/frontier_confinement_string_tension.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_confinement_string_tension.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_confinement_string_tension.py`
- `python3 -m py_compile scripts/frontier_confinement_string_tension.py`
- `git diff --check`

## Scope Guard

- No audit-loop run.
- No audit result, audit ledger, publication, or front-door edits.
- No review-loop run; reviewer owns extraction and landing.
