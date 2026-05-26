# PR Backlog

Suggested title:

`[physics-loop] strong CP selected-surface repair (bounded-support)`

Suggested body:

```markdown
## Summary

- narrows `strong_cp_theta_zero_note` to selected-surface consistency on the explicitly theta-free Wilson-plus-staggered scalar-mass surface
- removes physical strong-CP solution and neutron-EDM prediction language from theorem scope
- adds a runner source-firewall for `FtildeF`, mass-orientation, and prediction overclaims
- regenerates audit/publication views; target row is `unaudited`, ready, queue position 1, `deps: []`

## Status

- actual current surface: bounded-support
- conditional surface: selected theta-free scalar-mass surface only
- no new axioms or conventions
- no physical strong-CP theorem claimed
- no audit verdict applied

## Verification

- `docs/audit/scripts/run_pipeline.sh`
- `set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_strong_cp_theta_zero.py | tee outputs/strong_cp_selected_surface_repair_2026-05-25.txt`
- `python3 -m py_compile scripts/frontier_strong_cp_theta_zero.py`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/STRONG_CP_THETA_ZERO_NOTE.md scripts/frontier_strong_cp_theta_zero.py .claude/science/physics-loops/strong-cp-selected-surface-repair`
- `git diff --check`
```
