# [physics-loop] s3-route2-readout-endpoint block21 exact-support

## Summary

Adds a direct-consumer E-center dependency classifier for the current
S3/Route-2 readout/time surfaces.

Main result:

```text
(P(rho_b) - P(rho_a)) c = ((rho_b - rho_a) delta_E, 0)
```

So direct consumers are safe exactly when they avoid the E-center `delta_E`
direction. Time-channel and carrier-definition consumers can move forward;
unique readout, E-center endpoint, center-ratio, physical eta-floor, and final
Einstein/Regge consumers remain dependent on a separate E-center/source/readout
rule.

## Files

- `docs/S3_TIME_DIRECT_CONSUMER_ECENTER_DEPENDENCY_CLASSIFICATION_NOTE_2026-06-21.md`
- `scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py`
- `outputs/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py
TOTAL: PASS=29, FAIL=0
```

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
TOTAL: PASS=14, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py
TOTAL: PASS=24, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py
PASS=8 FAIL=0

python3 -m py_compile scripts/frontier_s3_time_direct_consumer_ecenter_dependency_classification_2026_06_21.py
pass

git diff --check
pass

branch-local wording scan
pass
```

## Boundary

This PR is exact support and dependency hygiene. It does not select `rho_E`,
does not supply a physical readout primitive, and does not change parent row
authority status.
