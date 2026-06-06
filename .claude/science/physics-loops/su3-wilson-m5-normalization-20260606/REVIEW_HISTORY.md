# Review History

Local checks:

- `python3 -m py_compile scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py`
- `python3 scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py`
- `python3 scripts/cached_runner_output.py scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py --refresh --timeout-sec 120`
- `python3 scripts/cached_runner_output.py scripts/frontier_su3_wilson_closed_form_fanout_2026_05_04.py --check-only`
- `git diff -- docs/audit --exit-code`
- `git diff --check`

Disposition: pass local checks. Full review-loop and audit landing are
reviewer-owned per campaign discipline.
