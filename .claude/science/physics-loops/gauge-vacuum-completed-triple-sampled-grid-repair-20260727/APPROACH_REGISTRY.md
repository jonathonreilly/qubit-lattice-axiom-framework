# Approach Registry

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| Finite machine predicate | 1440-element Cartesian set | Exhaustive evaluation; projection orthogonality; dependency fingerprint | All five executable checks pass | target-equivalent | candidate-complete | primary runner `PASS=5, FAIL=0` | a failed rerun or review finding |
| Exact sampled grid | Interval enclosures at fixed tuples | Validated matrix exponentials and norms | Positive lower enclosure at every tuple | stronger | unexplored | none | interval implementation |
| Continuous boxes | Compact four-dimensional domain | Interval branch-and-bound | Positive lower bound on every sub-box | stronger | unexplored | empirical runner is insufficient | certified interval operators |
| Analytic minimum | Continuous gap function | Derivative signs or global operator bounds | Prove global positive minimum | stronger | unexplored | none | new analytic invariant |
