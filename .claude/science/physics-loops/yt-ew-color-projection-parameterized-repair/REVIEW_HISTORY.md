# Review History

Local review findings:

- The old `kappa_EW = 0` admission language is removed from the theorem
  boundary.
- `9/8` and observed-coupling tables remain only as diagnostic context.
- The primary runner is now a lightweight exact algebra runner.
- Pipeline re-queued the row as `unaudited`, ready, queue position 1, `deps: []`.
- No new axiom, convention, observation, or selector is introduced.

Verification:

```bash
python3 -m py_compile scripts/frontier_yt_ew_color_projection_parameterized.py
docs/audit/scripts/run_pipeline.sh
set -o pipefail; PYTHONPATH=scripts python3 scripts/frontier_yt_ew_color_projection_parameterized.py | tee outputs/yt_ew_color_projection_parameterized_repair_2026-05-25.txt
```
