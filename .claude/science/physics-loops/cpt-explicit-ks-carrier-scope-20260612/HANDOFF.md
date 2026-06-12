# Handoff

## What Changed

This branch repairs the CPT row by making the load-bearing theorem an explicit finite KS matrix theorem. The staggered realization gate is still named, but only as non-load-bearing downstream framework-identification context.

The runner now checks the source boundary directly:

- explicit-carrier rescope is present;
- the finite-matrix theorem is over the explicit KS carrier family;
- the realization gate is non-load-bearing context;
- there is no markdown dependency edge to `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`.

## Verification

- `PYTHONPATH=scripts python3 scripts/axiom_first_cpt_check.py`
  - `TOTAL: PASS=118 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/axiom_first_cpt_check.py --force --concurrency 1 --push-mode none --allow-non-main`
  - `ok 1`, `nonzero_exit 0`
- `git diff --check`
  - clean

## Remaining Boundaries

- This does not derive the KS carrier from the framework.
- This does not close the full staggered realization gate.
- This does not close the SU(3) Wilson-plaquette CPT lift.
- This does not bridge CP-odd observables to `Theta_CPT`-odd observables.

