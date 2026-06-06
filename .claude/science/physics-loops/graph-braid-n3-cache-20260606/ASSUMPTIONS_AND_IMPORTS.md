# Assumptions And Imports

Load-bearing machinery:

- In-repo Abrams discretized unordered-configuration-space construction.
- Exact integer Smith normal form for integral `H_1`.
- Exact `GF(2)` cohomology/fibered-subspace linear algebra.
- `networkx` is used to construct/check finite graph witnesses; it is a runtime
  library dependency, not a theorem import.

Imports retired or reduced:

- The stale runtime artifact import is retired by a completed SHA-pinned cache
  with `SCORECARD: PASS=26 FAIL=0`.

