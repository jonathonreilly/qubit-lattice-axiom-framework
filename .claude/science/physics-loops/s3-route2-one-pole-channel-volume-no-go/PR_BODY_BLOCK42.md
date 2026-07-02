# Summary

This physics-loop block prunes a same-domain origin class for the Route-2
inverse-square covariance primitive.

It proves that every positive channel-volume cone with at most one inverse
channel-volume normalization,

```text
q_X=sum_i a_i w_X^p_i, a_i>=0, p_i>=-1,
```

obeys

```text
q_E/q_T <= 3/2 < 9/4.
```

Therefore positive polynomial and one-pole source/readout rules cannot derive
`rho_E=21/4`.

# Honest Status

- actual current-surface status: `no-go`
- trace class: `negative_route_pruning`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim over all future nonlinear observables

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_ONE_POLE_CHANNEL_VOLUME_NO_GO_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-one-pole-channel-volume-no-go/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_one_pole_channel_volume_no_go_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
git diff --cached --check
```

New runner result:

```text
PASS=19 FAIL=0 TOTAL=19
```

# Remaining Target

Derive a genuine two-pole inverse-square channel primitive, derive and police
a signed-cancellation mechanism, or expand the no-go to a wider nonlinear
class.
