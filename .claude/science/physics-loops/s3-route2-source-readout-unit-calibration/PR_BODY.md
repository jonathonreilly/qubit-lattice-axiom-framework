# Summary

Block126 prunes Block121 equal internal source-unit weights as a proof of the
physical source-to-readout calibration `mu=1` required by Block123 C4.

The same internal source jet and orientation sign permit an endpoint-free
family `c_TE(mu) = -mu * (8/9)`. The current surface still needs a Route-2
source-readout unit calibration theorem.

This is not an audit verdict. No audit worker was run and no audit verdict was
applied.

## Trace

```yaml
trace_class: negative_route_pruning
reachability_to_target: prunes
artifact_role: no_go
```

## Files

- `docs/QUARK_ROUTE2_SOURCE_READOUT_UNIT_CALIBRATION_NO_GO_2026-06-22.md`
- `scripts/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.py`
- `outputs/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.txt`
- `.claude/science/physics-loops/s3-route2-source-readout-unit-calibration/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/s3-route2-source-readout-unit-calibration/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-source-readout-unit-calibration/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-source-readout-unit-calibration/REVIEW_HISTORY.md`
- `.claude/science/physics-loops/s3-route2-source-readout-unit-calibration/STATE.yaml`

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_readout_unit_calibration_no_go_2026_06_22.py
TOTAL: PASS=55, FAIL=0

Adjacent guards:
- minimal_multirecord_extension_support: TOTAL: PASS=62, FAIL=0
- minimal_extension_readout_coupling_no_go: TOTAL: PASS=75, FAIL=0
- minimal_readout_coupling_contract_support: TOTAL: PASS=70, FAIL=0
- hessian_et_coefficient_normalization_no_go: TOTAL: PASS=49, FAIL=0

git diff --check: PASS
STATE.yaml parse: PASS
ASCII scan: PASS
overclaim marker scan: PASS
```

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4713
Number: 4713
Title: [physics-loop] s3-route2 source readout unit calibration block126 no-go
State: OPEN
Base: physics-loop/s3-route2-source-hessian-channel-coupling-block125-20260622
Head: physics-loop/s3-route2-source-readout-unit-calibration-block126-20260622
Science commit: 00be8d4a2
```
