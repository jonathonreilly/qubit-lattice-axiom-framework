# Summary

This physics-loop block tests the direct `p=-2` density-square primitive for
the Route-2 endpoint. Exact arithmetic shows that if a source/readout primitive
supplies

```text
q_X proportional to w_X^-2
```

then `q_E/q_T=9/4`, `q_E=15/8`, `rho_E=21/4`, and `c_TE=-8/9` follow exactly.
The current named Route-2 authority bank does not supply that typed primitive.

# Honest Status

- actual current-surface status: `no-go`
- conditional status if primitive is derived/admitted: exact support
- trace class: `negative_route_pruning`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim over arbitrary future nonlinear observables

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_DENSITY_SQUARE_PRIMITIVE_GAP_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_density_square_primitive_gap_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_density_square_primitive_gap_2026_06_21.txt`
- Parent verifier repair:
  `scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-density-square-primitive-gap/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_density_square_primitive_gap_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_density_square_primitive_gap_2026_06_21.py scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py
PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
git diff --cached --check
```

Results:

- new runner: `PASS=43 FAIL=0 TOTAL=43`
- `py_compile`: pass
- covariance Schur parent: `PASS=11 FAIL=0`
- s3-time primitive bridge assessment: `TOTAL: PASS=14, FAIL=0`
- exact readout parent: `PASS=11 FAIL=0`
- factor-rigidity parent: `PASS=64 FAIL=0`
- s3 primitive-chain reaudit: `TOTAL: PASS=24, FAIL=0`
- E-center lift attempt parent: `TOTAL: PASS=46, FAIL=0`
- E-center blindness parent: `TOTAL: PASS=14, FAIL=0`
- staged diff check: pass
- overclaim scan: pass

The bridge-assessment verifier needed a narrow tolerance repair for a
current-main `1.06 * EXACT_TOL` floating replay difference in the T-balance
cross-check. No audit verdicts were run or applied. No mergeability or conflict
checks are part of this physics-loop PR.

# Remaining Target

Try signed source/readout cancellation with a positivity firewall, then a
larger nonlinear tensor-observable class if the signed route remains blocked.
