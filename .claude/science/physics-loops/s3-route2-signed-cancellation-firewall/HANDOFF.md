# Handoff

## Block49 Summary

This block tests the signed affine one-pole escape:

```text
F_X = a / w_X + b.
```

The target equation forces `b=-6a/5`, so the exact fit exists but requires a
negative coefficient. Coefficient-positive affine rules cannot reach `9/4`;
pointwise positivity alone cannot derive or reject the signed fit.

Status: scoped `no-go` over coefficient-positive affine rules, with exact
conditional support if a typed signed selector and admissibility firewall are
later derived or admitted.

## Files

- `docs/QUARK_ROUTE2_SIGNED_CANCELLATION_FIREWALL_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py`
- `outputs/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-signed-cancellation-firewall/`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py`
  passed with `PASS=92 FAIL=0 TOTAL=92`.
- `python3 -m py_compile scripts/frontier_quark_route2_signed_cancellation_firewall_2026_06_21.py`
  passed.
- `PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py`
  passed with `TOTAL: PASS=8 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`
  passed with `TOTAL: PASS=14, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_channel_readout_naturality_no_go.py`
  passed with `TOTAL: PASS=28, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  passed with `PASS=11 FAIL=0`.
- `git diff --cached --check` passed.
- The staged overclaim scan passed.

## PR

Opened:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4579
```

Title:

```text
[physics-loop] s3-route2-signed-cancellation-firewall block49 no-go
```

Identity-only verification passed:

```json
{"baseRefName":"main","headRefName":"physics-loop/s3-route2-signed-cancellation-firewall-block49-20260621","number":4579,"state":"OPEN","title":"[physics-loop] s3-route2-signed-cancellation-firewall block49 no-go","url":"https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4579"}
```

No mergeability or conflict checks were run.

## Next Exact Science Action

After PR creation, define and test a larger nonlinear tensor-observable class
or pivot to a different direct consumer.
