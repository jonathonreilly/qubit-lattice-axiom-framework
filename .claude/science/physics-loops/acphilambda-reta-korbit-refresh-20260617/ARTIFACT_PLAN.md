# Artifact Plan

Artifacts:

- Update the ACPHILAMBDA R-eta note dependency boundary.
- Add runner source guards for the dependency refresh and no-promotion language.
- Refresh the runner cache.
- Add this handoff pack.

Verification:

- `python3 scripts/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.py`
- `python3 -m py_compile scripts/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_acphilambda_r_eta_readout_narrowing_2026_06_11.py`
- `git diff --check`
