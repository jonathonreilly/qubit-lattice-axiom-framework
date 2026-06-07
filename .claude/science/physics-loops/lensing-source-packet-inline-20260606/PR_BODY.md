# Summary

Repairs the active `lensing_finite_path_explanation_note` restricted-packet blocker by inlining long-path source/cache checks into the primary finite-path runner.

The latest audit asked for `scripts/lensing_long_path_test.py` and its fresh runner cache/output so the `T_phys=7.5` measured slope `-1.4356` and finite-path prediction `-1.7336` can be verified inside the restricted packet. The primary runner now verifies those artifacts directly and reports `INLINE SOURCE PACKET: PASS=31 FAIL=0`.

# Scope

This is exact support for a packet-completeness blocker. It does not retag the audit ledger, does not close the layer-weighted detector-centroid derivation, and does not claim standard `1/b` lensing closure.

# Verification

```bash
python3 -m py_compile scripts/lensing_analytical_finite_path.py scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/lensing_analytical_finite_path.py
PYTHONPATH=scripts python3 scripts/cached_runner_output.py --check-only scripts/lensing_finite_path_centroid_packet_manifest_2026_06_04.py
git diff --check
```
