## Summary

Block101 prunes the shortcut that exact `P_R` endpoint slots determine the
Route-2 Pcal moment realization and one-point product registry.

Even granting a raw second moment, finite record models with the same raw
moment can have different one-point products and therefore different connected
`kappa` values. The desired `m=1/3` product is a theorem to prove, not a
consequence of the raw slot alone.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 Pcal moment-realization theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py
     TOTAL: PASS=75, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py
     TOTAL: PASS=72, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py
     TOTAL: PASS=63, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
     PASS=11 FAIL=0
PASS python3 scripts/frontier_source_measure_pcal_cumulant_mobius.py
     SUMMARY: PASS=33 FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block100 and does not push to main.

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4688
Number: 4688
Title: [physics-loop] s3-route2 pcal moment realization block101 no-go
State: OPEN
Base: physics-loop/s3-route2-source-measure-product-registry-block100-20260622
Head: physics-loop/s3-route2-pcal-moment-realization-block101-20260622
Science commit: a6f0c9001
```
