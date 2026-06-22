## Summary

Block87 prunes the next Route-2 color-coupling attempt: keep the physical
`P_R/E-T` output as a pair of color-invariant scalars, but let it depend on the
same color source.

That still does not supply the bridge. The differential of such a readout is a
map `sl_3 -> C^2` whose components are SU(3)-invariant linear forms, and
`Hom_SU3(sl_3, C^2) = 0`. Higher scalar invariants also have zero first
derivative at `I_3/3` on traceless perturbations.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 covariant color-readout family or orientation-free multi-record
connected-cumulant source/readout theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.py
     TOTAL: PASS=50, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_factorized_color_source_extension_no_go_2026_06_22.py
     TOTAL: PASS=44, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_scalar_extension_adjoint_source_no_go_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_same_source_color_readout_primitive_obstruction_2026_06_22.py
     TOTAL: PASS=68, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_color_source_transfer_no_go_2026_06_22.py
     TOTAL: PASS=51, FAIL=0
PASS git diff --check
PASS STATE.yaml parse
PASS ASCII scan
PASS overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block86 and does not push to main.

## PR Identity

```text
PENDING
```
