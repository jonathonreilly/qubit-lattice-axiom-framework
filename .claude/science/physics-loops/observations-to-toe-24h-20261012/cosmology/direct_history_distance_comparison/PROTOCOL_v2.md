# Completed-history distance comparison — frozen scope

Parent /root authors this block after inspecting the thermal–matter histories.
The purpose is to reconnect the reconstructed classical action to the actual
processed supernova measurements that motivated the earlier expansion test.
The Pantheon+ table, covariance, selection and partition were exposed earlier
in this campaign. This is a model-development comparison, never a new blind
test or a claim of empirical acceptance.

Use the completed original/reference histories, with every supplied parameter
and initial condition unchanged: split and equal branches at k=.01,1e-5,1e-6.
The split1e-5 history is the completed v3 recovery; the other five are preserved
v1 executions reused by identity. The independently reproduced full trajectory
is equal k=.01. The weak split full trajectories have only independently
checked instantaneous readouts; their tighter and independent full reproductions
are incomplete. Preserve this qualification in every distance result.

Use the same 1358 non-calibrator rows with .0233<=zHD<=1.5, the same405
low-redshift rows below .1 for one additive magnitude intercept, and the same
953 exposed transfer rows. Do not change H0, Omega_d0, k, b, scalar initial
data, neutrino masses, source luminosity evolution or covariance to improve
the result. H0=70, Omega_d0=.3 and T0 are the existing supplied calibration.
The supernova intercept is a separate luminosity/distance normalization.

In a spatially flat physical Jordan FLRW metric, assuming photon number
conservation, the model distance shape is

    g_i=5 log10[(1+zHEL_i) integral_0^zHD_i dz/E_J(z)],
    E_J(z)=H_J(z)/H_J(0).

The use of zHEL in the prefactor and zHD in the radial integral follows the
already inspected official processed-data likelihood. Constant source
luminosity after the published light-curve corrections is an explicit bridge;
no stellar or supernova mechanism is derived from the scalar theory.

The stored histories have241 temperature samples. For this exploratory
comparison interpolate log(H_J/H_GR) against N_J with shape-preserving cubic
interpolation and independently compare linear interpolation. Evaluate the
reference fluid density directly from the frozen electron/photon/neutrino
gas and dust functions. On the selected late interval electron pairs are
absent to the implemented precision, so N_J=Ntotal-ln(1+z) and
L=Lf-ln(1+z). Check the latter entropy identity at all integration-control
nodes. Do not extrapolate beyond a history's sampled interval.

Numerically integrate on513 and1025 redshift nodes over[0,1.5], including all
selected redshifts through interpolation of the cumulative integral. Compare
the distance magnitudes between grids, and against direct adaptive quadrature
at nine fixed redshifts .0233,.05,.1,.2,.3,.5,.8,1.0,1.5. Freeze maximum
grid/adaptive difference2e-5mag and PCHIP-versus-linear difference2e-3mag.
These are finite interpolation diagnostics, not a rigorous bound on unsampled
rapid dynamics or the full-history ODE error. Keep failed controls visible.

Reuse the original full covariance and its exact partition. Fit only the low-z
intercept, propagate correlated low-z residuals into the conditional transfer
mean, and include the intercept uncertainty in the Schur-complement covariance.
Independently verify that calibration chi-square plus conditional-transfer
chi-square equals the full one-intercept profile quadratic. Recompute the
old supplied flat Omega_m=.3 reference and compare its previous stored result.
Do not report a fitted k, a model-selection significance, or a calibrated
sampling p-value. Compare fixed shapes and descriptive residuals.

Retain all input hashes, case labels, numerical failures, arrays and predictions.
The theory's potential and history remain candidate assumptions. Agreement
with this exposed sample would not supply its origin, quantum completion,
primordial perturbations, or the missing full-history numerical checks.

## Version2 affected validation correction

The independent checker actually removed the physical clock/conformal factor
from the interpolation input in v1. All219 original assertions passed despite
a .0185mag maximum shape change in split k=.01. The unmodified calculations
agreed with independent quadrature and covariance reconstruction; this was
an assertion coverage failure. Preserve v1 and its actual mutant results.

Version2 adds primitive-state physical-clock checks at all241 stored rows of
each of six histories. Derive B squared from the original metric, differentiate
its scale factor, construct HJ2 from Hhat2 and that clock, and compare directly
with the actual log-ratio interpolation input and present normalization.
The relative threshold is3e-12, with no floor set by tiny H or coupling. These
are instantaneous readout controls; they are not an ODE convergence certificate.
No history, quadrature, observation, fitted quantity, or score changes. Check
all scientific outputs and old non-source assertions for exact identity.
Rerun the same concrete omission with freshly bound inputs on v2.
