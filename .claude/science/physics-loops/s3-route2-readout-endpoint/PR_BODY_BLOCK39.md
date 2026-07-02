# [physics-loop] s3-route2-readout-endpoint block39 conditional-support

## Summary

This PR adds a conditional-support/current-source-boundary packet for the
Route-2 endpoint import.

It proves a supplied physical color ray would select one adjoint line:

```text
psi -> H_psi = |psi><psi| - I_3/3
```

The orthogonal complement in the adjoint space has rank `7`, so its normalized
fraction is `7/8`. Reading that as the E-center excess gives
`q_E=15/8`, `rho_E=21/4`, and `c_TE=-8/9` under the granted T-side Route-2
values.

The current-source boundary is also explicit: current color/source surfaces do
not supply the physical color ray. Color orientation is gauge/predictively
vacuous, color depolarization erases the traceless mean, and Fierz/singlet
surfaces supply `1+8` channel algebra rather than one line inside the adjoint.

## Artifacts

- `docs/QUARK_ROUTE2_COLOR_RAY_ADJOINT_LINE_SELECTOR_BOUNDARY_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.py`
- `outputs/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.py` -> `PASS=15 FAIL=0`
- `python3 -m py_compile scripts/frontier_quark_route2_color_ray_adjoint_line_selector_boundary_2026_06_21.py` -> pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py` -> `PASS=103 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py` -> `PASS=62 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py` -> `PASS=18 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_color_orientation_predictive_equivalence_2026_06_09.py` -> `PASS=19 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/cl3_quark_antiquark_color_singlet_check.py` -> `PASS=7 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_ew_current_fierz_channel_decomposition.py` -> `PASS=31 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py` -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py` -> `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py` -> `PASS=64 FAIL=0`

## Boundary

This is not a parent-target completion PR. It does not derive the endpoint triple on the
actual current surface, assign a physical color orientation, derive non-top
quark masses, apply audit verdicts, or update main authority surfaces.

Next science action: derive or rule out a physical color-ray/source-line
primitive; otherwise pivot to a stronger readout-map theorem.
