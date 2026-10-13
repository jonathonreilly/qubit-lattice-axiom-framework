# Fixed-history transfer to DESI DR2 BAO summaries

This protocol is written before retrieving the DESI DR2 consensus numeric
summary/covariance in this block. Use the official public2025 DR2 release,
pinned to its exact repository commit. This is new campaign input; it is a
published, previously analyzed data set, not a prospectively blind experiment.
The parent knows general published cosmological context; no claim of global
unexposed model development is made. If primary tables/covariance cannot be
verified, preserve the failure and do not substitute guessed values.

Freeze the same six completed thermal/matter/neutrino histories used for the
supernova comparison: split/equal k=.01,1e-5,1e-6. No scalar coupling, potential,
initial datum, gas assumption, H0, Omega_d, source correction, redshift range
or covariance may be fit to BAO. Keep the exposed supernova comparison and
all weak-history numerical limitations. Compute the same supplied flat
Omega_m=.3 reference as a comparison, not a newly selected best fit.

Use every consensus BAO distance-summary row in this release of types
DM/rd, DH/rd, or DV/rd, provided its published redshift is positive and<=4.5.
Do not mix a consensus release with its overlapping tracer-specific estimates.
The entire lowest-redshift bin is the only calibration subset; all other rows
are transfer rows. Apply the published full covariance without diagonalizing
or adding jitter. Any omitted non-distance statistic must be listed.

Assume the same spatially flat transparent physical metric. In units c/HJ0,
DM(z)=integral dz/EJ(z), DH(z)=1/EJ(z), DV(z)=[z DM(z)^2 DH(z)]^(1/3).
The predicted released distance vector is A times this shape, where the one
shared positive amplitude A=c/(HJ0 rd) is calibrated on the lowest-z bin only.
This is a ruler calibration, not a calculation of recombination/drag physics
or a derived sound horizon. The released BAO extraction/template assumptions
remain imported measurement bridges; no raw galaxy correlation fit is done.

For shape f and data d partitioned into L and T, put
G=C_TL C_LL^-1, v=f_T-G f_L,
VA=(f_L^T C_LL^-1 f_L)^-1, Ahat=VA f_L^T C_LL^-1 d_L.
Then predicted d_T=G d_L+v Ahat and
S=C_TT-G C_LT+VA v v^T. Use these correlated conditional residuals and report
the transfer quadratic. Positivity of the fitted amplitude is a check, not a
clipping prescription. Independently verify Qcal+Qtransfer equals the full
one-amplitude profile quadratic, without using the full-fit amplitude to
make predictions. Report residuals and all fitted normalizations. The global
profile identity is only an algebraic control. No model-selection significance
or calibrated p-value is claimed.

Use the same log(HJ/HGR) Hermite interpolation of241 stored history points,
now over the source's required redshift interval. No extrapolation is allowed.
Check the physical clock from original scalar state at all history knots.
Recompute late fluid density directly, use adaptive radial integration split
at every history knot, and compare with independent fixed quadrature and
linear-versus-Hermite interpolation. Freeze relative distance quadrature
tolerance2e-7 and interpolation diagnostic2e-3. These controls concern
interpolation/integration, not unsampled dynamics or finite-k ODE accuracy.
All selected predictions and failures, full arrays, primary bytes, hashes and
calibration/transfer roles must remain reviewable.
