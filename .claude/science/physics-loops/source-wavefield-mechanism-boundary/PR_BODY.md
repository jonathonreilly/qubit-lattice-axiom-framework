## Summary

This PR repairs the source-resolved wavefield mechanism surface so it is
reviewable as bounded support rather than closure language.

Changes:

- demotes `SOURCE_RESOLVED_WAVEFIELD_MECHANISM_NOTE.md` to a bounded
  depth-mechanism probe;
- replaces absolute local artifact links with repo-relative runner/cache links;
- names the finite-speed update rule and selected parameter envelope as open
  imports;
- updates runner output wording and refreshes the runner cache;
- adds a branch-local physics-loop pack with claim-status, trace, and handoff
  notes.

## Claim Boundary

The source-depth phase-ramp evidence is preserved. The PR does not claim a
framework-native derivation of the finite-speed wavefield rule, continuum
theorem status, absolute experimental transfer, or detector calibration.

## Verification

- `python3 scripts/cached_runner_output.py scripts/source_resolved_wavefield_mechanism.py --refresh --timeout-sec 1800`
- `python3 scripts/cached_runner_output.py scripts/source_resolved_wavefield_mechanism.py --check-only`
- `python3 -m py_compile scripts/source_resolved_wavefield_mechanism.py`
- `git diff --check`
- source-side diff guard for audit/publication/front-door files

## Reviewer Notes

Review-loop was not run here; disposition is `reviewer_owned_not_run`.
