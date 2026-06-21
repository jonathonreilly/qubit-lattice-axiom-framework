# Summary

This physics-loop block identifies a precise same-domain primitive that would
produce the Route-2 inverse-square covariance law:

```text
D_X = A_X / w_X
q_X proportional to D_X^2
```

It gives the endpoint exactly:

```text
q_E/q_T = 9/4
q_E = 15/8
rho_E = 21/4
c_TE = -8/9
```

# Honest Status

- actual current-surface status: `conditional-support`
- trace class: `upstream_support`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim that the current surface already derives the primitive

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_TWO_POLE_DENSITY_COVARIANCE_PRIMITIVE_CANDIDATE_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-two-pole-density-covariance-primitive/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
git diff --cached --check
```

New runner result:

```text
PASS=18 FAIL=0 TOTAL=18
```

# Remaining Target

Derive the channel-density normalization and density-covariance readout from
current support/readout structure, or prove the current polynomial carrier
cannot supply those steps.
