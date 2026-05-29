# Handoff

Target row: `newton_law_derived_note`.

Repair summary:

- Replaced the three-admission Newton force-law note with a bounded
  potential-kernel algebra packet.
- Added a dedicated scope runner.
- Physical Poisson EOM, Green-kernel derivation, BA-3 force response, product
  law, and gravity closure remain out of scope.

Verification before PR:

- `python3 -m py_compile scripts/newton_law_potential_kernel_scope_check.py`
- `python3 scripts/newton_law_potential_kernel_scope_check.py`
- `bash docs/audit/scripts/run_pipeline.sh`

Pipeline result:

- Target row queued `unaudited`.
- Audit queue rank: 246.
- Ready queue count: 63.
- Effective status counts after regeneration: `audited_conditional=14`,
  `unaudited=1197`.
- Target row has `open_dependency_paths=[]` after narrowing.
- Stale audit invalidations: 0.

`git diff --check` remains the final pre-commit check.

Reviewer should extract the exact gradient algebra without treating it as a
Newton force-law derivation.
