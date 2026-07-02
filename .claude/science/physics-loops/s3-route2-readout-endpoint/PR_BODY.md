## Summary

Adds block17 for the S3/Route-2 readout endpoint campaign: a finite-frame/Riesz
dual-leg count boundary for the residual

```text
rho_E = beta_E / alpha_E = 21/4
```

under the granted T-side endpoint algebra.

The exact six-arm `O_h` frame calculation shows:

- unnormalized projected-arm frames are Parseval and give `lambda=1`;
- one unit-frame analysis leg gives `lambda=3/2`;
- two reciprocal unit-frame analysis legs give `lambda=9/4`, hence
  conditionally `rho_E=21/4`;
- canonical Riesz reconstruction cancels the frame bound;
- the exact reduced readout map sees only the product `lambda`, not a derived
  source/readout split or `leg_count=2`.

Honest status: `conditional-support` plus no-go boundary. This PR does not
audit, apply verdicts, push to main, or claim the endpoint is closed.

## Artifacts

- `docs/QUARK_ROUTE2_FINITE_FRAME_DUAL_LEG_COUNT_BOUNDARY_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py`
- `logs/runner-cache/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py`
  - `PASS=9 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py`
  - `PASS=7 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py`
  - `PASS=46 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py`
  - `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  - `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_bilinear_tensor_primitive.py`
  - `PASS=4 FAIL=0`
- `python3 -m py_compile scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py`
- `git diff --check`
- overclaim wording scan

## Review Notes

No PR conflict or mergeability check was run. Existing physics-loop PRs are not
refreshed to main; the reviewer owns cherry-picking the science.
