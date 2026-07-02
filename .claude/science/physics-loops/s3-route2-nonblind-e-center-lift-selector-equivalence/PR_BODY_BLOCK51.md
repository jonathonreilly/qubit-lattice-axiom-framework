# [physics-loop] s3-route2-nonblind-e-center-lift block51 exact-support

## Summary

This PR adds an exact-support packet for the nonblind E-center lift target.
It proves the selector equivalences:

```text
rho_E=21/4 <=> q_E=15/8 <=> q_E/q_T=9/4 <=> center T/E=-8/9
```

and verifies that a typed `center T/E=-R_conn` bridge at `N_c=3` would force
the endpoint. It does not derive the selector or typed bridge.

## Trace

- Trace class: `upstream_support`
- Reachability: `supports`
- Parent gate remains blocked until a selector equation or typed bridge is
  actually derived.

## Artifacts

- `docs/QUARK_ROUTE2_NONBLIND_E_CENTER_LIFT_SELECTOR_EQUIVALENCE_EXACT_SUPPORT_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.py`
- `outputs/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-nonblind-e-center-lift-selector-equivalence/HANDOFF.md`

## Verification

Initial runner:

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.py
TOTAL: PASS=23, FAIL=0
```

Parent/local checks:

```text
python3 -m py_compile scripts/frontier_quark_route2_nonblind_e_center_lift_selector_equivalence_2026_06_21.py
ok

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py
TOTAL: PASS=46, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
TOTAL: PASS=103, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_box_size_scan_2026_06_10.py
TOTAL: PASS=7, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
TOTAL: PASS=14, FAIL=0
```

No audit verdict is applied. No main push. No PR conflict or mergeability
check.
