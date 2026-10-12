# Shared-response reconstruction: frozen direct-author protocol

2026-10-12. Freeze before the first response-basis galaxy operator or fitted
weight vector. The three original sources and their fixed-response results
are exposed. This family is motivated by those results and the exposed solar
comparison. It is model development, never a new blind confirmation.

## Conditional model and observation roles

Retain the supplied QUMOND equation and the same fixed64-ring baryonic sources,
gas sheet, exponential stellar height, distance, inclination and global
stellar mass-to-light ratio0.5605122519882025. Reconstruct the *response*, not
these sources. The primary reconstruction uses all scored rows of NGC2976,
UGC07577 and KK98-251, the original source-selected trio. Their observations
are fitting inputs. The six preselected extension objects are out of this
fit; all have prior exposure from the earlier algebraic campaign, so their
later comparison is an out-of-fit development test, not blind validation.
If the six-source forward gate fails, preserve the incomplete extension;
do not replace the source with an easier observed fit.

The input velocity/error arrays remain the processed SPARC release used by
the preceding forward contract. At each radius define

    A_i = V_i^2/R_i,
    L_i = max(0,V_i-2 e_i)^2/R_i,
    H_i = (V_i+2 e_i)^2/R_i.

Use nonnegative released e_i, with zero retained as zero. These rectangles
are descriptive marginal-error comparisons, not a joint confidence region.
Source and geometry uncertainties remain unpropagated. The fit minimizes
a nonnegative additional fractional acceleration tolerance t subject to

    L_i-t A_i <= g_i <= H_i+t A_i.

Thus t=0 means compatibility with the stated rectangles under the fixed
premises; a positive t measures the extra fractional acceleration allowance
needed in this finite family. It is not a sigma or likelihood statistic.
All rows receive the same fractional allowance; no galaxy is removed by
residual size and no row-error floor is fitted.

## Finite response family, including its unobserved tails

Set21 fixed logarithmic knots A_j=10^(-13+j/4) m/s^2 for j=0,...,20.
For each adjacent interval define the continuous logarithmic ramp b_j from
DIRECT_RESPONSE_BASIS_RESULTS.md. Use

    N(A)=1+sum_(j=0)^19 w_j b_j(A),   w_j>=0,   sum_j w_j<=100.

This has20 global nonnegative weights. Below the lowest knot the enhancement
is a bounded constant at most101; above the highest knot it is exactly one.
Those are explicit candidate assumptions, not inferred asymptotic laws.
In particular it has no unbounded deep-MOND tail. No knot, cap or family
member is selected by trying these data fits first.

Two declared versions will be reported: (M) this monotone enhancement family;
(D) the same family with nonnegative differential radial response
d[A N(A)]/dA>=0. D is a further physical premise. On interval j its minimum
occurs at the upper knot, so it is exactly the finite linear condition

    w_j/log(A_(j+1)/A_j) <= 1+sum_(k>j) w_k.

The low/high constant tails automatically satisfy it. No action, quantum
stability or relativistic completion is claimed merely from D.

## Field and solar operators

For fixed U=grad Phi_N, compute each radial column

    K_ij = radial component of P[b_j(|U|) U],
    g_i = g_N,i + sum_j K_ij w_j.

P is the full independently checked Poisson projection, including the gas
sheet. It is linear in its vector input. K_ij may have either sign; replacing
it by a positive radial algebraic weight would change the problem. The exact
Newtonian g_N,i supplies the baseline; finite-grid projection error in that
baseline is checked separately rather than incorporated as new physics.

For a chosen positive Newtonian solar background E, compute

    q_j(E)=E^(3/2)/sqrt(G M_sun) * F(A_j/E,A_(j+1)/E),
    Q2=sum_j q_j(E) w_j,

using the checked positive solar response integral. The same GM_sun is
1.32712440018e20 m^3/s^2. No redundant acceleration a0 is introduced.

The observed physical Galactic acceleration cannot be held at the old
conversion while changing N. For this block explicitly adopt the spherical
parent approximation

    g_e=E N(E),   2.00e-10 <= g_e <= 2.64e-10 m/s^2.

At fixed E this is also linear in w. It uses the same Gaia-derived rectangle
as the preceding solar contract, with its quasar-frame identification and
fixed Galactic-center direction. It is an additional approximation, not an
exact identity for the nonspherical Milky Way. No full Milky Way source or
orientation covariance is supplied here.

The primary solar rectangle remains -2.0e-27<=Q2<=5.2e-27 s^-2, from the
already exposed Park et al. summary. Positivity automatically meets its lower
edge. This is a fitted constraint in the combined reconstruction, never a
new successful prediction. The older overlapping Cassini estimate is not
combined as independent data.

## Optimizations, numerical checks and honest failure scope

For each M and D, report (1) galaxies alone, (2) galaxies plus the external
acceleration rectangle, (3) galaxies plus external acceleration and solar
rectangle. At each fixed E these are linear programs. Scale galaxy rows by
A_i and the solar row by5.2e-27 to keep numerical tolerances meaningful.
First minimize t; then minimize sum w while keeping t within1e-8 of its
optimum. Weights are not rounded before forward validation.

For the external-field cases sample129 E values geometrically spaced over
[2.00e-10/101,2.64e-10]. The interval follows from1<=N<=101 and the observed
g_e box. Then refine the two adjacent intervals of the three best initial
E nodes by midpoint subdivision for four levels, ranking by (t,sum w,E).
Keep all outcomes, including infeasible samples. Report a best sampled
candidate, not a global optimum over continuous E. No interval between
samples is silently excluded. LP feasibility alone is not a proof of exact
arithmetic feasibility; verify primal residuals on every reported solution.

Cache the fixed Newtonian fields at the accepted final forward grids.
Validate spherical/Kuzmin response controls and actual-source superposition
at synthetic weights before fitting. Each final fitted candidate must be
recomputed directly as P[N(|U|)U] and at a refined grid. Demand<=0.005
relative force change at scored radii, plus the preceding boundary gate.
Preserve any failed check and its weights; refine numerics, not data roles.
Only numerically validated candidates may receive an empirical comparison.
Failure to validate is an unresolved calculation, not rejection of physics.

Numerical column errors are not uniform certified bounds over the entire
weight simplex. Consequently an unsuccessful numerical LP or positive
minimum t can constrain this discretization but cannot be advertised as a
rigorous universal no-go. A candidate whose final field passes can be a
conditional existence example. Source-profile, nuisance, external-field,
out-of-fit and relativistic/quantum tests remain independent obligations.

Primary measurement sources and exact earlier contracts remain in
agents/galaxy_response/FROZEN_COMPARISON.md and
agents/galaxy_response/solar_external/FROZEN_NUMERICAL_CONTRACT.md. The field
equation is the supplied [QUMOND model](https://arxiv.org/abs/0911.5464v2).
The external magnitude comes from [Gaia EDR3](https://arxiv.org/abs/2012.02036);
the anomalous quadrupole summary comes from
[Park et al.](https://arxiv.org/abs/2602.17884v2).
