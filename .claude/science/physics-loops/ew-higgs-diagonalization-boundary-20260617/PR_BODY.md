## Summary

This PR repairs the EW Higgs gauge-mass diagonalization row by making its
claim boundary explicit.

Changes:

- replaces stale closure-status wording with bounded support over
  declared EW-Higgs inputs;
- names the electroweak gauge group, one Higgs doublet, `Y_H = 1/2`,
  neutral vacuum, covariant derivative, and GUT-normalization convention as
  boundary inputs;
- preserves the exact symbolic mass/charge/rho algebra;
- updates the runner to verify the bounded boundary and return
  `VERDICT: BOUNDED_SUPPORT`;
- refreshes the runner cache and adds a branch-local physics-loop pack.

## Claim Boundary

This PR does not derive the EW gauge group, Higgs carrier, hypercharge,
vacuum, or covariant derivative from the minimal framework. It also does not
derive pole masses, loop corrections, RGE running, threshold matching, or
precision numerical predictions.

## Verification

- `python3 scripts/frontier_ew_higgs_gauge_mass_diagonalization.py`
- `python3 scripts/cached_runner_output.py scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --refresh`
- `python3 scripts/cached_runner_output.py scripts/frontier_ew_higgs_gauge_mass_diagonalization.py --check-only`
- `python3 -m py_compile scripts/frontier_ew_higgs_gauge_mass_diagonalization.py`
- `git diff --check`
- source-side diff guard for audit/publication/front-door files

## Reviewer Notes

Review-loop was not run here; disposition is `reviewer_owned_not_run`.
