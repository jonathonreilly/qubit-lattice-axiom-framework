# No-Go Ledger — audited_conditional repair 2026-05-18

Routes ruled out at campaign start. Populated as cycles produce no-go
verdicts.

## Pre-campaign exclusions

### NG-PC1 — Do not promote audited_failed rows

Per scope: this campaign only touches `audited_conditional`.
`audited_failed` rows need scope rewrites or full new derivations, both
of which are out of scope per the user's brief and the physics-loop
"no-churn exception" rule.

### NG-PC2 — Do not run the audit-lane

This is the physics-loop, not the audit-loop. The campaign produces
**repair PRs**. The audit lane re-audits on its own cadence via the
cascade-resolution mechanism (`reaudit_candidates.json`).

### NG-PC3 — Do not enlarge the axiom stack

Per `feedback_no_new_axioms` and physics-loop §"No-new-axiom rule":
the framework's `A_min` is fixed. Any repair requiring a new axiom is
out of scope.

### NG-PC4 — Do not over-engineer Tier C rows

Per audit-loop SKILL §"audited_conditional from dependency_not_retained
is normal": these settle naturally when upstream lands. Don't burn
cycles trying to force-close them ahead of the cascade.

## Live no-go entries (populated during campaign)

(none yet)
