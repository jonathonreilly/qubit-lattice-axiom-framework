# Handoff

## Block107 Summary

Block107 proves an exact support theorem: if the direct Route-2 source row is
a scale-shift-invariant second variation in the physical positive weight
coordinate `w`, then its row degree is `d=-2`.

That gives:

```text
H(w_E)/H(w_T) = 9/4,
q_E = 15/8,
rho_E = 21/4,
c_TE = -8/9.
```

Derivative-order falsifiers show why the premise is load-bearing: first
variation gives degree `-1`, third variation gives degree `-3`, and fourth
variation gives degree `-4`.

## Claim Boundary

Actual status: exact-support/open boundary.

The current surface does not derive that the Route-2 source row is a
scale-shift-invariant second variation in `w`.

## Verification

- `git diff --check`
  -> pass
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.py`
  -> `TOTAL: PASS=45, FAIL=0`
- Output agreement against `outputs/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.txt`
  -> `output_matches`
- `python3 -m py_compile scripts/frontier_quark_route2_log_weight_second_variation_row_boundary_2026_06_22.py`
  -> pass
- Block106 source-row selector no-go runner
  -> `TOTAL: PASS=42, FAIL=0`
- Block105 direct row-degree runner
  -> `TOTAL: PASS=37, FAIL=0`
- Ray-quotient Hessian no-scale runner
  -> `TOTAL: PASS=38, FAIL=0`
- Block104 power-law coordinate bridge runner
  -> `TOTAL: PASS=37, FAIL=0`
- S3 theta-to-slice runner
  -> `PASS=12 FAIL=0`
- Exact readout map runner
  -> `PASS=11 FAIL=0`
- Overclaim scan for retained/audit-status wording
  -> only runner forbidden-word guard strings matched

## Branch-Local Review

Disposition: pass.

Audit pipeline must not be run, and no audit verdict should be applied.

## PR

Pending.

## Next Exact Action

Derive the physical source/readout theorem that makes the Route-2 row a
scale-shift-invariant second variation in the positive weight coordinate.
