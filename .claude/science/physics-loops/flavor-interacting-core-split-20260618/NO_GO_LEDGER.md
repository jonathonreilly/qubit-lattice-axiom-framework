# No-Go Ledger

| Route | Result | Reuse |
|---|---|---|
| Treat reported nonperturbative branch as runner-certified | Rejected. The runner did not compute the branch, critical coupling, or `r(g)`. | Branch source now labels these as context-only. |
| Claim global no-go for every `C3`-symmetric interaction | Rejected as too broad for this packet. | Runner proves only the finite diagonal/epsilon tested obstruction. |
| Use epsilon as generation-specific channel on `hw=1` | Fails. It is constant on `hw=1` and maps `hw=1` to `hw=2` as a shift. | Executable checks E1-E2. |
| Use diagonal `C3`-invariant operator to split generations | Fails. The invariant diagonal subspace is scalar. | Executable checks E4-E5. |
