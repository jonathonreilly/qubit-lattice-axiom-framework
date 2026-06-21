# Opportunity Queue

Existing open PRs should not be refreshed onto fast-moving `main`; the reviewer
lane will update and cherry-pick useful science/tooling.

| Rank | Candidate | Current read | Why it is nextable | Risk | Disposition |
|---:|---|---|---|---|---|
| 1 | `diamond_nv_phase_ramp_signal_budget_note` | medium bounded no-runner row | Has existing hardening script/cache | Higher risk: names a budget gap and depends on protocol/prediction rows | Defer unless another full block is available |
| 2 | `scalar_selector_remaining_open_imports_2026-04-20` | medium broad no-runner row | Could need aggregate runner/boundary repair | Many scripts and broad DM scalar-selector surface | Defer until a direct runner is isolated |
| 3 | `scalar_selector_proof_chains_2026-04-19` | leaf proof-chain row | One script passes, but only covers one chain | Historical overclaim language and incomplete runner coverage | Skip quick registration |

Block153 consumes the bounded protocol row with a wrapper runner and leaves the
signal-budget row for a separate reviewable block.
