# Assumptions And Imports

## Used

- Finite post-record word laws on a two-letter alphabet at horizon `N=4`.
- Exact rational arithmetic.
- A statistic/event: extreme count imbalance.
- A supplied concentration certificate `(law id, event id, epsilon)`.
- Exact enumeration and count pushforward to verify event probabilities.

## Not imported

- No Born rule.
- No record-derived probability law.
- No record-derived concentration theorem.
- No independence or mixing assumption unless carried by the supplied law.
- No kernel, clock/rate, Hamiltonian, or production dynamics.
- No audit verdict.
- No generation/Koide dial selection.

## Law-scope rule

Every concentration certificate is scoped to the law and hypotheses used to
prove it. Matching expected counts or one-time marginals does not transport a
certificate to a different law.
