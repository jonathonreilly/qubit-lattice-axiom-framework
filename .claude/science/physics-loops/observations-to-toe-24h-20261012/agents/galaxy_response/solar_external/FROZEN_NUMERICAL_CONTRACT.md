# QUMOND Solar quadrupole numerical contract

This freezes inputs and comparison roles after the independent `INITIAL_DERIVATION.md` freeze at 2026-10-12T18:32:17Z, and before this agent's first quadrupole evaluation. The parent's independent numerical results remain unread. Public Cassini estimates and the illustrative Park et al. (2026) quadrupole values have been seen: this is an unfitted model-development comparison, not a blind test.

## Supplied physical model and fixed inputs

- New completion: `laplacian Phi = div[nu(|grad Phi_N|/a0) grad Phi_N]`, `laplacian Phi_N=4 pi G rho`. Fix `nu(y)=1/[1-exp(-sqrt(y))]`; no shape change or Solar fit.
- Point Sun plus a constant Newtonian background directed toward the Galactic center; regular quadrupolar correction from the QUMOND Poisson solution, with no independently added harmonic tidal term. The ordinary Galactic tide is not identified with this anomalous quadrupole.
- Primary `a0=7.658058668049826e-11 m/s^2`, the already frozen free-global-M/L galaxy calibration. Fixed-M/L control: `8.533673475349299e-11`. Development envelope `[7.65,8.70]e-11` covers the reported alternative galaxy calibrations; it is not a statistical interval and does not include full distance, inclination, stellar-population or field-completion uncertainty.
- Adopt `GM_sun=1.32712440018e20 m^3/s^2`, AU `149597870700 m`, parsec `AU*648000/pi`. These are fixed numerical scale choices, not fitted parameters.
- Gaia EDR3 acceleration magnitude: `(2.32 +/- 0.16)e-10 m/s^2`, where the uncertainty is a bootstrap 1-sigma estimate (Klioner et al., arXiv:2012.02036v1, Table 2). Use central value and rectangular interval `[2.00,2.64]e-10`, formed as central +/- twice that uncertainty. This is not a joint 95% confidence region. Gaia measures acceleration relative to remote quasars; identifying it with a constant local Galactic external field is a premise. Other acceleration contributions are not separately fitted.
- Fix the field direction to the Galactic center, matching the Cassini quadrupole template. Gaia's fitted direction and its covariance are recorded as exposure, not marginalized. A scalar-magnitude box does not cover all orientation uncertainty.

## Physical-to-Newtonian conversion variants

Let `eta=g_Ne/a0`, `g_e` be the observed physical background magnitude. Solve uniquely for positive eta:

1. Spherical-parent approximation: `g_e/a0 = eta nu(eta)`.
2. Disk-surface-density approximation: `g_e/a0 = eta nu(sqrt(eta^2+s_b^2))`, `s_b=2 pi G Sigma_b/a0`. This is Park et al. arXiv:2602.17884v2 Eq. (12), explicitly an approximation for a flattened parent galaxy, not an exact QUMOND boundary identity. Adopt `Sigma_b=47 M_sun/pc^2` and a development range `[41,53]` from twice the `3 M_sun/pc^2` uncertainty adopted in that paper. Its underlying reference is Bland-Hawthorn & Gerhard (2016), a synthesis, not a new surface-density measurement here. Conversion use of Sigma is a declared nuisance prescription; no posterior is imported.

The galaxy acceleration calibration used an algebraic circular rule. It did not solve the QUMOND disk PDE. Its transfer to this Solar PDE completion is provisional. Neither conversion supplies the missing global Milky Way QUMOND solution, and neither tests arbitrary choices of the Newtonian external field.

## Numerical definitions and controls

Use `F(eta)=Q2*rM/a0`, `rM=sqrt(GM_sun/a0)`, potential correction `delta Phi=-(Q2/2)(z^2-r^2/3)`. Hence `Hzz*rM/a0=-2F/3`. Evaluate both frozen forms independently: phantom-density/nu-prime and integration-by-parts/nu-minus-one. In each, use `w=1/x`, `c=1-u^2`, `0<=u<=sqrt(2)`; the saddle is at `w=sqrt(eta),u=0`. Split radial integration at that saddle and resolve it without clipping the integrand. The integration-by-parts angular polynomial has zero angular mean, permitting an angular-constant subtraction for stability.

First diagnostic grid: `eta=[0,0.5,1,1.5,2,3,5,10]`; Gauss-Legendre orders 64,128,256 per interval/dimension, radial cutoff40 and cutoff60 for the highest-order check. Increase resolution if the two forms or successive refinements disagree by more than `2e-6` relative (absolute `2e-9` near zero); preserve failed checks. Spherical/nu=1 controls vanish exactly. Record cutoff tail bound, convergence differences, versions and file hashes. No parent's expected constants are imported.

For eta<=10 and W>=sqrt(2 eta), the absolute IBP tail beyond W is bounded by

`9 exp(eta/W-W) [W^2+2W+2+eta] / [1-exp(-sqrt(W^2-eta))]`.

This follows from `sqrt(v)>=sqrt(w^2-eta)>=w-eta/W`, `nu(v)-1 <= exp(-sqrt(v))/(1-exp(-sqrt(W^2-eta)))`, and the absolute polynomial bound `|B|<=2w^2+2eta`. It bounds the exact angular integral even when the implemented integrand uses the zero-mean subtraction.

After first numerical results are frozen, compare with the parent's independent Hessian result. Evaluate central physical conversions and all endpoint combinations of the a0, g_e and Sigma boxes, plus a declared interior grid (9 a0 values,17 g_e values,5 Sigma values for the disk approximation). Report a sampled numerical envelope unless global extrema are separately established. Parameter-box edges and monotonicity checks must not be represented as a confidence interval.

## Unfitted observational comparison

Primary target: Park et al. arXiv:2602.17884v2, Table I, all-data `Q2=(1.6 +/- 1.8)e-27 s^-2`, explicitly 1 sigma. Compare with the summary rectangle `[-2.0,5.2]e-27`; no raw-data refit, multidimensional likelihood or significance is constructed. Historical target: Hees et al. arXiv:1402.6950v2, `Q2=(3 +/- 3)e-27 s^-2`, with rectangle `[-3,9]e-27`. These overlapping Cassini measurements are not combined as independent data. The observable is an anomalous dynamical quadrupole, not the 2003 Shapiro fitted gamma.

Numerical reproduction of Park's exposed illustrative input `a0=1.02e-10`, `g_e=2.32e-10`, Sigma=47 may be used only after our own first result freeze as a normalization control, not to set precision or choose physical parameters. Quoted paper values are `3.387e-26` (spherical) and `3.411e-26` (disk approximation).
