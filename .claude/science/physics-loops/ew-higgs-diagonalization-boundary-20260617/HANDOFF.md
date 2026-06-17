# Handoff

This branch repairs `ew_higgs_gauge_mass_diagonalization_theorem_note_2026-04-26`.

What changed:

- status line is bounded support, not proposed-retained;
- a claim-boundary section names the EW-Higgs inputs as declared boundaries;
- the exact symbolic mass/charge/rho algebra is preserved;
- the runner now checks the bounded boundary and returns `VERDICT: BOUNDED_SUPPORT`;
- the cache is refreshed for the new runner/text.

Checks to run:

- `python3 scripts/frontier_ew_higgs_gauge_mass_diagonalization.py`
- `python3 scripts/cached_runner_output.py scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --refresh`
- `python3 scripts/cached_runner_output.py scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --check-only`
- `python3 -m py_compile scripts/frontier_ew_higgs_gauge_mass_diagonalization.py`
- `git diff --check`

Remaining blockers:

- derive the EW gauge group and Higgs carrier from framework-native inputs;
- derive `Y_H = 1/2`, the neutral vacuum, and the covariant derivative;
- keep numerical EW predictions downstream of running, matching, and pole-mass bridges.
