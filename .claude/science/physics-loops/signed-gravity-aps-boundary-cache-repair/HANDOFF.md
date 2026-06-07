# Handoff

## Summary

This PR repairs the audit-runnability of the signed-gravity APS source-action
boundary packet. The parent note and parent harness already agree on the
current Born/norm controls:

```text
I3=+5.381e-43
max drift=3.331e-15
```

The boundary checker still expected older values and therefore failed after the
parent harness changed. The PR updates the checker literals and refreshes the
SHA-pinned cache.

## Claim Movement

- Actual movement: open-gate boundary/demotion route is now runnable.
- Not claimed: source-action origin theorem.
- Not claimed: eta-sector superselection.
- Not claimed: physical signed-gravity closure.

## Verification

```bash
python3 scripts/signed_gravity_aps_locked_source_action_proposal.py
python3 scripts/signed_gravity_aps_source_action_boundary_repair.py
python3 scripts/cached_runner_output.py scripts/signed_gravity_aps_source_action_boundary_repair.py --refresh
```

## Reviewer Next Action

Review the narrow cache repair and decide whether it is enough to requeue the
row as an explicit `open_gate` boundary. If the reviewer wants positive closure
instead, the next science target is the source-action derivation, not another
cache edit.
