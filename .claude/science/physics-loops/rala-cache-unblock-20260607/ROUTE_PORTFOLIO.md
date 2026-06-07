# Route Portfolio

| route | result |
| --- | --- |
| Raise timeout only | Rejected. A single `dim=3, side=4, axis=0` profile took about 49 seconds, so the full default remains marginal. |
| Narrow default grid | Rejected. It would unblock the cache but unnecessarily shrink the audited surface. |
| Optimize large pair checks by logical factorization | Chosen. It preserves `{1,2,3} x {2,4}` with `PASS=96 FAIL=0` in 0.14 seconds. |
