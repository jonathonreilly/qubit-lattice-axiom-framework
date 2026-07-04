# Artifact Plan

## Primary artifact

- [`docs/TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md`](../../../../docs/TIER_A_RESIDUAL_OWNER_DECISION_PACKET_2026-07-04.md)

## Runner

- [`scripts/tier_a_residual_owner_decision_packet_2026_07_04.py`](../../../../scripts/tier_a_residual_owner_decision_packet_2026_07_04.py)
- Cached output:
  [`logs/runner-cache/tier_a_residual_owner_decision_packet_2026_07_04.txt`](../../../../logs/runner-cache/tier_a_residual_owner_decision_packet_2026_07_04.txt)

## Registry

- [`docs/audit/data/doc_authority_registry.json`](../../../../docs/audit/data/doc_authority_registry.json)
  registers the packet as Class D, landed, no premise weight until adopted.

## Audit-generated artifacts

The audit pipeline should seed:

- `tier_a_residual_owner_decision_packet_2026-07-04`
- `claim_type=meta`
- `effective_status=meta`

## Verification plan

1. Compile the runner.
2. Run the runner before and after audit-pipeline seeding.
3. Run the document-authority companion runner.
4. Run the full audit pipeline.
5. Run strict audit lint.
6. Run `git diff --check`.
7. Run ASCII hygiene over new artifacts.
