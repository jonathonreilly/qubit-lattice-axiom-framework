# Handoff

This PR repairs `shapiro_family_portability_note` as a bounded finite
cross-family replay:

- removes proposed-retained wording and absolute stale paths;
- removes failed archived bridge dependencies from the live source chain;
- adds explicit runner PASS gates for zero controls, spread below `2.5e-4 rad`,
  monotonicity, bounded source status, no failed archive dependency, and no
  lab/field-speed/unique-causality claims;
- refreshes the SHA-pinned runner cache.

Checks run:

- `python3 scripts/shapiro_family_portability.py`
- `python3 scripts/cached_runner_output.py scripts/shapiro_family_portability.py --refresh --timeout-sec 1800`
- `python3 -m py_compile scripts/shapiro_family_portability.py`
- `git diff --check`

No audit loop was run, no audit data was edited, and no main landing was done.
