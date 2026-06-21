# Handoff

## Block43 Summary

This block identifies a precise positive primitive for the Route-2
inverse-square rule:

```text
D_X = A_X / w_X
q_X proportional to D_X^2.
```

It gives

```text
q_E/q_T = 9/4
q_E = 15/8
rho_E = 21/4
c_TE = -8/9.
```

Status is `conditional-support`: the current surface does not derive the
channel-density normalization plus density-covariance readout primitive.

## Files

- `docs/QUARK_ROUTE2_TWO_POLE_DENSITY_COVARIANCE_PRIMITIVE_CANDIDATE_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py`
- `outputs/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-two-pole-density-covariance-primitive/`

## Verification

Completed:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py
python3 -m py_compile scripts/frontier_quark_route2_two_pole_density_covariance_candidate_2026_06_21.py
```

Results:

- new runner: `PASS=18 FAIL=0 TOTAL=18`
- py_compile: pass

Parent checks:

- `frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py`: `PASS=11 FAIL=0`
- `frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py`: `PASS=7 FAIL=0`
- `frontier_quark_route2_exact_readout_map.py`: `PASS=11 FAIL=0`
- `frontier_quark_route2_e_center_blindness_no_go.py`: `PASS=14 FAIL=0`
- `frontier_quark_route2_source_domain_bridge_no_go.py`: `PASS=103 FAIL=0`

Branch-local gates:

- staged `git diff --check`: pass
- overclaim scan: pass, no banned status wording matched
- PR creation: pass

## PR

- PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4573
- Number: 4573
- State: open
- Base: `main`
- Head: `physics-loop/s3-route2-two-pole-density-covariance-block43-20260621`

Title:

```text
[physics-loop] s3-route2-two-pole-density-covariance block43 conditional-support
```

Identity-only `gh pr view` passed for number, URL, title, head, base, and
state. No conflict or mergeability check was run.

## Next Exact Science Action

Try to derive the channel-density normalization `D_X=A_X/w_X` from current
support/readout structure, then derive or no-go the density-covariance readout
from the current tensor primitive.
