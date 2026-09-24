# Root controls for the full-ensemble candidate

These controls were run and read completely before independent PRE disclosure.
The source algebra explicitly reuses the frozen root word helpers from the
mixed-preparation calculation. New checks cover 1,260 edge/mark/input cases,
including moving spin-boundary words, and the operator coefficient cancelling
the second-high birth amplitude. Rotor arithmetic has exact integer
cancellation in the implemented operations; finite-spin checks use floating
weights. The wrong middle coefficient is actually computed and nonzero in
1,239 cases. This does not replace the analytic uniform contour argument.

The ten-state cascade retains a rotating two-component pre-birth input,
nontrivial low energy and four fast matter states. Its diagonal GKLS blocks
are evaluated by matrix exponentials. The stationary frozen-source covariance
is obtained separately by a Lyapunov solve. At t=1.1, epsilon=.01, the full
mean is 2.877541 versus 2.876752, and the scaled variance is 3.265279 versus
3.264409. The scaled high-density trace distance is .000937434. The exact
fast bright-balance formula has a numerical residual below 3e-15 over the
three time samples. Freezing the unevolved input gives a nonzero covariance
error at every tested time. The toy has a strict exponential fast gap; it is
not a numerical test of the cube's five-dimensional algebraic tail.

All fifteen rows, matrices, finite-spin coefficient rows and execution logs
were read. Small negative diagonal-block eigenvalues (about 7e-14 in
magnitude) are floating error diagnostics, not interval positivity claims.
There is no full-cube propagation, full-output Fisher result or conserving
apparatus in this control. Prior author/helper reuse is explicit.
