# Handoff

## Block41 Summary

This branch packages a Route-2 same-domain covariance target:

```text
q_X proportional to w_X^-2.
```

The runner proves the exact conditional endpoint chain:

```text
w_E=1/3, w_T=1/2, kappa=3/2
q_E/q_T=(w_T/w_E)^2=9/4
q_E=15/8
rho_E=21/4
c_TE=-8/9
```

It also proves uniqueness inside power-law channel rules:

```text
q_X proportional to w_X^p reaches q_E/q_T=9/4 exactly at p=-2.
```

The current surface does not derive the inverse-square primitive. The branch
therefore has status `conditional-support` and trace class `upstream_support`.

## Files

- `docs/QUARK_ROUTE2_INVERSE_SQUARE_COVARIANCE_PRIMITIVE_CANDIDATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py`
- `outputs/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-inverse-square-covariance-primitive/`

## Verification

Completed before commit:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_inverse_square_covariance_primitive_candidate_2026_06_21.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
```

Results:

- new runner: `PASS=23 FAIL=0 TOTAL=23`
- py_compile: pass
- parent checks: pass as recorded in `STATE.yaml`

Branch-local gates:

- staged `git diff --check`: pass
- overclaim scan: pass, no banned status wording matched
- PR creation: pass

## PR

- PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4571
- Number: 4571
- State: open
- Base: `main`
- Head: `physics-loop/s3-route2-inverse-square-covariance-primitive-block41-20260621`

Title:

```text
[physics-loop] s3-route2-inverse-square-covariance-primitive block41 conditional-support
```

Identity-only `gh pr view` passed for number, URL, title, head, base, and
state. No conflict or mergeability check was run.

## Next Exact Science Action

Start a new block that tries to derive the inverse-square covariance primitive
from a concrete same-domain nonlinear tensor/source/readout construction.
If that hits a hard wall, package a larger-class no-go that says exactly which
nonlinear functional family cannot produce `q_X proportional to w_X^-2`
without adding a new source measure or normalization primitive.
