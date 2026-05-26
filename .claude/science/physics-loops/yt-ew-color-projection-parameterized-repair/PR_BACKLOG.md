# PR Backlog

Suggested title:

`[physics-loop] YT EW color projection parameterized repair (bounded-support)`

Suggested body:

```markdown
## Summary

- narrows `yt_ew_color_projection_theorem` to the exact parameterized algebra `K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)`
- replaces the heavy MC runner as primary authority with a lightweight exact algebra runner
- keeps `kappa_EW = 0`, `K_EW = 9/8`, and observed-coupling comparisons as diagnostic context only
- regenerates audit/publication views; target row is `unaudited`, ready, queue position 1, `deps: []`

## Status

- actual current surface: bounded-support
- no new axioms or conventions
- no selector theorem claimed
- no audit verdict applied

## Verification

- `docs/audit/scripts/run_pipeline.sh`
- `set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_yt_ew_color_projection_parameterized.py | tee outputs/yt_ew_color_projection_parameterized_repair_2026-05-25.txt`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/YT_EW_COLOR_PROJECTION_THEOREM.md scripts/frontier_yt_ew_color_projection_parameterized.py .claude/science/physics-loops/yt-ew-color-projection-parameterized-repair`
- `git diff --check`
```
