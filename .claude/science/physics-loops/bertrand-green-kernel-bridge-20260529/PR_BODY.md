## Summary

Repairs the Bertrand stable-orbit conditional row without narrowing to
only `d=3,4`.

The note now derives the all-`d>=3` continuum Green-kernel shape directly:

- `Delta_d r^(2-d)=0` away from the source;
- `G_d(r)=1/((d-2)S_{d-1}) r^(2-d)` has unit outward `-grad` flux;
- an attractive source gives `V(r)=-k/r^(d-2)` after absorbing the
  positive normalization into `k`;
- the effective-potential sign reduces to `k(d-2)(4-d)/r_c^d`.

This closes the audit blocker for the `d>=5` potential law without adding
an axiom or importing a textbook theorem as a black box.

## Checks

- `python3 -m py_compile scripts/bertrand_stable_orbit_green_kernel_bridge.py`
- `python3 scripts/bertrand_stable_orbit_green_kernel_bridge.py`
  - `SCORECARD: PASS=8  FAIL=0`
- `bash docs/audit/scripts/run_pipeline.sh`
  - target row reset to `unaudited`
  - queue ready: `true`
  - open dependency paths: `[]`
  - deps: `[]`

## Status

Branch-local status: bounded-support, re-audit ready.

This PR does not apply an audit verdict and does not claim effective
retained status. Independent audit remains required.
