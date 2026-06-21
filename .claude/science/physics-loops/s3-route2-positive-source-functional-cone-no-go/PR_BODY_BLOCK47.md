# Summary

This physics-loop block proves a scoped positive-cone no-go for the Route-2
endpoint:

```text
finite positive channel-local source/readout functionals
with net channel-weight exponent p >= -1
```

cannot reach the needed covariance `q_E/q_T=9/4`. The exact upper bound is
`3/2`, which gives only `q_E=5/4`, `rho_E=3/2`, and `c_TE=-4/3`.

# Honest Status

- actual current-surface status: `no-go`
- trace class: `negative_route_pruning`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim over arbitrary future nonlinear observables

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_POSITIVE_SOURCE_FUNCTIONAL_CONE_NO_GO_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-positive-source-functional-cone-no-go/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_positive_source_functional_cone_no_go_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
git diff --cached --check
```

Results:

- new runner: `PASS=30 FAIL=0 TOTAL=30`
- `py_compile`: pass
- covariance Schur parent: `PASS=11 FAIL=0`
- structural narrowing parent: `TOTAL: PASS=47, FAIL=0`
- E-center blindness parent: `TOTAL: PASS=14, FAIL=0`
- exact readout parent: `PASS=11 FAIL=0`
- staged diff check: pass
- overclaim scan: pass

No audit verdicts were run or applied. No mergeability or conflict checks are
part of this physics-loop PR.

# Remaining Target

Construct a concrete `p=-2` density-square primitive, search signed
source/readout cancellation rules, or define a larger nonlinear tensor
observable class for the next no-go/support packet.
