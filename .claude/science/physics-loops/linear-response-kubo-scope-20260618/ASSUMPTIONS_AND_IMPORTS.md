# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `A,B,C` second-order propagators | Compute `kubo_1`, `kubo_2`, and finite replay ratios | computed lattice input | `scripts/linear_response_second_order_kubo.py` and frozen cache | yes | yes | already replayed in runner/cache | finite replay support |
| 44-family panel and strengths | Declared empirical/computational domain | computed lattice input | runner inputs and cached log | yes | yes | keep as explicit scope | explicit finite panel |
| First-order/range-of-validity sibling claims | Context for what the second-order replay does not extend | external sibling source notes | sibling notes/runners | yes for comparison only | no for all-order closure | reviewer/auditor checks sibling status separately | context only |
| Remainder/convergence/non-analyticity theorem | Would upgrade from finite second-order replay to Taylor-boundary no-go | open theorem | not supplied | no for narrowed claim; yes for all-order claim | prove separately | open residual |
| Third-or-higher-order computation | Would test higher Taylor orders on failing families | open computation | not supplied | no for narrowed claim; yes for all-order claim | compute separately | open residual |
