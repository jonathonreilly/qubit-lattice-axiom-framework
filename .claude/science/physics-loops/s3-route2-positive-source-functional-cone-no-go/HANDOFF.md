# Handoff

## Block47 Summary

This block proves a scoped positive-cone no-go:

```text
finite positive channel-local source/readout functionals
with net channel-weight exponent p >= -1
```

cannot reach the Route-2 endpoint covariance `q_E/q_T=9/4`. The exact bound is
`lambda <= 3/2`, giving at most `q_E=5/4`, `rho_E=3/2`, and `c_TE=-4/3`.

Status: scoped `no-go`.

Open escapes:

- explicit `p=-2` density-square primitive;
- signed source/readout cancellation;
- future nonlinear observable outside this exponent-cone class.

## Files

- `docs/QUARK_ROUTE2_POSITIVE_SOURCE_FUNCTIONAL_CONE_NO_GO_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py`
- `outputs/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-positive-source-functional-cone-no-go/`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py`
  passed with `PASS=30 FAIL=0 TOTAL=30`.
- `python3 -m py_compile scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py`
  passed.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  passed with `PASS=11 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py`
  passed with `TOTAL: PASS=47, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py`
  passed with `TOTAL: PASS=14, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  passed with `PASS=11 FAIL=0`.
- `git diff --cached --check` passed.
- The staged overclaim scan passed.

## PR

Opened:

```text
https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4577
```

Title:

```text
[physics-loop] s3-route2-positive-source-functional block47 no-go
```

Identity-only verification passed:

```json
{"baseRefName":"main","headRefName":"physics-loop/s3-route2-positive-source-functional-no-go-block47-20260621","number":4577,"state":"OPEN","title":"[physics-loop] s3-route2-positive-source-functional block47 no-go","url":"https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4577"}
```

No mergeability or conflict checks were run.

## Next Exact Science Action

After PR creation, try to construct a concrete `p=-2` density-square primitive,
or search signed source/readout cancellation rules with a positivity firewall.
