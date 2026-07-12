# Route Portfolio

| Route | Trace | Closure value | Risk | Disposition |
| --- | --- | --- | --- | --- |
| Explicit helper registration in both packet resolvers | direct blocker closure | high | low | selected |
| Depend only on dynamic-loader AST discovery | direct blocker closure | medium | parser-regression risk | retained as secondary detection |
| Duplicate helper implementation inside the primary runner | direct blocker closure | low | code divergence and audit ambiguity | rejected |
| New physics derivation of the supplied inputs | beyond scope | unknown | hard/open problem | rejected |

The selected route changes the claim state because it retires the auditor's
only named packet omission without altering the theorem or introducing a new
premise.
