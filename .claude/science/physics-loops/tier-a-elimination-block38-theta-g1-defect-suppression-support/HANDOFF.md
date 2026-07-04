# Handoff

## Current Block

Block38 is conditional exact support for the G1 dynamical-suppression route.
It proves that a supplied local penalty `exp(-kappa ||dn||^2)` on a supplied
4D branch carrier suppresses defectful branches in the strong-penalty limit
while preserving closed non-exact `H^2` sectors.

Branch: `physics-loop/tier-a-elimination-block38-theta-g1-defect-suppression-support-20260704`
Base: `physics-loop/tier-a-elimination-block37-theta-g1-4d-carrier-supply-no-go-20260704`
PR: pending

## Claim Movement

The block supports the alternative G1 route without adopting it. It separates
defect suppression from global exactness: exact branches and closed non-exact
branches both have zero penalty, but defectful branches have positive
`||dn||^2` and are exponentially projected away in finite regulated families.

## Boundaries

- No theta retirement.
- No `theta_bar = 0`.
- No Tier-A registry edit.
- No physical 4D carrier theorem.
- No current-surface defect-penalty action/measure/energy theorem.
- No finite-`kappa` physical suppression strength.
- No G2/G3/G4 or mass-side bridge.

## Verification

- `PYTHONPATH=scripts python3 scripts/theta_g1_defect_suppression_supplied_penalty_exact_support_2026_07_04.py` -> PASS (`PASS=128 FAIL=0`)
- `python3 -m py_compile scripts/theta_g1_defect_suppression_supplied_penalty_exact_support_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; row
  `theta_g1_defect_suppression_supplied_penalty_exact_support_note_2026-07-04`
  is `bounded_theorem`, `audit_status=unaudited`,
  `effective_status=unaudited`, with 7 deps
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS; existing 23
  warnings / 178 notices, no errors
- `git diff --check` -> PASS

## Review

Local review disposition: PASS WITH CONDITIONAL-SUPPORT BOUNDARIES.

The block does not adopt the supplied penalty, claim a physical action/measure
theorem, claim finite-`kappa` parameter selection, or replace the target with
global exactness.

## Next Exact Action

Commit/push/open PR. The next science move should derive a physical 4D
carrier, derive a physical defect-penalty action theorem, or close the
closed-nonexact interface directly.
