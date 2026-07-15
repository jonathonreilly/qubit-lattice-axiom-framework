# Route portfolio

| Route | Claim-state movement | Artifactability | Risk | Decision |
|---|---:|---:|---:|---|
| Detect static Python subprocess targets in the dependency resolver | 3 | 3 | low | selected |
| Add a claim-specific explicit helper mapping in two resolver copies | 2 | 3 | medium maintenance duplication | fallback |
| Inline or duplicate the canonical implementation in the wrapper | 1 | 1 | high source drift | rejected |
| Treat stdout as sufficient evidence | 0 | 3 | disallowed by audit rubric | rejected |

The selected route repairs the general packet mechanism and directly exposes
the previously omitted source without changing the numerical computation.
