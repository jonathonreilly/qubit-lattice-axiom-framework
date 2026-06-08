# Handoff

Target:
`i1_static_readout_is_native_field_integration_2026-06-06`.

Repair:
Added `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08`,
with a runner proving the finite-lattice complete-square identity and
two-source cross-term normalization:

```text
S_eff[J] = -(g^2/2) <J, L^+ J>
V_cross(r) = -g^2 s_1 s_2 G(r)
```

Verification:

```text
python3 scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py
TOTAL: PASS=18 FAIL=0

python3 scripts/i1_static_readout_is_native_field_integration_2026_06_06.py
TOTAL: PASS=10 FAIL=0

python3 scripts/cached_runner_output.py --check-only scripts/i1_native_quadratic_static_source_normalization_bridge_2026_06_08.py
python3 scripts/cached_runner_output.py --check-only scripts/i1_static_readout_is_native_field_integration_2026_06_06.py
```

Boundary:
No audit files are edited. This does not claim full I1 retained closure; the
general energy-readout bridge remains open.
