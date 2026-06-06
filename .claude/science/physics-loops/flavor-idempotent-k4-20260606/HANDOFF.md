This PR repairs the missing K4 executable check in
`docs/FLAVOR_IDEMPOTENT_U1_COLLAPSES_NOTE_2026-05-30.md`.

The new runner check constructs the C3 spectral projectors and verifies:

```text
P_omega + P_omegabar = P_d
P_omega - P_omegabar not in span{P_s, P_d}
```

Scope boundary:

- This closes the "K4 stated but not executed" repair item.
- It does not derive `r=1/2`.
- It does not derive a sector selector for the r ladder.
- It does not update `docs/audit/**` or any ledger status.
