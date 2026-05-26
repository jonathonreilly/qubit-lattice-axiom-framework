# Handoff

## Target

`plaquette_self_consistency_note`

## Repair

The note is narrowed to a finite Wilson-plaquette diagnostic:

- finite compact `SU(3)` Wilson surface;
- bounded average plaquette observable;
- deterministic runner checks finite definitions and a one-plaquette MC diagnostic;
- canonical `0.5934` value is admitted as a comparator/reuse number, not derived.

## Verification

- `bash docs/audit/scripts/run_pipeline.sh` — pass; known pre-existing Maradudin warning remains.
- `PYTHONPATH=scripts python3 scripts/frontier_plaquette_self_consistency_finite_mc_repair.py | tee outputs/plaquette_self_consistency_finite_mc_repair_2026-05-25.txt` — `PASS=31 FAIL=0`.
- `python3 -m py_compile scripts/frontier_plaquette_self_consistency_finite_mc_repair.py` — pass.
- `python3 docs/audit/scripts/audit_lint.py --strict` — pass with the known pre-existing Maradudin warning.
- `python3 scripts/render_controlled_vocabulary.py --check` — clean.
- `python3 scripts/vocab_lint.py --report-only docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md .claude/science/physics-loops/plaquette-finite-mc-diagnostic-repair/*.md` — 0 violations.
- `git diff --check` — pass.

Post-pipeline metadata: `claim_type=bounded_theorem`, `audit_status=unaudited`, `effective_status=unaudited`, `deps=[]`, `open_dependency_paths=[]`, `runner_path=scripts/frontier_plaquette_self_consistency_finite_mc_repair.py`, audit queue position 1, ready true.

## Remaining blockers

The physical plaquette lane still needs either a completed same-surface MC certificate for `0.5934` or analytic beta=6 boundary-character/tensor-transfer closure.
