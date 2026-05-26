# PR Backlog

Suggested title:

`[physics-loop] parity operator-basis formal sign repair (bounded-support)`

Suggested body:

```markdown
## Summary

- narrows `parity_operator_basis_dimension5_lv_no_go_theorem_note_2026-05-02` to formal Dirac-algebra P-weight identities
- removes the unproved lattice derivative representative bridge and physical lattice-action coefficient no-go from theorem scope
- adds a runner source-firewall for the formal boundary
- regenerates audit views; target row is `unaudited`, ready, queue position 1, `deps: []`

## Status

- actual current surface: bounded-support
- no new axioms or conventions
- no physical LV action no-go claimed
- no audit verdict applied

## Verification

- `docs/audit/scripts/run_pipeline.sh`
- `set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py | tee outputs/parity_operator_basis_formal_sign_repair_2026-05-25.txt`
- `python3 -m py_compile scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md scripts/frontier_parity_operator_basis_dimension5_lv_no_go.py .claude/science/physics-loops/parity-operator-basis-formal-sign-no-go-repair`
- `git diff --check`
```
