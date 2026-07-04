# Artifact Plan

## Primary artifact

- [`docs/TIER_A_RESIDUAL_GOVERNANCE_READINESS_PACKET_2026-07-04.md`](../../../../docs/TIER_A_RESIDUAL_GOVERNANCE_READINESS_PACKET_2026-07-04.md)

## Runner

- [`scripts/tier_a_residual_governance_readiness_packet_2026_07_04.py`](../../../../scripts/tier_a_residual_governance_readiness_packet_2026_07_04.py)
- Cached output:
  [`logs/runner-cache/tier_a_residual_governance_readiness_packet_2026_07_04.txt`](../../../../logs/runner-cache/tier_a_residual_governance_readiness_packet_2026_07_04.txt)

## Audit-generated artifacts

The audit pipeline seeds:

- `tier_a_residual_governance_readiness_packet_2026-07-04`
- `claim_type=meta`
- `audit_status=unaudited`
- `effective_status=meta`
- `criticality=leaf`

## Verification plan

1. Compile the runner.
2. Run the runner before and after audit-pipeline seeding.
3. Run the full audit pipeline.
4. Run strict audit lint.
5. Run `git diff --check`.
6. Run ASCII hygiene over new artifacts.
7. Run local compact review for overclaim, hidden import, and generated-file freshness.
