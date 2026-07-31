# Route portfolio

## Prior-art sweep

Searched `origin/main` commit
`deb3666ae3b989a548f9d70914a6f70c4f342f3e` with statement-level variants:

```text
git grep -n -iE '(full128.*intertwiner|intertwiner.*full128|128.*seam|seam.*128)' origin/main -- 'docs/*.md'
git ls-tree -r --name-only origin/main -- docs/ | rg -i 'full128|m64.*seam|seam.*intertwiner'
git grep -n -i '8.40686768501364e-15' origin/main -- 'docs/*.md' 'docs/audit/data/derivation_obligations.json' 'docs/audit/data/ledger/*.json'
```

The matching result is the target note itself; the two-rail and later compiler
notes are downstream consumers.  No separate landed transcript-repair result
was found.  Classification: the theorem is already present on matching
premises; the open target is its authenticated execution transport.

## Routes

| Route | Type | Trace | Score | Disposition |
|---|---|---|---:|---|
| dated source-hash rerender under the current 20k budget | exact runner | direct blocker closure | 3 | selected: source drift reliably requeues the complete live stdout |
| enlarge packet stdout globally | tooling | direct blocker closure | 1 | rejected as unnecessary repo-wide churn |
| compact the primary runner's default transcript | exact runner | direct blocker closure | 2 | explored but unnecessary; absent from final diff |
| add a separate audit-slice helper | tooling | direct blocker closure | 2 | rejected: adds authentication and selection surface |

The selected route changes only the note hash and source-bound cache
fingerprints.  The primary runner is unchanged: its complete 13-line stdout,
all-128 diagnostic, full summary, and result already fit the current packet.
