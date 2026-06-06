# Assumptions And Imports

## Used

- Finite alphabet `A, B`.
- Finite horizon `N=4`.
- Two explicitly supplied laws on words of length four:
  - iid fair law, probability `1/16` for each word;
  - perfectly correlated fair law, probability `1/2` on `AAAA` and `1/2`
    on `BBBB`.
- Exact rational arithmetic.
- Standard finite probability definitions for expectation, marginal,
  tail probability, and p-value under a supplied law.

## Not imported

- No Born rule.
- No Hamiltonian.
- No clock, time metric, or transition rate.
- No kernel derivation.
- No concentration theorem.
- No asymptotic approximation.
- No generation/Koide dial selection.
- No audit verdict.

## Interpretation firewall

The observed post-record word is realized information. Probability enters only
through a supplied pre-record or ensemble law over possible words. Expected
counts are therefore ensemble summaries, not replacement data for the realized
record and not enough to infer calibration.
