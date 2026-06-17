# Opportunity Queue

| Rank | Candidate | Reason | Status |
|---:|---|---|---|
| 1 | GR route no-runner registration | Two critical rows have blank runner paths despite existing scripts | This PR |
| 2 | Other critical no-runner rows | Several source rows have no runner path and may have existing scripts | Next scan target |
| 3 | Staggered-Dirac source bridge | Large downstream impact, but active audit queue already has runners | Defer unless audit needs source repair |
| 4 | Hard hierarchy/Higgs bridge science | Highest descendants but needs new theorem, not metadata repair | Frontier stretch target |

Do not spend time rebasing existing PRs unless a reviewer asks for a specific
branch update.
