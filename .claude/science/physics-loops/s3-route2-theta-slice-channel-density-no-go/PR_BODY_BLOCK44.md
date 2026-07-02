# Summary

This physics-loop block directly attacks the named theta-to-slice route.

It proves that the exact rank-one coupling family

```text
Xi_P(t;c) = (P_R c) tensor V_R(t)
```

preserves source-side readout ratios. Therefore the exact slice semigroup
cannot generate the missing channel-density normalization or inverse-square
covariance primitive needed for `rho_E=21/4`.

# Honest Status

- actual current-surface status: `no-go`
- trace class: `negative_route_pruning`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim over source/readout primitives generally

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_THETA_SLICE_CHANNEL_DENSITY_NO_GO_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-theta-slice-channel-density-no-go/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_theta_slice_channel_density_no_go_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
git diff --cached --check
```

New runner result:

```text
PASS=16 FAIL=0 TOTAL=16
```

# Remaining Target

Derive channel-density normalization on the source/readout side, or prove
that the current polynomial carrier cannot supply it.
