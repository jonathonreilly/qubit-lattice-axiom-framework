# Handoff

## What Changed

- Reframed the U4 conditional single-module row around the current minimal Quantum axiom.
- Preserved the abstract Cl(3) counterexample surface: `k >= 2` still exists if the one-qubit axiom is dropped.
- Added runner guards for the current-source split and one-qubit carrier arithmetic.
- Refreshed the runner cache.

## What Did Not Change

- No audit ledger/queue/publication/front-door files were edited.
- No audit verdict was applied.
- Full staggered-Dirac realization remains open outside this single-module/dimension piece.

## Verification

- `python3 scripts/audit_companion_staggered_dirac_substep1_u4_conditional_single_module_2026_05_17.py` -> `PASS=55 FAIL=0`
- `python3 scripts/cached_runner_output.py scripts/audit_companion_staggered_dirac_substep1_u4_conditional_single_module_2026_05_17.py` -> cache refreshed
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_companion_staggered_dirac_substep1_u4_conditional_single_module_2026_05_17.py` -> fresh
- `python3 -m py_compile scripts/audit_companion_staggered_dirac_substep1_u4_conditional_single_module_2026_05_17.py`
- stale-wording guard for the old open-input / old-axiom / U4-nonclosure phrases -> no matches
- `git diff --check`
