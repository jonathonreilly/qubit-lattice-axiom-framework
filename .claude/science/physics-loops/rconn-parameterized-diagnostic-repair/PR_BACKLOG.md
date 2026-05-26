# PR Backlog

Suggested title:

`[physics-loop] R_conn diagnostic scope repair (bounded-support)`

Suggested body:

```markdown
## Summary

- narrows `rconn_derived_note` to exact SU(N_c) channel-fraction arithmetic plus diagnostic MC consistency
- removes matching rule M, `kappa_EW = 0`, and the physical connected-trace readout from theorem scope
- replaces the heavy MC runner as primary authority with a lightweight exact/diagnostic runner
- regenerates audit/publication views; target row is `unaudited`, ready, queue position 1, `deps: []`

## Status

- actual current surface: bounded-support
- no new axioms or conventions
- no physical readout theorem claimed
- no audit verdict applied

## Verification

- `docs/audit/scripts/run_pipeline.sh`
- `set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_rconn_parameterized_diagnostic.py | tee outputs/rconn_parameterized_diagnostic_repair_2026-05-25.txt`
- `python3 -m py_compile scripts/frontier_rconn_parameterized_diagnostic.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/RCONN_DERIVED_NOTE.md scripts/frontier_rconn_parameterized_diagnostic.py .claude/science/physics-loops/rconn-parameterized-diagnostic-repair`
- `git diff --check`
```
