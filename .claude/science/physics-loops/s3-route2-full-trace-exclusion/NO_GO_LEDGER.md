# No-Go Ledger

| Route | Result | Reuse boundary |
|---|---|---|
| Fierz/channel-count selector | Leaves `kappa` free | Block69 |
| Current-projector idempotence | Narrows `kappa` to `{0,1}` only | Block70 |
| Exact full-trace exclusion from current controls | No-go; full trace survives | This block |
| Bounded OZI suppression | Size class only | Does not give exact zero |
| Target-value selection | Selects connected endpoint | Forbidden as proof input |
