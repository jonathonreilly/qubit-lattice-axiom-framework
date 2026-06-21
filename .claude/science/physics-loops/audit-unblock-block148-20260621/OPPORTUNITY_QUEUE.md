# Opportunity Queue

This queue is for the continuing audit-unblock campaign after block 148. Existing open PRs should not be refreshed onto fast-moving `main`; the reviewer lane will update and cherry-pick useful science/tooling.

| Rank | Candidate | Current read | Why it is nextable | Risk | Disposition |
|---:|---|---|---|---|---|
| 1 | `mass_spectrum_derived_note` | medium bounded row with multiple scripts | May have a runner-registration or boundary-packaging gap that can unblock audit | Broad quantitative lane; inspect carefully before editing | Next candidate to inspect |
| 2 | `koide_axiom_native_support_batch_note_2026-04-22` | high bounded row with many scripts | Potentially high-value if a narrow runner/discoverability gap exists | Large blast radius and likely support-only wording traps | Inspect only if time remains |
| 3 | `legacy_exploratory_drivers_note` | broad/open historical surface | Could need metadata/runner boundary cleanup | High risk of non-source archive churn | Low priority |
| 4 | `unified_program_note` | broad programmatic note | May have stale links or authority-boundary gaps | Too broad for a quick source-side PR | Low priority |

Skipped in recent blocks: `unpromoted_branch_retainability_audit_note`, `b_independence_mechanism_note`, and `koide_a1_loop_investigation_summary` because each appeared to need broader review or science judgment than a narrow unblock PR.
