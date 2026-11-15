# Exact contour filling and density mutation: second criteria

Written before program 02. Prior exposure: program 01 completed successfully and its periodic coarse-scaled curvature column 113.859 and elementary counting bound 5476.915 were observed. The choice to apply the missing-density mutation to that specific successful case is post-run, disclosed here; no claim of blind selection is made. Program 01 and its outputs will not be overwritten.

Construct each of the 4*24*3^4 actual paired S4-prime contours as an ordered signed step word. A different algorithm sorts its coordinate steps by adjacent exchanges; record each exchanged plaquette with integer orientation. Check by exact integer edge boundaries that the resulting surface equals the original contour minus the direct root-to-root straight path, then check every actual contour spread by subtracting the average surface. Require l1 surface coefficients <=25L^2 for an individual contour and <=50L^2 for a spread; record maximum area and maximum coordinate radius. Deleting one nonzero plaquette must fail an exact boundary equation. These finite certificates check the mechanism, not all L.

Read the untouched complete periodic output from program 01 and require its actual curvature column to exceed the corresponding elementary column bound with the factor r^4 removed, where r=3. This is an explicit falsifier of that particular no-density bound, not a universal counterexample to every possible column estimate.

Recheck the exact coth product sum and r^4 scaling for arbitrary subcell translations by the closed one-dimensional geometric-series formula. Numerical tests supplement the proof by convexity and monotonicity, not replace it.
