# Handoff

## Target

`sm_relativistic_dof_count_import_note_2026-05-17`

## Repair

The row is narrowed from a named textbook import wrapper to a finite declared
inventory arithmetic certificate. The runner verifies:

- `g_bosonic = 16 + 6 + 2 + 4 = 28`;
- `g_fermionic = 72 + 12 + 6 = 90`;
- retained fermion weight dependency is `7/8`;
- `g_* = 28 + (7/8) * 90 = 427/4 = 106.75`;
- the broken-phase bosonic bookkeeping also sums to `28`;
- no open dependency paths remain after pipeline regeneration.

## Verification

- `bash docs/audit/scripts/run_pipeline.sh` -> pass; pre-existing Maradudin
  warning/notices only.
- `PYTHONPATH=scripts python3 scripts/frontier_sm_relativistic_dof_finite_inventory.py | tee outputs/sm_relativistic_dof_finite_inventory_2026-05-26.txt` -> PASS=37 FAIL=0.
- `python3 -m py_compile scripts/frontier_sm_relativistic_dof_finite_inventory.py` -> pass.
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors;
  pre-existing warning/notices only.
- `python3 scripts/render_controlled_vocabulary.py --check` -> clean.
- `python3 scripts/vocab_lint.py --report-only docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md` -> 0 violations.
- `git diff --check` -> pass.

## Audit Queue State

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `deps`: `hierarchy_seven_eighths_riemann_dirichlet_dimensional_anchor_narrow_theorem_note_2026-05-10`
- `open_dependency_paths`: `[]`
- `transitive_descendants`: `248`
- `load_bearing_score`: `8.96`
- queue position: `251`
- queue ready: `true`
- criticality: `high`

## Remaining Blockers

The Standard Model particle inventory is still a declared physical input. This
branch does not derive it from Axiom 1 / Axiom 2 and does not close downstream
DM-leptogenesis thermal claims.
