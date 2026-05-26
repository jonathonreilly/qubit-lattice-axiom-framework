# PR Backlog

Suggested title:

`[physics-loop] Planck Target 3 Clifford/CAR repair (conditional-support)`

Suggested body:

```markdown
## Summary

- narrows `planck_target3_clifford_phase_bridge_theorem_note_2026-04-25` to the conditional Clifford/CAR carrier bridge
- preserves the exact `c_Widom=c_cell=1/4` result under the metric-compatible coframe response premise
- removes `G_Newton,lat=1`, `a/l_P=1`, and source-unit normalization closure from theorem scope
- regenerates audit/publication views; target row is `unaudited`, ready, queue position 1, `deps: []`

## Status

- actual current surface: conditional-support
- no new axioms or source-unit conventions
- no SI `hbar` claim
- no audit verdict applied

## Verification

- `docs/audit/scripts/run_pipeline.sh`
- `set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_planck_target3_clifford_phase_bridge.py | tee outputs/planck_target3_clifford_car_repair_2026-05-25.txt`
- `python3 -m py_compile scripts/frontier_planck_target3_clifford_phase_bridge.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md scripts/frontier_planck_target3_clifford_phase_bridge.py .claude/science/physics-loops/planck-target3-clifford-car-repair`
- `git diff --check`
```
