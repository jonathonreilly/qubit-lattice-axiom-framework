# Handoff

## Current Block

Block 4 retires AC_phi_lambda(iii)'s C3-grade species bridge from Tier-A by
owner path-extension and grade-scoped naming-class ratification.

## Completed

- Added the governance note and paired runner.
- Updated the human Tier-A registry and machine registry.
- Dropped `species_bridge` from AC_phi_lambda's live minimum decomposition.
- Added a partial reclassification row for `species_bridge_c3_grade`.
- Recorded the owner decision in `docs/audit/AXIOM_MINIMALITY_POLICY.md`.
- Regenerated audit data and refreshed runner caches.

## Boundaries

- AC_phi_lambda does not retire.
- The genuine admitted-target count remains two: AC_phi_lambda and theta.
- AC(i), AC(ii), theta, above-C3 taste/Dirac/chirality content, and CKM/PMNS
  alignment are untouched.
- No audit verdict is set.

## Verification

- `PYTHONPATH=scripts python3 scripts/acphilambda_species_bridge_c3_grade_owner_ratification_2026_07_04.py`: PASS=44 FAIL=0.
- `PYTHONPATH=scripts python3 scripts/admitted_input_registry_tier_a_boundary_check.py`: PASS=76 FAIL=0.
- `bash docs/audit/scripts/run_pipeline.sh`: pass; no errors, existing warnings/notices only.
- `python3 docs/audit/scripts/audit_lint.py --strict`: pass; no errors, existing warnings/notices only.
- `git diff --check`: pass.

## Next Exact Action

Open the stacked PR against
`physics-loop/tier-a-elimination-block03-ac-20260704`, then attack AC(ii)'s
R-eta atom or AC(i)'s measure-side occupancy binary.

## PR

- https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4929
- Base: `physics-loop/tier-a-elimination-block03-ac-20260704`
- Commit: `cc2bc71dc docs: ratify ac species bridge c3 grade`
