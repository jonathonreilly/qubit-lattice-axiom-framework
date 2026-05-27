# Handoff

## Summary

This branch repairs the Bertrand stable-orbit row by deriving the continuum
`d`-dimensional radial potential law and adding an exact-symbolic runner for
the stability calculation.

## Verification

- `python3 scripts/frontier_bertrand_stable_orbit_upper_bound_repair.py`
  - `SUMMARY: PASS=12 FAIL=0`
- `python3 scripts/vocab_lint.py --report-only docs/BERTRAND_STABLE_ORBIT_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md`
  - clean
- `docs/audit/scripts/run_pipeline.sh`
  - complete
- `git diff --check`
  - clean

## Pipeline Result

- Target row: `unaudited`, `bounded_theorem`, ready for audit.
- Runner: `scripts/frontier_bertrand_stable_orbit_upper_bound_repair.py`.
- Direct dependency remains `dimensional_gravity_table`; the repaired note
  states that dependency is context, not the source of the `d >= 5` continuum
  law.

## Residuals

- No framework-native universal dimensional-gravity law is claimed.
- Full Bertrand closed-orbit theorem remains an external classical-mechanics
  result.
