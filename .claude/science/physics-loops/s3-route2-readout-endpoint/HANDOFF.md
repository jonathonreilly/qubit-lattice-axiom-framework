# Handoff

## Block15 Summary

Branch: `physics-loop/s3-route2-readout-endpoint-block15-20260621`

This block adds a no-go for the pure `O_h` nonseparable quadratic primitive
route. Character arithmetic gives

```text
dim Hom_Oh(Sym^2(E (+) T1), E (+) T1) = 3,
```

with two independent `E`-output reduced coefficients and one `T1`-output
coefficient. A mixed `E tensor T1 -> T1` channel exists, but `O_h` does not
select the endpoint coefficient.

## Artifacts

- `docs/QUARK_ROUTE2_NONSEPARABLE_QUADRATIC_EQUIVARIANT_PRIMITIVE_NO_GO_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.py`
- `logs/runner-cache/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.txt`

## PR

PR #4544: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4544

Identity-only check:

```json
{"baseRefName":"main","headRefName":"physics-loop/s3-route2-readout-endpoint-block15-20260621","number":4544,"state":"OPEN","title":"[physics-loop] s3-route2-readout-endpoint block15 no-go","url":"https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4544"}
```

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.py`
  - `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py`
  - `PASS=7 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py`
  - `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_bilinear_tensor_primitive.py`
  - `PASS=4 FAIL=0`
- `python3 -m py_compile scripts/frontier_quark_route2_nonseparable_quadratic_equivariant_primitive_no_go_2026_06_21.py`
- `git diff --check`
- overclaim scan: only negative-boundary firewall hits such as "does not derive" / "does not propose endpoint closure".

## Remaining Blocker

The endpoint triple remains open. A successful positive route now needs a
coefficient-selection/normalization primitive that picks the correct point in
the three-dimensional equivariant quadratic map space, or a different
mechanism outside pure `O_h` representation content.

## Next Exact Action

Try the finite-frame/Riesz dual-leg route, with special attention to avoiding
the source/readout split gauge freedom. Fallback to a theta-to-slice
support/no-go packet if endpoint derivation remains hard-walled.
