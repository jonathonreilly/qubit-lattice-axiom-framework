# Handoff

## Summary

This PR repairs the DM leptogenesis expansion-boundary row by replacing
hard-coded boundary-collapse checks with direct computation of `eta[H]` from
a supplied normalized expansion profile.

## Claim Movement

- Before: runner asserted the decisive "given Hrad, eta is fixed" checks with
  `True`.
- After: runner computes `eta[H]` through the exact package and
  `solve_normalized_transport`, verifies repeatability for the same profile,
  and verifies sensitivity to a different normalized profile.
- Remaining: upstream transport/Hrad theorem rows still need audit; no
  observed `eta` match or DM flagship closure is claimed.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_dm_leptogenesis_expansion_axiom_boundary.py`
- `python3 scripts/vocab_lint.py --report-only docs/DM_LEPTOGENESIS_EXPANSION_AXIOM_BOUNDARY_NOTE_2026-04-16.md`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

## Next Action

Open as a draft PR. If review accepts the runner repair, the independent audit
lane can re-audit the row and any cascade can wait on upstream transport/Hrad
audits.
