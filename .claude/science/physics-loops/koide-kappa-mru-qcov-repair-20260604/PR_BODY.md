## Summary

Repairs the live conditional kappa factorization row by addressing both
named source blockers:

- adds `KOIDE_MOMENT_RATIO_UNIFORMITY_THEOREM_NOTE_2026-04-19.md` as a
  real one-hop retained-bounded dependency;
- repairs the Koide `Q` / `CoV` ratio convention;
- updates the runner to verify MRU packet presence and convention
  algebra;
- refreshes the runner cache to `PASS=31 FAIL=0`.

## Claim Status

`proposed_promoted` source repair only. Independent audit remains the
status authority. This PR does not touch `docs/audit/**`.

## Scope Firewall

The MRU dependency is used only as formal reduced two-slot support. The
physical SO(2) quotient/readout and operator-side charged-lepton closure
remain outside this PR.

## Verification

```bash
python3 -m py_compile scripts/frontier_koide_kappa_two_orbit_dimension_factorization.py
PYTHONPATH=scripts python3 scripts/frontier_koide_kappa_two_orbit_dimension_factorization.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_koide_kappa_two_orbit_dimension_factorization.py
git diff --check
git diff --name-only | rg '^docs/audit/' || true
```
