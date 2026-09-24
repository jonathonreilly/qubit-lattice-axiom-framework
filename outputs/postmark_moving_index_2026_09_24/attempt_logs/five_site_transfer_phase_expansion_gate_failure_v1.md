# First transfer-phase runner gate failure

The first runner version computed the corrected trace and phase coefficients
but then imposed an unjustified finite-sample threshold of 20 on every
`S^3`-scaled residual. It failed with maximum sampled scales
`110.03366674512493` for the trace and `4938.256448501578` for the phase.

This was a bad numerical acceptance threshold, not a derivation counterexample:
the compact-arc `O(S^-3)` theorem has a constant depending on the lower bounds
for `w`, `|sin(5k)|`, and `|sin(k)|`; the chosen `k=0.1` makes the phase
constant large while still lying in the regular set. The note already proves
uniformity for each fixed compact set and does not assert a universal constant
of 20.

I removed that arbitrary threshold and replaced it with a discriminating
finite-difference sentinel at `u=0.65`, `k=0.1`, and `S=240,480`. The ratio
of the unscaled residuals was `8.043633631324134` for the trace and
`8.517667526853339` for the phase, consistent with cubic error scaling at
these sizes. This numerical check is corroboration only; the compact analytic
argument carries the uniform theorem. Omitting the displayed `P5` coefficient
was separately tested and rejected by the symbolic trace-identity gate.
