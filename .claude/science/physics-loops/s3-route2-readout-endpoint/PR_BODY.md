## Summary

Adds block18 for the S3/Route-2 readout endpoint campaign: a
coefficient-selection boundary on the reduced positive E-row family

```text
ell_E ~ (1, rho_E), rho_E > -6.
```

The exact checks show:

- positivity and E-center-blind data leave `rho_E` free;
- ordinary target-free selectors pick `rho_E=-1`, `0`, or `3/2`, or leave the
  slope free;
- a quadratic variational selector lands on `rho_E=21/4` only by importing the
  target-equivalent coefficient ratio `B/A=-15/4`;
- inverse-square projector weighting lands exactly, but selecting that rule or
  exponent `n=2` remains the missing theorem content.

Honest status: `no-go` for target-free coefficient-selection routes. This PR
does not audit, apply verdicts, push to main, or claim the endpoint is closed.

## Artifacts

- `docs/QUARK_ROUTE2_COEFFICIENT_SELECTION_BOUNDARY_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.py`
- `logs/runner-cache/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.py`
  - `PASS=9 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py`
  - `PASS=47 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`
  - `PASS=14 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py`
  - `PASS=7 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  - `PASS=12 FAIL=0`
- `python3 -m py_compile scripts/frontier_quark_route2_coefficient_selection_boundary_2026_06_21.py`
- `git diff --check`
- overclaim wording scan

## Review Notes

No PR conflict or mergeability check will be run. Existing physics-loop PRs are
not refreshed to main; the reviewer owns cherry-picking the science.
