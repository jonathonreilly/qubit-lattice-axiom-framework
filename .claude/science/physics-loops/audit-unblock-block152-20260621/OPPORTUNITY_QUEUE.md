# Opportunity Queue

Existing open PRs should not be refreshed onto fast-moving `main`; the reviewer
lane will update and cherry-pick useful science/tooling.

| Rank | Candidate | Current read | Why it is nextable | Risk | Disposition |
|---:|---|---|---|---|---|
| 1 | `diamond_sensor_protocol_note` | medium bounded no-runner row with existing protocol probe | Likely small wrapper/metadata/cache registration | Must avoid bundling with prediction or lab-budget closure | Next small candidate if runtime remains |
| 2 | `diamond_nv_phase_ramp_signal_budget_note` | medium bounded no-runner row | Has existing signal-budget hardening script/cache | Higher risk because it names a budget gap and depends on prediction/protocol rows | Defer until protocol row is wired |
| 3 | `scalar_selector_remaining_open_imports_2026-04-20` | medium broad no-runner row | Could need aggregate runner/boundary repair | Many scripts and broad DM scalar-selector surface | Defer unless fresh runtime remains and a direct runner is isolated |
| 4 | `scalar_selector_proof_chains_2026-04-19` | leaf proof-chain row | One script passes, but only covers one chain | Historical overclaim language and incomplete runner coverage | Skip quick registration |

Block152 consumes the high-priority diamond prediction row by adding a bounded
wrapper runner rather than treating a printer-only card as decisive evidence.
