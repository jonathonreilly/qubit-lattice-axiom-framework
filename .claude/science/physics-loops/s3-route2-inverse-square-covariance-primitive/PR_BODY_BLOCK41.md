# Summary

This physics-loop block packages the exact same-domain inverse-square
covariance primitive needed by the S3/Route-2 endpoint triple:

```text
q_X proportional to w_X^-2
```

It proves that, if this primitive is supplied, the Route-2 endpoint arithmetic
is exact:

```text
q_E/q_T = 9/4
q_E = 15/8
rho_E = 21/4
c_TE = -8/9
```

It also proves uniqueness inside power-law channel rules: `p=-2` is the only
integer and real power-law exponent giving `q_E/q_T=9/4`.

# Honest Status

- actual current-surface status: `conditional-support`
- trace class: `upstream_support`
- no audit verdicts applied
- no repo-wide authority surfaces edited
- no claim that the current source/readout surface already derives the
  inverse-square primitive

# Artifacts

- Note:
  `docs/QUARK_ROUTE2_INVERSE_SQUARE_COVARIANCE_PRIMITIVE_CANDIDATE_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py`
- Output:
  `outputs/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-inverse-square-covariance-primitive/`

# Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
git diff --cached --check
```

New runner result:

```text
PASS=23 FAIL=0 TOTAL=23
```

# Remaining Blocker

Derive `q_X proportional to w_X^-2` from a named current-surface
source/readout construction, or prove a larger-class no-go that rules out that
primitive without adding a new source measure or normalization rule.
