# Trace Gate

## Trace Class

`owner_governed_residual_premise_retirement`

## Gate

This block is allowed to retire live Tier-A admissions only by explicit
owner-governance adoption of the four exact Block49 residual candidates into a
separate Class B owner-governed premise registry.

## Pass Criteria

- Tier-A admitted derivation target count is zero.
- Former live Tier-A ids are preserved as retired history.
- Former live Tier-A ids are listed in `owner_governed_premise_nodes.json`.
- Owner-governed ids do not overlap axiom/primitive ids.
- Effective-status logic recognizes owner-governed premises as
  chain-satisfying without Tier-A boundedness.
- Audit pipeline and strict lint pass.

## Stop Criteria

- Any axiom/primitive allowlist expansion.
- Any theorem-status claim for AC_phi_lambda or theta.
- Any live Tier-A derivation target after adoption.
- Any owner-governed premise outside the exact Block49 candidate set.
