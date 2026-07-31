# Route portfolio

## Prior-art sweep

Searched landed commit `b7145ec1d401593f41c4ffcc40edcf8f95ac06fa`
(`origin/main`) using both noun orders, `triangle inequality` with `Koide`,
filename enumeration, and sharded-ledger claim-id searches. The exact theorem
already exists at the target note; nearby signed-readout/chirality and
Dirac-mass notes have different scopes. Classification: **already proven on
matching premises; target only the authenticated-runner repair**.

Representative commands:

```text
git grep -n -iE '(signed[- ]eigenvalue.*singular[- ]value|singular[- ]value.*signed[- ]eigenvalue)' origin/main -- 'docs/*.md'
git grep -n -iE '(triangle inequality.*Koide|Koide.*triangle inequality)' origin/main -- 'docs/*.md'
git ls-tree -r --name-only origin/main -- docs/ | rg -i 'koide.*(signed|singular)|(signed|singular).*koide'
```

## Artifact routes

| Route | Expected trace | Result |
|---|---|---|
| Compact default live transcript without changing assertions | direct blocker closure | selected; 5,372 stdout chars, 30 checks |
| Depend only on the landed 20,000-character cap | supports closure but leaves legacy fragility | context only; not the sole repair |
| Refresh the old verbose cache | none for current-cycle live evidence | rejected as insufficient |
| Re-prove or rescope the theorem | duplicate science / corollary churn | rejected |

The five mathematical stress-test families for the derived boundary are
recorded in the source note's N1 section and the approach registry.
