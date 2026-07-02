# Handoff

## Block17 Summary

Branch: `physics-loop/s3-route2-readout-endpoint-block17-20260621`

This block adds a finite-frame/Riesz dual-leg count boundary for the Route-2
readout endpoint residual.

The exact six-arm `O_h` frame facts are:

```text
w_E = 1/3,
w_T = 1/2.
```

Unnormalized projected-arm frames are Parseval and give no factor. Unit-frame
analysis gives one reciprocal factor `3/2`. Two independent unit-frame
analysis legs give `9/4`, which conditionally reproduces

```text
rho_E = 21/4
```

under the granted T-side algebra. Canonical Riesz reconstruction cancels the
frame bound, and the exact readout map sees only the product factor, not a
derived source/readout split.

## Artifacts

- `docs/QUARK_ROUTE2_FINITE_FRAME_DUAL_LEG_COUNT_BOUNDARY_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.py`
- `logs/runner-cache/frontier_quark_route2_finite_frame_dual_leg_count_boundary_2026_06_21.txt`

## PR

PR #4546: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4546

Identity-only check:

```json
{"baseRefName":"main","headRefName":"physics-loop/s3-route2-readout-endpoint-block17-20260621","number":4546,"state":"OPEN","title":"[physics-loop] s3-route2-readout-endpoint block17 conditional-support","url":"https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4546"}
```

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
- overclaim scan: pass.

## Remaining Blocker

The endpoint triple remains open. A unique theta-to-slice theorem using the
E-center still requires an upstream theorem selecting `rho_E=21/4`.

After block17, the most direct remaining target is not more finite-frame
normalization restatement. It is the coefficient-selection principle: a
variational, boundary, source-domain, Ward-like, or normalization theorem that
selects `lambda=9/4` without importing the target.

## Next Exact Action

Create block18 for the coefficient-selection principle.
