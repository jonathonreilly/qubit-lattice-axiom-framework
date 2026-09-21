# Block 53 — refuting pass and findings (2026-09-21)

1. Disjoint machinery (`specs/supervisor_control_block53_refuter.py`): W1 symbolic solution of the covariance and shift conditions (`−c_0/6` for every neighbour); W2 the power mean with symbolic order (first derivatives `1/6`; second order `(p − 1)/6`); W3 a sparse solve on a `41³` box with zero walls; W4 twelve records on a `16³` torus by transform (sum exact to rounding); W5 a simulated test record (largest relative difference from `1/w`: `0.015`). All pass.
2. Finding folded: the first W3 compared `u r` with the infinite-lattice value and failed by 30 per cent — walls at distance 20 shift the field near the centre by a nearly constant amount. Differences of the field are compared instead (the same wall lesson as block 51, in a different guise).
3. Finding folded: the runner's first geometric-mean check scaled sixth roots where it meant to scale rates.
4. A supervisor's argument withdrawn in the lens pass: records as pinned values would give a capacity that adds for dilute bodies and saturates for compact ones; attractive as that looked, a pinned absolute rate is not scale covariant and the clause excludes it.
5. Recorded for block 50: under "no master clock" the global clock `1/π(C)` is a change of the unobservable unit of rate; what its stationary law means for an observer who can only compare rates is open.
