# Route Portfolio

| Route | Description | Result | Reason |
|---|---|---|---|
| A | Try to derive concentration from expected frequency alone | rejected | Expectation does not encode correlations or higher moments. |
| B | Construct finite laws with same expectation but different tails | selected | Exact and minimal counterexample on four events. |
| C | Use asymptotic concentration | rejected | Would import iid/mixing/sub-Gaussian assumptions not derived here. |
| D | Treat realized post-record counts as probabilities | rejected | Violates the pre-record probability / post-record information distinction. |

Selected route B gives a finite no-go rather than a conditional support theorem.
It prunes only the unsupported implication from expectation to concentration.
