# Exposed-data follow-up: seek an interior D-family candidate

Direct author protocol, 2026-10-12. Freeze before executing this additional
optimization or seeing its weights. The six original frozen fits remain
unaltered. They have zero working-grid primary t but minimize total weight
second, which can place them exactly against an observational rectangle.
Their actual direct/refined checks are still running. This follow-up asks
whether a candidate exists with margin against numerical perturbations.
It is an exposed-data development calculation, not a new blind test.

Keep every original source, geometry, response knot, weight cap, D inequality,
velocity/error input, external/solar rectangle and solar operator. Use only the
same three fitting galaxies. Fix Newtonian E to the original D combined-case
value from shared_response_fits_v1.json; do not optimize or scan E again here.

Introduce0<=z<=1. Maximize z subject to w>=0, sum w<=100, the original D
inequalities, and the tightened constraints

    L_i + z A_i <= g_N,i + sum_j K_ij w_j <= H_i - z A_i,
    g_min + z(g_max-g_min)/2 <= E N(E) <= g_max - z(g_max-g_min)/2,
    Q2 <= (1-z) Qmax.

The negative lower solar edge is still automatically satisfied by positivity.
The heterogeneous margin normalizations above are intentional: fractional
galaxy acceleration, fraction of external half-width, and fraction of positive
solar upper bound. z is a numerical robustness parameter, not a confidence
level. If any released zero-error row forces z0, preserve it; do not alter
its error or remove the row. D is not tightened into a new theory premise.

Then minimize sum w while retaining z>=z_max-1e-8. Require scaled LP primal
residual<=1e-7. Preserve all outcomes, including infeasibility or zero margin.
Never replace or relabel an original frozen-fit result with this follow-up.

Validate these new weights directly on the already planned base, refined and
extended-boundary field grids. Recheck every original (untightened) galaxy,
solar and external rectangle using the actual fields. Report the observed
margin changes rather than assuming the LP margin transfers. Reuse the same
finite numerical gates, and preserve failures. No interval or universal
existence certification follows from a numerical pass.

If the original D combined-case and this interior candidate pass their field
checks, carry both, without selection by extension residuals, to the six
preselected out-of-fit development objects. These observations were previously
exposed but will not fit either response. Retain the circular-speed readout
and source uncertainties. The resulting comparison is separate from a healthy
time-dependent or quantum completion of the static response.
