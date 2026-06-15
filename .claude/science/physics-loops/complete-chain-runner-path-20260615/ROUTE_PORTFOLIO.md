# Route Portfolio

| Route | Status | Reason |
|---|---|---|
| Edit generated audit JSON | rejected | User policy says not to add audit results/generated audit state to PRs. |
| Normalize source note paths | selected | Fixes the source signal consumed by extraction without touching verdicts. |
| Add wrapper runner at repo root | rejected | Would add duplicate execution surface for a stale path instead of correcting the source reference. |
