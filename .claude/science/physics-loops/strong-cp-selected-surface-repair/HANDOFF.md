# Handoff

## What Changed

This PR repairs `strong_cp_theta_zero_note` by narrowing it to the explicitly
theta-free Wilson-plus-staggered scalar-mass surface. The internal determinant,
axial, effective-action, and sampled positive-weight checks are preserved.

The note and runner now explicitly say they do not derive:

- absence of an admissible physical CP-odd `FtildeF` slot,
- the positive real quark-mass orientation,
- a neutron-EDM prediction.

## Audit Queue Result

After `docs/audit/scripts/run_pipeline.sh`:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `deps: []`
- audit queue position: 1
- ready: true
- critical row, 879 descendants

No audit verdict is applied by this PR.

## Verification

```bash
docs/audit/scripts/run_pipeline.sh
set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_strong_cp_theta_zero.py | tee outputs/strong_cp_selected_surface_repair_2026-05-25.txt
python3 -m py_compile scripts/frontier_strong_cp_theta_zero.py
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/STRONG_CP_THETA_ZERO_NOTE.md scripts/frontier_strong_cp_theta_zero.py .claude/science/physics-loops/strong-cp-selected-surface-repair
git diff --check
```

Results:

- runner: `THEOREM PASS=26, FAIL=0`; `SELECTED-SURFACE COMPUTE PASS=30, FAIL=0`
- pipeline: completed; target row `unaudited`, queue position 1, `deps: []`
- strict audit lint: no errors; one pre-existing Maradudin warning remains

## Remaining Blocker

A physical strong-CP theorem still needs a retained-grade action-surface result
showing that the framework forbids an admissible CP-odd `FtildeF` slot and
selects the positive real quark-mass orientation.
