# Artifact Plan

## Primary artifact

- [`docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`](../../../../docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md)

## Runner

- [`scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py`](../../../../scripts/tier_a_residual_owner_adoption_retirement_2026_07_04.py)
- Cached output:
  [`logs/runner-cache/tier_a_residual_owner_adoption_retirement_2026_07_04.txt`](../../../../logs/runner-cache/tier_a_residual_owner_adoption_retirement_2026_07_04.txt)

## Registries

- [`docs/audit/data/tier_a_admissions.json`](../../../../docs/audit/data/tier_a_admissions.json)
  has zero live derivation targets and preserves prior entries under
  `retired_derivation_targets`.
- [`docs/audit/data/owner_governed_premise_nodes.json`](../../../../docs/audit/data/owner_governed_premise_nodes.json)
  registers the former Tier-A target ids as Class B owner-governed residual
  premises.
- [`docs/audit/data/axiom_premise_nodes.json`](../../../../docs/audit/data/axiom_premise_nodes.json)
  is intentionally unchanged.

## Audit-generated artifacts

The audit pipeline should preserve:

- `tier_a_residual_owner_adoption_retirement_2026-07-04`
- `claim_type=meta`
- `effective_status=meta`
- zero live Tier-A admitted derivation targets in front-door and registry
  surfaces

## Verification plan

1. Compile modified Python scripts and tests.
2. Run the Tier-A boundary runner.
3. Run the owner-adoption retirement runner.
4. Run the document-authority companion runner.
5. Run full audit pipeline.
6. Run strict audit lint and unit tests.
7. Run `git diff --check`.
8. Run ASCII hygiene over new artifacts.
