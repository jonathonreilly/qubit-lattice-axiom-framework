# What matched torque shapes can test without absolute calibration

The observed 95-run torque table motivates this conditional screening test.
It does not supply missing calibration or geometry. The frozen plan classifies
all table rows and the published fit summaries as exposed development data.
This is elementary positive-Laplace-transform support, not a novel theory.

## Conditional shape statement

In the normalized finite-wedge calculation of
`LEE2020_CALIBRATION_DERIVATION_v1.md`, suppose the radial/angular patterns are
congruent up to positive density scales. Thicknesses may differ. For a chosen
nonzero common harmonic, select its fixed sign so its aligned amplitude is
positive. The radial Bessel factor then occurs as a square. All remaining
weights in the Newtonian or attractive Yukawa term are nonnegative. Therefore

`T(d) = integral_[0,infinity) exp(-q d) dnu(q)`, `dnu >= 0`, `d>0`.      (1)

A positive sum of such exchanges preserves (1). This does not assume the full
unknown potential has been reconstructed. The homogeneous linear field class,
matched patterns, positive coupling and common orientation are premises. A
negative harmonic of an unmatched geometry is not evidence for a negative
scalar kinetic term. Changing body positions or receiver transfer between runs
can also invalidate this single-curve contract.

When the integrals converge with the needed moments, differentiating (1) gives

`(-1)^p T^(p)(d) = integral q^p exp(-q d) dnu(q) >= 0`.                (2)

In particular T is nonnegative, decreasing and convex. Cauchy-Schwarz gives

`T T'' - (T')^2 = (1/2) integral integral (q-q')^2`
`                       *exp[-d(q+q')] dnu(q) dnu(q') >= 0`.           (3)

Thus nonzero T is log convex. At equal separation steps h>0,

`(-1)^p Delta_h^p T(d) = integral exp(-q d)(1-exp(-q h))^p dnu(q)>=0`,  (4)
`T(d+h)^2 <= T(d) T(d+2h)`.                                         (5)

An unknown common positive gain multiplies the measure. A common separation
offset replaces it by `exp(-q delta) dnu(q)` wherever the shifted integrals
exist. These operations preserve every displayed inequality. Consequently these
particular shape tests do not require absolute G, absolute torque gain or a
chosen common separation zero. They still require correct relative separations,
common calibration transfer, geometry and valid error bounds.

## Pattern mismatch does not disappear

For real radial transforms `R_A=R+e_A`, `R_B=R+e_B`, let `w_{p,d}(k)>=0` be the
positive geometric/exchange weight after p signed derivatives. The mismatch
relative to the matched reference obeys

`|integral w (R_A R_B-R^2)|`
` <= ||R||_w (||e_A||_w+||e_B||_w)+||e_A||_w ||e_B||_w`.              (6)

This follows by expansion and three Cauchy-Schwarz inequalities. Apply it
separately for each p and d; one error norm does not automatically certify all
derivatives. Noncongruent profiles can have signed cross-spectral weights even
when each underlying material density is positive. The actual measured foil
dimensions, edge roughness and varying centering therefore need an explicit
error propagation. A quoted standard error is not a deterministic certificate
for (6). This block does not replace those errors by zero.

## Deliberately weaker data diagnostics

For printed central separations, assign one latent t_i per distinct separation
and require each run j in that group to obey

`|t_i - N_j| <= k sigma_j`, `k>=0`.

The first linear program adds `t_i>=0` and decreasing order. The second also
requires successive secant slopes to be increasing. Minimizing k measures the
smallest *box expansion* consistent with these necessary shape conditions; it
is not a likelihood, confidence level or measurement of a physical parameter.
Convex feasibility is weaker than complete monotonicity or membership in the
actual finite-body field model.

A separate monotone relaxation keeps a latent torque per run and imposes an
order only when their `[s-sigma_s,s+sigma_s]` separation intervals do not overlap.
This ignores constraints between overlapping intervals and every convexity
constraint. Its feasible result therefore does not prove existence of one
physical separation assignment or one fully compatible curve. Its optimum is
a lower bound on the necessary torque-box multiplier under the stronger
contract. Separation intervals themselves are hypothetical deterministic boxes,
not an asserted coverage level for the experiment.

Both computations retain all rows and signs. Common phase fitting, calibration,
systematics subtraction and unknown correlations in the published products
remain part of their provenance. No scalar action is fitted. An infeasible
small-error envelope would diagnose a failure of the combined class, geometry,
transfer and error contract, not identify which premise failed. A feasible
envelope cannot validate a scalar theory, derive the action class or establish
the original experiment's exclusion likelihood.
