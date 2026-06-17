# No-Go Ledger

| Route | Reason rejected | Reuse |
|---|---|---|
| Generated audit data edit | Would be auditing/retagging rather than source repair | Leave audit pipeline to regenerate |
| Claiming GR closure | Dynamics bridge is explicitly still open | Keep open-gate/bounded-support wording |
| Exact/closed S3 wording | Current source boundary corrected this to bounded/conditional | Runner now checks current boundary |
| Reviewer-loop here | User assigned review-loop and landing to reviewer | Record `reviewer_owned_not_run` |
