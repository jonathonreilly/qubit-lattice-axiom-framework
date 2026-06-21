# Opportunity Queue

Existing open PRs should not be refreshed onto fast-moving `main`; the reviewer lane will update and cherry-pick useful science/tooling.

| Rank | Candidate | Current read | Why it is nextable | Risk | Disposition |
|---:|---|---|---|---|---|
| 1 | `scalar_selector_remaining_open_imports_2026-04-20` | medium broad no-runner row | Could need aggregate runner/boundary repair | Many scripts and broad DM scalar-selector surface | Defer unless fresh runtime remains |
| 2 | `scalar_selector_proof_chains_2026-04-19` | leaf proof-chain row | One script passes, but only covers one chain | Historical overclaim language and incomplete runner coverage | Skip quick registration |
| 3 | Lower-priority no-runner rows | source-side audit unblock | Potential small metadata/cache fixes | Unknown | Re-scan later |

Block151 consumed the highest-value remaining candidate by repairing the Koide aggregate rather than merely registering it.
