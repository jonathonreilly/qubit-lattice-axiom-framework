# Route portfolio

## Prior-art sweep

Searched landed commit `c0d9397c6f6e28b902bd011689eca07bdc8edd07` with:

```text
git grep -n -iE '(middle-branch.*breakpoint|breakpoint.*middle-branch)' origin/main -- 'docs/*.md'
git grep -n -i 'log(1 + b' origin/main -- 'docs/*.md'
git ls-tree -r --name-only origin/main -- docs/ | rg -i 'dm.selector.*(shoulder|threshold|stabilization)'
git grep -n -i 'tau_b,min' origin/main -- docs/audit/data/derivation_obligations.json 'docs/audit/data/ledger/*.json' 'docs/audit/data/ledger/**/*.json'
```

Matching hits were the target note itself, its criticality-bump hygiene
companion, two downstream relative-action notes, the missing-derivation prompt,
and the sharded ledger row. Classification: the scoped theorem is already
present on matching premises; this cycle is an explicit derivation-exposition
repair requested for re-audit, not a novelty claim.

## Routes considered

| Route | Type | Trace | Value | Decision |
|---|---|---|---|---|
| Explicit finite-bank margins | constructive proof certificate | directly closes quoted algebraic step | Makes every strict inequality inspectable | selected |
| Modify the runner | exact runner | supports same step | Existing substantive checks already pass; changing its hash would invalidate provenance without adding a needed computation | rejected |
| Derive `tau_phys=tau_b,min` | selector theorem | would close physical gate | New hard physics outside audited scope and short-task budget | rejected |
| Add another companion note | packaging | indirect | Duplicates existing companion and parent proof | rejected as churn |

The selected route preserves the established theorem and adds the missing
audit-facing proof certificate in the canonical source note.
