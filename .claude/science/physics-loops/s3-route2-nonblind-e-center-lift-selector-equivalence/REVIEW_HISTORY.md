# Review History

Initial new-runner result:

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

Disposition before diff/overclaim gates: `local_gates_passed`.
