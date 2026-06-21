# Opportunity Queue

Existing open PRs should not be refreshed onto fast-moving `main`; the reviewer lane will update and cherry-pick useful science/tooling.

| Rank | Candidate | Current read | Why it is nextable | Risk | Disposition |
|---:|---|---|---|---|---|
| 1 | `koide_axiom_native_support_batch_note_2026-04-22` | high bounded row with no runner | Important but currently failing integrated regression | Needs substantive runner/science repair, not a wrapper | Defer |
| 2 | `scalar_selector_proof_chains_2026-04-19` | leaf bounded row, one script | Potential narrow runner registration | DM scalar-selector overclaim risk | Inspect only with fresh runtime |
| 3 | `scalar_selector_remaining_open_imports_2026-04-20` | medium broad row, many scripts | Could have aggregate runner opportunity | Broad dependency surface | Low priority |

Block150 chose a leaf G1 row because the higher-priority Koide candidate was not safely wrapper-ready.
