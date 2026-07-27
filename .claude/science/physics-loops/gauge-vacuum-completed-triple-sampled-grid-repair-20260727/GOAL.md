# Goal

Close the audit-identified mismatch between a finite 1440-point computation and
an earlier continuous-family no-go by shipping only the exhaustive finite
numerical predicate and a complete No-Go Discipline packet.

## Exact target contract

| Field | Contract |
|---|---|
| Target statement | For every point in the explicit `6 x 6 x 5 x 8` Cartesian grid, `gap_at` returns a finite float64 gap greater than `10^-6`; the computed minimum and argmin equal the recorded regression values. |
| Quantifiers/domain | Exactly the 1440 listed tuples, the `beta=6` `spatial_pair` implementation, the supplied `Z^min`, and the analytic scalar projection inside `gap_at`. |
| Allowed premises | The checked helper-runner chain, declared grid construction, float64 arithmetic, and the explicit numerical-zero threshold. |
| Forbidden weakenings | Treating a subset of points as exhaustive; omitting the scalar optimization; using a different target triple. |
| Required edge cases | All advertised endpoints, uniqueness/cardinality, finite outputs, target identity, scalar-projection orthogonality, and post-sweep regression pins. |
| Completion witness | Primary runner `PASS=6, FAIL=0` plus a fresh dependency-pinned cache and source-note N1-N8 `PASS` at the same scope. |
| Non-closures | Exact real-arithmetic non-equality, an off-grid continuous lower bound, a global-minimum theorem, or full framework-point realization. |
