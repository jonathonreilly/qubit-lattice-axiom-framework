# Approach registry

| Family | Object / formulation | Mechanism / invariant | Terminal obligation | Strength vs target | Status | Evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| `l1_triangle` | signed and modulus denominators | equality in triangle inequality | strictness iff a negative entry exists | target-equivalent for T-ii | candidate-complete | proof T-ii; runner Part 3 | explicit counterexample to equality condition |
| `one_negative_piecewise` | one-negative spectral branch | `sum|lambda|=3a-2lambda_min` | strict denominator increase | target-equivalent on the branch | candidate-complete | C2; runner Part 8 | second-negative branch at `r=1/2` |
| `sign_window` | trigonometric zero cells | exact roots plus continuity | classify the closed equality interval | target-equivalent for C1 | candidate-complete | C1; runner Part 6 | missed root or periodic cell |
| `boundary_escape` | degenerate zero mode | endpoint evaluation | decide boundary inclusion | weaker edge-case obligation | candidate-complete | `Q(V)(pi/12)=2/3` | new degenerate point |
| `parameter_relaxation` | arbitrary-`r` spectra | exact falsifier | test whether `<2/3` survives relaxed hypothesis | stronger than narrowed target | candidate-complete | `423/512` counterexample | none; route already forced narrowing |
| `transport_compaction` | runner stdout | lossless removal of repeated successful detail | every check and forensic locator fits packet | target-equivalent for artifact repair | candidate-complete | 5,372 chars; 30 pass lines | transport cap below 5,372 |
