# Handoff

## Summary

This branch registers the Koide Z3 scalar-potential runner and removes its
SciPy compute blocker by replacing:

- `scipy.linalg.expm` with a Hermitian eigenvalue exponential;
- `scipy.optimize.brentq` with bracketed bisection;
- the imported SciPy-backed H_* helper with a local golden-section scan using
  the same retained constants.

The claim remains exact support only. The runner still records that the
Clifford-fixed `V_eff` minimum is not the physical selected point and that an
additional microscopic selector/scale theorem is needed for charged-lepton
tower closure.

## Verification

```bash
python3 scripts/frontier_koide_z3_scalar_potential.py
python3 scripts/cached_runner_output.py scripts/frontier_koide_z3_scalar_potential.py --refresh
python3 scripts/cached_runner_output.py scripts/frontier_koide_z3_scalar_potential.py --check-only
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_z3_scalar_potential.py --check-only
PYTHONDONTWRITEBYTECODE=1 python3 -m py_compile scripts/frontier_koide_z3_scalar_potential.py scripts/cached_runner_output.py docs/audit/scripts/build_citation_graph.py
```

## Reviewer Notes

No audit results, ledger rows, generated publication status files, or lane
registry/front-door surfaces are edited. Independent audit remains required.
