# Opportunity Queue

Existing open PRs should not be refreshed onto fast-moving `main`; the reviewer lane will update and cherry-pick useful science/tooling.

| Rank | Candidate | Current read | Why it is nextable | Risk | Disposition |
|---:|---|---|---|---|---|
| 1 | `koide_axiom_native_support_batch_note_2026-04-22` | high bounded row with no registered runner | Could have a narrow aggregate runner-registration gap | Many Koide support scripts and high overclaim risk | Inspect only if runtime remains |
| 2 | bounded/open-gate rows with `runner_path: null` and existing validation commands | source-side audit unblock | Likely small parser/cache PRs | Need avoid broad status rewrites | Scan fresh after this PR |
| 3 | `legacy_exploratory_drivers_note` | broad positive theorem row with no runner | Could need historical/archive boundary cleanup | Broad, likely non-source archive churn | Low priority |
| 4 | `unified_program_note` | broad program note with no runner | Maybe metadata-only repair | Too broad and high graph blast radius | Low priority |

Recently skipped: `unpromoted_branch_retainability_audit_note`, `b_independence_mechanism_note`, and `koide_a1_loop_investigation_summary` because each appeared to need broader review or human science judgment than a narrow unblock PR.
