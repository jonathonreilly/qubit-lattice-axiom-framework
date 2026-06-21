# [physics-loop] s3-route2-color-ray-source-primitive block40 no-go

## Summary

This PR adds a current-bank no-go/support-boundary packet for the physical
color-ray/source-line primitive needed by the Route-2 adjoint-line complement
route.

It proves the conditional consequence: if a physical color ray is supplied,
`H_psi = |psi><psi| - I_3/3` selects one line in the adjoint `8`; the
orthogonal complement has normalized fraction `7/8`; and under the granted
T-side values this gives `q_E=15/8`, `rho_E=21/4`, and `c_TE=-8/9`.

It also proves the current-bank no-go: current orientation, depolarization,
Fierz, Z3, and Route-2 readout surfaces do not supply that physical ray or an
equivalent source-line primitive.

## Artifacts

- `docs/QUARK_ROUTE2_PHYSICAL_COLOR_RAY_SOURCE_PRIMITIVE_NO_GO_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.py`
- `outputs/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-color-ray-source-primitive/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-color-ray-source-primitive/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-color-ray-source-primitive/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.py` -> `PASS=26 FAIL=0`
- `python3 -m py_compile scripts/frontier_quark_route2_physical_color_ray_source_primitive_no_go_2026_06_21.py` -> pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py` -> `PASS=103 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py` -> `PASS=62 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py` -> `PASS=14 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_color_orientation_predictive_equivalence_2026_06_09.py` -> `PASS=19 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_matter_color_depolarization_adm2_necessary_2026_06_09.py` -> `PASS=18 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_ew_current_fierz_channel_decomposition.py` -> `PASS=31 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py` -> `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_fierz_singlet_selector_weight_not_partition_2026_06_08.py` -> `PASS=14 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_rconn_kappa_ew_register_not_read.py` -> `PASS=20 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_z3_character_isomorphism_color_generation.py` -> `PASS=22 FAIL=0`

## Boundary

This is not a parent-target completion PR. It does not derive the endpoint
triple on the actual current surface, assign a physical color orientation, rule
out future source primitives, derive non-top quark masses, apply audit verdicts,
or update main authority surfaces.

Next science action: pivot to a stronger Route-2 readout-map theorem that
evaluates the E-center column directly, unless a new same-surface source theorem
can derive a physical color-ray/source-line primitive.
