This PR repairs source-runner drift in
`docs/SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md`.

The note's finite-harness controls now match the current runner/cache:

```text
Born I3, chi=+ sector: +5.381e-43
Born I3, chi=- sector: +5.381e-43
max norm drift: 3.331e-15
```

Scope boundary:

- This closes only the stale control-number repair item.
- It does not derive the APS-locked source-action cross term.
- It does not update `docs/audit/**` or any ledger status.
