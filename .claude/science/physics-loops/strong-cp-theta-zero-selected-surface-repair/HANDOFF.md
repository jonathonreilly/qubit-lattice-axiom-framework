# Handoff

## Target

`strong_cp_theta_zero_note`

## Repair

The source note is narrowed to the selected-surface algebra:

- no bare theta slot is a surface-selection hypothesis;
- positive real scalar quark masses are a surface-selection hypothesis;
- paired finite anti-Hermitian staggered spectra give positive determinants;
- real Wilson action plus positive determinant gives real effective action;
- nonnegative sector weights give `|Z(theta)| <= Z(0)`.

## What changed scientifically

The prior overstrong framing is removed. This row no longer claims a derived strong-CP solution or a derived action-surface selector. It claims the bounded theorem that, on the explicitly selected surface, the internal `theta_eff = 0` algebra closes.

## Verification

- `bash docs/audit/scripts/run_pipeline.sh` — pass; known pre-existing Maradudin warning remains.
- `PYTHONPATH=scripts python3 scripts/frontier_strong_cp_theta_zero_selected_surface_repair.py | tee outputs/strong_cp_theta_zero_selected_surface_repair_2026-05-25.txt` — `PASS=64 FAIL=0`.
- `python3 -m py_compile scripts/frontier_strong_cp_theta_zero_selected_surface_repair.py` — pass.
- `python3 docs/audit/scripts/audit_lint.py --strict` — pass with the known pre-existing Maradudin warning.
- `python3 scripts/render_controlled_vocabulary.py --check` — clean.
- `python3 scripts/vocab_lint.py --report-only docs/STRONG_CP_THETA_ZERO_NOTE.md .claude/science/physics-loops/strong-cp-theta-zero-selected-surface-repair/*.md` — 0 violations.
- `git diff --check` — pass.

Post-pipeline metadata: `claim_type=bounded_theorem`, `audit_status=unaudited`, `effective_status=unaudited`, `deps=[]`, `open_dependency_paths=[]`, `runner_path=scripts/frontier_strong_cp_theta_zero_selected_surface_repair.py`, audit queue position 1, ready true.

## Remaining blockers

For a framework-level strong-CP solution, separate retained derivations are still needed for the theta-free action-surface selector and the scalar-mass-only positive orientation. This PR does not supply those derivations.
