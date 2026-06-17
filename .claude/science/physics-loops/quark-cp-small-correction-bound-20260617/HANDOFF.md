# Handoff

## What Changed

This block adds a source-side boundary for the quark CP carrier completion's
small-correction residual.

- Exact fitted-ratio check: current `xi_u` is `101.908728437` Schur-base units;
  current `xi_d` is `6.643337509` Schur-base units.
- Bounded capped scan: common caps `R <= 5` fail to recover the parent
  Jarlskog target on the parent mass-ratio slice.
- Parent note now points to this boundary and frames the current completion as
  non-perturbative bounded ansatz, not small correction.

## What Did Not Change

- No audit ledger/status/generated files were edited.
- No claim is promoted.
- `xi_u`, `xi_d`, comparator targets, and non-perturbative carrier
  normalization are still open.
- Existing PRs were not rebased or refreshed against main.

## Reviewer Focus

Check that the note does not overclaim the bounded scan as a global no-go and
that the parent-note wording preserves the bounded numerical-match status.

## Verification

- `python3 scripts/frontier_quark_cp_small_correction_boundary.py`: `PASS=9 FAIL=0`
- `python3 scripts/frontier_quark_cp_carrier_completion.py`: `PASS=11 FAIL=0`
- `python3 scripts/cached_runner_output.py scripts/frontier_quark_cp_small_correction_boundary.py --check-only`: fresh
- `python3 -m py_compile scripts/frontier_quark_cp_small_correction_boundary.py scripts/frontier_quark_cp_carrier_completion.py`: pass
- `git diff --check`: pass
- forbidden generated/status diff scan: empty

## Next Action

After review, the next high-value science target is either the framework-native
non-perturbative carrier-normalization derivation or the comparator/readout
bridge.
