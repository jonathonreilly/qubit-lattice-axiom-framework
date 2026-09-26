# Declared test of formation during immutable context exchange

2026-09-21, before executing the growth cases below. The stationary screens
already show oscillatory correlations. They do not test a growing background.
All existing stationary data and the running side-64 follow-up are preserved.

Use the same seven-state simulator, supplied rates u=-1, E=1, kappa0=0.05,
and independent product initial data with vacancy probability 1/2 and each
occupied label probability 1/12. New records form at every vacant site at
rate epsilon for each of the six labels. Records already present only move
by immutable exchanges.

First calibrate the birth implementation on the complete 2401-state four-site
ring. Use 8192 trajectories per case, epsilon=0.08, times 0 through 5 at 21
equally spaced points, and density/vector correlations at wave numbers pi/2
and pi. Test both the isotropic initial law and the biased product with weights
(5,1,2,3,4,5,6)/26. Independently assemble every exchange and birth transition,
compare with the exact matrix exponential, check the evolving product law,
and check the final vacancy count against its exact binomial distribution.
The predeclared stochastic sanity threshold is a maximum real/imaginary
correlation discrepancy of 5.5 estimated standard errors. This is not a
simultaneous confidence theorem. Every path retains its count and Fourier
reconstruction audits. Seeds: 2026092160 and 2026092161.

If calibration passes, run these three cubic cases, 512 paths each:

| Case | Side L | Microscopic per-label formation epsilon | Seed |
|---|---:|---:|---:|
| growth_scaled_L24 | 24 | 0.04/24 | 2026092162 |
| growth_scaled_L48 | 48 | 0.04/48 | 2026092163 |
| growth_fixed_clock_L48 | 48 | 0.04/24 | 2026092164 |

Keep the 13 wave-vector representatives and six Fourier fields from the
stationary screen, and 65 times from zero to L sqrt(6). On macroscopic time
tau=t/L, the first two cases have the same evolving background
rho(tau)=1-0.5 exp(-6*0.04*tau). The third has twice the macroscopic birth
rate and makes the clock-scaling distinction visible. Its final occupancy
is therefore different; it is not a matched-density comparison.

Before interpreting the data, solve the full six-field linearized
reaction-conservation equation about that exact product background. In the
six occupied-label coordinates its Fourier propagator obeys

`M'=[-i sum_j (2 pi m_j) A_j(rho(tau))-b 11^T] M`, `M(0)=I`,

where b=L epsilon and A_j is the exact stationary current Jacobian with u,E
held fixed. Transform its predicted two-time covariance M C(0) to the six
measured fields. Do not impose the tuned-density two-field wave equation
after the background has left rho=1/2. The continuum propagator is a target
for a long-wavelength comparison, not an exact finite-lattice correlation.

Use 4000 complete-trajectory bootstrap samples and average symmetry-related
modes within each trajectory. Plot density correlations and their
pointwise intervals against the full time-dependent continuum target;
compare axial, face-diagonal and body-diagonal modes. Also report actual
birth counts and the exact final vacancy expectation. Do not select a new
fit window or interpret a fitted stationary speed for this changing state.
The existing no-birth screens are separate controls, with their original
sample sizes and uncertainties preserved.

This experiment tests transient response while formation continues. It
does not show permanent criticality, a selected clock or coupling, a
relativistic field, or a TOE limit.
