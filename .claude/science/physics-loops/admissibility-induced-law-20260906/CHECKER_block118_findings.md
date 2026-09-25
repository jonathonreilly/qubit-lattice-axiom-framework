# Block 118 — control and findings (2026-09-24)

1. **Provenance.** Three probes attempts (#8688 and #9127 by Claude Opus 5.5, #8583 by Claude Opus 5) derived the results, and Grok referees confirmed them (#9039, #9094, #9129). The supervisor re-checked the exact parts with its own runner, and β with its own float quadrature outside the runner.
2. **Numerical status.** β's values are quadrature. A float model of an interval-bound scheme closed the axes-and-faces side with a few thousand cells, but not the staircase side at 400000 cells. An exact enclosure is open.
3. **Scope.** Diagonal hops go outside the lane's six-neighbour stencil, and need exchange with diagonal targets and reflection as content reversal. The collisional viscosity and the two-body force off the axes are not treated.
