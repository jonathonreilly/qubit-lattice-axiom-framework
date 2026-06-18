## Summary

Hardens the live `minimal_axioms` primary runner so the high-load current axiom row is audit-ready with explicit registry, policy, Tier-A, stale-alias, and no-laundering checks.

## What changed

- Adds the cached-output pointer to `docs/MINIMAL_AXIOMS_2026-06-05.md`.
- Expands `scripts/audit_companion_three_axiom_clean_base_exact.py` from elementary algebra sanity checks to a source-boundary certificate.
- Refreshes `logs/runner-cache/audit_companion_three_axiom_clean_base_exact.txt`.
- Adds branch-local physics-loop handoff/certificate files.

## Boundary

This PR does not audit or retag `minimal_axioms`, does not add or amend axioms, and does not alias superseded `MINIMAL_AXIOMS_2026-04-11.md` or `MINIMAL_AXIOMS_2026-05-03.md` into the current stable node.

## Verification

- `python3 scripts/audit_companion_three_axiom_clean_base_exact.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/audit_companion_three_axiom_clean_base_exact.py`
- `python3 -m py_compile scripts/audit_companion_three_axiom_clean_base_exact.py`
- `python3 docs/audit/scripts/check_axiom_premise_clean.py`
- `git diff --check`
- forbidden-path guard for audit/publication/status surfaces
