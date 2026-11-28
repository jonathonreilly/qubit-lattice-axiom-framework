lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-29T04:59Z

# Independent Lean reproduction of the (PUR-io) consumer under the footprint cap (FINISH row 1691)

Started 2026-11-28T16:59:46Z (date -u). Worker: Claude Opus 5.5, effort high, Mac mini worker 1.
Pinned commit: 9cd49b2b27b8f085c9b9054ae060f48f51894845 (branch claude/ym4d-hard-route).

Scope: Part A of row 1681 (`library/lean-gap-chain-purio-check-opus.md`) again, with the lead's
new memory rule: kill the build when the physical footprint of the lean/lake process tree goes
above 6 GB, or when system free memory (memory_pressure) goes below 40 percent. Part B of row 1681
is done; it is not repeated here.

Credit: the Lean release is by Sussman-Alpoge (with Claude and Codex). GapChain Purity.lean,
PurIo.lean and Offset.lean are by gpt-6.2-astra max (rows 1676, 1678, 1679). The method reuses
rows 1671 and 1681 (`library/lean-gap-chain-final-check-opus.md`,
`library/lean-gap-chain-purio-check-opus.md`).

## Status

In progress.
