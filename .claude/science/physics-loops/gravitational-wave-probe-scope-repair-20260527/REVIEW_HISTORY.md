# Review History

No review-loop pass has been run in this block. The draft PR is for reviewer
extraction and independent audit handling.

Local checks:

- `PYTHONPATH=scripts python3 scripts/frontier_grav_wave_post_newtonian.py`
- `python3 scripts/vocab_lint.py --report-only docs/GRAVITATIONAL_WAVE_PROBE_NOTE.md scripts/frontier_grav_wave_post_newtonian.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`
