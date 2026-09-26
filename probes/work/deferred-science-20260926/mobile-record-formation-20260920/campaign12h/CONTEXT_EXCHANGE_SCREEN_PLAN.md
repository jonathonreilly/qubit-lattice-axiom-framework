# Declared context-exchange correlation screen

Declared before cubic simulations, 2026-09-21. The independent source check
of the proposed generator is in progress. No microscopic wave result is yet
established. All runs retain raw per-path Fourier amplitudes and seeds.

First calibrate the exact simulator against complete 2401-state four-ring
generators at 8192 paths each: flat symmetric exchange, the proposed context
rule at isotropic density one half, and a biased seven-category product law.
Compare density/vx auto and cross correlations at 21 times and two modes.
The predeclared maximum estimated-standard-error gate is 5.5; this is a
stochastic calibration sanity test rather than a rigorous confidence bound.
Do not begin cubic interpretation if it fails without resolving the cause.

Then use cubic sides 16, 24 and 32, 256 trajectories each, initially independent
with vacancy probability one half and each occupied label probability 1/12.
The conservative dynamics has u=-1, E=1 and exchange rate
`c=1/20+max(h,0)`. There are no births in this first stationary screen.
The generator's exact stationary current Jacobian predicts acoustic speed
1/sqrt(6); the microscopic dynamic correlation need not obey that prediction.

Measure 65 equally spaced times through one predicted axial period
`t_max=L sqrt(6)`, retaining density, vector content and two quadrupoles.
Use all three axial fundamental modes, six face-diagonal conjugacy classes
and four body-diagonal conjugacy classes. Preserve their actual wavevectors.
Average symmetry-related modes within each trajectory before uncertainty
estimation; resample complete independent trajectories, not separate times or
modes as though independent. Distinguish pointwise intervals from simultaneous
or fitted-parameter uncertainty.

Controls at side 16, also 256 trajectories: (a) context rates with constant
symmetric part `c=4+h/2`; (b) flat symmetric exchange `c=1/20`.
The flat model has exactly diffusive density autocorrelation with lattice
eigenvalue `2c sum_i(1-cos k_i)`. The context models share stationary currents
but need not share damping. These controls are not attempts to tune to data.

Primary quantities are the density autocorrelation and the complex
autocorrelations of normalized density plus/minus longitudinal-content modes.
Inspect negative density correlation near the predicted first minimum, phase
advance versus |k|, and consistency across directions and volumes. Any damped
cosine or phase/damping fit is explicitly phenomenological, with whole-path
bootstrap uncertainty. A resolved finite-system oscillation is not a proof of
a hydrodynamic limit, an isotropic continuum, a universal light speed or a TOE.

If these results justify continuation, separately declare a growth experiment
with ongoing uniform formation, or a larger-volume/more-trajectory follow-up.
Do not silently replace the fixed-density question with a changing-density one.
