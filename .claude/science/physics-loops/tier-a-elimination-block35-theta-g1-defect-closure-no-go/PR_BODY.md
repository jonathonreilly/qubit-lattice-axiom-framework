## Summary

Block35 tests theta G1 defect closure on the current surface.

Movement:
- proves a current-surface no-go against deriving `dn = 0` or defect
  suppression from the updated axioms/primitives plus closed-branch carrier
  support;
- recomputes the finite `T^4_2` contrast: closed branch local moves preserve
  `Q_raw=2`, while a defectful branch produces `{-2,-1,0,1,2}`;
- keeps theta live and makes no registry/status edits.

## Artifacts

- `docs/THETA_G1_DEFECT_CLOSURE_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`
- `scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py`
- `logs/runner-cache/theta_g1_defect_closure_current_surface_no_go_2026_07_04.txt`
- `.claude/science/physics-loops/tier-a-elimination-block35-theta-g1-defect-closure-no-go/`

## Verification

- `PYTHONPATH=scripts python3 scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py` -> `PASS=137 FAIL=0`
- `python3 -m py_compile scripts/theta_g1_defect_closure_current_surface_no_go_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; newly seeded rows=0 because the row already exists in the earlier stack
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS with existing 23 warnings / 178 notices, no errors
- `git diff --check` -> PASS
- local review-loop disposition -> PASS

## Boundaries

No theta retirement, no `theta_bar=0`, no G1 positive theorem, no defect
suppression dynamics, no Tier-A registry edit, and no audit/effective-status
edit.
